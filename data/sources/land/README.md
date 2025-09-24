# Kansas-Frontier-Matrix — Land, Soils & Cadastral Sources

This directory catalogs **land-related datasets** for Kansas, including cadastral parcels,  
Public Land Survey System (PLSS) grids, soil surveys, and land-cover/land-use maps.  
These layers document how land was divided, classified, and managed over time —  
from **tribal land cessions → township/range surveys → farms and parcels**.

---

## Purpose

- Provide **historical and modern cadastral context** (PLSS, parcels).  
- Track **land cover/land use change** (grassland → agriculture → urban).  
- Integrate **soil surveys and fertility data** into environmental analysis.  
- Link land datasets to **treaties, settlement patterns, and agricultural expansion**.  
- Enable **timeline visualization** of land transformation.

---

## Directory Layout

```

data/sources/land/
├── plss.json                 # Public Land Survey System (township, range, section grids)
├── parcels.json              # Modern cadastral parcels (select counties, as available)
├── soils\_ssurgo.json         # USDA NRCS SSURGO soil surveys
├── landcover\_nlcd.json       # NLCD land cover (1992–present)
├── landcover\_historic.json   # Historic vegetation/land use reconstructions
├── scans/                    # Scanned cadastral plats, atlases, early surveys
├── vectors/                  # Processed shapefiles/GeoJSON
└── README.md                 # This file

````

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
````

---

## Recommended Land Sources

* **Cadastral / PLSS**

  * BLM **PLSS Data** — township, range, section grids.
  * County-level cadastral parcels (KS GIS Hub, county assessors).

* **Soils**

  * USDA **NRCS SSURGO Database** — detailed soil surveys.
  * USDA **STATSGO2** — generalized soils, for statewide analysis.

* **Land Cover / Land Use**

  * **NLCD (1992–2021)** — 30m land cover classifications (cropland, grassland, urban).
  * **Kansas GAP (2001)** — ecological land cover map.
  * **Kansas Ecological Systems Map (2017–18, Sentinel-2)** — 10m classes.
  * **Historic reconstructions** — early vegetation maps, county atlases.

* **Historical Atlases & Plats**

  * Kansas Historical Society — county plat books, landowner atlases.
  * Library of Congress — cadastral plats & atlases.

---

## Integration Notes

* **Timeline support:**

  * PLSS grid (1850s–present).
  * Parcels with temporal attributes (owner, year).
  * Land-cover datasets (1992+, plus historic vegetation).

* **Soil surveys** link to **settlement + agriculture expansion** narratives.

* **Historic plats** (scanned) can be georeferenced with `data/gcp/*.yml`.

* Tag all layers with **confidence flags** where coverage is incomplete.

---

## Best Practices

* Keep **raw scans** in `scans/` and digitized vectors in `vectors/`.
* Update **checksums** in `data/provenance/registry.json`.
* Harmonize coordinate systems: store in EPSG:4326 for web, retain originals for precision.
* Cross-link to **treaties** (land cessions → PLSS surveys → parcels).

---

## References

* [BLM PLSS Data](https://gis.blm.gov/arcgis/rest/services/lands/PLSS/MapServer)
* [Kansas GIS Data Portal](https://hub.kansasgis.org/)
* [USDA NRCS SSURGO](https://sdmdataaccess.sc.egov.usda.gov/)
* [Kansas GAP Analysis Land Cover Map (2001)]: contentReference[oaicite:5]{index=5}
* [Kansas Ecological Systems Map (2017–18, Sentinel-2)]: contentReference[oaicite:6]{index=6}
* [Kansas Historical Society – County Plat Maps](https://www.kshs.org/)

---

