---
title: "🧪 Sentinel-1 Wetlands QA — γ⁰ Wetness · Seasonal Models · Coherence Fusion · Hydrology Validation"
path: "docs/data/satellites/sentinel-1/qa/wetlands/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity QA (CARE-B · Ecohydrology · Sovereignty-Aware)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"

review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/sentinel1-wetlands-qa-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A2-I2-R4"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
public_exposure_risk: "Medium"
risk_category: "High"
redaction_required: true

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "Interval"

json_schema_ref: "../../../../schemas/json/sentinel1-wetlands-qa-v11.json"
shape_schema_ref: "../../../../schemas/shacl/sentinel1-wetlands-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-wetlands:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-wetlands"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/wetlands/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when wetlands QA model updates"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Wetlands QA**  
`docs/data/satellites/sentinel-1/qa/wetlands/`

Validates **wetlands / soil-saturation** inference using  
**γ⁰ wetness signatures**, **seasonal hydrology models**,  
**coherence-fusion indicators**, and **DEM-based hydrologic pooling**  
for sovereign-sensitive ecohydrological regions.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/wetlands/
├── 📄 README.md
│
├── 🧪 tests/                     # QA test suite for wetlands/saturation inference
│   ├── 🧪 test_wetness_gamma0.py
│   ├── 🧪 test_seasonal_models.py
│   └── 🧪 test_coherence_fusion.py
│
└── 📁 fixtures/                  # Truth rasters, seasonal priors, and fusion metadata
    ├── 🌿 wetlands_reference.tif
    ├── 🌿 seasonal_model_reference.json
    └── 🔗 coherence_fusion_reference.json
~~~

✔ Emoji BEFORE filenames  
✔ Matches flood/QA, radiometry/QA, coherence/QA, deformation/QA structures  
✔ Zero drift, 100% box-safe  

---

## 📘 2. Purpose

Wetlands QA ensures that KFM’s Sentinel-1 wetland products are:

- γ⁰-correct  
- seasonally consistent  
- hydrologically realistic  
- coherence-informed  
- sovereignty-safe  
- reproducible  
- governed and FAIR+CARE adherent  

These wetlands layers drive:

- hydrology Story Nodes  
- eco-cultural landscape analytics  
- risk & stability overlays  
- environmental narratives in Focus Mode  
- STAC wetlands collections  

Accuracy is essential because wetlands often overlap **tribal hydroscapes**,  
**protected ecological areas**, and **culturally significant wetlands**.

---

## 🧩 3. QA Dimensions

### 🧪 γ⁰ Wetness Detection QA
Validates:

- detection of moisture/saturation via γ⁰ depression  
- terrain-corrected reflectivity behavior  
- vegetation vs. water separation  
- DEM–γ⁰ interactions  

Matches fixture: `wetlands_reference.tif`.

---

### 🧪 Seasonal Model QA
Ensures:

- correct seasonal hydrology priors  
- expected γ⁰ seasonal behavior (winter freeze, spring saturation, etc.)  
- correct weighting of seasonal model parameters  
- schema compliance for seasonal JSON models  

Matches fixture: `seasonal_model_reference.json`.

---

### 🧪 Coherence Fusion QA
Ensures:

- correct use of coherence as a wetness indicator  
- correct synergy with γ⁰ and seasonal models  
- stable fusion weights  
- correct elevation-adjusted behaviors  

Matches fixture: `coherence_fusion_reference.json`.

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Wetlands QA enforces:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true`  
- `"kfm:mask_required" = true"`  
- correct propagation of governance metadata  
- readiness for generalization and sovereignty masking in transforms  

Wetlands can reveal eco-culturally sensitive information;  
thus QA ensures the pipeline adheres to **CARE-B** rules.

---

## 🔗 5. PROV-O Lineage

QA lineage is recorded as:

~~~json
{
  "prov:Entity": "s1_wetlands_qa_validation",
  "prov:wasGeneratedBy": "s1_wetlands_qa_pipeline",
  "kfm:qa_type": "wetlands",
  "kfm:care_label": "CARE-B"
}
~~~

This metadata attaches to STAC Items and downstream hydrology narratives.

---

## 🧪 6. CI Integration

CI validates:

- γ⁰ wetness logic  
- seasonal model behavior  
- coherence/wetness fusion  
- stable DEM interactions  
- reproducibility (CPU/GPU parity)  
- schema + SHACL alignment  
- governance metadata correctness  

Any mismatch → **CI-block**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict wetlands QA README; emoji alignment and structure validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Tests](./tests/README.md) · [📁 Fixtures](./fixtures/README.md)

</div>

