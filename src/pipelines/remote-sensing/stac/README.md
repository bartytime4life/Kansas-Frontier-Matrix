---
title: "🛰️ Kansas Frontier Matrix — Remote Sensing STAC Integration Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/stac/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipelines-remote-sensing-stac-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — Remote Sensing STAC Integration Module**  
`src/pipelines/remote-sensing/stac/README.md`

**Purpose:**  
Define the **STAC construction, validation, enrichment, and publication model** for all remote-sensing products (optical, SAR, thermal, hazards, vegetation indices) processed by the Kansas Frontier Matrix (KFM).  
Ensures that every raster or vector asset produced by remote-sensing pipelines becomes a **FAIR+CARE-compliant, immutable, reproducible, versioned STAC Item / Collection**.

<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0_Compliant-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Integrated-orange"/>
<img alt="GDAL" src="https://img.shields.io/badge/GDAL-3.12-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

The Remote Sensing STAC Module handles:

- STAC Item creation for **every processed asset**  
- STAC Collection creation for **each dataset family** (e.g., LANDSAT L2, Sentinel-2 MSI, NDVI Composites, Flood Extents)  
- Schema validation (JSON Schema)  
- Great Expectations validation (supplemental semantic rules)  
- KFM metadata injection (`kfm:*` fields)  
- CARE-masking and sovereignty-aware spatial metadata adjustments  
- Publication to `data/stac/published/`  
- Neo4j graph hydration (Scenes, Datasets, Themes)

Outputs of this module are consumed by:

- The KFM STAC catalog  
- The map layer browser (MapLibre + Cesium)  
- Focus Mode v2.4  
- Predictive models  
- Time-series explorers  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/stac/
├── README.md                      # This file
│
├── build_item.py                  # Create STAC Item for a processed asset
├── build_collection.py            # Create STAC Collection for a dataset family
├── validate_item.py               # JSON Schema + GE validation for Items
└── publish.py                     # Write Items/Collections and hydrate graph
~~~~~

---

## 🧩 STAC Workflow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Processed Asset<br/>COG / GeoParquet / NetCDF"] --> B["build_item.py<br/>STAC Item Construction"]
  B --> C["validate_item.py<br/>Schema + GE Validation"]
  C -->|FAIL| Q["Quarantine<br/>Governance Review"]
  C -->|PASS| D["build_collection.py<br/>Align Dataset Family"]
  D --> E["publish.py<br/>Write Files · Update Catalog"]
  E --> F["Neo4j Hydration<br/>Scenes → Datasets → Themes"]
  F --> G["Telemetry<br/>focus-telemetry.json"]
~~~~~

---

## 📦 STAC Item Construction (build_item.py)

### Required STAC Fields

- `id`, `type`, `stac_version`  
- `geometry`, `bbox`  
- `properties.datetime`  
- `links`  
- `assets` with:
  - `href`  
  - `type` (MIME)  
  - `roles`  
  - extension-specific metadata  

### Required STAC Extensions

| Sensor Type | Required Extensions |
|-------------|---------------------|
| Optical | EO, VIEW, PROJ, RASTER |
| SAR | SAR, PROJ, RASTER |
| Thermal | PROJ, RASTER |
| Derived Indices | EO, PROJ, RASTER |

### Required KFM Extensions

- `kfm:ingest_version`  
- `kfm:checksum`  
- `kfm:provenance` (PROV-O bundle)  
- `kfm:care_label`  
- `kfm:sovereignty_flags` (if applicable)  

---

## 🗃️ STAC Collection Construction (build_collection.py)

Collections MUST include:

- Scientific & temporal summaries  
- Spatial extents (auto-computed from Items)  
- A list of required extensions  
- Keywords, providers, licensing  
- KFM metadata:
  - `kfm:collection_type`  
  - `kfm:doi` (optional)  
  - `kfm:themes`  

Collections MUST remain:

- Immutable per version  
- SemVer-governed  
- Schema-consistent across releases  

---

## 🧪 Validation (validate_item.py)

Validation includes:

1. **JSON Schema** checks  
2. **Asset property** checks (roles, MIME, href resolution)  
3. **Projection metadata** checks (PROJ)  
4. **Raster metadata** checks (`raster:bands`, data types, stats)  
5. **EO metadata** checks (bands, solar angles, cloud cover)  
6. **CARE governance checks**  
7. **Lineage consistency** (`kfm:checksum`, prov chain)  
8. **Sustainability metrics** (energy, CO₂e)  

**Validation failure → quarantine with governance escalation.**

---

## ⬆️ Publication (publish.py)

Publication writes:

~~~~~text
data/stac/published/collections/<collection_id>.json
data/stac/published/items/<collection_id>/<item_id>.json
~~~~~

Rules:

- No overwriting previously published Items  
- Versioned directories for updated datasets  
- Automatic graph hydration:
  - `(:Scene)-[:BELONGS_TO]->(:Dataset)`  
  - Themes derived from metadata (hydrology, climate, fire, vegetation, hazards)

---

## 🧬 Provenance & Lineage Integration

Remote-sensing STAC Items MUST:

- Include `kfm:provenance` linking to PROV-O lineage bundles  
- Include `kfm:checksum` using sha256  
- Capture:
  - Input source STAC Items  
  - Preprocessing parameters  
  - Model parameters (if AI involved)  
  - Software environment (GDAL, rasterio versions)  
  - CARE masking steps  

Lineage outputs stored under:

~~~~~text
src/pipelines/remote-sensing/lineage/provenance.jsonld
~~~~~

---

## ⚖️ FAIR+CARE Governance

### CARE Rules

- Apply spatial masking for sensitive areas  
- Propagate CARE labels from source → derived  
- Log sovereignty intersections  
- Escalate governance conflicts to FAIR+CARE Council  
- No publication if governance fails  

### FAIR Rules

- All STAC assets must:
  - Be discoverable  
  - Use open formats (COG, GeoParquet)  
  - Include required metadata  
  - Map cleanly to DCAT 3.0  

---

## 📡 Telemetry

Remote-sensing STAC module MUST emit:

- `items_published`, `items_quarantined`  
- `processing_time_sec`  
- `energy_wh`, `co2_g`  
- All validation failure classes  
- All CARE violations  

Telemetry aggregated into:

~~~~~text
../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧪 Local Development

~~~~~bash
# Build STAC Item from a processed asset
python src/pipelines/remote-sensing/stac/build_item.py --input raster.tif

# Validate the resulting STAC Item
python src/pipelines/remote-sensing/stac/validate_item.py item.json

# Publish
python src/pipelines/remote-sensing/stac/publish.py item.json
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Full STAC integration layer defined with validation, governance, provenance, and publication workflow. |

---

<div align="center">

**Kansas Frontier Matrix — Remote Sensing STAC Module**  
FAIR+CARE Geospatial Metadata × Immutable Publishing × Provenance by Design  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>
