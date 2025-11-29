---
title: "📦 NASA SMAP — QA / RFI Flags Assets (2025) · Radiometer QC · RFI · Uncertainty (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/data/satellites/smap/stac/qa-flags/2025/assets/README.md"
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

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-qa-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Asset Overview"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-A / CARE-B depending on intersection with tribal lands"
indigenous_rights_flag: true
sensitivity_level: "Low (raw QA) / Medium (derived QA patterns)"
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

json_schema_ref: "../../../../../../../../schemas/json/stac-smap-qa-v11.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/stac-smap-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:qa-flags:2025:assets-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-qa-2025-assets"
event_source_id: "ledger:docs/data/satellites/smap/stac/qa-flags/2025/assets/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next QA asset-schema revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# ⚠️ **NASA SMAP — QA / RFI Flags Assets (2025)**  
`docs/data/satellites/smap/stac/qa-flags/2025/assets/README.md`

**Purpose**  
Define the asset bundle for **2025 SMAP QA/RFI STAC Items**, including the  
QA mask raster, uncertainty layer, and metadata files.  
These assets support **soil moisture**, **freeze–thaw**, and **VWC** STAC products  
and enforce **KFM-STAC v11**, **FAIR+CARE**, and **H3 sovereignty masking**.

</div>

---

## 📘 1. Overview

This directory contains core SMAP QA/RFI rasters & metadata for **2025**, referenced by  
every daily QA STAC Item under:

`docs/data/satellites/smap/stac/qa-flags/2025/`

The assets include:

- ⚠️ **QA Flags raster**  
- 📈 **QA uncertainty raster**  
- 🧾 **Metadata JSON** (orbit, incidence, calibration, provenance, governance)

These files are critical for:

- Interpreting soil moisture + freeze/thaw + VWC data  
- Filtering low-confidence pixels  
- Enforcing sovereign-sensitivity constraints  
- Maintaining consistent QA logic across hydrology & climate ETL pipelines  
- Supporting Story Node v3 + Focus Mode v3 with reliability indicators  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/qa-flags/2025/assets/
├── 📄 README.md                       # This file
│
├── ⚠️ qa-flags.tif                    # Radiometer QA + RFI mask
├── 📈 qa-uncertainty.tif              # QA uncertainty / reliability raster
└── 🧾 metadata.json                   # Orbit/grid/provenance metadata (with CARE/H3 fields)
~~~

These files are referenced by all STAC Items such as:

- `2025-01-01-item.json`
- `2025-01-02-item.json`
- etc.

---

## 🧩 3. Asset Specifications (KFM-STAC v11)

### ⚠️ qa-flags.tif — QA / RFI Mask

Contains:

- RFI detection  
- Radiometer gain anomalies  
- Retrieval confidence degradation  
- Surface condition flags  
- Freeze–thaw adjacency warnings  
- Beam-edge and swath geometry warnings  

Required metadata:

- `kfm:qa_flag_schema`  
- `kfm:qa_values`  
- `kfm:qa_interpretation`  
- `raster:bands[]` (nodata, scale, offset)  
- `proj:*` EASE-Grid 2.0  

---

### 📈 qa-uncertainty.tif — QA Uncertainty Raster

Represents radiometric uncertainty in QA classification.

Required metadata:

- `kfm:uncertainty_type: "qa-confidence"`  
- `kfm:error_model`  
- `kfm:stdev`  
- Grid + projection metadata  

Used for:

- suppressing false-positive anomalies  
- Story Node v3 environmental uncertainty bars  
- Focus Mode v3 reliability reporting  

---

### 🧾 metadata.json — Orbit / Grid / Provenance Metadata

Contains:

- EASE-Grid parameters  
- Orbit geometry (local time of overpass, swath, direction)  
- Calibration notes  
- Sensor configuration  
- Provenance (NASA L3 QA product ID)  
- CARE/H3 sovereignty fields  
- `"kfm:mask_applied"` where required  
- Uncertainty model references  

---

## 🔐 4. Governance & Sovereignty Enforcement

QA layers can unintentionally reveal:

- vegetation stress  
- wetness transitions  
- ecohydrology-sensitive anomalies  
- culturally sensitive seasonal/land-use patterns  

Thus KFM enforces:

- **CARE-A/B classification**  
- **H3 spatial generalization** for sensitive Indigenous territories  
- `"kfm:mask_applied"` flag in masked Items  
- Full provenance transparency  
- QA flags must NOT sharpen interpretive signals  

Governance validation pipelines:  

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. QA & Validation

For each asset:

- COG structural validation  
- Raster alignment between QA, uncertainty, and data layers  
- Temporal sanity checks  
- Cross-sensor QA vs:
  - SMAP soil moisture  
  - SMAP freeze/thaw  
  - SMAP vegetation-water  
  - HydroGNSS wetness/biomass  
  - Mesonet & NCEI indices  
  - ERA5-Land surface conditions  

QA results stored at:  
`docs/data/satellites/smap/qa/`

---

## 🔁 6. Ingestion → Lineage Pipeline (2025)

```
NASA SMAP L3 QA/RFI Product
 → decode & EASE-Grid mapping
 → integrate QA/RFI flags
 → propagate QA uncertainty
 → produce COG rasters
 → apply CARE/H3 masking
 → attach PROV-O lineage
 → register STAC assets
 → export OpenLineage + OTel telemetry
```

All steps are WAL-safe, deterministic, and fully governed.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
- Suppress unreliable soil-moisture anomalies  
- Identify RFI-interfered wetness zones  

### Climate  
- Correct freeze-thaw or vegetation-water false positives  

### Ecology  
- Filter noisy biomass/wetness indicators  

### Archaeology  
- Avoid misinterpretation of low-confidence environmental signals  

### Story Node v3  
- Provide uncertainty indicators for environmental narratives  

### Focus Mode v3  
- Show reliability bars & QA context in environmental panels  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                           |
|--------:|------------|---------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full v11.2.2 asset README; emoji layout; CARE/H3 compliance; STAC v11 alignment; CI-safe.         |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal QA asset notes.                                                                    |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ QA STAC 2025](../README.md) · [🛡 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

