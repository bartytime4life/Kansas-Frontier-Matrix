# `release/` — Release Governance Root

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-readme
title: release/ — Release Governance Root
version: v1
status: draft
policy_label: public
owners:
  - <release-steward>
  - <data-steward>
  - <docs-steward>
  - <domain-stewards>
updated: 2026-07-03
tags: [kfm, release, governance, manifests, decisions, reviews, corrections, changelog, validation, evidence]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![authority](https://img.shields.io/badge/authority-release--governance-blueviolet)
![publication](https://img.shields.io/badge/publication-governed-orange)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/` is the KFM release-governance root.

It holds the records that explain whether a candidate, manifest, review, correction, notice, changelog entry, policy review, signature, or release-facing artifact family is ready, held, corrected, superseded, or not ready.

`release/` is distinct from `data/published/`. The `release/` root records release decisions and release governance; `data/published/` holds approved published artifacts after governed approval.

Release prose is not sovereign truth. Governed release records, evidence records, validation receipts, policy review, manifests, steward decisions, correction records, and changelog entries outrank this README.

## Status & authority

| Field | Value |
|---|---|
| Document type | Release root README |
| Owning root | `release/` |
| Root role | Release governance, review, decision, manifest, correction, notice, signature, and changelog records |
| Status | Draft README replacing compact root stub |
| Authority level | Root guidance and index. Actual release records, manifests, decisions, validation receipts, evidence records, policy records, correction records, notices, signatures, and steward approvals outrank this README. |
| Default posture | Do not infer release approval from prose alone. Require governed records, review, and release-steward decision. |
| Required reviewers | Release steward, data steward, affected domain steward, docs steward, and policy reviewer when required. |

## Placement basis

Current repo evidence confirms this root already described `release/` as the place for release decisions, manifests, promotion records, rollback cards, withdrawals, corrections, signatures, and changelog, distinct from `data/published/` artifacts.

Directory Rules state the deeper placement rule: where a file lives encodes ownership, governance, and lifecycle; topic does not justify a root folder, responsibility does.

This README keeps `release/` as a release-governance root and does not move data, schema, policy, source, contract, validator, or application authority into release space.

## Lifecycle boundary

Release work must preserve the KFM lifecycle boundary:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move.

Release records may point to lifecycle data records and artifacts. They must not duplicate those payloads.

## Repo fit

```text
release/                       # you are here
├── candidates/                # pre-release candidate review packets
├── reviews/                   # release review records
├── promotion_decisions/       # promotion decision records
├── manifest/                  # singular manifest lane; convention still open
├── manifests/                 # plural manifest collection lane
├── decisions/                 # final or release-facing decision records
├── policy/                    # release-facing policy review index; not policy authority
├── people-dna-land/           # sensitive domain dated release-review lane
├── changelog/                 # human-readable release-history index
├── correction/                # singular correction review lane
├── corrections/               # plural correction lane; convention still open
└── correction_notices/        # notice and communication records tied to corrections
```

## Current lane index

| Lane | Role | Current status |
|---|---|---|
| `candidates/` | Pre-release review packets used before governed release decisions. | Parent README exists. |
| `reviews/` | Review records for candidates, manifests, corrections, notices, or release-facing items. | Parent README exists; atmosphere sublane indexed. |
| `promotion_decisions/` | Decision records for moving a candidate toward manifest preparation or holding it. | Parent README exists; hydrology sublane indexed. |
| `manifest/` | Singular release manifest lane. | Draft lane exists; singular/plural convention remains open. |
| `manifests/` | Plural release manifest collection lane. | Parent README exists and indexes current sublanes. |
| `decisions/` | Release decision records. | Parent README exists with finite decision classes. |
| `policy/` | Release-facing policy review notes and policy pointers. | Parent README exists; canonical policy authority remains `policy/`. |
| `people-dna-land/` | Sensitive domain dated release-review lane. | Parent path may need manual update if connector blocks; dated child exists. |
| `changelog/` | Human-readable release history tied to governed records. | Parent README exists. |
| `correction/` | Singular correction review lane. | Parent README exists; convention remains draft. |
| `corrections/` | Plural correction lane. | Exists as draft lane in this release area; canonical singular/plural convention needs maintainer confirmation. |
| `correction_notices/` | Notice records that point to governed correction records. | Parent README exists. |

## Root responsibilities

| Responsibility | Expectation |
|---|---|
| Release identity | Preserve stable release, review, manifest, decision, correction, and notice identifiers. |
| Evidence linkage | Require evidence pointers when release claims depend on evidence. |
| Validation linkage | Require validation receipt pointers when validation is required. |
| Policy posture | Require policy review pointers when release posture depends on rights, sensitivity, access, or public-surface rules. |
| Steward decision | Require steward review and decision records for release-state changes. |
| Manifest readiness | Use manifests to name release targets, included records, support records, decision state, and release-facing effect. |
| Candidate discipline | Treat candidates as pre-release review packets, never as public release by themselves. |
| Review discipline | Treat reviews as support records, not approval by themselves. |
| Correction discipline | Treat correction as governed state transition, not a file edit or file move alone. |
| Changelog discipline | Treat changelog entries as human-readable companions, not sovereign release truth. |
| Reversibility | Preserve correction, withdrawal, supersession, and reversal planning where relevant. |

## What belongs here

- Release-root README and lane indexes.
- Candidate review records and candidate lane READMEs.
- Release review records and review lane READMEs.
- Promotion decision records.
- Release manifests and manifest indexes.
- Release decision records.
- Release-facing policy review records and policy pointers.
- Correction review records.
- Correction notice records.
- Changelog entries tied to governed release events.
- Signature, receipt, withdrawal, supersession, and reversal-planning records when those lanes are present and confirmed.
- Pointers to evidence records, validation receipts, policy reviews, source records, manifests, decisions, corrections, notices, and published artifact targets.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exports, service payloads, or map-ready artifacts.
- Source descriptors.
- Schemas.
- Contracts.
- Canonical policy-as-code files.
- Validator code.
- Application runtime code.
- Generated summaries used as sovereign truth.
- Final publication approval without governed release records and steward decision.
- Silent promotion by moving files between lifecycle paths.

## Release state model

Use finite release states where possible:

| State | Meaning |
|---|---|
| `DRAFT` | Record exists but is not ready for review. |
| `READY_FOR_REVIEW` | Record is ready for steward review. |
| `HELD` | Record is blocked or waiting on evidence, validation, policy, rights, sensitivity, or stewardship. |
| `READY_FOR_MANIFEST` | Candidate or review is ready to support manifest preparation. |
| `APPROVED` | Steward-approved record, not necessarily published payload. |
| `RELEASED` | Governed release state is complete for the referenced release target. |
| `CORRECTED` | Release state has been corrected by governed correction record. |
| `SUPERSEDED` | Newer governed record replaces the earlier release state. |
| `WITHDRAWN` | Release state is withdrawn through governed process. |
| `NO_ACTION` | Review found no release-state change is authorized. |

## Required release-root record fields

Release records should capture the fields appropriate to their lane. At minimum, release-root records should include:

- Stable record ID
- Record type
- Record status
- Domain or layer scope
- Affected candidate, manifest, release, artifact, claim, correction, notice, or changelog pointer
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Policy review pointer, when applicable
- Decision pointer, when applicable
- Manifest pointer, when applicable
- Correction pointer, when applicable
- Notice pointer, when applicable
- Changelog pointer, when applicable
- Signature or receipt pointer, when applicable
- Release-facing effect
- Steward review state
- Date recorded
- Recorded by
- Follow-up items

## Minimal release-root record

```markdown
# <release-record-id>

## Record type
CANDIDATE / REVIEW / PROMOTION_DECISION / MANIFEST / DECISION / POLICY_REVIEW / CORRECTION / NOTICE / CHANGELOG / SIGNATURE / WITHDRAWAL / SUPERSESSION / NO_ACTION

## Status
DRAFT / READY_FOR_REVIEW / HELD / READY_FOR_MANIFEST / APPROVED / RELEASED / CORRECTED / SUPERSEDED / WITHDRAWN / NO_ACTION

## Scope
<domain, layer family, artifact family, time slice, release target, or N/A>

## Affected record
<candidate, manifest, decision, release, correction, notice, changelog, or artifact pointer>

## Governed support pointers
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Policy review: <path or N/A>
- Manifest: <path or N/A>
- Decision: <path or N/A>
- Correction: <path or N/A>
- Notice: <path or N/A>
- Changelog: <path or N/A>
- Signature or receipt: <path or N/A>

## Release-facing effect
<none / ready / released / held / corrected / superseded / withdrawn / review pending>

## Steward review state
<reviewers, decision, and date>

## Date recorded
<YYYY-MM-DD>

## Recorded by
<steward or maintainer>

## Follow-up
<open items or none>
```

## Review checklist

Before release-state changes are treated as approved or released, confirm:

- [ ] The lane is appropriate for the record type.
- [ ] The record has a stable ID.
- [ ] The affected candidate, manifest, release, correction, notice, or changelog pointer is present.
- [ ] Evidence support is linked when claims depend on evidence.
- [ ] Validation support is linked when validation is required.
- [ ] Policy review is linked when release posture requires it.
- [ ] Steward decision is linked when release state changes.
- [ ] Manifest is linked when the release target is named or prepared.
- [ ] Correction, notice, changelog, signature, or reversal pointers are linked when applicable.
- [ ] Public or semi-public posture is explicit.
- [ ] No data payloads are stored in `release/` lanes.
- [ ] No canonical policy, schema, contract, source, validator, or app authority is duplicated under `release/`.

## Naming guidance

Prefer stable, readable, dated filenames:

```text
<YYYY-MM-DD>_<scope>_<record-type>.md
```

Examples:

```text
2026-07-03_hydrology-watershed-summary_promotion-decision.md
2026-07-03_atmosphere-weather-summary_release-review.md
2026-07-03_fauna-range-summary_manifest.md
2026-07-03_people-dna-land_policy-review.md
2026-07-03_release-correction_notice.md
```

Use lowercase filenames, hyphenated scope names, and stable IDs. Avoid renaming approved release records unless a migration note explains the change.

## Open verification

- [ ] Confirm CODEOWNERS for `release/`.
- [ ] Confirm final singular/plural convention for `release/manifest/` and `release/manifests/`.
- [ ] Confirm final singular/plural convention for `release/correction/` and `release/corrections/`.
- [ ] Confirm whether `release/reviews/`, `release/decisions/`, and `release/promotion_decisions/` remain distinct lanes or need consolidation.
- [ ] Confirm release record ID format.
- [ ] Confirm release filename convention.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm policy review pointer format.
- [ ] Confirm manifest, decision, correction, notice, changelog, signature, and receipt pointer formats.
- [ ] Confirm which release records require schema validation before approval.
- [ ] Confirm whether `release/people-dna-land/README.md` can be committed after connector safety blocks or should remain manually patched.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing compact root stub |
| Next review trigger | New release lane, lane consolidation decision, manifest convention decision, correction convention decision, first release-state approval, policy review update, correction, notice, signature, changelog, or schema update |
