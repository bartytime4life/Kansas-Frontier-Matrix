---
title: "🧪 NASA SMAP — Calibration Stage Test Suite (Gain · Offset · Drift · Uncertainty) · ETL Stage 3"
path: "docs/data/satellites/smap/transforms/calibration/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Calibration Subcommittee · FAIR+CARE Council Oversight"
status: "Active / Enforced"

classification: "Public ETL Test Documentation"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R3"
care_label: "CARE-A / CARE-B (inherited from dataset context)"
indigenous_rights_flag: false
sensitivity_level: "Low (synthetic test data only)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Calibration Subcommittee · Earth Systems QA · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareTest"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-calibration-v11.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-calibration-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:calibration-tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-calibration-tests"
event_source_id: "ledger:docs/data/satellites/smap/transforms/calibration/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "30 months"
sunset_policy: "Superseded upon next calibration test-suite revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **NASA SMAP — Calibration Test Suite (ETL Stage 3)**  
`docs/data/satellites/smap/transforms/calibration/tests/README.md`

**Purpose**  
Validate all calibration operations performed in ETL **Stage 3**, including:  
gain correction, offset correction, drift correction, and calibration-driven uncertainty updates.  
Ensures calibration NEVER introduces unethical precision, misalignment, or governance violations.

</div>

---

## 📘 1. Overview

The calibration-stage test suite ensures:

- 🎚️ Correct application of calibration coefficients  
- 🎚️ Correct radiometer drift adjustments  
- 🎚️ Correct gain/offset correction  
- 📉 Proper uncertainty propagation after calibration  
- 🧭 No CRS distortion  
- 🔐 Preservation of CARE/H3 sovereignty rules  
- 🧾 Accurate STAC/DCAT/PROV-O calibration metadata  
- 🧩 Stable output across calibration epoch changes  

All tests MUST pass before any calibration tables or derived rasters enter production.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/calibration/tests/
├── 📄 README.md                         # This file
│
├── 🧪 test_apply_calibration.py         # Core calibration correction tests
├── 🧪 test_offset_drift.py              # Drift + offset validation tests
├── 🧪 test_coeff_table_loading.py       # Calibration table load/parse/validate tests
├── 🧪 test_uncertainty_after_cal.py     # Post-calibration uncertainty propagation tests
├── 🧪 test_governance_preservation.py   # CARE/H3 governance flag preservation tests
│
└── 🔧 fixtures/                         # Synthetic test data
    ├── sample_precal.tif
    ├── sample_postcal_expected.tif
    ├── coeff_stub.json
    └── calibration_epoch_metadata.json
~~~

---

## 🧩 3. Test Domains & Requirements

### ✔ Calibration Coefficient Loading
- Validate coefficient tables (v001 → vXXX)  
- Match NASA-sourced coefficients  
- Ensure version continuity  

### ✔ Gain & Offset Correction
- Apply corrections exactly as expected  
- Reject invalid/unknown correction tables  
- Validate floating-point accuracy thresholds  

### ✔ Drift Correction (Sensor Lifetime)
- Apply radiometer drift models  
- Validate drift adjustments across decades  
- Ensure no reversed drift (negative → positive) occurs  

### ✔ Uncertainty Propagation
- Recompute uncertainty based on calibration changes  
- Ensure uncertainty never decreases when it shouldn’t  
- Maintain expected uncertainty floors  

### ✔ Metadata Alignment
- Validate `kfm:calibration_version`  
- Validate `prov:used` and `prov:wasGeneratedBy` correctness  
- Validate inclusion of calibration source DOIs  

### ✔ Governance Preservation
Calibration tests ensure:

- CARE labels remain attached  
- Sovereignty flags remain intact  
- No artificial precision is introduced in sensitive regions  
- All calibration-dependent metadata propagates downstream  

Governance tests use synthetic fixtures to simulate  
Indigenous land crossings and sovereign H3 zones.

---

## 🔐 4. Governance & FAIR+CARE Enforcement

Calibration can influence **interpretation** of SMAP soil moisture, FT, and VWC.  
Thus calibration tests must enforce:

- No unethical certainty  
- No calibration-driven sharpening of environmental gradients  
- Correct propagation of H3-sensitive flags  
- No exposure of sensitive patterns due to calibration errors  

Governance validation runs automatically via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. CI Integration

This suite runs under:

- `ci.yml` (unit + functional)  
- `data_pipeline.yml` (integration)  
- `stac_validate.yml` (post-calibration STAC readiness)  
- `faircare_validate.yml` (governance)  

Blocking violations include:

- incorrect coefficient mapping  
- drift sign errors  
- uncertainty inconsistencies  
- broken PROV-O lineage  
- CARE/H3 flag corruption  

---

## 🔁 6. Calibration’s Place in the Full ETL Chain

~~~text
decode
 → reprojection
 → calibration (this test suite validates this stage)
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → STAC/DCAT output
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Stable soil-moisture histories across many calibration epochs.

### Climate  
Consistent vegetation-water anomalies and freeze/thaw transitions.

### Archaeology  
Accurate environmental backdrops, unaffected by calibration drift.

### Story Node v3  
Calibration-aware provenance cues for environmental storytelling.

### Focus Mode v3  
Calibration transparency:  
“Why does this value look this way? What calibration epoch produced it?”

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                           |
|--------:|------------|---------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete calibration test-suite README; emoji layout; FAIR+CARE/H3 checks; CI-safe; STAC-aligned. |
| v10.3.2 | 2025-11-14 | Pre-v11 skeleton test index.                                                                       |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🎚️ Calibration Layer](../README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

