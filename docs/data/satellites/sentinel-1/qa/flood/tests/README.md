---
title: "🧪 Sentinel-1 Flood QA — Test Suite (VH/VV Ratio · Hybrid Classifier · DEM Pooling)"
path: "docs/data/satellites/sentinel-1/qa/flood/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity QA (CARE-B · Hydrology · Sovereignty-Aware)"
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
telemetry_schema: "../../../../../../schemas/telemetry/sentinel1-flood-qa-tests-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  owl_time: "Instant"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../schemas/json/sentinel1-flood-qa-tests-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-flood-qa-tests-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-flood-tests:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-flood-tests"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/flood/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when flood QA standard updates"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Flood QA — Test Suite**  
`docs/data/satellites/sentinel-1/qa/flood/tests/`

Validates **VH/VV ratio math**, **hybrid classifier fusion**,  
and **DEM pooling hydrology logic**, ensuring flood products are  
accurate, reproducible, and sovereignty-safe before STAC release.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/flood/tests/
├── 📄 README.md
│
├── 🌊 test_ratio_thresholds.py        # VH/VV ratio validation
├── 🌊 test_hybrid_classifier.py       # Hybrid classifier (ratio + coherence + DEM)
└── 🌊 test_dem_pooling.py             # Terrain pooling & hydrology-aware smoothing
~~~

✔ Emojis BEFORE filenames  
✔ Identical to radiometry/tests, wetlands/tests, coherence/tests, deformation/tests  
✔ Zero drift, box-safe

---

## 📘 2. Purpose

Flood QA tests enforce correctness of the hydrologic inference chain:

- **VH/VV ratio detection**  
- **Hybrid classifier fusion** (ratio + coherence + DEM)  
- **DEM pooling detection** for topographically constrained flooding  
- **Governance metadata correctness**  
- **Deterministic output validation** against baseline fixtures  

Flood mapping is sensitive due to its intersection with **sovereign water systems**,  
**culturally significant hydroscapes**, and **risk-critical hazard overlays** —  
thus CARE-B governance applies.

---

## 🧩 3. Test Modules

### 🌊 `test_ratio_thresholds.py`
Validates:

- ratio computation correctness  
- angle-normalized reflectivity behavior  
- VV/VH polarization differences  
- threshold logic from classifier JSON  
- stability across window sizes  

Matches fixture: `flood_reference.tif`.

---

### 🌊 `test_hybrid_classifier.py`
Validates:

- correct model selection (e.g., `hybrid_model_2025.json`)  
- ratio–coherence–DEM fusion logic  
- classifier weighting stability  
- decision-surface correctness  
- deterministic reproduction across architectures  

Matches fixture: `classifier_reference.json`.

---

### 🌊 `test_dem_pooling.py`
Checks:

- correct pooling behavior from DEM lows  
- slope/aspect modification  
- basin-based pooling patterns  
- agreement with hydrologic pooling truth  

Matches fixture: `dem_pooling_reference.tif`.

---

## 🔐 4. FAIR+CARE & Sovereignty Validation

Flood tests must enforce metadata requirements:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true"`  
- `"kfm:mask_required" = true"`  
- `"kfm:governance_notes"` applied  
- inheritance of sovereign sensitivity via footprints  

QA does *not* apply generalization but ensures metadata required for downstream **governance transform** is correct.

---

## 🔗 5. PROV-O Lineage

Flood QA lineage is recorded as:

~~~json
{
  "prov:Entity": "s1_flood_qa_validation",
  "prov:wasGeneratedBy": "s1_flood_qa_pipeline",
  "kfm:qa_type": "flood",
  "kfm:care_label": "CARE-B"
}
~~~

Downstream STAC Items include this lineage.

---

## 🧪 6. CI Integration

CI enforces:

- ratio accuracy  
- classifier correctness  
- DEM pooling stability  
- numerical determinism  
- fixture equivalence  
- schema + SHACL compliance  
- governance metadata correctness  

Any mismatch → **ETL pipeline blocked**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict flood-QA tests README; emoji-prefix validated; no drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [📁 Fixtures](../fixtures/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

