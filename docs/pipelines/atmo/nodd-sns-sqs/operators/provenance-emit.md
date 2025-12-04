---
title: "📚 KFM v11.2.3 — NODD Provenance Emit Operator Contract (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed contract and behavior specification for the provenance-emit operator in the NOAA NODD SNS → SQS ingestion pipeline, mapping runs into PROV-O and OpenLineage."
path: "docs/pipelines/atmo/nodd-sns-sqs/operators/provenance-emit.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x operator-contract compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/nodd-sns-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/nodd-sns-sqs-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Pipeline Operator Contract"
intent: "nodd-provenance-emit-operator"
category: "Pipelines · Atmospheric · Operators · Provenance"

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
sunset_policy: "Superseded by next major NODD provenance-emit contract"

header_profile: "standard"
footer_profile: "standard"
---

# 📚 NODD Provenance Emit Operator — Contract  

`docs/pipelines/atmo/nodd-sns-sqs/operators/provenance-emit.md`

The **provenance-emit** operator translates a completed NODD ingest unit into:

- **PROV-O** records (Activities, Entities, Agents) suitable for KFM’s provenance ledger and Neo4j graph.  
- **OpenLineage** events (Job, Run, Dataset) for lineage CI validation and observability.

It is:

- Deterministic — same envelope + config → same PROV-O and OpenLineage payloads.  
- Idempotent — repeat emissions for the same ingest unit do not create duplicate lineage edges.  
- Governance-aligned — all emissions respect FAIR+CARE, sovereignty flags, and lineage rules.

This operator executes last in the hot-path, after successful STAC registration.

⸻

## 🧭 1. Position in the Operator Chain

Conceptual operator chain for a single ingest unit:

    SNS/SQS Message
      → message-parse
      → integrity-check
      → metadata-extract
      → stac-register
      → provenance-emit

Requirements:

- `provenance-emit` MUST run only after `stac-register` has succeeded (or decided a no-op) for the unit.  
- It MUST NOT mutate STAC Items or underlying data; it only records lineage.  
- Failures in provenance emission MUST be visible and replayable via WAL and replay tooling.

⸻

## 📥 2. Input Contract

The operator consumes an envelope enriched by **all previous operators**.

### 2.1 Required Fields from Upstream

From `message-parse`:

- `event_time`  
- `dataset`  
- `object_uri`  
- `provider`  
- `time_range.start` / `time_range.end`  

From `integrity-check`:

- `integrity.status` (must not be `failed`).  
- `integrity.actual_size_bytes` (if available).  
- `integrity.actual_etag` (if available).

From `metadata-extract`:

- `metadata_extract.status` (usually `ok` or `suspect`).  
- `geometry` and `bbox` (if applicable).  
- `stac_properties` (used for contextual provenance metadata).

From `stac-register`:

- `stac_item_id` (required for successful ingest).  
- `stac_collection_id` (required; identifies collection).  
- `stac_write_status` — one of `created`, `updated`, `no-op`, `failed` (MUST NOT be `failed`).  
- Optional reference to STAC catalog path (e.g., `stac_item_href`).

From WAL / runtime context:

- `wal_id` — WAL entry associated with this ingest unit.  
- `ingest_run_id` — pipeline run identifier (if separate from WAL).  
- Optional `job_name` / `task_name` (for OpenLineage Job mapping).

If `stac_write_status = failed` or `stac_item_id` is missing, `provenance-emit` MUST treat the envelope as **not eligible** for provenance and signal a failure to upstream orchestrator.

⸻

## 📤 3. Output Contract — Provenance & Lineage IDs

The operator returns the same envelope, enriched with provenance identifiers:

- `provenance_emit.status`  
  - One of: `ok`, `failed`, `partial`.

- `provenance_emit.issues`  
  - Array of codes, e.g.:
    - `["prov_store_unavailable"]`, `["openlineage_emit_failed"]`.

- `provenance_emit.checks_run`  
  - List of sub-operations executed, e.g.:
    - `["prov_activity_upsert", "prov_entity_upsert", "openlineage_run_emit"]`.

- `prov_activity_id`  
  - Identifier for the `prov:Activity` representing this ingest run.

- `prov_entity_ids`  
  - Map of logical entity roles → IDs, e.g.:
    - `{"source_object": "...", "stac_item": "..."}`.

- `prov_agent_ids`  
  - IDs for agents (e.g., pipeline service, operator).

- `openlineage_run_id`  
  - Run ID emitted to OpenLineage.

- `openlineage_job_name`  
  - Job name used in OpenLineage.

These IDs must be stable or deterministically derived given the same inputs and configuration.

⸻

## 🧱 4. Provenance Model (PROV-O)

The operator MUST create or update PROV-O constructs for each ingest unit.

### 4.1 Activities

Create a `prov:Activity` representing the ingestion:

- Example type: `kfm:noddIngestActivity`.  
- Attributes:
  - Start/end time.  
  - Code and config versions.  
  - Dataset identifier.  
  - WAL ID and ingest run ID.

Relationships:

- `prov:used`:
  - The source NODD object entity.  
- `prov:generated`:
  - The resulting STAC Item entity.

### 4.2 Entities

At minimum:

- Source object entity (e.g., `prov:Entity`, mapped also to `crm:E73_Information_Object`):
  - Attributes:
    - `dataset`, `object_uri`, `provider`.  
    - Size, checksum, time range.  
    - Optional link to original NODD bucket path.

- STAC Item entity:
  - Attributes:
    - `stac_item_id`, `stac_collection_id`.  
    - `datetime` and time range.  
    - Key STAC properties (e.g., product type, platform, processing level).

Relationships:

- `prov:wasDerivedFrom`:
  - STAC Item entity ← Source object entity.

### 4.3 Agents

Establish `prov:Agent` for:

- Pipeline or service identity (e.g., `kfm-nodd-ingest`).  
- Optional user/operator identity for manual or semi-manual runs.

Relationships:

- `prov:wasAssociatedWith`:
  - Activity ← Agent.  
- `prov:wasAttributedTo`:
  - Generated entities ← Agent, where applicable.

ID assignment rules (e.g., URIs) must be deterministic and documented in implementation, ensuring graph safety in Neo4j.

⸻

## 🧬 5. OpenLineage Model

The operator MUST emit OpenLineage events consistent with KFM lineage CI.

### 5.1 Job & Run

- **Job**:
  - `name` — stable, descriptive job name (e.g., `kfm.nodd.ingest.<dataset>`).  
  - `namespace` — KFM lineage namespace (e.g., `kfm-nodd`).

- **Run**:
  - `runId` — stable or GUID, linked to `wal_id` and/or `ingest_run_id`.

### 5.2 Datasets

Emit OpenLineage dataset records for:

- Input dataset:
  - Represents the source NODD object (or bucket prefix).  
- Output dataset:
  - Represents the STAC collection or collection+item combination, depending on granularity.

Attributes should mirror PROV-O/PROV entity attributes as far as the OpenLineage schema allows.

### 5.3 Idempotency

Emissions MUST be idempotent:

- Re-emitting for the same `(job, runId)` pair MUST NOT create duplicate lineage records.  
- Either:
  - Use OpenLineage’s own idempotency semantics, or  
  - Implement dedupe in the lineage store.

⸻

## 🧮 6. Determinism & Idempotency

The provenance-emit operator MUST satisfy:

- Determinism:
  - Same envelope + same config → identical PROV-O and OpenLineage payloads (modulo timestamp resolution where allowed).  
  - ID schemes (URIs, UUIDv5, etc.) MUST be derived from stable fields (e.g., dataset, object URI hash, time).

- Idempotency:
  - Multiple runs for the same ingest unit (same WAL entry) MUST NOT produce semantically duplicate provenance edges.  
  - Replays MUST either update existing Activities/Entities or be recognized as replays via attributes.

Any non-deterministic aspects (e.g., unseeded random UUIDs) are not allowed.

⸻

## 🚨 7. Error Handling & Partial Emission

### 7.1 Status Semantics

- `provenance_emit.status = ok`:
  - Both PROV-O and OpenLineage emissions succeeded.  

- `provenance_emit.status = partial`:
  - One emission path succeeded (e.g., PROV-O) while the other failed.  
  - Issues array MUST reflect which path failed.

- `provenance_emit.status = failed`:
  - Neither emission path succeeded.

### 7.2 Failure Behavior

On any failure:

- Do NOT roll back STAC writes; provenance errors do not invalidate data, but they do create reliability incidents.  
- Emit telemetry that allows lineage CI and governance to detect gaps.  
- The WAL and replay specs MUST support re-emitting provenance later without altering STAC.

Dataset-specific policy may define whether `partial` is tolerated temporarily or treated as a hard incident.

⸻

## 📊 8. Telemetry Contract

The operator contributes to NODD telemetry.

### 8.1 Spans

Recommended span name: `nodd_sns.provenance_emit`.

Required attributes:

- `nodd.dataset`  
- `nodd.object_uri_hash`  
- `nodd.stac_item_id`  
- `nodd.provenance_status` — `ok`, `failed`, `partial`  
- `nodd.prov_activity_id` (if emitted)  
- `nodd.openlineage_run_id` (if emitted)  

On failure, span status MUST be error with associated exception info.

### 8.2 Metrics

At minimum:

- `nodd_sns.provenance_emits_total{dataset, status}`  
- `nodd_sns.provenance_failures_total{dataset, path}`  

Where:

- `status` ∈ `{ok, failed, partial}`.  
- `path` ∈ `{prov_o, openlineage, both}` (low-cardinality).

Labels MUST remain low-cardinality and avoid object-level identifiers.

⸻

## ⚙️ 9. Configuration Hooks

The operator is driven by logical configuration in:

- `docs/pipelines/lineage/ingestion-lineage/` (global lineage patterns).  
- `docs/pipelines/atmo/nodd-sns-sqs/config/datasets/*.yaml` (dataset-specific lineage settings).

Configurable aspects include:

- ID schemes:
  - URI prefixes, UUID strategies (e.g., UUIDv5 seeds).  
- Namespace mappings:
  - OpenLineage namespaces, graph namespaces.  
- Emission toggles:
  - Allow/require PROV-O, OpenLineage, or both.  
- Governance profiles:
  - Additional constraints for sensitive datasets.

Unknown or invalid configuration MUST be caught during CI validation and treated as errors.

⸻

## 🧪 10. Testing & CI Requirements

CI MUST validate provenance-emit behavior with:

- Happy-path tests:
  - For each key dataset, a complete envelope → `provenance_emit.status = ok` with valid IDs and payloads.

- Idempotency tests:
  - Multiple calls for the same WAL entry → no duplicate Activities/Entities/lineage edges.

- Partial-failure tests:
  - Simulated failure in PROV store or OpenLineage endpoint → `status = partial`, `issues` accurate.

- Determinism tests:
  - Same envelope + config → identical IDs and payloads across runs.

- Config tests:
  - Invalid ID strategy or namespace mapping → CI failure before deployment.

Any semantic change to provenance mappings or ID schemes MUST update this contract and the test suite.

⸻

## 📘 11. Version History

| Version  | Date       | Notes                                                                                                     |
|---------:|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial KFM-MDP v11.2.3-aligned provenance-emit operator contract for NODD SNS → SQS ingestion pipeline. |

---

<div align="center">

📚 NODD Provenance Emit Operator · KFM v11.2.3  

Lineage-Safe · PROV-O + OpenLineage · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Operators](README.md) ·  
[🗺️ STAC Register](stac-register.md) ·  
[🔗 Lineage Pipelines Index](../../../lineage/README.md) ·  
[⚖ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>