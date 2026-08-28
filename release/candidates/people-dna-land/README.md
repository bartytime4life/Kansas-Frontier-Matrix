# `release/candidates/people-dna-land/` — People, DNA, and Land Candidate Review Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-people-dna-land-readme
title: release/candidates/people-dna-land/ — People, DNA, and Land Candidate Review Lane
version: v1
status: draft
policy_label: public
owners:
  - <people-dna-land-domain-steward>
  - <release-steward>
  - <data-steward>
  - <policy-privacy-reviewer>
updated: 2026-07-03
tags: [kfm, release, candidates, people-dna-land, pre-publication, review, validation, rollback]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-people--dna--land-purple)
![publication](https://img.shields.io/badge/publication-not_yet-orange)
![review](https://img.shields.io/badge/review-required-red)
![posture](https://img.shields.io/badge/default-fail_closed-red)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Repo fit](#repo-fit) · [Current sublanes](#current-sublanes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Required review fields](#required-review-fields) · [Minimal candidate record](#minimal-candidate-record) · [Open verification](#open-verification)

---

## Purpose

This directory holds draft review notes for people-dna-land release candidates.

A candidate is not a release. It is a pre-release review packet used before a governed release decision.

Promotion must preserve the KFM lifecycle boundary:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move. This lane defaults to no public release until reviewers confirm evidence, rights, policy, privacy, validation, correction, and rollback posture.

---

## Status & authority

| Field | Value |
|---|---|
| Document type | People-dna-land release-candidate README |
| Owning root | `release/` |
| Candidate lane | `release/candidates/people-dna-land/` |
| Status | Draft |
| Authority level | Release guidance. Directory Rules, release discipline, policy, contracts, schemas, manifests, and final release records outrank this README. |
| Default posture | Candidate is not public until release gates pass and release steward approves promotion. |
| Required reviewers | People-dna-land steward, release steward, data steward, and policy/privacy reviewer. |

---

## Repo fit

```text
release/
├── candidates/
│   └── people-dna-land/       # you are here
│       └── land-ownership/
├── manifests/
├── corrections/
└── rollbacks/
```

This path belongs under the `release/` responsibility root. Release records are separate from data artifacts. Candidate payloads belong in the appropriate lifecycle data path. Published payloads belong under `data/published/` only after release approval.

---

## Current sublanes

| Sublane | Purpose | Status |
|---|---|---|
| `land-ownership/` | Candidate notes for land-ownership release review. | Draft sublane README exists. |

---

## What belongs here

- People-dna-land candidate notes.
- Readiness checklists.
- Review summaries.
- Links to source, evidence, validation, policy, manifest, correction, and rollback records.
- Rights, privacy, attribution, and public-surface review notes.
- Promote, defer, repair, block, or withdraw notes.
- Sublane indexes for candidate families.

---

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, parcel exports, tiles, API payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Personal records, DNA records, or direct land-record payloads.
- Final release approval without release-steward review.
- Generated text used as release evidence.

---

## Required review fields

- Candidate name and version
- Candidate owner
- People, DNA, and land scope
- Artifact pointer
- Proposed release target
- Source and evidence references
- Rights and attribution status
- Privacy and public-surface status
- Validation summary
- Release handoff status
- Correction path
- Rollback or supersession path
- Steward decision

---

## Minimal candidate record

```markdown
# <candidate-name>

## Status
PROPOSED / READY_FOR_REVIEW / APPROVED_FOR_MANIFEST / PROMOTED / DEFERRED / BLOCKED / WITHDRAWN

## Candidate scope
<people-dna-land scope, geography, time window, and intended release surface>

## Candidate artifact pointer
<data/processed/... or staging reference>

## Proposed published target
<data/published/... or release target>

## Evidence and source closure
<references and status>

## Rights, attribution, and privacy status
<status and blockers>

## Validation summary
<summary and receipt reference>

## Correction and rollback
<paths or notes>

## Decision
<decision and reason>
```

---

## Open verification

- [ ] Confirm CODEOWNERS for this path.
- [ ] Confirm people-dna-land candidate naming convention.
- [ ] Confirm processed and published artifact paths.
- [ ] Confirm ReleaseManifest path or schema.
- [ ] Confirm policy/privacy review requirements for this lane.
- [ ] Confirm correction and rollback record paths.
- [ ] Confirm whether more sublanes are needed beyond `land-ownership/`.

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | First people-dna-land candidate dossier, new sublane, manifest handoff, or release decision |
