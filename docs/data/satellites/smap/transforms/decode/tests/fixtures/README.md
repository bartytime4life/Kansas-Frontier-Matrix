---
title: "📦 NASA SMAP — Decode Stage Test Fixtures (L2/L3 Sample Inputs · HDF5/NetCDF) · KFM ETL v11.2.2"
path: "docs/data/satellites/smap/transforms/decode/tests/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · QA Subcommittee · FAIR+CARE Council"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

test_category: "Decode-Stage Fixtures · Unit/Integration"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
jsonld_profile: "KFM-JSONLD v11"
provenance_profile: "KFM-PROV-O v11.2"

sbom_ref: "../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public Test Fixtures"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

fair_category: "F1-A1-I1-R2"
care_label: "CARE-A / CARE-B depending on spatial metadata"
indigenous_rights_flag: true
sensitivity_level: "Low (mock data)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · QA Subcommittee · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../../../schemas/json/tests-smap-decode-v11.schema.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/tests-smap-decode-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:decode:fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-decode-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/transforms/decode/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "18 months"
sunset_policy: "Superseded upon fixture-format update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — Decode Test Fixtures (L2/L3 Sample HDF5/NetCDF)**  
`docs/data/satellites/smap/transforms/decode/tests/fixtures/README.md`

**Purpose**  
Define the **gold-standard sample input files** used by the SMAP Decode Stage  
unit + integration tests. These fixtures simulate SMAP L2/L3 radiometer products,  
ensuring deterministic, reproducible, FAIR+CARE-safe decode behavior before  
reprojection, calibration, QA, uncertainty, masking, STAC creation, and lineage export.

</div>

---

## 📘 1. Overview

The fixture files enable **safe, stable, offline testing** of:

- SMAP L2 radiometer decode  
- SMAP L3 Soil Moisture decode  
- SMAP L3 Freeze/Thaw decode  
- SMAP L3 Vegetation Water Content decode  
- QA/RFI field extraction  
- Orbit + geometry metadata extraction  
- Temporal conversion (NASA → ISO → OWL-Time)  
- Metadata flattening  
- Governance pre-scan (CARE/H3)  

These are **small, synthetic test products**, built to:

- Match NASA’s real HDF5/NetCDF schema  
- Be FAIR+CARE-safe  
- Contain no sensitive actual environmental measurements  
- Provide deterministic test patterns  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/decode/tests/fixtures/
├── 📄 README.md                           # This file
│
├── 🛰️ sample_l2.h5                        # Synthetic SMAP L2 swath radiometer product
├── 🛰️ sample_l3_sm.h5                     # Synthetic SMAP L3 soil moisture grid
├── 🛰️ sample_l3_ft.h5                     # Synthetic SMAP L3 freeze/thaw grid
├── 🛰️ sample_l3_vwc.h5                    # Synthetic SMAP L3 vegetation water content grid
│
└── 🧪 schema_expected.json                # Expected field presence/types for decode tests
~~~

Optional extras may be added:

- `orbit_mock.json`  
- `qa_mock.json`  
- `metadata_mock.json`  

…but only with CI-approved structure and size limits.

---

## 🧩 3. Fixture Design Rules (KFM v11.2.2)

### ✔ Deterministic  
- No timestamps based on “now”  
- No randomization unless seeded and declared  

### ✔ Schema-faithful  
- All required NASA groups/variables included  
- Shapes/dimensions match NASA HDF reference  
- Units + scale/offset set  

### ✔ FAIR+CARE-safe  
- No real environmental values  
- Synthetic, invented, non-sensitive arrays  
- Cannot be reverse-engineered into real-world interpretation  

### ✔ Governance-compatible  
Fixtures must contain:

- Synthetic geography that still triggers sovereignty logic  
- CARE/H3 flags in metadata (synthetic but valid)  
- Test-safe lat/lon bounds, not real land features  

### ✔ Test-ready  
- Tiny file sizes  
- Quick to load  
- Inline with pyro/pytest workflows  
- Stable across platforms  

---

## 🧪 4. Tests Powered by Fixtures

Fixtures are required by:

- `test_decode_l2.py`  
- `test_decode_l3_sm.py`  
- `test_decode_l3_ft.py`  
- `test_decode_l3_vwc.py`  
- `test_metadata_norm.py`  
- `test_temporal_norm.py`  
- `test_schema_conformance.py`  
- `test_care_prescan.py`  

They validate:

- Variable extraction  
- Schema conformance  
- Temporal correctness  
- Orbit/geometry extraction  
- Governance pre-scan logic  
- Readiness for STAC generation  

---

## 🔐 5. Governance & Sovereignty

Even though fixtures use *synthetic data*, they must:

- Include CARE labels appropriate to mission constraints  
- Include sovereignty fields  
- Include `"kfm:mask_applied": false` (decode stage never masks)  
- Demonstrate behaviors that downstream CARE/H3 masking will act upon  
- Match ethical requirements for test datasets  

Governance validation is performed by:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🔁 6. Update & Change Management

Any fixture changes require:

1. Updating the corresponding decode tests  
2. Updating schema_expected.json  
3. Updating this README’s version history  
4. Updating decode schemas if NASA changed upstream  
5. Running all decode-stage CI pipelines  

Fixture updates **must** be reviewed by:

- Earth Systems QA Team  
- FAIR+CARE Council  
- Sovereignty reviewers (if spatial fields change)  

---

## 🧭 7. Version History

| Version | Date       | Summary                                                                                                 |
|--------:|------------|---------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | First fully documented fixture README; emoji layout; FAIR+CARE; STAC/DCAT/JSON-LD alignment; CI-safe.   |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal fixture index.                                                                           |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🛠️ Decode Stage Tests](../README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

