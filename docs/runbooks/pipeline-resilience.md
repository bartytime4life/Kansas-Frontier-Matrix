<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://runbook/pipeline-resilience/v1
title: Pipeline Resilience Operator Runbook
type: runbook
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal-operations-guidance
related:
  - ../../contracts/runtime/pipeline_resilience_plan.md
  - ../../schemas/contracts/v1/runtime/pipeline_resilience_request.schema.json
  - ../../schemas/contracts/v1/runtime/pipeline_resilience_plan.schema.json
  - ../../packages/pipelines-core/src/pipelines_core/pipeline_resilience.py
  - ../../scripts/plan_pipeline_resilience.py
  - ../../fixtures/contracts/v1/runtime/pipeline_resilience_plan/
  - ../../tests/packages/pipelines_core/test_pipeline_resilience.py
tags: [kfm, runbook, pipelines, resilience, retry, backpressure, circuit-breaker, dead-letter, kill-switch]
notes:
  - "This runbook operates the planning-only decision kernel. It does not authorize a production toggle, replay, source activation, release, deployment, or publication."
  - "Actual actor roles, GitHub Actions wiring, queue/database adapters, and production thresholds remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

# Pipeline Resilience Operator Runbook

Use this runbook to evaluate a pipeline execution context before a governed executor starts, retries, replays, drains, pauses, or stops work.

The current implementation is a deterministic **planner only**. It does not connect to GitHub Actions, a queue, a database, an outbox, a WAL, a policy engine, secrets, or public delivery. Any real action requires a separately reviewed adapter and the appropriate authority.

## Preconditions

Before relying on a plan, confirm:

1. The request schema and planner version are the versions expected by the pipeline.
2. `pipeline_id`, `step_id`, `contract_version`, and `input_manifest` describe the intended logical work.
3. Trigger authorization and environment-gate references are current.
4. Queue and breaker observations come from the intended runtime and are not stale.
5. Outbox/WAL atomicity and consumer idempotency claims have supporting runtime evidence.
6. Dead-letter replay eligibility, authorization, admission recheck, and policy recheck are current.
7. Kill-switch receipt/review references resolve to auditable records.
8. No public client or downstream consumer reads canonical/internal queue, outbox, WAL, or dead-letter stores directly.

## Run the planner

```bash
python scripts/plan_pipeline_resilience.py \
  fixtures/contracts/v1/runtime/pipeline_resilience_plan/valid/allow_start.request.json
```

A valid request returns a JSON envelope with:

- `outcome: ANSWER`;
- a finite `plan.decision`;
- component decisions and reason codes;
- deterministic `spec_hash` and `idempotency_key`;
- required receipt classes;
- all authority flags set to `false`.

An invalid request returns:

- `DENY` for schema or semantic invalidity;
- `ERROR` for unreadable, duplicate-key, non-UTF-8, oversized, symlink, or malformed JSON input.

The CLI exit code is `0` only for a valid plan. A valid plan may itself say `DENY`, `PAUSE`, `QUARANTINE`, or `OPERATOR_REQUIRED`; that is a successful fail-closed planning result, not a CLI error.

## Decision response matrix

| Plan decision | Operator action |
|---|---|
| `ALLOW_START` | Confirm executor authority, then start the same idempotent work item. |
| `ALLOW_RETRY` | Wait at least `retry.delay_seconds`; reuse `idempotency_key`; emit an attempt receipt. |
| `ALLOW_REPLAY` | Confirm replay authorization and current checks; replay exactly the referenced event; emit a replay receipt. |
| `PAUSE` | Start no new work. Preserve queued/in-flight state according to the component reason. |
| `QUARANTINE` | Move the candidate to the governed quarantine path through an authorized executor; record the unresolved durability/policy reason. |
| `DENY` | Do not start, retry, or replay. Escalate only through the owning policy/governance path. |
| `NO_ACTION` | Record terminal outcome; do not retry unchanged deterministic or exhausted work. |
| `OPERATOR_REQUIRED` | Resolve the named authorization, review, admission, policy, or capacity requirement and re-plan. |

## Retry procedure

1. Confirm `retry.classification` is `TRANSIENT` or `RATE_LIMITED`.
2. Confirm the plan is still within max-attempt and wall-clock budgets.
3. Reuse the exact `idempotency_key`; do not generate a new logical work item.
4. Wait the planned delay.
5. For `RATE_LIMITED`, verify whether the source supplied a trusted `Retry-After` value and that the planner bounded it.
6. Emit an attempt receipt with attempt number, elapsed time, classification, delay, and source/runtime evidence.
7. Re-plan after the attempt. Never retry deterministic validation, policy denial, quarantine, or operator-required outcomes without changing the governing condition.

## Backpressure and canary procedure

### Queue pressure

- `THROTTLE`: stop admitting work until in-flight count falls below the limit.
- `HOLD`: keep the item queued; do not discard it.
- `SHED`: shed only the class explicitly allowed by accepted policy; record what was shed and why.
- Never treat a shed item as successfully processed or published.

Record queue depth, oldest queue age, in-flight count, and estimated time to drain.

### Canary

Before a canary starts:

1. Contracts, schemas, and policies must match the production versions.
2. Outputs must be isolated.
3. Public side effects must be disabled.
4. The canary must use the same validation and receipt shapes as the full run.
5. Acceptance thresholds must be supplied by the owning domain/pipeline policy; this planner does not invent them.

A canary failure does not authorize full-batch replay or public output.

## Circuit-breaker procedure

| Current/next state | Procedure |
|---|---|
| `CLOSED -> OPEN` | Stop new calls to the protected dependency; emit transition receipt; investigate failure threshold. |
| `OPEN -> OPEN` | Continue pause; do not probe before cooldown. |
| `OPEN -> HALF_OPEN` | Run exactly the bounded probe permitted by the owning adapter. |
| `HALF_OPEN -> CLOSED` | Resume gradually; monitor queue and retry counts. |
| `HALF_OPEN -> OPEN` | Stop again; preserve failure evidence and receipt. |

The planner does not store breaker state. The runtime adapter must persist it and prevent concurrent writers from racing the transition.

## Dead-letter replay procedure

1. Resolve the original event ID, reason code, attempt history, and original contract version.
2. Confirm `replay_eligibility` is `ELIGIBLE`.
3. Obtain a replay authorization reference.
4. Re-run current source admission and policy checks.
5. Record the target contract version.
6. Run the planner and require `ALLOW_REPLAY`.
7. Replay idempotently through the governed consumer, never by editing the dead-letter record in place.
8. Emit `dead_letter_replay_receipt` with original/target contract versions and the result.
9. On failure, append a new attempt/result; do not erase prior history.

`REVIEW_REQUIRED` and `INELIGIBLE` remain held/denied until the owning authority changes the record.

## Kill-switch procedure

### Pause new starts

Use `PAUSE_NEW_STARTS` for bounded operational recovery when in-flight work is safe to finish.

1. Create an activation receipt with reason, scope, affected job classes, and expected review time.
2. Set in-flight policy to `CONTINUE`.
3. Re-plan and require `PAUSE`.
4. Verify no new work starts.
5. Verify existing work continues and receipts remain available.
6. Monitor queue growth and time to drain.

### Emergency stop

Use `EMERGENCY_STOP` only when continuing in-flight work is unsafe.

1. Create an activation receipt identifying the emergency basis and scope.
2. Set in-flight policy to `CANCEL`.
3. Re-plan and require `PAUSE` with `STOP_ALL`.
4. Cancel only through an authorized adapter.
5. Preserve partial outputs in WORK/QUARANTINE; do not mark them complete.
6. Record cancellation outcomes and any correction/rollback obligations.

### Re-enable

1. Resolve the incident or capacity problem.
2. Obtain a separate re-enable review reference.
3. Confirm backlog ordering, idempotency retention, source freshness, and policy state.
4. Re-plan with previous paused/emergency mode and current `RUNNING`.
5. Require `ALLOW_START`, `ALLOW_RETRY`, or another expected finite result.
6. Resume with a canary or bounded concurrency where appropriate.
7. Monitor queue depth, retry count, breaker state, and time to drain.

A missing re-enable review is `DENY`.

## Verification commands

Focused tests:

```bash
python -m pytest -q tests/packages/pipelines_core/test_pipeline_resilience.py
```

Bytecode compilation:

```bash
python -m py_compile \
  packages/pipelines-core/src/pipelines_core/pipeline_resilience.py \
  scripts/plan_pipeline_resilience.py \
  tests/packages/pipelines_core/test_pipeline_resilience.py
```

Schema check:

```bash
python - <<'PY'
import json
from pathlib import Path
from jsonschema import Draft202012Validator

for path in (
    Path("schemas/contracts/v1/runtime/pipeline_resilience_request.schema.json"),
    Path("schemas/contracts/v1/runtime/pipeline_resilience_plan.schema.json"),
):
    Draft202012Validator.check_schema(json.loads(path.read_text()))
    print("PASS", path)
PY
```

## Failure handling

- Planner/schema mismatch: stop and treat as `ERROR`; do not fall back to permissive execution.
- Missing authorization/review reference: `DENY` or `OPERATOR_REQUIRED`.
- Missing outbox/WAL atomicity or consumer idempotency evidence: `QUARANTINE`.
- Stale queue/breaker observations: refresh observations and re-plan.
- Lost idempotency record: do not guess; hold or quarantine until duplication risk is bounded.
- Receipt emission failure: stop before promotion/release and preserve the failed run context.
- Adapter behavior diverges from the plan: disable the adapter and investigate; the planner does not authorize a workaround.

## Rollback

This planning slice has no runtime side effects. Repository rollback is a revert of the additive contract, schemas, planner, CLI, fixtures, tests, runbook, and generated receipt.

For a future operational adapter, rollback must additionally:

- pause new starts;
- stop or safely finish in-flight work according to the active mode;
- preserve outbox/WAL/dead-letter history;
- restore the prior adapter/configuration version;
- re-run validation;
- drain backlog through idempotent execution;
- emit rollback/correction receipts where public or release state was affected.

## Open operational decisions

The following remain `NEEDS VERIFICATION` before production wiring:

- exact GitHub Actions control surface and actor permissions;
- source/domain-specific retry and canary thresholds;
- idempotency-store technology and retention;
- queue and breaker state storage;
- transactional-outbox or WAL implementation;
- multi-region replication behavior;
- actual replay authority and review roles;
- whether kill-switch activation also requires a `RollbackReceipt`;
- telemetry backend and cardinality policy.
