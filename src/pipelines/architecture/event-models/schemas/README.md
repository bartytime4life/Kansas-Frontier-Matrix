---
title: "📐 Kansas Frontier Matrix — Pipeline Event Schema Definitions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/event-models/schemas/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/pipelines-event-schemas-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Pipeline Event Schema Definitions**  
`src/pipelines/architecture/event-models/schemas/README.md`

**Purpose:**  
Define the **canonical JSON Schema and validation contracts** for all event envelopes used in Kansas Frontier Matrix (KFM) pipelines — ingestion, ETL, AI, metadata, Story Nodes, governance, and publication.  
These schemas enforce **idempotency**, **FAIR+CARE compliance**, **sovereignty metadata**, and **SLSA-grade provenance** at the event layer.

<img alt="Docs" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue"/>
<img alt="License" src="https://img.shields.io/badge/License-MIT-green"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Schemas-success"/>

</div>

---

## 📘 Overview

All KFM pipeline activity is driven by **event envelopes** that MUST validate against **strict JSON Schemas** before any work executes.

These schemas:

- Ensure **structural correctness** (types, required fields, enums)  
- Enforce **governance requirements** (CARE labels, sovereignty metadata)  
- Guarantee **idempotency** (idempotency key, correlation IDs)  
- Bind events to **lineage and provenance** (source IDs, checksums, tools)  
- Align with **MCP-DL v6.3**, **FAIR+CARE**, and **pipeline_validation_standards**  

This directory hosts the **single source of truth** for event-level schemas.

---

## 📁 Directory Layout

~~~~~text
src/pipelines/architecture/event-models/schemas/
├── README.md                      # This file
├── base_event.schema.json         # Core envelope shared by all events
├── ingest_event.schema.json       # Ingestion-specific constraints
├── etl_event.schema.json          # ETL / transform-specific constraints
├── ai_event.schema.json           # AI & Focus Mode explainability events
├── metadata_event.schema.json     # STAC/DCAT metadata events
├── storynode_event.schema.json    # Story Node creation events
├── publish_event.schema.json      # Publication gate events
└── governance_event.schema.json   # FAIR+CARE / sovereignty review events
~~~~~

---

## 🧩 Schema Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Base Event Schema<br/>base_event.schema.json"]
    --> B["Ingest Event Schema<br/>ingest_event.schema.json"]
  A --> C["ETL Event Schema<br/>etl_event.schema.json"]
  A --> D["AI Event Schema<br/>ai_event.schema.json"]
  A --> E["Metadata Event Schema<br/>metadata_event.schema.json"]
  A --> F["Story Node Event Schema<br/>storynode_event.schema.json"]
  A --> G["Publish Event Schema<br/>publish_event.schema.json"]
  A --> H["Governance Event Schema<br/>governance_event.schema.json"]
~~~~~

---

## 📦 Base Event Schema Requirements

All event schemas MUST extend `base_event.schema.json`, which defines:

- `event_id` (UUID string)  
- `event_type` (enum)  
- `timestamp` (ISO8601 string)  
- `dataset_id` (string)  
- `version` (semantic version, x.y.z)  
- `source_uri` (URI string)  
- `idempotency_key` (string; sha256 hash)  
- `correlation_id` (string; trace ID)  
- `pipeline` (string; pipeline name)  
- `care_label` (`public`, `sensitive`, `restricted`)  
- `parameters` (object)  
- `provenance` (object; nested schema)  

### In JSON Schema Style (excerpt)

~~~~~json
{
  "$id": "https://kfm/schema/base_event.schema.json",
  "type": "object",
  "required": [
    "event_id",
    "event_type",
    "timestamp",
    "dataset_id",
    "version",
    "source_uri",
    "idempotency_key",
    "correlation_id",
    "pipeline",
    "care_label",
    "parameters",
    "provenance"
  ]
}
~~~~~

---

## 🧬 CARE & Sovereignty Fields (Governance Contract)

Schemas must encode CARE metadata as required fields where applicable:

- `care_label` (enum: `public`, `sensitive`, `restricted`)  
- Optional `sovereignty` object with:

  - `tribal_authority` (string)  
  - `review_status` (enum: `required`, `approved`, `exempt`)  
  - `masking` (string; e.g., `h3_r7`, `fuzz_500m`)  

Example snippet from `governance_event.schema.json`:

~~~~~json
{
  "type": "object",
  "properties": {
    "care_label": {
      "type": "string",
      "enum": ["public", "sensitive", "restricted"]
    },
    "sovereignty": {
      "type": "object",
      "required": ["tribal_authority", "review_status"],
      "properties": {
        "tribal_authority": { "type": "string" },
        "review_status": {
          "type": "string",
          "enum": ["required", "approved", "exempt"]
        },
        "masking": { "type": "string" }
      }
    }
  }
}
~~~~~

---

## 🔐 Idempotency & Replay Fields

All event schemas MUST support idempotent execution and deterministic replay via:

- `idempotency_key` (sha256 string)  
- `correlation_id` (trace/causality chain)  

These fields are:

- **Required** in `base_event.schema.json`  
- Validated in `etl_event`, `ai_event`, `publish_event`, and `governance_event` schemas  

---

## 🧾 Schema Validation & CI

Schemas are validated by:

- JSON Schema meta-validation (Draft 2020-12)  
- Pydantic v2-based runtime checks in validators  
- Dedicated CI tasks:

  - `schema-lint.yml`  
  - `docs-lint.yml`  
  - `faircare-validate.yml` (CARELABEL coverage)  

Any schema change requires:

- Version bump of `version` in this README  
- Updated telemetry schema, if relevant  
- Governance review sign-off for CARE fields  

---

## 📡 Telemetry & Governance Integration

Each event schema is associated with telemetry metadata (e.g., which fields are logged where).

Telemetry for schema validation writes to:

~~~~~text
../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

Governance ledger references (e.g., event validity logs) live under:

~~~~~text
../../../../../../docs/reports/audit/event_schema_ledger.json
~~~~~

---

## 🧪 Example: ETL Event Schema Outline

~~~~~json
{
  "$id": "https://kfm/schema/etl_event.schema.json",
  "allOf": [
    { "$ref": "base_event.schema.json" }
  ],
  "properties": {
    "event_type": {
      "type": "string",
      "const": "etl"
    },
    "parameters": {
      "type": "object",
      "properties": {
        "reprojection": { "type": "string" },
        "window": { "type": "string" }
      }
    }
  }
}
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Initial event schema README for v10.3; aligned with base event model, CARE metadata, and telemetry integration. |

---

<div align="center">

**Kansas Frontier Matrix — Pipeline Event Schemas**  
Strong Contracts × FAIR+CARE × Deterministic Events × Provenance Integrity  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Event Models](../README.md)

</div>
