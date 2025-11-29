---
title: "🧪 NASA SMAP — Transform Utilities Test Suite (Numeric · Geo · Metadata · Governance · JSON-LD · IO)"
path: "docs/data/satellites/smap/transforms/utils/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems QA · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public Utility-Test Documentation"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
jsonld_profile: "KFM-JSONLD v11"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B (context-dependent)"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: false

data_steward: "Earth Systems QA Subcommittee · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareTest"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../schemas/json/tests-smap-utils-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/tests-smap-utils-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:utils-tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-utils-tests"
event_source_id: "ledger:docs/data/satellites/smap/transforms/utils/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next utilities overhaul"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **NASA SMAP — Transform Utilities Test Suite**  
`docs/data/satellites/smap/transforms/utils/tests/README.md`

**Purpose**  
Validate the **core shared ETL utilities** used across ALL SMAP ETL stages:  
numeric transforms, geospatial helpers, metadata mergers, governance utilities,  
PROV-O JSON-LD builders, deterministic ID utilities, array handling, and safe I/O.

This suite ensures **determinism**, **FAIR+CARE compliance**, **sovereignty protection**,  
**schema correctness**, and **pipeline stability**.

</div>

---

## 📘 1. Overview

This test suite ensures:

- 🧮 Numeric utilities behave deterministically  
- 🌐 Geospatial helpers (CRS, H3, bbox ops) are correct  
- 🧾 Metadata utils preserve governance + FAIR fields  
- 🔐 Governance utils enforce sovereignty + masking rules  
- 📑 JSON-LD utils emit valid PROV-O structures  
- 🪪 ID utils generate stable IDs  
- 🔧 IO utils preserve metadata and enforce CRS rules  
- 🧬 Array utils remain deterministic and sorted  
- 🚫 No sensitive geographic detail leaks through any utility  
- 📜 All utils obey STAC, DCAT, PROV-O rules where relevant  

Any failure → **halts the entire SMAP ETL pipeline**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/utils/tests/
├── 📄 README.md                               # This file
│
├── 🧪 test_numeric.py                          # Numeric math, scaling, uncertainty helpers
├── 🧪 test_geo_utils.py                        # CRS, bbox, H3, pixel/geo transforms
├── 🧪 test_metadata_utils.py                   # STAC/DCAT metadata merging
├── 🧪 test_governance_utils.py                 # CARE/H3 sovereignty rule enforcement
├── 🧪 test_jsonld_utils.py                     # JSON-LD / PROV-O correctness
├── 🧪 test_id_utils.py                         # Deterministic STAC/ETL ID generation
├── 🧪 test_io_utils.py                         # Safe raster IO, metadata preservation
├── 🧪 test_array_utils.py                      # Deterministic array operations
│
└── 🔧 fixtures/                                # Synthetic deterministic inputs
    ├── sample_raster.tif
    ├── sample_metadata.json
    ├── sample_h3_mask.json
    ├── sample_prov_stub.json
    ├── sample_ids.json
    └── schema_expected.json
~~~

---

## 🧩 3. Test Domains & Expectations

### 🧮 **Numeric Utility Tests**
Validate:

- deterministic operations  
- safe scaling for QA/RFI uncertainty factors  
- correct uncertainty propagation  
- clipping without leaking extreme values  
- sovereignty-aware uncertainty-floor helpers  

---

### 🌐 **Geospatial Utility Tests**
Validate:

- CRS detection + reprojection correctness  
- H3 ↔ raster grid alignment  
- bbox ops (pad, merge, intersect, clamp)  
- sovereignty/H3 generalization correctness  
- no coordinate leaks in sensitive regions  

---

### 🧾 **Metadata Utility Tests**
Validate:

- STAC metadata merging  
- DCAT dataset/asset metadata correctness  
- manage `kfm:*` governance fields  
- integrate QA + uncertainty metadata  
- timeline/temporal normalization  

---

### 🔐 **Governance Utility Tests**
Validate:

- `"kfm:mask_required"` logic  
- `"kfm:h3_sensitive"` propagation  
- `"kfm:care_label"` preservation  
- `"kfm:sovereignty_uncertainty_floor"` logic  
- no false precision  
- no removal of sovereignty metadata  

---

### 📑 **JSON-LD Utility Tests (PROV-O)**
Validate:

- context correctness  
- Entity/Activity/Agent shapes  
- complete lineage  
- schema + SHACL compliance  
- no invented provenance  

---

### 🪪 **ID Utility Tests**
Validate:

- deterministic STAC Item IDs  
- deterministic pipeline Activity IDs  
- reproducible hash/encoded IDs  
- no collision risk in high-volume pipelines  

---

### 🔧 **IO Utility Tests**
Validate:

- safe COG read/write  
- metadata round-trip accuracy  
- nodata handling  
- CRS integrity  
- no metadata loss  

---

### 🧬 **Array Utility Tests**
Validate:

- stable sorting  
- deterministic `unique`  
- reproducible groupings  
- correct QA bitfield extraction  

---

## 🔐 4. Governance & FAIR+CARE Compliance

Utilities under test MUST comply with:

- FAIR principles  
- CARE principles  
- KFM Sovereignty Standards  
- Indigenous Data Protection rules  
- No leakage of precise coordinates  
- No unethical reduction of uncertainty  

Governance validated through:

- `faircare_validate.yml`  
- `jsonld_validate.yml`
- `stac_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. CI Integration

This suite executes automatically under:

- **ci.yml** (unit tests)  
- **data_pipeline.yml** (ETL graph tests)  
- **jsonld_validate.yml** (ontology + provenance checks)  
- **stac_validate.yml** (STAC/D


