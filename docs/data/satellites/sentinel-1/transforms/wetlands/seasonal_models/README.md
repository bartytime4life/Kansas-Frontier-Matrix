---
title: "🌿 Sentinel-1 Wetlands — Seasonal Hydrology Models (Winter/Spring/Summer/Fall)"
path: "docs/data/satellites/sentinel-1/transforms/wetlands/seasonal_models/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity (CARE-B Ecohydrology)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · FAIR+CARE Council · Remote Sensing WG"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A2-I2-R4"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
risk_category: "High"
public_exposure_risk: "Medium"
redaction_required: true

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "Interval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-wetlands-seasonal-models-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-wetlands-seasonal-models-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-wetlands-seasonalmodels:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-wetlands-seasonalmodels"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/wetlands/seasonal_models/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon next seasonal hydrology model release"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌿 **Seasonal Wetness Models for Sentinel-1 Wetlands ETL**  
`docs/data/satellites/sentinel-1/transforms/wetlands/seasonal_models/`

Season-specific ecohydrology models informing wetness/saturation classification  
by providing **expected seasonal γ⁰ baselines**, **phenology-aware weighting**,  
and **hydrologic regime priors**.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/wetlands/seasonal_models/
├── 📄 README.md
│
├── 🌿 seasonal_model_2024.json      # Winter/Spring/Summer/Fall hydrology patterns for 2024
└── 🌿 seasonal_model_2025.json      # Updated ecohydrology priors for 2025
~~~

✔ Emoji BEFORE filenames  
✔ Exact alignment with wetlands/, flood/, deformation/, rtc/, radiometric/  
✔ Zero drift, zero omissions  
✔ Guaranteed box-safe  

---

## 📘 2. Purpose

Seasonal wetness models define **hydrologic expectations** for each season of the year:  

- Winter: frozen soils, low γ⁰ variability  
- Spring: high saturation, snowmelt, pooling  
- Summer: drying cycles, vegetation interference  
- Fall: transitional moistening, early-season pooling  

These priors help the wetlands ETL system differentiate between:

- actual wetness events  
- seasonal vegetation effects  
- agricultural cycles  
- ephemeral pooling  
- background hydrologic regimes  

---

## 🧩 3. Structure of Seasonal Model JSON

Each file must contain:

~~~json
{
  "year": 2025,
  "seasons": {
    "winter": {
      "expected_gamma0_drop": 1.5,
      "vegetation_weight": 0.1,
      "coherence_floor": 0.4
    },
    "spring": {
      "expected_gamma0_drop": 3.0,
      "vegetation_weight": 0.4,
      "coherence_floor": 0.25
    },
    "summer": {
      "expected_gamma0_drop": 0.9,
      "vegetation_weight": 0.6,
      "coherence_floor": 0.35
    },
    "fall": {
      "expected_gamma0_drop": 2.1,
      "vegetation_weight": 0.3,
      "coherence_floor": 0.30
    }
  }
}
~~~

Values define:

- expected γ⁰ depression relative to dry baseline  
- vegetation influence weighting  
- expected minimum coherence floor  
- seasonal hydrology priors  

These are used inside the wetlands transform to adjust classification thresholds.

---

## 🔗 4. PROV-O Lineage

Each seasonal model is registered as:

~~~json
{
  "prov:Entity": "wetland_seasonal_model_2025",
  "prov:label": "Seasonal Wetness Model (2025)",
  "kfm:care_label": "CARE-B",
  "kfm:provenance_type": "classifier-model"
}
~~~

This ensures full traceability across wetland STAC Items and downstream Focus Mode reasoning.

---

## 🔐 5. FAIR+CARE & Sovereignty Handling

Seasonal hydrology models:

- do **not** contain sensitive geometry  
- but influence sensitive wetland classifications  
- are therefore **CARE-B** by association  

They must:

- propagate `"kfm:care_label" = "CARE-B"`  
- remain immutable once versioned  
- be referenced in wetlands STAC Item metadata  

---

## 🧪 6. CI Validation Requirements

CI validates:

- schema correctness  
- complete coverage of four seasons  
- numeric sanity (no negative thresholds, NaNs, etc.)  
- reproducibility of classification results  
- correct governance metadata  
- compatibility with wetlands fusion logic  

Any failure blocks merge.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict seasonal-models README; emoji style preserved; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🔗 Coherence Fusion](../coherence_fusion/README.md) · [🛡 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

