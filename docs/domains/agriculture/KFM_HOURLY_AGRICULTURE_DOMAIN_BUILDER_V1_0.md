# KFM Hourly Agriculture Domain Builder v1.0

**Issue anchor:** `bartytime4life/Kansas-Frontier-Matrix#3668`  
**Parent automation design:** `bartytime4life/Kansas-Frontier-Matrix#3663`  
**Status:** `PROPOSED TASK SPECIFICATION / RECURRING TRIGGER NOT ACTIVE`  
**Operational state (2026-08-29 update):** `PAUSED / BLOCKED`

This document records one serialized, evidence-first hourly builder contract for the Agriculture domain. It is a coordination and verification specification only.

It does **not** create or authorize a scheduler, workflow trigger, branch, pull request, source activation, release, deployment, promotion, or publication path.

## Task contract

```yaml
task_id: KFM_HOURLY_AGRICULTURE_DOMAIN_BUILDER_V1_0
repository: bartytime4life/Kansas-Frontier-Matrix
cadence: hourly
execution_mode: serialized
implementation_authority: current GitHub repository evidence
coordination_projection: Notion
read_only_lineage: Google Drive
parent_automation_design: issue-3663
pr_marker: KFM_HOURLY_AGRICULTURE_BUILDER_V1
max_task_owned_open_prs: 1
default_delivery: DRAFT_PR_OR_EXACT_NO_CHANGE
allowed_run_outcomes:
  - ADVANCED_TASK_PR
  - OPENED_DRAFT_PR
  - UPDATED_COORDINATION
  - MONITORING
  - BLOCKED
  - NO_ACTION
  - ERROR
terminal_ceiling: DRAFT_PR
merge: false
release: false
deployment: false
promotion: false
publication: false
source_activation: false
production_data_retrieval: false
repository_settings_change: false
self_approval: false
```

## Canonical coordination and lineage links

- Notion coordination page: <https://app.notion.com/p/3caa92021bf6814bb884ed13a2923c19?pvs=204>
- Drive specification (read-only lineage): <https://docs.google.com/document/d/1v7LTGH7V0Th4aGzqYywh7DoPe-vJRlrTTkvQm7aWsaA/edit?usp=drivesdk>
- Drive Agriculture lineage dossier (read-only): <https://drive.google.com/file/d/1TkFtqaDDtR9CiiEDdqGsyLgc2dDLX4qr/view?usp=drivesdk>

GitHub repository evidence remains implementation authority.

## Setup re-pin and reconciliation state

- Final setup re-pin checkpoint: `main@129ac47f359be143ce8bbe43d8401f8660b8be5f`
- Latest observed merge at that checkpoint: PR `#3666`
- Duplicate issue `#3669` closed as duplicate; canonical anchor remains `#3668`
- Duplicate Notion page marked superseded and redirected to the canonical page
- Resume-gate evidence checkpoint references `main@83ace64d7451eca641cbe9f3b6fe86eb0867cb0e`

Every execution attempt must re-pin current `main` and open work immediately before any delivery action.

## Agriculture boundary and source-role posture

Agriculture-owned surfaces may be advanced, plus only the smallest direct dependencies needed for one reviewable outcome. Agriculture may consume governed outputs from Soil, Hydrology, Atmosphere, Hazards, Flora, People-DNA-Land, and map/runtime surfaces, but must not redefine those lanes' canonical truth.

Source-role separation remains mandatory:

- SSURGO/SDA: vector and tabular soil authority
- gSSURGO: derived gridded support
- Kansas Mesonet, SCAN, USCRN: station observations
- SMAP: satellite/grid soil-moisture products
- HLS/HLS-VI: remote-sensing observations and derived indices
- NASS QuickStats/Crop Progress: aggregate statistics

A satellite grid is not field truth; aggregate statistics are not operator records; derived outputs are not sovereign evidence.

## Selection and execution constraints

Prefer candidates in this order:

1. introduced exact-head failure in the task-owned Agriculture PR;
2. materially false or stale Agriculture status with action risk;
3. broken Agriculture contract/schema/fixture/validator/test/workflow/docs binding;
4. one nearly-complete deterministic proof seam;
5. one no-network negative test or validator removing a bounded hold;
6. one compatibility or authority-convergence repair;
7. one public-safe cross-lane join repair;
8. one implementation-blocking documentation correction.

If no candidate passes bounded qualification, the valid output is `BLOCKED` or `NO_ACTION`.

## Concurrency and ownership

- Re-pin `main` and open work at run start and immediately before push.
- Search open PRs for markers `KFM_HOURLY_AGRICULTURE_BUILDER_V1` and `KFM_HOURLY_BUILDER_V1`.
- If a task-owned Agriculture PR exists, advance only that PR.
- Never take over another task's PR or use last-writer-wins.

## Validation posture

Use synthetic, public-safe, no-network fixtures by default and run only the narrowest repository-native checks needed for the selected seam, including relevant Agriculture workflows when impacted paths/contracts require them.

Validation reporting must classify outcomes separately (`PASS`, `FAIL`, `SKIPPED`, `NOT_RUN`, `CANCELLED`, `STARTUP_FAILURE`, environmental/unknown/pending).

## Rights, sensitivity, and non-effects

Field polygons, operator identities, proprietary yield, pesticide records, private farm-management data, person-parcel joins, precise private wells, and sensitive infrastructure remain deny-by-default.

Unknown rights/terms/quotas/automation permissions require `HOLD`, `DENY`, or `ABSTAIN`.

This specification does **not** authorize merge, release, deployment, promotion, publication, source activation, production retrieval, repository settings changes, secret changes, or self-approval.

## Draft-only delivery repair and resume gate (2026-08-29)

State remains `PAUSED / BLOCKED` until this evidence is satisfied:

- no competing open generic or Agriculture marker PR;
- current `main`/open work re-pinned immediately before delivery;
- PR `#3849` remains closed and unmerged, with retained branch refreshed or discarded;
- Codex P2 path-binding finding is resolved by test evidence;
- exact-head focused and dependent checks settle with truthful classification;
- one non-recurring fallback delivery survives immediate and later dual readback with no `ready_for_review` timeline event;
- either repaired draft-conversion round-trip passes, or immutable-metadata fallback mode is explicitly enforced with fail-closed closure behavior;
- this issue and canonical Notion page record exact proof before scheduler unpause.

### Required fallback before repair availability

A controlled one-shot draft PR delivery may proceed only in immutable mode:

- finalize title/body/base/head before creation;
- create once with `draft=true`;
- do not perform post-creation update calls, mark-ready calls, reviewer-request calls, approval, auto-merge, or merge;
- post later updates only as top-level comments;
- independently verify with connector read + raw REST that PR is open, unmerged, expected head/base, and `draft=true`;
- repeat verification after first comment-only update / next serialized observation and confirm no `ready_for_review` event;
- close unmerged immediately on any mismatch and keep Agriculture paused.

## Activation boundary

Hourly recurrence requires a separate scheduler activation with authenticated GitHub and Notion access. Routine execution must treat Drive as read-only lineage.
