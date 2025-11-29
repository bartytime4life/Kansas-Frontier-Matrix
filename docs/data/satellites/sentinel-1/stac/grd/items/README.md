---
title: "🛰️ Sentinel-1 GRD — Scene-Level STAC Items (σ⁰ VV/VH Backscatter · Hydrology · Land-Change)"
path: "docs/data/satellites/sentinel-1/stac/grd/items/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Earth Observation (CC-BY-4.0)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

license: "CC-BY-4.0 (ESA)"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F2-A1-I2-R4"
care_label: "CARE-A / CARE-B (depending on derived usage)"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: false

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-grd-items-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-grd-items-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-grd-items-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-grd-items"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/grd/items/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded on next ESA GRD reprocessing cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **Sentinel-1 GRD — Scene-Level STAC Items**  
`docs/data/satellites/sentinel-1/stac/grd/items/`

Governed STAC Items for  
**σ⁰ VV/VH calibrated backscatter**,  
used for hydrology, agriculture, hazard mapping, flood pre/post analysis, and land-change.

</div>

---

## 📘 1. Overview

Sentinel-1 **GRD Items** represent the core backscatter imagery used for mid-resolution  
environmental and land-surface analysis.

Each Item provides:

- σ⁰ **VV** and **VH** backscatter  
- full spatial footprint  
- ESA SAFE metadata  
- STAC 1.x compliance with SAR extension  
- JSON-LD semantics (SAR, GeoSPARQL, OWL-Time, KFM governance)  
- DCAT distribution crosswalk  
- PROV-O lineage (ESA scenes → GRD transform pipeline)  
- sovereignty-aware metadata (H3-generalization when triggered)  
- FAIR+CARE compliance  

GRD Items act as **inputs for RTC, coherence, flood, wetlands, and deformation products**.

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/grd/items/
├── 📄 README.md
│
├── 🛰️ S1A_IW_GRD_20250311T112845.json
├── 🛰️ S1B_IW_GRD_20250419T223015.json
└── …           # Additional sovereign-aware scene-level GRD Items
~~~

---

## 🧩 3. GRD STAC Item Structure

### 🌐 Core STAC Fields
- `id`, `type = "Feature"`  
- `datetime`  
- `"sar:product_type" = "GRD"`  
- `"sar:instrument_mode" = "IW"`  
- `"sar:polarizations" = ["VV","VH"]`  
- `"sar:frequency_band" = "C"`  
- `proj:*` (EPSG, transform, raster size)  
- orbit metadata (`cycle_number`, `relative_orbit`, `orbit_state`)  

---

### 🗺 Geometry (Sovereignty-Aware)
- footprint polygon  
- `bbox`  
- when sovereign H3 cells intersect:  
  - generalization applied  
  - `"kfm:mask_required"` set  

---

### 📦 Assets
- `"sigma0_vv"` → COG (calibrated σ⁰ VV)  
- `"sigma0_vh"` → COG (calibrated σ⁰ VH)  
- `"thumbnail"` → PNG preview  
- `"qa"` → QA mask (border noise, calibration flags)  
- `"metadata"` → ESA SAFE + transform metadata  

Optional:
- `"incidence_angle"` layer  
- `"orbit"` metadata asset  

---

### 🔗 Link Graph
- `"self"`  
- `"collection"` → GRD collection  
- `"parent"`  
- `"root"`  
- `"derived_from"` → ESA SAFE scene  

---

### 🧬 PROV-O Lineage
Includes:

- `prov:wasGeneratedBy` → GRD processing activity  
- `prov:used` → orbit files, auxiliary calibration data, ESA SAFE scene  
- `prov:wasDerivedFrom` → original ESA source products  
- sustainability metadata:
  - `"kfm:energy_wh"`  
  - `"kfm:carbon_gco2e"`  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

GRD is lower sensitivity than GRDH/InSAR, but still subject to governance:

**Required fields:**

- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"` (if sovereign areas affected)  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  
- `"kfm:care_label_reason"`  

Generalization rules apply if:

- backscatter reveals sovereign land surface change  
- flood/mapping derivatives could be inferred  
- land-use transitions are sensitive  

CI checks sovereignty enforcement via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 5. CI Validation Requirements

GRD Items must pass:

- STAC 1.x validation  
- SAR extension validation  
- geometry ↔ bbox checks  
- required `"kfm:*"` governance fields  
- PROV-O lineage checks  
- DCAT alignment  
- correct asset media types  
- sovereignty masking rules  

If validation fails → **item is blocked from release**.

---

## 🔁 6. GRD in the Sentinel-1 ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → speckle filtering
 → GRD σ⁰ generation
 → sovereignty generalization (conditional)
 → QA application
 → STAC Item generation (this directory)
 → Collection update
 → governed release
~~~

---

## 🔮 7. Applications Inside KFM

- hydrology models  
- flood pre/post comparisons  
- agricultural monitoring (tillage, canopy, harvest)  
- land-cover & land-use change  
- hazard detection (wind, disturbance)  
- Story Node v3 environmental context  
- Focus Mode v3 SAR evidence panels  
- upstream to RTC, coherence, flood, wetlands, deformation  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                       |
|--------:|------------|----------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 GRD Items README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-validated; emoji-rich.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 GRD Collections](../collections/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

