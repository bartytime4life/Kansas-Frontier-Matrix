---
title: "📓 KFM v11.2.3 — NODD WAL Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Write-Ahead Log (WAL) contract, record model, and replay semantics for the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/wal/README.md"

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

doc_kind: "Replay / WAL Specification"
intent: "nodd-sns-sqs-wal-spec"
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
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major NODD WAL contract"

header_profile: "standard"
footer_profile: "standard"
---

# 📓 NODD WAL Specification  

`docs/pipelines/atmo/nodd-sns-sqs/replay/wal/README.md`

Write-Ahead Log (WAL) contract for the NOAA NODD SNS → SQS ingestion pipeline.  
This document defines:

- The **canonical WAL record model** for NODD ingest units.  
- Allowed **state transitions** and replay semantics.  
- How WAL integrates with **SQS, STAC, provenance, and telemetry**.  
- Determinism and idempotency guarantees required by KFM v11.

⸻

## 🧭 1. Purpose & Scope

The NODD WAL is the **authoritative reliability ledger** for the NODD SNS → SQS pipeline. It exists to:

- Ensure every ingest unit is **recorded before side effects** (STAC writes, provenance).  
- Enable **deterministic replays** after failures, DLQ drains, or incident responses.  
- Provide a stable source of truth for **provenance, audits, and lineage CI**.  

This specification applies to:

- All workers consuming from the NODD SQS queues.  
- Any replay tooling documented under `../README.md` and `../runbooks/`.  
- Telemetry and lineage systems that rely on WAL IDs.

⸻

## 🗂 2. Directory Layout (WAL Subtree)

WAL-specific documentation and artifacts live under:

    docs/pipelines/atmo/nodd-sns-sqs/replay/wal/
    │
    ├── 📄 README.md                # This file — WAL contract and semantics
    │
    ├── 📄 wal-record-model.md      # Extended field dictionary, examples, mapping tables
    ├── 📄 wal-state-machine.md     # Detailed state diagrams and edge-case handling
    └── 📄 wal-storage-backends.md  # Implementation notes for storage engines (S3, DB, etc.)

Implementation code, schemas, and infra resources are referenced from here but live outside `docs/`.

⸻

## 🧬 3. WAL Record Model (Canonical)

Each ingestable NODD unit has exactly one **WAL record** identified by `wal_id`.  
The canonical logical shape (conceptual, not JSON-schema syntax) is:

    wal_id:               string (UUIDv7 or deterministic hash)
    dataset:              string (canonical NODD dataset ID, e.g., "goes-abi", "nexrad-l2")
    object_uri:           string (canonical object URI or key)
    provider:             string ("aws" | "azure" | "gcp" | other configured)
    queue:                string (logical SQS queue name)
    event_time:           string (RFC3339; upstream event timestamp)
    time_range_start:     string (RFC3339)
    time_range_end:       string (RFC3339)

    status:               string (see section 4; e.g., "pending", "in_progress", "succeeded", "failed", "quarantined")
    attempts:             integer (total attempts, including replays)
    last_attempt_at:      string (RFC3339 timestamp of latest attempt)
    last_error_code:      string | null (short machine-readable error code)
    last_error_message:   string | null (redacted, non-PII error summary)

    integrity_status:     string ("unknown" | "ok" | "suspect" | "failed")
    metadata_status:      string ("unknown" | "ok" | "suspect" | "failed")
    stac_status:          string ("unknown" | "created" | "updated" | "no-op" | "failed")
    provenance_status:    string ("unknown" | "ok" | "partial" | "failed")

    stac_item_id:         string | null
    stac_collection_id:   string | null
    stac_item_href:       string | null

    ingest_run_id:        string (pipeline run identifier)
    worker_id:            string (logical worker identity, not host identifier)
    replay_reason:        string | null ("none" | "dlq-drain" | "incident" | "backfill" | "test" | custom governed code)

    created_at:           string (RFC3339)
    updated_at:           string (RFC3339)
    version:              integer (monotonic version for optimistic concurrency)

Additional dataset-specific fields MAY be attached but MUST NOT conflict with these canonical names.

⸻

## 🔁 4. WAL Status Model

`status` describes the ingest lifecycle for a single WAL record. Allowed values:

- `pending`  
  Record created; work not yet started.

- `in_progress`  
  Worker currently processing the unit (short-lived state; must be bounded by visibility timeout + safety window).

- `succeeded`  
  Ingest fully completed:
  - STAC successfully registered (`stac_status ∈ {created, updated, no-op}`), and  
  - Provenance emission succeeded or is marked `provenance_status ∈ {"ok", "partial"}` per policy.

- `failed`  
  Ingest attempt failed and is eligible for **automatic retry or replay**.

- `quarantined`  
  Ingest is held for manual intervention (e.g., permanent validation failure, governance violation).

High-level rules:

- `succeeded` and `quarantined` are **terminal states** for reliability.  
- `failed` is a **non-terminal state**; replay tools may transition it back to `pending` under controlled workflows.  
- Transitions MUST follow the state machine in section 5.

⸻

## 🔄 5. WAL State Machine (Allowed Transitions)

Valid transitions for `status`:

- `null` → `pending`  
  Record is created when the worker first sees a new ingest unit.

- `pending` → `in_progress`  
  Worker claims the unit and begins processing.

- `in_progress` → `succeeded`  
  All downstream operators (`integrity-check`, `metadata-extract`, `stac-register`, `provenance-emit`) report acceptable outcomes.

- `in_progress` → `failed`  
  Any **hard failure** that aborts processing (validation failure, storage error, governance hard-fail).

- `failed` → `pending`  
  Controlled replay (via replay tooling); `attempts` is incremented, `replay_reason` set.

- `pending` | `failed` → `quarantined`  
  Manual or automated quarantine decision (e.g., repeated failures over limit, governance issues).

Constraints:

- `succeeded` or `quarantined` MUST NOT transition back to `in_progress` or `pending` except via an explicit, governance-approved migration process (not part of routine replay).  
- All transitions MUST be version-controlled via `version` (optimistic concurrency) to avoid race conditions.

⸻

## 🧱 6. WAL vs Operator Chain (Integration Points)

For each ingest attempt, operators interact with WAL as follows:

- `message-parse`:  
  - Ensures `wal_id` is present or deterministically derived.  
  - If record does not exist, creates a `pending` WAL entry.

- `integrity-check`:  
  - Updates `integrity_status` and `last_error_*` if applicable.  
  - Does not change `status` except indirectly via orchestrator.

- `metadata-extract`:  
  - Updates `metadata_status`.  

- `stac-register`:  
  - Updates `stac_status`, `stac_item_id`, `stac_collection_id`, `stac_item_href`.  
  - On hard failure, orchestrator sets `status = failed`.

- `provenance-emit`:  
  - Updates `provenance_status`.  
  - On success path, orchestrator marks `status = succeeded` (if all other conditions satisfied).

Write ordering:

1. Create/lock WAL record (`pending` → `in_progress`).  
2. Execute operators.  
3. Update WAL record with final statuses and `status` terminal state (`succeeded` / `failed` / `quarantined`).  

No STAC or provenance side-effect is considered committed until the WAL record reflects the final outcome.

⸻

## 🧮 7. Determinism & Idempotency Guarantees

The WAL provides the backbone for deterministic replays:

- **Deterministic identification**  
  - `wal_id` MUST be reproducible for the same `(dataset, object_uri, time_range_start)` or use a UUID assigned exactly once and persisted.  
  - Replay processes MUST NOT create a new WAL record for a unit that already has a record.

- **Idempotent replays**  
  - Re-running the ingest for the same WAL record MUST NOT create duplicate STAC Items or lineage edges.  
  - `stac-register` and `provenance-emit` operators rely on WAL fields (e.g., `stac_item_id`, `provenance IDs`) to ensure idempotency.

- **Single-writer semantics per record**  
  - At any point, exactly one worker may hold the `in_progress` lock for a WAL record (enforced via storage-level concurrency).

- **Purely functional transitions**  
  - Given the same WAL record, config, and external object state, replay outcomes MUST be consistent (same final statuses).

⸻

## 🔁 8. Replay Semantics & Safety Rules

Replay tooling (documented in `../README.md` and runbooks under `../runbooks/`) MUST follow these rules:

- Eligible records:
  - `status = failed` or specific `quarantined` records where policy allows.  
  - `attempts` below configured max retry/replay count.

- Replay actions:
  - Set `status = pending`, increment `attempts`, set `replay_reason` (`dlq-drain`, `incident`, `backfill`, etc.).  
  - Enqueue work back into SQS or schedule via internal replay mechanism.

- Safety limits:
  - Max attempts per WAL record (e.g., 5–10; defined in configuration).  
  - Hard cap on replays per batch to avoid overload.  
  - Optionally, **kill-switch flags per dataset** to pause all replays when required.

- Determinism enforcement:
  - Telemetry metric `nodd_sns.replay_mismatch_total` MUST be incremented if replay outcomes differ from prior successful runs in non-permitted ways (e.g., STAC item shape divergence).

Replays MUST always operate via WAL introspection, not ad hoc scanning of STAC or SQS alone.

⸻

## 📊 9. Telemetry & Lineage Integration

WAL operations contribute to both telemetry and lineage:

- Metrics:
  - `nodd_sns.wal_records_total{dataset,status}`  
  - `nodd_sns.wal_replays_total{dataset,replay_reason}`  
  - `nodd_sns.wal_attempts_histogram{dataset}`  
  - `nodd_sns.replay_mismatch_total{dataset}`  

- Spans:
  - Each ingest attempt span MUST carry `wal_id` as a primary correlation attribute.  
  - Replay spans MUST include `replay_reason` and reference the same `wal_id`.

- Lineage:
  - `wal_id` links OpenLineage runs and PROV-O Activities back to the canonical WAL record.  
  - WAL is expected to be queryable by lineage tooling for forensic/CI checks.

⸻

## 🧪 10. Testing & CI Requirements

CI MUST verify:

- **Schema compliance**  
  - WAL storage schema matches the canonical fields and types defined here.  
  - Changes to WAL schema are versioned and reviewed.

- **State machine enforcement**  
  - Unit tests for valid transitions and rejections of illegal transitions (e.g., `succeeded → pending`).

- **Deterministic ID tests**  
  - For deterministic `wal_id` strategies, the same inputs produce the same ID across runs.

- **Replay end-to-end tests**  
  - Simulate:
    - A failure leading to `status = failed`.  
    - Controlled replay of that WAL record.  
    - Confirm STAC and provenance outputs, and final `status = succeeded`, are consistent across runs.

- **Concurrency tests**  
  - Ensure only one worker can set `status = in_progress` for a given WAL record at a time.

Any change to WAL behavior, fields, or semantics MUST update this document and the associated tests.

⸻

## 📘 11. Version History

| Version  | Date       | Notes                                                                                                       |
|---------:|------------|-------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD WAL specification; defined record model, state machine, replay semantics, and telemetry hooks. |

---

<div align="center">

📓 NODD WAL Specification · KFM v11.2.3  

Deterministic · Replay-Safe · Provenance-Ready  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Replay](../README.md) ·  
[🧠 Operators](../../operators/README.md) ·  
[📊 Telemetry](../../telemetry/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
