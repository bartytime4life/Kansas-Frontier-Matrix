# 🗺️ Map Assets (`web/src/assets/map/`)

![Scope](https://img.shields.io/badge/scope-frontend%20map%20assets-informational)
![UI](https://img.shields.io/badge/UI-React%20%C2%B7%20MapLibre-informational)
![Tiles](https://img.shields.io/badge/tiles-vector%20MVT%20%28.pbf%29%20%7C%20raster%20%28.png%2F.webp%29-informational)
![CRS](https://img.shields.io/badge/CRS-WGS84%20EPSG%3A4326%20%2B%20Web%20Mercator%20EPSG%3A3857-informational)

> 🎯 **Goal:** This folder is the **single home** for *static* map UI assets used by the web app (styles, sprites, icons, small demo GeoJSON, etc.).  
> 🧠 **Rule of thumb:** If it’s “big data,” it belongs in the pipeline + API (tiles/queries), **not** bundled into the web build.

---

## ✨ What belongs here

✅ **UI-facing, versioned assets** that the map renderer needs at runtime:
- 🧾 **Map style JSON** (`*.style.json`) for MapLibre/OpenLayers clients
- 🧩 **Sprites** (sprite sheet + JSON index)
- 🔤 **Glyphs / fonts** (if self-hosting)
- 🧷 **Icons** for overlays/controls (SVG/PNG)
- 🧪 **Tiny sample GeoJSON** for dev/demo (kept small)

❌ **What should NOT live here**
- 🏋️ Large GeoJSON/shapefiles/rasters (serve via tiles instead)
- 🔐 Sensitive / restricted location data (even “temporary”)
- 🧬 “Authoritative” datasets (those belong in the governed pipeline + catalogs)

---

## 🧭 How the web map is expected to work (KFM-aligned)

- The UI is a **Map UI** in the pipeline (React + MapLibre; optionally Cesium). [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **All map data access goes through the API layer** (no direct graph access from the frontend). [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Map layers should ideally be delivered as **tiles**:
  - Vector tiles (MVT): `GET /tiles/{layer}/{z}/{x}/{y}.pbf`
  - Raster tiles: `GET /tiles/{layer}/{z}/{x}/{y}.png` (or `.webp`)
  - This lets external clients (MapLibre GL JS, OpenLayers, etc.) consume the same tile URLs the KFM web UI uses. [oai_citation:2‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 📁 Suggested folder layout (keep it tidy)

> ⚠️ This is a “target shape” for the folder. Add what you need, but follow the conventions.

```text
📦 web/src/assets/map/
├── 🧾 styles/
│   ├── kfm.base.style.json
│   ├── kfm.dark.style.json
│   └── kfm.print.style.json
├── 🧩 sprites/
│   ├── kfm-sprite.png
│   ├── kfm-sprite@2x.png
│   └── kfm-sprite.json
├── 🔤 glyphs/                       # only if self-hosting glyphs
│   └── {fontstack}/{range}.pbf
├── 🧷 icons/
│   ├── ui/
│   └── markers/
├── 🧪 data/
│   ├── sample/                      # tiny dev/demo GeoJSON only
│   └── extents/
└── 📄 README.md                      # you are here 🙂
```

---

## 🧱 Asset standards

### 🏷️ Naming
- **kebab-case** for files: `kfm.base.style.json`, `historic-trails.layer.json`
- Prefix KFM-owned assets with `kfm-` where ambiguity exists (sprites, icon packs)
- Keep styles *environment-agnostic* (don’t hardcode `localhost` URLs)

### 📦 Size & performance
- Don’t bundle large datasets into the web app.
- If a layer is intended for interactive use, publish it as tiles and reference it in style JSON. [oai_citation:3‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🌐 CRS / Projections (don’t get burned 🔥)

### ✅ GeoJSON in this repo: prefer WGS84 (EPSG:4326)
When exporting GeoJSON for quick checks (and especially for GitHub viewing), transform to **WGS84 / EPSG:4326**. [oai_citation:4‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

> 📝 Why: some tooling (including GitHub preview) expects WGS84 GeoJSON. [oai_citation:5‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

### 🧠 PostGIS → GeoJSON gotcha
PostGIS may output **only the geometry**, not a fully formed GeoJSON Feature/FeatureCollection—finish the structure in code when exporting. [oai_citation:6‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

### 🗺️ Web maps commonly operate in EPSG:3857
Some workflows involve GeoJSON in **EPSG:3857** derived from OSM WGS84 sources, with transformation steps handled upstream (ETL), not in the UI layer. [oai_citation:7‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

---

## ➕ Adding a new map layer (checklist ✅)

### 1) 📦 Make sure it’s a *published* artifact
KFM ordering is strict: **ETL → Catalogs → Graph → API → UI** is “inviolable.” [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Also: **Provenance first**—published data should be registered before UI use. [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 2) 🧊 Expose it via tiles (preferred)
Wire it behind the standard tile endpoints:
- Vector tiles: `.../{z}/{x}/{y}.pbf`
- Raster tiles: `.../{z}/{x}/{y}.png` or `.webp` [oai_citation:10‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 3) 🧾 Update style JSON (or add a new style)
Add/modify a `source` and corresponding `layers` in your MapLibre style.

<details>
<summary>🧩 Minimal example (illustrative)</summary>

```json
{
  "version": 8,
  "sources": {
    "kfm_trails": {
      "type": "vector",
      "tiles": ["/tiles/historic_trails/{z}/{x}/{y}.pbf"],
      "minzoom": 0,
      "maxzoom": 14
    }
  },
  "layers": [
    {
      "id": "trails-line",
      "type": "line",
      "source": "kfm_trails",
      "source-layer": "historic_trails"
    }
  ]
}
```
</details>

### 4) 🧾 Add attribution + metadata
Maps should include the **data sources and citations**, plus other credits and metadata as relevant. [oai_citation:11‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

> 📌 Include projection/CRS info when it matters for combining with other GIS data. [oai_citation:12‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

### 5) 🔐 Respect sovereignty + classification
No output may be **less restricted** than its inputs; sensitive sources require redaction/approval, and the UI may need safeguards (e.g., blurring/generalization). [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🎨 Cartography & UX checklist (from “Making Maps”) 🧠🖌️

Use this when you’re producing:
- 🗺️ a new style
- 📸 map screenshots for docs/story nodes
- 🧾 printable/export views

### 📏 Scale
- Local → continental maps should include a **scale** when measurement matters.
- If the map may be resized, a **visual scale** stays accurate after scaling.
- For very small-scale maps (large parts of Earth), simple visual scales can be misleading due to scale variation. [oai_citation:14‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

### 📝 Explanatory text
Text blocks are often vital—use them to explain map context, goals, and interpretations of patterns you’re showing. [oai_citation:15‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

### 🧩 Legend
Legends should include symbols your audience may not recognize; skip the obvious—your legend is the “key to interpretation.” [oai_citation:16‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

### 🧭 Directional indicator (north arrow)
Use one when:
- the map isn’t oriented north, or
- the area is unfamiliar to the audience.  
Also: avoid giant ugly arrows 🙂 [oai_citation:17‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

### 🖼️ Border / neatline
Try the design without borders first; if used, keep it narrow and non-distracting. [oai_citation:18‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

### 🧾 Sources & credits
Include (as relevant): data sources/citations, map maker/date, organization/logos, disclaimers, series info, copyright/use, and projection/CRS details. [oai_citation:19‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

---

## 🧰 Dev workflow tips (React tooling)

If using a CRA-like setup, the typical dev loop is:
- `npm start` launches the dev server (commonly at `http://localhost:3000/`). [oai_citation:20‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)
- Hot reloading is especially friendly for **CSS** changes (swap without full reload). [oai_citation:21‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)
- Prefer keeping bundler tooling (e.g., webpack) as a **project dependency** to control versions across environments. [oai_citation:22‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

---

## ✅ Do / ❌ Don’t

✅ Do
- Keep styles **portable** (env variables/config pick API base URL)
- Add **attribution + CRS** for any layer that could be reused in GIS [oai_citation:23‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)
- Prefer **tiles over bundled data** for anything non-trivial [oai_citation:24‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

❌ Don’t
- Don’t ship large “real” datasets under `web/src/assets/…`
- Don’t bypass the API boundary from the UI [oai_citation:25‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Don’t add unsourced narrative claims to map UI callouts/tooltips (evidence-first) [oai_citation:26‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔗 Related docs (repo)

- 📘 KFM master guide: `../../../../docs/MASTER_GUIDE_v13.md`
- 🧱 API contracts: `../../../../src/server/api/`
- 🧪 Pipelines & ETL: `../../../../src/pipelines/`

---

## 📚 Source materials used to shape this folder’s rules

- 🗺️ *Making Maps (GIS map design)* — scale/legend/credits/projection guidance. [oai_citation:27‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9) [oai_citation:28‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9) [oai_citation:29‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)  [oai_citation:30‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)  
- 🧭 *Python Geospatial Analysis Cookbook* — GeoJSON export + CRS transforms (EPSG:4326) + PostGIS caveats. [oai_citation:31‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp) [oai_citation:32‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  [oai_citation:33‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  
- 🧊 *KFM Comprehensive System Documentation* — canonical tile endpoints & multi-client consumption. [oai_citation:34‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  [oai_citation:35‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- 🧷 *KFM Markdown Guide v13* — pipeline invariants, API boundary, and UI stack expectation. [oai_citation:36‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:37‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  [oai_citation:38‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- ⚛️ *Node/React tooling notes* — dev server + hot reloading behavior. [oai_citation:39‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  [oai_citation:40‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  