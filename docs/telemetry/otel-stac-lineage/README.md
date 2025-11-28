---
title: "📡 KFM v11.2.2 — OpenTelemetry + STAC Lineage Schema (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/otel-stac-lineage/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Telemetry & Reliability · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../releases/v11.2.2/telemetry-otel-stac-lineage.json"
telemetry_schema: "../../../schemas/telemetry/otel-stac-lineage-v11.2.2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Operational Telemetry"
sensitivity_level: "None"
public_exposure_risk: "Low"

scope:
  domain: "telemetry"
  applies_to:
    - "otel"
    - "stac-lineage"
    - "orchestrators"
    - "energy-carbon"

semantic_intent:
  - "otel-schema"
  - "stac-lineage"
  - "reliability-telemetry"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:otel-stac-lineage:v11.2.2"
semantic_document_id: "kfm-telemetry-otel-stac-lineage-v11.2.2"
event_source_id: "ledger:telemetry-otel-stac-lineage-v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 📡 **KFM v11.2.2 — OpenTelemetry + STAC Lineage Schema**  
`docs/telemetry/otel-stac-lineage/README.md`

**Purpose**  
Define a **single, enforced OpenTelemetry span-attribute schema** that carries **STAC-based lineage, FAIR+CARE metadata, and reliability context** across:

- 🌀 Airflow DAGs  
- 🧠 LangGraph / agentic pipelines  
- 🪣 lakeFS / object-versioning events  
- 🌐 Any future orchestrator that can emit OTel traces

</div>

---

## 🧩 1. Scope & Goals

This standard governs **how KFM emits OpenTelemetry spans** whenever a component:

- Reads, transforms, or writes **STAC Collections / Items / Assets**  
- Mutates **versioned data** via lakeFS or equivalent storage backends  
- Performs **lineage-sensitive operations** that must be auditable by the FAIR+CARE Council  

It answers, for every span:

1. **What STAC resource is in play?**  
2. **Where did it come from and where is it going?** (lineage)  
3. **Under which reliability, ethics, and energy/carbon envelope did it run?**  

This schema is **normative**. If you are emitting spans for KFM datasets, you MUST:

- Implement all **required** fields, and  
- NOT redefine these keys with incompatible semantics  

Exceptions require a registered **governance exception** in:

- `docs/standards/governance/ROOT-GOVERNANCE.md`

---

## 🗂️ 2. Directory Layout

    docs/telemetry/otel-stac-lineage/
    ├── 📄 README.md                          # This spec (you are here)
    ├── 📁 examples/                          # Concrete JSON span examples
    │   ├── 📄 airflow-task-span.json         # Example Airflow DAG task span
    │   ├── 📄 langgraph-node-span.json       # Example LangGraph node span
    │   └── 📄 lakefs-commit-span.json        # Example lakeFS commit span
    └── 📁 diagrams/                          # Optional mermaid diagrams
        └── 📄 otel-stac-lineage-flow.md      # Orchestrator → OTel → Backend overview

Implementation references (non-normative but recommended):

    src/telemetry/
    ├── 📜 otel_stac_lineage.py               # Attribute helpers and validators
    └── 📁 exporters/
        └── 📜 otel_stac_lineage_exporter.py  # Optional custom processors/exporters

---

## 🧾 3. Attribute Schema (Canonical Keys)

### 3.1 Overview

All attributes below are **string-typed unless noted**.

Type shorthand:

- `str` – UTF-8 string  
- `int` – integer  
- `float` – floating-point number  
- `bool` – boolean  
- `json` – JSON-encoded string (e.g., `["item1","item2"]`)  

For each attribute we specify:

- **Req.** — `R` required, `C` conditionally required, `O` optional  
- **Domain** — `STAC`, `Lineage`, `Ethics`, `Geo`, `Energy`, `Reliability`, `Governance`  

---

### 3.2 STAC Identity Attributes

| Attribute         | Type | Req. | Domain | Example                                 | Notes                       |
|-------------------|------|------|--------|------------------------------------------|-----------------------------|
| `stac.collection` | str  | R    | STAC   | `"kfm-hydrology-kansas-river"`          | STAC Collection ID.         |
| `stac.item`       | str  | R    | STAC   | `"kansas-river-2024-08-01-hrrr-wind"`   | STAC Item ID.               |
| `stac.version`    | str  | C    | STAC   | `"1.0.0-kfm-v11"`                       | Required if versioned.      |
| `stac.asset_role` | str  | C    | STAC   | `"data"`, `"thumbnail"`, `"metadata"`   | Use STAC roles.             |
| `stac.asset_href` | str  | C    | STAC   | `"s3://kfm/hydrology/.../asset.parquet"`| URI/URL to asset.           |

**Rules**

- If a span **touches a specific STAC Item**, set `stac.collection` and `stac.item`.  
- If the span is **collection-level** only, `stac.collection` is still required; `stac.item` MAY be omitted.  
- For **asset-specific** operations, set both `stac.asset_role` and `stac.asset_href`.

---

### 3.3 Lineage Attributes

| Attribute               | Type | Req. | Domain   | Example                                             | Notes                                    |
|-------------------------|------|------|----------|-----------------------------------------------------|------------------------------------------|
| `lineage.parent_items`  | json | C    | Lineage  | `["kfm-hrrr-2024-08-01T00Z-wind","noaa-hrrr-raw"]` | JSON array of upstream STAC Item IDs.    |
| `lineage.parent_assets` | json | O    | Lineage  | `["s3://.../raw.grib2","s3://.../mask.geojson"]`    | Optional explicit upstream asset URIs.   |

**Rules**

- If a span **produces or mutates** data, `lineage.parent_items` SHOULD list the logical upstream items.  
- For read-only spans, `lineage.parent_items` is recommended but not mandatory.

---

### 3.4 Data Integrity & Size

| Attribute          | Type | Req. | Domain  | Example                      | Notes                                      |
|--------------------|------|------|---------|------------------------------|--------------------------------------------|
| `data.hash.sha256` | str  | C    | Lineage | `"e3b0c44298fc1c14..."`      | SHA-256 of the **primary output** asset.   |
| `data.bytes`       | int  | O    | Lineage | `524288000`                  | Total bytes written/read.                  |
| `data.encoding`    | str  | O    | Lineage | `"parquet"`, `"zarr"`        | Logical encoding/format.                   |

**Rules**

- For **write** spans, `data.hash.sha256` is strongly recommended and required in governed release pipelines.  

---

### 3.5 Geospatial & Temporal Context

| Attribute            | Type | Req. | Domain | Example                                              | Notes                          |
|----------------------|------|------|--------|------------------------------------------------------|--------------------------------|
| `geo.crs`            | str  | O    | Geo    | `"EPSG:4326"`                                        | Horizontal CRS.                |
| `geo.vertical_datum` | str  | C    | Geo    | `"NAVD88"`                                           | Required for vertical data.    |
| `time.interval`      | str  | O    | Geo    | `"2024-08-01T00:00:00Z/2024-08-01T01:00:00Z"`       | ISO-8601 time interval.        |

**Rules**

- `geo.vertical_datum` MUST conform to `docs/standards/geo/vertical-axis-and-dod.md`.  

---

### 3.6 FAIR+CARE & Privacy Attributes

| Attribute         | Type | Req. | Domain | Example                          | Notes                                        |
|-------------------|------|------|--------|----------------------------------|----------------------------------------------|
| `care.label`      | str  | C    | Ethics | `"Public"`, `"Sensitive-Heritage"`| CARE label at time of operation.            |
| `care.scope`      | str  | O    | Ethics | `"Tribal-partner-X-only"`       | Human-readable scope text.                   |
| `privacy.masking` | str  | C    | Ethics | `"h3_generalized"`, `"none"`    | Required for any spatially sensitive data.   |

**Rules**

- For heritage / Indigenous-related spans, `care.label` MUST NOT be empty and masking MUST follow H3 policies.

---

### 3.7 Governance & Policy

| Attribute                 | Type | Req. | Domain      | Example                            | Notes                             |
|---------------------------|------|------|-------------|------------------------------------|-----------------------------------|
| `governance.policy_id`    | str  | C    | Governance  | `"KFM-PA-001"`                     | Policy ID governing this span.    |
| `governance.approval_ref` | str  | O    | Governance  | `"council/minutes/2025-11-01#3"`   | Pointer to approvals / RFCs.      |

**Rules**

- Release or publish-type spans MUST set `governance.policy_id`.

---

### 3.8 Reliability & WAL Context

| Attribute            | Type | Req. | Domain       | Example                             | Notes                         |
|----------------------|------|------|--------------|-------------------------------------|-------------------------------|
| `reliability.retry`  | int  | O    | Reliability  | `0`, `1`, `2`                       | Attempt index.                |
| `reliability.wal_id` | str  | O    | Reliability  | `"wal-2025-11-28T02:31:44Z-01"`     | WAL / transaction ID.         |
| `slo.step_kind`      | str  | O    | Reliability  | `"ingest"`, `"transform"`, `"publish"` | Logical pipeline step name. |

---

### 3.9 Energy & Carbon Telemetry

| Attribute                | Type  | Req. | Domain | Example | Notes                  |
|--------------------------|-------|------|--------|---------|------------------------|
| `energy.kwh_estimate`    | float | O    | Energy | `0.023` | kWh estimate.          |
| `carbon.gco2e_estimate`  | float | O    | Energy | `12.4`  | grams CO₂e estimate.   |

**Rules**

- When the energy/carbon estimator is enabled, both attributes SHOULD be populated and aligned with the schemas in `energy_schema` and `carbon_schema`.

---

## 🔌 4. Orchestrator Integration Patterns

This section provides implementation guidance for common orchestrators.

### 4.1 Airflow Tasks

Applicable to:

- `@task` / `PythonOperator` / `TaskFlow` tasks that read/write KFM STAC assets.

Recommended attributes:

- `stac.collection`, `stac.item`  
- `lineage.parent_items` (for writers)  
- `reliability.retry`, `slo.step_kind`  
- `governance.policy_id` for release-type tasks  

### 4.2 LangGraph Nodes

Applicable to:

- LangGraph nodes performing enrichment, summarization, or AI interpretations using KFM data.

Recommended attributes:

- `stac.collection`, `stac.item`  
- `care.label`, `privacy.masking`  
- `slo.step_kind = "interpretation"` (or similar)  

### 4.3 lakeFS Hooks / Commit Events

Applicable to:

- lakeFS post-commit hooks or ingest events.

Recommended attributes:

- `stac.collection`, `stac.item`  
- `lineage.parent_items`  
- `data.hash.sha256`, `data.bytes`  
- `governance.policy_id`  

---

## 📚 5. Validation & Conformance

1. **JSON Schema**  
   - `telemetry_schema` defines these attributes and types.  
   - Additional attributes are allowed but MUST NOT override these keys with different semantics.

2. **CI Conformance**  
   - Example spans in `examples/` are validated against the schema.  
   - Pipelines that advertise v11.2.2 conformance MUST run a telemetry conformance test in CI.

3. **Evolution Rules**  
   - Adding new optional attributes → **minor** version bump.  
   - Changing requiredness or semantics of existing attributes → **major** version bump (v12+), with explicit migration guidance.

---

## 🎭 6. Story Node & Focus Mode Integration

When traces inform narratives:

- Story Nodes SHOULD link back to the originating trace via a **trace ID** or equivalent.  
- Narrative layers MUST NOT alter CARE labels or privacy settings; they can only surface them.  
- Focus Mode v3 may aggregate spans by:
  - `stac.collection`, `stac.item`  
  - `slo.step_kind` (ingest → transform → publish → visualize)  
  - `care.label`  

The goal is to let reviewers navigate from **story → trace → dataset** and verify lineage.

---

## 🕰️ 7. Version History

| Version  | Date       | Notes                                                                 |
|----------|------------|-----------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Upgraded to KFM-MDP v11.2.2; added energy/carbon v2 schema alignment |
| v11.1.0  | 2025-11-20 | Initial Diamond⁹ Ω / Crown∞Ω-certified release of OTel+STAC schema   |

---

<div align="center">

[📡 Telemetry Home](../README.md) · [📚 Standards](../../standards/README.md) · [📦 STAC Catalog](../../data/stac/)

</div>
