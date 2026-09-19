from __future__ import annotations

import argparse
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools import workspace_archaeology as wa


def git(*args: str, cwd: Path | None = None) -> None:
    subprocess.run(["git", *args], cwd=cwd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


class WorkspaceArchaeologyTests(unittest.TestCase):
    def test_default_index_is_repo_relative_not_cwd_relative(self) -> None:
        parser = argparse.ArgumentParser()
        wa.configure_parser(parser)
        args = parser.parse_args(["show", "pose-lab-v2-sprite-refinery"])
        self.assertEqual(Path(args.index), Path(wa.default_index_path()))
        self.assertTrue(str(args.index).endswith("generated/workspace/workspace_index.json"))

    def test_worktree_parser(self) -> None:
        rows = wa.parse_worktrees(
            "worktree /tmp/main\nHEAD abc123\nbranch refs/heads/main\n\n"
            "worktree /tmp/feature\nHEAD def456\ndetached\n\n"
        )
        self.assertEqual(rows[0]["worktree"], "/tmp/main")
        self.assertEqual(rows[0]["branch"], "refs/heads/main")
        self.assertTrue(rows[1]["detached"])

    def test_clean_branch_without_upstream_is_not_automatically_lost(self) -> None:
        repo = {
            "remote": "https://github.com/example/repo",
            "status": {"branch": "main", "upstream": "", "ahead": 0, "behind": 0, "dirty": False, "staged": 0, "modified": 0, "untracked": 0, "conflicted": 0},
            "branch_state": [{"name": "old-local-name", "upstream": "", "local_only": False, "ahead": 0}],
            "stash_count": 0,
            "runtime": {"active": False},
        }
        result = wa.recovery_state(repo)
        self.assertFalse(result["lost_candidate"])
        self.assertEqual(result["label"], "SYNCED_OR_UNVERIFIED")

    def test_tmux_runtime_maps_descendants_and_ports(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "project"
            (repo / "src").mkdir(parents=True)
            tmux = {
                "available": True,
                "sessions": ["project-dev"],
                "panes": [
                    {
                        "session": "project-dev",
                        "window": "0",
                        "pane": "0",
                        "pane_id": "%1",
                        "pane_pid": 100,
                        "cwd": str(repo / "src"),
                        "command": "python",
                        "title": "dev",
                    }
                ],
            }
            processes = {
                100: {"pid": 100, "ppid": 1, "args": "bash"},
                101: {"pid": 101, "ppid": 100, "args": "python -m http.server --port 8123"},
            }
            listeners = [{"port": 8123, "pids": [101], "raw": "LISTEN 0 5 127.0.0.1:8123 users:((python,pid=101,fd=3))"}]
            runtime = wa.runtime_for_repo(repo, tmux, processes, listeners)
            self.assertTrue(runtime["active"])
            self.assertEqual(runtime["tmux_sessions"], ["project-dev"])
            self.assertEqual(runtime["ports"], [8123])
            self.assertEqual(runtime["process_pids"], [100, 101])

    def test_scan_finds_unpushed_dirty_repo_handoff_and_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root = base / "workspace"
            root.mkdir()
            remote = base / "remote.git"
            git("init", "--bare", str(remote))
            repo = root / "project-one"
            git("clone", str(remote), str(repo))
            git("config", "user.name", "Thunder Test", cwd=repo)
            git("config", "user.email", "thunder@example.invalid", cwd=repo)

            (repo / "README.md").write_text("# Project One\n", encoding="utf-8")
            git("add", "README.md", cwd=repo)
            git("commit", "-m", "initial", cwd=repo)
            git("push", "-u", "origin", "HEAD", cwd=repo)

            docs = repo / "docs"
            docs.mkdir()
            (docs / "PROJECT_HANDOFF.md").write_text("# Project One Handoff\nResume the experiment.\n", encoding="utf-8")
            git("add", "docs/PROJECT_HANDOFF.md", cwd=repo)
            git("commit", "-m", "local handoff", cwd=repo)
            (repo / "scratch.txt").write_text("untracked local treasure\n", encoding="utf-8")

            payload = wa.build_index(
                [root],
                max_depth=4,
                max_files_per_repo=500,
                workers=2,
                fetch_remotes=False,
                include_runtime=False,
                machine="test-phone",
            )
            self.assertEqual(payload["summary"]["repo_count"], 1)
            item = payload["repos"][0]
            self.assertEqual(item["display_name"], "project-one")
            self.assertEqual(item["status"]["ahead"], 1)
            self.assertTrue(item["status"]["dirty"])
            self.assertTrue(any(x["path"] == "docs/PROJECT_HANDOFF.md" for x in item["handoffs"]))
            self.assertTrue(any(b["local_only"] for b in item["branch_state"]))
            self.assertTrue(item["recovery"]["lost_candidate"])
            self.assertIn("DIRTY_LOCAL_WORK", item["recovery"]["label"])

            out = base / "index"
            receipt = wa.write_index(out, payload)
            self.assertEqual(receipt["repo_count"], 1)
            loaded = wa.validate_index(out / "workspace_index.json")
            self.assertEqual(loaded["schema"], wa.SCHEMA)

            # Receipt validation must fail closed after index tampering.
            data = json.loads((out / "workspace_index.json").read_text(encoding="utf-8"))
            data["machine"] = "tampered"
            (out / "workspace_index.json").write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(SystemExit):
                wa.validate_index(out / "workspace_index.json")


if __name__ == "__main__":
    unittest.main()
