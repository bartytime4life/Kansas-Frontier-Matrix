---
title: "📑🏺 Kansas Frontier Matrix — Artifact Results: Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/artifacts/metadata/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Archaeology WG · FAIR+CARE Council · Material Culture Oversight Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-results-metadata-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Metadata Registry"
intent: "archaeology-artifacts-results-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Artifact Metadata"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Artifact Metadata with Cultural Sensitivity"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/artifacts/metadata/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../schemas/json/archaeology-artifact-results-metadata.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-artifact-results-metadata-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:artifact-results:metadata-v11.0.0"
semantic_document_id: "kfm-arch-artifact-results-metadata"
event_source_id: "ledger:docs/analyses/archaeology/results/artifacts/metadata/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Metadata-Only Integration"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "context-linking"
ai_transform_prohibited:
  - "provenience-reconstruction"
  - "cultural-identity-attribution"
  - "restricted-material-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-artifacts-metadata-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next metadata schema upgrade"
---

<div align="center">

# 📑🏺 **Artifact Results — Metadata Registry**  
`docs/analyses/archaeology/results/artifacts/metadata/README.md`

**Purpose:**  
Serve as the **central metadata governance hub** for all artifact result datasets—ceramics, lithics, faunal, clustering, distributions, environmental links, and temporal patterns—within the Kansas Frontier Matrix (KFM).  
Ensures every artifact-derived product adheres to **FAIR+CARE**, **STAC/DCAT**, **PROV-O lineage**, **H3 r7+ generalization**, and **KFM-MDP v11** compliance.

</div>

---

## 📘 Overview

Artifact metadata manages:

- dataset descriptions & semantic classification  
- generalization & masking descriptions  
- uncertainty annotation  
- environmental drivers and correlations  
- public-domain verification  
- access-level & CARE sensitivity  
- dataset lineage & reproducibility  
- STAC/DCAT/PROV crosswalk harmonization  
- AI narrative compatibility (metadata-only, no sensitive content)  

This registry is the backbone of **artifact governance**, ensuring:

- cultural safety  
- transparency  
- traceability  
- semantic interoperability  
- Focus Mode narrative protection  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/artifacts/metadata/
├── README.md                                  # This file
├── dcat/                                      # DCAT metadata documents for artifact datasets
│   ├── ceramics-dcat.jsonld
│   ├── lithics-dcat.jsonld
│   ├── faunal-dcat.jsonld
│   ├── clustering-dcat.jsonld
│   └── distributions-dcat.jsonld
├── stac/                                      # STAC Items/Collections & KFM extensions
│   ├── ceramics-collection.json
│   ├── lithics-collection.json
│   ├── faunal-collection.json
│   ├── clustering-collection.json
│   ├── distributions-collection.json
│   └── templates/
│       ├── stac-item-template.json
│       └── stac-collection-template.json
├── prov/                                      # PROV-O lineage bundles for artifact categories
│   ├── ceramics-prov.jsonld
│   ├── lithics-prov.jsonld
│   ├── faunal-prov.jsonld
│   ├── clustering-prov.jsonld
│   └── distributions-prov.jsonld
├── crosswalks/                                # STAC ↔ DCAT ↔ PROV harmonization schemas
│   ├── stac-dcat-crosswalk.json
│   ├── stac-prov-crosswalk.json
│   └── metadata-harmonization-rules.json
├── uncertainty/                               # Uncertainty schema + mapping guidelines
│   ├── ceramics-uncertainty.schema.json
│   ├── lithics-uncertainty.schema.json
│   ├── faunal-uncertainty.schema.json
│   ├── clustering-uncertainty.schema.json
│   └── distributions-uncertainty.schema.json
└── validation/
    ├── metadata-validation-report.json
    ├── schema-validation.json
    └── shacl-validation.json
~~~

---

## 🧩 Metadata Domains

### **1️⃣ DCAT Metadata (`dcat/`)**
Defines:

- dataset descriptions  
- spatial-temporal summaries  
- access/licensing statements  
- CARE sensitivity notes  
- provenance indicators  
- environmental context (if applicable)  

Required fields include:

- `dct:title`  
- `dct:description`  
- `dct:temporal`  
- `dct:spatial` (H3 generalized)  
- `dct:license`  
- `dcat:distribution`  

---

### **2️⃣ STAC Metadata (`stac/`)**
Each artifact result dataset must include a STAC Item with:

- H3 geometry  
- uncertainty layers  
- environmental-driver metadata  
- CARE labels  
- lineage references  
- standardized asset references  
- optional AI explainability assets (if public-domain + safe)  

Collections group items by category:

- ceramics  
- lithics  
- faunal  
- clustering  
- distributions  

---

### **3️⃣ PROV-O Metadata (`prov/`)**
Tracks:

- dataset sources  
- analytical & processing steps  
- clustering/PCA/typology operations  
- smoothing/generalization rules  
- uncertainty propagation  
- WAL → Retry → Rollback lineage  

Each dataset must have a valid `prov:Bundle`.

---

### **4️⃣ Crosswalks (`crosswalks/`)**
Ensure interoperability by harmonizing:

- STAC & DCAT metadata  
- DCAT & PROV lineage  
- STAC & PROV entities  

This prevents metadata drift and maintains CI validity.

---

### **5️⃣ Uncertainty Metadata (`uncertainty/`)**
Standardizes:

- proxy disagreement  
- distribution variance  
- classification uncertainty  
- compositional variation  
- temporal ambiguity  

These appear in Focus Mode as **Artifact Confidence Chips**.

---

## 🧠 Focus Mode Integration

Metadata governs Focus Mode behavior by providing:

- safe dataset descriptors  
- uncertainty levels  
- environmental drivers  
- semantic keywords  
- CARE labels  
- non-sensitive narrative components  

Focus Mode uses metadata—not raw artifact data—to create safe explanatory overlays.

Example Focus Summary:

> **Focus Summary:**  
> Metadata records document uncertainty, environmental drivers, and sovereignty safeguards for this artifact dataset. These controls preserve cultural safety and ensure transparent, FAIR-aligned interpretation.

---

## 🛡 CARE & Ethical Requirements

All artifact metadata must:

- exclude restricted artifact information  
- avoid cultural identity assignments  
- avoid reconstruction of provenance  
- apply H3 r7+ masking  
- include uncertainty + safety statements  
- undergo FAIR+CARE review  

If metadata introduces cultural risk → it must be corrected or removed.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council        | Initial artifact metadata registry under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Artifact Metadata · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Artifact Results](../README.md)

</div>