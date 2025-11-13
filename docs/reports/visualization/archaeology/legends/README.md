---
title: "🏺 Kansas Frontier Matrix — Archaeology Visualization Legends Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/archaeology/legends/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/reports-visualization-legends-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Archaeology Visualization Legends Index**  
`docs/reports/visualization/archaeology/legends/README.md`

**Purpose:**  
Provide a governed, FAIR+CARE-certified repository of **legend files, symbology keys, cultural sensitivity markers, and scale references** used in all archaeology visualizations across the Kansas Frontier Matrix (KFM).  
All legend assets are standardized for accessibility, reproducibility, and ethical representation of cultural and archaeological content.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../../../README.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-green)](../../../../../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Archaeology-orange)](../../../../../standards/faircare.md)  
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

</div>

---

## 📘 Overview

This directory houses **visual legends** required to interpret archaeological maps, hotspot models, paleoenvironment overlays, and multi-temporal density animations.  
Legends in this folder follow strict **FAIR+CARE design ethics**, **WCAG 2.1 AA accessibility**, and **visualization reproducibility rules** established by KFM v10.2.

All symbology:
- Avoids culturally inappropriate icons  
- Uses generalized markers for sensitive cultural/ceremonial sites  
- Includes accessible color palettes compatible with color-blindness standards  
- Links to STAC/DCAT provenance assets  
- Is validated in visualization CI workflows  

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/archaeology/legends/
├── README.md                    # This document
├── paleo_legend.svg             # Legend for paleoenvironment overlays
├── hotspot_legend.svg           # Legend for generalized hotspot models
└── symbols/
    ├── generic_pottery_marker.svg
    ├── settlement_grid_symbology.svg
    └── sensitive_site_mask.svg
```

---

## 🧩 Legend Standards (v10.2)

| Requirement | Description |
|-------------|-------------|
| **Accessible Colors** | Must meet WCAG contrast ≥ 4.5:1 |
| **Generalized Symbols** | No exact site markers for sensitive areas |
| **Consistent Scale Bars** | Standardized 5 km / 10 km bars |
| **Cultural Respect** | No imagery that implies sacred interpretation |
| **Metadata Binding** | Every legend references a `provenance.json` file |
| **Vector Format Preferred** | SVG recommended for clarity & scaling |

---

## 🧾 Example Legend Metadata

```json
{
  "legend_id": "kfm_archaeology_hotspot_legend_v10_2",
  "linked_visualization": "settlement_hotspots.geojson",
  "color_palette": "CBF-friendly sequential",
  "symbology": "grid_centroid_aggregation_5km",
  "sensitivity_class": "high",
  "faircare_review": "approved",
  "reviewers": [
    "FAIR+CARE Cultural Heritage Council",
    "Prairie Band Potawatomi Nation Heritage Office"
  ],
  "commit_sha": "<latest-commit-hash>",
  "telemetry_ref": "releases/v10.2.0/focus-telemetry.json",
  "license": "CC-BY 4.0"
}
```

---

## ⚙️ FAIR+CARE & Visualization Ethics Alignment

| Principle | Application in Legends |
|-----------|-------------------------|
| **Collective Benefit** | Symbology enhances public understanding without exposing sensitive data |
| **Authority to Control** | Tribal partners approve all culturally linked symbols |
| **Responsibility** | Legends must not depict precise ceremonial or burial symbols |
| **Ethics** | All Markers must remain generalized and non-identifying |

---

## 🧪 Validation Workflows

| Workflow | Purpose |
|----------|----------|
| `visualization-validate.yml` | Checks legend accessibility, symbology rules, metadata links |
| `faircare-validate.yml` | CARE ethics validation for symbols referencing Indigenous content |
| `telemetry-export.yml` | Logs sustainability and governance metrics |

---

## 🧭 Accessibility Requirements

- All text labels ≥ 12px  
- Minimum stroke width: 1.5px for clarity  
- No reliance on color alone — must pair color with pattern or label  
- Must pass color-blind palette validation (`cbf-validation.yml`)  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Cultural Heritage Council | Created legends index; added accessibility and FAIR+CARE governance rules. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Archaeology Visualizations](../README.md) · [Visualization Index](../../README.md)

</div>

