---
title: "📦 NASA SMAP — Radiometer QA Test Fixtures (Synthetic · Deterministic · FAIR+CARE/H3-Safe)"
path: "docs/data/satellites/smap/qa/radiometer/tests/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · SMAP QA Subcommittee · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public QA Test Fixtures"
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
care_label: "CARE-A / CARE-B (QA-dependent)"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: false

data_steward: "SMAP QA Subcommittee · Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-radiometer-qa-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-radiometer-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:radiometer-qa-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-radiometer-qa-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/qa/radiometer/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded when fixture logic updates"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **SMAP Radiometer QA — Test Fixtures**  
`docs/data/satellites/smap/qa/radiometer/tests/fixtures/README.md`

**Purpose**  
Provide deterministic, sovereignty-safe, FAIR+CARE-compliant synthetic test assets  
for validating NASA SMAP **Radiometer QA flags**, **QA code tables**, **RFI susceptibility**,  
**governance metadata**, and **STAC-ready QA layers**.

</div>

---

## 📘 1. Overview

These fixtures support tests that validate:

- bitfield → semantic QA decoding  
- QA flag ranges and consistency  
- radiometer QA alignment with reprojected rasters  
- correct mapping to unified KFM QA schema  
- governance metadata correctness  
- CARE/H3 propagation  
- RFI interference logic  
- STAC/DCAT metadata requirements  
- PROV lineage correctness  
- sovereignty-safe QA masking  

Fixtures contain **only synthetic data** and **no actual SMAP QA** to avoid leakage  
of sensitive radiometric patterns in tribal areas.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/radiometer/tests/fixtures/
├── 📄 README.md                           # This file
│
├── ⚠️ sample_qa_flags.tif                 # Synthetic radiometer QA layer (bitmasks)
├── 📝 sample_qa_codes.json                # QA code → meaning mapping (KFM Unified QA schema)
├── 📑 sample_metadata.json                # STAC/DCAT QA metadata block
│
├── 🎯 sample_expected_mask.json           # Expected QA interpretation & classified mask
├── 🗂️ schema_expected.json                # Validation schema for fixture structure & metadata
~~~

---

## 🧩 3. Fixture Responsibilities

### ⚠️ `sample_qa_flags.tif`
A synthetic raster representing:

- beam health indicators  
- channels A/B QA  
- surface contamination  
- RFI susceptibility  
- retrieval confidence constraints  

Used to test:

- bitfield integrity  
- geolocation alignment  
- sovereignty-safe values (H3-masked regions)  

---

### 📝 `sample_qa_codes.json`
Defines:

- all allowed QA codes  
- descriptive meanings  
- severity ordering  
- cross-product applicability (SM/FT/VWC)  
- KFM unified QA schema equivalence  

Tests ensure decoding matches NASA → KFM interpretation rules.

---

### 📑 `sample_metadata.json`
Contains synthetic DCAT/STAC metadata fields:

- QA schema  
- QA values/flags  
- temporal extent  
- CARE/H3 metadata  
- provenance annotations  

Used to validate:

- metadata_utils.py  
- stac_writer governance integration  
- DCAT dataset fields  

---

### 🎯 `sample_expected_mask.json`
Represents expected result of:

- QA bitfield decoding  
- unified QA classification  
- sovereignty masking  
- `"kfm:mask_required"` propagation  
- uncertainty modifier derivation  

Used to ensure deterministic decoding & classification.

---

### 🗂️ `schema_expected.json`
Defines strict rules for all fixtures:

- required keys  
- valid ranges  
- H3 schema structure  
- governance metadata expectations  
- STAC/DCAT compliance  
- PROV-O lineage fields  
- pixel-level QA mask format  

Any violation triggers CI failure.

---

## 🔐 4. Governance, FAIR+CARE, and Sovereignty Compliance

Fixtures enforce:

- `"kfm:care_label"` stability  
- `"kfm:h3_sensitive"` propagation  
- `"kfm:mask_required"` behavior near sovereign lands  
- `"kfm:sovereignty_uncertainty_floor"` consistency  
- NO real-world QA patterns from sensitive regions  
- explicit governance provenance  

Governance validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. QA & Validation

Tests using these fixtures validate:

- QA decoding  
- QA flag ranges  
- spatial alignment  
- STAC integration  
- metadata accuracy  
- governance safety  
- uncertainty modifier integration  
- PROV-O lineage correctness  

All fixtures **must** pass schema checks before QA dataset release.

---

## 🔁 6. Position in SMAP QA Pipeline

~~~text
radiometer QA (this directory)
 → QA/RFI integration (ETL Stage 4)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
 → QA dataset layer (public)
~~~

---

## 🔮 7. KFM Applications

### Hydrology  
QA-based reliability for soil moisture.

### Climate  
RFI-aware QA for FT/VWC anomalies.

### Archaeology  
Governance-safe suppression of questionable QA values.

### Story Node v3  
Confidence scoring based on QA context.

### Focus Mode v3  
Evidence weighting tied to QA flags.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                    |
|--------:|------------|------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial radiometer QA fixture README; emoji-rich; FAIR+CARE/H3 aligned; STAC/DCAT/PROV-O; CI-safe.         |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 Radiometer QA Tests](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

