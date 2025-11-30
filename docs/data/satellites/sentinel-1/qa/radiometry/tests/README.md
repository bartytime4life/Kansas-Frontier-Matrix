---
title: "🧪 Sentinel-1 Radiometry QA — Test Suite (σ⁰ Calibration · γ⁰ RTC Consistency · DEM & Incidence Alignment)"
path: "docs/data/satellites/sentinel-1/qa/radiometry/tests/README.md"
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
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-radiometry-qa-tests-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  geosparql: "geo:Feature"
  owl_time: "Instant"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-radiometry-tests:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-radiometry-tests"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/radiometry/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when radiometry QA standards update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Radiometry QA — Test Suite**  
`docs/data/satellites/sentinel-1/qa/radiometry/tests/`

Validates **σ⁰ calibration**, **γ⁰ terrain normalization**,  
and **DEM/incidence-angle alignment** to guarantee stable,  
FAIR+CARE-safe radiometric foundations for all downstream S1 products.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/radiometry/tests/
├── 📄 README.md
│
├── 🧪 test_sigma0_calibration.py        # σ⁰ VV/VH calibration QA
├── 🧪 test_rtc_gamma0_consistency.py    # γ⁰ terrain normalization + RTC QA
└── 🧪 test_dem_incidence_alignment.py   # DEM + incidence-angle alignment QA
~~~

✔ Emojis BEFORE filenames  
✔ Exact match to radiometry/, wetlands/tests, flood/tests, deformation/tests  
✔ 100% box-safe

---

## 📘 2. Purpose

These tests ensure Sentinel-1 **radiometric foundations** are correct before  
any product enters flood, wetlands, coherence, or deformation pipelines.

Radiometry QA tests validate:

- correct use of calibration LUTs  
- correct σ⁰ computation  
- correct DEM-aware RTC γ⁰ normalization  
- correct incidence-angle usage  
- correct projection (EPSG:32614)  
- correct slope/aspect handling  
- absence of numeric drift or artifacts  

---

## 🧩 3. Test Modules

### 🧪 `test_sigma0_calibration.py`
Checks:

- calibration constant correctness  
- sensor noise-floor behavior  
- VV/VH parity  
- slant-range → ground-range geometry  
- stable σ⁰ value ranges  

---

### 🧪 `test_rtc_gamma0_consistency.py`
Validates:

- RTC γ⁰ computation correctness  
- DEM slope/aspect dependency  
- terrain normalization math  
- orthorectification + warp fidelity  
- consistent γ⁰ distribution (bit-exact when deterministic)  
- matches reference `gamma0_reference_vv.tif`

---

### 🧪 `test_dem_incidence_alignment.py`
Ensures:

- correct incidence-angle derivation  
- correct DEM alignment to burst geometry  
- no spatial drift  
- correct DEM → angle coupling  
- expected match with fixture metadata  
- stable geometry across test scenes  

---

## 🔐 4. FAIR+CARE & Sovereignty QA Rules

Even though σ⁰/γ⁰ are not inherently sensitive,  
they feed **high-sensitivity products**:

- deformation  
- flood  
- wetlands  
- coherence  

QA validates:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive"` propagation  
- `"kfm:mask_required"` readiness  
- correct metadata transitions to transforms  

---

## 🔗 5. PROV-O Lineage

Outputs from radiometry QA are recorded as:

~~~json
{
  "prov:Entity": "s1_radiometry_qa_validation",
  "prov:wasGeneratedBy": "s1_radiometry_qa_pipeline",
  "kfm:qa_type": "radiometry",
  "kfm:care_label": "CARE-B"
}
~~~

These lineage records attach to downstream STAC Items.

---

## 🧪 6. CI Integration

CI enforces:

- deterministic values  
- valid sigma0/gamma0 calibrations  
- DEM alignment integrity  
- schema + SHACL compliance  
- governance metadata presence  
- correct fixture comparisons  

Any mismatch → **CI block**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict radiometry-QA test README; emoji-prefix alignment verified. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [📁 Fixtures](../fixtures/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

