---
title: "📘 Kansas Frontier Matrix — Flood Legend Metadata Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/hydrology/flood/legends/metadata/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Visualization Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/reports-visualization-hydrology-flood-legends-metadata-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📘 **Kansas Frontier Matrix — Flood Legend Metadata Index**  
`docs/reports/visualization/hydrology/flood/legends/metadata/README.md`

**Purpose:**  
Provide a unified, FAIR+CARE-compliant metadata index for all **flood visualization legend components** — including colorbars, symbols, linework, and annotations — used in hydrological map products across KFM.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory contains metadata documents describing all **flood legend components** used in the KFM hydrology visualization stack.  
Metadata ensures:
- Consistent symbol interpretation  
- High visual accessibility (WCAG 2.1 AA contrast tests)  
- STAC/DCAT discoverability  
- FAIR+CARE cultural and ethical review  
- Traceable provenance and checksum lineage  

These metadata files are used by:
- Hydrology rendering pipelines  
- KFM Focus Mode visual overlays  
- Web map clients (MapLibre, Cesium)  
- AI-driven visualization summaries  
- Public dashboards and reports  

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/hydrology/flood/legends/metadata/
├── README.md                                # This file
├── colorbars/                               
│   ├── colorbar_depth.json                   # Depth ramp metadata
│   ├── colorbar_risk.json                    # Flood risk categories
│   └── colorbar_velocity.json                # Flow velocity gradient
│
└── symbols/
    ├── flood_marker_major.json               # Major flood event icon metadata
    ├── flood_marker_minor.json               # Minor flood indicator metadata
    ├── flood_marker_flash.json               # Flash flood symbol metadata
    ├── levee_failure_icon.json               # Levee failure indicator metadata
    └── inundation_boundary.json              # Inundation boundary symbology metadata
```

---

## 🧩 Required Metadata Structure

Each metadata file must include:

| Field | Description |
|-------|-------------|
| `id` | Unique symbol or colorbar identifier |
| `title` | Human-readable legend component name |
| `description` | Purpose and semantic use-case |
| `component_type` | `colorbar` or `symbol` |
| `visual_properties` | Color, contrast, shape, WCAG testing |
| `care_status` | CARE review classification |
| `checksum_sha256` | SHA-256 integrity hash |
| `created` | ISO 8601 timestamp |
| `commit_sha` | Provenance tracking reference |
| `stac_item` | Optional STAC linkage for catalog integration |

---

## 🔍 Example Metadata Entry (Colorbar)

```json
{
  "id": "colorbar_flood_depth_v10",
  "title": "Flood Depth Gradient",
  "component_type": "colorbar",
  "description": "Represents estimated floodwater depth in meters.",
  "visual_properties": {
    "colors": ["#001F3F", "#0074D9", "#7FDBFF"],
    "contrast_rating": "AA"
  },
  "care_status": "approved",
  "checksum_sha256": "sha256-998cc0f1bd78df91...",
  "created": "2025-11-12T12:00:00Z",
  "commit_sha": "<latest-commit-hash>",
  "stac_item": "kfm-flood-visual-metadata-v10"
}
```

---

## ⚙️ FAIR+CARE Integration

| Principle | Implementation |
|-----------|----------------|
| **Findable** | STAC/DCAT registered legend metadata |
| **Accessible** | CC-BY 4.0 licensed JSON files |
| **Interoperable** | JSON-LD compatible structures |
| **Reusable** | Complete provenance + checksum tracking |
| **CARE** | Ensures no legend components misrepresent cultural sites |

---

## 🧪 Validation Pipelines

All metadata files undergo:

| Workflow | Function |
|----------|----------|
| `visualization-validate.yml` | Structure, checksum, and accessibility verification |
| `faircare-validate.yml` | CARE ethical review |
| `stac-validate.yml` | Catalog mapping tests |
| `telemetry-export.yml` | Sustainability & governance logging |

Outputs stored in:
```
reports/self-validation/visualization/
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|--------|--------|---------|
| v10.2.0 | 2025-11-12 | Hydrology Visualization Board | Created unified metadata index for flood legend components. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Flood Legends](../README.md) · [Visualization Index](../../../README.md)

</div>

