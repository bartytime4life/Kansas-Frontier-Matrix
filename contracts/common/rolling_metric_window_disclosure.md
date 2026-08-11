<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/rolling-metric-window-disclosure
title: RollingMetricWindowDisclosure Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Common contract steward · Analytics steward · Evidence steward · Temporal steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; common; analytics; rolling-metric; window-frame; disclosure
responsibility: Define fixture-only partition, ordering, frame, time, missing-data, revision, and parity disclosure semantics for a rolling metric without computing a metric or creating evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive disclosure; UNKNOWN consumer adoption; NEEDS VERIFICATION cross-engine behavior, human review, and hosted exact-head CI"
related:
  - ./aggregate_statistic.md
  - ../evidence/indicator_definition.md
  - ../evidence/measurement_scale_operation_assessment.md
  - ../release/release_manifest.md
  - ../../schemas/contracts/v1/common/rolling_metric_window_disclosure.schema.json
  - ../../fixtures/contracts/v1/common/rolling_metric_window_disclosure/cases.json
  - ../../tools/validators/validate_rolling_metric_window_disclosure.py
  - ../../tests/validators/test_validate_rolling_metric_window_disclosure.py
  - ../../docs/intake/exploratory/pass-18-rolling-metric-window-disclosure-source-map.md
[/KFM_META_BLOCK_V2] -->

# RollingMetricWindowDisclosure Candidate

`RollingMetricWindowDisclosureCandidate` is an additive, fixture-only profile for recording how one moving average, rolling rank, or trend indicator partitions and orders inputs, selects a frame, handles missing observations, and responds to revisions.

It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-479`: rolling public metrics should record partition, ordering, and frame definitions so they can be reproduced and audited.

## Boundary

A validator `PASS` means only that the candidate is internally coherent under this closed profile. It does not inspect source values, execute SQL, calculate a metric, prove cross-engine equality, resolve a claim or evidence reference, assess scientific fitness, decide policy or review, promote, release, deploy, publish, or authorize public use.

The profile binds an existing metric or claim by reference. It does not modify `AggregateStatistic`, `IndicatorDefinition`, or `ReleaseManifest` and cannot stand in for any of them.

## Reproducibility declarations

| Section | Required disclosure |
|---|---|
| `partition` | Whether the window is global or keyed and the exact partition fields. |
| `ordering` | Ordered fields, direction, null treatment, semantic role, and whether uniqueness is guaranteed. |
| `frame` | `ROWS`, `RANGE`, or `GROUPS`; inclusive start and end bounds; exclusion; and an offset unit where a ranged offset needs one. |
| `time_definition` | The window-time field, its temporal meaning, time zone, calendar, and local resolution state. |
| `missing_data` | Treatment, any method reference, minimum observations, and partial-window behavior. |
| `revision_behavior` | Late-arrival behavior plus correction and rollback references. |
| `engine_parity` | One or more engine profiles and whether parity is single-engine, synthetically declared, unresolved, or mismatched. |
| `disclosure` | Human-readable partition, ordering, frame, and missing-data labels plus review and release-manifest references for a public candidate. |

Ordering is sequence-sensitive. When the declared order is not unique, at least one explicit `TIE_BREAKER` is required. The first ordering field must be `WINDOW_TIME` and must match the time-definition field. These local rules prevent silent tie instability; they do not prove source uniqueness.

## Frame semantics

Bounds are inclusive in this v1 profile. Offset bounds require a positive integer. Non-offset bounds must carry no offset. `RANGE` offsets require an explicit unit reference; `ROWS` and `GROUPS` offsets must not pretend to have a measurement unit.

The validator maps each bound onto a finite ordering axis and rejects a start later than its end. It does not claim that every database expresses or executes the frame identically. Multi-engine use therefore requires a synthetic parity declaration and fixture reference; `UNRESOLVED` abstains and `MISMATCH` denies.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, partition, ordering, frame, time, missing-data, revision, parity, and disclosure declarations are coherent. |
| `ABSTAIN` | Claim scope, time definition, or cross-engine parity remains unresolved. |
| `DENY` | A deterministic identity, partition, ordering, frame, missing-data, parity, public-review, or canonicalization invariant fails. |
| `ERROR` | The candidate cannot be evaluated safely under the closed schema. |

These outcomes are validation results only, not analytical, evidence, policy, review, release, or publication decisions.

## Directory Rules basis

Reusable rolling-metric disclosure meaning is adjacent to `AggregateStatistic` under `contracts/common/`. Machine shape, synthetic cases, repository validation, executable checks, CI orchestration, source reconciliation, and generated authoring accountability remain in their established responsibility roots.

No analytics engine, metric store, evidence lane, policy lane, release path, database adapter, or public surface is created. The profile composes current authorities by reference and introduces no parallel authority.

## Validation

```bash
python -m unittest tests.validators.test_validate_rolling_metric_window_disclosure -v
python tools/validators/validate_rolling_metric_window_disclosure.py --fixtures
```

## Rollback

Revert the additive packet. It has no consumer and computes, changes, releases, deploys, or publishes nothing.
