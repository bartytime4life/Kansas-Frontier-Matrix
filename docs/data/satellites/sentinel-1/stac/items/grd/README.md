---
title: "🛰️ Sentinel-1 GRD — STAC Items (σ⁰ Backscatter · VV/VH · Hydrology · Land Change)"
path: "docs/data/satellites/sentinel-1/stac/items/grd/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Earth Observation (CC-BY 4.0)"
status: "Active / Enforced"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"

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

json_schema_ref: "../../../../../../../schemas/json/sentinel1-grd-items-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-grd-items-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-items-grd:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-items-grd"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/items/grd/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when ESA releases a GRD reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **Sentinel-1 GRD — Scene-Level STAC Items**  
`docs/data/satellites/sentinel-1/stac/items/grd/`

**Ground Range Detected (GRD) σ⁰ backscatter**  
VV/VH · All-weather · All-season  
Hydrology · Flood mapping · Agriculture · Land-change · Hazard analysis

</div>

---

## 📘 1. Overview

The **GRD STAC Items** describe individual Sentinel-1 **Ground Range Detected** scenes stored as  
governed, sovereignty-aware, reproducible **STAC 1.x Items**.

Each scene contains:

- calibrated σ⁰ backscatter (VV, VH)  
- precise acquisition timestamp  
- sensor mode (IW/SM/EW)  
- orbit direction & relative orbit number  
- valid STAC assets (COG backscatter, thumbnails, QA masks)  
- bounding geometry & bbox  
- JSON-LD metadata (semantic + ontology aligned)  
- DCAT properties  
- PROV-O lineage  
- FAIR+CARE sovereignty metadata (H3-aware)  
- complete CI validation  

These Items are consumed by KFM pipelines for:

- flood detection  
- land-change mapping  
- agricultural analytics  
- hydrology context  
- Focus Mode v3  
- Story Node v3 spatial evidence  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/sentinel-1/stac/items/grd/
├── 📄 README.md                          # This file
│
├── 🛰️ S1A_IW_GRDH_20250101T115932.json  # Example GRD Item (synthetic placeholder)
├── 🛰️ S1B_IW_GRD_20250312T223015.json   # Additional GRD Item(s)
└── …                                     # Many more scene Items
~~~

(The filenames above are EXAMPLES; KFM uses real scene IDs from ESA SciHub / ASF COG mirrors.)

---

## 🧩 3. GRD STAC Item Contents

Every GRD Item includes:

### 🌐 Core Properties
- `datetime`  
- `sar:instrument_mode` (IW/SM/EW)  
- `sar:polarizations` (["VV","VH"])  
- `sar:frequency_band = "C"`  
- `sar:product_type = "GRD"`  
- `proj:*` metadata  
- `orbit_state`, `relative_orbit`, `cycle_number`  

### 🗺️ Geometry
- GeoJSON polygon footprint  
- `bbox` with sovereign-safe generalization (if required)  

### 📦 Assets
- `"sigma0_vv"` → COG (VV)  
- `"sigma0_vh"` → COG (VH)  
- `"thumbnail"` → PNG preview  
- `"qa"` → QA masks (speckle, border-noise, calibration anomalies)  

### 🔐 Governance Fields
- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"` (if sovereignty rules trigger)  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  

### 🔗 Link Graph
- `"root"`, `"parent"`, `"collection"`, `"self"`  
- intra-collection link integrity enforced by CI  

### 🧬 Lineage (PROV-O)
- `prov:wasGeneratedBy` (KFM SAR transform pipeline)  
- `prov:used` (orbit files, calibration LUTs, DEM tiles)  
- `prov:wasDerivedFrom` (ESA scene references)  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

GRD Items may include SAR signals that correlate with:

- tribal lands & ecological boundaries  
- culturally sensitive landscapes  
- infrastructure patterns  

Therefore Items must:

- propagate `"kfm:h3_sensitive"`  
- generalize geometry in sovereign H3 cells  
- add `"kfm:mask_required"` for backscatter-derived sensitive areas  
- apply `"kfm:sovereignty_uncertainty_floor"` when needed  
- attach `"kfm:care_label_reason"` and `"kfm:governance_notes"`  
- maintain full PROV-O lineage  

Governance is validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 5. CI Validation Requirements

CI enforces:

- STAC 1.x schema validity  
- required `sar:*`, `proj:*`, `s1:*` fields  
- asset media types (COG/PNG/JSON)  
- semantic link correctness  
- bounding geometry validity  
- sovereignty metadata rules  
- PROV-O lineage presence  
- DCAT compatibility  

Failing Items are **blocked** from release.

---

## 🔁 6. GRD in the SAR ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → speckle filtering
 → (optional) terrain correction preview layers
 → sovereignty masking
 → GRD STAC Item generation
 → Collection update
 → governed release bundle
~~~

---

## 🔮 7. Applications Across KFM

- flood mapping  
- hydrology context  
- agricultural monitoring  
- land-change detection  
- hazard & disturbance analysis  
- Focus Mode v3 environmental evidence  
- Story Node v3 spatial context  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                               |
|--------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial GRD STAC Items README; FAIR+CARE/H3 aligned; CI-safe; STAC/DCAT/PROV integrated; emoji-rich. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Collections](../../collections/README.md) · [🌐 Sentinel-1 Root](../../../../sentinel-1/README.md)

</div>

