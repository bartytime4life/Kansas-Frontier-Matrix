<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidate-agriculture-county-year-panel-v0
title: release/candidates/agriculture/county_year_panel_v0/ — Agriculture County-Year Panel v0 Candidate Dossier
type: release-candidate-dossier
version: v0
status: draft
owners:
  - <agriculture-domain-steward>
  - <release-steward>
  - <data-steward>
created: 2026-07-03
updated: 2026-07-03
policy_label: public
related:
  - release/candidates/agriculture/README.md
  - release/agriculture/README.md
  - release/README.md
  - release/manifests/
  - release/corrections/
  - release/rollbacks/
  - data/processed/agriculture/
  - data/published/agriculture/
  - data/registry/sources/agriculture/
  - docs/domains/agriculture/
  - schemas/contracts/v1/
  - contracts/
  - policy/
  - docs/architecture/release-discipline.md
  - docs/doctrine/directory-rules.md
tags: [kfm, release, candidate, agriculture, county-year-panel, v0, pre-publication, validation]
notes:
  - "This is a release-candidate dossier shell for county_year_panel_v0. It is not a released artifact, final ReleaseManifest, approval, data payload, schema, source record, or policy rule."
  - "Artifact pointers, evidence links, validation receipts, and manifest references are NEEDS VERIFICATION until maintainers add concrete records."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `county_year_panel_v0/` — Agriculture County-Year Panel v0 Candidate Dossier

> **Candidate status:** `PROPOSED` — not released and not approved for manifest preparation.

![status](https://img.shields.io/badge/status-draft-yellow)
![candidate](https://img.shields.io/badge/candidate-county_year_panel_v0-blueviolet)
![domain](https://img.shields.io/badge/domain-agriculture-green)
![release](https://img.shields.io/badge/release-not_approved-orange)

---

## Purpose

This folder records the release-candidate dossier for `county_year_panel_v0`, a proposed agriculture-domain candidate. The working assumption is that the candidate represents a county-by-year agriculture panel, but the artifact path, schema, source set, evidence, and manifest are **NEEDS VERIFICATION** until maintainers add concrete records.

A candidate is not a release. This dossier supports review before any governed release decision.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move.

---

## Candidate identity

| Field | Value |
|---|---|
| Candidate id | `county_year_panel_v0` |
| Domain | `agriculture` |
| Candidate type | County-year panel release candidate |
| Status | `PROPOSED` |
| Release state | Not released |
| Candidate owner | `<agriculture-domain-steward>` |
| Release owner | `<release-steward>` |
| Data owner | `<data-steward>` |
| Artifact pointer | NEEDS VERIFICATION |
| Proposed published target | NEEDS VERIFICATION |
| ReleaseManifest | NEEDS VERIFICATION |

---

## Repo fit

```text
release/
└── candidates/
    └── agriculture/
        └── county_year_panel_v0/
            └── README.md
```

This folder holds the candidate dossier only. Candidate payloads belong in lifecycle data paths. Final release manifests normally belong under `release/manifests/` or another accepted release-manifest lane.

---

## Candidate scope

| Item | Status | Notes |
|---|---|---|
| Candidate name | CONFIRMED | `county_year_panel_v0` from path. |
| Domain | CONFIRMED | `agriculture` from path. |
| Panel grain | PROPOSED | County by year, inferred from candidate name. |
| Version | CONFIRMED | `v0` from path. |
| Source set | NEEDS VERIFICATION | Add source references. |
| Schema/contract | NEEDS VERIFICATION | Add schema and contract references. |
| Artifact path | NEEDS VERIFICATION | Add processed/staged artifact pointer. |
| Release readiness | NEEDS VERIFICATION | Complete checklist below. |

---

## What belongs here

- Candidate dossier notes for `county_year_panel_v0`.
- Readiness checklist and decision history.
- Links to processed candidate artifacts, not payload copies.
- Links to source, evidence, schema, contract, policy, validation, manifest, correction, and rollback records.
- Promote, block, defer, repair, or withdraw decision notes.

## What does not belong here

- Data payloads or bulk exports.
- Lifecycle artifacts that belong under `data/`.
- Final release approval without release-steward review.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Generated text presented as evidence or release approval.

---

## Required pointers

| Pointer | Required before promotion? | Status |
|---|---:|---|
| Candidate artifact path | Yes | NEEDS VERIFICATION |
| Proposed published target | Yes | NEEDS VERIFICATION |
| Source references | Yes | NEEDS VERIFICATION |
| Evidence references | Yes | NEEDS VERIFICATION |
| Schema/contract references | Yes | NEEDS VERIFICATION |
| Policy decision reference | Yes | NEEDS VERIFICATION |
| Validation receipt reference | Yes | NEEDS VERIFICATION |
| ReleaseManifest reference | Yes | NEEDS VERIFICATION |
| Correction path | Yes | NEEDS VERIFICATION |
| Rollback path | Yes | NEEDS VERIFICATION |

---

## Review checklist

- [ ] Candidate artifact is identified by path or stable reference.
- [ ] Source references resolve.
- [ ] Evidence references resolve.
- [ ] Rights and attribution are documented.
- [ ] Policy decision is recorded.
- [ ] Schema and contract validation pass.
- [ ] Data-quality checks are summarized.
- [ ] ReleaseManifest is prepared or explicitly blocked.
- [ ] Correction path is documented.
- [ ] Rollback, withdrawal, or supersession path is documented.
- [ ] Required stewards have reviewed the candidate.

---

## Decision log

| Date | Decision | Reviewer | Notes |
|---|---|---|---|
| 2026-07-03 | PROPOSED | `<release-steward>` | Initial dossier shell created. No release approval granted. |

---

## Current decision

`BLOCKED_FOR_EVIDENCE_AND_VALIDATION`

The candidate should not move to manifest preparation until required pointers, validation, policy review, correction path, and rollback path are complete.

---

## Open verification

- [ ] Confirm the concrete artifact path for `county_year_panel_v0`.
- [ ] Confirm the panel grain and fields.
- [ ] Confirm source references.
- [ ] Confirm schema and contract references.
- [ ] Confirm evidence references.
- [ ] Confirm validation receipt location.
- [ ] Confirm proposed published target.
- [ ] Confirm ReleaseManifest path or id.
- [ ] Confirm correction record path.
- [ ] Confirm rollback or withdrawal path.
- [ ] Confirm CODEOWNERS for this candidate folder.

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft candidate dossier shell replacing blank file |
| Next review trigger | First concrete artifact pointer, source/evidence references, validation receipt, policy decision, manifest handoff, or promote/block/defer decision |
