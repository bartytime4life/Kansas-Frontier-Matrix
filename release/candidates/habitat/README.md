# `release/candidates/habitat/` — Habitat Candidate Review Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-habitat-readme
title: release/candidates/habitat/ — Habitat Candidate Review Lane
version: v1
status: draft
policy_label: public
owners:
  - <habitat-domain-steward>
  - <release-steward>
  - <data-steward>
updated: 2026-07-03
tags: [kfm, release, candidates, habitat, pre-publication, review, validation, rollback]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-habitat-green)
![publication](https://img.shields.io/badge/publication-not_yet-orange)
![review](https://img.shields.io/badge/review-required-red)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Repo fit](#repo-fit) · [Current sublanes](#current-sublanes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Required review fields](#required-review-fields) · [Minimal candidate record](#minimal-candidate-record) · [Open verification](#open-verification)

---

## Purpose

This directory holds draft review notes for habitat release candidates.

A candidate is not a release. It is a pre-release review packet used before a governed release decision.

Promotion must preserve the KFM lifecycle boundary:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move.

---

## Status & authority

| Field | Value |
|---|---|
| Document type | Habitat release-candidate README |
| Owning root | `release/` |
| Candidate lane | `release/candidates/habitat/` |
| Status | Draft |
| Authority level | Release guidance. Directory Rules, release discipline, policy, contracts, schemas, manifests, and final release records outrank this README. |
| Default posture | Candidate is not public until release gates pass and release steward approves promotion. |
| Required reviewers | Habitat steward, release steward, and data steward; policy/sensitivity reviewer when needed. |

---

## Repo fit

```text
release/
├── candidates/
│   └── habitat/       # you are here
│       ├── ecoregions/
│       └── habitat_fauna_thin_slice/
├── manifests/
├── corrections/
└── rollbacks/
```

This path belongs under the `release/` responsibility root. Release records are separate from data artifacts. Candidate payloads belong in the appropriate lifecycle data path. Published payloads belong under `data/published/` only after release approval.

---

## Current sublanes

| Sublane | Purpose | Status |
|---|---|---|
| `ecoregions/` | Candidate notes for habitat ecoregion releases. | Draft sublane README exists. |
| `habitat_fauna_thin_slice/` | Candidate notes for a habitat + fauna proof slice. | Draft sublane README exists. |

---

## What belongs here

- Habitat candidate notes.
- Readiness checklists.
- Review summaries.
- Links to source, evidence, validation, policy, manifest, correction, and rollback records.
- Promote, defer, repair, or withdraw notes.
- Sublane indexes for habitat candidate families.

---

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exported files, or API payloads.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Final release approval without release-steward review.
- Generated text used as release evidence.

---

## Required review fields

- Candidate name and version
- Candidate owner
- Habitat scope
- Artifact pointer
- Proposed release target
- Source and evidence references
- Rights and policy status
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
PROPOSED / READY_FOR_REVIEW / APPROVED_FOR_MANIFEST / PROMOTED / DEFERRED / WITHDRAWN

## Candidate scope
<habitat scope>

## Candidate artifact pointer
<data/processed/... or staging reference>

## Proposed published target
<data/published/... or release target>

## Evidence and source closure
<references and status>

## Rights and policy status
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
- [ ] Confirm habitat candidate naming convention.
- [ ] Confirm processed and published artifact paths.
- [ ] Confirm ReleaseManifest path or schema.
- [ ] Confirm correction and rollback record paths.
- [ ] Expand this README into the full KFM candidate template once connector filtering allows it.

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Polished README replacing greenfield stub |
| Next review trigger | First habitat candidate dossier, new sublane, manifest handoff, or release decision |
