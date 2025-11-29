---
title: "🧪 Sentinel-1 Orbit Correction — Tests Overview"
path: "docs/data/satellites/sentinel-1/transforms/orbit/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Remote Sensing WG"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"

fair_category: "F1-A1-I1-R2"
care_label: "CARE-A"
indigenous_rights_flag: false
sensitivity_level: "Low"
risk_category: "Low"
public_exposure_risk: "Low"
redaction_required: false

doc_uuid: "urn:kfm:doc:data:sentinel1:transforms:orbit:tests:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-orbit-tests"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/orbit/tests/README.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "36 months"
sunset_policy: "Superseded on next orbit-model revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Orbit Transform — Test Suite**  
`docs/data/satellites/sentinel-1/transforms/orbit/tests/`

Tests validating state-vector interpolation, Doppler centroid modeling, SAFE/orbit alignment,  
and all deterministic geometry outputs for the orbit-correction transform.

</div>

---

## 🗂️ Directory Layout (STRICT OPTION-A EMOJI STYLE)

~~~text
docs/data/satellites/sentinel-1/transforms/orbit/tests/
├── 📄 README.md
│
├── 🔧 test_orbit_basic.py
├── 🔧 test_doppler.py
└── 🔧 test_state_vectors.py
~~~

**No drift.  
No lost emojis.  
Folder tree exactly matches the established STAC + transforms directory style.**

---

## 📘 1. Purpose

This directory contains **all unit + integration tests** for the Sentinel-1 orbit-correction stage.  
These tests guarantee:

- deterministic orbit correction  
- exact matching of ESA orbit-state vector expectations  
- correct Doppler centroid calculation  
- SAFE metadata ↔ orbit-file timestamp agreement  
- reproducible geometry preparation for downstream RTC, coherence, flood, wetlands, and deformation ETL

---

## 🧩 2. Test Coverage

### 🔧 `test_orbit_basic.py`
Validates fundamental orbit-correction behaviors:

- orbit file selection priority (POEORB → RESORB)  
- timestamp alignment  
- interpolation correctness  
- proper error handling for malformed metadata  

### 🔧 `test_doppler.py`
Ensures Doppler centroid (`f_dc`) modeling is:

- mathematically correct  
- continuous across bursts  
- aligned with ESA’s IW burst timing rules  

### 🔧 `test_state_vectors.py`
Verifies:

- interpolation accuracy of state vectors  
- monotonic timing  
- correct forward/backward propagation  
- consistency with KFM projection parameters  

---

## 🔗 3. Governance & FAIR+CARE Considerations

Orbit transforms are **CARE-A** and do not contain sensitive content.  
However tests MUST:

- preserve `"kfm:*"` metadata fields when validating transform outputs  
- check correct propagation of governance metadata to downstream stages  
- validate PROV-O activity generation where required  

---

## 🧪 4. How CI Runs These Tests

These tests are executed in:

- `transform-tests.yml`  
- `data-pipeline.yml`  
- PR checks for **sentinel-1 ETL** changes

CI enforces:

- deterministic output  
- stable numerical precision  
- reproducible Doppler modeling  
- alignment with SAFE metadata parsing rules  
- correct JSON schema output  

Failures → **block merge**.

---

## 🧭 5. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial test-suite README using strict emoji Option-A style. Zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [📁 Fixtures](../fixtures/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

