# `release/candidates/settlement/` — Settlement Candidate Review Lane

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-settlement-brown)
![publication](https://img.shields.io/badge/publication-not_yet-orange)
![review](https://img.shields.io/badge/review-required-red)

## Purpose

Draft candidate review lane for the settlement domain.

A candidate is not a release. It is a review packet used before a governed release decision.

Promotion must preserve the KFM lifecycle boundary:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move.

## Status & authority

| Field | Value |
|---|---|
| Document type | Settlement candidate README |
| Owning root | `release/` |
| Candidate lane | `release/candidates/settlement/` |
| Status | Draft |
| Default posture | Candidate is not public until release gates pass and release steward approves promotion. |
| Required reviewers | Settlement steward, release steward, and data steward. |

## Boundary

Keep review notes here. Keep data, schemas, contracts, policy, manifests, correction records, and rollback records in their proper authority roots.

Published payloads belong under `data/published/` only after release approval.

## Review fields

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

## Open verification

- [ ] Confirm CODEOWNERS for this path.
- [ ] Confirm candidate naming convention.
- [ ] Confirm processed and published artifact paths.
- [ ] Confirm ReleaseManifest path or schema.
- [ ] Confirm correction and rollback record paths.
- [ ] Confirm whether this lane needs sublanes.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Polished README replacing minimal placeholder |
| Next review trigger | First candidate dossier, new sublane, manifest handoff, or release decision |
