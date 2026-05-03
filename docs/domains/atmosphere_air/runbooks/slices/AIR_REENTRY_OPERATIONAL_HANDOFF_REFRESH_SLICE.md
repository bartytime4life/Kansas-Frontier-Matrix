# AIR Reentry Operational Handoff Refresh Slice

## KFM Meta Block v2
- Domain: atmosphere.air
- Slice: REENTRY_OPERATIONAL_HANDOFF_REFRESH
- Mode: fixture/candidate only
- Network: disabled by design

This layer consumes governed re-entry cutover-observation refresh artifacts and prepares local candidate artifacts for operational handoff, watch-window evaluation, runbook activation, stakeholder notice finalization, evidence archive manifesting, release closure dossier, manifesting, decisioning, ledgering, and postcheck/audit.

It does **not** publish, deploy, activate live operations, write `data/published/air/`, write `data/published/air/read_model/`, send notices, remove routes, or delete artifacts.
