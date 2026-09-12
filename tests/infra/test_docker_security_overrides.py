"""Static no-network checks for the Explorer review-image security overlays."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DOCKER_ROOT = REPO_ROOT / "infra" / "docker"
DOCKERFILE = DOCKER_ROOT / "Dockerfile.explorer-web"
MANIFEST = DOCKER_ROOT / "explorer-web" / "package.json"
LOCKFILE = DOCKER_ROOT / "explorer-web" / "package-lock.json"


class ExplorerImageSecurityOverrideTests(unittest.TestCase):
    def setUp(self) -> None:
        self.dockerfile = DOCKERFILE.read_text(encoding="utf-8")
        self.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.lock = json.loads(LOCKFILE.read_text(encoding="utf-8"))

    def test_manifest_pins_only_reviewed_runtime_overrides(self) -> None:
        self.assertEqual(
            self.manifest["dependencies"],
            {
                "brace-expansion": "5.0.9",
                "ip-address": "10.3.1",
                "tar": "7.5.22",
            },
        )

    def test_lock_binds_the_exact_tar_release_and_integrity(self) -> None:
        self.assertEqual(self.lock["lockfileVersion"], 3)
        self.assertEqual(
            self.lock["packages"][""]["dependencies"],
            self.manifest["dependencies"],
        )
        tar = self.lock["packages"]["node_modules/tar"]
        self.assertEqual(tar["version"], "7.5.22")
        self.assertEqual(
            tar["integrity"],
            "sha512-MFO/QzvtAOmJbkhOaCTvbGcFN9L9b+JunIsDwaKljSOdcLMea3NJ1k9Usz/rjdfSXTq4dfzfeS7W4p4YOAAHeA==",
        )

    def test_tar_runtime_dependencies_are_integrity_locked(self) -> None:
        packages = self.lock["packages"]
        for path in (
            "node_modules/@isaacs/fs-minipass",
            "node_modules/chownr",
            "node_modules/minipass",
            "node_modules/minizlib",
            "node_modules/yallist",
        ):
            self.assertIn(path, packages)
            self.assertRegex(packages[path]["integrity"], r"^sha512-")

    def test_dockerfile_replaces_and_asserts_the_bundled_tar(self) -> None:
        npm_tarball = (
            "ADD --checksum=sha256:31e9770f7dc71119a58509353b27917557aaf0ac9b5ef1a0465ee7d8ec67ae75"
        )
        self.assertIn(npm_tarball, self.dockerfile)
        self.assertIn(
            "/usr/local/lib/node_modules/npm/node_modules/tar;",
            self.dockerfile,
        )
        self.assertIn(
            "/tmp/npm-overrides/node_modules/tar \\",
            self.dockerfile,
        )
        for dependency, version in (
            ("tar", "7.5.22"),
            ("@isaacs/fs-minipass", "4.0.1"),
            ("chownr", "3.0.0"),
            ("minipass", "7.1.3"),
            ("minizlib", "3.1.0"),
            ("yallist", "5.0.0"),
        ):
            self.assertIn(
                f'"{dependency}":"{version}"',
                self.dockerfile,
            )
        self.assertIn(
            'typeof require(r+"/tar").extract!=="function"',
            self.dockerfile,
        )


    def test_review_images_refresh_and_assert_current_os_security_floors(self) -> None:
        expected_floors = {
            "libblkid1": "2.41.5-0+deb13u1",
            "libssl3t64": "3.5.7-1~deb13u2",
            "gzip": "1.13-1+deb13u1",
            "libpcre2-8-0": "10.46-1~deb13u2",
            "libsqlite3-0": "3.46.1-7+deb13u2",
            "perl-base": "5.40.1-6+deb13u1",
        }
        for dockerfile in (DOCKERFILE, DOCKER_ROOT / "Dockerfile.governed-api"):
            text = dockerfile.read_text(encoding="utf-8")
            self.assertIn(
                "apt-get install --yes --no-install-recommends --only-upgrade",
                text,
            )
            for package, version in expected_floors.items():
                self.assertIn(f"        {package}", text)
                self.assertIn(
                    f"$(dpkg-query --show --showformat='${{Version}}' {package})",
                    text,
                )
                self.assertIn(f'"{version}"', text)

if __name__ == "__main__":
    unittest.main()
