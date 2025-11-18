---
title: "📜🌾 Kansas Frontier Matrix — Cultural Landscape Results: Provenance Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/cultural-landscapes/provenance/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology WG · Cultural Landscape WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscapes-provenance-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Registry"
intent: "archaeology-cultural-landscapes-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Sensitive Workflow Documentation"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Provenance Documentation with Cultural Sensitivity"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/cultural-landscapes/provenance/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "Dataset"
  prov_o: "prov:Bundle"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../schemas/json/archaeology-cultural-landscapes-provenance.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-cultural-landscapes-provenance-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:cultural-landscapes:provenance-v11.0.0"
semantic_document_id: "kfm-arch-cultural-landscapes-provenance"
event_source_id: "ledger:docs/analyses/archaeology/results/cultural-landscapes/provenance/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "contextual-linking"
ai_transform_prohibited:
  - "fabrication-of-lineage"
  - "reverse-engineering-sensitive-locations"
  - "cultural-identity-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-cultural-landscapes-provenance-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next cultural-landscape provenance update"
---

<div align="center">

# 📜🌾 **Cultural Landscape Results — Provenance Registry**  
`docs/analyses/archaeology/results/cultural-landscapes/provenance/README.md`

**Purpose:**  
Record the complete, FAIR+CARE–aligned **PROV-O lineage** for all cultural landscape result datasets (interaction spheres, corridors, ecological affordances, temporal landscapes, and predictive modeling outputs).  
This registry ensures **traceability, reproducibility, cultural safety, and scientific auditability** across all modeling pipelines.

</div>

---

## 📘 Overview

Cultural landscape provenance documents:

- every dataset used (climate, hydrology, soils, vegetation, terrain, paleoenvironment, clusters, H3 generalization layers)  
- every modeling step (KDE, least-cost path, ML/GAM predictive modeling, H3 aggregation)  
- every transformation (normalization, masking, interpolation, compositing)  
- every generalization & redaction stage (H3 r7+ rules, spatial masking, sensitivity filtering)  
- every uncertainty propagation step (variance layers, proxy disagreement)  
- AI involvement (where applicable)  
- all metadata crosswalks (STAC, DCAT, KFM extensions)  
- every WAL → Retry → Rollback checkpoint  

This ensures:

- **sovereignty and cultural safety**  
- **reproducible scientific workflows**  
- **verifiable lineage in Focus Mode & Story Nodes**  
- **compliance with MCP-DL v6.3**  
- **alignment with CARE principles**  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/cultural-landscapes/provenance/
├── README.md                                  # This file
├── interaction-spheres/                       # Provenance for interaction sphere models
│   ├── late-prehistoric/
│   ├── protohistoric/
│   ├── multi-period/
│   └── hydrology-linked/
├── corridors/                                 # Lineage for corridor modeling workflows
│   ├── hydrology/
│   ├── terrain/
│   ├── vegetation/
│   ├── climate/
│   └── composite/
├── ecological-affordances/                    # Provenance for affordance models
│   ├── soils/
│   ├── vegetation/
│   ├── hydrology/
│   ├── climate/
│   └── composite/
├── predictive/                                # Provenance for predictive ML/GAM/GLM outputs
│   ├── machine-learning/
│   ├── composite/
│   └── environmental/
├── temporal/                                  # OWL-Time–aligned temporal landscape provenance
├── uncertainty/                               # Uncertainty propagation and variance documentation
├── stac/                                      # STAC → PROV crosswalk bundles
├── metadata/                                  # DCAT → PROV crosswalk bundles
└── lineage-bundles/                            # final PROV-O JSON-LD bundles for each dataset
    ├── interaction-spheres-prov.jsonld
    ├── corridors-prov.jsonld
    ├── ecological-affordances-prov.jsonld
    ├── temporal-landscapes-prov.jsonld
    └── predictive-prov.jsonld
~~~

---

## 🔍 What Cultural Landscape PROV-O Must Capture

### **1️⃣ Data Sources**
- Climate reconstructions  
- Hydrology models  
- Soil & pedology datasets  
- Vegetation/ecozone layers  
- Terrain derivatives (slope, ruggedness)  
- Paleoenvironmental proxies  
- KDE & clustering summaries  
- H3 generalized distributions  

### **2️⃣ Modeling Activities (`prov:Activity`)**
- KDE smoothing  
- H3 generalization  
- cost-distance modeling  
- composite modeling  
- machine-learning & GAM predictive workflows  
- uncertainty propagation  
- STAC export + DCAT linking  

### **3️⃣ Result Entities (`prov:Entity`)**
- interaction spheres  
- corridor models  
- ecological affordance layers  
- predictive landscapes  
- temporal landscape sequences  
- uncertainty surfaces  

### **4️⃣ Agents (`prov:Agent`)**
- KFM modeling pipelines  
- FAIR+CARE review processes  
- AI models (if involved)  
- human analysts (role-level only; no personal identifiers)  

### **5️⃣ Provenance Relationships**
- `prov:used`  
- `prov:wasGeneratedBy`  
- `prov:wasDerivedFrom`  
- `prov:wasAttributedTo`  
- `prov:wasInformedBy`  

Each dataset must include a **lineage bundle** with complete references.

---

## 🧠 Focus Mode Integration

Provenance drives:

- narrative safety checks  
- uncertainty chip displays  
- environmental justification panels  
- “Why this interpretation?” explanations  
- dataset cross-linking and Story Node validation  

Example Focus Summary:

> **Focus Summary:**  
> Cultural landscape provenance documents all datasets, environmental models, and generalization steps used to derive this landscape interpretation. Lineage confirms these results are environmentally grounded, sovereignty-safe, and FAIR+CARE compliant.

---

## ⚠️ CARE & Ethical Safeguards

All provenance must:

- avoid exposing restricted datasets  
- avoid enabling reverse inference of sensitive sites  
- track generalization and masking steps  
- document cultural-safety filters  
- record redactions applied  

If provenance reveals potential cultural harm → dataset must be masked or removed.

---

## 🔎 Validation

Stored in `validation/` inside parent metadata directory:

- JSON Schema validation  
- SHACL graph shape validation  
- H3 integrity checks  
- lineage completeness verification  
- CARE compliance audit  

No dataset enters KFM without perfect provenance validation.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · Cultural Landscape WG · FAIR+CARE Council | Initial cultural landscape provenance registry under MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Cultural Landscape Provenance · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Cultural Landscape Results](../README.md)

</div>