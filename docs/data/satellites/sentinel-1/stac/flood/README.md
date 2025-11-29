---
title: "🌊 Sentinel-1 Flood Mapping — STAC Directory (Binary Flood · Multi-Class Flood · Probability Surfaces)"
path: "docs/data/satellites/sentinel-1/stac/flood/README.md"
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

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A1-I2-R5"
care_label: "CARE-B (Flood Inference)"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
public_exposure_risk: "Medium"
risk_category: "Medium–High"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/sentinel1-flood-collection-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-flood-collection-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-flood-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-flood"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/flood/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "36 months"
sunset_policy: "Superseded on next ESA flood-map reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌊 **Sentinel-1 Flood Mapping STAC Directory**  
`docs/data/satellites/sentinel-1/stac/flood/`

Governed STAC Collections & Items for  
**binary flood masks, multi-class flood layers, coherence-assisted flood maps, and flood probability surfaces**  
derived from Sentinel-1 SAR (RTC γ⁰, VH/VV ratio, coherence loss).

</div>

---

## 📘 1. Overview

This directory contains the **full governed STAC structure** for Sentinel-1 SAR-derived flood products:

- binary flood masks (water / no-water)  
- multi-class flood depth indicators  
- VH/VV ratio-based flood classifiers  
- coherence-assisted flood detection  
- probability surfaces & confidence layers  
- QA & uncertainty layers  
- sovereignty-generalized geometries  
- FAIR+CARE compliant governance metadata  
- DCAT/JSON-LD + PROV-O lineage  

Flood datasets are **sensitive** due to their ability to reveal:

- hydrological behavior of sovereign lands  
- culturally significant waterways  
- ecological vulnerability zones  

Thus **CARE-B classification** and sovereignty generalization are **mandatory**.

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/flood/
├── 📄 README.md                          # This file
│
├── 🗂️ collections/                       # Flood STAC Collections
│   └── collection_flood.json
│
└── 📦 items/                              # Flood STAC Items (scene-level)
    ├── S1A_IW_FLD_20250411T120010.json
    ├── S1B_IW_FLD_20250318T223045.json
    └── …
~~~

---

## 🧩 3. Flood STAC Collection Structure

Defines:

- spatial & temporal extent  
- `"sar:product_type" = "FLOOD"`  
- hydrological taxonomy (binary/multi-class/probability)  
- acquisition & processing metadata  
- `"kfm:*"` governance inheritance  
- DCAT dataset crosswalk  
- JSON-LD context (SAR, hydrology, governance)  
- PROV-O lineage anchors  

Must pass:

- STAC schema validation  
- DCAT compliance  
- JSON-LD context rules  
- sovereignty checks  

---

## 🧩 4. Flood STAC Item Structure

### 🌐 Core Properties
- `datetime`  
- `"sar:product_type" = "FLOOD"`  
- `"sar:instrument_mode" = "IW"`  
- `"sar:polarizations"` = VV/VH  
- `sar:frequency_band = "C"`  
- `proj:*` CRS & transform  
- orbit metadata  

### 🗺 Geometry (Generalized)
- polygon footprint  
- bbox  
- sovereignty-generalized shape where required  
- `"kfm:mask_required"` frequently = true  

### 📦 Assets  
- `"flood_mask"` — binary COG  
- `"flood_multiclass"` — shallow / deep / mixed (optional)  
- `"flood_prob"` — probability surface (optional)  
- `"qa"` — flood QA mask  
- `"thumbnail"` — PNG quicklook  
- `"metadata"` — ancillary SAFE metadata  
- optional `"coherence"` asset for coherence-assisted mapping  

### 🔗 Link Graph
- `"self"`  
- `"collection"`  
- `"parent"`  
- `"root"`  
- `"derived_from"` → RTC/GRD/GRDH  

### 🧬 PROV-O Lineage
Documents:

- flood classification pipeline  
- DEM, RTC, coherence dependencies  
- sovereignty masking activity  
- energy/carbon metrics  

---

## 🔐 5. FAIR+CARE & Sovereignty Enforcement

Flood layers are **high governance priority**, due to:

- intersection with tribal lands  
- cultural/historical hydroscapes  
- ecological sensitivity (wetlands, riparian, protected waterways)

Every Item + Collection must include:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Governance validated by:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  

---

## 🧪 6. CI Validation Requirements

Flood STAC datasets must pass:

- STAC 1.x schemas  
- SAR/Flood extension compliance  
- geometry ↔ bbox consistency  
- correct asset roles (COG/PNG/JSON)  
- `"kfm:*"` governance metadata  
- PROV-O lineage completeness  
- DCAT metadata compatibility  

Any violation → **blocked release**.

---

## 🔁 7. Flood Pipeline Position

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → RTC gamma0 generation
 → VH/VV ratio + coherence-based flood detection
 → multi-class flood classification (optional)
 → probability surface generation (optional)
 → sovereignty masking (mandatory)
 → flood QA
 → STAC Item generation
 → flood Collection update
 → governed release
~~~

---

## 🔮 8. Applications Across KFM

- hydrology & watershed studies  
- hazard/flood risk analysis  
- ecological/wetland interaction modeling  
- disaster-response overlays  
- Story Node v3 flood narratives  
- Focus Mode v3 sovereign-safe hydrology reasoning  
- climate-change flood regime monitoring  

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                                      |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 flood STAC directory README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV-integrated; CI-safe.    |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Flood Collections](../collections/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

