---
title: "🧪 Sentinel-1 Flood QA — Hydrology Validation (VH/VV Ratio · Hybrid Classifier · DEM Pooling · Coherence Fusion)"
path: "docs/data/satellites/sentinel-1/qa/flood/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity QA (CARE-B · Sovereignty-Influenced)"
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
telemetry_schema: "../../../../schemas/telemetry/sentinel1-flood-qa-v11.json"

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
  owl_time: "Instant"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../schemas/json/sentinel1-flood-qa-v11.json"
shape_schema_ref: "../../../../schemas/shacl/sentinel1-flood-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-flood:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-flood"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/flood/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when flood QA models update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Flood QA**  
`docs/data/satellites/sentinel-1/qa/flood/`

Validates Sentinel-1 flood detection products:  
**VH/VV ratio**, **hybrid classifier**, **DEM pooling**,  
**coherence fusion**, and **sovereignty-safe hydrology output rules**.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/flood/
├── 📄 README.md
│
├── 🧪 tests/                     # Flood QA unit + integration tests
│   ├── 🧪 test_ratio_thresholds.py
│   ├── 🧪 test_hybrid_classifier.py
│   └── 🧪 test_dem_pooling.py
│
└── 📁 fixtures/                  # Reference flood masks, pooling maps, classifier truth
    ├── 🌊 flood_reference.tif
    ├── 🏞️ dem_pooling_reference.tif
    └── 📄 classifier_reference.json
~~~

✔ Emoji BEFORE filenames  
✔ Perfect alignment with all other QA fixture/test structures  
✔ 100% box-safe  

---

## 📘 2. Purpose

Flood QA ensures that flood products used in:

- hydrology modeling  
- emergency-aware overlays  
- Story Node v3 hydrological chains  
- Focus Mode environmental context  
- STAC flood Items  

are **correct, stable, reproducible, and sovereignty-safe.**

---

## 🧩 3. QA Dimensions

### 🧪 VH/VV Ratio QA
Checks:

- correct ratio math  
- expected VV stability vs VH attenuation  
- ratio-based threshold behavior  
- angle-normalized comparisons  
- masking/QA propagation  

### 🧪 Hybrid Classifier QA
Ensures:

- correct fusion of ratio + coherence + DEM  
- correct model selection (`hybrid_model_xxxx.json`)  
- classifier confidence scores  
- deterministic classification result  
- agreement with `classifier_reference.json`

### 🧪 DEM Pooling QA
Validates:

- accurate pooling-area detection  
- DEM slope/aspect influence on pooling  
- correct behavior for hydrologic basins  
- match with `dem_pooling_reference.tif`  

Flood pooling is crucial for:

- flood-risk narratives  
- hydrologic pathway simulation  
- hazard models  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Flood layers are **CARE-B** because floods frequently intersect:

- sovereign waters and wetlands  
- culturally important river corridors  
- hydrologic features used in traditional practices  

QA must enforce:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true`  
- `"kfm:mask_required" = true`  
- correct `"governance_notes"`  
- readiness for downstream generalization  

Flood QA does **not** apply generalization;  
it verifies metadata required for governance transforms later.

---

## 🔗 5. PROV-O Lineage

QA outputs attach governance lineage:

~~~json
{
  "prov:Entity": "s1_flood_qa",
  "prov:wasGeneratedBy": "s1_flood_qa_pipeline",
  "kfm:qa_type": "flood",
  "kfm:care_label": "CARE-B"
}
~~~

---

## 🧪 6. CI Integration

CI validates:

- ratio thresholds  
- hybrid model logic  
- DEM pooling surfaces  
- comparison against all fixtures  
- metadata correctness  
- schema + SHACL compliance  
- deterministic reproducibility across platforms  

Any mismatch → **pipeline blocked**.

---

## 🧭 7. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.2.2 | 2025-11-29 | Initial strict flood QA README; emoji alignment verified; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Tests](./tests/README.md) · [📁 Fixtures](./fixtures/README.md)

</div>

