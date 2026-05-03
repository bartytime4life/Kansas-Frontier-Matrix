# KFM Meta Block v2
- Domain: atmosphere.air
- Slice: PUBLIC_OPS/AUDIT
- Mode: Fixture-backed, no-network, fail-closed
- Status: Implemented (governance evidence only)

## Scope
This layer consumes Public Read Model + PublicationManifest lineage artifacts, replays lineage, verifies sha256/path safety, emits health/SLO reports, opens incident records, and prepares retraction request candidates.

Lifecycle: RAW/WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLICATION_CANDIDATE → PUBLISHED → PUBLIC_READ_MODEL → PUBLIC_OPS/AUDIT.

Public boundary: clients read only PublicIndex/PublicApiRecord/PublicStatus/PublicProvenanceTrace. Ops outputs are governance evidence, not live public truth.

## Gates
- Gate A: NowCast > 35 µg/m³
- Gate B: NowCast > baseline + 2σ
- Gate C: station coverage < 75%
- Gate D: signed attestation / override

## Checks
- Lineage replay
- sha256 verification
- stale index detection
- fixture-only status handling
- retracted/tombstoned active detection
- incident + retraction candidate workflow

AQS distinction: NowCast is operational evidence; validated AQS uses `24h_validated`; NowCast is never validated AQS truth.

PROPOSED / NEEDS_VERIFICATION: live monitoring, live alerting, prod dashboards/signatures, live AirNow/AQS/Mesonet ops.

This PR does not create live operations monitoring or live public air-quality publication.
