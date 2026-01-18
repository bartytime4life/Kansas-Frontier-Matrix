# 🗺️ Map Illustration Assets (Web UI)

![badge](https://img.shields.io/badge/assets-map%20illustrations-2b6cb0?style=for-the-badge)
![badge](https://img.shields.io/badge/formats-SVG%20%7C%20PNG%20%7C%20WebP-0f766e?style=for-the-badge)
![badge](https://img.shields.io/badge/focus-provenance--first-7c3aed?style=for-the-badge)

> **Path:** `web/assets/media/illustrations/map/`  
> **Purpose:** Static map-related **illustrations** used by the KFM web experience (thumbnails, legends, overlays, icons, story-map images), **not** the canonical geospatial datasets.

---

## 📌 Quick navigation

- [What belongs here (and what doesn’t)](#-what-belongs-here-and-what-doesnt)
- [Folder layout conventions](#-folder-layout-conventions)
- [Naming conventions](#-naming-conventions)
- [Formats and export specs](#-formats-and-export-specs)
- [Cartographic + UX checklist](#-cartographic--ux-checklist)
- [Provenance & metadata](#-provenance--metadata)
- [How to use in the web UI](#-how-to-use-in-the-web-ui)
- [Add a new asset checklist](#-add-a-new-asset-checklist)
- [References](#-references)

---

## ✅ What belongs here (and what doesn’t)

### ✅ Belongs here
Static media that *supports* mapping experiences in the UI, such as:

- 🧭 **Legend cards / legend swatches** (SVG preferred)
- 🧷 **Map markers / icons** (SVG preferred)
- 🗺️ **Map thumbnails / previews** (WebP/PNG)
- 🧩 **Explainer overlays** (e.g., “how to read this map”, timeline callouts)
- 🧾 **Story-map illustrations** (hero images, section headers, infographics)

### ❌ Does **not** belong here
If it’s data or must be queried/filtered/validated as truth, it should live in the **data pipeline**, not as a UI illustration:

- 🧱 GeoJSON, Shapefiles, rasters, COGs, MBTiles, STAC items, etc.
- 🧮 Anything requiring spatial joins or “measurement-grade” accuracy

> [!NOTE]
> The Kansas Frontier Matrix project is explicitly **provenance-first** and avoids “mystery layers.” Treat every illustration here like a user-facing claim: it must be traceable and documented.  [oai_citation:0‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj)

---

## 🗂️ Folder layout conventions

This folder may evolve, but aim for a structure like:

```
📁 web/
  📁 assets/
    📁 media/
      📁 illustrations/
        📁 map/
          📄 README.md  👈 you are here
          📁 icons/      (markers, pictograms, UI map symbols)
          📁 legends/    (legend cards, swatches, scale bars, north arrows)
          📁 thumbs/     (layer previews, mini-maps, selection tiles)
          📁 overlays/   (story-map overlays, callouts)
          📁 source/     (optional: “working” files if kept in repo)
          📁 meta/       (optional: centralized metadata if not sidecar)
```

> [!TIP]
> If your asset doesn’t fit an existing subfolder, create one—**but keep names simple** and consistent (kebab-case).

---

## 🏷️ Naming conventions

Use **kebab-case** and encode variants cleanly.

### ✅ Recommended pattern

`<domain>-<subject>-<purpose>--<variant>.<ext>`

Examples:

- `kfm-kansas-outline--light.svg`
- `kfm-kansas-outline--dark.svg`
- `legend-railroads-1870.svg`
- `thumb-tribal-territories-1854@2x.webp`
- `icon-trading-post.svg`
- `overlay-how-to-read-treaty-boundaries.svg`

### Variants we support

- **Theme:** `--light` / `--dark`
- **Density:** `@2x`, `@3x` (raster)
- **Locale (optional):** `--en`, `--es`, etc.
- **State/version (optional):** `--draft`, `--final` (avoid if possible; prefer git history)

---

## 🎨 Formats and export specs

| Asset Type | Preferred Format | Why | Notes |
|---|---:|---|---|
| Icons / markers | **SVG** | Crisp at any zoom | Include `<title>` / `<desc>` for accessibility |
| Legends / swatches | **SVG** | Scales + prints well | Prefer programmatic legend when feasible |
| Thumbnails | **WebP** (fallback PNG) | Smaller file sizes | Use `srcset` for density/viewport |
| Scanned historical map snippets | WebP/PNG | Image-based source | Include date + source attribution in metadata |

### SVG rules (non-negotiable)
- Must include a valid `viewBox` so it scales correctly.  [oai_citation:1‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)
- Don’t bake huge raster images inside SVG.
- Keep strokes consistent; avoid hairlines that disappear on mobile.
- Add `<title>` and (when helpful) `<desc>` so assistive tech has context.  [oai_citation:2‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)

### Raster rules
- Prefer **WebP** for UI thumbnails where supported.
- Export at least `1x` and `2x` (or use responsive sizing).  [oai_citation:3‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)
- Use PNG if you need **hard edges + transparency**.
- Use JPEG/WebP for photo-like imagery (not common for cartographic symbols).

> [!NOTE]
> PNG is generally superior to GIF for single images; GIF is mainly relevant for animation.  [oai_citation:4‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)

---

## 🧭 Cartographic + UX checklist

This is the “make it readable and honest” list—especially for **historical** mapping.

### 🗺️ When creating a *map image* (not just an icon)
Include (as applicable):

- 🏷️ Title (what + where + when)
- 🧾 Data/source credit + authoring credit
- 🧭 Orientation (north arrow) if ambiguity exists
- 📏 Scale (scale bar or statement like “not to scale”)
- 🧩 Legend (symbols/colors explained)
- 🗓️ Date/timeframe (historical period must be explicit)
- 🌐 Projection/datum statement when it matters
- ⚠️ Uncertainty cues (approximate boundaries, contested areas, etc.)

This aligns with practical map design guidance that stresses documentation, reader accessibility, and the presence (or intentional omission) of key map elements.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 📱 Mobile-first readability
Digital maps are inseparable from mobile use patterns; assume small screens, fast interactions, and imperfect attention.  [oai_citation:6‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj)  
So:

- ✅ Avoid tiny labels in static images (or provide a zoomed crop)
- ✅ Prefer icons with strong silhouettes
- ✅ Keep legends short, scannable, and consistent

### 🎛️ Legends: prefer “data-driven”
If a legend is fundamentally “palette + names,” prefer representing it as structured data (JSON/YAML) and rendering it in UI—similar to how mapping UIs build legends from colors and class names.  [oai_citation:7‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-JVv3nbvtonX1HcpeERi9kV)

---

## 🧾 Provenance & metadata

KFM’s core principle: **no mystery layers**. Every illustration must be attributable, reproducible, and honest about what it represents.  [oai_citation:8‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj)

### ✅ Minimum metadata requirement (sidecar file)

For every non-trivial asset, add:

- `my-asset.svg`
- `my-asset.meta.json`

**Example: `thumb-tribal-territories-1854.meta.json`**
```json
{
  "id": "thumb-tribal-territories-1854",
  "title": "Tribal Territories (1854) - Thumbnail",
  "type": "thumbnail",
  "description": "Layer selector thumbnail for the 1854 tribal territories view.",
  "created_by": "KFM",
  "created_at": "2026-01-18",
  "updated_at": "2026-01-18",
  "theme_variants": ["light", "dark"],
  "source": {
    "kind": "derived",
    "inputs": [
      {
        "name": "Dataset / archival source name here",
        "license": "License or terms here",
        "citation": "Bibliographic citation here",
        "url": "https://example.org/source"
      }
    ],
    "tools": ["QGIS", "Inkscape", "svgo"]
  },
  "cartography": {
    "projection": "EPSG:4326",
    "generalization": "Generalized for thumbnail; not for measurement",
    "timeframe": "1854"
  },
  "accessibility": {
    "alt": "Thumbnail map preview showing tribal territories in 1854.",
    "decorative": false
  }
}
```

> [!TIP]
> If the asset is purely decorative (e.g., a background texture), set `"decorative": true` and use empty alt text in the UI.

### 📎 Evidence mindset (borrowed from our doc practices)
Treat map illustrations as “evidence artifacts”: they should be easy to trace, review, and update without guesswork.  [oai_citation:9‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

## 🌐 How to use in the web UI

### Responsive image example (raster thumb)
Use `srcset` + `sizes` so the browser picks the right image.  [oai_citation:10‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)

```html
<img
  src="/assets/media/illustrations/map/thumbs/thumb-tribal-territories-1854.webp"
  srcset="
    /assets/media/illustrations/map/thumbs/thumb-tribal-territories-1854.webp 1x,
    /assets/media/illustrations/map/thumbs/thumb-tribal-territories-1854@2x.webp 2x
  "
  sizes="(max-width: 600px) 160px, 240px"
  alt="Thumbnail map preview showing tribal territories in 1854."
  loading="lazy"
/>
```

### SVG usage example (icon)
```html
<img
  src="/assets/media/illustrations/map/icons/icon-trading-post.svg"
  alt="Trading post"
/>
```

> [!NOTE]
> For complex SVGs with meaningful content, ensure the SVG contains `<title>` / `<desc>` and is authored with accessibility in mind.  [oai_citation:11‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)

---

## 🧰 Add a new asset checklist

- [ ] Pick the right **type** (icon / legend / thumb / overlay)
- [ ] Export to the right **format** (SVG/WebP/PNG)
- [ ] Ensure **mobile readability**
- [ ] Add required **metadata** (`.meta.json`)
- [ ] Confirm **license/attribution** for any external inputs
- [ ] Optimize:
  - [ ] SVG: run through an optimizer (e.g., SVGO)
  - [ ] Raster: compress (WebP preferred) and include `@2x` if needed
- [ ] Verify in UI:
  - [ ] light/dark themes (if relevant)
  - [ ] small screen + HiDPI
  - [ ] accessibility (alt text, contrast, non-color cues)

---

## 🧠 Advanced: “Map UI” context (why these assets exist)

KFM’s broader mapping architecture includes modern web mapping stacks (e.g., MapLibre/Leaflet/Cesium) and structured geospatial data pipelines. These **illustrations** complement that system by improving comprehension and navigation.  [oai_citation:12‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)

---

## 📚 References

Project + domain references used to shape these conventions:

- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** (provenance-first principles)  [oai_citation:13‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj)  
- **Kansas-Frontier-Matrix – Open-Source Geospatial Historical Mapping Hub Design** (web mapping stack context)  [oai_citation:14‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)  
- **MARKDOWN_GUIDE v13** (evidence artifacts + documentation mindset)  [oai_citation:15‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)  
- **Making Maps: A Visual Guide to Map Design for GIS** (cartographic elements + layout hygiene)  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- **Mobile Mapping: Space, Cartography and the Digital** (mobile-first map realities)  [oai_citation:17‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj)  
- **Responsive Web Design with HTML5 and CSS3** (SVG + responsive image delivery)  [oai_citation:18‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)  
- **WebGL Programming Guide** (WebGL rendering context & constraints)  [oai_citation:19‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7quELMw4FrspPczB9Y3BTp)  
- **Python Geospatial Analysis Cookbook** (geospatial workflow context)  [oai_citation:20‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  
- **Archaeological 3D GIS** (3D/temporal GIS context)  [oai_citation:21‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  
- **Cloud-Based Remote Sensing with Google Earth Engine** (legend/UI patterns for maps)  [oai_citation:22‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-JVv3nbvtonX1HcpeERi9kV)  
- **Compressed Image File Formats (JPEG/PNG/GIF/…)** (format tradeoffs)  [oai_citation:23‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)  

---

💡 **Principle to keep:** If a map illustration implies a fact, it must be traceable, dated, and clearly scoped.
