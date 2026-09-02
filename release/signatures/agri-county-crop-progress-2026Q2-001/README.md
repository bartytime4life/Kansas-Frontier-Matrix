# `release/signatures/agri-county-crop-progress-2026Q2-001/` — Agriculture Signature Packet

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-signatures-agri-county-crop-progress-2026q2-001-readme
title: release/signatures/agri-county-crop-progress-2026Q2-001/ — Agriculture Signature Packet
version: v1
status: draft
policy_label: public
owners:
  - <agriculture-domain-steward>
  - <release-steward>
  - <data-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, release, signatures, agriculture, crop-progress, 2026Q2, evidence, validation]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-signatures-blueviolet)
![domain](https://img.shields.io/badge/domain-agriculture-green)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/signatures/agri-county-crop-progress-2026Q2-001/` holds the signature packet index for the draft agriculture release unit `agri-county-crop-progress-2026Q2-001`.

A signature packet records review signoff, support pointers, unresolved blockers, and handoff state for a release-facing agriculture item. It is not the released artifact, not a manifest by itself, and not final publication approval unless a governed decision record says so.

## Status & authority

| Field | Value |
|---|---|
| Document type | Release signature packet README |
| Owning root | `release/` |
| Lane | `release/signatures/` |
| Packet path | `release/signatures/agri-county-crop-progress-2026Q2-001/` |
| Signature packet ID | `agri-county-crop-progress-2026Q2-001` |
| Domain | `agriculture` |
| Status | Draft |
| Authority level | Packet guidance and index. Actual signature records, manifests, validation receipts, evidence records, policy reviews, release decisions, correction records, and changelog entries outrank this README. |
| Default posture | Do not infer release approval from this README. Require governed records and release-steward decision. |
| Required reviewers | Agriculture steward, release steward, data steward, and docs steward; policy reviewer when needed. |

## Path status

Current-session evidence confirms this README existed as a blank file before this update.

Current-session evidence also confirms the parent `release/signatures/README.md` is still a greenfield stub. Treat this packet as draft until the parent signature lane is expanded.

## Repo fit

```text
release/
├── signatures/
│   └── agri-county-crop-progress-2026Q2-001/       # you are here
├── agriculture/
├── candidates/
│   └── agriculture/
├── manifests/
├── decisions/
├── changelog/
├── correction/
├── corrections/
└── correction_notices/
```

This path belongs under the `release/` responsibility root because it records release-governance signature state. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after governed approval.

## Packet identity

| Field | Value |
|---|---|
| Packet ID | `agri-county-crop-progress-2026Q2-001` |
| Domain | `agriculture` |
| Short name | County crop progress, 2026 Q2 |
| Quarter | `2026Q2` |
| Sequence | `001` |
| Release status | Draft signature packet; not a release approval |
| Candidate pointer | NEEDS VERIFICATION |
| Manifest pointer | NEEDS VERIFICATION |
| Decision pointer | NEEDS VERIFICATION |
| Evidence pointer | NEEDS VERIFICATION |
| Validation pointer | NEEDS VERIFICATION |
| Changelog pointer | NEEDS VERIFICATION |

## Signature packet responsibilities

| Responsibility | Expectation |
|---|---|
| Identity | Preserve stable packet ID and title. |
| Release target | Point to the candidate, manifest, decision, or release item being signed. |
| Evidence | Link evidence records when release claims depend on evidence. |
| Validation | Link validation receipts or checks when release readiness depends on validation. |
| Policy posture | Link policy review when rights, sensitivity, access, or public posture affects release. |
| Steward signoff | Record each required reviewer, status, date, and decision. |
| Manifest handoff | Link manifest record when the signature packet supports manifest readiness. |
| Decision handoff | Link release decision record when signoff supports release-state change. |
| Correction path | Link correction records when repair or replacement is required. |
| Changelog | Link release-history records when release state changes. |

## What belongs here

- Signature packet README and packet index.
- Signature records for this release unit.
- Reviewer signoff notes.
- Evidence, validation, policy, manifest, decision, correction, and changelog pointers.
- Open blocker notes for this signature packet.
- Handoff notes to manifest, decision, correction, or changelog lanes.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exports, service payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy files, or validator code.
- Application runtime code.
- Generated summaries used as evidence or final approval.
- Final release approval without governed decision record and release-steward signoff.

## Signature states

Use finite signature states where possible:

| State | Meaning |
|---|---|
| `DRAFT` | Packet exists but is not ready for review. |
| `READY_FOR_REVIEW` | Packet is ready for required reviewer checks. |
| `SIGNED` | Required reviewer has signed the packet. |
| `SIGNED_WITH_NOTES` | Reviewer signed but included notes or limitations. |
| `HELD` | Packet is blocked pending evidence, validation, policy, or steward review. |
| `REJECTED` | Reviewer does not approve the release-facing handoff. |
| `SUPERSEDED` | A newer packet replaces this packet. |
| `NO_ACTION` | No release-facing change is recommended. |

## Required signature packet fields

- Signature packet ID
- Signature packet status
- Release target pointer
- Candidate pointer, when applicable
- Manifest pointer, when applicable
- Decision pointer, when applicable
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Policy review pointer, when applicable
- Correction pointer, when applicable
- Changelog pointer, when applicable
- Required reviewer list
- Reviewer status
- Reviewer date
- Reviewer notes
- Release-facing effect
- Open blockers
- Follow-up items

## Minimal signature record

```markdown
# <signature-record-id>

## Signature packet
agri-county-crop-progress-2026Q2-001

## Status
DRAFT / READY_FOR_REVIEW / SIGNED / SIGNED_WITH_NOTES / HELD / REJECTED / SUPERSEDED / NO_ACTION

## Release target
<candidate, manifest, decision, release item, or N/A>

## Governed support pointers
- Candidate: <path or N/A>
- Manifest: <path or N/A>
- Decision: <path or N/A>
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Policy review: <path or N/A>
- Correction: <path or N/A>
- Changelog: <path or N/A>

## Reviewer
<steward or maintainer>

## Reviewer role
<agriculture steward / release steward / data steward / docs steward / policy reviewer>

## Signature date
<YYYY-MM-DD>

## Signature statement
<signed / signed with notes / held / rejected / no action>

## Notes
<short note grounded in governed records>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Signature packet ID is stable.
- [ ] Release target pointer is present or marked N/A.
- [ ] Candidate pointer is linked when applicable.
- [ ] Manifest pointer is linked when applicable.
- [ ] Decision pointer is linked when release state changes.
- [ ] Evidence support is linked when claims depend on evidence.
- [ ] Validation support is linked when readiness depends on validation.
- [ ] Policy review is linked when release posture requires it.
- [ ] Required reviewer list is complete.
- [ ] Reviewer statuses and dates are recorded.
- [ ] Open blockers are listed or marked none.
- [ ] No data payloads are stored in this lane.

## Naming guidance

Recommended signature-record pattern:

```text
<YYYY-MM-DD>_<reviewer-role>_signature.md
```

Examples:

```text
2026-07-03_agriculture-steward_signature.md
2026-07-03_release-steward_signature.md
2026-07-03_data-steward_signature.md
2026-07-03_docs-steward_signature.md
```

Use lowercase filenames, hyphenated reviewer roles, and stable signature IDs. Avoid renaming signed records unless a migration note explains the change.

## Open verification

- [ ] Expand `release/signatures/README.md` so this packet inherits from a complete parent contract.
- [ ] Confirm CODEOWNERS for `release/signatures/` and this packet path.
- [ ] Confirm signature packet ID format.
- [ ] Confirm signature record filename convention.
- [ ] Confirm release target pointer.
- [ ] Confirm candidate pointer, if this packet signs a candidate.
- [ ] Confirm manifest pointer, if this packet signs manifest readiness.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm decision, correction, and changelog pointer formats.
- [ ] Confirm whether signature records require schema validation before release-state changes.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Parent signature lane expansion, first signature record, manifest handoff, decision handoff, validation receipt update, correction, changelog update, or release-state change |
