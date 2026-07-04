# `release/reviews/` — Release Review Lane

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-reviews-blueviolet)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/reviews/` holds governed release-review records.

A release review records whether a candidate, manifest, correction, notice, or release-facing item is ready, held, deferred, repaired, superseded, or needs more evidence, validation, policy, or steward review.

A review is not a release. Review prose does not make an output public. Release requires governed records, validation support, steward decision, manifest readiness, correction path, and reversal posture where applicable.

## Status & authority

| Field | Value |
|---|---|
| Document type | Release-review parent README |
| Owning root | `release/` |
| Lane | `release/reviews/` |
| Status | Draft |
| Authority level | Parent guidance and index. Actual review records, manifests, validation receipts, evidence records, policy reviews, correction records, release-history records, and steward decisions outrank this README. |
| Default posture | Do not release from prose alone. Require governed review records and steward decision. |
| Required reviewers | Release steward, data steward, affected domain steward, and docs steward; policy reviewer when needed. |

## Repo fit

```text
release/
├── reviews/       # you are here
│   └── atmosphere/
├── candidates/
├── manifests/
├── decisions/
├── promotion_decisions/
├── changelog/
├── correction/
├── corrections/
└── correction_notices/
```

This path belongs under the `release/` responsibility root because it records release-review state. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## Current sublanes

| Sublane | Scope | Status |
|---|---|---|
| `atmosphere/` | Atmosphere release-review records. | Draft sublane README exists. |

Add new domain sublanes only when a release-review record family needs domain-specific fields, steward ownership, time posture, policy posture, or handoff notes.

## Review responsibilities

| Responsibility | Expectation |
|---|---|
| Identity | Provide a stable release-review ID. |
| Review target | Link the candidate, manifest, correction, notice, or release item being reviewed. |
| Scope | State the domain, layer family, artifact family, time posture, or release target. |
| Evidence | Link evidence records when release claims depend on evidence. |
| Validation | Link validation receipts or checks. |
| Policy posture | Link policy review when release posture requires it. |
| Decision support | Record review recommendation and reason. |
| Manifest handoff | Link the manifest path when review supports release preparation. |
| Correction path | Link correction records when repair or correction is required. |
| History path | Link release-history records when the review changes release state. |

## What belongs here

- Parent README and sublane indexes.
- Release-review records.
- Release-readiness checklists.
- Steward review summaries.
- Evidence, validation, policy, and release-posture review notes.
- Links to candidates, manifests, validation receipts, evidence records, policy reviews, correction records, notices, decisions, and release-history entries.
- Notes explaining review status, release-facing effect, public posture, and follow-up tasks.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exports, service payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy files, or validator code.
- Generated summaries used as release evidence or final approval.
- Final publication approval without release-steward review.
- Silent promotion by moving files between lifecycle paths.

## Review outcomes

| Outcome | Meaning |
|---|---|
| `READY_FOR_DECISION` | Review is complete enough for release-steward decision. |
| `READY_FOR_MANIFEST` | Review supports manifest preparation or update. |
| `HOLD_FOR_EVIDENCE` | Evidence is incomplete or unresolved. |
| `HOLD_FOR_VALIDATION` | Validation is incomplete or unresolved. |
| `HOLD_FOR_POLICY` | Policy review is incomplete or unresolved. |
| `REPAIR_REQUIRED` | Reviewed item needs correction before next step. |
| `SUPERSEDED` | Reviewed item has been replaced by a newer item. |
| `NO_ACTION` | No release-state change is recommended. |

## Required release-review fields

- Review ID
- Review status
- Review outcome
- Review target pointer
- Domain or layer scope
- Proposed release target, when applicable
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Policy review pointer, when applicable
- Time posture, when applicable
- Manifest pointer, when applicable
- Decision pointer, when applicable
- Correction pointer, when applicable
- Release-history pointer, when applicable
- Review reason
- Review date
- Reviewing steward
- Follow-up items

## Minimal release-review record

```markdown
# <review-id>

## Status
DRAFT / READY_FOR_REVIEW / APPROVED / HELD / SUPERSEDED / CORRECTED / NO_ACTION

## Review outcome
READY_FOR_DECISION / READY_FOR_MANIFEST / HOLD_FOR_EVIDENCE / HOLD_FOR_VALIDATION / HOLD_FOR_POLICY / REPAIR_REQUIRED / SUPERSEDED / NO_ACTION

## Review target
<release/candidates/... or manifest/decision/correction pointer>

## Scope
<domain, layer family, artifact family, time posture, or release target>

## Proposed release target
<release target or N/A>

## Governed support pointers
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Policy review: <path or N/A>
- Manifest: <path or N/A>
- Decision: <path or N/A>
- Correction: <path or N/A>
- Release history: <path or N/A>

## Review reason
<short reason grounded in evidence, validation, policy, or steward review>

## Review date
<YYYY-MM-DD>

## Reviewing steward
<steward or maintainer>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Review target pointer is present.
- [ ] Scope is clear.
- [ ] Proposed release target is stated or marked N/A.
- [ ] Evidence support is linked when release claims depend on evidence.
- [ ] Validation support is linked when validation is required.
- [ ] Policy review is linked when release posture requires it.
- [ ] Time posture is stated when relevant.
- [ ] Review outcome is one of the finite outcomes above.
- [ ] Review reason is recorded.
- [ ] Manifest or decision handoff is linked when review supports release state change.
- [ ] Correction and release-history pointers are linked when applicable.
- [ ] No data payloads are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<scope>_release-review.md
```

Examples:

```text
2026-07-03_atmosphere-weather-summary_release-review.md
2026-07-03_hydrology-stream-layer_release-review.md
2026-07-03_fauna-range-summary_release-review.md
```

## Open verification

- [ ] Confirm CODEOWNERS for `release/reviews/`.
- [ ] Confirm release-review ID format.
- [ ] Confirm release-review filename convention.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm policy review pointer format.
- [ ] Confirm manifest, decision, correction, and release-history pointer formats.
- [ ] Confirm whether release-review records require schema validation before manifest handoff or release decision.
- [ ] Confirm whether `release/reviews/` should remain distinct from `release/decisions/` and `release/promotion_decisions/`.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | First parent-level release review, new domain sublane, manifest handoff, validation receipt update, policy review, correction, or changelog integration |
