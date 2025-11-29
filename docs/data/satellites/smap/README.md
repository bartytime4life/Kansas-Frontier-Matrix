---
title: "🛰️ NASA SMAP — Soil Moisture Active/Passive Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/smap/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-A / Indigenous Sensitivity Reviewed"
classification: "Public Dataset Overview"
sensitivity_level: "Low (raw) / Medium (derived)"
public_exposure_risk: "Low"
indigenous_rights_flag: true
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "Dataset"
  owl_time: "ProperInterval"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/dataset-smap-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/dataset-smap-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-overview"
event_source_id: "ledger:docs/data/satellites/smap/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded on next SMAP-layer revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **NASA SMAP — Soil Moisture Active/Passive (v11.2.2)**  
`docs/data/satellites/smap/README.md`

### L-Band Radiometer · Freeze/Thaw · Soil Moisture Profiles  
### Global Water-Cycle Backbone for KFM Hydrology & Drought Pipelines

</div>

---

## 📌 Purpose

This directory documents the **NASA SMAP (Soil Moisture Active/Passive)** integration layer inside the Kansas Frontier Matrix (KFM).

SMAP provides **global L-band microwave soil moisture**, freeze/thaw, vegetation water content, and ancillary variables that form a **core input** to:

- KFM climate & drought analysis  
- Hydrology & ecohydrology ETL  
- Story Node v3 context layers  
- Focus Mode v3 drought/wetness narratives  
- Multi-sensor blending (HydroGNSS, Mesonet, NCEI, ERA5, NOAA indices)  

---

## 🌎 Mission Snapshot (KFM Knowledge Capsule)

- **Agency:** NASA  
- **Launch Date:** 31 January 2015  
- **Orbit:** Sun-synchronous, ~685 km, 6 AM descending node  
- **Sensor:** L-Band Radiometer (1.41 GHz)  
- **Revisit:** 2–3 days  
- **Swath:** ~1000 km  
- **Active SAR failed in 2015 → radiometer-only mode** (still highly valuable)

SMAP remains the **gold-standard** for global soil moisture and freeze–thaw detection.

---

## 📥 Why SMAP Matters in KFM

SMAP provides:

- 🌱 **Absolute soil moisture** (surface ~5 cm)  
- ❄️ **Freeze/thaw indicators**  
- 🌿 **Vegetation water content**  
- 🔍 **Deep water-cycle continuity**  
- 🛰️ **Cross-sensor fusion anchor** for HydroGNSS, Mesonet, ERA5  

KFM uses SMAP to:

- Calibrate and validate HydroGNSS GNSS-R moisture  
- Feed soil-water balance + runoff ETL  
- Support archaeological landscape moisture reconstructions  
- Anchor Focus Mode v3 “Drought Context” narratives  
- Normalize STAC temporal alignment across missions  

---

## 🗂️ Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/
├── 📄 README.md                        # This file
│
├── 🗂️ stac/                             # STAC Collections + Items for SMAP variables
│   ├── 🌱 soil-moisture/               # Primary L2/L3 soil moisture
│   ├── ❄️ freeze-thaw/                 # Freeze/thaw state (L3_FT)
│   ├── 🌿 vegetation-water/            # Vegetation water content
│   ├── ⚠️ qa-flags/                    # Quality flags, uncertainty surfaces
│   └── 📚 ancillary/                   # Ancillary orbits, grids, sensor geometry
│
├── 🧾 metadata/                        # DCAT, JSON-LD, PROV-O lineage metadata
├── 🛠️ transforms/                      # Harmonization + grid projection + band extraction
├── 🧪 qa/                              # QA, cross-mission comparisons (SMAP × HydroGNSS × Mesonet)
└── 🧷 samples/                          # Sample L3 rasters + STAC onboarding examples
~~~

---

## 🧩 Data Standards & Integration Model

### 📦 STAC-Level Harmonization (KFM-STAC v11)

Each SMAP variable is converted into:

- Mission-specific **STAC Collections**  
- Daily/3-day **STAC Items**  
- Assets:
  - COGs (primary)
  - Optional Zarr/NetCDF for long-range analyses  
- Metadata:
  - Footprint geometry  
  - Temporal extent (OWL-Time compliant)  
  - Grid metadata (EASE-Grid 2.0)  
  - Uncertainty & quality controls  

### 🧾 Metadata Stack

- **FAIR:** provenance, discoverability, versioning  
- **CARE:** sovereignty & sensitivity review (especially freeze/thaw → access vulnerability)  
- **PROV-O:** explicit derivations from NASA L2/L3 source products  
- **JSON-LD:** schema.org + GeoSPARQL + OWL-Time alignment  

### 🔗 Hydrology + Climate Interoperability

- Soil moisture feeds:
  - drought ETL  
  - hydrologic response models  
  - floodplain wetness analysis  
- Freeze/thaw integrates with:
  - ecohydrology models  
  - hazard layers (infrastructure, erosion risk)  

---

## 🛠️ KFM Ingestion Pipeline

1. Detect new NASA L2/L3 SMAP datasets  
2. Retrieve → stage → decode → geolocation  
3. Regrid (EASE-Grid ↔ KFM CRS)  
4. Extract variables & QA masks  
5. Create STAC Items/Collections  
6. Cross-compare with:
   - HydroGNSS  
   - Mesonet  
   - NCEI/NOAA drought indices  
7. Produce:
   - PROV-O lineage  
   - Dataset QA summary  
   - Telemetry (energy, carbon, compute)  
8. Register in:
   - `data/stac/catalog.json`
   - `docs/data/metadata/**`  

All ingestion steps are **OpenLineage-instrumented** and reproducible.

---

## 🔮 Applications Inside KFM

### 🌡️ Climate  
- Drought tracking  
- Wet/dry anomaly detection  
- Seasonal freeze line tracking  

### 🏺 Archaeology  
- Wetland reactivation indicators  
- Vegetation + freeze/thaw effects on site visibility  
- Paleo-hydrology reconstruction support  

### 💧 Hydrology  
- Soil infiltration modeling  
- Floodplain wetness  
- Groundwater recharge constraints (indirect)  

### 🌾 Ecology  
- Vegetation water availability  
- Fire risk preconditioning  

---

## 🔐 Governance & Sensitivity Notes

SMAP is open, but derived layers **must follow**:

- **CARE-A/CARE-B** labeling when intersecting tribal lands  
- H3-based generalization for:
  - biomass-related moisture  
  - inundation/freeze–thaw zones  
- No raw high-resolution anomalies in sensitive landscapes  
- Sovereignty checks for all downstream Story Node v3 and Focus Mode v3 layers  

All derived products must include:

- Provenance  
- Uncertainty  
- CARE/H3 masking details  

---

## 🧭 Version History

| Version | Date       | Summary                                                                                           |
|--------:|------------|---------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full v11.2.2 upgrade; emoji directory; governance/H3 updates; multi-mission integrations aligned. |
| v10.4.0 | 2025-11-15 | Early SMAP integration notes.                                                                     |
| v10.3.2 | 2025-11-14 | Pre-v11 Satellite data block.                                                                     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ Satellite Catalog](../README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

