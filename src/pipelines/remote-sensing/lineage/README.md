---
title: "🧬 Kansas Frontier Matrix — Remote Sensing Lineage & Provenance System (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/lineage/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-remote-sensing-lineage-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Remote Sensing Lineage & Provenance System**  
`src/pipelines/remote-sensing/lineage/README.md`

**Purpose:**  
Define how **Remote Sensing pipelines** track, serialize, publish, and validate **provenance, lineage, and transformation metadata** across all STAC ingestion, preprocessing, analysis, AI summarization, Neo4j publishing, and RDF/GeoSPARQL export steps.

This system ensures **complete reproducibility**, **FAIR+CARE governance compliance**, and **PROV-O/CIDOC-CRM semantic traceability** across the KFM remote-sensing architecture.

<img alt="Lineage" src="https://img.shields.io/badge/Lineage-Complete-blue"/>
<img alt="GeoSPARQL" src="https://img.shields.io/badge/GeoSPARQL-Linked_Data-success"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

Remote Sensing pipelines (LandsatLook, Sentinel-1/2, NAIP, MODIS/VIIRS, hazards, indices) require full lineage tracking from:

1. **STAC ingestion**  
2. **Preprocessing (cloud mask, SAR terrain correction, reprojection)**  
3. **Analysis (indices, hazards, summaries)**  
4. **AI summarization/tagging (optional)**  
5. **Neo4j publishing (Scene → County → AOI)**  
6. **RDF/GeoSPARQL export**  
7. **Telemetry + governance logging**  

This directory defines the lineage model, serialization, and governance requirements to achieve **deterministic, reconstructible, evidence-based** outputs.

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/lineage/
├── README.md                     # This file
│
├── lineage_builder.py            # Builds lineage chains from pipeline steps
├── stac_provenance.py            # Extracts STAC → provenance mappings
├── aoi_provenance.py             # County/priority-AOI lineage utilities
├── processing_steps.py           # Enumerates steps & PROV-O classes
├── rdf_lineage_export.py         # JSON-LD/Turtle lineage exporters
└── schemas/
    ├── lineage.schema.json       # Master lineage schema
    ├── prov_o_context.jsonld     # PROV-O JSON-LD context
    ├── geosparql_context.jsonld  # GeoSPARQL linked-data context
    └── kfm_lineage_rules.json    # Internal KFM lineage rules
~~~~~

---

## 🧩 Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["STAC Ingestion<br/>landsatlook.fetch"] --> B["Preprocessing<br/>cloud_mask · RTC · reprojection"]
  B --> C["Analysis<br/>indices · hazards · geometry"]
  C --> D["AI Summaries<br/>optional"]
  D --> E["Neo4j Publish<br/>Scene + County + AOI"]
  E --> F["RDF Export<br/>GeoSPARQL Linked Data"]
  F --> G["Lineage Builder<br/>JSON-LD + PROV-O + CIDOC CRM"]
  G --> H["Governance Ledger<br/>data_provenance_ledger.json"]
~~~~~

---

## 🧬 Lineage Model (PROV-O + CIDOC CRM + KFM Extensions)

Remote Sensing lineage uses:

### 🧱 **PROV-O Core**
- `prov:Entity` — STAC items, rasters, masks, derived layers  
- `prov:Activity` — preprocessing, analysis, AI summarization  
- `prov:Agent` — pipeline version, user, or automated CI agent  
- `prov:wasGeneratedBy`, `prov:used`, `prov:wasAttributedTo`  

### 🏺 **CIDOC CRM**
- `E7 Activity` — interpretation events (e.g., AI summaries)  
- `E53 Place` — counties, AOIs  
- `E94 Space Primitive` — geometry (WKT, centroid)  

### 🌐 **GeoSPARQL**
- `geo:Feature`  
- `geo:hasGeometry`  
- `geo:asWKT`  

### 🔧 **KFM Custom Extensions**
- `kfm:careLabel`  
- `kfm:maskingStrategy`  
- `kfm:aiSummaryRefusal`  
- `kfm:stacAssetHash`  
- `kfm:processingSteps[]`  
- `kfm:energyWh`, `kfm:co2g`  
- `kfm:telemetryRef`  

---

## 📦 Lineage Output Structure

All lineage records must be emitted as **JSON-LD** and validated against:

~~~~~text
src/pipelines/remote-sensing/lineage/schemas/lineage.schema.json
~~~~~

### Example (abridged):

~~~~~json
{
  "@context": [
    "prov_o_context.jsonld",
    "geosparql_context.jsonld",
    "https://schema.kfm/lineage/v1"
  ],
  "@id": "kfm:scene_2025_310923",
  "type": ["prov:Entity", "geo:Feature"],
  "generatedAtTime": "2025-11-14T03:03:35Z",
  "kfm:careLabel": "public",
  "kfm:stacAssetHash": "sha256:abc123...",
  "prov:wasGeneratedBy": {
    "@id": "kfm:landsat_pipeline_v10_3_1",
    "type": "prov:Activity",
    "prov:startedAtTime": "2025-11-14T03:00:00Z",
    "prov:used": [
      "stac:item:LC08_L2SP_030030_20251031",
      "aoi:KansasCounties"
    ]
  },
  "geo:hasGeometry": {
    "geo:asWKT": "POLYGON ((...))"
  },
  "kfm:processingSteps": ["cloud_mask", "harmonize_gsd", "reproject", "ndvi"],
  "kfm:energyWh": 12.4,
  "kfm:co2g": 16.2
}
~~~~~

---

## 🔍 lineage_builder.py — Core Responsibilities

- Collect `processingSteps` during the pipeline run  
- Capture STAC source metadata + asset hashes  
- Attach AOI overlap lineage  
- Record CARE masking and sovereignty violations  
- Serialize into JSON-LD + Turtle  
- Validate against lineage.schema.json  
- Emit entry into governance ledger  

Lineage builder MUST run **after** Neo4j publishing but **before** RDF export.

---

## 🌐 stac_provenance.py — STAC Entity Lineage

Extracts from STAC:
- `id`, `collection`, `datetime`, `bbox`  
- Asset types, hashes, roles  
- Provider metadata  
- License + attribution fields  

Maps them into PROV-O entities.

---

## 🗺️ aoi_provenance.py — Spatial Overlap Lineage

Adds:

- County/priority-AOI overlap metrics  
- Derived relationship lineage:
  - `Scene` ← `INTERSECTS` → `County`  
- CARE-sensitive AOI detections  
- Generalized geometries if required  

---

## 🛠 processing_steps.py — Pipeline Enumerations

Defines standard steps:

~~~~~text
cloud_mask
harmonize_gsd
reproject
sar_rtc
sar_speckle
ndvi
ndmi
ndwi
savi
burnscar
flood_extent
ai_summary
neo4j_publish
rdf_export
~~~~~

Each processing step must emit telemetry and attach to lineage.

---

## 🌐 rdf_lineage_export.py — Semantic Web Integration

Generates:

- JSON-LD lineage bundle  
- Turtle lineage graph  
- Optional **PROV-N** export  

Links entities:

- Scene → STAC source  
- Scene → AOI features  
- Scene → Derived index layers  
- Scene → AI summaries (if present)  

---

## ⚖️ FAIR+CARE Requirements

Lineage MUST include:

- `careLabel` at scene-level  
- Masking strategy (`maskingStrategy`)  
- Sovereignty violation flags  
- AI refusal logs  
- All transformations, even reversible ones  

Governance ledger reference:

~~~~~text
../../../../../docs/reports/audit/data_provenance_ledger.json
~~~~~

Lineage CI gate: **faircare-validate.yml**

---

## 📡 Telemetry Integration

Lineage modules emit:

- energy / CO₂e  
- pixel count summaries  
- stage durations  
- masking violations  
- assets processed  
- items skipped / deduped  

Telemetry writes to:

~~~~~text
data/processed/telemetry/<pipeline>.ndjson
~~~~~

Aggregated to:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧪 Testing Requirements

Must include tests for:

- JSON-LD validity  
- GeoSPARQL mapping correctness  
- PROV-O relation completeness  
- AI-summary lineage (if enabled)  
- STAC-to-lineage mapping  
- CARE/sovereignty lineage fields  

Must pass CI workflows:

- `codeql.yml`  
- `trivy.yml`  
- `faircare-validate.yml`  
- `telemetry-export.yml`  
- `docs-lint.yml`  

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Added full Remote-Sensing Lineage Module: PROV-O, GeoSPARQL, CIDOC, CARE, telemetry, JSON-LD exporters. |

---

<div align="center">

**Kansas Frontier Matrix — Remote Sensing Lineage System**  
Scientific Provenance × FAIR+CARE Governance × Deterministic ETL × Linked-Data Excellence  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>