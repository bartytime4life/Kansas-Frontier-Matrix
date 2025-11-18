---
title: "🗂️🌾 Kansas Frontier Matrix — Cultural Landscape Results: STAC Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/cultural-landscapes/stac/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology WG · Cultural Landscape WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscape-stac-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Registry"
intent: "archaeology-cultural-landscape-stac"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Spatial Metadata"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Spatial Metadata with Cultural Sensitivity"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/cultural-landscapes/stac/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../schemas/json/archaeology-cultural-landscape-stac.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-cultural-landscape-stac-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:cultural-landscapes:stac-v11.0.0"
semantic_document_id: "kfm-arch-cultural-landscapes-stac"
event_source_id: "ledger:docs/analyses/archaeology/results/cultural-landscapes/stac/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "precision-location-inference"
  - "boundary-reconstruction"
  - "identity-attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-cultural-landscapes-stac-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next STAC schema update"
---

<div align="center">

# 🗂️🌾 **Cultural Landscape Results — STAC Registry**  
`docs/analyses/archaeology/results/cultural-landscapes/stac/README.md`

**Purpose:**  
Provide the authoritative **STAC (SpatioTemporal Asset Catalog) registry** for all cultural landscape result datasets—interaction spheres, corridors, ecological affordances, predictive models, temporal landscapes—generated within the Kansas Frontier Matrix (KFM).  
This registry ensures **machine-readable metadata**, **generalized spatial geometry**, **CARE-compliant classification**, and full **provenance integration**.

</div>

---

## 📘 Overview

Every cultural landscape result layer must be represented as a **STAC Item** and grouped under one or more **STAC Collections**.  
STAC metadata ensures:

- discoverability across KFM systems  
- consistent geometry and temporal definitions  
- shared crosswalks with DCAT and PROV-O  
- sovereignty-safe spatial generalization (H3 r7+)  
- FAIR metadata requirements  
- Focus Mode v3 & Story Node v3 compatibility  
- uncertainty + explainability integration (if applicable)  

No STAC Item may contain:

- exact coordinates  
- reconstructed boundaries  
- sacred/restricted geographies  
- cultural identity associations  
- site-level geometry or proxies for exact locations  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/cultural-landscapes/stac/
├── README.md                                       # This file
├── items/                                          # Individual STAC Items
│   ├── interaction-spheres/                        # Interaction sphere STAC Items
│   ├── corridors/                                  # Corridor modeling STAC Items
│   ├── ecological-affordances/                     # Environmental affordance Item layers
│   ├── settlement-patterns/                        # Settlement-pattern generalized items
│   └── temporal-landscapes/                        # Time-based cultural landscape items
├── collections/                                    # Grouped STAC Collections
│   ├── interaction-spheres-collection.json
│   ├── corridors-collection.json
│   ├── ecological-affordances-collection.json
│   ├── settlement-patterns-collection.json
│   └── temporal-landscapes-collection.json
├── templates/                                      # Reusable templates for new items/collections
│   ├── stac-item-template.json
│   └── stac-collection-template.json
├── metadata/                                       # Crosswalk + extension schemas
│   ├── dcat-crosswalk.json
│   ├── stac-kfm-extensions.schema.json
│   └── stac-cultural-landscape-extension.schema.json
└── validation/                                     # Validation outputs for STAC metadata
    ├── stac-validation-report.json
    ├── schema-validation.json
    └── stac-integrity-results.json
~~~

---

## 🧬 STAC Requirements for Cultural Landscape Results

Every STAC Item must include:

### **1️⃣ Core STAC Fields**
- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- unique `id`  
- `bbox` derived from H3 geometry  
- `geometry` ONLY as **H3 multipolygon generalization**  
- `properties.datetime` or OWL-Time interval reference  

### **2️⃣ KFM Cultural Landscape Extensions**
STAC Items must include the following:

- `kfm:landscape_type` (sphere, corridor, affordance, pattern, temporal)  
- `kfm:uncertainty` fields  
- `kfm:drivers` (hydrology, soils, vegetation, climate, terrain)  
- `kfm:care_classification`  
- `kfm:ai_explainability` (if AI-supported)  
- `kfm:domain = "archaeology"`  
- `kfm:lineage_ref` → PROV-O bundle  

### **3️⃣ Assets**
Assets may include:

- raster predictions  
- H3 vector layers  
- uncertainty grids  
- environmental driver surfaces  
- SHAP/LIME layers (if applicable)  
- linkage to narrative-ready text (via JSON-LD)  

### **4️⃣ Collections**
Collections must group STAC Items by:

- cultural landscape domain  
- environmental driver  
- modeling approach (KDE, H3, ML, GAM)  
- temporal coverage  
- uncertainty classification  

---

## 🧭 STAC–DCAT–PROV Crosswalk

Metadata in `metadata/` ensures alignment between:

- STac Items → DCAT datasets  
- DCAT datasets → PROV-O bundles  
- STAC Items → PROV-O relationships  

Crosswalk rules define:

- spatial/temporal harmonization  
- shared metadata keys  
- consistent CARE labeling  
- safety-compliant dataset grouping  

---

## 🧪 Validation Requirements

STAC must pass:

- JSON Schema validation  
- STAC 1.0.0 compliance suite  
- KFM STAC extension validation  
- H3 geometry integrity checks  
- uncertainty/driver metadata checks  
- CARE classification consistency  
- PROV linkage verification  

Any STAC entry that fails validation is **rejected**.

---

## 🧠 Focus Mode Integration

STAC metadata powers:

- Focus Mode map-layer registry  
- context-aware narrative generation  
- uncertainty chips & environmental driver explanations  
- 3D/temporal scene previews  
- Story Node spatial anchoring  

Example Focus Summary:

> **Focus Summary:**  
> STAC metadata documents generalized geometry, environmental drivers, and provenance for this cultural-landscape dataset, ensuring safe, transparent integration into Focus Mode narrative systems.

---

## 🛡️ CARE & Ethical Safeguards

All STAC records must:

- avoid precise geometry  
- pass sovereignty review  
- disclose uncertainty  
- avoid cultural identity inference  
- reflect environmental frameworks only  
- follow tribal governance directives  
- comply with FAIR+CARE policies  

If STAC metadata introduces cultural risk → it must be corrected or removed.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · Cultural Landscape WG · FAIR+CARE Council | Initial cultural landscape STAC registry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Cultural Landscape STAC Registry · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Cultural Landscape Results](../README.md)

</div>