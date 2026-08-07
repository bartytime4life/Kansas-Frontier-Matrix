<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-data-catalog-health-readme
title: Catalog health fixture family
type: README; fixtures; catalog-health; stac-item
version: v1.0.0
status: PROPOSED; synthetic; no-network
created: 2026-08-07
updated: 2026-08-07
owning_root: fixtures/
policy_label: public; synthetic; no real source or sensitive data
related:
  - ../../../contracts/data/catalog_health_report.md
  - ../../../schemas/contracts/v1/data/catalog_health_report.schema.json
  - ../../../tools/validators/catalog/validate_catalog_health.py
  - ../../../tests/validators/test_validate_catalog_health.py
[/KFM_META_BLOCK_V2] -->

# Catalog health fixtures

This fixture family proves the proposed `kfm.catalog-health.stac-item.v1` profile without live sources or network access.

- `assets/sample.bin` is a 27-byte synthetic payload with SHA-256 `ab39b02de5828664a6643fc221de0c81f68e1c7e73ab3a347deb8381d8718466`.
- `valid/` contains a byte-verifiable local item and an intentionally embargoed item with a `via` request link.
- `hold/` contains a public HTTPS asset that must return `HOLD` while network mode is denied.
- `invalid/` covers missing provenance rels, checksum mismatch, path escape, and missing governance metadata.
- `expected_outcomes.json` and `expected_findings.json` make fixture polarity explicit and deterministic.

All names, geometry, URLs, digests, and content are synthetic. `catalog.example.invalid` is intentionally non-routable. No fixture is evidence, a source descriptor, a catalog release, or publication authority.
