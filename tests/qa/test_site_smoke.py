"""The local smoke runner must not test an unrelated listener or a failed start."""
import os
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


if __name__ == "__main__":
    unittest.main()
