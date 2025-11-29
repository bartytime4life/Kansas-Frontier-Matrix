---
title: "🧪 NASA SMAP — Uncertainty Propagation Test Suite (Radiometer · QA/RFI · Calibration · Sovereignty) · ETL Stage 5"
path: "docs/data/satellites/smap/transforms/uncertainty/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Uncertainty Subcommittee · FAIR+CARE Council Oversight"
status: "Active / Enforced"

classification: "Public ETL Test Documentation"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
jsonld_profile: "KFM-JSONLD v11"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B depending on scenario"
indigenous_rights_flag: true
sensitivity_level: "Medium (uncertainty impacts interpretation)"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: false

data_steward: "Uncertainty Subcommittee · Earth Systems QA · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareTest"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-uncertainty-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-uncertainty-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:uncertainty-tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-uncertainty-tests"
event_source_id: "ledger:docs/data/satellites/smap/transforms/uncertainty/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next uncertainty-model update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **NASA SMAP — Uncertainty Propagation Test Suite (ETL Stage 5)**  
`docs/data/satellites/smap/transforms/uncertainty/tests/README.md`

**Purpose**  
Validate **uncertainty propagation** across radiometer noise, calibration corrections,  
QA/RFI modifiers, and sovereignty-aware uncertainty floors.  
Ensures ethical, reproducible, scientifically valid and FAIR+CARE-governed uncertainty behavior  
in all SMAP-derived KFM datasets.

</div>

---

## 📘 1. Overview

This test suite ensures that uncertainty propagation in SMAP ETL Stage 5:

- 📉 Computes radiometer-origin uncertainty correctly  
- 🎚️ Integrates calibration-induced uncertainty adjustments  
- ⚠️ Applies QA/RFI uncertainty multipliers  
- 🧮 Merges uncertainty models into the combined model  
- 🔐 Enforces sovereignty-aware uncertainty floors (H3)  
- 🗺️ Maintains CRS/grid alignment across uncertainty rasters  
- 📦 Produces STAC v11-compliant uncertainty assets  
- 🧾 Emits correct PROV-O lineage  
- 🛡 Preserves CARE labels & governance metadata  

All tests MUST pass before uncertainty-enhanced datasets can leave ETL.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/uncertainty/tests/
├── 📄 README.md                                  # This file
│
├── 🧪 test_uncertainty_core.py                    # Test core radiometer + calibration uncertainty math
├── 🧪 test_uncertainty_scaling.py                # Test QA/RFI scaling behavior
├── 🧪 test_uncertainty_floor.py                  # Sovereignty-based minimum uncertainty floors
├── 🧪 test_governance_preservation.py            # CARE/H3 metadata integrity tests
├── 🧪 test_model_consistency.py                  # Combined model consistency (radiometer+QA/RFI+calibration)
│
└── 🔧 fixtures/                                   # Deterministic synthetic test datasets
    ├── sample_preuncertainty.tif
    ├── sample_postuncertainty_expected.tif
    ├── model_stub.json
    ├── sovereignty_mask_stub.json
    └── schema_expected.json
~~~

---

## 🧩 3. Test Domains

### 🧮 **Core Radiometer Uncertainty**
Validates:
- brightness-temperature noise handling  
- retrieval error bounds  
- non-negative constraints  
- floor enforcement  

### 🎚️ **Calibration-Induced Uncertainty**
Validates:
- drift/gain/offset-induced uncertainty  
- propagation of calibration-table deltas  
- no silent reduction of uncertainty  

### ⚠️ **QA/RFI Scaling**
Validates:
- RFI-driven uncertainty increases  
- Retrieval-confidence-based scaling  
- FT transition-region uncertainty boosts  
- VWC low-confidence penalties  

### 🔐 **Sovereignty-Aware Floors**
Validates:
- correct `"kfm:sovereignty_uncertainty_floor"` application  
- H3 propagation  
- uncertainty never decreases in sensitive zones  

### 📉 **Combined-Uncertainty Model Consistency**
Validates:
- merged radiometer + QA/RFI + calibration models  
- normalization of combined uncertainty  
- no cross-dimension mismatch  

### 🛡 **Governance Preservation**
Ensures:
- CARE labels preserved  
- `"kfm:mask_required"` propagates  
- Sovereignty flags not lost through math  
- No unethical sharpening or certainty inflation  

---

## 🔐 4. Governance, FAIR+CARE & Sovereignty Enforcement

All tests must ensure:

- No reduction in uncertainty near sensitive Indigenous lands  
- Masking implications are preserved  
- `"kfm:h3_sensitive"` propagated  
- Full provenance of uncertainty model use  
- Combined uncertainty respects ethical uncertainty floors  

Governance CI enforces via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  
- `stac_validate.yml`

---

## 🧪 5. CI Integration

This test suite is executed via:

- **ci.yml** — unit + integration  
- **data_pipeline.yml** — ETL stage graph  
- **stac_validate.yml** — uncertainty asset compliance  
- **jsonld_validate.yml** — ontology alignment  
- **faircare_validate.yml** — sovereignty/CARE compliance  

A single failure → ETL Stage 5 is blocked.

---

## 🔁 6. Uncertainty’s Place in the Full ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation (this test suite)
 → governance masking (CARE/H3)
 → STAC/DCAT dataset creation
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

---

## 🔮 7. Applications Across KFM

### Hydrology  
Stable soil-moisture uncertainty envelopes.

### Climate  
Uncertainty-aware VWC & FT anomaly maps.

### Archaeology  
Ethical interpretation of environmental change.

### Story Node v3  
Narratives include uncertainty bars & confidence statements.

### Focus Mode v3  
Uncertainty-weighted reasoning for environmental overlays.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                 |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full uncertainty-test README; emoji layout; sovereignty floors; QA/RFI scaling; STAC/PROV/CARE aligned. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📉 Uncertainty Fixtures](../fixtures/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

