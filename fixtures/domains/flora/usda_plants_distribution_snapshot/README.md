# Synthetic USDA PLANTS Distribution Snapshot Fixtures

These fixtures prove only the proposed no-network distribution-state profile.

- `input/` contains the exact synthetic CSV profile consumed by the normalizer.
- `valid/valid_snapshot.json` is the deterministic candidate produced from those inputs.
- `invalid/` contains independent failures for hash integrity, ordering, cross-product coverage, duplicate source rows, missing-row-as-absence collapse, authorship, internal lifecycle references, release-hold removal, and exact geometry.

The valid fixture intentionally contains one missing taxon-county source row. Its emitted state is `not_reported` with `interpretation: no_claim`; it is not converted to absence.

All taxa, counties, dates, digests, source rows, and evidence references are synthetic. The fixtures do not activate USDA PLANTS, prove botanical occurrence, clear rights or sensitivity, or authorize release.
