---
title: "💧 Kansas Frontier Matrix — Processed Hydrology Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/processed/hydrology/metadata/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-processed-hydrology-metadata-v11.0.0"
semantic_document_id: "kfm-doc-data-processed-hydrology-metadata-readme"
event_source_id: "ledger:data/processed/hydrology/metadata/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-hydrology-processed-metadata-v11.json"
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
intent: "processed-hydrology-metadata"
role: "hydrology-domain"
category: "Data · Hydrology · Metadata · Processed"

fair_category: "F1-A1-I1-R1"
care_label: "Medium — water resources & community impacts"
sensitivity_level: "Dataset-dependent"
indigenous_rights_flag: "Dataset-dependent"
redaction_required: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Medium"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/data-hydrology-processed-metadata-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/data-hydrology-processed-metadata-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified hydrological claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Public / Mixed Sensitivity"
jurisdiction: "Kansas / United States"
lifecycle_stage: "stable"
ttl_policy: "Permanent"
sunset_policy: "Superseded upon next hydrology-domain metadata update"
---

<div align="center">

# 💧 **Kansas Frontier Matrix — Processed Hydrology Metadata**  
`data/processed/hydrology/metadata/README.md`

Metadata governing:

- 🏞️ Streamflow composites & river-stage harmonizations  
- 💦 Watershed polygons & hydrologic unit models (HUC)  
- 📈 Flood recurrence intervals & peak-flow statistics  
- 🧪 Hydrologic indicators (runoff, baseflow, infiltration)  
- 🌧️ Precip-runoff hydrology models (PRMS-style outputs)  
- 🧠 Focus Mode v3 hydrology narratives & flow-variation stories  
- 🌐 STAC/DCAT metadata, FAIR+CARE governance, PROV-O lineage  

All artifacts here are **schema-validated, checksum-verified, and governance-approved**.

</div>

---

## 1. 📘 Purpose

This directory contains **all metadata artifacts** associated with processed hydrologic datasets.

Metadata files include:

- PROV-O lineage exports  
- Schema validation reports  
- FAIR+CARE certification records  
- Hydrology-domain checksum manifests  
- STAC/DCAT metadata catalogs  

These ensure:

- Accuracy of streamflow, discharge, and watershed datasets  
- Ethical water-resource data stewardship  
- Compatibility with hydrology-focused Focus Mode narratives  
- Reproducibility across long-term climate/hazards integrations  
- ISO 19115 lineage compliance  

---

## 2. 🗂️ Directory Layout (GitHub-Safe)

```text
data/processed/hydrology/metadata/
├── README.md                               ← this file
├── checksums.json                           ← SHA-256 checksums for hydrology datasets
├── provenance.json                          ← PROV-O lineage tree (multi-step)
├── schema_validation.json                   ← Validation results (schemas, fields, units)
├── faircare_certification.json              ← FAIR+CARE certification
└── metadata_manifest.json                   ← Linked metadata catalog (DCAT/STAC)
```

---

## 3. 📑 Metadata Coverage

Hydrology metadata covers:

### **Dataset Identity**
- Titles, keywords, semantic IDs  
- STAC Item fields  
- DCAT Dataset fields  
- Hydrological domain roles  

### **Schema Structure**
- Required hydrology fields:  
  - `flow_cfs`, `stage_ft`, `discharge_m3s`, `huc`, `watershed_area_km2`  
  - Units & transformations  
  - Temporal ranges  
  - Spatial coordinates (EPSG:4326)  

### **Ethical Flags**
- CARE review when hydrology affects communities  
- Potential sensitivity around tribal water rights  
- Aggregation rules for water-withdrawal datasets  

### **Quality & Lineage**
- DQ checks (ISO 19157)  
- Hydrological period-of-record checks  
- Multi-source reconciliation (e.g., USGS NWIS × Corps of Engineers × PRMS models)  

### **File Tracking**
- SHA-256 checksums  
- SBOM mapping  
- Manifest bindings  

---

## 4. 🔗 PROV-O Lineage Overview

Hydrologic datasets are expressed as **prov:Entity** objects whose lineage includes:

- **Raw inputs**  
  - USGS NWIS daily or instantaneous values  
  - NIDIS drought hydrology  
  - Watershed delineations (HUC2–HUC12)  

- **Pipeline activities**  
  - Streamflow harmonization  
  - Missing-value interpolation  
  - Watershed aggregation  
  - Derived hydrologic index computation  

- **Agents**  
  - KFM Data Council  
  - KFM Hydrology Domain Stewards  
  - USGS/NIDIS external agencies  

`provenance.json` captures:

- Entity → Activity → Agent chain  
- Execution timestamps  
- Parameter configurations  
- Input-output relationships  

---

## 5. ⚖️ FAIR+CARE Governance — Hydrology Domain

Hydrology datasets reflect **shared and contested community resources**, requiring:

### FAIR
- Public accessibility under CC-BY  
- Standardized metadata for hydrologic modeling  
- High-lineage traceability (streamflow & watershed data require accuracy)  

### CARE
- Hydrological data may intersect with tribal sovereignty  
- Use must avoid misrepresenting water availability or scarcity  
- High-context metadata necessary for downstream decision-making  

`faircare_certification.json` includes:

- Reviewer comments  
- Transparency notes  
- Approvals or restrictions  

---

## 6. 🧪 Schema Validation Summary

`schema_validation.json` verifies:

- Time-series validity (no backward timestamps, no null flow values)  
- Watershed geometry validity (no self-intersections)  
- CRS normalization to EPSG:4326  
- Hydrology-unit consistency (cfs/m³s, inches/mm)  
- Data-contract compliance (`data-contract-v3`)  

Validation blocks include:

- Field type checks  
- Range checks  
- Missing data audits  
- Unit checks  

---

## 7. 🧮 Checksums & Metadata Manifest

`checksums.json` includes:

- SHA-256 values for all hydrology outputs (COGs, CSVs, Parquet)  
- Provenance references per-file  
- Timestamps  
- Pipeline-of-origin  

`metadata_manifest.json` provides:

- A STAC-aligned hydrology metadata index  
- DCAT dataset and distribution references  
- Schema, QC, FAIR+CARE links  

---

## 8. 🖥️ Focus Mode Integration

Focus Mode v3 uses hydrology metadata for:

- Flow variability explanations  
- Drought/wet anomalies (hydroclimate narratives)  
- Watershed-based event clustering  
- Flood stage contextualization  

Metadata ensures Focus:

- Honors tribal sovereignty rules  
- Applies uncertainty estimates  
- Maintains provenance & ethical safeguards  

---

## 9. 🕰️ Version History

| Version | Date       | Summary                                                  |
|--------:|------------|----------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial metadata registry, preferred formatting applied  |
| v10.0.0 | 2025-11-10 | Preliminary hydrology metadata added                     |

<div align="center">

**Kansas Frontier Matrix — Hydrology Domain Metadata**  
💧 FAIR+CARE Certified · Integrity-Verified · Diamond⁹ Ω / Crown∞Ω  

© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Hydrology](../README.md) · [Data Architecture](../../ARCHITECTURE.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>