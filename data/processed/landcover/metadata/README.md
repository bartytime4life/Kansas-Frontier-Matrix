---
title: "🌿 Kansas Frontier Matrix — Processed Landcover Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/processed/landcover/metadata/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-processed-landcover-metadata-v11.0.0"
semantic_document_id: "kfm-doc-data-processed-landcover-metadata-readme"
event_source_id: "ledger:data/processed/landcover/metadata/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-landcover-processed-metadata-v11.json"
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
intent: "processed-landcover-metadata"
role: "landcover-domain"
category: "Data · Landcover · Metadata · Processed"

fair_category: "F1-A1-I1-R1"
care_label: "Low–Medium — ecological data intersecting community land use"
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
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/data-landcover-processed-metadata-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/data-landcover-processed-metadata-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified landcover claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Public Dataset"
jurisdiction: "Kansas / United States"
lifecycle_stage: "stable"
ttl_policy: "Permanent"
sunset_policy: "Superseded upon next landcover-domain metadata update"
---

<div align="center">

# 🌿 **Kansas Frontier Matrix — Processed Landcover Metadata**  
`data/processed/landcover/metadata/README.md`

Metadata governing:

- 🟩 NLCD-based landcover classifications  
- 🌄 MODIS & Sentinel-2 vegetation composites  
- 📈 NDVI, EVI, LAI vegetation index timeseries  
- 🗺️ Landcover change detection (2000–2025)  
- 🌾 Agricultural/urban expansion metrics  
- 🧠 Focus Mode v3 ecological narratives  
- 🌐 STAC/DCAT metadata & FAIR+CARE governance  

All metadata files are **schema-aligned, checksum-verified, and governance-certified**.

</div>

---

## 1. 📘 Purpose

This directory contains **all metadata associated with processed landcover datasets**, including:

- PROV-O lineage exports  
- FAIR+CARE certification files  
- Schema validation reports  
- Metadata manifests (DCAT/STAC)  
- SHA-256 checksum manifests  
- QC and domain compliance reports  

Landcover metadata ensures:

- Ecological datasets are **traceable, reproducible, and ethically governed**  
- Focus Mode v3 can generate accurate ecological narratives  
- All files comply with **KFM-PDC v11**, **ISO 19115**, **ISO 19157**, and **PROV-O**  

---

## 2. 🗂️ Directory Layout (Mobile-Safe)

```text
data/processed/landcover/metadata/
├── README.md                               ← this file
├── checksums.json                           ← SHA-256 checksums for landcover datasets
├── provenance.json                          ← PROV-O lineage tree
├── schema_validation.json                   ← Schema contract validation results
├── faircare_certification.json              ← FAIR+CARE certification record
└── metadata_manifest.json                   ← Linked metadata catalog (DCAT/STAC)
```

---

## 3. 📑 Metadata Coverage

### **Dataset Identity**
Covers all landcover product metadata, including:

- Dataset titles/descriptions  
- Landcover class schema mappings  
- STAC Item & Collection fields  
- DCAT Dataset & Distribution metadata  

### **Schema Structure**
Required landcover fields include:

- `landcover_class` (NLCD/ESA classification)  
- `ndvi`, `evi`, `lai` (vegetation indices)  
- `pixel_area_m2`, `resolution_m`  
- `year`, `month`, or `time_start/time_end`  
- Valid geometry (EPSG:4326)  

### **Ethical Flags**
Because landcover data intersects with:

- Indigenous homelands  
- Sensitive ecological areas  
- Agricultural production regions  

Metadata establishes:

- Aggregation rules for sensitive zones  
- Sovereignty restrictions where required  
- Ecological sensitivity flags  

### **Quality & Lineage Validation**
Checks include:

- Pixel validity checks  
- Index normalizations  
- Cloud-masking methodology documentation  
- Multi-source blending lineage  
- Uncertainty estimates per index  

### **File Tracking**
Each file is linked to:

- Checksums  
- Pipeline-of-origin  
- Source datasets (MODIS, Sentinel, NLCD, Landsat)  
- Governance ledger entries  

---

## 4. 🔗 PROV-O Lineage (Summary)

`provenance.json` contains relationships showing:

### Entities
- Raw: NLCD, MODIS, Sentinel-2, Landsat vegetation products  
- Derived: NDVI, EVI, LAI composites  
- Processed: annual/summer peak NDVI mosaics  
- Models: landcover change detection outputs  

### Activities
- Spectral preprocessing  
- Cloud masking  
- NDVI/EVI calculation  
- Temporal compositing  
- Harmonization across sensors  

### Agents
- KFM Data Council  
- KFM Landcover Stewards  
- NASA / USGS (data producers)  

---

## 5. ⚖️ FAIR+CARE Governance — Landcover Domain

### FAIR
- Publicly accessible ecological datasets  
- Standardized metadata across satellite sources  
- STAC/DCAT-based discovery for external scientists  
- Reusable for climate, hazards, and ecological studies  

### CARE
- Vegetation/crop layers may indirectly reveal culturally sensitive practices  
- Tribal sovereignty applied to:
  - Rangelands  
  - Resource zones  
  - Stewardship territories  

`faircare_certification.json` documents:

- Sensitivity assessments  
- Required aggregations or masks  
- Ethically appropriate use guidance  

---

## 6. 🧪 Schema Validation Summary

`schema_validation.json` checks:

- Valid numeric ranges for NDVI (-1 to +1)  
- Pixel-type conformity (uint8/float32)  
- Proper class mappings for NLCD types  
- Geometry validity for polygonized landcover products  
- CRS normalization to EPSG:4326  
- Metadata completeness (title, description, keywords)  

---

## 7. 🧮 Checksums & Metadata Manifest

`checksums.json` contains:

- SHA-256 for:
  - NDVI/EVI composites  
  - NLCD class layers  
  - Landcover change detection layers  
  - Vegetation index time-series  

`metadata_manifest.json` contains:

- STAC Items for each landcover product  
- DCAT Dataset & Distribution entries  
- Links to lineage & certification metadata  
- Schema/validation crosswalks  

---

## 8. 🖥️ Focus Mode Integration

Metadata enables Focus Mode v3 to:

- Summarize ecological change  
- Highlight landcover transitions across years  
- Compute vegetation stress narratives  
- Relate landcover to hazards, climate, and hydrology  
- Enforce sovereignty- & CARE-aware masking rules  

Focus Mode requires:

- Accurate temporal ranges  
- Valid NDVI/vegetation metrics  
- Human-friendly classifications  
- Governance flags  

---

## 9. 🕰️ Version History

| Version | Date       | Summary                                                  |
|--------:|------------|----------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial metadata registry using preferred formatting      |
| v10.0.0 | 2025-11-10 | Preliminary landcover metadata added                     |

<div align="center">

**Kansas Frontier Matrix — Landcover Domain Metadata**  
🌿 FAIR+CARE Certified · Integrity-Verified · Diamond⁹ Ω / Crown∞Ω  

© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Landcover](../README.md) · [Data Architecture](../../ARCHITECTURE.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>