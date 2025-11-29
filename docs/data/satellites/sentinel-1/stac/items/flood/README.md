---
title: "🌊 Sentinel-1 Flood Mapping — STAC Items (SAR Water Detection · VH/VV Ratio · Otsu/Hybrid Classifiers)"
path: "docs/data/satellites/sentinel-1/stac/items/flood/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (Governed SAR Derivative)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"

license: "CC-BY 4.0 (ESA)"
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

fair_category: "F3-A1-I2-R5"
care_label: "CARE-B (Floodwater Mapping)"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
public_exposure_risk: "Medium"
risk_category: "Medium–High"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-flood-items-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-flood-items-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-items-flood:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-items-flood"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/items/flood/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "36 months"
sunset_policy: "Superseded upon next ESA flood-mapping reprocessing cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌊 **Sentinel-1 Flood Mapping — Scene-Level STAC Items**  
`docs/data/satellites/sentinel-1/stac/items/flood/`

**SAR floodwater detection** using:  
VH/VV ratio · Otsu thresholding · hybrid classifiers · change detection · coherence loss signatures.

</div>

---

## 📘 1. Overview

Flood detection from Sentinel-1 SAR is central to KFM due to:

- all-weather capability  
- day/night imaging  
- sensitivity to inundation over vegetated and bare surfaces  
- rapid temporal refresh for flash and riverine flood events  

Flood STAC Items here represent:

- binary flood masks (water / no-water)  
- multi-class flood masks (deep / shallow / mixed)  
- probability surfaces (optional)  
- confidence maps  
- QA layers  
- governance metadata (CARE/H3 sovereignty controls)  

All Items are:

- STAC 1.x valid  
- DCAT 3.0 compatible  
- JSON-LD enriched  
- PROV-O lineage-complete  
- sovereignty-generalized  
- CI-validated  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/items/flood/
├── 📄 README.md
│
├── 🌊 S1A_IW_FLD_20250411T120010.json       # Example flood Item
├── 🌊 S1B_IW_FLD_20250318T223045.json       # Additional flood Items
└── …                                         # Many more flood scenes
~~~

---

## 🧩 3. Flood Item Components

### 🌐 Core STAC Fields
- `datetime`  
- `"sar:product_type" = "FLOOD"`  
- `sar:instrument_mode` (IW)  
- `sar:polarizations` (VV/VH)  
- `sar:frequency_band = "C"`  
- `proj:*` metadata  
- orbit info (`cycle_number`, `orbit_state`, `relative_orbit`)  

### 🗺️ Geometry (Generalized for Sovereignty)
- polygon footprint  
- bbox reflecting generalized boundaries  
- strict H3 boundary generalization where required  

### 📦 Assets
- `"flood_mask"` → COG (water / no water)  
- `"flood_prob"` → optional  
- `"confidence"` → flood-confidence COG  
- `"thumbnail"` → PNG flood preview  
- `"qa"` → QA mask (speckle, threshold ambiguity, vegetation interactions)  
- `"metadata"` → ancillary ESA metadata  

### 🔗 Link Structure
- `"self"`  
- `"collection"` → flood collection  
- `"parent"`  
- `"root"`  
- `"derived_from"` → RTC or GRD/GRDH sources  

### 🧬 PROV-O Lineage
- `prov:wasGeneratedBy` → flood mapping pipeline  
- `prov:used` → RTC/GRD Inputs, DEM, coherence tiles (for hybrid flood classifiers)  
- `prov:wasDerivedFrom` → ESA scenes  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Flood layers can intersect sensitive:

- tribal waterways  
- cultural heritage zones  
- ecologically vulnerable regions  
- treaty-defined areas  
- sovereign tribal jurisdictions  

KFM enforces:

- `"kfm:h3_sensitive"` propagation  
- `"kfm:mask_required"` whenever flood boundaries intersect sovereign H3 cells  
- `"kfm:care_label"` = CARE-B  
- `"kfm:care_label_reason"`  
- `"kfm:sovereignty_uncertainty_floor"` applied to probability layers  
- `"kfm:governance_notes"` describing all masking/generalization operations  

Validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 5. CI Validation Requirements

CI checks:

- STAC 1.x schema compliance  
- SAR/Flood extension correctness  
- bbox ↔ geometry consistency  
- asset media types & roles  
- required `"kfm:*"` governance metadata  
- sovereignty-generalization compliance  
- PROV-O lineage shape  
- DCAT metadata compatibility  

Any violation → **Item hard-blocked**.

---

## 🔁 6. Flood Mapping in the SAR ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → terrain correction (RTC)
 → speckle filtering
 → VH/VV ratio + change detection + coherence loss
 → flood classification (binary / multi-class / probability)
 → sovereignty masking (mandatory)
 → flood QA
 → STAC Item generation (this directory)
 → Collection update
 → governed release bundle
~~~

---

## 🔮 7. Applications Inside KFM

- hydrology modeling  
- flood forecasting validation  
- hazard analysis  
- ecological/wetland interaction studies  
- Story Node v3 flood narratives  
- Focus Mode v3 environmental evidence layers  
- cultural-landscape risk monitoring  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                          |
|--------:|------------|------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 Flood STAC Items README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe; emoji-rich.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Collections](../../collections/README.md) · [🌐 Sentinel-1 Root](../../../../../sentinel-1/README.md)

</div>

