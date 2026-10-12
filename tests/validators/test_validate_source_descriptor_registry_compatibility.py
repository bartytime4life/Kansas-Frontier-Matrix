from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

VALIDATOR_PATH = (
    Path(__file__).resolve().parents[2]
    / "tools"
    / "validators"
    / "catalog"
    / "validate_source_descriptor_registry_compatibility.py"
)

_SPEC = importlib.util.spec_from_file_location(
    "validate_source_descriptor_registry_compatibility", VALIDATOR_PATH
)
assert _SPEC and _SPEC.loader
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)

validate_source_descriptor_registry_compatibility = (
    _MODULE.validate_source_descriptor_registry_compatibility
)


def _compat_readme() -> str:
    return """<!-- [KFM_META_BLOCK_V2]
registry_scope: source-descriptor-compatibility-and-routing
path_posture: canonical-source-registry-parent-confirmed-at-data-registry-sources
[/KFM_META_BLOCK_V2] -->

# Source Descriptors Compatibility Lane

This path is a compatibility/routing lane.

The verified canonical source-registry parent is:

`data/registry/sources/`
"""


class SourceDescriptorRegistryCompatibilityTests(unittest.TestCase):
    def _fixture(self):
        tempdir = tempfile.TemporaryDirectory()
        repo = Path(tempdir.name)
        compatibility = repo / "data" / "registry" / "source_descriptors"
        canonical = repo / "data" / "registry" / "sources"
        compatibility.mkdir(parents=True)
        canonical.mkdir(parents=True)
        (compatibility / "README.md").write_text(_compat_readme(), encoding="utf-8")
        (canonical / "README.md").write_text("# Sources\n", encoding="utf-8")
        return tempdir, repo, compatibility, canonical

    def test_current_pointer_only_boundary_passes(self) -> None:
        tempdir, repo, _, _ = self._fixture()
        self.addCleanup(tempdir.cleanup)
        report = validate_source_descriptor_registry_compatibility(repo)
        self.assertEqual("PASS", report["outcome"])
        self.assertFalse(report["authority_created"])
        self.assertEqual([], report["findings"])

    def test_missing_canonical_target_fails_closed(self) -> None:
        tempdir, repo, _, canonical = self._fixture()
        self.addCleanup(tempdir.cleanup)
        for entry in canonical.iterdir():
            entry.unlink()
        canonical.rmdir()
        report = validate_source_descriptor_registry_compatibility(repo)
        self.assertEqual("FAIL", report["outcome"])
        self.assertIn("CANONICAL_SOURCE_REGISTRY_MISSING", report["findings"])

    def test_missing_compatibility_marker_fails_closed(self) -> None:
        tempdir, repo, compatibility, _ = self._fixture()
        self.addCleanup(tempdir.cleanup)
        readme = compatibility / "README.md"
        readme.write_text(
            _compat_readme().replace(
                "canonical-source-registry-parent-confirmed-at-data-registry-sources",
                "topology-needs-verification",
            ),
            encoding="utf-8",
        )
        report = validate_source_descriptor_registry_compatibility(repo)
        self.assertEqual("FAIL", report["outcome"])
        self.assertIn("COMPATIBILITY_MARKERS_MISSING", report["findings"])

    def test_non_markdown_payload_fails_closed(self) -> None:
        tempdir, repo, compatibility, _ = self._fixture()
        self.addCleanup(tempdir.cleanup)
        (compatibility / "duplicate.source.json").write_text("{}", encoding="utf-8")
        report = validate_source_descriptor_registry_compatibility(repo)
        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(["duplicate.source.json"], report["unexpected_entries"])

    def test_child_lane_fails_closed(self) -> None:
        tempdir, repo, compatibility, _ = self._fixture()
        self.addCleanup(tempdir.cleanup)
        (compatibility / "agriculture").mkdir()
        report = validate_source_descriptor_registry_compatibility(repo)
        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(["agriculture"], report["unexpected_entries"])

    def test_markdown_migration_note_remains_allowed(self) -> None:
        tempdir, repo, compatibility, _ = self._fixture()
        self.addCleanup(tempdir.cleanup)
        (compatibility / "MIGRATION.md").write_text("# Migration\n", encoding="utf-8")
        report = validate_source_descriptor_registry_compatibility(repo)
        self.assertEqual("PASS", report["outcome"])

    def test_cli_output_is_deterministic_json(self) -> None:
        tempdir, repo, _, _ = self._fixture()
        self.addCleanup(tempdir.cleanup)
        first = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--repo-root", str(repo)],
            check=False,
            capture_output=True,
            text=True,
        )
        second = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--repo-root", str(repo)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, first.returncode)
        self.assertEqual(first.stdout, second.stdout)
        parsed = json.loads(first.stdout)
        self.assertEqual(
            "kfm.source-descriptor-registry-compatibility.v1", parsed["profile"]
        )
        self.assertEqual("PASS", parsed["outcome"])


if __name__ == "__main__":
    unittest.main()
