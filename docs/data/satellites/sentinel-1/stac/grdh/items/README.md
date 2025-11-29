---
title: "🛰️ Sentinel-1 GRDH — Scene-Level STAC Items (High-Resolution σ⁰ Backscatter · Fine-Scale Hydrology & Land Dynamics)"
path: "docs/data/satellites/sentinel-1/stac/grdh/items/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (High-Resolution SAR)"
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

fair_category: "F3-A1-I2-R4"
care_label: "CARE-B (High-Resolution SAR)"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
public_exposure_risk: "Medium"
risk_category: "High"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-grdh-items-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-grdh-items-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-grdh-items-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-grdh-items"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/grdh/items/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next ESA GRDH reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **Sentinel-1 GRDH — Scene-Level STAC Items**  
`docs/data/satellites/sentinel-1/stac/grdh/items/`

Fine-resolution σ⁰ VV/VH backscatter scenes for  
**flood-edge detection**, **agricultural structure**, **land-change**, **disturbance mapping**, and  
**high-detail hydrology**, governed under CARE-B + sovereignty constraints.

</div>

---

## 📘 1. Overview

Sentinel-1 **GRDH (Ground Range Detected · High Resolution)** Items provide  
enhanced spatial fidelity relative to standard GRD scenes.

Each GRDH Item includes:

- σ⁰ **VV** and **VH** calibrated backscatter (high-resolution grid)  
- full footprint polygon  
- ESA SAFE ancillary metadata  
- RTC-ready backscatter metadata  
- QA layers (calibration, border noise, radiometric anomalies)  
- JSON-LD + DCAT metadata  
- PROV-O lineage for reproducibility  
- `"kfm:*"` governance & sovereignty requirements  

These Items are used in advanced KFM analytics:

- precise flood-edge delineation  
- riparian zone mapping  
- land-cover state changes  
- agricultural field-structure dynamics  
- micro-disturbance (wind/tornado) detection  
- Story Node v3 environmental narratives  
- Focus Mode v3 high-resolution evidence  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/grdh/items/
├── 📄 README.md
│
├── 🛰️ S1A_IW_GRDH_20250311T112845.json
├── 🛰️ S1B_IW_GRDH_20250419T223015.json
└── …                 # Many sovereign-generalized GRDH scenes
~~~

---

## 🧩 3. GRDH STAC Item Structure

### 🌐 Core STAC Properties
- `id`, `"type": "Feature"`  
- `datetime`  
- `"sar:product_type" = "GRDH"`  
- `"sar:instrument_mode" = "IW"`  
- `"sar:polarizations" = ["VV","VH"]`  
- `"sar:frequency_band" = "C"`  
- `proj:*` CRS & raster grid metadata  
- orbit metadata (`relative_orbit`, `cycle_number`, `orbit_state`)  

---

### 🗺 Geometry (Sovereignty-Aware)
- full-resolution footprint polygon  
- `bbox`  
- **H3 generalization** inside sovereign or ecologically sensitive cells  
- `"kfm:mask_required"` may be **true** for GRDH due to high detail  

---

### 📦 Assets
- `"sigma0_vv"` — VV COG  
- `"sigma0_vh"` — VH COG  
- `"thumbnail"` — PNG preview  
- `"qa"` — QA mask (border noise, calibration quality, radiometric anomalies)  
- `"metadata"` — SAFE metadata  

Optional assets:
- `"incidence_angle"`  
- `"orbit"` metadata  
- `"layout_preview"`  

---

### 🔗 Link Graph
- `"self"`  
- `"collection"` → GRDH collection  
- `"parent"`  
- `"root"`  
- `"derived_from"` → ESA SAFE scene  

---

### 🧬 PROV-O Lineage
- `prov:wasGeneratedBy` → GRDH processing pipeline  
- `prov:used` → orbit files, auxiliary calibration LUTs, SAFE metadata  
- `prov:wasDerivedFrom` → ESA source product  
- sustainability metrics (`kfm:energy_wh`, `kfm:carbon_gco2e`)  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Due to high spatial detail, GRDH Items can reveal:

- agricultural boundaries  
- hydrological micro-patterns  
- cultural landscape signals  
- disturbance footprints  
- infrastructure shifts  

Thus **mandatory** governance fields include:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Generalization rules may include:

- H3-based geometry coarsening  
- COG-level downsampling for sovereign zones  
- uncertainty flooring for sensitive signal inference  

---

## 🧪 5. CI Validation Requirements

All GRDH Items must pass:

- ✔ STAC 1.x validation  
- ✔ SAR extension validation  
- ✔ geometry ↔ bbox consistency  
- ✔ DCAT conformity  
- ✔ JSON-LD context resolution  
- ✔ `"kfm:*"` governance metadata checks  
- ✔ sovereignty generalization enforcement  
- ✔ PROV-O lineage correctness  
- ✔ asset mediatype/role verification  

Any failure → **item blocked from release**.

---

## 🔁 6. GRDH in Sentinel-1 ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → GRDH σ⁰ generation (high-resolution)
 → speckle filtering
 → sovereignty masking (mandatory)
 → GRDH QA generation
 → STAC Item creation
 → GRDH Collection update
 → governed release
~~~

---

## 🔮 7. Applications Across KFM

- high-detail flood mapping  
- precision hydrology layers  
- agricultural structure & field-scale transitions  
- vegetation & canopy disturbance  
- cultural landscape safety analysis  
- Story Node v3 fine-scale environmental context  
- Focus Mode v3 high-resolution reasoning  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                      |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial GRDH Items README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe; emoji-rich.             |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🗂 GRDH Collections](../collections/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

