---
title: "🗺️ Kansas Frontier Matrix — Visualization Reports Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/reports-visualization-v2.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Visualization Reports Index**  
`docs/reports/visualization/README.md`

**Purpose:**  
Provide a **unified, FAIR+CARE-certified directory** for all visualization outputs generated across Kansas Frontier Matrix (KFM) analytical pipelines.  
Includes **maps**, **dashboards**, **animations**, **3D scenes**, and **explainability visualizations** tied to reproducible workflows, SBOM-tracked assets, and telemetry logs.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../../../README.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-green)](../../../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Visualization_Ethics-orange)](../../../standards/faircare.md)  
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()

</div>

---

## 📘 Overview

This directory aggregates **rendered visual artifacts** used for analytical validation, interpretive storytelling, Focus Mode dashboards, and public-facing reporting.  
Each visualization is required to include:

- **Linked provenance** (dataset IDs, commit SHAs, STAC/DCAT metadata)  
- **FAIR+CARE visualization ethics review**  
- **Generalization of sensitive cultural coordinates when required**  
- **Telemetry records** (energy, carbon, rendering performance)

Assets are produced from deterministic workflows to ensure full reproducibility for scientific, educational, and community governance use.

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/
├── README.md
│
├── archaeology/                          # Archaeological & cultural overlays
│   ├── paleo_overlay.png
│   ├── density_timeline.gif
│   ├── settlement_hotspots.geojson
│   └── provenance.json
│
├── hydrology/                            # Hydrology + hazards
│   ├── drought_frequency_map.png
│   ├── flood_extent_animation.mp4
│   ├── correlation_heatmap.svg
│   └── provenance.json
│
├── focus_mode/                           # Focus Mode UI + explainability frames
│   ├── timeline_panel.png
│   ├── 3d_viewport_capture.webp
│   ├── shap_explainability.png
│   └── provenance.json
│
└── assets/                               # Shared textures, legends, colorbars
    ├── colorbar_plasma.svg
    ├── ui_legend_dark.png
    └── a11y_high_contrast_palette.json
```

---

## 🧩 Visualization Metadata Standard (v10.2)

Each visualization bundle must include a `provenance.json` with:

```json
{
  "asset_id": "viz_hydrology_drought_frequency_2025",
  "generated_by": "workflow:hydrology-visualization.yml",
  "datasets_used": ["processed_hydrology_summary_v10.2.0", "climate_normals_1991_2020"],
  "commit_sha": "<latest-commit-hash>",
  "stac_item": "data/stac/hydrology/drought_frequency_v10.2.0.json",
  "faircare_review": "approved",
  "sensitivity_class": "low",
  "telemetry_ref": "releases/v10.2.0/focus-telemetry.json",
  "license": "CC-BY 4.0"
}
```

FAIR+CARE visualization ethics require that:
- Sensitive archaeological coordinates must be **generalized**  
- Indigenous territorial boundaries must include **contextual disclaimers**  
- Climate/hazard maps must include **uncertainty annotations**  
- Dashboard captures must include **a11y auditing tags**

---

## 🧾 Visualization Standards & Compliance

| Category | Requirement | Standard |
|---------|-------------|----------|
| **Map Projections** | EPSG:4326 or EPSG:3857; declare CRS in metadata | ISO 19111 |
| **Raster Outputs** | Include colorbar legend + a11y contrast certification | WCAG 2.1 AA |
| **Vector Layers** | Must expose metadata for scale, simplification, masking | STAC 1.0 |
| **Animations** | Include frame timestamps + pipeline version | KFM Animation Spec v3 |
| **3D Scenes** | Materials + lighting documented for reproducibility | Cesium CZML Spec |
| **Dashboard Captures** | Provide context, filter states, and dataset references | Focus Mode v2 |
| **Explainability Visuals** | SHAP/LIME/IG outputs must include model version & seed | AI Ethics Spec |

---

## ⚙️ FAIR+CARE Visualization Ethics Alignment

### FAIR

| Principle | Implementation |
|----------|----------------|
| **Findable** | STAC/DCAT metadata registered; asset IDs unique per release. |
| **Accessible** | CC-BY outputs; downloadable formats (PNG/SVG/GIF/MP4). |
| **Interoperable** | GeoJSON, TIFF/COG, CZML, JSON-LD. |
| **Reusable** | Versioned outputs linked to commit SHA and SBOM. |

### CARE

| Principle | Implementation |
|----------|----------------|
| **Collective Benefit** | Visuals support research, education, and public good. |
| **Authority to Control** | Tribal partners approve cultural visualizations. |
| **Responsibility** | Sensitive locations masked or aggregated. |
| **Ethics** | No depictions that risk cultural harm or misrepresentation. |

---

## 🧠 Rendering Telemetry & Sustainability Metrics

All rendering workflows export sustainability metrics into `focus-telemetry.json`:

| Metric | Description | Target |
|--------|-------------|---------|
| **energy_wh** | Energy consumed during rendering runs | ≤ 12 Wh |
| **carbon_gco2e** | CO₂e emissions of GPU/CPU render | ≤ 0.004 gCO₂e |
| **render_time_ms** | Time to render visualization | ≤ 2500 ms |
| **a11y_contrast_score** | WCAG 2.1 AA pass rate | ≥ 98% |

These metrics enable continuous optimization and environmental accountability per ISO 50001.

---

## 🧪 Validation Workflows

| Workflow | Purpose | Output |
|----------|---------|---------|
| `visualization-validate.yml` | Ensures metadata, a11y contrast, CRS, scale, legends | `reports/visualization/validate.json` |
| `faircare-validate.yml` | CARE-sensitive layer detection and masking compliance | `reports/fair/faircare_summary.json` |
| `docs-lint.yml` | Lints documentation, provenance, and captions | `reports/docs_lint.json` |
| `telemetry-export.yml` | Merges rendering metrics into unified ledger | `focus-telemetry.json` |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.2.0 | 2025-11-12 | FAIR+CARE Visualization Board | Upgraded visualization metadata schema, added explainability visual support, sustainability targets, and STAC/DCAT alignment. |
| v10.1.0 | 2025-11-11 | FAIR+CARE Council | Initial creation for visualization directory. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
**Diamond⁹ Ω / Crown∞Ω Ultimate Certified**

[Back to Reports Index](../README.md) · [Standards Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
