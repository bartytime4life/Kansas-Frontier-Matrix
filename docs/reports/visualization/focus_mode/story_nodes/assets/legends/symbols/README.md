---
title: "🔖 Kansas Frontier Matrix — Legend Symbol Assets Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Visualization Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reports-visualization-focusmode-symbols-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🔖 **Legend Symbols — Focus Mode Story Node Visualization System**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/README.md`

**Purpose:**  
Provide the authoritative index for **legend symbol assets** used in **Focus Mode story nodes**, including archaeological icons, hydrology markers, climate indicators, event symbols, and contextual narrative elements.  
All assets must adhere to **FAIR+CARE visualization ethics**, **WCAG accessibility standards**, and **KFM v10 metadata schema**.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Legend symbols provide standardized, accessible visual encodings for maps and timelines within **Focus Mode**.  
This directory documents:

- Approved symbol categories  
- FAIR+CARE-compliant usage rules  
- Required metadata fields (linked to `metadata/` directory)  
- Icon formatting, color, and accessibility requirements  
- Reproducibility & provenance linkages  

Symbols support **2D maps**, **3D story scenes**, **temporal dashboards**, and **AI-driven narrative summaries**.

---

## 🗂️ Directory Layout

```plaintext
symbols/
├── README.md                        # This file
├── archaeological/                  # Icons for archaeological sites, features, cultural zones
│   ├── pottery_marker.svg
│   ├── burial_protected.svg
│   └── village_generalized.svg
│
├── hydrology/                       # Water resource + flood/drought indicators
│   ├── well_marker.svg
│   ├── flood_highwater.svg
│   └── drought_intensity.svg
│
├── climate/                         # Temperature / precipitation / anomaly indicators
│   ├── temp_anomaly_up.svg
│   └── precip_marker.svg
│
├── landcover/                       # Vegetation & landclass indicators
│   ├── grassland_icon.svg
│   └── woodland_icon.svg
│
├── events/                          # Historical events, treaties, migrations, conflicts
│   ├── treaty_marker.svg
│   └── migration_path_marker.svg
│
└── metadata/                        # Metadata & definitions
    ├── README.md
    ├── field_definitions.md
    └── examples/
```

---

## 🧩 Symbol Categories

| Category | Description | CARE Governance Notes |
|---------|-------------|------------------------|
| **Archaeological** | Icons marking heritage sites, excavation units, habitation clusters | Must be generalized; sensitive sites require CARE approval |
| **Hydrology** | Wells, aquifers, watersheds, flood extent markers | Mask well locations; ethics review for groundwater layers |
| **Climate** | Temperature, anomaly, drought/precip symbols | No restrictions unless culturally sensitive overlays |
| **Landcover** | Vegetation, biome, and ecological zone icons | Standard FAIR usage |
| **Events** | Indigenous routes, treaties, conflict sites | CARE review required for culturally sensitive event types |

---

## 🧠 Symbol Design Requirements

### Accessibility (WCAG 2.1 AA)
- Minimum **3:1 contrast ratio** for icons on standard basemaps  
- Scalable vector format (SVG mandatory)  
- Support for **dark/light mode** and high-contrast modes  
- Proper `role="img"` + accessible title/desc metadata for UI use  

### Icon Formatting
- Use **2px stroke** equivalent at 24px base scale  
- Prefer **round line caps**  
- SVG viewBox: `0 0 24 24`  
- No embedded raster images  

---

## 🔐 CARE Safeguards for Sensitive Symbols

Symbols referencing:
- **Burial sites**  
- **Sacred areas**  
- **Tribal restricted zones**  
- **Sensitive archaeological sites**

…must include:

- CARE metadata block (status: `"restricted"` or `"approved"` after review)  
- Upstream generalization (≥5–10 km spatial uncertainty)  
- Governance ledger entry sign-off prior to publication  

---

## 🧾 Example Symbol Metadata Entry

```json
{
  "id": "symbol_archaeology_burial_protected_v10",
  "title": "Generalized Burial Site (Protected)",
  "domain": "archaeology",
  "format": "SVG",
  "checksum_sha256": "sha256-29ffbb12a4c...",
  "care": {
    "status": "restricted",
    "reviewer": "FAIR+CARE Heritage Council",
    "statement": "Symbol allowed only for 20km generalized regions.",
    "date_reviewed": "2025-11-12"
  },
  "updated": "2025-11-12T20:50:00Z"
}
```

---

## 🔍 Metadata Requirements

Symbol metadata must conform to the schema in:

```
docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/field_definitions.md
```

Validation workflows:
- `faircare-validate.yml`  
- `stac-validate.yml`  
- `docs-lint.yml`  
- `telemetry-export.yml`  

---

## 🛠️ Reproducibility & Provenance

All symbol assets must:
- Be version-tracked  
- Include SHA-256 checksum in metadata  
- Link to the processing workflow or design source  
- Be referenced by Story Node metadata and Focus Mode pipelines  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Visualization Board | Created symbol asset index with FAIR+CARE safeguards and v10 metadata integration. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · Master Coder Protocol v6.3  
**Diamond⁹ Ω / Crown∞Ω Ultimate Certified**

[⬅ Back to Legend Assets](../README.md)

</div>

