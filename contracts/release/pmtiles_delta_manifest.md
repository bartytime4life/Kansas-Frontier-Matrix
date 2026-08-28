# PMTiles Delta Manifest Contract

**Status:** PROPOSED fixture-first release-support profile.  
**Scope:** one digest-bound PMTiles delta archive plus per-tile lineage and bounded quality-control evidence.  
**Authority boundary:** this contract does not define a release decision, verify a signature, approve policy, deploy an archive, or publish a map layer.

## Purpose

A PMTiles delta manifest lets reviewers and clients inspect which tiles changed, verify each changed tile's digest lineage against a prior digest, bind the delta to a base archive and index, and detect count or quality drift without trusting the build host.

This is a narrower profile alongside the existing general `TileArtifactManifest` and PMTiles attestation surfaces. It does not claim to resolve the broader placeholder schema or replace the established attestation-bundle validator. Instead, it links to a digest-bound `attestation_ref` and keeps cryptographic verification as an explicit later gate.

## Required invariants

- `delta_id` is deterministic from `layer_id` and the UTC start date.
- base and delta archive references end with their declared archive digests.
- `spec_hash` is SHA-256 over canonical JSON with `spec_hash` omitted.
- tile changes are unique and ordered by `(z, x, y)`.
- `tile_id` and `quadkey` are derived from the same coordinates.
- coordinates fit the declared zoom.
- `added` tiles have a new digest and no prior digest.
- `modified` tiles have distinct new and prior digests.
- `removed` tiles have only a prior digest and zero emitted bytes.
- `expected_tile_count` equals `base tile count + additions - removals`.
- observed QC values are recomputed from the tile list and count fields.
- the declared `PASS`, `REVIEW`, or `REJECT` decision matches the thresholds.
- non-removed `masked_pct + coverage_pct = 100` within numeric tolerance.
- run-receipt, source-manifest, artifact, and attestation references cannot point into RAW, WORK, or QUARANTINE.

## QC semantics

The profile carries thresholds rather than hard-coding one domain's policy:

| Metric | Effect |
|---|---|
| `max_masked_pct > reject_masked_pct` | `REJECT` |
| `max_masked_pct > review_masked_pct` but not reject | `REVIEW` |
| average emitted tile bytes above threshold | `REJECT` |
| produced-vs-expected tile-count deviation above threshold | `REJECT` |
| none of the above | `PASS` |

A manifest-level `PASS` is only structural/QC consistency. It is not a promotion, release, or publication decision.

## Directory Rules basis

- semantic release-support meaning: `contracts/release/`
- machine shape: `schemas/contracts/v1/map/`
- synthetic examples: `fixtures/pmtiles/delta_manifest/`
- executable checks: `tools/validators/`
- regression proof: `tests/validators/`
- CI integration: `.github/workflows/pmtiles-delta-manifest.yml`

These are existing responsibility roots under accepted ADR-0029. No new root, public artifact, proof, receipt, or release home is created.

## Non-effects

The validator reads local synthetic JSON only. It does not open PMTiles archives, fetch byte ranges, verify an actual tile digest, authenticate CORS/Range headers, validate a PMSIG/DSSE signature, resolve EvidenceBundles, evaluate policy, write lifecycle data, approve release, deploy, or publish.

## Validation

```bash
python -m pytest -q tests/validators/test_pmtiles_delta_manifest.py
python tools/validators/validate_pmtiles_delta_manifest.py --fixtures
```

## Rollback

Revert the contract, schema, fixture family, validator, test, and dedicated workflow together. Existing PMTiles archives, attestation bundles, manifests, receipts, proofs, and release history are unchanged by this slice.
