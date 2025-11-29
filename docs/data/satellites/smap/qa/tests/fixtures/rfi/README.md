---
title: "📦 NASA SMAP — RFI QA Fixtures (Contamination Masks · Bitfields · Sovereignty-Safe · Deterministic)"
path: "docs/data/satellites/smap/qa/tests/fixtures/rfi/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Synthetic QA Fixtures"
status: "Active / Enforced"
release_stage: "Stable · Governed"
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

fair_category: "F1-A1-I2-R5"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
risk_category: "Medium–High"
redaction_required: true

data_steward: "SMAP QA Subcommittee · Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-rfi-qa-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-rfi-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:rfi-qa-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-rfi-qa-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/qa/tests/fixtures/rfi/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next RFI fixture schema update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **SMAP RFI QA — Synthetic Test Fixtures**  
`docs/data/satellites/smap/qa/tests/fixtures/rfi/README.md`

**Purpose**  
Provide **synthetic, deterministic, sovereignty-safe** RFI QA test fixtures used to validate  
bitfield decoding, contamination detection, spatial alignment, governance propagation,  
uncertainty impacts, and STAC/DCAT/PROV-O metadata correctness.

</div>

---

## 📘 1. Overview

These fixtures simulate diverse **radio frequency interference (RFI)** conditions for the  
SMAP QA system. They are intentionally synthetic, engineered to:

- 📡 test RFI bitfield decoding  
- 🚨 validate contamination detection & classification  
- 🗺 ensure CRS + pixel alignment during ETL  
- 🛡 validate CARE/H3 sovereignty masking rules  
- 📉 verify RFI → uncertainty impacts (Stage 5)  
- 📑 validate STAC/DCAT metadata integration  
- 🔗 validate PROV-O lineage referencing  
- 🎯 provide deterministic results for CI pipelines  

No real RFI patterns or geographies are included.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/tests/fixtures/rfi/
├── 📄 README.md                               # This file
│
├── 📡 sample_rfi_mask.tif                     # Synthetic RFI contamination mask
├── 📝 sample_rfi_codes.json                   # Mapping of RFI bitfields → semantic QA states
├── 📑 sample_metadata.json                    # Metadata stub (STAC/DCAT + governance)
│
├── 🎯 expected_rfi_interpretation.json        # Deterministic RFI decoding + classification result
└── 🗂️ schema_expected.json                    # Strict validation schema for RFI QA fixtures
~~~

---

## 🧩 3. Fixture Responsibilities

### 📡 `sample_rfi_mask.tif`
Simulates:

- direct RFI contamination  
- moderate interference  
- ambiguous spectral anomalies  
- clean areas  
- sovereign crossover regions (synthetic only)  

Used to validate:

- contamination classification  
- RFI → uncertainty multipliers  
- CRS/pixel alignment  
- sovereignty masking & generalization  

---

### 📝 `sample_rfi_codes.json`
Defines:

- valid RFI bitfield patterns  
- SMAP → KFM unified QA-code mapping  
- contamination severity ordering  
- allowed QA transitions  

Ensures **decoder determinism** across runs.

---

### 📑 `sample_metadata.json`
Synthetic STAC/DCAT metadata including:

- `"kfm:qa_values"` for RFI  
- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- provenance anchors  
- temporal & spatial metadata  

Used to validate metadata preservation across ETL.

---

### 🎯 `expected_rfi_interpretation.json`
Contains deterministic expected output for:

- QA severity per pixel  
- ambiguous/intermediate states  
- sovereign masking  
- uncertainty-scaling behavior  
- classification groupings  

Used to validate test logic.

---

### 🗂️ `schema_expected.json`
Enforces:

- fixture schema correctness  
- valid bit ranges  
- required governance fields  
- STAC/DCAT QA metadata structure  
- PROV-O linkage  
- deterministic ordering  

Any mismatch → **CI hard block**.

---

## 🔐 4. FAIR+CARE & Sovereignty Compliance

RFI can correlate with infrastructure or land-use patterns.  
Fixtures enforce:

- `"kfm:care_label"` & `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"` propagation  
- `"kfm:mask_required"` for synthetic sovereign intersections  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  

Ensuring no sensitive pattern leakage.

Governance validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. Validation Workflow

Tests consuming these fixtures validate:

- bitfield decoding  
- contamination classification  
- QA → uncertainty integration  
- sovereignty-safe masking  
- metadata integrity  
- CRS/pixel alignment  
- deterministic behavior  
- STAC/DCAT/PROV-O compliance  

---

## 🔁 6. RFI QA in the SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → radiometer QA
 → QA/RFI integration (validated here)
 → retrieval QA
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Improves reliability of SM infiltration & anomaly detection.

### Climate  
Reduces misclassification in FT/VWC anomalies.

### Archaeology  
Protects culturally sensitive landscapes from overspecified environmental signals.

### Story Node v3  
RFI QA influences narrative reliability.

### Focus Mode v3  
Interference signals adjust reasoning confidence.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                           |
|--------:|------------|---------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial RFI QA fixture README; FAIR+CARE/H3 aligned; CI-safe; STAC/DCAT/PROV-O integrated; emoji-rich. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 RFI QA Tests](../../../rfi/tests/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

