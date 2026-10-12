# PolicyObligationReduction fixtures

**Status:** synthetic / fixture-only / non-authoritative

This directory exercises the proposed `PolicyObligationReduction` contract without a live policy engine, source, evidence resolver, transform executor, release gate, or public surface.

## Lanes

- `valid/valid_*.json` — schema-valid records whose deterministic result, identity, provenance, and non-effects pass.
- `invalid/invalid_*.json` — true JSON-Schema negatives used by the repository-wide contract fixture lane.
- `invalid/semantic_invalid_*.json` — schema-valid records that the dedicated semantic validator must reject.
- `expected_findings_manifest.json` — exact case/outcome/finding inventory for deterministic replay.

The naming split is intentional. Repository-wide schema tests require every `invalid_*.json` file to fail JSON Schema; semantic negatives therefore use the `semantic_invalid_*.json` prefix.

## Boundary

A passing fixture proves only deterministic synthetic reduction. It does not prove that an accepted policy emitted an obligation, that a transform was applied, or that any candidate may be promoted, released, published, or used publicly.
