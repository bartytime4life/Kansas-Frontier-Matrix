---
title: "📊 Kansas Frontier Matrix — Processed Tabular Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/processed/tabular/metadata/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-processed-tabular-metadata-v11.0.0"
semantic_document_id: "kfm-doc-data-processed-tabular-metadata-readme"
event_source_id: "ledger:data/processed/tabular/metadata/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-tabular-processed-metadata-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0 / FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Domain Metadata Registry"
intent: "processed-tabular-metadata"
role: "tabular-domain"
category: "Data · Tabular · Metadata · Processed"

fair_category: "F1-A1-I1-R1"
care_label: "Dataset-dependent"
sensitivity_level: "Dataset-dependent"
indigenous_rights_flag: "Dataset-dependent"
redaction_required: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low–Medium"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../schemas/json/data-tabular-processed-metadata-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/data-tabular-processed-metadata-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified statistical claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Public / Mixed Sensitivity"
jurisdiction: "Kansas / United States"
lifecycle_stage: "stable"
ttl_policy: "Permanent"
sunset_policy: "Superseded upon next tabular-domain metadata update"
---

<div align="center">

# 📊 **Kansas Frontier Matrix — Processed Tabular Metadata**  
`data/processed/tabular/metadata/README.md`

Metadata governing:

- 📋 CSV/Parquet processed tables  
- 🧮 Statistical aggregates, indicators, and metrics  
- 🗃️ Normalized tabular layers (tract, county, H3, watershed)  
- 📈 Time-series & longitudinal tabular datasets  
- 🧠 Focus Mode v3 tabular context & narrative linking  
- 🌐 STAC/DCAT catalog metadata  
- 📊 FAIR+CARE governance of sensitive tabular fields  

All metadata artifacts are **schema-validated, checksum-verified, and governance-approved**.

</div>

---

## 1. 📘 Purpose

This directory holds **metadata for processed tabular datasets**, including:

- Schema validation reports  
- FAIR+CARE certification outputs  
- Complete PROV-O lineage  
- Checksums & manifest bindings  
- Data-contract compliance records  
- DCAT/STAC tabular metadata catalogs  

Tabular metadata ensures:

- Reproducible statistical summaries  
- Valid demographic & socio-ecological metrics  
- Ethical handling of sensitive indicators  
- Compatibility with KFM analytical pipelines  
- Reliable integration into Story Nodes & Focus Mode  

---

## 2. 🗂️ Directory Layout (GitHub-Safe)

```text
data/processed/tabular/metadata/
├── README.md                               ← this file
├── checksums.json                           ← SHA-256 checksums for tabular datasets
├── provenance.json                          ← PROV-O lineage exports
├── schema_validation.json                   ← Schema contract + field validation results
├── faircare_certification.json              ← FAIR+CARE certification record
└── metadata_manifest.json                   ← STAC/DCAT metadata catalog
```

---

## 3. 📑 Metadata Coverage

### **Dataset Identity**
Metadata describes:

- Dataset titles & descriptions  
- Column-level metadata  
- Category/type indicators  
- Spatial linkage fields (FIPS, GEOID, H3 index, watershed ID, etc.)  
- Temporal linkage fields (year/month, period_start, period_end)  

### **Schema Structure**
Processed tabular datasets MUST include:

- Complete data dictionary  
- Explicit field types (`int`, `float`, `string`, `categorical`)  
- Units (e.g., `%`, people, sq_km, acres, USD)  
- Missing-data semantics (`null`, sentinel values, imputed flags)  
- Provenance and uncertainty annotations  

### **Ethical Flags**
Some columns may require CARE handling, including:

- Demographic vulnerability indices  
- Socio-economic indicators  
- Tribal identifiers or sensitive demographic markers  
- Health or safety-related tabular indicators  

Redaction or aggregation rules MUST be documented.

### **Quality & Lineage**
Metadata ensures:

- Column ranges are valid  
- Units are consistent  
- No broken joins between spatial or demographic keys  
- No invalid categories or enumerations  
- All values pass validation under `data-contract-v3`  

### **File Tracking**
All tabular datasets include:

- SHA-256 checksums  
- Schema and provenance references  
- Pipeline-of-origin identifiers  
- Data stewardship and governance links  

---

## 4. 🔗 PROV-O Lineage Overview

`provenance.json` describes:

### **Entities**
- Raw census or survey inputs  
- Environmental tabular summaries  
- Derived socio-demographic indicators  
- Time-series aggregates  
- Aggregated risk indices  

### **Activities**
- Normalization pipelines  
- Aggregation operations  
- Statistical transformations  
- Join/merge processes  
- Unit conversions  

### **Agents**
- KFM Data Council  
- Tabular-domain stewards  
- External agencies (Census Bureau, USDA, KDHE, etc.)  

---

## 5. ⚖️ FAIR+CARE Governance — Tabular Domain

Tabular datasets often contain **indirectly sensitive** information.

### **FAIR**
- Clear definitions  
- Reusable units  
- Reliable lookup fields  
- Accessible & interoperable metadata  

### **CARE**
- Some socioeconomic/demographic tables must be:
  - Aggregated  
  - Generalized  
  - Masked at tract or H3 thresholds  
  - Reviewed for cultural sensitivity  

`faircare_certification.json` contains reviewer notes, approvals, and restrictions.

---

## 6. 🧪 Schema Validation Summary

`schema_validation.json` verifies:

- Field types (int/float/string)  
- Expected ranges (e.g., population >= 0)  
- Valid enumerations for categories  
- Temporal completeness  
- Spatial key matching  
- Compliance with `data-contract-v3`  
- Integrity of join keys across datasets  

Data fails validation if:

- Keys mismatch  
- Units are inconsistent  
- Critical fields are missing  
- Nullability violates schema rules  

---

## 7. 🧮 Checksums & Metadata Manifest

`checksums.json` includes SHA-256 values for:

- Demographic aggregates  
- Environmental/landcover-derived tabular summaries  
- Census & ACS-based processed layers  
- Risk and vulnerability indices  
- All H3 or tract-level tabular derivatives  

`metadata_manifest.json` contains:

- STAC Items for tabular assets  
- DCAT Dataset + Distribution metadata  
- Provenance linkages  
- Schema validation + FAIRCARE references  

---

## 8. 🖥️ Focus Mode Integration

Focus Mode v3 uses tabular metadata to:

- Provide context for demographic or risk-related narratives  
- Support dynamic filtering in Focus Mode panels  
- Align story elements with spatial and temporal keys  
- Explain variability, uncertainty, and summary indicators  

Metadata ensures:

- Keys and join fields are correct  
- Units are consistent for narrative statements  
- Sensitive columns are ethically masked or aggregated  

---

## 9. 🕰️ Version History

| Version | Date       | Summary                                                 |
|--------:|------------|---------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial processed tabular metadata (preferred format)    |
| v10.0.0 | 2025-11-10 | Preliminary tabular metadata added                      |

<div align="center">

**Kansas Frontier Matrix — Tabular Metadata Domain**  
📊 FAIR+CARE Certified · Integrity-Verified · Diamond⁹ Ω / Crown∞Ω  

© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Tabular](../README.md) · [Data Architecture](../../ARCHITECTURE.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>