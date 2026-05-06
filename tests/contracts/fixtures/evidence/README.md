# `tests/contracts/fixtures/evidence/`

Evidence-oriented contract fixtures for `tests/contracts/`.

## Current fixtures

- `kfm_geo_manifest.valid.json`
  - Valid example for `EcologyLayerManifest` shape.
  - Intended for schema/contract validation and fixture-driven contract tests.

## Notes

- Keep fixtures deterministic and small.
- Name files by object family + polarity (`.valid` / `.invalid`) + reason when invalid.
- This directory stores examples only; canonical schema authority remains under `schemas/contracts/`.
