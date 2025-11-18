---
title: "📜 Kansas Frontier Matrix: Late Prehistoric H3 Activity Records (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/activity_records/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-activity-records-v1.json"
governance_ref: "../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Activity Records"
intent: "archaeology-late-prehistoric-h3-provenance-activities"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Lineage Documentation"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/activity_records/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "Dataset"
  prov_o: "prov:Activity"
json_schema_ref: "../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-activity-record.schema.json"
shape_schema_ref: "../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-activity-record-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:late-prehistoric-h3-activity-records-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-activity-records"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/activity_records/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative-additions"
  - "fabricated-lineage"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public / Provenance"
role: "archaeology-results-late-prehistoric-h3-provenance-activities"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next activity log update"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Late Prehistoric H3 Provenance Activity Records**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/activity_records/README.md`

**Purpose:**  
Provide a structured index of **per-step PROV-O Activity Records** documenting every transformation, redaction, modeling procedure, and cultural safety review applied during the creation of the Late Prehistoric H3 generalized cluster datasets.

These records form the **fine-grained lineage backbone** of KFM provenance governance.

![Docs](https://img.shields.io/badge/Docs·MCP_v6.3-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory contains **JSON-LD PROV-O activity files**, each representing one transformation or modeling operation used in producing the Late Prehistoric H3 layers.

Each file documents:

- Activity inputs (`prov:used`)  
- Outputs (`prov:generated`)  
- Agents (`prov:wasAssociatedWith`)  
- CARE decisions (`care:*`)  
- Parameters and configuration  
- Time stamps  
- Links to STAC lineage  
- WAL metadata for replay & rollback  

This allows complete **pipeline replay**, **auditing**, **AI explainability**, and **CARE compliance verification**.

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/activity_records/
├── README.md                        # This file
├── activity_0001_generalization.jsonld
├── activity_0002_h3_encoding.jsonld
├── activity_0003_kde_smoothing.jsonld
├── activity_0004_spatial_validation.jsonld
├── activity_0005_care_redaction.jsonld
├── activity_0006_public_export.jsonld
└── templates/
    ├── activity_record.template.jsonld
    └── care_redaction.template.jsonld
````

Each activity record must map cleanly into **CIDOC-CRM**, **PROV-O**, and **GeoSPARQL** constructs.

---

## 🧬 PROV-O Activity Schema Requirements

Every activity record must contain:

### **1. prov:Activity Fields**

* `@id` — stable URN for the activity
* `prov:startedAtTime`
* `prov:endedAtTime`
* `prov:type` (e.g., `h3-generalization`, `kde-smoothing`)
* `prov:used` — list of inputs

### **2. prov:Entity Records (Inputs & Outputs)**

Examples:

* generalized points
* H3 hex layers
* KDE rasters
* environmental predictors
* parameter definitions

### **3. prov:wasAssociatedWith (Agents)**

* Archaeology WG
* FAIR+CARE review team
* Pipeline version (software agent)

### **4. CARE Metadata**

Included as `care:*` fields:

* `care:sensitivity`
* `care:redaction_level`
* `care:review_status`
* `care:sovereignty_notes`

### **5. KFM Extensions**

Inside `kfm:*` namespaced fields:

* `kfm:pipeline_version`
* `kfm:model_parameters`
* `kfm:confidence_estimates`
* `kfm:generalization_level`

### **6. Provenance Linkages**

* `prov:wasDerivedFrom` (input → output)
* STAC Item links (IDs)
* WAL operation IDs for replay & rollback

---

## 🧭 Activity Record Templates

Templates located in `templates/` provide:

* Consistent JSON-LD structure
* Allowed fields and datatypes
* CARE review anchors
* Human-readable comments for modelers

Authors must copy templates and fill in all mandatory fields during modeling workflows.

---

## 🧪 Validation Requirements

All activity records must:

* Pass **JSON Schema** checks
* Pass **SHACL** shape validation
* Resolve all internal and external references
* Match filenames to `@id` activity URNs
* Use ISO datetimes
* Include explicit agent attribution

CI will reject missing, malformed, or incomplete activity files.

---

## 🧠 Focus Mode Integration

Focus Mode v3 uses activity records to:

* Provide explainability (“How was this layer generated?”)
* Display lineage chips
* Show CARE-driven modifications
* Support rollback-aware narratives

Example Focus Note:

> **Focus Note:**
> H3 r7 clusters were generated through activity_0002 (H3 encoding), followed by smoothing and CARE redaction stages.
> Each step is fully traceable via PROV-O activity logs.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                                         |
| ------: | ---------- | ---------------------------------- | ------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | FAIR+CARE Council · Archaeology WG | Initial activity records documentation for Late Prehistoric H3 generalizations. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Activity-Level Provenance · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Provenance](../README.md) · [Back to H3 Directory](../../README.md)

</div>
