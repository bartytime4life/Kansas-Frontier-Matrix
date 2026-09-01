<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/prompts/kfm-hourly-archaeology-domain-builder
title: KFM Hourly Archaeology Domain Builder — Governed Task Specification
type: prompt
version: v1.0.0
status: proposed; portable; inert-as-repository-content
owners: OWNER_TBD - repository steward; archaeology docs steward; coordination steward
created: 2026-09-01
updated: 2026-09-01
policy_label: archaeology; recurrent-task; evidence-first; no-activation
owning_root: docs/
responsibility: Portable, evidence-first archaeology-domain task packet for governed hourly improvement passes with strict sensitivity boundaries and no repository mutation authority unless separately activated.
truth_posture: cite-or-abstain
related:
  - ../domains/archaeology/README.md
  - ../adr/ADR-archaeology-exact-location-policy.md
  - ../../.github/workflows/archaeology-evidence-bundle-convergence.yml
  - ../../.github/ISSUE_TEMPLATE/README.md
notes:
  - "This task packet is repository documentation only. It does not by itself activate a recurrence, schedule a runner, or authorize writes."
  - "Activation requires a current authenticated scheduler or scheduled-task service with GitHub and Notion access that preserves the task marker, concurrency ceiling, archaeology sensitivity rules, and non-effects below."
  - "The repository placement and directly referenced controls were reconciled against current main at the active checkpoint in the issue description; this file remains a portable task packet, not a binding live-run log."
[/KFM_META_BLOCK_V2] -->

RUN KFM_HOURLY_ARCHAEOLOGY_BUILDER_V1

# KFM Hourly Archaeology Domain Builder — Governed Task Specification

> [!IMPORTANT]
> This repository file is inert prompt documentation. It does not activate a recurring task, schedule an agent, authorize repository mutation, or create repository writes. A current authenticated scheduler or scheduled-task service with GitHub and Notion access must separately activate the run while preserving the task marker, one-PR ceiling, archaeology sensitivity controls, and explicit non-effects below.

## Status

**PROPOSED recurring-task specification / coordination anchor.**
**Recurring trigger: NOT ACTIVE.** This issue does not schedule an agent, activate a workflow, or authorize background repository mutation.

Task marker: `KFM_HOURLY_ARCHAEOLOGY_BUILDER_V1`

## Mission

Run one serialized, evidence-first archaeology-domain improvement pass per hour. Each eligible run may inspect, reconcile, build, update, or fix **one small dependency-closed archaeology slice** and its directly necessary related files. A healthy run may end with `MONITORING`, `BLOCKED`, or `NO_ACTION`; it is not required to create an hourly pull request.

## Current preparation checkpoint

- Repository: `bartytime4life/Kansas-Frontier-Matrix`
- Observed `main`: `00975217b7df6e7a0bc68fc1ba429bea02067a00`
- Open PR observed: bartytime4life/Kansas-Frontier-Matrix#3666, MapLibre acquisition-inventory hardening; no archaeology path overlap was identified during preparation.
- Open archaeology-specific PRs observed: none.
- Broad overlap constraint: bartytime4life/Kansas-Frontier-Matrix#2874, source-corpus reconciliation.
- Existing archaeology implementation surfaces include domain docs, contracts, schema projections, policy scaffolds, validators, fixtures, lifecycle lanes, runbooks, governed-API seams, receipts/proofs, and `.github/workflows/archaeology-evidence-bundle-convergence.yml`. This task must inspect current main rather than scaffold a parallel lane.

These observations are a preparation checkpoint, not a permanently pinned execution base. Every run must re-pin current main and active work.

## Archaeology trust boundary

- Public or semi-public exact and reverse-engineerable archaeological location exposure defaults to `DENY`.
- Protected geometry must never be sent to a public client and hidden only through styling, filters, or feature-state.
- Burial sites, human remains, sacred/culturally restricted places, unresolved cultural or sovereignty concerns, private-land associations, collection-security details, and looting-risk data fail closed.
- LiDAR, aerial, satellite, geophysical, predictive, statistical, and model outputs remain candidate evidence; they do not automatically establish an `ArchaeologicalSite`.
- Generalization is not release authority. A public-safe derivative still requires evidence, rights/consent, cultural and sovereignty review, sensitivity, transform lineage, policy, validation, release, correction, withdrawal, and rollback closure.
- Use synthetic, generalized, non-sensitive, no-network fixtures by default.

## Authority and terminal ceiling

- GitHub is implementation authority.
- Accepted ADRs and adopted Directory Rules govern placement and architecture.
- Notion is coordination only.
- Google Drive is read-only doctrine, research, and candidate-idea lineage.

Allowed: inspect; reconcile; create or reuse one task-owned feature branch; edit reversible repository content; run focused validation; commit; push; open or update one draft PR; update Notion coordination.

Not allowed: direct writes to main; force-push; approval; marking ready; merge; release; deployment; promotion; publication; live source admission or activation; protected-data retrieval; repository settings, permissions, secrets, rulesets, environments, or branch-protection changes.

## Concurrency law

1. Pin current main and inspect every open PR, active branch, recent merge, relevant issue, and Notion work item.
2. Search for `KFM_HOURLY_ARCHAEOLOGY_BUILDER_V1`.
3. Maximum active output: one task-owned open PR.
4. If a task-owned PR exists, reconcile or advance only that PR.
5. Do not take over non-task-owned work. Return `BLOCKED` with exact paths, owner, and head when overlap exists.
6. Re-pin immediately before branch creation and push.

## Candidate priority

1. Exact/reconstructive archaeology-location fail-open risk.
2. Candidate-versus-confirmed source-role collapse.
3. Materially false current status that could cause unsafe action.
4. Broken `EvidenceRef -> EvidenceBundle` closure.
5. Nearly complete contract-schema-fixture-validator-test seam.
6. Deterministic no-network negative proof that removes an implementation HOLD.
7. Public-safe transform-receipt, inference-check, correction, withdrawal, or rollback closure.
8. Compatibility convergence that removes parallel/permissive authority.
9. Implementation-blocking documentation correction.

## Delivery contract

- Branch: `automation/hourly-archaeology/<short-scope>-<YYYYMMDD>`
- PR marker: `KFM_HOURLY_ARCHAEOLOGY_BUILDER_V1`
- Maximum: one coherent draft PR or one exact no-change result.
- PR body must record goal, observed main, base/head SHAs, changed paths, Directory Rules basis, dependencies, non-goals, focused and aggregate validation, hosted status, introduced/inherited failures, source effects, rights/sensitivity effects, rollback, and explicit non-effects.
- Preserve draft state. No merge, release, deployment, promotion, or publication effect.

## Run outcomes

`ADVANCED_TASK_PR` · `OPENED_DRAFT_PR` · `UPDATED_COORDINATION` · `MONITORING` · `BLOCKED` · `NO_ACTION` · `ERROR`

## Operating specification

The complete prompt, source ledger, first-run handoff, validation guidance, and activation boundary are in the read-only Google Drive task document:

https://docs.google.com/document/d/1YTyNTAyVQYkAm1Hh8spioWx2LqFPkMD7OoX9pvbFzGM/edit?usp=drivesdk

Relevant repository anchors:

- `docs/domains/archaeology/README.md`
- `docs/adr/ADR-archaeology-exact-location-policy.md`
- `.github/workflows/archaeology-evidence-bundle-convergence.yml`
- issue bartytime4life/Kansas-Frontier-Matrix#2874

## Activation boundary

This issue and the linked Drive document define the task but do not activate the recurrence. Activation requires an authenticated scheduler or scheduled-task service with GitHub and Notion access. The scheduler must preserve the task marker, one-PR concurrency ceiling, archaeology sensitivity rules, and explicit non-effects above.

---

## Minimal zero-authority activation contract

This task packet remains inert until a scheduler or orchestrator issues a fresh, attributable run request that includes all of the following as direct human-visible task input:

1. exact repository and branch target;
2. exact current base SHA and branch head to be reconciled;
3. the `KFM_HOURLY_ARCHAEOLOGY_BUILDER_V1` marker;
4. the allowed archaeology slice and relevant change boundary;
5. the required validation, source-guard, and no-network posture; and
6. the explicit ceiling: one task-owned PR, no merge, no release, no publication, and no protected-data retrieval.

Without all six, the run remains `NO_ACTION` or `BLOCKED` rather than granted mutation authority.
