# `release/correction/` — Release Correction Review Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-correction-readme
title: release/correction/ — Release Correction Review Lane
version: v1
status: draft
policy_label: public
owners:
  - <release-steward>
  - <correction-steward>
  - <data-steward>
  - <domain-stewards>
updated: 2026-07-03
tags: [kfm, release, correction, rollback, review, validation, audit]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-correction-blueviolet)
![publication](https://img.shields.io/badge/publication-governed-orange)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Path status](#path-status) · [Repo fit](#repo-fit) · [Current sublanes](#current-sublanes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Correction outcomes](#correction-outcomes) · [Required review fields](#required-review-fields) · [Minimal correction record](#minimal-correction-record) · [Open verification](#open-verification)

---

## Purpose

`release/correction/` holds review notes for changes to already-reviewed or already-released KFM release records.

This lane is for governance records, not data movement. It helps stewards document when a release, release candidate, public surface, manifest entry, claim, validation receipt, or changelog entry needs correction, repair, withdrawal, supersession, or rollback review.

A correction record should answer:

- What release, candidate, manifest entry, artifact, claim, or public surface is affected?
- Why is correction needed?
- Which evidence, validation, policy, or steward decision supports the correction?
- What public-surface effect should reviewers expect?
- Does the correction require rollback, withdrawal, supersession, or a new release manifest?
- Which steward approved the decision?

Correction is a governed state transition, not a file move.

---

## Status & authority

| Field | Value |
|---|---|
| Document type | Release correction README |
| Owning root | `release/` |
| Requested lane | `release/correction/` |
| Status | Draft |
| Authority level | Review guidance. ReleaseManifest, correction record, rollback card, changelog entry, signature, receipt, policy, schema, and validation records outrank this README. |
| Default posture | Do not alter public state from prose alone. Require steward decision and links to governed records. |
| Required reviewers | Release steward, correction steward, data steward, affected domain steward, and policy reviewer when needed. |

---

## Path status

This README documents the path exactly requested: `release/correction/`.

Current-session evidence confirms `release/correction/README.md` existed as a blank file before this update, and `release/correction/rollback/README.md` exists as a child lane. Current-session evidence did not confirm plural `release/corrections/README.md` or `release/rollbacks/README.md` as existing README files. Treat this singular path as a draft correction lane until the release directory convention is confirmed by Directory Rules, ADR, or maintainer decision.

---

## Repo fit

```text
release/
├── candidates/
├── manifests/
├── changelog/
└── correction/       # you are here
    └── rollback/
```

This path belongs under the `release/` responsibility root because it concerns release correction review. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

---

## Current sublanes

| Sublane | Purpose | Status |
|---|---|---|
| `rollback/` | Review notes for rollback actions tied to release corrections. | Draft sublane README exists. |

---

## What belongs here

- Release correction notes.
- Correction readiness checklists.
- Steward review summaries.
- Links to release manifests, changelog entries, validation receipts, affected published targets, and evidence records.
- Notes explaining whether the outcome is repair, replacement, supersession, withdrawal, rollback review, or defer.
- Public-surface effect summaries.
- Follow-up tasks for changelog, manifest, validation, rollback, or release-history updates.

---

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exported files, API payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Emergency instructions, live operations notes, credentials, secrets, or private operational material.
- Correction approval without steward review.
- Generated summaries used as sovereign truth.

---

## Correction outcomes

| Outcome | Meaning |
|---|---|
| `REPAIR` | The release record or public surface remains valid after a bounded correction. |
| `SUPERSEDE` | A newer governed record replaces the affected record. |
| `WITHDRAW` | The affected release, public surface, or claim is removed from publication. |
| `ROLLBACK_REVIEW` | The correction needs rollback review before public-state change. |
| `DEFER` | The issue is recorded but not ready for correction action. |
| `NO_ACTION` | Review found no release correction is required. |

---

## Required review fields

Every correction record should capture:

- Correction record ID
- Affected release or candidate pointer
- Affected manifest, artifact, claim, or public surface
- Date recorded
- Recorder
- Steward decision pointer
- Evidence pointer, when applicable
- Validation or receipt pointer, when applicable
- Policy review pointer, when applicable
- Changelog pointer, when applicable
- Public-surface effect
- Outcome type
- Rollback need
- Reason for correction
- Follow-up items

---

## Minimal correction record

```markdown
# <correction-record-id>

## Status
PROPOSED / READY_FOR_REVIEW / APPROVED / APPLIED / SUPERSEDED / WITHDRAWN / ROLLBACK_REVIEW / NO_ACTION

## Affected release or candidate
<release manifest, candidate lane, or release record>

## Affected record or public surface
<manifest entry, artifact, claim, map surface, API surface, or N/A>

## Date recorded
<YYYY-MM-DD>

## Recorded by
<steward or maintainer>

## Governed record pointers
- Manifest: <path or N/A>
- Artifact: <path or N/A>
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Policy review: <path or N/A>
- Changelog: <path or N/A>
- Rollback review: <path or N/A>

## Reason
<why correction is needed>

## Public-surface effect
<none / changed / withdrawn / superseded / repaired / rollback review needed>

## Outcome
<repair / supersede / withdraw / rollback review / defer / no action>

## Follow-up
<open items or none>

## Decision
<decision, steward, and reason>
```

---

## Open verification

- [ ] Confirm whether the canonical path should be `release/correction/`, `release/corrections/`, or another Directory Rules-approved lane.
- [ ] Confirm CODEOWNERS for this path.
- [ ] Confirm correction record naming convention.
- [ ] Confirm ReleaseManifest pointer format.
- [ ] Confirm changelog event linkage.
- [ ] Confirm rollback-review linkage.
- [ ] Confirm whether correction records need schema validation.

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | First correction record, path convention decision, ReleaseManifest update, changelog update, withdrawal, supersession, rollback review, or correction schema decision |
