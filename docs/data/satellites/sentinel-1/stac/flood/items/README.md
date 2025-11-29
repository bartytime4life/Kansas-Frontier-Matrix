---
title: "🌊 Sentinel-1 Flood — Scene-Level STAC Items (Binary · Multi-Class · Probability · Coherence-Assisted)"
path: "docs/data/satellites/sentinel-1/stac/flood/items/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (Governed SAR Derivative)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

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

fair_category: "F3-A1-I2-R5"
care_label: "CARE-B (Flood Mapping Output)"
indigenous_rights_flag: true
sensitivity_level: "High"
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

json_schema_ref: "../../../../../../../schemas/json/sentinel1-flood-items-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-flood-items-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-flood-items-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-flood-items"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/flood/items/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon next ESA flood reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌊 **Sentinel-1 Flood STAC Items**  
`docs/data/satellites/sentinel-1/stac/flood/items/`

Scene-level, sovereignty-generalized STAC Items representing  
**binary flood extent**, **multi-class flood severity**, **probability surfaces**,  
and **coherence-enhanced flood detection** from Sentinel-1 SAR.

</div>

---

## 📘 1. Overview

Flood STAC Items encode hydrologic conditions derived from Sentinel-1 SAR:

- 🌊 water / no-water (binary map)  
- 🌀 shallow / deep / mixed flooding (multi-class)  
- 📊 flood probability surfaces  
- 🔗 coherence-assisted flood detection (coherence loss + VH/VV ratio)  
- 🌱 flood–wetland interaction zones  
- 🗺 boundary uncertainty + masking in sovereign areas  

They are **governance-sensitive**, requiring:

- CARE-B classification  
- sovereignty generalization  
- uncertainty floors  
- full FAIR+CARE metadata propagation  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/flood/items/
├── 📄 README.md
│
├── 🌊 S1A_IW_FLD_20250411T120010.json       # Example flood Item
├── 🌊 S1B_IW_FLD_20250318T223045.json       # Additional flood Items
└── …                                         # More sovereign-generalized flood Items
~~~

---

## 🧩 3. Flood Item Structure (STAC Core)

### 🌐 Core Properties  
- `datetime`  
- `"sar:product_type" = "FLOOD"`  
- `"sar:instrument_mode" = "IW"`  
- `"sar:frequency_band" = "C"`  
- `"sar:polarizations" = ["VV","VH"]`  
- `proj:*` CRS, transform, shape  
- orbit metadata (cycle, relative orbit, orbit_state)

### 🗺 Geometry (Generalized)  
- polygon footprint  
- bbox  
- sovereignty-generalized polygon inside H3 tribal cells  
- `"kfm:mask_required"` frequently true  

### 📦 Assets  
- `"flood_mask"` — binary COG  
- `"flood_multiclass"` — optional  
- `"flood_prob"` — probability COG  
- `"coherence"` — optional for hybrid classifier  
- `"qa"` — flooded vs uncertain vs ambiguous  
- `"thumbnail"` — PNG  
- `"metadata"` — ESA SAFE metadata  

### 🔗 Link Structure  
- `"self"`  
- `"collection"` (from flood collection)  
- `"parent"`  
- `"root"`  
- `"derived_from"` → RTC/GRD/GRDH/Coherence  

### 🧬 PROV-O Lineage  
- `prov:wasGeneratedBy` → flood classifier pipeline  
- `prov:used` → RTC, coherence tiles, DEM, LUTs  
- `prov:wasDerivedFrom` → ESA GRD/GRDH source imagery  
- energy/carbon estimates included in `"kfm:*"` fields  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Flood datasets intersect:

- tribal waterways  
- culturally protected areas  
- ecologically sensitive zones  
- sovereignty-defined hydroscapes  

Therefore Items MUST include:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:care_label_reason"`  
- `"kfm:data_steward"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  

Sovereignty masking & generalization validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  

---

## 🧪 5. CI Validation Requirements

Flood Items must pass:

- STAC 1.x schema validation  
- SAR + flood product extension checks  
- geometry ↔ bbox consistency  
- required governance fields  
- sovereign H3 masking rules  
- asset media type/role validation  
- PROV-O lineage completeness  
- DCAT metadata compatibility  

Failure → **Item blocked from governed release**.

---

## 🔁 6. Flood Mapping in the SAR ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → terrain correction (RTC)
 → VH/VV ratio + coherence integration
 → binary/multi-class/probability flood classification
 → sovereignty masking (mandatory)
 → flood QA application
 → STAC Item generation (this directory)
 → flood Collection update
 → governed release bundle
~~~

---

## 🔮 7. Applications Across KFM

- flood risk and severity modeling  
- watershed hydrology analytics  
- wetlands–flood interaction modeling  
- disaster-response overlays  
- cultural-landscape safety mapping  
- Story Node v3 flood narratives  
- Focus Mode v3 sovereign-safe hydrology reasoning  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                   |
|--------:|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 Flood STAC Items README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe.     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Flood Collections](../collections/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

