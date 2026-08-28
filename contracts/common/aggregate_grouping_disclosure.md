<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/aggregate-grouping-disclosure
title: AggregateGroupingDisclosureCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Common contract steward · Analytics steward · Evidence steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; common; analytics; aggregate; grouping; disclosure
responsibility: Define fixture-only detail-row, subtotal-row, and grand-total-row grouping declarations for aggregate outputs without executing an aggregation or creating evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and bounded repository gap; PROPOSED inactive disclosure; UNKNOWN runtime adoption; NEEDS VERIFICATION cross-engine behavior, human review, and hosted exact-head CI"
related:
  - ./aggregate_statistic.md
  - ./rolling_metric_window_disclosure.md
  - ../evidence/indicator_definition.md
  - ../governance/query_run_record.md
  - ../../schemas/contracts/v1/common/aggregate_grouping_disclosure.schema.json
  - ../../fixtures/contracts/v1/common/aggregate_grouping_disclosure/cases.json
  - ../../tools/validators/validate_aggregate_grouping_disclosure.py
  - ../../tests/validators/test_validate_aggregate_grouping_disclosure.py
  - ../../docs/intake/exploratory/pass-18-aggregate-grouping-disclosure-source-map.md
tags: [kfm, common, aggregate, group-by, rollup, cube, subtotal, fixture-only, no-network]
notes:
  - "Implements the smallest dependency-closed portion of supplied Pass 18 card KFM-P18-INV-480."
  - "A PASS proves grouping-level declaration coherence only; it does not prove query execution, aggregate truth, review, release, or publication."
[/KFM_META_BLOCK_V2] -->

# AggregateGroupingDisclosureCandidate

`AggregateGroupingDisclosureCandidate` is an additive, fixture-only profile for making the aggregation level of declared output rows explicit. It distinguishes detail group rows from subtotal rows and grand-total rows, records grouping keys separately from rolled-up dimensions, distinguishes source-null dimensions from aggregation omissions, and binds every row to opaque aggregate-statistic and group-value references.

It implements the narrow requirement in supplied Pass 18 card `KFM-P18-INV-480`: aggregate outputs using `ROLLUP`, `CUBE`, grouping sets, or equivalent non-SQL behavior should not let subtotal or grand-total rows masquerade as observations.

## Boundary

A validator `PASS` proves only that:

- the closed candidate shape and deterministic profile hash agree;
- grouping dimensions, row ordinals, row references, evidence arrays, and limitations satisfy the profile's deterministic rules;
- each row partitions the declared dimensions into grouping keys and rolled-up dimensions;
- the declared grouping mask matches the rolled-up dimensions;
- detail, subtotal, and grand-total labels agree with their grouping level;
- `ROLLUP` subtotals use prefix grouping keys and suffix rollups;
- output row count matches the synthetic row declarations;
- public-support candidates carry explicit labels plus review and release-manifest references; and
- declared engine semantics do not claim unresolved or mismatched parity as coherent.

The validator does not execute SQL, dataframe, ETL, or other aggregation code. It does not inspect group values, recompute a statistic, normalize engine semantics, authenticate a query or reference, resolve evidence, assess statistical fitness, decide policy or review, promote, release, deploy, publish, or authorize public use.

## Row semantics

| Row kind | Grouping keys | Rolled-up dimensions | Required label |
|---|---|---|---|
| `DETAIL` | Every declared grouping dimension | None | `DETAIL_GROUP` |
| `SUBTOTAL` | A non-empty proper subset | The complementary non-empty subset | `SUBTOTAL` |
| `GRAND_TOTAL` | None | Every declared grouping dimension | `GRAND_TOTAL` |

`source_null_dimensions` may name only active grouping keys. A source-null marker must never be used as a substitute for a rolled-up dimension, and a rolled-up dimension must never be presented as a source null.

## Grouping mask

The first grouping dimension is bit zero, the second is bit one, and so on. A set bit means that dimension is rolled up. The mask is declaration metadata, not a claim that a particular SQL engine's native `GROUPING_ID` uses the same external ordering.

## Operation-specific rules

- `GROUP_BY` admits detail rows only.
- `ROLLUP` admits detail rows, prefix-key subtotals, and a grand total. A complete two-or-more-dimension packet must visibly contain all three kinds.
- `CUBE` admits arbitrary dimension subsets and a complete packet must visibly contain detail, subtotal, and grand-total rows.
- `GROUPING_SETS` and `NON_SQL_EQUIVALENT` admit declared subsets but do not claim equivalence to `ROLLUP` or `CUBE`.

Cross-engine parity remains separately declared as `SINGLE_ENGINE_DECLARED`, `SYNTHETIC_PARITY`, `UNRESOLVED`, or `MISMATCH`. This profile invents no engine compatibility result.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Identity, grouping partitions, row kinds, masks, references, labels, parity, and non-authority declarations are locally coherent. |
| `ABSTAIN` | Execution, engine parity, or a required reference remains incomplete or unresolved. |
| `DENY` | Dimension, row, mask, operation, null-role, label, review, count, parity, timestamp, or deterministic-identity declarations are incoherent. |
| `ERROR` | The candidate cannot be parsed or evaluated safely, or declares execution error. |

These are validation results only, not aggregate truth, evidence, policy, review, release, or publication decisions.

## Directory Rules basis

Reusable aggregate grouping semantics are adjacent to `AggregateStatistic` and `RollingMetricWindowDisclosureCandidate` under `contracts/common/`. Machine shape, synthetic replay, executable validation, conformance proof, orchestration, source reconciliation, and generated authoring provenance remain in their established responsibility roots.

No analytics engine, query store, aggregate dataset, evidence store, policy lane, release path, database adapter, public panel, or new root is created.

## Validation

```bash
python -m unittest tests.validators.test_validate_aggregate_grouping_disclosure -v
python tools/validators/validate_aggregate_grouping_disclosure.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and changes no query, aggregate, evidence, policy, lifecycle, review, release, deployment, or public artifact.
