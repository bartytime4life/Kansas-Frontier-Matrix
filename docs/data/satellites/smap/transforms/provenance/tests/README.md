---
title: "🧪 NASA SMAP — Provenance Builder Test Suite (PROV-O · JSON-LD · Governance Lineage) · ETL Stage 7"
path: "docs/data/satellites/smap/transforms/provenance/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Provenance Board · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public PROV-O Test Documentation"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2 (Extended)"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R5"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low"
risk_category: "Medium"
redaction_required: false

data_steward: "KFM Provenance Board · FAIR+CARE Council · Earth Systems Working Group"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareTest"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-provenance-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-provenance-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:provenance-tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-smap-provenance-tests"
event_source_id: "ledger:docs/data/satellites/smap/transforms/provenance/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next provenance-update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **NASA SMAP — Provenance Builder Test Suite (ETL Stage 7)**  
`docs/data/satellites/smap/transforms/provenance/tests/README.md`

**Purpose**  
Validate the completeness, correctness, governance alignment, and sovereignty-aware behavior  
of all **PROV-O lineage graphs** generated during SMAP ETL → before STAC Writer  
emits final STAC/DCAT records.

</div>

---

## 📘 1. Overview

This suite ensures that SMAP PROV-O lineage:

- 🔗 includes **all ETL stages**  
- 🧩 defines correct **Entities, Activities, and Agents**  
- 📄 includes complete **decode → reprojection → calibration → QA/RFI → uncertainty → governance → STAC Writer** chains  
- 🛡 retains all **CARE/H3 sovereignty metadata**  
- 📤 exports valid JSON-LD  
- 📚 passes PROV-O SHACL and JSON Schema rules  
- ⚠️ prevents missing, invented, or conflicting lineage  
- 🧬 ensures reproducibility across runs  
- 🧭 is safe and interpretable for Focus Mode v3 & Story Node v3  

If any test fails, **no STAC Item may be generated**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/provenance/tests/
├── 📄 README.md                                # This file
│
├── 🧪 test_prov_entities.py                     # Validates Entity definitions
├── 🧪 test_prov_activities.py                   # Validates Activity chain correctness
├── 🧪 test_prov_agents.py                       # Validates all Agent definitions
├── 🧪 test_prov_lineage_chain.py                # Ensures decode → STAC Writer chain is complete
├── 🧪 test_jsonld_validity.py                   # JSON-LD + PROV-O schema conformance
│
└── 🔧 fixtures/                                 # Deterministic synthetic lineage data
    ├── sample_etl_inputs.json                   # Synthetic decode → governance inputs
    ├── synthetic_agent_defs.json                # Agent registry stubs
    ├── synthetic_entity_defs.json               # Entity structure stubs
    ├── sample_prov_expected.json                # Expected final PROV graph
    └── schema_expected.json                     # Validation schema for fixtures
~~~

---

## 🧩 3. Test Domains & Requirements

### 🔗 **Entity Tests (prov:Entity)**
Validate:

- all required entities exist (rasters, masks, QA, uncertainty, metadata)  
- `"kfm:*"` governance metadata attached when applicable  
- sovereignty tags preserved  

### 🎛 **Activity Tests (prov:Activity)**
Validate:

- decode, reprojection, calibration, QA/RFI, uncertainty, governance, provenance, STAC writer  
- all Activities have timestamps  
- all Activities are ordered correctly  
- Activities use appropriate provenance relations  

### 👤 **Agent Tests (prov:Agent)**
Validate:

- pipelines, councils, working groups, AI agents, and external NASA agents  
- correct `"prov:actedOnBehalfOf"` relationships  
- sovereignty/governance agents represented  

### 🔗 **Lineage Chain Tests**
Validate:

- no broken links  
- no missing transformations  
- no invented transformations  
- `"prov:wasGeneratedBy"` and `"prov:used"` relationships complete  

### 📄 **JSON-LD Validity Tests**
Validate:

- context correctness  
- PROV-O terms valid  
- no undefined JSON-LD types  
- correct embedding for STAC integration  

---

## 🔐 4. Governance, Sovereignty & FAIR+CARE Enforcement

Tests ensure:

- `"kfm:care_label"` preserved  
- `"kfm:h3_sensitive"` propagated  
- `"kfm:mask_required"` conditions noted  
- `"kfm:sovereignty_uncertainty_floor"` preserved  
- `"kfm:care_label_reason"` maintained  
- no transformative step loses sovereignty context  

Governance CI enforces via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  
- `stac_validate.yml`

---

## 🧪 5. CI Integration

This suite runs under:

- `ci.yml`  
- `data_pipeline.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `faircare_validate.yml`  

Any failure → **full SMAP pipeline stop**.

---

## 🔁 6. Provenance in Full ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → provenance building (THIS SUITE VALIDATES)
 → STAC Writer
 → DCAT + PROV export
~~~

---

## 🔮 7. Applications Across KFM

### Hydrology  
Traceable soil-moisture lineage.

### Climate  
Traceable FT/VWC anomaly lineage.

### Archaeology  
Transparent environmental provenance for Story Nodes.

### Story Node v3  
Full lineage used for environmental narrative rendering.

### Focus Mode v3  
Lineage is the basis for “Why am I seeing this?” explanations.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                      |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete PROV-O test-suite README; emoji layout; FAIR+CARE/H3 aligned; JSON-LD compliant; CI-safe.           |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📦 Provenance Fixtures](../fixtures/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

