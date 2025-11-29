---
title: "🛰️ Sentinel-1 RTC — Radiometrically Terrain Corrected STAC Items (γ⁰ Backscatter · Terrain-Normalized)"
path: "docs/data/satellites/sentinel-1/stac/items/rtc/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Earth Observation (CC-BY 4.0)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"

license: "CC-BY 4.0 (ESA Open Data)"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
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
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-rtc-items-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-rtc-items-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-items-rtc:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-items-rtc"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/items/rtc/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded on next ESA RTC reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **Sentinel-1 RTC — Radiometrically Terrain-Corrected STAC Items**  
`docs/data/satellites/sentinel-1/stac/items/rtc/`

**γ⁰ terrain-normalized SAR backscatter**  
Essential for hydrology, flood mapping, ecosystem change, soil moisture proxies, and  
multi-temporal trend analysis.

</div>

---

## 📘 1. Overview

Sentinel-1 **RTC (Radiometrically Terrain Corrected)** Items provide **γ⁰ backscatter**  
corrected for terrain-induced illumination effects to produce stable, comparable  
values across time.

RTC Items are used in KFM for:

- 🌊 flood monitoring (VH/VV ratio + normalized backscatter)  
- 🌿 wetland / riparian zone detection  
- 🌾 agriculture & land-change mapping  
- 🏔 topographic normalization for mountainous regions  
- 🧭 Focus Mode v3 SAR-based environmental reasoning  
- 📖 Story Node v3 context (governance-bounded)  

All RTC Items:

- are STAC 1.x valid  
- include JSON-LD + PROV-O lineage  
- incorporate sovereignty/H3 masking and CARE metadata  
- undergo CI schema, geometry, and governance validation  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/items/rtc/
├── 📄 README.md                                # This file
│
├── 🛰️ S1A_IW_RTC_20250101T115932.json          # Example RTC Item (synthetic placeholder)
├── 🛰️ S1B_IW_RTC_20250314T004012.json          # Additional scene-level Items
└── …                                            # More RTC scene entries
~~~

---

## 🧩 3. RTC Item Component Structure

### 🌐 Core STAC Properties
- `datetime`  
- `sar:product_type = "RTC"`  
- `sar:instrument_mode = "IW"` (typically)  
- `sar:polarizations` (VV/VH)  
- `sar:frequency_band = "C"`  
- `proj:*` (EPSG, transform, shape)  
- orbit metadata: `orbit_state`, `relative_orbit`, `cycle_number`  

### 🗺️ Geometry
- Full footprint polygon  
- Sovereignty-generalized bbox when required  
- `geometry` + `bbox` must match within tolerance  

### 📦 Assets
- `"gamma0_vv"` — γ⁰ VV COG  
- `"gamma0_vh"` — γ⁰ VH COG  
- `"thumbnail"` — PNG preview  
- `"qa"` — RTC QA masks (radiometric quality, terrain artifacts)  
- `"metadata"` — ancillary ESA SAFE metadata  

### 🔗 Link Graph
- `"self"`  
- `"parent"` → `collection_rtc.json`  
- `"collection"`  
- `"root"`  
- `"derived_from"` → original GRD/GRDH Item (PROV)  

### 🧬 Lineage (PROV-O)
- `prov:wasGeneratedBy` → RTC transform pipeline  
- `prov:used` → DEM tiles, orbit files, calibration LUTs  
- `prov:wasDerivedFrom` → ESA GRD/GRDH base scene  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

RTC Items often intersect:

- sovereign ecological transitions  
- archaeological landscapes  
- culturally sensitive regions  
- hydrologically-important Indigenous territories  

KFM enforces:

- `"kfm:h3_sensitive"` tagging  
- `"kfm:mask_required"` if γ⁰ reveals sensitive detail  
- sovereignty-aware geometry generalization  
- `"kfm:care_label"` + `"kfm:care_label_reason"`  
- `"kfm:sovereignty_uncertainty_floor"` for derivative products  
- `"kfm:governance_notes"` describing masking decisions  

Governance validation applied under:

- `stac_validate.yml`  
- `faircare_validate.yml`  
- `jsonld_validate.yml`

---

## 🧪 5. CI Validation Requirements

RTC Items must pass:

- STAC 1.x schema validation  
- SAR extension checks (`sar:*`, `s1:*`)  
- geometry ↔ bbox consistency  
- proper asset media types (COG, PNG, JSON)  
- required `"kfm:*"` governance metadata  
- sovereign generalization rules  
- DCAT metadata compatibility  
- PROV-O lineage completeness  

Violations → **Item blocked from governed release**.

---

## 🔁 6. RTC in the SAR ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → terrain correction (RTC)
 → speckle filtering (optional RTC-level)
 → sovereignty masking
 → RTC STAC Item generation
 → Collection update
 → governed release bundle
~~~

---

## 🔮 7. Applications Inside KFM

- hydrology (flood, wetlands, soil moisture proxies)  
- agriculture & land-surface modeling  
- freeze–thaw contextual maps  
- terrain-normalized land-change analysis  
- Story Node v3 environmental panels  
- Focus Mode v3 SAR-based evidence  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                     |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 RTC STAC Items README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; emoji-rich; CI-safe.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Collections](../../collections/README.md) · [🛰 Sentinel-1 Root](../../../../../sentinel-1/README.md)

</div>

