# `release/correction_notices/` — Release Correction Notice Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-correction-notices-readme
title: release/correction_notices/ — Release Correction Notice Index
version: v1
status: draft
policy_label: public
owners:
  - <release-steward>
  - <correction-steward>
  - <docs-steward>
  - <domain-stewards>
updated: 2026-07-03
tags: [kfm, release, correction-notices, review, validation, audit, changelog]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-correction--notices-blueviolet)
![publication](https://img.shields.io/badge/publication-governed-orange)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Path status](#path-status) · [Repo fit](#repo-fit) · [Current sublanes](#current-sublanes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Notice types](#notice-types) · [Required notice fields](#required-notice-fields) · [Minimal correction notice](#minimal-correction-notice) · [Open verification](#open-verification)

---

## Purpose

`release/correction_notices/` is the parent lane for KFM release correction notices.

A correction notice is not the correction itself. It is a communication record that should point to governed release, correction, validation, policy, manifest, changelog, and steward-decision records.

This lane helps reviewers and maintainers explain what changed, why a notice is needed, which governed correction record supports it, and what follow-up remains open.

Notice prose is not sovereign truth. Evidence, validation, policy review, release manifests, correction records, changelog entries, and steward decisions outrank notice text.

---

## Status & authority

| Field | Value |
|---|---|
| Document type | Release correction notice parent README |
| Owning root | `release/` |
| Notice lane | `release/correction_notices/` |
| Status | Draft |
| Authority level | Notice guidance. ReleaseManifest, correction record, validation receipt, policy review, changelog entry, rollback card, schema, and steward decision records outrank this README. |
| Default posture | Do not change release state from notice prose alone. Require a governed correction record and steward decision. |
| Required reviewers | Release steward, correction steward, docs steward, data steward, affected domain steward, and policy reviewer when needed. |

---

## Path status

This README documents the path exactly requested: `release/correction_notices/`.

Current-session evidence confirms this parent README was a greenfield stub before this update. Current-session evidence also confirms the related `release/correction/` lane exists and states that correction prose must not alter release state without steward decision and links to governed records.

Treat this notice lane as a communication and review lane, not as the canonical correction record home.

---

## Repo fit

```text
release/
├── correction/
├── correction_notices/       # you are here
│   ├── flora/
│   ├── hydrology/
│   └── roads-rail-trade/
├── changelog/
├── candidates/
└── manifests/
```

This path belongs under the `release/` responsibility root because it records release correction notices. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

---

## Current sublanes

| Sublane | Purpose | Status |
|---|---|---|
| `flora/` | Flora release correction notices. | Draft README exists. |
| `hydrology/` | Hydrology release correction notices, including time-validity notes. | Draft README exists. |
| `roads-rail-trade/` | Roads, rail, and trade release correction notices. | Draft README exists. |

---

## What belongs here

- Correction-notice README files and sublane indexes.
- Notice drafts and notice readiness checklists.
- Steward review summaries for notice wording.
- Links to release manifests, correction records, validation receipts, policy review notes, changelog entries, and affected release targets.
- Notes explaining whether a notice describes repair, supersession, withdrawal, review hold, time or version update, or no release-facing change.
- Follow-up tasks for changelog, manifest, correction, validation, or release-history updates.

---

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exported files, API payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Correction approval without steward review.
- Notice text used as evidence.
- Generated summaries used as sovereign truth.
- Secrets, credentials, or private operational material.

---

## Notice types

| Notice type | Meaning |
|---|---|
| `INFORMATIONAL` | Clarifies release-facing material without changing release state. |
| `CORRECTION` | Explains a bounded correction. |
| `TIME_VALIDITY_UPDATE` | Explains a changed time window, stale-state posture, or validity note. |
| `VERSION_UPDATE` | Explains a changed version, interpretation, or release-context note. |
| `SUPERSESSION` | Explains that a newer governed record replaces an earlier one. |
| `WITHDRAWAL` | Explains that a release item or claim was withdrawn. |
| `ROLLBACK_REVIEW` | Explains that a correction has entered rollback review. |
| `POLICY_HOLD` | Explains that policy review delays or limits release-facing presentation. |
| `NO_NOTICE` | Records that no notice is needed after review. |

---

## Required notice fields

Every correction notice should capture:

- Notice ID
- Notice type
- Affected release or candidate pointer
- Affected manifest, artifact, claim, or release target
- Domain scope
- Time, version, or interpretation context, when applicable
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
DRAFT / READY_FOR_REVIEW / APPROVED / PUBLISHED / SUPERSEDED / WITHDRAWN / NO_NOTICE

## Notice type
INFORMATIONAL / CORRECTION / TIME_VALIDITY_UPDATE / VERSION_UPDATE / SUPERSESSION / WITHDRAWAL / ROLLBACK_REVIEW / POLICY_HOLD / NO_NOTICE

## Affected release or candidate
<release manifest, candidate lane, or release record>

## Affected record
<manifest entry, artifact, claim, release target, or N/A>

## Domain scope
<domain scope or feature family>

## Context
<time, version, interpretation, or policy context; N/A when not applicable>

## Correction record
<release/correction/... pointer or N/A>

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

- [ ] Confirm CODEOWNERS for `release/correction_notices/`.
- [ ] Confirm correction notice naming convention.
- [ ] Confirm release correction pointer format.
- [ ] Confirm changelog event linkage.
- [ ] Confirm policy review linkage for notice records.
- [ ] Confirm whether notice records need schema validation.
- [ ] Confirm whether additional domain notice lanes are needed.

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | New domain notice lane, first notice, correction record, changelog update, withdrawal, supersession, rollback review, or notice schema decision |
