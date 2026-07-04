# `release/policy/` — Release Policy Review Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-policy-readme
title: release/policy/ — Release Policy Review Lane
version: v1
status: draft
policy_label: public
owners:
  - <release-steward>
  - <policy-steward>
  - <data-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, release, policy, review, governance, publication, sensitivity]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-policy-blueviolet)
![authority](https://img.shields.io/badge/authority-review_index-lightgrey)
![review](https://img.shields.io/badge/review-required-red)
![policy](https://img.shields.io/badge/policy-pointer--only-orange)

## Purpose

`release/policy/` holds release-facing policy review notes and policy decision pointers.

This lane exists to show how policy review affects release readiness, candidate promotion, manifest approval, correction, notice, rollback, public-surface posture, and changelog interpretation.

This lane is not the canonical home for policy rules. Canonical policy-as-code and policy documentation belong under `policy/`.

## Status & authority

| Field | Value |
|---|---|
| Document type | Release policy review README |
| Owning root | `release/` |
| Lane | `release/policy/` |
| Status | Draft |
| Authority level | Review/index guidance only. Canonical `policy/` files, policy decisions, manifests, validation receipts, evidence records, steward decisions, correction records, notices, rollback records, and changelog entries outrank this README. |
| Default posture | Do not infer release approval from policy prose. Require governed policy review and release-steward decision. |
| Required reviewers | Release steward, policy steward, affected domain steward, data steward, and docs steward. |

## Repo fit

```text
release/
├── policy/          # you are here
├── candidates/
├── manifests/
├── decisions/
├── changelog/
├── correction/
├── corrections/
└── correction_notices/

policy/              # canonical policy-as-code and policy documentation root
```

`release/policy/` belongs under `release/` because it records release-facing policy review state. It must not become a parallel policy authority. Policy rules, policy bundles, policy fixtures, and policy runtime material belong under the canonical `policy/` root or related tested roots.

## Responsibilities

| Responsibility | Expectation |
|---|---|
| Release posture | State how policy review affects a release candidate, manifest, decision, correction, notice, or rollback. |
| Policy pointer | Link to canonical policy records, not duplicate them. |
| Evidence pointer | Link to evidence when policy posture depends on evidence. |
| Validation pointer | Link to validation receipts or checks when policy status depends on validation. |
| Sensitivity posture | Record whether a release is public-safe, generalized, redacted, restricted, held, or not ready. |
| Decision pointer | Link the steward decision that applies the policy result to release state. |
| Changelog pointer | Link release-history records when policy review changes release state. |
| Follow-up | List required release, policy, manifest, correction, notice, or validation work. |

## What belongs here

- Release policy review indexes.
- Policy-readiness notes for release candidates and manifests.
- Links to canonical policy files or policy decision records.
- Links to candidates, manifests, decisions, validation receipts, evidence records, corrections, notices, rollback records, and changelog entries.
- Notes explaining release-facing policy posture and follow-up tasks.
- Dated release policy review summaries.

## What does not belong here

- Canonical policy-as-code files.
- Policy bundles, policy fixtures, or policy runtime code.
- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Source descriptors, schemas, contracts, or validator code.
- Generated summaries used as policy authority.
- Release approval without steward decision and governed record pointers.

## Required release policy review fields

- Review ID
- Review status
- Release or candidate pointer
- Manifest pointer, when applicable
- Decision pointer, when applicable
- Domain or layer scope
- Canonical policy pointer
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Sensitivity or access posture
- Correction pointer, when applicable
- Notice pointer, when applicable
- Rollback pointer, when applicable
- Changelog pointer, when applicable
- Release-facing effect
- Follow-up items
- Steward review state

## Minimal release policy review record

```markdown
# <review-id>

## Status
DRAFT / READY_FOR_REVIEW / APPROVED / HELD / SUPERSEDED / CORRECTED / NO_ACTION

## Release or candidate
<release ID, candidate path, or N/A>

## Scope
<domain, layer family, artifact family, release target, or N/A>

## Canonical policy pointer
<policy/... path or policy decision pointer>

## Governed support pointers
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Manifest: <path or N/A>
- Decision: <path or N/A>
- Changelog: <path or N/A>
- Correction: <path or N/A>
- Notice: <path or N/A>
- Rollback: <path or N/A>

## Policy posture
PUBLIC_SAFE / GENERALIZED / REDACTED / RESTRICTED / HELD / NOT_READY / ABSTAIN

## Release-facing effect
<none / ready / held / corrected / superseded / review pending>

## Follow-up
<open items or none>

## Steward review state
<reviewers, decision, and date>
```

## Review checklist

- [ ] Canonical policy pointer is present.
- [ ] Release or candidate pointer is present when review applies to a release item.
- [ ] Manifest and decision pointers are linked when release state changes.
- [ ] Evidence support is linked when policy posture depends on evidence.
- [ ] Validation support is linked when policy posture depends on validation.
- [ ] Sensitivity or access posture is explicit.
- [ ] Correction, notice, rollback, and changelog pointers are linked when applicable.
- [ ] Follow-up items are listed or marked none.
- [ ] No policy-as-code or payload files are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<scope>_policy-review.md
```

Examples:

```text
2026-07-03_people-dna-land_policy-review.md
2026-07-03_fauna-release_policy-review.md
2026-07-03_manifest-public-surface_policy-review.md
```

Use lowercase filenames, hyphenated scope names, and stable review IDs. Avoid renaming approved review records unless a migration note explains the change.

## Open verification

- [ ] Confirm CODEOWNERS for `release/policy/`.
- [ ] Confirm whether release policy review records need schema validation.
- [ ] Confirm canonical policy pointer format.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm manifest, decision, changelog, correction, notice, and rollback pointer formats.
- [ ] Confirm whether review status values should be mirrored in a schema enum.
- [ ] Confirm whether dated sublanes are needed for release policy reviews.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | First release policy review record, policy schema update, candidate promotion, manifest decision, correction, notice, rollback, or changelog integration |
