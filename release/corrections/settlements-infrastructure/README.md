# `release/corrections/settlements-infrastructure/` — Settlement Systems Corrections

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-corrections-blueviolet)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/corrections/settlements-infrastructure/` holds correction records for settlement systems release material.

A correction record is a governed review artifact. It should point to the affected release, candidate, manifest entry, validation result, changelog entry, and steward decision.

Correction is a governed state transition, not a file move.

## Status & authority

| Field | Value |
|---|---|
| Document type | Settlement systems correction README |
| Owning root | `release/` |
| Correction lane | `release/corrections/settlements-infrastructure/` |
| Status | Draft |
| Authority level | Correction guidance. Governed release records outrank this README. |
| Default posture | Do not change release state from prose alone. |
| Required reviewers | Domain steward, release steward, correction steward, and data steward. |

## Path status

This README documents the requested path: `release/corrections/settlements-infrastructure/`.

Current-session evidence confirms this README existed as a blank file before this update. Current-session evidence also confirms `release/corrections/README.md` currently exists as a blank file, while `release/correction/README.md` is already documented as a singular correction review lane. Treat this lane as draft until the repo confirms whether the canonical correction home is singular `release/correction/`, plural `release/corrections/`, or both with distinct meanings.

## Repo fit

```text
release/
├── correction/
├── corrections/
│   └── settlements-infrastructure/       # you are here
├── correction_notices/
├── changelog/
├── candidates/
└── manifests/
```

Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## What belongs here

- Settlement systems correction records.
- Correction readiness notes.
- Steward review summaries.
- Links to manifests, validation receipts, changelog entries, and related release records.
- Notes explaining whether the outcome is repair, replacement, review hold, defer, or no action.
- Follow-up tasks for changelog, manifest, validation, notice, or release-history updates.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exports, API payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Approval without steward review.
- Generated summaries used as sovereign truth.

## Correction outcomes

| Outcome | Meaning |
|---|---|
| `REPAIR` | A bounded correction preserves the release path. |
| `REPLACE` | A newer governed record replaces the affected record. |
| `REVIEW_HOLD` | Review continues before final disposition. |
| `DEFER` | The issue is recorded but not ready for action. |
| `NO_ACTION` | Review found no correction is required. |

## Required correction fields

- Correction record ID
- Affected release or candidate pointer
- Affected manifest entry or release record
- Domain scope
- Time or version context
- Date recorded
- Recorded by
- Steward decision pointer
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Changelog pointer, when applicable
- Notice pointer, when applicable
- Outcome type
- Reason for correction
- Follow-up items

## Minimal correction record

```markdown
# <correction-record-id>

## Status
PROPOSED / READY_FOR_REVIEW / APPROVED / APPLIED / REPLACED / REVIEW_HOLD / NO_ACTION

## Affected release or candidate
<release manifest, candidate lane, or release record>

## Affected record
<manifest entry, release record, or N/A>

## Domain scope
<domain scope or feature family>

## Time or version context
<date range, version note, interpretation note, or N/A>

## Governed record pointers
- Manifest: <path or N/A>
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Changelog: <path or N/A>
- Notice: <path or N/A>

## Reason
<why correction is needed>

## Outcome
<repair / replace / review hold / defer / no action>

## Follow-up
<open items or none>

## Decision
<decision, steward, and reason>
```

## Open verification

- [ ] Expand `release/corrections/README.md` so this lane inherits from a complete parent correction contract.
- [ ] Confirm whether the canonical correction home is `release/correction/`, `release/corrections/`, or both.
- [ ] Confirm CODEOWNERS for this path.
- [ ] Confirm correction record naming convention.
- [ ] Confirm manifest pointer format.
- [ ] Confirm changelog and notice linkage.
- [ ] Confirm whether correction records need schema validation.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | First correction record, parent corrections-lane expansion, path convention decision, changelog update, notice, or schema decision |
