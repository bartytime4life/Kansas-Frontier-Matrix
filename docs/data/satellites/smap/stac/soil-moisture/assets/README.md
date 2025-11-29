---
title: "📦 NASA SMAP — Global Soil Moisture Asset Definitions (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/data/satellites/smap/stac/soil-moisture/assets/README.md"
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

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-smap-soil-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Asset Overview"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-A / CARE-B depending on location"
indigenous_rights_flag: true
sensitivity_level: "Low (raw) / Medium (derived wetness indicators)"
public_exposure_risk: "Low"
redaction_required: false
risk_category: "Low"

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "DataDownload"
  prov_o: "prov:Entity"
  owl_time: "ProperInterval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../schemas/json/stac-smap-soil-v11.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/stac-smap-soil-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:soil-moisture:assets:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-soil-assets"
event_source_id: "ledger:docs/data/satellites/smap/stac/soil-moisture/assets/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next soil-moisture asset-schema revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — Soil Moisture Asset Definitions (Global)**  
`docs/data/satellites/smap/stac/soil-moisture/assets/README.md`

**Purpose**  
Define the **global asset templates** used for all SMAP Soil Moisture STAC Items  
(2023, 2024, 2025, …), including the COG rasters, QA masks, uncertainty layers,  
and metadata JSON objects used across the entire KFM STAC ingestion pipeline.

</div>

---

## 📘 1. Overview

SMAP’s L-band radiometer products provide:

- 🌱 **Surface soil moisture** (0–5 cm)  
- 📉 **Uncertainty estimates**  
- ⚠️ **RFI + QA masks**  
- 🧾 **Orbit/grid/sensor metadata**  

These global asset definitions act as the **shared schema** for all SMAP per-day  
STAC Items, ensuring:

- Consistency across years  
- FAIR+CARE & sovereignty enforcement  
- STAC/DCAT/PROV alignment  
- Deterministic ingestion & lineage tracking  
- Valid cross-mission fusion with HydroGNSS, Mesonet, ERA5, NCEI  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/soil-moisture/assets/
├── 📄 README.md                          # This file
│
├── 🌱 soil-moisture.tif                  # Global SMAP soil moisture raster template
├── ⚠️ qa-flags.tif                       # QA/RFI mask (radiometer condition flags)
├── 📈 soil-moisture-uncertainty.tif      # Uncertainty raster (stdev/error estimates)
└── 🧾 metadata.json                      # Orbit/grid/provenance metadata (EASE-Grid, processing notes)
~~~

👉 **These serve as the canonical asset schema** for all per-Item files inside e.g.:  
`docs/data/satellites/smap/stac/soil-moisture/YYYY/assets/`.

---

## 🧩 3. Asset Specifications (KFM-STAC v11)

### 🌱 soil-moisture.tif — Primary Soil Moisture Raster

- Unit: `m3/m3`  
- Grid: **EASE-Grid 2.0**  
- Required metadata:
  - `raster:bands[0]`  
  - `proj:epsg`, `proj:shape`, `proj:transform`  
  - `kfm:unit`  
  - `kfm:uncertainty_link`  

### ⚠️ qa-flags.tif — QA & RFI Mask

Encodes:

- Radiometric QC flags  
- RFI detection  
- Gain stability issues  
- Retrieval confidence drops  

Metadata required:

- `kfm:qa_flag_schema`  
- `kfm:qa_values`  
- `kfm:qa_interpretation`  

### 📈 soil-moisture-uncertainty.tif — Uncertainty Raster

Contains:

- Per-pixel uncertainty  
- Retrieval confidence  
- Radiometric noise propagation  

Metadata required:

- `kfm:uncertainty_type: "radiometric"`  
- `kfm:stdev`  
- `kfm:error_model`  

### 🧾 metadata.json — Orbit/Grid/Provenance Metadata

Must include:

- NASA L2/L3 reference product IDs  
- Orbit parameters & sensor geometry  
- EASE-Grid metadata  
- Calibration/processing notes  
- `kfm:lineage` block (PROV-O linked)  
- `kfm:care_label` + sovereignty notes  

---

## 🔐 4. Governance & Sovereignty

Soil moisture layers may indicate:

- wetland activation  
- drought stress  
- access to sensitive land  
- vegetation/hydrology conditions relevant to tribal territories  

Thus KFM requires:

- **CARE-A/B labels** where applicable  
- **H3 generalization** in sensitive geographies  
- `"kfm:mask_applied": true` when masking is active  
- Explicit lineage + uncertainty in derived visual layers  

All assets are validated via:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`  

---

## 🧪 5. QA & Validation Requirements

Asset QA includes:

- COG structural validation  
- Raster alignment checks (soil, QA, uncertainty)  
- BBox/geometry consistency with STAC Items  
- Temporal consistency  
- Cross-sensor QA vs:
  - HydroGNSS  
  - Mesonet  
  - NOAA NCEI & USGS products  
  - ERA5-Land  

QA reports stored in:  
`docs/data/satellites/smap/qa/`

Telemetry published to:  
`releases/<version>/data-telemetry.json`

---

## 🔁 6. Ingestion → Lineage Workflow

```
NASA SMAP L2/L3 Product
 → decode + EASE-Grid mapping
 → QA mask integration
 → uncertainty propagation
 → COG/template creation
 → CARE/H3 enforcement
 → STAC asset registration
 → OpenLineage & OTel telemetry
 → DCAT registration
```

All steps are WAL-protected and deterministic.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
- Floodplain wetness  
- Soil infiltration  
- Runoff modeling  

### Climate  
- Drought severity  
- Soil moisture anomalies  
- Seasonal moisture cycles  

### Archaeology  
- Cultural landscape wetness context  
- Vegetation/wetness interpretation  

### Story Node v3  
- Environmental context layers  

### Focus Mode v3  
- Drought/wetness contextualization per entity/event  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                 |
|--------:|------------|---------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Created global soil-moisture asset README; emoji layout; governance/H3; STAC v11 compliance; CI-safe.  |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal asset notes.                                                                            |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ Soil Moisture STAC](../README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

