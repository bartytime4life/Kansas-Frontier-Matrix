<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/expansion-backlog
title: Soil - Expansion Backlog
type: domain-expansion-backlog
version: v1.0
status: active; repository-grounded; proposed-work
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Program steward
created: 2026-05-19
updated: 2026-08-28
policy_label: public
owning_root: docs/
responsibility: Dependency-ordered Soil improvement queue; does not authorize implementation, source activation, release, or publication
truth_posture: CONFIRMED current-session gap inventory / PROPOSED dependency order and candidate work / UNKNOWN future review, implementation, release, and operational state
evidence_snapshot: "repository=bartytime4life/Kansas-Frontier-Matrix; base_commit=813ef14b1dbe5bd236fc902ce8fc3bb2e8ae7e80"
related:
  - docs/domains/soil/README.md
  - docs/domains/soil/VERIFICATION_BACKLOG.md
  - docs/domains/soil/MISSING_OR_PLANNED_FILES.md
  - docs/domains/soil/EXPANSION_PLAN.md
  - docs/domains/soil/DEFINITION_OF_DONE.md
tags: [kfm, soil, backlog, dependency-closed, fixtures, validators, evidence, release-hold]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil expansion backlog

This queue selects small, reversible Soil improvements from current repository
evidence and the supplied Soil architecture report. The report's minimum slice
- SSURGO/SDA lineage, station moisture, support-type separation, validators,
receipts, catalog closure, and PMTiles delivery - remains useful design lineage.
Current repository state already implements portions of that slice, so the
queue starts from the remaining gaps rather than recreating proposed paths.

## Selection law

A candidate is eligible only when it has one authority owner, verified path
placement, no open path collision, dependency closure, public-safe synthetic
fixtures, finite outcomes, proportional validation, and a one-commit or
documented forward-fix rollback. A healthy pass may end with no code change.

## Dependency-ordered queue

| Priority | ID | Candidate | Current state | Acceptance boundary |
|---:|---|---|---|---|
| 0 | `SOIL-EXP-001` | Reconcile Soil planning registers | `IN_PROGRESS` in this bounded docs repair | Placeholder files are replaced by exact-main inventories; no source, policy, release, or runtime claim changes |
| 0 | `SOIL-EXP-002` | Refresh the Soil README and architecture maturity claims | `READY_CANDIDATE` | Current implemented profiles, placeholders, workflow scope, exact snapshot, and holds agree across docs without broad rewrite |
| 0 | `SOIL-EXP-003` | Replace short `VERIFICATION.md`, `DEFINITION_OF_DONE.md`, `EXPANSION_PLAN.md`, `FILE_SYSTEM_PLAN.md`, `PRESERVATION_MATRIX.md`, `MAP_UI_CONTRACTS.md`, and `RELEASE_INDEX.md` scaffolds one coherent family at a time | `DEPENDENCY_READY` | Each file is grounded in exact paths and explicit non-effects; no proposed path becomes authority |
| 0 | `SOIL-EXP-004` | Assign accountable Soil roles | `BLOCKED_OWNER_DECISION` | Owner/reviewer route is explicit; no self-approval or CODEOWNERS-as-review claim |
| 1 | `SOIL-EXP-005` | Bind the existing SoilMoistureObservation fixture profile into `domain-soil` | `READY_CANDIDATE` | Existing schema, 14 fixtures, validator, contract, and test run under the shared no-network startup guard; workflow summary preserves `PROPOSED_INACTIVE` and no-authority boundaries |
| 1 | `SOIL-EXP-006` | Inventory every Soil validator/test profile against CI | `READY_CANDIDATE` | Each profile is classified `ACTIVE`, `ISOLATED`, `PLACEHOLDER`, `COMPATIBILITY`, or `HOLD`; no path presence is counted as coverage |
| 1 | `SOIL-EXP-007` | Converge support-type vocabulary | `BLOCKED_SEMANTIC_REVIEW` | One semantic contract, alias map, strict schema, positive/negative fixtures, consumer crosswalk, and deprecation plan agree |
| 1 | `SOIL-EXP-008` | Classify permissive and compatibility Soil schemas | `DEPENDENCY_READY` | Every permissive/alias schema has a canonical target or explicit hold, consumer evidence, negative-test posture, and retirement/rollback rule |
| 1 | `SOIL-EXP-009` | Close one SSURGO map-unit/component/horizon fixture chain | `PARTIAL` | Synthetic MUKEY/COKEY/CHKEY lineage, horizon bounds, source vintage, query/spec hash, deterministic identity, exact findings, and no-network proof pass together |
| 1 | `SOIL-EXP-010` | Reconcile human and machine Soil planning registers | `BLOCKED_PROJECTION_CONTRACT` | Single writer, schema, digest binding, parity validator, correction path, and cross-domain register relationship are accepted |
| 2 | `SOIL-EXP-011` | Reconcile Soil source-registry aliases and duplicate identities | `BLOCKED_AUTHORITY_REVIEW` | Canonical source IDs, aliases, writers, consumers, migration steps, and rollback are recorded before new writes |
| 2 | `SOIL-EXP-012` | Prepare one source-admission packet without activation | `BLOCKED_RIGHTS_REVIEW` | Current terms, role, steward, sensitivity, cadence, attribution, deterministic fixtures, validators, correction, and rollback are complete |
| 2 | `SOIL-EXP-013` | Implement one offline ingest-to-PROCESSED fixture path | `BLOCKED_DEPENDENCIES` | Source decision, contract, strict schema, identity, policy, fixtures, validator, receipt, and quarantine behavior close first; no live fetch |
| 2 | `SOIL-EXP-014` | Bind substantive Soil policy evaluation | `BLOCKED_POLICY_PROFILE` | Pinned evaluator, reviewed policies, finite decisions, fail-closed fixtures, decision receipt, and no-network CI pass |
| 3 | `SOIL-EXP-015` | Resolve one Soil EvidenceBundle and catalog candidate | `BLOCKED_EVIDENCE_CLOSURE` | EvidenceRef resolution, source/rights/sensitivity state, validation, catalog identity, correction, and rollback are reviewable |
| 3 | `SOIL-EXP-016` | Produce one proof packet | `BLOCKED_CATALOG_CLOSURE` | Immutable inputs/outputs, receipts, policy state, review state, exact digests, and proof validator close without release claims |
| 3 | `SOIL-EXP-017` | Execute a candidate-specific release dry run | `BLOCKED_PROOF_AND_REVIEW` | Prior target, correction, withdrawal, rollback, cache/derivative invalidation, independent review, and public readback plan are present |
| 4 | `SOIL-EXP-018` | Add governed API and Evidence Drawer resolution | `BLOCKED_RELEASED_CARRIER` | Public-safe released fixture carrier resolves through governed interfaces with citations, support type, time caveat, stale/deny states, and no internal-store access |
| 4 | `SOIL-EXP-019` | Add bounded Focus Mode interpretation | `BLOCKED_GOVERNED_RESOLVER` | EvidenceBundle-only context; ANSWER cites, ABSTAIN narrows, DENY protects, ERROR does not answer; AI receipt and rollback state remain visible |

## Recommended next implementation slice

After this documentation repair, `SOIL-EXP-005` is the smallest executable
candidate: the contract, strict schema, six valid fixtures, eight reviewed
invalid fixtures, validator, and focused test already exist. The change should
only inject the shared startup no-network guard, add that existing suite to the
Soil workflow, and update the workflow's scope statement. It must not activate
a source or widen the fixture profile.

## Non-effects

This backlog does not admit SSURGO, SDA, Mesonet, SCAN, USCRN, SMAP, SoilGrids,
or any other source. It does not retrieve production data, establish scientific
fitness, expose field- or person-specific data, mutate lifecycle stores, accept
policy, resolve evidence, approve a candidate, release, deploy, promote, or
publish.

[Back to top](#top)
