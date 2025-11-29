---
title: "📦 NASA SMAP — VWC Retrieval QA Test Fixtures (Synthetic · Deterministic · Sovereignty-Safe)"
path: "docs/data/satellites/smap/qa/vegetation_water/tests/fixtures/README.md"
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

sbom_ref: "../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

json_schema_ref: "../../../../../../../../../schemas/json/tests-smap-vwc-qa-v11.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/tests-smap-vwc-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:vwc-qa-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-vwc-qa-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/qa/vegetation_water/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next VWC QA fixture update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **SMAP Vegetation Water Content (VWC) Retrieval QA — Test Fixtures**  
`docs/data/satellites/smap/qa/vegetation_water/tests/fixtures/README.md`

**Purpose**  
Provide **synthetic, deterministic, FAIR+CARE + sovereignty-safe** test fixtures  
to validate VWC QA decoding, ambiguity detection, metadata preservation,  
sovereignty masking, uncertainty scaling, and PROV-O lineage in the  
KFM v11.2 SMAP ETL pipeline.

</div>

---

## 📘 1. Overview

These fixtures validate:

- 🌱 VWC retrieval confidence decoding  
- 🎚️ confidence → classification logic  
- ⚠️ ambiguous/mixed-pixel detection  
- 🌡️ VWC ↔ FT interaction sensitivity  
- 🗺️ CRS + grid alignment  
- 🛡 governance (CARE/H3) propagation  
- 📉 QA → uncertainty scaling  
- 📑 STAC/DCAT QA metadata correctness  
- 🔗 PROV-O lineage integrity  
- 🚫 sovereignty-safe generalization for sensitive ecological areas  

All fixtures are **synthetic** and **CI-fast**, containing **NO real SMAP values**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/vegetation_water/tests/fixtures/
├── 📄 README.md                                   # This file
│
├── 🌱 sample_vwc_conf.tif                         # Synthetic VWC confidence raster
├── ⚠️ sample_vwc_qa_mask.tif                      # Low-confidence / ambiguous retrieval mask
├── 📑 sample_metadata.json                        # Metadata stub for VWC QA layer
│
├── 🎯 expected_vwc_interpretation.json            # Deterministic VWC QA decoding
└── 🗂️ schema_expected.json                        # Strict validation schema for all fixtures
~~~

---

## 🧩 3. Fixture Responsibilities

### 🌱 `sample_vwc_conf.tif`
Tests:

- valid confidence range behavior  
- canopy-driven retrieval instability  
- synthetic vegetation gradients  
- sovereignty masking inside H3-sensitive zones  
- interaction with uncertainty propagation  

---

### ⚠️ `sample_vwc_qa_mask.tif`
Represents ambiguous or unreliable pixels.  
Used to validate:

- mixed vegetation–soil pixels  
- RFI-interfered retrievals  
- seasonal instability  
- synthetic ecological transitions  
- sovereign-safe masking behavior  

---

### 📑 `sample_metadata.json`
Validates:

- STAC QA scheme (`kfm:qa_values`)  
- DCAT metadata  
- `"kfm:care_label"` and `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- temporal and spatial metadata correctness  
- PROV-O linkage  

---

### 🎯 `expected_vwc_interpretation.json`
Provides the deterministic classification for test scenarios:

- high/medium/low confidence  
- ambiguous transitions  
- uncertainty scaling multipliers  
- governance-driven suppression  
- H3 propagation  

This ensures stable decoding behavior across CI runs.

---

### 🗂️ `schema_expected.json`
Defines strict validation rules:

- QA field ranges  
- required metadata keys  
- sovereignty + CARE metadata presence  
- STAC/DCAT QA structure  
- PROV-O constraints  
- correct JSON typing  
- consistency rules across fixtures  

Any mismatch → **CI block**.

---

## 🔐 4. FAIR+CARE & Sovereignty Compliance

Fixtures enforce:

- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:care_label_reason"`  
- `"kfm:governance_notes"`  

VWC QA fixtures avoid:

- revealing true vegetation gradients  
- exposing high-resolution ecological signals in sensitive areas  
- embedding real-world seasonal or biomass patterns  

Sovereignty compliance validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. Validation Workflow

Tests using these fixtures verify:

- decoding correctness  
- classification stability  
- uncertainty scaling  
- sovereign masking  
- metadata preservation  
- STAC schema compliance  
- PROV-O lineage correctness  
- deterministic output ordering  

---

## 🔁 6. Position in SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → VWC retrieval QA (validated using these fixtures)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Vegetation filtering informs soil-moisture anomaly detection.

### Climate  
VWC QA supports drought/phenology analysis.

### Archaeology  
Ensures safe environmental interpretations near cultural landscapes.

### Story Node v3  
Narratives weight VWC data by QA confidence.

### Focus Mode v3  
Explanation detail influenced by QA and uncertainty.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                 |
|--------:|------------|---------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial VWC QA fixture README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe; emoji-rich.     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 VWC QA Tests](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

