# Hydrology Proof Slice — Current State

Date: 2026-05-05

## CONFIRMED (by files)
- Source descriptor exists for synthetic/no-network posture in `fixtures/source/source_descriptor.valid.json`.
- Evidence closure primitives exist in `fixtures/evidence/evidence_ref.valid.json` and `fixtures/evidence/evidence_bundle.valid.json`.
- Evidence Drawer payload exists in `fixtures/ui/evidence_drawer_payload.valid.json`.
- Focus-mode outcomes and hydrology focus fixtures exist in `fixtures/ai/` and `fixtures/domains/hydrology/focus/`.
- Release manifest and rollback artifacts exist in `fixtures/release/release_manifest.valid.json` and `fixtures/release/rollback_card.valid.json`.
- Mock API read-only surfaces exist in `apps/api/kfm_mock_api.py`.

## CONFIRMED (by tests/checks)
- `tools/validators/validate_evidence_closure.py` confirms ref-to-bundle closure logic for baseline fixtures.
- `tools/validators/validate_hydrology_proof_slice.py` confirms hardening checks for source/evidence/drawer/release consistency.
- `tests/test_mock_api_read_only_routes.py` confirms stable read-only mock surfaces.
- `tests/test_hydrology_proof_slice_current_state.py` confirms new negative proofs:
  - Focus ABSTAINS when EvidenceBundle closure is missing.
  - Promotion DENIES before release manifest + rollback reference.

## Added negative proofs
- `fixtures/domains/hydrology/focus/hydrology_synthetic_streamflow.public_abstain_missing_bundle_closure.json`
- `fixtures/domains/hydrology/release_dry_runs/hydrology_synthetic_streamflow.publish_denied.missing_manifest_and_rollback_ref.json`

## Remaining UNKNOWN/NEEDS VERIFICATION
- Whether additional domain-specific closure reasons should be enumerated beyond `MISSING_EVIDENCE`.
- Whether promotion denial reason taxonomy should be expanded for finer rollback/manifest sub-states.
