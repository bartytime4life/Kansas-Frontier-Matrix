<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://docs/intake/exploratory/pass-32-streamflow-qc-dashboard-source-map
title: Pass 32 Streamflow QC Dashboard Source Map
type: exploratory-source-map
version: v0.1.0
status: proposed; implementation-bounded; non-authoritative
owners: [kfm-maintainers]
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; public-safe-projection
owning_root: docs/
responsibility: source-to-repository reconciliation for the bounded streamflow QC dashboard adaptation
truth_posture: CONFIRMED source and repository reconciliation; PROPOSED fixture-backed implementation
source_ideas: [KFM-P32-IDEA-0002, KFM-P32-FEAT-0001]
related:
  - ../../../contracts/domains/hydrology/streamflow_qc_context_assessment.md
  - ../../../schemas/contracts/v1/domains/hydrology/streamflow_qc_context_assessment.schema.json
  - ../../../apps/explorer-web/src/adapters/StreamflowQcDashboardProjection.ts
  - ../../../apps/explorer-web/src/features/streamflow_qc_dashboard/README.md
  - ../../../fixtures/ui/streamflow_qc_dashboard_projection/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 32 Streamflow QC Dashboard Source Map

## Source candidate

| Candidate | Source statement | Source spec hash |
|---|---|---|
| KFM-P32-IDEA-0002 | Use percentile, drought, adjacent-gauge, and integrity context to distinguish regional low-flow evidence from a local signal that needs review. | sha256:dabbc806be96d4b66132a4c3cd4b6ceaecd0d043bbd6d838a67c771f52db0f0b |
| KFM-P32-FEAT-0001 | Operators should see low-flow percentile state, drought context, adjacent-gauge contrast, and recalibration priority in one evidence-visible view. | sha256:b1918f996e70f5ba901cf5e5979e2c2f00672e2486caa064ccbaf56f6fb0ae4b |

The source review used the supplied consolidated Pass 23–32 domain atlas and matching connected Drive corpus. Private Drive locators are intentionally excluded from this repository document.

## Repository reconciliation

The current main branch already contains the STREAMFLOW_QC_CONTEXT_V1 contract, schema, validator, fixtures, tests, and source map. That packet is explicitly a non-UI precursor and does not implement a dashboard or route. Repository and pull-request review found no bounded dashboard on the reconciled base.

The implementation consumes a closed projection derived after the existing assessment. It does not call WaterWatch, NWIS, drought, or gauge sources and does not duplicate or replace the domain validator.

## Bounded adaptation

The implementation provides:

- finite regional-context, local-review, no-escalation, hold, deny, and error states;
- a deterministic identity check between assessment_id and spec_hash;
- display of declared flow, adjacent-gauge, drought, ingest, unit, cadence, and review-priority classifications;
- a bounded, sorted list of opaque EvidenceRefs;
- exact-field rejection and semantic checks aligned to the existing domain contract;
- fixture-backed unit and browser coverage for positive and negative paths.

The source phrase recalibration priority is adapted as review priority only. No recalibration command, threshold, detector write, or sensor-invalidity conclusion is introduced.

## Source pressure and response

| Source pressure | Bounded repository response |
|---|---|
| Low-flow percentile context | Display the finite LOW_PERCENTILE, NOT_LOW, or UNKNOWN classification; never expose or calculate a number. |
| Drought context | Display the predeclared finite context; never infer a drought event. |
| Adjacent-gauge contrast | Display the predeclared count and corroboration state with opaque evidence references. |
| Recalibration priority | Display ROUTINE, ELEVATED, HIGH, or NONE as review routing only. |
| Evidence-visible view | Render sorted EvidenceRefs without resolving them or exposing source payloads. |

## Directory Rules basis

The adapter and feature remain under apps/explorer-web; synthetic packets remain under fixtures/ui; executable tests remain with the Explorer application; source reconciliation remains under docs/intake/exploratory; and the generated receipt remains under data/receipts/generated. This follows DIR-PLACE-002, DIR-PLACE-005, DIR-EXEC-001, and DIR-DEP-002 without creating a new root or bypassing the governed API boundary.

## Explicit non-effects

This packet does not fetch a source, expose a raw flow value, compute a percentile, set a threshold, invalidate a sensor, declare a hydrologic event, mutate detector configuration, evaluate policy, approve review, change lifecycle state, release, deploy, or publish. Missing, malformed, contradictory, or direct-store-shaped input fails closed without reflecting unknown fields.

## Rollback

Close the draft or revert the additive adapter, feature, fixtures, tests, source map, and receipt. No source, detector, sensor, release, deployment, or publication state is changed.
