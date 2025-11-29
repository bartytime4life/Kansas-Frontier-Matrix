---
title: "📦 NASA SMAP — Soil Moisture Assets (2025) · COG, QA, Uncertainty (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/data/satellites/smap/stac/soil-moisture/2025/assets/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-soil-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Asset Overview"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-A / CARE-B (intersection-dependent)"
indigenous_rights_flag: true
sensitivity_level: "Low (raw) / Medium (derived)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false
data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "DataDownload"
  owl_time: "ProperInterval"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../../schemas/json/stac-smap-soil-v11.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/stac-smap-soil-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:soil-moisture:2025:assets-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-soil-2025-assets"
event_source_id: "ledger:docs/data/satellites/smap/stac/soil-moisture/2025/assets/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next SMAP asset-schema revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — Soil Moisture Assets (2025)**  
`docs/data/satellites/smap/stac/soil-moisture/2025/assets/README.md`

**Purpose**  
Document the **per-Item asset set** for daily/3-day SMAP Soil Moisture STAC Items for **2025**.  
These assets represent the **actual geospatial rasters and metadata** referenced by each STAC Item  
(data, QA, uncertainty, ancillary), packaged according to **KFM-STAC v11** and governed under  
FAIR+CARE + sovereignty rules.

</div>

---

## 📘 1. Overview

Each STAC Item for SMAP Soil Moisture (2025) links to **four core asset types**:

- 🌱 **Soil Moisture COG** — primary radiometric soil moisture value (`m³/m³`)  
- ⚠️ **QA Flags COG** — RFI contamination, gain stability, surface-condition flags  
- 📈 **Uncertainty COG** — pixel-level uncertainty estimates  
- 🧾 **Metadata JSON** — orbit, grid, calibration, lineage notes  

Assets are:

- Stored in **Cloud-Optimized GeoTIFF (COG)** format  
- Indexed in STAC Items using the `data`, `qa`, `uncertainty`, and `metadata` roles  
- Aligned to the **EASE-Grid 2.0** reference grid  
- Reprojected to KFM CRS during ETL when needed  
- Covered by **CARE + sovereignty masking rules**  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/soil-moisture/2025/assets/
├── 📄 README.md                         # This file
│
├── 🌱 soil-moisture.tif                 # Primary SMAP soil moisture COG
├── ⚠️ qa-flags.tif                      # QA / RFI mask raster
├── 📈 soil-moisture-uncertainty.tif      # Uncertainty raster (per-pixel variability)
└── 🧾 metadata.json                     # Orbit + grid + provenance metadata
~~~

Each STAC Item for 2025 points into this directory via relative asset HREFs.

---

## 🧩 3. Asset Specifications (KFM-STAC v11)

### 🌱 **soil-moisture.tif**

- Unit: `m3/m3`  
- Grid: EASE-Grid 2.0  
- Required raster extension fields:
  - `raster:bands[0].scale`, `offset`, `nodata`, `data_type`  
  - `proj:epsg`, `proj:shape`, `proj:transform`  
- CARE/H3 masking applied where necessary

### ⚠️ **qa-flags.tif**

Contains RFI, calibration, and radiometer-status quality flags.  
Required metadata:

- `kfm:qa_flag_schema`  
- `kfm:qa_values` (coded legend)  
- `kfm:qa_interpretation`  

### 📈 **soil-moisture-uncertainty.tif**

Uncertainty band aligned to soil moisture raster:

- `kfm:stdev`  
- `kfm:error_model`  
- `kfm:uncertainty_type` (radiometric / retrieval)

### 🧾 **metadata.json**

Must include:

- Orbit parameters  
- Incidence angle  
- Grid metadata (EASE-Grid)  
- Provenance:
  - NASA SMAP L2/L3 product IDs  
  - Processing chain  
  - Reprojection steps  

---

## 🔐 4. Governance & Sovereignty

Because soil moisture may imply environmental stress, hydrologic change, or wetland reactivation:

- **CARE-A/B** labels applied where overlapping tribal or sensitive lands  
- **H3 generalization** enforced for any derived wetness anomaly layers  
- STAC Items **must** include:
  - `kfm:care_label`  
  - `kfm:sovereignty_note`  
  - `kfm:mask_applied` (if generalization performed)

No precise-pixel anomalies are displayed in sensitive regions.

---

## 🧪 5. QA & Validation

All assets undergo:

- COG structure validation  
- Raster alignment check (soil, qa, uncertainty)  
- Temporal consistency checks vs original SMAP products  
- Geometry + BBox comparisons against STAC metadata  
- Cross-sensor checks (HydroGNSS, Mesonet, ERA5)  

QA logs appear in:

`docs/data/satellites/smap/qa/`

Telemetry exported to:

`releases/<version>/data-telemetry.json`

---

## 🔁 6. Ingestion Lineage

Each asset set represents:

```
NASA SMAP L2/L3 Radiometer Product
 → decode + resample (EASE-Grid)
 → QA mask integration
 → uncertainty propagation
 → COG creation
 → CARE/H3 masking checks
 → STAC Item asset registration
```

All lineage is exported to PROV-O and OpenLineage.

---

## 🔮 7. Applications Inside KFM

### Hydrology
- Floodplain wetness mapping  
- Soil infiltration estimation  
- Drought classification  

### Climate
- Soil moisture anomaly trends  
- Freeze-line inference (cross-mission)

### Archaeology
- Wetness & landscape access patterns  
- Vegetation-linked site visibility  

### Story Node v3  
- Temporal-spatial environmental context layers  

### Focus Mode v3  
- “Environmental background” contextualization per entity  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                               |
|--------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Created full asset-level README; governance, QA, STAC v11 alignment; emoji layout; CI-safe.           |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal placeholder.                                                                          |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ 2025 STAC Items](../README.md) · [🛡 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

