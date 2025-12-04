---
title: "🗺️ KFM v11.2.3 — NODD STAC Register Operator Contract (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed contract and behavior specification for the stac-register operator in the NOAA NODD SNS → SQS ingestion pipeline, performing deterministic, atomic STAC Item/Collection writes."
path: "docs/pipelines/atmo/nodd-sns-sqs/operators/stac-register.md"

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
intent: "nodd-stac-register-operator"
category: "Pipelines · Atmospheric · Operators · STAC"

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
sunset_policy: "Superseded by next major NODD STAC register contract"

header_profile: "standard"
footer_profile: "standard"
---

# 🗺️ NODD STAC Register Operator — Contract  

`docs/pipelines/atmo/nodd-sns-sqs/operators/stac-register.md`

The **stac-register** operator is responsible for turning a fully validated NODD ingest envelope into a **STAC Item** (and associated Collection updates) using:

- Deterministic STAC Item IDs.  
- Atomic write/validate/promote semantics.  
- KFM STAC profile validation.  
- Idempotent create/update behavior aligned with WAL and auto-update contracts.

It is the **only** operator in the NODD SNS → SQS pipeline allowed to mutate the STAC catalog.

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

- `stac-register` MUST NOT run if:
  - `integrity.status = failed`, or  
  - `metadata_extract.status = failed`.  

- `provenance-emit` MUST assume that STAC registration has already completed (or decided a `no-op`).  
- No other operator may directly write STAC Items or Collections for NODD ingestion.

⸻

## 📥 2. Input Contract

The operator consumes an envelope enriched by `message-parse`, `integrity-check`, and `metadata-extract`.

### 2.1 Required Upstream Fields

From `message-parse`:

- `event_time`  
- `dataset`  
- `object_uri`  
- `provider`  
- `time_range.start` / `time_range.end`  
- `priority`  
- `schema_version`

From `integrity-check`:

- `integrity.status` — must be `ok` or `suspect`.  
- `integrity.actual_size_bytes` (if available).  
- `integrity.actual_etag` (if available).

From `metadata-extract`:

- `metadata_extract.status` — must be `ok` or `suspect`.  
- `geometry` — GeoJSON geometry.  
- `bbox` — `[minLon, minLat, maxLon, maxLat]`.  
- `stac_properties` — dictionary of STAC-ready properties (including time, product, platform, etc.).

From configuration (resolved before or inside this operator):

- `stac_collection_id` — canonical Collection ID for the dataset.  
- Catalog root / base HREF and path layout (logical spec).

From WAL / runtime context:

- `wal_id` — WAL entry for this ingest unit (required for WAL-backed pipelines).  
- `ingest_run_id` — pipeline run identifier (optional but recommended).

If any required field or configuration is missing, the operator MUST treat the envelope as **not eligible** for STAC registration and surface a hard failure.

⸻

## 📤 3. Output Contract — STAC Write Results

The operator returns the same envelope, enriched with STAC write metadata:

- `stac_item_id`  
  - Deterministic ID for the STAC Item (details in section 4).  

- `stac_collection_id`  
  - Collection ID used for the Item (from config).  

- `stac_item_href`  
  - Canonical HREF/URI of the Item within the STAC catalog.  

- `stac_write_status`  
  - One of:
    - `created` — new Item created.  
    - `updated` — existing Item modified.  
    - `no-op` — Item already up-to-date; no change applied.  
    - `failed` — STAC write attempted but failed (downstream operators must treat as non-ingested).

- `stac_register.status`  
  - One of:
    - `ok` — STAC write succeeded (`created`, `updated`, or `no-op`).  
    - `failed` — STAC write failed.  

- `stac_register.issues`  
  - Array of issue codes, e.g.:
    - `["stac_validation_failed"]`, `["catalog_conflict"]`, `["io_error"]`.

Downstream contract:

- `provenance-emit` MUST only proceed when `stac_write_status ∈ {created, updated, no-op}` and `stac_register.status = ok`.  
- If `stac_write_status = failed`, the ingest unit is considered **not registered** and must be eligible for replay.

⸻

## 🗺️ 4. STAC Item & Collection Construction

### 4.1 Item ID Strategy

`stac_item_id` MUST be:

- Deterministically derived from:
  - `dataset`  
  - `object_uri` (or a canonicalized key)  
  - Relevant temporal keys (e.g., `time_range.start`)  

KFM recommendation:

- Use a UUIDv5 or equivalent deterministic scheme with a fixed namespace seed and canonical input string.  

Example canonical key (conceptual):

    key = dataset + "|" + normalized_object_key + "|" + time_range.start

Item ID rules:

- No sensitive or high-cardinality raw identifiers (like full object keys) should be exposed if governance requires hashing or truncation.  
- Item IDs must be stable across replays and code versions (unless explicit ID migration is performed under governance).

### 4.2 Item JSON Construction

The operator constructs a valid STAC Item JSON object:

- Required fields:
  - `id` → `stac_item_id`.  
  - `type = "Feature"`.  
  - `geometry` → from envelope `geometry`.  
  - `bbox` → from envelope `bbox`.  
  - `properties` → `stac_properties` with at least:
    - `datetime` or `start_datetime`/`end_datetime`.  
    - Dataset-specific STAC extension fields.  

- `assets`:
  - At minimum:
    - Primary asset pointing to the NODD object (`object_uri`).  
  - May include:
    - Sidecar metadata, QA products, quicklooks, etc., per dataset config.

### 4.3 Collection Handling

- `stac_collection_id` must refer to an existing Collection or a Collection created ahead of time.  
- The operator may perform:
  - Extent updates (temporal/spatial) when allowed and configured.  
  - Summary updates (e.g., data coverage, counts), typically through batched or periodic processes (documented elsewhere).

Collection updates must be:

- Idempotent.  
- Validated against the KFM STAC Collection profile.

### 4.4 Validation & Profile Compliance

Before promotion to the canonical catalog, the Item MUST:

- Validate against:
  - STAC core schema.  
  - KFM STAC profile (extensions and required fields).  

Validation failures:

- Set `stac_write_status = failed`.  
- Record `stac_register.issues` (e.g., `stac_validation_failed`).  
- Prevent promotion to canonical catalog.

⸻

## 🧮 5. Determinism, Idempotency & Atomicity

The stac-register operator MUST satisfy:

### 5.1 Determinism

For a fixed:

- `dataset`  
- `object_uri` / canonical key  
- `time_range`  
- `geometry` and `stac_properties`  
- Configuration version  

the resulting:

- `stac_item_id`  
- Item JSON content (excluding internal metadata like last-modified if not controlled)  
- `stac_item_href`  

MUST be identical across runs.

### 5.2 Idempotency

Repeated invocations with the same envelope and object MUST:

- Not create duplicate Items.  
- Either:
  - Detect that the existing Item matches the candidate and set `stac_write_status = no-op`, or  
  - Update the Item only when acceptable differences exist (e.g., new fields added in a non-breaking way).

Item comparison strategy must be defined and tested (e.g., canonical JSON or schema-aware comparison).

### 5.3 Atomicity

STAC write sequence MUST follow:

1. Build candidate Item JSON.  
2. Write to a temporary location (e.g., staging bucket/path).  
3. Validate against schemas and KFM profile.  
4. On success:
   - Atomically promote to canonical catalog path (e.g., move/rename).  
5. On failure:
   - Remove or quarantine the temporary Item.  
   - Set `stac_write_status = failed`.

At no point should an invalid or incomplete Item be visible in the canonical STAC catalog.

⸻

## 🚨 6. Error Handling & Conflict Resolution

### 6.1 STAC Validation Errors

- Example issues:
  - Missing required fields.  
  - Invalid geometry or bbox.  
  - Extension fields not matching schema.

Handling:

- `stac_write_status = failed`.  
- Add `stac_register.issues += ["stac_validation_failed"]`.  
- Envelope routed to replay or incident path via higher-level orchestration.

### 6.2 Catalog Conflicts

Conflicts may arise when:

- Another process concurrently modifies the same Item.  
- Collection constraints are violated.

Handling:

- Detect using underlying storage semantics (e.g., conditional writes based on version or ETag).  
- On conflict:
  - `stac_write_status = failed`.  
  - Issue code `catalog_conflict`.  
  - Telemetry and incident review required.

### 6.3 IO or Storage Failures

- Network errors, storage unavailability, or permission errors should be treated as transient/infra issues.  
- Behavior:
  - Bounded retries.  
  - If still failing:
    - `stac_write_status = failed`.  
    - Issue `io_error` or `storage_unavailable`.

Under no circumstance should partial writes be treated as success.

⸻

## 📊 7. Telemetry Contract

The operator contributes to NODD telemetry and SLOs.

### 7.1 Spans

Recommended span name: `nodd_sns.stac_register`.

Required attributes:

- `nodd.dataset`  
- `nodd.object_uri_hash`  
- `nodd.stac_item_id`  
- `nodd.stac_collection_id`  
- `nodd.stac_write_status` — `created`, `updated`, `no-op`, `failed`  

On error:

- Span status MUST be set to error.  
- Include error type (e.g., `validation_error`, `io_error`, `catalog_conflict`).

### 7.2 Metrics

At minimum:

- `nodd_sns.stac_writes_total{dataset, outcome}`  

Where:

- `outcome` ∈ `{created, updated, no_op, failed}` (using a consistent naming convention).  

Optional metrics:

- `nodd_sns.stac_write_latency_seconds{dataset}` — histogram of STAC write durations.  

Metric labels MUST remain low-cardinality (dataset, outcome, environment).

⸻

## ⚙️ 8. Configuration Hooks

The operator is driven by configuration from:

- `docs/pipelines/atmo/nodd-sns-sqs/config/datasets/*.yaml`  
- Global STAC configuration (e.g., under `docs/data/stac/`, defined elsewhere)

Configurable aspects include:

- `stac_collection_id` and any per-dataset Collection details.  
- Item ID generation strategy (input keys, namespace seed).  
- Asset mapping rules:
  - How to map `object_uri` and sidecars into STAC assets.  
- Catalog layout rules:
  - Path templates for Items (e.g., `<dataset>/<year>/<day>/<item_id>.json`).  
- Validation and promotion rules:
  - Which validators must pass before promotion.

Configuration errors must be detected in CI and must not be allowed into production deployments.

⸻

## 🧪 9. Testing & CI Requirements

CI MUST validate stac-register behavior with:

- Happy-path tests:
  - For each major dataset:
    - Input envelope → valid STAC Item creation with `stac_write_status = created` and correct Item shape.

- Idempotency tests:
  - Second run with the same envelope:
    - `stac_write_status = no-op` or `updated` with well-defined and tested semantics.  

- Validation failure tests:
  - Intentionally malformed metadata → `stac_write_status = failed` and appropriate issue codes.

- Conflict tests (where feasible with mocks):
  - Simulated concurrent write or version mismatch → `catalog_conflict` issue and `failed` status.

- Determinism tests:
  - Same envelope + configuration → identical `stac_item_id`, Item content, and `stac_item_href`.

Any semantic change to STAC ID generation, asset mapping, or promotion rules MUST:

- Update this contract.  
- Update tests to assert new behavior.

⸻

## 📘 10. Version History

| Version  | Date       | Notes                                                                                                  |
|---------:|------------|--------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial KFM-MDP v11.2.3-aligned stac-register operator contract for NODD SNS → SQS ingestion pipeline. |

---

<div align="center">

🗺️ NODD STAC Register Operator · KFM v11.2.3  

Deterministic · Atomic · STAC-First · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Operators](README.md) ·  
[🧬 Metadata Extract](metadata-extract.md) ·  
[📚 Provenance Emit](provenance-emit.md) ·  
[📊 Telemetry & SLOs](../telemetry/README.md) ·  
[⚖ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>