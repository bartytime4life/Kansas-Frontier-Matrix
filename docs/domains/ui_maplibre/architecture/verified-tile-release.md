# Verified Tile Release (Governed Layer)

## KFM Meta Block V2
- Spec ID: `NEEDS_VERIFICATION`
- Owner: `NEEDS_VERIFICATION`
- Status: `draft`
- Last Reviewed: `NEEDS_VERIFICATION`
- Policy Bundle: `NEEDS_VERIFICATION`

This layer defines governed release evidence for verified tiles. Publication is a policy-controlled state transition. RAW/WORK/QUARANTINE references are denied.

## Artifacts
- `VerifiedTileReleaseEvidence.v1`
- `TilePromotionProofBundle.v1`
- `TileVerificationReceipt.v1`
- `TileRuntimeVerificationContract.v1`
- `TileVerificationFailureReport.v1`

## Tooling
- Validator: `tools/validators/tiles/validate_verified_tile_release.py`
- Builder: `tools/tiles/build_tile_promotion_proof_bundle.py`
- Policy: `policy/tiles/verified_tile_release.rego`
