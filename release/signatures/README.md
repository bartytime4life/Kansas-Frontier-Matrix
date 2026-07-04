# `release/signatures/` — Release Signature Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-signatures-readme
title: release/signatures/ — Release Signature Lane
version: v1
status: draft
policy_label: public
owners:
  - <release-steward>
  - <data-steward>
  - <docs-steward>
  - <domain-stewards>
updated: 2026-07-03
tags: [kfm, release, signatures, signoff, evidence, validation, review]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-signatures-blueviolet)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/signatures/` holds release signature packets and reviewer signoff records.

A signature packet records who reviewed a release-facing item, what support records were checked, what is still blocked, and whether the packet is ready for manifest, decision, correction, changelog, or other release handoff.

A signature packet is not the released artifact, not a manifest by itself, and not final publication approval unless a governed decision record says so.

## Status & authority

| Field | Value |
|---|---|
| Document type | Release signatures parent README |
| Owning root | `release/` |
| Lane | `release/signatures/` |
| Status | Draft |
| Authority level | Parent guidance and index. Actual signature records, manifests, validation receipts, evidence records, policy reviews, release decisions, correction records, and changelog entries outrank this README. |
| Default posture | Do not infer release approval from this README. Require governed records and release-steward decision. |
| Required reviewers | Release steward, data steward, affected domain steward, and docs steward; policy reviewer when needed. |

## Path status

Current-session evidence confirms this README was a greenfield stub before this update.

Current-session evidence also confirms one child signature packet already exists: `agri-county-crop-progress-2026Q2-001/`.

## Repo fit

```text
release/
├── signatures/       # you are here
│   └── agri-county-crop-progress-2026Q2-001/
├── agriculture/
├── candidates/
├── manifests/
├── decisions/
├── changelog/
├── correction/
├── corrections/
└── correction_notices/
```

This path belongs under the `release/` responsibility root because it records release-governance signature state. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after governed approval.

## Current packets

| Packet | Scope | Status |
|---|---|---|
| `agri-county-crop-progress-2026Q2-001/` | Agriculture county crop progress, 2026 Q2, sequence 001. | Draft packet README exists. |

Add new signature-packet directories only when a release-facing item needs its own reviewer signoff trail, stable packet ID, support-pointer index, and handoff record.

## Signature lane responsibilities

| Responsibility | Expectation |
|---|---|
| Packet identity | Preserve stable signature packet IDs. |
| Release target | Link the candidate, manifest, decision, release item, correction, or notice being signed. |
| Evidence | Link evidence records when release claims depend on evidence. |
| Validation | Link validation receipts or checks when readiness depends on validation. |
| Policy posture | Link policy review when rights, sensitivity, access, or public posture affects release. |
| Reviewer signoff | Record required reviewers, role, status, date, and notes. |
| Manifest handoff | Link manifest records when signatures support manifest readiness. |
| Decision handoff | Link release decision records when signatures support release-state change. |
| Correction path | Link correction records when repair or replacement is required. |
| Changelog | Link release-history records when release state changes. |

## What belongs here

- Parent README and signature packet indexes.
- Signature packet directories.
- Reviewer signoff records.
- Signature readiness summaries.
- Evidence, validation, policy, manifest, decision, correction, notice, and changelog pointers.
- Open blocker notes for signature packets.
- Handoff notes to manifest, decision, correction, notice, or changelog lanes.

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

## Required signature fields

Every signature packet should capture:

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
- Notice pointer, when applicable
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
<signature-packet-id>

## Status
DRAFT / READY_FOR_REVIEW / SIGNED / SIGNED_WITH_NOTES / HELD / REJECTED / SUPERSEDED / NO_ACTION

## Release target
<candidate, manifest, decision, release item, correction, notice, or N/A>

## Governed support pointers
- Candidate: <path or N/A>
- Manifest: <path or N/A>
- Decision: <path or N/A>
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Policy review: <path or N/A>
- Correction: <path or N/A>
- Notice: <path or N/A>
- Changelog: <path or N/A>

## Reviewer
<steward or maintainer>

## Reviewer role
<domain steward / release steward / data steward / docs steward / policy reviewer>

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

Recommended packet pattern:

```text
<domain-or-release-shortname>-<time-or-version>-<sequence>/
```

Recommended signature-record pattern:

```text
<YYYY-MM-DD>_<reviewer-role>_signature.md
```

Examples:

```text
agri-county-crop-progress-2026Q2-001/
2026-07-03_release-steward_signature.md
2026-07-03_data-steward_signature.md
```

Use lowercase filenames for signature records, hyphenated reviewer roles, and stable packet IDs. Avoid renaming signed records unless a migration note explains the change.

## Open verification

- [ ] Confirm CODEOWNERS for `release/signatures/`.
- [ ] Confirm signature packet ID format.
- [ ] Confirm signature record filename convention.
- [ ] Confirm release target pointer format.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm policy review pointer format.
- [ ] Confirm decision, correction, notice, and changelog pointer formats.
- [ ] Confirm whether signature records require schema validation before release-state changes.
- [ ] Confirm whether the release root lane index should list `signatures/` directly.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | New signature packet, first signature record, manifest handoff, decision handoff, validation receipt update, correction, notice, changelog update, or release-state change |
