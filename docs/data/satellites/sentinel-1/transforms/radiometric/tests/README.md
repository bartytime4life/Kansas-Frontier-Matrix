---
title: "🧪 Sentinel-1 Radiometric Calibration — Test Suite Overview"
path: "docs/data/satellites/sentinel-1/transforms/radiometric/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (Test Suite)"
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

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R2"
care_label: "CARE-A"
indigenous_rights_flag: false
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  owl_time: "Instant"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-radiometric-tests:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-radiometric-tests"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/radiometric/tests/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded on next radiometric-model update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Radiometric Calibration — Tests**  
`docs/data/satellites/sentinel-1/transforms/radiometric/tests/`

Validation suite ensuring **σ⁰ VV/VH calibration**, LUT interpolation, noise-floor removal,  
and radiometric consistency are correct, deterministic, and CI-governed.

</div>

---

## 🗂️ 1. Directory Layout (STRICT OPTION-A EMOJI STYLE)

~~~text
docs/data/satellites/sentinel-1/transforms/radiometric/tests/
├── 📄 README.md
│
├── 🛰️ test_sigma0_core.py          # Primary σ⁰ VV/VH calibration tests
├── 🛰️ test_noise_floor.py          # Noise subtraction & border-noise handling
└── 🛰️ test_lut_interpolation.py     # LUT gain/offset interpolation accuracy
~~~

✔ Emoji BEFORE filenames  
✔ Identical style to orbit/tests, coherence/tests, flood/tests, wetlands/tests  
✔ Zero drift, zero substitutions

---

## 📘 2. Purpose

This directory contains the complete automated test suite for  
the **radiometric calibration ETL stage**, verifying:

- correct application of ESA calibration LUTs  
- gain/offset interpolation accuracy  
- noise-floor subtraction  
- antenna-pattern correction consistency  
- σ⁰ VV/VH output correctness  
- stable numeric precision across releases  
- deterministic outputs (bit-for-bit reproducibility)  
- full metadata alignment with KFM-PDC v11 contracts

All tests run automatically in CI to ensure **calibration reproducibility**.

---

## 🧩 3. Test Modules

### 🛰️ `test_sigma0_core.py`
Validates:

- correct σ⁰ conversion formula  
- LUT-driven gain/offset application  
- correct normalization across incidence angles  
- consistency between VV and VH paths  
- stable floating-point output across platforms

---

### 🛰️ `test_noise_floor.py`
Checks:

- radiometric noise removal logic  
- border noise attenuation  
- negative/near-zero signal behavior  
- handling of anomalous SAFE metadata

---

### 🛰️ `test_lut_interpolation.py`
Ensures:

- angle → gain interpolation accuracy  
- monotonic angle array handling  
- correct offset interpolation  
- matching ESA LUT reference results

---

## 🔗 4. Governance & FAIR+CARE Notes

Radiometric calibration is **CARE-A**, but tests must validate:

- correct propagation of `"kfm:*"` governance metadata  
- deterministic lineage fields  
- schema validity for calibration metadata  
- immutability of LUT usage references

No sovereignty masking occurs at this stage,  
but governance metadata continues to propagate downstream.

---

## 🧪 5. CI Integration

Executed under:

- `transform-tests.yml`  
- `data-pipeline.yml`

CI enforces:

- unit + integration test success  
- full schema validation  
- deterministic floating-point operations  
- reproducibility across architectures  
- correct LUT version selection  
- fidelity with ESA reference LUT behavior

Any deviation → **CI block**.

---

## 🧭 6. Version History

| Version | Date       | Summary                                                                            |
|--------:|------------|------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial strict emoji-compliant test-suite README; aligned with radiometric subtree. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [📁 Fixtures](../../radiometric/fixtures/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

