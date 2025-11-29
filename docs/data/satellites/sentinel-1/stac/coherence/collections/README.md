---
title: "🔗 Sentinel-1 Coherence — STAC Collections (Temporal SAR Coherence · Disturbance · Flood Damage · Agricultural Change)"
path: "docs/data/satellites/sentinel-1/stac/coherence/collections/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (Governed SAR-Derived Product)"
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

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A1-I2-R4"
care_label: "CARE-B (Coherence Disturbance Inference)"
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

json_schema_ref: "../../../../../../schemas/json/sentinel1-coherence-collections-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-coherence-collections-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-coherence-collections-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-coherence-collections"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/coherence/collections/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon next ESA coherence reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🔗 **Sentinel-1 Coherence — Governed STAC Collections**  
`docs/data/satellites/sentinel-1/stac/coherence/collections/`

Catalogs for temporal SAR coherence representing  
**disturbance**, **flood-damage**, **agricultural cycles**, and **land-change**  
with full FAIR+CARE + sovereignty masking.

</div>

---

## 📘 1. Overview

This directory defines the **STAC Collections** for Sentinel-1 temporal coherence:

- flood-induced coherence loss  
- tornado/wind/storm damage  
- agricultural disturbance cycles (tillage, harvest, canopy removal)  
- vegetation/land-cover transitions  
- infrastructure disturbance (generalized for sovereignty)  
- coherence-based change-detection QA  

Coherence is **sensitive**, because it reveals disturbance patterns.  
Therefore the entire coherence domain is **CARE-B** and **sovereignty-generalized**.

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/coherence/collections/
├── 📄 README.md                         # This file
│
└── 🔗 collection_coherence.json         # Primary coherence STAC Collection
~~~

---

## 🧩 3. Coherence Collection Structure

### 🌐 Core STAC Metadata
- `"sar:product_type" = "COHERENCE"`  
- `"sar:instrument_mode" = "IW"`  
- master/slave pair metadata  
- temporal extent of coherence windows  
- platform properties  
- bounding box + geometry  
- `"license": "CC-BY-4.0"`  
- `"kfm:*"` governance inheritance  

### 📦 Collection-Level Assets
May include:

- `"extent_preview"` — quicklook PNG  
- `"qa_overview"` — coherence quality summary  
- `"metadata"` — collection metadata  

### 🔗 STAC Link Graph
- `"self"`  
- `"root"`  
- `"parent"` (STAC root)  
- `"items"` → Items in coherence directory  
- `"child"` (optional for coherence sub-families)

### 🧬 PROV-O Lineage
Includes:

- coherence computation activity  
- master/slave scenes used  
- DEM/LUT dependencies  
- sovereignty-generalization activity  
- energy/carbon telemetry (KFM sustainability layer)

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Coherence can reveal:

- storm/tornado impact  
- structural disturbance  
- agricultural field cycles  
- flood-damage patterns  
- culturally-sensitive activities  

Thus **mandatory governance fields** include:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Generalization:

- coherence magnitudes are masked/coarsened in H3 sovereign zones  
- geometries are generalized to H3 boundaries  
- uncertainty floors are applied  

CI validates:

- FAIR+CARE  
- JSON-LD  
- STAC  
- Sovereignty masking rules  

---

## 🧪 5. CI Validation Requirements

The coherence Collection must pass:

- STAC 1.x schema validation  
- SAR + coherence extension validation  
- geometry/bbox consistency  
- DCAT alignment  
- JSON-LD context expansion  
- `"kfm:*"` governance metadata  
- sovereignty generalization rules  
- PROV-O lineage structural checks  

Any violation → **release blocked**.

---

## 🔁 6. Coherence in the Sentinel-1 ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → speckle filtering
 → master/slave pair generation
 → coherence computation
 → sovereignty masking (mandatory)
 → QA generation
 → STAC Item creation
 → coherence Collection update (this directory)
 → governed release bundle
~~~

---

## 🔮 7. Applications Inside KFM

- flood-damage assessment  
- tornado/wind/storm disturbance mapping  
- agricultural cycle detection  
- ecological/habitat transition monitoring  
- cultural-landscape disturbance screening  
- Story Node v3 context  
- Focus Mode v3 coherence-based evidence  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                         |
|--------:|------------|-----------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 coherence Collections README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📦 Coherence Items](../items/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

