#!/usr/bin/env python3
"""Capture a GitHub PR fixture for offline Claude review-driver tests."""
from __future__ import annotations

import argparse
import base64
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTS = {
    ".gd", ".py", ".js", ".ts", ".tsx", ".jsx", ".vue", ".cs", ".cpp", ".c", ".h", ".hpp",
    ".java", ".kt", ".swift", ".rs", ".go", ".rb", ".php", ".html", ".css", ".scss", ".md",
    ".json", ".yaml", ".yml", ".toml", ".ini", ".godot", ".sh", ".mjs", ".cjs",
}


class FixtureError(RuntimeError):
    pass


def parse_pr_target(raw: str) -> tuple[str, str, int]:
    raw = raw.strip()
    url_match = re.match(r"https://github\.com/([^/]+)/([^/]+)/pull/(\d+)", raw)
    if url_match:
        return url_match.group(1), url_match.group(2), int(url_match.group(3))
    match = re.match(r"([^\s/#]+)/([^\s#]+)#(\d+)$", raw)
    if match:
        return match.group(1), match.group(2), int(match.group(3))
    raise FixtureError("PR target must be OWNER/REPO#NUMBER or a GitHub pull request URL")


def run_gh(args: list[str]) -> str:
    try:
        return subprocess.check_output(["gh", "api", *args], stderr=subprocess.PIPE, text=True)
    except FileNotFoundError as exc:
        raise FixtureError("required command not found: gh") from exc
    except subprocess.CalledProcessError as exc:
        raise FixtureError(f"gh api failed: {' '.join(args)}\n{exc.stderr.strip()}") from exc


def gh_json(path: str) -> Any:
    return json.loads(run_gh([path]))


def gh_diff(owner: str, repo: str, number: int) -> str:
    return run_gh([f"repos/{owner}/{repo}/pulls/{number}", "-H", "Accept: application/vnd.github.v3.diff"])


def read_file(owner: str, repo: str, path: str, ref: str) -> str:
    from urllib.parse import quote
    data = gh_json(f"repos/{owner}/{repo}/contents/{quote(path, safe='/')}?ref={quote(ref, safe='')}")
    if data.get("encoding") != "base64" or not data.get("content"):
        raise FixtureError(f"GitHub did not return base64 file content for {path}")
    return base64.b64decode(data["content"]).decode("utf-8", errors="ignore")


def is_text_file(path: str) -> bool:
    suffix = Path(path).suffix.lower()
    return not suffix or suffix in TEXT_EXTS


def capture_fixture(pr: str, out_dir: Path, max_files: int) -> dict[str, Any]:
    owner, repo, number = parse_pr_target(pr)
    out_dir.mkdir(parents=True, exist_ok=True)
    files_dir = out_dir / "files"
    files_dir.mkdir(parents=True, exist_ok=True)

    metadata = gh_json(f"repos/{owner}/{repo}/pulls/{number}")
    files = gh_json(f"repos/{owner}/{repo}/pulls/{number}/files?per_page=100")
    diff = gh_diff(owner, repo, number)
    head_sha = metadata.get("head", {}).get("sha", "")
    copied: list[str] = []
    skipped: list[dict[str, str]] = []

    for item in files[:max_files]:
        path = item.get("filename", "")
        if not path or not is_text_file(path):
            skipped.append({"path": path, "reason": "non-text or missing filename"})
            continue
        if item.get("status") == "removed":
            skipped.append({"path": path, "reason": "removed file has no head content"})
            continue
        try:
            text = read_file(owner, repo, path, head_sha)
        except Exception as exc:
            skipped.append({"path": path, "reason": str(exc)})
            continue
        target = files_dir / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        copied.append(path)

    minimal_metadata = {
        "number": metadata.get("number"),
        "title": metadata.get("title"),
        "state": metadata.get("state"),
        "html_url": metadata.get("html_url"),
        "base": {"ref": metadata.get("base", {}).get("ref"), "sha": metadata.get("base", {}).get("sha")},
        "head": {"ref": metadata.get("head", {}).get("ref"), "sha": head_sha},
        "user": metadata.get("user"),
    }
    (out_dir / "pr_metadata.json").write_text(json.dumps(minimal_metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out_dir / "pr_files.json").write_text(json.dumps(files, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out_dir / "pr.diff").write_text(diff, encoding="utf-8")
    try:
        checks = gh_json(f"repos/{owner}/{repo}/commits/{head_sha}/check-runs")
    except Exception as exc:
        checks = {"error": str(exc), "check_runs": []}
    (out_dir / "ci_checks.json").write_text(json.dumps(checks, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    manifest = {"pr": f"{owner}/{repo}#{number}", "head_sha": head_sha, "copied_files": copied, "skipped_files": skipped}
    (out_dir / "fixture_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture a GitHub PR fixture compatible with tools/claude_code_review.py --mock-github.")
    parser.add_argument("--pr", required=True, help="OWNER/REPO#NUMBER or GitHub PR URL")
    parser.add_argument("--out", required=True, help="Fixture output directory")
    parser.add_argument("--max-files", type=int, default=80, help="Maximum changed files to copy from PR head")
    args = parser.parse_args()

    manifest = capture_fixture(args.pr, Path(args.out), args.max_files)
    command = f"python tools/claude_code_review.py --pr {manifest['pr']} --mock-github {args.out} --mock-claude PATH_TO_REVIEW_JSON --out-dir generated/code_reviews/mock_run"
    print(json.dumps({"fixture": args.out, "copied_files": len(manifest["copied_files"]), "skipped_files": len(manifest["skipped_files"]), "mock_review_command": command}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except FixtureError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
