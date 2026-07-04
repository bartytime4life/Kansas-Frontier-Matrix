# `release/people-dna-land/2026-05-15/` — People DNA Land Dated Release Review Lane

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![domain](https://img.shields.io/badge/domain-people--dna--land-purple)
![date](https://img.shields.io/badge/date-2026--05--15-lightgrey)
![review](https://img.shields.io/badge/review-required-red)
![posture](https://img.shields.io/badge/default-fail--closed-red)

## Purpose

`release/people-dna-land/2026-05-15/` is a dated release-review lane for people, DNA, and land material prepared or grouped around 2026-05-15.

This folder is for release-facing review records, not source data and not public payload storage. It should hold the dated index, review notes, steward decisions, and pointers to governed evidence, validation, manifest, correction, notice, and rollback records.

The default posture is fail-closed. No people, genetic, kinship, land, parcel, ownership, or identity-linked material should be treated as public from this README alone.

## Status & authority

| Field | Value |
|---|---|
| Document type | Dated release review README |
| Owning root | `release/` |
| Dated lane | `release/people-dna-land/2026-05-15/` |
| Status | Draft |
| Date represented | 2026-05-15 |
| Authority level | Guidance and dated index. Final release records, steward decisions, validation receipts, evidence bundles, policy reviews, manifests, correction records, and changelog entries outrank this README. |
| Default posture | No public release unless evidence, rights, privacy, policy, validation, review, correction path, and rollback path are resolved. |
| Required reviewers | People-dna-land steward, release steward, data steward, policy/privacy reviewer, and docs steward. |

## Repo fit

```text
release/
├── people-dna-land/
│   └── 2026-05-15/       # you are here
├── candidates/
│   └── people-dna-land/
├── manifests/
├── decisions/
├── changelog/
├── correction/
└── correction_notices/
```

This path belongs under the `release/` responsibility root because it records a dated release-review lane. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## Dated lane responsibilities

| Responsibility | Expectation |
|---|---|
| Date scope | State why 2026-05-15 is the date for this review group. |
| Release scope | Identify the release candidate, manifest, decision, correction, or notice being reviewed. |
| Evidence | Link evidence records when claims depend on evidence. |
| Validation | Link validation receipts or checks. |
| Rights and privacy | Link review records for rights, consent, attribution, privacy, and public-surface posture. |
| Sensitivity posture | State whether material is public-safe, generalized, redacted, restricted, held, or not ready. |
| Decision | Link the steward decision that supports any release state. |
| Changelog | Link the release-history entry when release history changes. |
| Correction path | Link correction records when the dated review changes a release state. |
| Rollback path | Link rollback review when the dated review requires reversal planning. |

## What belongs here

- Dated release-review README files.
- People-dna-land release review notes for the 2026-05-15 group.
- Links to candidate records, manifest records, decisions, validation receipts, evidence records, policy/privacy reviews, correction records, notices, rollback records, and changelog entries.
- Notes explaining dated review scope, release-facing effect, sensitivity posture, and follow-up tasks.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, parcel exports, tiles, service payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy files, or validator code.
- Person-level, genetic, identity, family, or land-record payloads.
- Generated summaries used as sovereign truth.
- Public release approval without governed release records and steward review.

## Required dated review fields

- Review ID
- Date represented
- Release or candidate pointer
- Manifest pointer, when applicable
- Decision pointer, when applicable
- Domain scope
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Rights review pointer, when applicable
- Privacy review pointer, when applicable
- Policy review pointer, when applicable
- Correction pointer, when applicable
- Notice pointer, when applicable
- Rollback pointer, when applicable
- Changelog pointer, when applicable
- Release-facing effect
- Public-surface posture
- Steward review state
- Follow-up items

## Minimal dated review record

```markdown
# <review-id>

## Status
DRAFT / READY_FOR_REVIEW / APPROVED / HELD / SUPERSEDED / CORRECTED / NO_ACTION

## Date represented
2026-05-15

## Release or candidate
<release ID, candidate path, or N/A>

## Domain scope
<people-dna-land scope, land-ownership scope, evidence family, summary family, or release target>

## Governed support pointers
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Rights review: <path or N/A>
- Privacy review: <path or N/A>
- Policy review: <path or N/A>
- Manifest: <path or N/A>
- Decision: <path or N/A>
- Changelog: <path or N/A>
- Correction: <path or N/A>
- Notice: <path or N/A>
- Rollback: <path or N/A>

## Sensitivity posture
PUBLIC_SAFE / GENERALIZED / REDACTED / RESTRICTED / HELD / NOT_READY

## Release-facing effect
<none / ready / held / corrected / superseded / review pending>

## Public-surface posture
<what governed public or restricted surfaces may use this review, or N/A>

## Steward review state
<reviewers, decision, and date>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Date scope for 2026-05-15 is explained.
- [ ] Release or candidate pointer is present.
- [ ] Evidence support is linked when claims depend on evidence.
- [ ] Validation support is linked when validation is required.
- [ ] Rights and privacy review are linked when release posture requires them.
- [ ] Policy review is linked before any public-facing use.
- [ ] Manifest and decision pointers are linked when release state changes.
- [ ] Correction, notice, rollback, and changelog pointers are linked when applicable.
- [ ] Public-surface posture is explicit.
- [ ] No data payloads are stored in this lane.

## Naming guidance

Recommended pattern for records inside this dated lane:

```text
<YYYY-MM-DD>_<people-dna-land-scope>_<record-type>.md
```

Examples:

```text
2026-05-15_people-dna-land_release-review.md
2026-05-15_land-ownership_review-summary.md
2026-05-15_people-dna-land_policy-posture.md
```

## Open verification

- [ ] Confirm whether `release/people-dna-land/` needs a parent README.
- [ ] Confirm why 2026-05-15 is the dated review group.
- [ ] Confirm CODEOWNERS for this dated lane.
- [ ] Confirm dated release-review record ID format.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm rights, privacy, and policy review pointer formats.
- [ ] Confirm manifest, decision, changelog, correction, notice, and rollback pointer formats.
- [ ] Confirm whether records in this dated lane require schema validation before release approval.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Parent lane README, first dated review record, manifest link, release decision, privacy review, policy review, correction, notice, rollback, or changelog integration |
