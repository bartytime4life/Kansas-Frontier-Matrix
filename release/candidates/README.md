# `release/candidates/` — Release Candidate Review Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-readme
title: release/candidates/ — Release Candidate Review Index
version: v1
status: draft
policy_label: public
owners:
  - <release-steward>
  - <data-steward>
  - <domain-stewards>
updated: 2026-07-03
tags: [kfm, release, candidates, pre-publication, review, validation, rollback]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![publication](https://img.shields.io/badge/publication-not_yet-orange)
![review](https://img.shields.io/badge/review-required-red)
![posture](https://img.shields.io/badge/default-candidate_not_release-orange)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Repo fit](#repo-fit) · [Candidate lanes](#candidate-lanes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Candidate lifecycle](#candidate-lifecycle) · [Required review fields](#required-review-fields) · [Minimal candidate record](#minimal-candidate-record) · [Open verification](#open-verification)

---

## Purpose

`release/candidates/` is the parent review lane for proposed KFM release candidates.

A candidate is not a release. It is a pre-release review packet used before a governed release decision.

Candidate notes help stewards decide whether a proposed artifact or public surface is ready to move toward a ReleaseManifest, needs repair, should be deferred, or should be withdrawn.

Promotion must preserve the KFM lifecycle boundary:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move.

---

## Status & authority

| Field | Value |
|---|---|
| Document type | Release candidate parent README |
| Owning root | `release/` |
| Candidate lane | `release/candidates/` |
| Status | Draft |
| Authority level | Release guidance. Directory Rules, release discipline, policy, contracts, schemas, manifests, and final release records outrank this README. |
| Default posture | Candidate is not public until release gates pass and release steward approves promotion. |
| Required reviewers | Release steward, data steward, affected domain steward, and policy reviewer when needed. |

---

## Repo fit

```text
release/
├── candidates/       # you are here
│   ├── agriculture/
│   ├── archaeology/
│   ├── atmosphere/
│   ├── fauna/
│   ├── flora/
│   ├── geology/
│   ├── habitat/
│   ├── hazards/
│   ├── hydrology/
│   ├── people/
│   ├── people-dna-land/
│   ├── roads-rail-trade/
│   ├── settlement/
│   ├── settlements-infrastructure/
│   └── soil/
├── manifests/
├── corrections/
└── rollbacks/
```

This path belongs under the `release/` responsibility root. Release records are separate from data artifacts. Candidate payloads belong in the appropriate lifecycle data path. Published payloads belong under `data/published/` only after release approval.

---

## Candidate lanes

| Lane | Role | Notes |
|---|---|---|
| `agriculture/` | Agriculture candidate review. | Includes `county_year_panel_v0/` sublane. |
| `archaeology/` | Archaeology candidate review. | Requires careful policy review before release. |
| `atmosphere/` | Atmosphere candidate review. | Time validity matters. |
| `fauna/` | Fauna candidate review. | Policy review may be required. |
| `flora/` | Flora candidate review. | Policy review may be required. |
| `geology/` | Geology candidate review. | Natural-resource and geologic-context candidates. |
| `habitat/` | Habitat candidate review. | Includes `ecoregions/` and `habitat_fauna_thin_slice/`. |
| `hazards/` | Hazards candidate review. | Time validity and stale-state posture matter. |
| `hydrology/` | Hydrology candidate review. | Water, watershed, gauge, flow, and time-validity candidates. |
| `people/` | People candidate review. | Defaults to privacy review before release. |
| `people-dna-land/` | People, DNA, and land candidate review. | Includes `land-ownership/` sublane. |
| `roads-rail-trade/` | Roads, rail, and trade candidate review. | Compact README currently used due connector filtering. |
| `settlement/` | Settlement candidate review. | Compact polished README currently used due connector filtering. |
| `settlements-infrastructure/` | Settlement systems candidate review. | Polished non-operational README currently used. |
| `soil/` | Soil candidate review. | Survey, map unit, horizon, and interpretation candidates. |

---

## What belongs here

- Candidate README files and candidate-lane indexes.
- Candidate dossiers and readiness notes.
- Review checklists.
- Links to source, evidence, validation, policy, manifest, correction, and rollback records.
- Promote, defer, repair, block, supersede, withdraw, or manifest-handoff notes.
- Notes needed by release stewards before a ReleaseManifest is prepared.

---

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exported files, API payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Final release approval without release-steward review.
- Generated text used as release evidence.
- Secrets, credentials, or private operational material.

---

## Candidate lifecycle

| Candidate status | Meaning |
|---|---|
| `PROPOSED` | Candidate has been named but is not ready for release review. |
| `ASSEMBLING` | Candidate packet is being gathered. |
| `READY_FOR_REVIEW` | Candidate packet is ready for steward review. |
| `APPROVED_FOR_MANIFEST` | Candidate may move toward ReleaseManifest preparation. |
| `PROMOTED` | Candidate has become part of an approved release path. |
| `DEFERRED` | Candidate is valid to keep, but not ready now. |
| `REPAIR_REQUIRED` | Candidate needs correction before review can continue. |
| `BLOCKED` | Candidate cannot proceed until a named blocker is resolved. |
| `WITHDRAWN` | Candidate was removed from consideration. |
| `SUPERSEDED` | Candidate was replaced by a newer candidate. |

---

## Required review fields

Every domain candidate README or dossier should capture:

- Candidate name and version
- Candidate owner
- Candidate scope
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
PROPOSED / ASSEMBLING / READY_FOR_REVIEW / APPROVED_FOR_MANIFEST / PROMOTED / DEFERRED / REPAIR_REQUIRED / BLOCKED / WITHDRAWN / SUPERSEDED

## Candidate scope
<scope, geography, time period, and intended release surface>

## Candidate artifact pointer
<data/processed/... or staging reference>

## Proposed release target
<data/published/... or release target>

## Evidence and source closure
<references and status>

## Rights and policy status
<status and blockers>

## Validation summary
<summary and receipt reference>

## Release handoff
<manifest readiness and remaining blockers>

## Correction and rollback
<paths or notes>

## Decision
<decision and reason>
```

---

## Open verification

- [ ] Confirm CODEOWNERS for `release/candidates/`.
- [ ] Confirm candidate naming convention across all domain lanes.
- [ ] Confirm canonical ReleaseManifest schema path.
- [ ] Confirm validation receipt format and location.
- [ ] Confirm correction and rollback record paths.
- [ ] Confirm whether additional candidate lanes are needed.
- [ ] Expand compact lanes that were shortened by connector filtering.

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | New candidate lane, first ReleaseManifest handoff, candidate promotion, withdrawal, correction, or rollback update |
