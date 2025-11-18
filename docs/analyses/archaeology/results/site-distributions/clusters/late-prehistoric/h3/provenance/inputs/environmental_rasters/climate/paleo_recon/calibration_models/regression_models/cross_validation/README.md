---
title: "📊 Kansas Frontier Matrix: Late Prehistoric H3 — Regression Model Cross-Validation Records (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/paleo_recon/calibration_models/regression_models/cross_validation/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-regression-cv-v1.json"
governance_ref: "../../../../../../../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Cross-Validation Records"
intent: "archaeology-late-prehistoric-h3-regression-cross-validation"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Model Validation"
redaction_required: false
provenance_chain:
  - "docs/.../cross_validation/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Activity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-regression-cv.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-regression-cv-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:late-prehistoric-h3-regression-cv-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-regression-cv"
event_source_id: "ledger:docs/.../cross_validation/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "timeline-generation"
ai_transform_prohibited:
  - "fabricated-validation-data"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-regression-cv"
lifecycle_stage: "stable"
ttl_policy: "Review every 24 months"
sunset_policy: "Superseded upon next CV dataset revision"
---

<div align="center">

# 📊 **Late Prehistoric H3 — Regression Model Cross-Validation Records**  
`docs/.../cross_validation/README.md`

**Purpose:**  
Provide a complete, FAIR+CARE-governed record of **cross-validation (CV) outputs** for all regression and machine-learning climate calibration models used in Late Prehistoric paleoenvironmental reconstruction.  
These CV artifacts ensure methodological transparency, reproducibility, uncertainty tracking, and full integration into the PROV-O lineage graph and Focus Mode v3 narrative safety systems.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Cross-validation is a **required validation step** for all regression and ML calibration models feeding into:

- Holocene temperature/precipitation reconstructions  
- Seasonal climate surfaces  
- Moisture-balance and hydroclimate models  
- Predictive/affordance modeling for archaeological interpretations  
- H3 generalization weighting  
- CARE-reviewed narrative framing in Story Nodes  

These CV outputs:

- quantify model reliability  
- highlight proxy dataset performance  
- document calibration limitations  
- feed uncertainty propagation  
- ensure reproducibility under WAL → Retry → Rollback → Lineage  

---

## 🗂️ Directory Layout

```text
docs/.../regression_models/cross_validation/
├── README.md                        # This file
├── cv_results_temp.csv              # Temperature CV metrics (RMSE, MAE, R²)
├── cv_results_precip.csv            # Precipitation CV metrics
├── cv_geographic_blocks.json        # Metadata for spatial block CV partitions
├── cv_proxy_leaveout.json           # Leave-one-proxy-out validation metrics
├── cv_metadata.json                 # Model-level CV metadata (folds, seeds, configs)
└── validation/                      # CV-specific validation reports
    ├── cv_schema_validation.json
    └── cv_summary_report.json
````

---

## 🔍 Cross-Validation Methods

### 1️⃣ **Geographic Block CV**

Documented in: `cv_geographic_blocks.json`

* Divides Kansas into spatial blocks
* Prevents spatial leakage
* Required for climate-proxy spatial models

### 2️⃣ **Leave-One-Proxy-Out CV (LOPO)**

Recorded in: `cv_proxy_leaveout.json`

Ensures no single proxy family (pollen, isotopes, lake cores) disproportionately biases reconstructions.

### 3️⃣ **K-Fold or Repeated K-Fold CV**

Defined in: `cv_metadata.json`

Includes:

* number of folds
* random seeds
* fold-wise metrics
* config hash

### 4️⃣ **Proxy Weight Sensitivity CV**

Assesses:

* how proxy weighting changes results
* stability of calibration functions
* robustness of reconstruction pipelines

---

## 📊 Key Metrics

All metrics must appear in `cv_results_temp.csv` and `cv_results_precip.csv`:

| Metric                 | Meaning                           | Required |
| ---------------------- | --------------------------------- | -------- |
| RMSE                   | Root Mean Squared Error           | ✔        |
| MAE                    | Mean Absolute Error               | ✔        |
| R²                     | Coefficient of Determination      | ✔        |
| NSE                    | Nash–Sutcliffe Efficiency         | optional |
| Bias                   | Systematic model bias             | ✔        |
| Proxy Influence Scores | Proxy-specific error contribution | ✔        |

---

## 🧬 Metadata Requirements (STAC/DCAT)

All CV outputs require accompanying metadata stored in:

```
metadata/ (inside parent directory)
```

Metadata MUST include:

### STAC

* model identifier
* CV method
* performance metrics
* CARE sensitivity classification
* PROV-O lineage references

### DCAT

* dataset descriptions
* distribution info
* citations for underlying proxy datasets
* temporal & spatial extents

---

## 🧠 Focus Mode Integration

Focus Mode v3 uses CV metadata to:

* scale narrative confidence scores
* provide contextual warnings (“low proxy agreement,” “high variance zone”)
* append provenance & model transparency chips
* prevent overinterpretation of paleo-environmental reconstructions

Example Focus Summary:

> **Focus Summary:**
> Cross-validation results show strong proxy agreement for central Kansas,
> with higher uncertainty toward upland regions.
> These factors inform confidence scores in environmental narratives for Late Prehistoric clusters.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                                           |
| ------: | ---------- | ---------------------------------- | --------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial regression/ML CV documentation for paleoenvironmental modeling pipelines. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Cross-Validation Records · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Regression Models](../README.md) · [Back to Calibration Models](../../README.md)

</div>
