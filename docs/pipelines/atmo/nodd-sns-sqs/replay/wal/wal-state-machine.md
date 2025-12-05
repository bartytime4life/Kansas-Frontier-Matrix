---
title: "📓 KFM v11.2.3 — NODD WAL State Machine (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Formal state machine, transition rules, and edge-case handling for the NODD Write-Ahead Log (WAL) in the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/wal/wal-state-machine.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x wal-contract compatible"
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

doc_kind: "Replay / WAL State Machine"
intent: "nodd-sns-sqs-wal-state-machine"
category: "Pipelines · Atmospheric · Replay · WAL"

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
sunset_policy: "Superseded by next major NODD WAL contract"
header_profile: "standard"
footer_profile: "standard"
---

# 📓 NODD WAL State Machine  

`docs/pipelines/atmo/nodd-sns-sqs/replay/wal/wal-state-machine.md`

Formal definition of the **Write-Ahead Log (WAL) state machine** for the NOAA NODD SNS → SQS ingestion pipeline.

This document:

- Defines the **allowed values of `status`** and their semantics.  
- Specifies **legal transitions**, triggers, and failure handling.  
- Describes how the WAL state machine integrates with **SQS semantics, operators, and replay tools**.  
- Establishes invariants that CI and runtime enforcement MUST uphold.

It refines the WAL contract in `README.md` and the record model in `wal-record-model.md`.

⸻

## 🧭 1. State Machine Scope

The WAL state machine governs the field:

- `status` (on the canonical WAL record)

and its evolution over time for a single ingest unit.

The machine is:

- **Per-record**: each `wal_id` has exactly one `status` at any given time.  
- **Global**: rules apply regardless of dataset or queue, unless a governed exception is declared.  
- **Authoritative**: other systems (SQS, STAC, provenance) may influence transitions but do not override them.

The machine is designed to:

- Provide **deterministic replay semantics**.  
- Distinguish between **recoverable failures** and **terminal outcomes**.  
- Allow robust **incident forensics and lineage analysis**.

⸻

## 🧱 2. State Set & Roles

Allowed values of `status`:

1. `pending`  
2. `in_progress`  
3. `succeeded`  
4. `failed`  
5. `quarantined`

Each state has a clear role.

2.1 `pending`  

- Meaning:  
  WAL record exists; work is **eligible** but not currently being processed.  
- Typical situations:  
  - New unit discovered from SQS message.  
  - Record has been reset for replay, awaiting processing.  
- Worker expectations:  
  - Workers may claim `pending` records and move them to `in_progress`.

2.2 `in_progress`  

- Meaning:  
  A worker is actively processing the ingest unit.  
- Lifetime:  
  - Short-lived; bounded by SQS visibility timeout + safety margin.  
- Worker expectations:  
  - Only **one** worker may hold `in_progress` at a time (enforced by optimistic concurrency or locking).  
- Safety:  
  - If the worker crashes or visibility expires, another worker may reattempt, but MUST respect WAL invariants.

2.3 `succeeded`  

- Meaning:  
  Ingest is **fully complete** from a reliability standpoint.  
- Requirements (baseline policy):  
  - `stac_status ∈ {"created","updated","no-op"}`.  
  - `provenance_status ∈ {"ok","partial"}` (exact policy defined in WAL README).  
- Replay expectations:  
  - No further automatic replays; only possible under explicit, governed migration.

2.4 `failed`  

- Meaning:  
  Ingest attempt **did not complete successfully** and is eligible for retry or replay.  
- Typical causes:  
  - Validation errors.  
  - Governance hard-fails.  
  - IO/storage errors.  
- Replay expectations:  
  - Replay tools may transition `failed → pending` subject to policy and retry limits.

2.5 `quarantined`  

- Meaning:  
  Record is **isolated** for manual inspection or long-term hold.  
- Typical causes:  
  - Repeated failures beyond retry budget.  
  - Irreconcilable governance issues (e.g., sensitive content flags).  
- Replay expectations:  
  - No automatic replays; only manual, governed interventions may move it again (if allowed).

⸻

## 🔄 3. Allowed Transitions (Logical Model)

Legal transitions for `status`:

- `null` → `pending`  
- `pending` → `in_progress`  
- `in_progress` → `succeeded`  
- `in_progress` → `failed`  
- `failed` → `pending`  
- `pending` → `quarantined`  
- `failed` → `quarantined`

Constraints:

- `succeeded` and `quarantined` are **terminal** in normal operation.  
- There is no direct `succeeded → failed` or `succeeded → pending` in routine flows.  
- Any transition not listed above is **illegal** and MUST be rejected by validation logic.

⸻

## 🧩 4. Transition Triggers & Preconditions

4.1 `null` → `pending` (Record Creation)

Trigger:

- New ingest unit discovered from SQS, and no existing WAL record for its `(dataset, object_uri, time_range_start)` (or equivalent key).

Preconditions:

- No WAL record with same logical identity.  
- WAL record created with:
  - `status = "pending"`.  
  - `attempts = 0`.  
  - `created_at = updated_at = now()`.  

4.2 `pending` → `in_progress` (Worker Claim)

Trigger:

- Worker decides to process a WAL record / associated SQS message.

Preconditions:

- Current `status = "pending"`.  
- Worker acquires lock or passes optimistic concurrency check (e.g., `version` unchanged).  

Actions:

- Set `status = "in_progress"`.  
- Increment `attempts` by 1.  
- Set `last_attempt_at = now()`.  
- Update `updated_at` and `version`.

4.3 `in_progress` → `succeeded` (Happy Path Completion)

Trigger:

- All required operators have completed satisfactorily for this attempt.

Preconditions (baseline policy):

- `integrity_status ∈ {"ok","suspect"}`.  
- `metadata_status ∈ {"ok","suspect"}`.  
- `stac_status ∈ {"created","updated","no-op"}`.  
- `provenance_status ∈ {"ok","partial"}`.

Actions:

- Set `status = "succeeded"`.  
- Clear or leave `last_error_*` as appropriate (implementation choice; must be documented).  
- Update `updated_at` and `version`.

4.4 `in_progress` → `failed` (Attempt Failure)

Trigger:

- Hard failure in any operator, or orchestration layer decides the attempt is irrecoverable for now.

Preconditions:

- `status = "in_progress"` at decision time.  

Actions:

- Set `status = "failed"`.  
- Populate `last_error_code` and `last_error_message` (redacted).  
- Update `updated_at` and `version`.  
- SQS and replay behavior (DLQ vs visibility extension) is handled by orchestrator but MUST reflect this WAL outcome.

4.5 `failed` → `pending` (Controlled Replay)

Trigger:

- Replay tooling or orchestrator elects to retry this WAL record.

Preconditions:

- `status = "failed"`.  
- `attempts < max_attempts` (governed limit).  
- Replay policy allows replay for this error condition and dataset.  

Actions:

- Set `status = "pending"`.  
- Update `replay_reason` to managed code (`"dlq-drain"`, `"incident"`, `"backfill"`, `"test"`, etc.).  
- MAY reset `last_error_*` or leave them for history; behavior must be consistent.  
- Update `updated_at` and `version`.

4.6 `pending` → `quarantined` or `failed` → `quarantined` (Quarantine)

Trigger:

- Governance or reliability policy decides record must be **taken out of automatic flows**.

Preconditions:

- `status ∈ {"pending","failed"}`.  
- Quarantine policy satisfied (e.g., repeated failures, severe governance violation).

Actions:

- Set `status = "quarantined"`.  
- Set `last_error_code` (if not already) to an appropriate quarantine reason.  
- Update `updated_at` and `version`.

⸻

## 📡 5. Interaction with SQS Semantics

SQS provides **at-least-once** delivery with visibility timeouts. The state machine must be consistent with SQS behavior.

5.1 Worker Start

- When a worker receives a message from SQS:
  - It either:
    - Finds an existing WAL record and transitions `failed → pending → in_progress`, or  
    - Creates a new WAL record (`null → pending → in_progress`).

5.2 Worker Crash or Timeout

Cases:

- If worker crashes while `status = "in_progress"`:
  - SQS visibility timeout expires; another worker may receive the message.  
  - New worker MUST:
    - Re-check WAL record.  
    - If `status = "in_progress"` but last attempt is older than a safety threshold, it MAY transition to `failed` or directly back to `pending` via a recovery workflow (documented in implementation).  
    - All such transitions MUST be explicit and governed, not implicit.

5.3 DLQ Behavior

- If a message is eventually sent to DLQ:
  - The associated WAL record SHOULD have `status = "failed"` or `status = "quarantined"`.  
  - DLQ-drain tooling reads DLQ, correlates to WAL via `wal_id`, and decides whether to:
    - Replay (`failed → pending`), or  
    - Quarantine (`failed → quarantined`).

⸻

## 🔐 6. Concurrency & Locking Invariants

To prevent race conditions:

- At most **one worker** may successfully transition a WAL record into `in_progress` at a time.  
- Concurrency control:

  - Implementations MUST use either:
    - Optimistic concurrency via `version` (compare-and-swap semantics), or  
    - Explicit locking in the storage layer.

- Illegal concurrent transitions:

  - Two workers both seeing `status = "pending"` MUST NOT both be allowed to commit `pending → in_progress`.  

- CI and integration tests MUST simulate:

  - Contended claims of the same WAL record.  
  - Race conditions involving `in_progress` and crashes.

⸻

## 🧪 7. Edge Cases & Recovery Patterns

7.1 Permanent Upstream Failure

- Example: source object permanently missing, or upstream provider returns 404 consistently.

Policy:

- After `max_attempts` with `last_error_code` indicating permanent failure:
  - `status` SHOULD be set to `quarantined`.  
  - Replay tooling MUST NOT attempt further automatic retries.

7.2 Governance Hard-Fail

- Example: CARE/FAIR governance gate rejects payload irrecoverably.

Policy:

- Governance layer marks error and signals orchestrator.  
- WAL record:

  - `status` transitions to `quarantined`.  
  - `last_error_code = "governance_hard_fail"` (or equivalent).  

7.3 Intermittent Infra Failures

- Example: transient network or storage I/O failures.

Policy:

- `status` transitions to `failed`.  
- Replay logic, via `failed → pending`, handles retries up to explicit limits.  
- Repeated infra failures MAY eventually be treated as incidents with `replay_reason = "incident"`.

7.4 Manual Overrides

- Rare, governed cases:

  - Operator may manually move `quarantined → pending` for a one-off replay after remediation.  
  - Such transitions MUST:
    - Be recorded in a governance log or change record.  
    - Be subject to review.

⸻

## 📊 8. Telemetry Expectations per State

State changes MUST be reflected in WAL-related metrics and spans:

- On `pending → in_progress`:
  - Increment or set spans/metrics for new attempts (`wal_attempts_histogram`, etc.).  

- On `in_progress → succeeded`:
  - Increment `nodd_sns.wal_records_total{status="succeeded"}`.  

- On `in_progress → failed`:
  - Increment `nodd_sns.wal_records_total{status="failed"}`.  
  - Log a structured event with `wal_id`, `dataset`, `last_error_code`.

- On `failed → pending`:
  - Increment `nodd_sns.wal_replays_total{replay_reason=...}`.  

- On transitions to `quarantined`:
  - Increment `nodd_sns.wal_records_total{status="quarantined"}`.  
  - Emit governance/audit events as defined in higher-level specs.

⸻

## 🧪 9. CI Validation of State Machine

CI MUST include tests and static validation that:

- Only legal transitions are allowed:
  - Any attempt to perform an undefined transition (e.g., `succeeded → pending`) is rejected.  

- State + related fields invariants are upheld:
  - If `status = "succeeded"`, then `stac_status ∈ {"created","updated","no-op"}`.  
  - If `stac_status = "failed"`, then `status ≠ "succeeded"` (normally `failed` or `quarantined`).  

- Replay logic respects:
  - `max_attempts` limits.  
  - `replay_reason` vocabulary.  

- Concurrency:
  - Simulated tests prove that two concurrent claims cannot both set `in_progress` for the same `wal_id`.

Any change to state names, semantics, or allowed transitions MUST:

- Update this file.  
- Update `wal-record-model.md` and `README.md`.  
- Update storage schemas and CI tests.

⸻

## 📘 10. Version History

| Version  | Date       | Notes                                                                                                    |
|---------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD WAL state machine; defined states, transitions, SQS interplay, concurrency and CI rules.    |

---

<div align="center">

📓 NODD WAL State Machine · KFM v11.2.3  

Stateful · Deterministic · Replay-Governed  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to WAL Spec](README.md) ·  
[📓 WAL Record Model](wal-record-model.md) ·  
[🧠 NODD Replay Overview](../README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
