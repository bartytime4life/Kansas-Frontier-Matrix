# `release/manifests/layers/` — Layer Release Manifests

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-manifests-blueviolet)
![scope](https://img.shields.io/badge/scope-layers-blue)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/manifests/layers/` holds release manifest records for governed KFM layer releases when maintainers choose the plural manifest collection lane.

A layer manifest names the layer release target, included records, validation support, evidence support, decision state, presentation posture, and release-facing effect.

A manifest record should answer:

- What layer release or candidate is being described?
- Which layer, style, dataset, catalog, triplet, or release-target pointers are included?
- Which evidence and validation records support the layer release?
- Which decision approved, held, corrected, or deferred the release?
- What presentation posture applies?
- What changelog, correction, or notice records are linked?
- What should governed release consumers treat as ready, held, superseded, or not ready?

A manifest is not the payload itself. It is the governed release record that points to approved release inputs and outputs.

## Status & authority

| Field | Value |
|---|---|
| Document type | Layer release manifest README |
| Owning root | `release/` |
| Manifest lane | `release/manifests/layers/` |
| Status | Draft |
| Authority level | Manifest guidance. Actual manifest records, validation receipts, evidence records, decisions, changelog entries, correction records, presentation-review records, and schemas outrank this README. |
| Default posture | Do not change release state from prose alone. Require governed manifest records and steward review. |
| Required reviewers | Release steward, layer steward, data steward, docs steward, and presentation reviewer when needed. |

## Path status

This README documents the requested path: `release/manifests/layers/`.

Current-session evidence confirms this README existed as a blank file before this update. Current-session evidence also confirms `release/manifests/README.md` exists as a greenfield stub, while `release/manifest/README.md` is already documented as the singular manifest lane. Treat this layers manifest sublane as draft until maintainers confirm whether the canonical manifest home is singular `release/manifest/`, plural `release/manifests/`, or both with distinct meanings.

## Repo fit

```text
release/
├── manifest/
├── manifests/
│   └── layers/       # you are here
├── candidates/
├── decisions/
├── changelog/
├── correction/
└── correction_notices/
```

This path belongs under the `release/` responsibility root because layer manifests are release governance records. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## Layer manifest responsibilities

| Responsibility | Manifest expectation |
|---|---|
| Identity | Provide a stable layer release or manifest ID. |
| Scope | State the layer family, map layer, style family, dataset family, or release target. |
| Inclusion | List included layer release records or artifacts by pointer. |
| Evidence | Link evidence records when layer claims depend on evidence. |
| Validation | Link validation receipts or checks. |
| Presentation posture | State whether layer outputs are ready, generalized, redacted, held, or not ready. |
| Decision | Link the steward decision that supports the release state. |
| Changelog | Link the release-history entry. |
| Correction path | Link correction records when the manifest is corrected, superseded, or held. |
| Client posture | State what governed surfaces may use this release. |

## What belongs here

- Layer release manifest records.
- Layer manifest readiness checklists.
- Layer manifest review summaries.
- Links to layer candidates, decisions, validation receipts, evidence records, presentation reviews, changelog entries, corrections, and notices.
- Notes explaining layer manifest state, included release targets, release scope, presentation posture, and follow-up tasks.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, exports, service payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy files, or validator code.
- Generated summaries used as sovereign truth.
- Unreviewed layer claims presented as approved release state.

## Required manifest fields

- Manifest ID
- Manifest status
- Layer release or candidate pointer
- Layer scope
- Artifact or release target pointers
- Included claim or record pointers, when applicable
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Presentation review pointer, when applicable
- Decision pointer
- Changelog pointer
- Correction pointer, when applicable
- Notice pointer, when applicable
- Release-facing effect
- Client-consumption posture
- Date recorded
- Recorded by
- Steward review state
- Follow-up items

## Minimal layer manifest record

```markdown
# <manifest-id>

## Status
DRAFT / READY_FOR_REVIEW / APPROVED / RELEASED / HELD / SUPERSEDED / CORRECTED / NO_ACTION

## Layer release or candidate
<release ID, candidate path, or N/A>

## Layer scope
<layer family, map layer, style family, dataset family, artifact family, or release target>

## Included records
- <artifact, claim, catalog, triplet, layer, style, or release-target pointer>

## Presentation posture
READY / GENERALIZED / REDACTED / HELD / NOT_READY

## Governed support pointers
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Presentation review: <path or N/A>
- Decision: <path or N/A>
- Changelog: <path or N/A>
- Correction: <path or N/A>
- Notice: <path or N/A>

## Release-facing effect
<none / ready / released / held / superseded / corrected / review pending>

## Client posture
<which governed release surfaces may use this layer release, or N/A>

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
- [ ] Layer release or candidate pointer is present.
- [ ] Included records are listed by pointer.
- [ ] Evidence support is linked when release claims depend on evidence.
- [ ] Validation support is linked when validation is required.
- [ ] Presentation review is linked when needed.
- [ ] Steward decision is linked.
- [ ] Changelog entry is linked when release history changes.
- [ ] Correction or notice pointers are linked when applicable.
- [ ] Client-consumption posture is explicit.
- [ ] No data payloads are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<layer-scope>_manifest.md
```

Examples:

```text
2026-07-03_county-boundary-layer_manifest.md
2026-07-03_hydrology-layer-release_manifest.md
2026-07-03_public-map-style-layer_manifest.md
```

## Open verification

- [ ] Expand `release/manifests/README.md` so this layers lane inherits from a complete plural manifest parent contract.
- [ ] Confirm whether the canonical manifest home is `release/manifest/`, `release/manifests/`, or both.
- [ ] Confirm CODEOWNERS for `release/manifests/layers/`.
- [ ] Confirm layer manifest ID format.
- [ ] Confirm layer manifest filename convention.
- [ ] Confirm manifest schema location.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm presentation review pointer format.
- [ ] Confirm decision, changelog, correction, and notice pointer formats.
- [ ] Confirm whether layer manifest records require schema validation before release approval.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | First layer manifest record, plural manifest-lane expansion, manifest schema update, candidate promotion, release decision, presentation review, or changelog integration |
