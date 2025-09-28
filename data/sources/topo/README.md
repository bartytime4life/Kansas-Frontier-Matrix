# Kansas-Frontier-Matrix — Topographic & Elevation Sources

This directory catalogs **topographic and elevation-related datasets** for Kansas.
It includes **historic USGS topo maps**, **digital elevation models (DEMs)**,
and **derived terrain layers** (hillshade, slope, aspect). These layers are foundational
for understanding how terrain shaped **settlement, trails, military campaigns,
hydrology, and agriculture**.

---

## Purpose

* Provide **baseline terrain context** (DEM, contours, shaded relief).
* Preserve **historic USGS topo sheets** (19th–20th century, multiple editions).
* Enable **temporal comparisons** (historic topo vs. modern DEM).
* Support **hydrology, soils, and land-use overlays** with terrain backdrops.
* Link terrain data to **migration routes, forts, flood events, and Dust Bowl studies**.

---

## Directory Layout

```
data/sources/topo/
├── usgs_historic_topo.json   # Historic USGS topographic map scans (GeoTIFF/COG)
├── ks_dem.json               # Kansas statewide DEM (1m LiDAR, 10m USGS NED)
├── hillshade.json            # Hillshade overlays (LiDAR-derived, statewide)
├── contours.json             # Derived contours from DEM
├── scans/                    # Raw scanned topo maps (GeoTIFF, MrSID, PDF)
├── vectors/                  # Contour shapefiles/GeoJSON
└── README.md                 # This file
```

---

## Metadata Schema

Datasets follow the **STAC-like JSON schema** (id, type, endpoints, temporal, spatial, provenance):

```json
{
  "id": "usgs_historic_topo",
  "title": "USGS Historical Topographic Maps (Kansas)",
  "type": "raster",
  "version": "1.0.0",
  "description": "Georeferenced scans of historic USGS topo maps (1880s–2000s), clipped to Kansas. Includes 15', 7.5', and 1:24k series. Useful for tracing settlement, railroads, hydrology changes, and land use evolution.",
  "temporal": { "start": "1880-01-01", "end": "2000-12-31" },
  "spatial": { "bbox": [-102.05, 36.99, -94.61, 40.00] },
  "endpoints": [
    {
      "type": "http",
      "role": ["source"],
      "urls": [
        "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/"
      ]
    }
  ],
  "lineage": [
    "Fetched from USGS Historical Topo Map Collection",
    "Converted to Cloud-Optimized GeoTIFF (COG)",
    "Clipped to Kansas boundary"
  ],
  "license": "public-domain",
  "provenance": {
    "retrieved": "2025-09-21",
    "checksum_sha256": "placeholder123...",
    "filesize_bytes": null
  },
  "keywords": ["topographic", "USGS", "Kansas", "historic maps", "terrain"],
  "confidence": "high"
}
```

---

## Recommended Topo & Elevation Sources

* **Historic Topographic Maps**

  * USGS **Historical Topo Map Collection** (GeoTIFF, 1880s–2000s).
  * Kansas GIS Archive — county topo sheets, plats.

* **Digital Elevation Models (DEM)**

  * **USGS 3DEP** 10m DEM (nationwide).
  * Kansas 1m LiDAR DEM (KARS / DASC).

* **Derived Terrain Products**

  * Hillshade, slope, aspect, roughness (from DEM).
  * Contours (10–50 ft intervals, county/statewide).

---

## Integration Notes

* **Time-aware topo layers**: Historic sheets are tagged by survey/publication year.
* **DEM → derivatives**: Run `make terrain` to generate slope, aspect, TRI/TPI.
* **Georeferencing**: Scanned sheets rectified to WGS84 EPSG:4326 for consistency.
* **Cross-links**:

  * **Trails & forts** align to ridges, rivers, passes.
  * **Dust Bowl** overlays require slope/erosion factors.
  * **Flood studies** integrate DEM + hydrology (see `data/processed/hydrology/`).

---

## Best Practices

* Store **raw scans** in `scans/` (GeoTIFF/MrSID, unmodified).
* Convert to **COGs** for web tiling (`rio cogeo create …`).
* For vectors (contours, boundaries), standardize to **GeoJSON EPSG:4326**.
* Update checksums in `data/provenance/registry.json`.
* Always include **temporal attributes** (survey year, edition).

---

## References

* [USGS Historical Topographic Map Collection](https://www.usgs.gov/programs/national-geospatial-program/historical-topographic-maps-preserving-past) 
* [Kansas GIS Archive Hub – Historical Datasets](https://archive-gis-data-ksdot.hub.arcgis.com/) 
* [Kansas Data Access & Support Center (DASC)](https://data.kansasgis.org/)
* [USGS 3DEP (National DEM)](https://www.usgs.gov/3d-elevation-program)

---

