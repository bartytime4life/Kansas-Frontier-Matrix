# `release/withdrawal_notices/` — Release Withdrawal Notice Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-withdrawal-notices-readme
title: release/withdrawal_notices/ — Release Withdrawal Notice Index
version: v1
status: draft
policy_label: public
owners:
  - <release-steward>
  - <docs-steward>
  - <data-steward>
  - <domain-stewards>
updated: 2026-07-03
tags: [kfm, release, withdrawal-notices, review, validation, audit, changelog]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-withdrawal--notices-blueviolet)
![publication](https://img.shields.io/badge/publication-governed-orange)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/withdrawal_notices/` is the parent lane for KFM release withdrawal notices.

A withdrawal notice is a communication and review record. It should explain that a release-facing item has been withdrawn, held from use, superseded, or marked not ready, while pointing to the governed records that support that status.

A withdrawal notice is not the withdrawal decision by itself. It does not remove data, publish data, alter release state, or replace a release decision, manifest, correction record, validation receipt, evidence record, or steward approval.

## Status & authority

| Field | Value |
|---|---|
| Document type | Release withdrawal notice parent README |
| Owning root | `release/` |
| Notice lane | `release/withdrawal_notices/` |
| Status | Draft |
| Authority level | Notice guidance and index. Release manifests, decisions, validation receipts, evidence records, policy reviews, correction records, changelog entries, signatures, and steward decisions outrank this README. |
| Default posture | Do not change release state from notice prose alone. Require governed records and release-steward decision. |
| Required reviewers | Release steward, docs steward, data steward, affected domain steward, and policy reviewer when needed. |

## Path status

Current-session evidence confirms this README was a greenfield stub before this update.

Current-session evidence also confirms the release root already treats withdrawals as part of release governance, distinct from `data/published/` payload storage. This lane is therefore a release-governance notice lane, not a data lifecycle home.

## Repo fit

```text
release/
├── withdrawal_notices/       # you are here
├── decisions/
├── manifests/
├── reviews/
├── signatures/
├── correction/
├── corrections/
├── correction_notices/
├── rollback/
├── rollback_cards/
└── changelog/
```

This path belongs under the `release/` responsibility root because it records release withdrawal notice metadata and communication review. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after governed approval.

## Withdrawal-notice responsibilities

| Responsibility | Expectation |
|---|---|
| Notice identity | Provide a stable withdrawal-notice ID. |
| Affected record | Link the release, manifest, decision, candidate, correction, notice, changelog entry, or artifact pointer being withdrawn or held. |
| Withdrawal reason | State the reason using governed support records. |
| Evidence | Link evidence records when the notice depends on evidence. |
| Validation | Link validation receipts or checks when withdrawal depends on validation. |
| Policy posture | Link policy review when rights, sensitivity, access, or public posture affects the notice. |
| Decision | Link the steward decision authorizing withdrawal or hold status. |
| Correction path | Link correction records when repair or replacement is required. |
| Replacement path | Link supersession or replacement records when applicable. |
| Changelog | Link release-history records when release state changes. |

## What belongs here

- Withdrawal-notice README files and sublane indexes.
- Withdrawal notice drafts and readiness checklists.
- Steward review summaries for notice wording.
- Links to release manifests, decisions, evidence records, validation receipts, policy review notes, correction records, replacement records, signatures, and changelog entries.
- Notes explaining whether a notice describes withdrawal, hold, supersession, replacement, time/version update, public-surface note, or no release-facing change.
- Follow-up tasks for changelog, manifest, decision, correction, validation, or release-history updates.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exported files, API payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Application runtime code.
- Withdrawal approval without steward decision.
- Notice text used as evidence.
- Generated summaries used as sovereign truth.
- Secrets, credentials, or private operational material.

## Notice types

Use finite notice types where possible:

| Notice type | Meaning |
|---|---|
| `WITHDRAWAL_NOTICE` | Release-facing item is withdrawn under governed decision. |
| `HOLD_NOTICE` | Release-facing item is held pending evidence, validation, policy, or steward review. |
| `SUPERSESSION_NOTICE` | A newer governed record replaces the affected record. |
| `REPLACEMENT_NOTICE` | Replacement material is available or planned. |
| `CORRECTION_LINKED_NOTICE` | Withdrawal is tied to a correction record. |
| `TIME_VERSION_NOTICE` | Withdrawal or hold is tied to time validity, stale state, or version update. |
| `NO_ACTION_NOTICE` | Review found that no public notice is needed. |

## Required notice fields

Every withdrawal notice should capture:

- Notice ID
- Notice type
- Notice status
- Affected release-facing record pointer
- Withdrawal decision pointer, when applicable
- Manifest pointer, when applicable
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Policy review pointer, when applicable
- Correction pointer, when applicable
- Replacement or supersession pointer, when applicable
- Changelog pointer, when applicable
- Public-facing effect
- Notice audience
- Notice reason
- Notice date
- Reviewing steward
- Follow-up items

## Minimal withdrawal notice

```markdown
# <withdrawal-notice-id>

## Status
DRAFT / READY_FOR_REVIEW / APPROVED / HELD / PUBLISHED_NOTICE / SUPERSEDED / NO_ACTION

## Notice type
WITHDRAWAL_NOTICE / HOLD_NOTICE / SUPERSESSION_NOTICE / REPLACEMENT_NOTICE / CORRECTION_LINKED_NOTICE / TIME_VERSION_NOTICE / NO_ACTION_NOTICE

## Affected record
<release, manifest, decision, candidate, correction, notice, changelog, or artifact pointer>

## Governed support pointers
- Withdrawal decision: <path or N/A>
- Manifest: <path or N/A>
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Policy review: <path or N/A>
- Correction: <path or N/A>
- Replacement or supersession: <path or N/A>
- Changelog: <path or N/A>

## Public-facing effect
<none / held / withdrawn / superseded / replaced / correction linked / review pending>

## Notice audience
<internal / public / semi-public / steward-only / N/A>

## Notice reason
<short reason grounded in governed records>

## Notice date
<YYYY-MM-DD>

## Reviewing steward
<steward or maintainer>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Affected release-facing record pointer is present.
- [ ] Withdrawal decision pointer is linked when release state changes.
- [ ] Manifest pointer is linked when the affected item is in a manifest.
- [ ] Evidence support is linked when the notice depends on evidence.
- [ ] Validation support is linked when the notice depends on validation.
- [ ] Policy review is linked when public posture requires it.
- [ ] Correction, replacement, supersession, and changelog pointers are linked when applicable.
- [ ] Public-facing effect is explicit.
- [ ] Notice audience is explicit.
- [ ] Notice reason is grounded in governed records.
- [ ] No data payloads are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<scope>_withdrawal-notice.md
```

Examples:

```text
2026-07-03_agriculture-county-crop-progress_withdrawal-notice.md
2026-07-03_hydrology-time-validity_hold-notice.md
2026-07-03_release-manifest-supersession_withdrawal-notice.md
```

Use lowercase filenames, hyphenated scope names, and stable notice IDs. Avoid renaming approved notice records unless a migration note explains the change.

## Open verification

- [ ] Confirm CODEOWNERS for `release/withdrawal_notices/`.
- [ ] Confirm whether this lane should be indexed directly in `release/README.md`.
- [ ] Confirm notice ID format.
- [ ] Confirm withdrawal-notice filename convention.
- [ ] Confirm withdrawal decision pointer format.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm policy review pointer format.
- [ ] Confirm correction, replacement, supersession, and changelog pointer formats.
- [ ] Confirm whether notice records require schema validation before release-facing action.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | First withdrawal notice, release decision update, manifest update, correction, replacement, supersession, policy review, changelog update, or release-facing action |
