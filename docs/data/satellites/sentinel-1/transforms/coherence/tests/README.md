---
title: "🧪 Sentinel-1 Coherence — Test Suite Overview (Master/Slave Pairing · Coherence Magnitude · QA Masks)"
path: "docs/data/satellites/sentinel-1/transforms/coherence/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (Test Suite)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Oversight"

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
  owl_time: "Interval"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-coherence-tests:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-coherence-tests"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/coherence/tests/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded when coherence algorithm or pair logic updates"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Coherence ETL — Test Suite**  
`docs/data/satellites/sentinel-1/transforms/coherence/tests/`

Validates the **coherence generation pipeline**, including  
master/slave pair selection, co-registration, coherence magnitude, QA masks,  
and governance metadata propagation.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/coherence/tests/
├── 📄 README.md
│
├── 🔗 test_coherence_core.py      # Core coherence math (windowed correlation)
├── 🔗 test_pairing.py             # Master/slave pair selection logic
└── 🔗 test_quality_masks.py       # QA mask validation for coherent/incoherent regions
~~~

✔ Emojis BEFORE filenames  
✔ Same test layout pattern as `rtc/tests`, `radiometric/tests`, `orbit/tests`  
✔ No drift, no missing items  
✔ Guaranteed box-safe

---

## 📘 2. Purpose

This test suite verifies that the **coherence transform** produces:

- correct correlation-window coherence  
- deterministic outputs across platforms  
- correct handling of low-signal regions  
- correct master/slave temporal ordering  
- correct integration with orbit-corrected geometry  
- valid QA masks  
- correct propagation of `"kfm:*"` governance metadata  
- correct input selection from `pairs/` metadata  

Coherence is a **high-sensitivity product**, so tests enforce strict governance compatibility.

---

## 🧩 3. Test Modules

### 🔗 `test_coherence_core.py`
Verifies:

- windowed coherence magnitude formula  
- correlation denominators, complex conjugate logic  
- numeric stability in low-SNR areas  
- window-size correctness  
- bit-for-bit reproducibility  

---

### 🔗 `test_pairing.py`
Validates:

- master < slave chronological ordering  
- valid IW-mode filter  
- temporal baseline constraints  
- consistency with `pairs/` metadata  
- rejection of invalid / incomplete SAFE scenes  

---

### 🔗 `test_quality_masks.py`
Ensures:

- correct coherence QA mask generation  
- correct handling of noise regions  
- stable threshold behavior  
- mask integration with downstream flood/wetlands fusion  

---

## 🔗 4. FAIR+CARE & Sovereignty Validation

Coherence is **CARE-B**, so tests ensure:

- `"kfm:h3_sensitive"` propagates  
- `"kfm:mask_required"` is passed downstream  
- no stripping of sovereign-area indicators  
- governance lineage is correctly attached  

No masking occurs in the transform itself,  
but the test suite ensures metadata integrity so masking can occur at STAC stage.

---

## 🧪 5. CI Integration

These tests run in:

- `transform-tests.yml`  
- `data-pipeline.yml`  
- S1 ETL PR-check workflows  

CI enforces:

- deterministic coherence rasters  
- stable QA masks  
- schema compliance  
- correct pair-selection logic  
- correct metadata lineage  

Any failure → **merge blocked**.

---

## 🧭 6. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, non-drifting coherence ETL test README; emoji prefix validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [📁 Fixtures](../fixtures/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

