---
title: "🌈 Kansas Frontier Matrix — Flood Colorbar Metadata Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/hydrology/flood/legends/metadata/colorbars/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Visualization Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/reports-visualization-hydrology-flood-colorbars-v1.json"
governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌈 **Kansas Frontier Matrix — Flood Colorbar Metadata Index**  
`docs/reports/visualization/hydrology/flood/legends/metadata/colorbars/README.md`

**Purpose:**  
Provide FAIR+CARE-certified metadata definitions for all **flood visualization colorbars** used in hydrology analysis, dashboard displays, STAC visual layers, and Focus Mode overlays across the Kansas Frontier Matrix (KFM).

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Colorbars in hydrological flood visualizations represent **depth**, **velocity**, **risk**, and **uncertainty layers**.  
This directory contains metadata describing visual rules, accessibility compliance, contrast validation, and provenance for each colorbar.  
All definitions must conform to:
- WCAG 2.1 AA contrast standards  
- FAIR+CARE visualization ethics  
- STAC/DCAT compliant metadata schemas  
- MCP-DL v6.3 reproducibility rules  

These metadata files power:
- MapLibre/Leaflet flood visualization layers  
- Cesium 3D flood depth renderers  
- KFM Focus Mode interpretations and legend overlays  
- Scientific and educational dashboards

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/hydrology/flood/legends/metadata/colorbars/
├── README.md
├── colorbar_depth.json
├── colorbar_risk.json
├── colorbar_velocity.json
└── colorbar_uncertainty.json
```

---

## 🧩 Required Fields for Each Colorbar Metadata File

| Field | Description |
|-------|-------------|
| `id` | Unique identifier for the colorbar |
| `title` | Human-readable name |
| `description` | What the colorbar visually expresses |
| `visual_properties.colors` | Array of hex color codes |
| `visual_properties.contrast_rating` | WCAG contrast score |
| `visual_properties.scale_domain` | Min/max or category thresholds |
| `component_type` | Must be `"colorbar"` |
| `care_status` | CARE ethical classification |
| `checksum_sha256` | Integrity verification hash |
| `created` | ISO 8601 timestamp |
| `commit_sha` | Provenance for regeneration |
| `stac_item` | Optional STAC catalog link |

---

## 🧪 Example Colorbar Metadata (Depth)

```json
{
  "id": "colorbar_flood_depth_v10",
  "title": "Flood Depth Gradient",
  "description": "Displays estimated flood depth based on hydrological modeling.",
  "component_type": "colorbar",
  "visual_properties": {
    "colors": ["#001F3F", "#003C78", "#0074D9", "#7FDBFF"],
    "contrast_rating": "AA",
    "scale_domain": [0, 3, 6, 10]
  },
  "care_status": "approved",
  "checksum_sha256": "sha256-9ae33fa24ab8c0f123bdaf98...",
  "created": "2025-11-12T12:35:00Z",
  "commit_sha": "<latest-commit-hash>",
  "stac_item": "kfm-flood-depth-visual-v10"
}
```

---

## ⚙️ FAIR+CARE Integration

| Principle | Implementation |
|-----------|----------------|
| **Findable** | Metadata stored in STAC/DCAT-accessible structures |
| **Accessible** | Public CC-BY JSON, referenced in flood STAC Items |
| **Interoperable** | JSON-LD ready fields; CIDOC CRM-compatible attributes |
| **Reusable** | Full checksum + provenance ensures reproducibility |
| **CARE** | Ensures colorbars do not misrepresent culturally sensitive zones or site extents |

---

## 🧮 Validation Pipelines

All colorbar metadata files are validated under:

| Workflow | Validation Scope |
|----------|------------------|
| `visualization-validate.yml` | Structural schema + contrast tests |
| `faircare-validate.yml` | Ethical visualization checks |
| `stac-validate.yml` | Metadata–catalog linkage tests |
| `telemetry-export.yml` | Sustainability and governance metrics |

All reports stored under:
```
reports/self-validation/visualization/colorbars/
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|--------|--------|---------|
| v10.2.0 | 2025-11-12 | Hydrology Visualization Board | Established metadata index for flood colorbars; aligned with FAIR+CARE, WCAG AA, and STAC/DCAT. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Flood Legend Metadata](../README.md) · [Visualization Index](../../../../README.md)

</div>

