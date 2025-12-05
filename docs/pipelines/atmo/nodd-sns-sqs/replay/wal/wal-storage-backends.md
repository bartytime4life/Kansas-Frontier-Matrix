---
title: "📓 KFM v11.2.3 — NODD WAL Storage Backends (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed guidance for implementing durable, deterministic, and queryable storage backends for the NODD Write-Ahead Log (WAL) in the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/wal/wal-storage-backends.md"

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

doc_kind: "Replay / WAL Storage Backends"
intent: "nodd-sns-sqs-wal-storage-backends"
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

# 📓 NODD WAL Storage Backends  

`docs/pipelines/atmo/nodd-sns-sqs/replay/wal/wal-storage-backends.md`

Guidance for implementing **durable, deterministic, and queryable storage backends** for the NODD Write-Ahead Log (WAL) used by the NOAA NODD SNS → SQS ingestion pipeline.

This document:

- Describes the allowed storage patterns for WAL records.  
- Defines durability, consistency, and indexing requirements.  
- Details backup, retention, and encryption expectations.  
- Aligns storage backends with the WAL record model and state machine.

It is a companion to:

- `wal-record-model.md` — field dictionary and invariants.  
- `wal-state-machine.md` — legal transitions and replay semantics.  
- `README.md` — overall WAL contract.

⸻

## 🧭 1. Design Goals

Any NODD WAL storage backend MUST satisfy:

- Durability  
  WAL records MUST survive individual worker failures, node restarts, and routine maintenance.

- Determinism  
  The same WAL record MUST be readable and updateable in a way that respects the WAL state machine and idempotency rules.

- Queryability  
  Operators, SREs, and replay tools MUST be able to query WAL records by `wal_id`, `dataset`, `status`, time ranges, and error codes.

- Concurrency Safety  
  No two workers may simultaneously commit conflicting changes for the same `wal_id`.

- Governance & Security  
  WAL contents MUST be encrypted at rest, protected in transit, and retained according to TTL and audit requirements.

NODD allows multiple backend implementations, provided they respect this contract.

⸻

## 🧱 2. Canonical Logical Model (Reminder)

The logical model is defined in `wal-record-model.md`.  
At minimum, each WAL record MUST support:

    wal_id, dataset, object_uri, provider, queue
    event_time, time_range_start, time_range_end
    status, attempts, last_attempt_at, last_error_code, last_error_message
    integrity_status, metadata_status, stac_status, provenance_status
    stac_item_id, stac_collection_id, stac_item_href
    ingest_run_id, worker_id, replay_reason
    created_at, updated_at, version

Any storage backend MUST be capable of storing and retrieving these fields with sufficient precision and type fidelity.

⸻

## 🗃 3. Backend Types (Recommended Patterns)

Three backend patterns are explicitly supported for NODD WAL:

1. Relational DB (preferred)  
2. Object Store + Index  
3. Log/Stream-backed WAL (advanced, optional)

Implementers MAY combine patterns (e.g., DB + archive to object storage), but MUST keep a single, authoritative WAL per environment.

### 3.1 Relational DB Backend (Preferred)

Typical systems:

- PostgreSQL, Aurora/Postgres, or equivalent.

Logical table:

    nodd_wal_records
      wal_id              PRIMARY KEY
      dataset
      object_uri
      provider
      queue
      event_time
      time_range_start
      time_range_end

      status
      attempts
      last_attempt_at
      last_error_code
      last_error_message

      integrity_status
      metadata_status
      stac_status
      provenance_status

      stac_item_id
      stac_collection_id
      stac_item_href

      ingest_run_id
      worker_id
      replay_reason

      created_at
      updated_at
      version

Key requirements:

- Strong consistency for single-record reads/writes.  
- Row-level locking or optimistic concurrency for `wal_id`.  
- Indices on:
  - `status` (for scanning failed/pending records).  
  - `(dataset, status, updated_at)` (for replay selection).  
  - `updated_at` (for time-based retention and reporting).

### 3.2 Object Store + Index

Pattern:

- Store each WAL record as a JSON object in an object store (e.g., S3), keyed by `wal_id` (or partitioned hash).  
- Maintain a separate, smaller index structure (DB table or key-value store) with a subset of fields used for queries.

Object store:

- Keys like:
  - `wal/<dataset>/<yyyy>/<mm>/<dd>/<wal_id>.json`  
- Used primarily for:
  - Durability.  
  - Forensic inspection.  
  - Offline batch analyses.

Index:

- Contains:
  - `wal_id`, `dataset`, `status`, `updated_at`, `last_error_code`, and pointers to the full object.  
- Used for:
  - Replay candidate selection.  
  - Status dashboards.

Constraints:

- Updates MUST remain atomic from an application perspective:
  - The record and its index entry MUST represent a consistent view (use transactions or idempotent upserts).  

### 3.3 Stream / Log-backed WAL (Advanced)

Pattern:

- WAL records write-ahead to an append-only log (e.g., Kafka, Kinesis).  
- A derived store (DB or object store) materializes the **current** record state per `wal_id`.

Constraints:

- The **materialized store** still MUST obey all standard WAL invariants.  
- Log compaction and retention MUST NOT break the ability to reconstruct or audit the WAL within the governed time horizon.

This pattern is advanced and SHOULD be used only where the log system is already part of the KFM stack and has clear operational ownership.

⸻

## 🔐 4. Durability, Encryption & Access Control

### 4.1 Durability

Backends MUST:

- Be configured with redundancy appropriate for production (e.g., multi-AZ or equivalent).  
- Implement regular backups or snapshots.  
- Support point-in-time recovery within the WAL retention window.

### 4.2 Encryption

- At rest:
  - Data MUST be encrypted with approved KMS keys or equivalent.  
- In transit:
  - Connections MUST use TLS or equivalent encryption.

Encryption keys:

- MUST be managed following KFM governance rules; access must be auditable and least-privilege.

### 4.3 Access Control

Principles:

- Write access:
  - Only WAL writers (ingestion workers, replay tools) and migration tools.  
- Read access:
  - Ingestion workers, replay tools, SREs, and governance tooling.  
- Restricted access:
  - Direct access from non-privileged applications is discouraged; use dedicated APIs or views.

Auditing:

- Access to WAL backends SHOULD be logged and auditable (especially for administrative and manual replay tools).

⸻

## 🧮 5. Concurrency & Consistency Requirements

Any backend MUST support:

- Single-record consistency for updates to `status`, `attempts`, `version`, and timestamps.  
- A concurrency mechanism that enforces:

    If two writers attempt to update the same wal_id concurrently:
      Only one update may succeed.
      The other MUST receive a conflict and retry with fresh state.

Implementation options:

- Optimistic concurrency:

    - Use `version` column/field; update only if `version` matches.  
    - Increment `version` on each successful write.

- Pessimistic locking:

    - Use SELECT FOR UPDATE or equivalent.  
    - Ensure locks are held only for brief operations.

State-machine validation MUST occur in the application layer:

- Illegal transitions (e.g., `succeeded → pending`) MUST be rejected before writing.

⸻

## 🧪 6. Backups, Retention & Archival

### 6.1 Retention Policy

Baseline expectations:

- WAL records SHOULD be retained for at least the same duration as:
  - STAC Item retention.  
  - Provenance records, or the governed minimum for atmospheric pipelines (whichever is longer).

The `ttl_policy` for this document (24 months) is the **review** policy, not necessarily the storage TTL.  
Actual WAL retention MUST be set by governance/infra teams and documented elsewhere (e.g., infra repo, ops runbook).

### 6.2 Backups & Recovery

Backends MUST support:

- Regular scheduled backups (DB dumps, snapshots, incremental backups).  
- Documentation of:
  - RPO (Recovery Point Objective).  
  - RTO (Recovery Time Objective) for the WAL.

Recovery expectations:

- After a restore, the WAL MUST still be consistent with the state machine and replay semantics.  
- Replays MUST NOT unintentionally re-ingest already succeeded items in ways that violate idempotency.

### 6.3 Archival

Long-lived WALs MAY be:

- Moved to cheaper storage tiers after a period (e.g., > 1 year).  
- Kept read-only for audits and research.

Any archival process MUST:

- Preserve the full WAL record.  
- Document how to reconstruct or query archived WAL records if required.

⸻

## 🧬 7. Environment & Multi-Region Considerations

Per environment:

- Each environment (`dev`, `stage`, `prod`) MUST have a separate WAL backend or clear separation within a shared backend (e.g., schema or prefix).

Cross-region or cross-account:

- If NODD ingestion is deployed in multiple regions or accounts:
  - WAL instances MUST NOT conflict (no shared `wal_id` namespace across uncoordinated deployments).  
  - Governance MUST define whether cross-region replication of WAL is needed for DR.

Replay and incident tooling MUST be aware of the environment and region boundaries.

⸻

## 📡 8. Observability of WAL Backends

Backends MUST expose telemetry:

- Availability:
  - DB connection errors, object-store failures, and latency metrics.  
- Capacity:
  - Storage size and growth trends (DB table size, bucket size).  
- Performance:
  - WAL read/write latency P50/P90/P99.  
- Errors:
  - Update conflicts (version mismatch), failed writes, and failed reads.

Where possible, WAL observability SHOULD integrate into:

- NODD ingestion dashboards (e.g., a WAL health section).  
- Global KFM reliability dashboards.

⸻

## 🧪 9. CI, Migrations & Compatibility

### 9.1 Schema Validation

CI MUST validate:

- That WAL storage schema matches the logical record model:
  - All canonical fields present.  
  - Correct types (or compatible equivalents).  
  - Constraints (e.g., primary key on `wal_id`) in place.

### 9.2 Migrations

Schema migrations MUST:

- Be versioned and backwards-compatible where feasible.  
- Ensure no data loss of canonical fields.  
- Be able to run without blocking ingestion for unacceptable periods (use rolling migration patterns).

Any migration affecting:

- Field types.  
- Allowed `status` values.  
- Indexing strategies that impact replay.

MUST be reviewed by the Provenance & Reliability Council and reflected in WAL documentation.

### 9.3 Backend Changes

Changing backend type (e.g., from DB to object-store+index) is a **major operation** and MUST:

- Include a full data migration plan.  
- Guarantee preservation of `wal_id`, statuses, and critical fields.  
- Be coordinated with replay, telemetry, and lineage systems.

⸻

## 📘 10. Version History

| Version  | Date       | Notes                                                                                                        |
|---------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD WAL storage backends guidance; defined DB, object, and log patterns plus durability and CI rules.|

---

<div align="center">

📓 NODD WAL Storage Backends · KFM v11.2.3  

Durable · Queryable · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to WAL Spec](README.md) ·  
[📓 WAL Record Model](wal-record-model.md) ·  
[📓 WAL State Machine](wal-state-machine.md) ·  
[🧠 NODD Replay Overview](../README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
