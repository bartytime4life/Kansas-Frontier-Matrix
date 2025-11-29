---
title: "🌿 Sentinel-1 Wetlands — STAC Collections & Items (SAR Wetness · Inundation · Riparian Dynamics)"
path: "docs/data/satellites/sentinel-1/stac/wetlands/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (Governed SAR Derivative)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

license: "CC-BY 4.0 (ESA)"
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
care_label: "CARE-B"
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

json_schema_ref: "../../../../../schemas/json/sentinel1-wetlands-collection-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-wetlands-collection-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-wetlands-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-wetlands"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/wetlands/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded on next ESA wetlands reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌿 **Sentinel-1 Wetlands / Inundation STAC Directory**  
`docs/data/satellites/sentinel-1/stac/wetlands/`

All governed STAC **Collections & Items** for  
**SAR-derived wetland, saturated soil, riparian, and shallow inundation indicators.**

</div>

---

## 📘 1. Overview

This directory contains the **full STAC structure** for Sentinel-1 wetland & inundation mapping:

- SAR-based shallow water detection  
- riparian/wet meadow dynamics  
- ephemeral ponding  
- seasonal wetland expansion/contraction  
- vegetation–water interaction signals  
- semi-persistent inundation detection  

These layers are **governance-sensitive** due to overlap with:

- tribal waterways  
- culturally protected areas  
- ecologically sensitive zones  
- sovereign land hydrological dynamics  

Thus, **sovereignty-safe H3 generalization** and **CARE-aligned governance** are mandatory.

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/wetlands/
├── 📄 README.md                          # This file
│
├── 🗂️ collections/                       # STAC Collections (wetlands)
│   └── collection_wetlands.json
│
└── 📦 items/                              # Scene-level wetland Items
    ├── S1A_IW_WET_20250411T120010.json
    ├── S1B_IW_WET_20250318T223045.json
    └── …
~~~

---

## 🧩 3. Wetland STAC Collection Features

The wetlands Collection defines:

- temporal & spatial extents  
- SAR product type `WETLAND`  
- hydro-ecological classification semantics  
- governance metadata inheritance  
- DCAT Dataset metadata  
- JSON-LD context (SAR + GeoSPARQL + governance)  
- PROV-O lineage references  
- sovereignty generalization rules  

It is validated by:

- `stac_validate.yml`  
- `jsonld_validate.yml`  
- `faircare_validate.yml`

---

## 🧩 4. Wetland STAC Item Features

Each Item provides:

### 🌐 Core Metadata  
- `datetime`  
- `sar:product_type = "WETLAND"`  
- `sar:instrument_mode = "IW"`  
- `sar:polarizations = ["VV","VH"]`  
- DEM-based metadata for terrain-normalized layers  
- orbit metadata (state, cycle, relative orbit)

### 🗺 Geometry / Sovereignty Generalization  
- polygon footprint  
- bbox  
- **H3-generalized shape inside sovereign zones**  
- `"kfm:mask_required"` ALWAYS considered

### 📦 Assets  
- `"wetland_mask"` — binary COG (wetland / non-wetland)  
- `"wetland_prob"` — optional probability surface  
- `"coherence"` — optional supporting coherence  
- `"thumbnail"`  
- `"qa"` — ambiguity/saturation QA  
- `"metadata"` — SAFE metadata  

### 🔗 Link Structure  
- `"self"`  
- `"collection"`  
- `"parent"`  
- `"root"`  
- `"derived_from"` → RTC / GRD/GRDH scene

### 🧬 PROV-O Lineage  
Includes:

- DEM dependencies  
- RTC backscatter  
- coherence (if used)  
- flood adjacency models (optional)  
- sovereignty masking activity signatures

---

## 🔐 5. FAIR+CARE & Sovereignty Controls (Mandatory)

Wetland mapping intersects high-sensitivity regions.  
Thus all Items and Collections must include:

- `"kfm:care_label"` (CARE-B)  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Geometry & uncertainty are **generalized**, not raw.

Validated by CI pipelines:

- FAIR+CARE validation  
- STAC validation  
- JSON-LD validation  

---

## 🧪 6. CI Validation Behavior

Wetland STAC data must pass:

- STAC 1.x schema checks  
- SAR extension → wetlands extension validation  
- geometry/bbox consistency  
- governance metadata completeness  
- sovereignty masking enforcement  
- asset role/type correctness  
- PROV-O lineage presence  
- DCAT compatibility  

Any violations → **blocked from release**.

---

## 🔁 7. Wetlands in the Sentinel-1 ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → RTC normalization
 → flood + coherence + seasonal wetness modeling
 → wetland detection classifiers
 → sovereignty masking (mandatory)
 → QA application
 → STAC Item generation
 → STAC Collection update
 → governed release bundle
~~~

---

## 🔮 8. Applications Across KFM

- hydrology & watershed modeling  
- ecological habitat analysis  
- riparian corridor studies  
- cultural-landscape safety overlays  
- Story Node v3 narratives  
- Focus Mode v3 SAR-based environmental reasoning  
- long-term wetland trend analysis  

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                                     |
|--------:|------------|-------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 wetlands STAC overview; FAIR+CARE/H3 aligned; STAC/DCAT/PROV-integrated; CI-safe.        |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 STAC Collections](../collections/README.md) · [🌐 Sentinel-1 Root](../../../../../sentinel-1/README.md)

</div>

