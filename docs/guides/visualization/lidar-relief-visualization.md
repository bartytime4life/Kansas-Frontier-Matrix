---
title: "🗺️ Kansas Frontier Matrix — LiDAR Relief Visualization (SVF + LRM Integration)"
path: "docs/guides/visualization/lidar-relief-visualization.md"
version: "v9.7.0"
last_updated: "2025-11-09"
review_cycle: "Biannual / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/visualization-terrain-v1.json"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — LiDAR Relief Visualization (SVF + LRM Integration)**
`docs/guides/visualization/lidar-relief-visualization.md`

**Purpose:**  
Define and standardize terrain visualization workflows—**Sky-View Factor (SVF)** and **Local Relief Model (LRM)**—for LiDAR-based archaeological and geomorphological prospection.  
Ensures reproducible FAIR+CARE-aligned visualization across KFM datasets, enabling discovery of subtle landscape features such as buried mounds, trails, terraces, and hydrological remnants.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY-green)](../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)](../../../docs/standards/FAIR-CARE.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen)](../../../releases/v9.7.0/)
</div>

---

## 📘 Overview

The **Sky-View Factor (SVF)** and **Local Relief Model (LRM)** techniques enhance LiDAR Digital Elevation Models (DEMs) by highlighting fine-scale terrain irregularities independent of illumination direction.  
In KFM, they serve as core raster derivatives supporting archaeological discovery, hydrological mapping, and change detection across Kansas.

---

## 🗂️ Directory Layout
```bash
KansasFrontierMatrix/
├── data/
│   ├── processed/
│   │   ├── lidar/                     # LiDAR DEM & derived products
│   │   │   ├── svf/                   # Sky-View Factor outputs
│   │   │   ├── lrm/                   # Local Relief Models
│   │   │   └── combined/              # Composite visualizations (SVF+LRM)
│   │   └── metadata/                  # Processing metadata, provenance
│   └── raw/lidar/                     # Source LAS/LAZ tiles
│
├── docs/
│   ├── guides/visualization/          # Visualization guides
│   └── standards/telemetry/           # Visualization telemetry schemas
│
└── src/pipelines/terrain/             # Automated SVF/LRM pipelines
```

---

## 🧩 Techniques Overview

| Technique | Concept | Visualization Goal |
|------------|----------|---------------------|
| **Sky-View Factor (SVF)** | Calculates openness to the sky for each DEM cell; lower values indicate enclosed or concave features. | Highlights depressions, ditches, and enclosure features with reduced directional bias. |
| **Local Relief Model (LRM)** | Removes large-scale topography via smoothing and subtraction. | Emphasizes small-scale terrain deviations such as foundations or embankments. |

---

## ⚙️ Parameter Guidelines

| Technique | Key Parameter | Typical Range | Notes |
|------------|----------------|----------------|-------|
| **SVF** | Search radius | 5 – 25 m | Smaller for micro-relief; larger for broad forms |
| | Directions | 8 – 32 | Higher = less azimuthal bias |
| | Minimum angle | 0° – 5° | Higher values exaggerate depth contrast |
| **LRM** | Filter radius | 5 – 50 m | Defines scale of “local” topography |
| | Smoothing type | Gaussian / mean / morphological | Gaussian preferred for continuity |
| | Normalization | Optional (0 – 255) | Improves interpretability |

---

## 🧾 Software Workflows

### GRASS GIS
```bash
# Sky-View Factor
r.skyview input=dem output=svf n_directions=16 maxdistance=20

# Local Relief Model
r.local.relief input=dem output=lrm filter_radius=15
```

### Relief Visualization Toolbox (RVT)
- Supports SVF, Openness, LRM, Multidirectional Hillshade.
- Combine rasters in QGIS using *Multiply* blending.

### QGIS Workflow
1. Generate SVF with RVT or WhiteboxTools.  
2. Create LRM via **Raster → Terrain Analysis → Local Relief Model**.  
3. Combine in Raster Calculator:
   ```text
   ("SVF@1" * 0.6) + ("LRM@1" * 0.4)
   ```
4. Adjust brightness, contrast, or color ramps.

---

## 🧩 Archaeological Case Studies

| Region | Study | Visualization Outcome |
|---------|--------|------------------------|
| **Maya Lowlands (Belize/Guatemala)** | Chase et al. 2021 — *Standardizing Visualization in Ancient Maya LiDAR Research* | SVF + LRM revealed terraces, causeways, and berms beneath dense canopy. |
| **Central Europe (Slovenia)** | Kokalj & Hesse 2017 — *Sky-View Factor as a Relief Visualization Technique* | Combined SVF with Openness to map prehistoric enclosures. |
| **Teotihuacan Valley, Mexico** | Štular et al. 2012 | Diffuse SVF illumination highlighted buried platforms invisible in hillshade. |
| **Germany (Neolithic Cursuses)** | Doneus & Briese 2011 | LRM isolated faint linear earthworks despite ploughing. |

---

## 🧩 Integration with Kansas Frontier Matrix

- Store outputs in `data/processed/lidar/svf/` and `data/processed/lidar/lrm/`.
- Generate combined rasters for visualization overlays.  
- Record processing metadata:
  ```json
  {
    "processing_tool": "GRASS GIS v8.3",
    "parameters": {"svf_radius": 20, "lrm_filter": 15},
    "generated": "2025-11-09",
    "provenance": "USGS 1m LiDAR tiles (EPSG:26914)"
  }
  ```
- Export to **Cloud-Optimized GeoTIFF (COG)** format for STAC compatibility.
- Link telemetry data under `telemetry/visualization/terrain.json`.

---

## ⚖️ FAIR+CARE Alignment

| Principle | Implementation |
|------------|----------------|
| **Findable** | Each derivative raster assigned DOI and metadata record. |
| **Accessible** | Stored as COG via public STAC endpoint. |
| **Interoperable** | Tagged with OGC-standard projection & DCAT fields. |
| **Reusable** | Licensed under CC-BY 4.0 with documented processing chain. |
| **Collective Benefit** | Prioritizes Indigenous landscape transparency. |
| **Authority to Control** | Community-governed visualization parameters. |
| **Responsibility** | Ethical release with energy & data provenance metrics. |
| **Ethics** | Avoids revealing culturally sensitive sites in public layers. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-09 | A. Barta / Focus AI | Initial LiDAR SVF + LRM visualization standard integrated with MCP-DL v6.3 |
| v9.6.0 | 2025-10-10 | FAIR+CARE Council | Added parameter harmonization section |
| v9.5.0 | 2025-09-01 | Terrain Team | Prototype workflows for GRASS GIS and RVT |

---

<div align="center">

© 2025 Kansas Frontier Matrix. All Rights Reserved.  
**Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified**

[Back to Visualization Guides](../README.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)
</div>
