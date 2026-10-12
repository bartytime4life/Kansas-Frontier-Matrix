# `release/rollback/archaeology/` — Archaeology Rollback Review Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-rollback-archaeology-readme
title: release/rollback/archaeology/ — Archaeology Rollback Review Lane
version: v1
status: draft
policy_label: public
owners:
  - <archaeology-domain-steward>
  - <release-steward>
  - <policy-sensitivity-reviewer>
  - <data-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, release, rollback, archaeology, sensitivity, correction, review]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-rollback-blueviolet)
![domain](https://img.shields.io/badge/domain-archaeology-brown)
![review](https://img.shields.io/badge/review-required-red)
![posture](https://img.shields.io/badge/default-fail--closed-red)

## Purpose

`release/rollback/archaeology/` holds archaeology rollback review records.

A rollback review records whether an archaeology release, candidate, manifest, correction, notice, public-facing derivative, or release-facing artifact family must be reversed, held, withdrawn, superseded, corrected, generalized, redacted, or repaired.

Rollback is a governed state transition, not a file move. A rollback note does not itself change public state. It must point to governed records, evidence, validation, policy or sensitivity review, steward decision, correction path, and follow-up tasks.

## Status & authority

| Field | Value |
|---|---|
| Document type | Archaeology rollback review README |
| Owning root | `release/` |
| Lane | `release/rollback/archaeology/` |
| Status | Draft |
| Authority level | Review guidance and index. Actual rollback records, correction records, release manifests, validation receipts, evidence records, policy/sensitivity reviews, notices, changelog entries, and steward decisions outrank this README. |
| Default posture | Do not alter release state from prose alone. Require governed rollback or correction record and steward decision. |
| Required reviewers | Archaeology steward, release steward, policy/sensitivity reviewer, data steward, and docs steward. |

## Path status

This README documents the requested path: `release/rollback/archaeology/`.

Current-session evidence confirms this README existed as a blank file before this update. Current-session evidence did not find a parent `release/rollback/README.md`. Treat this archaeology sublane as draft until the parent rollback lane is created or confirmed.

## Repo fit

```text
release/
├── rollback/
│   └── archaeology/       # you are here
├── candidates/
│   └── archaeology/
├── manifests/
├── decisions/
├── changelog/
├── correction/
├── corrections/
└── correction_notices/
```

This path belongs under the `release/` responsibility root because it records release-governance rollback review. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## Rollback responsibilities

| Responsibility | Expectation |
|---|---|
| Identity | Provide a stable rollback-review ID. |
| Affected record | Link the release, candidate, manifest, correction, notice, or public-facing derivative being reviewed. |
| Scope | State the archaeology release family, artifact family, layer family, time slice, or public-surface target. |
| Sensitivity posture | State whether the affected material is held, restricted, redacted, generalized, corrected, withdrawn, or not ready. |
| Evidence | Link evidence records when rollback rationale depends on evidence. |
| Validation | Link validation receipts or checks when rollback depends on validation results. |
| Policy review | Link policy or sensitivity review when public posture or protected-resource exposure is involved. |
| Decision | Link the steward decision that authorizes rollback, correction, withdrawal, or supersession. |
| Correction path | Link correction records when repair or replacement is required. |
| Notice path | Link correction notice records when communication is required. |
| Changelog | Link release-history records when release state changes. |

## What belongs here

- Archaeology rollback review records.
- Archaeology rollback-readiness checklists.
- Steward rollback summaries.
- Links to archaeology candidates, manifests, decisions, evidence records, validation receipts, policy/sensitivity reviews, correction records, notices, changelog entries, and supersession records.
- Notes explaining rollback scope, affected release-facing material, review posture, release-facing effect, and follow-up tasks.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exports, service payloads, or map-ready artifacts.
- Protected-resource details or sensitive location material.
- Source descriptors, schemas, contracts, policy files, or validator code.
- Generated summaries used as rollback evidence or approval.
- Final rollback, withdrawal, or publication-state change without steward decision and governed record pointers.

## Rollback outcomes

Use a finite rollback outcome where possible:

| Outcome | Meaning |
|---|---|
| `ROLLBACK_REQUIRED` | Release-facing state must be reversed through governed process. |
| `WITHDRAW_REQUIRED` | Release-facing state should be withdrawn. |
| `CORRECTION_REQUIRED` | A correction record is required before the release state can stand. |
| `GENERALIZATION_REQUIRED` | Public-facing output requires generalized form before release state can stand. |
| `REDACTION_REQUIRED` | Public-facing output requires redaction before release state can stand. |
| `SUPERSESSION_REQUIRED` | A newer governed record should replace the affected state. |
| `HOLD_FOR_REVIEW` | More evidence, validation, policy, sensitivity, or steward review is required. |
| `NO_ACTION` | No rollback-state change is authorized. |

## Required rollback-review fields

- Rollback review ID
- Rollback review status
- Rollback outcome
- Affected record pointer
- Archaeology scope
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Policy or sensitivity review pointer, when applicable
- Decision pointer, when applicable
- Correction pointer, when applicable
- Notice pointer, when applicable
- Changelog pointer, when applicable
- Supersession pointer, when applicable
- Release-facing effect
- Rollback reason
- Review date
- Reviewing steward
- Follow-up items

## Minimal rollback-review record

```markdown
# <rollback-review-id>

## Status
DRAFT / READY_FOR_REVIEW / APPROVED / HELD / CORRECTED / SUPERSEDED / WITHDRAWN / NO_ACTION

## Rollback outcome
ROLLBACK_REQUIRED / WITHDRAW_REQUIRED / CORRECTION_REQUIRED / GENERALIZATION_REQUIRED / REDACTION_REQUIRED / SUPERSESSION_REQUIRED / HOLD_FOR_REVIEW / NO_ACTION

## Affected record
<release, candidate, manifest, correction, notice, changelog, or artifact pointer>

## Archaeology scope
<release family, artifact family, layer family, time slice, public-surface target, or N/A>

## Governed support pointers
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Policy or sensitivity review: <path or N/A>
- Decision: <path or N/A>
- Correction: <path or N/A>
- Notice: <path or N/A>
- Changelog: <path or N/A>
- Supersession: <path or N/A>

## Release-facing effect
<none / held / rollback required / withdrawn / corrected / generalized / redacted / superseded / review pending>

## Rollback reason
<short reason grounded in evidence, validation, policy, sensitivity, or steward review>

## Review date
<YYYY-MM-DD>

## Reviewing steward
<steward or maintainer>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Affected record pointer is present.
- [ ] Archaeology scope is clear.
- [ ] Evidence support is linked when rollback rationale depends on evidence.
- [ ] Validation support is linked when rollback depends on validation.
- [ ] Policy or sensitivity review is linked when public posture is involved.
- [ ] Decision pointer is linked when release state changes.
- [ ] Correction, notice, changelog, and supersession pointers are linked when applicable.
- [ ] Rollback outcome is one of the finite outcomes above.
- [ ] Rollback reason is recorded.
- [ ] Public-facing posture is explicit.
- [ ] No data payloads or sensitive location material are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<archaeology-scope>_rollback-review.md
```

Examples:

```text
2026-07-03_archaeology-release-summary_rollback-review.md
2026-07-03_archaeology-public-surface_rollback-review.md
2026-07-03_archaeology-redaction-posture_rollback-review.md
```

Use lowercase filenames, hyphenated scope names, and stable review IDs. Avoid renaming approved rollback records unless a migration note explains the change.

## Open verification

- [ ] Create or confirm `release/rollback/README.md` so this archaeology lane inherits from a complete parent contract.
- [ ] Confirm whether `release/rollback/` and `release/correction/rollback/` should remain distinct lanes or be reconciled.
- [ ] Confirm CODEOWNERS for `release/rollback/archaeology/`.
- [ ] Confirm rollback-review ID format.
- [ ] Confirm rollback-review filename convention.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm policy and sensitivity review pointer formats.
- [ ] Confirm decision, correction, notice, changelog, and supersession pointer formats.
- [ ] Confirm whether rollback-review records require schema validation before release-state changes.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Parent rollback lane creation, first archaeology rollback review, correction, notice, policy/sensitivity review, changelog update, or release-state change |
