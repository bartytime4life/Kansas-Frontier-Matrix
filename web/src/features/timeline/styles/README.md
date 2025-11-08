---
title: "🎨 Timeline Style System — MapLibre Styles, Tokens & Legends (KFM-Ready)"
path: "web/src/features/timeline/styles/README.md"
version: "v9.9.0"
last_updated: "2025-11-08"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.9.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.9.0/manifest.zip"
telemetry_ref: "../../../../releases/v9.9.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-timeline-v1.json"
governance_ref: "../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "MIT"
---

<div align="center">

# 🎨 **Timeline Style System — MapLibre Styles, Tokens & Legends**  
`web/src/features/timeline/styles/README.md`

**Purpose:**  
Define **style conventions, variables, tokens, palettes, and legends** for the **Interactive Timeline**.  
Standardize **MapLibre style JSON**, **time expressions**, **era palettes**, **performance**, and **a11y** across KFM.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../../../../../docs/)
[![License](https://img.shields.io/badge/License-MIT-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Aligned-orange)](../../../../../docs/standards/)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)](#)

</div>

---

## 📘 Overview

This playbook specifies how **timeline styles** bind to a global **`currentYear`** and render **time-aware layers** (settlements, hydrology, landcover, ownership, species).  
It provides **reference snippets**, **naming rules**, **color/a11y tokens**, **legends**, and **CI validation hooks**.

**Goals**
- One **style variable** (`currentYear`) drives layer **filters/paints**.
- Era colors use **tokenized palettes** (color-blind safe).
- Layers follow **predictable IDs** and **z-order**.
- Styles are **validated** in CI and **telemetrized** for performance.

---

## 🗂️ Directory Layout

```plaintext
web/src/features/timeline/styles/
├─ README.md                 # This file
├─ timeline-style.json       # Main MapLibre style (variables, sources, layers)
├─ palette.json              # Era color tokens & ramps (WCAG-checked)
├─ tokens.json               # Size/opacity/outline tokens
├─ layers.json               # Layer registry (order, visibility, governance tags)
└─ legends.json              # Legend definitions and label ramps
```

---

## 🧩 Style Variables & Expressions

**Global variable** set by the Timeline feature:

```json
// timeline-style.json (top-level)
"metadata": { "vars": { "currentYear": 1900 } }
```

**Core expressions**

- **Visibility (active at Y):**
  ```json
  ["all",
    ["<=", ["get","year_start"], ["var","currentYear"]],
    [">=", ["coalesce", ["get","year_end"], 9999], ["var","currentYear"]]
  ]
  ```
- **Recency fade:**
  ```json
  ["interpolate", ["linear"],
    ["-", ["var","currentYear"], ["coalesce", ["get","year"], ["get","year_start"], 0]],
    0, 1.0, 50, 0.25
  ]
  ```
- **Era buckets (step colors):**
  ```json
  ["step", ["var","currentYear"],
    ["to-color", ["get","era.base"]],
    1850, ["to-color", ["get","era.1850"]],
    1900, ["to-color", ["get","era.1900"]],
    1950, ["to-color", ["get","era.1950"]],
    2000, ["to-color", ["get","era.2000"]]
  ]
  ```

> *Tip:* prefer `step`/`interpolate` over deep nested `case`s for performance.

---

## 🏷️ Layer Naming, Sources & Z-Order

**IDs**
- `timeline-[domain]-[geom]-[purpose]`  
  e.g. `timeline-settlements-point-main`, `timeline-hydrology-line-historic`

**Sources**
- PMTiles protocol URIs: `pmtiles://datasets/<name>.pmtiles`
- **source-layer** equals vector layer name in the tile (e.g., `settlements`).

**Z-order (bottom → top)**
1. basemap
2. `timeline-landcover-*`
3. `timeline-hydrology-*`
4. `timeline-ownership-*`
5. `timeline-settlements-*`
6. outlines/labels (`*-outline`, `*-label`)

**Filter contract**
- Every time-aware layer must implement the **active-at-Y** filter above.

---

## 🎨 Tokens & Palettes

### `palette.json` (example)

```json
{
  "era": {
    "base": "#C9C9C9",
    "pre1850": "#B3C7E6",
    "1850": "#8FD3A1",
    "1900": "#5BBF8F",
    "1950": "#2B9F7A",
    "2000": "#0F7A5D"
  },
  "a11y": {
    "outline": "#101010",
    "highlight": "#FF6F59",
    "focusRing": "#FFB703"
  }
}
```

### `tokens.json` (example)

```json
{
  "size": { "xs": 1.2, "sm": 2, "md": 3.5, "lg": 6 },
  "opacity": { "emphasis": 1.0, "muted": 0.4, "ghost": 0.15 },
  "stroke": { "thin": 0.5, "base": 1, "bold": 2 }
}
```

**Usage in style**
- Import tokens into layer paints with explicit values (MapLibre has no variable import for external JSON; a build step can inline tokens if desired).

---

## 🧾 Layer Registry & Legends

### `layers.json` (schema)

```json
{
  "layers": [
    {
      "id": "timeline-settlements-point-main",
      "domain": "settlements",
      "visible": true,
      "governance": { "care_tag": "public" },
      "legend": "settlements-era",
      "order": 50
    }
  ]
}
```

### `legends.json` (example)

```json
{
  "settlements-era": {
    "title": "Settlements (by era)",
    "type": "step",
    "stops": [
      { "label": "≤ 1850", "color": "{palette.era.pre1850}" },
      { "label": "≤ 1900", "color": "{palette.era.1850}" },
      { "label": "≤ 1950", "color": "{palette.era.1900}" },
      { "label": "≤ 2000", "color": "{palette.era.1950}" },
      { "label": "> 2000", "color": "{palette.era.2000}" }
    ]
  }
}
```

> *Note:* If your build system supports token interpolation, resolve `{palette.*}` at build time.

---

## 🧪 Reference Layer Snippet

```json
{
  "id": "timeline-settlements-point-main",
  "type": "circle",
  "source": "settlements",
  "source-layer": "settlements",
  "filter": ["all",
    ["<=", ["get","year_start"], ["var","currentYear"]],
    [">=", ["coalesce", ["get","year_end"], 9999], ["var","currentYear"]]
  ],
  "paint": {
    "circle-radius": ["interpolate", ["linear"], ["zoom"], 5, 1.2, 10, 3.5, 12, 6],
    "circle-stroke-color": "#101010",
    "circle-stroke-width": 0.5,
    "circle-color": ["step", ["var","currentYear"],
      "#C9C9C9", 1850, "#8FD3A1", 1900, "#5BBF8F", 1950, "#2B9F7A", 2000, "#0F7A5D"
    ],
    "circle-opacity": ["interpolate", ["linear"],
      ["-", ["var","currentYear"], ["coalesce", ["get","year"], ["get","year_start"], 0]],
      0, 1.0, 50, 0.25
    ]
  }
}
```

---

## ⚙️ Performance Guidelines

- **Single control variable**: update only `currentYear` (or a shared filter), not per-feature.
- Prefer **`step` / `interpolate`** expressions; avoid deep `case` nesting.
- Use **PMTiles/vector tiles**; pre-index by year to accelerate scrubs.
- **Debounce** slider updates (~16–33ms) to keep 60fps.
- Downsample at low zoom; reveal detail as users zoom in.
- Keep **label** layers light; consider runtime toggles for heavy outlines.

---

## ♿ Accessibility & Color

- Ensure **contrast ≥ 4.5:1** for symbols against basemap (outline tokens help).
- Provide **focus rings** for selected features (`palette.a11y.focusRing`).
- Use **color-blind safe** ramps; avoid hue-only differentiation—add size/opacity or pattern cues.
- Legends must include **text labels** (not just color swatches).

---

## 🔐 Governance & Visibility

- Each layer has a **`governance.care_tag`** (`public`, `restricted`, `sensitive`).  
- The web app enforces **role-based** visibility; styles should be **idempotent** if layers are hidden.  
- Sensitive sites (e.g., cultural heritage) **must not** be re-identifiable from symbology/opacity alone.

---

## 🧪 Validation & CI

- **Style lint:** validate `timeline-style.json` with MapLibre style-spec (JSON schema).  
- **Layer audit:** ensure all `timeline-*` layers implement the **active-at-Y** filter contract.  
- **A11y audit:** minimum contrast checks per symbol color vs. background.  
- **Telemetry:** record frame time, layer count, and interaction latency into `focus-telemetry.json`.

> CI workflows: `docs-lint.yml`, `faircare-validate.yml`, and `stac-validate.yml` (if style references STAC-derived assets).

---

## 🔧 PMTiles Protocol Setup (reference)

```ts
import { Protocol } from 'pmtiles';
import maplibregl from 'maplibre-gl';

const protocol = new Protocol();
maplibregl.addProtocol('pmtiles', protocol.tile);
// on teardown: maplibregl.removeProtocol('pmtiles', protocol.tile);
```

---

## 🧱 Data Contract (timeline-ready features)

| Field          | Req | Type     | Description                                  |
|----------------|-----|----------|----------------------------------------------|
| `year_start`   | ✅  | number   | First active year (inclusive).                |
| `year_end`     | —   | number   | Last active year (inclusive, default `9999`). |
| `year`         | —   | number   | Single-year features (optional).             |
| `epoch`        | —   | string   | Era label for legend bucketing.              |
| `class`        | —   | string   | Domain category (e.g., landcover class).     |

Reject features without `year_start` in ETL; fill `year_end` with `9999` where open-ended.

---

## 🧭 Known Good Defaults

- Bounds: `min=1700`, `max=2025`, `step=1` (adjust per dataset range).  
- Initial: median of active `year_start` for higher feature density.  
- Outline: `#101010` @ `0.5–1` px to preserve contrast on all basemaps.

---

## 🕰️ Version History

| Version | Date       | Author | Summary                                              |
|--------:|------------|--------|------------------------------------------------------|
| v9.9.0  | 2025-11-08 | KFM    | Initial styles/tokens/legends spec for timeline UI.  |

---

<div align="center">

© 2025 Kansas Frontier Matrix — Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Timeline Docs](../README.md) · [Web Docs](../../../README.md) · [Governance Charter](../../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>

