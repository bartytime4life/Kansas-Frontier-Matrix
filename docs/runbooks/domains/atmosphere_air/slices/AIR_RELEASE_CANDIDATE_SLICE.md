# AIR_RELEASE_CANDIDATE_SLICE

## KFM Meta Block v2
- **Layer**: Atmosphere/Air release-candidate slice (fixture-backed, no-network)
- **Status**: Implemented for candidate generation; live connector publication remains **PROPOSED / NEEDS_VERIFICATION**
- **Contract scope**: EvidenceBundle → PromotionDecision → ReleaseManifest → STAC/DCAT/PROV/Triplet candidate outputs
- **Doctrine**: cite-or-abstain, evidence-first, fail-closed

## Purpose
This layer consumes a validated air QA summary and run receipt, then creates an EvidenceBundle and PromotionDecision before writing ReleaseManifest and catalog/triplet candidate records.

NowCast is explicitly treated as operational evidence and **not** validated AQS truth.

## Lifecycle
`RAW/WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`

- Candidate artifacts are written in non-public candidate locations.
- `data/published/air/` requires explicit approval, signed attestation, and release manifest controls.

## Gate conditions
- **Gate A**: NowCast > 35 µg/m³
- **Gate B**: NowCast > baseline + 2σ
- **Gate C**: station coverage < 75%
- **Gate D**: signed attestation (required for override/publication)

If deny conditions trigger, the builder emits a quarantine PromotionDecision and blocks catalog publication.

## Public boundary
- Catalog candidate output is not public truth.
- Fixture-backed artifacts must not be marked published.
- Public references must never include RAW, WORK, or QUARANTINE paths.

## NEEDS_VERIFICATION
- Live AirNow/AQS/Mesonet connectors are out of scope for this slice.
- Automated AQS reconciliation attestation workflows are not implemented here.
