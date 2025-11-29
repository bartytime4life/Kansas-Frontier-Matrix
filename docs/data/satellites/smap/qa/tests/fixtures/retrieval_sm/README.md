---
title: "📦 NASA SMAP — Soil Moisture (SM) Retrieval QA Fixtures (Synthetic · Deterministic · Sovereignty-Safe)"
path: "docs/data/satellites/smap/qa/tests/fixtures/retrieval_sm/README.md"
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
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-retrieval-sm-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-retrieval-sm-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:retrieval-sm-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-retrieval-sm-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/qa/tests/fixtures/retrieval_sm/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next SM QA revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **SMAP Soil Moisture (SM) Retrieval QA — Synthetic Test Fixtures**  
`docs/data/satellites/smap/qa/tests/fixtures/retrieval_sm/README.md`

**Purpose**  
Provide **synthetic, deterministic, sovereignty-safe** soil moisture retrieval (SM) QA fixtures  
used to validate QA decoding, classification, uncertainty propagation, governance metadata,  
and STAC/DCAT/PROV-O correctness within the SMAP SM QA pipeline.

</div>

---

## 📘 1. Overview

These fixtures validate:

- 🎚️ SM retrieval confidence decoding  
- ⚠️ ambiguous/noisy SM retrieval states  
- 🌱 soil–canopy interaction ambiguity patterns  
- 🗺 CRS and pixel alignment  
- 🛡 CARE/H3 sovereignty metadata  
- 📉 QA → uncertainty multiplier correctness  
- 📑 STAC/DCAT QA metadata structure  
- 🔗 PROV-O lineage linkage  
- 🎯 deterministic QA decoding across CI runs  

No fixture contains any real SMAP soil-moisture values — all data is synthetic.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/tests/fixtures/retrieval_sm/
├── 📄 README.md                                  # This file
│
├── 🎚️ sample_sm_conf.tif                         # Synthetic SM retrieval confidence raster
├── 📑 sample_metadata.json                        # STAC/DCAT QA metadata stub
│
├── 🎯 expected_sm_classification.json            # Deterministic SM QA decoding/classification
└── 🗂️ schema_expected.json                        # Strict validation schema for fixture correctness
~~~

---

## 🧩 3. Fixture Responsibilities

### 🎚️ `sample_sm_conf.tif`
Simulates:

- low/medium/high SM retrieval confidence  
- ambiguous retrieval zones  
- synthetic canopy interference  
- RFI/FT-influenced ambiguity  
- sovereign-region generalization  

Used for:

- confidence decoding tests  
- uncertainty scaling checks  
- sovereignty masking tests  
- pixel-level CRS alignment validation  

---

### 📑 `sample_metadata.json`
Contains synthetic metadata fields:

- `kfm:qa_values` for SM  
- STAC QA schema entries  
- CARE label fields  
- sovereignty/H3 metadata  
- `"kfm:mask_required"` logic  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- PROV-O root references  
- temporal/spatial metadata  

Tests ensure metadata consistency after ETL transformation.

---

### 🎯 `expected_sm_classification.json`
Provides deterministic output for:

- SM QA confidence → classification  
- ambiguous region tagging  
- sovereign-region generalization  
- QA → uncertainty mapping  
- governance enforcement outcomes  

Used for exact-match CI validation.

---

### 🗂️ `schema_expected.json`
Validates:

- required QA fields  
- correct SM QA classification schema  
- sovereignty metadata  
- STAC/DCAT compliance  
- PROV-O field presence  
- JSON structure & types  
- deterministic ordering  

Any mismatch → **hard CI failure**.

---

## 🔐 4. FAIR+CARE & Sovereignty Safety

Soil Moisture retrieval QA can indirectly reveal sensitive ecological patterns.  
These fixtures enforce:

- `"kfm:care_label"` propagation  
- `"kfm:h3_sensitive"` tagging  
- `"kfm:mask_required"` and sovereign generalization  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:care_label_reason"`  
- `"kfm:governance_notes"`  

No real soil moisture patterns or gradients are present.

---

## 🧪 5. QA Processes Validated by These Fixtures

- SM QA decoding  
- SM QA → uncertainty propagation  
- sovereign masking in SM QA  
- metadata preservation rules  
- PROV-O lineage building  
- correct CRS alignment  
- deterministic classification  

---

## 🔁 6. SM QA in the SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → SM retrieval QA (validated via these fixtures)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. KFM Applications

### Hydrology  
Soil-moisture anomaly detection with QA-informed reliability.

### Climate  
Better modeling of wet/dry transitions.

### Archaeology  
Environmentally safe SM context for cultural landscape analysis.

### Story Node v3  
Narratives weighted by SM QA reliability.

### Focus Mode v3  
Confidence influences reasoning and narrative emphasis.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                        |
|--------:|------------|----------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial SM Retrieval QA fixture README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe; emoji-rich. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 SM Retrieval QA Tests](../../../retrieval/tests/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

