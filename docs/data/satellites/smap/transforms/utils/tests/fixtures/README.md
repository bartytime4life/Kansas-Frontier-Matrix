---
title: "📦 NASA SMAP — Transform Utility Test Fixtures (Synthetic · Deterministic · FAIR+CARE/H3 Safe)"
path: "docs/data/satellites/smap/transforms/utils/tests/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems QA · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public Utility-Test Fixtures"
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

data_steward: "Earth Systems Working Group · FAIR+CARE Council · QA Subcommittee"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../schemas/json/tests-smap-utils-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/tests-smap-utils-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:utils-test-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-utils-test-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/transforms/utils/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon fixture-set revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — Transform Utility Test Fixtures**  
`docs/data/satellites/smap/transforms/utils/tests/fixtures/README.md`

**Purpose**  
Provide **synthetic, deterministic, sovereignty-safe, FAIR+CARE-aligned**  
fixtures used to test the shared ETL utilities powering  
decode → reprojection → calibration → QA/RFI → uncertainty → governance → provenance → STAC  
for all SMAP-derived datasets in KFM.

</div>

---

## 📘 1. Overview

These fixtures ensure:

- 🧮 numeric utils behave deterministically  
- 🌐 geospatial utils respect CRS/H3 alignment & sovereignty rules  
- 🧾 metadata utils preserve governance, QA, uncertainty, STAC fields  
- 🔐 governance utils apply masking + CARE/H3 rules  
- 📑 JSON-LD utils output valid PROV-O nodes  
- 🪪 id utils generate stable IDs  
- 🔧 I/O utils preserve metadata & nodata integrity  
- 🧬 array utils remain stable + schema-correct  
- 🚫 no fixture contains real-world sensitive data  

All fixtures are **CI-fast**, **repeatable**, and **validatable**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/utils/tests/fixtures/
├── 📄 README.md                         # This file
│
├── 🛰️ sample_raster.tif                 # Synthetic raster for geo/IO tests
├── 🧾 sample_metadata.json              # STAC/DCAT/governance metadata stub
├── 🌐 sample_h3_mask.json               # Synthetic H3 sovereignty mask
│
├── 🧬 sample_prov_stub.json             # PROV-O Entity/Activity/Agent snippet
├── 🪪 sample_ids.json                   # Deterministic ID inputs & expected outputs
│
└── 🔧 schema_expected.json              # Schema for validating fixture structure & contents
~~~

---

## 🧩 3. Fixture Responsibilities

### 🛰️ sample_raster.tif  
Used to validate:

- CRS detection  
- pixel ↔ geo transforms  
- nodata handling  
- sovereignty-aware masking in `geo_utils`  
- array ops consistency  
- safe COG IO behavior  

Raster contains purely synthetic values.

---

### 🧾 sample_metadata.json  
Validates:

- STAC property merging  
- DCAT dataset & distribution fields  
- QA + uncertainty metadata integration  
- CARE/H3 metadata structure  
- `"kfm:*"` fields  
- temporal normalization  

Ensures metadata utils never drop governance fields.

---

### 🌐 sample_h3_mask.json  
Synthetic H3 mask used to test:

- sovereignty masking  
- `"kfm:h3_sensitive"` propagation  
- `"kfm:mask_required"` rules  
- uncertainty-floor enforcement  
- H3 ↔ raster alignment  

Fixtures include:

- parent → child H3 relationships  
- mixed-resolution cells  
- safe synthetic locations  

---

### 🧬 sample_prov_stub.json  
Tests correctness of JSON-LD provenance generation:

- Entity / Activity / Agent structure  
- correct PROV-O relations  
- `"prov:wasGeneratedBy"` consistency  
- `"prov:used"` lists for decode → governance pipeline  
- `"kfm:governance_notes"` propagation  

---

### 🪪 sample_ids.json  
Validates deterministic ID helpers:

- STAC Item ID generation  
- raster + mask + uncertainty asset ID patterns  
- hashing stability  
- no collisions  

Ensures cross-stage reproducibility.

---

### 🔧 schema_expected.json  
Defines validation rules:

- expected keys  
- raster shape patterns  
- metadata structure  
- H3 mask schema  
- PROV-O JSON-LD schema  
- sovereignty + CARE field expectations  
- deterministic ID patterns  

Used in ALL utility tests to ensure fixture correctness.

---

## 🔐 4. Governance, FAIR+CARE & Sovereignty Compliance

Fixtures ensure utility functions:

- never leak sensitive coordinates  
- respect sovereignty-aware generalization  
- apply `"kfm:sovereignty_uncertainty_floor"` logic  
- preserve `"kfm:care_label"`  
- propagate `"kfm:h3_sensitive"`  
- remain compliant with Indigenous Data Protection policies  
- embed governance lineage into PROV-O graphs  

Governance verified via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. QA & Validation

Using these fixtures, tests verify:

- deterministic numeric + geospatial behavior  
- CRS correctness  
- metadata merge accuracy  
- PROV-O JSON-LD validity  
- sovereignty-safe operations  
- correct ID generation  
- consistent IO round-trips  
- stable array transformations  

Any mismatches → **CI pipeline hard-fail**.

---

## 🔁 6. Position in SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
       ↑
  utilities validated with these fixtures
~~~

---

## 🔮 7. Applications Across KFM

### Hydrology  
CRS/metadata/uncertainty correctness for SM products.

### Climate  
Stable VWC/FT/soil-moisture metadata behavior.

### Archaeology  
Generalization + sovereignty protections validated at utility layer.

### Story Node v3  
Correct provenance & metadata driving environmental narratives.

### Focus Mode v3  
Utility stability ensures reliable context explanations.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                       |
|--------:|------------|----------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial utility-fixture README; emoji-rich; FAIR+CARE/H3 aligned; PROV/O/JSON-LD compliant; CI-ready.        |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 Utility Tests](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

