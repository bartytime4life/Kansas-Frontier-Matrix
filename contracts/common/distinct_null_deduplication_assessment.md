<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/distinct-null-deduplication-assessment
title: DistinctNullDeduplicationAssessmentCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Common contract steward · Analytics steward · Identity steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; common; analytics; distinct; null-semantics; deduplication
responsibility: Define fixture-only DISTINCT-like tuple, NULL, dialect, and reconciliation declarations without executing SQL, deduplicating rows, reconciling identity, or creating evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and bounded repository gap; PROPOSED inactive assessment; UNKNOWN engine parity and consumer adoption; NEEDS VERIFICATION analytics, identity, and validation review plus hosted exact-head CI"
related:
  - ./aggregate_null_semantics_disclosure.md
  - ./reversible_entity_reconciliation.md
  - ../evidence/count_population_disclosure.md
  - ../../schemas/contracts/v1/common/distinct_null_deduplication_assessment.schema.json
  - ../../fixtures/contracts/v1/common/distinct_null_deduplication_assessment/cases.json
  - ../../tools/validators/validate_distinct_null_deduplication_assessment.py
  - ../../tests/validators/test_validate_distinct_null_deduplication_assessment.py
  - ../../docs/intake/exploratory/pass-18-distinct-null-deduplication-source-map.md
tags: [kfm, common, analytics, distinct, null, multi-column, deduplication, fixture-only]
notes:
  - "Implements the smallest dependency-closed portion of supplied Pass 18 card KFM-P18-INV-155."
  - "SQL DISTINCT and grouping are never accepted as entity-identity reconciliation in this profile."
[/KFM_META_BLOCK_V2] -->

# DistinctNullDeduplicationAssessmentCandidate

`DistinctNullDeduplicationAssessmentCandidate` is an additive declaration of
how one DISTINCT-like operation treats ordered value tuples and NULLs before a
count, row-deduplication candidate, or entity-match candidate is considered for
downstream use. It implements supplied Pass 18 card `KFM-P18-INV-155` without
performing the operation.

## Boundary

A validator `PASS` proves only that the closed declaration, deterministic hash,
dialect binding, tuple fields, NULL semantics, synthetic fixture summary, and
adjacent contract references agree. It does not:

- execute SQL, inspect rows, recompute counts, or authenticate a fixture receipt;
- select or remove a source record;
- establish that two records describe the same entity;
- resolve a metric, evidence, source, policy, review, or release reference; or
- promote, deploy, publish, or authorize public use.

The schema admits opaque references, digests, field names, and aggregate fixture
counts. It admits no raw SQL, source rows, parameter values, connection details,
credentials, or source-native identity payloads.

## Declared semantics

| Axis | Declaration |
|---|---|
| Use | `COUNT_POPULATION`, `DATASET_ROW_DEDUPLICATION`, `ENTITY_MATCH_CANDIDATE`, or `UNRESOLVED`. |
| Operation | `SQL_DISTINCT`, `EXPLICIT_GROUP_BY`, `DETERMINISTIC_RECONCILIATION`, or `UNRESOLVED`. |
| Tuple identity | A canonical ordered list of one or more field names. One field uses `SINGLE_FIELD`; multiple fields use `ORDERED_VALUE_TUPLE`. |
| Row NULL posture | Include rows, exclude rows with any NULL, exclude only all-NULL rows, error, or abstain. |
| NULL equivalence | Collapse equal NULL positions, keep NULL-bearing rows separate, bind behavior to a dialect profile, error, or abstain. |
| Fixture check | Digest-bound synthetic coverage for NULL rows, duplicate rows, and multi-column tuples, with expected and observed distinct counts. |

SQL-backed operations require an opaque dialect-profile reference. A
`DIALECT_DEFINED` NULL declaration additionally requires a matched synthetic
fixture check. This profile records engine-specific behavior; it does not claim
cross-engine parity.

## Identity anti-collapse rule

`SQL_DISTINCT` and `EXPLICIT_GROUP_BY` may describe count or row-deduplication
semantics. They may not stand in for entity reconciliation. An
`ENTITY_MATCH_CANDIDATE` must use `DETERMINISTIC_RECONCILIATION` and reference
the existing reversible reconciliation contract. That reference still grants no
match, merge, split, or canonical-identity authority.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, tuple, NULL, dialect, fixture, use-case, and disclosure declarations are coherent. |
| `ABSTAIN` | A required use, operation, NULL rule, or fixture execution remains unresolved. |
| `DENY` | The declaration is contradictory, noncanonical, fixture-mismatched, identity-collapsing, or hash-invalid. |
| `ERROR` | The candidate cannot be read or evaluated safely, or records a fixture/NULL-semantics error. |

These are local validation results, not deduplication, identity, evidence,
policy, review, promotion, release, or publication decisions.

## Directory Rules basis

Reusable DISTINCT/NULL tuple semantics are a small cross-domain disclosure
adjacent to aggregate NULL semantics and reversible reconciliation under
`contracts/common/`. Machine shape, synthetic replay, executable validation,
tests, read-only CI, source reconciliation, and authoring accountability remain
in their established responsibility roots.

No SQL engine, metric registry, identity store, reconciliation queue, evidence
store, policy lane, release path, public API, or new root is introduced.

## Validation and rollback

```bash
python -m unittest tests.validators.test_validate_distinct_null_deduplication_assessment -v
python tools/validators/validate_distinct_null_deduplication_assessment.py --fixtures
```

Rollback is one additive commit revert. The profile has no runtime consumer and
mutates no query, row, identity, evidence, policy, lifecycle, review, release,
deployment, cache, or public artifact.
