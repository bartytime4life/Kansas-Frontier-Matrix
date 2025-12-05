---
title: "📓 KFM v11.2.3 — NODD WAL Record Model (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Canonical WAL record field dictionary, types, and invariants for the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/wal/wal-record-model.md"

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

doc_kind: "Replay / WAL Record Model"
intent: "nodd-sns-sqs-wal-record-model"
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

# 📓 NODD WAL Record Model  

`docs/pipelines/atmo/nodd-sns-sqs/replay/wal/wal-record-model.md`

This document defines the **canonical field dictionary and invariants** for the NODD Write-Ahead Log (WAL) record used by the NOAA NODD SNS → SQS ingestion pipeline.

It specializes the high-level WAL contract in `README.md` by:

- Enumerating all core fields, types, and valid values.  
- Defining normalization and defaulting rules.  
- Describing how WAL records map into **JSON schema**, **Neo4j**, and **PROV-O / OpenLineage**.  
- Establishing validation requirements for CI and runtime.

All implementations of the NODD WAL MUST conform to this record model unless a future, versioned update states otherwise.

⸻

## 🧭 1. Relationship to WAL Specification

This file is a child of:

- `docs/pipelines/atmo/nodd-sns-sqs/replay/wal/README.md`

The WAL spec:

- Defines the **purpose**, **state machine**, and **replay semantics**.  
- Presents the **logical shape** of a WAL record.

This record model:

- Freezes the **field-level contract**.  
- Provides a single source of truth for:
  - Storage schemas (SQL, NoSQL, object).  
  - JSON schemas.  
  - API payloads.  
  - Graph and provenance mappings.

Any change to core fields or semantics MUST update **both** this file and the parent WAL README.

⸻

## 🧬 2. Canonical Record Shape (Logical)

The canonical NODD WAL record is a single, flat object with the following core fields:

    wal_id
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

Additional dataset-specific fields MAY be attached via governed extensions (section 7) but MUST NOT:

- Shadow any canonical field name.  
- Change the semantics of canonical fields.

⸻

## 🧱 3. Field Dictionary — Core Identity & Context

### 3.1 wal_id

- Type: `string`  
- Format: UUIDv7 or deterministic string (e.g., UUIDv5) as documented in implementation.  
- Role: **Primary key** for the WAL record.  
- Rules:
  - MUST be unique across all WAL records.  
  - MUST be stable across replays; a given ingest unit MUST always reference the same `wal_id`.  
  - Must be suitable as a **Neo4j node key** and **OpenLineage run correlation** attribute.

### 3.2 dataset

- Type: `string`  
- Examples: `"goes-abi"`, `"nexrad-l2"`, `"nexrad-l3"`, `"hrrr"`, `"surface-obs"`.  
- Role: Canonical NODD dataset identifier.  
- Rules:
  - MUST match dataset IDs declared in NODD config (`config/dataset-contracts` and `config/datasets/*.yaml`).  
  - Must NOT be free-form; all values must be from a controlled vocabulary.

### 3.3 object_uri

- Type: `string`  
- Examples: `s3://bucket/path/file`, `https://example.com/object`.  
- Role: Canonical pointer to the upstream object being ingested.  
- Rules:
  - MUST be normalized according to provider rules (e.g., no duplicate slashes, stable casing where applicable).  
  - MUST match the URI used by operators (`integrity-check`, `metadata-extract`, `stac-register`).

### 3.4 provider

- Type: `string`  
- Allowed values: `"aws"`, `"azure"`, `"gcp"`, or other governed provider codes.  
- Role: Indicates the upstream storage provider or mirror.  
- Rules:
  - MUST be consistent with `object_uri` and NODD config for the dataset.

### 3.5 queue

- Type: `string`  
- Role: Logical name of the SQS queue from which the worker consumed the message.  
- Rules:
  - SHOULD be a stable logical identifier (e.g., `nodd-primary`, `nodd-dlq`), not a full ARN.  
  - MUST be sufficient for SREs to map back to the physical queue.

### 3.6 event_time

- Type: `string` (RFC3339)  
- Role: The **upstream event timestamp** (e.g., when NODD published SNS).  
- Rules:
  - MUST be copied or derived from the canonical event envelope (`message-parse`).  
  - Used in ordering and provenance, but not necessarily equal to ingest time.

### 3.7 time_range_start, time_range_end

- Type: `string` (RFC3339)  
- Role: Temporal coverage of the object (e.g., observation or model window).  
- Rules:
  - MUST satisfy `time_range_start ≤ time_range_end`.  
  - MUST match or be compatible with the values used for STAC temporal properties.  
  - If the object represents an instantaneous event, both MAY be equal to `event_time` or another canonical timestamp, per dataset config.

⸻

## 🔄 4. Field Dictionary — Lifecycle & Errors

### 4.1 status

- Type: `string`  
- Allowed values:
  - `"pending"`  
  - `"in_progress"`  
  - `"succeeded"`  
  - `"failed"`  
  - `"quarantined"`  
- Role: High-level lifecycle state of the ingest unit.  
- Rules:
  - MUST follow the state machine defined in WAL `README.md`.  
  - Transitions MUST be enforced by state machine validation logic.

### 4.2 attempts

- Type: `integer` (non-negative)  
- Role: Total number of ingest attempts, including initial run and all replays.  
- Rules:
  - MUST increment exactly once per transition `pending → in_progress` for a new attempt.  
  - MUST NOT be decremented.  
  - MUST be used to enforce maximum retry / replay thresholds.

### 4.3 last_attempt_at

- Type: `string` (RFC3339)  
- Role: Timestamp of the most recent attempt start or completion (implementation choice; MUST be documented).  
- Rules:
  - MUST be updated on each new attempt.  
  - MAY be used by replay tooling to prioritize older failures.

### 4.4 last_error_code

- Type: `string | null`  
- Role: Short, machine-readable error code for the most recent failure.  
- Examples: `"validation_failed"`, `"integrity_missing_object"`, `"stac_validation_failed"`, `"io_error"`, `"governance_hard_fail"`.  
- Rules:
  - MUST be `null` if there has never been a failure.  
  - MUST NOT contain full stack traces or PII.

### 4.5 last_error_message

- Type: `string | null`  
- Role: Redacted, human-readable error summary.  
- Rules:
  - MUST avoid PII, secrets, and long stack traces.  
  - SHOULD be bounded in length (implementation-defined limit).  
  - MUST be `null` when `status` has never been `"failed"` or `"quarantined"`.

⸻

## 🧪 5. Field Dictionary — Operator Statuses & STAC

### 5.1 integrity_status

- Type: `string`  
- Allowed values: `"unknown"`, `"ok"`, `"suspect"`, `"failed"`.  
- Role: Summarizes `integrity-check` outcome.  
- Rules:
  - Initial value MUST be `"unknown"`.  
  - MUST reflect the latest integrity-check results.  
  - `"failed"` MAY be used by orchestrators to drive `status = failed` or `quarantined`.

### 5.2 metadata_status

- Type: `string`  
- Allowed values: `"unknown"`, `"ok"`, `"suspect"`, `"failed"`.  
- Role: Summarizes `metadata-extract` outcome.  
- Rules:
  - Initial value MUST be `"unknown"`.  
  - After `metadata-extract` runs, MUST be one of the non-unknown values.  
  - `"failed"` MUST prevent STAC registration in normal flows.

### 5.3 stac_status

- Type: `string`  
- Allowed values: `"unknown"`, `"created"`, `"updated"`, `"no-op"`, `"failed"`.  
- Role: Summarizes `stac-register` outcome.  
- Rules:
  - `"created"`: Item did not exist before and was created.  
  - `"updated"`: Item existed and was modified.  
  - `"no-op"`: Item existed and was already up to date.  
  - `"failed"`: Registration attempt failed and MUST be coupled with `status = failed`.

### 5.4 provenance_status

- Type: `string`  
- Allowed values: `"unknown"`, `"ok"`, `"partial"`, `"failed"`.  
- Role: Summarizes `provenance-emit` outcome.  
- Rules:
  - `"partial"` indicates one of PROV-O or OpenLineage succeeded and the other failed.  
  - `"failed"` MUST be visible to reliability and governance tooling, but may still allow `status = succeeded` if pipeline policy permits (documented in WAL `README.md`).

### 5.5 stac_item_id

- Type: `string | null`  
- Role: Identifier of the STAC Item associated with this WAL record.  
- Rules:
  - MUST be set when `stac_status ∈ {"created", "updated", "no-op"}`.  
  - MUST be `null` when STAC was never successfully registered.

### 5.6 stac_collection_id

- Type: `string | null`  
- Role: STAC Collection ID that owns the Item.  
- Rules:
  - MUST be non-null whenever `stac_item_id` is non-null.  
  - MUST match dataset configuration.

### 5.7 stac_item_href

- Type: `string | null`  
- Role: Canonical URI/HREF pointing to the STAC Item in the catalog.  
- Rules:
  - MUST be set when STAC registration succeeds.  
  - MUST be stable across replays (same item, same location) unless a governed migration occurs.

⸻

## 🧵 6. Field Dictionary — Run & Replay Metadata

### 6.1 ingest_run_id

- Type: `string`  
- Role: Identifies the pipeline run that processed this WAL record (e.g., a worker batch, job run ID).  
- Rules:
  - MUST be set on first attempt.  
  - MAY change on replays if reprocessed by a different run.

### 6.2 worker_id

- Type: `string`  
- Role: Logical identity of the worker processing the record.  
- Rules:
  - SHOULD be stable across a worker instance but MUST NOT include host-level PII.  
  - Used for debugging and hotspot detection.

### 6.3 replay_reason

- Type: `string | null`  
- Allowed values (baseline): `"none"`, `"dlq-drain"`, `"incident"`, `"backfill"`, `"test"`, or other governed codes.  
- Rules:
  - Initial value SHOULD be `"none"` or `null`.  
  - MUST be updated when a replay is triggered for a specific reason.  
  - MUST be from a controlled vocabulary declared in replay configs.

### 6.4 created_at, updated_at

- Type: `string` (RFC3339)  
- Role:
  - `created_at`: when the WAL record was first created.  
  - `updated_at`: when it was last modified.  
- Rules:
  - `created_at` MUST NOT change.  
  - `updated_at` MUST be bumped on every write.

### 6.5 version

- Type: `integer` (monotonic, ≥ 1)  
- Role: Optimistic concurrency control version.  
- Rules:
  - MUST increment by 1 for each successful write to the record.  
  - MUST be enforced by storage layer or ORM to prevent concurrent races.

⸻

## 🧩 7. Extensions & Dataset-Specific Fields

KFM allows **governed extensions** to the WAL record for dataset-specific needs.

### 7.1 Extension Rules

- Extension fields:
  - MUST live under a namespaced prefix (e.g., `ext_nodd_*` or `ext_<dataset>_*`) if risk of collision exists.  
  - MUST be documented in dataset-specific pipeline docs, not only in code.  
  - MUST NOT alter semantics of any canonical field.

Examples (illustrative):

- `ext_partition_key` — partition or shard key used by a downstream data store.  
- `ext_model_run_id` — full model run ID for HRRR or similar product.  

### 7.2 Validation of Extensions

- CI MUST validate:
  - That all extension fields used in production WAL records are declared and documented.  
  - That no extension field shares a name with any canonical field in this file.  

⸻

## 🗃 8. JSON Schema & Storage Bindings

### 8.1 JSON Schema

An official JSON Schema for NODD WAL records SHOULD be stored under:

- `schemas/json/nodd-wal-record-v1.json` (or equivalent).

The schema MUST:

- Match the field names and allowed values from this document.  
- Declare required vs optional fields:
  - Required: `wal_id`, `dataset`, `object_uri`, `provider`, `queue`, `status`, `attempts`, `created_at`, `updated_at`, `version`.  
  - Optional but recommended: `event_time`, `time_range_start`, `time_range_end`, `ingest_run_id`, `worker_id`.  
- Support extension fields via a governed pattern (e.g., `ext_*` with looser constraints).

### 8.2 Storage Backends

Bindings MAY include:

- Relational (SQL):  
  - Table `nodd_wal_records` with columns matching this model.  
  - Indices on `wal_id`, `dataset`, `status`, `updated_at`.

- Object (S3, GCS, etc.):  
  - One JSON record per key (e.g., keyed by `wal_id` or hashed path).  

Regardless of backend, the **logical model** MUST remain identical.

⸻

## 🧬 9. Mapping to Neo4j & PROV-O / OpenLineage

### 9.1 Neo4j

In the KFM graph:

- Node type:
  - `(:WalRecord { wal_id, dataset, status, attempts, ... })`  
- Important relationships:
  - `(:WalRecord)-[:DERIVES_ITEM]->(:StacItem { stac_item_id })`  
  - `(:WalRecord)-[:HAS_PROVENANCE_ACTIVITY]->(:Activity { id = prov activity })`  

`wal_id` MUST be used as a stable node key to attach:

- Spans and metrics.  
- Provenance activities and entities.  
- Replay analysis and mismatch investigations.

### 9.2 PROV-O / OpenLineage

- `wal_id` MUST appear as:
  - A PROV-O attribute on the `prov:Activity` representing ingestion.  
  - An attribute (e.g., `kfm:walId`) on OpenLineage `Run` objects.

This provides a single, cross-system handle for:

- CI lineage checks.  
- Incident forensics.  
- Replay mismatch detection.

⸻

## 🧪 10. Validation & CI Requirements

CI MUST include:

1. **Schema Validation**  
   - JSON representations of WAL records validate against the WAL JSON Schema that implements this model.

2. **Enum Validation**  
   - Fields with enumerated values (`status`, `integrity_status`, `metadata_status`, `stac_status`, `provenance_status`, `provider`, `replay_reason`) MUST use only allowed values.

3. **Invariant Checks**  
   - `time_range_start ≤ time_range_end`.  
   - `attempts ≥ 0`.  
   - `created_at ≤ updated_at`.  
   - If `stac_status ∈ {"created","updated","no-op"}`, then:
     - `stac_item_id` and `stac_collection_id` MUST be non-null.

4. **Extension Audit**  
   - Detect any field outside the canonical set and ensure it is declared as an allowed extension.

5. **Fixture Tests**  
   - Reference WAL fixtures (e.g., `docs/pipelines/atmo/nodd-sns-sqs/replay/wal/fixtures/*.json` if present) MUST validate and cover:
     - A successful ingest.  
     - A failed ingest.  
     - A replay scenario.

Any change to field definitions, types, or allowed values MUST:

- Update this document.  
- Update JSON Schema and WAL storage migrations.  
- Update associated CI tests.

⸻

## 📘 11. Version History

| Version  | Date       | Notes                                                                                                       |
|---------:|------------|-------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD WAL record model; aligned with WAL spec, defined field dictionary, enums, and validation rules.|

---

<div align="center">

📓 NODD WAL Record Model · KFM v11.2.3  

Schema-Grounded · Deterministic · Replay-Ready  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to WAL Spec](README.md) ·  
[📓 WAL State Machine](wal-state-machine.md) ·  
[🧠 NODD Replay Overview](../README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
