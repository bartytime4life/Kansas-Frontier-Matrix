---
title: "📐 Kansas Frontier Matrix — Remote Sensing Ingest Schema Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/ingest/schemas/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-remote-sensing-ingest-schemas-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Remote Sensing Ingest Schema Registry**  
`src/pipelines/remote-sensing/ingest/schemas/README.md`

**Purpose:**  
Define the **JSON Schemas** that validate all Remote Sensing ingest configurations and STAC batch outputs for KFM.  
These schemas ensure that ingestion is **structurally correct**, **FAIR+CARE-governed**, **STAC-compliant**, and ready for downstream preprocessing, analysis, Neo4j publishing, and lineage export.

<img alt="Schemas" src="https://img.shields.io/badge/Schemas-Ingest-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="STAC" src="https://img.shields.io/badge/STAC-Batch_Validated-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

Remote-sensing ingestion in KFM is driven by:

- **Ingest configuration files** (YAML/JSON)  
- **STAC batch outputs** (JSON/JSONL)  

This directory contains the **canonical JSON Schemas** that all such inputs/outputs MUST satisfy:

- `ingest.schema.json` — required fields for ingest configuration objects  
- `stac_batch.schema.json` — required structure for a single STAC Feature within batch files  

These schemas are consumed by CI workflows (e.g., `config-validate`, `stac-validate.yml`, `faircare-validate.yml`) to enforce:

- Correct STAC search usage  
- Consistent AOI references  
- Valid ingest metadata and CARE markers  
- Batch-level STAC integrity before preprocessing begins  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/ingest/schemas/
├── README.md                   # This file
├── ingest.schema.json          # Schema for ingest configs
└── stac_batch.schema.json      # Schema for STAC batch Features/records
~~~~~

---

## 🧾 `ingest.schema.json` — Ingest Config Schema

**Role:**  
Validate the ingest configuration structures passed to:

- `landsatlook_ingest.py`  
- `sentinel2_ingest.py`  
- `sentinel1_ingest.py`  
- `naip_ingest.py`  
- `modis_ingest.py`  

### Required Top-Level Fields

| Field | Type | Description |
|-------|------|-------------|
| `stac.endpoint` | string (URL) | STAC search endpoint |
| `stac.collections` | array(string) | STAC collections to query |
| `stac.datetime_lookback` | string | ISO 8601 duration (e.g., `P7D`) |
| `stac.limit` | integer | Max items per page ( > 0 ) |
| `stac.intersects` | string | Path to AOI geometry file |
| `aoi.counties` | string | Path to Kansas counties layer (optional but recommended) |
| `telemetry.log_file` | string | NDJSON telemetry output path |
| `care_label` | string | `public` / `sensitive` / `restricted` |

Abridged schema (conceptual):

~~~~~json
{
  "type": "object",
  "required": ["stac", "telemetry", "care_label"],
  "properties": {
    "stac": {
      "type": "object",
      "required": ["endpoint", "collections", "datetime_lookback", "limit", "intersects"],
      "properties": {
        "endpoint": { "type": "string", "format": "uri" },
        "collections": {
          "type": "array",
          "items": { "type": "string" },
          "minItems": 1
        },
        "datetime_lookback": { "type": "string" },
        "limit": { "type": "integer", "minimum": 1 },
        "intersects": { "type": "string" }
      }
    },
    "telemetry": {
      "type": "object",
      "required": ["log_file"],
      "properties": {
        "log_file": { "type": "string" }
      }
    },
    "care_label": {
      "type": "string",
      "enum": ["public", "sensitive", "restricted"]
    }
  }
}
~~~~~

---

## 🛰️ `stac_batch.schema.json` — STAC Batch Feature Schema

**Role:**  
Validate each STAC Feature in JSON/JSONL batches written to staging (e.g. `data/stac/landsat/...`).

Each line / record MUST be a valid STAC Item with KFM ingest metadata, including:

- `id` (string)  
- `type = "Feature"`  
- `stac_version` (1.0.x)  
- `collection` (string)  
- `bbox` (array of 4 or 6 numbers)  
- `geometry` (valid GeoJSON Polygon/MultiPolygon)  
- `properties.datetime` (ISO 8601 datetime string)  
- `assets` (object with keys → asset objects)  
- `links` (array of STAC link objects)  

KFM-specific extensions:

- `properties["kfm:ingest_time"]`  
- `properties["kfm:ingest_version"]`  
- `properties["kfm:source_endpoint"]`  
- `properties["kfm:stacAssetHash"]`  

Abridged schema (conceptual):

~~~~~json
{
  "type": "object",
  "required": ["id", "type", "stac_version", "geometry", "properties", "assets"],
  "properties": {
    "id": { "type": "string" },
    "type": { "type": "string", "enum": ["Feature"] },
    "stac_version": { "type": "string" },
    "collection": { "type": "string" },
    "bbox": {
      "type": "array",
      "minItems": 4,
      "items": { "type": "number" }
    },
    "geometry": {
      "type": "object",
      "required": ["type", "coordinates"]
    },
    "properties": {
      "type": "object",
      "required": ["datetime", "kfm:ingest_time", "kfm:source_endpoint"],
      "properties": {
        "datetime": { "type": "string" },
        "kfm:ingest_time": { "type": "string" },
        "kfm:ingest_version": { "type": "string" },
        "kfm:source_endpoint": { "type": "string" },
        "kfm:stacAssetHash": { "type": "string" }
      }
    },
    "assets": { "type": "object" },
    "links": { "type": "array" }
  }
}
~~~~~

---

## ⚖️ FAIR+CARE Governance Hooks

The ingest schemas enforce:

- `care_label` in configs, which guides:
  - Downstream masking requirements  
  - AOI-based sensitivity checks  
- Presence of ingest-time metadata needed for **provenance** and **replay**.  

`faircare-validate.yml` uses:

- `ingest.schema.json` to check:
  - CARE label correctness  
  - AOI specifications for sensitive labels  
- `stac_batch.schema.json` to ensure:
  - No ingest batch is missing required metadata  
  - No ingest output bypasses governance metadata tags  

Configs with `care_label = "sensitive"` or `"restricted"` MUST define masking or generalization in the broader Remote Sensing config schemas.

---

## 📡 Telemetry & Schema Alignment

Telemetry records generated by ingest modules must:

- Follow observability fields defined at:

  ~~~~~text
  src/pipelines/architecture/observability/fields.md
  ~~~~~

- Use paths declared in ingest configs (validated by `ingest.schema.json`)  
- Be aggregated into:

  ~~~~~text
  ../../../../../releases/v10.3.0/focus-telemetry.json
  ~~~~~

Telemetry CI (`telemetry-export.yml`) cross-checks:

- That ingest telemetry includes:
  - `items_polled`, `items_retained`, `items_deduped`  
  - `etag_used`, `request_latency_ms`  
  - `energy_wh`, `co2_g`  
  - `care_violations`  

---

## 🧪 Local Validation Example

Validate a config:

~~~~~bash
python -m jsonschema \
  -i src/pipelines/remote-sensing/configs/landsatlook-stac-ingest.config.yaml \
  src/pipelines/remote-sensing/ingest/schemas/ingest.schema.json
~~~~~

Validate a STAC batch file (line-by-line):

~~~~~bash
jq -c '.' data/stac/landsat/2025-11-14/items_001.jsonl \
  | while read -r feature; do
      echo "$feature" | jsonschema -i - src/pipelines/remote-sensing/ingest/schemas/stac_batch.schema.json
    done
~~~~~

(Adapt as needed with YAML→JSON conversion.)

---

## 🛠️ CI Integration

Schemas in this registry are used by:

- `config-validate.yml` — validates ingest configs before merges  
- `stac-validate.yml` — validates ingested STAC batches  
- `faircare-validate.yml` — checks for CARE/governance alignment  
- `docs-lint.yml` — ensures schema references stay in sync with documentation  

Any ingest config or batch failing these schemas MUST be:

- Rejected in CI  
- Investigated by ingest pipeline maintainers  
- Not passed to downstream preprocessing/analysis  

---

## 🕰️ Version History

| Version | Date       | Author            | Summary                                                                |
|---------|------------|-------------------|------------------------------------------------------------------------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Introduced Remote Sensing ingest schema registry; aligned with STAC, CARE, telemetry, and KFM Markdown Protocol. |

---

<div align="center">

**Kansas Frontier Matrix — Remote Sensing Ingest Schemas**  
Schema-Validated Ingestion × FAIR+CARE Governance × STAC-Compliant Batches  
© 2025 Kansas Frontier Matrix — MIT License  

</div>