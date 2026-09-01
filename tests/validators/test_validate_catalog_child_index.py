from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/catalog/validate_catalog_child_index.py"

SPEC = importlib.util.spec_from_file_location("catalog_child_index_under_test", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _readme(*lanes: str) -> str:
    rows = "\n".join(f"| `{lane}` | test posture |" for lane in lanes)
    return (
        "# catalog\n\n"
        "## Current bounded child-lane index\n\n"
        "| Child lane | Bounded posture |\n"
        "|---|---|\n"
        f"{rows}\n\n"
        "## Next section\n"
    )


class CatalogChildIndexDriftTests(unittest.TestCase):
    def test_current_repository_catalog_index_matches_direct_children(self) -> None:
        report = MODULE.validate_catalog_child_index(REPO_ROOT / "data/catalog")
        self.assertEqual(report["outcome"], "PASS", report)
        self.assertEqual(
            report["actual_children"],
            [
                "dcat/",
                "domain/",
                "domains/",
                "prov/",
                "settlements-infrastructure/",
                "stac/",
            ],
        )
        self.assertFalse(report["authority_created"])

    def test_missing_child_lane_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalog"
            root.mkdir()
            (root / "stac").mkdir()
            (root / "domain").mkdir()
            (root / "README.md").write_text(_readme("stac/"), encoding="utf-8")
            report = MODULE.validate_catalog_child_index(root)
            self.assertEqual(report["outcome"], "FAIL")
            self.assertEqual(report["missing_from_index"], ["domain/"])

    def test_stale_index_entry_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalog"
            root.mkdir()
            (root / "stac").mkdir()
            (root / "README.md").write_text(
                _readme("stac/", "removed-lane/"),
                encoding="utf-8",
            )
            report = MODULE.validate_catalog_child_index(root)
            self.assertEqual(report["outcome"], "FAIL")
            self.assertEqual(report["stale_index_entries"], ["removed-lane/"])

    def test_duplicate_index_entry_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalog"
            root.mkdir()
            (root / "stac").mkdir()
            (root / "README.md").write_text(
                _readme("stac/", "stac/"),
                encoding="utf-8",
            )
            report = MODULE.validate_catalog_child_index(root)
            self.assertEqual(report["outcome"], "FAIL")
            self.assertEqual(report["duplicate_entries"], ["stac/"])

    def test_cli_emits_deterministic_machine_readable_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalog"
            root.mkdir()
            (root / "stac").mkdir()
            (root / "README.md").write_text(_readme("stac/"), encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR_PATH), "--catalog-root", str(root)],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            report = json.loads(completed.stdout)
            self.assertEqual(report["profile"], MODULE.PROFILE)
            self.assertEqual(report["outcome"], "PASS")
            self.assertFalse(report["authority_created"])


if __name__ == "__main__":
    unittest.main()
