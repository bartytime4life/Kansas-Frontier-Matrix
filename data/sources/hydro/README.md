# Kansas-Frontier-Matrix — Hydrology & Water Resources Sources

This directory catalogs **hydrological datasets** for Kansas.  
Layers include rivers, streams, lakes, wetlands, aquifers, and water-quality records.  
These datasets are essential for analyzing **settlement patterns, hazards (floods/droughts),  
and environmental change** across time.

---

## Purpose

- Represent **surface water networks** (streams, rivers, reservoirs, wetlands).  
- Integrate **groundwater and aquifer extents** (High Plains/Ogallala, Equus Beds, etc.).  
- Link hydrology to **historical events** (floods, irrigation projects, treaties).  
- Provide **baseline water-quality and monitoring data** (KDHE, USGS).  
- Enable **time-aware visualization** (pre-dam vs. post-dam river courses, floodplains).  
- Connect water data to **hazards** (floods, droughts, HABs) and **land use change**.

---

## Directory Layout

```

data/sources/hydro/
├── rivers_streams.json       # NHD flowlines & waterbody polygons
├── lakes_reservoirs.json     # USACE & KDHE reservoirs/lakes
├── wetlands.json             # USFWS NWI wetlands polygons
├── aquifers.json             # USGS/KGS aquifer extents
├── groundwater_levels.json   # KGS monitoring wells
├── water_quality.json        # KDHE stream & lake monitoring sites
├── scans/                    # Historical floodplain & river maps (scanned)
├── vectors/                  # Processed shapefiles/GeoJSON layers
└── README.md                 # This file

````

> **Note:** Large shapefiles and rasters live in `data/raw/hydro/` (ignored).  
> Only JSON descriptors, checksums, and metadata are tracked here.  
> Processed outputs (`data/processed/hydro/**`) are in Git LFS.

---

## Metadata Schema

Each dataset config must follow the  
**KFM Source Descriptor schema** (`data/sources/schema.source.json`). Example:

```json
{
  "id": "rivers_streams",
  "title": "Kansas Rivers and Streams (NHD Subset)",
  "type": "vector",
  "description": "Stream and river centerlines from the USGS National Hydrography Dataset (NHD), clipped to Kansas. Includes flowlines, waterbody polygons, stream order, and perennial/intermittent flow attributes.",
  "period": "current",
  "bbox": [-102.05, 36.99, -94.61, 40.00],
  "urls": [
    "https://prd-tnm.s3.amazonaws.com/NHD/HU4/0108/NHD_H_0108_GDB.zip"
  ],
  "license": {
    "name": "Public Domain",
    "url": "https://www.usgs.gov/national-hydrography"
  },
  "provenance": {
    "attribution": "USGS NHD",
    "retrieved": "2025-09-21T00:00:00Z"
  },
  "keywords": ["hydrology", "rivers", "streams", "Kansas"]
}
````

**Rules:**

* `bbox` always in EPSG:4326 (WGS84 lon/lat).
* `period` should be explicit (`YYYY`, `YYYY-YYYY`, `1930s`, or `current`).
* Always include `license` and `provenance`.
* `urls[]` may list multiple services, e.g. one per HUC or county.

---

## Recommended Hydrology Sources

### Surface Water

* USGS **National Hydrography Dataset (NHD)** — rivers, streams, lakes.
* USFWS **National Wetlands Inventory (NWI)** — wetlands polygons.
* USACE & KDHE **Reservoir Data** — major dams/lakes (Tuttle Creek, Cheney, Milford, etc.).
* FEMA **Flood Insurance Rate Maps (FIRM)** — historical + modeled floodplains.

### Groundwater

* USGS/KGS **Aquifer Extents** (Ogallala, Equus Beds, Great Bend Prairie).
* KGS **Groundwater-Level Monitoring Wells** (time series).
* DWR/USGS **Water Use Reports** (irrigation, municipal, industrial).

### Water Quality

* KDHE **Surface Water Monitoring Program** — 327 stream stations, 175 lakes.
* EPA/STORET **Water Quality Portal** — chemistry, nutrients, HABs.

---

## Integration Notes

* **Timeline-aware**: annotate reservoir construction and channel modifications.
* **Flood history**: link 1903, 1951, 1993 Kansas River floods to hazard datasets (NOAA/FEMA).
* **Aquifer depletion**: tie groundwater decline (post-1950 Ogallala) to irrigation expansion.
* **Cross-domain links**:

  * Hazards (`Event`: floods, droughts).
  * Settlements (`Place`: towns along rivers).
  * Documents (USACE reports, KDHE advisories).

---

## Best Practices

* Keep **raw shapefiles/GeoDBs** in `data/raw/` (ignored by git).
* Store **processed GeoJSON/COGs** in `data/processed/hydro/` (LFS).
* Update **checksums (`*.sha256`)** and **fetch dates** when refreshing data.
* Normalize to **EPSG:4326** for viewer; record original CRS in `_meta.json`.
* Use `make fetch hydro`, `make vectors`, and `make stac` for automation.
* Add `confidence` flags for incomplete datasets (e.g., wells with short records).

---

## Debugging & Validation

* `make validate-sources` → schema validation.
* `make fetch` → pulls shapefiles/GeoDBs.
* `make vectors` → converts to GeoJSON.
* `make stac` → rebuilds STAC Items for rivers, aquifers, etc.
* `make validate-stac` → ensures STAC compliance.
* `make checksums` → refresh integrity sidecars.

---

## References

* [USGS National Hydrography Dataset](https://www.usgs.gov/national-hydrography)
* [Kansas GIS Data Portal – Hydrology Layers](https://hub.kansasgis.org/)
* [Kansas Geological Survey – Groundwater Data](https://www.kgs.ku.edu/)
* [KDHE Water Quality Monitoring Strategy 2019–2028](https://www.kdhe.ks.gov/)
* [FEMA Flood Insurance Maps](https://msc.fema.gov/portal/home)

---

✦ **Summary:**
`data/sources/hydro/` contains descriptors for Kansas hydrology datasets — rivers, lakes, wetlands, aquifers, and water quality.
They ensure water resources are **traceable**, **timeline-aware**, and linked into the STAC catalog, hazards layers, and the Kansas-Frontier-Matrix knowledge graph.

```
