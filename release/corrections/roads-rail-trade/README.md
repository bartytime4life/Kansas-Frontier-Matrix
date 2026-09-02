# `release/corrections/roads-rail-trade/` — Roads Rail Trade Correction Record Lane

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-corrections-blueviolet)
![domain](https://img.shields.io/badge/domain-roads--rail--trade-brown)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/corrections/roads-rail-trade/` holds correction records for roads, rail, and trade release material.

A correction record is a governed review artifact. It should point to the affected release, candidate, manifest entry, artifact, claim, validation result, changelog entry, and steward decision.

This lane should help reviewers explain what changed, why correction is needed, which governed record supports it, and what follow-up remains open.

Correction is a governed state transition, not a file move.

## Status & authority

| Field | Value |
|---|---|
| Document type | Roads rail trade correction README |
| Owning root | `release/` |
| Correction lane | `release/corrections/roads-rail-trade/` |
| Status | Draft |
| Authority level | Correction guidance. Governed release records outrank this README. |
| Default posture | Do not alter release state from prose alone. Require steward decision and governed record pointers. |
| Required reviewers | Domain steward, release steward, correction steward, and data steward. |

## Path status

This README documents the path exactly requested: `release/corrections/roads-rail-trade/`.

Current-session evidence confirms this README existed as a blank file before this update. Current-session evidence also confirms `release/corrections/README.md` currently exists as a blank file, while `release/correction/README.md` is already documented as a singular correction review lane. Treat this correction lane as draft until the repo confirms whether the canonical correction home is singular `release/correction/`, plural `release/corrections/`, or both with distinct meanings.

## Repo fit

```text
release/
├── correction/
├── corrections/
│   └── roads-rail-trade/       # you are here
├── correction_notices/
├── changelog/
├── candidates/
└── manifests/
```

This path belongs under the `release/` responsibility root because it records release corrections. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## What belongs here

- Roads rail trade correction records.
- Correction readiness checklists.
- Steward review summaries.
- Links to release manifests, validation receipts, changelog entries, affected release targets, and evidence records.
- Notes explaining whether the outcome is repair, replacement, review hold, defer, or no action.
- Time-context and version-context notes for release-facing materials.
- Follow-up tasks for changelog, manifest, validation, correction notice, or release-history updates.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exported files, API payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Correction approval without steward review.
- Generated summaries used as sovereign truth.
- Notice text unless it points to a governed correction record.

## Correction outcomes

| Outcome | Meaning |
|---|---|
| `REPAIR` | A bounded correction preserves the release path. |
| `REPLACE` | A newer governed record replaces the affected record. |
| `REVIEW_HOLD` | Review must continue before final disposition. |
| `DEFER` | The issue is recorded but not ready for action. |
| `NO_ACTION` | Review found no release correction is required. |

## Required correction fields

Every roads rail trade correction record should capture:

- Correction record ID
- Affected release or candidate pointer
- Affected manifest, artifact, claim, or release target
- Domain scope
- Time or version context
- Date recorded
- Recorded by
- Steward decision pointer
- Evidence pointer, when applicable
- Validation or receipt pointer, when applicable
- Changelog pointer, when applicable
- Correction notice pointer, when applicable
- Release-facing effect
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
<manifest entry, artifact, claim, release target, or N/A>

## Domain scope
<domain scope or feature family>

## Time or version context
<date range, version note, interpretation note, or N/A>

## Governed record pointers
- Manifest: <path or N/A>
- Artifact: <path or N/A>
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Changelog: <path or N/A>
- Correction notice: <path or N/A>

## Reason
<why correction is needed>

## Release-facing effect
<none / changed / replaced / repaired / review pending>

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
- [ ] Confirm ReleaseManifest pointer format.
- [ ] Confirm changelog and correction-notice linkage.
- [ ] Confirm time or version vocabulary for correction records.
- [ ] Confirm whether correction records need schema validation.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | First correction record, parent corrections-lane expansion, path convention decision, changelog update, correction notice, version-context decision, or schema decision |
