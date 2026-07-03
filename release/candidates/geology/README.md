<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-geology-readme
title: release/candidates/geology/ — Geology Release Candidate Review Lane
type: per-domain-release-candidate-readme
version: v1
status: draft
owners:
  - <geology-domain-steward>
  - <release-steward>
  - <data-steward>
created: 2026-07-03
updated: 2026-07-03
policy_label: public
related:
  - release/README.md
  - release/candidates/
  - release/manifests/
  - release/corrections/
  - release/rollbacks/
  - data/processed/geology/
  - data/published/geology/
  - data/registry/sources/geology/
  - docs/domains/geology/
  - schemas/contracts/v1/
  - contracts/
  - policy/
  - docs/architecture/release-discipline.md
  - docs/doctrine/directory-rules.md
tags: [kfm, release, candidates, geology, pre-publication, validation, review, rollback]
notes:
  - "This directory is for geology release-candidate dossiers and readiness records, not final release approval or published artifact storage."
  - "Geology candidates remain pre-publication until evidence, source, rights, policy, validation, review, correction, and rollback posture are resolved."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `release/candidates/geology/` — Geology Release Candidate Review Lane

> Hold geology release-candidate dossiers so proposed geologic, mineral, geomorphic, subsurface, or natural-resource outputs can be reviewed before governed release.

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-geology-brown)
![publication](https://img.shields.io/badge/publication-not_yet-orange)

---

## Purpose

`release/candidates/geology/` is the geology pre-publication review lane. It holds candidate dossiers, readiness notes, validation summaries, and review decisions before a geology output becomes a released public or semi-public artifact.

A candidate is not a release. A candidate is a proposed release unit that still needs evidence closure, source closure, rights review, policy decision, validation, steward review, release manifest readiness, correction path, and rollback path.

The lifecycle boundary still applies:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move.

---

## Status & authority

| Field | Value |
|---|---|
| Document type | Per-domain release-candidate README |
| Owning root | `release/` |
| Subpath role | Geology candidate dossiers and pre-publication review records |
| Authority level | Draft guidance. Directory Rules, release discipline, policy, contracts, schemas, manifests, and final release records outrank this README. |
| Default posture | Candidate is not public until release gates pass and release steward approves promotion. |
| Required reviewers | Geology steward, release steward, and data steward; policy/sensitivity reviewer when public-facing risk exists. |

---

## Repo fit

```text
release/
├── candidates/
│   └── geology/       # you are here
├── manifests/
├── corrections/
└── rollbacks/
```

`release/candidates/geology/` records candidate review. It does not store published artifacts. Candidate payloads belong under the appropriate lifecycle data path. Published payloads belong under `data/published/geology/` only after release approval.

---

## What belongs here

- Geology candidate dossiers.
- Candidate readiness checklists.
- Candidate version notes.
- Source and evidence closure notes.
- Rights, policy, validation, and review summaries.
- Public-surface review summaries.
- Promote, block, defer, repair, or withdraw recommendations.
- Links to processed artifacts, proposed published targets, source records, evidence records, policy decisions, validation receipts, correction records, and rollback records.
- Notes required to prepare a ReleaseManifest.

---

## What does not belong here

- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads.
- Bulk datasets, map tiles, exported files, API payloads, or map-ready artifacts.
- Final release approval without release-steward review.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Generated narratives presented as release evidence or approval.
- Credentials or private operational material.

---

## Required candidate dossier

```markdown
# <geology-candidate-name> candidate dossier

## Status
PROPOSED / ASSEMBLING / READY_FOR_REVIEW / BLOCKED / DEFERRED / APPROVED_FOR_MANIFEST / PROMOTED / SUPERSEDED / WITHDRAWN

## Candidate identity
<name, version, owner, date, target release unit>

## Candidate artifact pointer
<data/processed/... or staging path; do not duplicate payload here>

## Proposed published target
<data/published/... or API/tile/export target>

## Evidence closure
<EvidenceRef / EvidenceBundle references and resolution status>

## Source closure
<SourceDescriptor / SourceIntakeRecord references and resolution status>

## Rights and policy posture
<license, attribution, policy decision, blockers>

## Validation summary
<schema, geometry, citation, quality, and public-surface checks>

## Review checklist
<domain, data, release, policy/sensitivity if needed>

## Promotion readiness
<ReleaseManifest readiness and remaining blockers>

## Correction path
<how errors would be corrected after promotion>

## Rollback path
<withdrawal, supersession, tombstone, or rollback path after promotion>

## Decision
<PROMOTE / BLOCK / DEFER / REPAIR / WITHDRAW with reason>
```

---

## Validation

| Check | Expected result |
|---|---|
| Candidate identity | Candidate is named, versioned, and owned. |
| Artifact pointer | Candidate points to processed/staged artifact without duplicating payload. |
| Proposed target | Proposed published target is named. |
| Source closure | Sources resolve to source records. |
| Evidence closure | Evidence resolves or candidate is blocked. |
| Rights and policy | Publication posture is clear or candidate is blocked. |
| Validation | Schema, geometry, citation, quality, and public-surface checks pass or block. |
| Correction path | Candidate has a correction path if promoted. |
| Rollback path | Candidate has rollback/withdrawal/supersession path if promoted. |

A candidate is not ready for manifest preparation until reviewers can explain what the candidate is, where the artifact is, what would be published, what evidence supports it, what rights allow it, what validates it, and what correction/rollback path exists.

---

## Review burden

| Change type | Required review |
|---|---|
| README-only wording | Docs steward or release steward |
| New geology candidate dossier | Geology domain steward + release steward |
| Candidate involving processed geology data | Geology domain steward + data steward + release steward |
| Candidate requiring rights or public-surface review | Policy/sensitivity reviewer + geology domain steward + release steward |
| Candidate recommended for manifest preparation | Release steward + geology domain steward + data steward |
| Candidate promoted, superseded, withdrawn, or deferred | Release steward + geology domain steward |

---

## Open verification

- [ ] Confirm CODEOWNERS for `release/candidates/geology/`.
- [ ] Confirm geology candidate naming and version convention.
- [ ] Confirm canonical ReleaseManifest schema path.
- [ ] Confirm processed/staged geology artifact paths.
- [ ] Confirm proposed published artifact paths under `data/published/geology/`.
- [ ] Confirm policy/sensitivity review requirements for geology candidates.
- [ ] Confirm validation receipt format and location.
- [ ] Confirm candidate-to-manifest handoff process.
- [ ] Confirm correction and rollback record paths for promoted geology candidates.

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | First geology release candidate, candidate dossier, promote/block/defer decision, ReleaseManifest handoff, or public artifact target PR |
