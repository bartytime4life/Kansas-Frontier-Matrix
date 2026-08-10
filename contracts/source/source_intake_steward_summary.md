<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-intake-steward-summary/v1
title: SourceIntake steward summary projection
type: semantic-contract; source-intake; reviewer-projection; fixture-first
version: v1.0.0
status: proposed; inactive; fixture-first; no-network; non-authoritative
owning_root: contracts/
truth_posture: validated-record projection only; summary status never approves policy, promotion, release, or publication
related:
  - ./source_intake_record.md
  - ./drift_summary.md
  - ../../tools/ci/render_source_intake_steward_summary.py
  - ../../tools/ci/render_stable_diff_summary.py
  - ../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# SourceIntake steward summary projection

> **Status:** `PROPOSED_INACTIVE` · **Output:** deterministic Markdown · **Review/promotion authority:** none

## Purpose

The source-intake lane already has closed `SourceIntakeRecord` and `DriftSummary` candidates. The repository also has a generic stable-diff reviewer renderer and handoff. What is missing is a source-specific human projection that turns a valid intake record into the bounded questions a steward must see without asking the steward to interpret raw JSON.

This projection renders:

- the exact input-record SHA-256 binding;
- disposition, drift kind, materiality, and review posture;
- a redacted or public-safe “what changed” explanation;
- stable reason and change codes;
- derived policy implications;
- a rollback target, or an explicit `NOT_DECLARED` hold;
- finite next-action options; and
- an authority boundary.

It reuses existing source schemas and validator behavior. It does not create another source event, diff, review, policy, evidence, or release object family.

## Input gate

The renderer accepts exactly one local `SourceIntakeRecord` JSON file. It first runs the existing `validate_source_intake_record.py` schema and semantic checks. Invalid, duplicate-key, non-finite, non-object, oversized, or symbolic-link input fails with a value-free `ERROR` payload and no Markdown summary.

## Deterministic projection statuses

| Status | Condition | Blocking |
|---|---|---:|
| `NO_ACTION` | Valid `NO_MATERIAL_CHANGE`. | no |
| `READY_FOR_REVIEW` | Valid `PROPOSED_WORK_RECORD` with a declared prior identity for rollback. | no |
| `HOLD` | Valid quarantine, abstain, error, or work proposal missing rollback evidence. | yes |
| `ERROR` | Input or output handling failed safely. | yes |

`READY_FOR_REVIEW` means only that the summary contains enough declared structure to enter a human review queue. It is not a policy result, approval, promotion, or release decision.

## Redaction and disclosure rules

- When `sensitive_implication != NONE` or `public_detail_allowed=false`, the renderer does not reproduce `DriftSummary.summary`, changed-field pointers, metric values, identity references, or source values.
- Safe records may show the bounded summary and changed-field names, with Markdown metacharacters escaped.
- Policy-decision, EvidenceBundle, CandidateDelta, receipt, and emitter references are not reproduced. Only their declared posture is summarized.
- Diagnostics contain stable reason codes and fields, never candidate values.

## Policy implications and next actions

Policy implications are derived from declared posture, not invented by the renderer: promotion required, evidence unresolved, policy review required, sensitivity posture, and public-detail denial.

Next actions are finite and disposition-sensitive. They may include `NO_ACTION`, `REQUEST_EXPANSION`, `REVIEW_FOR_PROCESSED`, `DENY`, and `ESCALATE`. `REVIEW_FOR_PROCESSED` is withheld when rollback evidence is missing. The renderer never executes an action.

## Directory Rules basis

`contracts/source/` owns this source-specific projection meaning. `tools/ci/` owns the deterministic reviewer renderer, `tests/source/` owns proof, `.github/workflows/` owns hosted orchestration, `docs/intake/exploratory/` owns source mapping, and `data/receipts/generated/` owns authoring accountability. No parallel schema, lifecycle, policy, review, release, or report authority is created.

## Non-effects and rollback

The renderer performs no network access, source fetch, RAW write, evidence resolution, policy evaluation, review approval, notification, issue creation, candidate mutation, promotion, release, deployment, publication, or public-use authorization.

Rollback is a revert of this additive projection packet. Existing source records, schemas, validators, stable-diff tooling, workflows, lifecycle data, and public artifacts remain unchanged.
