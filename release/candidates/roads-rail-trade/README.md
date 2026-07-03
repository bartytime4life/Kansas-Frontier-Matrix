# `release/candidates/roads-rail-trade/` — Candidate Review Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-roads-rail-trade-readme
title: release/candidates/roads-rail-trade/ — Candidate Review Lane
version: v1
status: draft
policy_label: public
owners:
  - <domain-steward>
  - <release-steward>
  - <data-steward>
updated: 2026-07-03
tags: [kfm, release, candidates, roads-rail-trade, pre-publication, review]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-roads--rail--trade-slategray)
![publication](https://img.shields.io/badge/publication-not_yet-orange)
![review](https://img.shields.io/badge/review-required-red)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Repo fit](#repo-fit) · [Boundary](#boundary) · [Review fields](#review-fields) · [Open verification](#open-verification)

---

## Purpose

This directory holds draft candidate review notes for the roads-rail-trade domain.

A candidate is not a release. It is a review packet used before a governed release decision.

Promotion must preserve the KFM lifecycle boundary:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move.

---

## Status & authority

| Field | Value |
|---|---|
| Document type | Domain candidate README |
| Owning root | `release/` |
| Candidate lane | `release/candidates/roads-rail-trade/` |
| Status | Draft |
| Authority level | Release guidance. Directory Rules, release discipline, policy, contracts, schemas, manifests, and final release records outrank this README. |
| Default posture | Candidate is not public until release gates pass and release steward approves promotion. |
| Required reviewers | Domain steward, release steward, and data steward; policy reviewer when needed. |

---

## Repo fit

```text
release/
├── candidates/
│   └── roads-rail-trade/       # you are here
├── manifests/
├── corrections/
└── rollbacks/
```

---

## Boundary

Keep review notes here. Keep data, schemas, contracts, policy, manifests, correction records, and rollback records in their proper authority roots.

Published payloads belong under `data/published/` only after release approval.

---

## Review fields

- Candidate name and version
- Candidate owner
- Candidate scope
- Artifact pointer
- Proposed release target
- Source and evidence references
- Rights and policy status
- Time coverage
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
<scope and intended release surface>

## Candidate artifact pointer
<data/processed/... or staging reference>

## Proposed published target
<data/published/... or release target>

## Evidence and source closure
<references and status>

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
- [ ] Confirm candidate naming convention.
- [ ] Confirm processed and published artifact paths.
- [ ] Confirm ReleaseManifest path or schema.
- [ ] Confirm correction and rollback record paths.
- [ ] Confirm whether this lane needs sublanes.

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Polished README replacing minimal placeholder |
| Next review trigger | First candidate dossier, new sublane, manifest handoff, or release decision |
