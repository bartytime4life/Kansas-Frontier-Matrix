# `release/correction/rollback/` — Correction Rollback Review Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-correction-rollback-readme
title: release/correction/rollback/ — Correction Rollback Review Lane
version: v1
status: draft
policy_label: public
owners:
  - <release-steward>
  - <correction-steward>
  - <rollback-steward>
  - <data-steward>
updated: 2026-07-03
tags: [kfm, release, correction, rollback, review, validation, audit]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-correction--rollback-blueviolet)
![publication](https://img.shields.io/badge/publication-governed-orange)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Path status](#path-status) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Required review fields](#required-review-fields) · [Minimal rollback record](#minimal-rollback-record) · [Open verification](#open-verification)

---

## Purpose

`release/correction/rollback/` holds review notes for rollback actions that are tied to release corrections.

This lane is for governance records, not data movement. It should help stewards document when a released item, public surface, manifest entry, or correction path needs to be reverted, superseded, withdrawn, or repaired under review.

A rollback record should answer:

- What release or correction is affected?
- Why is rollback being considered or recorded?
- Which manifest, artifact, validation, correction, or changelog entry is involved?
- What public-surface effect should reviewers expect?
- What is the safe replacement, supersession, or withdrawal path?
- Which steward approved the decision?

Rollback is a governed state transition, not a file move.

---

## Status & authority

| Field | Value |
|---|---|
| Document type | Correction rollback README |
| Owning root | `release/` |
| Requested lane | `release/correction/rollback/` |
| Status | Draft |
| Authority level | Review guidance. ReleaseManifest, correction record, rollback card, changelog entry, signature, receipt, policy, schema, and validation records outrank this README. |
| Default posture | Do not alter public state from prose alone. Require steward decision and links to governed records. |
| Required reviewers | Release steward, correction steward, rollback steward, data steward, and affected domain steward. |

---

## Path status

This README documents the path exactly requested: `release/correction/rollback/`.

Current-session evidence confirms this README existed as a blank file before this update. Current-session evidence did not confirm `release/correction/README.md`, `release/corrections/README.md`, or `release/rollbacks/README.md` as existing README files. Treat this nested path as a draft bridge lane until the release directory convention is confirmed by Directory Rules, ADR, or maintainer decision.

---

## Repo fit

```text
release/
├── candidates/
├── manifests/
├── changelog/
└── correction/
    └── rollback/       # you are here
```

This path belongs under the `release/` responsibility root because it concerns release correction and rollback review. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

---

## What belongs here

- Correction-linked rollback notes.
- Rollback readiness checklists.
- Steward review summaries.
- Links to release manifests, changelog entries, corrections, validation receipts, and affected published targets.
- Notes explaining whether the outcome is revert, supersede, withdraw, repair, or defer.
- Public-surface effect summaries.
- Follow-up tasks for correction closure and release-history updates.

---

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exported files, API payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Emergency instructions, live operations notes, credentials, secrets, or private operational material.
- Rollback approval without steward review.
- Generated summaries used as sovereign truth.

---

## Required review fields

Every correction rollback record should capture:

- Rollback record ID
- Affected release or candidate pointer
- Affected correction pointer
- Date recorded
- Recorder
- Steward decision pointer
- Manifest pointer, when applicable
- Artifact pointer, when applicable
- Validation or receipt pointer, when applicable
- Changelog pointer, when applicable
- Public-surface effect
- Replacement, supersession, or withdrawal path
- Reason for rollback
- Correction closure status
- Follow-up items

---

## Minimal rollback record

```markdown
# <rollback-record-id>

## Status
PROPOSED / READY_FOR_REVIEW / APPROVED / APPLIED / SUPERSEDED / WITHDRAWN / REPAIR_REQUIRED

## Affected release or candidate
<release manifest, candidate lane, or release record>

## Affected correction
<correction record or N/A>

## Date recorded
<YYYY-MM-DD>

## Recorded by
<steward or maintainer>

## Governed record pointers
- Manifest: <path or N/A>
- Artifact: <path or N/A>
- Validation: <path or N/A>
- Changelog: <path or N/A>
- Supersession: <path or N/A>

## Reason
<why rollback, withdrawal, supersession, or repair is needed>

## Public-surface effect
<none / changed / withdrawn / superseded / repaired>

## Replacement or supersession path
<path or N/A>

## Correction closure
<closed / open / blocked, with reason>

## Decision
<decision, steward, and reason>
```

---

## Open verification

- [ ] Confirm whether the canonical path should be `release/correction/rollback/`, `release/corrections/`, `release/rollbacks/`, or another Directory Rules-approved lane.
- [ ] Confirm CODEOWNERS for this path.
- [ ] Confirm rollback card naming convention.
- [ ] Confirm ReleaseManifest pointer format.
- [ ] Confirm correction record pointer format.
- [ ] Confirm changelog event linkage.
- [ ] Confirm whether rollback records need schema validation.

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | First correction rollback record, path convention decision, ReleaseManifest update, correction, withdrawal, supersession, or rollback schema decision |
