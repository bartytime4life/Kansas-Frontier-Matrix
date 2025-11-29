---
title: "🧪 NASA SMAP — Radiometer QA Test Suite (Beam QA · Channel QA · RFI Susceptibility · QA Codes)"
path: "docs/data/satellites/smap/qa/radiometer/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · SMAP QA Subcommittee · FAIR+CARE Council Oversight"
status: "Active / Enforced"

classification: "Public QA Test Documentation"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
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
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: false

data_steward: "SMAP QA Subcommittee · Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareTest"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-radiometer-qa-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-radiometer-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:radiometer-qa-tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-radiometer-qa-tests"
event_source_id: "ledger:docs/data/satellites/smap/qa/radiometer/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon QA rule update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **SMAP Radiometer QA Test Suite**  
`docs/data/satellites/smap/qa/radiometer/tests/README.md`

**Purpose**  
Validate the **radiometer QA rasters**, QA code tables, metadata, and governance flags  
produced after full KFM ETL processing.  
This suite ensures **QA flags are correct, interpretable, sovereignly safe, and FAIR+CARE compliant**,  
and that all QA assets integrate properly into STAC & DCAT metadata.

</div>

---

## 📘 1. Overview

These tests confirm the correctness of the **Radiometer QA dataset** by verifying:

- ⚠️ radiometer QA bitflag decoding  
- 📡 RFI susceptibility flag integrity  
- 🎚️ retrieval QA consistency for SM/FT/VWC  
- 🗺️ spatial alignment of QA masks (CRS, pixel alignment, H3 correctness)  
- 📑 metadata correctness (`qa_codes.json`, `metadata.json`)  
- 🛡 CARE/H3 sovereignty metadata propagation  
- 📉 QA → uncertainty modifier integrity (Stage 5 alignment)  
- 🔗 PROV-O lineage references  
- 📦 STAC/DCAT readiness  

If any component fails → **KFM blocks SMAP QA dataset release**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/radiometer/tests/
├── 📄 README.md                                 # This file
│
├── 🧪 test_qa_flag_values.py                    # Validate QA bitfields and expected code ranges
├── 🧪 test_qa_decoding.py                       # Test bitfield → semantic QA decoding
├── 🧪 test_radiometer_mask_alignment.py         # Validate spatial/geolocation alignment of QA masks
├── 🧪 test_metadata_fields.py                   # Check STAC/DCAT metadata correctness
├── 🧪 test_governance_preservation.py           # Validate CARE/H3 propagation across QA assets
│
└── 🔧 fixtures/
    ├── sample_qa_flags.tif                     # Synthetic or real QA mask
    ├── sample_qa_codes.json                    # Mapping of QA flags → meanings
    ├── sample_metadata.json                    # STAC/DCAT metadata stub for QA
    ├── sample_expected_mask.json               # Expected results from QA interpretation
    └── schema_expected.json                    # Validation schema for all fixture structures
~~~

---

## 🧩 3. Test Domains & Requirements

### ⚠️ **QA Flag Value Tests**
Validate:

- all flag values fall within allowed NASA ranges  
- no NaN or invalid regional encodings  
- correct masking of “unusable” pixels  

### 📡 **QA Code Decoding Tests**
Validate:

- correct mapping of bitfields → semantic labels  
- unified KFM QA schema (`qa_flag_schema.json`)  
- consistent interpretation across tiles and time ranges  

### 🗺️ **Mask Alignment Tests**
Validate:

- CRS correctness  
- pixel-level alignment with radiometer input rasters  
- correct alignment with downstream freeze–thaw / VWC grids  
- H3 alignment for sovereignty masking  

### 📑 **Metadata Tests**
Validate:

- STAC properties (`kfm:qa_values`, `qa_flag_schema`, etc.)  
- DCAT QA fields (quality notes, license, rights)  
- temporal + spatial extents  

### 🔐 **Governance Preservation Tests**
Validate that QA layers:

- correctly propagate `"kfm:care_label"`  
- include `"kfm:h3_sensitive"` when required  
- apply `"kfm:mask_required"` in sovereignty-sensitive regions  
- never reveal more precision than allowed  
- follow CARE A/B policies  

---

## 🔐 4. Sovereignty, FAIR+CARE, and Ethical Constraints

QA datasets interact with sovereignty concerns when:

- QA anomalies intersect tribal territories  
- RFI-driven degradation aligns with culturally sensitive lands  
- retrieval confidence interacts with land-use patterns  

Thus tests ensure:

- sovereignty/H3 tags preserved  
- full governance metadata present  
- uncertainty floors not reduced  
- QA masks never increase precision within protected areas  

Integration validated using:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. CI Integration

Runs under:

- **ci.yml** (all tests)  
- **data_pipeline.yml** (ETL provenance chain)  
- **stac_validate.yml** (STAC correctness)  
- **jsonld_validate.yml** (JSON-LD/PROV ontology correctness)  
- **faircare_validate.yml** (sovereignty + CARE enforcement)  

Any failure blocks the QA dataset release for SMAP.

---

## 🔁 6. QA in the Full SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration (ETL Stage 4)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
 → QA DATASET LAYER (validated by this suite)
~~~

QA Test Suite ensures **final QA integrity** before STAC/DCAT publication.

---

## 🔮 7. Applications in KFM

### Hydrology  
Better wetness anomaly control.

### Climate  
Improved VWC/FT reliability.

### Archaeology  
Governance-safe context layers.

### Story Node v3  
QA-backed narrative reliability scores.

### Focus Mode v3  
QA-based confidence modulation.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                     |
|--------:|------------|-------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Radiometer QA Test Suite README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV compliant; CI-safe.          |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [⚠️ Radiometer QA Layer](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

