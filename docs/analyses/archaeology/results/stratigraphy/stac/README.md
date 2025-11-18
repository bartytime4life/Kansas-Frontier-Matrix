---
title: "🗂️⛏️ Kansas Frontier Matrix — Stratigraphy Results: STAC Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/stratigraphy/stac/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Stratigraphy WG · Metadata WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-stratigraphy-stac-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Registry"
intent: "archaeology-stratigraphy-stac-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Subsurface-Generalized Metadata"
sensitivity_level: "High"
public_exposure_risk: "High"
indigenous_rights_flag: true
data_steward: "Stratigraphy WG · FAIR+CARE Council"
risk_category: "Subsurface Metadata"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/stratigraphy/stac/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-stratigraphy-stac.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-stratigraphy-stac-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:stratigraphy:stac-registry-v11.0.0"
semantic_document_id: "kfm-arch-stratigraphy-stac-registry"
event_source_id: "ledger:docs/analyses/archaeology/results/stratigraphy/stac/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Metadata-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "subsurface inference"
  - "feature prediction"
  - "cultural/temporal attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / Highly Sensitive / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-stratigraphy-stac-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Changed upon next STAC-governance revision"
---

<div align="center">

# 🗂️⛏️ **Stratigraphy Results — STAC Registry**  
`docs/analyses/archaeology/results/stratigraphy/stac/README.md`

**Purpose:**  
Define the **STAC (SpatioTemporal Asset Catalog) metadata** for generalized stratigraphy results—depositional models, geomorphology surfaces, soil horizons, predictive stratigraphy, and environmental drivers—within the Kansas Frontier Matrix (KFM).  
All STAC Items and Collections must protect cultural heritage, avoid subsurface inference, and comply with **FAIR+CARE**, **H3 r7+ masking**, and **sovereignty safeguards**.

</div>

---

## 📘 Overview

Stratigraphy STAC metadata:

- describes **generalized subsurface environmental layers**, not feature-level stratigraphy  
- represents **broad depositional, geomorphic, pedogenic, and soil tendencies**  
- ensures **H3 r7+ spatial generalization** for all geometries  
- encodes **uncertainty** (variance, disagreement, model fragility)  
- includes **temporal coverage** using OWL-Time  
- links to **PROV-O lineage bundles**  
- integrates with **DCAT metadata** and internal governance tooling  
- enables safe rendering in Focus Mode, the Web Explorer, and Story Nodes  

Forbidden:

- precise soil horizons  
- buried feature or pit inference  
- cultural stratum interpretation  
- fine-grained geomorph detail  
- sub-H3 spatial geometry  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/stratigraphy/stac/
├── README.md                           # This file
├── items/                              # STAC Items for stratigraphy layers
│   ├── depositional/
│   ├── geomorphology/
│   ├── soil-horizons/
│   ├── predictive/
│   └── composite/
├── collections/                        # STAC Collections
│   ├── stratigraphy-collection.json
│   ├── depositional-collection.json
│   └── geomorphology-collection.json
├── templates/                          # Item/Collection templates
│   ├── stac-item-template.json
│   └── stac-collection-template.json
├── metadata/                           # Extensions & DCAT crosswalks
│   ├── stac-kfm-extensions.schema.json
│   ├── stac-stratigraphy-extension.schema.json
│   └── dcat-crosswalk.json
├── qa/                                 # Validation outputs
│   ├── stac-validation-report.json
│   ├── schema-validation.json
│   └── generalization-integrity.json
└── exports/                            # Finalized STAC JSON files
~~~

---

## 🧩 Required STAC Components

### **1️⃣ Core STAC Fields**
Every Item must include:

- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- geometry: **H3 MultiPolygon generalized**  
- bbox: H3-derived  
- OWL-Time temporal fields  
- assets for generalized rasters & metadata  

---

### **2️⃣ KFM STAC Extensions**
Required:

- `kfm:domain = "archaeology/stratigraphy"`  
- `kfm:generalization >= H3 r7`  
- `kfm:uncertainty` (required)  
- `kfm:care_classification`  
- `kfm:lineage_ref` (PROV-O bundle)  
- `kfm:environmental_drivers`  

---

### **3️⃣ Allowed Assets**
- generalized rasters (COG)  
- uncertainty surfaces  
- MultiPolygon geometries  
- driver rasters (generalized)  
- lineage JSON-LD  

Forbidden:

- point coordinates  
- feature-level surfaces  
- any sub-H3 geometry  

---

## 🧪 Validation Rules

All STAC metadata must pass:

- JSON Schema validation  
- KFM STAC extension validation  
- SHACL rules  
- sovereignty masking checks  
- CARE compliance checks  
- asset-path & field consistency checks  

Failures → **block dataset**.

---

## 🧠 Focus Mode Integration

STAC metadata supports:

- dataset cards  
- uncertainty chips  
- environmental narrative panels  
- timeline anchoring  
- sovereignty alerts  

**Example Focus Summary:**  
> Stratigraphy STAC metadata encodes generalized environmental-layer information, uncertainty, and lineage to enable sovereignty-safe, non-invasive interpretation in Focus Mode.

---

## 🛡 CARE & Ethical Requirements

Required for all Items:

- H3 r7+ masking  
- sovereignty-based redaction  
- FAIR+CARE classification  
- no cultural interpretation  
- no buried feature inference  
- full uncertainty documentation  

If metadata could enable sensitive inference → **withhold or generalize**.

---

## 🕰️ Version History

| Version | Date       | Author                                | Summary |
|--------:|------------|---------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Stratigraphy WG · FAIR+CARE Council   | Initial stratigraphy STAC registry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Stratigraphy STAC Registry · FAIR+CARE · Sovereignty-Protected  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Stratigraphy Results](../README.md)

</div>
