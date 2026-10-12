# `release/manifests/settlements-infrastructure/` — Settlement Systems Release Manifests

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-manifests-blueviolet)
![domain](https://img.shields.io/badge/domain-settlement--systems-brown)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/manifests/settlements-infrastructure/` holds release manifest records for the settlement systems domain when maintainers choose the plural manifest collection lane.

A manifest record names the release target, included records, validation support, evidence support, decision state, time and place context, and release-facing effect.

A manifest is not the payload itself. It is the governed release record that points to approved release inputs and outputs.

## Status & authority

| Field | Value |
|---|---|
| Document type | Settlement systems release manifest README |
| Owning root | `release/` |
| Manifest lane | `release/manifests/settlements-infrastructure/` |
| Status | Draft |
| Authority level | Manifest guidance. Actual manifest records, validation receipts, evidence records, decisions, changelog entries, correction records, and schemas outrank this README. |
| Default posture | Do not change release state from prose alone. Require governed manifest records and steward review. |
| Required reviewers | Release steward, settlement systems steward, data steward, and docs steward. |

## Path status

This README documents the requested path: `release/manifests/settlements-infrastructure/`.

This sublane is draft. The repo also contains a singular manifest lane and a plural manifest parent stub. Maintainers still need to confirm the canonical manifest convention.

## Repo fit

```text
release/
├── manifest/
├── manifests/
│   └── settlements-infrastructure/       # you are here
├── candidates/
│   └── settlements-infrastructure/
├── decisions/
├── changelog/
├── correction/
└── correction_notices/
```

Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## Manifest responsibilities

| Responsibility | Manifest expectation |
|---|---|
| Identity | Provide a stable release or manifest ID. |
| Scope | State the settlement systems family, place-summary family, time slice, layer family, artifact family, or release target. |
| Inclusion | List included release records or artifacts by pointer. |
| Evidence | Link evidence records when claims depend on evidence. |
| Validation | Link validation receipts or checks. |
| Time and place context | State geography, time period, temporal confidence, or version context when relevant. |
| Decision | Link the steward decision that supports the release state. |
| Changelog | Link the release-history entry. |
| Correction path | Link correction records when the manifest is corrected, superseded, or held. |
| Client posture | State what governed surfaces may use this release. |

## What belongs here

- Settlement systems release manifest records.
- Manifest readiness checklists.
- Manifest review summaries.
- Links to candidates, decisions, validation receipts, evidence records, changelog entries, corrections, and notices.
- Notes explaining manifest state, included release targets, release scope, time and place context, and follow-up tasks.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, exports, rendered outputs, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy files, or validator code.
- Generated summaries used as sovereign truth.
- Unreviewed claims presented as approved release state.

## Required manifest fields

- Manifest ID
- Manifest status
- Release or candidate pointer
- Domain scope
- Geography and time period, when applicable
- Artifact or release target pointers
- Included claim or record pointers, when applicable
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Decision pointer
- Changelog pointer
- Correction pointer, when applicable
- Notice pointer, when applicable
- Release-facing effect
- Client posture
- Date recorded
- Recorded by
- Steward review state
- Follow-up items

## Minimal manifest record

```markdown
# <manifest-id>

## Status
DRAFT / READY_FOR_REVIEW / APPROVED / RELEASED / HELD / SUPERSEDED / CORRECTED / NO_ACTION

## Release or candidate
<release ID, candidate path, or N/A>

## Domain scope
<settlement systems family, place-summary family, time slice, layer family, artifact family, or release target>

## Geography and time period
<geography, time period, temporal confidence, or N/A>

## Included records
- <artifact, claim, catalog, triplet, or release-target pointer>

## Governed support pointers
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Decision: <path or N/A>
- Changelog: <path or N/A>
- Correction: <path or N/A>
- Notice: <path or N/A>

## Release-facing effect
<none / ready / released / held / superseded / corrected / review pending>

## Client posture
<which governed release surfaces may use this release, or N/A>

## Date recorded
<YYYY-MM-DD>

## Recorded by
<steward or maintainer>

## Review state
<reviewers, decision, and date>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Manifest ID is stable.
- [ ] Release or candidate pointer is present.
- [ ] Included records are listed by pointer.
- [ ] Evidence support is linked when release claims depend on evidence.
- [ ] Validation support is linked when validation is required.
- [ ] Geography and time period are stated when relevant.
- [ ] Steward decision is linked.
- [ ] Changelog entry is linked when release history changes.
- [ ] Correction or notice pointers are linked when applicable.
- [ ] Client posture is explicit.
- [ ] No data payloads are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<settlement-systems-scope>_manifest.md
```

Examples:

```text
2026-07-03_settlement-systems-place-summary_manifest.md
2026-07-03_settlement-systems-layer-release_manifest.md
2026-07-03_settlement-systems-time-slice_manifest.md
```

## Open verification

- [ ] Expand `release/manifests/README.md` so this lane inherits from a complete plural manifest parent contract.
- [ ] Confirm whether the canonical manifest home is singular, plural, or both.
- [ ] Confirm CODEOWNERS for this path.
- [ ] Confirm manifest ID format.
- [ ] Confirm manifest filename convention.
- [ ] Confirm manifest schema location.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm decision, changelog, correction, and notice pointer formats.
- [ ] Confirm whether manifest records require schema validation before release approval.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | First manifest record, plural manifest-lane expansion, manifest schema update, candidate promotion, release decision, or changelog integration |
