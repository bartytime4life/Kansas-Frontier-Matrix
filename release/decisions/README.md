# `release/decisions/` — Release Decision Records

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-decisions-blueviolet)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/decisions/` holds decision records for the KFM release lane.

A decision record explains what was decided, what release record it affects, who reviewed it, what governed records support it, and what follow-up remains open.

Decision prose is not sovereign truth. Manifests, validation receipts, evidence records, changelog entries, correction records, and steward decisions outrank this README.

## Authority

| Field | Value |
|---|---|
| Owning root | `release/` |
| Lane | `release/decisions/` |
| Status | Draft |
| Authority | Guidance and index only. Governed release records outrank this README. |
| Review | Release steward, data steward, docs steward, and affected domain steward. |

## Repo fit

```text
release/
├── decisions/       # you are here
├── manifests/
├── candidates/
├── changelog/
├── correction/
├── corrections/
└── correction_notices/
```

This path belongs under `release/` because it records release governance decisions. Data artifacts belong in lifecycle data roots, not here.

## Decision classes

| Class | Meaning |
|---|---|
| `PROMOTE_CANDIDATE` | Move a candidate to the next release step. |
| `HOLD_CANDIDATE` | Keep a candidate under review. |
| `REJECT_CANDIDATE` | Stop a candidate from continuing in this release path. |
| `APPROVE_RELEASE` | Approve a release record. |
| `DEFER_RELEASE` | Record that a release is not ready. |
| `CORRECT_RELEASE` | Link a release decision to a correction path. |
| `SUPERSEDE_RELEASE` | Mark that a newer governed record replaces an older one. |
| `NOTICE_REQUIRED` | Record that a notice should be prepared or linked. |
| `DOCS_ONLY` | Record a documentation-only release decision. |
| `NO_ACTION` | Record that review found no change is needed. |

## What belongs here

- Release decision records.
- Decision readiness notes.
- Steward review summaries.
- Links to manifests, candidates, validation receipts, evidence records, correction records, notices, and changelog entries.
- Follow-up tasks for manifest, changelog, correction, notice, validation, or release-history updates.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exports, API payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy files, or validator code.
- Generated summaries used as sovereign truth.
- Release decisions without governed record pointers.

## Required decision fields

- Decision ID
- Decision class
- Affected release, candidate, manifest entry, artifact, claim, correction, notice, or changelog pointer
- Domain scope, when applicable
- Date recorded
- Decision maker or approving steward
- Review participants
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Manifest pointer, when applicable
- Changelog pointer, when applicable
- Correction pointer, when applicable
- Notice pointer, when applicable
- Release-facing effect
- Decision rationale
- Follow-up items
- Correction or supersession path
- Closure status

## Minimal decision record

```markdown
# <decision-id>

## Status
PROPOSED / READY_FOR_REVIEW / APPROVED / REJECTED / HELD / APPLIED / SUPERSEDED / NO_ACTION

## Decision class
PROMOTE_CANDIDATE / HOLD_CANDIDATE / REJECT_CANDIDATE / APPROVE_RELEASE / DEFER_RELEASE / CORRECT_RELEASE / SUPERSEDE_RELEASE / NOTICE_REQUIRED / DOCS_ONLY / NO_ACTION

## Affected record
<release, candidate, manifest entry, artifact, claim, correction, notice, changelog entry, or N/A>

## Domain scope
<domain scope or N/A>

## Date recorded
<YYYY-MM-DD>

## Decision maker
<steward or maintainer>

## Governed record pointers
- Manifest: <path or N/A>
- Candidate: <path or N/A>
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Changelog: <path or N/A>
- Correction: <path or N/A>
- Notice: <path or N/A>

## Decision
<the decision>

## Rationale
<why the decision was made>

## Follow-up
<open items or none>

## Closure
<open / closed / blocked, with reason>
```

## Review checklist

- [ ] Affected record is identified.
- [ ] Decision class is the smallest accurate class.
- [ ] Evidence link is present when evidence is needed.
- [ ] Validation link is present when validation is needed.
- [ ] Changelog link is present when release history changes.
- [ ] Correction link is present when a correction is required.
- [ ] Notice link is present when a notice is required.
- [ ] Steward decision and reviewer roles are recorded.
- [ ] Follow-up items are listed or marked none.
- [ ] No data payloads are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<decision-class>_<short-topic>.md
```

Examples:

```text
2026-07-03_approve-release_agriculture-county-year-panel.md
2026-07-03_hold-candidate_hydrology-time-validity.md
2026-07-03_correct-release_atmosphere-time-coverage.md
2026-07-03_docs-only_release-candidate-readme-cleanup.md
```

## Open verification

- [ ] Confirm CODEOWNERS for `release/decisions/`.
- [ ] Confirm decision naming convention.
- [ ] Confirm decision ID format.
- [ ] Confirm manifest pointer format.
- [ ] Confirm validation pointer format.
- [ ] Confirm changelog linkage.
- [ ] Confirm correction and notice linkage.
- [ ] Confirm whether decision records need schema validation.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | First decision record, decision schema, manifest promotion, correction approval, notice approval, or changelog integration |
