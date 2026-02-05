<div align="center">

# 🧱 Base Layer Definitions

![KFM](https://img.shields.io/badge/KFM-Frontier%20Matrix-2ea44f?style=flat-square)
![Layers](https://img.shields.io/badge/Layers-Definitions-555?style=flat-square)
![MapLibre](https://img.shields.io/badge/MapLibre-GL%20JS-blue?style=flat-square)
![Cesium](https://img.shields.io/badge/Cesium-JS-0b7285?style=flat-square)
![Tiles](https://img.shields.io/badge/Tiles-MVT%20%7C%20XYZ%20Raster-6f42c1?style=flat-square)
![Provenance](https://img.shields.io/badge/Provenance-STAC%20%7C%20DCAT%20%7C%20PROV-orange?style=flat-square)
![Governance](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-critical?style=flat-square)

**Path:** `web/src/layers/definitions/base/`

_Boring, fast, legal, provenance-rich._ ✅

</div>

---

## 🎯 What this folder is for

This directory contains **base layer definitions** — the foundational map layers that everything else sits on top of:

- 🗺️ **Basemaps** (light/dark, terrain, imagery, etc.)
- 🧭 **Reference context** layers that help users orient themselves (boundaries, labels, hillshade, etc.)
- 🧱 **Base primitives** that must be stable across stories, dashboards, and modes (2D MapLibre + optional 3D Cesium)

These are *not* “story overlays.” Base layers should provide **context**, not steal attention.

> ✨ KFM principle: every visible layer should have **“the map behind the map”** — clear provenance, metadata, license, and attribution surfaced in the UI.

---

## 🧠 How base layers fit into KFM’s “truth path”

KFM is designed so the UI doesn’t “wing it” or bypass governance. Base layers should follow the same rules as every other layer:

```text
Raw ➜ Processed ➜ Catalog (STAC/DCAT + PROV) ➜ DB ➜ API ➜ UI (MapLibre/Cesium)
```

### Why this matters for **base** layers
Even if a basemap “feels generic,” it still needs:
- ✅ **Attribution** (who made it)
- ✅ **License constraints** (what we’re allowed to do with it)
- ✅ **Metadata + provenance links** (where it came from, and how it was produced/served)
- ✅ **Classification & governance** (especially if it includes sensitive content)

---

## 🧩 What a “base layer definition” should contain

A base layer definition is a **front-end contract** that answers:

1) **What do we render?**  
2) **Where does it come from?** (KFM API tiles, external tiles, GeoJSON, 3D tiles, etc.)  
3) **How do we style it?** (MapLibre paint/layout, Cesium imagery settings)  
4) **How do we cite it?** (dataset metadata + provenance)  
5) **How do we govern it?** (classification, redaction rules, CARE constraints)

### ✅ Recommended minimum fields (shape may vary by actual TypeScript types)

> ⚠️ Use this as a checklist. The real interface/type lives in code (nearby `types.ts` / `registry.ts` / `index.ts` patterns).

- `id` — stable identifier (never reuse)
- `title` / `summary` — human-friendly UI strings
- `kind` — `basemap` | `reference`
- `renderer` — `maplibre` | `cesium` | `both`
- `defaultVisibility` — on/off by default
- `order` — render order (base layers should always be near the bottom)
- `source` — where data/tiles come from
- `style` — how it looks
- `attribution` — required for any third-party or derived work
- `license` — *must* be explicit (even for “free” tiles)
- `catalogRef` — pointer to DCAT/STAC dataset IDs (or external-catalog metadata)
- `provenanceRef` — pointer to PROV lineage bundle (or provenance statement)
- `classification` — `public` | `internal` | `confidential` | `restricted`
- `ui` — grouping, icon, legend behavior, info panel / “Layer Details” integration

---

## 🗺️ Rendering targets: MapLibre + Cesium

KFM’s map UI is built around:

- **MapLibre GL JS (2D)** — vector map styling + tile layers + GeoJSON overlays  
- **CesiumJS (3D)** — imagery draped on terrain + 3D tiles (optional mode)

Base definitions should declare how they behave in each renderer when relevant:
- a MapLibre **style URL** or **source/layer injection**
- a Cesium **imagery provider** / **terrain** configuration (when applicable)

---

## 🧵 Tile endpoints & data sourcing rules

### ✅ Preferred: KFM-served tiles (governed, consistent)
When the data is part of KFM, the base layer should reference **KFM tile endpoints** (vector or raster), so web/3D/mobile can “drink from the same well.”

Typical patterns:
- Vector tiles (MVT): `.../tiles/<layer>/{z}/{x}/{y}.pbf`
- Raster tiles: `.../tiles/<layer>/{z}/{x}/{y}.png` (or `.webp`)

### ⚠️ Allowed: external tiles (only with explicit licensing + attribution)
If you use external tiles (OSM styles, imagery providers, etc.), the definition **must**:
- include a clear attribution string,
- declare the license,
- document any usage restrictions,
- avoid sources that cannot legally be reused in our context.

---

## 🧾 Metadata: “map behind the map” requirements

Base layers must carry enough metadata for the UI to show:
- **Identification** (what is it?)
- **Quality** (how reliable / resolution / update cadence)
- **Spatial reference** (projection / tiling scheme assumptions)
- **Distribution & use policy** (license, attribution)
- **Temporal context** (when collected/updated)
- **Contact** (who maintains it)

> 🏷️ Treat metadata as a first-class product. If we can’t explain a base layer, we shouldn’t ship it.

---

## 🪶 Visual design principles for base layers

Base layers should support strong **figure–ground**:
- 🫥 Base = low-contrast, calm texture
- 🌟 Overlays = higher contrast, story-relevant color & emphasis
- 🧭 Labels should be readable but not overpower thematic layers

**Rule of thumb:** if the basemap is the first thing you notice, it’s too loud.

---

## 🛡️ Governance & sensitivity (FAIR + CARE)

Base layers are *not exempt* from governance.

### Classification (recommended)
Use a simple classification model to prevent accidental exposure:
- `public` — safe for all
- `internal` — team-only
- `confidential` — limited group
- `restricted` — sensitive/high-impact

### CARE considerations
If a base layer includes culturally sensitive information (e.g., tribal lands, archaeological site indicators, sacred sites):
- ✅ it **triggers governance review**
- ✅ it may require **redaction/generalization**
- ✅ it must clearly document what was redacted and why
- ✅ the UI should avoid exposing precise coordinates when inappropriate

---

## ➕ Adding a new base layer (step-by-step)

### 1) 📦 Confirm the data path is valid
- If it’s KFM data, confirm it exists in:
  - STAC/DCAT catalogs (discoverable metadata)
  - PROV lineage (traceable processing)
  - API surface (tiles or GeoJSON)

### 2) 🧱 Create the layer definition file in this folder
Keep it small and explicit. Prefer config over logic.

✅ Include:
- stable `id`
- clear title/summary
- attribution + license
- a catalog/provenance reference
- source URL templates (KFM tiles or approved external provider)
- default visibility + ordering

### 3) 🧬 Register it in the layer registry
Wherever the central registry lives (often `web/src/layers/registry.ts` or `web/src/layers/definitions/index.ts`):
- export it
- assign it to the correct UI group (Basemaps, Reference, etc.)

### 4) 🔎 Add/verify UI “Layer Details”
Every base layer should open an info panel that includes:
- source links (DCAT/STAC)
- license text / attribution
- provenance summary (PROV)
- data freshness notes (if known)

### 5) ✅ QA checklist
- [ ] Renders in 2D (MapLibre) at expected zooms
- [ ] Renders in 3D (Cesium) if applicable
- [ ] Attribution visible & correct
- [ ] License declared & consistent with intended usage
- [ ] No sensitive coordinates leaked (if applicable)
- [ ] Performance acceptable (no giant GeoJSON blobs)
- [ ] Works across story mode / free explore / focus mode

---

## 🧪 Example (pseudo-code) base layer definition

> 🧷 This is illustrative. Align it to the project’s real type/interface.

```ts
export const kansasBaseImagery = {
  id: "basemap_kansas_imagery",
  kind: "basemap",
  title: "Kansas Imagery",
  summary: "High-resolution imagery basemap for Kansas (governed via KFM tiles).",
  defaultVisibility: true,
  order: 0,

  classification: "public",

  attribution: "© Provider Name / Agency Name (see Layer Details)",
  license: "CC-BY-4.0 (example — must be verified)",

  catalogRef: {
    datasetId: "ks_imagery_basemap",
    // optionally: stacCollectionId, dcatId, etc.
  },
  provenanceRef: {
    provBundleId: "prov:ks_imagery_basemap_v1",
  },

  maplibre: {
    source: {
      type: "raster",
      tiles: ["/tiles/ks_imagery/{z}/{x}/{y}.png"],
      tileSize: 256,
    },
    layer: {
      id: "ks_imagery",
      type: "raster",
      // paint/layout as needed
    },
  },

  cesium: {
    imagery: {
      urlTemplate: "/tiles/ks_imagery/{z}/{x}/{y}.png",
      // Cesium imagery provider options as needed
    },
  },

  ui: {
    group: "Basemaps",
    icon: "🛰️",
    showInLayerPicker: true,
    showLegend: false,
  },
};
```

---

## 🧯 Common pitfalls (and how to avoid them)

- **“It renders, ship it”** ❌  
  If it doesn’t have license + provenance hooks, it’s not done.

- **Embedding raw GeoJSON for a basemap** ❌  
  Basemaps should be tile-based and fast.

- **Using restricted imagery sources casually** ❌  
  Many popular imagery sources have strict reuse rules. Default to open/government imagery or KFM-governed tiles.

- **Noisy base styling** ❌  
  If overlays can’t stand out, tone down the basemap.

---

## 🔗 See also (inside the repo)

- `src/server/api/README.md` — dataset + tile endpoints (DCAT/STAC + MVT/XYZ)
- `docs/architecture/system_overview.md` — canonical pipeline + “truth path”
- `docs/governance/*` — review gates, sensitivity rules, CARE practices (if present)

---

## ✅ Definition of “done”

A base layer is **done** when:
- it renders reliably,
- it’s fast,
- it’s legally usable,
- and the UI can explain it with metadata + provenance (“map behind the map”).

🧠 **If we can’t defend it, we don’t ship it.**