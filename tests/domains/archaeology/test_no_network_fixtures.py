"""No-network proof for the Archaeology EvidenceBundle fixture projection.

The tests start fresh Python interpreters with the reviewed CI ``sitecustomize``
path. They prove that the local synthetic fixture validation succeeds while the
guard is active and that a representative network connection is denied before
egress. They do not establish runner-wide or non-Python isolation.
"""

from __future__ import annotations

import os
import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
GUARD_ROOT = REPO_ROOT / "tools/ci/kfm_no_network"
VALIDATOR = "tools/validators/validate_archaeology_evidence_bundle_projection.py"
DENIAL_MESSAGE = "KFM no-network guard denied Python network egress"


def _guarded_python(source: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["KFM_NO_NETWORK"] = "1"
    python_path = [str(GUARD_ROOT), str(REPO_ROOT)]
    if env.get("PYTHONPATH"):
        python_path.append(env["PYTHONPATH"])
    env["PYTHONPATH"] = os.pathsep.join(python_path)
    return subprocess.run(
        [sys.executable, "-c", source],
        cwd=REPO_ROOT,
        env=env,
        check=False,
        capture_output=True,
        text=True,
        timeout=20,
    )


class ArchaeologyNoNetworkFixtureTests(unittest.TestCase):
    def test_projection_fixtures_validate_with_startup_guard_active(self) -> None:
        source = (
            "import runpy, sitecustomize, sys; "
            "assert sitecustomize.GUARD_ACTIVE; "
            f"sys.argv = [{VALIDATOR!r}, '--fixtures']; "
            f"runpy.run_path({VALIDATOR!r}, run_name='__main__')"
        )
        result = _guarded_python(source)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("EXPECTED_FAIL", result.stdout)

    def test_startup_guard_denies_network_probe(self) -> None:
        result = _guarded_python(
            "import sitecustomize, socket; "
            "assert sitecustomize.GUARD_ACTIVE; "
            "socket.socket().connect(('192.0.2.1', 443))"
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(DENIAL_MESSAGE, result.stderr)
        self.assertIn("socket.connect", result.stderr)


if __name__ == "__main__":
    unittest.main()
