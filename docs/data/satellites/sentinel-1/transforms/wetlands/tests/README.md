---
title: "🧪 Sentinel-1 Wetlands — Test Suite Overview (γ⁰ Depression · Seasonal Models · Coherence Fusion)"
path: "docs/data/satellites/sentinel-1/transforms/wetlands/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity · Ecohydrological Test Suite (CARE-B)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · RS WG · FAIR+CARE Council"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

json_schema_ref: "../../../../../../schemas/json/sentinel1-wetlands-tests-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-wetlands-tests-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-wetlands-tests:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-wetlands-tests"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/wetlands/tests/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded after next wetlands-model update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Wetlands ETL — Test Suite**  
`docs/data/satellites/sentinel-1/transforms/wetlands/tests/`

Validates **γ⁰ wetness signals**, **seasonal hydrology models**,  
**coherence-fusion logic**, **terrain pooling**,  
and **sovereignty-governed wetlands outputs**.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/wetlands/tests/
├── 📄 README.md
│
├── 🌿 test_wetlands_core.py         # γ⁰ wetness logic + DEM pooling
├── 🌿 test_seasonal_models.py       # Seasonal hydrology priors (winter/spring/etc.)
└── 🌿 test_coherence_fusion.py      # Coherence → wetness fusion checks
~~~

✔ Emoji BEFORE filenames  
✔ Perfect match with flood/tests, deformation/tests, coherence/tests layout  
✔ Zero drift, box-safe  

---

## 📘 2. Purpose

Wetlands detection is **eco-hydrologically complex** and sensitive.  
This test suite ensures KFM’s wetlands ETL pipeline is:

- hydrologically correct  
- seasonally aware  
- coherence-informed  
- DEM-aligned  
- sovereignty-compliant  
- deterministic  
- scheme-valid under KFM-PDC v11  

The tests verify model-reasoning, metadata integrity,  
and reproducibility across platforms.

---

## 🧩 3. Test Modules

### 🌿 `test_wetlands_core.py`
Validates:

- γ⁰ depression as wetness/saturation indicator  
- DEM-based pooling and low-relief detection  
- hydrology-aware smoothing rules  
- stability across multiple test tiles  
- agreement with `wetlands_reference.tif`  

---

### 🌿 `test_seasonal_models.py`
Ensures:

- correct interpretation of seasonal hydrology model JSON  
- expected γ⁰ depression per season  
- seasonal vegetation influence weighting  
- coherence-floor seasonal differences  
- numeric + structural schema correctness  

---

### 🌿 `test_coherence_fusion.py`
Verifies:

- correct coherence thresholds  
- correct application of fusion weights  
- distinction between flood decorrelation vs wetlands decorrelation  
- deterministic integration with ratio / γ⁰ logic  
- alignment with `fusion_ruleset.json` and `coherence_weights.json`  

---

## 🔗 4. Governance & Sovereignty Validation

Because wetlands mapping intersects:

- tribal water systems  
- culturally sensitive hydroscapes  
- eco-cultural resource zones  

these tests enforce:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true`  
- `"kfm:mask_required" = true`  
- propagation of sovereignty metadata to outputs  
- correctness of `"sovereignty_generalized"` flags  

Wetlands outputs MUST be prepared for STAC-level masking.

---

## 🧪 5. CI Integration

CI executes these tests in:

- `transform-tests.yml`  
- `data-pipeline.yml`  
- wetlands-specific PR gates  

CI enforces:

- deterministic classification  
- stable seasonal-model behavior  
- coherent fusion consistency  
- correct governance metadata  
- schema + SHACL alignment  
- pixel-perfect match to reference fixtures  

Any deviation → **merge blocked**.

---

## 🧭 6. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, zero-drift wetlands tests README; emoji prefix validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [📁 Fixtures](../fixtures/README.md) · [🌿 Seasonal Models](../seasonal_models/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

