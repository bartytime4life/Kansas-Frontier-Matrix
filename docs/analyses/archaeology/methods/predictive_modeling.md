---
title: "📊 Kansas Frontier Matrix: Archaeology Predictive Modeling Methods"
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
  - "docs/analyses/archaeology/methods/README.md@v10.4.0"
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
  - "summaries"
  - "semantic-highlighting"
  - "timeline-generation"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
  - "re-attribution of cultural ownership"
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

# 📊 **Kansas Frontier Matrix: Archaeology Predictive Modeling Methods**  
`docs/analyses/archaeology/methods/predictive_modeling.md`

**Purpose:**  
Define the **methods, constraints, reproducibility rules, and ethical guardrails** for archaeological predictive modeling in the Kansas Frontier Matrix (KFM), aligning with FAIR+CARE, MCP-DL v6.3, ontology standards (CIDOC-CRM, GeoSPARQL, OWL-Time), and Story Node / Focus Mode v3 integration requirements.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.0](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.0-informational)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]()  
[![Status: Draft](https://img.shields.io/badge/Status-Draft-yellow)]()

</div>

---

## 📘 Overview

This document defines the **predictive modeling framework** for archaeology in KFM.  
It establishes:

- Required modeling practices (statistical, GIS-based, ML, Bayesian)
- Data inputs and feature engineering rules
- Spatial, temporal, and cultural constraints
- FAIR+CARE-compliant handling of sensitive landscapes
- Evaluation, uncertainty, and reproducibility rules
- Integration with STAC/DCAT, Neo4j, Story Nodes, and Focus Mode

Predictive models are **contextual**, not determinative.  
They support narrative understanding, not discovery of protected sites.

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/methods/
├── README.md
├── predictive_modeling.md            # This file
├── spatial-statistics.md
├── interaction-spheres.md
└── validation/
    └── README.md
````

Model code & data:

```text
src/pipelines/archaeology/predictive_modeling/
data/work/archaeology/predictive_modeling/
```

---

## 🧭 Modeling Goals

Predictive modeling supports:

* Landscape-scale probability of site presence
* Interaction sphere & corridor reconstruction
* Environmental affordance studies
* Scenario analysis for movement, settlement, and cultural geography
* Narrative enrichment for Story Nodes and Focus Mode

Explicitly excluded:

* Precise site prediction
* Any tool usable for unauthorized prospecting or looting
* Deterministic statements about Indigenous cultural behavior
* Any output violating CARE/sovereignty rules

---

## 📊 Data Inputs & Feature Engineering

### Environmental Predictors

* Elevation, slope, aspect, relative relief
* Distance to rivers, hydrology indices
* Soil class, drainage, fertility
* Vegetation / landcover (historical + modern)
* Climate (temperature, precip, drought indices)

### Cultural & Historical Predictors

* Known archaeological sites (generalized or masked)
* Trails, corridors, protohistoric routes
* Ethnohistoric territories
* Cultural landscape zones (Great Bend Aspect, Wichita, Plains Village)

### Feature Engineering Rules

* Transformations **must be logged** (`provenance/transformations-log.csv`).
* H3 generalization applied for sensitive inputs.
* Derived rasters must include STAC lineage and PROV-O links.

---

## ⚙️ Modeling Approaches

### 1️⃣ Heuristic Models

* Expert rule sets (buffers, ranges, thresholds)
* GIS operations (slope < X°, distance < Y km)
* Requires clear justification with citations or expert rationale

### 2️⃣ Statistical Models

* Logistic / GLM
* Inhomogeneous Poisson processes
* KDE & density surfaces
* Spatial autocorrelation diagnostics (Moran’s I)

### 3️⃣ Machine Learning

* Random forest, gradient boosting
* Elastic net / LASSO
* Simple neural nets with documented architecture
* Requires:

  * Explainability (SHAP, permutation importance)
  * Logged seeds, hyperparameters, configs
  * Stored evaluation splits

---

## 🧪 Training, Evaluation & Uncertainty

### Splits

* Spatial cross-validation preferred
* No co-located train/test leakage
* Declare geographic & temporal relevance bounds

### Metrics

* AUC, ROC, PR
* Calibration curves
* Spatial stratified accuracy
* Error surfaces preserved in STAC assets

### Uncertainty

* Surfaces must accompany predictions when possible
* Limitations section required in the model’s narrative report

---

## ⚖️ FAIR+CARE & Cultural Safety

Predictive modeling in archaeology comes with **high ethical risk**.
KFM enforces:

* Sensitive predictions must be **generalized** (H3 smoothing).
* No high-resolution “site likelihood” maps in public layers.
* Tribal partners may veto or revise outputs.
* All outputs must carry CARE labels and narrative warnings.
* Focus Mode must clearly distinguish:

  * **Model-derived inference**
  * **Archival / factual records**

CARE is **non-negotiable**.

---

## 🧠 Graph, Story Node & Focus Mode Integration

### Neo4j Graph

Predictive layers generate or link to:

* `Dataset` nodes
* Generalized `Place` nodes (H3-based)
* Modeling `Activity` nodes
* PROV-O relationships:

  * `prov:wasGeneratedBy`
  * `prov:used`

### Story Nodes

Predictive models contribute:

* Regional context surfaces
* Movement corridors
* Environmental affordance interpretation

Story Nodes treat predictive results as **interpretive**, not authoritative.

### Focus Mode

Focus Mode surfaces:

* Overlays with provenance chips
* Uncertainty + CARE warnings
* Narrative **Focus Summary** callouts, e.g.:

> **Focus Summary:**
> Late Prehistoric settlement likelihood is highest along terrace systems, but outputs are generalized and not suitable for locating specific sites.

---

## 🛰 STAC/DCAT Metadata & Provenance

All model outputs MUST be registered as STAC Items.

Example:

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "archaeology-predictive-late-prehistoric-v1",
  "properties": {
    "kfm:domain": "archaeology",
    "kfm:model_type": "predictive",
    "care:sensitivity": "generalized"
  },
  "assets": {
    "raster": {
      "href": "s3://kfm/arch/predictive/lp_model_v1.tif",
      "roles": ["data"]
    }
  }
}
```

Provenance recorded in:

* PROV-O graph
* transformations-log.csv
* STAC lineage fields

---

## 🧪 Reproducibility Requirements

* WAL → Retry → Rollback → Lineage compliance
* Full configuration snapshot logged
* All random processes seeded
* Deterministic pipeline runs
* Exact replayability required

Rollback triggers include:

* CARE violations
* Data errors
* Governance veto

---

## 🕰️ Version History

| Version | Date       | Author                            | Summary                                                                                       |
| ------: | ---------- | --------------------------------- | --------------------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology Working Group (Draft) | Initial predictive modeling framework for archaeology; aligned to KFM-MDP v11 rules and CARE. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Archaeology Methods · MCP-DL v6.3 Compatible · FAIR+CARE Governed
Predictive Modeling Methods (Draft v11.0.0)

</div>
