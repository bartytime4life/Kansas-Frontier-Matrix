---
title: "🛰️ Sentinel-1 GRDH — STAC Directory (High-Resolution σ⁰ Backscatter · Fine-Scale Land & Hydrology Dynamics)"
path: "docs/data/satellites/sentinel-1/stac/grdh/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (High-Resolution SAR Derivative)"
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

fair_category: "F3-A1-I2-R4"
care_label: "CARE-B (High-Resolution SAR · Disturbance-Sensitive)"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
public_exposure_risk: "Medium"
risk_category: "High"
redaction_required: true

data_steward: "Remote Sensing Working Group · FAIR+CARE Council"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/sentinel1-grdh-collection-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-grdh-collection-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-grdh-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-grdh"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/grdh/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded upon next ESA GRDH reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **Sentinel-1 GRDH STAC Directory**  
`docs/data/satellites/sentinel-1/stac/grdh/`

Governed STAC structure for  
**Ground Range Detected · High Resolution (GRDH)**  
σ⁰ VV/VH calibrated SAR backscatter used for  
fine-scale hydrology, disturbance, infrastructure impact, & land-change analytics.

</div>

---

## 📘 1. Overview

This directory defines the **STAC Collections & Items** for **Sentinel-1 GRDH**  
(high-resolution Ground Range Detected backscatter).  
Compared to standard GRD:

- GRDH has **finer pixel spacing**,  
- reveals **more spatial detail**,  
- supports **higher-resolution hydrology, flood edges, disturbance, and ecological mapping**,  
- and therefore requires **stricter sovereignty & CARE controls**.

GRDH data in KFM is:

- STAC 1.x compliant  
- JSON-LD enriched  
- DCAT-mappable  
- PROV-O lineage-complete  
- FAIR+CARE aligned  
- **Sovereignty-generalized** when required  
- Fully CI-validated  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/grdh/
├── 📄 README.md                       # This file
│
├── 🗂️ collections/                    # GRDH STAC Collections
│   └── collection_grdh.json
│
└── 📦 items/                           # Scene-level GRDH Items
    ├── S1A_IW_GRDH_20250311T112845.json
    ├── S1B_IW_GRDH_20250419T223015.json
    └── …
~~~

---

## 🧩 3. GRDH STAC Collection Responsibilities

The GRDH Collection includes:

- `"sar:product_type" = "GRDH"`  
- `"sar:polarizations" = ["VV","VH"]`  
- `"sar:instrument_mode" = "IW"`  
- `"sar:frequency_band" = "C"`  
- spatial + temporal extents  
- license & provider metadata  
- `"kfm:*"` FAIR+CARE governance inheritance  
- JSON-LD SAR + governance contexts  
- DCAT Dataset metadata  
- PROV-O lineage anchors  

Collections are validated by:

- `stac_validate.yml`  
- `jsonld_validate.yml`  
- `faircare_validate.yml`  
- `data_pipeline.yml`  

---

## 🧩 4. GRDH STAC Items (Overview Only)

Scene-level Items include:

- σ⁰ VV & σ⁰ VH calibrated backscatter  
- enhanced spatial resolution  
- sovereignty-generalized footprints when required  
- ESA SAFE ancillary metadata  
- QA layers (radiometric, border-noise, speckle artifacts)  
- `"kfm:*"` governance metadata  
- PROV-O lineage (`prov:wasGeneratedBy`, `prov:used`, `prov:wasDerivedFrom`)  

Details in:

```
docs/data/satellites/sentinel-1/stac/grdh/items/README.md
```

---

## 🔐 5. FAIR+CARE & Sovereignty Enforcement

GRDH reveals more spatial detail than GRD, raising governance sensitivity:

- agricultural field transitions  
- riparian zone structure  
- fine-scale disturbance  
- infrastructure impact footprints  
- culturally sensitive patterns  

Thus **mandatory** governance metadata:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"` (often true at GRDH)  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  
- `"kfm:care_label_reason"`  

Generalization (H3 and displacement uncertainty) applied for sovereign intersections.

---

## 🧪 6. CI Validation Requirements

GRDH STAC structures must pass:

- STAC 1.x schema validation  
- SAR extension validation  
- footprint/bbox geometry checks  
- JSON-LD context resolution  
- `"kfm:*"` governance metadata  
- sovereignty masking rules  
- DCAT dataset integrity  
- PROV-O lineage structure  

Violations → **release blocked**.

---

## 🔁 7. GRDH in Sentinel-1 ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → GRDH σ⁰ backscatter generation
 → speckle filtering (high-resolution)
 → sovereignty masking (mandatory)
 → GRDH QA generation
 → STAC Item creation (items/)
 → Collection update (collections/)
 → governed release bundle
~~~

---

## 🔮 8. Applications Across KFM

- fine-scale hydrology & flood-edge detection  
- agricultural structure & field transitions  
- ecological boundary mapping  
- disturbance detection (wind, tornado, clearing)  
- Story Node v3 environmental evidence  
- Focus Mode v3 high-resolution context  
- hazard analysis & land-change monitoring  

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                                      |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 GRDH STAC directory README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-validated.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🗂 GRDH Collections](./collections/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

