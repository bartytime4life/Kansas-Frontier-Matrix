# Kansas-Frontier-Matrix — Hazards & Disasters Sources

This directory catalogs **hazard and disaster datasets** for Kansas.  
Layers include tornadoes, floods, droughts, wildfires, severe storms,  
and FEMA-declared disasters. These datasets allow **historical risk analysis**  
and link environmental events to **timelines, places, and documents**  
in the Kansas-Frontier-Matrix knowledge hub.

---

## Purpose

- Track **hazard events** (tornadoes, droughts, floods, wildfires, storms).  
- Provide **geospatial layers** (vector shapefiles, GeoJSON, rasters) for analysis and visualization.  
- Link hazards to **documents and events** (e.g., Greensburg Tornado 2007).  
- Maintain **provenance, lineage, and licensing** per MCP protocol.  
- Enable **cross-domain reasoning**: climate ↔ settlement ↔ environment.

---

## Directory Layout

```

data/sources/hazards/
├── tornado\_tracks.json         # NOAA SPC tornado paths (1950–present)
├── severe\_storms.json          # Hail / wind reports (1955–present)
├── fema\_disasters.json         # FEMA declarations (1953–present)
├── drought\_monitor.json        # US Drought Monitor (2000–present)
├── wildfire\_perimeters.json    # NIFC & Kansas Wildland Fire polygons
├── scans/                      # Optional scanned maps / PDFs
├── vectors/                    # Converted shapefiles/GeoJSONs
└── README.md                   # This file

````

---

## Metadata Schema

Each hazard dataset config (`.json` or `.yml`) should follow the **STAC-like schema**:

```json
{
  "id": "tornado_tracks",
  "title": "NOAA SPC Tornado Paths (1950–present)",
  "type": "vector",
  "version": "1.0.0",
  "description": "Line geometries representing tornado tracks across Kansas from 1950 to present, including EF scale, fatalities, and damage.",
  "temporal": {
    "start": "1950-01-01",
    "end": "2024-12-31"
  },
  "spatial": {
    "bbox": [-102.05, 36.99, -94.61, 40.00]
  },
  "endpoints": [
    {
      "type": "http",
      "role": ["source"],
      "urls": [
        "http://www.spc.noaa.gov/gis/svrgis/"
      ]
    }
  ],
  "lineage": [
    "Fetched from NOAA SPC SVRGIS endpoint",
    "Clipped to Kansas bounding box",
    "Exported to GeoJSON"
  ],
  "license": "public-domain",
  "provenance": {
    "retrieved": "2025-09-21",
    "checksum_sha256": "placeholder123abc…",
    "filesize_bytes": null
  },
  "keywords": ["tornado", "SPC", "Kansas", "hazard"],
  "confidence": "high"
}
````

---

## Recommended Hazard Sources

* **NOAA Storm Events Database** — multi-hazard archive (1950–present)
* **NOAA SPC Severe Weather GIS** — tornado tracks, hail, wind reports
* **FEMA Disaster Declarations** — federal declarations by county, disaster type
* **US Drought Monitor** — weekly drought polygons (2000–present)
* **NIFC Wildfire Perimeters** — large fire polygons (2000–present)
* **Kansas Forest Service** — state-specific wildfire perimeter datasets

---

## Integration Notes

* Hazards are **time-enabled**: events must include start/end dates for timeline queries.
* **Tornadoes**: store as polylines with EF scale, path width, fatalities.
* **Drought**: polygons by category (D0–D4). Weekly snapshots form a time series.
* **Floods**: link FEMA declarations and NOAA Storm Data flood events.
* **Wildfires**: polygons with burn dates, acres, and fire names.
* Link hazards to **knowledge graph** nodes:

  * `Event` (e.g., “Greensburg Tornado 2007”)
  * `Place` (county or polygon)
  * `Document` (newspaper articles, FEMA PDFs)

---

## Best Practices

* Store **raw shapefiles/CSVs** under `data/raw/`, keep processed GeoJSON/COGs in `vectors/`.
* Always update **checksums** and **fetch dates** in `data/provenance/`.
* Use **confidence flags** if event data is incomplete (e.g., missing path geometry).
* Ensure **licensing compliance** (NOAA/NIFC/FEMA are public-domain; check state data licenses).

---

## References

* [NOAA Storm Events Database](https://www.ncei.noaa.gov/stormevents/)
* [NOAA SPC Severe Weather GIS](http://www.spc.noaa.gov/gis/svrgis/)
* [FEMA Disaster Declarations](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2)
* [US Drought Monitor GIS Data](https://droughtmonitor.unl.edu/DmData/GISData.aspx)
* [National Interagency Fire Center Open Data](https://www.drought.gov/data-maps-tools/wildland-fire-open-data)
* [Kansas Forest Service Wildland Fire Perimeters](https://hub.kansasgis.org/)

---
