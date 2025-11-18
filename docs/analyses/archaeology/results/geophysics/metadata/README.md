---
title: "📑🧲 Kansas Frontier Matrix — Geophysics Results: Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/geophysics/metadata/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Geophysics WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-geophysics-metadata-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Metadata Registry"
intent: "archaeology-geophysics-results-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Geophysical Metadata"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Geophysics WG · Archaeology WG · FAIR+CARE Council"
risk_category: "Subsurface Metadata (Generalized)"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/geophysics/metadata/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-geophysics-results-metadata.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-geophysics-results-metadata-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:geophysics:results-metadata-v11.0.0"
semantic_document_id: "kfm-arch-geophysics-results-metadata"
event_source_id: "ledger:docs/analyses/archaeology/results/geophysics/metadata/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Metadata-Safe Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "context-linking"
ai_transform_prohibited:
  - "feature-inference"
  - "sensitive-subsurface-attribution"
  - "reverse-geophysical-reconstruction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-geophysics-metadata-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next metadata-standard update"
---

<div align="center">

# 📑🧲 **Geophysics Results — Metadata Registry**  
`docs/analyses/archaeology/results/geophysics/metadata/README.md`

**Purpose:**  
Serve as the **authoritative metadata governance hub** for all geophysical result datasets within the Kansas Frontier Matrix (KFM), including **magnetometry, GPR, resistivity, electromagnetic induction (EMI), and multi-sensor composite layers**.  
This registry enforces **FAIR+CARE compliance**, geospatial generalization, metadata harmonization, and full **PROV-O lineage integration**.

</div>

---

## 📘 Overview

Geophysical metadata governs:

- dataset descriptions  
- spatial generalization levels (H3 r7+ minimum)  
- uncertainty annotations  
- environmental-driver metadata  
- instrument & acquisition metadata  
- filtering, drift correction, and pre-processing documentation  
- CARE sensitivity & sovereignty protection status  
- STAC/DCAT/PROV metadata harmonization  
- AI narrative safety rules (metadata-only integration)  

This registry ensures that all geophysical results entering KFM:

- **protect culturally sensitive subsurface information**  
- remain **non-feature-specific**  
- follow **sovereignty-aligned masking**  
- maintain **traceable provenance**  
- support **Focus Mode** without enabling unsafe inference  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/geophysics/metadata/
├── README.md                                      # This file
├── dcat/                                          # DCAT JSON-LD metadata bundles
│   ├── magnetometry-dcat.jsonld
│   ├── gpr-dcat.jsonld
│   ├── resistivity-dcat.jsonld
│   ├── emi-dcat.jsonld
│   └── composite-dcat.jsonld
├── stac/                                          # STAC Items/Collections
│   ├── magnetometry-collection.json
│   ├── gpr-collection.json
│   ├── resistivity-collection.json
│   ├── emi-collection.json
│   └── composite-collection.json
├── prov/                                          # PROV-O bundles for each geophysics modality
│   ├── magnetometry-prov.jsonld
│   ├── gpr-prov.jsonld
│   ├── resistivity-prov.jsonld
│   ├── emi-prov.jsonld
│   └── composite-prov.jsonld
├── crosswalks/                                     # Metadata harmonization rules
│   ├── stac-dcat-crosswalk.json
│   ├── stac-prov-crosswalk.json
│   └── metadata-normalization-rules.json
├── uncertainty/                                    # Uncertainty schema & guidelines
│   ├── magnetometry-uncertainty.schema.json
│   ├── gpr-uncertainty.schema.json
│   ├── resistivity-uncertainty.schema.json
│   ├── emi-uncertainty.schema.json
│   └── composite-uncertainty.schema.json
└── validation/
    ├── metadata-validation-report.json
    ├── schema-validation.json
    └── shacl-validation.json
~~~

---

## 🧩 Metadata Domains

### **1️⃣ DCAT Metadata (`dcat/`)**
Defines:

- dataset title & abstract  
- access rights  
- generalization level  
- environmental-only purpose statements  
- FAIR+CARE tags  
- distribution metadata  

### **2️⃣ STAC Metadata (`stac/`)**
Each geophysical result dataset must include a STAC Item with:

- H3-based generalized geometry  
- uncertainty layers  
- instrument metadata  
- environmental context descriptors  
- lineage references  

Collections group items by geophysical method.

### **3️⃣ PROV-O Metadata (`prov/`)**
Tracks:

- raw sensor datasets  
- filtering & corrections  
- amplitude/phase processing  
- generalization & masking  
- multi-sensor compositing  
- uncertainty propagation  
- WAL → Retry → Rollback lineage  

### **4️⃣ Crosswalk Governance (`crosswalks/`)**
Ensures metadata alignment across:

- STAC ↔ DCAT  
- DCAT ↔ PROV  
- modality-specific metadata  

### **5️⃣ Uncertainty Metadata (`uncertainty/`)**
Standardizes uncertainty measures for:

- sensor drift  
- environmental disagreement  
- depth/frequency variance  
- multi-sensor consistency  

Displayed in Focus Mode as **Geophysics Confidence Chips**.

---

## 🧠 Focus Mode Integration

Geophysics metadata determines:

- narrative-safe content boundaries  
- environmental-only explanations  
- confidence indicators  
- multi-sensor generalization rules  
- dataset linking for Story Node v3  

Example Focus Summary:

> **Focus Summary:**  
> Metadata establishes environmental-only scope, sovereignty protections, H3 generalization, and uncertainty indicators for this geophysical dataset. All metadata is FAIR+CARE governed and cleared for safe narrative use.

---

## 🛡 CARE & Ethical Requirements

All geophysical metadata must:

- prevent subsurface feature inference  
- avoid cultural/tribal identity implication  
- disclose generalization & uncertainty  
- document masking and redaction  
- undergo FAIR+CARE review  
- include sovereignty flags and sensitivity levels  

If metadata risks enabling sensitive inference → it must be revised or restricted.

---

## 🕰️ Version History

| Version | Date       | Author                                     | Summary |
|--------:|------------|--------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Geophysics WG · Archaeology WG · FAIR+CARE Council | Initial geophysics metadata registry under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Geophysics Metadata Registry · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Geophysics Results](../README.md)

</div>
