<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/aggregate-null-semantics-disclosure
title: AggregateNullSemanticsDisclosure Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Common contract steward · Analytics steward · Data-quality steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; common; analytics; aggregate; null-semantics; data-quality
responsibility: Define fixture-only NULL-treatment declarations for aggregate metric reports without executing SQL, computing a metric, imputing data, resolving evidence, or creating policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and bounded repository gap; PROPOSED inactive disclosure; UNKNOWN consumer adoption and cross-engine parity; NEEDS VERIFICATION analytics, data-quality, and validation review plus hosted exact-head CI"
related:
  - ./aggregate_statistic.md
  - ./aggregate_grouping_disclosure.md
  - ./missing_value_filter_receipt.md
  - ../evidence/count_population_disclosure.md
  - ../../schemas/contracts/v1/common/aggregate_null_semantics_disclosure.schema.json
  - ../../fixtures/contracts/v1/common/aggregate_null_semantics_disclosure/cases.json
  - ../../tools/validators/validate_aggregate_null_semantics_disclosure.py
  - ../../tests/validators/test_validate_aggregate_null_semantics_disclosure.py
  - ../../docs/intake/exploratory/pass-18-aggregate-null-semantics-disclosure-source-map.md
[/KFM_META_BLOCK_V2] -->

# AggregateNullSemanticsDisclosure Candidate

`AggregateNullSemanticsDisclosureCandidate` is an additive declaration of how
one aggregate metric treats missing input values, null grouping keys, and an
empty eligible input. It implements the smallest reviewable portion of
supplied Pass 18 card `KFM-P18-INV-430`.

## Boundary

A validator `PASS` means only that a synthetic report declaration coherently
binds opaque aggregate-statistic, query-receipt, and missingness-profile
identities to one aggregate kind and its declared NULL semantics. It does not:

- execute SQL, dataframe, ETL, or other aggregation code;
- inspect rows, compute or recompute a metric, or prove a numeric result;
- impute values, authenticate a query receipt, or resolve a missingness profile;
- decide statistical fitness, evidence, policy, review, or lifecycle state; or
- promote, release, deploy, publish, or authorize public use.

The schema contains opaque references and digests only. It admits no raw SQL,
query parameters, source rows, computed metric value, or imputed value.

## Aggregate and NULL declarations

| Aggregate kind | Value fields | Input NULL posture | Empty-input posture |
|---|---|---|---|
| `ROW_COUNT` | None | `INCLUDED_AS_ROW` | `ZERO` |
| `VALUE_COUNT` | Exactly one | `EXCLUDED` | `ZERO` |
| `DISTINCT_COUNT` | One or more | `EXCLUDED` | `ZERO` |
| `SUM` | Exactly one | `EXCLUDED`, `IMPUTED`, or `ERROR` | Declared explicitly |
| `AVERAGE`, `MINIMUM`, `MAXIMUM` | Exactly one | `EXCLUDED`, `IMPUTED`, or `ERROR` | `NULL`, `NO_RESULT`, or `ERROR` |
| `UNRESOLVED` | None | `UNRESOLVED` | `UNRESOLVED` |

Count kinds must reference the existing
`CountPopulationDisclosureCandidate`; non-count kinds must not. This profile
therefore composes population semantics instead of duplicating them. An
`IMPUTED` declaration requires an opaque imputation-receipt reference, while
all other postures prohibit that reference.

When no grouping field is declared, group-key NULL handling must be
`NOT_GROUPED`. A grouped report must declare `OWN_GROUP`, `ROW_EXCLUDED`,
`ERROR`, or `UNRESOLVED`. This declaration does not replace the existing
aggregate-grouping contract's ownership of detail, subtotal, and grand-total
row roles.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, deterministic identity, aggregate kind, NULL treatment, adjacent references, and disclosure are coherent. |
| `ABSTAIN` | Aggregate, input, grouping, empty-input, query, missingness, or disclosure posture remains unresolved. |
| `DENY` | Aggregate fields, composed references, imputation, grouping, public disclosure, timestamp, or deterministic identity is contradictory. |
| `ERROR` | The candidate cannot be parsed or evaluated safely under the closed schema. |

These are validation outcomes only, not data-quality findings, metric values,
evidence decisions, policy decisions, review decisions, or release states.

## Directory Rules basis

Reusable aggregate NULL semantics are adjacent to `AggregateStatistic` and
`AggregateGroupingDisclosureCandidate` under `contracts/common/`. Machine
shape, synthetic replay, executable validation, conformance tests, read-only
CI, source reconciliation, and authoring accountability remain in their
established responsibility roots.

No analytics engine, query store, data-quality store, missingness registry,
evidence store, policy lane, release path, public API, or new root is created.

## Validation and rollback

```bash
python -m unittest tests.validators.test_validate_aggregate_null_semantics_disclosure -v
python tools/validators/validate_aggregate_null_semantics_disclosure.py --fixtures
```

Rollback is one additive commit revert. The profile has no runtime consumer and
creates no live metric, query, imputation, evidence, policy, review, release,
deployment, cache, or public state.
