#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import claude_code_review as review
import capture_pr_review_fixture as fixture


class ClaudeCodeReviewTests(unittest.TestCase):
    def test_parse_pr_target(self) -> None:
        parsed = review.parse_pr_target("Valar05/example#42")
        self.assertEqual((parsed.owner, parsed.repo, parsed.number), ("Valar05", "example", 42))
        parsed = review.parse_pr_target("https://github.com/Valar05/example/pull/7")
        self.assertEqual((parsed.owner, parsed.repo, parsed.number), ("Valar05", "example", 7))

    def test_changed_line_map(self) -> None:
        diff = """diff --git a/src/app.py b/src/app.py
--- a/src/app.py
+++ b/src/app.py
@@ -1,3 +1,4 @@
 keep
-old
+new
+added
"""
        changed = review.changed_line_map(diff)
        self.assertIn(("src/app.py", 2, "LEFT"), changed)
        self.assertIn(("src/app.py", 2, "RIGHT"), changed)
        self.assertIn(("src/app.py", 3, "RIGHT"), changed)

    def test_verify_findings_rejects_unmapped(self) -> None:
        state = review.ReadState(
            files=[{"filename": "src/app.py"}],
            diff="""diff --git a/src/app.py b/src/app.py
--- a/src/app.py
+++ b/src/app.py
@@ -1,2 +1,2 @@
-old
+new
""",
        )
        payload = {
            "summary": "x",
            "perspectives_used": ["Quartermaster"],
            "findings": [
                {"severity": "high", "path": "src/app.py", "line": 1, "side": "RIGHT", "issue": "bug", "impact": "bad", "evidence": "new", "recommendation": "fix", "confidence": "high"},
                {"severity": "high", "path": "src/app.py", "line": 10, "side": "RIGHT", "issue": "no", "impact": "bad", "evidence": "x", "recommendation": "fix", "confidence": "high"},
            ],
            "test_gaps": [],
            "non_postable_concerns": [],
        }
        verified, rejected = review.verify_findings(payload, state)
        self.assertEqual(len(verified), 1)
        self.assertEqual(len(rejected), 1)

    def test_fixture_helpers(self) -> None:
        owner, repo, number = fixture.parse_pr_target("https://github.com/Valar05/example/pull/9")
        self.assertEqual((owner, repo, number), ("Valar05", "example", 9))
        self.assertTrue(fixture.is_text_file("src/app.py"))
        self.assertFalse(fixture.is_text_file("assets/icon.png"))


    def test_pr_tool_outputs_are_clamped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            mock = base / "mock"
            mock.mkdir()
            long_patch = "+" + ("x" * (review.MAX_PR_FILE_PATCH_BYTES + 500))
            long_diff = "diff --git a/src/app.py b/src/app.py\n" + ("+line\n" * 20000)
            (mock / "pr_files.json").write_text(json.dumps([{"filename": "src/app.py", "status": "modified", "additions": 1, "deletions": 0, "changes": 1, "patch": long_patch}]), encoding="utf-8")
            (mock / "pr.diff").write_text(long_diff, encoding="utf-8")
            reader = review.GitHubReader(review.ReviewTarget("Valar05", "example", 1), mock)
            files = reader.list_pr_files()
            self.assertTrue(files[0]["patch_truncated"])
            self.assertLessEqual(len(files[0]["patch"].encode("utf-8")), review.MAX_PR_FILE_PATCH_BYTES + len("\n[TRUNCATED]"))
            state = review.ReadState()
            diff_result = review.dispatch_tool("get_pr_diff", {}, reader, state)
            self.assertTrue(diff_result["truncated"])
            self.assertLessEqual(len(diff_result["diff"].encode("utf-8")), review.MAX_PR_DIFF_BYTES + len("\n[TRUNCATED]"))

    def test_claude_5_requests_omit_temperature(self) -> None:
        captured = []
        original_urlopen = review.urllib.request.urlopen
        original_key = os.environ.get("ANTHROPIC_API_KEY")

        class FakeResponse:
            def __enter__(self):
                return self
            def __exit__(self, exc_type, exc, tb):
                return False
            def read(self):
                return json.dumps({"content": []}).encode("utf-8")

        def fake_urlopen(request, timeout=0):
            captured.append(json.loads(request.data.decode("utf-8")))
            return FakeResponse()

        try:
            os.environ["ANTHROPIC_API_KEY"] = "test-key"
            review.urllib.request.urlopen = fake_urlopen
            review.call_anthropic(model="claude-fable-5", system="s", tools=[], messages=[], max_tokens=10)
            review.call_anthropic(model="claude-sonnet-5", system="s", tools=[], messages=[], max_tokens=10)
            review.call_anthropic(model="claude-sonnet-4-6", system="s", tools=[], messages=[], max_tokens=10)
        finally:
            review.urllib.request.urlopen = original_urlopen
            if original_key is None:
                os.environ.pop("ANTHROPIC_API_KEY", None)
            else:
                os.environ["ANTHROPIC_API_KEY"] = original_key
        self.assertNotIn("temperature", captured[0])
        self.assertNotIn("temperature", captured[1])
        self.assertEqual(captured[2].get("temperature"), 0.1)


    def test_repeated_file_reads_are_compact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            mock = base / "mock"
            files = mock / "files" / "src"
            files.mkdir(parents=True)
            (files / "app.py").write_text("new\n", encoding="utf-8")
            reader = review.GitHubReader(review.ReviewTarget("Valar05", "example", 1), mock)
            state = review.ReadState()
            first = review.dispatch_tool("read_file_at_ref", {"path": "src/app.py", "ref": "head"}, reader, state)
            second = review.dispatch_tool("read_file_at_ref", {"path": "src/app.py", "ref": "head"}, reader, state)
            self.assertIn("content", first)
            self.assertTrue(second["already_read"])
            self.assertNotIn("content", second)

    def test_mock_dry_run_writes_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            mock = base / "mock"
            files = mock / "files" / "src"
            files.mkdir(parents=True)
            (mock / "pr_metadata.json").write_text(json.dumps({"number": 1, "title": "T", "state": "open", "html_url": "u", "base": {"ref": "main", "sha": "base"}, "head": {"ref": "branch", "sha": "head"}, "user": {"login": "u"}}), encoding="utf-8")
            (mock / "pr_files.json").write_text(json.dumps([{"filename": "src/app.py", "status": "modified", "additions": 1, "deletions": 1, "changes": 2, "patch": ""}]), encoding="utf-8")
            (mock / "pr.diff").write_text("diff --git a/src/app.py b/src/app.py\n--- a/src/app.py\n+++ b/src/app.py\n@@ -1 +1 @@\n-old\n+new\n", encoding="utf-8")
            (files / "app.py").write_text("new\n", encoding="utf-8")
            mock_review = base / "review.json"
            mock_review.write_text(json.dumps({"summary": "ok", "perspectives_used": ["Quartermaster"], "findings": [{"severity": "medium", "path": "src/app.py", "line": 1, "side": "RIGHT", "issue": "issue", "impact": "impact", "evidence": "new", "recommendation": "fix", "confidence": "high"}], "test_gaps": [], "non_postable_concerns": []}), encoding="utf-8")
            out = base / "out"
            import subprocess
            result = subprocess.check_output([sys.executable, str(ROOT / "tools" / "claude_code_review.py"), "--pr", "Valar05/example#1", "--mock-github", str(mock), "--mock-claude", str(mock_review), "--out-dir", str(out)], text=True)
            data = json.loads(result)
            self.assertEqual(data["verified_findings"], 1)
            self.assertTrue((out / "review_report.md").exists())
            self.assertTrue((out / "claude_raw.json").exists())


if __name__ == "__main__":
    unittest.main()
