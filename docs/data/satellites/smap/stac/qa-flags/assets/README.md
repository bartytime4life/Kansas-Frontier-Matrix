---
title: "📦 NASA SMAP — Global QA / RFI Flags Asset Definitions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/smap/stac/qa-flags/assets/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-smap-qa-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Asset Overview"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-A / CARE-B depending on geographic overlap"
indigenous_rights_flag: true
sensitivity_level: "Low (raw) / Medium (derived QA patterns)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "DataDownload"
  prov_o: "prov:Entity"
  owl_time: "ProperInterval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../schemas/json/stac-smap-qa-v11.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/stac-smap-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:qa-flags:assets:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-qa-assets"
event_source_id: "ledger:docs/data/satellites/smap/stac/qa-flags/assets/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next QA asset-schema update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# ⚠️ **NASA SMAP — QA / RFI Flags (Global Asset Definitions)**  
`docs/data/satellites/smap/stac/qa-flags/assets/README.md`

**Purpose**  
Define the **global QA/RFI asset schema** used for all SMAP QA STAC Items  
(across multiple years: 2023, 2024, 2025, …).  
These assets provide radiometer quality indicators, RFI masks, and reliability metadata  
supporting all SMAP product families: soil moisture, freeze–thaw, and vegetation water content.

</div>

---

## 📘 1. Overview

The QA/RFI assets define:

- ⚠️ **Quality flags** (radiometer performance, gain, calibration, RFI detection)  
- 📈 **Uncertainty layers** (QA reliability surface)  
- 🧾 **Metadata** (orbit, calibration, grid mapping, provenance, CARE/H3 governance)  

These global templates are pulled by **every** per-year QA STAC directory, ensuring:

- Cross-year consistency  
- FAIR+CARE & sovereignty compliance  
- Stable QA logic across soil moisture / freeze-thaw / VWC pipelines  
- STAC v11 structural correctness  
- Reusable metadata & uncertainty models  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/qa-flags/assets/
├── 📄 README.md                         # This file
│
├── ⚠️ qa-flags.tif                      # Global QA / RFI classification template
├── 📈 qa-uncertainty.tif                # QA confidence / uncertainty raster
└── 🧾 metadata.json                     # Orbit/grid/provenance + CARE/H3 metadata
~~~

Per-year asset directories (e.g., `/2025/assets/`) contain **actual daily rasters**;  
this directory contains **the schema templates** they must conform to.

---

## 🧩 3. Asset Specifications (KFM-STAC v11)

### ⚠️ qa-flags.tif — Radiometer QA / RFI Mask

Includes:

- RFI detection  
- Gain fluctuations  
- Sensor performance degradation  
- Retrieval failure flags  
- Border-of-swath anomalies  
- Freeze/thaw adjacency warnings  

Metadata requirements:

- `kfm:qa_flag_schema`  
- `kfm:qa_values` legend  
- `kfm:qa_interpretation` (semantic description of codes)  
- `raster:bands[]` (nodata, data_type, scale, offset)  
- `proj:*` → EASE-Grid 2.0 parameters  

---

### 📈 qa-uncertainty.tif — QA Confidence / Uncertainty Surface

Captures uncertainty in QA classification:

- `kfm:uncertainty_type: "qa-confidence"`  
- `kfm:error_model`  
- `kfm:stdev`  
- Alignment with primary soil-moisture / FT / VWC grids  

Supports downstream:

- Filtering low-confidence pixels  
- Focus Mode v3 “environment reliability” indicators  
- Story Node v3 context uncertainty bars  

---

### 🧾 metadata.json — Orbit/Grid/Provenance Metadata

Must include:

- Orbit geometry (swath, pass direction, LTAN)  
- EASE-Grid 2.0 metadata  
- NASA L3 QA product references  
- Calibration notes  
- Care/H3 sovereignty metadata:  
  - `kfm:care_label`  
  - `kfm:sovereignty_note`  
  - `"kfm:mask_applied": true` (if generalization used)  
- PROV-O lineage  
- Uncertainty model linkages  

This file is **not speculative** and must match upstream ground-truth metadata.

---

## 🔐 4. Governance & Sovereignty

QA/RFI data can reveal patterns correlated with:

- vegetation stress  
- freeze–thaw anomalies  
- hydrology-state transitions  
- culturally sensitive land-use cycles  

Thus KFM requires:

- CARE-A/B classification  
- Sovereignty checks for tribal lands  
- Mandatory **H3 masking** in sensitive geographies  
- `"kfm:mask_applied"` on derived datasets  
- Explicit uncertainty & provenance disclosure  

Governance pipelines include:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`  

---

## 🧪 5. QA & Validation Requirements

Assets must pass:

- COG structural verification  
- Raster alignment checks (QA, uncertainty, data layers)  
- Projection & CRS checks  
- BBox consistency validation  
- Temporal QA consistency across sensors  
- Cross-sensor QA vs:
  - SMAP soil moisture  
  - SMAP freeze–thaw  
  - SMAP VWC  
  - HydroGNSS  
  - Mesonet + ERA5  

QA logs → `docs/data/satellites/smap/qa/`  
Telemetry → `releases/<version>/data-telemetry.json`

---

## 🔁 6. Ingestion → Lineage Workflow

```
NASA SMAP L3 QA Product
 → decode + EASE-Grid harmonization
 → RFI & QA integration
 → uncertainty propagation
 → generate COG templates
 → CARE/H3 masking
 → register assets (STAC/DCAT)
 → publish PROV-O lineage
 → emit OpenLineage + OTel telemetry
```

All steps are WAL-safe & reproducible.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
- Soil moisture reliability filters  
- Floodplain anomaly correction  

### Climate  
- Quality-aware freeze/thaw detection  
- Vegetation stress false-positive suppression  

### Ecology  
- Noise-filtered biomass/wetness assessments  

### Archaeology  
- High-confidence environmental context for heritage analysis  

### Story Node v3  
- QA-derived certainty indicators for narratives  

### Focus Mode v3  
- Environmental “confidence indicators”  
- Suppresses misleading anomalies near sensitive regions  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                       |
|--------:|------------|------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Created global SMAP QA asset README; emoji-rich; governance/H3 rules; STAC v11; CI-safe.       |
| v10.3.2 | 2025-11-14 | Early pre-v11 minimal QA asset documentation.                                                  |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ QA Flags STAC Home](../README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

