# 🗺️ Layer Manifests (Web Map) — `web/assets/maps/manifests/layers/`

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Manifest%20Type](https://img.shields.io/badge/manifest-layer-blue)
![Provenance](https://img.shields.io/badge/provenance-required-purple)
![UI%20First](https://img.shields.io/badge/web-UI%20first-informational)

> [!NOTE]
> This folder contains **declarative “Layer Manifests”** that power the Web Map layer registry/panel.  
> A layer manifest answers: **what to draw**, **how to style it**, **how to explain it** (legend + provenance), and **how it behaves** (click/hover/time).

> [!IMPORTANT]
> A layer manifest is **not** the canonical dataset contract. Canonical dataset metadata lives in the governed catalog + provenance system (see: `data/catalog/`, `data/sources/`, `data/provenance/`).  
> A layer manifest should **reference** those records — not duplicate them.

---

## 🧾 Policy metadata

| Field | Value |
|---|---|
| File | `web/assets/maps/manifests/layers/README.md` |
| Status | ✅ Active |
| Last updated | `2026-01-17` |
| Scope | Web UI layer registry + map viewer |
| Primary consumers | Map layer panel, Story Nodes / Focus Mode, timeline UI |
| Guarantees | Stable IDs, provenance linkbacks, accessible legends, safe defaults |

---

## 🧭 Quick links

- 🏠 Project overview: `../../../../../README.md`
- 🧬 Data manifests (external sources): `../../../../../data/sources/`
- 🗂️ Data catalog metadata (STAC/DCAT): `../../../../../data/catalog/`
- 🧾 Provenance lineage records: `../../../../../data/provenance/`
- 📚 Docs: `../../../../../docs/`

---

## 📦 What lives here?

Think of this directory as a **UI registry** for map layers — each file is one layer (or one “layer package” that expands into multiple render layers).

```text
📁 web/
  📁 assets/
    📁 maps/
      📁 manifests/
        📁 layers/
          📄 README.md         👈 you are here
          📄 <layer>.json      ✅ recommended (portable, build-friendly)
          📄 <layer>.yml       🟡 optional (only if the loader supports YAML)
```

### ✅ What’s okay to include
- Render config (MapLibre/Cesium) → sources, style layers, ordering hints
- UI metadata → name, group, tags, default visibility, default opacity
- Legend spec → categorical / ramp / gradient + units
- Interaction spec → click popup template, hover, feature-id strategy
- Temporal spec → how the layer participates in the timeline/time filter
- Provenance pointers → `catalogId`, `sourceManifestRef`, license, attribution

### 🚫 What’s *not* okay to include
- Huge raw datasets embedded directly into the web bundle (large GeoJSON, rasters, etc.)
- Private/sensitive coordinates without redaction rules
- “Mystery meat” layers without provenance / licensing / attribution

---

## 🎯 Design goals

### 1) **Provenance-first UI**
Every layer should be explainable: **where it came from**, **what it represents**, **what’s uncertain**, and **how to cite it**.

### 2) **Stable identifiers**
Layer IDs must be stable so Story Nodes, bookmarks, and saved views can reliably reference them.

### 3) **Accessible cartography**
Legends, color ramps, and labels must support readability + high-contrast needs.  
Prefer meaningful color semantics (water ≈ blue, vegetation ≈ green, etc.) and avoid “pretty but misleading” symbology.

### 4) **Composable render blocks**
A single manifest can define one conceptual layer even if it expands into multiple style layers (e.g., fill + outline + labels).

---

## 🏷️ Naming conventions

### File naming
Use **lowercase**, **kebab-case**, and **namespacing**:

- `boundaries__counties.json`
- `history__railroads_1880s.json`
- `environment__ndvi_latest.json`

### `id` naming
Use a stable slug matching the file stem:

- `boundaries__counties`
- `history__railroads_1880s`

> [!TIP]
> If your render config defines multiple MapLibre style layer IDs, prefix them with the manifest `id` to avoid collisions:
> - `history__railroads_1880s::lines`
> - `history__railroads_1880s::labels`

---

## 🧩 Layer Manifest contract (v1)

A manifest is **one JSON object** with predictable top-level sections:

### Required (minimum viable layer)
| Key | Type | Why it exists |
|---|---|---|
| `id` | string | Stable reference across UI + Story Nodes |
| `title` | string | Human-readable name in the layer panel |
| `description` | string | What the layer means (not just “roads”) |
| `group` | string | Layer panel grouping (e.g., `History`, `Boundaries`) |
| `render` | object | How the map draws it (MapLibre / Cesium config) |
| `provenance` | object | Attribution + license + pointers to catalog/manifests |

### Recommended (strongly encouraged)
| Key | Type | Why it exists |
|---|---|---|
| `version` | string | Change tracking + safe upgrades (`1.0.0`) |
| `tags` | string[] | Search + filtering |
| `ui` | object | Defaults: visibility, opacity, order |
| `legend` | object | Explain symbology and units |
| `interaction` | object | Popup/hover behavior |
| `temporal` | object | Timeline integration |
| `security` | object | Classification + redaction hints |

---

## 🗺️ `render` (MapLibre) — recommended shape

A MapLibre layer manifest should behave like a **style fragment**:

- `sources` is a dictionary of MapLibre sources
- `layers` is an array of MapLibre style layers
- Optional ordering hints help merge into a shared basemap style

```json
{
  "id": "boundaries__counties",
  "title": "Kansas Counties",
  "description": "County boundaries for Kansas (reference layer).",
  "group": "Boundaries",
  "version": "1.0.0",
  "tags": ["kansas", "boundaries", "reference"],
  "ui": {
    "defaultVisible": true,
    "defaultOpacity": 0.85,
    "panelOrder": 20
  },
  "render": {
    "engine": "maplibre",
    "sources": {
      "boundaries__counties": {
        "type": "vector",
        "tiles": ["https://example.com/tiles/counties/{z}/{x}/{y}.pbf"],
        "minzoom": 4,
        "maxzoom": 12
      }
    },
    "layers": [
      {
        "id": "boundaries__counties::outline",
        "type": "line",
        "source": "boundaries__counties",
        "source-layer": "counties",
        "minzoom": 4,
        "paint": {
          "line-width": 1.2,
          "line-opacity": 0.9
        }
      }
    ],
    "orderHint": {
      "beforeLayerId": "labels::places"
    }
  },
  "legend": {
    "type": "categorical",
    "items": [
      { "label": "County boundary", "symbol": { "kind": "line", "width": 2 } }
    ]
  },
  "provenance": {
    "catalogId": "kfm:dataset:counties",
    "sourceManifestRef": "data/sources/kansas_counties.json",
    "attribution": "Kansas source agency (see catalog entry)",
    "license": "See catalog entry",
    "citation": "See catalog entry"
  }
}
```

### MapLibre best practices ✅
- Prefer **vector tiles** for large geometry (performance + styling).
- Keep style layer `id`s unique (prefix with manifest `id`).
- Put expensive layers behind zoom thresholds (`minzoom`/`maxzoom`).
- Prefer a shared basemap style and **merge fragments** using `orderHint`.

---

## 🌍 `render` (Cesium) — optional shape

Use Cesium render blocks for true 3D assets (terrain, 3D Tiles, point clouds).

```json
{
  "id": "terrain__kansas_dem",
  "title": "Kansas Terrain (DEM)",
  "description": "3D terrain visualization for Kansas.",
  "group": "Terrain",
  "version": "1.0.0",
  "ui": { "defaultVisible": false, "defaultOpacity": 1.0, "panelOrder": 5 },
  "render": {
    "engine": "cesium",
    "type": "terrain",
    "url": "https://example.com/cesium/terrain"
  },
  "provenance": {
    "catalogId": "kfm:dataset:kansas_dem",
    "sourceManifestRef": "data/sources/kansas_dem.json",
    "attribution": "See catalog entry",
    "license": "See catalog entry"
  }
}
```

---

## ⏳ `temporal` — timeline integration

If a layer changes over time, it must be discoverable + filterable.

```json
{
  "temporal": {
    "enabled": true,
    "mode": "filter", 
    "timeField": "year",
    "extent": { "start": "1850-01-01", "end": "1950-12-31" },
    "resolution": "year",
    "defaultTime": "1900-01-01"
  }
}
```

### Common patterns
- `mode: "filter"` → web filters features by time (client or server)
- `mode: "swap"` → web swaps sources by time slices (e.g., tilesets per decade)
- `mode: "animate"` → playback/animation support (be careful with perf)

> [!TIP]
> If time filtering can’t be done cheaply in the browser, prefer **server-side filtering** (API query params) or **time-sliced tiles**.

---

## 🧾 `legend` — explain the symbology

### Categorical legend
```json
{
  "legend": {
    "type": "categorical",
    "items": [
      { "label": "Railroad", "symbol": { "kind": "line", "width": 3 } },
      { "label": "Station", "symbol": { "kind": "point", "shape": "circle" } }
    ]
  }
}
```

### Ramp / gradient legend
```json
{
  "legend": {
    "type": "ramp",
    "title": "Population density",
    "units": "people / sq mi",
    "stops": [
      { "value": 0, "label": "0" },
      { "value": 50, "label": "50" },
      { "value": 200, "label": "200+" }
    ],
    "notes": "Classification method documented in the catalog entry."
  }
}
```

---

## 🖱️ `interaction` — click/hover behavior

```json
{
  "interaction": {
    "hover": { "enabled": true },
    "click": {
      "enabled": true,
      "popupTemplate": {
        "title": "{{name}}",
        "rows": [
          { "label": "Type", "value": "{{type}}" },
          { "label": "Year", "value": "{{year}}" }
        ],
        "footer": "Source + license in the layer info panel."
      }
    },
    "featureId": {
      "strategy": "property",
      "property": "id"
    }
  }
}
```

> [!IMPORTANT]
> Any map overlay should expose an **info popup or legend that cites the data source** (through catalog references). ✅

---

## 🔐 `security` — sensitivity + redaction hints

When a layer contains sensitive geography (sacred sites, private addresses, endangered resources, etc.), encode safety constraints here and ensure the UI/API honors them.

```json
{
  "security": {
    "classification": "public",
    "sensitive": false,
    "redaction": {
      "enabled": false,
      "method": "none"
    }
  }
}
```

Examples of redaction strategies:
- Snap to grid / reduce precision (e.g., 3-decimal coords)
- Aggregate to area (county/tract) instead of point
- Hide until zoomed out (no close zoom)

---

## 🧬 `provenance` — required for every layer ✅

The map must never become a “black box of pretty colors.” Every layer needs provenance.

```json
{
  "provenance": {
    "catalogId": "kfm:dataset:railroads_1885",
    "sourceManifestRef": "data/sources/khs_railroads_1885.json",
    "attribution": "Kansas Historical Society",
    "license": "See catalog entry",
    "citation": "See catalog entry",
    "notes": [
      "Georeferencing uncertainty documented in catalog metadata.",
      "Not suitable for parcel-level decisions."
    ]
  }
}
```

---

## ✅ Add a new layer (checklist)

1) 🧾 **Confirm the dataset is governed**
- [ ] External source described in `data/sources/`
- [ ] Canonical metadata exists in `data/catalog/` (STAC/DCAT-ish)
- [ ] License + attribution are explicit

2) 🧩 **Create a manifest file here**
- [ ] File name matches `id`
- [ ] `render` block works (MapLibre or Cesium)
- [ ] `legend` is present (or intentionally `type: "none"`)
- [ ] `provenance` points back to catalog/manifests

3) 🧠 **Story Node / Focus Mode compatibility**
- [ ] Layer has a stable `id` for Story Nodes to reference
- [ ] Interactions don’t leak sensitive detail (if applicable)

4) ♿ **Accessibility + clarity**
- [ ] Readable at intended zooms
- [ ] Color + contrast are sensible (consider high-contrast needs)
- [ ] Legend labels are human-friendly and unit-aware

---

## 🚧 Common pitfalls (please avoid)

- ❌ **No provenance** (“we’ll add it later”)  
- ❌ Huge GeoJSON files bundled into the web app  
- ❌ Styling that only looks good on one monitor (low contrast / thin strokes)  
- ❌ Temporal layers without a temporal contract (`temporal.enabled`)  
- ❌ ID collisions in MapLibre `layers[]`

---

## 🧪 Suggested validation rules (future-proofing)

Even if validation is currently lightweight, write manifests as if they are validated:

- `id` must be unique across all manifests
- `provenance.catalogId` + `sourceManifestRef` required
- `render.engine` ∈ {`maplibre`, `cesium`}
- MapLibre style layer IDs must be unique (prefix rule)
- If `temporal.enabled === true`, require `extent` + `resolution`

---

## 🗺️ Example library (recommended to add over time)

As the project grows, consider adding an `examples/` subfolder:

```text
📁 layers/
  📁 examples/
    📄 vector-tiles.json
    📄 raster-tiles.json
    📄 time-filtered.json
    📄 cesium-3dtiles.json
```

> [!TIP]
> Examples are “living tests” — they help onboarding and prevent schema drift. 🧪
