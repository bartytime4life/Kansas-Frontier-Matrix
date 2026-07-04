# `release/rollback_cards/roads-rail-trade/` — Roads Rail Trade Rollback Cards

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-rollback-cards-roads-rail-trade-readme
title: release/rollback_cards/roads-rail-trade/ — Roads Rail Trade Rollback Cards
version: v1
status: draft
policy_label: public
owners:
  - <roads-rail-trade-domain-steward>
  - <release-steward>
  - <rollback-steward>
  - <data-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, release, rollback-cards, roads-rail-trade, correction, review]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-rollback--cards-blueviolet)
![domain](https://img.shields.io/badge/domain-roads--rail--trade-slategray)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/rollback_cards/roads-rail-trade/` holds compact rollback cards for the roads-rail-trade release lane.

A rollback card is a review aid. It summarizes what release-facing record may need reversal, correction, withdrawal, supersession, or hold-for-review treatment. It should point to governed support records rather than duplicate data or decide release state by itself.

Rollback is a governed state transition, not a file move. A rollback card does not itself change public state.

## Status & authority

| Field | Value |
|---|---|
| Document type | Roads-rail-trade rollback-card README |
| Owning root | `release/` |
| Lane | `release/rollback_cards/roads-rail-trade/` |
| Status | Draft |
| Authority level | Review-card guidance and index. Actual rollback records, correction records, release manifests, validation receipts, evidence records, notices, changelog entries, and steward decisions outrank this README. |
| Default posture | Do not change release state from card prose alone. Require governed records and steward decision. |
| Required reviewers | Roads-rail-trade steward, release steward, rollback steward, data steward, and docs steward; policy reviewer when needed. |

## Path status

Current-session evidence confirms this README existed as a blank file before this update.

Current-session evidence also confirms the parent `release/rollback_cards/README.md` is still a greenfield stub. Treat this sublane as draft until the parent rollback-card lane is expanded.

## Repo fit

```text
release/
├── rollback_cards/
│   └── roads-rail-trade/       # you are here
├── rollback/
├── correction/
├── candidates/
│   └── roads-rail-trade/
├── manifests/
├── decisions/
├── changelog/
├── corrections/
└── correction_notices/
```

This path belongs under the `release/` responsibility root because it records release-governance review cards. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## Rollback-card responsibilities

| Responsibility | Expectation |
|---|---|
| Identity | Provide a stable rollback-card ID. |
| Affected record | Link the release, candidate, manifest, correction, notice, changelog, or artifact being reviewed. |
| Scope | State the roads-rail-trade release family, artifact family, layer family, geography, time slice, or release target. |
| Evidence | Link evidence records when the card depends on evidence. |
| Validation | Link validation receipts or checks when the card depends on validation. |
| Decision | Link the steward decision that authorizes any release-state change. |
| Correction path | Link correction records when repair or replacement is required. |
| Notice path | Link notice records when communication is required. |
| Changelog | Link release-history records when release state changes. |
| Handoff | Link a full rollback review record when the card is not enough to support a decision. |

## What belongs here

- Roads-rail-trade rollback cards.
- Short rollback-readiness summaries.
- Steward review notes.
- Links to candidates, manifests, decisions, evidence records, validation receipts, correction records, notices, changelog entries, supersession records, and full rollback review records.
- Notes explaining rollback scope, affected release-facing record, review posture, release-facing effect, and follow-up tasks.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exports, service payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy files, or validator code.
- Application runtime code.
- Detailed release-sensitive network material or unreviewed public-surface details.
- Generated summaries used as rollback evidence or approval.
- Final release-state change without steward decision and governed record pointers.
- Silent rollback by moving files between lifecycle paths.

## Card outcomes

Use a finite card outcome where possible:

| Outcome | Meaning |
|---|---|
| `ROLLBACK_REVIEW_REQUIRED` | A full rollback review should be opened. |
| `WITHDRAW_REVIEW_REQUIRED` | Withdrawal review should be opened. |
| `CORRECTION_REQUIRED` | A correction record is required before the release state can stand. |
| `REFRESH_REQUIRED` | A stale or time-valid record requires refresh before the release state can stand. |
| `GENERALIZATION_REQUIRED` | Release-facing output requires generalized form before release state can stand. |
| `REDACTION_REQUIRED` | Release-facing output requires redaction before release state can stand. |
| `SUPERSESSION_REQUIRED` | A newer governed record should replace the affected state. |
| `HOLD_FOR_REVIEW` | More review is required. |
| `NO_ACTION` | No release-state change is recommended by this card. |

## Required rollback-card fields

- Rollback card ID
- Card status
- Card outcome
- Affected record pointer
- Roads-rail-trade scope
- Geography and time period, when applicable
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Decision pointer, when applicable
- Correction pointer, when applicable
- Notice pointer, when applicable
- Changelog pointer, when applicable
- Supersession pointer, when applicable
- Full rollback-review pointer, when applicable
- Release-facing effect
- Card reason
- Review date
- Reviewing steward
- Follow-up items

## Minimal rollback-card record

```markdown
# <rollback-card-id>

## Status
DRAFT / READY_FOR_REVIEW / APPROVED / HELD / CORRECTED / SUPERSEDED / WITHDRAWN / NO_ACTION

## Card outcome
ROLLBACK_REVIEW_REQUIRED / WITHDRAW_REVIEW_REQUIRED / CORRECTION_REQUIRED / REFRESH_REQUIRED / GENERALIZATION_REQUIRED / REDACTION_REQUIRED / SUPERSESSION_REQUIRED / HOLD_FOR_REVIEW / NO_ACTION

## Affected record
<release, candidate, manifest, correction, notice, changelog, or artifact pointer>

## Roads-rail-trade scope
<release family, artifact family, layer family, geography, time slice, release target, or N/A>

## Governed support pointers
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Decision: <path or N/A>
- Correction: <path or N/A>
- Notice: <path or N/A>
- Changelog: <path or N/A>
- Supersession: <path or N/A>
- Full rollback review: <path or N/A>

## Release-facing effect
<none / held / rollback review required / withdrawn / corrected / refreshed / generalized / redacted / superseded / review pending>

## Card reason
<short reason grounded in evidence, validation, or steward review>

## Review date
<YYYY-MM-DD>

## Reviewing steward
<steward or maintainer>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Affected record pointer is present.
- [ ] Roads-rail-trade scope is clear.
- [ ] Evidence support is linked when needed.
- [ ] Validation support is linked when needed.
- [ ] Decision pointer is linked when release state changes.
- [ ] Correction, notice, changelog, and supersession pointers are linked when applicable.
- [ ] Full rollback review pointer is linked when the card escalates beyond summary review.
- [ ] Card outcome is one of the finite outcomes above.
- [ ] Card reason is recorded.
- [ ] Release-facing effect is explicit.
- [ ] No data payloads or unreviewed public-surface details are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<roads-rail-trade-scope>_rollback-card.md
```

Examples:

```text
2026-07-03_roads-rail-trade-summary_rollback-card.md
2026-07-03_roads-rail-trade-public-surface_rollback-card.md
2026-07-03_roads-rail-trade-validation-posture_rollback-card.md
```

Use lowercase filenames, hyphenated scope names, and stable card IDs. Avoid renaming approved rollback cards unless a migration note explains the change.

## Open verification

- [ ] Expand `release/rollback_cards/README.md` so this roads-rail-trade lane inherits from a complete parent contract.
- [ ] Confirm whether rollback cards are distinct from full rollback review records under `release/rollback/`.
- [ ] Confirm CODEOWNERS for `release/rollback_cards/roads-rail-trade/`.
- [ ] Confirm rollback-card ID format.
- [ ] Confirm rollback-card filename convention.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm decision, correction, notice, changelog, supersession, and full rollback-review pointer formats.
- [ ] Confirm whether rollback-card records require schema validation before release-state changes.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Parent rollback-card lane expansion, first roads-rail-trade rollback card, full rollback review, correction, notice, changelog update, or release-state change |
