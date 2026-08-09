# SpatialTransformReceipt

Status: **PROPOSED** · scope: deterministic transformation process memory.

Pass 9 identifies CRS and resolution transformation as an evidence concern rather than a background GIS implementation detail. A promoted raster, vector extract, tile package, or generalized output that crossed CRS or resolution boundaries should retain enough process memory to reconstruct what changed.

A `SpatialTransformReceipt` records input/output artifact references, source and target CRS, transform operations, resampling/generalization method where applicable, before/after digests, evidence references, and a finite validation outcome.

## Invariants

- input and output artifact references are distinct;
- source and target CRS are explicit non-empty identifiers;
- at least one transform operation is named;
- input and output SHA-256 digests are present and cannot be equal when `changed=true`;
- `network_access` is false for fixture validation;
- `PASS` requires at least one evidence reference and `changed=true`;
- `ERROR` never degrades to `PASS`;
- this receipt proves a declared transform ran; it does not prove source authority, policy approval, promotion, release, or publication.

## Directory Rules basis

Accepted ADR-0029 / Directory Rules v2 places semantic meaning in `contracts/evidence/`, machine shape in `schemas/contracts/v1/evidence/`, fixtures in `fixtures/contracts/v1/evidence/`, validators in `tools/validators/evidence/`, tests in `tests/validators/`, CI in `.github/workflows/`, and source lineage in `docs/intake/exploratory/`.
