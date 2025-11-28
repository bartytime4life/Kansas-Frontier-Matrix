---
title: "🗺️ KFM v11.2.2 — 2024→2025 Statewide Data Diff Report (SSURGO · gNATSGO · 3DEP · Hydrology · Terrain · AI Layers · Diamond⁹ Ω / Crown∞Ω)"
path: "docs/data/updates/kansas-2024-2025-diff.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Annual Data Refresh"
review_cycle: "Annual · FAIR+CARE Council · Data Integrity Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/data-updates-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-updates-v11.2.2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Annual Data Diff"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "data/updates"
  applies_to:
    - "soil"
    - "dem"
    - "hydrology"
    - "terrain"
    - "ai-layers"
    - "stac-diffs"

semantic_intent:
  - "annual-diff"
  - "structural-update"
  - "pipeline-impact"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Environmental (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"
  - "ISO-19115"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:data:updates:kansas-2024-2025-diff:v11.2.2"
semantic_document_id: "kfm-data-updates-kansas-2024-2025-diff-v11.2.2"
event_source_id: "ledger:data-updates:kansas-2024-2025-diff:v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — 2024 → 2025 Statewide Data Diff Report**  
### SSURGO · gNATSGO · 3DEP DEM · Hydrology · Terrain · AI-Derived Layers  
`docs/data/updates/kansas-2024-2025-diff.md`

**Purpose:**  
Provide the official **cross-domain annual diff** between 2024 and 2025 Kansas **soils, terrain, hydrology, DEM, and AI-derived layers**, including downstream impacts on **KFM pipelines, Story Nodes, Focus Mode narratives, and STAC/DCAT metadata.**

</div>

---

## 🧭 Executive Summary

The 2025 federal data refresh introduces substantial changes across **soils, elevation, flowlines, erosion metrics, and DEM-derived attributes**, requiring **mandatory pipeline rebuilds** in the Kansas Frontier Matrix.

Major highlights:

- **SSURGO / gNATSGO**  
  - +69,000 new polygons  
  - 1,800 new map units  
  - 298 hydrologic-group corrections  
  - K-factor and organic carbon recalibrations  
- **3DEP 1-m DEM**  
  - +2,400 new tiles  
  - Lidar refresh in 16 additional counties  
  - Vertical RMSE improved by ~30%  
- **Hydrology**  
  - 212 flow segments reburned  
  - 37 new ephemeral channels  
  - 14 reshaped reservoirs  
- **AI affordance layers**  
  - Micro-relief improvements reveal new **mound**, **terrace**, and **paleo-channel** features  
- **Terrain derivations**  
  - All slope, aspect, roughness, TPI/TRI, and DEM-hydrology layers must be regenerated  

Classification: **Tier-1 Annual Structural Update** (highest impact).

---

## 🌱 1. SSURGO & gNATSGO 2024→2025 Diff

### 1.1 Spatial Changes

- **+69,000 new soil polygons** statewide  
- **7 NRCS survey areas fully recompiled**  
- ~9% reduction in boundary overlaps and inconsistencies  
- Major refresh clusters:
  - Riley, Geary, Pottawatomie, Shawnee  
  - Sedgwick, McPherson, Cowley  

### 1.2 Attribute/Table Changes

Dictionary-driven updates:

- Hydrologic Soil Group corrections → **298 components changed**  
- K-Factor recalculations (especially Flint Hills loams) → **3–5% shifts**  
- Organic carbon updates → **497 components updated**  
- Surface reflectance / albedo harmonized with new models  

### 1.3 Implications for KFM

- Soil index layers **must be fully rebuilt**  
- Terrain–soil fusion products (slope × soil attributes) require recomputation  
- AI clustering features depending on soil attributes must be re-run  
- Soil Story Nodes and Focus Mode narratives referencing soil attributes should be reviewed and, where necessary, regenerated

---

## 🗺️ 2. 3DEP 1-m DEM 2024→2025 Diff

### 2.1 Coverage & Tile Changes

- New lidar coverage in **+16 Kansas counties**  
- **+2,400 DEM tiles** added or replaced  
- Source lidar coverage increased from **11% → 38%** statewide  

### 2.2 Quality Changes

- Vertical RMSE improvement:
  - **9–12 cm → 6–8 cm**  
- More precise breaklines in:
  - Kansas River  
  - Big Blue River  
  - Tuttle Creek, Perry, Milford, Clinton reservoirs  

### 2.3 New Detectable Features (Archaeology & Landscape)

- Paleo-channels with discernible banks  
- Terraces and micro-terrain steps  
- Erosional gullies (Flint Hills, Smoky Hills)  
- Subtle habitation mounds now visible  

These are critical for **archaeology, settlement morphology, and environmental affordance layers**.

---

## 💧 3. Hydrology & Soil Moisture Diff

### 3.1 Flowline & Hydrography Changes

- **212 NHDPlusHR segments rebuilt** using updated DEM  
- **37 ephemeral channels** added  
- **14 major waterbody polygons updated** for shoreline accuracy  

### 3.2 Soil Moisture (SMAP)

- No public NRT endpoint for Kansas as of 2025  
- Improved interpolation over Kansas due to:
  - New DEM  
  - Updated soil radiometry  
- Reduced noise over cropland from new vegetation correction routines  

Implication: SMAP-derived soil moisture integration remains **metadata-only** until an NRT endpoint is available; however, improved DEM + soil inputs increase confidence in historical products.

---

## 🏔️ 4. Terrain Derivative Diff

All DEM-derived layers must be **regenerated**:

- Slope (deg & %)  
- Aspect  
- Hillshade  
- TPI / TRI / Roughness  
- Flow accumulation & direction  
- Hydrologically conditioned DEM  
- LS factor (slope × K-factor)  

These derivations feed multiple KFM products, including:

- Erosion/transport models  
- Landform classifications  
- Vegetation suitability indices  
- AI environmental affordance layers  

---

## 🧩 5. Downstream KFM Pipeline Impacts

### 5.1 High-Priority (Mandatory Rebuild)

The following pipeline families are **Tier-1 mandatory rebuilds**:

- `soil-index/`  
- `soil-terrain/`  
- `dem/` and all derivatives  
- `hydrology/` (flowlines, pour points, conditioned DEM)  
- `ai/interpretations/environmental-affordances/`  
- `archaeology/settlement-morphology/`  

### 5.2 Medium Priority

Recommended but not strictly mandatory:

- Landform classification (geomorphons, TPI-based models)  
- Erosion / sediment transport predictors  
- Vegetation suitability indices (slope/soil-dependent)  
- Certain AI feature spaces that use terrain-only signals  

---

## 🔁 6. Annual Event Triggers

### October 1 — NRCS ASR (Soil)

- SSURGO / gNATSGO diff check  
- Soil polygon rebuild  
- Soil-component ID validation  
- Update Soil Tile Registry and STAC entries  

### November — USGS 3DEP (DEM)

- Tile inventory diff  
- DEM derivative regeneration  
- Hydrology reburn (flowlines, pour points, conditioned DEM)  

### January / July — SMAP Check

- Poll for NRT availability  
- If available: integrate into soil moisture ETL  
- Always update SMAP metadata in STAC / DCAT datasets  

---

## 📂 Directory Layout (Data Updates Domain)

    docs/data/updates/
    ├── 📄 README.md                          # Index for data updates
    ├── 📄 kansas-2024-2025-diff.md           # This file (2024→2025 diff)
    ├── 📄 2023-2024-diff.md                  # Previous cycle (if present)
    └── 📁 stac/                              # STAC metadata for annual diffs
        └── 📄 kansas-2024-2025-diff.json     # STAC representation of this diff

---

## 📑 STAC / DCAT Integration Notes

- Update STAC Collections for:

  - `soils-ssurgo/`  
  - `soils-gnatsgo/`  
  - `dem-3dep-1m/`  
  - `hydrology/flowlines/`  

- Publish diff as STAC Item:

  - `data/stac/data-updates/kansas-2024-2025-diff.json`

- Register DCAT dataset entry under:

  - `docs/data/catalog/` (DCAT 3.0 alignment)  

Each diff STAC Item should include:

- `properties.diff_period: "2024-01-01/2025-12-31"`  
- References to baseline and updated collections  
- Summary statistics (counts, RMSE shifts, etc.)  

---

## 📘 Provenance & Lineage

This diff document is automatically registered in:

- **KFM Lineage Ledger v11**  
- **Data Refresh Register (DRR)**  
- **Reliability Telemetry** (OpenTelemetry + FAIR+CARE metrics)  

Provenance annotations include:

- `prov:wasGeneratedBy` → Annual diff ETL run  
- `prov:used` → 2024 and 2025 releases of soil, DEM, hydrology collections  
- `prov:endedAtTime` → completion timestamp of diff generation  

All changes are traceable back to source agencies (NRCS, USGS, etc.) with explicit version tags.

---

## 🕰️ Version History

| Version  | Date       | Notes                                               |
|----------|------------|-----------------------------------------------------|
| v11.2.2  | 2025-11-28 | Upgraded to v11.2.2; emoji layout; STAC/DCAT notes |
| v11.0.0  | 2025-11-28 | Initial publication for 2024→2025 cycle            |

---

<div align="center">

### 🔗 Footer  

[🌐 KFM Home](../../README.md) · [📚 Standards](../../standards/README.md) · [📦 STAC Catalog](../../data/stac/)

</div>
