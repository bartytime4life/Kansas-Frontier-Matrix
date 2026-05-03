# AIR_REENTRY_MAINTENANCE_ROLLFORWARD_REFRESH_SLICE

## KFM Meta Block v2
- Status: PROPOSED / NEEDS_VERIFICATION
- Domain: atmosphere.air
- Mode: fixture-backed candidate-only

This layer consumes re-entry maintenance/remediation-refresh outputs and prepares candidate-only maintenance roll-forward refresh artifacts. It does not publish, deploy, notify, or mutate production truth.

Lifecycle chain preserved through REENTRY_MAINTENANCE_ROLLFORWARD_REFRESH with artifact separation. RAW/WORK/QUARANTINE and direct PROCESSED exposure are forbidden. NowCast remains operational evidence and never validated AQS truth; validated AQS rows use `24h_validated`.

Public boundary: no writes to `data/published/air/` or `data/published/air/read_model/`; no notices, route removals, deletions, rollback execution, or production baseline rotation.

No-network/no-live-ops: no live AirNow/AQS/Mesonet/NOAA/API/CDN/DNS/cloud/ticketing/monitoring/calendar actions.
