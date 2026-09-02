# `release/changelog/` — Release Changelog Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-changelog-readme
title: release/changelog/ — Release Changelog Lane
version: v1
status: draft
policy_label: public
owners:
  - <release-steward>
  - <data-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, release, changelog, manifests, corrections, withdrawals, rollback, audit]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-changelog-blueviolet)
![publication](https://img.shields.io/badge/publication-record-orange)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Changelog event types](#changelog-event-types) · [Required fields](#required-fields) · [Minimal changelog entry](#minimal-changelog-entry) · [Open verification](#open-verification)

---

## Purpose

`release/changelog/` records human-readable release history for KFM release activity.

This lane is for change summaries tied to governed release events. It should help maintainers answer:

- What changed?
- When did it change?
- Which release, manifest, correction, withdrawal, or rollback does it relate to?
- Which steward approved or recorded the change?
- Where are the evidence, validation, correction, and rollback pointers?

The changelog is not a substitute for ReleaseManifest records, receipts, validation outputs, policy review, or rollback cards. It is an index and narrative companion to those governed records.

---

## Status & authority

| Field | Value |
|---|---|
| Document type | Release changelog README |
| Owning root | `release/` |
| Changelog lane | `release/changelog/` |
| Status | Draft |
| Authority level | Human-readable release history. ReleaseManifest, correction, withdrawal, rollback, signature, receipt, policy, schema, and validation records outrank this README. |
| Default posture | Record the change, cite the governed record, and avoid treating prose as the source of truth. |
| Required reviewers | Release steward and docs steward; data steward or domain steward when the change affects release scope. |

---

## Repo fit

```text
release/
├── candidates/
├── manifests/
├── corrections/
├── rollbacks/
├── changelog/       # you are here
└── signatures/
```

This path belongs under the `release/` responsibility root. Release changelog entries are release records, not data artifacts. Published payloads belong under `data/published/` only after release approval.

---

## What belongs here

- Release changelog README files and yearly or release-series indexes.
- Human-readable summaries of approved release events.
- Links to ReleaseManifest records.
- Links to correction, withdrawal, rollback, validation, and signature records.
- Notes explaining why a release changed, was superseded, was corrected, or was withdrawn.
- Steward-facing history that helps reviewers trace release movement without opening every manifest.

---

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exported files, API payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Unreviewed candidate claims presented as release history.
- Release approval without a manifest or steward decision.
- Generated summaries used as sovereign truth.
- Secrets, credentials, private operational notes, or unredacted sensitive review material.

---

## Changelog event types

| Event type | Meaning |
|---|---|
| `RELEASED` | A governed release was approved and recorded. |
| `CORRECTED` | A released record or artifact was corrected. |
| `WITHDRAWN` | A release, candidate, or public surface was withdrawn from publication. |
| `ROLLED_BACK` | A release path was reverted or superseded by rollback action. |
| `SUPERSEDED` | A later release replaced an earlier release. |
| `RETRACTED_CLAIM` | A claim was removed or changed because support was insufficient. |
| `MANIFEST_UPDATED` | A ReleaseManifest changed under review or correction discipline. |
| `POLICY_REVIEW_UPDATED` | A policy or sensitivity review changed release posture. |
| `VALIDATION_UPDATED` | A validation result, receipt, or quality status changed. |
| `DOCS_UPDATED` | Release-facing documentation changed without changing the release artifact itself. |

---

## Required fields

Every changelog entry should capture:

- Event ID
- Event type
- Release or candidate pointer
- Date recorded
- Recorder
- Steward decision pointer
- Manifest pointer, when applicable
- Artifact pointer, when applicable
- Evidence or validation pointer, when applicable
- Correction, rollback, withdrawal, or supersession pointer, when applicable
- Public-surface effect
- Summary
- Open follow-up items

---

## Minimal changelog entry

```markdown
# <YYYY-MM-DD> — <event-title>

## Event
RELEASED / CORRECTED / WITHDRAWN / ROLLED_BACK / SUPERSEDED / RETRACTED_CLAIM / MANIFEST_UPDATED / POLICY_REVIEW_UPDATED / VALIDATION_UPDATED / DOCS_UPDATED

## Release or candidate pointer
<release manifest, candidate lane, or release record>

## Date recorded
<YYYY-MM-DD>

## Recorded by
<steward or maintainer>

## Governed record pointers
- Manifest: <path or N/A>
- Artifact: <path or N/A>
- Validation: <path or N/A>
- Correction: <path or N/A>
- Rollback: <path or N/A>
- Supersession: <path or N/A>

## Public-surface effect
<none / added / changed / corrected / withdrawn / rolled back>

## Summary
<short human-readable summary>

## Follow-up
<open items or none>
```

---

## Naming guidance

Prefer dated or release-scoped changelog files:

```text
release/changelog/
├── README.md
├── 2026.md
└── releases/
    └── <release-id>.md
```

The exact substructure is PROPOSED until confirmed by repo convention or ADR. Do not create parallel release-history roots without an ADR or migration note.

---

## Open verification

- [ ] Confirm CODEOWNERS for `release/changelog/`.
- [ ] Confirm whether changelog entries should be yearly files, per-release files, or both.
- [ ] Confirm canonical ReleaseManifest path and naming convention.
- [ ] Confirm correction, rollback, withdrawal, and signature record paths.
- [ ] Confirm whether changelog event IDs need a formal schema.
- [ ] Confirm whether changelog entries need generated index validation.

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | First changelog entry, new ReleaseManifest, correction, withdrawal, rollback, supersession, or changelog schema decision |
