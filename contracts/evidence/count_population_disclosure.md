<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/count-population-disclosure
title: CountPopulationDisclosureCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Analytics steward · Metric steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; evidence; analytics; count; population; disclosure
responsibility: Define fixture-only disclosure semantics for the population counted by one public-metric candidate without computing a value or creating evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./indicator_definition.md
  - ./analytic_output_disclosure_assessment.md
  - ../common/aggregate_statistic.md
  - ../../schemas/contracts/v1/evidence/count_population_disclosure.schema.json
  - ../../fixtures/contracts/v1/evidence/count_population_disclosure/cases.json
  - ../../tools/validators/evidence/validate_count_population_disclosure.py
  - ../../tests/validators/evidence/test_validate_count_population_disclosure.py
  - ../../docs/intake/exploratory/pass-18-count-population-disclosure-source-map.md
[/KFM_META_BLOCK_V2] -->

# CountPopulationDisclosureCandidate

`CountPopulationDisclosureCandidate` is an additive, fixture-only profile for declaring what population one count represents before that count is considered for a map, dashboard, Focus Mode response, or export.

It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-157`: a count must disclose whether it counts all rows, non-null values, distinct value tuples, grouped output rows, or a filtered subset.

## Boundary

The profile is `PROPOSED_INACTIVE`, deterministic, no-network, and non-authoritative. A validator `PASS` means only that:

- the candidate is closed under this schema and its deterministic profile hash replays;
- the count kind, counted fields, null posture, grouping, and population basis agree;
- filtered and unfiltered declarations carry coherent predicate references;
- evidence, metric-definition, and query-receipt identities remain explicit opaque references; and
- a public-facing candidate supplies a visible population note, details surface, and review references.

It does **not** execute SQL, inspect rows, recompute a count, resolve a reference, authenticate a query receipt, select a population, prove statistical fitness, decide evidence or policy, approve review, promote lifecycle state, release, deploy, publish, or authorize public use.

## Relationship to adjacent contracts

`IndicatorDefinition` defines what an indicator method means. `AggregateStatistic` defines a source-issued or source-derived aggregate with geography and method context. This profile owns neither responsibility. It records the result-side population semantics of a count by reference so `COUNT(*)`, `COUNT(field)`, distinct counts, grouped rows, and filtered subsets cannot be presented as interchangeable.

For this profile, **population basis** is not a rate or ratio denominator. It is the set of rows or values eligible to be counted.

## Count kinds

| Count kind | Required population declaration |
|---|---|
| `ROWS` | No counted field, distinct field, or group key; null rows remain included. |
| `NON_NULL_VALUES` | Exactly one counted field; null values are excluded. |
| `DISTINCT_NON_NULL_VALUES` | One or more distinct fields; null values are excluded. |
| `GROUPED_ROWS` | One or more group keys; null grouping behavior is explicit. |
| `UNRESOLVED` | The candidate abstains until count semantics are declared. |

Filtering is a separate axis. `FILTERED` requires an opaque predicate reference; `UNFILTERED` prohibits one. The validator never evaluates the predicate.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, count-kind, population, filter, null, disclosure, and local review-reference invariants are coherent. |
| `ABSTAIN` | Count kind, filter state, null posture, population basis, evidence scope, or disclosure remains unresolved or incomplete. |
| `DENY` | Count-kind fields, population basis, filter reference, public disclosure, canonicalization, or deterministic identity is contradictory. |
| `ERROR` | The candidate cannot be evaluated safely under the closed schema. |

These are validator outcomes only. They are not statistical findings, evidence decisions, policy decisions, review decisions, release states, runtime answers, or publication states.

## Directory Rules basis

Accepted Directory Rules place semantic meaning for an evidence-bound analytic disclosure under `contracts/evidence/`, machine shape under `schemas/`, synthetic cases under `fixtures/`, repository validation under `tools/`, executable conformance under `tests/`, CI orchestration under `.github/`, human source reconciliation under `docs/`, and authoring accountability under `data/receipts/generated/`.

The object is adjacent to `IndicatorDefinition` and `AnalyticOutputDisclosureAssessment` because it discloses how a derived count may be interpreted. It does not create a parallel metric registry, query library, evidence store, data lane, policy surface, release lane, or public API.

## Validation

```bash
python -m unittest tests.validators.evidence.test_validate_count_population_disclosure -v
python tools/validators/evidence/validate_count_population_disclosure.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and mutates no data, query, metric, evidence, policy, review, lifecycle, release, cache, deployment, or public artifact.
