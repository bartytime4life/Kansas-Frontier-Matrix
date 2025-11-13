---
title: "🌦️ Kansas Frontier Matrix — Climate Symbol Legend Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/README.md"
version: "v10.2.2"
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
Define a consistent, accessible, and AI-aware **climate symbol set** for Focus Mode Story Nodes and map legends, aligned with STAC, Story Node schema, and FAIR+CARE governance.

<img alt="Docs · MCP" src="https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue" />
<img alt="Legend Type: Climate Symbols" src="https://img.shields.io/badge/Legend-Symbols%20·%20Climate-teal" />
<img alt="License: CC-BY 4.0" src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img alt="STAC Linked" src="https://img.shields.io/badge/Metadata-STAC%201.0%20aligned-purple" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Verified-gold" />

</div>

---

## 📚 Overview

This document specifies the **climate symbol legend** used by Kansas Frontier Matrix (KFM) in:

- Focus Mode climate overlays  
- Story Node cards and mini-maps  
- Report-ready map exports in `docs/reports/visualization/...`  

The symbols defined here provide a canonical library for representing **temperature, precipitation, drought, flood, wind, severe storms, and derived indices** across:

- Static maps (PDF / PNG exports)  
- Interactive MapLibre layers  
- Story Node narrative badges (for example, “Severe Drought · 1934 · 🟧”)  

All definitions are:

- 📐 Cartographically consistent (color, size, hierarchy)  
- ♿ Accessible (WCAG 2.1 AA contrast, shape redundancy)  
- 🛰 Machine-readable (JSON / YAML / STAC and Story Node schema references)  
- ⚖️ Governed by MCP + FAIR+CARE (no misleading or stigmatizing encodings)

> 💡 **Tip:** Treat this README as the **single source of truth** for climate symbols. All code, icons, and STAC items must match the rules defined here.

---

## 🎯 Objectives & Scope

This legend aims to:

- Provide a **standard climate symbol vocabulary** for:
  - Focus Mode climate layers (for example “Dust Bowl Drought, 1934”, “Great Flood, 1951”)  
  - Story Node visual summaries (icons on cards, timelines, mini-maps)  
  - Analytical maps for climate, hydrology, and hazard reports  

- Ensure symbols:
  - Are readable at multiple scales (desktop, tablet, projector)  
  - Encode severity in a predictable way (light → intense)  
  - Can be linked to data (STAC, Story Node `spacetime`, OWL-Time, GeoSPARQL)  

- Keep symbol metadata:
  - Versioned (semver)  
  - Validated via CI (schema + visual snapshot tests)  
  - Traceable back to inputs (NOAA, USGS, Mesonet, etc.)

Out of scope for this file:

- Detailed color ramp rules for continuous rasters (see colorbar legend docs)  
- Full STAC collection definitions (see `data/stac/*.json`)  
- Per-analysis styling overrides (handled in report-specific configs)

---

#### 📁 Directory Layout

climate/
|-- README.md                       # This document
|
|-- svg/                            # Source vector icons
|   |-- temp_anomaly_cool.svg
|   |-- temp_anomaly_warm.svg
|   |-- precip_heavy.svg
|   |-- drought_severe.svg
|   |-- flood_major.svg
|   |-- wind_high.svg
|   |-- storm_severe.svg
|   |-- index_pdsiextr.svg
|
|-- png/                            # Raster icons
|   |-- temp_anomaly_cool@2x.png
|   |-- ...
|
|-- metadata/                       # Machine-readable definitions
|   |-- climate-symbols.json
|   |-- climate-symbols.stac.json
|   |-- climate-symbols-story-nodes.json
|
|-- tests/                          # QA + visual validation
    |-- snapshots/
    |-- validate_metadata.py
    |-- generate_previews.py

> ⚙️ **Implementation note:** Do **not** add ad-hoc icons outside `svg/` or `png/`. All new symbols must be cataloged in `metadata/climate-symbols.json` and referenced in the Story Node + STAC metadata.

---

## 🌦 Symbol Categories & Semantics

Climate symbols are grouped into **thematic categories**.  
Each symbol has:

- A **semantic key** (stable ID used by code and metadata)  
- A **glyph** (SVG shape)  
- A **base color** (with severity variants)  
- Mappings to:
  - Data variables (for example `tas_anom`, `prcp`, `pdsiextr`)  
  - Units (for example °C, mm, index value)  
  - Severity bins (for example moderate, severe, extreme)

---

### 🌡 Temperature

Symbol keys (examples):

- `temp_anomaly_cool` — Cooler than baseline (for example `< -1 °C anomaly`)  
- `temp_anomaly_warm` — Warmer than baseline (for example `> +1 °C anomaly`)  
- `heat_extreme` — Extreme heat events (for example ≥ 100 °F days)

Visual guidance:

- Cool anomalies: blue diamonds (`#2b6cb0` → `#63b3ed`)  
- Warm anomalies: red / orange diamonds (`#c53030` → `#f6ad55`)  
- Extreme heat: deep red square with radiating tick marks  

Severity bins (example):

- `moderate`: absolute ΔT from 1–2 °C  
- `severe`:   absolute ΔT from 2–4 °C  
- `extreme`:  absolute ΔT greater than 4 °C  

The primary shape stays constant; **stroke width or inner marker** changes with severity.

---

### 💧 Precipitation & Moisture

Symbol keys:

- `precip_light` — Light precipitation anomaly (10–50% above baseline)  
- `precip_heavy` — Heavy precipitation anomaly (> 50% above baseline)  
- `snow_heavy` — Heavy snow events (region- and time-specific)  
- `soil_moisture_deficit` — Dry soils (for example Mesonet-based anomalies)

Visual guidance:

- Precipitation: inverted teardrop / raindrop glyph in blue-green  
- Snow: droplet with snowflake overlay (white marking)  
- Soil moisture deficit: droplet with dashed outline and brown infill

Severity mapping (intensity → stroke and size):

- Light → small glyph, thin stroke  
- Heavy → larger glyph, thicker outline, halo on interactive map

---

### 🌵 Drought & Aridity

Symbol keys:

- `drought_moderate` — e.g., USDM D1  
- `drought_severe` — D2–D3  
- `drought_extreme` — D4 (exceptional drought)

Visual guidance:

- Hexagon glyph with subtle cracked-earth texture in SVG  
- Color ramp: `#f6e05e` (moderate) → `#dd6b20` (severe) → `#9b2c2c` (extreme)  
- For Story Nodes, the emoji shorthand is standardized as:
  - `🟨` moderate, `🟧` severe, `🟥` extreme (always paired with text to avoid ambiguity)

---

### 🌊 Flood & Inundation

Symbol keys:

- `flood_minor` — Minor / recurring flood (for example bankfull level)  
- `flood_major` — Major flood (historical, for example 1903, 1951, 1993 events)  
- `flood_flash` — Flash flooding from convective storms

Visual guidance:

- Wave-shaped glyph (three arcs) in deep blue (`#2c5282`)  
- Major floods: thicker wave lines plus halo  
- Flash floods: wave glyph plus lightning bolt overlay  

Where possible, pair with **extent polygons** (flooded area) and use the glyph at a representative centroid.

---

### 🌬 Wind, Storms & Severe Weather

Symbol keys:

- `wind_high` — High wind (for example ≥ 40 mph sustained)  
- `storm_severe` — Severe storm cluster (hail, wind, tornado proxies)  
- `tornado_cluster` — Cluster representing tornado outbreak (not individual tracks)

Visual guidance:

- Wind: streamlined arrow glyph; orientation can encode prevailing direction  
- Severe storm: cloud plus lightning motif  
- Tornado cluster: stylized funnel icon (used sparingly; tracks and polygons are preferred for detail)

> ⚠️ **Ethical note:** Do **not** encode social vulnerability directly in symbols (no skull or “catastrophe” icons). Vulnerability and impacts must be communicated via contextual overlays and Story Node text, not stigmatizing glyphs.

---

### 📊 Climate Indices & Composites

Symbol keys:

- `index_pdsiextr` — Extreme Palmer Drought Severity Index values  
- `index_spi` — Standardized Precipitation Index anomalies  
- `index_heatwave` — Heatwave duration index (for example days above threshold)

Visual guidance:

- Rounded square glyph with internal bar or line indicating index magnitude  
- Neutral gray border, inner color mapped to sign (cool vs warm; wet vs dry)  
- These symbols often appear on **Story Node cards** as badges rather than main map icons.

---

## 🎨 Cartographic & Accessibility Rules

To comply with **accessibility** and **cartographic** standards:

- **Minimum map size**  
  - Interactive map: symbols must be legible at roughly 32 × 32 px at common zoom levels.  
  - Print exports: 16 pt minimum icon size on A4 or Letter at 300 dpi.

- **Redundancy**  
  - Use shape + color + label together. Do not rely on color alone to encode severity.

- **Contrast**  
  - All symbol strokes and fills must maintain WCAG 2.1 AA contrast against basemap tones.  
  - Prefer dark outlines around light fills and light outlines around dark fills.

- **Label rules**  
  - For dense maps, use aggregate symbols (for example `tornado_cluster`) with labels such as “15 events”.  
  - On hover or click, show detailed breakdown in a popup or Focus Mode side panel.

- **Cultural sensitivity**  
  - Avoid iconography that trivializes harm or disaster.  
  - Use neutral, informative metaphors (water, sun, clouds, etc.).

---

## 🧩 Integration with Story Nodes & Focus Mode

Climate symbols integrate tightly with:

- Story Node schema (`story-node.schema.json`)  
- Focus Mode v2 entity-centric views  
- STAC Items and Collections for climate layers  

### Story Node alignment

For each Story Node with climate context:

- `spacetime.geometry` and `spacetime.when` locate the climate event or condition.  
- `narrative.body` may reference a symbol key using a lightweight convention.  

Example snippet inside a narrative string:

- “Conditions were **{symbol:drought_extreme} extreme drought** across central Kansas in 1934.”

During rendering, `{symbol:drought_extreme}` is replaced by the appropriate SVG or emoji shorthand and the legend entry is activated.

### Focus Mode behavior

When a user focuses on:

- A **Place**  
  - Map and story panel show aggregate climate badges (for example “Top 3 drought years”, “Major floods”).  

- An **Event**  
  - Relevant climate symbols (for example flood glyphs along a river reach) are highlighted.  

- A **Story Node**  
  - Climate symbol badges appear in the header or summary if the node is climate-heavy.

These behaviors are configured via `metadata/climate-symbols-story-nodes.json`.

---

## ⚙️ Data & Metadata Requirements

All climate symbols must be defined in **machine-readable metadata**.

### Symbol catalog (conceptual)

`metadata/climate-symbols.json` follows a structure similar to:

    {
      "version": "1.0.0",
      "symbols": [
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
      ]
    }

Key fields:

- `id` — canonical symbol key (used by Story Nodes, Focus Mode, and UI code)  
- `category` — category name (temperature, precipitation, drought, etc.)  
- `svg` / `emoji` — reference to assets plus emoji shorthand  
- `data_mapping` — link back to underlying variables, units, thresholds  

### STAC alignment

`metadata/climate-symbols.stac.json` must register symbol assets as STAC `assets` with:

- `roles` set to `["legend", "symbol"]`  
- `type` set to `image/svg+xml` or `image/png`  
- Descriptive `title` and (optionally) `description`  

Example item (simplified):

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

### Story Node alignment

`metadata/climate-symbols-story-nodes.json` maps symbol IDs to Story Node usage patterns, including:

- Default badge placement (header, sidebar, timeline card)  
- Standard label strings  
- Recommended contexts or node types (for example hydrology, historical, hazards)

---

## 🧪 QA, Validation & CI Hooks

Legend consistency is enforced through:

- **Schema validation**  
  - `metadata/climate-symbols.json` is validated against `schemas/legends/climate-symbols.schema.json`.  

- **Link checks**  
  - All SVG and PNG paths referenced in metadata must exist.  

- **Visual regression tests**  
  - `tests/generate_previews.py` renders a test grid of symbols to `tests/snapshots/climate-symbols.png`.  
  - CI compares against the golden snapshot to catch breaking visual changes.

Recommended local command (exact target may be wired in `Makefile`):

    make test-legends-climate
    # Runs:
    #  python docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/tests/validate_metadata.py
    #  python docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/tests/generate_previews.py

Any failure in these tests should block merges until resolved.

---

## 📚 End-to-End Example (Symbol + STAC + Story Node)

This example ties a climate symbol into both STAC metadata and a Story Node.

1️⃣ **Symbol catalog entry (`metadata/climate-symbols.json`):**

    {
      "id": "flood_major",
      "category": "flood",
      "label": "Major Flood",
      "description": "Historical major flood with documented impacts.",
      "svg": "svg/flood_major.svg",
      "emoji": "🌊",
      "severity": "severe",
      "data_mapping": {
        "variable": "streamflow_anomaly",
        "threshold": "Q > Q100",
        "unit": "m³/s"
      }
    }

2️⃣ **STAC item asset (`metadata/climate-symbols.stac.json` snippet):**

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-climate-v1",
      "collection": "kfm-legends",
      "properties": {
        "datetime": "1951-07-10T00:00:00Z",
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

3️⃣ **Story Node snippet referencing the symbol:**

    {
      "id": "storynode-kansas-river-flood-1951",
      "type": "story-node",
      "title": "The Great 1951 Kansas River Flood",
      "summary": "A devastating flood that reshaped communities along the Kansas River.",
      "narrative": {
        "body": "In July 1951, a series of heavy rains led to a {symbol:flood_major} major flood along the Kansas River..."
      },
      "spacetime": {
        "geometry": { "type": "LineString", "coordinates": [/* simplified */] },
        "when": {
          "start": "1951-07-09T00:00:00Z",
          "end": "1951-07-31T00:00:00Z",
          "precision": "day"
        }
      }
    }

When rendered, `{symbol:flood_major}` is replaced with the climate icon and the legend entry is displayed on the map.

---

## 🕒 Version History

| Version | Date       | Author        | Notes                                                                 |
|--------|------------|---------------|-----------------------------------------------------------------------|
| v10.2.2 | 2025-11-13 | KFM Docs AI   | Initial climate symbol legend spec for Focus Mode Story Nodes & maps. |
| v10.2.3 | TBD        | TBD           | Planned: hail / ice, fire-weather, and uncertainty overlay symbols.   |