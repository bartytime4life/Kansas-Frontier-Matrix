---
title: "📑🌾 Kansas Frontier Matrix — Cultural Landscape Results: Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/cultural-landscapes/metadata/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology WG · Cultural Landscape WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscapes-metadata-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Metadata Registry"
intent: "archaeology-cultural-landscape-results-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Generalized Cultural Landscape Metadata"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Landscape Metadata with Cultural Sensitivity"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/cultural-landscapes/metadata/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E27 Site"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../schemas/json/archaeology-cultural-landscapes-metadata.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-cultural-landscapes-metadata-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:cultural-landscapes:metadata-v11.0.0"
semantic_document_id: "kfm-arch-cultural-landscapes-metadata"
event_source_id: "ledger:docs/analyses/archaeology/results/cultural-landscapes/metadata/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "contextual-linking"
ai_transform_prohibited:
  - "cultural-boundary-attribution"
  - "restricted-landscape-inference"
  - "site-level deduction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-cultural-landscapes-metadata-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded with next metadata schema update"
---

<div align="center">

# 📑🌾 **Cultural Landscape Results — Metadata Registry**  
`docs/analyses/archaeology/results/cultural-landscapes/metadata/README.md`

**Purpose:**  
Define, organize, and enforce all metadata rules for **cultural landscape result datasets** in the Kansas Frontier Matrix (KFM).  
This registry ensures that all cultural landscape outputs—interaction spheres, corridors, ecological affordances, temporal landscapes—are compliant with **FAIR+CARE**, **PROV-O**, **STAC**, **DCAT**, and **KFM-MDP v11** standards.

</div>

---

## 📘 Overview

Cultural landscape metadata describes:

- environmental affordance layers  
- generalized corridor models  
- interaction sphere results  
- temporal cultural landscape sequences  
- composite cultural-landscape evaluations  
- uncertainty and sensitivity markers  
- explainability references (if AI-assisted)  
- provenance and transformation lineage  

This registry guarantees:

- **sovereignty-respecting metadata**  
- **H3 r7+ spatial generalization enforcement**  
- **interoperable crosswalks** (STAC + DCAT + PROV-O)  
- **machine-readable formats** for graph ingestion and Focus Mode  
- **culture-safe content boundaries**  

No metadata may imply cultural territory, identity, ownership, or restricted knowledge.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/cultural-landscapes/metadata/
├── README.md                                 # This file
├── dcat/                                     # DCAT JSON-LD datasets
│   ├── corridors-dcat.jsonld
│   ├── interaction-spheres-dcat.jsonld
│   ├── ecological-affordances-dcat.jsonld
│   └── temporal-landscapes-dcat.jsonld
├── stac/                                     # STAC Items & Collections
│   ├── corridors-collection.json
│   ├── interaction-spheres-collection.json
│   ├── ecological-affordances-collection.json
│   ├── temporal-landscapes-collection.json
│   └── templates/
│       ├── stac-item-template.json
│       └── stac-collection-template.json
├── prov/                                     # PROV-O lineage bundles
│   ├── corridors-prov.jsonld
│   ├── interaction-spheres-prov.jsonld
│   ├── ecological-affordances-prov.jsonld
│   └── temporal-landscapes-prov.jsonld
├── crosswalks/                                # STAC ↔ DCAT ↔ PROV crosswalk schemas
│   ├── stac-dcat-crosswalk.json
│   ├── stac-prov-crosswalk.json
│   └── metadata-harmonization-rules.json
├── uncertainty/                               # Uncertainty metadata schemas
│   ├── affordance-uncertainty.schema.json
│   ├── corridor-uncertainty.schema.json
│   └── interaction-sphere-uncertainty.schema.json
└── validation/
    ├── metadata-validation-report.json
    ├── schema-validation.json
    └── shacl-validation.json
~~~

---

## 🧩 Metadata Domains

### **1️⃣ DCAT Metadata (`dcat/`)**
Describes:

- dataset purpose  
- environmental drivers  
- generalization level  
- temporal extent (OWL-Time)  
- access rights & licensing  
- CARE governance metadata  

Each dataset must include:

- `dct:description`  
- `dct:temporal`  
- `dct:spatial` (generalized only)  
- `dcat:distribution`  
- sensitivity classification  

---

### **2️⃣ STAC Metadata (`stac/`)**
STAC Items define:

- dataset geometry (H3)  
- derived environmental layers  
- uncertainty assets  
- lineage references  
- dataset tags  
- temporal interval (if applicable)  

STAC Collections group datasets by:

- interaction sphere family  
- corridor type  
- environmental domain  
- temporal category  

---

### **3️⃣ PROV-O Metadata (`prov/`)**
Includes:

- model transformations  
- dataset dependencies  
- uncertainty propagation  
- lineage of composite layers  
- WAL → Retry → Rollback lineage  
- generalization & masking logs  

Every cultural landscape result MUST have a `prov:Bundle`.

---

### **4️⃣ Crosswalks (`crosswalks/`)**
Ensures perfect interoperability between:

- STAC → DCAT  
- DCAT → PROV-O  
- STAC → PROV-O  

These define:

- harmonized field names  
- required/optional fields  
- hierarchical alignment  
- spatial/temporal harmonization  

---

### **5️⃣ Uncertainty Metadata (`uncertainty/`)**
Defines:

- proxy disagreement  
- environmental model variance  
- prediction reliability  
- spatial confidence scores  

Focus Mode displays this as **Affordance Confidence Chips**, **Corridor Uncertainty Bands**, or **Landscape Stability Indicators**.

---

## 🧬 Metadata Requirements

All cultural landscape metadata MUST adhere to:

### ✔ FAIR  
- machine-readable  
- indexable  
- documented lineage  

### ✔ CARE  
- sovereignty-respecting  
- no sacred/restricted geographies  
- transparent uncertainty  
- culturally neutral language  

### ✔ PROV-O  
- complete process lineage  
- clear input–output relationships  
- no missing dependency references  

### ✔ STAC 1.0.0  
- valid schemas  
- H3 geometry  
- asset references  
- temporal extent if applicable  

### ✔ DCAT 3.0  
- dataset distribution  
- license  
- access rights  
- semantic descriptors  

---

## 🧠 Focus Mode Integration

Metadata feeds:

- narrative safety engines  
- explainability overlays  
- dataset lineage panels  
- environmental context blocks  
- time-aligned interpretation segments  

Example Focus Summary:

> **Focus Summary:**  
> Cultural landscape metadata documents environmental drivers, spatial generalization levels, and provenance for all interaction spheres, corridors, and affordance layers. These metadata ensure sovereignty-safe interpretation in Focus Mode.

---

## ⚠ Ethical & CARE Guards

Metadata must:

- avoid cultural identity inference  
- avoid reconstructing territories  
- reference environmental & ecological factors only  
- mask sensitive geographies  
- undergo FAIR+CARE review before release  

If metadata introduces cultural risk → it must be revised or removed.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council        | Initial cultural landscape metadata registry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Cultural Landscape Metadata · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Cultural Landscape Results](../README.md)

</div>