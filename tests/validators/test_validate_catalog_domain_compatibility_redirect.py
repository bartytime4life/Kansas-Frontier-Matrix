from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from tools.validators.catalog.validate_catalog_domain_compatibility_redirect import (
    main,
    validate_catalog_domain_compatibility_redirect,
)

SECTION = "## Current bounded inventory\n\nVerified domain redirect children:\n\n"


def _write_layout(
    root: Path,
    *,
    actual: list[str],
    indexed: list[str],
    canonical: list[str] | None = None,
    missing_readme: set[str] | None = None,
    row_overrides: dict[str, str] | None = None,
    readme_overrides: dict[str, str] | None = None,
) -> tuple[Path, Path]:
    compat = root / "catalog" / "domain"
    canonical_root = root / "data" / "catalog" / "domain"
    compat.mkdir(parents=True)
    canonical_root.mkdir(parents=True)
    missing_readme = missing_readme or set()
    row_overrides = row_overrides or {}
    readme_overrides = readme_overrides or {}

    for lane in actual:
        child = compat / lane
        child.mkdir()
        if lane not in missing_readme:
            (child / "README.md").write_text(
                readme_overrides.get(
                    lane,
                    (
                        "# redirect\n\n"
                        f"Canonical catalog: data/catalog/domain/{lane}/\n"
                    ),
                ),
                encoding="utf-8",
            )

    for lane in canonical if canonical is not None else actual:
        (canonical_root / lane).mkdir()

    rows = []
    for lane in indexed:
        rows.append(
            row_overrides.get(
                lane,
                f"- [`{lane}/`](./{lane}/README.md)",
            )
        )
    (compat / "README.md").write_text(
        SECTION + "\n".join(rows) + "\n",
        encoding="utf-8",
    )
    return compat, canonical_root


class CatalogDomainCompatibilityRedirectTests(unittest.TestCase):
    def test_current_redirect_inventory_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            compat, canonical = _write_layout(
                Path(tmp),
                actual=["agriculture", "archaeology", "atmosphere"],
                indexed=["agriculture", "archaeology", "atmosphere"],
                canonical=["agriculture", "archaeology", "atmosphere", "people"],
            )
            report = validate_catalog_domain_compatibility_redirect(compat, canonical)
            self.assertEqual("PASS", report["outcome"])
            self.assertTrue(report["canonical_only_children_allowed"])
            self.assertFalse(report["authority_created"])

    def test_unindexed_redirect_child_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            compat, canonical = _write_layout(
                Path(tmp),
                actual=["agriculture", "fauna"],
                indexed=["agriculture"],
            )
            report = validate_catalog_domain_compatibility_redirect(compat, canonical)
            self.assertEqual("FAIL", report["outcome"])
            self.assertEqual(["fauna/"], report["missing_from_index"])

    def test_stale_redirect_entry_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            compat, canonical = _write_layout(
                Path(tmp),
                actual=["agriculture"],
                indexed=["agriculture", "retired"],
                canonical=["agriculture", "retired"],
            )
            report = validate_catalog_domain_compatibility_redirect(compat, canonical)
            self.assertEqual("FAIL", report["outcome"])
            self.assertEqual(["retired/"], report["stale_index_entries"])

    def test_duplicate_redirect_entry_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            compat, canonical = _write_layout(
                Path(tmp),
                actual=["agriculture"],
                indexed=["agriculture", "agriculture"],
            )
            report = validate_catalog_domain_compatibility_redirect(compat, canonical)
            self.assertEqual("FAIL", report["outcome"])
            self.assertEqual(["agriculture/"], report["duplicate_entries"])

    def test_mismatched_redirect_link_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            compat, canonical = _write_layout(
                Path(tmp),
                actual=["agriculture"],
                indexed=["agriculture"],
                row_overrides={
                    "agriculture": "- [`agriculture/`](./fauna/README.md)"
                },
            )
            report = validate_catalog_domain_compatibility_redirect(compat, canonical)
            self.assertEqual("FAIL", report["outcome"])
            self.assertEqual(1, len(report["invalid_redirect_rows"]))

    def test_missing_canonical_target_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            compat, canonical = _write_layout(
                Path(tmp),
                actual=["agriculture", "fauna"],
                indexed=["agriculture", "fauna"],
                canonical=["agriculture"],
            )
            report = validate_catalog_domain_compatibility_redirect(compat, canonical)
            self.assertEqual("FAIL", report["outcome"])
            self.assertEqual(["fauna/"], report["missing_canonical_targets"])

    def test_missing_redirect_readme_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            compat, canonical = _write_layout(
                Path(tmp),
                actual=["agriculture"],
                indexed=["agriculture"],
                missing_readme={"agriculture"},
            )
            report = validate_catalog_domain_compatibility_redirect(compat, canonical)
            self.assertEqual("FAIL", report["outcome"])
            self.assertEqual(["agriculture/"], report["missing_child_readmes"])

    def test_contradictory_child_redirect_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            compat, canonical = _write_layout(
                Path(tmp),
                actual=["agriculture"],
                indexed=["agriculture"],
                readme_overrides={
                    "agriculture": (
                        "# redirect\n\n"
                        "Canonical catalog: data/catalog/domain/fauna/\n"
                    )
                },
            )
            report = validate_catalog_domain_compatibility_redirect(compat, canonical)
            self.assertEqual("FAIL", report["outcome"])
            self.assertEqual(["agriculture/"], report["invalid_child_redirects"])
            self.assertEqual(
                [
                    {
                        "lane": "agriculture/",
                        "reason_codes": ["CANONICAL_TARGET_MISSING"],
                    }
                ],
                report["invalid_child_redirect_details"],
            )

    def test_conflicted_child_redirect_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            compat, canonical = _write_layout(
                Path(tmp),
                actual=["agriculture"],
                indexed=["agriculture"],
                readme_overrides={
                    "agriculture": (
                        "<<<<<<< HEAD\n"
                        "Canonical catalog: data/catalog/domain/agriculture/\n"
                        "=======\n"
                        "Canonical catalog: data/catalog/domain/agriculture/\n"
                        ">>>>>>> origin/main\n"
                    )
                },
            )
            report = validate_catalog_domain_compatibility_redirect(compat, canonical)
            self.assertEqual("FAIL", report["outcome"])
            self.assertEqual(["agriculture/"], report["invalid_child_redirects"])
            self.assertEqual(
                [
                    {
                        "lane": "agriculture/",
                        "reason_codes": ["MERGE_CONFLICT_MARKER"],
                    }
                ],
                report["invalid_child_redirect_details"],
            )

    def test_child_redirect_reason_codes_are_stable_and_composable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            compat, canonical = _write_layout(
                Path(tmp),
                actual=["agriculture"],
                indexed=["agriculture"],
                readme_overrides={
                    "agriculture": (
                        "<<<<<<< HEAD\n"
                        "Canonical catalog: data/catalog/domain/fauna/\n"
                        "=======\n"
                        "Canonical catalog: data/catalog/domain/flora/\n"
                        ">>>>>>> origin/main\n"
                    )
                },
            )
            report = validate_catalog_domain_compatibility_redirect(compat, canonical)
            self.assertEqual("FAIL", report["outcome"])
            self.assertEqual(
                [
                    {
                        "lane": "agriculture/",
                        "reason_codes": [
                            "MERGE_CONFLICT_MARKER",
                            "CANONICAL_TARGET_MISSING",
                        ],
                    }
                ],
                report["invalid_child_redirect_details"],
            )

    def test_cli_json_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            compat, canonical = _write_layout(
                Path(tmp),
                actual=["agriculture", "fauna"],
                indexed=["agriculture", "fauna"],
            )
            outputs = []
            for _ in range(2):
                stream = io.StringIO()
                with redirect_stdout(stream):
                    rc = main(
                        [
                            "--compatibility-root",
                            str(compat),
                            "--canonical-root",
                            str(canonical),
                        ]
                    )
                self.assertEqual(0, rc)
                outputs.append(stream.getvalue())
            self.assertEqual(outputs[0], outputs[1])
            report = json.loads(outputs[0])
            self.assertEqual(
                "kfm.catalog-domain-compatibility-redirect.v3",
                report["profile"],
            )


if __name__ == "__main__":
    unittest.main()
