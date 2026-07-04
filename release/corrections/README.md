# `release/corrections/` — Release Corrections Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-corrections-readme
title: release/corrections/ — Release Corrections Index
version: v1
status: draft
policy_label: public
owners:
  - <release-steward>
  - <correction-steward>
  - <data-steward>
  - <docs-steward>
  - <domain-stewards>
updated: 2026-07-03
tags: [kfm, release, corrections, review, validation, changelog, notices, rollback]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-corrections-blueviolet)
![publication](https://img.shields.io/badge/publication-governed-orange)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Path status](#path-status) · [Repo fit](#repo-fit) · [Current sublanes](#current-sublanes) · [Relation to sibling release lanes](#relation-to-sibling-release-lanes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Correction outcomes](#correction-outcomes) · [Required correction fields](#required-correction-fields) · [Minimal correction record](#minimal-correction-record) · [Review checklist](#review-checklist) · [Open verification](#open-verification)

---

## Purpose

`release/corrections/` is the parent lane for domain-scoped KFM release correction records.

A correction record is a governed review artifact. It exists to document a release-facing problem, connect that problem to evidence and validation, record the steward decision, and preserve the release-history trail.

Correction records should answer:

* What release, release candidate, manifest entry, artifact, claim, or release target is affected?
* Why is correction needed?
* Which governed evidence, validation record, receipt, policy review, or steward decision supports the correction?
* What release-facing effect should reviewers expect?
* Does the correction require a notice, replacement, review hold, rollback review, or no action?
* Which steward approved the decision?
* What follow-up remains open?

Correction is a governed state transition, not a file move.

This lane is not a data-artifact home and does not replace release manifests, validation receipts, evidence records, policy review, changelog entries, correction notices, rollback records, or steward decisions.

---

## Status & authority

| Field              | Value                                                                                                                                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Document type      | Release corrections parent README                                                                                                                                                                            |
| Owning root        | `release/`                                                                                                                                                                                                   |
| Correction lane    | `release/corrections/`                                                                                                                                                                                       |
| Status             | Draft                                                                                                                                                                                                        |
| Authority level    | Guidance and index only. ReleaseManifest, validation receipt, evidence record, policy review, changelog entry, correction notice, rollback record, schema, and steward decision records outrank this README. |
| Default posture    | Do not change release state from prose alone. Require steward decision and governed record pointers.                                                                                                         |
| Required reviewers | Release steward, correction steward, data steward, affected domain steward, and policy reviewer when needed.                                                                                                 |

---

## Path status

This README documents the requested plural path: `release/corrections/`.

The repo also has `release/correction/`, which is already documented as a singular correction review lane. Treat this plural lane as draft until maintainers confirm whether the canonical correction home is:

1. `release/correction/` only,
2. `release/corrections/` only, or
3. both paths with distinct meanings.

Recommended distinction, pending maintainer confirmation:

| Path                           | Proposed role                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------- |
| `release/correction/`          | General correction review lane and cross-cutting correction workflow notes.           |
| `release/corrections/`         | Domain-scoped correction records.                                                     |
| `release/correction_notices/`  | Release-facing or steward-facing notice drafts that communicate approved corrections. |
| `release/correction/rollback/` | Rollback review notes tied to correction decisions.                                   |

Until that convention is confirmed, do not move files only to satisfy naming preference. Record the uncertainty and keep changes reversible.

---

## Repo fit

```text
release/
├── correction/
├── corrections/       # you are here
│   ├── atmosphere/
│   ├── roads-rail-trade/
│   └── settlements-infrastructure/
├── correction_notices/
├── changelog/
├── candidates/
└── manifests/
```

This path belongs under the `release/` responsibility root because it records release correction review. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

---

## Current sublanes

| Sublane                       | Purpose                                                                                | Status               |
| ----------------------------- | -------------------------------------------------------------------------------------- | -------------------- |
| `atmosphere/`                 | Atmosphere release correction records, including time-coverage or stale-state context. | Draft README exists. |
| `roads-rail-trade/`           | Roads, rail, and trade release correction records.                                     | Draft README exists. |
| `settlements-infrastructure/` | Settlement systems release correction records.                                         | Draft README exists. |

Additional domain lanes should be added only when there is an actual correction-record need or a maintainers’ decision to pre-stage the lane.

---

## Relation to sibling release lanes

| Lane                           | Relationship                                                                                                           |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| `release/candidates/`          | Candidate records may become correction targets if a release candidate is revised, withdrawn, or superseded.           |
| `release/manifests/`           | Manifest records identify the governed release state that a correction may affect.                                     |
| `release/changelog/`           | Changelog entries record release-history events and should link to approved corrections.                               |
| `release/correction/`          | Singular correction lane; currently a related draft convention.                                                        |
| `release/correction_notices/`  | Notice drafts that communicate approved or reviewed correction decisions.                                              |
| `release/correction/rollback/` | Rollback review notes tied to correction decisions.                                                                    |
| `data/published/`              | Published artifacts live there, not here. Correction records may point to published artifacts but must not store them. |

---

## What belongs here

* Correction README files and sublane indexes.
* Domain-scoped correction records.
* Correction readiness notes.
* Steward review summaries.
* Links to release manifests, validation receipts, evidence records, changelog entries, correction notices, rollback review records, and related release records.
* Notes explaining whether the outcome is repair, replacement, review hold, defer, no action, notice required, or rollback review required.
* Time, version, interpretation, or policy context needed to understand the correction.
* Follow-up tasks for changelog, manifest, validation, notice, rollback review, or release-history updates.

---

## What does not belong here

* Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
* Bulk datasets, tiles, exports, API payloads, or map-ready artifacts.
* Source descriptors.
* Schemas.
* Contracts.
* Policy rule files.
* Validator code.
* Secrets, credentials, or private operational material.
* Correction approval without steward review.
* Generated summaries used as sovereign truth.
* Notice text unless it points to a governed correction record.
* Release-state changes without a governed decision trail.

---

## Correction outcomes

| Outcome           | Meaning                                                                          |
| ----------------- | -------------------------------------------------------------------------------- |
| `REPAIR`          | A bounded correction preserves the release path.                                 |
| `REPLACE`         | A newer governed record replaces the affected record.                            |
| `SUPERSEDE`       | A newer governed record supersedes the affected record and should be linked.     |
| `WITHDRAW`        | The affected release item, public surface, or claim is removed from release use. |
| `REVIEW_HOLD`     | Review continues before final disposition.                                       |
| `ROLLBACK_REVIEW` | The correction needs rollback review before final action.                        |
| `DEFER`           | The issue is recorded but not ready for action.                                  |
| `NO_ACTION`       | Review found no correction is required.                                          |

Use the smallest accurate outcome. Do not choose `REPAIR`, `REPLACE`, `SUPERSEDE`, `WITHDRAW`, or `ROLLBACK_REVIEW` without steward decision support.

---

## Required correction fields

Every correction record should capture:

* Correction record ID
* Affected release or candidate pointer
* Affected manifest entry, artifact, claim, or release target
* Domain scope
* Time, version, interpretation, or policy context, when applicable
* Date recorded
* Recorded by
* Steward decision pointer
* Evidence pointer, when applicable
* Validation or receipt pointer, when applicable
* Policy review pointer, when applicable
* Changelog pointer, when applicable
* Correction notice pointer, when applicable
* Rollback-review pointer, when applicable
* Release-facing effect
* Outcome type
* Reason for correction
* Follow-up items
* Closure status

---

## Naming guidance

Use stable, readable names that sort well and preserve review history.

Recommended pattern:

```text
<YYYY-MM-DD>_<domain>_<short-topic>_correction.md
```

Examples:

```text
2026-07-03_atmosphere_time-coverage_correction.md
2026-07-03_roads-rail-trade_manifest-pointer_correction.md
2026-07-03_settlement-systems_release-context_correction.md
```

Use the domain lane name in the path and avoid creating new naming conventions inside each sublane unless a maintainer-approved convention requires it.

---

## Minimal correction record

```markdown
# <correction-record-id>

## Status

PROPOSED / READY_FOR_REVIEW / APPROVED / APPLIED / REPLACED / SUPERSEDED / WITHDRAWN / REVIEW_HOLD / ROLLBACK_REVIEW / NO_ACTION

## Affected release or candidate

<release manifest, candidate lane, or release record>

## Affected record

<manifest entry, artifact, claim, release target, or N/A>

## Domain scope

<domain scope or feature family>

## Context

<time, version, interpretation, or policy context; N/A when not applicable>

## Date recorded

<YYYY-MM-DD>

## Recorded by

<steward or maintainer>

## Governed record pointers

- Manifest: <path or N/A>
- Artifact: <path or N/A>
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Policy review: <path or N/A>
- Changelog: <path or N/A>
- Notice: <path or N/A>
- Rollback review: <path or N/A>

## Reason

<why correction is needed>

## Release-facing effect

<none / changed / replaced / superseded / withdrawn / repaired / review pending>

## Outcome

<repair / replace / supersede / withdraw / review hold / rollback review / defer / no action>

## Follow-up

<open items or none>

## Decision

<decision, steward, and reason>

## Closure

<open / closed / blocked, with reason>
```

---

## Review checklist

Before marking a correction record `APPROVED`, `APPLIED`, `REPLACED`, `SUPERSEDED`, or `WITHDRAWN`, confirm:

* [ ] The affected release or candidate pointer is present.
* [ ] The affected manifest entry, artifact, claim, or release target is identified.
* [ ] Evidence or validation support is linked when the correction depends on evidence.
* [ ] Policy review is linked when the correction has policy, sensitivity, rights, or access implications.
* [ ] Changelog linkage is present when release history changes.
* [ ] Correction notice linkage is present when a notice is needed.
* [ ] Rollback-review linkage is present when rollback is needed.
* [ ] Steward decision is present.
* [ ] Follow-up tasks are listed or explicitly marked none.
* [ ] No raw, work, processed, catalog, triplet, or published data payloads are stored in this lane.

---

## Publication and notice posture

A correction record may support a release-state change, but it does not itself publish, unpublish, replace, or withdraw an artifact.

When a correction changes what users should see or understand, create or link a notice under `release/correction_notices/`.

When a correction requires reverting or undoing a release action, create or link rollback review under `release/correction/rollback/`.

When a correction only documents an internal review with no release-facing effect, mark the outcome as `NO_ACTION`, `DEFER`, or `REVIEW_HOLD` as appropriate.

---

## Open verification

* [ ] Confirm whether the canonical correction home is `release/correction/`, `release/corrections/`, or both.
* [ ] Confirm CODEOWNERS for `release/corrections/`.
* [ ] Confirm correction record naming convention.
* [ ] Confirm manifest pointer format.
* [ ] Confirm validation receipt pointer format.
* [ ] Confirm changelog linkage.
* [ ] Confirm correction-notice linkage.
* [ ] Confirm rollback-review linkage.
* [ ] Confirm whether correction records need schema validation.
* [ ] Confirm whether additional domain correction lanes are needed.
* [ ] Confirm whether `release/corrections/` should keep KFM_META_BLOCK_V2 after the release path convention is finalized.

---

## Last reviewed

| Field               | Value                                                                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Last reviewed       | 2026-07-03                                                                                                                                              |
| Review status       | Full proposed README content; not yet committed because connector filtering blocked richer versions                                                     |
| Next review trigger | New domain correction lane, first correction record, path convention decision, changelog update, correction notice, rollback review, or schema decision |
