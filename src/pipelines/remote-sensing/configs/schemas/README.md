---
title: "📐 Kansas Frontier Matrix — Remote Sensing Config Schema Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/configs/schemas/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-remote-sensing-config-schemas-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Remote Sensing Config Schema Registry**  
`src/pipelines/remote-sensing/configs/schemas/README.md`

**Purpose:**  
Define the **JSON Schema contracts** used to validate all Remote Sensing pipeline configurations in KFM (LandsatLook, Sentinel-1/2, NAIP, MODIS/VIIRS, hazards, spectral indices, AI summarization, Neo4j publishing, RDF exports).  
These schemas ensure configs are **structurally sound**, **FAIR+CARE-aware**, **telemetry-linked**, and **MCP-DL v6.3 compliant**.

<img alt="Schemas" src="https://img.shields.io/badge/Schemas-Canonical-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="Config" src="https://img.shields.io/badge/Configs-Validated-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

Remote-sensing configurations in KFM are **declarative** YAML/JSON files that drive ingestion, preprocessing, analytics, publishing, and telemetry for multiple pipelines.  

This directory houses the **canonical JSON Schemas** that all such configs MUST satisfy:

- **Remote Sensing Master Config Schema** (top-level)  
- **STAC Query Schema** (STAC Item Search parameters)  
- **Preprocessing Schema** (cloud mask, atmo-corr, terrain-corr)  
- **Neo4j Publish Schema** (graph publishing behavior)  
- **RDF Export Schema** (GeoSPARQL/JSON-LD constraints)  
- **AI Summarization Schema** (prompt + tags governance)  

All schemas are used in CI (`config-validate`, `telemetry-export`, `faircare-validate`) to reject invalid or non-governed configs.

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/configs/schemas/
├── README.md                               # This file
│
├── remote_sensing_config.schema.json       # Master schema for all configs
├── stac_query.schema.json                  # STAC search and filters
├── preprocessing.schema.json               # Preprocessing parameters
├── neo4j_publish.schema.json               # Graph publishing & spatial SRID
├── rdf_export.schema.json                  # RDF/GeoSPARQL export rules
└── ai_summarization.schema.json            # AI summary & tags governance
~~~~~

---

## 🧬 Master Schema — `remote_sensing_config.schema.json`

**Role:** Top-level schema for all Remote Sensing configs.

### Core Sections

- `stac` — Item Search parameters (endpoint, collections, datetime, filters)  
- `aoi` — AOI and overlays (counties, priority AOIs, sovereignty layers)  
- `preprocessing` — sensor-specific preprocessing rules  
- `analysis` — index/hazard analysis parameters  
- `neo4j` — graph publishing configuration  
- `rdf` — linked-data export settings  
- `ai` — AI summarization/tagging settings  
- `telemetry` — NDJSON telemetry output path  
- `care_label` — dataset CARE classification  

Example of required top-level properties (abbreviated):

~~~~~json
{
  "type": "object",
  "required": ["stac", "preprocessing", "analysis", "neo4j", "telemetry", "care_label"],
  "properties": {
    "stac": { "$ref": "stac_query.schema.json" },
    "preprocessing": { "$ref": "preprocessing.schema.json" },
    "neo4j": { "$ref": "neo4j_publish.schema.json" },
    "rdf": { "$ref": "rdf_export.schema.json" },
    "ai": { "$ref": "ai_summarization.schema.json" }
  }
}
~~~~~

---

## 🌐 STAC Query Schema — `stac_query.schema.json`

Defines the structure for:

- `endpoint` (string; valid URL)  
- `collections` (non-empty array of strings)  
- `datetime_lookback` (ISO 8601 duration, e.g. `P7D`)  
- Optional `query` object (STAC `query` clause)  
- `limit` (integer, > 0)  
- `max_cloud_cover` (0–100)  
- `intersects` (path to AOI geometry file)

Key constraints:

- `endpoint` MUST be HTTPS.  
- `collections` MUST not be empty.  
- `max_cloud_cover` MUST be a number between 0 and 100.  

---

## ⚙️ Preprocessing Schema — `preprocessing.schema.json`

Defines sensor-specific preprocessing options, such as:

- `cloud_mask` (boolean)  
- `s2cloudless` (boolean) for Sentinel-2  
- `harmonize_gsd` (integer; e.g. 10, 30)  
- `reproject` (CRS string; e.g., `EPSG:4326`)  
- `sar` block:
  - `terrain_correction` (boolean)  
  - `speckle_filter` (enum: `lee`, `refined_lee`, `none`)  
- `thermal` block:
  - `emissivity_correction` (boolean)  
  - `lst_scale`, `offset` (numbers)  

Configs failing preprocessing schema must be rejected in CI.

---

## 🧵 Neo4j Publish Schema — `neo4j_publish.schema.json`

Defines fields for graph publishing:

- `uri` (Bolt URI)  
- `user` (string)  
- `secret_ref` (path to secret file)  
- `spatial_srid` (integer; MUST be 4326 or compatible)  
- `index_labels` (array of labels to index, e.g. `["Scene","County"]`)  

Constraints:

- `uri` MUST begin with `bolt://` or `neo4j://`.  
- `spatial_srid` MUST be valid for WGS84 if using EPSG:4326.  

---

## 🌍 RDF Export Schema — `rdf_export.schema.json`

Defines fields for RDF/GeoSPARQL export:

- `enable` (boolean)  
- `out_dir` (string; path)  
- `context` (string; path or URL to JSON-LD context)  

Constraints:

- If `enable: true`, both `out_dir` and `context` MUST be set.  
- `context` MUST be compatible with KFM’s GeoSPARQL mapping.

---

## 🧠 AI Summarization Schema — `ai_summarization.schema.json`

Governs AI summarization/tagging settings:

- `enable` (boolean)  
- `prompt_template` (string; path to prompt file)  
- `max_tokens` (integer)  
- `tags_allowed` (array of strings; allowed tag vocab)  

Governance rules:

- AI MUST NOT be enabled without a valid prompt path.  
- `tags_allowed` MUST be non-empty if AI is enabled.  
- All AI configs are subject to `faircare-validate.yml` checks.

Example snippet:

~~~~~json
{
  "type": "object",
  "properties": {
    "enable": { "type": "boolean" },
    "prompt_template": { "type": "string" },
    "max_tokens": { "type": "integer", "minimum": 1 },
    "tags_allowed": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 1
    }
  }
}
~~~~~

---

## ⚖️ FAIR+CARE Governance Hooks

Schema-level governance checks include:

- Required `care_label` (enum: `public`, `sensitive`, `restricted`) on master config.  
- If `care_label != "public"`:
  - **Masking strategy** must be present in config or derived from AOI.  
- STAC ingest for **sensitive AOIs** must specify:
  - `priority_aoi` overlays  
  - Required masking/generalization options.  

`faircare-validate.yml` enforces:

- Proper use of `care_label`  
- Presence of sovereignty-related parameters when needed  
- AI summarization guardrails (prompt + tags schemas)  

---

## 📡 Telemetry Schema Integration

All configs validated by these schemas must declare telemetry NDJSON outputs.  
Telemetry emitters must follow:

- Field definitions from `src/pipelines/architecture/observability/fields.md`  
- Telemetry schema referenced in front matter (`telemetry_schema`)  

Aggregated telemetry is written to:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

CI enforces telemetry class via `telemetry-export.yml`.

---

## 🧪 Local Validation Example

Run JSON Schema validation locally:

~~~~~bash
python -m jsonschema \
  -i src/pipelines/remote-sensing/configs/landsatlook-stac-ingest.config.yaml \
  src/pipelines/remote-sensing/configs/schemas/remote_sensing_config.schema.json
~~~~~

(Can be adapted with yaml→json conversion step.)

---

## 🛠️ CI Validation in KFM

Schemas are applied in CI via:

- `config-validate` workflow (JSON Schema validation for configs)  
- `faircare-validate.yml` (governance checks using these schemas)  
- `docs-lint.yml` (ensuring README and schema references are consistent)  

Any config failing schema validation or governance checks → **CI block**.

---

## 🕰️ Version History

| Version | Date       | Author             | Summary                                                                                |
|---------|------------|--------------------|----------------------------------------------------------------------------------------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Introduced remote sensing config schema registry; aligned with FAIR+CARE, telemetry, and KFM Markdown Protocol. |

---

<div align="center">

**Kansas Frontier Matrix — Remote Sensing Config Schemas**  
Schema-Validated Pipelines × FAIR+CARE × Telemetry-Ready × Reproducible ETL  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>