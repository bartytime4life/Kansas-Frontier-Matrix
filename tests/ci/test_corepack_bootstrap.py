"""Exercise the workflow's real npm integrity boundary without registry access."""
from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path
import re
import shlex
import subprocess
import tarfile
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
BOOTSTRAP = ROOT / "tools/ci/corepack"
WORKFLOW = ROOT / ".github/workflows/maplibre-package-compatibility.yml"


class CorepackBootstrapTests(unittest.TestCase):
    def install_arguments(self, project: Path, cache: Path) -> list[str]:
        commands = re.findall(r"^\s*npm ci[^\n]*$", WORKFLOW.read_text(), re.MULTILINE)
        self.assertEqual(len(commands), 1, "use one locked bootstrap installation")
        args = shlex.split(commands[0])
        prefix = args.index("--prefix")
        self.assertEqual(args[prefix + 1], "tools/ci/corepack")
        self.assertIn("--ignore-scripts", args, "do not run package lifecycle hooks")
        args[prefix + 1] = str(project)
        return [*args, "--offline", "--cache", str(cache)]

    def fixture(self):
        temporary = tempfile.TemporaryDirectory(prefix="kfm-corepack-integrity-")
        self.addCleanup(temporary.cleanup)
        directory = Path(temporary.name)
        package = directory / "package"
        (package / "dist").mkdir(parents=True)
        marker = directory / "lifecycle-executed"
        (package / "package.json").write_text(json.dumps({
            "name": "corepack",
            "version": "0.34.0",
            "bin": {"corepack": "dist/corepack.js"},
            "scripts": {"postinstall": "node postinstall.cjs"},
        }))
        (package / "dist/corepack.js").write_text('#!/usr/bin/env node\nconsole.log("0.34.0");\n')
        (package / "postinstall.cjs").write_text(
            "require('node:fs').writeFileSync(" + json.dumps(str(marker)) + ", 'ran');"
        )
        archive = directory / "corepack.tgz"

        def pack():
            with tarfile.open(archive, "w:gz") as output:
                output.add(package, arcname="package")

        pack()
        project = directory / "bootstrap"
        project.mkdir()
        dependency = archive.as_uri()
        manifest = json.loads((BOOTSTRAP / "package.json").read_text())
        lock = json.loads((BOOTSTRAP / "package-lock.json").read_text())
        manifest["dependencies"]["corepack"] = dependency
        lock["packages"][""]["dependencies"]["corepack"] = dependency
        entry = lock["packages"]["node_modules/corepack"]
        entry["resolved"] = dependency
        entry["integrity"] = "sha256-" + base64.b64encode(hashlib.sha256(archive.read_bytes()).digest()).decode()
        (project / "package.json").write_text(json.dumps(manifest))
        (project / "package-lock.json").write_text(json.dumps(lock))

        def install():
            return subprocess.run(
                self.install_arguments(project, directory / "empty-cache"),
                cwd=directory, text=True, capture_output=True, timeout=30,
            )

        return directory, package, archive, marker, project, pack, install

    def test_complete_graph_uses_the_official_release_digest(self):
        manifest = json.loads((BOOTSTRAP / "package.json").read_text())
        lock = json.loads((BOOTSTRAP / "package-lock.json").read_text())
        url = "https://github.com/nodejs/corepack/releases/download/v0.34.0/corepack.tgz"
        self.assertIs(manifest["private"], True)
        self.assertEqual(manifest["dependencies"], {"corepack": url})
        self.assertEqual(set(lock["packages"]), {"", "node_modules/corepack"})
        self.assertEqual(lock["packages"][""]["dependencies"], manifest["dependencies"])
        entry = lock["packages"]["node_modules/corepack"]
        self.assertEqual(entry["version"], "0.34.0")
        self.assertEqual(entry["resolved"], url)
        # https://api.github.com/repos/nodejs/corepack/releases/assets/274407268
        digest = "0c85699ec30b495273df7f8391235135d9aa43297265f03cf8c8005a17fa693f"
        self.assertEqual(entry["integrity"], "sha256-" + base64.b64encode(bytes.fromhex(digest)).decode())
        self.assertNotIn("dependencies", entry, "bundled Corepack has no unlocked transitive graph")

    def test_valid_bytes_install_without_running_lifecycle_scripts(self):
        _, _, _, marker, project, _, install = self.fixture()
        result = install()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse(marker.exists())
        result = subprocess.run(
            ["node", str(project / "node_modules/corepack/dist/corepack.js")],
            text=True, capture_output=True, timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "0.34.0")

    def test_same_version_replacement_fails_integrity(self):
        _, package, _, marker, _, pack, install = self.fixture()
        (package / "dist/corepack.js").write_text('#!/usr/bin/env node\nconsole.log("replaced same-version bytes");\n')
        pack()
        result = install()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("EINTEGRITY", result.stdout + result.stderr)
        self.assertFalse(marker.exists())

    def test_truncated_archive_fails_closed(self):
        _, _, archive, marker, _, _, install = self.fixture()
        content = archive.read_bytes()
        archive.write_bytes(content[:len(content) // 2])
        result = install()
        self.assertNotEqual(result.returncode, 0)
        self.assertRegex(result.stdout + result.stderr, r"EINTEGRITY|TAR_BAD_ARCHIVE|Z_BUF_ERROR")
        self.assertFalse(marker.exists())


if __name__ == "__main__":
    unittest.main()
