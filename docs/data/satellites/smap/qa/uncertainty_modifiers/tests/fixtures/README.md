---
title: "📦 NASA SMAP — Uncertainty Modifier Test Fixtures (Synthetic · Deterministic · Sovereignty-Safe)"
path: "docs/data/satellites/smap/qa/uncertainty_modifiers/tests/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Synthetic QA/Uncertainty Fixtures"
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
previous_version_hash: "<previous-sha>"
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

data_steward: "SMAP QA Subcommittee · Earth Systems Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../../../schemas/json/tests-smap-uncertainty-modifiers-v11.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/tests-smap-uncertainty-modifiers-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:uncertainty-modifiers-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-uncertainty-modifiers-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/qa/uncertainty_modifiers/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next uncertainty fixture update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **SMAP QA → Uncertainty Modifier Fixtures**  
`docs/data/satellites/smap/qa/uncertainty_modifiers/tests/fixtures/README.md`

**Purpose**  
Provide **synthetic, deterministic, sovereignty-safe** inputs used to validate the ETL Stage 5  
**Uncertainty Modifier Layer**, ensuring QA signals (Radiometer, RFI, SM/FT/VWC retrieval QA)  
are correctly integrated into uncertainty-scaling and governance-aligned uncertainty floors.

</div>

---

## 📘 1. Overview

These fixtures validate:

- 📉 correct computation of uncertainty multipliers  
- 🎚️ QA → uncertainty integration logic  
- 🌡️ FT-driven uncertainty increases  
- 🌱 VWC ambiguity → increased uncertainty  
- ⚠️ radiometer + RFI anomaly propagation  
- 🗺️ CRS + pixel alignment  
- 🛡 sovereignty floors & masking behavior  
- 📑 STAC/DCAT metadata correctness  
- 🔗 PROV-O lineage references  
- 🚫 no real-world environmental clues in sovereign regions  
- deterministic reproducibility across CI runs  

All fixture data is **purely synthetic**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/uncertainty_modifiers/tests/fixtures/
├── 📄 README.md                                   # This file
│
├── 📉 sample_uncertainty_scale.tif                # Synthetic uncertainty multiplier grid
├── 📑 sample_metadata.json                        # STAC/DCAT + governance metadata stub
│
├── 🎯 expected_uncertainty_output.json            # Deterministic QA → uncertainty classification
└── 🗂️ schema_expected.json                        # Strict validation schema for all fixtures
~~~

---

## 🧩 3. Fixture Responsibilities

### 📉 `sample_uncertainty_scale.tif`
Validates:

- QA-derived uncertainty behavior  
- sovereign H3 uncertainty floors  
- consistent scaling across tiles  
- integration with radiometer/RFI/retrieval QA  
- correct min/max range enforcement  
- no sovereign-zone precision leakage  

---

### 📑 `sample_metadata.json`
Tests correctness of:

- STAC uncertainty metadata  
- DCAT quality notes  
- `"kfm:care_label"` & `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"` & `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- provenance metadata entry points  

---

### 🎯 `expected_uncertainty_output.json`
Defines deterministic expected behavior:

- uncertainty multipliers per QA level  
- sovereign-zone generalization  
- RFI/FT/VWC interaction penalties  
- final sovereignty-aligned uncertainties  

Used by tests for exact matching.

---

### 🗂️ `schema_expected.json`
Enforces constraints:

- allowed uncertainty ranges  
- required metadata fields  
- STAC/DCAT structure  
- PROV-O linkage requirements  
- sovereignty metadata presence  
- correct JSON types  
- deterministic ordering  

Violation → **CI hard fail**.

---

## 🔐 4. FAIR+CARE & Sovereignty Compliance

Fixtures enforce:

- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:care_label_reason"`  
- `"kfm:governance_notes"`  

Uncertainty MUST:
- never decrease in sovereign H3 cells  
- be aggregated to safe precision  
- reflect governance-aligned uncertainty bounds  

Fully validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`
- `stac_validate.yml`
- `data_pipeline.yml`

---

## 🧪 5. Validation Workflow

Tests using these fixtures verify:

- uncertainty scaling logic  
- QA → uncertainty integration  
- sovereign masking rules  
- metadata preservation  
- STAC/DCAT/PROV compliance  
- CRS/pixel alignment  
- deterministic output  

---

## 🔁 6. Placement in SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → retrieval QA (SM/FT/VWC)
 → uncertainty modifiers (validated using these fixtures)
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. Applications in KFM

### Hydrology  
Stronger safeguards for extreme wet/dry anomalies.

### Climate  
FT/VWC seasonal modeling with uncertainty floors.

### Archaeology  
Sovereign-safe environmental interpretation.

### Story Node v3  
Uncertainty influences narrative grading.

### Focus Mode v3  
Uncertainty-aware explanations & reliability scoring.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                          |
|--------:|------------|------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial uncertainty-modifier fixture README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV-ready; CI-safe; emoji-rich.    |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 Uncertainty Tests](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

