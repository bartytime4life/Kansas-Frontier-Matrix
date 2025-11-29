---
title: "📦 NASA SMAP — Uncertainty Modifier Fixtures (QA→Uncertainty · Synthetic · Sovereignty-Safe)"
path: "docs/data/satellites/smap/qa/tests/fixtures/uncertainty_modifiers/README.md"
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

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-uncertainty-modifiers-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-uncertainty-modifiers-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:uncertainty-modifiers-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-uncertainty-modifiers-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/qa/tests/fixtures/uncertainty_modifiers/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next uncertainty-modifier revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **SMAP QA → Uncertainty Modifier Fixtures**  
`docs/data/satellites/smap/qa/tests/fixtures/uncertainty_modifiers/README.md`

**Purpose**  
Provide **synthetic, deterministic, sovereignty-safe** fixture data used to validate  
ETL Stage 5 uncertainty scaling derived from QA layers  
(Radiometer, RFI, SM, FT, VWC), including  
FAIR+CARE governance enforcement, sovereignty floors, STAC/DCAT metadata,  
and PROV-O lineage integrity.

</div>

---

## 📘 1. Overview

These fixtures ensure:

- 📉 correct QA→uncertainty scaling  
- 🎚️ integration of all QA sources (SM/FT/VWC/RFI/Radiometer)  
- 🗺 pixel-level CRS & grid alignment  
- 🛡 `"kfm:sovereignty_uncertainty_floor"` is always upheld  
- ☑️ `"kfm:mask_required"` enforced in sovereign H3 zones  
- 📑 STAC/DCAT uncertainty metadata correctness  
- 🔗 PROV-O lineage connections  
- 🚫 no real-world ecological or cultural patterns leak  
- 🎯 deterministic behavior under CI  

All data is **synthetic**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/tests/fixtures/uncertainty_modifiers/
├── 📄 README.md                                   # This file
│
├── 📉 sample_uncertainty_scale.tif                # Synthetic uncertainty multiplier raster
├── 📑 sample_metadata.json                        # STAC/DCAT + CARE/H3 metadata stub
│
├── 🎯 expected_uncertainty_output.json            # Deterministic expected uncertainty classification
└── 🗂️ schema_expected.json                        # Strict validation schema for all fixture fields
~~~

---

## 🧩 3. Fixture Responsibilities

### 📉 `sample_uncertainty_scale.tif`
Validates:

- QA-derived uncertainty multipliers  
- influence of RFI, Radiometer, SM/FT/VWC QA  
- sovereign-zone uncertainty floors  
- expected scaling ranges (never negative, never > allowed max)  
- CRS/pixel alignment  
- deterministic tile behavior  

---

### 📑 `sample_metadata.json`
Synthetic metadata including:

- `"kfm:uncertainty_schema"`  
- `"kfm:qa_values"` → uncertainty mapping  
- `"kfm:care_label"` & `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- STAC/DCAT fields  
- PROV-O entrypoints  
- spatial + temporal metadata  

Used to validate metadata-preservation logic.

---

### 🎯 `expected_uncertainty_output.json`
Provides the exact, deterministic expected behavior:

- scaled uncertainties for each synthetic QA scenario  
- sovereign-safe generalization  
- uncertainty-floor enforcement  
- classification boundaries  
- QA→uncertainty interactions (e.g., FT ambiguity → higher uncertainty)  
- independence from tile ordering  

Validated via strict equality in test assertions.

---

### 🗂️ `schema_expected.json`
Enforces:

- structural validity  
- correct typing for each field  
- presence of required governance metadata  
- correct STAC/DCAT uncertainty fields  
- PROV-O lineage field conformance  
- deterministic ordering guarantees  

Any mismatch → **CI hard block**.

---

## 🔐 4. FAIR+CARE & Sovereignty Compliance

All fixtures enforce:

- `"kfm:care_label"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  

Uncertainty MUST NEVER:

- decrease inside sovereign H3 zones  
- reveal sensitive gradients  
- contradict sovereignty masking policies  

Governance validated via:

- **faircare_validate.yml**  
- **jsonld_validate.yml**  
- **stac_validate.yml**  
- **data_pipeline.yml**

---

## 🧪 5. CI Validation Workflow

Tests using these fixtures validate:

- QA→uncertainty integration  
- sovereignty-floor consistency  
- metadata preservation (STAC/DCAT/CARE/H3)  
- PROV-O lineage correctness  
- correct CRS & geospatial alignment  
- deterministic output across CI runs  

---

## 🔁 6. Placement in the SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → retrieval QA (SM / FT / VWC)
 → QA → uncertainty modifiers (validated here)
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. KFM Applications

### Hydrology  
Uncertainty-aware soil-moisture anomaly interpretation.

### Climate  
Safe FT/VWC seasonal analysis under sovereignty constraints.

### Archaeology  
Reduces misinterpretation risk for culturally sensitive landscapes.

### Story Node v3  
Uncertainty-weighted narrative evidence.

### Focus Mode v3  
Reasoning influenced by uncertainty confidence weighting.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                             |
|--------:|------------|---------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial uncertainty modifier fixture README; FAIR+CARE/H3 aligned; CI-safe; STAC/DCAT/PROV integrated; emoji-rich. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 Uncertainty Tests](../../../uncertainty_modifiers/tests/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

