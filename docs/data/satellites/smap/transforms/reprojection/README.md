---
title: "🗺️ NASA SMAP — Reprojection Stage (EASE-Grid 2.0 → KFM CRS) · ETL Stage 2 (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/data/satellites/smap/transforms/reprojection/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
provenance_profile: "KFM-PROV-O v11.2"
jsonld_profile: "KFM-JSONLD v11"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public ETL Documentation"
fair_category: "F1-A1-I2-R3"
care_label: "CARE-A / CARE-B depending on spatial intersection"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
risk_category: "Low"
public_exposure_risk: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../schemas/json/transform-smap-reprojection-v11.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/transform-smap-reprojection-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:transform:reprojection-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-transform-reprojection"
event_source_id: "ledger:docs/data/satellites/smap/transforms/reprojection/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next SMAP reprojection pipeline revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🗺️ **NASA SMAP — Reprojection Stage (EASE-Grid 2.0 → KFM CRS)**  
`docs/data/satellites/smap/transforms/reprojection/README.md`

**Purpose**  
Document ETL **Stage 2: Reprojection**, converting NASA’s EASE-Grid 2.0  
(L3) and swath-mapped (L2) radiometer products into **KFM’s unified spatial CRS**,  
ensuring geometric consistency across hydrology, climate, archaeology, ecology,  
Story Node v3, and Focus Mode v3.

</div>

---

## 📘 1. Overview

The **Reprojection Stage**:

- 🗺️ Converts **EASE-Grid 2.0 → KFM CRS**  
- 🧭 Handles swath-derived geolocation (L2)  
- 📏 Enforces BBox normalization & anti-meridian safety  
- 🧠 Ensures consistent grid alignment  
- ⚠️ Preserves QA semantics  
- 📉 Applies uncertainty interpolation rules  
- 🔐 Propagates CARE/H3 governance flags  
- 🧾 Annotates spatial provenance for STAC/DCAT/PROV-O  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/reprojection/
├── 📄 README.md                        # This file
│
├── 🗺️ ease_to_kfm_grid.py              # Core reprojection engine
├── 🧭 geolocation_utils.py             # CRS + L2 swath helpers
├── 📏 bbox_normalization.py            # BBox/antimeridian correction logic
│
├── 📚 grid_defs/                       # Projection definitions
│   ├── ease_grid_2.0.json
│   ├── kfm_crs.json
│   └── cell_mappings.json
│
└── 🧪 tests/
    ├── test_ease_projection.py
    ├── test_bbox_normalization.py
    └── test_crs_integrity.py
~~~

---

## 🧩 3. Responsibilities

### 🗺️ EASE-Grid 2.0 → KFM CRS Conversion
- Equal-area → geographic conversion  
- Pixel-edge/pixel-center consistency  
- Multi-resolution handling  

### 🧭 Swath-Level (L2) Geolocation
- Lat/Lon + incidence angle → regular grid  
- Brightness-temperature geometry correction  

### 📏 Geometry + BBox Safety
- Anti-meridian fix  
- Proper winding order  
- STAC-valid bounding boxes  

### 📉 Uncertainty Interpolation
- Unit-aware resampling  
- No artificial sharpening of environmental signals  

### 🔗 Metadata Harmonization
- Update:
  - `proj:*`
  - `raster:*`
  - KFM provenance  
  - Grid definitions & transforms  

### 🔐 Governance-Aware Spatial Logic
- Preserve CARE + sovereignty markers  
- Add H3 sensitivity flags without masking  
- Ensure transforms never increase precision in restricted areas  

---

## 🔐 4. Governance & Sovereignty Rules

Reprojection must:

- Keep CARE/H3 flags intact  
- Identify sovereign H3 intersections  
- Maintain ethical de-precision around sensitive zones  
- Prepare datasets for downstream masking (Stage 6)  

Validated by:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 5. QA & Validation

Checks include:

- CRS integrity  
- Geometry validity  
- BBox vs geometry consistency  
- Raster alignment  
- Uncertainty-resampling correctness  
- Cross-sensor consistency with:
  - HydroGNSS  
  - Mesonet  
  - NCEI/NOAA  
  - ERA5-Land  

Results stored under:

`docs/data/satellites/smap/qa/`

Telemetry → `releases/<version>/data-telemetry.json`

---

## 🔁 6. Integration in the Full ETL Chain

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking (CARE/H3)
 → STAC Item/Collection construction
 → DCAT dataset registration
 → PROV-O lineage export
 → OpenLineage telemetry emission
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
- Soil moisture consistency  
- Freeze-line structure  

### Climate  
- Seasonal anomaly grids  

### Archaeology  
- Vegetation masking consistency  
- Environmental transitions  

### Story Node v3 & Focus Mode v3  
- Accurate spatial anchors  
- Reliable environmental context  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                         |
|--------:|------------|-------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Fixed fenced-block break; fully v11.2.2 compliant; emoji layout; governance/H3 validation.      |
| v10.3.2 | 2025-11-14 | Early pre-v11 version.                                                                           |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🛠️ SMAP Transform Layer](../README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

