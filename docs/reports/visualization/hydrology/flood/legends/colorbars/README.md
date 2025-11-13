---
title: "🎨 Kansas Frontier Matrix — Flood Colorbar Legends Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/hydrology/flood/legends/colorbars/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Hydrology Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/reports-visualization-hydrology-flood-colorbars-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Flood Colorbar Legends Index**  
`docs/reports/visualization/hydrology/flood/legends/colorbars/README.md`

**Purpose:**  
Provide a **centralized, accessibility-validated collection of color ramps** used across all flood-related KFM visualizations—depth maps, recurrence charts, inundation animations, and hydrodynamic risk products.  
These colorbars are **FAIR+CARE compliant**, **WCAG 2.1 AA accessible**, and fully traceable via STAC/DCAT metadata.

![Docs MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Flood depth, severity, and recurrence visualizations require **consistent, colorblind-safe, semantically meaningful colorbars**.  
This directory houses all such colorbars, each with its own **metadata record**, provenance, accessibility scoring, and linkage to specific KFM maps and animation artifacts.

Colorbars support:
- Flood depth (continuous & binned)
- Flood severity index layers
- Recurrence interval heatmaps (RI-10, RI-50, RI-100)
- Confidence/uncertainty layers
- CARE-generalized masked regions

All assets are validated through KFM’s visualization governance workflows and registered in STAC.

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/hydrology/flood/legends/colorbars/
├── README.md                            # This file
├── flood_depth_viridis.png              # Colorblind-safe depth ramp (0–6m)
├── flood_depth_cividis.png              # Alternative WCAG-safe depth ramp
├── flood_severity_cb.png                # Severity ramp for hazard overlays
├── recurrence_heatmap.svg               # 10–100 yr recurrence interval ramp
├── uncertainty_bluepurple.png           # Confidence/uncertainty gradient
└── metadata/
    ├── flood_depth_viridis.json
    ├── flood_depth_cividis.json
    ├── flood_severity_cb.json
    ├── recurrence_heatmap.json
    └── uncertainty_bluepurple.json
```

---

## 🎨 Colorbar Standards (WCAG + FAIR+CARE)

| Requirement | Description |
|------------|-------------|
| **Colorblind Safety** | All colorbars must use CB-safe palettes (Viridis, Cividis, Tol, CB-Safe Red-Yellow). |
| **Contrast Ratio** | Minimum 4.5:1 for key breakpoints and boundaries. |
| **Semantic Meaning** | Hues must follow intuitive hydrologic meaning (cool = shallow, warm = deep/severe). |
| **Accessibility Metadata** | Each colorbar requires accurate `alt`, `aria-label`, and provenance tags. |
| **CARE Sensitivity** | Masked-region palettes must not reveal sensitive tribal/archaeological flood impacts. |
| **Reusability** | Colorbars must be linked to STAC Items for downstream reproducibility. |

---

## 🧩 Required Metadata for Each Colorbar

| Field | Purpose |
|--------|----------|
| `id` | Unique registry ID |
| `type` | Always `"colorbar"` |
| `title` | Human-friendly name |
| `description` | What the gradient encodes |
| `license` | SPDX or CC |
| `care_status` | `approved` / `restricted` |
| `accessibility_score` | 0–1 WCAG compliance |
| `created` | ISO timestamp |
| `source_visualizations` | Array of KFM visualizations using this legend |

---

## 🧠 Example Metadata (Recurrence Heatmap)

```json
{
  "id": "legend_recurrence_heatmap_v10",
  "type": "colorbar",
  "title": "Recurrence Interval Heatmap (10–100 yr)",
  "description": "Colorblind-safe ramp for flood recurrence interval mapping.",
  "license": "CC-BY-4.0",
  "care_status": "approved",
  "accessibility_score": 1.0,
  "created": "2025-11-12T11:20:00Z",
  "source_visualizations": [
    "kfm_flood_recurrence_2025_v10",
    "kfm_flood_risk_timeseries_v10"
  ]
}
```

---

## ⚙️ Validation Workflows

| Workflow | Purpose |
|----------|----------|
| `visualization-validate.yml` | Ensures the colorbar matches map encoding + metadata integrity |
| `faircare-validate.yml` | Confirms ethical masking rules for sensitive region colorbars |
| `stac-validate.yml` | Validates STAC/DCAT binding for legend assets |
| `telemetry-export.yml` | Logs sustainability + energy metrics for colorbar generation |

---

## 🧭 Usage Guidance

- Always include colorbar attribution in visualization markdowns or UI:  
  `Legend: flood_depth_viridis (KFM v10 · CC-BY 4.0)`
- Use **vector (SVG)** for anything requiring scalable clarity.  
- Use **PNG** for raster gradient bars in animation frames.  
- For CARE-sensitive datasets, **do not** use depth or severity colorbars that reveal localized extremes—use **hatching/aggregation palettes** instead.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|---------|---------|
| v10.2.0 | 2025-11-12 | Hydrology Visualization Council | Created flood colorbar index with metadata schema & FAIR+CARE alignment. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Flood Legends](../README.md) · [Flood Visualization](../../README.md)

</div>

