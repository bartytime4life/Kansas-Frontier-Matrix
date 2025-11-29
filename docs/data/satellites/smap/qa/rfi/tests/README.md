---
title: "🧪 NASA SMAP — RFI QA Test Suite (Interference Masks · Bitfields · Metadata · Governance)"
path: "docs/data/satellites/smap/qa/rfi/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · SMAP QA Subcommittee · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public QA Test Documentation"
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
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
risk_category: "Medium"
redaction_required: true

data_steward: "SMAP QA Subcommittee · Earth Systems Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareTest"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-rfi-qa-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-rfi-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:rfi-qa-tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-rfi-qa-tests"
event_source_id: "ledger:docs/data/satellites/smap/qa/rfi/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon RFI QA revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **SMAP RFI QA Test Suite**  
`docs/data/satellites/smap/qa/rfi/tests/README.md`

**Purpose**  
Validate the **RFI contamination masks**, **bitfield decoding**, **QA metadata**,  
and **sovereignty-aware governance behavior** of the RFI QA dataset produced in KFM.  
Ensures RFI layers are safe, interpretable, and compliant with  
FAIR+CARE, sovereignty rules, and STAC/DCAT/PROV-O requirements.

</div>

---

## 📘 1. Overview

These tests confirm that SMAP RFI QA products:

- 📡 correctly decode RFI bitfields  
- ⚠️ identify contaminated or suspect radiometer pixels  
- 🎚️ integrate with retrieval QA (SM/FT/VWC)  
- 📉 apply correct uncertainty-scaling factors  
- 🗺️ align spatially with soil-moisture and FT grids  
- 🛡 propagate sovereignty (H3) + CARE metadata  
- 📑 produce schema-valid STAC & DCAT metadata  
- 🔗 embed valid PROV-O lineage  
- 🚫 contain no unmasked sensitive geographical detail  

Any test failure → **KFM blocks RFI QA dataset release**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/rfi/tests/
├── 📄 README.md                               # This file
│
├── 🧪 test_rfi_flag_values.py                 # Validate RFI bit ranges and code boundaries
├── 🧪 test_rfi_decoding.py                    # Confirm bitfield → semantic meaning mapping
├── 🧪 test_rfi_mask_alignment.py              # Validate CRS + pixel alignment of RFI masks
├── 🧪 test_rfi_metadata.py                    # Test STAC/DCAT metadata for QA layers
├── 🧪 test_governance_preservation.py         # Validate CARE + H3 sovereignty propagation
│
└── 🔧 fixtures/
    ├── sample_rfi_mask.tif                    # Synthetic RFI mask
    ├── sample_rfi_codes.json                  # Bitfield → meaning mapping
    ├── sample_metadata.json                   # Metadata stub for QA
    ├── expected_rfi_interpretation.json       # Expected bitfield-decoded results
    └── schema_expected.json                   # Strict validation schema for all fixtures
~~~

---

## 🧩 3. Test Domains & Expectations

### 📡 **Bitfield Decoding Tests**
Validate:

- correct interpretation of NASA RFI bitfields  
- support for KFM unified RFI QA schema  
- deterministic behavior across runs  

### 🚨 **Contamination Mask Tests**
Validate:

- identification of contaminated pixels  
- classification of ambiguous/intermediate RFI states  
- usability flags for SM/FT/VWC pipelines  

### 🗺️ **Spatial Alignment Tests**
Validate:

- CRS consistency  
- alignment with soil-moisture rasters  
- compatibility with ETL Stage 4 masks  
- H3 alignment in sovereign regions  

### 📑 **Metadata Tests**
Validate:

- STAC/QC metadata blocks  
- QA schema correctness  
- DCAT fields including quality notes  
- uncertainty & calibration references  

### 🛡 **Governance Preservation Tests**
Validate:

- `"kfm:care_label"` preservation  
- `"kfm:h3_sensitive"` propagation  
- `"kfm:mask_required"` when RFI intersects sovereign lands  
- `"kfm:sovereignty_uncertainty_floor"` consistency  
- `"kfm:governance_notes"` correctness  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

RFI QA interacts with sovereignty when:

- interference patterns intersect cultural landscapes  
- RFI shadows align with tribal territories  
- contamination effects imply sensitive environmental conditions  

Thus RFI QA outputs **must**:

- avoid revealing precise environmental states  
- be aggregated in sovereign regions  
- retain sovereignty metadata  
- include explicit `"kfm:governance_notes"`  

Compliance validated under:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. CI Integration

This test suite is executed under:

- **ci.yml**  
- **data_pipeline.yml**  
- **jsonld_validate.yml**  
- **stac_validate.yml**  
- **faircare_validate.yml**  

Any mismatch at this stage → automatic block.

---

## 🔁 6. RFI QA in the SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration (this layer validated here)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. Applications in KFM

### Hydrology  
Remove RFI anomalies from soil-moisture signals.

### Climate  
Prevent RFI-driven FT/VWC misclassifications.

### Archaeology  
Protect sensitive ecosystems from misinterpreted environmental states.

### Story Node v3  
Improve reliability of environmental context narratives.

### Focus Mode v3  
Integrate RFI confidence into reasoning weights.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                         |
|--------:|------------|------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial SMAP RFI QA Test Suite README; governance/H3 aligned; FAIR+CARE compliant; STAC/DCAT/PROV ready; CI-safe.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📡 RFI QA Fixtures](../fixtures/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

