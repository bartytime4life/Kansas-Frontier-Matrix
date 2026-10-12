<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-intake-record
title: SourceIntakeRecord semantic contract
type: semantic-contract; source-intake; watcher-candidate; fixture-first
version: v0.1.0
status: proposed; inactive; fixture-first; no-network; non-publisher
owners: OWNER_TBD — Source steward · Contracts steward · Schema steward · Validation steward · Policy steward · Evidence steward
created: 2026-08-08
updated: 2026-08-08
policy_label: repository-facing; source; intake; watcher; fail-closed; promotion-required; non-authoritative
related:
  - ./drift_summary.md
  - ../../schemas/contracts/v1/source/source_intake_record.schema.json
  - ../../fixtures/contracts/v1/source/source_intake_record/
  - ../../tools/validators/validate_source_intake_record.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, source, intake, watcher, drift, candidate, quarantine, no-network]
notes:
  - "Source idea: KFM-P4-PROG-0001."
  - "This contract resolves the SourceIntakeRecord-to-CandidateDelta question by making CandidateDelta an optional downstream proposal reference, never an intake prerequisite or promotion authority."
[/KFM_META_BLOCK_V2] -->

# SourceIntakeRecord semantic contract

`SourceIntakeRecord` is the shared candidate envelope for source-watch and source-health observations. It replaces arbitrary watcher outbox JSON with one closed, finite, reviewable record that binds source identity, source role, publication posture, evidence-resolution posture, policy-review posture, and a `DriftSummary`.

The record is a **WORK or QUARANTINE candidate only**. It cannot represent `PUBLISHED`, cannot authorize RAW admission, and always declares `promotion_required=true`.

## Required fields

A conforming record carries:

- `intake_id`, `source_descriptor_ref`, and the descriptor-declared `source_role`;
- canonical `observed_at` time;
- `publication_state` limited to `WORK` or `QUARANTINE`;
- `promotion_required=true`;
- `evidence_bundle_resolved` and, when true, `evidence_bundle_ref`;
- `policy_review_required` and an optional policy-decision reference;
- one inline `DriftSummary`;
- one finite `disposition` and canonically sorted `reason_codes`;
- an optional `candidate_delta_ref`; and
- an emitter identity and optional receipt reference.

## Finite dispositions

| Disposition | Meaning | Required posture |
|---|---|---|
| `NO_MATERIAL_CHANGE` | Comparison did not produce a review-worthy delta. | `WORK`; drift materiality `NONE` or `BELOW_THRESHOLD`; no `candidate_delta_ref`. |
| `PROPOSED_WORK_RECORD` | A bounded downstream change proposal may be created. | `WORK`; drift materiality `REVIEW_REQUIRED`; optional `candidate_delta_ref`. |
| `QUARANTINED` | Rights, sensitivity, geometry, taxonomy, integrity, or another blocking condition requires hold. | `QUARANTINE`; drift materiality `BLOCKING`; policy review required. |
| `ABSTAIN` | The watcher cannot make a supportable candidate determination. | `QUARANTINE`; no publication effect. |
| `ERROR` | Bounded processing failed. | `QUARANTINE`; no publication effect. |

## Relationship to CandidateDelta

`SourceIntakeRecord` and `CandidateDelta` are distinct object families:

1. `SourceIntakeRecord` records a source observation and finite intake disposition.
2. A `PROPOSED_WORK_RECORD` may reference a separately governed `CandidateDelta` using `candidate_delta_ref`.
3. A `CandidateDelta` must never be inferred from a no-change, abstain, error, or quarantined record.
4. Neither object self-promotes; review, policy, evidence closure, validation, release, correction, and rollback remain separate.

This preserves the query-save-recompile loop without collapsing observation and proposed mutation into one object.

## Invariants

- Direct-to-`PUBLISHED` is schema-invalid.
- An evidence resolution claim requires a concrete EvidenceBundle reference.
- `BLOCKING` drift must be quarantined and require policy review.
- A candidate delta reference is valid only for `PROPOSED_WORK_RECORD`.
- Reason codes, drift change codes, and changed fields are deterministic and sorted.
- No exact sensitive geometry, raw payload, credential, or private operational detail belongs in this envelope.

## Non-effects

A passing record or validator does not activate a source, fetch a live endpoint, admit RAW, resolve evidence authenticity, approve policy, create a release, publish a map layer, notify users, or grant a watcher authority.

## Rollback

Before merge, close the draft pull request and delete only its feature branch. After merge, revert the implementation commit through a reviewed pull request. This inactive fixture-first slice has no external cleanup or lifecycle migration.
