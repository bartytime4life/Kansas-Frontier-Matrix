# `release/people-dna-land/` — People DNA Land Release Review Lane

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![domain](https://img.shields.io/badge/domain-people--dna--land-purple)
![review](https://img.shields.io/badge/review-required-red)
![policy](https://img.shields.io/badge/policy-deny--by--default-red)
![posture](https://img.shields.io/badge/default-fail--closed-red)

## Purpose

`release/people-dna-land/` is the release-review parent lane for people-dna-land material.

This folder is for release-facing indexes, dated review groups, steward decisions, and pointers to governed support records. It is not a data home and it is not a public payload lane.

The default posture is fail-closed. No release status should be inferred from this README alone.

## Status & authority

| Field              | Value                                                                                                                                                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Document type      | Domain release-review parent README                                                                                                                                                                                              |
| Owning root        | `release/`                                                                                                                                                                                                                       |
| Parent lane        | `release/people-dna-land/`                                                                                                                                                                                                       |
| Status             | Draft                                                                                                                                                                                                                            |
| Authority level    | Parent guidance and index. Final release records, steward decisions, validation receipts, evidence bundles, policy reviews, manifests, correction records, rollback records, notices, and changelog entries outrank this README. |
| Default posture    | No release unless evidence, rights, review, validation, correction path, and rollback path are resolved.                                                                                                                         |
| Required reviewers | People-dna-land steward, release steward, data steward, policy reviewer, and docs steward.                                                                                                                                       |

## Repo fit

```text
release/
├── people-dna-land/       # you are here
│   └── 2026-05-15/
├── candidates/
│   └── people-dna-land/
├── manifests/
├── decisions/
├── changelog/
├── correction/
├── corrections/
└── correction_notices/
```

This path belongs under the `release/` responsibility root because it records release review and publication posture for a domain. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## Current dated lanes

| Sublane       | Scope                                                                                          | Status               |
| ------------- | ---------------------------------------------------------------------------------------------- | -------------------- |
| `2026-05-15/` | Dated release-review group for people-dna-land material prepared or grouped around 2026-05-15. | Draft README exists. |

Add new dated sublanes only when there is a real dated review group, release decision, manifest, correction, notice, or steward review event to index.

## Parent lane responsibilities

| Responsibility      | Expectation                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------- |
| Indexing            | List dated release-review groups and their status.                                            |
| Scope               | Identify the dated group, release family, review family, or release target.                   |
| Evidence            | Point to evidence records when claims depend on evidence.                                     |
| Validation          | Point to validation receipts or checks.                                                       |
| Rights review       | Point to rights, attribution, and public-surface review records when needed.                  |
| Sensitivity posture | State whether material is public-safe, generalized, redacted, restricted, held, or not ready. |
| Decision            | Point to steward decisions that support release state.                                        |
| Manifest            | Point to manifest records when release state is proposed or approved.                         |
| Correction path     | Point to correction records when a release-facing state changes.                              |
| Rollback path       | Point to rollback review when reversal planning is required.                                  |

## What belongs here

* Parent README and dated release-review indexes.
* Dated release-review group folders.
* Pointers to candidates, manifests, decisions, validation receipts, evidence records, policy reviews, corrections, notices, rollback records, and changelog entries.
* Review notes explaining release scope, sensitivity posture, public-surface posture, and follow-up tasks.
* Lightweight status tables that help stewards find governed records.

## What does not belong here

* Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
* Bulk datasets, exports, service payloads, or map-ready artifacts.
* Source descriptors, schemas, contracts, policy files, or validator code.
* Restricted domain payloads or direct identifying records.
* Generated summaries used as sovereign truth.
* Final release approval without governed release records and steward review.

## Required parent index fields

Every dated review group listed here should eventually capture:

* Review group date
* Review group path
* Release or candidate pointer
* Manifest pointer, when applicable
* Decision pointer, when applicable
* Domain scope
* Evidence pointer, when applicable
* Validation pointer, when applicable
* Rights or policy review pointer, when applicable
* Correction pointer, when applicable
* Notice pointer, when applicable
* Rollback pointer, when applicable
* Changelog pointer, when applicable
* Release-facing effect
* Public-surface posture
* Steward review state
* Follow-up items

## Minimal dated group index record

```markdown
## <YYYY-MM-DD>

| Field | Value |
|---|---|
| Review group path | `release/people-dna-land/<YYYY-MM-DD>/` |
| Status | DRAFT / READY_FOR_REVIEW / APPROVED / HELD / SUPERSEDED / CORRECTED / NO_ACTION |
| Scope | <review group scope or release target> |
| Candidate pointer | <path or N/A> |
| Manifest pointer | <path or N/A> |
| Decision pointer | <path or N/A> |
| Evidence pointer | <path or N/A> |
| Validation pointer | <path or N/A> |
| Policy review | <path or N/A> |
| Correction / notice / rollback | <paths or N/A> |
| Release-facing effect | <none / ready / held / corrected / superseded / review pending> |
| Public-surface posture | PUBLIC_SAFE / GENERALIZED / REDACTED / RESTRICTED / HELD / NOT_READY |
| Follow-up | <open items or none> |
```

## Review checklist

* [ ] Dated review group exists and has a README.
* [ ] Release or candidate pointer is present.
* [ ] Evidence support is linked when claims depend on evidence.
* [ ] Validation support is linked when validation is required.
* [ ] Rights or policy review is linked when release posture requires it.
* [ ] Manifest and decision pointers are linked when release state changes.
* [ ] Correction, notice, rollback, and changelog pointers are linked when applicable.
* [ ] Public-surface posture is explicit.
* [ ] No data payloads are stored in this lane.

## Naming guidance

Dated sublanes should use ISO dates:

```text
YYYY-MM-DD/
```

Records inside a dated sublane should use:

```text
<YYYY-MM-DD>_<people-dna-land-scope>_<record-type>.md
```

Examples:

```text
2026-05-15/
2026-05-15_people-dna-land_release-review.md
2026-05-15_land-ownership_review-summary.md
2026-05-15_people-dna-land_policy-posture.md
```

## Open verification

* [ ] Confirm whether `release/people-dna-land/` is the canonical parent lane for dated release review groups.
* [ ] Confirm CODEOWNERS for this parent lane.
* [ ] Confirm dated release-review record ID format.
* [ ] Confirm evidence pointer format.
* [ ] Confirm validation receipt pointer format.
* [ ] Confirm rights and policy review pointer formats.
* [ ] Confirm manifest, decision, changelog, correction, notice, and rollback pointer formats.
* [ ] Confirm whether records in this lane require schema validation before release approval.
* [ ] Confirm whether additional dated sublanes exist or should be created.

## Last reviewed

| Field               | Value                                                                                                                                                     |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Last reviewed       | 2026-07-03                                                                                                                                                |
| Review status       | Draft README content prepared; connector blocked commit                                                                                                   |
| Next review trigger | New dated review group, first dated review record, manifest link, release decision, policy review, correction, notice, rollback, or changelog integration |

