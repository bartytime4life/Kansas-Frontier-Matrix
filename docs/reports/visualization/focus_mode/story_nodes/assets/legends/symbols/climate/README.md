---
title: "🌦️ Kansas Frontier Matrix — Climate Symbol Legend Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/reports-visualization-focus-climate-symbols-v1.json"
governance_ref: "../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌦️ **Kansas Frontier Matrix — Climate Symbol Legend Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/README.md`

**Purpose:**  
Define a FAIR+CARE-governed climate symbol system for Focus Mode Story Nodes, analytical maps, and STAC metadata, with consistent semantics across the Kansas Frontier Matrix (KFM).

<img alt="Docs · MCP" src="https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue" />
<img alt="Legend Type: Climate Symbols" src="https://img.shields.io/badge/Legend-Symbols%20·%20Climate-teal" />
<img alt="License: CC-BY 4.0" src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img alt="STAC Linked" src="https://img.shields.io/badge/Metadata-STAC%201.0%20aligned-purple" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Verified-gold" />

</div>

---

## 📚 Overview

This document standardizes the **climate symbol legend** used by:

- Focus Mode v2 climate overlays  
- Story Nodes (badges, timelines, narrative glyphs)  
- Climatology and hydrology reports under `docs/reports/visualization/...`  
- STAC Items & Collections (via `legend` / `symbol` assets)  
- MapLibre-based interactive maps in the KFM front-end  

The legend encodes:

- Temperature anomalies  
- Precipitation anomalies  
- Drought severity  
- Flood extent / type  
- Wind and severe storms  
- Composite climate indices (SPI, PDSI, heatwave indices)  

All symbols are:

- 📐 Cartographically consistent  
- ♿ WCAG 2.1 AA accessible (shape + color + label)  
- 🛰 Linked to variables, units, and thresholds  
- ⚖️ FAIR+CARE compliant, with explicit governance and provenance  

---

### 🗂️ Directory Layout

    climate/
    ├── README.md                        # This document (spec + usage)
    ├── svg/                             # Source vector icons (preferred assets)
    │   ├── temp_anomaly_cool.svg
    │   ├── temp_anomaly_warm.svg
    │   ├── precip_heavy.svg
    │   ├── drought_severe.svg
    │   ├── flood_major.svg
    │   ├── wind_high.svg
    │   ├── storm_severe.svg
    │   └── index_pdsiextr.svg
    ├── png/                             # Raster icons for non-SVG contexts
    │   ├── temp_anomaly_cool@2x.png
    │   └── ...
    ├── metadata/                        # Machine-readable symbol definitions
    │   ├── climate-symbols.json
    │   ├── climate-symbols.stac.json
    │   └── climate-symbols-story-nodes.json
    └── tests/                           # QA + visual regression
        ├── snapshots/
        ├── validate_metadata.py
        └── generate_previews.py

> ⚙️ **Implementation rule:**  
> All climate symbols **must** be defined in `metadata/climate-symbols.json` and wired into STAC + Story Node metadata.  
> No icons may exist outside `svg/` or `png/`.

---

## 🌦 Symbol Categories & Semantics

Climate symbols are organized into **thematic categories**, each with:

- A **semantic ID** (canonical key used in code and metadata)  
- An **SVG glyph** (primary visual)  
- A **base color** with severity variants  
- **Data variable mappings** (for example `tas_anom`, `prcp`, `spi`, `pdsiextr`)  
- **Units and thresholds** (for example °C anomaly, mm anomaly, index values)  
- Standard **Story Node replacement rules** (for example `{symbol:drought_extreme}`)  

---

### 🌡 Temperature

**Keys**

- `temp_anomaly_cool` — below-baseline temperature anomaly  
- `temp_anomaly_warm` — above-baseline temperature anomaly  
- `heat_extreme` — extreme heat episode  

**Visual guidance**

- Cool anomalies: blue diamonds  
- Warm anomalies: orange/red diamonds  
- Extreme heat: radiant red square  

**Severity bands (example)**

- `moderate`: |ΔT| 1–2 °C  
- `severe`:   |ΔT| 2–4 °C  
- `extreme`:  |ΔT| > 4 °C  

---

### 💧 Precipitation & Moisture

**Keys**

- `precip_light` — light positive anomaly  
- `precip_heavy` — heavy anomaly / extreme rainfall  
- `snow_heavy` — heavy snowfall events  
- `soil_moisture_deficit` — anomalously dry soils  

**Visual guidance**

- Droplet glyphs with overlays (snowflake, dashed outline)  
- Size and stroke indicate intensity; halo used for extremes on interactive maps  

---

### 🌵 Drought & Aridity

**Keys**

- `drought_moderate`  
- `drought_severe`  
- `drought_extreme`  

**Visual guidance**

- Hexagon glyph with cracked-earth texture (subtle)  
- Color ramp: yellow → orange → red  
- Emoji shorthand for Story Nodes:
  - 🟨 `drought_moderate`  
  - 🟧 `drought_severe`  
  - 🟥 `drought_extreme`  

---

### 🌊 Flood & Inundation

**Keys**

- `flood_minor` — bankfull / nuisance flooding  
- `flood_major` — historical major floods (for example 1903, 1951, 1993)  
- `flood_flash` — flash flooding from convective storms  

**Visual guidance**

- Wave glyph (three arcs) in deep blue  
- Major floods: thicker wave lines + halo  
- Flash floods: wave glyph plus lightning bolt overlay  

Where possible, major floods should be paired with **extent polygons**; the glyph marks a representative reach or centroid.

---

### 🌬 Wind, Storms & Severe Weather

**Keys**

- `wind_high` — sustained high winds  
- `storm_severe` — severe storm cluster (hail, wind, tornado proxies)  
- `tornado_cluster` — tornado outbreak cluster (not individual tracks)  

**Visual guidance**

- Wind: streamlined arrow; orientation encodes prevailing direction  
- Severe storm: cloud + lightning motif  
- Tornado cluster: stylized funnel glyph, used sparingly (paths/polygons preferred for detail)

> ⚠️ **Ethical rule:**  
> Do **not** encode social vulnerability or impact with fear-based symbols (skulls, disaster icons).  
> Represent risk through context, overlays, and narrative text rather than stigmatizing glyphs.

---

### 📊 Climate Indices & Composites

**Keys**

- `index_pdsiextr` — extreme Palmer Drought Severity Index  
- `index_spi` — Standardized Precipitation Index  
- `index_heatwave` — heatwave duration index  

**Visual guidance**

- Rounded square glyph containing a bar/line representing index magnitude  
- Neutral frame; inner color indicates sign (wet/dry, cool/warm)  

---

## 🎨 Cartographic & Accessibility Rules

- **Size**
  - ≥ 32×32 px on interactive maps  
  - ≥ 16 pt on A4/Letter 300 dpi exports  

- **Redundancy**
  - Use **shape + color + text label** together for severity.  
  - Never rely on color alone.

- **Contrast**
  - All glyphs must maintain **WCAG 2.1 AA** contrast against the basemap.  
  - Prefer dark outlines around light fills and vice versa.

- **Labeling**
  - In dense areas, use aggregated symbols with counts (“15 tornadoes”) and show detail in Focus Mode panels.

- **Cultural sensitivity**
  - Use neutral meteorological metaphors (water, wind, sun, clouds).  
  - Avoid imagery that trivializes harm or disaster.

---

## 🧩 Story Node & Focus Mode Integration

### Story Node Usage

Story Nodes may embed climate symbols using a lightweight placeholder syntax:

    "Conditions were {symbol:drought_extreme} extreme drought across central Kansas in 1934."

Renderer responsibilities:

- Replace `{symbol:drought_extreme}` with the correct SVG/emoji  
- Add the referenced symbol to the map legend  
- Log symbol usage in telemetry for explainability traces  

### Focus Mode Behavior

When Focus Mode is centered on:

- **Place** — show aggregated climate badges (e.g., “Top 3 drought years”, “Major floods”).  
- **Event** — highlight relevant symbols along the event geometry (river reach, storm track).  
- **Story Node** — show climate badges in the Story Node header if climate is a primary dimension.

These bindings are configured in `metadata/climate-symbols-story-nodes.json`.

---

## ⚙️ Metadata & STAC Requirements

### Symbol catalog (`metadata/climate-symbols.json`)

Example entry:

    {
      "id": "drought_extreme",
      "category": "drought",
      "label": "Extreme Drought",
      "description": "USDM D4 or equivalent PDSI threshold.",
      "svg": "svg/drought_extreme.svg",
      "emoji": "🟥",
      "severity": "extreme",
      "data_mapping": {
        "variable": "pdsiextr",
        "min": -6,
        "unit": "index"
      }
    }

Key fields:

- `id` — canonical symbol key  
- `category` — temperature, precipitation, drought, flood, etc.  
- `svg` / `emoji` — primary glyphs  
- `data_mapping` — link to variables, thresholds, and units  

### STAC alignment (`metadata/climate-symbols.stac.json`)

Example asset snippet:

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-climate-v1",
      "collection": "kfm-legends",
      "properties": {
        "datetime": "2025-01-01T00:00:00Z",
        "kfm:legend_type": "symbols-climate"
      },
      "assets": {
        "flood_major_svg": {
          "href": "svg/flood_major.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Major Flood Icon"
        }
      }
    }

### Story Node bindings (`metadata/climate-symbols-story-nodes.json`)

This file defines:

- Default badge placement (header, sidebar, timeline card)  
- Standard label strings  
- Recommended usage contexts (disciplines, layer types)  

---

## 🧪 QA, Validation & CI

Tests under `climate/tests/` enforce:

- JSON schema validity for `climate-symbols.json`  
- File path integrity (all referenced SVG/PNG exist)  
- Visual regression via golden snapshot images  

Local helper target:

    make test-legends-climate
    # Runs:
    #  python docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/tests/validate_metadata.py
    #  python docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/tests/generate_previews.py

CI MUST block merges on any legend-related test failure.

---

## 🕒 Version History

| Version  | Date       | Author        | Notes                                                                     |
|----------|------------|---------------|---------------------------------------------------------------------------|
| v10.2.2  | 2025-11-13 | KFM Docs AI   | Initial climate symbol legend specification for Focus Mode Story Nodes.   |
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Heading hierarchy + directory layout aligned with KFM markdown standards. |