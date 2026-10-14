"""The local smoke runner must not test an unrelated listener or a failed start."""
import os
import json
import re
import shutil
import sqlite3
from pathlib import Path
import socket
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "apps/site/smoke-local.sh"


class SiteSmokeStartupTests(unittest.TestCase):
    def run_smoke(self, port):
        with tempfile.TemporaryDirectory(prefix="kfm-smoke-test-") as directory:
            root = Path(directory)
            # Never launch the real Site, migrations, or provider requests here.
            commands = {
                "setsid": 'printf started > "$SMOKE_TEST_MARKERS/started"\nexec /usr/bin/setsid /bin/sleep 20\n',
                "curl": 'printf requested >> "$SMOKE_TEST_MARKERS/requests"\nexit 1\n',
                "sleep": "exit 0\n",
            }
            for name, body in commands.items():
                target = root / name
                target.write_text("#!/bin/sh\n" + body)
                target.chmod(0o700)
            result = subprocess.run(
                ["bash", str(RUNNER)], cwd=ROOT, text=True, capture_output=True,
                timeout=15, env={**os.environ, "PATH": f"{root}:{os.environ['PATH']}",
                                 "SITE_PORT": str(port), "SMOKE_TEST_MARKERS": str(root)},
            )
            return result, (root / "started").exists(), (root / "requests").exists()

    def test_occupied_port_refused_before_launch_or_http(self):
        with socket.socket() as listener:
            listener.bind(("127.0.0.1", 0))
            listener.listen()
            result, launched, requested = self.run_smoke(listener.getsockname()[1])
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(launched)
        self.assertFalse(requested)
        self.assertIn("already in use", result.stderr)

    def test_invalid_port_refused_before_launch_or_http(self):
        result, launched, requested = self.run_smoke("4173/other")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(launched)
        self.assertFalse(requested)
        self.assertIn("SITE_PORT", result.stderr)

    def test_failed_readiness_never_runs_route_assertions(self):
        with socket.socket() as listener:
            listener.bind(("127.0.0.1", 0))
            port = listener.getsockname()[1]
        result, launched, requested = self.run_smoke(port)
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(launched)
        self.assertTrue(requested)
        self.assertIn("did not become ready", result.stderr)
        self.assertNotIn("wanted", result.stderr)
        self.assertNotIn("backend checks passed", result.stdout)


class SiteMigrationPreflightTests(unittest.TestCase):
    def preflight(self, mutate=None):
        script = (ROOT / "apps/site/serve-local.sh").read_text()
        code = re.search(r"additive_migrations=\"\$\(node -e '\n(.*?)\n}' \"\$migration_workspace\"\)\"", script, re.S).group(1) + "\n}"
        with tempfile.TemporaryDirectory(prefix="kfm-migration-test-") as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "apps/site/source/drizzle", root / "drizzle")
            work = root / "replay"; work.mkdir()
            if mutate: mutate(root)
            result = subprocess.run(["node", "-e", code, str(work)], cwd=root, text=True, capture_output=True, timeout=10)
            replay = (work / "0010_api_connections.sql").read_text() if (work / "0010_api_connections.sql").exists() else None
            return result, replay

    def test_verified_connection_replay_is_idempotent_without_changing_source(self):
        original = (ROOT / "apps/site/source/drizzle/0010_api_connections.sql").read_bytes()
        result, replay = self.preflight()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIsNotNone(replay)
        with sqlite3.connect(":memory:") as db:
            db.executescript("CREATE TABLE daily_archive_captures(id TEXT PRIMARY KEY);")
            db.executescript(replay); db.executescript(replay)
            self.assertEqual(db.execute("SELECT count(*) FROM api_connection_receipts").fetchone()[0], 0)
        self.assertEqual((ROOT / "apps/site/source/drizzle/0010_api_connections.sql").read_bytes(), original)

    def test_changed_published_connection_migration_is_refused(self):
        def mutate(root):
            path = root / "drizzle/0010_api_connections.sql"
            path.write_text(path.read_text() + "\n-- Unverified source change\n")
        result, replay = self.preflight(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("0010_api_connections changed", result.stderr)
        self.assertIsNone(replay)

    def test_unknown_nonadditive_migration_remains_refused(self):
        def mutate(root):
            path = root / "drizzle/meta/_journal.json"; journal = json.loads(path.read_text())
            journal["entries"].append({"idx": 11, "tag": "0011_synthetic_unsafe"})
            path.write_text(json.dumps(journal))
            (root / "drizzle/0011_synthetic_unsafe.sql").write_text("DROP TABLE api_connection_receipts;")
        result, _ = self.preflight(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("is not additive", result.stderr)


if __name__ == "__main__":
    unittest.main()
