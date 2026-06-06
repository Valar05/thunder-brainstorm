#!/usr/bin/env python3
from __future__ import annotations

import argparse
import http.client
import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = os.environ.get("THUNDER_CLAUDE_MODEL", os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6"))


def load_env() -> None:
    for path in (Path.home() / ".secrets" / "anthropic.env", Path.home() / ".bashrc", Path.home() / ".profile"):
        if not path.exists():
            continue
        for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("export "):
                line = line[len("export ") :].strip()
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            if not key or key in os.environ:
                continue
            value = value.strip().strip('"').strip("'")
            os.environ[key] = value


def extract_json_object(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json)?\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)
    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        pass
    start = stripped.find("{")
    end = stripped.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("Claude response did not contain a JSON object")
    return json.loads(stripped[start : end + 1])


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


def decode_stream(response: Any) -> str:
    text_parts: list[str] = []
    stop_reason = ""
    for raw_line in response:
        line = raw_line.decode("utf-8", errors="replace").strip()
        if not line.startswith("data:"):
            continue
        data = line[5:].strip()
        if data == "[DONE]":
            break
        try:
            event = json.loads(data)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "error":
            raise SystemExit(f"Anthropic stream error: {json.dumps(event.get('error', event), ensure_ascii=False)}")
        if event.get("type") == "message_delta":
            delta = event.get("delta", {})
            if isinstance(delta, dict):
                stop_reason = str(delta.get("stop_reason", "") or stop_reason)
        if event.get("type") == "content_block_delta":
            delta = event.get("delta", {})
            if isinstance(delta, dict) and delta.get("type") == "text_delta":
                text_parts.append(str(delta.get("text", "")))
    text = "".join(text_parts).strip()
    if stop_reason == "max_tokens":
        raise SystemExit("Anthropic stopped at max_tokens; retry with --max-output-tokens higher")
    if not text:
        raise SystemExit("Anthropic stream returned no text")
    return text


def call_claude(system: str, user: str, model: str, max_tokens: int) -> tuple[dict[str, Any] | None, str]:
    api_key = env_value("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("ANTHROPIC_API_KEY is not set")
    body = {
        "model": model,
        "max_tokens": max_tokens,
        "temperature": 0.35,
        "stream": True,
        "system": system,
        "messages": [{"role": "user", "content": user}],
    }
    request = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "thunder-brainstorm-claude-packet/1.0",
            "Connection": "close",
        },
        method="POST",
    )
    attempts = int(os.environ.get("THUNDER_CLAUDE_API_ATTEMPTS", "2"))
    timeout = int(os.environ.get("THUNDER_CLAUDE_API_TIMEOUT", "180"))
    errors: list[str] = []
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return None, decode_stream(response)
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise SystemExit(f"Anthropic API error {exc.code}: {detail}") from exc
        except (urllib.error.URLError, TimeoutError, ConnectionResetError, BrokenPipeError, json.JSONDecodeError, http.client.HTTPException) as exc:
            errors.append(f"attempt {attempt}: {exc}")
            if attempt < attempts:
                time.sleep(min(2 ** attempt, 6))
    raise SystemExit("Anthropic API connection failed:\n" + "\n".join(errors))


def response_text(payload: dict[str, Any]) -> str:
    parts: list[str] = []
    for block in payload.get("content", []):
        if block.get("type") == "text":
            parts.append(block.get("text", ""))
    return "\n".join(parts).strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", default="generated/source_packets/claude_maze_chase_roguelike_prompt.md")
    parser.add_argument("--source", default="generated/source_packets/maze_chase_roguelike_pacman_stub.md")
    parser.add_argument("--out", default="generated/game_stubs/scrap_cathedral_maze_chase_claude_candidate.json")
    parser.add_argument("--raw-out", default="generated/game_stubs/scrap_cathedral_maze_chase_claude_raw.txt")
    parser.add_argument("--response-json", default="generated/game_stubs/scrap_cathedral_maze_chase_claude_response.json")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--max-output-tokens", type=int, default=5000)
    args = parser.parse_args()

    load_env()
    prompt = (ROOT / args.prompt).read_text(encoding="utf-8")
    source = (ROOT / args.source).read_text(encoding="utf-8")
    system = "You are a game systems designer. Return only the requested JSON object, with no prose wrapper."
    user = f"{prompt}\n\n## Full Source Packet Contents\n\n```markdown\n{source}\n```"
    print(json.dumps({
        "model": args.model,
        "estimated_input_tokens": max(1, (len(system) + len(user) + 3) // 4),
        "max_output_tokens": args.max_output_tokens,
    }, indent=2))
    payload, text = call_claude(system, user, args.model, args.max_output_tokens)

    raw_out = ROOT / args.raw_out
    raw_out.parent.mkdir(parents=True, exist_ok=True)
    raw_out.write_text(text + "\n", encoding="utf-8")
    if payload is not None:
        (ROOT / args.response_json).write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    candidate = extract_json_object(text)
    out = ROOT / args.out
    out.write_text(json.dumps(candidate, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
