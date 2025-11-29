---
title: "🌱 NASA SMAP — Soil Moisture STAC Items for 2025 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/smap/stac/soil-moisture/2025/README.md"
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

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-smap-soil-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Overview"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-A / CARE-B (depending on geographic overlap)"
indigenous_rights_flag: true
sensitivity_level: "Low (raw) / Medium (derived)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "ProperInterval"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../schemas/json/stac-smap-soil-v11.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/stac-smap-soil-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:soil-moisture:2025:readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-stac-soil-2025"
event_source_id: "ledger:docs/data/satellites/smap/stac/soil-moisture/2025/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next per-year STAC revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌱 **NASA SMAP — Soil Moisture STAC Items (Year: 2025)**  
`docs/data/satellites/smap/stac/soil-moisture/2025/README.md`

**Purpose**  
Document the **daily and 3-day SMAP Soil Moisture STAC Items** for the year **2025**,  
fully aligned with **KFM-STAC v11**, FAIR+CARE governance, sovereignty masking rules,  
and KFM’s hydrology/climate ETL pipelines.

</div>

---

## 📘 1. Overview

This directory contains *all* **per-day** or **3-day** SMAP Soil Moisture STAC Items for **2025**.

Each Item contains:

- 🌱 Soil moisture estimate (`m³/m³`)  
- 🌿 Vegetation water content modifier  
- ⚠️ QA & RFI contamination masks  
- 📉 Uncertainty layers  
- 🌍 EASE-Grid 2.0 → KFM CRS geolocation  
- 🧭 BBox + geometry footprints  
- 🔐 CARE/H3 sovereignty protection (if applicable)  
- 🧾 PROV-O lineage from L2/L3 SMAP → KFM  

These Items support:

- Drought modeling  
- Story Node v3 environmental overlays  
- Focus Mode v3 hydrology background context  
- Cross-mission fusion with HydroGNSS, Mesonet, NCEI, ERA5  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A · v11.2.2)

~~~text
docs/data/satellites/smap/stac/soil-moisture/2025/
├── 📄 README.md                           # This file
│
├── 📅 2025-01-01-item.json                # STAC Item (daily/3-day composite)
├── 📅 2025-01-02-item.json
├── 📅 2025-01-03-item.json
├── 📅 ... (one Item per day or composite)
│
└── 🗃️ assets/                             # Stored COGs & supporting layers
    ├── 🌱 soil-moisture.tif                # Primary soil moisture raster
    ├── 📈 soil-moisture-uncertainty.tif    # Uncertainty layer
    ├── ⚠️ qa-flags.tif                      # QA/RFI mask
    └── 🧾 metadata.json                    # Orbit/grid/provenance metadata
~~~

Notes:

- All Item filenames must follow:  
  `YYYY-MM-DD-item.json`  
- COG filenames follow KFM naming convention:  
  `soil-moisture_<YYYYMMDD>.tif`  

---

## 🧩 3. STAC Item Requirements (Daily / 3-Day Composites)

Each STAC Item in this folder MUST contain:

### Required Fields

- `"type": "Feature"`  
- `"id": "smap-soil-2025-<date>"`  
- `"collection": "smap-soil-moisture"`  
- `geometry` + `bbox`  
- `properties.datetime` or `start_datetime` + `end_datetime`  
- `kfm:unit: "m3/m3"`  
- `kfm:uncertainty`  
- `kfm:qa_flags`  
- `kfm:care_label`  
- `kfm:sovereignty_note`  
- `kfm:mask_applied` (if H3 generalization used)  

### Required Asset Roles

- `data` → soil moisture raster  
- `qa` → QA/RFI flag raster  
- `uncertainty` → uncertainty raster  
- `metadata` → grid/orbit/sensor metadata  

---

## 🔐 4. Governance & Sovereignty Safeguards

Because soil moisture can reveal sensitive patterns related to:

- wetland activation  
- land management  
- ecological stress  
- cultural or tribal areas  

KFM enforces:

- **CARE-A/B labelling**  
- **Dynamic H3 masking** – upscaling to a safe resolution near protected lands  
- No display of raw anomalies in sensitive areas  
- Lineage + uncertainty disclosure in all derived views  
- Full sovereignty audit at STAC creation time  

All Items must pass:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml` QA hooks  

---

## 🧪 5. QA & Validation

Each Item undergoes:

- JSON Schema validation  
- BBox/geometry validation (GeoJSON-safe)  
- Temporal validation  
- Raster integrity check  
- QA mask alignment (`qa-flags.tif`)  
- Cross-sensor QA vs:
  - HydroGNSS  
  - Mesonet  
  - NOAA NCEI Drought Monitor  
  - ERA5  

QA results feed into:  
`docs/data/satellites/smap/qa/`

---

## 🔁 6. Ingestion → Lineage Workflow (2025)

```
NASA SMAP L2/L3 Product
 → decode + EASE-Grid mapping
 → QA + RFI flag integration
 → extract soil moisture band
 → spatial reprojection (to KFM CRS)
 → STAC Item creation (daily/3d)
 → CARE/H3 masking check
 → lineage + uncertainty export
 → catalog registration (STAC/DCAT)
 → telemetry (OpenLineage + OTel)
```

All steps are reproducible and WAL-protected.

---

## 🔮 7. Applications Inside KFM (2025 Data)

### 🌡️ Climate  
- Drought index calibration  
- Monthly anomaly mapping  

### 💧 Hydrology  
- Wetness preconditioning before floods  
- Soil infiltration modeling  

### 🏺 Archaeology  
- Seasonal wetness support for Story Node v3  
- Site-accessibility inference  
- Vegetation context (via linked vegetation-water layers)  

### 🛰 Multi-Sensor Fusion  
- HydroGNSS GNSS-R soil moisture  
- Mesonet in-situ moisture  
- ERA5 + NCEI land-surface models  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                               |
|--------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Created full v11.2.2 STAC-year README; emoji layout; CARE/H3 rules; ingestion + governance alignment. |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal STAC structure.                                                                       |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ Soil Moisture STAC](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

