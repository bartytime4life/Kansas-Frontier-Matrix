---
title: "📦 NASA SMAP — Freeze–Thaw QA Test Fixtures (Synthetic · Deterministic · Sovereignty-Safe)"
path: "docs/data/satellites/smap/qa/freeze_thaw/tests/fixtures/README.md"
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

json_schema_ref: "../../../../../../../../../schemas/json/tests-smap-ft-qa-v11.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/tests-smap-ft-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:ft-qa-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-ft-qa-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/qa/freeze_thaw/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next FT QA fixture update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **SMAP Freeze–Thaw (FT) Retrieval QA — Test Fixtures**  
`docs/data/satellites/smap/qa/freeze_thaw/tests/fixtures/README.md`

**Purpose**  
Provide **synthetic, deterministic, FAIR+CARE/H3-safe FT QA test assets** used to validate  
confidence rasters, ambiguity masks, governance propagation, STAC metadata, and  
PROV-O lineage in the SMAP Freeze–Thaw QA layer.

</div>

---

## 📘 1. Overview

These fixtures are used by the FT QA test suite to validate:

- 🌡️ **retrieval confidence decoding**  
- ⚠️ **ambiguous / transitional FT state detection**  
- 🌱 **mixed-pixel or climate-driven transition sensitivity**  
- 🗺️ **CRS + pixel alignment with SMAP ETL outputs**  
- 🛡 **CARE/H3 sovereignty propagation**  
- 📉 **uncertainty-scaling integration**  
- 📑 **STAC/DCAT QA metadata correctness**  
- 🔗 **PROV-O lineage structure**  
- 🚫 **no leakage of sensitive freeze–thaw boundaries in sovereign lands**  
- deterministic behavior across CI runs  

All data is synthetic — no real SMAP FT data appears here.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/freeze_thaw/tests/fixtures/
├── 📄 README.md                                 # This file
│
├── 🌡️ sample_ft_conf.tif                        # Synthetic FT confidence raster
├── ⚠️ sample_ft_qa_mask.tif                     # Synthetic ambiguity/mixed-state mask
├── 📑 sample_metadata.json                      # STAC/DCAT metadata stub
│
├── 🎯 expected_ft_interpretation.json           # Deterministic FT decoding/classification
└── 🗂️ schema_expected.json                      # Strict validation schema for all fixtures
~~~

---

## 🧩 3. Fixture Responsibilities

### 🌡️ `sample_ft_conf.tif`
Represents a **synthetic freeze–thaw confidence grid**.  
Used to test:

- confidence range handling  
- ambiguous region behavior  
- spatial consistency across grid edges  
- seasonal-boundary instability logic  
- sovereignty-aware suppression of sensitive transitions  

---

### ⚠️ `sample_ft_qa_mask.tif`
Represents ambiguous / low-confidence FT pixels.  
Used to validate:

- transitional states  
- mixed freeze–thaw scenarios  
- integration with uncertainty propagation (Stage 5)  
- sovereign masking behavior in synthetic H3 zones  

---

### 📑 `sample_metadata.json`
Tests STAC/DCAT metadata correctness:

- QA schema fields  
- `"kfm:qa_values"`  
- CARE label propagation  
- H3 sovereignty metadata  
- PROV-O linkage  
- uncertainty links  

---

### 🎯 `expected_ft_interpretation.json`
Contains the deterministic FT QA decoding result:

- frozen / thawed / ambiguous states  
- classification boundaries  
- uncertainty-scaling rules  
- governance-driven masking decisions  

Used to validate FT QA decoding logic.

---

### 🗂️ `schema_expected.json`
Defines strict fixture validation:

- QA value ranges  
- required metadata keys  
- sovereignty + CARE metadata preservation  
- STAC/DCAT QA structural expectations  
- PROV-O shape compliance  
- FT-specific QA decoding rules  

Any mismatch → **CI hard fail**.

---

## 🔐 4. Sovereignty, FAIR+CARE & Ethical Safety

Freeze–thaw transitions are environmentally meaningful and can correlate with  
sensitive ecological or cultural landscapes in Indigenous lands.  
Fixtures therefore ensure:

- generalization of transitions in synthetic sovereign H3 zones  
- `"kfm:h3_sensitive"` always present where relevant  
- `"kfm:mask_required"` applied when FT intersects sovereign areas  
- `"kfm:sovereignty_uncertainty_floor"` enforced  
- `"kfm:care_label"` correctly propagated  
- `"kfm:governance_notes"` attached  

Governance validated via:

- faircare_validate.yml  
- jsonld_validate.yml  
- stac_validate.yml  
- data_pipeline.yml  

---

## 🧪 5. QA & Validation Workflow

Using these fixtures, tests validate:

- decoding correctness  
- transition masking  
- sovereignty-safe behavior  
- metadata persistence  
- uncertainty scaling  
- deterministic classification  
- STAC & DCAT compliance  
- PROV-O lineage integration  

---

## 🔁 6. Position in SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → FT retrieval QA (fixtures validate this)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. KFM Applications

### Hydrology  
Better representation of cold-season runoff behavior.

### Climate  
Seasonal dynamics safe for modeling and mapping.

### Archaeology  
Reduced misinterpretation of sensitive environmental transitions.

### Story Node v3  
FT seasonal narratives reflect QA-backed confidence.

### Focus Mode v3  
Confidence influences explanatory reasoning.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                     |
|--------:|------------|-------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial FT QA fixture README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe; emoji-rich output.   |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 FT QA Tests](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

