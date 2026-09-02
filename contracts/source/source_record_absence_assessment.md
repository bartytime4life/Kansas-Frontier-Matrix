<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-record-absence-assessment
title: SourceRecordAbsenceAssessment Contract
type: semantic-contract; source-semantics; false-clear-prevention
version: v0.1.0
status: proposed; fixture-first; no-network; non-authoritative
owners: OWNER_TBD — Source steward · Evidence steward · Domain steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; source; absence-semantics; false-clear-prevention; no-public-authority
related:
  - ./README.md
  - ../../schemas/contracts/v1/source/source_record_absence_assessment.schema.json
  - ../../fixtures/contracts/v1/source/source_record_absence_assessment/
  - ../../tools/validators/validate_source_record_absence_assessment.py
  - ../../tests/validators/test_validate_source_record_absence_assessment.py
tags: [kfm, source, missing-record, complete-snapshot, incremental-feed, false-clear, deterministic]
notes:
  - "A missing record has different meaning for a complete snapshot, incremental feed, publication page, and mixed surface."
  - "This profile emits a removal candidate only; it never clears an event, deletes history, or authorizes publication."
[/KFM_META_BLOCK_V2] -->

# SourceRecordAbsenceAssessment

> `SourceRecordAbsenceAssessment` records the bounded interpretation of a previously present source record that is absent from a later capture. It prevents a missing row from becoming an unsupported clear, deletion, rescission, or public-state transition.

## Status and authority boundary

| Field | Value |
|---|---|
| Status | `PROPOSED` / fixture-first / no-network |
| Semantic home | `contracts/source/source_record_absence_assessment.md` |
| Machine shape | `schemas/contracts/v1/source/source_record_absence_assessment.schema.json` |
| Authority | Source-mode semantics and local consistency only |
| Public use | Always false in this profile |
| Domain transition | Candidate only; owning domain policy must decide |

A valid record does **not** prove that a source is complete, healthy, authoritative, current, rights-cleared, or admitted. It does not resolve evidence, clear an advisory, mutate source state, delete history, evaluate policy, promote, release, publish, or create a public route.

## Why this object exists

Source absence is not one universal fact. The governing briefing-integration architecture distinguishes four source modes:

| Source mode | Missing record meaning | Safe assessment behavior |
|---|---|---|
| `COMPLETE_AUTHORITATIVE_SNAPSHOT` | May indicate removal only when completeness, source health, and parsing are verified. | Emit `REMOVAL_CANDIDATE`; preserve history; require later domain/evidence/policy review. |
| `INCREMENTAL_EVENT_FEED` | No new event was observed. | Emit `RETAIN_PRIOR_STATE`; wait for a superseding event. |
| `PUBLICATION_PAGE` | Layout, content, or parser behavior may have changed. | `ABSTAIN`; preserve the source artifact and parse confidence. |
| `MIXED_SURFACE` | Tables, releases, feeds, and corrections may disagree or update at different times. | `ABSTAIN`; reconcile separate artifacts by identity and time. |

This common source contract keeps those meanings explicit without replacing domain-specific rescission, expiration, correction, or withdrawal contracts.

## Required shape

The object binds:

- an admitted-source reference and explicit source-semantics contract;
- source mode, health, snapshot completeness, parse status, and parse confidence;
- a SHA-256 record-key token rather than raw identifying values;
- prior and current immutable source-artifact references;
- the last known state reference;
- capture and assessment times;
- a finite outcome and reviewed reason-code vocabulary;
- provenance references; and
- hard false values for mutation, clearance, promotion, release, publication, and public-use authority.

## Deterministic identity

`assessment_id` is content-derived:

```text
urn:kfm:source-record-absence:sha256:<digest>
```

The canonical identity projection contains:

```text
source_descriptor_ref
source_mode
record_key_hash
prior_snapshot_ref
current_snapshot_ref
current_captured_at
```

The validator serializes that projection as sorted-key UTF-8 JSON without insignificant whitespace and hashes it with SHA-256. `spec_hash` binds the full assessment except the `spec_hash` field itself using the same bounded fixture canonicalization profile.

## Finite outcomes

| Outcome | Required posture |
|---|---|
| `REMOVAL_CANDIDATE` | Allowed only for a healthy, fully parsed, completeness-verified authoritative snapshot. Requires a transition-candidate reference and does not retain the prior state as current. |
| `RETAIN_PRIOR_STATE` | Required for incremental-feed absence. No transition candidate is allowed. |
| `ABSTAIN` | Required when publication-page or mixed-surface absence is ambiguous, or a complete snapshot is not strongly verified. |
| `ERROR` | Required when source-health or parsing failed. Prior state remains retained. |

## Invariants

- The record was present in the prior capture and absent in the current capture.
- `prior_captured_at <= current_captured_at <= assessed_at`.
- A removal candidate is impossible unless source mode, health, completeness, and parse state all support it.
- Incremental-feed absence cannot clear prior state.
- Publication-page absence cannot create a removal candidate.
- Mixed surfaces remain separate and require reconciliation.
- Reason, input, and evidence arrays are unique and lexically sorted.
- Source history cannot be deleted by this object.
- All governance authority flags remain false.

## Validation

```bash
python -m unittest discover   --start-directory tests/validators   --pattern 'test_validate_source_record_absence_assessment.py'  --verbose

python tools/validators/validate_source_record_absence_assessment.py --fixtures
```

The validator performs no network access. Diagnostics contain only finite finding codes and JSON pointers; candidate values are not echoed.

## Integration boundary

A later source-adapter PR may consume this object after it declares its exact source mode and can prove source health, completeness, parser behavior, and immutable capture identity. Existing domain-specific delta code must not be changed merely because this profile exists. Integration requires its own fixtures showing that missing rows no longer produce false clears.

## Correction and rollback

Before merge, close the draft pull request and delete the feature branch. After merge, revert this contract/schema/fixture/validator/test/workflow slice. If downstream records begin referencing stable assessment IDs, preserve them and use correction or supersession instead of destructive deletion.
