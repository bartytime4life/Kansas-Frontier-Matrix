<!-- [KFM_META_BLOCK_V2]
doc_id: kfm.runbook.reliability.trigger_retry_matrix.v1
title: Reliability Trigger/Retry Matrix
type: runbook
version: v1
status: active
owners: kfm-maintainers
created: 2026-04-28
updated: 2026-04-28
policy_label: safe_retries
related:
  - docs/runbooks/README.md
  - docs/runbooks/stale_projection.md
[/KFM_META_BLOCK_V2] -->

# Reliability Trigger/Retry Matrix

Use this matrix to choose retry behavior by trigger type.

| Trigger type | Default retry posture | Max attempts | Backoff | Terminal action |
|---|---|---:|---|---|
| Manual operator action | No automatic retry | 1 | none | Escalate to operator |
| Scheduled batch | Safe automatic retry | 3 | exponential | Queue for next schedule + alert |
| Event/webhook (idempotent) | Automatic retry with idempotency key | 5 | exponential + jitter | Dead-letter queue |
| Event/webhook (non-idempotent) | Guarded retry only after validation | 2 | fixed | Quarantine + manual review |
| User synchronous request | Minimal retry to protect latency | 1 | short fixed | Return governed error envelope |

## Rules

1. Never retry non-idempotent writes blindly.
2. Prefer jittered exponential backoff for async workers.
3. Emit retry telemetry for every attempt.
4. Escalate once attempts are exhausted; do not loop indefinitely.
