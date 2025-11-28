---
title: "🌀 KFM v11.2.2 — HRRR Smart Subsetting & Change-Aware Storage (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/atmo/hrrr-smart-subsetting/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
signature_ref: "../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../releases/v11.2.2/slsa-attestation.json"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/atmo-hrrr-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-hrrr-v11.2.2.json"
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
doc_kind: "Pipeline Runbook"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "pipelines/atmo"
  applies_to:
    - "etl"
    - "subset"
    - "delta-detection"
    - "stac-publication"

semantic_intent:
  - "atmospheric-data"
  - "cost-optimization"
  - "change-aware-storage"

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

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:pipelines:atmo:hrrr-smart-subsetting:v11.2.2"
semantic_document_id: "kfm-pipelines-atmo-hrrr-smart-subsetting-v11.2.2"
event_source_id: "ledger:pipelines-atmo-hrrr-smart-subsetting-v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🌀 **KFM v11.2.2 — HRRR Smart Subsetting & Change-Aware Storage**  
`docs/pipelines/atmo/hrrr-smart-subsetting/README.md`

**Purpose:**  
Cost-optimized, deterministic, change-aware HRRR ETL for Kansas, publishing KFM-STAC v11 Items with complete PROV-O lineage and FAIR+CARE alignment.

</div>

---

## 📘 Overview

This pipeline ingests NOAA HRRR CONUS from AWS Open Data and:

1. Clips HRRR fields to Kansas AOIs (statewide, county dissolves, research AOIs).  
2. Retains only variables needed for wind, smoke, visibility, temp, and cloud overlays.  
3. Computes change-aware deltas and **skips lakeFS commits** when the atmosphere is essentially unchanged.  
4. Publishes hourly STAC v11 Items with full provenance, telemetry, and grid metadata.

Outcome: **>90% storage reduction** with no loss of high-value atmospheric signal.

---

## 🧱 Architecture

### 1. HRRR Loader (xarray/Zarr)

- fsspec + zarr lazy chunk reads  
- CF metadata normalization  
- Units/time harmonization to KFM standards  
- UTC alignment (Temporal Contract v11)

### 2. AOI Subsetting

- Uses rioxarray `.rio.clip()` with pre-transformed AOI geometries  
- AOI masks cached under `data/work/atmo/hrrr/aoi_masks/`  
- Output tiles reprojected to EPSG:4326 COGs, aligned with KFM web stack

### 3. Variable Selector

Default variable set:

| Category | Variables |
|---------|-----------|
| Wind | `UGRD_10m`, `VGRD_10m`, `WINDgust_surface` |
| Temp | `TMP_2m`, `DPT_2m` |
| Visibility / Smoke | `VVIS_surface`, `PMTF*`, `HGT_surface` |
| Clouds | `TCDC_low`, `TCDC_mid`, `TCDC_high` |

Override via:

- `src/pipelines/atmo/hrrr/config/variables.yaml`

### 4. Delta Engine (Change-Aware)

Per-tile metrics:

- Mean and max Δ  
- Directional Δ (wind)  
- Percent-grid Δ above thresholds  
- Smoke/visibility class transitions  
- Cloud cover changes per layer  

Only if thresholds are exceeded will a new snapshot be **committed and published**.

### 5. lakeFS Commit & Tagging

Commit naming:

- `hrrr-{YYYYMMDDHH}-subset`  
- `hrrr-change-{YYYYMMDDHH}-{category}`  

Categories: `wind-shift`, `temp-change`, `smoke-arrival`, `visibility-drop`, `cloud-transition`.

### 6. STAC v11 Publication

Emits STAC Items under:

- `data/stac/atmo/hrrr/items/`

Each Item includes:

- `proj:epsg`, `grid:source`  
- AOI identifiers (`kfm:aoi_id`)  
- `derived_from` (HRRR source URI + lakeFS commit)  
- Per-asset SHA256 checksums  
- Energy (`energy_kwh`) and carbon (`carbon_gco2e`) telemetry  
- CF variable metadata and temporal extents  

---

## 📦 Directory Layout

    docs/pipelines/atmo/hrrr-smart-subsetting/
    ├── 📄 README.md                           # This file
    │
    ├── 🧬 src/pipelines/atmo/hrrr/            # Code, referenced path (monorepo)
    │   ├── 📜 loader.py                       # HRRR Zarr reader
    │   ├── ✂️ subsetter.py                    # AOI clipping and CRS transforms
    │   ├── 🔁 delta_engine.py                 # Change-detection thresholds
    │   ├── 🌐 publisher.py                    # STAC item generator
    │   └── 📁 config/
    │       ├── 🧾 variables.yaml              # Variable selection set
    │       └── 🧾 thresholds.yaml             # Delta thresholds
    │
    ├── 📁 data/work/atmo/hrrr/                # Work-layer outputs
    │   ├── 🗺️ aoi_masks/                      # Pre-generated spatial masks
    │   └── 🧩 subsets/                        # Hourly clipped HRRR tiles
    │
    ├── 📁 data/stac/atmo/hrrr/                # STAC metadata
    │   ├── 🌐 collection.json                 # STAC collection definition
    │   └── 📂 items/                          # Hourly STAC items
    │
    └── 🤖 .github/workflows/                  # CI integration
        └── 🌀 hrrr-smart-subsetting.yml       # CI workflow (cron hourly)

---

## 🔧 Delta Thresholds (Default v11)

| Variable Class | Condition to Trigger Commit |
|----------------|-----------------------------|
| Wind @10m | Max Δ ≥ 1.0 m/s OR direction Δ ≥ 10° over ≥5% AOI |
| Temperature @2m | Mean Δ ≥ 0.5 K |
| Visibility | Drop ≥ 1 km anywhere in AOI |
| Smoke | Any class/category shift in any cell |
| Cloud Cover | ≥20% change in low/mid/high layer coverage |

Override defaults via:

- `src/pipelines/atmo/hrrr/config/thresholds.yaml`

---

## 🧭 STAC & Metadata Alignment

Each HRRR STAC Item:

- Conforms to **STAC 1.0.0** and **KFM-STAC v11**  
- Includes spatial/temporal extents and AOI metadata  
- Declares license, processing steps, and derived-from lineage  
- Embeds PROV-O fields for ETL and lakeFS commit activities  
- References energy/carbon telemetry schemas for sustainability tracing  

---

## 🧪 Validation & CI/CD

The HRRR Smart Subsetting pipeline is covered by:

- **Unit tests** for loader, subsetter, delta engine, and publisher  
- **Contract tests** (KFM-PDC v11) on variables and thresholds  
- **STAC validation** via pystac/stac-validate  
- **Linting** (flake8, black, mypy)  
- **Telemetry checks** for energy and carbon fields  
- **FAIR+CARE audit** to ensure open, non-sensitive data practices  

CI workflow:

- `.github/workflows/hrrr-smart-subsetting.yml`  
- Runs on schedule (e.g., hourly) and on manual dispatch  
- Reports metrics to `telemetry_ref` paths defined in front-matter  

---

## 🧠 Story Node & Focus Mode Integration

This pipeline populates atmospheric Story Nodes and Focus Mode narratives:

- Wind stress on archaeological landscapes  
- Smoke plumes intersecting hydrology interpretation clusters  
- Visibility changes affecting travel corridors and affordances  
- Temperature regime shifts tied to environmental interpretations  

Story Nodes are written to:

- `data/story/atmo/hrrr/`

Focus Mode v3:

- Pulls HRRR-derived Story Nodes  
- Cites corresponding STAC Items and lakeFS commits  
- Enforces CARE filters (no sensitive locations; no re-identification of protected sites)  

---

## 🕰️ Version History

- **v11.2.2** — Integrated emoji-enhanced full directory tree; enforced single-fence rule; upgraded to KFM-MDP v11.2.2.  
- **v11.0.0** — Initial canonical release of HRRR Smart Subsetting & Change-Aware Storage pipeline.  

---

<div align="center">

### 🔗 Footer

[🌐 KFM Home](../../../README.md) · [📚 Standards](../../standards/README.md) · [📦 STAC Catalog](../../../data/stac/)

</div>
