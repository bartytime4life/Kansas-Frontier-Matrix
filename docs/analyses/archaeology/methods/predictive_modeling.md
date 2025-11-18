---
title: "📊 Kansas Frontier Matrix — Archaeology Predictive Modeling Methods"
path: "docs/analyses/archaeology/methods/predictive_modeling.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/archaeology-predictive-modeling-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Draft / In Review"
doc_kind: "Methods"
intent: "archaeology-predictive-modeling"
fair_category: "F1-A1-I1-R1"
care_label: "Public / CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Modeling / Interpretive"
redaction_required: true
provenance_chain:
"docs/analyses/archaeology/methods/README.md@v10.4.0"
  previous_version_hash: "<previous-sha256>"
  ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "HowTo"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  json_schema_ref: "../../../../schemas/json/archaeology-predictive-modeling-methods.schema.json"
  shape_schema_ref: "../../../../schemas/shacl/archaeology-predictive-modeling-methods-shape.ttl"
  doc_uuid: "urn:kfm:doc:archaeology:methods:predictive-modeling-v11.0.0"
  semantic_document_id: "kfm-doc-archaeology-predictive-modeling-methods"
  event_source_id: "ledger:docs/analyses/archaeology/methods/predictive_modeling.md"
  immutability_status: "mutable-draft"
  doc_integrity_checksum: "<sha256>"
  ai_training_inclusion: false
  ai_focusmode_usage: "Allowed with restrictions"
  ai_transform_permissions:
* "summaries"
* "semantic-highlighting"
* "timeline-generation"
* "a11y-adaptations"
  ai_transform_prohibited:
* "speculative additions"
* "unverified historical claims"
* "re-attribution of cultural ownership"
  machine_extractable: true
  accessibility_compliance: "WCAG 2.1 AA"
  jurisdiction: "Kansas / United States"
  classification: "Public / Methods"
  role: "archaeology-methods-predictive"
  lifecycle_stage: "draft"
  ttl_policy: "Review every 12 months or upon major model change"
  sunset_policy: "Superseded when v11.x predictive modeling framework is adopted"
---

<div align="center">

# 📊 **Kansas Frontier Matrix — Archaeology Predictive Modeling Methods**

`docs/analyses/archaeology/methods/predictive_modeling.md`

**Purpose:**
Define the **methods, constraints, and governance rules** for **archaeological predictive modeling** in the Kansas Frontier Matrix (KFM), including how models use environmental, cultural, and historical inputs to estimate site likelihood, interaction zones, and landscape use in a **FAIR+CARE-compliant**, reproducible, and ontology-aligned manner.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()
[![KFM-MDP v11.0](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.0-informational)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]()
[![Status: Draft](https://img.shields.io/badge/Status-Draft-yellow)]()

</div>

---

## 📘 Overview

This document standardizes **predictive modeling methods** for archaeology within KFM, covering:

* How environmental, cultural, and historical variables are combined to model:

  * **Site location likelihood**
  * **Settlement corridors and interaction spheres**
  * **Landscape use intensity and change through time**
* How models are documented, validated, and integrated with:

  * **STAC/DCAT datasets**
  * **Neo4j knowledge graph (CIDOC-CRM, PROV-O, GeoSPARQL)**
  * **Story Nodes and Focus Mode narratives**
* How CARE principles constrain which outputs may be displayed, generalized, or fully hidden.

All predictive models must be:

* **Methodologically explicit** (no “black box” models).
* **Reproducible** from code, parameters, and inputs.
* **Ethically constrained**, especially for sensitive site prediction.
* Integrated into the **WAL → Retry → Rollback → Lineage** safety plane for data and model results.

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/methods/
├── README.md                         # Archaeology methods index
├── predictive_modeling.md            # This file (methods framework)
├── spatial-statistics.md             # Spatial autocorrelation, clustering, KDE
├── interaction-spheres.md            # Interaction sphere methods (Great Bend, Protohistoric Wichita, etc.)
└── validation/
    └── README.md                     # Archaeology validation framework
```

Model-specific implementations, notebooks, and scripts live under:

```text
src/pipelines/archaeology/predictive_modeling/
data/work/archaeology/predictive_modeling/
```

---

## 🧭 Modeling Goals & Use Cases

Predictive modeling in KFM aims to:

* Estimate **relative probability** of archaeological site occurrence across the landscape.
* Highlight **potential corridors** (trails, riverine networks, trade routes).
* Explore **interaction spheres** (e.g., Great Bend Aspect, Protohistoric Wichita).
* Support **scenario testing**, not deterministic “site finding” tools.
* Provide **context layers** for Focus Mode Story Nodes (e.g., “high-likelihood settlement band along river X”).

Explicitly **out of scope**:

* Exact site prediction for undisclosed or sacred locations.
* Automated decision-making for land management, development, or excavation without expert review.
* Any use that undermines tribal or community sovereignty over heritage information.

---

## 📊 Data Inputs & Feature Engineering

Predictive models must declare and document all input data and features. Typical categories:

### Environmental Predictors

* Topography: elevation, slope, aspect, relative relief.
* Hydrology: distance to rivers/streams/springs, floodplain indicators.
* Soils: soil type, drainage, fertility, parent material.
* Vegetation & landcover: historical and modern, where available.
* Climate: temperature, precipitation, drought indices (historical or reconstructed).

### Cultural & Historical Predictors

* Known archaeological sites (generalized or masked) used **only** in training/evaluation.
* Historic trails, roads, and travel corridors.
* Proximity to known settlements, mound groups, or ritual landscapes (generalized).
* Ethnohistoric geography and documented land use patterns.

### Feature Engineering Rules

* Feature transformations (e.g., log distance, normalized slope) must be:

  * Documented in **code comments** and **method reports**.
  * Logged in **transformations logs** (`provenance/transformations-log.csv`).
* Any masking or H3 generalization applied to sensitive inputs must be recorded as part of **CARE provenance**.
* Derived rasters must be registered in **STAC Collections/Items** with clear lineage.

---

## ⚙️ Modeling Approaches

KFM allows a mix of **classical**, **Bayesian**, and **machine learning** approaches, with strict documentation.

### 1️⃣ Heuristic/Knowledge-Driven Models

* Based on expert-defined rules (e.g., buffers and thresholds):

  * “Within X km of major river”
  * “Slope less than Y degrees”
  * “Within Z km of known trade corridor”
* Must be accompanied by a **transparent justification** (literature, expert consensus).
* Implemented with explicit GIS operations and documented in method logs.

### 2️⃣ Statistical & Spatial Models

* Logistic regression, generalized linear models (GLM).
* Spatial point process models (e.g., inhomogeneous Poisson models).
* Kernel density estimation (KDE) for use-intensity surfaces.
* Geostatistical approaches (e.g., variograms, kriging) where appropriate.

Requirements:

* Report coefficients, p-values, confidence intervals.
* Assess multicollinearity and model fit.
* Evaluate spatial autocorrelation (e.g., Moran’s I on residuals).

### 3️⃣ Machine Learning & Ensemble Models

Allowed methods (with full documentation):

* Random forest, gradient boosting, and other tree ensembles.
* Regularized regression (LASSO, elastic net) for feature selection.
* Basic neural models, **only** if architecture and training data are fully documented.

Requirements:

* No opaque “black box” models without explainability (e.g., SHAP, permutation importance).
* Store model configuration, hyperparameters, and random seeds.
* Log training/validation splits and cross-validation schemes.

---

## 🧪 Model Training, Validation & Uncertainty

### Training & Test Splits

* Use spatially-aware partitioning where possible (e.g., block cross-validation).
* Never train and test on overlapping or nearly co-located sites.
* Document split strategy (random, spatial blocks, temporal holdout).

### Evaluation Metrics

At minimum:

* AUC / ROC and PR curves where applicable.
* Accuracy / recall / precision for classification-style models.
* Brier score or calibration curves for probability outputs.
* Spatial performance summaries (e.g., accuracy per eco-region or watershed).

### Uncertainty & Limitations

Each model must have a **limitations** subsection summarizing:

* Temporal applicability (e.g., only Late Prehistoric, etc.).
* Geographic bounds (study area extent).
* Known biases (survey coverage, reporting biases, colonial archive skew).
* Appropriate usage (contextualization vs. operational decision-making).

Uncertainty surfaces (where calculated) must be stored alongside primary predictions and described in STAC metadata.

---

## ⚖️ FAIR+CARE & Cultural Safety Constraints

Predictive models in archaeology are **ethically high-risk**. KFM enforces:

* **Generalization of outputs**:

  * Public layers must be generalized (e.g., H3 cells, smoothed rasters), especially in high-likelihood regions.
  * High-resolution probability maps are restricted to authorized reviewers and tribal partners.

* **No “prospecting maps” for looting**:

  * All public visualizations must be clearly contextual and non-operational.
  * Legends and descriptions should emphasize uncertainty and ethical constraints.

* **CARE enforcement**:

  * Tribal and community partners may veto or revise model outputs that intersect sensitive landscapes.
  * If CARE risk is high, a model may be marked **internal-only** or suppressed from the public map.

* **Narrative framing**:

  * Focus Mode must describe predictive outputs as **scenario-based** and interpretive, not as definitive truth.
  * Avoid language implying discovery rights or ownership.

---

## 🧠 Graph, Story Node & Focus Mode Integration

### Knowledge Graph (Neo4j)

Predictive surfaces and derived regions create or link to:

* `Dataset` nodes describing model outputs (raster/vector).
* `Place` nodes representing generalized regions (H3 cells, buffered zones).
* `Event` or `Activity` nodes for modeling runs (PROV-O `prov:Activity`).
* Relationships:

  * `prov:wasGeneratedBy` (dataset → modeling activity)
  * `prov:used` (activity → environmental/cultural datasets)
  * `ASSOCIATED_WITH` (region → interaction sphere, culture, phase)

### Story Nodes

Predictive models inform Story Nodes by:

* Providing **context surfaces** (e.g., “this Story Node occurs in a region of high predicted Late Prehistoric settlement likelihood”).
* Supplying **narrative hooks** about landscape constraints, movement corridors, and environmental affordances.
* Being cited in Story Node metadata as **interpretive layers**, not primary evidence.

### Focus Mode

Focus Mode:

* Uses predictive layers as **optional overlays**, clearly labeled as models.
* May show **Focus Summary** callouts such as:

> **Focus Summary:** Modelled Late Prehistoric settlement likelihood is highest along major river terraces, but this surface is generalized and should not be used to infer specific undiscovered sites.

* Must show model provenance (author, date, method, data inputs) and CARE labels alongside any predictive visualization.

---

## 🛰 STAC/DCAT Metadata & Provenance

All predictive model outputs must be registered as STAC/DCAT assets with full provenance.

Example STAC Item snippet for a predictive raster:

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "archaeology-predictive-model-late-prehistoric-v1",
  "bbox": [-102.0, 37.0, -94.6, 40.0],
  "properties": {
    "datetime": "2025-11-15T00:00:00Z",
    "kfm:domain": "archaeology",
    "kfm:model_type": "predictive-site-likelihood",
    "kfm:temporal_scope": "Late Prehistoric",
    "care:sensitivity": "generalized",
    "prov:wasGeneratedBy": "urn:kfm:activity:arch-predmodel-lp-2025-11-15"
  },
  "assets": {
    "prediction_raster": {
      "href": "s3://kfm/archaeology/predictive/late_prehistoric_prob_v1.tif",
      "type": "image/tiff; application=geotiff",
      "roles": ["data"]
    }
  }
}
```

Provenance entries must appear in:

* `provenance/transformations-log.csv` for the modeling run.
* PROV-O-compatible graphs in Neo4j.

---

## 🧪 Reproducibility & WAL / Rollback Integration

Predictive modeling pipelines must:

* Run within the **reliable pipelines** framework (WAL → Retry → Rollback → Hotfix).
* Record configuration, code version, and environment details.
* Support **exact re-runs** given the same inputs and parameters.

If a model is later deemed problematic (e.g., ethical concern, data error):

* WAL entries allow tracing all derived products.
* Rollback procedures ensure dependent layers (e.g., Story Nodes, web overlays) are updated or disabled.
* Governance ledger entries record the deprecation and replacement of models.

---

## 🕰️ Version History

| Version | Date       | Author                            | Summary                                                                                          |
| ------: | ---------- | --------------------------------- | ------------------------------------------------------------------------------------------------ |
| v11.0.0 | 2025-11-17 | Archaeology Working Group (Draft) | Initial v11 methods framework for archaeology predictive modeling; aligned with KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Archaeology Methods · MCP-DL v6.3 Compatible · FAIR+CARE Governed · Predictive Modeling Methods (Draft v11.0.0)

</div>
