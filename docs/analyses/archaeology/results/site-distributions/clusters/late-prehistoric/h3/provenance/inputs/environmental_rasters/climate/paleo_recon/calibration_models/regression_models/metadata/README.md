---
title: "🧮📚 Kansas Frontier Matrix: Late Prehistoric H3 — Regression & ML Calibration Model Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/paleo_recon/calibration_models/regression_models/metadata/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-regression-metadata-v1.json"
governance_ref: "../../../../../../../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Metadata"
intent: "archaeology-late-prehistoric-h3-regression-calibration-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Model Metadata"
redaction_required: false
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/paleo_recon/calibration_models/regression_models/metadata/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-regression-metadata.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-regression-metadata-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:regression-metadata-late-prehistoric-h3-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-regression-metadata"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/paleo_recon/calibration_models/regression_models/metadata/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-metadata"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-regression-model-metadata"
lifecycle_stage: "stable"
ttl_policy: "Review every 24 months"
sunset_policy: "Superseded upon next regression metadata revision"
---

<div align="center">

# 🧮📚 **Late Prehistoric H3 — Regression & ML Calibration Metadata Registry**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/paleo_recon/calibration_models/regression_models/metadata/README.md`

**Purpose:**  
Document all **metadata artifacts** describing regression and machine-learning calibration models used in paleo-seasonal climate reconstruction for the Late Prehistoric H3 workflow.  
These metadata files ensure full FAIR+CARE compliance, complete PROV-O lineage, and safe use in Story Node v3 and Focus Mode v3 narrative systems.

</div>

---

## 📘 Overview

This registry captures metadata for:

- GLM temperature and precipitation calibration models  
- Random forest climate predictors  
- GAM (Generalized Additive Model) climate reconstructions  
- Hybrid proxy–ML calibration models  
- Cross-validation outputs referenced by models  
- Calibration configuration and hyperparameter sets  
- Spatial and temporal applicability ranges  
- Proxy source linkages  
- CARE constraints and governance notes  

All metadata must:

- conform to **KFM-MDP v11.0.0**  
- be validated via JSON Schema and SHACL  
- integrate with **STAC 1.0.0** and **DCAT 3.0**  
- participate in **PROV-O** lineage graphs  
- support **Focus Mode v3** explainability

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/paleo_recon/calibration_models/regression_models/metadata/
├── README.md                                # This file
├── glm_temp_metadata.json                    # GLM temperature calibration metadata
├── glm_precip_metadata.json                  # GLM precipitation calibration metadata
├── rf_climate_metadata.json                  # Random Forest predictor metadata
├── gam_climate_metadata.json                 # GAM climate model metadata
├── combined_regression_metadata.jsonld       # Unified metadata record for all regression models
├── model_extent.geojson                      # Spatial applicability metadata
├── temporal_extent.json                      # OWL-Time intervals for calibration windows
└── validation_report.json                    # Schema/shape validation results
~~~

---

## 🧮 GLM Calibration Metadata

### `glm_temp_metadata.json`

Describes:

- regression formula and coefficients  
- proxy variable definitions and weights  
- temporal calibration windows (OWL-Time intervals)  
- cross-validation metrics (RMSE, MAE, R²)  
- uncertainty fields for temperature estimates  
- CARE sensitivity classification  
- STAC/DCAT mapping fields  
- PROV-O lineage references (`prov:wasGeneratedBy`, `prov:used`)

### `glm_precip_metadata.json`

Includes:

- precipitation calibration regression functions  
- seasonal variables (e.g., winter/summer components)  
- proxy combination rules  
- calibration windows  
- performance metrics and residual statistics  
- spatial smoothing and transformation notes  
- CARE notes for hydroclimate interpretation  

---

## 🌲 Random Forest Climate Model Metadata

### `rf_climate_metadata.json`

Contains:

- forest hyperparameters (number of trees, depth, min samples, seed)  
- feature importance metrics  
- proxy-specific contributions to variance explained  
- training/validation dataset partitions  
- model performance metrics (RMSE, MAE, R², NSE if used)  
- spatial applicability notes and limits  
- PROV-O activity URNs for training runs  

---

## 📈 GAM Climate Model Metadata

### `gam_climate_metadata.json`

Captures:

- spline basis and smooth term definitions  
- partial effect summaries for each proxy feature  
- smoothing penalties and hyperparameters  
- cross-validation scores and diagnostics  
- temporal calibration coverage  
- uncertainty and sensitivity metadata  

---

## 📦 Combined Metadata Registry

### `combined_regression_metadata.jsonld`

This unified record:

- aggregates all GLM, RF, and GAM metadata  
- provides global model identifiers and versions  
- cross-references proxy datasets and CV results  
- encodes PROV-O lineage URNs for each calibration activity  
- contains STAC/DCAT crosswalks for model artifacts  
- embeds CARE notes and narrative safety guidance  
- includes convenience fields for Focus Mode v3 (e.g., short descriptions, confidence labels)

This file is the **canonical ingest source** for pipelines and knowledge-graph loaders.

---

## 🗺️ Spatial Extent Metadata

### `model_extent.geojson`

Specifies:

- generalized polygons describing regions where calibration models are valid  
- eco-regions or hydrological units tied to model applicability  
- exclusion zones with insufficient proxy support  
- GeoSPARQL-compatible geometry definitions  

---

## 🕰️ Temporal Metadata

### `temporal_extent.json`

Defines:

- calibration date ranges (e.g., Holocene windows, Late Prehistoric emphasis)  
- seasonal calibration intervals (winter/summer)  
- proxy chronology alignment ranges  
- OWL-Time `Interval` objects and properties  

---

## 🧪 Validation Records

### `validation_report.json`

Stores:

- JSON Schema validation results for all metadata files  
- SHACL shape validation outcomes  
- FAIR+CARE governance checks on metadata fields  
- link integrity tests (internal/ external references)  
- lineage completeness tests (presence of required `prov:*` fields)  

No metadata file may be used in production pipelines unless it passes all validations.

---

## 🧠 Focus Mode Integration

Focus Mode v3 uses regression calibration metadata to:

- explain how proxies and models yield reconstructed climate values  
- surface confidence levels and uncertainties  
- show model families and their relative performance  
- qualify environmental narrative components in Story Nodes  
- warn users where calibration reliability drops (e.g., weak proxy coverage areas)

Example Focus Summary:

> **Focus Summary:**  
> Regression and ML calibration metadata document how pollen, isotopic, and lake-core proxies  
> are combined to reconstruct Late Prehistoric temperature and precipitation.  
> These metadata-driven insights constrain confidence levels in environmental narratives and H3 cluster interpretations.

---

## 🕰️ Version History

| Version | Date       | Author                            | Summary |
|--------:|------------|-----------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial regression/ML calibration metadata registry for Late Prehistoric H3 paleoenvironmental models. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Regression Calibration Metadata · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Regression Models](../README.md) · [Back to Calibration Models](../../README.md)

</div>