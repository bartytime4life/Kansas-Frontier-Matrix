# 🎨 Overlay Styles — `<overlay-id>`  

![KFM](https://img.shields.io/badge/KFM-Living%20Atlas-blue)
![UI](https://img.shields.io/badge/UI-React%20%2B%20MapLibre-success)
![3D](https://img.shields.io/badge/3D-Cesium%20optional-informational)
![Contract](https://img.shields.io/badge/Contracts-Provenance--first-important)
![Status](https://img.shields.io/badge/Scope-Overlay%20presentation%20only-lightgrey)

> [!IMPORTANT]
> Styling is “just presentation”… but in KFM it’s still **governed**: anything that appears in the UI must remain traceable to cataloged sources and provable processing, and the UI must consume data only through the API boundary. See **Provenance & API rules** below.  🧾🧭[^contract-provenance][^pipeline]

---

## 📍 What this folder is

This folder contains **overlay-specific style assets** for the map overlay identified by:

- **Overlay ID:** `<overlay-id>`
- **Path:** `web/assets/maps/overlays/<overlay-id>/styles/`

In the KFM web app, the map viewer is responsible for rendering basemaps and **overlaying layers** + interactions; MapLibre GL JS is used for the 2D map experience, and Cesium may be used for optional 3D views. 🗺️✨[^ui-stack]

---

## 🧠 Mental model: “data ≠ style”

KFM is designed so that **evidence flows through a strict pipeline** (ETL → catalogs → graph → API → UI → story) and the UI is the final consumer. 🧱➡️🗺️[^kfm-what][^pipeline]

**This `styles/` folder is intentionally “downstream”:**
- ✅ It defines **how** an overlay looks (colors, widths, labels, icons, legend rules).
- ❌ It must **not** define *what* the data is, *where* it comes from, or bypass the API/metadata gates.

---

## ⚡ Quick start

1. **Create (or update) a style variant** (recommended: `default`, `dark`, `print`).
2. **Add MapLibre layer rules** that reference the overlay’s **source id** and properties.
3. **Define/update the legend spec** so the UI can render a correct legend.
4. **Test in the map UI**:
   - Toggle the layer
   - Adjust opacity
   - Validate the legend updates and matches visible data
   - If time-enabled, validate the timeline/slider behavior  
   ✅ These are first-class UI behaviors in KFM’s map experience. 🧪🧷[^maplibre-overlays][^timeline]

---

## 🗂️ Recommended file layout

```text
📁 web/assets/maps/overlays/<overlay-id>/
  ├─ 📁 styles/
  │   ├─ 📄 README.md                       ← you are here
  │   ├─ 🎨 style.default.maplibre.json      ← MapLibre layer fragment (recommended)
  │   ├─ 🌙 style.dark.maplibre.json         ← optional theme variant
  │   ├─ 🖨️ style.print.maplibre.json        ← optional print-friendly variant
  │   ├─ 🧾 legend.default.json              ← legend rules + labels
  │   ├─ 🧾 legend.dark.json                 ← optional legend variant
  │   ├─ 🧩 tokens.json                      ← colors / widths / icon names (optional)
  │   └─ 📁 icons/                           ← svg/png used by the overlay (optional)
  │       └─ 🖼️ <icon>.svg
  └─ (other overlay assets live alongside, not inside styles/)
```

> [!NOTE]
> If your implementation currently prefers a **single** file (style + legend combined), you can still keep the same structure—just collapse the pieces. The key is: **keep it deterministic + reviewable**.

---

## 🧩 Style contract

### ✅ Preferred: MapLibre “layer fragment” JSON

Rather than storing a *full* basemap style, we recommend storing **overlay layer fragments** that can be merged onto the active basemap style.

**File:** `style.<variant>.maplibre.json`  
**Shape (recommended):**

```json
{
  "$schema": "../../../../../../schemas/ui/overlay-style.schema.json",
  "styleId": "default",
  "target": "maplibre",
  "overlayId": "<overlay-id>",
  "layers": [
    {
      "id": "overlay.<overlay-id>.fill",
      "type": "fill",
      "source": "<overlay-id>",
      "source-layer": "<tile-layer-name>",
      "minzoom": 4,
      "maxzoom": 14,
      "paint": {
        "fill-opacity": 0.6
      },
      "metadata": {
        "kfm": {
          "overlayId": "<overlay-id>",
          "legendKey": "treaty_type",
          "interactive": true,
          "provenanceHint": "show-tooltip"
        }
      }
    }
  ]
}
```

**Rules of thumb (do these every time):**
- **Namespace layer ids** with `overlay.<overlay-id>.*` (avoids collisions).
- Keep `minzoom/maxzoom` tight (performance + clarity).
- Use `metadata.kfm.*` for UI hints (legend binding, interactivity, tooltip mode).
- **Don’t bake in “data fetching”** (no URLs to Neo4j, no graph queries; the UI must go through the API). 🧱🛑[^pipeline]

---

## 🧾 Legend spec

KFM’s map UI supports a **layer panel, opacity controls, and legends that update with what’s visible**. Your legend files should stay in sync with the style and the current data/filters. 📊🧭[^maplibre-overlays]

**File:** `legend.<variant>.json`  
**Two common patterns:**

### 1) Categorical (discrete classes)

```json
{
  "overlayId": "<overlay-id>",
  "variant": "default",
  "type": "categorical",
  "title": "Treaty Classification",
  "items": [
    { "label": "Category A", "symbol": { "shape": "square", "color": "#RRGGBB" } },
    { "label": "Category B", "symbol": { "shape": "square", "color": "#RRGGBB" } }
  ],
  "notes": "Legend reflects current map filters and time range."
}
```

### 2) Continuous (numeric ramp)

```json
{
  "overlayId": "<overlay-id>",
  "variant": "default",
  "type": "continuous",
  "title": "Population Density",
  "units": "people / sq mi",
  "ramp": {
    "stops": [
      { "value": 0, "color": "#RRGGBB" },
      { "value": 50, "color": "#RRGGBB" },
      { "value": 200, "color": "#RRGGBB" }
    ]
  }
}
```

---

## 🧾 Provenance & interaction requirements

### ✅ Keep the “map behind the map” visible

KFM’s map experience is explicitly designed to preserve provenance context—e.g., **interactive tooltips** showing **source and metadata** for map elements. 🔎🗺️[^tooltips]

**Therefore:**
- Don’t style in a way that **prevents feature interaction** unless there’s a reason.
- Keep “click/hover target layers” consistent and documented.
- Use `metadata.kfm.interactive=true` (or your project’s equivalent) so the UI knows which layers are pickable.

### 🧱 Respect KFM’s pipeline and API boundary

KFM’s v13 invariants include:
- **Pipeline ordering is absolute** (ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode).
- **Frontend must never query Neo4j directly; all access goes through the API layer** (`src/server/`) to enforce redaction, access controls, and schema consistency. 🔐🧯[^pipeline]

Your styles should only reference:
- stable `overlayId` identifiers
- attribute/property names present in the overlay payload/tiles
- legend keys and UI hints (metadata)

---

## ♿ Accessibility & cartographic hygiene

A style is “correct” only if it’s readable and inclusive:

- ✅ Don’t rely on color alone (use outlines, dashes, icons, patterns).
- ✅ Keep line weights readable at typical zoom levels.
- ✅ Ensure sufficient contrast against **both** light and dark basemaps.
- ✅ For dense point layers: prefer clustering and/or progressive disclosure by zoom.

> [!TIP]
> If an overlay is time-enabled, prioritize clarity while scrubbing the timeline (avoid flicker and “color popping”). The UI supports a timeline slider for temporal exploration. ⏳🧭[^timeline]

---

## 🚀 Performance guardrails

MapLibre is fast, but you can still DDoS the GPU with “pretty”:

- Prefer **fewer layers** with clear rules over many micro-layers.
- Keep expressions simple (avoid nested `case` explosions).
- Set `minzoom/maxzoom` thoughtfully.
- Use server-side generalization / tiling where possible (style shouldn’t compensate for unbounded geometry).

---

## ✅ PR / review checklist

**Before merging style changes:**

- [ ] Layer IDs are namespaced: `overlay.<overlay-id>.*`
- [ ] Legend matches the style (labels, symbols, ranges)
- [ ] Layer panel toggle works + opacity slider behaves as expected[^maplibre-overlays]
- [ ] Tooltip/click still exposes source + metadata (“map behind the map”)[^tooltips]
- [ ] Time-enabled layers behave with the timeline slider (if applicable)[^timeline]
- [ ] No direct Neo4j / graph access assumptions; data is API-served[^pipeline]
- [ ] Accessibility: readable at common zooms; not color-only
- [ ] Performance: no unnecessary layers; zoom bounds set

---

## 🔗 Related docs (repo)

- `docs/MASTER_GUIDE_v13.md` — overall repo blueprint & invariants[^dir-layout]
- `web/` — frontend home (React + MapLibre) and map viewer code[^dir-layout][^ui-stack]
- `src/server/` — API boundary (contracts + redaction)[^pipeline][^dir-layout]
- `schemas/` — schemas for UI + other contracts (add overlay-style schema here if missing)[^dir-layout]

---

## 📚 References (project sources)

[^kfm-what]: KFM overview: catalogs (STAC/DCAT/PROV), graph, and “map-and-narrative UI” workflow. [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

[^pipeline]: v13 invariants: pipeline ordering is inviolable and UI must not query Neo4j directly; all access goes through the API boundary for controls/redaction/schemas. [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

[^dir-layout]: v13 directory layout: UI lives in `web/`, API boundary lives in `src/server/`, and schemas live in `schemas/` (including UI schemas). [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

[^ui-stack]: KFM frontend details: `web/` is React; `viewers/` includes MapLibre GL JS (2D) and CesiumJS (3D), and `MapViewer.jsx` handles basemap + overlays + interactions. [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^maplibre-overlays]: MapLibre usage: interactive overlays, layer toggles, opacity adjustment, and legends that update based on visible data. [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^timeline]: Temporal exploration: the UI includes a time slider; time-enabled layers sync to browse change over time. [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^tooltips]: Provenance-in-UI: interactive tooltips show source + metadata, keeping the “map behind the map” visible. [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^contract-provenance]: Architecture rule: anything shown in UI/Focus Mode must trace back to cataloged sources and provable processing; uses STAC/DCAT/PROV standards. [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
