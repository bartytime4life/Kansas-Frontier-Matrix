# `release/manifests/` — Release Manifest Collection Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-manifests-readme
title: release/manifests/ — Release Manifest Collection Lane
version: v1
status: draft
policy_label: public
owners:
  - <release-steward>
  - <data-steward>
  - <docs-steward>
  - <domain-stewards>
updated: 2026-07-03
tags: [kfm, release, manifests, publication, validation, evidence, audit]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-manifests-blueviolet)
![publication](https://img.shields.io/badge/publication-governed-orange)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/manifests/` is the plural collection lane for KFM release manifest records.

A release manifest names a release target, lists the governed records included in that release, points to validation and evidence support, records the decision state, and states the release-facing effect.

A manifest should answer:

- What release or candidate is being described?
- Which artifacts, claims, catalog entries, triplet records, layers, or release targets are included?
- Which evidence and validation records support the release?
- Which decision approved, held, corrected, or deferred the release?
- Which changelog, correction, notice, or signature records are linked, when applicable?
- What should governed clients treat as ready, held, superseded, corrected, or not ready?

A manifest is not a payload. It is a governed release record that points to approved release inputs and outputs.

## Status & authority

| Field | Value |
|---|---|
| Document type | Release manifest collection README |
| Owning root | `release/` |
| Manifest lane | `release/manifests/` |
| Status | Draft |
| Authority level | Parent guidance and index. Actual manifest records, validation receipts, evidence records, decisions, changelog entries, correction records, notices, signatures, schemas, and steward decisions outrank this README. |
| Default posture | Do not change release state from prose alone. Require governed records and steward review. |
| Required reviewers | Release steward, data steward, affected domain steward, docs steward, and policy reviewer when needed. |

## Path status

This README documents the plural path: `release/manifests/`.

The repo also has `release/manifest/`, which is documented as the singular manifest lane. Treat both paths as draft until maintainers confirm whether the canonical manifest home is singular, plural, or both with distinct meanings.

Recommended distinction, pending maintainer confirmation:

| Path | Proposed role |
|---|---|
| `release/manifest/` | Singular lane for current or canonical manifest workflow notes. |
| `release/manifests/` | Plural lane for manifest collections and domain-scoped manifest files. |

Do not move files only to satisfy naming preference. Record uncertainty and keep changes reversible.

## Repo fit

```text
release/
├── manifest/
├── manifests/       # you are here
│   ├── agriculture/
│   ├── fauna/
│   ├── flora/
│   ├── layers/
│   ├── people/
│   ├── roads-rail-trade/
│   └── settlements-infrastructure/
├── candidates/
├── decisions/
├── changelog/
├── correction/
├── corrections/
└── correction_notices/
```

This path belongs under the `release/` responsibility root because manifests are release governance records. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## Current sublanes

| Sublane | Scope | Notes |
|---|---|---|
| `agriculture/` | Agriculture release manifests. | Draft sublane README exists. |
| `fauna/` | Fauna release manifests. | Draft sublane README exists; sensitive exposure requires review posture. |
| `flora/` | Flora release manifests. | Draft sublane README exists; sensitive exposure requires review posture. |
| `layers/` | Layer release manifests. | Draft sublane README exists for layer release records. |
| `people/` | People-domain release manifests. | Draft path exists; review posture and rights posture need maintainer confirmation. |
| `roads-rail-trade/` | Roads, rail, and trade release manifests. | Draft path exists; sublane content may need separate maintainer update if connector edits are blocked. |
| `settlements-infrastructure/` | Settlement systems release manifests. | Draft sublane README exists. |

## Manifest responsibilities

| Responsibility | Manifest expectation |
|---|---|
| Identity | Provide a stable manifest ID. |
| Scope | State the domain, layer family, candidate, artifact family, time slice, or release target. |
| Inclusion | List included release records or artifacts by pointer. |
| Evidence | Link evidence records when release claims depend on evidence. |
| Validation | Link validation receipts or checks. |
| Decision | Link the steward decision that supports the release state. |
| Changelog | Link the release-history entry when release history changes. |
| Correction path | Link correction records when a manifest is corrected, superseded, or held. |
| Notice path | Link notice records when a release-facing notice is needed. |
| Client posture | State what governed surfaces may use the release. |

## What belongs here

- Parent README and sublane indexes.
- Release manifest records when maintainers choose this plural lane as the manifest home.
- Domain-scoped manifest records.
- Layer-scoped manifest records.
- Manifest readiness checklists.
- Manifest review summaries.
- Links to candidates, decisions, validation receipts, evidence records, changelog entries, corrections, notices, and signatures.
- Notes explaining manifest state, included release targets, release scope, review posture, and follow-up tasks.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exports, service payloads, or map-ready artifacts.
- Source descriptors.
- Schemas.
- Contracts.
- Policy rule files.
- Validator code.
- Generated summaries used as sovereign truth.
- Unreviewed release claims presented as approved release state.
- Public-client shortcuts around governed release interfaces.

## Required manifest fields

Every manifest record should capture:

- Manifest ID
- Manifest status
- Release or candidate pointer
- Domain or layer scope
- Artifact or release target pointers
- Included claim or record pointers, when applicable
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Policy or review pointer, when applicable
- Decision pointer
- Changelog pointer, when applicable
- Correction pointer, when applicable
- Notice pointer, when applicable
- Signature pointer, when applicable
- Release-facing effect
- Client-consumption posture
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

## Scope
<domain, layer family, time slice, artifact family, or release target>

## Included records
- <artifact, claim, catalog, triplet, layer, or release-target pointer>

## Governed support pointers
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Review: <path or N/A>
- Decision: <path or N/A>
- Changelog: <path or N/A>
- Correction: <path or N/A>
- Notice: <path or N/A>
- Signature: <path or N/A>

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

Before marking a manifest `APPROVED` or `RELEASED`, confirm:

- [ ] Manifest ID is stable.
- [ ] Release or candidate pointer is present.
- [ ] Included records are listed by pointer.
- [ ] Evidence support is linked when release claims depend on evidence.
- [ ] Validation support is linked when validation is required.
- [ ] Policy or review support is linked when release posture requires it.
- [ ] Steward decision is linked.
- [ ] Changelog entry is linked when release history changes.
- [ ] Correction or notice pointers are linked when applicable.
- [ ] Signature is linked when signing applies.
- [ ] Client-consumption posture is explicit.
- [ ] No data payloads are stored in this lane.

## Naming guidance

Use stable, readable names that sort well and preserve release history.

Recommended pattern:

```text
<YYYY-MM-DD>_<domain-or-layer-scope>_manifest.md
```

Examples:

```text
2026-07-03_agriculture-county-year-panel_manifest.md
2026-07-03_fauna-range-summary_manifest.md
2026-07-03_flora-restoration-release_manifest.md
2026-07-03_public-map-style-layer_manifest.md
2026-07-03_settlement-systems-place-summary_manifest.md
```

Use lowercase filenames, hyphenated short topics, and stable release scope names. Avoid renaming approved manifest records unless a migration note explains the change.

## Open verification

- [ ] Confirm whether the canonical manifest home is `release/manifest/`, `release/manifests/`, or both.
- [ ] Confirm CODEOWNERS for `release/manifests/`.
- [ ] Confirm manifest ID format.
- [ ] Confirm manifest filename convention.
- [ ] Confirm manifest schema location.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm decision, changelog, correction, notice, and signature pointer formats.
- [ ] Confirm whether manifest records require schema validation before release approval.
- [ ] Confirm whether all listed sublanes should remain under `release/manifests/` after the path convention decision.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | Manifest path convention decision, first manifest record, schema update, candidate promotion, release decision, correction, notice, signature workflow, or changelog integration |
