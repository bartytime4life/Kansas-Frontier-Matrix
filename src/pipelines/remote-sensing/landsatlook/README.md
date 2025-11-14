---
title: "🛰️ Kansas Frontier Matrix — LandsatLook Remote-Sensing Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/landsatlook/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-landsatlook-module-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — LandsatLook Remote-Sensing Module**  
`src/pipelines/remote-sensing/landsatlook/README.md`

**Purpose:**  
Implement the **complete LandsatLook ingestion → validation → enrichment → AI tagging → Neo4j publishing → RDF export** pipeline for the Kansas Frontier Matrix (KFM).  
This module transforms raw LandsatLook STAC Items into **FAIR+CARE-certified**, **GeoSPARQL-aligned**, **provenance-tracked**, **graph-ready** geospatial assets.

<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0_Compliant-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Integrated-orange"/>
<img alt="GeoSPARQL" src="https://img.shields.io/badge/GeoSPARQL-Linked_Data-success"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-green"/>

</div>

---

## 📘 Overview

The **LandsatLook module** handles:

- Discovery of Landsat scenes via **STAC Item Search**  
- Enforced validation (JSON Schema + Great Expectations)  
- Geometry normalization, centroid extraction, and CRS harmonization  
- County + priority AOI spatial intersections  
- Optional AI scene summarization + controlled tag assignment  
- Cypher-based Neo4j publishing (Scene nodes + INTERSECTS relationships)  
- RDF/GeoSPARQL export for semantic web and linked-data consumers  
- Telemetry logging + FAIR+CARE governance integration  
- Full reproducibility under MCP-DL v6.3 and KFM sustainability targets  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/landsatlook/
├── __init__.py
├── fetch.py             # STAC search, pagination, raw storage
├── validate.py          # STAC Item structural + semantic validation
├── enrich.py            # AOI overlaps, geometry fixes, footprint → centroid
├── ai_describe.py       # Optional 1–2 sentence summary + tags (controlled vocab)
├── publish_neo4j.py     # Cypher MERGE; spatial + temporal indexing
├── export_rdf.py        # GeoSPARQL JSON-LD/Turtle export
└── config.py            # Loads YAML config, applies schema validation
~~~~~

Config file associated with this module:

~~~~~text
src/pipelines/remote-sensing/configs/landsatlook-stac-ingest.config.yaml
~~~~~

---

## 🧩 Module Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["STAC Fetch<br/>landsatlook.fetch"] --> B["Validate<br/>landsatlook.validate"]
  B -->|PASS| C["Enrich<br/>landsatlook.enrich"]
  B -->|FAIL| Q["Quarantine · Governance Review"]

  C --> D["AI Summaries (Optional)<br/>landsatlook.ai_describe"]
  D --> E["Neo4j Publish<br/>landsatlook.publish_neo4j"]
  E --> F["GeoSPARQL Export<br/>landsatlook.export_rdf"]
  F --> G["Telemetry + Governance Ledgers"]
~~~~~

---

## 🔍 fetch.py — STAC Discovery

**Responsibilities:**

- Query LandsatLook STAC API  
- Support pagination via `links[].rel == "next"`  
- Deduplicate items by:
  - `id`
  - asset checksums  
- Save raw per-page results to:

  ~~~~~text
  data/stac/landsat/YYYY/MM/DD/items_###.json
  ~~~~~

**Validation Inputs:**  
Used later by `validate.py` for structural checks.

---

## 🧪 validate.py — STAC Validation

Validation rules include:

- STAC 1.0 required fields  
- `type="Feature"`  
- Valid GeoJSON geometry (Polygon/MultiPolygon)  
- Datetime parseable + timezone normalized (Z)  
- Assets contain MIME types + valid `roles`  
- JSON Schema + Great Expectations checks  
- CARE/Governance flags:
  - licensing present  
  - sovereignty/cultural-land intersections validated  

On failure:

- Write STAC Item batch to `data/stac/quarantine/<timestamp>/`  
- Produce `last_failure_summary.md`  
- CI opens GitHub Issue  

---

## 🧭 enrich.py — AOI & Geometry Processing

**Operations:**

- Convert multipart → single dissolved polygon  
- Compute:
  - centroid (EPSG:4326)  
  - bounding box  
- Intersect with:
  - **Kansas counties** → add FIPS, overlap %, area_km2  
  - **priority AOIs** → add hazard/interest flags  

Outputs added to:

- `scene.county_overlaps[*]`  
- `scene.priority_hits[*]`  

Used by Neo4j publishing and AI summaries.

---

## 🧠 ai_describe.py — AI Summaries & Tags (Optional)

**Purpose:** Produce human-interpretable summaries with controlled tags.

Uses:

- Prompt at `docs/prompts/remote-sensing/scene-brief.v1.txt`  
- Strict output schema:

~~~~~json
{
  "summary": "…",
  "tags": ["crop_stress","burn_scar"]
}
~~~~~

**Safety & Governance:**

- No PII.  
- No speculative catastrophic claims.  
- Tags restricted to allow-list declared in config YAML.  
- All outputs logged to telemetry with refusal stats.

---

## 🧵 publish_neo4j.py — Graph Publishing

**Cypher MERGE pattern:**

- Node: `(:Scene {id})`  
- Properties:
  - `datetime`  
  - `collection`  
  - `cloud`  
  - `thumbnail`  
  - `geom_wkt`  
  - `centroid` (`point({longitude,latitude,srid:4326})`)  

**Relationships:**

- `(:Scene)-[:INTERSECTS]->(:County)`  
- Relationship properties:
  - `percent_overlap`  
  - `area_km2`  

**Indexes:**

- `Scene(id)`  
- `County(fips)`  
- `Scene.centroid` supported by Neo4j spatial index (v5+).

---

## 🌐 export_rdf.py — GeoSPARQL Linked Data

Exports:

- JSON-LD using context:
  
  ~~~~~text
  schemas/rdf/geosparql.context.jsonld
  ~~~~~

- Turtle (`.ttl`)

Mappings:

| KFM Node | GeoSPARQL Class/Prop |
|---------|------------------------|
| Scene | geo:Feature |
| County | geo:Feature |
| Footprint WKT | geo:asWKT |
| centroid POINT | geo:hasGeometry |
| INTERSECTS rel | geo:sfIntersects |

Outputs saved under:

~~~~~text
data/processed/rdf/landsat/
~~~~~

---

## 📡 Telemetry (Module-Level)

Telemetry NDJSON logged to:

~~~~~text
data/processed/telemetry/landsat_ingest.ndjson
~~~~~

Fields include:

- `stage`  
- `items`  
- `filtered_cloud`  
- `valid`  
- `invalid`  
- `with_county`  
- `priority_hits`  
- `ai_enabled`  
- `neo4j_nodes`  
- `rels`  
- `rdf_files`  
- `energy_wh`  
- `co2_g`  

Aggregated into release:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## ⚖️ FAIR+CARE Governance Integration

- CARE label must propagate from STAC → Scene → RDF export.  
- Sovereignty intersection detection is **mandatory**.  
- AI outputs logged with:
  - prompt path  
  - model ID  
  - refusal flags  
  - controlled-tag enforcement results  
- Provenance logs captured in governance ledgers:
  
  ~~~~~text
  docs/reports/audit/data_provenance_ledger.json
  ~~~~~

No asset may be published if governance rules fail.

---

## 🚀 Local Development Runbook

~~~~~bash
# Fetch
python -m landsatlook.fetch \
  --config src/pipelines/remote-sensing/configs/landsatlook-stac-ingest.config.yaml

# Validate
python -m landsatlook.validate --input data/stac/landsat/ --fail-on-error

# Enrich
python -m landsatlook.enrich \
  --counties data/processed/admin/kansas_counties.gpkg \
  --priority-aoi data/processed/aoi/priority_aoi.gpkg

# AI Summaries
python -m landsatlook.ai_describe \
  --prompt docs/prompts/remote-sensing/scene-brief.v1.txt

# Publish to Neo4j
python -m landsatlook.publish_neo4j --neo4j secrets/neo4j.txt

# RDF Export
python -m landsatlook.export_rdf --out data/processed/rdf/landsat/
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Added full module specification, FAIR+CARE rules, GeoSPARQL mapping, telemetry integration. |

---

<div align="center">

**Kansas Frontier Matrix — LandsatLook Module**  
FAIR+CARE Geospatial ETL × Scientific Provenance × GeoSPARQL Linked Data  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>