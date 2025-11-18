---
title: "🧬🤖 Kansas Frontier Matrix — AI Interpretation Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/ai-interpretations/metadata/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / AI Governance Board · FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-ai-interpretations-metadata-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Metadata Registry"
intent: "archaeology-ai-interpretations-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Sensitive Interpretation Metadata"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "AI Governance Board · Archaeology WG · FAIR+CARE Council"
risk_category: "AI Metadata / Narrative Safety"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/ai-interpretations/metadata/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../schemas/json/archaeology-ai-interpretations-metadata.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-ai-interpretations-metadata-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:ai-interpretations:metadata-v11.0.0"
semantic_document_id: "kfm-arch-ai-interpretations-metadata"
event_source_id: "ledger:docs/analyses/archaeology/results/ai-interpretations/metadata/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Narrative-Safe"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "context-linking"
ai_transform_prohibited:
  - "speculation"
  - "cultural-identity-attribution"
  - "inferred-site-locations"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-ai-interpretations-metadata-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next metadata schema release"
---

<div align="center">

# 🧬🤖 **AI Interpretation Metadata Registry**  
`docs/analyses/archaeology/results/ai-interpretations/metadata/README.md`

**Purpose:**  
Define the **complete metadata framework** governing all AI-generated interpretive outputs across the Kansas Frontier Matrix (KFM), ensuring they remain FAIR+CARE–aligned, culturally safe, scientifically grounded, and fully traceable through PROV-O lineage.  
This registry ensures that every AI narrative, cluster explanation, corridor summary, or environmental interpretation is supported by **validated metadata**, **ethical constraints**, and **machine-readable structure**.

</div>

---

## 📘 Overview

This metadata registry documents:

- metadata schemas governing AI interpretive assets  
- required STAC/DCAT fields  
- CARE classification and narrative-safety levels  
- AI model version metadata  
- explainability metadata (SHAP/LIME)  
- uncertainty metadata  
- temporal (OWL-Time) and spatial (H3 generalized) descriptors  
- PROV-O lineage integration  
- dataset cross-references  
- narrative safety filters and logs  

Metadata captured here ensures AI interpretations:

- cannot produce sensitive cultural information  
- remain grounded in validated datasets only  
- include uncertainty transparency  
- are reproducible and governed under AI safety rules  
- meet CARE sovereignty requirements  
- comply with FAIR metadata guidelines  
- integrate seamlessly with Focus Mode v3 and Story Node v3  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/ai-interpretations/metadata/
├── README.md                                 # This file
├── ai-metadata.schema.json                    # Master AI metadata schema
├── ai-metadata.shacl.ttl                      # SHACL validation rules
├── classification/                            # CARE classification metadata bundles
│   ├── narrative-safety-levels.json
│   ├── cultural-sensitivity-flags.json
│   └── ai-governance-flags.json
├── stac/                                      # STAC metadata templates for AI outputs
│   ├── narrative-item-template.json
│   ├── cluster-item-template.json
│   └── environmental-item-template.json
├── dcat/                                      # DCAT metadata templates
│   ├── narrative-dcat.jsonld
│   ├── cluster-dcat.jsonld
│   └── cultural-landscape-dcat.jsonld
├── explainability/                            # SHAP/LIME metadata structures
│   ├── shap-metadata.schema.json
│   └── lime-metadata.schema.json
├── uncertainty/                               # Uncertainty metadata schemas
│   ├── ai-uncertainty.schema.json
│   └── ai-uncertainty-template.jsonld
├── provenance/                                # PROV-O metadata templates
│   ├── prov-template.jsonld
│   └── prov-ai-activity.schema.json
└── validation/                                # Validation artifacts for metadata
    ├── validation_report.json
    ├── schema_results.json
    └── shacl_results.json
~~~

---

## 🧩 Metadata Domains

### **1️⃣ Classification Metadata (`classification/`)**
Defines:

- narrative safety levels  
- cultural sensitivity flags  
- AI governance-triggered safeguards  

Used by:

- Focus Mode filters  
- Story Node safety checks  
- AI Safety Engine  

---

### **2️⃣ STAC Metadata Templates (`stac/`)**
Provide STAC Items for:

- cluster interpretations  
- environmental narratives  
- cultural landscape summaries  

Required fields include:

- temporal extent (OWL-Time)  
- spatial H3 geometry  
- `care:sensitivity`  
- dataset references  
- explainability artifact links  

---

### **3️⃣ DCAT Metadata Templates (`dcat/`)**
Define dataset-level metadata:

- purpose  
- rights  
- distribution  
- accessibility  
- FAIR+CARE statements  

All AI outputs must be represented in DCAT form.

---

### **4️⃣ Explainability Metadata (`explainability/`)**
Schemas governing:

- SHAP values  
- LIME explanations  
- model-weight summaries  
- input contribution documentation  

These support Focus Mode explainability.

---

### **5️⃣ Uncertainty Metadata (`uncertainty/`)**
Documents:

- confidence intervals  
- proxy disagreement  
- model agreement scores  
- narrative uncertainty levels  

Presented to users via Focus Mode “confidence chips.”

---

### **6️⃣ Provenance Metadata (`provenance/`)**
Includes:

- AI activity records  
- dataset inputs (`prov:used`)  
- model versioning  
- safety filter logs  
- WAL lineage  

All provenance metadata must validate via SHACL and JSON schema.

---

## 🧠 Focus Mode Integration

Focus Mode v3 consumes metadata here to:

- construct narrative info panels  
- display dataset lineage  
- show confidence indicators  
- enforce narrative safety  
- dynamically redact risky content  
- support time- and space-aware explanations  

Example Focus Summary:

> **Focus Summary:**  
> AI interpretation metadata defines narrative safety levels, uncertainty ranges, and connections to underlying datasets. These constraints ensure that Focus Mode delivers culturally safe, scientifically grounded contextual information.

---

## ⚠️ CARE & Ethical Controls

All AI metadata must enforce:

- no tribal identity inference  
- no sacred landscape inference  
- spatial masking via H3 r7+  
- narrative boundaries based on AI safety triggers  
- transparency in uncertainty  
- adherence to CARE data sovereignty  
- review by FAIR+CARE + AI Governance Board  

If metadata fails validation → output must not be published.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v11.0.0 | 2025-11-17 | AI Governance Board · Archaeology WG · FAIR+CARE Council | Initial AI-interpretation metadata registry under KFM-MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
AI Interpretation Metadata · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to AI Interpretations](../README.md)

</div>