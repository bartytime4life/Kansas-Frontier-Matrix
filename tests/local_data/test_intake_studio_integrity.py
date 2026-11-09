"""Original-byte identity must hold at reuse, download and export boundaries."""

import tempfile
import os
import json
import threading
import urllib.request
import urllib.error
import unittest
import shutil
from pathlib import Path
from unittest.mock import patch

from tests.local_data.test_intake_studio import fake_extract
from tools.local_data.intake_studio.intake_server import Store


class IntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.store = Store(self.temp.name, Path(self.temp.name) / "runtime")
        self.body = b"\x89PNG\r\n\x1a\nprivate synthetic integrity test"
        with patch(
            "tools.local_data.intake_studio.intake_server.subprocess.run",
            side_effect=fake_extract,
        ):
            self.record, _ = self.store.ingest("test.png", self.body)
        self.original = self.store.objects / self.record["sha256"] / "original"

    def test_duplicate_does_not_reuse_corrupt_original(self):
        self.original.write_bytes(b"corrupt")
        with self.assertRaisesRegex(ValueError, "integrity"):
            self.store.ingest("same-content.png", self.body)
        self.assertEqual(len(self.store.list()), 1)
        self.assertEqual(self.original.read_bytes(), b"corrupt")

    def test_download_refuses_corrupt_original(self):
        self.original.write_bytes(b"corrupt")
        with self.assertRaisesRegex(ValueError, "integrity"):
            self.store.original_bytes(self.record)

    def test_original_reader_preserves_exact_bytes(self):
        self.assertEqual(self.store.original_bytes(self.record), self.body)


class LauncherTests(unittest.TestCase):
    def test_source_fingerprint_tracks_workspace_qwen_and_desk_changes(self):
        from tools.local_data.intake_studio import intake_server

        with tempfile.TemporaryDirectory() as directory:
            local_data = Path(directory) / "local_data"
            shutil.copytree(intake_server.APP.parent, local_data,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            expected = intake_server.source_fingerprint()
            with patch.object(intake_server, "APP", local_data / "intake_studio"):
                self.assertEqual(intake_server.source_fingerprint(), expected)
                for relative in ("ai_acceptance.py", "text_sample.py", "grounded_review.py",
                                 "intake_studio/workspace.py", "intake_studio/handoff.py",
                                 "intake_desk/ai-review.js"):
                    with self.subTest(relative=relative):
                        path = local_data / relative
                        original = path.read_bytes()
                        path.write_bytes(original + b"\n")
                        self.assertNotEqual(intake_server.source_fingerprint(), expected)
                        path.write_bytes(original)

    def test_older_instance_is_preserved_and_cannot_be_mistaken_for_this_copy(self):
        from tools.local_data.intake_studio import launch_local

        for session in [
            {"app": "kfm-local-intake-studio"},
            {"app": "kfm-local-intake-studio", "sourceFingerprint": "different"},
        ]:
            with self.subTest(session=session), tempfile.TemporaryDirectory() as root:
                with (
                    patch.object(Path, "home", return_value=Path(root)),
                    patch.object(launch_local, "running", return_value=session),
                    patch.object(
                        launch_local, "source_fingerprint", return_value="expected"
                    ),
                    patch.object(launch_local.subprocess, "Popen") as spawn,
                ):
                    with self.assertRaisesRegex(SystemExit, "different or older"):
                        launch_local.main()
                    spawn.assert_not_called()
                    self.assertFalse(
                        (
                            Path(root) / ".local/state/kfm-intake-studio/server.pid"
                        ).exists()
                    )

    def test_matching_instance_can_be_reused_without_starting_another_process(self):
        from tools.local_data.intake_studio import launch_local

        with tempfile.TemporaryDirectory() as root:
            with (
                patch.object(Path, "home", return_value=Path(root)),
                patch.object(
                    launch_local,
                    "running",
                    return_value={"sourceFingerprint": "expected"},
                ),
                patch.object(
                    launch_local, "source_fingerprint", return_value="expected"
                ),
                patch.object(launch_local.subprocess, "Popen") as spawn,
                patch("sys.argv", ["launch_local.py", "--no-open"]),
                patch("builtins.print"),
            ):
                launch_local.main()
                spawn.assert_not_called()


@unittest.skipIf(
    os.environ.get("KFM_NO_NETWORK") == "1",
    "Loopback test runs separately from the no-network guard",
)
class IntegrityHTTPTests(unittest.TestCase):
    setUp = IntegrityTests.setUp

    def test_http_original_and_duplicate_corruption_are_rejected(self):
        from tools.local_data.intake_studio.intake_server import (
            Server,
            source_fingerprint,
        )

        server = Server(0, self.store)
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        try:
            with urllib.request.urlopen(server.origin + "/api/session") as response:
                session = json.load(response)
            self.assertEqual(session["sourceFingerprint"], source_fingerprint())
            self.original.write_bytes(b"corrupt")
            for path, body in [
                ("/api/files/" + self.record["id"] + "/original", None),
                ("/api/upload?name=duplicate.png", self.body),
                ("/api/files/" + self.record["id"] + "/export", None),
            ]:
                with self.subTest(path=path):
                    request = urllib.request.Request(
                        server.origin + path,
                        data=body,
                        headers={"X-KFM-Token": server.token},
                    )
                    with self.assertRaises(urllib.error.HTTPError) as caught:
                        urllib.request.urlopen(request)
                    try:
                        self.assertEqual(caught.exception.code, 400)
                        self.assertIn("integrity", json.load(caught.exception)["error"])
                    finally:
                        caught.exception.close()
            self.assertEqual(len(self.store.list()), 1)
        finally:
            server.shutdown()
            server.server_close()
            worker.join(timeout=5)
