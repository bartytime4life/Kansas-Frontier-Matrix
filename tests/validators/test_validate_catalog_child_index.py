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


def _readme(*rows: tuple[str, str]) -> str:
    rendered = "\n".join(f"| `{lane}` | {posture} |" for lane, posture in rows)
    return (
        "# catalog\n\n"
        "## Current bounded child-lane index\n\n"
        "| Child lane | Bounded posture |\n"
        "|---|---|\n"
        f"{rendered}\n\n"
        "## Next section\n"
    )


def _write_alias_readme(alias_dir: Path, target: str) -> None:
    alias_dir.mkdir(parents=True, exist_ok=True)
    (alias_dir / "README.md").write_text(
        f"# compatibility alias\n\nGoverning lane: `data/catalog/{target}`\n",
        encoding="utf-8",
    )


class CatalogChildIndexDriftTests(unittest.TestCase):
    def test_current_repository_catalog_index_matches_direct_children_and_aliases(self) -> None:
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
        self.assertEqual(
            report["compatibility_aliases"],
            [
                {"alias": "domains/", "canonical_target": "domain/"},
                {
                    "alias": "settlements-infrastructure/",
                    "canonical_target": "domain/settlements-infrastructure/",
                },
            ],
        )
        self.assertFalse(report["authority_created"])

    def test_missing_child_lane_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalog"
            root.mkdir()
            (root / "stac").mkdir()
            (root / "domain").mkdir()
            (root / "README.md").write_text(
                _readme(("stac/", "test posture")),
                encoding="utf-8",
            )
            report = MODULE.validate_catalog_child_index(root)
            self.assertEqual(report["outcome"], "FAIL")
            self.assertEqual(report["missing_from_index"], ["domain/"])

    def test_stale_index_entry_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalog"
            root.mkdir()
            (root / "stac").mkdir()
            (root / "README.md").write_text(
                _readme(
                    ("stac/", "test posture"),
                    ("removed-lane/", "test posture"),
                ),
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
                _readme(
                    ("stac/", "test posture"),
                    ("stac/", "duplicate posture"),
                ),
                encoding="utf-8",
            )
            report = MODULE.validate_catalog_child_index(root)
            self.assertEqual(report["outcome"], "FAIL")
            self.assertEqual(report["duplicate_entries"], ["stac/"])

    def test_missing_alias_target_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalog"
            root.mkdir()
            _write_alias_readme(root / "legacy", "canonical/")
            (root / "README.md").write_text(
                _readme(
                    (
                        "legacy/",
                        "`PROPOSED / COMPATIBILITY-ALIAS` to `canonical/`",
                    ),
                ),
                encoding="utf-8",
            )
            report = MODULE.validate_catalog_child_index(root)
            self.assertEqual(report["outcome"], "FAIL")
            self.assertEqual(
                report["missing_alias_targets"],
                ["legacy/ -> canonical/"],
            )

    def test_missing_alias_readme_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalog"
            root.mkdir()
            (root / "canonical").mkdir()
            (root / "legacy").mkdir()
            (root / "README.md").write_text(
                _readme(
                    ("canonical/", "governing"),
                    (
                        "legacy/",
                        "`PROPOSED / COMPATIBILITY-ALIAS` to `canonical/`",
                    ),
                ),
                encoding="utf-8",
            )
            report = MODULE.validate_catalog_child_index(root)
            self.assertEqual(report["outcome"], "FAIL")
            self.assertEqual(report["missing_alias_readmes"], ["legacy/"])

    def test_alias_readme_target_mismatch_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalog"
            root.mkdir()
            (root / "canonical").mkdir()
            _write_alias_readme(root / "legacy", "wrong/")
            (root / "README.md").write_text(
                _readme(
                    ("canonical/", "governing"),
                    (
                        "legacy/",
                        "`PROPOSED / COMPATIBILITY-ALIAS` to `canonical/`",
                    ),
                ),
                encoding="utf-8",
            )
            report = MODULE.validate_catalog_child_index(root)
            self.assertEqual(report["outcome"], "FAIL")
            self.assertEqual(
                report["alias_target_not_documented"],
                ["legacy/ -> canonical/"],
            )

    def test_malformed_alias_mapping_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalog"
            root.mkdir()
            (root / "legacy").mkdir()
            (root / "README.md").write_text(
                _readme(
                    ("legacy/", "`PROPOSED / COMPATIBILITY-ALIAS`"),
                ),
                encoding="utf-8",
            )
            report = MODULE.validate_catalog_child_index(root)
            self.assertEqual(report["outcome"], "FAIL")
            self.assertEqual(report["invalid_alias_entries"], ["legacy/"])

    def test_alias_chain_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalog"
            root.mkdir()
            (root / "canonical").mkdir()
            _write_alias_readme(root / "legacy-a", "legacy-b/")
            _write_alias_readme(root / "legacy-b", "canonical/")
            (root / "README.md").write_text(
                _readme(
                    ("canonical/", "governing"),
                    (
                        "legacy-a/",
                        "`PROPOSED / COMPATIBILITY-ALIAS` to `legacy-b/`",
                    ),
                    (
                        "legacy-b/",
                        "`PROPOSED / COMPATIBILITY-ALIAS` to `canonical/`",
                    ),
                ),
                encoding="utf-8",
            )
            report = MODULE.validate_catalog_child_index(root)
            self.assertEqual(report["outcome"], "FAIL")
            self.assertEqual(
                report["alias_targets_are_aliases"],
                ["legacy-a/ -> legacy-b/"],
            )

    def test_cli_emits_deterministic_machine_readable_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "catalog"
            root.mkdir()
            (root / "stac").mkdir()
            (root / "README.md").write_text(
                _readme(("stac/", "test posture")),
                encoding="utf-8",
            )
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
            self.assertEqual(report["compatibility_aliases"], [])
            self.assertFalse(report["authority_created"])


if __name__ == "__main__":
    unittest.main()
