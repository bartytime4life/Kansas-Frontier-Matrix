<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://apps/explorer-web/features/streamflow-qc-dashboard
title: Streamflow QC Prioritization Dashboard
type: feature-readme
version: v0.1.0
status: proposed; fixture-backed; read-only
owner: OWNER_TBD - Explorer and hydrology stewards
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; public-safe-projection; no-network
owning_root: apps/
responsibility: bounded read-only presentation of a closed streamflow QC context projection
truth_posture: PROPOSED fixture-backed UI; production wiring and hosted exact-head results need verification
source_ideas: [KFM-P32-IDEA-0002, KFM-P32-FEAT-0001]
related:
  - ../../adapters/StreamflowQcDashboardProjection.ts
  - ../../../../../contracts/domains/hydrology/streamflow_qc_context_assessment.md
  - ../../../../../fixtures/ui/streamflow_qc_dashboard_projection/README.md
  - ../../../../../docs/intake/exploratory/pass-32-streamflow-qc-dashboard-source-map.md
[/KFM_META_BLOCK_V2] -->

# Streamflow QC Prioritization Dashboard

This additive Explorer feature renders a closed, public-safe projection of the existing streamflow QC context assessment. It makes declared low-flow, adjacent-gauge, drought, ingest, unit, cadence, and review-priority classifications visible alongside opaque EvidenceRefs.

The adapter accepts an exact field set, binds assessment identity to the spec hash, checks finite outcome semantics, requires canonical evidence ordering, denies direct-store-shaped references, and fails closed on contradictions or unknown fields.

The surface is intentionally read-only. It cannot retrieve gauge data, compute a percentile, expose raw flow values or coordinates, invalidate a sensor, declare a hydrologic event, change detector configuration, approve a review, release, deploy, or publish.

Synthetic fixtures cover regional context, local review, no escalation, hold, deny, error, shape rejection, and semantic contradiction. Browser coverage confirms that held or invalid input exposes no gauge or evidence detail and that no button or link is rendered.
