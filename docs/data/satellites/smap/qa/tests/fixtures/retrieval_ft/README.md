---
title: "📦 NASA SMAP — Freeze–Thaw (FT) Retrieval QA Fixtures (Synthetic · Deterministic · Sovereignty-Safe)"
path: "docs/data/satellites/smap/qa/tests/fixtures/retrieval_ft/README.md"
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
previous_version_hash: "<previous-sha>"
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

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-retrieval-ft-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-retrieval-ft-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:retrieval-ft-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-retrieval-ft-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/qa/tests/fixtures/retrieval_ft/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next FT QA fixture revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **SMAP Freeze–Thaw (FT) Retrieval QA — Synthetic Test Fixtures**  
`docs/data/satellites/smap/qa/tests/fixtures/retrieval_ft/README.md`

**Purpose**  
Provide **synthetic, deterministic, sovereignty-safe** Freeze–Thaw (FT) Retrieval QA fixtures  
used to validate FT confidence decoding, ambiguity detection, governance metadata propagation,  
uncertainty scaling, STAC/DCAT correctness, and PROV-O lineage in the KFM SMAP QA pipeline.

</div>

---

## 📘 1. Overview

These fixtures validate:

- 🌡️ correct FT retrieval confidence interpretation  
- ⚠️ ambiguous seasonal transitions  
- ❄️ freeze/thaw boundary instability handling  
- 🌱 canopy-driven FT ambiguity  
- 🗺 pixel-level CRS & grid alignment  
- 🛡 sovereignty/H3 masking behaviors  
- 📉 QA → uncertainty propagation  
- 📑 STAC/DCAT QA metadata preservation  
- 🔗 PROV-O lineage inclusion  
- 🎯 deterministic outputs for CI stability

All data is **synthetic** (no real SMAP FT patterns included).

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/tests/fixtures/retrieval_ft/
├── 📄 README.md                                  # This file
│
├── 🌡️ sample_ft_conf.tif                         # Synthetic FT retrieval confidence raster
├── ⚠️ sample_ft_qa_mask.tif                      # Ambiguous / mixed-state FT mask
├── 📑 sample_metadata.json                       # STAC/DCAT + governance metadata stub
│
├── 🎯 expected_ft_interpretation.json            # Deterministic FT QA decoding output
└── 🗂️ schema_expected.json                        # Strict validation schema for all fixtures
~~~

---

## 🧩 3. Fixture Responsibilities

### 🌡️ `sample_ft_conf.tif`
Simulates:

- low/medium/high FT confidence  
- ambiguous season transitions (spring/fall)  
- synthetic anomalies influenced by canopy or RFI  
- sovereign-region generalization (H3 masking)  

Used for:

- confidence decoding tests  
- QA → uncertainty integration  
- governance masking validation  
- CRS alignment checks  

---

### ⚠️ `sample_ft_qa_mask.tif`
Represents ambiguous FT pixels:

- mixed freeze + thaw states  
- noisy seasonal edges  
- canopy-driven instability  
- synthetic proxy transitions  

Used to validate:

- ambiguity detection  
- uncertainty inflation  
- masking in sovereign H3 areas  

---

### 📑 `sample_metadata.json`
Contains synthetic metadata including:

- `kfm:qa_values` for FT  
- QA schema & quality notes  
- `"kfm:care_label"` & `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- temporal + spatial extents  
- PROV-O lineage roots  

Used to validate metadata preservation rules.

---

### 🎯 `expected_ft_interpretation.json`
Provides deterministic expected outputs:

- classified states (Frozen / Thawed / Ambiguous)  
- QA → uncertainty scaling  
- sovereign-safe classification  
- metadata-driven outcomes  

Used for CI exact-match validation.

---

### 🗂️ `schema_expected.json`
Defines strict constraints:

- expected JSON structures  
- allowed FT QA values  
- sovereignty metadata requirements  
- STAC/DCAT QA field structure  
- PROV-O linkage correctness  
- deterministic ordering rules  

Any mismatch → **CI hard fail**.

---

## 🔐 4. FAIR+CARE & Sovereignty Requirements

Fixtures enforce:

- `"kfm:care_label"` presence  
- `"kfm:h3_sensitive"` propagation  
- `"kfm:mask_required"` when synthetic FT patterns intersect sovereign H3 zones  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- NO real FT gradients or eco-signals  

Critical: FT transitions **cannot** expose sensitive ecological boundaries in sovereign areas.

Governance is validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. Validation Workflow

Tests using these fixtures confirm:

- FT confidence decoding  
- ambiguity boundary detection  
- uncertainty propagation  
- sovereignty-safe outputs  
- metadata correctness  
- PROV-O lineage completion  
- CRS/pixel alignment integrity  
- deterministic behavior for CI reproducibility  

---

## 🔁 6. FT Retrieval QA in the SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → FT retrieval QA (validated here)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. Applications in KFM

### Hydrology  
Better freeze-up and thaw-transition interpretation.

### Climate  
FT seasonality influences hazard + ecological modeling.

### Archaeology  
Sovereign-safe FT patterns protect culturally sensitive terrains.

### Story Node v3  
Seasonal narratives shaped by FT QA confidence.

### Focus Mode v3  
Confidence informs environmental reasoning weights.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                  |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial FT Retrieval QA fixture README; FAIR+CARE/H3 aligned; CI-safe; STAC/DCAT/PROV-ready; emoji-rich. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 FT Retrieval QA Tests](../../../retrieval/tests/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

