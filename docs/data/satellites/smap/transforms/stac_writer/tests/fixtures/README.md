---
title: "📦 NASA SMAP — STAC Writer Test Fixtures (Collections · Items · Assets · Governance · Provenance)"
path: "docs/data/satellites/smap/transforms/stac_writer/tests/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · STAC Review Board · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public Test Fixtures"
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
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-stac-writer-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-stac-writer-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:stac-writer-tests-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-stac-writer-tests-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/transforms/stac_writer/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next fixture revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — STAC Writer Test Fixtures**  
`docs/data/satellites/smap/transforms/stac_writer/tests/fixtures/README.md`

**Purpose**  
Provide deterministic, sovereignty-safe, FAIR+CARE-compliant synthetic datasets used  
to validate STAC Collections, Items, Assets, Governance metadata, DCAT metadata,  
and PROV-O lineage emitted by the **STAC Writer (Final ETL Stage)**.

</div>

---

## 📘 1. Overview

These fixtures validate that generated STAC metadata is:

- ✔ STAC v1.0 compliant  
- ✔ KFM-STAC v11 compliant  
- ✔ DCAT v3 aligned  
- ✔ PROV-O lineage correct  
- ✔ Governance metadata complete (CARE/H3/sensitivity)  
- ✔ Uncertainty metadata consistent with ETL Stage 5  
- ✔ QA metadata preserved  
- ✔ CRS + projection metadata valid  
- ✔ No sensitive geography leaked  
- ✔ No unmasked values inside H3 sovereign zones  

Fixtures are fully synthetic and contain NO real-world sensitive data.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/stac_writer/tests/fixtures/
├── 📄 README.md                                 # This file
│
├── 🛰️ sample_processed_raster.tif               # Processed SMAP raster before STAC writing
├── 🛰️ sample_qa_mask.tif                        # QA mask (synthetic)
├── 📉 sample_uncertainty.tif                    # Uncertainty grid (synthetic)
├── 🛡 sample_governance_mask.tif                # Governance/H3 mask (synthetic)
│
├── 🧾 sample_governance_metadata.json           # CARE/H3 governance metadata block
├── 🔗 sample_provenance_input.json              # PROV-O inputs used during STAC creation
│
├── 📄 expected_stac_item.json                   # Expected Item JSON (CI reference)
├── 📄 expected_stac_collection.json             # Expected Collection JSON (CI reference)
│
└── 🔧 schema_expected.json                      # Schema for verifying fixture integrity
~~~

---

## 🧩 3. Fixture Responsibilities

### 🛰️ sample_processed_raster.tif  
Simulates a **final post-governance raster** ready for STAC inclusion.  
Used to validate:

- projection/raster extension blocks  
- asset definitions  
- bbox/geometry reconstruction  

### 🛰️ sample_qa_mask.tif  
Synthetic QA mask verifying:

- correct asset roles (`qa`)  
- boolean mask correctness  
- QA metadata mapping  

### 📉 sample_uncertainty.tif  
Tests:
- uncertainty asset correctness  
- uncertainty floors encoded in metadata  
- pixel-level alignment with the primary raster  

### 🛡 sample_governance_mask.tif  
Validates:
- `"kfm:mask_required"` asset output  
- sovereignty-protected areas masked correctly  
- governance extension metadata applied  

### 🧾 sample_governance_metadata.json  
Tests:
- CARE/H3 metadata block  
- sovereignty metadata  
- mask reasoning (`"kfm:care_label_reason"`)  
- governance timestamps  

### 🔗 sample_provenance_input.json  
Used to validate:

- correct PROV-O graph embedding  
- `"prov:wasGeneratedBy"`  
- `"prov:used"` chain (decode → reprojection → calibration → QA → uncertainty → governance → STAC Writer)  

### 📄 expected_stac_item.json / expected_stac_collection.json  
Gold-standard reference objects used in CI to ensure:

- deterministic field ordering  
- correct extension usage  
- valid geometry and bbox  
- correct governance metadata  
- correct uncertainty metadata  
- correct QA metadata  
- accurate provenance graph  

### 🔧 schema_expected.json  
Defines the **allowed structure** of:

- fixture rasters  
- fixture metadata  
- expected STAC Items  
- expected governance blocks  
- required provenance fields  
- required uncertainty attributes  

Ensures tests fail if fixtures are malformed or incomplete.

---

## 🔐 4. Governance, Sovereignty & FAIR+CARE Requirements

Fixtures validate that:

- no unmasked values appear in sovereign H3 regions  
- `"kfm:mask_required"` is correctly set  
- `"kfm:h3_sensitive"` propagated  
- `"kfm:sovereignty_uncertainty_floor"` included  
- CARE labels preserved and correctly surfaced  
- governance lineage is complete  
- uncertainty never decreases in sensitive areas  
- STAC Items include all required `"kfm:*"` metadata  

CI runs via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. QA & Validation

These fixtures drive tests that validate:

- STAC Collection schema  
- STAC Item schema  
- Asset-level correctness  
- Governance extension validity  
- CARE/H3 metadata presence  
- DCAT Dataset generation  
- PROV-O lineage  
- geometric correctness  
- sovereignty-aware masking  
- uncertainty & QA metadata linking  
- deterministic output ordering  

---

## 🔁 6. Role in the Full SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → STAC Writer (validated by these fixtures)
 → STAC/DCAT publication
 → PROV-O lineage archival
~~~

These fixtures help guarantee **safe-to-publish**, **governed**,  
**scientifically sound** SMAP datasets.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Governed & uncertainty-aware SMAP soil-moisture STAC archives.

### Climate  
FT/VWC anomaly STAC collections integrated with QA + uncertainty.

### Archaeology  
Sensitive landscape protections preserved in STAC metadata.

### Story Node v3  
Rich governance + uncertainty metadata powering environmental narratives.

### Focus Mode v3  
STAC-backed environmental reasoning, sovereignty-aware.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                      |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full STAC Writer fixture README; emoji layout; governance/uncertainty/QA/PROV aligned; CI-safe.             |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 STAC Writer Tests](../README.md) · [🛡 Governance Standards](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

