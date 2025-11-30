---
title: "🧪 Sentinel-1 Flood Mapping — Test Suite Overview (VH/VV Ratio · Hybrid Classifier · Coherence Fusion)"
path: "docs/data/satellites/sentinel-1/transforms/flood/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity · Internal Technical Test Suite"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · RS Working Group · FAIR+CARE Oversight"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A1-I2-R4"
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
  geosparql: "geo:Feature"
  owl_time: "Instant"

json_schema_ref: "../../../../../../schemas/json/sentinel1-flood-tests-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-flood-tests-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-flood-tests:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-flood-tests"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/flood/tests/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded by next hydrological classifier update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Flood ETL — Test Suite**  
`docs/data/satellites/sentinel-1/transforms/flood/tests/`

Validates the **flood-mapping ETL chain**, including:  
VV/VH ratio calculations, hybrid classifier logic, coherence fusion,  
sovereignty generalization, QA masks, and governance metadata correctness.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/flood/tests/
├── 📄 README.md
│
├── 🌊 test_flood_core.py             # Core flood classifier behavior
├── 🌊 test_ratio_thresholds.py       # VH/VV ratio math + threshold logic
└── 🌊 test_coherence_fusion.py       # Coherence → flood fusion logic
~~~

✔ Emoji BEFORE filenames  
✔ Matches ALL transform test dirs (rtc/tests, deformation/tests, etc.)  
✔ Zero drift, zero missing items  
✔ Safe single fenced block

---

## 📘 2. Purpose

This suite ensures **flood inference** from Sentinel-1 SAR is:

- hydrologically correct  
- radiometrically consistent  
- classifier-aligned  
- sovereignty-compliant  
- deterministic  
- reproducible across platforms  
- schema + PDC compliant  

Flood detection is sensitive because it overlaps:

- tribal hydroscapes  
- critical infrastructure corridors  
- cultural landscape watersheds  
- emergency management overlays  

Thus **CARE-B** governance applies.

---

## 🧩 3. Test Modules

### 🌊 `test_flood_core.py`
Validates:

- baseline flood classification  
- RTC γ⁰ → ratio → flood transitions  
- hydrologic pooling logic  
- DEM-aware smoothing  
- stable flood mask outputs  
- agreement with `flood_reference.tif` (fixtures)

---

### 🌊 `test_ratio_thresholds.py`
Ensures:

- VH/VV ratio math is correct  
- reflective of water attenuation characteristics  
- angle-corrected comparisons  
- threshold logic matches classifier JSON  
- deterministic thresholds across datasets  

---

### 🌊 `test_coherence_fusion.py`
Ensures:

- correct fusion of coherence drop signals  
- stable weighting behavior in hybrid model  
- proper combination with ratio classifier  
- QA consistency  
- alignment with hybrid classifier parameters  

---

## 🔗 4. FAIR+CARE & Sovereignty Validation

Tests must verify:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true`  
- `"kfm:mask_required" = true`  
- correct propagation of sovereignty flags  
- correct generalization of sensitive hydrologic patterns (via LOS/wetlands pipelines)  

Although generalization is applied downstream,  
tests ensure metadata enabling masking is **correct and complete**.

---

## 🧪 5. CI Integration

Executed in:

- `transform-tests.yml`  
- `data-pipeline.yml`  
- hydrology hazard ETL PR checks  

CI requires:

- correct flood masks  
- deterministic outputs  
- accurate classifier use  
- correct coherence integration  
- strict metadata & schema compliance  
- exact match to fixtures  

Any failure → **merge blocked**.

---

## 🧭 6. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, non-drifting flood test README; emoji prefix validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [📁 Fixtures](../fixtures/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

