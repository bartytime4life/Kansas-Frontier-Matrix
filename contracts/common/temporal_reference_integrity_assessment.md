<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/temporal-reference-integrity-assessment/v1
title: TemporalReferenceIntegrityAssessmentCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Common contract steward · Temporal steward · Data steward · Evidence steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; common; temporal-integrity; referential-integrity; no-public-authority
owning_root: contracts/
responsibility: Define a deterministic assessment of time-bounded subject-to-target references without executing constraints or creating source, evidence, policy, review, lifecycle, release, or publication authority.
truth_posture: "CONFIRMED source-card traceability and repository gap; PROPOSED inactive semantics; NEEDS VERIFICATION human review, failure-policy selection, and consumer adoption"
related:
  - ./temporal_window.md
  - ./period_boundary_predicate_disclosure.md
  - ./temporal_authority_envelope.md
  - ../data/temporal_slice.md
  - ../../schemas/contracts/v1/common/temporal_reference_integrity_assessment.schema.json
  - ../../fixtures/contracts/v1/common/temporal_reference_integrity_assessment/cases.json
  - ../../tools/validators/validate_temporal_reference_integrity_assessment.py
  - ../../tests/validators/test_validate_temporal_reference_integrity_assessment.py
  - ../../docs/intake/exploratory/pass-18-temporal-reference-integrity-source-map.md
tags: [kfm, common, temporal, referential-integrity, valid-time, transaction-time, fixture-only]
notes:
  - "Implements the shared assessment portion of supplied Pass 18 card KFM-P18-INV-490."
  - "DENY_CANDIDATE and QUARANTINE_CANDIDATE are non-executing recommendations; the source's default-policy question remains open."
[/KFM_META_BLOCK_V2] -->

# TemporalReferenceIntegrityAssessmentCandidate

`TemporalReferenceIntegrityAssessmentCandidate` makes one time-bounded
subject-to-target relationship inspectable. It answers a narrow local
question: does the declared observation or history-row interval satisfy the
declared valid-time or transaction-time relationship to the referenced source,
geography, identity, or other version record?

## Status and boundary

| Field | Value |
|---|---|
| Profile | `kfm.common.temporal-reference-integrity-assessment.fixture.v1` |
| Adoption | `PROPOSED_INACTIVE` |
| Execution | Fixture-only, deterministic, no-network |
| Reference resolution | Not performed |
| Database constraint or write | Not performed |
| Quarantine or denial action | Not performed |
| Evidence, policy, review, release, publication | Not performed |
| Public-use authority | Fixed `false` |

The profile composes existing temporal contracts by reference. It does not
alter `TemporalWindow`, select a repository-wide boundary convention, inspect a
database, authenticate a record, or prove that a supplied interval is true.

## Relationship and axis declarations

Each candidate binds one subject record, one target version record, one target
role, and one temporal mode:

- `VALID_TIME` checks only the period in which the represented fact is valid;
- `TRANSACTION_TIME` checks only the period in which the represented row is
  present in the governed system; and
- `BITEMPORAL` requires one check for each axis, in that order.

The target roles are `SOURCE_VERSION`, `GEOGRAPHY_VERSION`,
`IDENTITY_VERSION`, and `OTHER`. A reference marked `PRESENT` is still only a
local declaration; no resolver is invoked. `MISSING` is a deterministic
integrity failure. `UNRESOLVED` causes abstention.

## Finite temporal constraints

Each axis check declares one of four bounded constraints:

| Constraint | Local meaning |
|---|---|
| `SUBJECT_WITHIN_TARGET` | Every included instant in the subject interval is included by the target interval. |
| `SUBJECT_OVERLAPS_TARGET` | The intervals share at least one included instant. |
| `SUBJECT_START_WITHIN_TARGET` | The subject start instant is included by the target interval. |
| `SUBJECT_END_WITHIN_TARGET` | The subject end instant is included by the target interval. |

Intervals are finite proper UTC intervals. Start and end inclusivity are
explicit, so a shared endpoint counts only when both intervals include it.
This local vocabulary does not claim adoption of a SQL dialect or an external
temporal standard.

## States and non-executing failure handling

Every axis declares `SATISFIED`, `VIOLATED`, or `UNRESOLVED`. The overall state
is `VIOLATED` when a record is known missing or any resolved axis fails;
otherwise it is `UNRESOLVED` when a record or window reference is unresolved;
otherwise it is `SATISFIED`.

For a violation, the packet may recommend either `DENY_CANDIDATE` or
`QUARANTINE_CANDIDATE`. Both are labels for later governed review. The schema
fixes `recommendation_only` to `true` and `disposition_executed` to `false`.
This deliberately preserves the source card's open question about the default
failure policy.

## Outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Present records and resolved intervals satisfy every declared check. |
| `ABSTAIN` | A subject, target, or window reference remains unresolved. |
| `DENY` | A record is known missing, a temporal relation fails, or a resolved declaration is contradictory. |
| `ERROR` | The candidate cannot be evaluated under the closed schema. |

These are validator outcomes only. They are not database constraint actions,
policy decisions, review decisions, lifecycle states, or public answers.

## Directory Rules basis

Accepted ADR-0029 and connected Directory Rules place shared temporal meaning
under `contracts/common/`, machine shape under `schemas/`, synthetic replay
under `fixtures/`, executable validation under `tools/`, conformance proof
under `tests/`, orchestration under `.github/`, source reconciliation under
`docs/intake/exploratory/`, and generated process memory under
`data/receipts/generated/`. No history-table, database, evidence, policy,
release, or public-surface root is created.

## Validation and rollback

```bash
python -m unittest tests.validators.test_validate_temporal_reference_integrity_assessment -v
python tools/validators/validate_temporal_reference_integrity_assessment.py --fixtures
```

Before merge, close the draft pull request and abandon its branch. After an
authorized merge, revert this additive packet. It mutates no record,
relationship, table, source, geography, identity, evidence object, policy,
review state, lifecycle state, release, deployment, or public surface.
