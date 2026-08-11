"""Static, no-network checks for the bounded KFM Compose placeholder."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
COMPOSE_PATH = REPO_ROOT / "infra" / "compose" / "docker-compose.yml"


class ComposeStaticBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.text = COMPOSE_PATH.read_text(encoding="utf-8")
        self.compose_dir = COMPOSE_PATH.parent

    def test_build_context_and_dockerfiles_resolve(self):
        contexts = re.findall(r"^\s+context:\s*(\S+)\s*$", self.text, re.MULTILINE)
        dockerfiles = re.findall(r"^\s+dockerfile:\s*(\S+)\s*$", self.text, re.MULTILINE)
        self.assertEqual(contexts, ["..", ".."])
        self.assertEqual(
            dockerfiles,
            ["docker/Dockerfile.governed-api", "docker/Dockerfile.explorer-web"],
        )
        for context, dockerfile in zip(contexts, dockerfiles, strict=True):
            context_path = (self.compose_dir / context).resolve()
            dockerfile_path = context_path / dockerfile
            self.assertTrue(context_path.is_dir(), context_path)
            self.assertTrue(dockerfile_path.is_file(), dockerfile_path)
            dockerfile_text = dockerfile_path.read_text(encoding="utf-8")
            self.assertRegex(dockerfile_text, r"(?m)^FROM\s+\S+")
            self.assertRegex(dockerfile_text, r"(?m)^WORKDIR\s+\S+")

            users = re.findall(r"(?m)^USER\s+(\S+)\s*$", dockerfile_text)
            self.assertTrue(users, f"{dockerfile_path}: missing final USER")
            runtime_user = users[-1].split(":", maxsplit=1)[0]
            self.assertNotIn(
                runtime_user.lower(),
                {"0", "root"},
                f"{dockerfile_path}: final USER must be non-root",
            )

    def test_published_ports_are_loopback_only(self):
        port_specs = re.findall(r'ports:\s*\["([^"]+)"\]', self.text)
        self.assertEqual(len(port_specs), 2)
        for port_spec in port_specs:
            self.assertTrue(port_spec.startswith("127.0.0.1:"), port_spec)

    def test_placeholder_has_no_sensitive_mount_or_privileged_escape(self):
        forbidden = (
            "privileged:",
            "network_mode: host",
            "/var/run/docker.sock",
            "data/raw",
            "data/work",
            "data/quarantine",
            "data/proofs",
            "data/receipts",
            "release/",
            "secrets:",
        )
        lowered = self.text.lower()
        for token in forbidden:
            self.assertNotIn(token.lower(), lowered)


if __name__ == "__main__":
    unittest.main()
