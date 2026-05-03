# AIR Re-Entry Read-Model Refresh Slice

## KFM Meta Block v2
- Status: draft fixture-only slice
- Domain: atmosphere.air
- Scope: governed preview artifacts only; no publication/deployment

This slice consumes re-entry publication materialization artifacts and produces candidate-only read-model refresh preview artifacts (index/API/status/provenance/delta/invalidation/version/manifest/decision/ledger/postcheck/audit). It is no-network and fixture-backed.

It does **not** publish, deploy, notify clients, delete artifacts, remove routes, or mutate public truth. It does **not** write to `data/published/air/` or `data/published/air/read_model/`.

NowCast is operational evidence and must never be treated as validated AQS truth; validated rows use `24h_validated` semantics.

NEEDS_VERIFICATION: all live operations (AirNow/AQS/Mesonet calls, CDN/DNS/cloud/ticketing/alerting/calendar, production signatures/publication/deployment/rebuild).
