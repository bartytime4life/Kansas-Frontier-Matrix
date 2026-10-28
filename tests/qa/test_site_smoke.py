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
            idx = len(journal["entries"])
            tag = f"{idx:04d}_synthetic_unsafe"
            journal["entries"].append({"idx": idx, "tag": tag})
            path.write_text(json.dumps(journal))
            (root / f"drizzle/{tag}.sql").write_text("DROP TABLE api_connection_receipts;")
        result, _ = self.preflight(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("is not additive", result.stderr)


class SiteLocalLaunchBoundaryTests(unittest.TestCase):
    def launch(self, *, host="127.0.0.1", port="4173", version=None, secret_file=None):
        with tempfile.TemporaryDirectory(prefix="kfm-launch-test-") as directory:
            root = Path(directory)
            source = root / "source"
            scripts = source / "scripts"
            scripts.mkdir(parents=True)
            shutil.copy2(ROOT / "apps/site/serve-local.sh", root / "serve-local.sh")
            for name in ("serve-local-worker.mjs", "archive-access.mjs", "validate-subsurface-public.mjs", "validate-history-public.mjs"):
                shutil.copy2(ROOT / "apps/site/source/scripts" / name, scripts / name)
            if secret_file:
                (source / secret_file).write_text("PRIVATE_TEST_VALUE=synthetic-only")
            # No real Worker, database, private access file, or dependency tree.
            # Any Wrangler call (including migrations) is a preflight failure.
            wrangler = source / "node_modules/.bin/wrangler"
            wrangler.parent.mkdir(parents=True)
            wrangler.write_text('#!/bin/sh\nprintf called > "$LAUNCH_TEST_MARKER"\nprintf \'[{"results":[{"count":2}]}]\\n\'\nexit 89\n')
            wrangler.chmod(0o700)
            config = source / "dist/server/wrangler.json"
            config.parent.mkdir(parents=True)
            config.write_text("{}")
            binary = root / "bin"
            binary.mkdir()
            preload = root / "version.cjs"
            preload.write_text('Object.defineProperty(process.versions, "node", { value: process.env.LAUNCH_TEST_VERSION });')
            node = binary / "node"
            node.write_text('#!/bin/sh\nexec "$LAUNCH_TEST_NODE" --require "$LAUNCH_TEST_PRELOAD" "$@"\n')
            node.chmod(0o700)
            marker = root / "wrangler-called"
            env = {**os.environ, "SITE_HOST": host, "SITE_PORT": port,
                   "SITE_STATE_DIR": str(root / "state"), "LAUNCH_TEST_MARKER": str(marker)}
            if version:
                env.update(PATH=f"{binary}:{os.environ['PATH']}", LAUNCH_TEST_NODE=shutil.which("node"),
                           LAUNCH_TEST_PRELOAD=str(preload), LAUNCH_TEST_VERSION=version)
            result = subprocess.run(["bash", str(root / "serve-local.sh")], cwd=root,
                                    env=env, text=True, capture_output=True, timeout=10)
            return result, marker.exists(), (root / "state").exists()

    def test_former_fallbacks_refuse_before_storage_or_runtime(self):
        cases = [(dict(host=host), "SITE_HOST") for host in ("0.0.0.0", "localhost", "::1", "127.0.0.1.example")]
        cases += [(dict(port=port), "INVALID") for port in ("80", "0", "65536", "04173", "4173/other")]
        cases += [(dict(version=version), "REQUIRES_NODE_22_13_OR_LATER") for version in ("20.19.0", "22.12.0")]
        cases += [(dict(secret_file=name), "LOCAL_SECRET_CONFIGURATION_REQUIRES_REVIEW")
                  for name in (".env", ".env.local", ".env.production", ".dev.vars", ".dev.vars.local")]
        for options, reason in cases:
            with self.subTest(**options):
                result, called, state_created = self.launch(**options)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(reason, result.stderr)
                self.assertFalse(called, "refused configuration reached Wrangler")
                self.assertFalse(state_created, "refused configuration changed storage")

    def test_supported_ports_and_runtime_versions_reach_existing_migration_path(self):
        for options in ({}, dict(port="4175"), dict(port="65535"), dict(version="24.0.0")):
            with self.subTest(**options):
                result, called, state_created = self.launch(**options)
                self.assertEqual(result.returncode, 89, result.stderr)
                self.assertTrue(called)
                self.assertTrue(state_created)


if __name__ == "__main__":
    unittest.main()
