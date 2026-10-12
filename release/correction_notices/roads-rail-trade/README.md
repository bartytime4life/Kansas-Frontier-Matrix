# `release/correction_notices/roads-rail-trade/` — Roads Rail Trade Correction Notice Lane

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-correction--notices-blueviolet)
![domain](https://img.shields.io/badge/domain-roads--rail--trade-brown)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/correction_notices/roads-rail-trade/` holds notice drafts for roads, rail, and trade release corrections.

A notice is not the correction itself. It is a communication record that should point to governed release, correction, validation, and changelog records.

Notice prose is not sovereign truth. Evidence, validation, release manifests, correction records, and steward decisions outrank notice text.

This lane should help reviewers explain what changed, why a notice is needed, which governed correction record supports it, and what follow-up remains open.

## Status & authority

| Field | Value |
|---|---|
| Document type | Roads rail trade correction notice README |
| Owning root | `release/` |
| Notice lane | `release/correction_notices/roads-rail-trade/` |
| Status | Draft |
| Authority level | Notice guidance. Governed release records outrank this README. |
| Default posture | Do not change release state from a notice draft alone. |
| Required reviewers | Domain steward, release steward, correction steward, and data steward. |

## Path status

This README documents the path exactly requested: `release/correction_notices/roads-rail-trade/`.

Current-session evidence confirms this README existed as a blank file before this update. Current-session evidence also confirms `release/correction_notices/README.md` currently exists only as a greenfield stub. Treat this notice lane as self-contained until the parent notice lane is expanded.

## Repo fit

```text
release/
├── correction/
├── correction_notices/
│   └── roads-rail-trade/       # you are here
├── changelog/
├── candidates/
└── manifests/
```

This path belongs under the `release/` responsibility root. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## What belongs here

- Roads rail trade notice drafts.
- Notice readiness checklists.
- Steward review summaries for notice wording.
- Links to manifests, correction records, validation receipts, changelog entries, and affected release targets.
- Notes explaining whether the notice describes repair, supersession, withdrawal, review hold, or no release-facing change.
- Time-context and version-context notes for release-facing transport and trade materials.
- Follow-up tasks for changelog, manifest, correction, validation, or release-history updates.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exported files, API payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy rules, or validator code.
- Correction approval without steward review.
- Notice text used as evidence.
- Generated summaries used as sovereign truth.

## Notice types

| Notice type | Meaning |
|---|---|
| `INFORMATIONAL` | Clarifies release-facing material. |
| `CORRECTION` | Explains a bounded correction. |
| `VERSION_UPDATE` | Explains a changed version, date range, or interpretation note. |
| `SUPERSESSION` | Explains that a newer governed record replaces an earlier one. |
| `NO_NOTICE` | Records that no notice is needed after review. |

## Required notice fields

- Notice ID
- Notice type
- Affected release or candidate pointer
- Affected manifest, artifact, claim, or release target
- Domain scope
- Time or version context
- Correction record pointer
- Date drafted
- Drafted by
- Steward decision pointer
- Evidence pointer, when applicable
- Validation or receipt pointer, when applicable
- Changelog pointer, when applicable
- Release-facing effect
- Notice audience
- Summary
- Follow-up items

## Minimal correction notice

```markdown
# <notice-id>

## Status
DRAFT / READY_FOR_REVIEW / APPROVED / PUBLISHED / SUPERSEDED / NO_NOTICE

## Notice type
INFORMATIONAL / CORRECTION / VERSION_UPDATE / SUPERSESSION / NO_NOTICE

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

## Notice text
<approved or draft notice text>

## Follow-up
<open items or none>

## Decision
<decision, steward, and reason>
```

## Open verification

- [ ] Expand `release/correction_notices/README.md` so this lane inherits from a complete parent notice contract.
- [ ] Confirm CODEOWNERS for this path.
- [ ] Confirm correction notice naming convention.
- [ ] Confirm release correction pointer format.
- [ ] Confirm changelog event linkage.
- [ ] Confirm time or version notice vocabulary.
- [ ] Confirm whether notice records need schema validation.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | First notice, parent notice-lane expansion, correction record, changelog update, version-context decision, or notice schema decision |
