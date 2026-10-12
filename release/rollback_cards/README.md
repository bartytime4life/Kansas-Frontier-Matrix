# `release/rollback_cards/` — Release Review Card Index

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-review--cards-blueviolet)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/rollback_cards/` is the parent index for compact release review cards.

A card is a short release-governance aid. It identifies an affected release-facing record, summarizes why the record needs review, and links the governed records that support the next step.

A card is not a final approval record. It should not publish artifacts, replace manifests, replace correction records, or stand in for steward decisions.

## Status & authority

| Field | Value |
|---|---|
| Document type | Release review-card parent README |
| Owning root | `release/` |
| Lane | `release/rollback_cards/` |
| Status | Draft |
| Authority level | Parent index and card guidance. Child cards, manifests, validation receipts, evidence records, correction records, notices, changelog entries, and steward decisions outrank this README. |
| Default posture | Use cards as short review aids only. Link governed records for any release-facing effect. |
| Required reviewers | Release steward, data steward, affected domain steward, and docs steward. |

## Repo fit

```text
release/
├── rollback_cards/       # you are here
│   ├── roads-rail-trade/
│   └── settlements-infrastructure/
├── rollback/
├── correction/
├── candidates/
├── manifests/
├── decisions/
├── changelog/
├── corrections/
└── correction_notices/
```

This path belongs under `release/` because it records release-governance review cards. It is not a lifecycle data directory.

## Current sublanes

| Sublane | Scope | Status |
|---|---|---|
| `roads-rail-trade/` | Roads-rail-trade release review cards. | Draft README exists. |
| `settlements-infrastructure/` | Settlement systems release review cards. | Draft README exists. |

Add new sublanes only when a domain needs its own card fields, review ownership, or handoff notes.

## Card responsibilities

| Responsibility | Expectation |
|---|---|
| Card identity | Provide a stable card ID. |
| Affected record | Link the release-facing record being reviewed. |
| Scope | State the domain, artifact family, geography, time slice, or release target. |
| Evidence | Link evidence records when the card depends on evidence. |
| Validation | Link validation receipts when the card depends on validation. |
| Decision | Link steward decision when a decision exists. |
| Correction path | Link correction records when repair or replacement is required. |
| Notice path | Link notice records when communication is required. |
| Changelog | Link release-history records when release history changes. |
| Handoff | Link a full review record when a short card is not enough. |

## What belongs here

- Parent README and sublane indexes.
- Compact release review cards.
- Short readiness summaries.
- Steward review notes.
- Links to candidates, manifests, decisions, evidence records, validation receipts, correction records, notices, changelog entries, supersession records, and full review records.
- Notes explaining scope, affected record, review posture, release-facing effect, and follow-up tasks.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exports, service payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy files, or validator code.
- Application runtime code.
- Generated summaries used as evidence or approval.
- Final release approval without governed records and steward decision.

## Card outcomes

| Outcome | Meaning |
|---|---|
| `REVIEW_REQUIRED` | A full release review should be opened. |
| `CORRECTION_REQUIRED` | A correction record is required before the release-facing record can stand. |
| `REFRESH_REQUIRED` | A stale or time-valid record requires refresh. |
| `GENERALIZATION_REQUIRED` | Release-facing output requires a generalized form. |
| `REDACTION_REQUIRED` | Release-facing output requires redaction. |
| `SUPERSESSION_REQUIRED` | A newer governed record should replace the affected record. |
| `HOLD_FOR_REVIEW` | More review is required. |
| `NO_ACTION` | No release-facing change is recommended by this card. |

## Required card fields

Every card should capture:

- Card ID
- Card status
- Card outcome
- Affected record pointer
- Domain or layer scope
- Evidence pointer, when applicable
- Validation pointer, when applicable
- Decision pointer, when applicable
- Correction pointer, when applicable
- Notice pointer, when applicable
- Changelog pointer, when applicable
- Supersession pointer, when applicable
- Full review pointer, when applicable
- Release-facing effect
- Card reason
- Review date
- Reviewing steward
- Follow-up items

## Minimal card record

```markdown
# <card-id>

## Status
DRAFT / READY_FOR_REVIEW / APPROVED / HELD / CORRECTED / SUPERSEDED / NO_ACTION

## Card outcome
REVIEW_REQUIRED / CORRECTION_REQUIRED / REFRESH_REQUIRED / GENERALIZATION_REQUIRED / REDACTION_REQUIRED / SUPERSESSION_REQUIRED / HOLD_FOR_REVIEW / NO_ACTION

## Affected record
<release, candidate, manifest, correction, notice, changelog, or artifact pointer>

## Scope
<domain, artifact family, geography, time slice, release target, or N/A>

## Governed support pointers
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Decision: <path or N/A>
- Correction: <path or N/A>
- Notice: <path or N/A>
- Changelog: <path or N/A>
- Supersession: <path or N/A>
- Full review: <path or N/A>

## Release-facing effect
<none / held / review required / corrected / refreshed / generalized / redacted / superseded / review pending>

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
- [ ] Scope is clear.
- [ ] Evidence support is linked when needed.
- [ ] Validation support is linked when needed.
- [ ] Decision pointer is linked when a decision exists.
- [ ] Correction, notice, changelog, and supersession pointers are linked when applicable.
- [ ] Full review pointer is linked when the card escalates beyond summary review.
- [ ] Card outcome is one of the finite outcomes above.
- [ ] Card reason is recorded.
- [ ] Release-facing effect is explicit.
- [ ] No data payloads are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<scope>_release-review-card.md
```

Examples:

```text
2026-07-03_roads-rail-trade-summary_release-review-card.md
2026-07-03_settlement-systems-public-surface_release-review-card.md
2026-07-03_release-validation-posture_release-review-card.md
```

Use lowercase filenames, hyphenated scope names, and stable card IDs.

## Open verification

- [ ] Confirm CODEOWNERS for `release/rollback_cards/`.
- [ ] Confirm whether these cards remain distinct from full review records under `release/rollback/`.
- [ ] Confirm card ID format.
- [ ] Confirm card filename convention.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm decision, correction, notice, changelog, supersession, and full-review pointer formats.
- [ ] Confirm whether card records require schema validation before release-facing action.
- [ ] Confirm whether the release root lane index should list `rollback_cards/` directly.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Expanded README replacing minimal parent index |
| Next review trigger | New card sublane, first card, full review handoff, correction, notice, changelog update, or release-facing action |
