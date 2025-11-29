---
title: "📦 NASA SMAP — Retrieval QA Test Fixtures (SM · FT · VWC · Sovereignty-Safe Synthetic Assets)"
path: "docs/data/satellites/smap/qa/retrieval/tests/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · SMAP QA Subcommittee · FAIR+CARE Council Oversight"
status: "Active / Enforced"

classification: "Public Synthetic Test Fixtures"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/sat-smap-v11.json"

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

data_steward: "SMAP QA Subcommittee · Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../../schemas/json/tests-smap-retrieval-qa-v11.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/tests-smap-retrieval-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:retrieval-qa-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-retrieval-qa-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/qa/retrieval/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon Retrieval QA fixture update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **SMAP Retrieval QA — Test Fixtures (SM · FT · VWC)**  
`docs/data/satellites/smap/qa/retrieval/tests/fixtures/README.md`

**Purpose**  
Provide **synthetic, deterministic, FAIR+CARE + sovereignty-safe test datasets**  
used to validate the Retrieval QA layers for Soil Moisture (SM), Freeze–Thaw (FT),  
and Vegetation Water Content (VWC) within the governed KFM v11.2 ETL chain.

</div>

---

## 📘 1. Overview

These fixtures validate:

- 🎚️ retrieval confidence decoding  
- 🌡️ freeze–thaw QA boundaries under noisy conditions  
- 🌱 VWC retrieval uncertainty behavior  
- 🗺 pixel-level geolocation & CRS alignment  
- 🛡 sovereignty-aware masking (H3-region protection)  
- 📉 QA → uncertainty scaling interactions  
- 📑 STAC/DCAT QA metadata  
- 🔗 PROV-O lineage representation  
- deterministic outputs across CI runs  

All fixture data is **synthetic** and intentionally **non-representative** of real SMAP values  
to protect sensitive sovereign territories and avoid accidental leakage of meaningful patterns.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/retrieval/tests/fixtures/
├── 📄 README.md                                  # This file
│
├── 🎚️ sample_sm_conf.tif                         # Soil moisture retrieval confidence (synthetic)
├── 🌡️ sample_ft_conf.tif                          # Freeze–Thaw retrieval confidence (synthetic)
├── 🌱 sample_vwc_conf.tif                         # VWC retrieval confidence (synthetic)
│
├── 📝 sample_metadata.json                       # STAC/DCAT QA metadata block
│
├── 🎯 expected_sm_classification.json            # Expected SM QA decoding
├── 🎯 expected_ft_classification.json            # Expected FT QA decoding
├── 🎯 expected_vwc_classification.json           # Expected VWC QA decoding
│
└── 🗂️ schema_expected.json                       # Validation schema for fixture structure
~~~

---

## 🧩 3. Fixture Responsibilities

### 🎚️ `sample_sm_conf.tif`
Tests:

- SM retrieval confidence range correctness  
- handling of ambiguous retrievals  
- sovereignty-safe suppression inside synthetic H3 zones  
- correct integration with uncertainty scaling rules  

---

### 🌡️ `sample_ft_conf.tif`
Tests:

- freeze–thaw transition QA boundaries  
- early/late-season classification uncertainty  
- mixed-pixel ambiguity  
- sovereignty/climate sensitive zones (synthetic)  

---

### 🌱 `sample_vwc_conf.tif`
Tests:

- canopy-driven retrieval instability  
- low-confidence vegetation-water estimation  
- expected governance masking behavior  
- QA → uncertainty relationships  

---

### 📝 `sample_metadata.json`
Validates metadata fields for:

- STAC QA fields (`kfm:qa_values`, QA schema)  
- DCAT quality notes  
- CARE label propagation  
- sovereignty/H3 metadata inclusion  
- PROV-O lineage hooks  

---

### 🎯 `expected_*_classification.json`
These files store deterministic decoding results for:

- SM QA  
- FT QA  
- VWC QA  

Used to validate:

- decoding logic  
- classification stability  
- uncertainty assignment  
- sovereignty-safe output behavior  

---

### 🗂️ `schema_expected.json`
Defines fixture validation rules:

- allowed QA ranges  
- required metadata keys  
- strict governance-field presence  
- spatial metadata expectations  
- provenance-field patterns  
- QA → uncertainty integration checks  

Any fixture mismatch → **CI hard-fail**.

---

## 🔐 4. FAIR+CARE & Sovereignty Compliance

Fixtures enforce:

- `"kfm:care_label"` stability  
- `"kfm:h3_sensitive"` propagation  
- `"kfm:mask_required"` when QA intersects synthetic protected regions  
- `"kfm:sovereignty_uncertainty_floor"` consistency  
- `"kfm:care_label_reason"` clarity  
- `"kfm:governance_notes"` inclusion  

No fixture reveals meaningful environmental information.

---

## 🧪 5. Validation Workflow

Tests built from these fixtures verify:

- QA confidence decoding  
- QA → uncertainty linkage  
- sovereignty-safe QA outputs  
- STAC/DCAT QA metadata correctness  
- PROV-O lineage completeness  
- deterministic ordering of QA values  

Executed via:

- `ci.yml`  
- `data_pipeline.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `faircare_validate.yml`

---

## 🔁 6. Place in SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → retrieval QA (fixtures validate decoding here)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. Applications in KFM

### Hydrology  
QA informs the quality of SM anomalies.

### Climate  
FT/VWC anomaly confidence derived from this QA.

### Archaeology  
Environmental signals filtered through QA for safe interpretation.

### Story Node v3  
Retrieval QA shapes narrative reliability weighting.

### Focus Mode v3  
QA confidence → explanation strength & uncertainty.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                    |
|--------:|------------|------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Retrieval QA fixture README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV-O integrated; CI-safe; emoji-rich.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 Retrieval QA Tests](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

