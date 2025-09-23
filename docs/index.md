# Kansas Geo Timeline — **Time · Terrain · History**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validation](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](../LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)](../pyproject.toml)

A minimal **Google Earth + Web (GitHub Pages)** mapping system for Kansas elevation and historical layers.

- **Earth deliverables**: regionated **KML/KMZ** (progressive loading via NetworkLinks)  
- **Web app**: lightweight **MapLibre** viewer with a **time slider**  
- **Catalog**: **STAC 1.0.0** (Catalog → Collections → Items) for clean provenance  
- **Pipelines**: `Makefile` targets to **fetch → COG → derivatives (slope/aspect/hillshade) → site**  
- **CLI**: `kgt` (Kansas Geo Timeline) for STAC validation, listing, and web-config rendering  

> Start small (one county), then scale out. Keep STAC tight and versioned.

---

## 🌐 Live Demo

- **Web Viewer (MapLibre + Time Slider)** → [View Demo](https://bartytime4life.github.io/Kansas-Frontier-Matrix/web/)  
- **Google Earth KMZ (download)** → [Kansas_Terrain.kmz](https://bartytime4life.github.io/Kansas-Frontier-Matrix/earth/Kansas_Terrain.kmz)

---

## Pipeline Overview

```mermaid
flowchart TD
    A[Data Sources] -->|fetch| B[COGs (DEM, overlays)]
    B -->|terrain| C[Derivatives (slope, aspect, hillshade)]
    C -->|stac| D[STAC Catalog & Items]
    D -->|render-config| E[Web Viewer Config (app.config.json)]
    D -->|kml| F[KML/KMZ for Google Earth]
    E -->|serve| G[MapLibre Web Viewer]
    F --> H[Google Earth 3D]
