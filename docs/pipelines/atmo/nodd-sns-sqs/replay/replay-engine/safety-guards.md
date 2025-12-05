---
title: "🛡️ KFM v11.2.3 — NODD Replay Engine Safety Guards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed safety, rate, and scope controls for the NODD WAL-driven replay engine in the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/replay-engine/safety-guards.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x replay-engine-guards compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/nodd-sns-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/nodd-sns-sqs-v1.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Replay Engine Safety Spec"
intent: "nodd-sns-sqs-replay-engine-safety-guards"
category: "Pipelines · Atmospheric · Replay · Engine"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
immutability_status: "version-pinned"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: false
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major NODD replay engine safety standard"

header_profile: "standard"
footer_profile: "standard"
---

# 🛡️ NODD Replay Engine Safety Guards  

`docs/pipelines/atmo/nodd-sns-sqs/replay/replay-engine/safety-guards.md`

This document defines the **safety, rate, and scope controls** that every NODD replay operation MUST obey.

It complements:

- Replay Engine overview: `README.md`  
- CLI spec: `cli-spec.md`  
- Integration notes: `integration-notes.md`  
- WAL specs: `../wal/README.md`, `../wal/wal-record-model.md`, `../wal/wal-state-machine.md`  
- Runbooks: `../runbooks/README.md`  

These guards are **non-optional** and MUST be enforced in:

- CLI (`nodd-replay`)  
- Any replay service or automation  
- All environments (`dev`, `stage`, `prod`)

⸻

## 🧭 1. Guarding Principles

All safety logic is built on four core principles:

1. **WAL-First & Deterministic**  
   - WAL is the **only** source of truth for replay eligibility and state.  
   - Replays MUST produce deterministic results given the same WAL slice and code.

2. **Scoped & Bounded**  
   - Every replay MUST have a **finite, explicit scope** (datasets, time windows, error classes).  
   - Volume and rate MUST be bounded by configurable limits.

3. **SLO-Respectful**  
   - Replays MUST NOT silently break queue-age or latency SLOs.  
   - If replay threatens SLOs, it must slow down, pause, or require human confirmation.

4. **Governance-Aligned**  
   - Replays MUST obey FAIR+CARE, sovereignty rules, and LangGraph governance gates.  
   - No replay is allowed to “skip” governance just because it is a repair operation.

⸻

## 🧱 2. Guard Categories

Safety guards are grouped into six categories:

1. **Scope Guards** — What can be replayed.  
2. **Volume & Batch Guards** — How much can be replayed at once.  
3. **Rate & Concurrency Guards** — How fast replays can run.  
4. **State & Attempts Guards** — How many times a record can be retried.  
5. **Environment & Kill-Switch Guards** — Where and when replays can run.  
6. **Governance & Lineage Guards** — How replays interact with ethics and provenance.

Every replay invocation MUST satisfy all applicable categories.

⸻

## 🎯 3. Scope Guards

Scope guards ensure **clear, auditable replay boundaries**.

### 3.1 Required Scope Dimensions

Each replay MUST specify:

- At least one **dataset** filter:
  - `--dataset` or `--dataset-in` (or equivalent in selection spec).  
- At least one **time dimension**:
  - `event_time` range, OR  
  - `created_at` range, OR  
  - `time_range_start` / `time_range_end` overlap.  
- At least one **status or error-class constraint**:
  - Typically `status = "failed"` for failed-only mode.  
  - Optionally restricted by `last_error_code`.

### 3.2 Forbidden “Global” Scopes

The following are **forbidden** in `prod` without explicit Council approval:

- No dataset filter (e.g., replaying **all** datasets).  
- No time filter (e.g., unbounded historical range).  
- No status filter (e.g., targeting all statuses simultaneously).  

CLI MUST reject such invocations unless:

- An override flag (for example, `--allow-global-scope`) is set, AND  
- The environment is non-prod OR a governance-approved configuration is present.

### 3.3 Selection Spec Validation

Selection specs (YAML/JSON) MUST:

- Include a `version` field compatible with current engine version.  
- Encode all scope dimensions explicitly.  
- Fail validation if dimensions are missing or contradict guards (e.g., empty dataset list in `prod`).

⸻

## 📦 4. Volume & Batch Guards

Volume and batch guards prevent **oversized replay waves** from overwhelming the system.

### 4.1 Maximum Selection Size

Configurable limit:

- `max_selection_records` per replay invocation.  

Behavior:

- If a selection yields more than this limit:
  - CLI MUST:
    - Fail with a guardrail error, OR  
    - Require an explicit `--force-split` / `--shard` pattern that breaks work into multiple runs.

### 4.2 Batch Size Limits

Each active replay **run** MUST enforce:

- `max_batch_size` (records per batch).  
- Optional `max_batch_volume` (estimated data volume, if available).

Recommended pattern:

- `batch_size` tuned such that:
  - Each batch is processable within SQS visibility timeout + safety margin.  
  - Workers and WAL backends are not saturated.

### 4.3 Bounded Number of Batches

Replay invocations MUST accept:

- `--max-batches` flag (or config equivalent).  

Guard:

- If replay would exceed `max_baches` for the selection:
  - Engine MUST stop or refuse to start until `max_batches` is raised deliberately.

⸻

## ⏱ 5. Rate & Concurrency Guards

Rate and concurrency guards control the **tempo** of replays.

### 5.1 Throughput Limits

Engine MUST support:

- `max_records_per_second` and/or `max_batches_per_minute` limits.  

Behavior:

- If calculated replay rate would exceed these:
  - Engine MUST self-throttle (sleep/delay between batches).  
  - Or refuse to start with a clear guardrail violation.

### 5.2 Queue & Latency Awareness

Replay engine MUST:

- Periodically sample:
  - Primary queue depth and age.  
  - Ingest latency P90.  

Guard:

- If queue-age or latency is near SLO thresholds:
  - Engine SHOULD:
    - Slow down, OR  
    - Pause and emit telemetry indicating backoff.  

Integration with `delayed-queue-runbook.md`:

- If replay pushes system into delayed-queue territory:
  - On-call MUST follow delayed-queue runbook for remediation.

### 5.3 Worker Concurrency Limits

Engine MUST respect:

- Per-environment and per-dataset concurrency caps.  

Example:

- No more than **N** replay batches in-flight per dataset.  
- No more than **M** concurrent replay batches overall.

These caps MUST be configurable via:

- Config file (`--config`), AND/OR  
- Environment-level infra configuration.

⸻

## 🔁 6. State & Attempts Guards

State and attempts guards preserve the **WAL state machine** and prevent infinite retry loops.

### 6.1 Max Attempts Enforcement

Each WAL record MUST have:

- A governed `max_attempts` (global or per-dataset).  

Guard:

- Engine MUST NOT replay records where `attempts ≥ max_attempts`.  
- CLI and services MUST:
  - Report how many candidates were skipped due to attempts limits.  
  - Surface this in telemetry and runbook-facing summaries.

### 6.2 Legal Status Transitions Only

All transitions MUST obey `wal-state-machine.md`. In particular:

- Failed-only replay:
  - Allowed: `failed → pending → in_progress → succeeded/failed/quarantined`.  
  - Forbidden: `succeeded → pending` (unless special repair-and-replace mode under explicit governance).

Guard:

- Engine MUST validate each intended transition and fail the batch if any illegal transition is encountered.

### 6.3 Concurrency Safety

Engine MUST:

- Use optimistic concurrency or locking against WAL backend, so that:
  - Only one worker/engine instance can move a given `wal_id` from `failed → pending` at a time.  

If a conflict is detected:

- Engine MUST retry with fresh WAL data or skip affected records, logging a conflict event.

⸻

## 🧬 7. Environment & Kill-Switch Guards

Environment and kill-switch guards prevent replay misuse across environments.

### 7.1 Environment-Specific Limits

Per `env` (`dev`, `stage`, `prod`), defaults SHOULD differ:

- `dev`: very small batch sizes and strict limits, safe for experimentation.  
- `stage`: moderate limits, used for realistic testing.  
- `prod`: carefully tuned limits, with additional confirmations and guardrails.

Engine MUST:

- Read environment from `--env` or `KFM_ENV`.  
- Apply **stricter defaults** in `prod` unless configuration expressly loosens them (with governance approval).

### 7.2 Dataset Kill-Switches

Replay engine MUST respect dataset-level kill-switch flags:

- If a dataset is under kill-switch (ingest paused):

  - For new replays:
    - Engine MUST NOT enqueue replay work for that dataset.  
  - For already in-flight replays:
    - Behavior must be documented; preferred pattern:
      - Allow in-flight batches to finish while blocking new ones.

Kill-switch state MUST be visible in:

- Telemetry  
- Incident/runbook guidance  

and MUST be logged during replay runs.

### 7.3 Non-Prod Routing

In non-prod environments:

- All SQS queue and WAL endpoints MUST point to non-prod infrastructure.  
- Engine MUST fail fast if misconfigured to target prod queues from non-prod `env` values.

⸻

## 🧬 8. Governance, Ethics & Sovereignty Guards

Replay MUST obey KFM governance:

- Root governance: `${governance_ref}`  
- FAIR/CARE: `${ethics_ref}`  
- Sovereignty: `${sovereignty_policy}`  

### 8.1 Governance Gate Equivalence

Replay ingest MUST:

- Pass through the same LangGraph governance gates as hot-path ingestion.  
- Emit the same provenance and governance audit events.

No “fast-path replay” is allowed that bypasses:

- Sensitivity labels  
- Sovereignty controls  
- Redaction/generalization logic

### 8.2 Sensitive Data Handling

During replay:

- Logs MUST NOT dump full payloads or sensitive fields.  
- Any validation-error payload sampling MUST:
  - Obey redaction practices.  
  - Apply generalization for sensitive spatial data where required.

### 8.3 Policy-Aware Replay Reasons

`replay_reason` MUST be set to a controlled vocabulary, such as:

- `"dlq-drain"`  
- `"incident"`  
- `"backfill"`  
- `"test"` (non-prod only)

Governance reviews MAY use this field to:

- Audit replay patterns.  
- Investigate whether replay usage aligns with policy.

⸻

## 📡 9. Telemetry & Guardrail Observability

Safety guards are only useful if observable.

Replay engine MUST emit metrics and logs whenever a guard:

- Prevents a replay  
- Truncates a selection  
- Throttles throughput  

### 9.1 Guardrail Metrics

Examples (names indicative, not exhaustive):

- `nodd_sns.replay_guardrail_violations_total{guard_type,env}`  
- `nodd_sns.replay_throttled_batches_total{reason,env}`  
- `nodd_sns.replay_skipped_records_total{reason,env}`

Guard types might include:

- `scope_too_broad`  
- `selection_too_large`  
- `attempts_exceeded`  
- `kill_switch_active`  
- `env_mismatch`  
- `slo_risk`

### 9.2 Logging

Structured logs SHOULD include:

- Guard name  
- Selection spec hash / ID  
- Short, redacted explanation  
- Suggested next steps (e.g., “reduce batch size”, “narrow time window”).

⸻

## 🧪 10. CI & Validation of Guards

CI MUST validate that:

- Guard enforcement logic is covered by tests.  
- Known bad invocations (missing scope, illegal transitions, over-limit batches) are rejected.  
- Non-prod defaults are stricter or equal to prod for high-risk operations.

Minimum tests:

- Scope guard tests:
  - Verify that missing dataset/time/status filters are rejected in `prod`.  
- Volume/batch guard tests:
  - Confirm `max_selection_records`, `max_batch_size`, and `max_batches` are respected.  
- Attempts/state tests:
  - Verify that records with `attempts ≥ max_attempts` are never replayed.  
- Kill-switch tests:
  - Confirm replay is blocked or altered when kill-switch flags are active.  
- Governance tests:
  - Confirm that governance-hard-fail error codes lead to correct terminal states and are not silently retried.

Any change to:

- Guard names  
- Limit semantics  
- Default thresholds  

MUST:

- Update this document.  
- Update CLI help and integration docs where relevant.  
- Pass CI guard tests.

⸻

## 📘 11. Version History

| Version  | Date       | Notes                                                                                                                  |
|---------:|------------|------------------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD replay engine safety guards; defined scope, volume, rate, state, environment, and governance guardrails. |

---

<div align="center">

🛡️ NODD Replay Engine Safety Guards · KFM v11.2.3  

Scoped · Bounded · Governance-Enforced  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Replay Engine](README.md) ·  
[🧾 CLI Spec](cli-spec.md) ·  
[🔗 Integration Notes](integration-notes.md) ·  
[📓 WAL Spec](../wal/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
