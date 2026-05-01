# AIR Re-Entry Deployment Readiness Refresh Slice

## KFM Meta Block v2
- Domain: atmosphere.air
- Layer: ReEntryDeploymentReadinessRefresh
- Mode: fixture/candidate only
- Network: disabled by design

This slice consumes governed re-entry client-delivery-refresh preview artifacts and prepares candidate deployment-readiness artifacts only. It does not deploy, publish, notify, or mutate public truth.

Key constraints:
- No writes to `data/published/air/`.
- No writes to `data/published/air/read_model/`.
- No RAW/WORK/QUARANTINE/PROCESSED exposure.
- No live AirNow/AQS/Mesonet/API/CDN/DNS/cloud/ticketing/alerting/calendar operations.
- NowCast is operational evidence only, never validated AQS truth.

Lifecycle carry-forward includes:
`... -> ReEntryClientDeliveryRefresh -> ReEntryDeploymentReadinessRefresh`.

All production-signature, production deployment, publication, and live operations are **PROPOSED / NEEDS_VERIFICATION**.
