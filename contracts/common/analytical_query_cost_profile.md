<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/analytical-query-cost-profile
title: AnalyticalQueryCostProfile Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Common contract steward · Analytics steward · Runtime steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; common; analytics; query-cost; reproducibility; disclosure
responsibility: Define fixture-only query-plan identity, input-size, index-assumption, resource-budget, observation, and disclosure semantics without storing SQL or plan text, running a query, authenticating telemetry, or creating policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card and current-repository gap; PROPOSED inactive profile; UNKNOWN engine portability and consumer adoption; NEEDS VERIFICATION analytics, runtime, security, and validation review plus hosted exact-head CI"
related:
  - ./aggregate_grouping_disclosure.md
  - ./rolling_metric_window_disclosure.md
  - ../evidence/analytic_output_disclosure_assessment.md
  - ../governance/query_run_record.md
  - ../../schemas/contracts/v1/common/analytical_query_cost_profile.schema.json
  - ../../fixtures/contracts/v1/common/analytical_query_cost_profile/cases.json
  - ../../tools/validators/validate_analytical_query_cost_profile.py
  - ../../tests/validators/test_validate_analytical_query_cost_profile.py
  - ../../docs/intake/exploratory/pass-18-analytical-query-cost-profile-source-map.md
[/KFM_META_BLOCK_V2] -->

# AnalyticalQueryCostProfile Candidate

`AnalyticalQueryCostProfileCandidate` is an additive disclosure for the
performance assumptions of one analytical query. It implements the smallest
reviewable portion of supplied Pass 18 card `KFM-P18-INV-406`.

## Boundary

A validator `PASS` means only that one synthetic declaration coherently binds
an opaque query identity to an engine profile, input-size assumptions, safe
query-plan identity, logical index assumptions, resource budgets, a measured
observation, and review disclosure. It does not execute SQL, inspect a plan,
authenticate a run receipt or telemetry record, prove an index exists, approve
a budget, decide policy or review, promote, release, deploy, publish, or
authorize public use.

The closed schema contains no raw SQL, bound values, connection strings,
credentials, plan text, table paths, or unrestricted engine metadata. Plan and
query bytes are represented only by opaque references and SHA-256 digests.

## Portable disclosure surface

| Section | Required declaration |
|---|---|
| `engine` | Engine kind, opaque profile reference, and portability posture. |
| `input_scope` | Dataset references, size basis, estimated rows, and estimated bytes. |
| `plan_capture` | Capture state, format class, digest, safe parameter names, and fixed-false raw-content flags. |
| `index_assumptions` | Logical index roles, fields, access kind, and whether each assumption is required for the budget. |
| `budget` | Optional duration, row-read, byte-read, and peak-memory ceilings plus a resource-only or referenced billing posture. |
| `observation` | Measured values, opaque run/telemetry references, and a derived within-budget or exceeded result. |
| `disclosure` | Intended use, bounded summary, and review references. |

The v1 profile intentionally uses resource counters rather than vendor prices.
A billing estimate is represented only by an opaque billing-profile reference.
This keeps the carrier portable while the source card's cross-engine question
remains open.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, assumptions, budget, measurement, result, and disclosure are coherent. |
| `ABSTAIN` | Engine, input, plan, index, cost, observation, or disclosure posture remains unresolved. |
| `DENY` | A declared assumption is contradictory, an observed limit is exceeded, a result is false, or a public-candidate disclosure is incomplete. |
| `ERROR` | Input cannot be evaluated safely, or the record declares an execution error. |

These are profile-validation outcomes, not query, evidence, policy, review,
release, or publication decisions.

## Directory Rules basis

The profile is a small cross-domain disclosure value object, adjacent to the
existing aggregate-grouping and rolling-window disclosures under
`contracts/common/`. Machine shape, synthetic replay, repository validation,
executable conformance, read-only orchestration, source reconciliation, and
authoring accountability remain in their established responsibility roots.

No query engine, analytics store, plan store, telemetry store, budget registry,
policy surface, release lane, public API, or publication path is introduced.

## Validation and rollback

```bash
python -m unittest tests.validators.test_validate_analytical_query_cost_profile -v
python tools/validators/validate_analytical_query_cost_profile.py --fixtures
```

Rollback is one additive commit revert. The profile has no runtime consumer and
creates no live query, telemetry, policy, review, release, deployment, cache, or
public state.
