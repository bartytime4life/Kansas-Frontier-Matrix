# KFM Meta Block v2
- object_family: pmtiles_runtime_client.v1
- status: draft
- updated_at: 2026-05-01

## Purpose
Runtime PMTiles client loader that consumes governed PMTiles time index manifests and fails closed for public rendering.

## Lifecycle placement
This layer executes in `apps/web` after PMTiles governance CI has validated/produced manifests and before MapLibre adds sources.

## Relationship to governance CI
The runtime loader trusts governed manifest structure but still enforces client posture checks: digest format, proof refs, rights posture, completeness/masking thresholds, and release stage gates.

## Base + delta layering
- Add base archive first.
- Add latest render-eligible delta second (deterministic by `generated_at`).
- Denied deltas are never attached to MapLibre.

## Fail-closed runtime behavior
- Missing/invalid digest => deny.
- Public released artifact missing proof/signature => deny.
- `completeness_pct < 0.95` => deny.
- `masked_pct > 0.30` => deny.
- `0.15 < masked_pct <= 0.30` requires steward/reviewer attestation; render with review badge.
- Public refs to RAW/WORK/QUARANTINE => deny.
- Unknown rights/license => deny.
- Unknown/unimplemented verification status => deny.

## Evidence Drawer fields
Adapter surfaces `href`, `digest`, `spec_hash`, `generated_at`, release/promotion refs, completeness/masked/coverage pct, proof/signature refs, geoprivacy/redaction receipt refs, runtime decision, deny reasons, and review badge reason.

## Mobile defaults
The installer deduplicates deterministic source IDs (`pmtiles-<archive_id>`) and skips duplicate source installs.

## Known limitations
- Real Cosign/DSSE verification is not implemented here.
- Runtime currently relies on `proof_ref_present` + digest format checks and `verification_status` fields.

## NEEDS_VERIFICATION
- Wire real cryptographic verification (Cosign/DSSE) to replace `verification_status: not_implemented` posture.
- Confirm production manifest URL wiring in deployment environment config.
