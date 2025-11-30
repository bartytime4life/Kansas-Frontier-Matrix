---
title: "🧪 Sentinel-1 Wetlands QA — Test Suite (γ⁰ Wetness · Seasonal Models · Coherence Fusion)"
path: "docs/data/satellites/sentinel-1/qa/wetlands/tests/README.md"
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

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sentinel1-wetlands-qa-tests-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  owl_time: "Interval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../schemas/json/sentinel1-wetlands-qa-tests-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-wetlands-qa-tests-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-wetlands-tests:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-wetlands-tests"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/wetlands/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when wetlands QA standard updates"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Wetlands QA — Test Suite**  
`docs/data/satellites/sentinel-1/qa/wetlands/tests/`

Validates **γ⁰ wetness detection**, **seasonal hydrology models**,  
and **coherence-fusion behavior**, ensuring wetlands/saturation products  
are hydrologically correct, stable, deterministic, and sovereignty-safe.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/wetlands/tests/
├── 📄 README.md
│
├── 🌿 test_wetness_gamma0.py         # Wetness via γ⁰ depression (terrain-normalized)
├── 🌿 test_seasonal_models.py        # Seasonal hydrology model correctness (winter/spring/etc.)
└── 🌿 test_coherence_fusion.py       # Coherence → wetness fusion logic + weights
~~~

✔ Emojis BEFORE filenames  
✔ Exact match to flood/tests, coherence/tests, radiometry/tests, deformation/tests  
✔ Box-safe, zero drift  

---

## 📘 2. Purpose

Wetlands QA tests ensure that all **soil-moisture / wetness / saturation** layers  
produced from Sentinel-1 SAR obey:

- γ⁰ wetness physics  
- seasonal hydrology expectations  
- coherence-driven saturation signatures  
- DEM-aware hydrology  
- sovereignty-sensitive governance requirements  
- deterministic and reproducible ETL logic  

These layers drive:

- ecohydrology Story Nodes  
- Focus Mode v3 environmental reasoning  
- hydrologic change detection  
- wetlands STAC Items  
- risk assessments in sovereign/cultural hydroscapes  

---

## 🧩 3. Test Modules

### 🌿 `test_wetness_gamma0.py`
Validates:

- γ⁰ depression as wetness indicator  
- terrain normalization effects  
- vegetation–moisture separation  
- stable numeric ranges  
- agreement with `wetlands_reference.tif` (fixtures)  

---

### 🌿 `test_seasonal_models.py`
Ensures:

- correct seasonal hydrology priors  
- correct weighting of seasonal parameters  
- winter freeze vs. spring saturation correctness  
- schema-valid seasonal JSON files  
- matches `seasonal_model_reference.json`  

---

### 🌿 `test_coherence_fusion.py`
Checks:

- correct coherence weighting  
- correct application of fusion rules  
- distinction between flood decorrelation and wetness decorrelation  
- deterministic outputs across architectures  
- compatibility with `coherence_fusion_reference.json`  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Wetlands QA enforces:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true`  
- `"kfm:mask_required" = true"`  
- correct governance metadata propagation  
- full sovereignty readiness  

Wetlands crosscut **tribal ecological resources**,  
thus strict sovereignty protection is mandatory through QA → ETL → STAC.

---

## 🔗 5. PROV-O Lineage

Wetlands QA lineage is stored as:

~~~json
{
  "prov:Entity": "s1_wetlands_qa_validation",
  "prov:wasGeneratedBy": "s1_wetlands_qa_pipeline",
  "kfm:qa_type": "wetlands",
  "kfm:care_label": "CARE-B"
}
~~~

Each wetlands STAC Item includes this provenance entity.

---

## 🧪 6. CI Integration

CI validates:

- γ⁰ wetness behavior  
- seasonal-model logic  
- coherence fusion  
- DEM interactions  
- schema/SHACL correctness  
- fixture equivalence  
- governance metadata integrity  
- cross-platform determinism (CPU/GPU parity)  

Any mismatch → **CI BLOCK**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict wetlands-QA tests README; emoji prefix validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [📁 Fixtures](../fixtures/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

