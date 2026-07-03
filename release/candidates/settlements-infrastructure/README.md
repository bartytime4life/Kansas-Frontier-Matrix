# `release/candidates/settlements-infrastructure/` — Settlement Systems Candidate Review Lane

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-settlement--systems-brown)
![publication](https://img.shields.io/badge/publication-not_yet-orange)
![review](https://img.shields.io/badge/review-required-red)

## Purpose

Draft candidate review lane for the settlement systems domain.

A candidate is not a release. It is a review packet used before a governed release decision.

Promotion must preserve the KFM lifecycle boundary:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move.

## Status & authority

| Field | Value |
|---|---|
| Document type | Settlement systems candidate README |
| Owning root | `release/` |
| Candidate lane | `release/candidates/settlements-infrastructure/` |
| Status | Draft |
| Default posture | Candidate is not released until release gates pass and release steward approves promotion. |
| Required reviewers | Domain steward, release steward, and data steward. |

## Repo fit

```text
release/
├── candidates/
│   └── settlements-infrastructure/       # you are here
├── manifests/
├── corrections/
└── rollbacks/
```

## Boundary

Keep review notes here. Keep data, schemas, contracts, policy, manifests, correction records, and rollback records in their proper authority roots.

Released payloads belong under `data/published/` only after approval.

## What belongs here

- Candidate notes.
- Readiness checklists.
- Review summaries.
- Links to source, evidence, validation, manifest, correction, and rollback records.
- Promote, defer, repair, block, or withdraw notes.
- Sublane indexes for candidate families.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exported files, API payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Final release approval without release-steward review.
- Generated text used as release evidence.

## Review fields

- Candidate name and version
- Candidate owner
- Candidate scope
- Geography and time period
- Artifact pointer
- Proposed release target
- Source and evidence references
- Rights and policy status
- Validation summary
- Release handoff status
- Correction path
- Rollback or supersession path
- Steward decision

## Minimal candidate record

```markdown
# <candidate-name>

## Status
PROPOSED / READY_FOR_REVIEW / APPROVED_FOR_MANIFEST / PROMOTED / DEFERRED / BLOCKED / WITHDRAWN

## Candidate scope
<scope, geography, time period, and intended release surface>

## Candidate artifact pointer
<data/processed/... or staging reference>

## Proposed release target
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

## Open verification

- [ ] Confirm CODEOWNERS for this path.
- [ ] Confirm candidate naming convention.
- [ ] Confirm processed and released artifact paths.
- [ ] Confirm ReleaseManifest path or schema.
- [ ] Confirm correction and rollback record paths.
- [ ] Confirm whether this lane needs sublanes.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Polished README replacing minimal placeholder |
| Next review trigger | First candidate dossier, new sublane, manifest handoff, or release decision |
