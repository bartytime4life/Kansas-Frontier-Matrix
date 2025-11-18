---
title: "🧮 Kansas Frontier Matrix: Late Prehistoric H3 — Paleo-Seasonal Regression & ML Calibration Models (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/paleo_recon/calibration_models/regression_models/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-regression-models-v1.json"
governance_ref: "../../../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Calibration Models"
intent: "archaeology-late-prehistoric-h3-regression-calibration"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Paleoenvironmental Calibration / ML Models"
redaction_required: false
provenance_chain:
  - "docs/.../calibration_models/regression_models/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Activity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-regression-calibration.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-regression-calibration-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:paleo-regression-calibration-late-prehistoric-h3-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-regression-calibration"
event_source_id: "ledger:docs/.../calibration_models/regression_models/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-model-details"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-regression-calibration"
lifecycle_stage: "stable"
ttl_policy: "Review every 24 months"
sunset_policy: "Superseded on next regression model update"
---

<div align="center">

# 🧮 **Late Prehistoric H3 — Regression & ML Calibration Models**  
`docs/.../regression_models/README.md`

**Purpose:**  
Document all **regression-based and machine learning climate calibration models** used in the generation of Late Prehistoric paleoenvironmental reconstructions that feed the H3 generalized cluster workflows.  
These models serve as the computational backbone for transforming proxy datasets (pollen, isotopes, lake cores) into climate reconstruction surfaces.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Regression & ML calibration models perform the following:

- Convert raw proxy observations into continuous climate variables  
- Integrate multi-proxy datasets into weighted prediction frameworks  
- Estimate seasonal/annual temperature and precipitation  
- Provide uncertainty quantification for climate reconstructions  
- Document all modeling steps in a reproducible, lineage-governed manner  

These models are:

- deterministic, version-controlled, and reproducible  
- governed by CARE cultural data rules  
- integrated into PROV-O lineage for full transparency  
- validated via schema compliance and WAL → Retry → Rollback lineage safety  

---

## 🗂️ Directory Layout

```text
docs/.../regression_models/
├── README.md                             # This file
├── paleo_glm_temp.json                    # GLM temperature calibration
├── paleo_glm_precip.json                  # GLM precipitation calibration
├── paleo_rf_climate_model.json            # Random Forest ensemble model
├── paleo_gam_climate_model.json           # GAM-based climate predictor
├── cross_validation/                      # CV metrics & validation datasets
│   ├── cv_results_temp.csv
│   ├── cv_results_precip.csv
│   └── cv_metadata.json
└── metadata/                              # STAC/DCAT metadata for regression models
````

---

## 🔧 Model Types

### 1️⃣ Generalized Linear Models (GLM)

**Files:**

* `paleo_glm_temp.json`
* `paleo_glm_precip.json`

Used for:

* direct regression between proxy indicators and climate variables
* parametric modeling with explicit coefficients
* interpretable climate response curves

Metadata includes:

* regression formula
* coefficient tables
* validation scores
* proxy weights
* temporal calibration windows

---

### 2️⃣ Random Forest Climate Model

**File:** `paleo_rf_climate_model.json`

Used for:

* complex, nonlinear relationships
* multi-proxy integration
* variable importance measurement

Includes:

* n_estimators
* depth constraints
* RF feature importance
* reproducibility seeds

---

### 3️⃣ GAM (Generalized Additive Model)

**File:** `paleo_gam_climate_model.json`

Useful when:

* proxy–climate relationships are smooth but nonlinear
* environmental gradients drive climate patterns

Includes:

* spline basis specifications
* smoothing penalties
* proxy-specific partial effects

---

## 🧪 Cross-Validation & Performance Metrics

Stored in:

```
cross_validation/
```

Contains:

* `cv_results_temp.csv` — RMSE, MAE, R² for temperature models
* `cv_results_precip.csv` — RMSE, MAE, R² for precipitation models
* `cv_metadata.json` — fold count, random seeds, geographic CV metadata

Must include:

* spatially aware cross-validation (block-CV)
* proxy-based validation (leave-one-proxy-out)
* reproducibility metadata (seed, config hash)

---

## 🧬 Metadata Requirements (STAC/DCAT)

All regression models require metadata stored under:

```
metadata/
```

Metadata MUST include:

### STAC Fields

* `stac_version: 1.0.0`
* `type: "Feature"`
* model identifier
* CARE tags
* spatial & temporal validity
* links to input proxies and outputs
* `prov:wasGeneratedBy` lineage fields

### DCAT Fields

* title, description
* distribution (model JSON files)
* calibration dataset citations
* methodology summaries
* uncertainty & performance indicators

---

## 🧠 Focus Mode Integration Notes

Focus Mode v3 uses regression model metadata to:

* explain how raw proxy signals produce climate surfaces
* provide confidence notes
* warn users about reconstruction limitations
* support narrative-safe environmental explanations

Example Focus Summary:

> **Focus Summary:**
> Machine learning and regression climate models combine pollen, isotope, and lake-core proxies
> to estimate Late Prehistoric temperature and precipitation.
> These models introduce quantified uncertainty that informs settlement and cluster interpretations.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                                          |
| ------: | ---------- | ---------------------------------- | -------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial regression/ML calibration documentation for paleoenvironmental modeling. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Regression & ML Calibration · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Calibration Models](../README.md) · [Back to Paleo Recon Inputs](../../README.md)

</div>
