# `release/correction_notices/flora/` — Flora Correction Notice Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-correction-notices-flora-readme
title: release/correction_notices/flora/ — Flora Correction Notice Lane
version: v1
status: draft
policy_label: public
owners:
  - <flora-domain-steward>
  - <release-steward>
  - <correction-steward>
  - <data-steward>
updated: 2026-07-03
tags: [kfm, release, correction-notices, flora, review, validation, audit]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-correction--notices-blueviolet)
![domain](https://img.shields.io/badge/domain-flora-green)
![publication](https://img.shields.io/badge/publication-governed-orange)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Path status](#path-status) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Notice types](#notice-types) · [Required notice fields](#required-notice-fields) · [Minimal correction notice](#minimal-correction-notice) · [Open verification](#open-verification)

---

## Purpose

`release/correction_notices/flora/` holds notice drafts for flora release corrections.

A correction notice is not the correction itself. It is a communication record that should point to governed release, correction, validation, policy, and changelog records.

This lane helps reviewers explain what changed, why the notice is needed, which governed correction record supports it, and what follow-up is still open.

Notice prose is not sovereign truth. Evidence, validation, policy review, release manifests, correction records, and steward decisions outrank notice text.

---

## Status & authority

| Field | Value |
|---|---|
| Document type | Flora correction notice README |
| Owning root | `release/` |
| Notice lane | `release/correction_notices/flora/` |
| Status | Draft |
| Authority level | Notice guidance. ReleaseManifest, correction record, validation receipt, policy review, changelog entry, rollback card, schema, and steward decision records outrank this README. |
| Default posture | Do not change release state from a notice draft alone. Require a governed correction record and steward decision. |
| Required reviewers | Flora steward, release steward, correction steward, data steward, and policy reviewer when needed. |

---

## Path status

This README documents the path exactly requested: `release/correction_notices/flora/`.

Current-session evidence confirms this README existed as a blank file before this update. Current-session evidence also confirms `release/correction_notices/README.md` currently exists only as a greenfield stub. Treat this flora notice lane as self-contained until the parent correction-notices README is expanded.

The related governed correction lane is `release/correction/`, whose README states that correction prose must not alter release state without steward decision and links to governed records.

---

## Repo fit

```text
release/
├── correction/
├── correction_notices/
│   └── flora/       # you are here
├── changelog/
├── candidates/
└── manifests/
```

This path belongs under the `release/` responsibility root because it records release correction notices. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

---

## What belongs here

- Flora correction notice drafts.
- Notice readiness checklists.
- Steward review summaries for notice wording.
- Links to release manifests, correction records, validation receipts, policy review notes, changelog entries, and affected release targets.
- Notes explaining whether the notice describes repair, supersession, withdrawal, rollback review, or no release-facing change.
- Follow-up tasks for changelog, manifest, correction, validation, or release-history updates.

---

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exported files, API payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Correction approval without steward review.
- Notice text used as evidence.
- Generated summaries used as sovereign truth.

---

## Notice types

| Notice type | Meaning |
|---|---|
| `INFORMATIONAL` | Explains a release-facing clarification without changing release state. |
| `CORRECTION` | Explains a bounded correction to flora release material. |
| `SUPERSESSION` | Explains that a newer governed record replaces an earlier one. |
| `WITHDRAWAL` | Explains that a release item or claim was withdrawn. |
| `ROLLBACK_REVIEW` | Explains that a correction has entered rollback review. |
| `POLICY_HOLD` | Explains that policy review delays or limits release-facing presentation. |
| `NO_PUBLIC_NOTICE` | Records that no release-facing notice is needed after review. |

---

## Required notice fields

Every flora correction notice should capture:

- Notice ID
- Notice type
- Affected flora release or candidate pointer
- Affected manifest, artifact, claim, or release target
- Correction record pointer
- Date drafted
- Drafted by
- Steward decision pointer
- Evidence pointer, when applicable
- Validation or receipt pointer, when applicable
- Policy review pointer, when applicable
- Changelog pointer, when applicable
- Release-facing effect
- Notice audience
- Summary
- Follow-up items

---

## Minimal correction notice

```markdown
# <notice-id>

## Status
DRAFT / READY_FOR_REVIEW / APPROVED / PUBLISHED / SUPERSEDED / WITHDRAWN / NO_PUBLIC_NOTICE

## Notice type
INFORMATIONAL / CORRECTION / SUPERSESSION / WITHDRAWAL / ROLLBACK_REVIEW / POLICY_HOLD / NO_PUBLIC_NOTICE

## Affected flora release or candidate
<release manifest, candidate lane, or release record>

## Affected record
<manifest entry, artifact, claim, release target, or N/A>

## Correction record
<release/correction/... pointer or N/A>

## Date drafted
<YYYY-MM-DD>

## Drafted by
<steward or maintainer>

## Governed record pointers
- Manifest: <path or N/A>
- Artifact: <path or N/A>
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Policy review: <path or N/A>
- Changelog: <path or N/A>
- Rollback review: <path or N/A>

## Release-facing effect
<none / changed / withdrawn / superseded / repaired / review pending>

## Notice text
<approved or draft notice text>

## Follow-up
<open items or none>

## Decision
<decision, steward, and reason>
```

---

## Open verification

- [ ] Expand `release/correction_notices/README.md` so this flora lane inherits from a complete parent notice contract.
- [ ] Confirm CODEOWNERS for this path.
- [ ] Confirm correction notice naming convention.
- [ ] Confirm release correction pointer format.
- [ ] Confirm changelog event linkage.
- [ ] Confirm policy review linkage for flora notices.
- [ ] Confirm whether notice records need schema validation.

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | First flora correction notice, parent notice-lane expansion, correction record, changelog update, withdrawal, supersession, rollback review, or notice schema decision |
