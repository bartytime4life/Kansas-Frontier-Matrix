---
title: "📐 NASA SMAP — Grid Definition Library (EASE-Grid 2.0 → KFM CRS) · Reprojection Stage"
path: "docs/data/satellites/smap/transforms/reprojection/grid_defs/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
provenance_profile: "KFM-PROV-O v11.2"
jsonld_profile: "KFM-JSONLD v11"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public ETL Support Documentation"
fair_category: "F1-A1-I2-R3"
care_label: "CARE-A/B depending on user of derived grids"
indigenous_rights_flag: true
sensitivity_level: "Low (grids only)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../../schemas/json/transform-smap-griddefs-v11.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/transform-smap-griddefs-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:reprojection:grid-defs-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-griddefs"
event_source_id: "ledger:docs/data/satellites/smap/transforms/reprojection/grid_defs/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded at next CRS/grid-schema update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📐 **NASA SMAP — Grid Definition Library (EASE-Grid 2.0 → KFM CRS)**  
`docs/data/satellites/smap/transforms/reprojection/grid_defs/README.md`

**Purpose**  
Provide the **formal grid definition library** used during SMAP ETL **Stage 2 (Reprojection)**.  
These grid specifications ensure accurate, deterministic spatial transforms,  
FAIR+CARE-aligned governance, and STAC v11 spatial metadata correctness across  
all SMAP datasets: Soil Moisture, Freeze/Thaw, Vegetation Water, QA/RFI, and ancillary metadata.

</div>

---

## 📘 1. Overview

The **grid_defs/** directory contains the authoritative definitions for:

- 🗺️ **EASE-Grid 2.0** (native SMAP grid)  
- 🌐 **KFM CRS** (the unified Kansas Frontier Matrix spatial reference system)  
- 🧩 **Cell mappings** for interpolation, resampling, and reprojection  
- 📏 **Transform metadata** required for STAC v11 projection/raster extensions  
- 🧬 **Spatial provenance** used in PROV-O lineage  

These files drive the reprojection engine in:

```
ease_to_kfm_grid.py
geolocation_utils.py
bbox_normalization.py
```

Without these definitions, reprojection would be non-deterministic, non-FAIR, and  
non-compliant with STAC/DCAT/PROV/Owl-Time alignment.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/reprojection/grid_defs/
├── 📄 README.md                  # This file
│
├── 🗺️ ease_grid_2.0.json         # SMAP native grid definition (EASE-Grid 2.0)
├── 🌐 kfm_crs.json               # KFM canonical CRS + projection metadata
└── 📏 cell_mappings.json         # Pixel-to-pixel + grid-to-grid mapping tables
~~~

Each file is machine-readable, JSON-schema-validated, and referenced by  
KFM reprojection code and STAC metadata generation.

---

## 🧩 3. File Specifications

### 🗺️ `ease_grid_2.0.json` — SMAP Native Grid

Contains:

- Grid definition for **SMAP L3**  
- Projection details (Lambert azimuthal equal-area)  
- Cell size, shape, orientation  
- Row/column ordering  
- Metadata required for STAC `proj:*` and `raster:*` extensions  
- Bounding polygon of global grid  

**Used by:**

- Soil Moisture L3  
- Freeze/Thaw L3  
- Vegetation Water L3  
- QA/RFI L3

---

### 🌐 `kfm_crs.json` — KFM Unified CRS

Defines the **canonical geospatial coordinate reference system** used for:

- All environmental layers  
- Archaeology surfaces  
- Hydrology + climate models  
- Focus Mode v3 map/timeline linkage  
- Story Node v3 spatial anchors  

Includes:

- CRS definition (EPSG code + proj4 + WKT)  
- Axis orientation  
- Stable transformation parameters for all SMAP sources  
- STAC `proj:epsg` + `proj:wkt` fields  
- Metadata on CRS version + KFM spatial governance policy  

---

### 📏 `cell_mappings.json` — Grid & Pixel Mappings

Provides:

- Transformation lookup tables  
- Interpolation rules  
- Pixel-center → pixel-edge semantic correction  
- Anti-meridian behavior rules  
- H3 sensitivity flags for grid transitions  
- Provenance fields identifying grid-definition versions  

Used by:

- `ease_to_kfm_grid.py`  
- STAC writer (for generating cell/cellsize metadata)  
- Uncertainty interpolation stage  

---

## 🔐 4. Governance & Sovereignty Considerations

Grid definitions themselves can influence how sensitive features appear.

KFM mandates:

- No grid definition may **increase precision** in sovereign Indigenous regions  
- Any grid cell that intersects protected territory must have:
  - `kfm:sovereignty_flag: true`  
  - `kfm:care_label` (CARE-A/B)  
  - `"kfm:mask_required": true` for downstream masking stages  
- All grid files must retain CARE metadata fields  

These rules are validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. Validation & QA

Grid files undergo:

- JSON Schema validation  
- SHACL shape validation  
- CRS-projection integrity checks  
- Interpolation-rule conformity tests  
- Cross-grid consistency with:
  - HydroGNSS grid profiles  
  - ERA5-Land  
  - NOAA NCEI grids  
  - Mesonet observation grids  

Any mismatch → **CI Hard Fail**.

---

## 🔁 6. Integration in the SMAP ETL Chain

~~~text
decode
 → reprojection (uses grid_defs/*)
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking (CARE/H3)
 → STAC Item/Collection construction
 → DCAT dataset registration
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

Grid definitions power the **entire spatial branch** of this pipeline.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
- Soil moisture wetness fields  
- Freeze-line detection  
- Floodplain infiltration  

### Climate  
- Vegetation moisture  
- Seasonal anomalies  

### Archaeology  
- Site-landscape spatial context  
- Vegetation masking  

### Story Node v3  
- Spatial anchoring of historical/cultural events  

### Focus Mode v3  
- Reliable spatial reasoning  
- Layer alignment  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                             |
|--------:|------------|-----------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full grid-defs documentation; emoji layout; governance/H3 rules; CRS/STAC alignment; CI-safe.      |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal grid-definition notes.                                                              |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗺️ Reprojection Layer](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

