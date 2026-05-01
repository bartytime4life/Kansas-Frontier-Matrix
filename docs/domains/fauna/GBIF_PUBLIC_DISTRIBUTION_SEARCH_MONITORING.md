# KFM Meta Block v2
- Domain: fauna
- Source: GBIF
- Layer: PUBLIC_DISTRIBUTION_BUNDLE -> SEARCH_INDEX/STATIC_EXPORT/API_DTO -> CACHE_INVALIDATION -> PUBLIC_ENDPOINT_MONITORING -> TAKEDOWN_ENFORCEMENT

## Purpose
Fixture-backed public distribution pipeline for approved GBIF releases only.

## Evidence-to-distribution chain
EvidenceBundle -> Public Aggregate -> Geoprivacy Receipt -> Catalog Entry -> Triplet Claim -> Runtime Answer -> UI DTO/Map -> Answer Receipt -> Publication Package -> Audit Ledger -> Replay Verification -> Steward Review -> Release Registry -> Public Manifest -> Distribution Bundle -> Search/API/Public Endpoint.

## Contracts
Implemented in schemas under `schemas/distribution`, `schemas/search`, `schemas/api`, `schemas/monitoring`, `schemas/ci`, and `schemas/receipts`.

## Safe distribution rules
- Ready bundles require published release + approve_publish review + manifest citation index + public-safe postures.
- Forbidden coordinate fields/language denied recursively.
- Presence posture fixed: `reported_occurrence_not_confirmed_presence`.

## Blocked / withdrawn / superseded behavior
- Non-published or non-approved inputs produce `blocked` distribution state.
- Superseded without successor is blocked.
- Takedown emits receipt + cache invalidation and sets `public_use_allowed=false`.

## Cache and route semantics
Deterministic cache key format: `gbif:fauna:{route_type}:{artifact_id}`.

## CLI examples
Use tools in `tools/distribution/fauna`, `tools/search/fauna`, `tools/api/fauna`, `tools/cache/fauna`, `tools/monitoring/fauna`, `tools/takedown/fauna`, and `tools/ci/fauna` as documented in task prompt.

## Validator and policy gates
- Python validator: `tools/validators/fauna/gbif_distribution_validator.py`.
- Rego deny policy: `policy/fauna/gbif_distribution.rego`.

## Testing posture
Pytest covers end-to-end generation and validator checks.

## Limitations
Fixture-only simulation; no live endpoints or network calls.

## Promotion checklist
1. Validate bundle/search/static/api/receipts.
2. Confirm endpoint checks passed.
3. Run distribution gate.

## Rollback/takedown notes
Run takedown tool with withdrawal receipt and emit invalidation receipt.

## NEEDS_VERIFICATION
- Canonical cache key namespace for production edge caches.
- Search index registration naming in production deployment.
- API route registration source-of-truth.
- Endpoint monitoring integration target system.
