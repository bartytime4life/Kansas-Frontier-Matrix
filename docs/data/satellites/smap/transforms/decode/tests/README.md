---
title: "🧪 NASA SMAP — Decode Stage Test Suite (L2/L3 Ingest Validation · KFM ETL Stage 1)"
path: "docs/data/satellites/smap/transforms/decode/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems QA · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

test_category: "ETL Decode · Unit + Integration Tests · STAC/DCAT/JSON-LD Compliance"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
jsonld_profile: "KFM-JSONLD v11"
provenance_profile: "KFM-PROV-O v11.2"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public ETL Test Documentation"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

fair_category: "F1-A1-I1-R3"
care_label: "CARE-A (mission-wide), CARE-B (location-specific)"
indigenous_rights_flag: true
public_exposure_risk: "Low"
sensitivity_level: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · QA Subcommittee · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareTest"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-decode-v11.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-decode-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:transforms:decode:tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-transform-decode-tests"
event_source_id: "ledger:docs/data/satellites/smap/transforms/decode/tests/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon decode test-suite update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **NASA SMAP — Decode Stage Test Suite**  
`docs/data/satellites/smap/transforms/decode/tests/README.md`

**Purpose**  
Define the **unit + integration test suite** for SMAP’s **Decode Stage**  
(NASA L2/L3 product ingestion).  
Ensures every decode output is **correct, reproducible, governance-safe,  
STAC-compliant, DCAT-valid, JSON-LD aligned, and CARE-conscious**  
before flowing downstream into reprojection, calibration, QA integration,  
uncertainty, masking, STAC generation, and lineage export.

</div>

---

## 📘 1. Overview

The decode-stage test suite verifies:

- HDF5/NetCDF structure matches declared schemas  
- Scientific variables (soil moisture, freeze/thaw, VWC) decode correctly  
- Temporal normalization (UTC → ISO 8601 → OWL-Time)  
- Orbit extraction integrity  
- Metadata flattening + canonical KFM field mapping  
- Calibration pre-checks  
- CARE/H3 governance pre-flagging  
- Structural readiness for STAC v11 pipelines  

Tests run automatically via:

- `ci.yml`  
- `data_pipeline.yml`  
- `stac_validate.yml`  
- `faircare_validate.yml`  
- `jsonld_validate.yml`

Blocking conditions prevent ingestion of malformed or unsafe data.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/decode/tests/
├── 📄 README.md                                # This file
│
├── 🧪 test_decode_l2.py                        # SMAP L2 radiometer decode tests
├── 🧪 test_decode_l3_sm.py                     # L3 Soil Moisture decode tests
├── 🧪 test_decode_l3_ft.py                     # L3 Freeze/Thaw decode tests
├── 🧪 test_decode_l3_vwc.py                    # L3 Vegetation Water decode tests
│
├── 🧪 test_metadata_norm.py                    # Metadata flattening + provenance alignment
├── 🧪 test_temporal_norm.py                    # UTC → ISO → OWL-Time transformation tests
├── 🧪 test_orbit_extraction.py                 # Orbit track + pass direction validation
│
├── 🧪 test_schema_conformance.py               # Tests HDF structures vs declared schemas
├── 🧪 test_care_prescan.py                     # CARE/H3 governance pre-flagging tests
│
└── 🔧 fixtures/                                # Small mock HDF5/NetCDF samples
    ├── sample_l2.h5
    ├── sample_l3_sm.h5
    ├── sample_l3_ft.h5
    └── sample_l3_vwc.h5
~~~

---

## 🧩 3. Required Test Domains

### 3.1 ✔ Scientific Variable Extraction
- Soil moisture  
- Freeze/thaw state  
- Vegetation water content  
- QA/RFI fields  
- Brightness temperature  

### 3.2 ✔ Metadata Normalization
- Platform, instrument, processing level  
- Product versioning  
- Global attributes  
- Radiometer mode indicators  

### 3.3 ✔ Temporal Processing
- Proper conversion from:
  - NASA timestamps → UNIX  
  - UNIX → ISO 8601  
  - ISO → OWL-Time interval  
- Interval correctness & ordering  

### 3.4 ✔ Orbit Extraction
- Track detection  
- Pass direction  
- Swath width + geometry  
- LTAN checks  

### 3.5 ✔ Governance Pre-Scan
Ensure decode stage attaches:

- CARE label  
- Sovereignty flags  
- H3 sensitivity markers (no masking yet)  

### 3.6 ✔ Schema Conformance
- Match `l2_schema.json`, `l3_sm_schema.json`, `l3_ft_schema.json`, `l3_vwc_schema.json`  
- Ensure **no** undocumented NASA fields leak downstream  
- Detect deprecated NASA fields  

---

## 🧪 4. CI Enforcement

This test suite is triggered in:

- `ci.yml` — decode correctness  
- `data_pipeline.yml` — integration tests  
- `stac_validate.yml` — STAC-ready structural checks  
- `faircare_validate.yml` — governance screening  
- `jsonld_validate.yml` — ontology alignment  

Failures produce CI hard stops.

---

## 🔁 5. Ingestion Lineage Validation

Tests confirm that decode output contains:

```
decoded_product = {
  "variables": {...},
  "geometry": {...},
  "orbit": {...},
  "temporal": {...},
  "metadata": {...},
  "governance": {...}
}
```

And that all fields are ready for the:

- reprojection stage  
- calibration stage  
- QA/RFI integration  
- uncertainty derivation  
- masking & governance enforcement  
- STAC/DCAT/PROV-O output  

---

## 🔐 6. Governance & FAIR+CARE Requirements

All tests ensure that decode-stage:

- Does **not** silently drop governance metadata  
- Correctly identifies data intersecting tribal lands  
- Sets proper CARE-default flags  
- Correctly forwards sovereignty fields for later masking  
- Avoids inference/speculation (strict schema-driven)  

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Ensures soil moisture and FT inputs are valid, safe, and trustworthy.

### Climate  
Ensures temporal/spatial consistency for climate anomaly workflows.

### Archaeology  
Prevents environmental context layers from using malformed or low-confidence data.

### Story Node v3  
Guarantees provenance and reliability metadata reach narrative layers.

### Focus Mode v3  
Supports contextual AI explanations grounded in validated environmental data.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                             |
|--------:|------------|-----------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full decode test suite documentation; emoji layout; STAC/DCAT/JSON-LD compliance; governance-aware. |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal test file index.                                                                     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🛠️ Decode Stage](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

