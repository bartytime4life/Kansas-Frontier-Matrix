# STAC Collections — Kansas-Frontier-Matrix

This folder contains **STAC 1.0.0 Collection JSONs** that describe the major
geospatial and historical data groupings used by the Kansas-Frontier-Matrix
platform.

Each Collection provides:
- **ID**: stable identifier (used by Items to link back).
- **Title / Description**: plain-language overview of the dataset.
- **Extent**: spatial bbox + temporal range.
- **Providers**: source attribution (USGS, KGS, NOAA, tribal archives, etc.).
- **Keywords / Themes**: searchable tags (e.g. `treaties`, `railroads`, `hillshade`).
- **License**: public-domain / CC-BY / other.

Collections are modular: new layers (e.g. soils, oral histories, wildfire perimeters)
can be added incrementally.

---

## Current Collections

| File | Purpose |
|------|---------|
| `elevation.json` | Kansas DEMs and terrain derivatives (slope, aspect, hillshade). |
| `historic_topo.json` | USGS & state historic topographic sheets (1880s–2000s) with georeferencing. |
| `vectors.json` | Boundaries, railroads, trails, PLSS, hydrology, treaty lands ([Mapping Hub Design](../docs/Kansas-Frontier-Matrix_Design.pdf)). |
| `ks_kansas_river.json` | Kansas River — hydrography, floods (e.g. 1951), hazards, overlays. |

---

## Design Notes

- **Provenance**  
  Each Collection must document:
  - Source URL(s) and citation  
  - Processing steps (e.g. georeferencing, reprojection, COG conversion)  
  - Temporal coverage (open intervals `[null,null]` if spanning eras)  

- **Audit Enhancements**  
  Future Collections should integrate:
  - Oral histories & Indigenous narratives  
  - Paleoclimate proxies (tree rings, pollen, drought indices)  
  - Fire regimes, hydrology, and uncertainty ranges  

- **Cross-Linking**  
  Items → Collections → Root Catalog  
  - Example: A scanned 1894 topo sheet Item links to `historic_topo.json`.  
  - Example: A 1951 Kansas River flood overlay Item links to `ks_kansas_river.json`.  

- **Visualization**  
  Collections power the **time-slider** and map UI (MapLibre + KML/KMZ exports).  
  Each should support both **web tile formats** (COG, GeoJSON) and **Earth formats** (KML/KMZ).  

---

## Adding a New Collection

1. Create a new JSON file in this folder (follow STAC 1.0.0 schema).  
2. Include:  
   - `id`, `title`, `description`  
   - `extent` (bbox + temporal)  
   - `stac_extensions` if needed (e.g. `proj`, `version`)  
   - `providers` with roles (`host`, `processor`, `licensor`)  
   - `keywords`, `license`  
3. Validate with `make stac-validate` or `stac-validator`.  
4. Submit via Pull Request with description + sources.  

---

## References

- [STAC Spec 1.0.0](https://github.com/radiantearth/stac-spec)  
- Kansas-Frontier-Matrix design documents:  
  - *Open-Source Geospatial Historical Mapping Hub Design*  
  - *Design Audit – Gaps and Enhancement Opportunities*  
  - *Data Resource Analysis*  
  - *Historical Knowledge Hub System Design*  

---

> **Tip:** Collections are the **backbone catalog**. Items may come and go,
> but Collections anchor provenance, themes, and temporal coverage across the hub.
```

