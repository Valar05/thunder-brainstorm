#!/usr/bin/env python3
"""Receipt-gated recovery campaign for Thunder Brainstorm archaeology.

This script does not crawl code. It verifies the existing Run-One survey artifacts,
merges them through tools/turbo_survey.py when both machine receipts are valid,
and emits a compact recovery manifest suitable for durable Home Center ingestion.

Acceptance is strict: both physical-machine surveys must parse, match their expected
machine identities, be fresh enough for the campaign, have receipt hashes matching
survey.json, and the resulting kingdom must contain both verified inputs and a
matching receipt. Unknown or stale evidence remains CONTINUE_REQUIRED.
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


def parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError:
        return None


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def verify_scan(
    label: str,
    directory: Path,
    expected_machine_names: set[str],
    max_age_hours: float,
) -> dict[str, Any]:
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
    normalized = str(machine or "").strip().lower()
    allowed = {x.strip().lower() for x in expected_machine_names}
    if not normalized:
        result["errors"].append("missing machine identity")
    elif normalized not in allowed:
        result["errors"].append(
            f"machine identity {machine!r} does not match expected {sorted(expected_machine_names)!r}"
        )

    receipt_machine = str(receipt.get("machine") or "").strip().lower()
    if receipt_machine and normalized and receipt_machine != normalized:
        result["errors"].append("receipt machine identity does not match survey machine identity")

    created = parse_time(survey.get("created_at"))
    if created is None:
        result["errors"].append("missing or invalid survey created_at")
        age_hours = None
    else:
        age_hours = (datetime.now(timezone.utc) - created).total_seconds() / 3600.0
        if age_hours < -0.25:
            result["errors"].append("survey created_at is implausibly in the future")
        elif max_age_hours > 0 and age_hours > max_age_hours:
            result["errors"].append(
                f"survey is stale: age_hours={age_hours:.2f} exceeds max_age_hours={max_age_hours:.2f}"
            )

    if receipt.get("created_at") and receipt.get("created_at") != survey.get("created_at"):
        result["errors"].append("receipt created_at does not match survey created_at")
    if receipt.get("repo_count") != len(repos):
        result["errors"].append("receipt repo_count does not match survey repos length")

    result.update({
        "machine": machine,
        "created_at": survey.get("created_at"),
        "age_hours": round(age_hours, 3) if age_hours is not None else None,
        "roots": survey.get("roots", []),
        "repo_count": len(repos),
        "duplicate_groups": len(survey.get("duplicates", [])),
        "survey_sha256": actual,
        "survey_path": str(survey_path),
        "receipt_path": str(receipt_path),
        "valid": not result["errors"],
    })
    return result


def read_jsonl_count(path: Path) -> tuple[int, list[str]]:
    count = 0
    errors: list[str] = []
    try:
        with path.open("r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                if not line.strip():
                    continue
                try:
                    json.loads(line)
                    count += 1
                except Exception as exc:
                    errors.append(f"invalid JSONL at line {lineno}: {exc!r}")
                    break
    except Exception as exc:
        errors.append(f"queue read failure: {exc!r}")
    return count, errors


def verify_kingdom(directory: Path, verified_scans: list[dict[str, Any]]) -> dict[str, Any]:
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
    if receipt.get("repos") != len(repos):
        result["errors"].append("kingdom receipt repo count does not match kingdom repos length")
    if receipt.get("machines") != len(machines):
        result["errors"].append("kingdom receipt machine count does not match kingdom machines length")

    queue_count, queue_errors = read_jsonl_count(queue_path)
    result["errors"].extend(queue_errors)
    if not queue_errors and queue_count != len(repos):
        result["errors"].append(
            f"excavation queue count {queue_count} does not match kingdom repo count {len(repos)}"
        )

    expected_machine_names = {str(s.get("machine") or "").strip().lower() for s in verified_scans}
    kingdom_machine_names = {
        str(m.get("machine_label") or m.get("environment", {}).get("machine") or "").strip().lower()
        for m in machines if isinstance(m, dict)
    }
    if "" in kingdom_machine_names:
        result["errors"].append("kingdom contains machine entry without identity")
    if expected_machine_names != kingdom_machine_names:
        result["errors"].append(
            f"kingdom machine set {sorted(kingdom_machine_names)!r} does not equal verified inputs {sorted(expected_machine_names)!r}"
        )

    expected_hashes = {str(s.get("survey_sha256")) for s in verified_scans}
    input_repo_counts = sum(int(s.get("repo_count", 0)) for s in verified_scans)
    if len(repos) != input_repo_counts:
        result["errors"].append(
            f"kingdom repo count {len(repos)} does not equal verified input repo total {input_repo_counts}"
        )

    # turbo_survey v1 does not yet embed input hashes in kingdom_survey.json. Record
    # the verified input hashes here so the recovery manifest binds the merge to them.
    result["verified_input_survey_sha256"] = sorted(expected_hashes)

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
        "queue_count": queue_count,
        "duplicate_groups": len(kingdom.get("duplicates", [])),
        "kingdom_sha256": actual,
        "kingdom_path": str(kingdom_path),
        "queue_path": str(queue_path),
        "queue_sha256": sha256(queue_path),
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
    ap.add_argument(
        "--max-age-hours", type=float, default=24.0,
        help="maximum accepted survey age; <=0 disables freshness gate (default: 24)",
    )
    args = ap.parse_args()

    phone_dir = Path(args.phone).expanduser().resolve()
    laptop_dir = Path(args.laptop).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    phone = verify_scan(
        "primary-phone", phone_dir,
        {"primary-phone"}, args.max_age_hours,
    )
    laptop = verify_scan(
        "THECAULDRON", laptop_dir,
        {"THECAULDRON", "TheCauldron", "windows-hands-01"}, args.max_age_hours,
    )
    merge_attempt: dict[str, Any] = {"attempted": False}

    both_valid = bool(phone["valid"] and laptop["valid"])
    if both_valid and not args.no_merge:
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

    verified_inputs = [s for s in (phone, laptop) if s.get("valid")]
    kingdom = verify_kingdom(out_dir, verified_inputs) if both_valid else {
        "valid": False,
        "errors": ["kingdom verification withheld until both physical-machine surveys are valid"],
        "directory": str(out_dir),
    }

    if merge_attempt.get("attempted") and merge_attempt.get("returncode") != 0:
        kingdom["valid"] = False
        kingdom.setdefault("errors", []).append(
            f"Thunder merge process exited {merge_attempt.get('returncode')}"
        )

    accepted = bool(both_valid and kingdom.get("valid") and kingdom.get("machine_count", 0) == 2)
    blockers = []
    if not phone["valid"]:
        blockers.append({"stage": "primary-phone survey", "errors": phone["errors"]})
    if not laptop["valid"]:
        blockers.append({"stage": "THECAULDRON survey", "errors": laptop["errors"]})
    if both_valid and not kingdom.get("valid"):
        blockers.append({"stage": "kingdom merge", "errors": kingdom.get("errors", [])})

    manifest = {
        "schema": "thunder.recovery-campaign.v2",
        "created_at": utcnow(),
        "accepted": accepted,
        "state": "RECEIPT_BACKED_COMPLETE" if accepted else "CONTINUE_REQUIRED",
        "venice_review": {
            "rule": "truth survives desire for completion",
            "machine_identity_enforced": True,
            "freshness_enforced": args.max_age_hours > 0,
            "input_output_membership_enforced": True,
            "queue_consistency_enforced": True,
            "merge_exit_enforced": True,
        },
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
