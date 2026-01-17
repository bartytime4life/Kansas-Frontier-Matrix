---
title: "🧭 boundaries.counties — County Boundaries Overlay"
layer_id: "boundaries.counties"
doc_kind: "README"
status: "active"
version: "1.0.0"
last_updated: "2026-01-17"
license: "MIT"
audience: ["web", "gis", "design"]
tags: ["map", "overlay", "boundaries", "counties", "maplibre", "vector-tiles"]
doc_uuid: "urn:kfm:doc:web:assets:maps:styles:overlays:boundaries.counties:readme:1.0.0"
---

# 🗺️ `boundaries.counties` — County Boundary Overlay

![Overlay](https://img.shields.io/badge/overlay-boundaries.counties-2ea44f)
![Type](https://img.shields.io/badge/type-boundaries-lightgrey)
![Engine](https://img.shields.io/badge/engine-MapLibre_GL_JS-blue)
![Spec](https://img.shields.io/badge/style-Mapbox_Spec_v8-orange)
![Scope](https://img.shields.io/badge/scope-Kansas_(counties)-6f42c1)

A **subtle, non-dominant** boundary overlay for **county outlines** used in the KFM web map viewer. This is meant to provide **geographic context** (and optional click/hover targeting) without overpowering thematic layers.

> [!IMPORTANT]
> County boundaries are administrative constructs and **may change over time**. If your map view includes temporal navigation, prefer a dataset that supports *valid-from / valid-to* filtering (or a versioned-by-era tileset).

---

## 📌 TL;DR

- ✅ Adds **county outlines** (and optional **hover/selected** styling)  
- ✅ Designed to stay **quiet in the visual hierarchy**  
- ✅ Supports **interactive inspection** (feature click → side panel / popup)  
- ✅ Works as a drop-in **overlay style** on top of a basemap + thematic layers  

---

## 📁 Where this lives

`web/assets/maps/styles/overlays/boundaries.counties/`

---

## 🧩 Recommended folder contents

> Your repo may not include all of these yet — this is the **convention** we’re standardizing around.

```text
📁 web/assets/maps/styles/overlays/
  📁 boundaries.counties/
    📄 README.md          ← you are here
    🎨 style.json         ← overlay style (sources + layers)
    🧾 overlay.json       ← UI descriptor (name, group, defaults, legend ref)
    🗺️ legend.json        ← legend entries used by layer list
    🧬 metadata.json      ← provenance + processing notes (human-readable)
```

---

## 🧾 Data contract

This overlay assumes a **polygon** (preferred) or **line** representation of counties delivered as **vector tiles** (recommended) or **GeoJSON** (acceptable for small extents).

### ✅ Expected source + layer naming

Pick one convention and stick to it (examples):

- **Source ID**: `boundaries.counties`
- **Vector tile source-layer**: `counties` *(or `boundaries_counties`)*

### ✅ Minimum attribute fields (recommended)

| Field | Type | Why it matters |
|---|---:|---|
| `geoid` (or `fips`) | string | Stable ID for selection, joins, caching |
| `name` | string | Labels + UI display |
| `statefp` | string | Kansas validation / multi-state safety |
| `valid_from` | number/string | Time filtering (optional but ideal) |
| `valid_to` | number/string | Time filtering (optional but ideal) |

> [!TIP]
> If you want hover/selection to be reliable, ensure features have a **stable ID**. For vector tiles, prefer `promoteId` to a stable field like `geoid`.

---

## 🎨 Cartographic intent

County lines should be:
- **distinct enough** to guide the eye
- **not so bold** that they dominate choropleths, rasters, or feature overlays

### Visual hierarchy rules (recommended)

- **State boundary > County boundary > Township/parcel boundary**
- County boundaries should be **thin**, often slightly **transparent**, and ideally **not pure black**
- Avoid heavy outlines that fight with:
  - choropleths
  - hillshades
  - raster overlays
  - dense linework layers

---

## 🧱 Layer layout (style.json)

Below is a suggested layer breakdown. Your actual IDs can differ, but keep them **namespaced** and predictable.

| Layer ID (suggested) | Type | Purpose |
|---|---|---|
| `kfm-boundaries-counties-fill` | `fill` | Optional subtle fill for hit-targeting |
| `kfm-boundaries-counties-outline` | `line` | Default county outlines |
| `kfm-boundaries-counties-hover` | `line` | Hover highlight via `feature-state` |
| `kfm-boundaries-counties-selected` | `line` | Selected county highlight |
| `kfm-boundaries-counties-label` | `symbol` | Optional labels (often separate overlay) |

> [!NOTE]
> Labels are frequently better as a **separate overlay** so users can toggle boundaries independently from text density.

---

## 🔎 Interaction states

This overlay is commonly used with:
- **hover**: outline brightens / thickens
- **selected**: outline becomes more prominent + optional fill
- **disabled**: overlay hidden

### Suggested MapLibre pattern (feature-state)

```js
// Hover
map.on("mousemove", "kfm-boundaries-counties-fill", (e) => {
  if (!e.features?.length) return;
  const id = e.features[0].id; // requires promoteId or generated ids
  map.setFeatureState({ source: "boundaries.counties", id }, { hover: true });
});

// Clear hover (example)
map.on("mouseleave", "kfm-boundaries-counties-fill", () => {
  // track last hovered id in your app state and clear it here
});
```

And in `style.json`, use an expression like:

```json
{
  "id": "kfm-boundaries-counties-hover",
  "type": "line",
  "source": "boundaries.counties",
  "source-layer": "counties",
  "paint": {
    "line-width": [
      "case",
      ["boolean", ["feature-state", "hover"], false],
      2,
      1
    ]
  }
}
```

---

## ⏳ Temporal filtering (optional but encouraged)

If the dataset includes `valid_from` / `valid_to`, the web app’s timeline slider can update the overlay by applying a filter:

```js
// Example: year = 1870
map.setFilter("kfm-boundaries-counties-fill", [
  "all",
  ["<=", ["get", "valid_from"], 1870],
  [">", ["get", "valid_to"], 1870]
]);
```

> [!IMPORTANT]
> Be consistent about whether `valid_to` is **inclusive** or **exclusive** and document it in `metadata.json`.

---

## 🧬 Provenance requirements

County boundaries are a **foundational reference layer**. Treat them as first-class, auditable data.

### Minimum provenance checklist

- [ ] Original source name + link (dataset/provider)
- [ ] License + attribution text
- [ ] Retrieval date (and snapshot/version if available)
- [ ] Processing summary (simplification, topology fixes, tiling steps)
- [ ] Temporal model (if historical): how validity is encoded
- [ ] Known caveats (disputed boundaries, gaps, uncertain eras)

> [!TIP]
> If the project uses a catalog approach (STAC-like JSON entries), ensure this layer has a matching dataset record (e.g., `data/sources/boundaries.counties.json`) and that the UI can surface attribution from it.

---

## ✅ Quick QA (smoke test)

1. Toggle **County Boundaries** on/off in the layer list  
2. Zoom from statewide → local:
   - lines should remain readable without turning into a “spiderweb”
3. Confirm hover/click behavior:
   - hover highlight appears and clears cleanly
   - click opens correct county metadata
4. Check overlay ordering:
   - boundaries should sit **above basemap** but **below labels** (unless labels belong to this overlay)

---

## 🔁 Versioning

- Increment `version` when you change:
  - layer IDs
  - source IDs / source-layer names
  - styling defaults that affect map readability
  - temporal semantics (`valid_to` inclusive/exclusive)

Changelog (optional):
- **1.0.0** — Initial overlay README + conventions

---

## 🤝 Contributing

If you adjust this overlay, please:
- keep changes **subtle** and test against at least one “busy” thematic layer
- update `metadata.json` if styling changes imply a new data assumption
- avoid introducing hard-coded, app-specific hacks into the overlay style

> [!NOTE]
> The goal is composability: this overlay should work in the base map, story mode, and catalog previews without special-case code.
