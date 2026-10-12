# `release/rollback/` — Rollback Review Lane

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-rollback-blueviolet)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/rollback/` holds rollback review records for KFM release governance.

Rollback is a governed state transition, not a file move. A rollback record should identify the affected release-facing record, explain the reason for review, point to governed support records, and state the follow-up path.

This lane is not a data home and does not approve or publish artifacts by itself.

## Status & authority

| Field | Value |
|---|---|
| Document type | Rollback parent README |
| Owning root | `release/` |
| Lane | `release/rollback/` |
| Status | Draft |
| Authority level | Parent guidance and index. Actual rollback records, manifests, validation receipts, evidence records, correction records, notices, changelog entries, and steward decisions outrank this README. |
| Default posture | Do not change release state from prose alone. Require governed records and steward decision. |
| Required reviewers | Release steward, rollback steward, data steward, affected domain steward, and docs steward. |

## Path status

Current-session evidence confirms this README existed as a blank file before this update.

Current-session evidence also confirms `release/correction/rollback/` exists as a related nested lane. Treat both rollback paths as draft until maintainers confirm whether both remain distinct or should be reconciled.

## Repo fit

```text
release/
├── rollback/       # you are here
│   ├── archaeology/
│   ├── atmosphere/
│   ├── fauna/
│   └── settlements-infrastructure/
├── correction/
│   └── rollback/
├── candidates/
├── manifests/
├── decisions/
├── changelog/
├── corrections/
└── correction_notices/
```

This path belongs under the `release/` responsibility root because it records release-governance review. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## Current sublanes

| Sublane | Scope | Status |
|---|---|---|
| `archaeology/` | Archaeology rollback review records. | Draft sublane README exists. |
| `atmosphere/` | Atmosphere rollback review records. | Draft sublane README exists. |
| `fauna/` | Fauna rollback review records. | Draft sublane README exists. |
| `settlements-infrastructure/` | Settlement systems rollback review records. | Draft sublane README exists. |

## Responsibilities

| Responsibility | Expectation |
|---|---|
| Identity | Provide a stable rollback-review ID. |
| Affected record | Link the release, candidate, manifest, correction, notice, changelog, or artifact being reviewed. |
| Scope | State the domain, layer family, artifact family, geography, time slice, or release target. |
| Evidence | Link evidence records when the review depends on evidence. |
| Validation | Link validation receipts or checks when the review depends on validation. |
| Decision | Link the steward decision that authorizes any release-state change. |
| Correction path | Link correction records when repair or replacement is required. |
| Notice path | Link notice records when communication is required. |
| Changelog | Link release-history records when release state changes. |

## What belongs here

- Parent README and sublane indexes.
- Rollback review records.
- Rollback-readiness checklists.
- Steward review summaries.
- Links to candidates, manifests, decisions, evidence records, validation receipts, correction records, notices, changelog entries, and supersession records.
- Notes explaining rollback scope, affected release-facing record, review posture, release-facing effect, and follow-up tasks.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, tiles, exports, service payloads, or map-ready artifacts.
- Source descriptors, schemas, contracts, policy files, or validator code.
- Application runtime code.
- Generated summaries used as rollback evidence or approval.
- Final release-state change without steward decision and governed record pointers.
- Silent rollback by moving files between lifecycle paths.

## Rollback outcomes

| Outcome | Meaning |
|---|---|
| `ROLLBACK_REQUIRED` | Release-facing state must be reversed through governed process. |
| `WITHDRAW_REQUIRED` | Release-facing state should be withdrawn. |
| `CORRECTION_REQUIRED` | A correction record is required before the release state can stand. |
| `REFRESH_REQUIRED` | A stale or time-valid record requires refresh before the release state can stand. |
| `GENERALIZATION_REQUIRED` | Release-facing output requires a generalized form before release state can stand. |
| `REDACTION_REQUIRED` | Release-facing output requires redaction before release state can stand. |
| `SUPERSESSION_REQUIRED` | A newer governed record should replace the affected state. |
| `HOLD_FOR_REVIEW` | More review is required. |
| `NO_ACTION` | No rollback-state change is authorized. |

## Required fields

- Rollback review ID
- Rollback review status
- Rollback outcome
- Affected record pointer
- Domain or layer scope
- Evidence pointer, when applicable
- Validation pointer, when applicable
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
ROLLBACK_REQUIRED / WITHDRAW_REQUIRED / CORRECTION_REQUIRED / REFRESH_REQUIRED / GENERALIZATION_REQUIRED / REDACTION_REQUIRED / SUPERSESSION_REQUIRED / HOLD_FOR_REVIEW / NO_ACTION

## Affected record
<release, candidate, manifest, correction, notice, changelog, or artifact pointer>

## Scope
<domain, layer family, artifact family, geography, time slice, release target, or N/A>

## Governed support pointers
- Evidence: <path or N/A>
- Validation: <path or N/A>
- Decision: <path or N/A>
- Correction: <path or N/A>
- Notice: <path or N/A>
- Changelog: <path or N/A>
- Supersession: <path or N/A>

## Release-facing effect
<none / held / rollback required / withdrawn / corrected / refreshed / generalized / redacted / superseded / review pending>

## Rollback reason
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
- [ ] Decision pointer is linked when release state changes.
- [ ] Correction, notice, changelog, and supersession pointers are linked when applicable.
- [ ] Rollback outcome is one of the finite outcomes above.
- [ ] Rollback reason is recorded.
- [ ] Release-facing effect is explicit.
- [ ] No data payloads are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<scope>_rollback-review.md
```

Examples:

```text
2026-07-03_archaeology-public-surface_rollback-review.md
2026-07-03_atmosphere-time-validity_rollback-review.md
2026-07-03_fauna-geoprivacy-posture_rollback-review.md
2026-07-03_settlement-systems-summary_rollback-review.md
```

## Open verification

- [ ] Confirm CODEOWNERS for `release/rollback/`.
- [ ] Confirm whether `release/rollback/` and `release/correction/rollback/` should remain distinct lanes or be reconciled.
- [ ] Confirm whether `release/rollbacks/` should exist as a plural compatibility lane or remain absent.
- [ ] Confirm rollback-review ID format.
- [ ] Confirm rollback-review filename convention.
- [ ] Confirm evidence pointer format.
- [ ] Confirm validation receipt pointer format.
- [ ] Confirm decision, correction, notice, changelog, and supersession pointer formats.
- [ ] Confirm whether rollback-review records require schema validation before release-state changes.
- [ ] Confirm whether the release root lane index should list `rollback/` directly.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | New rollback sublane, correction rollback reconciliation, first rollback review, correction, notice, changelog update, or release-state change |
