---
title: "📦 NASA SMAP — Global Vegetation Water Content (VWC) Asset Definitions (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/data/satellites/smap/stac/vegetation-water/assets/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-smap-vwc-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Asset Overview"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-A / CARE-B (variable-dependent)"
indigenous_rights_flag: true
sensitivity_level: "Low (raw vegetation-water) / Medium (derived biomass/wetness indicators)"
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

json_schema_ref: "../../../../../../schemas/json/stac-smap-vwc-v11.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/stac-smap-vwc-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:vwc:assets:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-vwc-assets"
event_source_id: "ledger:docs/data/satellites/smap/stac/vegetation-water/assets/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next VWC asset-schema revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌿 **NASA SMAP — Vegetation Water Content (VWC) Asset Definitions (Global)**  
`docs/data/satellites/smap/stac/vegetation-water/assets/README.md`

**Purpose**  
Define the **global asset schema** used by all SMAP VWC STAC Items  
(across years such as 2023/2024/2025).  
This directory contains **canonical asset templates**: vegetation-water rasters,  
uncertainty rasters, QA/RFI masks, and orbit/grid/provenance metadata,  
all aligned with **KFM-STAC v11** and FAIR+CARE governance.

</div>

---

## 📘 1. Overview

This directory holds the **master asset templates** for SMAP Vegetation Water Content (VWC):

- 🌿 **Vegetation water content raster (primary)**  
- ⚠️ **QA / RFI mask**  
- 📈 **Uncertainty raster**  
- 🧾 **Metadata JSON** including:
  - orbit & overpass info  
  - EASE-Grid specifications  
  - calibration + processing notes  
  - PROV-O lineage  
  - CARE/H3 masking rules  

These assets are referenced by **every year-level STAC folder**, e.g.:

```
docs/data/satellites/smap/stac/vegetation-water/2025/assets/
docs/data/satellites/smap/stac/vegetation-water/2024/assets/
docs/data/satellites/smap/stac/vegetation-water/2023/assets/
```

They ensure:

- Structural consistency  
- Deterministic ingestion  
- Proper FAIR+CARE + sovereignty behavior  
- Schema validity across the entire SMAP VWC STAC collection  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/vegetation-water/assets/
├── 📄 README.md                             # This file
│
├── 🌿 vegetation-water.tif                  # Primary VWC raster template
├── 📈 vegetation-uncertainty.tif            # Uncertainty raster template
├── ⚠️ qa-flags.tif                           # QA / RFI mask template
└── 🧾 metadata.json                          # Orbit/grid/provenance metadata (global template)
~~~

**Note:**  
These are **templates**. Actual per-day/per-year rasters live in their respective  
year folders (e.g., `/2025/assets/`).

---

## 🧩 3. Asset Specifications (KFM-STAC v11)

### 🌿 vegetation-water.tif — VWC Raster

- Units: `"kg/m2"` or `"dimensionless"` depending on SMAP retrieval mode  
- `raster:bands[]` → nodata, scale, offset, bit-depth  
- `proj:*` parameters for EASE-Grid 2.0  
- `kfm:unit`  
- `kfm:uncertainty_link` → ties to uncertainty raster  

Used in:

- Ecohydrology models  
- Biomass-moisture mapping  
- Focus Mode v3 vegetation context  
- Story Node v3 environmental interpretation  

---

### 📈 vegetation-uncertainty.tif — Uncertainty Raster

Provides:

- Per-pixel retrieval uncertainty  
- Radiometer noise propagation estimates  
- Sensor geometry-dependent error values  

Metadata includes:

- `kfm:uncertainty_type: "radiometric"`  
- `kfm:error_model`  
- `kfm:stdev`  

Used by downstream:

- Fire-risk modeling  
- Seasonal vegetation analysis  
- Context-aware uncertainty rendering in UI (indicator bars, overlays)

---

### ⚠️ qa-flags.tif — QA / RFI Mask

Contains:

- Radiometric QC codes  
- RFI detection  
- Gain stability anomalies  
- Retrieval-confidence anomalies  

Metadata must include:

- `kfm:qa_flag_schema`  
- `kfm:qa_values` (legend)  
- `kfm:qa_interpretation`  

---

### 🧾 metadata.json — Orbit/Grid/Provenance Metadata

Must contain:

- NASA L2/L3 VWC product IDs  
- Orbit time / incidence geometry  
- EASE-Grid definitions  
- Calibration notes  
- Provenance chain (PROV-O)  
- CARE/H3 sovereignty metadata  
- Masking rules + `"kfm:mask_applied"`  

This file is used by all per-year asset bundles.

---

## 🔐 4. Governance & Sovereignty

VWC and biomass indicators can reveal:

- vegetation stress  
- land-management practices  
- spatio-cultural land transitions  
- heritage-landscape exposure dynamics  

Therefore:

- CARE-A/B classification applies  
- H3-based generalization is required in sovereign & high-sensitivity areas  
- `"kfm:mask_applied"` must appear for masked Items  
- All derived products must include uncertainty + provenance  

Validated through:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`  

---

## 🧪 5. QA & Validation Requirements

Validation includes:

- Structural COG validation  
- Raster-grid coherence (VWC, QA, uncertainty)  
- BBox/geometry alignment  
- Temporal consistency checks  
- Cross-sensor QA vs:
  - SMAP soil moisture  
  - HydroGNSS biomass/wetness indicators  
  - Landsat/Sentinel NDVI/EVI  
  - VIIRS fire/thermal  
  - ERA5 vegetation and surface fluxes  

QA logs → `docs/data/satellites/smap/qa/`  
Telemetry → `releases/<version>/data-telemetry.json`

---

## 🔁 6. Ingestion → Lineage Workflow

```
NASA SMAP L3 Vegetation Water Product
 → decode + EASE-Grid mapping
 → integrate QA/RFI
 → derive VWC + biomass-moisture indices
 → compute uncertainty
 → generate COG templates
 → enforce CARE/H3 governance
 → register as global STAC assets
 → export lineage (PROV-O)
 → emit OpenLineage + Telemetry
```

All steps are WAL-safe and deterministic.

---

## 🔮 7. Applications Inside KFM

### Climate  
- Vegetation stress diagnostics  
- Seasonal greenness/hydration cycles  

### Ecology  
- Fire-risk analytics  
- Grassland/plains moisture modeling  

### Archaeology  
- Visibility of cultural materials  
- Biomass-driven land-use interpretation  

### Story Node v3  
- Environmental sequence overlays  
- Seasonal descriptors for historical events  

### Focus Mode v3  
- Vegetation-wetness context for entities & events  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                               |
|--------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Created global VWC asset README; emoji layout; STAC v11 compliance; CARE/H3 governance; CI-safe.     |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal asset overview.                                                                        |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ VWC STAC Home](../README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

