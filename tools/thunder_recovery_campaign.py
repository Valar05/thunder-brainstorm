#!/usr/bin/env python3
"""Receipt-gated recovery campaign for Thunder Brainstorm archaeology.

This script does not crawl code. It verifies the existing Run-One survey artifacts,
merges them through tools/turbo_survey.py when both machine receipts are valid,
and emits a compact recovery manifest suitable for durable Home Center ingestion.

Typical use on a body that can see both receipts:
  python tools/thunder_recovery_campaign.py \
    --phone generated/survey/phone \
    --laptop generated/survey/laptop \
    --out generated/survey/recovery

Acceptance is intentionally strict: both physical-machine surveys must parse, their
receipt hashes must match survey.json, the kingdom merge receipt must match its
output, and the manifest records what is still missing instead of inventing success.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def verify_scan(label: str, directory: Path) -> dict[str, Any]:
    survey_path = directory / "survey.json"
    receipt_path = directory / "receipt.json"
    result: dict[str, Any] = {
        "label": label,
        "directory": str(directory),
        "valid": False,
        "errors": [],
    }
    if not survey_path.is_file():
        result["errors"].append("missing survey.json")
        return result
    if not receipt_path.is_file():
        result["errors"].append("missing receipt.json")
        return result
    try:
        survey = load_json(survey_path)
        receipt = load_json(receipt_path)
    except Exception as exc:
        result["errors"].append(f"parse failure: {exc!r}")
        return result
    if survey.get("schema") != "thunder.turbo-survey.v1":
        result["errors"].append(f"unexpected survey schema: {survey.get('schema')!r}")
    if receipt.get("kind") != "thunder-run-one-survey":
        result["errors"].append(f"unexpected receipt kind: {receipt.get('kind')!r}")
    actual = sha256(survey_path)
    if receipt.get("sha256") != actual:
        result["errors"].append("receipt sha256 does not match survey.json")
    repos = survey.get("repos")
    if not isinstance(repos, list):
        result["errors"].append("survey repos is not a list")
        repos = []
    machine = survey.get("machine_label") or survey.get("environment", {}).get("machine")
    if not machine:
        result["errors"].append("missing machine identity")
    result.update({
        "machine": machine,
        "created_at": survey.get("created_at"),
        "roots": survey.get("roots", []),
        "repo_count": len(repos),
        "duplicate_groups": len(survey.get("duplicates", [])),
        "survey_sha256": actual,
        "survey_path": str(survey_path),
        "receipt_path": str(receipt_path),
        "valid": not result["errors"],
    })
    return result


def verify_kingdom(directory: Path) -> dict[str, Any]:
    kingdom_path = directory / "kingdom_survey.json"
    queue_path = directory / "excavation_queue.jsonl"
    receipt_path = directory / "receipt.json"
    result: dict[str, Any] = {"valid": False, "errors": [], "directory": str(directory)}
    for path in (kingdom_path, queue_path, receipt_path):
        if not path.is_file():
            result["errors"].append(f"missing {path.name}")
    if result["errors"]:
        return result
    try:
        kingdom = load_json(kingdom_path)
        receipt = load_json(receipt_path)
    except Exception as exc:
        result["errors"].append(f"parse failure: {exc!r}")
        return result
    if kingdom.get("schema") != "thunder.turbo-survey-merge.v1":
        result["errors"].append(f"unexpected kingdom schema: {kingdom.get('schema')!r}")
    if receipt.get("kind") != "thunder-kingdom-survey":
        result["errors"].append(f"unexpected receipt kind: {receipt.get('kind')!r}")
    actual = sha256(kingdom_path)
    if receipt.get("sha256") != actual:
        result["errors"].append("receipt sha256 does not match kingdom_survey.json")
    repos = kingdom.get("repos") if isinstance(kingdom.get("repos"), list) else []
    machines = kingdom.get("machines") if isinstance(kingdom.get("machines"), list) else []
    top = []
    for r in repos[:25]:
        top.append({
            "machine": r.get("machine"),
            "path": r.get("path"),
            "remote": r.get("remote"),
            "head": r.get("head"),
            "priority_score": r.get("priority_score"),
            "status": r.get("status"),
            "technology_hints": r.get("tree", {}).get("technology_hints", []),
            "filename_tags": r.get("tree", {}).get("filename_tags", {}),
        })
    result.update({
        "valid": not result["errors"],
        "created_at": kingdom.get("created_at"),
        "machine_count": len(machines),
        "repo_count": len(repos),
        "duplicate_groups": len(kingdom.get("duplicates", [])),
        "kingdom_sha256": actual,
        "kingdom_path": str(kingdom_path),
        "queue_path": str(queue_path),
        "receipt_path": str(receipt_path),
        "top_excavation_targets": top,
    })
    return result


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify, merge, and recover Thunder archaeology receipts")
    ap.add_argument("--phone", required=True, help="directory containing phone survey.json and receipt.json")
    ap.add_argument("--laptop", required=True, help="directory containing laptop survey.json and receipt.json")
    ap.add_argument("--out", required=True, help="output directory for kingdom + recovery manifest")
    ap.add_argument("--no-merge", action="store_true", help="verify an already existing kingdom in OUT")
    args = ap.parse_args()

    phone_dir = Path(args.phone).expanduser().resolve()
    laptop_dir = Path(args.laptop).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    phone = verify_scan("primary-phone", phone_dir)
    laptop = verify_scan("THECAULDRON", laptop_dir)
    merge_attempt: dict[str, Any] = {"attempted": False}

    if phone["valid"] and laptop["valid"] and not args.no_merge:
        turbo = Path(__file__).resolve().with_name("turbo_survey.py")
        cmd = [
            sys.executable, str(turbo), "merge",
            str(phone_dir / "survey.json"), str(laptop_dir / "survey.json"),
            "--out", str(out_dir),
        ]
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors="replace")
        merge_attempt = {
            "attempted": True,
            "returncode": p.returncode,
            "stdout": p.stdout[-4000:],
            "stderr": p.stderr[-4000:],
            "command": cmd,
        }

    kingdom = verify_kingdom(out_dir)
    accepted = bool(phone["valid"] and laptop["valid"] and kingdom["valid"] and kingdom.get("machine_count", 0) >= 2)
    blockers = []
    if not phone["valid"]:
        blockers.append({"stage": "primary-phone survey", "errors": phone["errors"]})
    if not laptop["valid"]:
        blockers.append({"stage": "THECAULDRON survey", "errors": laptop["errors"]})
    if phone["valid"] and laptop["valid"] and not kingdom["valid"]:
        blockers.append({"stage": "kingdom merge", "errors": kingdom["errors"]})

    manifest = {
        "schema": "thunder.recovery-campaign.v1",
        "created_at": utcnow(),
        "accepted": accepted,
        "state": "RECEIPT_BACKED_COMPLETE" if accepted else "CONTINUE_REQUIRED",
        "phone": phone,
        "laptop": laptop,
        "merge_attempt": merge_attempt,
        "kingdom": kingdom,
        "blockers": blockers,
        "home_center_contract": {
            "destination": "Home Center Drive",
            "required_delivery": [
                "recovery_manifest.json",
                "kingdom_survey.json",
                "excavation_queue.jsonl",
                "kingdom receipt.json",
            ],
            "readback_required": True,
            "assistant_recovery_rule": "Future ChatGPT sessions retrieve the durable Home Center recovery record; Drew must not be asked to paste crawl output.",
        },
    }
    manifest_path = out_dir / "recovery_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "accepted": accepted,
        "state": manifest["state"],
        "manifest": str(manifest_path),
        "manifest_sha256": sha256(manifest_path),
        "blockers": blockers,
    }, ensure_ascii=False))
    return 0 if accepted else 2


if __name__ == "__main__":
    raise SystemExit(main())
