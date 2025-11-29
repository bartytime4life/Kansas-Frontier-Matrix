---
title: "📦 NASA SMAP — Provenance Test Fixtures (Entities · Activities · Agents · Governance) · ETL Stage 7"
path: "docs/data/satellites/smap/transforms/provenance/tests/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Provenance Board · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public Test Fixtures"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2 (Extended)"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R5"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low"
risk_category: "Medium"
redaction_required: false

data_steward: "KFM Provenance Board · FAIR+CARE Council · Earth Systems Working Group"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../../schemas/json/tests-smap-provenance-v11.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/tests-smap-provenance-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:provenance-tests-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-smap-provenance-tests-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/transforms/provenance/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon fixture update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — Provenance Test Fixtures (ETL Stage 7)**  
`docs/data/satellites/smap/transforms/provenance/tests/fixtures/README.md`

**Purpose**  
Provide deterministic, sovereignty-aware, FAIR+CARE-compliant synthetic fixtures  
used to validate all PROV-O lineage components in SMAP ETL Stage 7:  
**Entities**, **Activities**, **Agents**, **Governance fields**, and  
**decode → reprojection → calibration → QA/RFI → uncertainty → governance → provenance**  
lineage completeness.

</div>

---

## 📘 1. Overview

These fixtures validate that:

- ✔ PROV-O Entities are complete and correct  
- ✔ Activities correctly represent all SMAP ETL transformations  
- ✔ Agents include pipelines, toolchains, FAIR+CARE councils, sovereignty groups  
- ✔ Governance metadata is preserved in provenance  
- ✔ JSON-LD outputs validate under PROV-O shapes and schemas  
- ✔ Lineage is deterministic and reproducible  
- ✔ No invented lineage elements are introduced  
- ✔ No sovereignty/CARE metadata is lost  
- ✔ STAC integration receives correct provenance blocks  

All fixtures contain **no real-world sensitive data** — fully synthetic and CI-fast.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/provenance/tests/fixtures/
├── 📄 README.md                                # This file
│
├── 📁 sample_etl_inputs.json                    # Synthetic decode → governance input definitions
├── 🧾 sample_prov_expected.json                 # Expected PROV-O lineage graph output
│
├── 👤 synthetic_agent_defs.json                 # Agents used during provenance (pipelines, councils, orgs)
├── 🗃️ synthetic_entity_defs.json                # Entity samples (rasters, metadata, masks, QA, uncertainty)
│
└── 🔧 schema_expected.json                      # Validation schema for fixture integrity
~~~

---

## 🧩 3. Fixture Responsibilities

### 📁 **sample_etl_inputs.json**  
Defines synthetic representations of:

- decode results  
- reprojection results  
- calibration results  
- QA/RFI artifacts  
- uncertainty grids  
- governance masks  
- metadata blocks  

Used to test whether the provenance builder ingests and references  
all ETL-stage artifacts correctly.

---

### 🧾 **sample_prov_expected.json**  
The “gold standard” deterministic PROV-O JSON-LD graph used to check that:

- all Entities appear exactly once  
- all Activities appear in correct order  
- all Agents are correctly associated  
- all relationships (`prov:wasGeneratedBy`, `prov:used`, `prov:wasDerivedFrom`) exist  
- all governance metadata is preserved  
- lineage is free of cycles  
- lineage is machine-extractable and schema-valid  

---

### 👤 **synthetic_agent_defs.json**  
Defines all synthetic Agents used in tests:

- `"kfm:etl_pipeline"`  
- `"kfm:governance_board"`  
- `"kfm:faircare_council"`  
- `"kfm:sovereignty_group"`  
- `"kfm:stac_writer"`  
- `"nasa:smap_team"`  

This validates:

- `prov:Agent` correctness  
- `"prov:actedOnBehalfOf"` chains  
- FAIR+CARE governance participation  

---

### 🗃️ **synthetic_entity_defs.json**  
Defines mock Entities:

- rasters  
- QA masks  
- uncertainty grids  
- governance masks  
- metadata blobs  
- STAC JSON components  

Used to validate:

- Entity typing  
- governance attributes  
- spatial metadata  
- uncertainty and QA metadata inclusion  

---

### 🔧 **schema_expected.json**  
Defines validation rules for all fixtures:

- required keys  
- valid provenance graph shape  
- expected relationships  
- JSON-LD context expectations  
- governance metadata expectations  
- sovereignty/H3 requirements  
- cross-stage linkage checks  

If any mismatch → **CI failure**.

---

## 🔐 4. Governance, FAIR+CARE & Sovereignty Requirements

Fixtures test preservation of:

- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:care_label_reason"`  
- `"kfm:governance_notes"`  

Provenance is required to:

- record sovereignty-driven masking operations  
- declare provenance of ethical decisions  
- show lineage of environmental uncertainty  
- prevent accidental removal of sensitive metadata  

CI enforcement via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. QA & Validation

Tests using these fixtures validate:

- PROV-O structure  
- JSON-LD encoding  
- sovereignty-aware lineage  
- CARE metadata continuity  
- temporal consistency  
- deterministic ordering  
- correct ETL Activity chain  
- STAC-ready provenance blocks  

Fixtures are designed so **any missing or incorrect part fails CI immediately**.

---

## 🔁 6. Provenance in Full SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → provenance building (validated here)
 → STAC Writer
 → DCAT + PROV export
~~~

Without passing these fixtures, the STAC Writer is **not allowed to run**.

---

## 🔮 7. Applications Across KFM

### Hydrology  
End-to-end environmental dataset lineage.

### Climate  
Traceable anomaly and FT/VWC provenance.

### Archaeology  
Transparent environmental provenance for culturally sensitive analyses.

### Story Node v3  
Environmental narratives cite the exact provenance chain.

### Focus Mode v3  
Lineage-based explainability for environmental reasoning.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                     |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full provenance-fixture README; emoji-rich; FAIR+CARE + H3 aligned; JSON-LD/PROV-O validated; CI-safe.       |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 Provenance Tests](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

