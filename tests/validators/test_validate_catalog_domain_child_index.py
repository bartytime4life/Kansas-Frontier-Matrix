from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = (
    REPO_ROOT / "tools/validators/catalog/validate_catalog_domain_child_index.py"
)

SPEC = importlib.util.spec_from_file_location(
    "catalog_domain_child_index_under_test",
    VALIDATOR_PATH,
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _readme(*lanes: str) -> str:
    rendered = "\n".join(
        f"| `{lane}` | PROPOSED | synthetic test lane |" for lane in lanes
    )
    return (
        "# domain catalog\n\n"
        "## Known child lanes\n\n"
        "This table is an index, not a completeness claim.\n\n"
        "| Child lane | Posture | Notes |\n"
        "|---|---|---|\n"
        f"{rendered}\n\n"
        "## Catalog requirements\n"
    )


class CatalogDomainChildIndexDriftTests(unittest.TestCase):
    def test_current_repository_domain_index_matches_direct_children(self) -> None:
        report = MODULE.validate_catalog_domain_child_index(
            REPO_ROOT / "data/catalog/domain"
        )
        self.assertEqual(report["outcome"], "PASS", report)
        self.assertEqual(
            report["actual_children"],
            [
                "agriculture/",
                "archaeology/",
                "atmosphere/",
                "fauna/",
                "flora/",
                "geology/",
                "habitat/",
                "hazards/",
                "hydrology/",
                "people-dna-land/",
                "people/",
                "roads-rail-trade/",
                "settlement/",
                "settlements-infrastructure/",
                "soil/",
            ],
        )
        self.assertEqual(
            report["indexed_children"],
            [
                "agriculture/",
                "archaeology/",
                "atmosphere/",
                "fauna/",
                "flora/",
                "geology/",
                "habitat/",
                "hazards/",
                "hydrology/",
                "people-dna-land/",
                "people/",
                "roads-rail-trade/",
                "settlements-infrastructure/",
                "settlement/",
                "soil/",
            ],
        )
        self.assertFalse(report["authority_created"])

    def test_missing_domain_lane_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "domain"
            root.mkdir()
            (root / "agriculture").mkdir()
            (root / "hydrology").mkdir()
            (root / "README.md").write_text(
                _readme("agriculture/"),
                encoding="utf-8",
            )
            report = MODULE.validate_catalog_domain_child_index(root)
            self.assertEqual(report["outcome"], "FAIL")
            self.assertEqual(report["missing_from_index"], ["hydrology/"])

    def test_stale_domain_index_entry_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "domain"
            root.mkdir()
            (root / "agriculture").mkdir()
            (root / "README.md").write_text(
                _readme("agriculture/", "removed-domain/"),
                encoding="utf-8",
            )
            report = MODULE.validate_catalog_domain_child_index(root)
            self.assertEqual(report["outcome"], "FAIL")
            self.assertEqual(report["stale_index_entries"], ["removed-domain/"])

    def test_duplicate_domain_index_entry_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "domain"
            root.mkdir()
            (root / "agriculture").mkdir()
            (root / "README.md").write_text(
                _readme("agriculture/", "agriculture/"),
                encoding="utf-8",
            )
            report = MODULE.validate_catalog_domain_child_index(root)
            self.assertEqual(report["outcome"], "FAIL")
            self.assertEqual(report["duplicate_entries"], ["agriculture/"])

    def test_missing_known_child_lanes_section_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "domain"
            root.mkdir()
            (root / "agriculture").mkdir()
            (root / "README.md").write_text("# domain catalog\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "missing section"):
                MODULE.validate_catalog_domain_child_index(root)

    def test_closing_hash_known_child_lanes_section_is_parseable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "domain"
            root.mkdir()
            (root / "agriculture").mkdir()
            readme = _readme("agriculture/").replace(
                "## Known child lanes",
                "## Known child lanes ##",
            )
            (root / "README.md").write_text(readme, encoding="utf-8")
            report = MODULE.validate_catalog_domain_child_index(root)
            self.assertEqual(report["outcome"], "PASS")

    def test_duplicate_closing_hash_known_child_lanes_section_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "domain"
            root.mkdir()
            (root / "agriculture").mkdir()
            duplicate = _readme("agriculture/").replace(
                "## Catalog requirements",
                "## Known child lanes ##\n\n## Catalog requirements",
            )
            (root / "README.md").write_text(duplicate, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate section"):
                MODULE.validate_catalog_domain_child_index(root)

    def test_cli_emits_deterministic_machine_readable_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "domain"
            root.mkdir()
            (root / "agriculture").mkdir()
            (root / "README.md").write_text(
                _readme("agriculture/"),
                encoding="utf-8",
            )
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR_PATH), "--domain-root", str(root)],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            report = json.loads(completed.stdout)
            self.assertEqual(report["profile"], MODULE.PROFILE)
            self.assertEqual(report["outcome"], "PASS")
            self.assertEqual(report["actual_children"], ["agriculture/"])
            self.assertEqual(report["indexed_children"], ["agriculture/"])
            self.assertFalse(report["authority_created"])


if __name__ == "__main__":
    unittest.main()
