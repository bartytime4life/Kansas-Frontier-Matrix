# Changelog

All notable changes to KFM are recorded here. The repository uses
governed releases — see `release/` for manifests, rollback cards,
and correction notices.

## [Unreleased]
- Greenfield scaffolding generated.
- PR-001: local JSON Schema `$ref` resolver wired; `make schemas` and `make test` now executable; three CI workflows live.
- PR-002: validator/test floor green; `api-test` workflow now runs governed-api smoke and envelope-shape tests; domain-alias schemas converted to `unevaluatedProperties` to honor `allOf/$ref`.
- PR-003: CONFIRMED floor mismatch corrected by schema tightenings for invalid fixtures; PROPOSED hydrology source spine seeded with wbd_huc12 descriptor + ADR-0026.
