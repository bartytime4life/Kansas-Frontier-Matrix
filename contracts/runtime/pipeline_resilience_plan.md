<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/pipeline-resilience-plan/v1
title: Pipeline Resilience Plan Contract
type: semantic-contract
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: public
related:
  - ../../schemas/contracts/v1/runtime/pipeline_resilience_request.schema.json
  - ../../schemas/contracts/v1/runtime/pipeline_resilience_plan.schema.json
  - ../../packages/pipelines-core/src/pipelines_core/pipeline_resilience.py
  - ../../scripts/plan_pipeline_resilience.py
  - ../../fixtures/contracts/v1/runtime/pipeline_resilience_plan/
  - ../../tests/packages/pipelines_core/test_pipeline_resilience.py
  - ../../docs/runbooks/pipeline-resilience.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, runtime, pipeline, resilience, trigger, retry, idempotency, backpressure, circuit-breaker, outbox, wal, dead-letter, kill-switch]
notes:
  - "Implements a planning-only, no-network decision kernel derived from KFM-P8-PROG-0001 through KFM-P8-PROG-0005."
  - "The plan does not mutate workflows, databases, queues, kill switches, lifecycle data, policy, release state, or publication state."
  - "Connector transport retry remains owned by connectors-core; this contract governs pipeline-step orchestration decisions."
[/KFM_META_BLOCK_V2] -->

# Pipeline Resilience Plan

A `PipelineResiliencePlan` converts one immutable pipeline execution context into deterministic, finite decisions for:

- trigger admission and environment routing;
- idempotency identity and retention expectations;
- bounded retry with explicit transient, rate-limited, deterministic, policy, quarantine, and operator-required classes;
- queue backpressure, canary isolation, and load shedding;
- circuit-breaker transitions;
- replay-safe event delivery through a transactional outbox or WAL;
- dead-letter replay review;
- new-start pause, emergency stop, and reviewed re-enablement.

This contract is the smallest dependency-closed implementation slice for the Pass 8 pipeline-resilience cards:

| Source idea | Contract realization |
|---|---|
| `KFM-P8-PROG-0001` | Trigger matrix, environment gate, authorization reference, concurrency group, secret scope, finite trigger decision. |
| `KFM-P8-PROG-0002` | Queue bounds, canary parity/isolation, load-shedding decision, circuit-breaker transition, observability requirements. |
| `KFM-P8-PROG-0003` | Canonical idempotency key, bounded retry budget, rate-limit distinction, deterministic caller-supplied jitter, attempt/terminal receipt requirements. |
| `KFM-P8-PROG-0004` | Transactional-outbox/WAL gate, consumer-idempotency gate, dead-letter reason/history fields, authorization and admission/policy rechecks before replay. |
| `KFM-P8-PROG-0005` | Auditable kill-switch state, distinct pause/emergency semantics, in-flight behavior, and reviewed re-enablement. |

All five source cards were proposal material. This contract therefore remains `draft` and `PROPOSED` until accepted through repository review.

## Authority and non-effects

The planner is side-effect-free. It has no authority to:

- fetch a source or activate a connector;
- create, update, cancel, or replay a workflow job;
- read or write a queue, database, transactional outbox, or WAL;
- read secrets or change secret scope;
- evaluate policy or create a `PolicyDecision`;
- flip a repository/environment variable or GitHub Actions control;
- mutate RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLETS, or PUBLISHED state;
- promote, release, deploy, or publish.

A valid plan is not a `RunReceipt`, `EvidenceBundle`, `ProofPack`, `PromotionDecision`, `ReleaseManifest`, rollback action, or publication event. It identifies which receipts and checks a governed executor would still need.

## Directory Rules basis

ADR-0029 adopts Directory Governance Standard v2.0.0 as KFM placement authority.

- `contracts/runtime/` owns semantic meaning for this runtime-facing decision object.
- `schemas/contracts/v1/runtime/` owns machine shape.
- `packages/pipelines-core/` owns reusable, source-agnostic pipeline planning logic.
- `scripts/` owns the operator-invoked, no-network planner CLI.
- `fixtures/contracts/v1/runtime/` and `tests/packages/pipelines_core/` prove deterministic behavior.
- `docs/runbooks/` owns operator procedure and recovery guidance.
- `data/receipts/generated/` records generated-artifact provenance for this implementation packet.

No new root or parallel schema, contract, policy, release, proof, or receipt authority is created.

## Request semantics

### Stable identity fields

| Field | Meaning |
|---|---|
| `pipeline_id` | Stable pipeline identity using a responsibility-safe slug. |
| `step_id` | Stable pipeline-step identity. |
| `contract_version` | Governing pipeline contract version. |
| `input_manifest` | Non-empty JSON object carrying stable normalized inputs and parameters. |

The planner computes:

```text
idempotency_key = sha256(canonical_json(
  pipeline_id,
  step_id,
  contract_version,
  trigger.type,
  trigger.environment,
  trigger.concurrency_group,
  input_manifest
))
```

Canonical JSON is UTF-8, key-sorted, whitespace-minimized, and rejects non-finite numbers. Queue depth, breaker state, retry attempt, and kill-switch state do not enter the idempotency key because they describe operational state rather than the logical work item. They do enter `spec_hash`, which binds the complete planning request.

The request supplies `idempotency_retention_seconds`. The planner does not create or retain keys; an executor must persist them longer than the applicable event-redelivery window.

### Trigger matrix

Supported trigger classes are:

```text
push
pull_request
schedule
workflow_dispatch
repository_dispatch
release
workflow_call
pipeline_handoff
external_webhook
```

Finite rules in v1:

1. `workflow_dispatch`, `repository_dispatch`, and `external_webhook` require an `authorization_ref`.
2. Every production target requires an `environment_gate_ref`.
3. `push` and `pull_request` cannot target production directly.
4. An external webhook cannot request `ENVIRONMENT_SCOPED` secrets.
5. The plan carries a concurrency group and finite secret-scope class but does not acquire secrets or enforce repository permissions.

These rules resolve a bounded first slice. Who may grant dispatch/repository-dispatch authority remains a governance decision outside this planner.

### Retry taxonomy

The request distinguishes:

| Error class | Planner behavior |
|---|---|
| `NONE` | No retry action. |
| `TRANSIENT` | Retry only within attempt and wall-clock budgets. |
| `RATE_LIMITED` | Retry within budgets; honor bounded `retry_after_seconds` when supplied. |
| `DETERMINISTIC` | Stop; never retry an unchanged deterministic failure. |
| `POLICY_DENIED` | Stop and deny; retry cannot override policy. |
| `QUARANTINE` | Route to quarantine; no retry. |
| `OPERATOR_REQUIRED` | Hold for an operator; no automatic retry. |

Backoff is exponential with bounded, caller-supplied deterministic jitter:

```text
base = min(base_delay * multiplier^(attempt_number - 1), max_delay)
factor = 1 + jitter_fraction * (2 * jitter_unit - 1)
delay = min(base * factor, max_delay)
```

The planner samples no randomness and reads no clock. A governed caller supplies elapsed time, `retry_after_seconds`, and `jitter_unit`.

This pipeline-step taxonomy is distinct from `packages/connectors-core` transport retry. Connector retry decides whether a transport observation may be attempted again. Pipeline resilience decides whether a governed orchestration step may start, retry, pause, quarantine, or require review.

### Backpressure and canaries

Queue input carries depth, oldest age, in-flight count, and partition class. Policy supplies finite limits.

- Within limits: `ACCEPT`.
- In-flight at the limit: `THROTTLE`.
- Queue depth or age beyond limits: `SHED` only when explicitly allowed; otherwise `HOLD`.
- A `CANARY` must use production-identical contracts, schemas, and policies, write to isolated outputs, and have no public side effects. Failure of any condition is `DENY`.

The planner does not choose domain-specific canary acceptance thresholds. Those remain `NEEDS VERIFICATION` and belong in domain/pipeline policy or accepted configuration.

### Circuit breaker

The circuit breaker uses `CLOSED`, `OPEN`, and `HALF_OPEN`.

- A closed breaker opens when consecutive failures reach the configured threshold.
- An open breaker remains open until the caller reports cooldown elapsed.
- After cooldown, the planner allows only a half-open probe.
- A successful probe closes the breaker.
- A failed probe reopens it.

The planner emits a circuit-breaker transition receipt requirement whenever state changes. It does not persist breaker state.

### Durable delivery and dead-letter replay

When a step emits an event, the plan requires:

- `TRANSACTIONAL_OUTBOX` or `WAL` durability;
- verified atomic commit between the business mutation and durable event record;
- verified consumer idempotency.

Missing proof causes `QUARANTINE`. The planner never permits a public consumer to read the outbox or WAL directly.

A dead-letter entry carries:

- stable event ID;
- reason code;
- attempt count;
- original and target contract versions;
- replay eligibility;
- replay authorization reference;
- current admission and policy recheck status.

Replay is allowed only when eligibility is `ELIGIBLE`, authorization exists, and current admission and policy checks have been rerun. A contract-version change is retained as an explicit reason code. The plan does not answer multi-region replication or physical outbox retention; those remain operational design questions.

### Kill switch

The kill-switch model separates:

| Mode | New starts | In-flight work |
|---|---|---|
| `RUNNING` | Allowed when other gates pass. | Continues. |
| `PAUSE_NEW_STARTS` | Paused. | Must continue; cancellation would require emergency mode. |
| `EMERGENCY_STOP` | Stopped. | Must use explicit `CANCEL`. |

Non-running modes require an activation receipt reference. Returning from a paused/emergency state to `RUNNING` requires a re-enable review reference. This v1 model produces a `kill_switch_state_receipt` requirement but does not itself generate a `RollbackReceipt`; whether that receipt is mandatory remains a governance decision.

## Plan decisions

Top-level decisions are finite:

| Decision | Meaning |
|---|---|
| `ALLOW_START` | A new step may start under the supplied context. |
| `ALLOW_RETRY` | The same idempotent work item may retry after the planned delay. |
| `ALLOW_REPLAY` | An eligible dead-letter event may be replayed after current checks and authorization. |
| `PAUSE` | Do not start/retry/replay now; queue, breaker, canary, or kill-switch state blocks progress. |
| `QUARANTINE` | Durability, consumer-idempotency, or explicit quarantine conditions are unresolved. |
| `DENY` | Trigger, policy, canary, delivery, or kill-switch conditions explicitly forbid the action. |
| `NO_ACTION` | The failure is terminal/non-retriable or no further action is appropriate. |
| `OPERATOR_REQUIRED` | A review, authorization, or manual remediation is required. |

The aggregate decision uses fail-closed precedence. Section decisions and reason codes remain visible so an operator can reconstruct why the top-level result was chosen.

## Required receipts and observability

The plan always requires a terminal receipt and conditionally requires:

- `attempt_receipt`;
- `backpressure_decision_receipt`;
- `circuit_breaker_transition_receipt`;
- `dead_letter_replay_receipt`;
- `kill_switch_state_receipt`.

The plan lists the minimum observability measurements expected from a governed executor:

```text
queue_depth
oldest_queue_age_seconds
retry_attempt_count
breaker_state
time_to_drain_seconds
```

These names are requirements, not emitted telemetry and not a new telemetry authority.

## Validation

Focused acceptance includes:

- Draft 2020-12 schema self-checks;
- exact fixture replay for allow-start, retry, replay, pause, and canary-deny states;
- canonicalization/key-order invariance;
- retry budget and rate-limit behavior;
- trigger authorization and production-routing denies;
- queue shedding/throttling;
- breaker transitions;
- outbox/WAL and consumer-idempotency quarantine;
- dead-letter authorization and current-check requirements;
- kill-switch activation/re-enable semantics;
- duplicate-key, non-finite-number, and invalid-shape CLI failures.

## Rollback

This is an additive, planning-only packet. Rollback is a revert that removes:

- this semantic contract;
- the two schemas;
- the planner module and CLI;
- fixtures and focused tests;
- the operator runbook;
- the generated receipt.

No data migration, queue drain, workflow reconfiguration, database rollback, public correction, or release reversal is required because this slice performs no side effects.

## Open verification backlog

- Decide the actual persistent idempotency store and retention per event source.
- Decide domain-specific queue, canary, and circuit-breaker thresholds.
- Decide authority roles for dispatch, emergency stop, replay, and re-enablement.
- Decide whether kill-switch activation must also emit a `RollbackReceipt`.
- Verify actual GitHub Actions adapter design before wiring repository/environment controls.
- Verify transactional-outbox/WAL implementation and multi-region behavior in the selected runtime/database.
- Decide whether replay uses original or current transformation code; this v1 planner requires current admission/policy checks and records original/target contract versions.
