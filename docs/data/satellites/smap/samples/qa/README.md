---
title: "🧪 NASA SMAP — Sample QA Examples (Synthetic QA Masks · QA Codes · Uncertainty Demos)"
path: "docs/data/satellites/smap/samples/qa/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public · Non-Sensitive · Synthetic Examples"
status: "Active / Public"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Documentation WG · FAIR+CARE Council"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-A (Public / Low-Risk)"
indigenous_rights_flag: false
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems WG · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/smap-sample-qa-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/smap-sample-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:samples-qa-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-samples-qa"
event_source_id: "ledger:docs/data/satellites/smap/samples/qa/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "72 months"
sunset_policy: "Superseded on next sample-data refresh"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **SMAP Sample QA Artifacts**  
`docs/data/satellites/smap/samples/qa/`

**Purpose**  
Provide **synthetic, tutorial-grade QA examples** demonstrating how SMAP QA layers work:  
bitfields, QA masks, QA codes, uncertainty mappings, and governance metadata.  
For **documentation, onboarding, teaching, and CI smoke tests only**.  
**No real QA data** appears here.

</div>

---

## 📘 1. Overview

This directory contains **small, synthetic** QA examples that illustrate:

- how SMAP QA flags work  
- how QA codes map to meaningful states  
- how ambiguity/low-confidence pixels appear  
- how QA influences uncertainty  
- how STAC “qa_values” metadata is shaped  
- how `"kfm:*"` governance metadata is embedded  
- how safe QA overlays appear in MapLibre/Cesium demos  

These files are **NOT** used in production ETL — they are purely for documentation and CI.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/samples/qa/
├── 📄 README.md                             # This file
│
├── ⚠️ sm_qa_mask_sample.json                 # Soil moisture QA (synthetic)
├── 🌡️ ft_qa_mask_sample.json                 # Freeze–Thaw QA example
├── 🌿 vwc_qa_mask_sample.json                # Vegetation-water QA example
│
├── 📝 qa_codes_sample.json                   # Mapping of QA flags → semantic meaning
└── 📉 uncertainty_mapping.json               # Mini uncertainty scaling example
~~~

---

## 🧩 3. File Responsibilities

### ⚠️ `sm_qa_mask_sample.json`
Demonstrates:

- synthetic SM retrieval confidence categories  
- ambiguous/low-confidence areas  
- governance flags (`"kfm:care_label"`)  

### 🌡️ `ft_qa_mask_sample.json`
Shows:

- simple FT ambiguous boundary  
- safe synthetic seasonal-transition pattern  
- uncertainty implications  

### 🌿 `vwc_qa_mask_sample.json`
Shows:

- canopy-driven retrieval uncertainty  
- synthetic noise in VWC data  
- simplified QA states  

### 📝 `qa_codes_sample.json`
Demonstrates:

- SMAP → KFM unified QA-code mapping  
- semantic meanings  
- severity scale examples  

### 📉 `uncertainty_mapping.json`
Shows:

- simplified QA→uncertainty mapping  
- safe synthetic modifiers  
- how uncertainty links into STAC metadata  

---

## 🔐 4. FAIR+CARE & Sovereignty Notes

All samples:

- contain **no real-world ecological or cultural information**  
- are **synthetic**, **non-sensitive**, **public**  
- do not intersect sovereign lands  
- follow KFM governance rules for labeling & documentation  
- optionally include `"kfm:*"` governance metadata for training/demo consistency  

Full H3 sovereignty logic is demonstrated only conceptually; actual masking is not required.

---

## 🧪 5. Validation & CI Behavior

CI checks that:

- sample JSON files are valid and loadable  
- QA codes match the sample schema  
- STAC metadata examples follow valid structure  
- no forbidden keys appear  
- semantic key names align with docs  
- filenames and paths match doc references  

Failures here break **documentation CI**, not production ETL.

---

## 🔁 6. Relationship to SMAP ETL

These sample QA artifacts are:

❌ NOT used for ingest  
❌ NOT used for QA/RFI integration  
❌ NOT used for uncertainty propagation  
❌ NOT part of the SMAP science pipeline  

They are used for:

- documentation  
- developer onboarding  
- STAC examples  
- Focus Mode narrative examples  
- notebooks/tutorials  
- CI documentation checks  

---

## 🔮 7. Applications Across KFM

- 📘 educational walkthroughs  
- 🧪 sample QA overlays  
- 🗺️ map demo layers  
- 🌐 STAC tutorials  
- 🧭 Focus Mode examples  
- 🎓 training workshops  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial SMAP sample QA README; synthetic safe QA masks; FAIR+CARE aligned; CI-safe; emoji-rich.      |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📦 STAC Samples](../stac/README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

