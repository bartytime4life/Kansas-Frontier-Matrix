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
    / "validate_crosswalk_registry_inventory.py"
)

_SPEC = importlib.util.spec_from_file_location(
    "validate_crosswalk_registry_inventory", VALIDATOR_PATH
)
assert _SPEC and _SPEC.loader
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)

validate_crosswalk_registry_inventory = _MODULE.validate_crosswalk_registry_inventory


def _readme(*rows: tuple[str, str]) -> str:
    table_rows = "\n".join(
        f"| [`{label}`]({link}) | role | state |"
        for label, link in rows
    )
    return f"""# Crosswalk Registry

## Current inventory

At the pinned base, the tracked subtree inventory is:

| Tracked path | Role | Bounded state |
|---|---|---|
{table_rows}

## Repository fit
"""


class CrosswalkRegistryInventoryTests(unittest.TestCase):
    def _fixture(
        self,
        rows: tuple[tuple[str, str], ...],
        actual_paths: tuple[str, ...],
    ):
        tempdir = tempfile.TemporaryDirectory()
        repo = Path(tempdir.name)
        root = repo / "data" / "registry" / "crosswalks"
        root.mkdir(parents=True)
        (root / "README.md").write_text(_readme(*rows), encoding="utf-8")

        for relative in actual_paths:
            if relative == "README.md":
                continue
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("{}\n" if path.suffix == ".json" else "# lane\n", encoding="utf-8")
        return tempdir, repo

    def test_current_bounded_inventory_passes(self) -> None:
        paths = (
            "README.md",
            "water_planning/README.md",
            "water_planning/kwo_rac_counties_2026-06-24__tiger2025.json",
        )
        rows = tuple((path, path) for path in paths)
        tempdir, repo = self._fixture(rows, paths)
        self.addCleanup(tempdir.cleanup)

        report = validate_crosswalk_registry_inventory(repo)
        self.assertEqual("PASS", report["outcome"])
        self.assertFalse(report["authority_created"])
        self.assertEqual(["water_planning"], report["child_lanes"])

    def test_unindexed_new_record_fails_closed(self) -> None:
        rows = (
            ("README.md", "README.md"),
            ("water_planning/README.md", "water_planning/README.md"),
        )
        actual = (
            "README.md",
            "water_planning/README.md",
            "water_planning/new_mapping.json",
        )
        tempdir, repo = self._fixture(rows, actual)
        self.addCleanup(tempdir.cleanup)

        report = validate_crosswalk_registry_inventory(repo)
        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(
            ["water_planning/new_mapping.json"], report["unindexed_paths"]
        )

    def test_stale_inventory_row_fails_closed(self) -> None:
        rows = (
            ("README.md", "README.md"),
            ("water_planning/README.md", "water_planning/README.md"),
            ("water_planning/stale.json", "water_planning/stale.json"),
        )
        actual = ("README.md", "water_planning/README.md")
        tempdir, repo = self._fixture(rows, actual)
        self.addCleanup(tempdir.cleanup)

        report = validate_crosswalk_registry_inventory(repo)
        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(
            ["water_planning/stale.json"], report["stale_index_paths"]
        )

    def test_duplicate_inventory_row_fails_closed(self) -> None:
        rows = (
            ("README.md", "README.md"),
            ("water_planning/README.md", "water_planning/README.md"),
            ("water_planning/README.md", "water_planning/README.md"),
        )
        actual = ("README.md", "water_planning/README.md")
        tempdir, repo = self._fixture(rows, actual)
        self.addCleanup(tempdir.cleanup)

        report = validate_crosswalk_registry_inventory(repo)
        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(
            ["water_planning/README.md"], report["duplicate_index_paths"]
        )

    def test_label_link_mismatch_fails_closed(self) -> None:
        rows = (
            ("README.md", "README.md"),
            ("water_planning/WRONG.md", "water_planning/README.md"),
        )
        actual = ("README.md", "water_planning/README.md")
        tempdir, repo = self._fixture(rows, actual)
        self.addCleanup(tempdir.cleanup)

        report = validate_crosswalk_registry_inventory(repo)
        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(
            ["water_planning/WRONG.md!=water_planning/README.md"],
            report["label_link_mismatches"],
        )

    def test_malformed_inventory_row_fails_closed(self) -> None:
        paths = ("README.md", "water_planning/README.md")
        rows = tuple((path, path) for path in paths)
        tempdir, repo = self._fixture(rows, paths)
        self.addCleanup(tempdir.cleanup)
        readme = repo / "data" / "registry" / "crosswalks" / "README.md"
        readme.write_text(
            readme.read_text(encoding="utf-8").replace(
                "| [`water_planning/README.md`](water_planning/README.md) |",
                "| [`water_planning/README.md`](water_planning/README.md |",
            ),
            encoding="utf-8",
        )

        report = validate_crosswalk_registry_inventory(repo)

        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(1, len(report["invalid_inventory_rows"]))
        self.assertEqual(
            ["water_planning/README.md"], report["unindexed_paths"]
        )

    def test_child_lane_without_readme_fails_closed(self) -> None:
        rows = (
            ("README.md", "README.md"),
            ("water_planning/mapping.json", "water_planning/mapping.json"),
        )
        actual = ("README.md", "water_planning/mapping.json")
        tempdir, repo = self._fixture(rows, actual)
        self.addCleanup(tempdir.cleanup)

        report = validate_crosswalk_registry_inventory(repo)
        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(["water_planning"], report["missing_child_readmes"])

    def test_missing_inventory_section_errors(self) -> None:
        rows = (("README.md", "README.md"),)
        actual = ("README.md",)
        tempdir, repo = self._fixture(rows, actual)
        self.addCleanup(tempdir.cleanup)
        readme = repo / "data" / "registry" / "crosswalks" / "README.md"
        readme.write_text("# Crosswalk Registry\n", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "missing section marker"):
            validate_crosswalk_registry_inventory(repo)

    def test_duplicate_inventory_section_errors(self) -> None:
        rows = (("README.md", "README.md"),)
        actual = ("README.md",)
        tempdir, repo = self._fixture(rows, actual)
        self.addCleanup(tempdir.cleanup)
        readme = repo / "data" / "registry" / "crosswalks" / "README.md"
        readme.write_text(
            readme.read_text(encoding="utf-8")
            + "\n## Current inventory\n\n"
            + "| Tracked path | Role | Bounded state |\n"
            + "|---|---|---|\n"
            + "| [`README.md`](README.md) | role | state |\n",
            encoding="utf-8",
        )

        with self.assertRaisesRegex(ValueError, "duplicate section marker"):
            validate_crosswalk_registry_inventory(repo)

    def test_cli_output_is_deterministic_json(self) -> None:
        paths = (
            "README.md",
            "water_planning/README.md",
            "water_planning/kwo_rac_counties_2026-06-24__tiger2025.json",
        )
        rows = tuple((path, path) for path in paths)
        tempdir, repo = self._fixture(rows, paths)
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
        self.assertEqual("kfm.crosswalk-registry-inventory-drift.v2", parsed["profile"])
        self.assertEqual("PASS", parsed["outcome"])


if __name__ == "__main__":
    unittest.main()
