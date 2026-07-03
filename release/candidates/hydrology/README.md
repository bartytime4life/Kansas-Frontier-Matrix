# `release/candidates/hydrology/` — Hydrology Candidate Review Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-hydrology-readme
title: release/candidates/hydrology/ — Hydrology Candidate Review Lane
version: v1
status: draft
policy_label: public
owners:
  - <hydrology-domain-steward>
  - <release-steward>
  - <data-steward>
updated: 2026-07-03
tags: [kfm, release, candidates, hydrology, pre-publication, review, validation, rollback]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-hydrology-blue)
![publication](https://img.shields.io/badge/publication-not_yet-orange)
![review](https://img.shields.io/badge/review-required-red)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Required review fields](#required-review-fields) · [Minimal candidate record](#minimal-candidate-record) · [Open verification](#open-verification)

---

## Purpose

This directory holds draft review notes for hydrology release candidates.

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
| Document type | Hydrology release-candidate README |
| Owning root | `release/` |
| Candidate lane | `release/candidates/hydrology/` |
| Status | Draft |
| Authority level | Release guidance. Directory Rules, release discipline, policy, contracts, schemas, manifests, and final release records outrank this README. |
| Default posture | Candidate is not public until release gates pass and release steward approves promotion. |
| Required reviewers | Hydrology steward, release steward, and data steward; policy/sensitivity reviewer when needed. |

---

## Repo fit

```text
release/
├── candidates/
│   └── hydrology/       # you are here
├── manifests/
├── corrections/
└── rollbacks/
```

This path belongs under the `release/` responsibility root. Release records are separate from data artifacts. Candidate payloads belong in the appropriate lifecycle data path. Published payloads belong under `data/published/` only after release approval.

---

## What belongs here

- Hydrology candidate notes.
- Readiness checklists.
- Review summaries.
- Links to source, evidence, validation, policy, manifest, correction, and rollback records.
- Waterbody, watershed, stream, aquifer, gauge, flow, or time-validity notes.
- Promote, defer, repair, or withdraw notes.
- Sublane indexes for hydrology candidate families.

---

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exported files, or API payloads.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Final release approval without release-steward review.
- Generated text used as release evidence.
- Operational emergency instructions or public-safety directives.

---

## Required review fields

- Candidate name and version
- Candidate owner
- Hydrology type and scope
- Artifact pointer
- Proposed release target
- Source and evidence references
- Rights and policy status
- Time validity and stale-state posture
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
<waterbody, watershed, gauge, aquifer, flow, time window, and intended release surface>

## Candidate artifact pointer
<data/processed/... or staging reference>

## Proposed published target
<data/published/... or release target>

## Evidence and source closure
<references and status>

## Rights and policy status
<status and blockers>

## Time validity
<observation, model, update, or stale-state notes>

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
- [ ] Confirm hydrology candidate naming convention.
- [ ] Confirm processed and published artifact paths.
- [ ] Confirm ReleaseManifest path or schema.
- [ ] Confirm stale-state and time-validity rules for hydrology candidates.
- [ ] Confirm correction and rollback record paths.
- [ ] Confirm whether hydrology needs sublanes for watersheds, streams, reservoirs, aquifers, gauges, or other candidate families.

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | First hydrology candidate dossier, new sublane, manifest handoff, or release decision |
