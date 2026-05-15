# Runtime Fixtures

This directory contains runtime/benchmark fixture corpora used by renderer smoke tests and performance governance.

## Purpose

`fixtures/` is for operational rendering inputs, not validator-only test data.

Use this lane for:

- PMTiles benchmark datasets
- MLT benchmark datasets
- MapLibre runtime fixtures
- Cesium runtime fixtures
- public-safe generalized geospatial corpora
- slim/heavy renderer stress scenarios

## Boundary

| Path | Purpose |
|---|---|
| `fixtures/` | runtime benchmark inputs |
| `tests/fixtures/` | deterministic test-only fixtures |
| `artifacts/` | generated CI outputs |
| `data/` | governed data lifecycle lanes |

## Rules

- Do not place RAW, WORK, or QUARANTINE data here.
- Do not place sensitive exact geometry here.
- Do not treat fixture corpora as canonical truth.
- Prefer small, public-safe, reproducible datasets.
- Large fixture corpora should use external storage or Git LFS only by explicit repo decision.
- Every corpus should eventually have a source note, rights note, and generation receipt.

## Suggested layout

```text
fixtures/
├── slim/
├── heavy/
├── ecology/
├── hydrology/
├── archaeology-public-safe/
└── infrastructure-generalized/
