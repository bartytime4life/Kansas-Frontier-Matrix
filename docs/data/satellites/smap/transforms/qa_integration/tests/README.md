---
title: "🧪 NASA SMAP — QA/RFI Integration Test Suite (ETL Stage 4)"
path: "docs/data/satellites/smap/transforms/qa_integration/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems QA · FAIR+CARE Council Oversight"
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

fair_category: "F1-A1-I2-R3"
care_label: "CARE-A / CARE-B depending on spatial crossovers"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems QA Subcommittee · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareTest"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-qa-integration-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-qa-integration-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:qa-integration-tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-qa-integration-tests"
event_source_id: "ledger:docs/data/satellites/smap/transforms/qa_integration/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded when QA/RFI spec is updated"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **NASA SMAP — QA/RFI Integration Test Suite (KFM ETL Stage 4)**  
`docs/data/satellites/smap/transforms/qa_integration/tests/README.md`

**Purpose**  
Validate all QA/RFI integration behaviors in SMAP ETL Stage 4:  
QA code normalization, RFI decoding, uncertainty scaling,  
CRS-consistent QA rasters, KFM unified QA schema validation,  
and preservation of FAIR+CARE + sovereignty governance metadata.

</div>

---

## 📘 1. Test Suite Overview

This test suite ensures that SMAP QA/RFI integration:

- ⚠️ Correctly merges all NASA QA fields (L2/L3)  
- 📡 Correctly decodes and classifies Radio Frequency Interference (RFI)  
- 🧬 Maps NASA QA → KFM unified QA schema (`qa_flag_schema.json`, `qa_mappings.json`)  
- 📉 Applies QA-driven uncertainty modifiers correctly  
- 🌍 Preserves CRS / grid alignment  
- 🔐 Preserves all CARE/H3 governance metadata  
- 🧾 Emplaces proper STAC QA metadata fields:
  - `kfm:qa_flag_schema`
  - `kfm:qa_values`
  - `kfm:qa_interpretation`
  - `kfm:qa_confidence_score`  
- 🧭 Attaches correct PROV-O lineage entries  

All of these MUST pass before QA-enhanced data enters downstream uncertainty, masking, STAC, DCAT, and Focus Mode v3.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/qa_integration/tests/
├── 📄 README.md                             # This file
│
├── 🧪 test_integrate_qa.py                  # Tests full QA merge behavior
├── 🧪 test_rfi_decoding.py                  # Tests raw RFI → KFM semantic mapping/decoding
├── 🧪 test_qa_mappings.py                   # Tests NASA QA → KFM QA schema normalization
├── 🧪 test_uncertainty_postqa.py            # Tests QA-influenced uncertainty propagation
├── 🧪 test_governance_preservation.py       # Validates CARE/H3 metadata survival
│
└── 🔧 fixtures/                             # Synthetic QA/RFI test data
    ├── sample_preqa.tif
    ├── sample_postqa_expected.tif
    ├── sample_rfi_flags.json
    ├── sample_qa_metadata.json
    └── schema_expected.json
~~~

---

## 🧩 3. Test Domains

### ✔ Radiometer QA Merging  
- Combines L2 + L3 QA layers  
- Validates QA codes exist and conform to NASA schema  
- Verifies presence of FT-QA, VWC-QA, soil-moisture QA fields  

### ✔ RFI Decoding  
- Parses raw RFI bitfields  
- Maps codes → KFM interpretation  
- Ensures RFI scaling influences uncertainty correctly  

### ✔ KFM Unified QA Schema  
Verifies correctness of:

- `kfm:qa_flag_schema`  
- `kfm:qa_values`  
- `kfm:qa_interpretation`  
- `kfm:qa_confidence_score`  

### ✔ Uncertainty Propagation  
- QA-induced uncertainty NEVER decreases artificially  
- Uncertainty floors remain intact  
- Noise propagation matches KFM uncertainty rules  

### ✔ Governance Preservation  
- CARE metadata retained  
- H3 sovereignty flags retained  
- `"kfm:mask_required"` set appropriately  
- No sharpening of spatial detail near sensitive areas  

### ✔ STAC/DCAT/PROV-O Readiness  
- Correct projection metadata  
- QA asset shape validation  
- Required STAC extensions present  
- PROV-O lineage relations included  

---

## 🔐 4. Governance & Sovereignty Enforcement

QA/RFI tests MUST ensure:

- No test introduces sensitive, real-world data  
- Synthetic coordinates avoid actual sovereign lands  
- CARE/H3 behavior is exercised using mocked geometry  
- Uncertainty inflation near sovereign lands is **never suppressed**  
- Pixel masking implications are correctly propagated  

These are validated through:

- `faircare_validate.yml`
- `jsonld_validate.yml`
- `data_pipeline.yml`
- `stac_validate.yml`  

---

## 🧪 5. CI Integration

This test suite runs under:

- **ci.yml** — unit + integration  
- **data_pipeline.yml** — ETL graph test  
- **stac_validate.yml** — QA metadata correctness  
- **faircare_validate.yml** — governance compliance  
- **jsonld_validate.yml** — ontology correctness  

Any failure → **CI hard fail**.

---

## 🔁 6. Placement in the SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration (TESTS HERE)
 → uncertainty propagation
 → governance masking (CARE/H3)
 → STAC/DCAT metadata generation
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
- Filters unreliable soil-moisture pixels  
- Improves flood/wetness modeling  

### Climate  
- Improves freeze-thaw reliability  
- Enhances VWC seasonal interpretation  

### Archaeology  
- Reduces misleading environmental context in high-QA-uncertainty regions  

### Story Node v3  
- Integrates QA-derived reliability cues into narrative rendering  

### Focus Mode v3  
- Uses QA signals to weight contextual environmental interpretations  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                 |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full QA Integration Test Suite README; emoji layout; governance/H3; STAC/DCAT/PROV compliance; CI-safe. |
| v10.3.2 | 2025-11-14 | Pre-v11 basic test index.                                                                                |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 QA Integration Fixtures](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

