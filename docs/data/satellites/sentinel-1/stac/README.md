---
title: "🗂️ ESA Sentinel-1 — STAC Collections & Items (SAR · Coherence · Flood · Wetlands · RTC)"
path: "docs/data/satellites/sentinel-1/stac/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Earth Observation (CC-BY-4.0)"
status: "Active / Enforced"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F2-A1-I2-R4"
care_label: "CARE-A / CARE-B (depending on downstream derivative)"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/sentinel1-stac-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-stac-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel-1:stac-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded upon next ESA reprocessing cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🗂️ **Sentinel-1 STAC Collections & Items**  
`docs/data/satellites/sentinel-1/stac/`

**Synthetic Aperture Radar (SAR) STAC ecosystem for KFM v11:**  
GRD · GRDH · RTC · Coherence · Deformation (InSAR) · Flood · Wetlands

</div>

---

## 📘 1. Overview

This directory defines the **STAC Collections and Items** that represent the governed  
Sentinel-1 SAR datasets within the Kansas Frontier Matrix v11:

- **Ground Range Detected (GRD / GRDH)** backscatter  
- **Radiometrically Terrain Corrected (RTC)** sigma0/gamma0  
- **Coherence** products (temporal coherence)  
- **Flood mapping** layers  
- **Wetland indicators**  
- **Deformation (InSAR)** LOS displacement (sovereignty-generalized when required)  
- **Ancillary** metadata and calibration assets  

Each product is:

- fully STAC 1.x compliant  
- JSON-LD embedded  
- DCAT 3.0 compatible  
- configured for PROV-O lineage  
- FAIR+CARE + sovereignty-safe  
- versioned and CI-validated  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/sentinel-1/stac/
├── 📄 README.md                           # This file
│
├── 🗂️ collections/                        # STAC Collections (one per product family)
│   ├── collection_grd.json                # GRD (VV/VH)
│   ├── collection_grdh.json               # High-resolution GRDH
│   ├── collection_rtc.json                # Radiometrically Terrain Corrected
│   ├── collection_coherence.json          # Coherence series
│   ├── collection_deformation.json        # Sovereignty-safe InSAR (LOS)
│   ├── collection_flood.json              # Floodwater detection
│   └── collection_wetlands.json           # Wetlands / inundation
│
├── 🧩 items/                               # Scene-level STAC Items
│   ├── grd/                               # GRD scene Items
│   ├── grdh/                              # GRDH scene Items
│   ├── rtc/                               # RTC sigma0/gamma0 items
│   ├── coherence/                         # Coherence tiles
│   ├── deformation/                       # Displacement tiles (masked/generalized)
│   ├── flood/                             # Flood-mapping Items
│   └── wetlands/                          # Wetlands Items
│
└── 📁 metadata/                            # Supplemental structured metadata
    ├── dcat/                               # DCAT Dataset & Distribution blocks
    ├── jsonld/                             # JSON-LD contexts and provenance
    └── provenance/                         # PROV-O lineage templates
~~~

---

## 🧩 3. STAC Product Families in KFM v11

### 🛰️ Ground Range Detected (GRD / GRDH)
- Calibrated σ⁰  
- VV/VH backscatter  
- Multi-temporal stacks for land-change & hydrology context  

### 🛰️ Radiometrically Terrain Corrected (RTC)
- γ⁰ backscatter  
- DEM-corrected  
- Stable for time-series SAR analytics  

### 🔗 Coherence (Temporal)
- Flood damage detection  
- Agricultural disturbance  
- Landcover change  

### 🌍 InSAR Deformation (Sovereignty-Generalized)
- LOS displacement  
- Seasonal ground motion  
- Long-term subsidence  
- **Generalized inside tribal/sovereign H3 cells** via KFM sovereignty engine  

### 🌊 Flood Detection
- VH/VV thresholding  
- Otsu, cluster, or ML-based flood classifiers  
- Linked to hydrology Story Nodes  

### 🌿 Wetlands / Soil Saturation
- Backscatter- and coherence-based detection  
- Optional integration with SMAP/HydroGNSS derivatives  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

**Critical:**  
SAR can reveal sensitive environmental and infrastructural patterns.  
KFM enforces:

- `"kfm:h3_sensitive"` propagation in Items  
- `"kfm:mask_required"` for deformation & flood layers near sovereign zones  
- `"kfm:care_label"` & `"kfm:care_label_reason"`  
- `"kfm:sovereignty_uncertainty_floor"` for derived layers  
- `"kfm:governance_notes"` describing masking/generalization  
- geometric generalization where risk of sensitive inference exists  

All validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🛠️ 5. Asset Types Used in Sentinel-1 STAC Items

- **COGs** (Cloud-Optimized GeoTIFFs)  
- **NetCDF/Zarr** (for coherence stacks)  
- **PNG** thumbnails  
- **JSON** metadata (ancillary/orbit/calibration)  

Asset fields include:

- `s1:instrument_mode`  
- `s1:polarization` (VV/VH)  
- `proj:epsg`  
- `sar:frequency_band = "C"`  
- `sar:product_type` (GRD/GRDH/RTC)  
- temporal & spatial extents  
- KFM governance metadata  
- PROV-O lineage descriptors  

---

## 🧪 6. Validation Workflow (CI)

CI tests:

- STAC schema validity  
- collection/item link graph correctness  
- geometry consistency  
- footprint vs. raster alignment  
- governance metadata presence  
- sovereignty generalization  
- PROV-O lineage embedding  
- DCAT compatibility  

Failing Items are **blocked from release**.

---

## 🔁 7. End-to-End Pipeline Relationship

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → RTC (optional)
 → speckle filtering
 → coherence / deformation / flood detection
 → sovereignty masking
 → STAC Item generation
 → STAC Collection update
 → governed release bundle
~~~

---

## 🔮 8. Applications in KFM

- flood-extent modeling  
- hydrology & watershed analysis  
- ecological monitoring  
- cultural-landscape risk assessment  
- land-change & disturbance monitoring  
- Focus Mode v3 environmental evidence panels  
- Story Node v3 spatial context  

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                                      |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 STAC README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; emoji-rich; CI-safe.        |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🛠 Transforms](../transforms/README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

