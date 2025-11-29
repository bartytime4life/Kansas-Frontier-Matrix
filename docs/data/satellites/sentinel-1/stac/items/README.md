---
title: "📦 ESA Sentinel-1 — STAC Items (Scene-Level SAR Products · GRD · GRDH · RTC · Coherence · Deformation · Flood)"
path: "docs/data/satellites/sentinel-1/stac/items/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Earth Observation (CC-BY 4.0)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"

review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

json_schema_ref: "../../../../../../schemas/json/sentinel1-stac-items-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-stac-items-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-items-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-items"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/items/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded upon next ESA reprocessing cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **Sentinel-1 STAC Items**  
`docs/data/satellites/sentinel-1/stac/items/`

**Scene-level STAC Items** for all Sentinel-1 SAR product families integrated into  
KFM v11: GRD · GRDH · RTC · Coherence · Deformation (InSAR) · Flood · Wetlands.

</div>

---

## 📘 1. Purpose

This directory contains **all scene-level STAC Items** representing individual  
Sentinel-1 SAR acquisitions and derived SAR layers.  
Each Item includes:

- footprint geometry  
- temporal metadata  
- sensor + mode + polarization properties  
- links to COG assets (VV/VH, RTC, coherence, flood, deformation)  
- JSON-LD + PROV-O lineage  
- FAIR+CARE governance metadata  
- sovereignty masking / generalization flags  
- CI-validated STAC 1.x definitions  

These Items feed directly into:

- hydrology mapping  
- flood modeling  
- ecological change analysis  
- cultural-landscape risk overlays  
- Story Node v3 context  
- Focus Mode v3 environmental reasoning  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/sentinel-1/stac/items/
├── 📄 README.md                         # This file
│
├── 🛰️ grd/                              # GRD Items (σ⁰ backscatter, VV/VH)
│   ├── <scene>.json
│   └── …
│
├── 🛰️ grdh/                             # High-resolution GRDH Items
│   ├── <scene>.json
│   └── …
│
├── 🛰️ rtc/                              # Radiometrically Terrain Corrected Items
│   ├── <scene>.json
│   └── …
│
├── 🔗 coherence/                        # Coherence Item scenes
│   ├── <coh-tile>.json
│   └── …
│
├── 🌍 deformation/                      # InSAR LOS deformation Items (H3-generalized)
│   ├── <los-tile>.json
│   └── …
│
├── 🌊 flood/                            # SAR flood-mapping Items
│   ├── <flood-tile>.json
│   └── …
│
└── 🌿 wetlands/                         # SAR-derived wetland & inundation Items
    ├── <wetland-tile>.json
    └── …
~~~

---

## 🧩 3. Item Responsibilities by Product Family

### 🛰️ GRD / GRDH Items
- σ⁰ VV, VH calibrated backscatter  
- used for hydrology, land change, agricultural monitoring  
- multi-temporal stacks in KFM analysis pipelines  

### 🛰️ RTC Items
- DEM-corrected γ⁰  
- stable illumination conditions for time-series use  
- essential for flood + wetland detection  

### 🔗 Coherence Items
- temporal coherence  
- flood damage detection  
- disturbance mapping  

### 🌍 Deformation (InSAR) Items
- LOS displacement  
- seasonal deformation signals  
- **sovereignty-generalized inside tribal H3 cells**  
- `"kfm:mask_required"` & `"kfm:sovereignty_uncertainty_floor"` applied  

### 🌊 Flood Items
- VH/VV threshold maps  
- regression / Otsu masks  
- hydrology Story Node integrations  

### 🌿 Wetlands Items
- inundation/wetland SAR signatures  
- synthetic/low-risk H3-generalization near sensitive areas  

---

## 🔐 4. FAIR+CARE & Sovereignty Controls

Scene-level SAR scans often intersect:

- tribal lands  
- culturally sensitive landscapes  
- ecologically vulnerable zones  

KFM enforces:

- `"kfm:h3_sensitive"` tags  
- `"kfm:mask_required"` on deformation/flood Items  
- geometric generalization rules  
- `"kfm:care_label"` and `"kfm:care_label_reason"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- PROV-O lineage for each Item  

Governance validated by:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`

---

## 🧪 5. CI Validation Behavior

Each Item is validated for:

- STAC 1.x schema compliance  
- SAR extension compliance (`sar:*`, `s1:*`)  
- correct geometry (GeoJSON + bbox)  
- link graph correctness  
- sovereign masking rules  
- required `"kfm:*"` governance fields  
- correct asset media types  
- DCAT alignment  
- PROV-O lineage compatibility  

Failures → **Item blocked from release** in KFM.

---

## 🔁 6. STAC Item Lifecycle in ETL

~~~text
ESA ingest
 → orbit correction
 → calibration
 → speckle filtering
 → RTC (optional)
 → coherence / deformation / flood extraction
 → sovereignty masking
 → STAC Item generation (this directory)
 → STAC Collection update
 → governed release
~~~

---

## 🔮 7. Applications Inside KFM

- hydrology & flood intelligence  
- ecological monitoring  
- deformation hazard analysis  
- land-use & land-change mapping  
- cultural-landscape risk overlays  
- Focus Mode v3 reasoning  
- Story Node v3 environmental narrative context  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                    |
|--------:|------------|------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 STAC Items README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; emoji-rich; CI-safe.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Collections](../collections/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

