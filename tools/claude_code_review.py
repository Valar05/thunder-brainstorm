#!/usr/bin/env python3
"""Claude-backed GitHub PR review driver with read-only repo tools."""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import http.client
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = os.environ.get("THUNDER_CLAUDE_REVIEW_MODEL", os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6"))
TEXT_EXTS = {
    ".gd", ".py", ".js", ".ts", ".tsx", ".jsx", ".vue", ".cs", ".cpp", ".c", ".h", ".hpp",
    ".java", ".kt", ".swift", ".rs", ".go", ".rb", ".php", ".html", ".css", ".scss", ".md",
    ".json", ".yaml", ".yml", ".toml", ".ini", ".godot", ".sh", ".mjs", ".cjs",
}
MAX_TOOL_BYTES = 60_000
MAX_PR_FILE_PATCH_BYTES = 8_000
MAX_PR_DIFF_BYTES = 50_000
SECRET_RE = re.compile(r"(?i)(api[_-]?key|token|secret|password|authorization)(\s*[:=]\s*)([^\s'\"`]+)")


class ReviewError(RuntimeError):
    pass


@dataclass
class ReviewTarget:
    owner: str
    repo: str
    number: int

    @property
    def full_repo(self) -> str:
        return f"{self.owner}/{self.repo}"

    @property
    def slug(self) -> str:
        return f"{self.owner}_{self.repo}_pr_{self.number}".replace("/", "_")


@dataclass
class ReadState:
    metadata: dict[str, Any] = field(default_factory=dict)
    files: list[dict[str, Any]] = field(default_factory=list)
    diff: str = ""
    checks: dict[str, Any] = field(default_factory=dict)
    read_files: set[str] = field(default_factory=set)
    tool_names: list[str] = field(default_factory=list)


def parse_pr_target(raw: str) -> ReviewTarget:
    raw = raw.strip()
    url_match = re.match(r"https://github\.com/([^/]+)/([^/]+)/pull/(\d+)", raw)
    if url_match:
        return ReviewTarget(url_match.group(1), url_match.group(2), int(url_match.group(3)))
    match = re.match(r"([^\s/#]+)/([^\s#]+)#(\d+)$", raw)
    if match:
        return ReviewTarget(match.group(1), match.group(2), int(match.group(3)))
    raise ReviewError("PR target must be OWNER/REPO#NUMBER or a GitHub pull request URL")


def redact(text: str) -> str:
    return SECRET_RE.sub(r"\1\2[REDACTED]", text)


def clamp_text(text: str, limit: int = MAX_TOOL_BYTES) -> tuple[str, bool]:
    text = redact(text)
    encoded = text.encode("utf-8", errors="replace")
    if len(encoded) <= limit:
        return text, False
    truncated = encoded[:limit].decode("utf-8", errors="ignore")
    return truncated + "\n[TRUNCATED]", True


def run_command(args: list[str], *, cwd: Path | None = None, text: bool = True) -> str:
    try:
        return subprocess.check_output(args, cwd=str(cwd) if cwd else None, stderr=subprocess.PIPE, text=text)
    except FileNotFoundError as exc:
        raise ReviewError(f"required command not found: {args[0]}") from exc
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr if isinstance(exc.stderr, str) else str(exc.stderr)
        raise ReviewError(f"command failed: {' '.join(args)}\n{detail.strip()}") from exc


def gh_json(path: str) -> Any:
    return json.loads(run_command(["gh", "api", path]))


def gh_text(args: list[str]) -> str:
    return run_command(["gh", "api", *args])


class GitHubReader:
    def __init__(self, target: ReviewTarget, mock_dir: Path | None = None) -> None:
        self.target = target
        self.mock_dir = mock_dir

    def _mock_json(self, name: str) -> Any:
        assert self.mock_dir is not None
        return json.loads((self.mock_dir / name).read_text(encoding="utf-8"))

    def get_pr_metadata(self) -> dict[str, Any]:
        if self.mock_dir:
            data = self._mock_json("pr_metadata.json")
        else:
            data = gh_json(f"repos/{self.target.owner}/{self.target.repo}/pulls/{self.target.number}")
        return {
            "number": data.get("number"),
            "title": data.get("title"),
            "state": data.get("state"),
            "html_url": data.get("html_url"),
            "base": {"ref": data.get("base", {}).get("ref"), "sha": data.get("base", {}).get("sha")},
            "head": {"ref": data.get("head", {}).get("ref"), "sha": data.get("head", {}).get("sha")},
            "user": (data.get("user") or {}).get("login"),
        }

    def list_pr_files(self) -> list[dict[str, Any]]:
        if self.mock_dir:
            data = self._mock_json("pr_files.json")
        else:
            data = gh_json(f"repos/{self.target.owner}/{self.target.repo}/pulls/{self.target.number}/files?per_page=100")
        files = []
        for item in data:
            patch, truncated = clamp_text(item.get("patch", ""), MAX_PR_FILE_PATCH_BYTES)
            files.append({
                "filename": item.get("filename"),
                "status": item.get("status"),
                "additions": item.get("additions"),
                "deletions": item.get("deletions"),
                "changes": item.get("changes"),
                "patch": patch,
                "patch_truncated": truncated,
            })
        return files

    def get_pr_diff(self) -> str:
        if self.mock_dir:
            return (self.mock_dir / "pr.diff").read_text(encoding="utf-8")
        return gh_text([f"repos/{self.target.owner}/{self.target.repo}/pulls/{self.target.number}", "-H", "Accept: application/vnd.github.v3.diff"])

    def read_file_at_ref(self, path: str, ref: str) -> dict[str, Any]:
        safe = Path(path)
        if safe.is_absolute() or ".." in safe.parts:
            raise ReviewError("path must be a repository-relative file path")
        if safe.suffix.lower() and safe.suffix.lower() not in TEXT_EXTS:
            raise ReviewError(f"refusing likely-binary file extension: {safe.suffix}")
        if self.mock_dir:
            file_path = self.mock_dir / "files" / path
            if not file_path.exists():
                raise ReviewError(f"mock file not found: {path}")
            text = file_path.read_text(encoding="utf-8", errors="ignore")
        else:
            encoded_path = urllib.parse.quote(path, safe="/")
            data = gh_json(f"repos/{self.target.owner}/{self.target.repo}/contents/{encoded_path}?ref={urllib.parse.quote(ref, safe='')}")
            if data.get("encoding") != "base64" or not data.get("content"):
                raise ReviewError(f"GitHub did not return base64 text content for {path}")
            raw = base64.b64decode(data["content"])
            text = raw.decode("utf-8", errors="ignore")
        body, truncated = clamp_text(text)
        return {"path": path, "ref": ref, "truncated": truncated, "content": body}

    def search_repo_at_ref(self, query: str, limit: int = 10) -> dict[str, Any]:
        query = query.strip()
        if not query or len(query) < 2:
            raise ReviewError("query must be at least two characters")
        limit = max(1, min(limit, 25))
        if self.mock_dir:
            results: list[dict[str, Any]] = []
            files_dir = self.mock_dir / "files"
            if files_dir.exists():
                for path in files_dir.rglob("*"):
                    if len(results) >= limit or not path.is_file():
                        break
                    rel = str(path.relative_to(files_dir))
                    text = path.read_text(encoding="utf-8", errors="ignore")
                    for idx, line in enumerate(text.splitlines(), start=1):
                        if query.lower() in line.lower():
                            results.append({"path": rel, "line": idx, "text": clamp_text(line, 240)[0]})
                            break
            return {"query": query, "results": results}
        search_query = urllib.parse.quote(f"{query} repo:{self.target.owner}/{self.target.repo}")
        data = gh_json(f"search/code?q={search_query}&per_page={limit}")
        return {
            "query": query,
            "note": "GitHub code search is repo-scoped; read candidate files at the PR head ref before relying on them.",
            "results": [
                {"path": item.get("path"), "url": item.get("html_url"), "repository": item.get("repository", {}).get("full_name")}
                for item in data.get("items", [])[:limit]
            ],
        }

    def list_ci_checks(self, sha: str) -> dict[str, Any]:
        if self.mock_dir:
            path = self.mock_dir / "ci_checks.json"
            return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"check_runs": []}
        try:
            runs = gh_json(f"repos/{self.target.owner}/{self.target.repo}/commits/{sha}/check-runs")
        except ReviewError as exc:
            return {"error": str(exc), "check_runs": []}
        return {
            "total_count": runs.get("total_count"),
            "check_runs": [
                {
                    "name": item.get("name"),
                    "status": item.get("status"),
                    "conclusion": item.get("conclusion"),
                    "html_url": item.get("html_url"),
                }
                for item in runs.get("check_runs", [])
            ],
        }


def changed_line_map(diff: str) -> set[tuple[str, int, str]]:
    changed: set[tuple[str, int, str]] = set()
    path = ""
    old_line = 0
    new_line = 0
    for raw in diff.splitlines():
        if raw.startswith("diff --git "):
            path = ""
        elif raw.startswith("+++ b/"):
            path = raw[6:]
        elif raw.startswith("@@"):
            match = re.search(r"@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@", raw)
            if match:
                old_line = int(match.group(1))
                new_line = int(match.group(2))
        elif path and raw.startswith("+") and not raw.startswith("+++"):
            changed.add((path, new_line, "RIGHT"))
            new_line += 1
        elif path and raw.startswith("-") and not raw.startswith("---"):
            changed.add((path, old_line, "LEFT"))
            old_line += 1
        elif path and raw.startswith(" "):
            old_line += 1
            new_line += 1
    return changed


def review_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "properties": {
            "summary": {"type": "string"},
            "perspectives_used": {"type": "array", "items": {"type": "string"}},
            "findings": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "severity": {"type": "string", "enum": ["critical", "high", "medium", "low"]},
                        "path": {"type": "string"},
                        "line": {"type": "integer"},
                        "side": {"type": "string", "enum": ["RIGHT", "LEFT"]},
                        "issue": {"type": "string"},
                        "impact": {"type": "string"},
                        "evidence": {"type": "string"},
                        "recommendation": {"type": "string"},
                        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
                    },
                    "required": ["severity", "path", "line", "side", "issue", "impact", "evidence", "recommendation", "confidence"],
                },
            },
            "test_gaps": {"type": "array", "items": {"type": "string"}},
            "non_postable_concerns": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["summary", "perspectives_used", "findings", "test_gaps", "non_postable_concerns"],
    }


def tool_definitions() -> list[dict[str, Any]]:
    return [
        {"name": "get_pr_metadata", "description": "Read GitHub PR metadata including base/head refs and commits.", "input_schema": {"type": "object", "properties": {}, "additionalProperties": False}},
        {"name": "list_pr_files", "description": "List changed files and per-file patch snippets for the PR.", "input_schema": {"type": "object", "properties": {}, "additionalProperties": False}},
        {"name": "get_pr_diff", "description": "Read the full unified diff for the PR.", "input_schema": {"type": "object", "properties": {}, "additionalProperties": False}},
        {"name": "read_file_at_ref", "description": "Read one text file from the repository at a specific ref or SHA. Use PR head SHA for changed code and base SHA for comparison.", "input_schema": {"type": "object", "properties": {"path": {"type": "string"}, "ref": {"type": "string"}}, "required": ["path", "ref"], "additionalProperties": False}},
        {"name": "search_repo_at_ref", "description": "Search the repository for a symbol or phrase and return candidate paths. Read candidate files before relying on them.", "input_schema": {"type": "object", "properties": {"query": {"type": "string"}, "limit": {"type": "integer", "minimum": 1, "maximum": 25}}, "required": ["query"], "additionalProperties": False}},
        {"name": "list_ci_checks", "description": "List GitHub check runs for a commit SHA.", "input_schema": {"type": "object", "properties": {"sha": {"type": "string"}}, "required": ["sha"], "additionalProperties": False}},
        {"name": "finalize_review", "description": "Submit the final strict JSON code review after inspecting the PR through tools. Do not call until get_pr_metadata, list_pr_files, and get_pr_diff have been used.", "input_schema": review_schema()},
    ]


def env_value(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if value:
        return value
    for path in (Path.home() / ".secrets" / "anthropic.env", Path.home() / ".bashrc", Path.home() / ".profile"):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        match = re.search(rf"^\s*(?:export\s+)?{re.escape(name)}=([\'\"]?)(.*?)\1\s*$", text, re.MULTILINE)
        if match:
            return match.group(2).strip()
    return ""


def call_anthropic(*, model: str, system: str, tools: list[dict[str, Any]], messages: list[dict[str, Any]], max_tokens: int) -> dict[str, Any]:
    api_key = env_value("ANTHROPIC_API_KEY")
    if not api_key:
        raise ReviewError("ANTHROPIC_API_KEY is not set")
    body = {"model": model, "max_tokens": max_tokens, "system": system, "tools": tools, "messages": messages}
    if not re.match(r"^claude-[a-z]+-5(?:$|-)", model):
        body["temperature"] = 0.1
    request = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "thunder-brainstorm-claude-pr-review/1.0",
        },
        method="POST",
    )
    attempts = int(os.environ.get("THUNDER_CLAUDE_API_ATTEMPTS", "2"))
    timeout = int(os.environ.get("THUNDER_CLAUDE_API_TIMEOUT", "180"))
    errors: list[str] = []
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise ReviewError(f"Anthropic API error {exc.code}: {detail}") from exc
        except (urllib.error.URLError, TimeoutError, ConnectionResetError, BrokenPipeError, json.JSONDecodeError, http.client.RemoteDisconnected, http.client.HTTPException) as exc:
            errors.append(f"attempt {attempt}: {exc}")
            if attempt < attempts:
                time.sleep(min(2 ** attempt, 6))
    raise ReviewError("Anthropic API connection failed:\n" + "\n".join(errors))


def build_system_prompt() -> str:
    return """You are Claude acting as an independent code-review critic.

Repository truth comes from tools only. You must inspect the PR with tools before finalizing. Do not ask for pasted source context. If tool access is insufficient, use finalize_review with no findings and explain the capability failure in non_postable_concerns.

Perspective-Guided Command rules:
- Quartermaster owns final synthesis: repository truth, evidence, verification, continuity, preservation.
- Perspectives are responsibilities, not personalities or roleplay.
- Select only lenses that materially improve judgment; never rotate through a fixed council.
- Foreman notices implementation, sequencing, and verification risks.
- Gasket/Auditor notices contradiction, failure modes, unsafe claims, and missing evidence.

Review priorities:
- correctness bugs, regressions, lifecycle/state/API/schema/migration breaks
- security, privacy, data loss, permissions, secrets
- missing tests for changed behavior
- performance, accessibility, UX, maintainability only when materially relevant

Rules:
- Prefer fewer high-confidence findings.
- Findings must be actionable and grounded in tool-read repo evidence.
- Put speculative or unmappable concerns in non_postable_concerns, not findings.
- Every finding must target a changed diff line when possible.
- Call finalize_review with the strict JSON review object when done."""


def build_mission(target: ReviewTarget) -> str:
    return f"""Review GitHub PR {target.full_repo}#{target.number}.

Required first steps:
1. Call get_pr_metadata.
2. Call list_pr_files.
3. Call get_pr_diff.
4. Read touched files and relevant call sites/tests/docs with read_file_at_ref and search_repo_at_ref.
5. Use list_ci_checks for the PR head SHA when available.
6. Call finalize_review with strict JSON.

Do not produce prose as the final review. Use finalize_review."""


def dispatch_tool(name: str, tool_input: dict[str, Any], reader: GitHubReader, state: ReadState) -> Any:
    state.tool_names.append(name)
    if name == "get_pr_metadata":
        state.metadata = reader.get_pr_metadata()
        return state.metadata
    if name == "list_pr_files":
        state.files = reader.list_pr_files()
        return {"files": state.files}
    if name == "get_pr_diff":
        state.diff = reader.get_pr_diff()
        body, truncated = clamp_text(state.diff, MAX_PR_DIFF_BYTES)
        return {"diff": body, "truncated": truncated}
    if name == "read_file_at_ref":
        path = str(tool_input.get("path", ""))
        ref = str(tool_input.get("ref", ""))
        if path in state.read_files:
            return {"path": path, "ref": ref, "already_read": True, "note": "This file was already returned earlier in the review; use the prior tool result instead of rereading it."}
        result = reader.read_file_at_ref(path, ref)
        state.read_files.add(path)
        return result
    if name == "search_repo_at_ref":
        return reader.search_repo_at_ref(str(tool_input.get("query", "")), int(tool_input.get("limit", 10)))
    if name == "list_ci_checks":
        state.checks = reader.list_ci_checks(str(tool_input.get("sha", "")))
        return state.checks
    raise ReviewError(f"blocked or unknown tool requested: {name}")


def run_claude_review(target: ReviewTarget, reader: GitHubReader, *, model: str, max_tool_turns: int, max_tokens: int, transcript_path: Path) -> tuple[dict[str, Any], ReadState, list[dict[str, Any]]]:
    messages: list[dict[str, Any]] = [{"role": "user", "content": build_mission(target)}]
    tools = tool_definitions()
    state = ReadState()
    transcript: list[dict[str, Any]] = []
    final_review: dict[str, Any] | None = None
    system = build_system_prompt()

    for turn in range(1, max_tool_turns + 1):
        if turn == max_tool_turns:
            messages.append({"role": "user", "content": "This is the final allowed tool turn. Do not call additional repo-reading tools. Call finalize_review now with the best evidence already gathered."})
        payload = call_anthropic(model=model, system=system, tools=tools, messages=messages, max_tokens=max_tokens)
        transcript.append({"turn": turn, "type": "assistant", "payload": payload})
        messages.append({"role": "assistant", "content": payload.get("content", [])})
        tool_blocks = [block for block in payload.get("content", []) if block.get("type") == "tool_use"]
        if not tool_blocks:
            text = "\n".join(block.get("text", "") for block in payload.get("content", []) if block.get("type") == "text")
            if final_review is not None:
                break
            raise ReviewError("Claude ended without calling finalize_review. Text was: " + text[:500])

        results = []
        for block in tool_blocks:
            tool_name = block.get("name", "")
            tool_id = block.get("id", "")
            tool_input = block.get("input") or {}
            if tool_name == "finalize_review":
                final_review = tool_input
                result_content = {"accepted": True, "note": "final review captured by Thunder"}
            else:
                try:
                    result_content = dispatch_tool(tool_name, tool_input, reader, state)
                except Exception as exc:  # keep tool errors inside tool_result blocks
                    results.append({"type": "tool_result", "tool_use_id": tool_id, "is_error": True, "content": json.dumps({"error": str(exc)}, ensure_ascii=False)})
                    continue
            results.append({"type": "tool_result", "tool_use_id": tool_id, "content": json.dumps(result_content, ensure_ascii=False)})
        transcript.append({"turn": turn, "type": "tool_result", "payload": results})
        with transcript_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(transcript[-2], ensure_ascii=False) + "\n")
            handle.write(json.dumps(transcript[-1], ensure_ascii=False) + "\n")
        if final_review is not None:
            break
        messages.append({"role": "user", "content": results})

    if final_review is None:
        raise ReviewError("Claude did not finalize review within max tool turns")
    required = {"get_pr_metadata", "list_pr_files", "get_pr_diff"}
    missing = sorted(required - set(state.tool_names))
    if missing:
        raise ReviewError("Claude finalized before required repo reads: " + ", ".join(missing))
    return final_review, state, transcript


def validate_review_shape(review: dict[str, Any]) -> None:
    for key in review_schema()["required"]:
        if key not in review:
            raise ReviewError(f"review JSON missing required key: {key}")
    if not isinstance(review.get("findings"), list):
        raise ReviewError("review findings must be a list")
    for idx, finding in enumerate(review.get("findings", [])):
        for key in ("severity", "path", "line", "side", "issue", "impact", "evidence", "recommendation", "confidence"):
            if key not in finding:
                raise ReviewError(f"finding {idx} missing {key}")
        if finding["severity"] not in {"critical", "high", "medium", "low"}:
            raise ReviewError(f"finding {idx} has invalid severity")
        if finding["side"] not in {"RIGHT", "LEFT"}:
            raise ReviewError(f"finding {idx} has invalid side")
        if not isinstance(finding["line"], int):
            raise ReviewError(f"finding {idx} line must be an integer")


def verify_findings(review: dict[str, Any], state: ReadState) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    validate_review_shape(review)
    changed = changed_line_map(state.diff)
    pr_paths = {item.get("filename") for item in state.files}
    verified: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    for finding in review.get("findings", []):
        path = finding.get("path")
        line = int(finding.get("line"))
        side = finding.get("side", "RIGHT")
        reasons = []
        if path not in pr_paths:
            reasons.append("path is not in changed PR files")
        if (path, line, side) not in changed:
            reasons.append("line/side does not map to a changed diff line")
        if finding.get("confidence") == "low":
            reasons.append("low confidence findings are report-only")
        if reasons:
            rejected.append({"finding": finding, "reasons": reasons})
        else:
            verified.append(finding)
    return verified, rejected


def build_github_payload(target: ReviewTarget, state: ReadState, verified: list[dict[str, Any]], report_url: str = "") -> dict[str, Any]:
    head_sha = state.metadata.get("head", {}).get("sha") or ""
    body = f"Claude independent review for {target.full_repo}#{target.number}. Verified inline findings: {len(verified)}."
    if report_url:
        body += f"\n\nFull report: {report_url}"
    return {
        "commit_id": head_sha,
        "event": "COMMENT",
        "body": body,
        "comments": [
            {
                "path": item["path"],
                "line": item["line"],
                "side": item["side"],
                "body": format_inline_comment(item),
            }
            for item in verified
        ],
    }


def format_inline_comment(finding: dict[str, Any]) -> str:
    return "\n".join([
        f"**{finding['severity'].upper()}**: {finding['issue']}",
        "",
        f"Impact: {finding['impact']}",
        f"Evidence: {finding['evidence']}",
        f"Recommendation: {finding['recommendation']}",
    ])


def write_report(path: Path, target: ReviewTarget, review: dict[str, Any], verified: list[dict[str, Any]], rejected: list[dict[str, Any]], state: ReadState) -> None:
    lines = [
        f"# Claude PR Review: {target.full_repo}#{target.number}",
        "",
        f"Summary: {review.get('summary', '')}",
        "",
        f"Perspectives used: {', '.join(review.get('perspectives_used', []))}",
        f"Verified inline findings: {len(verified)}",
        f"Report-only or rejected findings: {len(rejected)}",
        "",
        "## Verified Findings",
        "",
    ]
    if not verified:
        lines.append("No verified inline findings.")
    for item in verified:
        lines.extend([f"- {item['severity']} `{item['path']}:{item['line']}` {item['issue']}", f"  Recommendation: {item['recommendation']}"])
    lines.extend(["", "## Report-Only Findings", ""])
    if not rejected:
        lines.append("No rejected findings.")
    for item in rejected:
        finding = item["finding"]
        lines.extend([f"- `{finding.get('path')}:{finding.get('line')}` {finding.get('issue')}", f"  Reasons: {', '.join(item['reasons'])}"])
    lines.extend(["", "## Test Gaps", ""])
    for gap in review.get("test_gaps", []):
        lines.append(f"- {gap}")
    lines.extend(["", "## Non-Postable Concerns", ""])
    for concern in review.get("non_postable_concerns", []):
        lines.append(f"- {concern}")
    lines.extend(["", "## Read Log", "", f"- Tools used: {', '.join(state.tool_names)}", f"- Files read: {', '.join(sorted(state.read_files)) or 'none'}"])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def post_github_review(target: ReviewTarget, payload_path: Path) -> None:
    run_command(["gh", "api", f"repos/{target.owner}/{target.repo}/pulls/{target.number}/reviews", "-X", "POST", "--input", str(payload_path)])


def default_out_dir(target: ReviewTarget) -> Path:
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return ROOT / "generated" / "code_reviews" / f"{target.slug}_{stamp}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Claude as an independent GitHub PR reviewer through read-only repo tools.")
    parser.add_argument("--pr", required=True, help="OWNER/REPO#NUMBER or GitHub PR URL")
    parser.add_argument("--post", action="store_true", help="Submit verified inline comments as a GitHub PR review")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--out-dir", default="")
    parser.add_argument("--max-tool-turns", type=int, default=12)
    parser.add_argument("--max-output-tokens", type=int, default=6000)
    parser.add_argument("--mock-claude", default="", help="Path to a strict review JSON file; skips Anthropic API")
    parser.add_argument("--mock-github", default="", help="Directory with pr_metadata.json, pr_files.json, pr.diff, files/")
    args = parser.parse_args()

    target = parse_pr_target(args.pr)
    out_dir = Path(args.out_dir) if args.out_dir else default_out_dir(target)
    out_dir.mkdir(parents=True, exist_ok=True)
    reader = GitHubReader(target, Path(args.mock_github) if args.mock_github else None)
    transcript_path = out_dir / "tool_transcript.jsonl"
    state = ReadState()

    mission = build_mission(target)
    (out_dir / "review_mission.md").write_text(mission + "\n", encoding="utf-8")
    (out_dir / "claude_prompt.md").write_text(build_system_prompt() + "\n\n" + mission + "\n", encoding="utf-8")

    if args.mock_claude:
        review = json.loads(Path(args.mock_claude).read_text(encoding="utf-8"))
        (out_dir / "claude_raw.json").write_text(json.dumps({"mock_claude": str(args.mock_claude), "review": review}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        state.metadata = reader.get_pr_metadata()
        state.files = reader.list_pr_files()
        state.diff = reader.get_pr_diff()
        state.tool_names = ["get_pr_metadata", "list_pr_files", "get_pr_diff", "finalize_review"]
    else:
        review, state, transcript = run_claude_review(target, reader, model=args.model, max_tool_turns=args.max_tool_turns, max_tokens=args.max_output_tokens, transcript_path=transcript_path)
        (out_dir / "claude_raw.json").write_text(json.dumps(transcript, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    validate_review_shape(review)
    verified, rejected = verify_findings(review, state)
    payload = build_github_payload(target, state, verified)

    (out_dir / "repo_read_log.json").write_text(json.dumps({"tools_used": state.tool_names, "files_read": sorted(state.read_files), "metadata": state.metadata, "checks": state.checks}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out_dir / "claude_review.json").write_text(json.dumps(review, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out_dir / "verified_findings.json").write_text(json.dumps({"verified": verified, "rejected": rejected}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    payload_path = out_dir / "github_review_payload.json"
    payload_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_report(out_dir / "review_report.md", target, review, verified, rejected, state)

    if args.post:
        if not verified:
            raise ReviewError("--post requested but no verified inline findings were available")
        post_github_review(target, payload_path)

    print(json.dumps({"out_dir": str(out_dir), "verified_findings": len(verified), "rejected_findings": len(rejected), "posted": bool(args.post)}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ReviewError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
