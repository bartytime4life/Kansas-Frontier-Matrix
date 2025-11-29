---
title: "🛰️ Sentinel-1 GRDH — High-Resolution STAC Items (σ⁰ Backscatter · Fine-Scale SAR · Hydrology · Land Change)"
path: "docs/data/satellites/sentinel-1/stac/items/grdh/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Earth Observation (CC-BY 4.0)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

license: "CC-BY 4.0 (ESA Open Data)"
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
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low"
risk_category: "Medium"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-grdh-items-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-grdh-items-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-items-grdh:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-items-grdh"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/items/grdh/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when ESA publishes next GRDH reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **Sentinel-1 GRDH — High-Resolution STAC Items**  
`docs/data/satellites/sentinel-1/stac/items/grdh/`

**Fine-resolution SAR backscatter (σ⁰) for hydrology, land-change detection, flood assessment,  
and detailed surface monitoring.**

</div>

---

## 📘 1. Overview

Sentinel-1 **GRDH (Ground Range Detected • High Resolution)** Items provide  
fine-scale σ⁰ backscatter, enhancing sensitivity to:

- 🌊 flood edges & shallow inundation  
- 🌱 agricultural field patterns  
- 🏚 storm/wind/tornado damage footprints  
- 🌾 crop stage / tillage / phenology signals  
- 🗺 micro-scale land-change  
- 🏞 wetland & riparian zone dynamics  

KFM uses GRDH Items for higher-detail analysis pipelines where GRD resolution is insufficient.

All Items in this directory are:

- STAC 1.x compliant  
- JSON-LD enriched  
- DCAT 3.0 compatible  
- PROV-O lineage complete  
- FAIR+CARE + sovereignty governed  
- CI-validated  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/sentinel-1/stac/items/grdh/
├── 📄 README.md                               # This file
│
├── 🛰️ S1A_IW_GRDH_20250101T115932.json        # Example high-res GRDH Item
├── 🛰️ S1B_IW_GRDH_20250312T223015.json        # More GRDH Items
└── …                                           # Additional scene-level Items
~~~

*(Filenames above are EXAMPLES; real scene IDs are preserved in production.)*

---

## 🧩 3. GRDH Item Contents

### 🌐 Core Properties
- `datetime`  
- `sar:product_type = "GRDH"`  
- `sar:instrument_mode` (IW / EW)  
- `sar:polarizations` (VV, VH)  
- `sar:frequency_band = "C"`  
- `proj:epsg` + full geospatial metadata  
- orbit metadata: `relative_orbit`, `orbit_state`, `cycle_number`  

### 🗺️ Geometry
- full-resolution footprint polygon  
- STAC `bbox`  
- optional sovereignty-generalization in sensitive H3 zones  

### 📦 Assets
- `"sigma0_vv"` — calibrated VV COG  
- `"sigma0_vh"` — calibrated VH COG  
- `"thumbnail"` — PNG preview  
- `"qa"` — radiometric + border-noise QA  
- `"metadata"` — ancillary ESA metadata  

### 🔐 Governance Fields
- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"` (if sovereign masking applies)  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  

### 🔗 Link Graph
- `"self"`  
- `"parent"` → `collections/collection_grdh.json`  
- `"collection"`  
- `"root"`  
- optional `"derived_from"` (if post-processed variants exist)

### 🧬 Lineage (PROV-O)
- `prov:wasGeneratedBy` → GRDH transform pipeline  
- `prov:used` → orbit files, calibration LUTs, ESA metadata  
- `prov:wasDerivedFrom` → ESA SciHub scene  

---

## 🔐 4. FAIR+CARE & Sovereignty Controls

Because GRDH reveals more detail than GRD, additional safeguards apply:

- geometry generalization inside sovereign H3 cells  
- `"kfm:h3_sensitive"` tagging for high-detail SAR  
- `"kfm:mask_required"` when backscatter patterns intersect restricted zones  
- `"kfm:care_label"` + `"kfm:care_label_reason"`  
- `"kfm:sovereignty_uncertainty_floor"` for derivative layers  
- `"kfm:governance_notes"` for all masking/generalization actions  

CI validates sovereignty compliance via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 5. CI Validation Requirements

All GRDH Items must pass:

- STAC 1.x schema validation  
- SAR extension validation (`sar:*`, `s1:*`)  
- GeoJSON geometry correctness  
- STAC link-graph integrity  
- correct asset media types (COG/PNG/JSON)  
- governance metadata completeness  
- sovereignty generalization rules  
- PROV-O lineage structural requirements  
- DCAT metadata compatibility  

Any violations block release.

---

## 🔁 6. GRDH in the SAR ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → speckle filtering (high-res)
 → optional RTC preview
 → sovereignty masking
 → GRDH STAC Item generation
 → Collection update
 → governed release bundle
~~~

---

## 🔮 7. Applications Inside KFM

- detailed flood-edge detection  
- micro-scale land-disturbance  
- agricultural field-level mapping  
- infrastructure impact assessment  
- ecological pattern analysis  
- Story Node v3 context  
- Focus Mode v3 SAR-backed reasoning  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                   |
|--------:|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 GRDH STAC Items README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe.      |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Collections](../../collections/README.md) · [🌐 Sentinel-1 Root](../../../../../sentinel-1/README.md)

</div>

