---
title: "🧪 Kansas Frontier Matrix: Late Prehistoric H3 — Paleo-Seasonal Calibration Models (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/paleo_recon/calibration_models/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-paleo-calibration-v1.json"
governance_ref: "../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Calibration Metadata"
intent: "archaeology-late-prehistoric-h3-paleo-calibration-models"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Paleoenvironmental Calibration Models"
redaction_required: false
provenance_chain:
  - "docs/.../calibration_models/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Activity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-paleo-calibration-models.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-paleo-calibration-models-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:paleo-calibration-models-late-prehistoric-h3-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-paleo-calibration-models"
event_source_id: "ledger:docs/.../calibration_models/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-calibration-data"
  - "unsupported-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-calibration-models"
lifecycle_stage: "stable"
ttl_policy: "Review every 24 months"
sunset_policy: "Superseded upon next calibration-model update"
---

<div align="center">

# 🧪 **Late Prehistoric H3 — Paleo-Seasonal Calibration Models**  
`docs/.../paleo_recon/calibration_models/README.md`

**Purpose:**  
Document the **calibration models** used to generate paleoenvironmental climate reconstructions for the Late Prehistoric H3 workflow.  
These models define how raw proxy datasets (pollen, isotopes, lake cores) are transformed into temperature, precipitation, moisture balance, and vegetation reconstructions.  
Calibration logic is essential for reproducibility, interpretability, CARE governance, and Story Node v3 / Focus Mode v3 environmental narratives.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Calibration models translate multi-proxy inputs into **quantitative paleo-seasonal climate surfaces**.  
They include:

- climate analog models  
- proxy calibration curves  
- regression / ML climate prediction models  
- proxy weighting algorithms  
- uncertainty propagation frameworks  

These models:

- enforce deterministic reproducibility  
- link deep-time climate cycles to Late Prehistoric activity  
- document assumptions and transformation steps via PROV-O  
- remain compliant with CARE cultural data protections  
- support cross-mapping to STAC/DCAT metadata  

---

## 🗂️ Directory Layout

```text
docs/.../paleo_recon/calibration_models/
├── README.md                           # This file
├── temp_calibration.json               # Temperature calibration model specs
├── precip_calibration.json             # Precipitation calibration model specs
├── moisture_balance_model.json         # Hydroclimate reconstruction model
├── vegetation_calibration.json         # Paleo-vegetation calibration specifications
├── regression_models/                  # ML/GLM-based calibration logs and configs
│   ├── paleo_glm_temp.json
│   ├── paleo_glm_precip.json
│   └── paleo_rf_climate_model.json
└── metadata/                           # STAC/DCAT metadata for calibration models
````

---

## 🌡️ Temperature Calibration Model

**File:** `temp_calibration.json`

Includes:

* proxy-to-temperature calibration equations
* isotopic data mappings (δ18O)
* pollen analog climate inference models
* regional regression curves
* confidence intervals
* reproducibility parameters (seeds, config hashes)

**Used for:**

* Holocene temperature reconstruction
* seasonal (winter/summer) climate models
* cluster-environment context building

---

## 🌧️ Precipitation Calibration Model

**File:** `precip_calibration.json`

Contains:

* pollen-to-precipitation inference models
* SPEI/SPI-based proxy mappings
* sediment proxy precipitation calibration
* regression/ML model parameters

---

## 💧 Hydroclimate / Moisture Balance Models

**File:** `moisture_balance_model.json`

Defines:

* moisture balance equations
* proxy weighting schemes
* model training window
* hydrological cycle reconstruction parameters

Used in:

* terrace/corridor hydrology modeling
* Late Prehistoric environmental suitability studies

---

## 🌱 Paleo-Vegetation Calibration Models

**File:** `vegetation_calibration.json`

Includes:

* vegetation assemblage reconstruction
* biomass estimation methods
* proxy-to-vegetation calibration functions
* ecozone transition models
* uncertainty propagation

---

## 🧪 Regression & ML Calibration Models

Stored in: `regression_models/`

Includes:

* GLMs predicting climate variables from multi-proxy data
* random forest ensembles for Holocene patterns
* cross-validation summaries
* hyperparameters
* model performance metrics

Each model must include:

* full reproducibility metadata
* provenance URNs
* calibration dataset citations
* WAL-safe execution metadata

---

## 🧬 Metadata Requirements (STAC/DCAT)

All calibration models *must* include metadata files in:

```
metadata/
```

### STAC Requirements

* `type: "Feature"`
* calibration model ID
* CARE classification
* model version
* provenance references

### DCAT Requirements

* `dct:title`, `dct:description`
* `dcat:distribution`
* proxy dataset citations
* calibration method summaries
* spatial/temporal applicability ranges

---

## 🧠 Focus Mode Integration

Focus Mode v3 uses calibration metadata to:

* explain underlying climate reconstruction logic
* qualify environmental interpretations
* serve as narrative guardrails
* contextualize settlement–environment relationships

Example Focus Summary:

> **Focus Summary:**
> Calibration models integrate pollen, isotopic, and lacustrine proxy records
> to reconstruct seasonal temperature and precipitation patterns influencing Late Prehistoric settlement clustering.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                                      |
| ------: | ---------- | ---------------------------------- | ---------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial calibration metadata for Late Prehistoric paleoenvironmental inputs. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Paleoenvironmental Calibration Models · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Paleo Recon Inputs](../README.md) · [Back to Environmental Rasters](../../../README.md)

</div>
