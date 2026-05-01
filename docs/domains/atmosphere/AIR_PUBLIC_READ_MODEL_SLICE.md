# AIR_PUBLIC_READ_MODEL_SLICE

## KFM Meta Block v2
- Domain: atmosphere.air
- Slice: Public Read Model + Client-Safe Catalog/API
- Status: IMPLEMENTED (fixture-backed only)
- Verification: NEEDS_VERIFICATION for live serving and production signatures.

This layer consumes PublicationManifest-governed artifacts and emits client-safe `PublicIndex`, `PublicApiRecord`, `PublicStatus`, and `PublicProvenanceTrace` artifacts.

It never exposes `RAW`, `WORK`, `QUARANTINE`, or direct `PROCESSED` paths. It surfaces retractions/tombstones and keeps lifecycle artifacts separated.

Lifecycle: `RAW/WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLICATION_CANDIDATE -> PUBLISHED -> PUBLIC_READ_MODEL`.

Public boundary: clients read only public read model artifacts and never dereference internal governed artifacts directly.

Gates:
- Gate A: NowCast > 35 µg/m³
- Gate B: NowCast > baseline + 2σ
- Gate C: station coverage < 75%
- Gate D: signed attestation / override

AQS distinction:
- NowCast is operational evidence.
- Validated AQS rows use `24h_validated`.
- NowCast must never be labelled validated AQS truth.

PROPOSED / NEEDS_VERIFICATION:
- Live API serving.
- Live AirNow/AQS/Mesonet publication.
- Production signing workflow.

This PR does not create live public air-quality publication.
