---
title: "🧬 KFM v11.2.3 — NODD Metadata Extract Operator Contract (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed contract and behavior specification for the metadata-extract operator in the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/operators/metadata-extract.md"

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
intent: "nodd-metadata-extract-operator"
category: "Pipelines · Atmospheric · Operators"

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
sunset_policy: "Superseded by next major NODD metadata-extract contract"

header_profile: "standard"
footer_profile: "standard"
---

# 🧬 NODD Metadata Extract Operator — Contract  

`docs/pipelines/atmo/nodd-sns-sqs/operators/metadata-extract.md`

The **metadata-extract** operator derives **spatial, temporal, product, and platform metadata** from NOAA NODD objects and their headers, preparing a **STAC-ready envelope** for the `stac-register` operator.

It is:

- Deterministic — same object + envelope + config → same derived metadata.  
- Idempotent — repeat runs do not change external state (read-only w.r.t. data stores).  
- Standards-aligned — outputs map directly into STAC, GeoJSON, GeoSPARQL, OWL-Time, and KFM graph models.

This operator executes after `integrity-check` and before `stac-register`.

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

- `metadata-extract` MUST NOT run if `integrity.status = failed`.  
- `stac-register` MUST assume the envelope has passed through `metadata-extract`.  
- All metadata needed for STAC Item construction MUST be produced here (or explicitly marked as unavailable).

⸻

## 📥 2. Input Contract

The operator consumes an **envelope enriched by message-parse and integrity-check**.

### 2.1 Required Fields from Upstream

From `message-parse`:

- `event_time`  
- `dataset`  
- `object_uri`  
- `provider`  
- `time_range.start` / `time_range.end`  
- `priority`  
- `schema_version`

From `integrity-check`:

- `integrity.status` — must be `ok` or `suspect` (never `failed`).  
- `integrity.actual_size_bytes` (where available).  
- `integrity.actual_etag` (where available).  
- `integrity.issues` (for awareness; may guide stricter extraction behavior).

### 2.2 Object Access

The operator may:

- Reuse an already-fetched object handle (if provided upstream), or  
- Perform read-only access (e.g., partial reads, header reads, sidecar downloads) as required.

No modifications to the underlying object or bucket contents are allowed.

If essential metadata cannot be obtained due to access issues, the operator must mark the extraction as failed or suspect per configuration.

⸻

## 📤 3. Output Contract — Extracted Metadata & STAC Properties

The operator returns the **same envelope**, enriched with:

- `metadata_extract.status`  
  - One of: `ok`, `failed`, `suspect`.

- `metadata_extract.issues`  
  - Array of issue codes, e.g.:
    - `["missing_geolocation"]`, `["invalid_time_range"]`, `["incomplete_product_metadata"]`.

- `metadata_extract.checks_run`  
  - List of checks applied, e.g.:
    - `["temporal", "spatial", "product", "platform", "coverage"]`.

- `geometry`  
  - GeoJSON geometry representing the spatial footprint (e.g., Polygon, MultiPolygon, Point).

- `bbox`  
  - `[minLon, minLat, maxLon, maxLat]` bounding box.

- `stac_properties`  
  - A dictionary of STAC-compliant properties, including at least:
    - `datetime` (or `start_datetime` / `end_datetime` where appropriate).  
    - Dataset-specific STAC extension fields (e.g., `sat:*`, `eo:*`, `proj:*`, `raster:*`).  
    - Product identifiers, platform identifiers, processing-level attributes.

Downstream, `stac-register` uses `geometry`, `bbox`, and `stac_properties` directly when constructing STAC Items.

⸻

## 🧱 4. Derived Metadata Categories

### 4.1 Temporal Metadata

The operator MUST derive:

- Primary `datetime` for STAC:
  - Usually the mid-point of `time_range`, or dataset-defined time (e.g., observation time, model valid time).  
- Optional `start_datetime` and `end_datetime`:
  - From `time_range.start` and `time_range.end`.  

Rules:

- If time fields are inconsistent (e.g., end before start), mark:
  - `metadata_extract.status = failed` or `suspect` per config.  
  - Issue `invalid_time_range`.

### 4.2 Spatial Metadata

The operator MUST derive:

- `geometry` — spatial footprint in GeoJSON.  
- `bbox` — bounding box.

Sources may include:

- Sidecar metadata files.  
- Object headers.  
- Filename patterns (e.g., tile identifiers) plus dataset lookups.  

Rules:

- Geometry must be valid (no self-intersection) or normalized when feasible.  
- If spatial metadata is missing or invalid and dataset requires it:
  - Mark appropriate issues (`missing_geolocation`, `invalid_geometry`).  
  - Behavior (`failed` vs `suspect`) is controlled by config.

### 4.3 Product-Level Metadata

Examples include:

- Product code (e.g., for GOES/NEXRAD/HRRR).  
- Channel/band identifiers.  
- Scan mode, elevation angle, radar volume type.  
- Model run ID and forecast hour.

These are mapped into `stac_properties` using dataset-specific rules described in configuration, and may also be mirrored into graph properties for later KFM ingestion.

### 4.4 Platform & Instrument Metadata

Derive:

- Platform identifiers (e.g., GOES-East vs GOES-West, station IDs).  
- Instrument identifiers or radar site codes.  
- Optional orbit/scan metadata, where applicable.

These must be normalized against canonical KFM platform/instrument vocabularies when configuration provides mappings.

### 4.5 Quality & Coverage Metrics

Where available, the operator may derive:

- Cloud cover estimates or coverage fractions.  
- Spatial completeness indicators.  
- Internal quality flags consolidated into a small set of standard fields.

These are attached either as part of `stac_properties` or as separate fields referenced in configuration.

⸻

## 🧮 5. Determinism & Idempotency

The metadata-extract operator MUST be:

- Deterministic:
  - For the same `object_uri`, `dataset`, `integrity` results, and configuration:
    - `geometry`, `bbox`, `stac_properties`, and `metadata_extract.*` MUST be identical across runs.  
  - Coordinate rounding and temporal normalization strategies must be fixed and documented.

- Idempotent:
  - The operator only reads object content/metadata, never writes to buckets or catalogs.  
  - Telemetry emission is acceptable and must tolerate repeated runs.

Any inherently non-deterministic source (e.g., statistically derived quality metrics) must be:

- Either disabled for this operator, or  
- Made deterministic (e.g., fixed sampling offsets, deterministic windows).

⸻

## 🚨 6. Error Handling & Status Semantics

### 6.1 `metadata_extract.status = ok`

Conditions:

- All required temporal, spatial, product, and platform metadata derived successfully.  
- No critical issues encountered.

Downstream:

- `stac-register` may treat the envelope as fully ready for Item creation.

### 6.2 `metadata_extract.status = suspect`

Conditions (examples):

- Geometry simplified or normalized due to minor issues.  
- Some non-critical metadata fields missing or inconsistent (per dataset config).  
- Coverage metrics incomplete but not required.

Downstream:

- `stac-register` may still proceed.  
- QA and governance stages MUST be able to see `metadata_extract.issues` and decide whether to elevate.

### 6.3 `metadata_extract.status = failed`

Conditions (examples):

- No valid geometry for a dataset that requires spatial footprints.  
- Invalid or inconsistent time range that cannot be corrected.  
- Missing essential product identifiers (e.g., cannot determine band, product type).

Downstream:

- Envelope MUST be quarantined (DLQ or replay path).  
- `stac-register` MUST NOT attempt to create or update Items for this unit.

⸻

## 📊 7. Telemetry Contract

The operator contributes to the NODD telemetry model.

### 7.1 Spans

Recommended span name: `nodd_sns.metadata_extract`.

Required attributes:

- `nodd.dataset`  
- `nodd.object_uri_hash` (hashed/truncated URI for privacy)  
- `nodd.metadata_status` — `ok`, `failed`, `suspect`  
- `nodd.metadata_issues` — compact list or encoded representation of issue codes  

Errors MUST mark the span as error and include exception details where appropriate.

### 7.2 Metrics

At minimum:

- `nodd_sns.metadata_extract_total{dataset, status}`  
- `nodd_sns.metadata_extract_failures_total{dataset, issue}`  

Where:

- `status` ∈ `{ok, failed, suspect}`.  
- `issue` is a low-cardinality bucket (e.g., `missing_geolocation`, `invalid_time_range`, `product_metadata_incomplete`).

Labels MUST be low-cardinality; object-level identifiers are not allowed as metric labels.

⸻

## ⚙️ 8. Configuration Hooks

The operator is driven by logical configuration declared in:

- `docs/pipelines/atmo/nodd-sns-sqs/config/datasets/*.yaml`  

Configurable aspects include:

- Temporal rules:
  - Which fields to use for `datetime`, `start_datetime`, `end_datetime`.  
  - Handling of missing or partial time information.

- Spatial rules:
  - Source of footprints (sidecars, headers, filename patterns).  
  - Simplification/normalization strategies.  
  - Requirements for valid geometry and bbox.

- Product/platform rules:
  - Mapping from raw metadata fields to canonical product and platform identifiers.  
  - Required vs optional product metadata.

- Issue severity mapping:
  - Mapping of `metadata_extract.issues` codes to `ok` vs `suspect` vs `failed`.

Unknown or invalid configuration MUST be caught in CI validation and treated as configuration errors prior to deployment.

⸻

## 🧪 9. Testing & CI Requirements

CI MUST include tests that validate metadata-extract behavior:

- Happy-path:
  - For each supported dataset:
    - Valid object metadata → `metadata_extract.status = ok`, with valid `geometry`, `bbox`, and `stac_properties`.

- Missing or invalid spatial metadata:
  - No geometry available or invalid geometry → issue codes and status behavior match configuration.

- Temporal edge cases:
  - Out-of-order times, missing end time, or mismatched fields → status and issues as configured.

- Product/platform completeness:
  - Missing essential product code or platform ID → correctly marked as `failed` or `suspect`.

- Determinism:
  - Same envelope + mocked object metadata + config → identical derived metadata across runs.

Any change to metadata extraction logic or envelope schema MUST:

- Update this contract if semantics change.  
- Update or extend the test suite to cover new behaviors.

⸻

## 📘 10. Version History

| Version  | Date       | Notes                                                                                                 |
|---------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial KFM-MDP v11.2.3-aligned metadata-extract operator contract for NODD SNS → SQS ingestion.     |

---

<div align="center">

🧬 NODD Metadata Extract Operator · KFM v11.2.3  

Deterministic · STAC-Ready · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Operators](README.md) ·  
[✉️ Message Parse](message-parse.md) ·  
[🛡️ Integrity Check](integrity-check.md) ·  
[🗺️ STAC Register](stac-register.md) ·  
[⚖ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>