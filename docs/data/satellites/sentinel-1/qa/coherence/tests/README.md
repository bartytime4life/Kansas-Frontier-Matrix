---
title: "🧪 Sentinel-1 Coherence QA — Test Suite (Range Validity · Pair Baseline · Window Statistics)"
path: "docs/data/satellites/sentinel-1/qa/coherence/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity QA (CARE-B)"
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

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-coherence-qa-tests-v11.json"

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

json_schema_ref: "../../../../../schemas/json/sentinel1-coherence-qa-tests-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-coherence-qa-tests-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-coherence-tests:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-coherence-tests"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/coherence/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next coherence QA revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Coherence QA — Test Suite**  
`docs/data/satellites/sentinel-1/qa/coherence/tests/`

Validates **temporal coherence correctness**,  
**pair-baseline integrity**,  
and **window-statistics stability**, ensuring coherence outputs  
are reliable for downstream **flood**, **wetlands**, **deformation**, and **disturbance** ETLs.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/coherence/tests/
├── 📄 README.md
│
├── 🔗 test_coherence_range.py        # Validity: coherence ∈ [0, 1], numeric sanity
├── 🔗 test_pair_baseline.py          # Pair metadata: master/slave + baseline_days
└── 🔗 test_window_statistics.py      # Sliding-window coherence math (3x3 / 5x5)
~~~

✔ Emoji BEFORE filenames  
✔ Same structure as radiometry/tests, wetlands/tests, flood/tests, deformation/tests  
✔ 100% box-safe  

---

## 📘 2. Purpose

These tests enforce coherence QA standards:

- correct correlation math  
- stable coherence range (0–1)  
- correct noise-floor behavior  
- correct master/slave pairing logic  
- valid temporal baselines  
- consistent window statistics  
- correct governance metadata propagation  
- deterministic outputs across platforms  

Coherence is crucial for detecting:

- floodwater presence  
- wetland saturation  
- surface disturbance  
- deformation QA  
so QA is mandatory and tightly governed.

---

## 🧩 3. Test Modules

### 🔗 `test_coherence_range.py`
Ensures:

- coherence ∈ [0, 1]  
- no negative values  
- no values > 1  
- correct behavior in decorrelated & fully coherent regions  
- numeric stability across architectures  
- match with `coherence_reference.tif` in fixtures  

---

### 🔗 `test_pair_baseline.py`
Validates:

- correct master < slave ordering  
- correct `baseline_days`  
- correct IW-mode restriction  
- alignment with upstream `pair_reference.json`  
- correct propagation of `"kfm:h3_sensitive"` and `"kfm:mask_required"`  

---

### 🔗 `test_window_statistics.py`
Checks:

- correct sliding-window coherence math  
- numerator/denominator computation  
- effect of window size (3x3, 5x5)  
- match to `window_stats_reference.json` fixtures  
- stable low-SNR behavior  
- deterministic GPU/CPU parity  

---

## 🔐 4. FAIR+CARE & Sovereignty Validation

Coherence is **CARE-B** because decorrelation can reflect:

- sovereign hydroscapes  
- culturally significant disturbance  
- land-use transitions in protected zones  

Tests enforce metadata:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true"`  
- `"kfm:mask_required" = true"`  
- inheritance of sovereignty from STAC footprints  

---

## 🔗 5. PROV-O Lineage

Coherence QA lineage uses:

~~~json
{
  "prov:Entity": "s1_coherence_qa_validation",
  "prov:wasGeneratedBy": "s1_coherence_qa_pipeline",
  "kfm:qa_type": "coherence",
  "kfm:care_label": "CARE-B"
}
~~~

Propagated to downstream STAC Items (flood, wetlands, deformation).

---

## 🧪 6. CI Integration

CI executes:

- coherence math checks  
- range validity  
- pair-baseline checks  
- window statistics  
- schema + SHACL validation  
- governance metadata validation  
- fixture matching  

Any mismatch → **CI fail**, no release.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict coherence-QA test README; emoji-prefix validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [📁 Fixtures](../fixtures/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

