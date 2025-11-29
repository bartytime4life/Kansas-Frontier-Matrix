---
title: "🧪 NASA SMAP — STAC Writer Test Suite (Collections · Items · Assets · Governance · Provenance)"
path: "docs/data/satellites/smap/transforms/stac_writer/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · STAC Review Board · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public STAC Test Documentation"
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

fair_category: "F1-A1-I3-R5"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
public_exposure_risk: "Medium"
risk_category: "Medium"
redaction_required: true

data_steward: "STAC/DCAT Review Board · FAIR+CARE Council · Earth Systems Working Group"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareTest"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-stac-writer-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-stac-writer-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:stac-writer-tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-stac-writer-tests"
event_source_id: "ledger:docs/data/satellites/smap/transforms/stac_writer/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next STAC/DCAT update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **NASA SMAP — STAC Writer Test Suite (Final ETL Validation Layer)**  
`docs/data/satellites/smap/transforms/stac_writer/tests/README.md`

**Purpose**  
Provide the **complete testing framework** validating SMAP STAC Collections, Items, Assets,  
Governance Metadata, Uncertainty Metadata, DCAT metadata, and PROV-O lineage produced  
by the STAC Writer stage — the final ETL step before publication.

</div>

---

## 📘 1. Overview

This test suite ensures:

- 📦 **STAC Collections** follow STAC v1.0 + KFM-STAC v11  
- 🗂 **STAC Items** include correct geometry, bbox, datetime, assets  
- 🖼 **Assets** (COGs, QA masks, uncertainty surfaces, governance masks) follow projection/raster rules  
- 🛡 **Governance/CARE/H3 metadata** is applied correctly  
- 📉 **Uncertainty metadata** matches ETL Stage 5 outputs  
- ⚠️ **QA/RFI metadata** is preserved  
- 📜 **DCAT metadata** is internally consistent  
- 🔗 **PROV-O lineage** is correct and complete  
- 📏 **Schema compliance** validated against JSON Schema & SHACL  
- 🚫 **No unmasked sensitive geographies** appear in outputs  
- 📁 **STAC template history/diffs remain consistent**  

Any failure → KFM blocks the entire SMAP publish pipeline.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/stac_writer/tests/
├── 📄 README.md                                            # This file
│
├── 🧪 test_collection_build.py                              # Validates Collection metadata output
├── 🧪 test_item_build.py                                    # Validates Item creation logic
├── 🧪 test_governance_metadata.py                           # Ensures CARE/H3/sovereignty metadata survives
├── 🧪 test_stac_schema_compliance.py                        # STAC v1.0 schema validation (JSON Schema + SHACL)
├── 🧪 test_provenance.py                                    # PROV-O JSON-LD validation
├── 🧪 test_dcat_metadata.py                                 # DCAT v3 structure validation
│
└── 🔧 fixtures/                                             # Deterministic synthetic test assets
    ├── sample_processed_raster.tif
    ├── sample_qa_mask.tif
    ├── sample_uncertainty.tif
    ├── sample_governance_mask.tif
    ├── sample_governance_metadata.json
    ├── sample_provenance_input.json
    ├── expected_stac_item.json
    ├── expected_stac_collection.json
    └── schema_expected.json
~~~

---

## 🧩 3. Test Domains & Requirements

### 📦 **Collection Tests**
Validate:

- Required STAC fields  
- Correct temporal + spatial extent  
- Summaries for SM/FT/VWC/QA/uncertainty  
- Governance extension  
- Links + version history  

### 🗂 **Item Tests**
Validate:

- geometry & bbox alignment  
- datetime correctness  
- asset presence + roles  
- projection/raster extension accuracy  
- QA + uncertainty + governance assets  
- STAC link structure  

### 🖼 **Asset Tests**
Validate:

- TIFF COG compliance  
- Nodata rules  
- Band structures  
- QA masks  
- governance masks  
- uncertainty grids  
- provenance links  

### 🛡 **Governance Tests**
Validate:

- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  

### 📉 **Uncertainty Tests**
Validate:

- uncertainty metadata completeness  
- uncertainty floors in Item properties  
- asset-level uncertainty correctness  

### ⚠️ **QA/RFI Metadata Tests**
Validate:

- QA flag schema  
- QA value mapping  
- QA confidence scores  
- RFI-derived uncertainty influence  

### 🧾 **DCAT Tests**
Validate:

- Dataset → Distribution mapping  
- JSON-LD correctness  
- Rights & licensing  

### 🔗 **PROV-O Tests**
Validate:

- complete lineage graph  
- decode → reprojection → calibration → QA → uncertainty → governance → STAC Writer  
- all `prov:used` elements present  
- correct generative activity  

---

## 🔐 4. Governance, FAIR+CARE & Sovereignty Enforcement

This suite ensures:

- no sensitive geographies are exposed  
- sovereignty-aware masking preserved  
- uncertainty metadata not reduced illegitimately  
- CARE labels remain correct  
- STAC Items include all governance properties  
- provenance fully reflects governance transforms  
- DCAT metadata represents sensitivity correctly  

Governance enforced by:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. CI Integration

Runs in:

- **ci.yml**  
- **data_pipeline.yml**  
- **stac_validate.yml**  
- **jsonld_validate.yml**  
- **faircare_validate.yml**  

Any inconsistency = hard block.

---

## 🔁 6. Placement in SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → STAC Writer
    → (validated by this test suite)
 → STAC/DCAT publishing
 → PROV-O archival
~~~

---

## 🔮 7. Applications Across KFM

### Environmental  
Reliable STAC archives for SM, FT, VWC.

### Archaeological  
Governance-safe environmental layers for research.

### Story Node v3  
Stable STAC metadata for narrative environments.

### Focus Mode v3  
STAC-backed environmental reasoning with uncertainty & governance info.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                 |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full STAC Writer test-suite README; governance/H3 aligned; STAC/DCAT/PROV correct; CI-safe; emoji-rich. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 STAC Writer Fixtures](../fixtures/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

