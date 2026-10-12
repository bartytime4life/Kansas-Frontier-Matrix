# `release/source_role_anti_collapse/` — Source Role Review Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-source-role-anti-collapse-readme
title: release/source_role_anti_collapse/ — Source Role Review Lane
version: v1
status: draft
policy_label: public
owners:
  - <release-steward>
  - <source-steward>
  - <data-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, release, source-role, review, evidence, validation]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-source--role--review-blueviolet)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/source_role_anti_collapse/` is a release review lane for source role checks.

Its job is to help reviewers confirm that source role information remains visible, traceable, and reviewable during release preparation. A release review note should show which release-facing record was checked, which support records were consulted, and which follow-up is still open.

This lane is not the doctrine source. It is a release-side review and pointer lane.

## Status & authority

| Field | Value |
|---|---|
| Document type | Source role release review README |
| Owning root | `release/` |
| Lane | `release/source_role_anti_collapse/` |
| Status | Draft |
| Authority level | Review guidance and index. Source role doctrine, source contracts, schemas, policy files, validation tools, manifests, evidence records, validation receipts, release decisions, and correction records outrank this README. |
| Default posture | Hold the release review when source role information is missing or unclear. |
| Required reviewers | Release steward, source steward, data steward, affected domain steward, and docs steward. |

## Path status

Current-session evidence confirms this README existed as a blank file before this update.

Current-session evidence also confirms source role doctrine exists outside `release/`, including `docs/architecture/cross-domain/source-role-anti-collapse.md` and an atlas pointer page. This lane should link to those sources rather than duplicate them.

## Repo fit

```text
release/
├── source_role_anti_collapse/       # you are here
├── candidates/
├── manifests/
├── decisions/
├── signatures/
├── reviews/
├── policy/
├── changelog/
├── correction/
├── corrections/
└── correction_notices/
```

This path belongs under `release/` because it records release review notes. It does not own source records, lifecycle data, schemas, contracts, policy files, or validation code.

## Review responsibilities

| Responsibility | Expectation |
|---|---|
| Release target | Link the candidate, manifest, decision, release item, correction, or notice being reviewed. |
| Source role status | Record whether source role information is present, clear, and traceable. |
| Evidence | Link evidence records when the review depends on evidence. |
| Validation | Link validation receipts when a source role check has been run. |
| Manifest | Link manifests when packaging is involved. |
| Decision | Link decisions when release-facing approval or hold status is involved. |
| Correction | Link correction records when repair is required. |
| Changelog | Link release-history records when the release trail changes. |

## What belongs here

- Source role release review records.
- Release-readiness checklists for source role traceability.
- Review notes for missing or unclear source role information.
- Links to evidence records, validation receipts, manifests, decisions, corrections, notices, and changelog entries.
- Domain-specific notes explaining source role status for a release target.
- Handoff notes to other release lanes when repair or additional review is needed.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Source descriptors.
- Source catalog profiles.
- Schemas.
- Contracts.
- Policy files.
- Validation tool code.
- Application runtime code.
- Duplicated doctrine.
- Generated summaries used as evidence or final approval.

## Review outcomes

Use finite outcomes where possible:

| Outcome | Meaning |
|---|---|
| `PASS_ROLE_TRACEABLE` | Source role information is present and linked for review. |
| `HOLD_ROLE_MISSING` | Source role information is missing. |
| `HOLD_ROLE_UNCLEAR` | Source role information is unclear. |
| `REPAIR_REQUIRED` | A support record or release note needs repair before review can continue. |
| `REVIEW_REQUIRED` | Additional steward review is required. |
| `CORRECTION_REQUIRED` | A correction record is required. |
| `NO_ACTION` | No source role release action is required. |

## Required review fields

Every source role review record should capture:

- Review ID
- Review status
- Review outcome
- Release target pointer
- Candidate pointer, when applicable
- Manifest pointer, when applicable
- Domain or layer scope
- Source role status or distribution
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Decision pointer, when applicable
- Correction pointer, when applicable
- Changelog pointer, when applicable
- Reviewer name or role
- Review date
- Open blockers
- Follow-up items

## Minimal review record

```markdown
# <source-role-review-id>

## Status
DRAFT / READY_FOR_REVIEW / PASS_ROLE_TRACEABLE / HELD / REPAIR_REQUIRED / CORRECTION_REQUIRED / NO_ACTION

## Review outcome
PASS_ROLE_TRACEABLE / HOLD_ROLE_MISSING / HOLD_ROLE_UNCLEAR / REPAIR_REQUIRED / REVIEW_REQUIRED / CORRECTION_REQUIRED / NO_ACTION

## Release target
<candidate, manifest, decision, release item, correction, notice, or N/A>

## Scope
<domain, layer family, artifact family, geography, time slice, release target, or N/A>

## Source role status or distribution
<role status, role distribution, or NEEDS VERIFICATION>

## Governed support pointers
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Manifest: <path or N/A>
- Decision: <path or N/A>
- Correction: <path or N/A>
- Changelog: <path or N/A>

## Reviewer
<steward or maintainer>

## Review date
<YYYY-MM-DD>

## Notes
<short note grounded in governed records>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Release target pointer is present or marked N/A.
- [ ] Source role status or distribution is present.
- [ ] Evidence support is linked when needed.
- [ ] Validation support is linked when checked.
- [ ] Manifest pointer is linked when packaging is involved.
- [ ] Decision pointer is linked when approval or hold status is involved.
- [ ] Correction and changelog pointers are linked when applicable.
- [ ] No data payloads, source descriptors, schemas, contracts, policy files, or validation code are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<scope>_source-role-review.md
```

Examples:

```text
2026-07-03_agriculture-county-crop-progress_source-role-review.md
2026-07-03_release-manifest-role-check_source-role-review.md
```

Use lowercase filenames, hyphenated scope names, and stable review IDs.

## Open verification

- [ ] Confirm CODEOWNERS for `release/source_role_anti_collapse/`.
- [ ] Confirm whether this lane should be indexed directly in `release/README.md`.
- [ ] Confirm source role review ID format.
- [ ] Confirm source role review filename convention.
- [ ] Confirm source role distribution field format for manifests.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm decision, correction, notice, and changelog pointer formats.
- [ ] Confirm whether source role release reviews require schema validation before release-facing action.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Expanded README replacing minimal initialization |
| Next review trigger | First source role release review, source role schema update, policy update, manifest field update, correction, notice, changelog update, or release-facing action |
