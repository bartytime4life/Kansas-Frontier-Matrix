# Kansas-Frontier-Matrix — Land, Soils & Cadastral Sources

This directory catalogs **land-related datasets** for Kansas, including cadastral parcels,
Public Land Survey System (PLSS) grids, soil surveys, and land-cover/land-use maps.
These layers document how land was divided, classified, and managed over time —
from **tribal land cessions → township/range surveys → farms and parcels**.

---

## Purpose

* Provide **historical and modern cadastral context** (PLSS, parcels).
* Track **land cover/land use change** (grassland → agriculture → urban).
* Integrate **soil surveys, fertility, and erosion data** into environmental analysis.
* Link land datasets to **treaties, settlement patterns, and agricultural expansion**.
* Enable **timeline visualization** of land transformation.
* Support **AI-driven correlations** between land data and climate, hydrology, or social records.

---

## Directory Layout

```
data/sources/land/
├── plss.json                 # Public Land Survey System (township, range, section grids)
├── parcels.json              # Modern cadastral parcels (select counties, as available)
├── soils_ssurgo.json         # USDA NRCS SSURGO soil surveys
├── landcover_nlcd.json       # NLCD land cover (1992–present)
├── landcover_historic.json   # Historic vegetation/land use reconstructions
├── scans/                    # Scanned cadastral plats, atlases, early surveys
├── vectors/                  # Processed shapefiles/GeoJSON
└── README.md                 # This file
```

---

## Metadata Schema

Each dataset follows the **STAC-like schema** with provenance and lineage:

```json
{
  "id": "plss",
  "title": "Public Land Survey System (Kansas PLSS Grid)",
  "type": "vector",
  "version": "1.0.0",
  "description": "Township, range, and section boundaries from BLM PLSS data, clipped to Kansas. Useful for georeferencing historical plats, deeds, and surveys.",
  "temporal": { "start": "1854-01-01", "end": "2025-01-01" },
  "spatial": { "bbox": [-102.05, 36.99, -94.61, 40.00] },
  "endpoints": [
    {
      "type": "http",
      "role": ["source"],
      "urls": [
        "https://gis.blm.gov/arcgis/rest/services/lands/PLSS/MapServer"
      ]
    }
  ],
  "lineage": [
    "Fetched from BLM PLSS dataset",
    "Clipped to Kansas extent",
    "Converted to GeoJSON for integration"
  ],
  "license": "public-domain",
  "provenance": {
    "retrieved": "2025-09-21",
    "checksum_sha256": "placeholder123...",
    "filesize_bytes": null
  },
  "keywords": ["PLSS", "cadastral", "township", "range", "Kansas"],
  "confidence": "high"
}
```

---

## Recommended Land Sources

* **Cadastral / PLSS**

  * BLM **PLSS Data** — township, range, section grids.
  * County-level cadastral parcels (KS GIS Hub, county assessors).
  * Register of Deeds archives (historic tract books, title chains).

* **Soils**

  * USDA **NRCS SSURGO Database** — detailed soil surveys.
  * USDA **STATSGO2** — generalized soils, for statewide analysis.
  * Kansas Geological Survey core records and erosion studies.

* **Land Cover / Land Use**

  * **NLCD (1992–2021)** — 30m land cover classifications.
  * **Kansas GAP (2001)** — ecological land cover map.
  * **Kansas Ecological Systems Map (2017–18, Sentinel-2)** — 10m classes.
  * **Historic reconstructions** — early vegetation maps, county atlases.

* **Historical Atlases & Plats**

  * Kansas Historical Society — county plat books, landowner atlases.
  * Library of Congress — cadastral plats & atlases.
  * Digitized scans via Kansas GIS Archive Hub.

---

## Integration Notes

* **Timeline support**:

  * PLSS grid (1850s–present).
  * Parcels with temporal attributes (owner, year).
  * Land-cover datasets (1992+, plus historic vegetation).

* **Soil surveys** tie directly to **settlement + agriculture expansion** narratives.

* **Historic plats** (scanned) can be georeferenced with `data/gcp/*.yml`.

* **AI modules**: entity linking aligns land units with treaties, disasters, or diaries.

* Tag all layers with **confidence flags** where coverage is incomplete.

---

## Best Practices

* Keep **raw scans** in `scans/` and digitized vectors in `vectors/`.
* Update **checksums** in `data/provenance/registry.json`.
* Harmonize coordinate systems: store in EPSG:4326 for web, retain originals for precision.
* Cross-link to **treaties and tribal cessions** (land cessions → PLSS → parcels).
* Record **uncertainty metadata** (confidence scores, alignment errors).

---

## Advanced Concepts

* **Predictive modeling**: simulate land-use trajectories under drought/fire scenarios.
* **Fractal analysis**: test for self-similar patterns in settlement clusters or parcel divisions.
* **Geoarchaeology integration**: soil cores + land use overlays to distinguish human vs natural change.
* **Story-mapping**: connect parcels and plats to human narratives (settler diaries, tribal oral histories).

---

## References

* [BLM PLSS Data](https://gis.blm.gov/arcgis/rest/services/lands/PLSS/MapServer)
* [Kansas GIS Data Portal](https://hub.kansasgis.org/)
* [Kansas GIS Archive Hub](https://archive-gis-data-ksdot.hub.arcgis.com) 
* [USDA NRCS SSURGO](https://sdmdataaccess.sc.egov.usda.gov/)
* [Kansas GAP Analysis Land Cover Map (2001)]
* [Kansas Ecological Systems Map (2017–18, Sentinel-2)]
* [Kansas Geological Survey Core Library](https://www.kgs.ku.edu/Magellan/CoreLibrary/index.html) 
* [Kansas Historical Society – County Plat Maps](https://www.kshs.org/)

---
