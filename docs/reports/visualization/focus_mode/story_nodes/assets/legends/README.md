---
title: "🎨 Kansas Frontier Matrix — Story Node Legend Assets Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Visualization Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reports-visualization-focusmode-legends-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Story Node Legend Assets Index**
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/README.md`

**Purpose:**  
Serve as the authoritative index and metadata hub for **legend assets** used by **Focus Mode Story Nodes**, including colorbars, symbology sets, classification scales, confidence indicators, CARE-modified masking tiles, and domain-specific legend families.

![Docs MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License CC-BY](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status Active](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Legend assets provide **visual semantic context** for:
- Hydrology layers (drought, flood, groundwater, watersheds)
- Archaeology overlays (generalized site density, cultural boundaries)
- Climate and landcover systems
- 3D Focus Mode scenes (elevation, terrain materials)
- Story Node timelines, uncertainty visualization, and CARE-governed data generalization

All legend assets must:
- Include **STAC/DCAT-aligned metadata**
- Contain **checksum + provenance** references
- Include **FAIR+CARE visibility notes** for culturally sensitive symbology
- Be linkable from **Story Node asset bundles**

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/story_nodes/assets/legends/
├── README.md                       # This file
│
├── colorbars/                      # Raster and vector continuous scales
│   ├── precipitation.png
│   ├── drought_index.svg
│   └── README.md
│
├── symbols/                        # Point/line/polygon symbols
│   ├── archaeological_sites.svg
│   ├── watershed_boundaries.svg
│   └── README.md
│
└── metadata/                       # CARE-aware legend metadata definitions
    ├── field_definitions.md
    └── README.md
```

---

## 🧩 Legend Asset Types

| Legend Type | Description | Formats | Use Cases |
|-------------|-------------|---------|-----------|
| **Colorbars** | Continuous scales: elevation, precipitation, moisture index, soil depth | PNG, SVG | Hydrology, climate, landcover |
| **Symbols** | Point/line/polygon style dictionaries | SVG, JSON | Archaeology, treaties, hazard markers |
| **CARE Masks** | Ethically generalized masks for sensitive overlays | PNG (alpha), GeoJSON | Indigenous/cultural data restrictions |
| **Classification Keys** | Thematic groupings of values → labels | JSON, CSV | Story Node classification logic |
| **3D Material Keys** | Legend for terrain textures / PBR materials | JSON | Focus Mode 3D |

---

## 🧾 Metadata Requirements (All Legend Assets)

Every legend asset must include metadata with:

| Field | Required | Description |
|-------|----------|-------------|
| `id` | ✅ | Unique identifier for the legend asset |
| `title` | ✅ | Human-readable title |
| `domain` | ✅ | E.g., hydrology, archaeology, climate, landcover |
| `format` | ✅ | PNG, SVG, JSON, etc. |
| `checksum_sha256` | ✅ | Artifact integrity verification |
| `provenance` | ✅ | Source data + processing description |
| `care` | ⚙️ | Whether sensitive sites influence legend masking |
| `workflow` | ⚙️ | ETL or rendering pipeline ID |
| `updated` | ✅ | ISO 8601 timestamp |
| `stac_extensions` | ⚙️ | `["checksum", "version", "kfm:legend"]` recommended |

---

## 🧩 Example Metadata Block — Archaeology Symbols

```json
{
  "id": "kfm_legend_archaeology_sites_v10",
  "title": "Archaeological Site Symbol Set (Generalized)",
  "domain": "archaeology",
  "format": "SVG",
  "checksum_sha256": "sha256-83aa122ef9e4a1bb9e...",
  "provenance": {
    "source": "KFM Archaeology Council",
    "method": "Generalized icons aligned to CIDOC CRM",
    "workflow": "legend_generation_pipeline_v3",
    "commit_sha": "<commit-hash>"
  },
  "care": {
    "status": "generalized",
    "statement": "Symbols designed to avoid exposure of precise site categories.",
    "reviewer": "Prairie Band Potawatomi Nation",
    "date_reviewed": "2025-11-12"
  },
  "updated": "2025-11-12T18:00:00Z"
}
```

---

## 🎨 Example Metadata Block — Drought Colorbar

```json
{
  "id": "kfm_colorbar_drought_index_v10",
  "title": "Drought Severity Index Colorbar",
  "domain": "hydrology",
  "format": "PNG",
  "checksum_sha256": "sha256-19feab33490ce1df87b...",
  "provenance": {
    "source": "NOAA NIDIS",
    "method": "Linear gradient from -4 (extreme drought) to +4 (extreme wet)",
    "workflow": "colorbar_render_v2",
    "commit_sha": "<commit-hash>"
  },
  "care": {
    "status": "public",
    "statement": "No cultural sensitivity implications.",
    "reviewer": "FAIR+CARE Hydrology Committee",
    "date_reviewed": "2025-11-12"
  },
  "updated": "2025-11-12T18:00:00Z"
}
```

---

## 🧠 Usage in Focus Mode

Legend assets are consumed by:
- **Focus Mode UI (React + Cesium)**  
- **Story Node AI narrative panels**  
- **3D scene contextual overlay frameworks**  
- **Animated hydrology & climate timelines**  
- **Archaeological density & cultural significance maps**

They are validated by:
- `stac-validate.yml` (metadata)  
- `docs-lint.yml` (Markdown integrity)  
- `faircare-validate.yml` (CARE compliance)  
- `telemetry-export.yml` (energy/carbon/ethical logs)

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Visualization Board | Created index for legend assets with STAC/DCAT/CARE examples and directory structure. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Story Node Map Assets](../maps/README.md)

</div>

