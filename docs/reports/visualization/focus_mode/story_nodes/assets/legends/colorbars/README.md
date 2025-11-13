---
title: "🌈 Kansas Frontier Matrix — Focus Mode Colorbar Legend Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/colorbars/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Visualization Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/reports-visualization-focusmode-colorbars-v1.json"
governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌈 **Focus Mode Colorbar Legend Assets**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/colorbars/README.md`

**Purpose:**  
Provide a centralized, FAIR+CARE-certified index for **colorbar legends** used in **Focus Mode Story Nodes**, hydrological maps, archaeological overlays, climate visualizations, and 3D narrative layers.

![Docs MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License CC-BY](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status Active](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Colorbars give users **immediate, intuitive understanding** of quantitative ranges in maps and visualizations.  
They are used across Focus Mode in:

- Hydrology layers (drought index, flood depth, groundwater change)  
- Climate and meteorology layers (precipitation, humidity, anomaly grids)  
- Landcover and soil layers  
- Archaeology overlays with generalized intensity tiers  
- 3D scene shading and elevation encoding (Cesium PBR materials)

Colorbar assets must follow STAC/DCAT metadata standards, include checksums, and pass FAIR+CARE audits wherever cultural or ecological sensitivity exists.

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/story_nodes/assets/legends/colorbars/
├── README.md                       # This file
├── precipitation.png
├── drought_index.svg
├── ground_water_change.svg
├── elevation_gradient.png
└── metadata/
    ├── README.md
    └── field_definitions.md
```

---

## 🎨 Colorbar Types & Usage

| Colorbar | Domain | Format | Description |
|----------|---------|---------|-------------|
| `precipitation.png` | Climate | PNG | Annual/seasonal precipitation intensity scale |
| `drought_index.svg` | Hydrology | SVG | Multi-year drought severity scale (−4 → +4) |
| `ground_water_change.svg` | Hydrology | SVG | Groundwater delta scale (recharge ↔ depletion) |
| `elevation_gradient.png` | 3D Terrain | PNG | Terrain elevation gradient for 3D Focus Mode |

---

## 🧾 Metadata Requirements (All Colorbars)

Each colorbar asset must include a metadata JSON file in the `metadata/` directory with:

| Field | Required | Description |
|-------|----------|-------------|
| `id` | ✅ | Unique ID for the colorbar |
| `title` | ✅ | Human-readable name |
| `domain` | ✅ | hydrology, climate, archaeology, landcover, terrain |
| `min_value` / `max_value` | ⚙️ | Numeric min/max for continuous scales |
| `units` | ⚙️ | e.g., mm/year, meters, index (−4 to +4) |
| `format` | ✅ | PNG or SVG |
| `checksum_sha256` | ✅ | Integrity verification |
| `provenance` | ✅ | Processing pipeline, raw source origin |
| `care` | ⚙️ | CARE governance block for sensitive domains |
| `updated` | ✅ | ISO timestamp |

---

## 🧩 Example Colorbar Metadata

```json
{
  "id": "kfm_colorbar_precip_v10",
  "title": "Annual Precipitation Gradient",
  "domain": "climate",
  "min_value": 0,
  "max_value": 1500,
  "units": "mm/year",
  "format": "PNG",
  "checksum_sha256": "sha256-29cf117e0abc93ef91a3...",
  "provenance": {
    "source": "NOAA CPC + Daymet",
    "method": "Linear gradient; RGB stops tuned for accessibility.",
    "workflow": "colorbar_render_v3",
    "commit_sha": "<latest-commit-hash>"
  },
  "care": {
    "status": "public",
    "statement": "No culturally sensitive information contained.",
    "reviewer": "FAIR+CARE Climate Committee",
    "date_reviewed": "2025-11-12"
  },
  "updated": "2025-11-12T19:00:00Z"
}
```

---

## ⚙️ FAIR+CARE Requirements for Colorbars

| Requirement | Description |
|-------------|-------------|
| **Accessibility** | Must meet WCAG color contrast rules |
| **Cultural Sensitivity** | Archaeology colorbars may require generalized intensity bins |
| **Sustainability** | Export pipelines must log telemetry (energy + carbon) |
| **Governance** | Every colorbar version is logged in the governance ledger |

---

## 🧠 Integration in Focus Mode

Colorbars are used in:

- **Legend drawers**  
- **Story Node side-panels**  
- **Map overlays (2D & 3D)**  
- **Time-based animated transitions**  
- **AI narrative generation (providing context)**  

Pipelines consuming colorbar assets:
- `focus-mode-render.yml`  
- `stac-validate.yml`  
- `ai-train.yml` (Explainability overlays)

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Visualization Board | Initial creation of colorbar asset index with metadata requirements and CARE alignment. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Legend Assets](../README.md)

</div>

