#!/usr/bin/env python3
"""Offline half of Thunder's JIT source-intake transaction."""
from __future__ import annotations
import argparse, hashlib, json, os, shutil, subprocess, tempfile, time
from pathlib import Path
from typing import Any

GAP_SCHEMA = "thunder-source-gap-v1"
PACKET_SCHEMA = "thunder-source-packet-v1"
RECEIPT_SCHEMA = "thunder-source-publication-v1"
LOCK_SCHEMA = "thunder-source-lock-v1"
SHA = set("0123456789abcdef")
class ThunderSourceError(RuntimeError): pass

def canonical(v: Any) -> bytes:
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
def digest(v: bytes | Any) -> str:
    return hashlib.sha256(v if isinstance(v, bytes) else canonical(v)).hexdigest()
def sealed(v: dict[str, Any], key: str) -> dict[str, Any]:
    clean = {k: x for k, x in v.items() if k != key}
    return {**clean, key: digest(clean)}
def verify_seal(v: dict[str, Any], key: str, label: str) -> None:
    if v.get(key) != digest({k: x for k, x in v.items() if k != key}):
        raise ThunderSourceError(f"{label} seal mismatch")
def load(path: Path) -> Any:
    try: return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as e: raise ThunderSourceError(f"cannot read {path}: {e}") from e
def save(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + f".tmp-{os.getpid()}")
    data = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False).encode() + b"\n"
    with temp.open("xb") as f: f.write(data); f.flush(); os.fsync(f.fileno())
    if temp.read_bytes() != data: raise ThunderSourceError("temporary readback mismatch")
    os.replace(temp, path)
    if path.read_bytes() != data: raise ThunderSourceError("final readback mismatch")
def run(argv: list[str], cwd: Path, ok: tuple[int, ...] = (0,)) -> subprocess.CompletedProcess[str]:
    r = subprocess.run(argv, cwd=cwd, text=True, capture_output=True, check=False)
    if r.returncode not in ok: raise ThunderSourceError(f"command failed {argv!r}: {r.stderr[-1000:]}")
    return r
def git(repo: Path, *args: str) -> str: return run(["git", *args], repo).stdout.strip()
def require_clean(repo: Path) -> str:
    if git(repo, "status", "--porcelain=v1"): raise ThunderSourceError("canonical Thunder is dirty")
    return git(repo, "rev-parse", "HEAD")
def valid_sha(x: Any) -> bool: return isinstance(x, str) and len(x) == 64 and not (set(x) - SHA)
def require_text(x: Any, label: str) -> str:
    if not isinstance(x, str) or not x.strip() or "\x00" in x: raise ThunderSourceError(f"{label} must be nonempty text")
    return x

def pid_alive(pid: int) -> bool:
    try: os.kill(pid, 0); return True
    except ProcessLookupError: return False
    except (PermissionError, OSError): return True
def acquire(repo: Path, operation: str) -> Path:
    lock = repo / ".git" / ".thunder-source.lock.d"
    try: lock.mkdir()
    except FileExistsError:
        owner_path = lock / "owner.json"
        if not owner_path.is_file(): raise ThunderSourceError("ambiguous Thunder lock")
        owner = load(owner_path); verify_seal(owner, "owner_seal", "lock")
        raise ThunderSourceError(f"Thunder lock held by pid {owner['pid']} for {owner['operation']}")
    owner = sealed({"schema": LOCK_SCHEMA, "pid": os.getpid(), "operation": operation, "head": git(repo, "rev-parse", "HEAD")}, "owner_seal")
    save(lock / "owner.json", owner)
    save(lock / "journal.json", sealed({"schema": "thunder-source-lock-journal-v1", "pid": owner["pid"], "operation": operation, "head": owner["head"]}, "journal_seal"))
    return lock
def release(lock: Path) -> None:
    (lock / "journal.json").unlink(); (lock / "owner.json").unlink(); lock.rmdir()
def recover_lock(repo: Path) -> dict[str, Any]:
    repo = repo.resolve(); lock = repo / ".git" / ".thunder-source.lock.d"
    if not lock.is_dir(): return {"ok": True, "action": "no-lock"}
    owner = load(lock / "owner.json"); journal = load(lock / "journal.json")
    verify_seal(owner, "owner_seal", "lock"); verify_seal(journal, "journal_seal", "lock journal")
    if any(owner[k] != journal[k] for k in ("pid", "operation", "head")): raise ThunderSourceError("lock owner and journal disagree")
    if pid_alive(owner["pid"]): raise ThunderSourceError(f"cannot recover live Thunder lock pid {owner['pid']}")
    if git(repo, "rev-parse", "HEAD") != owner["head"] or git(repo, "status", "--porcelain=v1"): raise ThunderSourceError("canonical state disagrees with lock journal")
    release(lock); return {"ok": True, "action": "recovered", "operation": owner["operation"]}

def validate_gap(v: Any) -> dict[str, Any]:
    if not isinstance(v, dict) or v.get("schema") != GAP_SCHEMA: raise ThunderSourceError("gap schema mismatch")
    verify_seal(v, "gap_seal", "gap")
    for key in ("capability", "query", "project", "local_index_sha256"): require_text(v.get(key), f"gap.{key}")
    if not valid_sha(v["local_index_sha256"]): raise ThunderSourceError("gap local index hash invalid")
    if not isinstance(v.get("owner_evidence"), list) or not v["owner_evidence"]: raise ThunderSourceError("owner evidence required")
    if v.get("local_result") != "NO_REUSABLE_SOURCE": raise ThunderSourceError("gap requires sealed NO_REUSABLE_SOURCE")
    if v.get("jit_order") != ["local-combined-index", "github:Valar05", "github:bounded-authoritative-public"]: raise ThunderSourceError("JIT order mismatch")
    return v
def validate_packet(v: Any, gap: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(v, dict) or v.get("schema") != PACKET_SCHEMA: raise ThunderSourceError("packet schema mismatch")
    verify_seal(v, "packet_seal", "packet")
    if v.get("gap_seal") != gap["gap_seal"]: raise ThunderSourceError("packet does not match active gap")
    if v.get("search_order") != gap["jit_order"]: raise ThunderSourceError("packet search order mismatch")
    sources = v.get("sources")
    if not isinstance(sources, list) or not sources: raise ThunderSourceError("packet sources required")
    required = {"origin", "repo", "commit", "path", "line", "symbol", "license", "sha256", "compatibility", "behavioral_contract", "deviations"}
    for i, source in enumerate(sources):
        if not isinstance(source, dict) or set(source) != required: raise ThunderSourceError(f"source {i} fields mismatch")
        for key in required - {"line", "deviations"}: require_text(source[key], f"source {i}.{key}")
        if not isinstance(source["line"], int) or source["line"] < 1: raise ThunderSourceError("source line invalid")
        if not valid_sha(source["sha256"]): raise ThunderSourceError("source hash invalid")
        if not isinstance(source["deviations"], list): raise ThunderSourceError("source deviations invalid")
    return v

def create_gap(args: argparse.Namespace) -> dict[str, Any]:
    repo = Path(args.repo).resolve(); require_clean(repo)
    index = (repo / args.index).resolve()
    try: index.relative_to(repo)
    except ValueError as e: raise ThunderSourceError("index escapes repo") from e
    if not index.is_file(): raise ThunderSourceError("combined index missing")
    command = [args.python, str(repo / "thunder_brainstorm.py"), "search-index", args.query, "--index", str(index), "--limit", str(args.limit)]
    result = run(command, repo)
    hits = [x for x in result.stdout.splitlines() if x.strip()]
    if hits: raise ThunderSourceError("LOCAL_REUSABLE_SOURCE: inspect search results before requesting GitHub")
    gap = sealed({"schema": GAP_SCHEMA, "capability": args.capability, "query": args.query, "project": args.project, "owner_evidence": args.owner_evidence, "local_index": args.index, "local_index_sha256": digest(index.read_bytes()), "local_result": "NO_REUSABLE_SOURCE", "jit_order": ["local-combined-index", "github:Valar05", "github:bounded-authoritative-public"], "external_only": True, "organ_network_forbidden": True}, "gap_seal")
    save(Path(args.out), gap)
    return {"ok": True, "state": "NEEDS_THUNDER_SOURCE", "gap": str(Path(args.out)), "gap_seal": gap["gap_seal"]}

def recovery(recovery_dir: Path, payload: dict[str, Any]) -> Path:
    recovery_dir.mkdir(parents=True, exist_ok=True)
    out = recovery_dir / f"thunder-recovery-{digest(payload)}.json"; save(out, sealed(payload, "recovery_seal")); return out

def publish(args: argparse.Namespace) -> dict[str, Any]:
    repo = Path(args.repo).resolve(); recovery_dir = Path(args.recovery_dir).resolve(); entry = require_clean(repo)
    gap = validate_gap(load(Path(args.gap))); packet = validate_packet(load(Path(args.packet)), gap)
    lock = acquire(repo, packet["packet_seal"]); work = None; commit = None; dirty_started = None
    try:
        if git(repo, "rev-parse", "HEAD") != entry: raise ThunderSourceError("canonical HEAD changed before transaction")
        work = Path(tempfile.mkdtemp(prefix="thunder-jit-", dir=args.temp_root))
        run(["git", "worktree", "add", "--detach", str(work), entry], repo)
        dirty_started = time.monotonic()
        packet_rel = Path("generated/jit_source_packets") / f"{packet['packet_seal']}.json"
        refs_rel = Path("generated/source_refs_manual") / f"jit_{gap['gap_seal']}.jsonl"
        learning_rel = Path("generated/session_learnings") / f"jit_{gap['gap_seal']}.md"
        save(work / packet_rel, packet)
        refs = b"".join(canonical(s) + b"\n" for s in packet["sources"])
        (work / refs_rel).parent.mkdir(parents=True, exist_ok=True); (work / refs_rel).write_bytes(refs)
        learning = f"# JIT source intake {gap['capability']}\n\nGap: `{gap['gap_seal']}`\n\nPacket: `{packet['packet_seal']}`\n\nBehavioral contract: {packet['sources'][0]['behavioral_contract']}\n"
        (work / learning_rel).parent.mkdir(parents=True, exist_ok=True); (work / learning_rel).write_text(learning)
        for command in json.loads(args.test_commands):
            if not isinstance(command, list) or not command or not all(isinstance(x, str) and x for x in command): raise ThunderSourceError("test commands must be argv arrays")
            run(command, work)
        run(["git", "add", "--", str(packet_rel), str(refs_rel), str(learning_rel)], work)
        if time.monotonic() - dirty_started >= args.dirty_window_seconds: raise ThunderSourceError("dirty-window overrun before commit")
        run(["git", "-c", "user.name=Thunder JIT", "-c", "user.email=thunder-jit@localhost", "commit", "-m", f"JIT source intake: {gap['capability']}"], work)
        commit = git(work, "rev-parse", "HEAD")
        if time.monotonic() - dirty_started >= args.dirty_window_seconds: raise ThunderSourceError("dirty-window overrun after commit")
        if require_clean(repo) != entry: raise ThunderSourceError("canonical HEAD changed during transaction")
        run(["git", "merge", "--ff-only", commit], repo)
        if require_clean(repo) != commit: raise ThunderSourceError("canonical did not finish clean at publication commit")
        receipt = sealed({"schema": RECEIPT_SCHEMA, "entry_head": entry, "commit": commit, "gap_seal": gap["gap_seal"], "packet_seal": packet["packet_seal"], "dirty_window_seconds": round(time.monotonic() - dirty_started, 6), "canonical_clean": True, "network_used": False}, "receipt_seal")
        return {"ok": True, **receipt}
    except Exception as e:
        state = git(repo, "rev-parse", "HEAD") if (repo / ".git").exists() else "UNKNOWN"
        packet_path = recovery(recovery_dir, {"schema": "thunder-source-recovery-v1", "entry_head": entry, "current_head": state, "prospective_commit": commit, "gap_seal": gap["gap_seal"], "packet_seal": packet["packet_seal"], "error": str(e), "canonical_clean": not bool(git(repo, "status", "--porcelain=v1"))})
        raise ThunderSourceError(f"{e}; recovery={packet_path}") from e
    finally:
        if work is not None:
            subprocess.run(["git", "worktree", "remove", "--force", str(work)], cwd=repo, text=True, capture_output=True)
            shutil.rmtree(work, ignore_errors=True)
        release(lock)

def parser() -> argparse.ArgumentParser:
    p=argparse.ArgumentParser(); s=p.add_subparsers(dest="command", required=True)
    g=s.add_parser("gap"); g.add_argument("--repo", required=True); g.add_argument("--index", default="generated/index_combined/mechanic_source_refs.jsonl"); g.add_argument("--python", default="python"); g.add_argument("--query", required=True); g.add_argument("--capability", required=True); g.add_argument("--project", required=True); g.add_argument("--owner-evidence", action="append", required=True); g.add_argument("--limit", type=int, default=20); g.add_argument("--out", required=True)
    x=s.add_parser("publish"); x.add_argument("--repo", required=True); x.add_argument("--gap", required=True); x.add_argument("--packet", required=True); x.add_argument("--test-commands", default='[["python","-m","py_compile","thunder_brainstorm.py"]]'); x.add_argument("--dirty-window-seconds", type=float, default=60); x.add_argument("--temp-root", default=None); x.add_argument("--recovery-dir", required=True)
    r=s.add_parser("recover-lock"); r.add_argument("--repo", required=True)
    return p
def main() -> int:
    a=parser().parse_args()
    result = create_gap(a) if a.command == "gap" else recover_lock(Path(a.repo)) if a.command == "recover-lock" else publish(a)
    print(json.dumps(result, sort_keys=True)); return 0
if __name__ == "__main__":
    try: raise SystemExit(main())
    except ThunderSourceError as e: print(json.dumps({"ok":False,"state":"REJECT","error":str(e)},sort_keys=True)); raise SystemExit(2)
