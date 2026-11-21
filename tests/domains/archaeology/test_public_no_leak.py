"""Archaeology public no-leak tests stay held until their subjects exist.

Planned intent (docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md): Public layers, manifests, tile binaries, popups, and exports contain no exact-site geometry, sensitive attributes, or PII.

Its schemas (layer_manifest, publication_transform_receipt) define no domain
fields. data/published/archaeology and pipelines/domains/archaeology/publish
hold only README files. Each check fails with PUBLIC_NO_LEAK_NOT_IMPLEMENTED
when its subject gains content, so the real tests must land in the same change.

Two more checks cover the rest of data/published/: no archaeology
directory there may hold anything but READMEs and the PROPOSED
layers/archaeology/layer_registry.yaml, which registers no layer.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
REASON = "PUBLIC_NO_LEAK_NOT_IMPLEMENTED"
SCHEMAS = (
    "schemas/contracts/v1/domains/archaeology/layer_manifest.schema.json",
    "schemas/contracts/v1/domains/archaeology/publication_transform_receipt.schema.json",
)
GENERIC_FIELDS = {"id", "spec_hash", "version"}
DIRECTORIES = (
    "data/published/archaeology",
    "pipelines/domains/archaeology/publish",
)
LAYER_REGISTRY = "data/published/layers/archaeology/layer_registry.yaml"


class HeldTests(unittest.TestCase):
    def test_schemas_still_have_no_domain_fields(self) -> None:
        for relative in SCHEMAS:
            schema = json.loads((REPO_ROOT / relative).read_text(encoding="utf-8"))
            fields = set(schema.get("properties", {})) - GENERIC_FIELDS
            self.assertEqual(fields, set(),
                             f"{REASON}: {relative} now defines {sorted(fields)}. Replace this hold "
                             "with tests that accept valid and reject invalid fixtures.")

    def test_directories_still_hold_only_readmes(self) -> None:
        for relative in DIRECTORIES:
            base = REPO_ROOT / relative
            self.assertTrue(base.is_dir(), f"{REASON}: {relative} moved; point this hold at its new home.")
            content = sorted(
                path.relative_to(REPO_ROOT).as_posix()
                for path in base.rglob("*")
                if path.is_file() and path.suffix != ".md" and path.name != ".gitkeep"
                and "__pycache__" not in path.parts
            )
            self.assertEqual(content, [], f"{REASON}: {relative} now holds {content}. Replace this hold "
                             "with tests for that content.")

    def test_nothing_archaeological_is_published_anywhere(self) -> None:
        published = sorted(
            path.relative_to(REPO_ROOT).as_posix()
            for path in (REPO_ROOT / "data/published").rglob("*")
            if path.is_file() and "archaeology" in path.relative_to(REPO_ROOT / "data/published").parts[:-1]
            and path.suffix != ".md" and path.name != ".gitkeep"
        )
        self.assertEqual(published, [LAYER_REGISTRY],
                         f"{REASON}: archaeology content is published. Replace this hold with no-leak "
                         "tests that scan it for exact geometry, sensitive attributes and PII.")

    def test_layer_registry_is_still_a_placeholder(self) -> None:
        relative = LAYER_REGISTRY
        lines = (REPO_ROOT / relative).read_text(encoding="utf-8").splitlines()
        keys = sorted(line.split(":", 1)[0] for line in lines if line and not line[0].isspace() and ":" in line)
        self.assertEqual(keys, ["notes", "path", "source_docs", "status"],
                         f"{REASON}: {relative} now registers layers. Replace this hold with tests that "
                         "scan every registered public layer, manifest and export for exact geometry.")
        self.assertIn("status: PROPOSED", lines)


if __name__ == "__main__":
    unittest.main()
