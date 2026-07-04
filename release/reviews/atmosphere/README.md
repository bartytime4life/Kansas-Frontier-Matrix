# `release/reviews/atmosphere/` — Atmosphere Release Reviews

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-reviews-atmosphere-readme
title: release/reviews/atmosphere/ — Atmosphere Release Reviews
version: v1
status: draft
policy_label: public
owners:
  - <atmosphere-domain-steward>
  - <release-steward>
  - <data-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, release, reviews, atmosphere, validation, evidence, publication]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-reviews-blueviolet)
![domain](https://img.shields.io/badge/domain-atmosphere-skyblue)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/reviews/atmosphere/` holds atmosphere release-review records.

A release review records whether an atmosphere candidate, manifest, correction, notice, or release-facing artifact family is ready, held, deferred, repaired, superseded, or requires additional evidence, validation, policy, or steward review.

A review is not a release. Review prose does not make an atmosphere output public. Release requires governed records, validation support, steward decision, manifest readiness, correction path, and rollback posture where applicable.

## Status & authority

| Field | Value |
|---|---|
| Document type | Atmosphere release-review README |
| Owning root | `release/` |
| Lane | `release/reviews/atmosphere/` |
| Status | Draft |
| Authority level | Review guidance and index. Actual review records, release manifests, validation receipts, evidence records, policy reviews, correction records, rollback records, and steward decisions outrank this README. |
| Default posture | Do not release from prose alone. Require governed review records and steward decision. |
| Required reviewers | Atmosphere steward, release steward, data steward, and docs steward; policy reviewer when public-facing risk exists. |

## Path status

This README documents the requested path: `release/reviews/atmosphere/`.

Current-session evidence confirms this README existed as a blank file before this update. Current-session evidence also confirms `release/reviews/README.md` was not found. Treat this atmosphere sublane as draft until the parent `release/reviews/` lane is created or confirmed.

## Repo fit

```text
release/
├── reviews/
│   └── atmosphere/       # you are here
├── candidates/
│   └── atmosphere/
├── manifests/
├── decisions/
├── changelog/
├── correction/
├── corrections/
└── correction_notices/
```

This path belongs under the `release/` responsibility root because it records release-governance review state. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## Release review responsibilities

| Responsibility | Expectation |
|---|---|
| Identity | Provide a stable release-review ID. |
| Review target | Link the atmosphere candidate, manifest, correction, notice, or release item being reviewed. |
| Scope | State atmosphere type, time-validity posture, artifact family, layer family, or release target. |
| Evidence | Link evidence records when release claims depend on evidence. |
| Validation | Link validation receipts or checks. |
| Policy posture | Link policy review when rights, sensitivity, access, or public-surface posture affects release. |
| Time validity | State temporal coverage, refresh expectation, stale-state posture, or version context when relevant. |
| Decision support | Record review recommendation and reason. |
| Manifest handoff | Link manifest path when review supports promotion or release preparation. |
| Correction path | Link correction records when repair or correction is required. |
| Rollback path | Link rollback or supersession notes when needed. |
| Changelog | Link release-history records when the review changes release state. |

## What belongs here

- Atmosphere release-review records.
- Atmosphere release-readiness checklists.
- Steward review summaries.
- Evidence, validation, policy, and time-validity review notes.
- Links to atmosphere candidates, manifests, validation receipts, evidence records, policy reviews, correction records, rollback records, notices, and changelog entries.
- Notes explaining review status, release-facing effect, public-surface posture, and follow-up tasks.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exports, service payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy files, or validator code.
- Generated summaries used as release evidence or final approval.
- Final publication approval without release-steward review.
- Credentials or private operational material.

## Review outcomes

Use a finite review outcome where possible:

| Outcome | Meaning |
|---|---|
| `READY_FOR_DECISION` | Review is complete enough for release-steward decision. |
| `READY_FOR_MANIFEST` | Review supports manifest preparation or update. |
| `HOLD_FOR_EVIDENCE` | Evidence is incomplete or unresolved. |
| `HOLD_FOR_VALIDATION` | Validation is incomplete or unresolved. |
| `HOLD_FOR_POLICY` | Policy or public-surface review is incomplete or unresolved. |
| `REPAIR_REQUIRED` | Candidate or release item needs correction before next step. |
| `SUPERSEDED` | Reviewed item has been replaced by a newer item. |
| `NO_ACTION` | No release-state change is recommended. |

## Required release-review fields

- Review ID
- Review status
- Review outcome
- Review target pointer
- Atmosphere scope
- Proposed release target, when applicable
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Policy review pointer, when applicable
- Time-validity posture, when applicable
- Manifest pointer, when applicable
- Decision pointer, when applicable
- Correction pointer, when applicable
- Rollback or supersession pointer, when applicable
- Changelog pointer, when applicable
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
<release/candidates/atmosphere/... or manifest/decision/correction pointer>

## Atmosphere scope
<weather, climate, air-quality, time-validity scope, artifact family, layer family, or release target>

## Proposed release target
<release target or N/A>

## Governed support pointers
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Policy review: <path or N/A>
- Manifest: <path or N/A>
- Decision: <path or N/A>
- Correction: <path or N/A>
- Rollback or supersession: <path or N/A>
- Changelog: <path or N/A>

## Time-validity posture
<coverage, refresh expectation, stale-state posture, version context, or N/A>

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
- [ ] Atmosphere scope is clear.
- [ ] Proposed release target is stated or marked N/A.
- [ ] Evidence support is linked when release claims depend on evidence.
- [ ] Validation support is linked when validation is required.
- [ ] Policy review is linked when public-surface posture requires it.
- [ ] Time-validity posture is stated when relevant.
- [ ] Review outcome is one of the finite outcomes above.
- [ ] Review reason is recorded.
- [ ] Manifest or decision handoff is linked when review supports release state change.
- [ ] Correction, rollback, supersession, and changelog pointers are linked when applicable.
- [ ] No data payloads are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<atmosphere-scope>_release-review.md
```

Examples:

```text
2026-07-03_atmosphere-weather-summary_release-review.md
2026-07-03_atmosphere-air-quality-layer_release-review.md
2026-07-03_atmosphere-time-validity_release-review.md
```

Use lowercase filenames, hyphenated scope names, and stable review IDs. Avoid renaming approved review records unless a migration note explains the change.

## Open verification

- [ ] Create or confirm `release/reviews/README.md` so this atmosphere lane inherits from a complete parent contract.
- [ ] Confirm CODEOWNERS for `release/reviews/atmosphere/`.
- [ ] Confirm release-review ID format.
- [ ] Confirm release-review filename convention.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm policy review pointer format.
- [ ] Confirm manifest, decision, correction, rollback, supersession, and changelog pointer formats.
- [ ] Confirm whether release-review records require schema validation before manifest handoff or release decision.
- [ ] Confirm whether `release/reviews/` should remain distinct from `release/decisions/` and `release/promotion_decisions/`.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Parent lane creation, first atmosphere release review, manifest handoff, validation receipt update, policy review, correction, rollback, or changelog integration |
