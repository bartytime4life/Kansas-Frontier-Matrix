<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/hydrology/huc12-comid-crosswalk-manifest
title: HUC12⇄COMID Crosswalk Manifest Governance Slice
type: standard
version: v1
status: draft
owners: hydrology domain steward; policy steward
created: 2026-05-01
updated: 2026-05-01
policy_label: public
related: [schemas/hydrology/huc12_comid_manifest.schema.json, policy/hydrology/huc12_comid_manifest.rego, tools/validators/hydrology/validate_huc12_comid_manifest.py]
tags: [kfm, hydrology, governance, crosswalk, manifest, promotion-gate]
notes: [Fixture-backed and no-network by design, Any runtime promotion wiring is NEEDS_VERIFICATION]
[/KFM_META_BLOCK_V2] -->

# HUC12⇄COMID Crosswalk Manifest

## Purpose
This slice governs release-candidate manifest records that bind a HUC12 unit to a COMID crosswalk artifact and prevents auto-promotion when anchor identities drift. The slice is fixture-backed and no-network.

## Manifest fields
Canonical schema: `schemas/hydrology/huc12_comid_manifest.schema.json`.

Required fields include:
- `layer_type = "huc12"`
- `huc12` (12-digit string)
- `snapshot_id`, `nhd_snapshot_id`
- `spec_hash` (sha256-tagged)
- `run_receipt_url`
- `valid_from`, `valid_to`
- `comid_crosswalk`, `crosswalk_digest` (sha256-tagged)

`additionalProperties` is disallowed.

## Stable IDs
Validator emits stable IDs:
- `manifest_id = huc12@<snapshot_id>::<spec_hash>`
- `timeslice_id = huc12::<snapshot_id>::<YYYYMMDD>-<YYYYMMDD>`

These IDs are deterministic under identical manifest content.

## Validator behavior
`tools/validators/hydrology/validate_huc12_comid_manifest.py` performs:
1. Draft 2020-12 schema validation.
2. Temporal check (`valid_from <= valid_to`).
3. Deterministic digest verification for local crosswalk paths (or paths resolvable under `--crosswalk-root`).
4. Stable JSON output envelope:
   - `ok`
   - `errors`
   - `manifest_id`
   - `timeslice_id`

No live network calls are made.

## Promotion gate behavior
Policy: `policy/hydrology/huc12_comid_manifest.rego`.

Denies promotion when:
- `nhd_snapshot_id` changes between previous released and current candidate.
- `crosswalk_digest` changes between previous released and current candidate.
- `spec_hash` is not `sha256:*`.
- `run_receipt_url_verified` is not `true`.
- previous/current records are missing (fail-closed comparison posture).

Promotion remains a governed state transition, not a file move.

## Evidence Drawer fields
For public evidence-bound clients, this slice expects at least:
- `snapshot_id`
- `nhd_snapshot_id`
- `spec_hash`
- `run_receipt_url` (+ verification state)
- `comid_crosswalk`
- `crosswalk_digest`
- validity range (`valid_from`, `valid_to`)

Any UI payload mapping is NEEDS_VERIFICATION.

## No-network fixture posture
All tests in this slice use local fixtures under `tests/fixtures/hydrology/huc12_comid_manifest/`; no WBD/NHD live pulls are performed.

## Rollback and correction implications
- If `nhd_snapshot_id` or `crosswalk_digest` changes, candidate is denied for auto-promotion and requires governed correction/supersession flow.
- Rollback should revert released alias/state to a prior approved manifest; immutable artifacts should not be deleted.
- Integration with release registries and alias wiring is NEEDS_VERIFICATION.
