---
title: "🌿 Sentinel-1 Wetlands — STAC Collections (Inundation · Shallow Water · Riparian Wetness · Seasonal Dynamics)"
path: "docs/data/satellites/sentinel-1/stac/wetlands/collections/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public with Restrictions (Governed SAR Derivative)"
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

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../schemas/json/sentinel1-wetlands-collections-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-wetlands-collections-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-wetlands-collections-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-wetlands-collections"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/wetlands/collections/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon next ESA wetlands reprocessing cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌿 **Sentinel-1 Wetlands — Governed STAC Collections**  
`docs/data/satellites/sentinel-1/stac/wetlands/collections/`

Spatial–temporal catalogs for SAR-derived  
**wetland, saturation, shallow inundation, and riparian wetness indicators.**

</div>

---

## 📘 1. Overview

This directory contains the **STAC Collections** that organize all Sentinel-1 wetland and inundation Items.

Collections describe:

- temporal/spatial extents  
- SAR product metadata  
- wetland/inundation classification semantics  
- environmental domain attributes  
- governance controls (CARE, sovereignty, masking)  
- DCAT + JSON-LD + PROV-O metadata inheritance  
- STAC extension bindings (`sar:*`, `proj:*`, `h3:*`, `kfm:*`)  

These Collections provide the **entry points** into all wetland-related STAC Items under:

```
docs/data/satellites/sentinel-1/stac/wetlands/items/
```

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/wetlands/collections/
├── 📄 README.md                         # This file
│
└── 🌿 collection_wetlands.json          # Wetlands / Inundation STAC Collection
~~~

---

## 🧩 3. Wetland Collection Structure

### 🌐 Core Metadata
- `id = "sentinel1-wetlands"`  
- `stac_version = "1.x"`  
- `"sar:product_type" = "WETLAND"`  
- `"sar:instrument_mode" = "IW"`  
- `license = "CC-BY-4.0"` (ESA Open Data)  
- provider metadata (ESA + KFM)  
- bounding box + geometry  
- acquisition temporal extent  

### 🗺️ Spatial / Temporal Extents
Includes:

- full Collection-scale bbox  
- seasonal wetness ranges  
- time slices used for riparian/wetland expansion trends  

### 📦 Assets
Collection-level assets may include:

- `"extent_preview"` — Quicklook PNG  
- `"metadata"` — summary metadata  
- `"qa_overview"` — optional governance QA summary  

### 🔗 STAC Links
- `"self"`  
- `"root"`  
- `"parent"` (STAC root)  
- `"items"` → wetlands items index  
- `"child"` links for grouping  

### 🧬 PROV-O Lineage
Defines:

- root lineage anchors  
- pointer to SAR → wetlands transform pipeline  
- sustainability metrics (energy, CO₂e)  
- governance agents  

---

## 🔐 4. Governance & Sovereignty Controls

All wetland collections must encode:

- `"kfm:care_label"` = CARE-B  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"` → marks sovereign hydrology zones  
- `"kfm:mask_required"` → required for sovereign H3 regions  
- `"kfm:sovereignty_uncertainty_floor"` → applied to probability products  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Sovereignty generalization is **always enforced** for wetland boundaries.

Validated by:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`

---

## 🧪 5. CI Validation Behaviors

Collection must pass:

- STAC 1.x schema validation  
- correct `sar:*` + `proj:*` metadata  
- bounding geometry validity  
- internal link structure correctness  
- JSON-LD context resolution  
- DCAT dataset compliance  
- required KFM governance fields  
- PROV-O lineage structure  

Failure → **collection is blocked from release**.

---

## 🔁 6. Wetland Collection Role in the ETL Pipeline

~~~text
ESA ingest
 → RTC gamma0 creation
 → coherence integration (optional)
 → wetlands/inundation classification
 → sovereignty masking (mandatory)
 → STAC Item creation
 → STAC wetlands Collection update (this directory)
 → governed release bundle
~~~

---

## 🔮 7. Applications Inside KFM

- hydrology & ecosystem modeling  
- protected riparian area monitoring  
- wetland–flood interaction analysis  
- Story Node v3 wetland narratives  
- Focus Mode v3 environmental evidence  
- sovereignty-safe land-surface change analysis  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                         |
|--------:|------------|-----------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 Wetlands Collections README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-validated.  |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📦 Wetland Items](../items/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

