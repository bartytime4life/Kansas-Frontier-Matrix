---
title: "📊🧪 Kansas Frontier Matrix: Late Prehistoric H3 — Regression Model Cross-Validation Validation Reports (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/paleo_recon/calibration_models/regression_models/cross_validation/validation/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-regression-cv-validation-v1.json"
governance_ref: "../../../../../../../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Validation Reports"
intent: "archaeology-late-prehistoric-h3-regression-cv-validation"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Model Validation"
redaction_required: false
provenance_chain:
  - "docs/.../cross_validation/validation/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-regression-cv-validation.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-regression-cv-validation-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:late-prehistoric-h3-regression-cv-validation-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-regression-cv-validation"
event_source_id: "ledger:docs/.../cross_validation/validation/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "timeline-generation"
ai_transform_prohibited:
  - "fabricated-validation"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-regression-cv-validation"
lifecycle_stage: "stable"
ttl_policy: "Review every 24 months"
sunset_policy: "Superseded upon next validation report revision"
---

<div align="center">

# 📊🧪 **Late Prehistoric H3 — Regression Model CV Validation Reports**  
`docs/.../cross_validation/validation/README.md`

**Purpose:**  
Provide a complete set of **validation records** for regression and machine-learning cross-validation (CV) processes used in the Late Prehistoric H3 paleoenvironmental reconstruction workflow.  
These reports ensure that all CV outputs are **accurate, schema-valid, reproducible, culturally safe**, and fully traceable under KFM’s FAIR+CARE governance and PROV-O lineage requirements.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory contains **automated and manual validation artifacts** confirming the correctness of cross-validation outputs generated for:

- GLM climate models  
- GAM climate models  
- Random Forest climate ensembles  
- Hybrid ML-proxy climate predictors  

Validation ensures compliance with:

- JSON Schema  
- SHACL constraints  
- CARE cultural governance  
- PROV-O lineage logic  
- KFM-MDP v11 structure  
- WAL → Retry → Rollback safety guarantees  

These validation artifacts feed directly into:

- **Focus Mode v3 confidence scoring**  
- **Story Node v3 environmental explainability**  
- **STAC/DCAT model metadata integrity**  
- **Neo4j provenance chain validation**  

---

## 🗂️ Directory Layout

```text
docs/.../cross_validation/validation/
├── README.md                                # This file
├── cv_schema_validation.json                # JSON Schema validation results
├── cv_shacl_validation.json                 # SHACL shape validation report
├── cv_integrity_report.json                 # Consistency & completeness checks
├── cv_faircare_review.md                    # FAIR+CARE governance review log
├── cv_lineage_validation.json               # PROV-O lineage validation
└── cv_summary_report.json                   # High-level summary of all validation outcomes
````

---

## 🧩 Validation Components

### 1️⃣ JSON Schema Validation

**File:** `cv_schema_validation.json`
Ensures all CV outputs conform to:

* regression CV schema
* field presence rules
* datatype consistency
* correct metric formatting

### 2️⃣ SHACL Validation

**File:** `cv_shacl_validation.json`
Validates:

* semantic constraints on model metadata
* expected relationships among metrics
* GeoSPARQL/OWL-Time shape compliance (if applicable)

### 3️⃣ Lineage Validation

**File:** `cv_lineage_validation.json`
Checks:

* each CV artifact links to a valid modeling `prov:Activity`
* no missing `prov:used` or `prov:generated` relations
* WAL checkpoint IDs present

### 4️⃣ FAIR+CARE Review Log

**File:** `cv_faircare_review.md`
Documents:

* cultural safety screening
* sovereignty considerations
* ethical guardrails applied to environmental interpretations

### 5️⃣ Integrity Checks

**File:** `cv_integrity_report.json`
Ensures:

* metric consistency
* convergence checks
* performance threshold confirmation
* no contradictory results

### 6️⃣ CV Summary

**File:** `cv_summary_report.json`
Provides:

* cross-model validation overview
* model performance comparison
* proxy reliability indicators
* environment-specific validation concerns

---

## 🧠 Focus Mode Integration Notes

Focus Mode v3 uses validation metadata to:

* scale narrative certainty
* annotate environmental explanations
* highlight regions with low proxy agreement
* provide transparency regarding model robustness

Example Focus Summary:

> **Focus Summary:**
> CV validation indicates strong model performance in central Kansas
> but reduced reliability in upland regions where proxy agreement is weaker.
> These confidence levels adjust environmental narratives for Late Prehistoric clusters.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                                                      |
| ------: | ---------- | ---------------------------------- | -------------------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial CV validation documentation for paleoenvironmental regression/ML calibration models. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
CV Validation · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Cross-Validation](../README.md) · [Back to Regression Models](../../README.md)

</div>
