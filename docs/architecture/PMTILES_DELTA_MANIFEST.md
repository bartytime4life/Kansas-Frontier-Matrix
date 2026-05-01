# PMTiles Delta Manifest (KFM Meta Block v2)

## Meta
- status: PROPOSED
- object_family: delta_manifest.v1
- scope: PMTiles time-sliced delta publication control slice
- last_updated: 2026-05-01

## Purpose
Defines a governed manifest for PMTiles delta slices so clients and policy gates can verify tile-level change integrity, rollback posture, and receipt linkage before public use.

## Lifecycle placement
- Base input: published PMTiles base archive reference (`base_pmtiles`).
- Delta build: time-sliced tile changes (`time_start`, `time_end`, `tiles`).
- Verification: schema + semantic validator + policy deny rules.
- Promotion: only if fail-closed checks pass.

## Manifest fields (v1)
- `manifest_version` = `v1`
- `delta_id`
- `base_pmtiles.url`, `base_pmtiles.spec_hash`, optional `base_pmtiles.etag`
- `time_start`, `time_end` (ISO date-time)
- `expected_tile_count`, `produced_tile_count`
- `tiles[]` with tile coordinate identity and rollback digests
- `qc.masked_pct_pass_threshold`, `qc.masked_pct_review_threshold`
- optional `signatures[]` with `method=cosign` and `sig_url`

## Client verification behavior
Clients should:
1. Validate against `contracts/kfm/delta_manifest.v1.json`.
2. Recompute canonical manifest hash from sorted-key canonical JSON.
3. Enforce rollback-safety semantics:
   - `modified`/`removed` must include non-null `prior_digest`
   - `added` must have null `prior_digest`
4. Enforce receipt and path boundaries:
   - each tile requires non-empty `run_receipt_url`
   - deny public references to `RAW`, `WORK`, or `QUARANTINE`

## Fail-closed rules
Validation fails when:
- any digest is malformed
- `base_pmtiles.spec_hash` missing
- produced tile count mismatch
- masked percentage exceeds review threshold
- receipt reference missing/empty
- forbidden storage strata appear in public references

## Implementation paths
- Schema: `contracts/kfm/delta_manifest.v1.json`
- Validator: `tools/validators/tiles/validate_delta_manifest.py`
- Policy: `policy/tiles/delta_manifest.rego`
- Policy tests: `policy/tiles/delta_manifest_test.rego`
- Fixtures: `tests/fixtures/tiles/delta_manifest/`
- CI workflow: `.github/workflows/tiles-ci.yml`

## Limitations / NEEDS_VERIFICATION
- NEEDS_VERIFICATION: production deployment wiring for this new workflow in branch protection.
- NEEDS_VERIFICATION: long-term canonical hash embedding field standardization across object families.
- NEEDS_VERIFICATION: signature verification execution policy for `cosign` entries.
- This document does not assert production enforcement unless CI/tests pass for the current run.
