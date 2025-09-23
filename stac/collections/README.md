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
| `base_maps.json` | USGS & state historical topo sheets (1880s–2000s) with georeferencing. |
| `vectors.json` | Boundaries, railroads, trails, PLSS, hydrology, treaty lands [oai_citation:4‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv). |
| `dem.json` | Kansas 1-m DEM & derivatives (slope, aspect, hillshade) [oai_citation:5‡Data resource analysis.pdf](file-service://file-GdS9Kcw7Xbfqpy4xwwdqWS). |
| `hillshade.json` | LiDAR-derived shaded relief overlays [oai_citation:6‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv). |
| `documents.json` | Archival texts linked to places (treaties, diaries, newspapers). |
| `events.json` | Historical events catalog (battles, floods, droughts, fires) [oai_citation:7‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-BgUSuffTiRq4qidye2sPwN). |

---

## Design Notes

- **Provenance**  
  Each Collection must document source URL, processing steps (e.g. georeferencing),
  and temporal coverage [oai_citation:8‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv) [oai_citation:9‡Data resource analysis.pdf](file-service://file-GdS9Kcw7Xbfqpy4xwwdqWS).

- **Audit Enhancements**  
  Future Collections should integrate:
  - Oral histories & Indigenous narratives [oai_citation:10‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-BgUSuffTiRq4qidye2sPwN).
  - Paleoclimate proxies (tree rings, pollen, drought indices).
  - Fire regimes, hydrology, and uncertainty ranges.

- **Cross-Linking**  
  Items reference Collections → Collections reference upstream datasets.  
  Example: A scanned 1894 topo sheet Item links to `base_maps.json`.

- **Visualization**  
  Collections power the time-slider and map UI (MapLibre / KML exports).  
  Each should support both web tile (COG/GeoJSON) and Earth (KML/KMZ) formats.

---

## Adding a New Collection

1. Create a new JSON file in this folder (follow STAC 1.0.0 schema).
2. Include:
   - `id`, `title`, `description`
   - `extent` (bbox + temporal)
   - `stac_extensions` if needed (e.g. `proj`, `version`)
   - `providers` with roles (host, processor, licensor)
   - `keywords`, `license`
3. Validate with `stac-validate` (Makefile target).
4. Submit via Pull Request with description + sources.

---

## References

- [STAC Spec 1.0.0](https://github.com/radiantearth/stac-spec)
- Kansas-Frontier-Matrix design documents [oai_citation:11‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv) [oai_citation:12‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-BgUSuffTiRq4qidye2sPwN) [oai_citation:13‡Data resource analysis.pdf](file-service://file-GdS9Kcw7Xbfqpy4xwwdqWS) [oai_citation:14‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB)

---

> **Tip:** Treat Collections as the **backbone catalog**. Items may come and go,
> but Collections anchor provenance, themes, and temporal coverage across the hub.
