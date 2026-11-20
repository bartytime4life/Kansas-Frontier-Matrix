"""Settlements and infrastructure catalog closure stays held until settlements and infrastructure catalog records exist.

Planned intent (docs/domains/settlements-infrastructure/EXPANSION_BACKLOG.md): SET-BL-0009, catalog / proof / release closure test.

No settlements and infrastructure domain, STAC, DCAT or PROV catalog record is tracked, so there is
nothing to close yet. The hold test fails with CATALOG_CLOSURE_NOT_IMPLEMENTED as
soon as one appears, so closure tests must land with the first record. Catalog
emission itself is held separately (tests/qa/test_held_entry_points.py).
"""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DOMAIN = "settlements-infrastructure"
LANES = (
    f"data/catalog/domain/{DOMAIN}",
    f"data/catalog/domains/{DOMAIN}",
    f"data/catalog/stac/{DOMAIN}",
    f"data/catalog/dcat/{DOMAIN}",
    f"data/catalog/prov/{DOMAIN}",
    f"data/catalog/{DOMAIN}",
)


def catalog_records(root: Path) -> list[str]:
    """Return files in the domain catalog lanes other than Markdown docs and .gitkeep files."""
    found = []
    for lane in LANES:
        base = root / lane
        if base.is_dir():
            found.extend(
                path.relative_to(root).as_posix()
                for path in base.rglob("*")
                if path.is_file() and path.suffix != ".md" and path.name != ".gitkeep"
            )
    return sorted(found)


class CatalogClosureHoldTests(unittest.TestCase):
    def test_catalog_closure_is_held_while_no_records_exist(self) -> None:
        records = catalog_records(REPO_ROOT)
        self.assertEqual(
            records,
            [],
            "CATALOG_CLOSURE_NOT_IMPLEMENTED: settlements and infrastructure catalog records exist without "
            "closure tests. Replace this hold with closure tests before admitting: "
            + ", ".join(records),
        )

    def test_hold_detects_a_record_and_ignores_docs(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            lane = root / LANES[0]
            lane.mkdir(parents=True)
            (lane / "README.md").write_text("docs", encoding="utf-8")
            (lane / ".gitkeep").write_text("", encoding="utf-8")
            self.assertEqual(catalog_records(root), [])
            (lane / "collection.json").write_text("{}", encoding="utf-8")
            self.assertEqual(catalog_records(root), [f"{LANES[0]}/collection.json"])

    def test_hold_scans_the_canonical_domain_catalog_lane(self) -> None:
        self.assertTrue((REPO_ROOT / LANES[0] / "README.md").is_file())


if __name__ == "__main__":
    unittest.main()
