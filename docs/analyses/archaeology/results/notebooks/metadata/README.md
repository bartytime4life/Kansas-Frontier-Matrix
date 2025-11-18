---
title: "📓📑 Kansas Frontier Matrix — Analysis Notebooks: Metadata Generation & Governance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/notebooks/metadata/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Metadata WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-metadata-notebooks-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Notebook Index"
intent: "archaeology-metadata-analysis-notebooks"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed Metadata"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology WG · Metadata WG · FAIR+CARE Council"
risk_category: "Metadata Governance"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/notebooks/metadata/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "HowTo"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-metadata-notebooks.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-metadata-notebooks-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:notebooks:metadata-v11.0.0"
semantic_document_id: "kfm-arch-metadata-notebooks"
event_source_id: "ledger:docs/analyses/archaeology/results/notebooks/metadata/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Metadata-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "schema-explanation"
ai_transform_prohibited:
  - "cultural-identity-inference"
  - "location-reconstruction"
  - "metadata-based speculation"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-metadata-notebooks-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Revised upon next metadata-framework upgrade"
---

<div align="center">

# 📓📑 **Metadata Analysis Notebooks — Results Index**  
`docs/analyses/archaeology/results/notebooks/metadata/README.md`

**Purpose:**  
Provide the authoritative index for all **metadata-generation and metadata-governance notebooks** used across archaeology, geophysics, cultural landscapes, environmental modeling, artifact analyses, and predictive pipelines in the Kansas Frontier Matrix (KFM).  
These notebooks generate **STAC/DCAT/PROV-O metadata**, enforce FAIR+CARE, and validate lineage, uncertainty, and masking rules.

</div>

---

## 📘 Overview

Metadata notebooks support:

- automated generation of **STAC Items**  
- automated generation of **DCAT JSON-LD descriptors**  
- creation & validation of **PROV-O bundles**  
- metadata harmonization across domains (artifacts, geophysics, landscapes, environmental data)  
- H3 generalization compliance checking  
- sovereignty protections & CARE labeling  
- uncertainty/variance metadata creation  
- field-level validation and schema testing  
- integration pathways for Focus Mode v3 semantic anchoring  

Outputs from these notebooks feed the final metadata directories:

- `metadata/`  
- `stac/`  
- `provenance/`  
- and narrative metadata hooks for Story Nodes.

They **never** include:

- restricted cultural identifiers  
- sacred knowledge  
- precise coordinates  
- non-generalized spatial metadata (< H3 r7)  
- speculative model interpretation  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/notebooks/metadata/
├── README.md                               # This file
├── stac/                                   # STAC metadata generation notebooks
├── dcat/                                   # DCAT JSON-LD metadata notebooks
├── prov/                                   # PROV-O bundle assembly & validation
├── harmonization/                          # STAC ↔ DCAT ↔ PROV crosswalk construction
├── uncertainty/                            # Uncertainty-metadata derivation notebooks
├── qa/                                     # Metadata integrity, schema validation, FAIR+CARE checks
└── exports/                                # JSON-LD outputs, schema logs, validation reports
~~~

---

## 🧪 Notebook Categories

### **1️⃣ STAC Notebooks (`stac/`)**
Produce:

- STAC Items for every dataset type  
- generalized geometry metadata (H3 r7+)  
- asset declarations (COG, GeoJSON, JSON-LD)  
- temporal extent metadata  
- link relationships  
- dataset previews (environmental-only)  

---

### **2️⃣ DCAT Notebooks (`dcat/`)**
Generate:

- dataset descriptions  
- licensing metadata  
- spatial/temporal descriptors  
- distribution entries  
- FAIR+CARE metadata fields  
- JSON-LD crosswalk outputs  

---

### **3️⃣ PROV-O Notebooks (`prov/`)**
Construct:

- activity → agent → entity chains  
- lineage for ETL pipelines  
- transformation logs  
- generalization & redaction records  
- uncertainty propagation metadata  
- WAL → Retry → Rollback lineage structures  

---

### **4️⃣ Metadata Harmonization (`harmonization/`)**
Create:

- STAC ↔ DCAT crosswalk tables  
- STAC ↔ PROV-O mappings  
- KFM metadata extension blocks  
- schema-level constraints  

These notebooks ensure interoperability.

---

### **5️⃣ Uncertainty Metadata (`uncertainty/`)**
Generate:

- variance estimates  
- proxy disagreement tables  
- ensemble spread metadata  
- error surface summaries  

Used by Focus Mode as **Metadata Confidence Chips**.

---

### **6️⃣ Metadata QA (`qa/`)**
Perform:

- schema validation (JSON Schema, SHACL)  
- H3-level spatial masking checks  
- sovereignty compliance verification  
- CARE risk scanning  
- STAC/DCAT/PROV synchronization testing  

---

## 🧬 Provenance & Metadata Export

Each notebook must export:

- **prov:Bundle** lineage  
- **STAC metadata blocks**  
- **DCAT JSON-LD records**  
- **uncertainty metadata**  
- **schema validation reports**  
- **generalization + redaction logs**  
- environment snapshot + config hashes  

These outputs populate the top-level dataset metadata directories.

---

## 🧠 Focus Mode Integration

Metadata notebooks feed:

- semantic anchors for Story Nodes  
- dataset badges and info cards  
- environmental-only reasoning blocks  
- uncertainty + lineage chips  
- dataset summaries in Focus Mode’s Explorer  

Example Focus Summary:

> **Focus Summary:**  
> Metadata notebooks generate the STAC, DCAT, and PROV-O structures that govern dataset discoverability, transparency, and cultural-safety in the Kansas Frontier Matrix.

---

## 🛡 CARE & Ethical Requirements

Metadata notebooks must:

- respect sovereignty & tribal data protections  
- avoid sensitive cultural identifiers  
- enforce spatial generalization rules  
- disclose uncertainty and masking  
- include CARE labels and governance notes  
- pass FAIR+CARE Council review  

If metadata introduces risk → it must be corrected or blocked.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Metadata WG · Archaeology WG · FAIR+CARE Council | Initial metadata-notebook index under KFM-MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Metadata Analysis Notebooks · FAIR+CARE Certified · Sovereignty-Safe  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Notebooks Index](../README.md)

</div>
