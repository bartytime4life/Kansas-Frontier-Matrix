---
title: "📦 NASA SMAP — Radiometer QA Fixtures (Beam QA · Channel QA · Bitfield Decoding · Sovereignty-Safe)"
path: "docs/data/satellites/smap/qa/tests/fixtures/radiometer/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Synthetic QA Fixtures"
status: "Active / Enforced"
release_stage: "Stable / Governed"

lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · SMAP QA Subcommittee · FAIR+CARE Council Oversight"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-radiometer-qa-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-radiometer-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:radiometer-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-radiometer-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/qa/tests/fixtures/radiometer/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next Radiometer QA revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **SMAP Radiometer QA — Synthetic Test Fixtures**  
`docs/data/satellites/smap/qa/tests/fixtures/radiometer/README.md`

**Purpose**  
Provide **synthetic, deterministic, sovereignty-safe test datasets** for validating  
SMAP **Radiometer QA** decoding, bitfield interpretation, spatial alignment,  
STAC/DCAT metadata, and CARE/H3 governance propagation.

</div>

---

## 📘 1. Overview

Radiometer QA fixtures are used to validate:

- ⚠️ beam-level QA bitfields  
- 🛰️ channel A/B health indicators  
- ✳️ radiance anomalies (synthetic)  
- 📡 RFI-adjacent QA effects  
- 🗺️ spatial alignment (CRS + pixel grid)  
- 🛡 sovereignty-safe masking behavior  
- 📑 STAC/DCAT QA metadata accuracy  
- 🔗 PROV-O lineage correctness  
- 🎯 deterministic decoding behavior  

ALL fixture content is **synthetic** and **contains no real SMAP signals**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/tests/fixtures/radiometer/
├── 📄 README.md                       # This file
│
├── ⚠️ sample_qa_flags.tif             # Synthetic Radiometer QA bitfield raster
├── 📝 sample_qa_codes.json            # Unified SMAP→KFM QA code mapping
├── 📑 sample_metadata.json            # Metadata stub (STAC/DCAT/CARE/H3)
│
├── 🎯 expected_decoded_qa.json        # Deterministic expected bitfield interpretation
└── 🗂️ schema_expected.json            # Strict validation schema
~~~

---

## 🧩 3. Fixture Responsibilities

### ⚠️ `sample_qa_flags.tif`
Simulates Radiometer QA bitfields including:

- beam saturation  
- missing radiances  
- anomalous brightness temperatures  
- channel-specific faults  
- RFI interference proxies (synthetic)  

Used to test:

- correct QA bit decoding  
- grid integrity  
- alignment with other QA/ETL rasters  
- sovereign masking logic  

---

### 📝 `sample_qa_codes.json`
Defines:

- allowed code ranges  
- SMAP → KFM QA code normalization  
- severity types (OK / caution / warning / fail)  
- semantic names for bitfields  

Used for validating **deterministic decoding** across CI.

---

### 📑 `sample_metadata.json`
Synthetic metadata including:

- QA schema (`kfm:qa_values`)  
- `"kfm:care_label"` & `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- temporal/spatial extents  
- PROV-O entrypoints  

Ensures metadata utils preserve all governance attributes.

---

### 🎯 `expected_decoded_qa.json`
Contains deterministic expected results for:

- decoded QA classes  
- severe/moderate/low QA patterns  
- masked regions inside sovereign H3 areas  
- expected QA summaries for STAC  
- QA → uncertainty implications  

Used to validate decoding logic.

---

### 🗂️ `schema_expected.json`
Enforces:

- required QA keys  
- valid bitfield → semantic mapping  
- governance field presence  
- STAC/DCAT QA field structure  
- JSON typing rules  
- PROV-O structural constraints  
- deterministic ordering  

Any mismatch = **CI hard fail**.

---

## 🔐 4. FAIR+CARE & Sovereignty Compliance

Radiometer QA may reflect sensitive ecological variations; fixtures enforce:

- **no real radiance patterns**  
- `"kfm:care_label"` propagation  
- `"kfm:h3_sensitive"` tagging  
- `"kfm:mask_required"` in synthetic sovereign regions  
- `"kfm:sovereignty_uncertainty_floor"` enforcement  
- `"kfm:governance_notes"` inclusion  

Governance applied during all QA tests under:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. Validation Workflow

This fixture directory supports tests verifying:

- bitfield decoding and semantic mapping  
- QA thresholds and ranges  
- sovereignty-safe output  
- CRS & grid alignment  
- metadata correctness  
- PROV-O lineage integrity  
- deterministic behavior across runs  
- STAC/DCAT QA structure conformance  

---

## 🔁 6. Position in SMAP QA ETL

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration (uses these Radiometer fixtures)
 → retrieval QA
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
QA protects soil-moisture anomaly interpretation.

### Climate  
Stable QA feeds freeze–thaw + VWC modeling.

### Archaeology  
Safe environmental QA reduces misinterpretation risk.

### Story Node v3  
QA influences reliability of contextual environmental narratives.

### Focus Mode v3  
QA informs explanatory weighting & confidence.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                   |
|--------:|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Radiometer QA fixture README; FAIR+CARE/H3 aligned; CI-safe; STAC/DCAT/PROV integrated; emoji-rich.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 Radiometer QA Tests](../../../radiometer/tests/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

