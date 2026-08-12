#!/usr/bin/env python3
"""Thunder Brainstorm Run-One turbo archaeology survey.

Read-mostly, cross-platform, stdlib-only. Survey local repositories and project trees
quickly, in parallel, without deep source interpretation. Produces durable JSON/JSONL
receipts that can be merged across phone + laptop.

Examples:
  python tools/turbo_survey.py scan --root /storage/emulated/0/Documents/GodotProjects --out generated/survey/phone
  python tools/turbo_survey.py scan --root C:\\Users\\dclar\\workspace --out generated/survey/laptop
  python tools/turbo_survey.py merge generated/survey/phone/survey.json generated/survey/laptop/survey.json --out generated/survey/kingdom
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

SKIP_DIRS = {
    ".git", ".hg", ".svn", "node_modules", ".godot", ".gradle", ".idea",
    "__pycache__", ".venv", "venv", "dist", "build", "Library", "Temp",
    "Cache", "Caches", "$RECYCLE.BIN", "System Volume Information",
}
MANIFESTS = {
    "project.godot": "godot", "package.json": "javascript", "pyproject.toml": "python",
    "requirements.txt": "python", "Cargo.toml": "rust", "go.mod": "go",
    "CMakeLists.txt": "cmake", "Dockerfile": "docker", "manifest.json": "web_manifest",
    "build.gradle": "gradle", "build.gradle.kts": "gradle", "settings.gradle": "gradle",
    "settings.gradle.kts": "gradle", "tsconfig.json": "typescript", "vite.config.js": "vite",
    "vite.config.ts": "vite", "webpack.config.js": "webpack", "Makefile": "make",
    "justfile": "just", "Taskfile.yml": "taskfile", "Taskfile.yaml": "taskfile",
    ".gitattributes": "git_attributes", ".gitmodules": "git_submodules", ".gitignore": "git_ignore",
}
EXT_TECH = {
    ".gd": "godot", ".gdshader": "shader", ".glsl": "shader", ".wgsl": "shader",
    ".vert": "shader", ".frag": "shader", ".blend": "blender", ".glb": "3d",
    ".gltf": "3d", ".fbx": "3d", ".obj": "3d", ".ase": "2d_art",
    ".aseprite": "2d_art", ".ts": "typescript", ".tsx": "typescript", ".js": "javascript",
    ".py": "python", ".rs": "rust", ".go": "go", ".cs": "dotnet", ".csproj": "dotnet",
    ".sln": "dotnet", ".cpp": "cpp", ".c": "c", ".java": "java", ".kt": "kotlin",
    ".sql": "database", ".proto": "protobuf", ".html": "web", ".css": "web",
}
KEYWORD_TAGS = {
    "animation": ("anim", "tween", "rig", "skeleton", "bone", "ik", "morph", "blendshape"),
    "rendering": ("shader", "material", "render", "postprocess", "palette", "dither"),
    "audio": ("audio", "sound", "sfx", "music", "tts", "voice"),
    "testing": ("test", "fixture", "spec", "smoke", "acceptance", "fuzz"),
    "agent": ("agent", "worker", "orchestrat", "prompt", "memory", "capability", "dispatcher"),
    "reliability": ("receipt", "checkpoint", "recovery", "retry", "backoff", "idempot", "watchdog"),
    "accessibility": ("accessib", "screenreader", "screen_reader", "semantic", "tts", "caption"),
    "deployment": ("deploy", "docker", "workflow", "bootstrap", "provision", "cloud", "ci"),
    "data": ("sqlite", "schema", "migration", "database", "jsonl", "wal", "cache"),
    "cli": ("cli", "command", "terminal", "shell", "argparse"),
    "mechanics": ("combat", "quest", "spawn", "enemy", "upgrade", "cooldown", "hitbox", "physics"),
}
LFS_HEADER = b"version https://git-lfs.github.com/spec/v1"
TOOL_NAMES = ["git", "gh", "git-lfs", "python", "python3", "node", "godot", "godot4", "blender", "ffmpeg", "ffprobe"]


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def run(cmd: list[str], cwd: Path | None = None, timeout: float = 8.0) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, cwd=str(cwd) if cwd else None, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, text=True, errors="replace", timeout=timeout)
        return p.returncode, p.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return 127, ""


def git(repo: Path, *args: str, timeout: float = 8.0) -> str:
    code, out = run(["git", *args], cwd=repo, timeout=timeout)
    return out if code == 0 else ""


def normalize_remote(url: str) -> str:
    s = url.strip().replace("\\", "/")
    s = re.sub(r"^git@github\.com:", "https://github.com/", s, flags=re.I)
    s = re.sub(r"^ssh://git@github\.com/", "https://github.com/", s, flags=re.I)
    s = re.sub(r"\.git$", "", s)
    return s.lower()


def parse_status(raw: str) -> dict[str, Any]:
    out: dict[str, Any] = {"branch": "", "upstream": "", "ahead": 0, "behind": 0,
                           "staged": 0, "modified": 0, "untracked": 0, "conflicted": 0}
    for line in raw.splitlines():
        if line.startswith("# branch.head "):
            out["branch"] = line[14:].strip()
        elif line.startswith("# branch.upstream "):
            out["upstream"] = line[18:].strip()
        elif line.startswith("# branch.ab "):
            m = re.search(r"\+(\d+)\s+-(\d+)", line)
            if m:
                out["ahead"], out["behind"] = int(m.group(1)), int(m.group(2))
        elif line.startswith("? "):
            out["untracked"] += 1
        elif line.startswith("u "):
            out["conflicted"] += 1
        elif line.startswith(("1 ", "2 ")):
            parts = line.split(" ", 2)
            if len(parts) > 1 and len(parts[1]) >= 2:
                if parts[1][0] != ".": out["staged"] += 1
                if parts[1][1] != ".": out["modified"] += 1
    out["dirty"] = any(out[k] for k in ("staged", "modified", "untracked", "conflicted"))
    return out


def discover_repos(root: Path, max_depth: int = 8) -> list[Path]:
    found: set[Path] = set()
    root = root.expanduser().resolve()
    if not root.exists(): return []
    for current, dirs, _files in os.walk(root):
        p = Path(current)
        try: depth = len(p.relative_to(root).parts)
        except ValueError: depth = 0
        if depth > max_depth:
            dirs[:] = []
            continue
        if ".git" in dirs or (p / ".git").is_file():
            found.add(p)
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    return sorted(found, key=lambda p: str(p).lower())


def shallow_tree(repo: Path, max_files: int) -> dict[str, Any]:
    ext = Counter(); top = Counter(); tech = Counter(); tags = Counter(); interesting: list[str] = []
    newest: list[tuple[float, str]] = []; largest: list[tuple[int, str]] = []
    total = 0; lfs_pointers = 0; symlinks = 0; executable = 0
    for current, dirs, files in os.walk(repo):
        p = Path(current); dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if total >= max_files: break
            path = p / name
            try:
                rel = path.relative_to(repo); st = path.lstat()
            except OSError: continue
            total += 1
            suffix = path.suffix.lower() or "<none>"; ext[suffix] += 1
            if rel.parts: top[rel.parts[0]] += 1
            if path.is_symlink(): symlinks += 1
            if os.name != "nt" and bool(st.st_mode & 0o111): executable += 1
            if name in MANIFESTS:
                interesting.append(str(rel)); tech[MANIFESTS[name]] += 1
            if suffix in EXT_TECH: tech[EXT_TECH[suffix]] += 1
            hay = str(rel).lower()
            for tag, needles in KEYWORD_TAGS.items():
                if any(n in hay for n in needles): tags[tag] += 1
            newest.append((st.st_mtime, str(rel))); largest.append((st.st_size, str(rel)))
            if st.st_size <= 1024:
                try:
                    with path.open("rb") as f:
                        if f.read(len(LFS_HEADER)) == LFS_HEADER: lfs_pointers += 1
                except OSError: pass
        if total >= max_files: break
    newest.sort(reverse=True); largest.sort(reverse=True)
    return {
        "files_seen": total, "extensions": dict(ext.most_common(40)),
        "top_level_counts": dict(top.most_common(30)), "technology_hints": sorted(tech),
        "filename_tags": dict(tags.most_common()), "interesting_files": sorted(interesting)[:120],
        "newest_files": [{"path": p, "mtime": datetime.fromtimestamp(t, timezone.utc).isoformat()} for t,p in newest[:25]],
        "largest_files": [{"path": p, "bytes": s} for s,p in largest[:25]],
        "lfs_pointer_files_seen": lfs_pointers, "symlinks_seen": symlinks,
        "executables_seen": executable, "truncated": total >= max_files,
    }


def repo_score(r: dict[str, Any]) -> int:
    s = r["status"]
    return (10000 if s.get("dirty") else 0) + 500*s.get("untracked",0) + 300*s.get("staged",0) + \
           200*s.get("modified",0) + 1000*s.get("ahead",0) - 20*s.get("behind",0) + \
           len(r.get("tree",{}).get("technology_hints",[]))*5


def survey_repo(repo: Path, max_files: int, fetch_remotes: bool) -> dict[str, Any]:
    t0 = time.time()
    if fetch_remotes:
        run(["git", "fetch", "--quiet", "--prune", "--no-tags", "origin"], cwd=repo, timeout=30)
    status = parse_status(git(repo, "status", "--porcelain=v2", "--branch", "--untracked-files=normal"))
    origin = git(repo, "remote", "get-url", "origin")
    head = git(repo, "rev-parse", "HEAD")
    git_dir = git(repo, "rev-parse", "--git-common-dir")
    last = git(repo, "log", "-1", "--format=%cI%x09%s")
    first = git(repo, "log", "--reverse", "--format=%cI", "--max-count=1")
    commit_count = git(repo, "rev-list", "--count", "HEAD")
    tags = git(repo, "tag", "--points-at", "HEAD")
    branches = git(repo, "branch", "--format=%(refname:short)")
    stashes = git(repo, "stash", "list", "--format=%gd%x09%ci%x09%s")
    submodules = git(repo, "submodule", "status", "--recursive", timeout=10)
    worktrees = git(repo, "worktree", "list", "--porcelain")
    object_stats = git(repo, "count-objects", "-v")
    diff_stat = git(repo, "diff", "--stat", "--no-ext-diff")
    staged_stat = git(repo, "diff", "--cached", "--stat", "--no-ext-diff")
    untracked_names = git(repo, "ls-files", "--others", "--exclude-standard").splitlines()
    tracked_count_raw = git(repo, "ls-files", "-z")
    tracked_count = tracked_count_raw.count("\x00") if tracked_count_raw else 0
    lfs = git(repo, "lfs", "ls-files", timeout=10) if run(["git", "lfs", "version"])[0] == 0 else ""
    tree = shallow_tree(repo, max_files=max_files)
    rec: dict[str, Any] = {
        "path": str(repo), "remote": origin, "remote_key": normalize_remote(origin), "head": head,
        "git_common_dir": git_dir, "status": status, "last_commit": last, "first_commit": first,
        "commit_count": int(commit_count) if commit_count.isdigit() else None,
        "branches": [x for x in branches.splitlines() if x][:100], "head_tags": tags.splitlines()[:30],
        "stash_count": len([x for x in stashes.splitlines() if x]), "stash_preview": stashes.splitlines()[:10],
        "submodules": submodules.splitlines()[:100], "worktrees": worktrees.splitlines()[:200],
        "object_stats": object_stats.splitlines(), "diff_stat": diff_stat.splitlines()[-20:],
        "staged_diff_stat": staged_stat.splitlines()[-20:], "untracked_preview": untracked_names[:100],
        "tracked_file_count": tracked_count, "git_lfs_files": len([x for x in lfs.splitlines() if x]),
        "tree": tree, "survey_seconds": round(time.time()-t0, 3),
    }
    rec["priority_score"] = repo_score(rec)
    return rec


def tool_versions() -> dict[str, Any]:
    out: dict[str, Any] = {}
    version_args = {"git":["--version"], "gh":["--version"], "git-lfs":["--version"], "python":["--version"],
                    "python3":["--version"], "node":["--version"], "godot":["--version"], "godot4":["--version"],
                    "blender":["--version"], "ffmpeg":["-version"], "ffprobe":["-version"]}
    for name in TOOL_NAMES:
        exe = shutil.which(name)
        if not exe: continue
        code, text = run([exe, *version_args[name]], timeout=4)
        out[name] = {"path": exe, "version": (text.splitlines()[0] if text else "")[:200], "ok": code == 0}
    return out


def environment() -> dict[str, Any]:
    du = shutil.disk_usage(Path.home())
    return {
        "machine": socket.gethostname(), "platform": platform.platform(), "system": platform.system(),
        "release": platform.release(), "machine_arch": platform.machine(), "python": sys.version.split()[0],
        "cpu_count": os.cpu_count(), "home": str(Path.home()), "cwd": str(Path.cwd()),
        "disk_home": {"total": du.total, "used": du.used, "free": du.free}, "tools": tool_versions(),
    }


def group_duplicates(repos: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in repos:
        key = r.get("remote_key") or ("head:" + r.get("head", "")) or ("path:" + r["path"])
        groups[key].append(r)
    out = []
    for key, members in groups.items():
        if len(members) < 2: continue
        ordered = sorted(members, key=lambda r: r.get("priority_score",0), reverse=True)
        out.append({"identity": key, "copies": [{"machine": r.get("machine"), "path": r["path"], "head": r.get("head"),
                     "status": r.get("status"), "priority_score": r.get("priority_score")} for r in ordered],
                    "preferred_first": ordered[0]["path"],
                    "rule": "preserve unique dirty/ahead evidence; dedupe identical committed state"})
    return sorted(out, key=lambda g: g["identity"])


def write_outputs(out_dir: Path, payload: dict[str, Any]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir/"survey.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    with (out_dir/"repos.jsonl").open("w", encoding="utf-8") as f:
        for r in payload["repos"]: f.write(json.dumps(r, ensure_ascii=False)+"\n")
    receipt = {"kind":"thunder-run-one-survey", "created_at":payload["created_at"], "machine":payload["environment"]["machine"],
               "repo_count":len(payload["repos"]), "duplicate_groups":len(payload["duplicates"]),
               "sha256":hashlib.sha256((out_dir/"survey.json").read_bytes()).hexdigest()}
    (out_dir/"receipt.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")


def cmd_scan(args: argparse.Namespace) -> int:
    roots = [Path(r) for r in args.root]
    env = environment(); machine = args.machine or env["machine"]
    repos = sorted({p for root in roots for p in discover_repos(root, args.max_depth)}, key=lambda p: str(p).lower())
    workers = args.workers or min(32, max(4, (os.cpu_count() or 4)*4))
    results: list[dict[str, Any]] = []
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(survey_repo, repo, args.max_files_per_repo, args.fetch_remotes): repo for repo in repos}
        for fut in cf.as_completed(futs):
            repo = futs[fut]
            try:
                rec = fut.result(); rec["machine"] = machine; results.append(rec)
                if not args.quiet:
                    s=rec["status"]; print(f"[{machine}] {repo.name}: dirty={s['dirty']} +{s['ahead']}/-{s['behind']} score={rec['priority_score']}")
            except Exception as e:
                results.append({"machine":machine,"path":str(repo),"error":repr(e),"priority_score":-1})
    results.sort(key=lambda r: (-r.get("priority_score",-1), r.get("path","")))
    payload = {"schema":"thunder.turbo-survey.v1", "created_at":utcnow(), "environment":env,
               "machine_label":machine, "roots":[str(r) for r in roots], "workers":workers,
               "fetch_remotes":args.fetch_remotes, "repos":results, "duplicates":group_duplicates(results)}
    write_outputs(Path(args.out), payload)
    print(json.dumps({"machine":machine,"repos":len(results),"duplicates":len(payload["duplicates"]),"out":str(Path(args.out)/"survey.json")}))
    return 0


def cmd_merge(args: argparse.Namespace) -> int:
    surveys = [json.loads(Path(p).read_text(encoding="utf-8")) for p in args.survey]
    repos = [r for s in surveys for r in s.get("repos",[])]
    repos.sort(key=lambda r: (-r.get("priority_score",-1), r.get("machine",""), r.get("path","")))
    machines = [{"machine_label":s.get("machine_label"), "environment":s.get("environment"), "roots":s.get("roots")} for s in surveys]
    payload = {"schema":"thunder.turbo-survey-merge.v1", "created_at":utcnow(), "machines":machines,
               "repos":repos, "duplicates":group_duplicates(repos)}
    out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    (out/"kingdom_survey.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    with (out/"excavation_queue.jsonl").open("w",encoding="utf-8") as f:
        for r in repos: f.write(json.dumps({"machine":r.get("machine"),"path":r.get("path"),"remote":r.get("remote"),
            "head":r.get("head"),"status":r.get("status"),"priority_score":r.get("priority_score"),
            "technology_hints":r.get("tree",{}).get("technology_hints",[]),"filename_tags":r.get("tree",{}).get("filename_tags",{})},ensure_ascii=False)+"\n")
    receipt={"kind":"thunder-kingdom-survey","created_at":payload["created_at"],"machines":len(machines),"repos":len(repos),
             "duplicate_groups":len(payload["duplicates"]),"sha256":hashlib.sha256((out/"kingdom_survey.json").read_bytes()).hexdigest()}
    (out/"receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(receipt))
    return 0


def main() -> int:
    ap=argparse.ArgumentParser(description="Thunder Run-One turbo local archaeology survey")
    sub=ap.add_subparsers(dest="cmd",required=True)
    sp=sub.add_parser("scan"); sp.add_argument("--root",action="append",required=True); sp.add_argument("--out",required=True)
    sp.add_argument("--machine",default=""); sp.add_argument("--workers",type=int,default=0)
    sp.add_argument("--max-depth",type=int,default=8); sp.add_argument("--max-files-per-repo",type=int,default=25000)
    sp.add_argument("--fetch-remotes",action="store_true",help="network read + local remote-ref update; off by default")
    sp.add_argument("--quiet",action="store_true"); sp.set_defaults(func=cmd_scan)
    mp=sub.add_parser("merge"); mp.add_argument("survey",nargs="+"); mp.add_argument("--out",required=True); mp.set_defaults(func=cmd_merge)
    args=ap.parse_args(); return args.func(args)

if __name__=="__main__": raise SystemExit(main())
