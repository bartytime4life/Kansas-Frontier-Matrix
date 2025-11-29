---
title: "🔗 Sentinel-1 Coherence — Scene-Level STAC Items (Temporal SAR Coherence · Disturbance · Flood Damage)"
path: "docs/data/satellites/sentinel-1/stac/coherence/items/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (Governed SAR Disturbance Product)"
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

fair_category: "F3-A1-I2-R4"
care_label: "CARE-B (Disturbance-Sensitive SAR Product)"
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

json_schema_ref: "../../../../../../../schemas/json/sentinel1-coherence-items-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-coherence-items-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-coherence-items-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-coherence-items"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/coherence/items/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon next ESA coherence reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🔗 **Sentinel-1 Temporal Coherence STAC Items**  
`docs/data/satellites/sentinel-1/stac/coherence/items/`

Scene-pair coherence tiles representing  
**disturbance**, **flood damage**, **agricultural change**, and **land-cover transitions**,  
governed under strict CARE-B and sovereignty-generalization rules.

</div>

---

## 📘 1. Overview

Sentinel-1 **coherence STAC Items** describe the temporal similarity between  
two SAR acquisitions (master + slave), enabling detection of:

- 🌪️ storm/tornado damage  
- 🌊 flood-induced coherence loss  
- 🚜 agricultural disturbance / harvest cycles  
- 🌿 vegetation transitions  
- 🏗️ infrastructure disturbance (generalized)  
- 🗺️ land-cover & land-use change  

These layers are **disturbance-sensitive**, making them subject to:

- sovereignty masking  
- H3 generalization  
- CARE-B classification  
- uncertainty flooring  
- complete provenance capture  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/coherence/items/
├── 📄 README.md
│
├── 🔗 S1A_IW_COH_20250101_20250113.json
├── 🔗 S1B_IW_COH_20250314_20250326.json
└── …                                # Additional scene-pair coherence Items
~~~

---

## 🧩 3. Coherence Item Structure

### 🌐 Core STAC Properties
- `datetime` = mid-time of pair  
- `"sar:product_type" = "COHERENCE"`  
- `"sar:instrument_mode" = "IW"`  
- `"insar:pair" = ["2025-01-01T…", "2025-01-13T…"]`  
- `"sar:frequency_band" = "C"`  
- `"sar:polarizations" = ["VV","VH"]`  
- `proj:*` CRS, transform, shape  
- orbit metadata (cycle, relative orbit, orbit_state)

---

### 🗺 Geometry (Sovereignty-Generalized)
- footprint polygon (generalized where required)  
- bbox consistent with generalized geometry  
- `"kfm:mask_required"` triggered when tiles intersect  
  sovereign H3 cells or cultural landscapes  

---

### 📦 Assets
- `"coherence"` — main coherence COG  
- `"amplitude_master"` (optional)  
- `"amplitude_slave"` (optional)  
- `"thumbnail"` — PNG preview  
- `"qa"` — coherence quality flags  
- `"metadata"` — ancillary SAFE metadata  

---

### 🔗 Link Graph
- `"self"`  
- `"collection"` → coherence collection  
- `"parent"`  
- `"root"`  
- `"insar:master_scene"`  
- `"insar:slave_scene"`  

---

### 🧬 PROV-O Lineage
Every item includes:

- `prov:wasGeneratedBy` → coherence pipeline  
- `prov:used` → DEM, orbit files, calibration LUTs, master/slave imagery  
- `prov:wasDerivedFrom` → input GRD/GRDH/RTC scenes  
- `"kfm:energy_wh"` / `"kfm:carbon_gco2e"` sustainability metrics  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Coherence can reveal:

- disturbance from weather events  
- shifts in land-use  
- agricultural transformations  
- infrastructure damage  

Therefore each item **must** include:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Generalization is **always applied** over sovereign areas.

Governance is validated through:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  

---

## 🧪 5. CI Validation Requirements

Coherence Items must pass:

- full STAC 1.x validation  
- SAR & coherence extension checks  
- geometry consistency  
- correct asset mediatypes & roles  
- `"kfm:*"` governance field completeness  
- sovereignty masking enforcement  
- PROV-O lineage shape validation  
- DCAT compatibility  

Any failure → **item blocked**.

---

## 🔁 6. Coherence in the Sentinel-1 ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → speckle filtering
 → pair selection (master/slave)
 → coherence computation
 → sovereignty masking (mandatory)
 → QA application
 → STAC Item creation (this directory)
 → coherence Collection update
 → governed release bundle
~~~

---

## 🔮 7. Applications Across KFM

- flood damage detection  
- tornado/wind-damage mapping  
- agricultural disturbance  
- ecological change  
- cultural-landscape disturbance screening  
- Focus Mode v3 evidence layers  
- Story Node v3 environmental context  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                       |
|--------:|------------|---------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 coherence Items README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe; emoji-rich.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🗂 Coherence Collections](../collections/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

