---
title: "🛰️ Sentinel-1 GRD — STAC Directory (σ⁰ Backscatter · VV/VH · Hydrology · Land-Change)"
path: "docs/data/satellites/sentinel-1/stac/grd/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Earth Observation (CC-BY-4.0)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

license: "CC-BY-4.0 (ESA Open Data)"
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

fair_category: "F2-A1-I2-R4"
care_label: "CARE-A / CARE-B (depending on downstream transformations)"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: false

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/sentinel1-grd-collection-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-grd-collection-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-grd-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-grd"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/grd/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded upon next ESA GRD reprocessing cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **Sentinel-1 GRD STAC Directory**  
`docs/data/satellites/sentinel-1/stac/grd/`

Governed STAC Collections & Items for  
**Ground Range Detected (GRD) σ⁰ backscatter**  
used across hydrology, flood mapping, agriculture, land-change, and hazard analysis.

</div>

---

## 📘 1. Overview

This directory contains the managed STAC structure for **Sentinel-1 GRD** (Ground Range Detected) backscatter products:

- σ⁰ VV/VH calibrated backscatter  
- standard spatial resolution (not GRDH high-res)  
- used for coarse-to-mid scale land-change, hydrology, flood pre/post, and agricultural monitoring  
- foundational source for RTC, coherence, flood, deformation, and wetlands processes  
- fully governed by FAIR+CARE and sovereignty masking where required  

All GRD STAC products are:

- STAC 1.x compliant  
- JSON-LD enriched  
- DCAT compatible  
- PROV-O lineage complete  
- sovereignty-aware  
- CI-validated  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/grd/
├── 📄 README.md                           # This file
│
├── 🗂️ collections/                        # GRD STAC Collections
│   └── collection_grd.json
│
└── 📦 items/                               # GRD scene-level Items
    ├── S1A_IW_GRD_20250311T112845.json
    ├── S1B_IW_GRD_20250419T223015.json
    └── …
~~~

---

## 🧩 3. GRD STAC Collection Responsibilities

The GRD Collection defines:

- `"sar:product_type" = "GRD"`  
- `"sar:polarizations" = ["VV","VH"]`  
- `"sar:instrument_mode" = "IW"`  
- mission/platform metadata  
- bounding boxes & spatial extents  
- temporal extents  
- license & provider metadata  
- DCAT Dataset metadata  
- JSON-LD contexts (SAR, governance, provenance)  
- `"kfm:*"` governance inheritance  
- PRV-O lineage anchors  

CI validates:

- STAC Collection schema  
- DCAT compliance  
- JSON-LD resolvability  
- sovereignty metadata  
- geometry & bbox integrity  

---

## 🧩 4. GRD STAC Items (Overview Only)

GRD Items include:

- σ⁰ VV, σ⁰ VH calibrated backscatter  
- full spatial footprint polygons  
- ancillary SAFE metadata  
- thumbnails  
- QA layers (border noise, radiometric issues)  
- `"kfm:*"` governance fields  
- PROV-O lineage to source ESA scenes  
- DCAT Distribution metadata  

Full Item documentation is in:

```
docs/data/satellites/sentinel-1/stac/items/grd/README.md
```

---

## 🔐 5. FAIR+CARE & Sovereignty Controls

Although GRD is less sensitive than GRDH or InSAR deformation,  
it **can still reflect**:

- land-use changes  
- agricultural cycles  
- disturbance from storms  
- ecologically sensitive patterns  
- sovereign land surface conditions  

Thus **all GRD collections and items must include**:

- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"` (when applicable)  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Generalization rules may apply at GRD level if signals intersect sovereign H3 regions.

---

## 🧪 6. CI Validation Requirements

The GRD STAC directory must pass:

- STAC 1.x schema validation  
- SAR extension validation (`sar:*`, `s1:*`)  
- geometry/bbox sanity  
- DCAT Dataset compliance  
- JSON-LD validation  
- `"kfm:*"` governance metadata completeness  
- PROV-O lineage shape validation  
- sovereignty masking/generalization  

Any violation → **release blocked**.

---

## 🔁 7. GRD in Sentinel-1 ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → GRD σ⁰ backscatter generation
 → speckle filtering
 → sovereignty-check & potential generalization
 → STAC Item creation (items/)
 → GRD Collection update (collections/)
 → governed release bundle
~~~

---

## 🔮 8. Applications Inside KFM

- hydrology & flood pre/post comparison  
- land-cover & land-use mapping  
- agricultural monitoring (crop cycles, disturbance)  
- Story Node v3 environmental context  
- Focus Mode v3 SAR evidence  
- wetland/flood interaction context  
- mid-resolution hazard detection  

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                                         |
|--------:|------------|-----------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 GRD STAC directory README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-validated.    |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 GRD Collections](./collections/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

