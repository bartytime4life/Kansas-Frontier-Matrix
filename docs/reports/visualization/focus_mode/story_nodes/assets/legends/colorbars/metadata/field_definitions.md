---
title: "📘 Kansas Frontier Matrix — Colorbar Metadata Field Definitions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/colorbars/metadata/field_definitions.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Visualization Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/reports-visualization-focusmode-colorbars-metadata-v1.json"
governance_ref: "../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📘 **Colorbar Metadata Field Definitions — Focus Mode Visualization System**
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/colorbars/metadata/field_definitions.md`

**Purpose:**  
Define all **required and optional metadata fields** for colorbars used in **Focus Mode Story Node visualizations**, ensuring FAIR+CARE governance, reproducibility, accessibility, and schema integrity.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Colorbars are a foundational component for **map layers, hydrology analytics, climate overlays, archaeological reconstructions, and Focus Mode story node visual cues**.  
This document defines:

- Standard fields across all colorbar metadata  
- Domain-specific optional fields  
- CARE governance mappings for sensitive domains  
- Required schema conformance for STAC/DCAT interoperability  
- Validation expectations for CI workflows  

All metadata files must conform to this specification and be validated under:

- `docs-lint.yml`  
- `faircare-validate.yml`  
- `stac-validate.yml`  
- `telemetry-export.yml`

---

## 🗂️ Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `id` | string | Unique colorbar identifier | `"kfm_colorbar_precip_v10"` |
| `title` | string | Human-readable title | `"Daily Precipitation Gradient"` |
| `domain` | string | Visualization domain (`climate`, `hydrology`, `terrain`, `archaeology`, etc.) | `"hydrology"` |
| `format` | string | Output format for colorbar asset | `"PNG"` |
| `units` | string | Units associated with represented values | `"mm/day"` |
| `min_value` | number | Minimum represented value | `0` |
| `max_value` | number | Maximum represented value | `300` |
| `checksum_sha256` | string | SHA-256 integrity hash | `"sha256-a13be9..."` |
| `updated` | string (ISO datetime) | Last modification timestamp | `"2025-11-12T17:40:00Z"` |
| `provenance` | object | Metadata about source data + processing pipeline | See provenance block |
| `care` | object | CARE ethical metadata | See CARE block |

---

## 🧩 Optional Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `color_ramp` | array<string> | HEX colors in sequence | `["#08306b","#4292c6","#deebf7"]` |
| `discrete_steps` | boolean | TRUE if discrete classed ramp | `true` |
| `step_labels` | array<string> | Labels for discrete ranges | `["D0","D1","D2","D3","D4"]` |
| `stac_item` | string | STAC Item ID if colorbar tied to dataset | `"kfm_hydro_drought_2025"` |
| `dcat_theme` | string | DCAT thematic category | `"Hydrology"` |
| `gradient_orientation` | string | `"horizontal"` or `"vertical"` | `"horizontal"` |
| `legend_title` | string | Override legend title | `"Drought Severity"` |
| `legend_subtitle` | string | Optional description | `"USDM-scale aggregated index"` |

---

## 📦 Provenance Metadata Block

All colorbars must include a `provenance` object:

```json
{
  "provenance": {
    "source": "Daymet v4 Daily Precipitation",
    "pipeline": "colorbar_render_v3",
    "commit_sha": "<latest-commit-hash>",
    "processor": "kfm-visualization-lab"
  }
}
```

### Required fields:
- `source` (string)  
- `pipeline` (string)  
- `commit_sha` (string)  
- `processor` (string)  

---

## 🧭 CARE Metadata Block

CARE metadata is required for **archaeology**, **hydrology (wells)**, **tribal lands**, and **any potentially sensitive datasets**.

```json
{
  "care": {
    "status": "approved",
    "reviewer": "FAIR+CARE Visualization Board",
    "date_reviewed": "2025-11-12",
    "statement": "Representation does not reveal sensitive geographic detail.",
    "notes": "Generalization applied upstream."
  }
}
```

### Allowed `status` values:
- `"approved"`
- `"revision"`
- `"restricted"`

---

## 🧠 Domain-Specific Guidance

### 🌧️ Climate Colorbars
- Use WCAG-compliant contrast ratios  
- Required units: `"mm/day"`, `"°C"`, `"K"`, `"index"`  

### 💧 Hydrology Colorbars
- Must include masking of sensitive well data  
- Optional `step_labels` for flood stage categories  

### 🏺 Archaeology Colorbars
- Mandatory CARE block  
- Must avoid excessive detail that suggests precise site position  

### 🏞️ Terrain / Elevation Colorbars
- Must include `units: "meters"`  
- Compatible with USGS/3DEP metadata  

---

## 🔍 Full Example (Compliant Metadata)

```json
{
  "id": "kfm_colorbar_groundwater_change_v10",
  "title": "Groundwater Δ (m)",
  "domain": "hydrology",
  "format": "PNG",
  "units": "meters",
  "min_value": -12,
  "max_value": 8,
  "color_ramp": ["#54278f", "#756bb1", "#bcbddc", "#edf8fb"],
  "checksum_sha256": "sha256-9f2a1e9c0ad4f21a33...",
  "provenance": {
    "source": "KDHE / USGS Groundwater Monitoring Program",
    "pipeline": "hydro_colorbar_gen_v4",
    "commit_sha": "<latest-commit-hash>",
    "processor": "kfm-visualization-lab"
  },
  "care": {
    "status": "approved",
    "reviewer": "FAIR+CARE Hydrology Ethics Board",
    "date_reviewed": "2025-11-12",
    "statement": "Sensitive well coordinates generalized; only aggregated change values shown."
  },
  "updated": "2025-11-12T20:12:00Z"
}
```

---

## 🧪 Validation Requirements

| Validation Type | Workflow | Output |
|------------------|----------|---------|
| Schema Validation | `stac-validate.yml` | STAC/DCAT cross-check |
| FAIR+CARE Ethics | `faircare-validate.yml` | CARE block verification |
| Markdown + Metadata | `docs-lint.yml` | Structural compliance |
| Telemetry | `telemetry-export.yml` | Sustainability metrics & lineage |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Visualization Board | Established definitive field definitions for Focus Mode colorbar metadata. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · Master Coder Protocol v6.3  
**Diamond⁹ Ω / Crown∞Ω Ultimate Certified**

[⬅ Back to Metadata Index](README.md)

</div>

