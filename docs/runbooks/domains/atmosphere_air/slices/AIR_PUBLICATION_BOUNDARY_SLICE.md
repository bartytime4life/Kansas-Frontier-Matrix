# AIR_PUBLICATION_BOUNDARY_SLICE

## KFM Meta Block v2
- Domain: atmosphere.air
- Layer: Public Publication Boundary (fixture-backed slice)
- Status: IMPLEMENTED (fixture/no-network), live publication PROPOSED / NEEDS_VERIFICATION
- Doctrine: cite-or-abstain, evidence-first, fail-closed

This layer consumes release-candidate artifacts (`qa_summary`, `evidence_bundle`, `promotion_decision`, `release_manifest`, `run_receipt`) and verifies Gate D attestation and AQS reconciliation where required before emitting `publication_manifest.json`.

Lifecycle: `RAW/WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLICATION_CANDIDATE -> PUBLISHED`.

Public boundary rules:
- public clients must never read RAW/WORK/QUARANTINE
- public clients must not read PROCESSED directly
- `data/published/air/` is immutable release output only

Gates:
- Gate A: NowCast > 35 µg/m³
- Gate B: NowCast > baseline + 2σ
- Gate C: station coverage < 75%
- Gate D: signed attestation / override

AQS reconciliation:
- validated AQS rows are separate from NowCast
- reconciliation required within 72 hours before override/publication when applicable

This PR does **not** create live AirNow/AQS/Mesonet publication.
