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
    / "validate_layer_registry_discovery_index.py"
)

_SPEC = importlib.util.spec_from_file_location(
    "validate_layer_registry_discovery_index", VALIDATOR_PATH
)
assert _SPEC and _SPEC.loader
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)

validate_layer_registry_discovery_index = (
    _MODULE.validate_layer_registry_discovery_index
)


def _readme(*lanes: str) -> str:
    rows = "\n".join(
        f"| [`{lane}/`]({lane}/README.md) | CONFIRMED README | bounded |"
        for lane in lanes
    )
    return f"""# Layer Registry

## Confirmed child lanes

| Child lane | Status | Layer registry posture |
|---|---:|---|
{rows}

## Layer registry boundary
"""


class LayerRegistryDiscoveryIndexTests(unittest.TestCase):
    def _fixture(self, indexed: tuple[str, ...], actual: tuple[str, ...]):
        tempdir = tempfile.TemporaryDirectory()
        root = Path(tempdir.name) / "data" / "registry" / "layers"
        root.mkdir(parents=True)
        (root / "README.md").write_text(_readme(*indexed), encoding="utf-8")
        for lane in actual:
            child = root / lane
            child.mkdir()
            (child / "README.md").write_text(f"# {lane}\n", encoding="utf-8")
        return tempdir, root

    def test_current_parity_passes(self) -> None:
        tempdir, root = self._fixture(
            ("agriculture", "atmosphere", "flora", "habitat"),
            ("agriculture", "atmosphere", "flora", "habitat"),
        )
        self.addCleanup(tempdir.cleanup)
        report = validate_layer_registry_discovery_index(root)
        self.assertEqual("PASS", report["outcome"])
        self.assertFalse(report["authority_created"])
        self.assertEqual([], report["missing_from_index"])
        self.assertEqual([], report["stale_index_entries"])

    def test_unindexed_lane_fails_closed(self) -> None:
        tempdir, root = self._fixture(
            ("agriculture", "atmosphere"),
            ("agriculture", "atmosphere", "geology"),
        )
        self.addCleanup(tempdir.cleanup)
        report = validate_layer_registry_discovery_index(root)
        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(["geology/"], report["missing_from_index"])

    def test_stale_index_entry_fails_closed(self) -> None:
        tempdir, root = self._fixture(
            ("agriculture", "atmosphere", "flora"),
            ("agriculture", "atmosphere"),
        )
        self.addCleanup(tempdir.cleanup)
        report = validate_layer_registry_discovery_index(root)
        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(["flora/"], report["stale_index_entries"])

    def test_duplicate_index_entry_fails_closed(self) -> None:
        tempdir, root = self._fixture(
            ("agriculture", "atmosphere", "atmosphere"),
            ("agriculture", "atmosphere"),
        )
        self.addCleanup(tempdir.cleanup)
        report = validate_layer_registry_discovery_index(root)
        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(["atmosphere/"], report["duplicate_entries"])

    def test_mismatched_link_destination_fails_closed(self) -> None:
        tempdir, root = self._fixture(("agriculture",), ("agriculture",))
        self.addCleanup(tempdir.cleanup)
        (root / "README.md").write_text(
            _readme("agriculture").replace(
                "agriculture/README.md", "missing/README.md"
            ),
            encoding="utf-8",
        )

        report = validate_layer_registry_discovery_index(root)

        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(1, len(report["invalid_link_rows"]))

    def test_missing_child_readme_fails_closed(self) -> None:
        tempdir, root = self._fixture(("agriculture",), ("agriculture",))
        self.addCleanup(tempdir.cleanup)
        (root / "agriculture" / "README.md").unlink()

        report = validate_layer_registry_discovery_index(root)

        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(["agriculture/"], report["missing_child_readmes"])
        self.assertEqual([], report["missing_from_index"])
        self.assertEqual([], report["stale_index_entries"])

    def test_missing_section_errors(self) -> None:
        tempdir, root = self._fixture(("agriculture",), ("agriculture",))
        self.addCleanup(tempdir.cleanup)
        (root / "README.md").write_text("# Layer Registry\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "missing section"):
            validate_layer_registry_discovery_index(root)

    def test_duplicate_section_errors(self) -> None:
        tempdir, root = self._fixture(("agriculture",), ("agriculture",))
        self.addCleanup(tempdir.cleanup)
        duplicate = _readme("agriculture").replace(
            "## Layer registry boundary",
            "## Confirmed child lanes\n\n## Layer registry boundary",
        )
        (root / "README.md").write_text(duplicate, encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "duplicate section"):
            validate_layer_registry_discovery_index(root)

    def test_cli_output_is_deterministic_json(self) -> None:
        tempdir, root = self._fixture(
            ("agriculture", "atmosphere"),
            ("agriculture", "atmosphere"),
        )
        self.addCleanup(tempdir.cleanup)
        first = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--registry-root", str(root)],
            check=False,
            capture_output=True,
            text=True,
        )
        second = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--registry-root", str(root)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, first.returncode)
        self.assertEqual(first.stdout, second.stdout)
        parsed = json.loads(first.stdout)
        self.assertEqual(
            "kfm.layer-registry-discovery-index-drift.v4", parsed["profile"]
        )
        self.assertEqual("PASS", parsed["outcome"])


if __name__ == "__main__":
    unittest.main()
