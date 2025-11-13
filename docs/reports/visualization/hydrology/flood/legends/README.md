---
title: "🗺️ Kansas Frontier Matrix — Flood Visualization Legends Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/hydrology/flood/legends/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Hydrology Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reports-visualization-hydrology-flood-legends-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Flood Visualization Legends Index**  
`docs/reports/visualization/hydrology/flood/legends/README.md`

**Purpose:**  
Provide a curated, standardized collection of **colorbars, symbology keys, hazard overlays, and accessibility-compliant visual encodings** for flood-related maps, animations, and 3D renderings within the Kansas Frontier Matrix (KFM).  
Ensures reproducible, ethically governed, and accessible hydrological visualization practices under **FAIR+CARE**, **ISO 19115**, and **MCP-DL v6.3**.

![Docs MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Flood visualizations—especially inundation maps, recurrence heatmaps, and hydrological risk layers—must use **consistent, accessible, and FAIR+CARE-aligned legend systems**.  
This directory stores all **legend assets**, including:

- Color ramps for depth, severity, recurrence, and confidence  
- Symbology for rivers, basins, and hydrological boundaries  
- Accessibility-validated palettes for colorblind users  
- CARE-restricted categories and masked-region indicators  

Each legend is linked to:
- Its generating **pipeline**,  
- Its **metadata JSON**, and  
- Its **STAC/DCAT** registry entry for global discoverability.

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/hydrology/flood/legends/
├── README.md                    # This file
├── colorbars/                   # PNG/SVG color ramps (CB-safe)
│   ├── flood_depth_viridis.png
│   ├── flood_severity_cb.png
│   └── recurrence_heatmap.svg
│
├── symbols/                     # Iconography and hydrologic symbols
│   ├── river_outline.svg
│   ├── highflow_triangle.svg
│   ├── masked_region_hatch.svg
│   └── watershed_boundary.svg
│
└── metadata/                    # Legend-specific metadata records
    ├── flood_depth_viridis.json
    ├── masked_region_hatch.json
    └── recurrence_heatmap.json
```

---

## 🎨 Legend Standards (FAIR+CARE + WCAG)

| Category | Requirement | Standard |
|----------|-------------|----------|
| **Colorblind Safety** | Must provide CB-safe palettes (e.g., Viridis, Cividis) | WCAG 2.1 AA |
| **Contrast Minimums** | 4.5:1 for critical boundaries and overlays | WCAG 1.4.3 |
| **Accessibility Labels** | Legends must include alt-text and aria-label metadata | WCAG 1.1.1 |
| **CARE Restrictions** | Sensitive hydrology areas must use masking or hatching, not precise coordinates | FAIR+CARE |
| **Reusability** | Legends must be linked to STAC/DCAT visualization items | FAIR |
| **Interoperability** | Vector icons must use standard SVG semantics | ISO 19115 |

---

## 🧩 Metadata Requirements for Legends

Each legend **must** have a metadata file containing:

| Field | Description | Required |
|-------|-------------|----------|
| `id` | Unique legend identifier | ✅ |
| `type` | `colorbar` \| `symbol` \| `mask` | ✅ |
| `title` | Human-readable name | ✅ |
| `description` | What the legend represents | ✅ |
| `license` | SPDX or CC | ✅ |
| `care_status` | `approved`, `restricted`, etc. | ⚙️ |
| `accessibility_score` | WCAG 2.1 AA compliance score | ⚙️ |
| `created` | ISO timestamp | ⚙️ |
| `source_visualizations` | Which maps/charts use it | ⚙️ |

---

## 🧠 Example Legend Metadata (Colorbar)

```json
{
  "id": "legend_flood_depth_viridis_v10",
  "type": "colorbar",
  "title": "Flood Depth Gradient — Viridis",
  "description": "Colorblind-safe flood depth gradient for inundation maps (0–6m).",
  "license": "CC-BY-4.0",
  "care_status": "approved",
  "accessibility_score": 1.0,
  "created": "2025-11-12T10:15:00Z",
  "source_visualizations": ["kfm_flood_extent_2025_v10"]
}
```

---

## ⚙️ Validation Workflows

| Workflow | Purpose |
|----------|----------|
| `visualization-validate.yml` | Confirms legend–visualization linkage integrity |
| `stac-validate.yml` | Ensures legends attached to STAC visualization Items |
| `faircare-validate.yml` | Validates CARE masking & ethical compliance |
| `telemetry-export.yml` | Records legend generation & usage metrics |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|---------|---------|
| v10.2.0 | 2025-11-12 | Hydrology Visualization Council | Created flood legend index with WCAG/FAIR+CARE-compliant metadata structure. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Governed under **Master Coder Protocol v6.3** · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Flood Visualizations](../README.md) · [Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

