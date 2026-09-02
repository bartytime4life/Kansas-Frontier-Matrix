<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixtures/ui/streamflow-qc-dashboard-projection
title: Streamflow QC Dashboard Projection Fixtures
type: fixture-readme
version: v0.1.0
status: proposed; synthetic; non-authoritative
owner: OWNER_TBD - Explorer and hydrology stewards
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; fixture-only; no-network
owning_root: fixtures/
responsibility: synthetic positive and negative packets for the streamflow QC dashboard adapter
truth_posture: CONFIRMED synthetic fixture shapes only; production data and public use need verification
related:
  - ../../../apps/explorer-web/src/adapters/StreamflowQcDashboardProjection.ts
  - ../../../apps/explorer-web/src/features/streamflow_qc_dashboard/README.md
  - ../../../contracts/domains/hydrology/streamflow_qc_context_assessment.md
[/KFM_META_BLOCK_V2] -->

# Streamflow QC Dashboard Projection Fixtures

These synthetic packets exercise the Explorer adapter after upstream streamflow QC context validation. They contain finite classifications and opaque references only.

Valid cases cover regional context, local review, no escalation, hold, deny, and upstream error. Invalid cases prove exact-field rejection and semantic fail-closed behavior.

The fixtures do not contain a raw flow value, numeric percentile, coordinate, source endpoint, credential, detector configuration, or authority to invalidate a sensor, declare an event, approve, release, or publish.
