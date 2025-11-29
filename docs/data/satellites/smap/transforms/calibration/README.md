---
title: "🎚️ NASA SMAP — Calibration Stage (Radiometer Drift · Gain · Offset) · ETL Stage 3 (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/data/satellites/smap/transforms/calibration/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council · Calibration Subcommittee"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
provenance_profile: "KFM-PROV-O v11.2"
jsonld_profile: "KFM-JSONLD v11"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public ETL Documentation"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

fair_category: "F1-A1-I2-R3"
care_label: "CARE-A / CARE-B (context dependent)"
indigenous_rights_flag: true
sensitivity_level: "Low (calibration surface only)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · Calibration Subcommittee · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"

json_schema_ref: "../../../../../../../schemas/json/transform-smap-calibration-v11.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/transform-smap-calibration-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:transform:calibration-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-transform-calibration"
event_source_id: "ledger:docs/data/satellites/smap/transforms/calibration/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon next calibration pipeline revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🎚️ **NASA SMAP — Calibration Stage (Radiometer Drift, Gain, Offset Correction)**  
`docs/data/satellites/smap/transforms/calibration/README.md`

**Purpose**  
Document the **Calibration Stage** (ETL Stage 3) that corrects SMAP L2/L3 radiometer outputs  
for **drift**, **gain offsets**, **instrument performance changes**, and **calibration table updates**,  
ensuring geospatial & temporal consistency for soil moisture, freeze–thaw, VWC, and QA/RFI STAC outputs.

</div>

---

## 📘 1. Overview

The Calibration Stage:

- 🎚️ Applies NASA-provided **calibration coefficients**  
- 🛠 Adjusts **brightness temperature** and derived geophysical products  
- 🧪 Handles **instrument drift** over mission lifetime  
- 🧭 Harmonizes calibration across SMAP modes/versions  
- 📉 Updates uncertainty values associated with calibration changes  
- 🔐 Propagates governance flags (never sharpens sensitive environmental signatures)  
- 🧾 Writes calibration-adjusted metadata for STAC/DCAT/PROV-O items  

This is ETL **Stage 3**, after:

```
decode
 → reprojection
 → calibration   (this stage)
 → QA/RFI integration
 → uncertainty propagation
 → governance masking (CARE/H3)
 → STAC/DCAT + lineage export
```

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/calibration/
├── 📄 README.md                       # This file
│
├── 🎚️ apply_calibration.py            # Main calibration engine
├── 🧮 coefficients.json                # NASA coefficient tables (vetted & versioned)
├── 📚 calibration_tables/             # Per-version calibration lookup tables
│   ├── table_v001.json
│   ├── table_v002.json
│   └── table_vXXX.json
│
├── 🧪 tests/                           # Calibration test suite
│   ├── test_apply_calibration.py
│   ├── test_offset_drift.py
│   ├── test_coeff_table_loading.py
│   └── fixtures/
│       ├── sample_precal.tif
│       ├── sample_postcal_expected.tif
│       └── coeff_stub.json
~~~

---

## 🧩 3. Calibration Responsibilities

### ✔ Radiometer Drift Correction
- Adjust for long-term sensor drift  
- Use NASA mission drift tables  
- Prevent false environmental shifts due to instrument changes  

### ✔ Gain/Offset Adjustment
- Apply radiometer gain corrections  
- Offset calibration aligned with NASA L2/L3 product notes  

### ✔ Mode-Specific Calibration
- Handle different SMAP modes:
  - Radiometer-only  
  - Radiometer + backscatter (if present)  
- Ensure mode-consistent correction across cycles  

### ✔ Metadata Updates
- Update:
  - `kfm:calibration_version`  
  - `kfm:calibration_source`  
  - `kfm:calibration_applied: true`  
- Add PROV-O entries:
  - `prov:used` calibration table  
  - `prov:wasGeneratedBy` calibration process  

### ✔ Error-Budget Adjustments
- Update uncertainty fields  
- Track correction-induced error propagation  
- Ensure uncertainty never **artificially decreases**  

---

## 🔐 4. Governance & Sovereignty

Calibration must **not**:

- Increase spatial precision  
- Introduce artifacts near sensitive Indigenous lands  
- Reduce uncertainty in ways that could mislead interpretation  
- Remove sovereignty-required uncertainty floors  

Calibration **must**:

- Carry CARE labels inherited from decode/reprojection  
- Preserve H3 sovereignty flags  
- Never sharpen environmental contrasts in protected areas  
- Log all calibration actions into PROV-O lineage  

Governance checks run via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 5. QA & Validation

Calibration tests verify:

- Correct coefficient loading for each NASA version  
- Proper drift/gain/offset correction  
- Accurate propagation of uncertainty  
- Integrity of raster math (no NaN propagation unless expected)  
- CRS consistency post-calibration  
- Governance field preservation  

QA results appear in:

`docs/data/satellites/smap/qa/`

Telemetry recorded in:

`releases/<version>/data-telemetry.json`

---

## 🔁 6. Integration in the Full ETL Chain

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking (CARE/H3)
 → STAC/DCAT item construction
 → PROV-O lineage export
 → OpenLineage telemetry emission
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
- Soil moisture consistency across calibration epochs  
- Accurate wetness trend detection  

### Climate  
- Stable VWC anomaly tracking  
- Improved freeze/thaw classification accuracy  

### Archaeology  
- Consistent environmental backdrops  
- Avoid calibration-driven misinterpretation  

### Story Node v3  
- Reliable calibration-sensitive environmental narratives  

### Focus Mode v3  
- Transparent calibration provenance for AI explanations  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                     |
|--------:|------------|---------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full calibration-stage README; emoji layout; STAC/DCAT/PROV-O/H3 governance; CI-safe.       |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal calibration notes.                                                           |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🛠️ Transform Layer](../README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

