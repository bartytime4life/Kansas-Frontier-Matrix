<div align="center">

# 🗺️ Kansas Frontier Matrix — **Public Map Overlays**  
`web/public/assets/maps/`

**Historic Maps · Overlays · Geospatial Rasters**

[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../../docs/)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../.github/workflows/stac-validate.yml)
[![Accessibility](https://img.shields.io/badge/WCAG%202.1-AA-yellow)](../../../../docs/design/reviews/accessibility/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../LICENSE)

</div>

---

## 🧭 Overview

`web/public/assets/maps/` hosts **static raster/vector overlays** used by **MapView** and **LayerControls** to weave Kansas’s geography with time-aware narratives: USGS topographic scans, treaty boundaries, hydrology networks, soil/flood/drought layers, and more.  
Each overlay is paired to a **STAC Item** (`data/stac/items/*`), ensuring **provenance**, **reproducibility**, and **timeline alignment** under **MCP-DL v6.2**.

> *Mission: fuse historical cartography and scientific data into verifiable geospatial storytelling.*

---

## 🧱 Directory Structure

```text
web/public/assets/maps/
├── topo_1894_overlay.png            # USGS historic topographic (Larned, 1894)
├── topo_1905_overlay.png            # USGS historic topographic (Fort Hays, 1905)
├── treaty_boundaries_outline.svg    # Digitized treaty territories
├── hydrology_network_light.svg      # Simplified rivers/streams
├── soil_survey_1967.png             # USDA NRCS soil survey overlay
├── floodplain_zones_1975.png        # Kansas River floodplain map (historic)
├── drought_index_1936.png           # Dust Bowl drought index visualization
├── legend_treaty.png                # Treaty boundary legend
├── legend_topo.png                  # Topographic legend
└── README.md
```

---

## 🧩 Asset Categories

| Type                | Description                                   | Formats                   | Primary Use                    |
| :------------------ | :-------------------------------------------- | :------------------------ | :----------------------------- |
| **Raster Overlays** | Scanned maps & environmental rasters          | PNG / WebP / (COG source) | Base narrative layers          |
| **Vector Overlays** | Simplified thematic boundaries/networks       | SVG / GeoJSON             | Crisp outlines & labels        |
| **Legend Images**   | Visual reference for interpretation           | PNG                       | LayerControls + docs           |
| **Previews**        | Small thumbnails for UI cards                  | PNG/WebP (≤ 256 px)       | Quick browsing & selection     |

---

## 🌍 Geospatial Standards

| Parameter         | Spec / Guidance                                                                 |
| :---------------- | :------------------------------------------------------------------------------ |
| **CRS**           | WGS84 — **EPSG:4326**                                                           |
| **Resolution**    | 1–10 m/px, tuned for zoom levels Z6–Z12                                        |
| **Compression**   | PNG (lossless, 8-bit) / WebP (~85% quality)                                    |
| **Tiling (opt.)** | 256×256 tiles when pre-tiled; otherwise direct raster load                     |
| **Alignment**     | Verified against Kansas grid & reference control points (QGIS + GDAL)          |

**Example Overlay Descriptor (`topo_1894_overlay.json`):**
```json
{
  "id": "topo_1894_overlay",
  "title": "USGS Topographic Map (Larned, 1894)",
  "type": "raster",
  "crs": "EPSG:4326",
  "spatial_extent": [-99.3, 38.1, -98.8, 38.5],
  "temporal_extent": { "start": "1894-01-01", "end": "1894-12-31" },
  "license": "Public Domain",
  "source": "USGS Historical Topographic Map Collection",
  "stac_id": "kfm-topo-1894-larned"
}
```

---

## 🗺️ MapLibre Integration (reference)

```js
map.addSource("topo1894", {
  type: "raster",
  tiles: ["/assets/maps/topo_1894_overlay.png"],
  tileSize: 256
});

map.addLayer({
  id: "topo1894-layer",
  type: "raster",
  source: "topo1894",
  paint: { "raster-opacity": 0.8 }
});
```

> In production, overlays are **registered via STAC → `layers.json`** then toggled by **LayerControls**.

---

## 🧮 Optimization & Provenance

| Tool / Step         | Purpose                                             |
| :------------------ | :-------------------------------------------------- |
| **GDAL**            | Georeferencing & reprojection                       |
| **rio-cogeo**       | Convert masters to **Cloud-Optimized GeoTIFFs**     |
| **MapTiler**        | Pre-generate tiles for very large rasters           |
| **pngquant / cwebp**| Compress rasters                                    |
| **SVGO**            | Minify vectors; preserve `<metadata>` for licensing |
| **SHA-256**         | Per-file integrity checks (`*.sha256`)              |

Each asset ships with:
- a **checksum** (`.sha256`)  
- a **descriptor** (`.json`) with source, license, and processing notes  
- a **STAC Item** binding (`data/stac/items/*`) for deterministic loading

---

## ♿ Accessibility & Thematic Design

- **Colorblind-safe** palettes validated (deuteranopia/protanopia).  
- **Legends** use ≥ 12 pt sans-serif labels; ramps labeled with units.  
- **High contrast** on light/dark map themes; tokens from Design System.  
- **ARIA**: legends and layer toggles labelled in **LayerControls**.  
- **Keyboard**: focusable controls; no pointer-only affordances.

Automated checks: **axe-core** + **Lighthouse** in CI.

---

## 🧾 Licensing & Attribution

| Overlay                        | Source                                  | License        | Attribution                 |
| :----------------------------- | :--------------------------------------- | :------------- | :-------------------------- |
| `topo_1894_overlay.png`        | USGS Historic Topo Collection            | Public Domain  | U.S. Geological Survey      |
| `treaty_boundaries_outline.svg`| Digitized by KFM                         | CC-BY 4.0      | Kansas Frontier Matrix      |
| `soil_survey_1967.png`         | USDA NRCS Archive                        | Public Domain  | NRCS / USDA                 |
| `floodplain_zones_1975.png`    | FEMA Archive                              | Public Domain  | FEMA                        |
| `drought_index_1936.png`       | NOAA NCEI                                | Public Domain  | NOAA                        |
| `hydrology_network_light.svg`  | Derived from USGS NHD (generalized)      | CC-BY 4.0      | KFM Hydrology Team          |

All derivative works are cross-referenced in **STAC** for full traceability.

---

## 🧪 Validation Workflow (CI)

- ✅ Validate STAC descriptors (JSON Schema)  
- ✅ Ensure filenames ↔ STAC `id` parity  
- ✅ Verify checksums; block drift on mismatch  
- ✅ Generate 128×128 previews for UI/docs  
- ✅ Publish validation logs to `ci/reports/map-validation/`

---

## 🧠 MCP Compliance Checklist

| Principle           | Implementation                                           |
| :------------------ | :------------------------------------------------------- |
| Documentation-first | Per-asset descriptors & this README                      |
| Provenance          | Source + license + process notes + checksum              |
| Reproducibility     | STAC-aligned items and deterministic layer configs       |
| Accessibility       | Colorblind-tested legends; WCAG-oriented tokens          |
| Open Standards      | EPSG:4326 · STAC 1.0 · GeoJSON · WebP/PNG                |
| Auditability        | CI artifacts: schema reports, checksums, thumbnails      |

---

## 🔗 Related Documentation

- **LayerControls** — `web/src/components/LayerControls/README.md`  
- **MapView** — `web/src/components/MapView/README.md`  
- **STAC Catalog** — `data/stac/README.md`  
- **Design — Maps** — `docs/design/mockups/maps/`  
- **Web Architecture** — `web/ARCHITECTURE.md`

---

## 🧾 Versioning & Metadata

| Field | Value |
| :---- | :---- |
| **Version** | `v1.6.0` |
| **Codename** | *Historic Layers & STAC Binding Upgrade* |
| **Last Updated** | 2025-10-17 |
| **Maintainers** | @kfm-gis · @kfm-data |
| **License** | MIT (docs/packaging) · Public Domain / CC-BY 4.0 as noted on assets |
| **Alignment** | STAC 1.0 · EPSG:4326 · WCAG 2.1 AA |
| **Maturity** | Stable / Production |

---

## 📜 License

KFM-generated overlays are **MIT** unless marked otherwise; third-party assets retain their published **Public Domain**/**CC-BY 4.0** licenses.  
© 2025 Kansas Frontier Matrix — produced under **MCP-DL v6.2** for **traceable**, **reproducible**, and **educational** geospatial visualization.

> *“Maps are memory etched on the land—these overlays surface Kansas’s stories through time and terrain.”*
