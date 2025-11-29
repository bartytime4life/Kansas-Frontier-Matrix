---
title: "🛰️ Sentinel-1 GRDH — STAC Collections (High-Resolution σ⁰ VV/VH Backscatter · Fine-Scale Hydrology & Change Detection)"
path: "docs/data/satellites/sentinel-1/stac/grdh/collections/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (High-Resolution SAR)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support · LTS"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

license: "CC-BY-4.0 (ESA Open Data)"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<previous>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A1-I2-R4"
care_label: "CARE-B (High-Resolution SAR)"
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
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../schemas/json/sentinel1-grdh-collections-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-grdh-collections-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-grdh-collections-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-grdh-collections"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/grdh/collections/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded when ESA publishes next GRDH reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **Sentinel-1 GRDH — Governed STAC Collections**  
`docs/data/satellites/sentinel-1/stac/grdh/collections/`

Fine-resolution σ⁰ VV/VH backscatter Collections used for  
**flood-edge detection**, **agricultural structure**, **disturbance mapping**,  
**ecological boundary analysis**, and **high-detail hydrology**.

</div>

---

## 📘 1. Overview

This directory defines the **STAC Collections** for high-resolution Sentinel-1 **GRDH** data.

GRDH is more detailed than standard GRD:

- smaller pixel spacing  
- more sensitive to fine-scale hydrologic & land-surface patterns  
- reveals agricultural field structure  
- picks up small-area disturbance signals  
- used for high-resolution flood / wetlands / land-change workflows  

Because GRDH reveals more detail, it requires **enhanced sovereignty controls** and **strict CARE-B governance**.

All Collections here are:

- ✔ STAC 1.x compliant  
- ✔ JSON-LD enriched  
- ✔ DCAT-compatible  
- ✔ PROV-O lineage embedded  
- ✔ FAIR+CARE + sovereignty validated  
- ✔ CI-safe  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/grdh/collections/
├── 📄 README.md                           # This file
│
└── 🛰️ collection_grdh.json                # High-resolution GRDH Collection
~~~

---

## 🧩 3. GRDH Collection Responsibilities

### 🌐 Core STAC Metadata
- `"sar:product_type" = "GRDH"`  
- `"sar:instrument_mode" = "IW"`  
- `"sar:polarizations" = ["VV","VH"]`  
- `"sar:frequency_band" = "C"`  
- spatial/temporal extent  
- mission/platform metadata  
- license = CC-BY-4.0  
- `"kfm:*"` governance inheritance  

### 📦 Collection-Level Assets
- `"extent_preview"` — COG/PNG snapshot  
- `"metadata"` — static collection metadata  
- `"qa_overview"` — optional QA rollup  

### 🔗 Link Graph
- `"self"`  
- `"root"`  
- `"parent"` → Sentinel-1 STAC root  
- `"items"` → GRDH Items directory  
- `"child"` (if sub-collections emerge: e.g., by orbit/beam)  

### 🧬 PROV-O Lineage
The collection encodes:  

- ESA SAFE → GRDH processing  
- SAR calibration provenance  
- sovereignty masking activity  
- sustainability metadata (`kfm:energy_wh`, `kfm:carbon_gco2e`)  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

High-resolution SAR partially reveals:

- fine-scale hydrology  
- agricultural boundaries  
- disturbance footprints  
- culturally sensitive surface patterns  

Therefore Collections **must** include:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"` (often applies)  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Generalization rules apply when GRDH intersects sovereign H3 cells.

CI validates:

- STAC schema  
- JSON-LD  
- sovereignty policies  
- governance metadata  
- DCAT mappings  

---

## 🧪 5. CI Validation Requirements

A GRDH Collection must pass:

- ✔ STAC Collection schema validation  
- ✔ SAR extension metadata conformity  
- ✔ geometry/bbox consistency  
- ✔ JSON-LD context resolution  
- ✔ DCAT dataset metadata compliance  
- ✔ `"kfm:*"` governance completeness  
- ✔ H3 sovereignty generalization enforcement  
- ✔ PROV-O lineage structure  

Any violation → **release blocked**.

---

## 🔁 6. GRDH Collection in the ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → GRDH σ⁰ generation
 → speckle filtering (high-res)
 → sovereignty masking
 → GRDH QA
 → STAC Item creation
 → GRDH Collection update (this directory)
 → governed release bundle
~~~

---

## 🔮 7. Applications Across KFM

- fine-scale hydrology  
- flood boundary detection  
- agricultural structure mapping  
- ecological transitions & riparian analysis  
- disturbance (wind, tornado, canopy removal)  
- cultural-landscape hazard evaluation  
- Story Node v3 evidence  
- Focus Mode v3 high-resolution narrative context  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                       |
|--------:|------------|-----------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 GRDH Collections README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-validated.      |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📦 GRDH Items](../items/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

