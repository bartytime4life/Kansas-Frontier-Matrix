---
title: "📦 NASA SMAP — Vegetation Water Content (VWC) Retrieval QA Fixtures (Synthetic · Deterministic · Sovereignty-Safe)"
path: "docs/data/satellites/smap/qa/tests/fixtures/retrieval_vwc/README.md"
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
public_exposure_risk: "Medium"
risk_category: "Medium"
redaction_required: true

data_steward: "SMAP QA Subcommittee · Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-retrieval-vwc-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-retrieval-vwc-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:retrieval-vwc-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-retrieval-vwc-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/qa/tests/fixtures/retrieval_vwc/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next VWC QA fixture revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **SMAP Vegetation Water Content (VWC) Retrieval QA — Synthetic Test Fixtures**  
`docs/data/satellites/smap/qa/tests/fixtures/retrieval_vwc/README.md`

**Purpose**  
Provide **synthetic, deterministic, sovereignty-safe** test assets for validating  
VWC retrieval QA decoding, ambiguity classification, uncertainty impacts,  
governance metadata propagation, and STAC/DCAT/PROV-O correctness  
within the SMAP QA pipeline.

</div>

---

## 📘 1. Overview

These fixtures validate:

- 🌱 VWC retrieval confidence decoding  
- ⚠️ ambiguous/mixed vegetation–soil states  
- 🌿 canopy-driven retrieval instability  
- 📡 RFI-driven VWC degradation (synthetic)  
- 🌡️ VWC ↔ FT interaction patterns  
- 🗺 CRS + pixel grid alignment  
- 🛡 sovereignty-safe generalization  
- 📉 QA → uncertainty scaling (Stage 5)  
- 📑 STAC/DCAT metadata preservation  
- 🔗 PROV-O lineage correctness  
- 🎯 deterministic CI behavior  

All fixtures contain **synthetic** data—NO real SMAP VWC values appear.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/tests/fixtures/retrieval_vwc/
├── 📄 README.md                                     # This file
│
├── 🌱 sample_vwc_conf.tif                           # Synthetic VWC retrieval confidence raster
├── ⚠️ sample_vwc_qa_mask.tif                        # Ambiguous/low-confidence mask
├── 📑 sample_metadata.json                          # STAC/DCAT QA metadata stub
│
├── 🎯 expected_vwc_interpretation.json              # Deterministic QA decoding + classification
└── 🗂️ schema_expected.json                          # Strict validation schema
~~~

---

## 🧩 3. Fixture Responsibilities

### 🌱 `sample_vwc_conf.tif`
Simulates:

- low/medium/high VWC confidence  
- canopy-density–driven uncertainty  
- RFI-affected retrievals  
- mixed soil–vegetation pixels  
- sovereign-safe generalization boundaries  

Used for:

- decoding tests  
- QA → uncertainty propagation  
- CARE/H3 sovereignty masking checks  
- spatial-alignment validation  

---

### ⚠️ `sample_vwc_qa_mask.tif`
Represents ambiguous VWC pixels:

- canopy saturation  
- mixed VWC states  
- noise-driven uncertainty  
- synthetic eco-boundaries (never real)  

Used to test:

- ambiguity detection  
- uncertainty inflation  
- sovereign masking rules  

---

### 📑 `sample_metadata.json`
Synthetic metadata includes:

- `"kfm:qa_values"` for VWC  
- QA schema descriptors  
- CARE/H3 sovereignty metadata  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- PROV-O entrypoints  
- temporal + spatial metadata matching STAC/DCAT patterns  

---

### 🎯 `expected_vwc_interpretation.json`
Deterministic expected output for:

- VWC classification (high / medium / low / ambiguous)  
- sovereign-generalized versions  
- uncertainty scaling logic  
- QA summary generation  
- classification stability  

Used for CI exact-match testing.

---

### 🗂️ `schema_expected.json`
Defines strict validation rules:

- allowed confidence ranges  
- QA → classification structure  
- governance/sovereignty metadata requirements  
- STAC/DCAT QA metadata formatting  
- PROV-O lineage keys  
- JSON type correctness  
- deterministic ordering  

Any deviation fails CI.

---

## 🔐 4. FAIR+CARE & Sovereignty Requirements

Fixtures enforce:

- `"kfm:care_label"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  

All data is synthetic and **never** reflects real ecological/cultural gradients.

Governance validated by:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. Validation Workflow

Tests consuming these fixtures verify:

- correct QA decoding  
- ambiguous-pixel detection  
- sovereignty-safe uncertainty behavior  
- metadata correctness  
- PROV-O lineage linkage  
- CRS alignment  
- deterministic classification  

---

## 🔁 6. VWC QA in the SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → VWC retrieval QA (validated here)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. KFM Applications

### Hydrology  
Vegetation–soil interactions interpreted with QA protections.

### Climate  
Robust VWC anomaly trends with sovereign-safe uncertainty floors.

### Archaeology  
Avoid misinterpreting vegetation signals near cultural landscapes.

### Story Node v3  
Narratives integrate QA-weighted vegetation context.

### Focus Mode v3  
Confidence drives reasoning weight & narrative emphasis.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                    |
|--------:|------------|------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial VWC QA fixture README; FAIR+CARE/H3 aligned; CI-safe; STAC/DCAT/PROV integrated; emoji-rich.        |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 VWC Retrieval QA Tests](../../../retrieval/tests/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

