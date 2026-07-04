# `release/promotion_decisions/hydrology/` — Hydrology Promotion Decisions

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-promotion-decisions-hydrology-readme
title: release/promotion_decisions/hydrology/ — Hydrology Promotion Decisions
version: v1
status: draft
policy_label: public
owners:
  - <hydrology-domain-steward>
  - <release-steward>
  - <data-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, release, promotion-decisions, hydrology, review, validation, evidence]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-promotion--decisions-blueviolet)
![domain](https://img.shields.io/badge/domain-hydrology-blue)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/promotion_decisions/hydrology/` holds hydrology promotion-decision records.

A promotion decision records whether a hydrology candidate may move forward into a release manifest, remain held, be repaired, be deferred, be superseded, or require correction follow-up.

Promotion is a governed state transition, not a file move. A hydrology candidate is not public merely because it appears in this lane.

## Status & authority

| Field | Value |
|---|---|
| Document type | Hydrology promotion-decision README |
| Owning root | `release/` |
| Lane | `release/promotion_decisions/hydrology/` |
| Status | Draft |
| Authority level | Review guidance and index. Actual promotion decisions, release manifests, validation receipts, evidence records, policy reviews, correction records, rollback records, and steward decisions outrank this README. |
| Default posture | Do not promote from prose alone. Require governed decision records and steward review. |
| Required reviewers | Hydrology steward, release steward, data steward, and docs steward; policy reviewer when needed. |

## Path status

This README documents the requested path: `release/promotion_decisions/hydrology/`.

Current-session evidence confirms this README existed as a blank file before this update. Current-session evidence also confirms the parent `release/promotion_decisions/README.md` is still a greenfield stub. Treat this hydrology sublane as draft until the parent promotion-decision lane is expanded.

## Repo fit

```text
release/
├── promotion_decisions/
│   └── hydrology/       # you are here
├── candidates/
│   └── hydrology/
├── manifests/
├── decisions/
├── changelog/
├── correction/
├── corrections/
└── correction_notices/
```

This path belongs under the `release/` responsibility root because it records a release-governance decision. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## Promotion decision responsibilities

| Responsibility | Expectation |
|---|---|
| Identity | Provide a stable promotion-decision ID. |
| Candidate pointer | Link the hydrology candidate being evaluated. |
| Scope | State the hydrology type, release family, time-validity posture, or release target. |
| Evidence | Link evidence records when release claims depend on evidence. |
| Validation | Link validation receipts or checks. |
| Policy posture | Link policy review when access, sensitivity, rights, or public-surface posture affects promotion. |
| Decision | Record the steward decision and reason. |
| Manifest handoff | Link the manifest path when promotion proceeds. |
| Correction path | Link correction records when repair or correction is required. |
| Rollback path | Link rollback or supersession notes when needed. |
| Changelog | Link release-history records when the decision changes release state. |

## What belongs here

- Hydrology promotion-decision records.
- Hydrology promotion-readiness checklists.
- Steward decision summaries.
- Links to hydrology candidates, manifests, validation receipts, evidence records, policy reviews, correction records, rollback records, notices, and changelog entries.
- Notes explaining decision status, release-facing effect, time-validity posture, and follow-up tasks.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exports, service payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy files, or validator code.
- Generated summaries used as release evidence.
- Final publication approval without release-steward review.

## Decision outcomes

Use a finite decision outcome where possible:

| Outcome | Meaning |
|---|---|
| `PROMOTE_TO_MANIFEST` | Candidate may proceed to manifest preparation or update. |
| `HOLD_FOR_EVIDENCE` | Evidence is incomplete or unresolved. |
| `HOLD_FOR_VALIDATION` | Validation is incomplete or unresolved. |
| `HOLD_FOR_POLICY` | Policy or public-surface review is incomplete or unresolved. |
| `REPAIR_REQUIRED` | Candidate needs correction before promotion. |
| `SUPERSEDE_CANDIDATE` | Candidate should be replaced by a newer candidate. |
| `NO_ACTION` | No release-state change is authorized. |

## Required promotion-decision fields

- Decision ID
- Decision status
- Decision outcome
- Hydrology candidate pointer
- Hydrology scope
- Proposed release target
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Policy review pointer, when applicable
- Manifest pointer, when applicable
- Correction pointer, when applicable
- Rollback or supersession pointer, when applicable
- Changelog pointer, when applicable
- Decision reason
- Decision date
- Deciding steward
- Follow-up items

## Minimal promotion-decision record

```markdown
# <decision-id>

## Status
DRAFT / READY_FOR_REVIEW / APPROVED / HELD / SUPERSEDED / CORRECTED / NO_ACTION

## Decision outcome
PROMOTE_TO_MANIFEST / HOLD_FOR_EVIDENCE / HOLD_FOR_VALIDATION / HOLD_FOR_POLICY / REPAIR_REQUIRED / SUPERSEDE_CANDIDATE / NO_ACTION

## Hydrology candidate
<release/candidates/hydrology/... or N/A>

## Hydrology scope
<waterbody, watershed, stream, aquifer, gauge, flow, time-validity scope, artifact family, or release target>

## Proposed release target
<release target or N/A>

## Governed support pointers
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Policy review: <path or N/A>
- Manifest: <path or N/A>
- Correction: <path or N/A>
- Rollback or supersession: <path or N/A>
- Changelog: <path or N/A>

## Decision reason
<short reason grounded in evidence, validation, policy, or steward review>

## Decision date
<YYYY-MM-DD>

## Deciding steward
<steward or maintainer>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Candidate pointer is present.
- [ ] Hydrology scope is clear.
- [ ] Proposed release target is stated or marked N/A.
- [ ] Evidence support is linked when release claims depend on evidence.
- [ ] Validation support is linked when validation is required.
- [ ] Policy review is linked when public-surface posture requires it.
- [ ] Decision outcome is one of the finite outcomes above.
- [ ] Decision reason is recorded.
- [ ] Manifest handoff is linked when promotion proceeds.
- [ ] Correction, rollback, supersession, and changelog pointers are linked when applicable.
- [ ] No data payloads are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<hydrology-scope>_promotion-decision.md
```

Examples:

```text
2026-07-03_hydrology-watershed-summary_promotion-decision.md
2026-07-03_hydrology-stream-layer_promotion-decision.md
2026-07-03_hydrology-time-validity_promotion-decision.md
```

## Open verification

- [ ] Expand `release/promotion_decisions/README.md` so this hydrology lane inherits from a complete parent contract.
- [ ] Confirm CODEOWNERS for `release/promotion_decisions/hydrology/`.
- [ ] Confirm promotion-decision ID format.
- [ ] Confirm promotion-decision filename convention.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm policy review pointer format.
- [ ] Confirm manifest, correction, rollback, supersession, and changelog pointer formats.
- [ ] Confirm whether promotion-decision records require schema validation before manifest handoff.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Parent lane expansion, first hydrology promotion decision, manifest handoff, validation receipt update, policy review, correction, rollback, or changelog integration |
