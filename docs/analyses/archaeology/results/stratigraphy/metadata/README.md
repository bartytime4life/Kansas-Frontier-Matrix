---
title: "📑⛏️ Kansas Frontier Matrix — Stratigraphy Results: Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/stratigraphy/metadata/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Stratigraphy WG · Metadata WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-stratigraphy-metadata-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Metadata Registry"
intent: "archaeology-stratigraphy-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Subsurface-Sensitive Metadata"
sensitivity_level: "High"
public_exposure_risk: "High"
indigenous_rights_flag: true
data_steward: "Stratigraphy WG · FAIR+CARE Council"
risk_category: "Subsurface Metadata Governance"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/stratigraphy/metadata/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-stratigraphy-metadata.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-stratigraphy-metadata-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:stratigraphy:metadata-v11.0.0"
semantic_document_id: "kfm-arch-stratigraphy-metadata"
event_source_id: "ledger:docs/analyses/archaeology/results/stratigraphy/metadata/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Metadata-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "stratigraphic-inference"
  - "reverse-subsurface-reconstruction"
  - "cultural-period attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / Highly Sensitive / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-stratigraphy-metadata-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Updated with next stratigraphic metadata framework revision"
---

<div align="center">

# 📑⛏️ **Stratigraphy Results — Metadata Registry**  
`docs/analyses/archaeology/results/stratigraphy/metadata/README.md`

**Purpose:**  
Provide the authoritative metadata specification for all **generalized stratigraphic result layers** in the Kansas Frontier Matrix (KFM).  
This registry governs **STAC**, **DCAT**, and **PROV-O** metadata for stratigraphic surfaces (depositional, geomorphologic, paleosols, environmental stacks), ensuring sovereignty-safe, uncertainty-aware documentation.

</div>

---

## 📘 Overview

Stratigraphy metadata governs:

- **environment-only stratigraphic descriptors**  
- **H3 r7+ generalization of all spatial layers**  
- **uncertainty metadata** (variance, reconstruction spread)  
- **proxy-source descriptions** (PD-only)  
- **DCAT dataset fields** (scope, rights, FAIR+CARE)  
- **STAC Items** for generalized subsurface layers  
- **PROV-O lineage** documenting reconstruction workflow  
- **no feature-level stratigraphy disclosure**  
- **no burial, pit, structure, or cultural inference**  

All metadata supports:

- KFM Web STAC Explorer  
- Focus Mode (environment-only reasoning)  
- Story Node context layers (non-cultural)  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/stratigraphy/metadata/
├── README.md                          # This file
├── stac/                              # STAC Items for stratigraphic layers
├── dcat/                              # DCAT JSON-LD dataset records
├── prov/                              # PROV-O metadata bundles
├── harmonization/                     # STAC ↔ DCAT ↔ PROV crosswalks
├── sensitivity/                       # CARE classification + spatial-sensitivity flags
├── uncertainty/                       # Uncertainty metadata blocks
├── qa/                                # Metadata validation outputs (schema, SHACL)
└── exports/                           # Published metadata bundles
~~~

---

## 🧩 Metadata Categories

### **1️⃣ STAC Metadata (`stac/`)**
Covers:

- STAC Items for depositional/geomorphic layers  
- H3 generalized geometry (MultiPolygon only)  
- environmental drivers  
- uncertainty surfaces  
- lineage references  

### **2️⃣ DCAT Metadata (`dcat/`)**
Includes:

- dataset definitions  
- licensing  
- temporal coverage (OWL-Time)  
- FAIR+CARE attributes  
- distribution metadata  

### **3️⃣ PROV-O Metadata (`prov/`)**
Represents:

- entity–activity–agent chains  
- smoothing / interpolation steps  
- masking and redaction logs  
- WAL → Retry → Rollback lineage  

### **4️⃣ Metadata Harmonization (`harmonization/`)**
Ensures:

- STAC ↔ DCAT consistency  
- STAC ↔ PROV linking  
- field-level normalization across layers  

### **5️⃣ Sensitivity Metadata (`sensitivity/`)**
Tracks:

- CARE labels  
- sovereignty protections  
- masking & generalization requirements  
- redaction flags  

### **6️⃣ Uncertainty Metadata (`uncertainty/`)**
Documents:

- variance  
- disagreement  
- model fragility  
- stratigraphic ambiguity  
- Focus Mode “Stratigraphy Confidence Chips”  

### **7️⃣ Metadata QA (`qa/`)**
Includes:

- JSON Schema validation  
- SHACL shape validation  
- CARE sensitivity audit  
- generalization integrity checks  

---

## 🧬 Export Requirements

Every stratigraphy result MUST include:

- STAC JSON  
- DCAT JSON-LD  
- prov:Bundle lineage  
- uncertainty metadata  
- masking logs  
- CARE labels  

Exports populate:

- `metadata/stac/`  
- `metadata/dcat/`  
- `metadata/prov/`  
- `metadata/exports/`

---

## 🧠 Focus Mode Integration

Metadata supports:

- dataset info cards  
- sovereignty alerts  
- uncertainty chips  
- environmental-only context narratives  

**Example Focus Summary:**  
> Stratigraphy metadata describes generalized subsurface tendencies, uncertainty, and sovereign masking rules—never feature-level stratigraphy or cultural information.

---

## 🛡 CARE & Ethical Requirements

All stratigraphic metadata must:

- avoid sensitive archaeology  
- generalize all spatial forms (H3 r7+)  
- document redaction steps  
- include CARE labels  
- avoid cultural or site-level inference  
- undergo FAIR+CARE review  

If metadata risks exposure → **generalize or withhold**.

---

## 🕰️ Version History

| Version | Date       | Author                                | Summary |
|--------:|------------|---------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Stratigraphy WG · FAIR+CARE Council   | Initial stratigraphy metadata registry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Stratigraphy Metadata Registry · FAIR+CARE · Sovereignty-Protected  
Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Stratigraphy Results](../README.md)

</div>
