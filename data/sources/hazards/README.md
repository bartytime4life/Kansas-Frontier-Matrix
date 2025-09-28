# Kansas-Frontier-Matrix — Hazards & Disasters Sources

This directory catalogs **hazard and disaster datasets** for Kansas.  
Layers include tornadoes, floods, droughts, wildfires, severe storms,  
and FEMA-declared disasters. These datasets allow **historical risk analysis**  
and link environmental events to **timelines, places, and documents**  
in the Kansas-Frontier-Matrix knowledge hub.

---

## Purpose

- Track **hazard events** (tornadoes, droughts, floods, wildfires, storms).  
- Provide **geospatial layers** (vectors, rasters, tabular CSVs) for analysis and visualization.  
- Link hazards to **documents and events** (e.g., Greensburg Tornado 2007).  
- Maintain **provenance, lineage, and licensing** per Master Coder Protocol.  
- Enable **cross-domain reasoning**: climate ↔ settlement ↔ environment.

---

## Directory Layout

```

data/sources/hazards/
├── tornado_tracks.json       # NOAA SPC tornado paths (1950–present)
├── severe_storms.json        # Hail / wind reports (1955–present)
├── fema_disasters.json       # FEMA declarations (1953–present)
├── drought_monitor.json      # US Drought Monitor (2000–present)
├── wildfire_perimeters.json  # NIFC & Kansas Forest Service polygons
├── scans/                    # Optional scanned maps / PDFs
├── vectors/                  # Converted shapefiles/GeoJSONs (processed)
└── README.md                 # This file

````

> **Note:** Large binaries (shapefiles, rasters) live in `data/raw/` (ignored)  
> or `data/processed/hazards/` (LFS). Only descriptors, checksums, and metadata  
> should be tracked here.

---

## Descriptor Schema

Each hazard dataset config (`.json` or `.yml`) must follow the  
**KFM Source Descriptor schema** (`data/sources/schema.source.json`). Example:

```json
{
  "id": "tornado_tracks",
  "title": "NOAA SPC Tornado Paths (1950–present)",
  "type": "vector",
  "description": "Line geometries representing tornado tracks across Kansas from 1950 to present, including EF scale, fatalities, and damage.",
  "period": "1950-2024",
  "bbox": [-102.05, 36.99, -94.61, 40.00],
  "urls": [
    "https://www.spc.noaa.gov/gis/svrgis/"
  ],
  "license": {
    "name": "Public Domain",
    "url": "https://www.spc.noaa.gov/gis/svrgis/"
  },
  "provenance": {
    "attribution": "NOAA Storm Prediction Center",
    "retrieved": "2025-09-21T00:00:00Z"
  },
  "keywords": ["tornado", "hazard", "Kansas", "SPC"]
}
````

Key rules:

* `bbox` always in EPSG:4326 (WGS84 lon/lat).
* `period` covers temporal range; STAC will use this for timeline queries.
* Always include `license` and `provenance`.
* `urls[]` may point to bulk shapefile zips, API endpoints, or feature services.

---

## Recommended Hazard Sources

* **NOAA Storm Events Database** — multi-hazard archive (1950–present)
* **NOAA SPC Severe Weather GIS** — tornado tracks, hail, wind reports
* **FEMA Disaster Declarations** — federal declarations by county/type (1953–present)
* **US Drought Monitor** — weekly drought polygons (2000–present)
* **NIFC Wildfire Perimeters** — large fire polygons (2000–present)
* **Kansas Forest Service** — state-specific wildfire perimeter datasets

---

## Integration Notes

* Hazards are **time-enabled**: descriptors must include start/end dates.
* **Tornadoes**: store as polylines with EF scale, path width, fatalities.
* **Drought**: polygons by category (D0–D4). Weekly snapshots form a time series.
* **Floods**: link FEMA declarations and NOAA Storm Events flood reports.
* **Wildfires**: polygons with ignition dates, acres, fire names.

Link hazards to **knowledge graph** entities:

* `Event` → e.g., “Greensburg Tornado 2007”
* `Place` → county, polygon, or watershed
* `Document` → newspaper articles, FEMA reports, NOAA Storm Data PDFs

---

## Best Practices

* Place **raw shapefiles/CSVs** in `data/raw/hazards/` (ignored).
* Place **converted GeoJSON/COGs** in `data/processed/hazards/` (LFS).
* Update **checksums (`*.sha256`)** and **fetch dates (`retrieved`)** after each pull.
* Use **confidence flags** if event geometries are incomplete.
* Verify **licensing compliance** (NOAA/NIFC/FEMA are public-domain; confirm Kansas Forest Service license).
* Normalize CRS → EPSG:4326 for viewer, but record source CRS in `_meta.json`.

---

## Debugging & Validation

* `make validate-sources` → schema validation of hazard descriptors.
* `make fetch` → downloads raw data to `data/raw/hazards/`.
* `make vectors` → converts shapefiles to GeoJSON.
* `make stac` → builds STAC Items/Collections for hazards.
* `make validate-stac` → ensures STAC compliance.
* `make checksums` → updates `.sha256` integrity files.

---

## References

* [NOAA Storm Events Database](https://www.ncei.noaa.gov/stormevents/)
* [NOAA SPC Severe Weather GIS](https://www.spc.noaa.gov/gis/svrgis/)
* [FEMA Disaster Declarations](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2)
* [US Drought Monitor GIS Data](https://droughtmonitor.unl.edu/DmData/GISData.aspx)
* [National Interagency Fire Center Open Data](https://data-nifc.opendata.arcgis.com/)
* [Kansas Forest Service Wildland Fire Perimeters](https://hub.kansasgis.org/)

---

✦ **Summary:**
`data/sources/hazards/` contains the **blueprints for hazard + disaster datasets**.
They guarantee that tornadoes, floods, droughts, wildfires, and FEMA disasters
are traceable, reproducible, and discoverable in the STAC catalog and linked into
the Kansas-Frontier-Matrix timeline + map viewer.

```
