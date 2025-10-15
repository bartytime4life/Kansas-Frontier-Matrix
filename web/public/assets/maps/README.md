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

```yaml
---
title: "KFM • Public Map Overlays (web/public/assets/maps/)"
version: "v1.5.0"
last_updated: "2025-10-14"
owners: ["@kfm-gis", "@kfm-data"]
tags: ["maps","raster","overlay","stac","gis","geospatial","mcp"]
license: "MIT"
semantic_alignment:
  - STAC 1.0
  - EPSG:4326 (WGS84)
  - WCAG 2.1 AA
---
````

---

## 🧭 Overview

The `web/public/assets/maps/` directory hosts **static raster and vector overlays** that bring Kansas’s geography and history to life within the **MapView** and **LayerControls** components.
It includes **historic USGS topographic maps**, **digitized treaty boundaries**, **hydrology networks**, and **environmental datasets** (e.g., floodplains, soil surveys, drought indices).

Each asset corresponds to a **STAC Item** defined in `data/stac/`, enabling reproducible linking between map layers, timeline data, and provenance sources.
All overlays are **georeferenced** to **EPSG:4326 (WGS84)** and optimized for web performance under the **Master Coder Protocol (MCP)** reproducibility framework.

> **Mission:** Fuse historical cartography and scientific data into accessible, verified geospatial storytelling.

---

## 🧱 Directory Structure

```text
web/public/assets/maps/
├── topo_1894_overlay.png          # Historic USGS topographic map (Larned, 1894)
├── topo_1905_overlay.png          # Historic USGS map (Fort Hays, 1905)
├── treaty_boundaries_outline.svg  # Vector outline of tribal treaty territories
├── hydrology_network_light.svg    # Simplified Kansas river and stream network
├── soil_survey_1967.png           # USDA NRCS Soil Survey overlay
├── floodplain_zones_1975.png      # Historic Kansas River floodplain map
├── drought_index_1936.png         # Dust Bowl drought index visualization
├── legend_treaty.png              # Legend for treaty boundary layers
├── legend_topo.png                # Legend for topographic overlays
└── README.md                      # This documentation file
```

---

## 🧩 Asset Categories

| File Type          | Description                                      | Format               | Use Case                            |
| :----------------- | :----------------------------------------------- | :------------------- | :---------------------------------- |
| **Raster Overlay** | Scanned historical maps or environmental rasters | PNG / WebP / GeoTIFF | Base map layers                     |
| **Vector Overlay** | Simplified thematic data (boundaries, hydrology) | SVG / GeoJSON        | Overlay outlines                    |
| **Legend Image**   | Descriptive reference for map interpretation     | PNG                  | Shown in LayerControls              |
| **Composite Map**  | Blended raster combinations                      | WebP                 | Visual storytelling / preview tiles |

---

## 🌍 Geospatial Standards

| Parameter       | Specification                                                 |
| :-------------- | :------------------------------------------------------------ |
| **Projection**  | WGS84 (EPSG:4326)                                             |
| **Resolution**  | 1–10 m/px optimized for web zoom (Z6–Z12)                     |
| **Compression** | PNG (8-bit lossless) / WebP (85% quality)                     |
| **Tile Size**   | 256×256 px (for tile generation)                              |
| **Alignment**   | Overlays aligned to Kansas state grid using QGIS verification |

**Example Metadata (`topo_1894_overlay.json`):**

```json
{
  "id": "topo_1894_overlay",
  "title": "USGS Topographic Map (Larned, 1894)",
  "type": "raster",
  "crs": "EPSG:4326",
  "spatial_extent": [-99.3, 38.1, -98.8, 38.5],
  "temporal_extent": { "start": "1894-01-01", "end": "1894-12-31" },
  "license": "Public Domain",
  "source": "USGS Historical Topographic Map Collection"
}
```

---

## 🗺️ Example Integration (MapLibre GL JS)

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

> These overlays are automatically registered within `LayerControls` via their STAC metadata definitions.

---

## 🧮 Optimization & Provenance

| Tool                 | Purpose                                       |
| :------------------- | :-------------------------------------------- |
| **GDAL**             | Georeferencing, coordinate reprojection       |
| **rio-cogeo**        | Conversion to Cloud-Optimized GeoTIFFs (COGs) |
| **MapTiler**         | Tile generation for large rasters             |
| **pngquant / cwebp** | Raster compression                            |
| **SVGO**             | Vector simplification and optimization        |
| **SHA256 Checksums** | Integrity verification for all map assets     |

Each overlay includes:

* A `.sha256` checksum for integrity
* A `.json` descriptor documenting source, license, and transformation process
* A `meta` tag referencing the dataset’s DOI or STAC ID

---

## ♿ Accessibility & Thematic Design

* **Colorblind-Safe Palettes:** Tested under Deuteranopia and Protanopia filters.
* **Legends:** Large sans-serif text (≥ 12pt) and labeled color ramps.
* **High Contrast:** Clear visibility on both light and dark map themes.
* **ARIA Labels:** Accessible titles and metadata surfaced in LayerControls.
* **Keyboard Navigation:** Focusable legends and toggle buttons for map overlays.

Accessibility validation is automated in CI using **axe-core** and **Lighthouse** scans.

---

## 🧾 Licensing & Attribution

| Map Overlay                     | Source                                     | License       | Attribution            |
| :------------------------------ | :----------------------------------------- | :------------ | :--------------------- |
| `topo_1894_overlay.png`         | USGS Historical Topographic Map Collection | Public Domain | U.S. Geological Survey |
| `treaty_boundaries_outline.svg` | Digitized by KFM Team                      | CC-BY 4.0     | Kansas Frontier Matrix |
| `soil_survey_1967.png`          | USDA NRCS Archive                          | Public Domain | NRCS / USDA            |
| `floodplain_zones_1975.png`     | FEMA Archive                               | Public Domain | FEMA                   |
| `drought_index_1936.png`        | NOAA NCEI Dataset                          | Public Domain | NOAA                   |
| `hydrology_network_light.svg`   | Derived from USGS NHD                      | CC-BY 4.0     | KFM Hydrology Team     |

All derivative works are cited and cross-referenced in the project’s **STAC metadata** for traceability.

---

## 🧪 Validation Workflow (CI/CD)

* ✅ Validate all map overlays against **STAC schema** via JSON Schema Validator
* ✅ Match filenames with dataset IDs in `data/stac/items/`
* ✅ Compute & compare checksums to detect data drift
* ✅ Generate 128×128 px previews for LayerControls & docs
* ✅ Publish validation logs as build artifacts for transparency

Validation results are archived under `ci/reports/map-validation/`.

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                        |
| :------------------ | :---------------------------------------------------- |
| Documentation-first | All geospatial overlays documented with metadata      |
| Provenance          | Source metadata + checksum in every file              |
| Reproducibility     | STAC-aligned descriptors ensure deterministic loading |
| Accessibility       | Colorblind & contrast-tested palettes                 |
| Open Standards      | EPSG:4326, STAC 1.0, GeoJSON, WebP                    |
| Auditability        | CI pipeline produces verifiable validation logs       |

---

## 🔗 Related Documentation

* **LayerControls Component** — `web/src/components/LayerControls/README.md`
* **MapView Component** — `web/src/components/MapView/README.md`
* **STAC Catalog Overview** — `data/stac/README.md`
* **Design Mockups — Maps** — `docs/design/mockups/maps/`
* **Web UI Architecture** — `web/ARCHITECTURE.md`

---

## 📜 License

All map overlays and derivative works created by the Kansas Frontier Matrix are released under the **MIT License**,
unless explicitly marked as **Public Domain** or **CC-BY 4.0** from their source archives.

© 2025 Kansas Frontier Matrix — produced under **MCP-DL v6.2** for **traceable**, **reproducible**, and **educational geospatial visualization**.

> *“Maps are memory etched on the land — these overlays reveal Kansas’s stories through time and terrain.”*

```
```
