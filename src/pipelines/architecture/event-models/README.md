---
title: "📨 Kansas Frontier Matrix — Pipeline Event Models (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/event-models/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-event-models-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📨 **Kansas Frontier Matrix — Pipeline Event Models**  
`src/pipelines/architecture/event-models/README.md`

**Purpose:**  
Define the **canonical event envelope structures** used across all Kansas Frontier Matrix (KFM) pipelines — ingestion, ETL, AI, metadata, geospatial processing, Story Nodes, STAC/DCAT publication, and governance operations.  
These event models ensure **idempotency**, **replayability**, **traceability**, **FAIR+CARE safety**, and **SLSA-grade provenance** across the entire system.

</div>

---

## 📘 Overview

KFM uses an **event-driven pipeline mesh**, where every action — from downloading NOAA rasters to publishing Story Nodes — is triggered by a fully-typed **event envelope**.

This document defines:

- Event schema requirements  
- Envelope fields  
- CARE/ethics metadata  
- Provenance linkage  
- Validation rules  
- Trigger patterns  
- Versioning of events  
- Compatibility across distributed services  

Every event must be **strictly validated**, **governance-checked**, and **telemetry-logged** before pipeline execution continues.

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/architecture/event-models/
├── README.md                    # This file
├── schemas/                     # JSON Schemas for events
├── examples/                    # Example envelopes
└── validators/                  # Pydantic/JSONSchema validation modules
~~~~~

---

## 🧩 Event Model Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Trigger (Webhook · Cron · STAC Update · Dispatch)"] --> B["Event Envelope"]
  B --> C["Validator<br/>JSONSchema · Pydantic"]
  C --> D["Governance Layer<br/>CARE · License · Sovereignty"]
  D --> E["Pipeline Orchestrator<br/>ETL · AI · Geospatial"]
  E --> F["Telemetry Export<br/>Validation · Energy · Provenance"]
  F --> G["Governance Ledger<br/>Append-Only Entry"]
~~~~~

---

## 📨 1. Event Envelope Specification (Required v10.3)

Every event JSON must include the following **required fields**:

| Field | Type | Description |
|-------|------|-------------|
| `event_id` | string | UUIDv4 |
| `event_type` | enum | `"ingest" | "etl" | "ai" | "metadata" | "storynode" | "publish" | "governance"` |
| `timestamp` | ISO8601 | Event creation time (UTC) |
| `dataset_id` | string | Dataset being processed |
| `version` | string | Semantic version string |
| `source_uri` | string | Original data location |
| `idempotency_key` | string | Deterministic dedupe key |
| `correlation_id` | string | Trace ID for distributed tracing |
| `pipeline` | string | Pipeline name |
| `care_label` | enum | `"public" | "sensitive" | "restricted"` |
| `parameters` | object | Pipeline parameters/config |
| `provenance` | object | Input lineage summary |
| `auth_context` | object | Optional (system identity / OIDC claims) |

---

## 🧱 2. Required CARE/Sovereignty Metadata

Every event MUST include:

~~~~~json
{
  "care_label": "sensitive",
  "sovereignty": {
    "tribal_authority": "Kanza Nation",
    "review_status": "required",
    "masking": "h3_r7"
  }
}
~~~~~

**Rules:**

- `restricted` labels cannot proceed without governance approval  
- `sensitive` labels force masking and metadata review  
- All sovereignty notes written to ledger  

---

## 📦 3. Provenance Block Specification

The `provenance` field must capture:

| Field | Description |
|-------|-------------|
| `source_ids` | Input STAC/DCAT dataset IDs |
| `source_checksums` | sha256 inputs |
| `lineage_refs` | Prior lineage files |
| `tools` | Software versions (GDAL, spaCy, transformers) |
| `derived_from` | Previous dataset versions |

Example:

~~~~~json
{
  "source_ids": ["noaa_storms_1950_2025"],
  "source_checksums": ["sha256:aaa..."],
  "tools": {
    "python": "3.11.5",
    "gdal": "3.12.0"
  }
}
~~~~~

---

## 🧪 4. Event Validation Rules

Events MUST pass:

- JSON Schema validation  
- Pydantic structural validation  
- License compliance checks  
- CARE compliance checks  
- Sovereignty-metadata presence  
- Idempotency key recomputation  
- Replay safety verification  

If **any validation fails** → pipeline stops immediately.

---

## ⚙️ 5. Event Types (Canonical)

### 1. `ingest`
Triggered when raw data is discovered.

### 2. `etl`
Transformation (OCR, NER, raster processing, etc.).

### 3. `ai`
AI/ML tasks (summaries, embeddings, explanations).

### 4. `metadata`
STAC/DCAT generation, schema extraction.

### 5. `storynode`
Create Story Nodes & narrative linkage.

### 6. `publish`
Publication to catalogs, Neo4j, or processed datasets.

### 7. `governance`
FAIR+CARE reviews, overrides, compliance runs.

---

## 📘 6. Example Event Envelope (v10.3.1)

~~~~~json
{
  "event_id": "92f09bd1-d66a-4f30-99c5-d1884ddfd3bb",
  "event_type": "etl",
  "timestamp": "2025-11-13T22:44:12Z",
  "dataset_id": "hydrology_flow_ks",
  "version": "v10.3.1",
  "source_uri": "https://noaa.gov/hydro/file_2025.tif",
  "idempotency_key": "sha256:93ab2333e9f...",
  "correlation_id": "b1a8c66e-e389-4c0a-9d74-8b620fe62ee5",
  "pipeline": "hydrology_flow",
  "care_label": "public",
  "parameters": {
    "reprojection": "EPSG:4326",
    "window": "full"
  },
  "provenance": {
    "source_ids": ["noaa_hydro_archive"],
    "source_checksums": ["sha256:448bbf..."],
    "tools": {
      "python": "3.11.5",
      "gdal": "3.12.0"
    }
  }
}
~~~~~

---

## 🧠 7. Example `restricted` Event (Governance Required)

~~~~~json
{
  "event_id": "f1f12bb1-b1e1-4d9f-a95d-431343f7af09",
  "event_type": "ingest",
  "timestamp": "2025-11-13T15:21:08Z",
  "dataset_id": "ks_archaeology_sensitive",
  "version": "v10.3.1",
  "source_uri": "s3://tribal-archive/private/ks-sites.geojson",
  "idempotency_key": "sha256:bfcc9e...",
  "correlation_id": "3c71c3ab-f201-493c-bc3c-18c3d88c79ad",
  "pipeline": "archaeology_ingest",
  "care_label": "restricted",
  "sovereignty": {
    "tribal_authority": "Prairie Band Potawatomi Nation",
    "review_status": "required",
    "masking": null
  },
  "parameters": {},
  "provenance": {
    "source_ids": ["tribal_archive_2025"],
    "source_checksums": ["sha256:99f11..."],
    "tools": {
      "python": "3.11.5"
    }
  }
}
~~~~~

---

## 📡 8. Telemetry Requirements

Every event must contribute to pipeline telemetry:

| Field | Description |
|--------|-------------|
| `retry_attempts` | retry count |
| `validation_errors` | failed checks |
| `care_label` | public/sensitive/restricted |
| `energy_wh` | sustainability |
| `co2_g` | sustainability |
| `pipeline_id` | linked run ID |
| `governance_ref` | pointer to ledger |

Stored in:

```
../../../../../releases/v10.3.0/focus-telemetry.json
```

---

## 🛡️ 9. Governance Ledger Output

Each validated event writes an immutable entry:

```
docs/reports/audit/event_ledger.json
```

Event ledger entry includes:

- event_id  
- dataset_id  
- pipeline  
- care_label  
- reviewer (if applicable)  
- sovereignty notes  
- compliance decision  
- telemetry hash  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|---------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Event model library finalized for v10.3; added sovereignty block, CARE enforcement, Pydantic v2 schema. |
| v10.2.2 | 2025-11-12 | Pipeline Architecture Team | Initial event envelope standard introduced. |

---

<div align="center">

**Kansas Frontier Matrix — Pipeline Event Models**  
Deterministic Events × Ethical Governance × Immutable Provenance  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Pipeline Architecture](../README.md)

</div>