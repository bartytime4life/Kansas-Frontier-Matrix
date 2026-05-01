# PMTiles Governance (KFM)

## KFM_META_BLOCK_V2 Placement
PMTiles base/delta manifests are governance objects with `version`, `spec_hash`, `generated_at`, and release/promotion references. Promotion is a state transition; it is not a file move.

## Lifecycle and Layering
- Base PMTiles: immutable, long-TTL artifacts.
- Delta PMTiles: short-TTL overlays bound to a base archive.
- Public clients should resolve only released/published manifests.

## Cache TTL Rules
- Base archive manifests should emit long-lived `Cache-Control` values.
- Delta manifests should emit shorter `Cache-Control` values suitable for rapid updates.

## Manifest Fields and Completeness
The governed delta manifest schema requires:
- base/delta refs with href + digest + zoom/bbox
- `tile_count`, `expected_tile_count`, `completeness_pct`
- `masked_pct`, `coverage_pct`
- proof/signature refs
- rights/license posture
- geoprivacy envelope and release/promotion refs

## CI and Promotion Gates
CI fail-closed checks enforce:
- completeness recomputation and threshold (`>=0.95`)
- masked thresholds: PASS (`<=0.15`), REVIEW (`0.15..0.30`) with attestation, REJECT (`>0.30`)
- required digest/proof/signature posture for public/released state
- policy denials for RAW/WORK/QUARANTINE references and missing geoprivacy receipt

## Fail-Closed Behavior
Unknown or missing digest/signature/proof posture is denied for released/public artifacts.

## TODOs
- Wire DSSE/Cosign signature verification in a follow-on validator.
- Add register-linked release evidence bundle cross-checks once release object family is extended.
