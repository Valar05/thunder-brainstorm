#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import threading
import unittest
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("thunder_doc_server", ROOT / "tools" / "doc_server.py")
SERVER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(SERVER)


class FleshpunkGalleryTest(unittest.TestCase):
    def test_manifest_is_ordered_and_content_addressed(self):
        manifest = json.loads((ROOT / "generated/galleries/fleshpunk-maze/gallery.json").read_text())
        self.assertEqual(manifest["marker"], "THUNDER_FLESHPUNK_GALLERY_V1")
        self.assertEqual(manifest["stage_count"], 6)
        self.assertEqual([stage["stage"] for stage in manifest["stages"]], [1, 2, 3, 4, 5, 6])
        self.assertEqual(manifest["stages"][0]["verdict"], "QUARANTINED")
        self.assertEqual(manifest["stages"][4]["verdict"], "CURRENT_CHAMPION")
        for stage in manifest["stages"]:
            path = ROOT / stage["gallery_path"]
            self.assertTrue(path.is_file())
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), stage["gallery_sha256"])
            self.assertEqual(stage["gallery_sha256"], stage["source_sha256"])

    def test_gallery_slug_fails_closed(self):
        with self.assertRaises(ValueError):
            SERVER.gallery_page("../../outside")
        with self.assertRaises(FileNotFoundError):
            SERVER.gallery_page("does-not-exist")

    def test_real_http_route_serves_gallery_manifest_and_pixels(self):
        httpd = SERVER.ReuseTCPServer(("127.0.0.1", 0), SERVER.Handler)
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
        base = f"http://127.0.0.1:{httpd.server_address[1]}"
        try:
            with urllib.request.urlopen(base + "/gallery/fleshpunk-maze", timeout=5) as response:
                page = response.read().decode()
                self.assertEqual(response.status, 200)
                self.assertIn("THUNDER_FLESHPUNK_GALLERY_V1", page)
                self.assertIn("Drag from baseline to champion", page)
            with urllib.request.urlopen(base + "/raw/generated/galleries/fleshpunk-maze/gallery.json", timeout=5) as response:
                self.assertEqual(json.load(response)["stage_count"], 6)
            with urllib.request.urlopen(base + "/raw/generated/galleries/fleshpunk-maze/assets/05-clean-line-master.png", timeout=5) as response:
                self.assertEqual(response.read(8), b"\x89PNG\r\n\x1a\n")
        finally:
            httpd.shutdown()
            httpd.server_close()
            thread.join(timeout=5)


if __name__ == "__main__":
    unittest.main()
