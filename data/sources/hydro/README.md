Here’s a structured `data/sources/hydro/README.md` tailored for your Kansas-Frontier-Matrix repo. It captures both **surface water and groundwater** sources, aligns with your STAC/MCP design, and notes key Kansas-specific datasets.

```markdown
# Kansas-Frontier-Matrix — Hydrology & Water Resources Sources

This directory catalogs **hydrological datasets** for Kansas.  
Layers include rivers, streams, lakes, wetlands, aquifers, and water-quality records.  
These datasets are essential for analyzing **settlement patterns, hazards (floods/droughts), and environmental change**.

---

## Purpose

- Represent **surface water networks** (streams, rivers, reservoirs, wetlands).  
- Integrate **groundwater and aquifer extents** (e.g., High Plains/Ogallala).  
- Link hydrology to **historical events** (floods, irrigation projects, treaties).  
- Provide **baseline water-quality and monitoring data** (KDHE, USGS).  
- Enable **time-aware visualization** (pre-dam vs. post-dam river courses, floodplains).

---

## Directory Layout

```

data/sources/hydro/
├── rivers\_streams.json        # National Hydrography Dataset (NHD, Kansas subset)
├── lakes\_reservoirs.json      # USACE & KDHE reservoir/lake polygons
├── wetlands.json              # National Wetlands Inventory (Kansas subset)
├── aquifers.json              # USGS/KGS aquifer extents (Ogallala, Equus Beds, etc.)
├── groundwater\_levels.json    # KGS monitoring wells
├── water\_quality.json         # KDHE stream & lake monitoring sites
├── scans/                     # Historical river/flood maps (scanned)
├── vectors/                   # Processed shapefiles/GeoJSON layers
└── README.md                  # This file

````

---

## Metadata Schema

Each dataset config follows the **STAC-like JSON template**:

```json
{
  "id": "rivers_streams",
  "title": "Kansas Rivers and Streams (NHD Subset)",
  "type": "vector",
  "version": "1.0.0",
  "description": "Stream and river centerlines from the USGS National Hydrography Dataset (NHD), clipped to Kansas. Includes flowlines, waterbody polygons, and attributes for stream order and perennial/intermittent flow.",
  "temporal": {
    "start": null,
    "end": "2025-01-01"
  },
  "spatial": {
    "bbox": [-102.05, 36.99, -94.61, 40.00]
  },
  "endpoints": [
    {
      "type": "http",
      "role": ["source"],
      "urls": [
        "https://prd-tnm.s3.amazonaws.com/NHD/HU4/0108/NHD_H_0108_GDB.zip"
      ]
    }
  ],
  "lineage": [
    "Fetched from USGS NHD",
    "Clipped to Kansas",
    "Converted to GeoJSON"
  ],
  "license": "public-domain",
  "provenance": {
    "retrieved": "2025-09-21",
    "checksum_sha256": "placeholder123...",
    "filesize_bytes": null
  },
  "keywords": ["hydrology", "rivers", "streams", "Kansas"],
  "confidence": "high"
}
````

---

## Recommended Hydrology Sources

* **Surface Water**

  * USGS **National Hydrography Dataset (NHD)** — rivers, streams, lakes
  * **National Wetlands Inventory (NWI)** — wetlands polygons
  * **USACE & KDHE Reservoir Data** — major dams/lakes (Tuttle Creek, Cheney, Milford, etc.)
  * FEMA **Flood Insurance Rate Maps (FIRM)** — historical + modeled floodplains

* **Groundwater**

  * USGS/KGS **Aquifer Extents** (Ogallala, Equus Beds, Great Bend Prairie)
  * KGS **Groundwater-Level Monitoring Wells** (time series)
  * DWR/USGS **Water Use Reports** (irrigation, municipal, industrial)

* **Water Quality**

  * **KDHE Surface Water Monitoring Program** (327 stream stations, 175 lakes)
  * EPA/STORET **Water Quality Portal** — chemistry, nutrients, HABs

---

## Integration Notes

* **Timeline-aware:** mark river modifications (reservoirs built, channels straightened).
* **Historical floods:** link 1951 Great Flood, 1903 Kaw River flood, 1993 Midwest Flood to FEMA/NOAA records.
* **Aquifer depletion:** tie groundwater declines (Ogallala post-1950) to land-use changes.
* Use **provenance registry** (`data/provenance/registry.json`) to track file checksums and fetch dates.

---

## References

* [USGS National Hydrography Dataset](https://www.usgs.gov/national-hydrography)
* [Kansas GIS Data Portal – Hydrology Layers](https://hub.kansasgis.org/)
* [Kansas Geological Survey – Groundwater Data](https://www.kgs.ku.edu/)
* [KDHE Water Quality Monitoring Strategy 2019–2028](https://www.kdhe.ks.gov/)&#x20;
* [FEMA Flood Insurance Maps](https://msc.fema.gov/portal/home)

---

```

---

Would you like me to also **pre-build JSON configs** for `aquifers.json` and `lakes_reservoirs.json` (with example endpoints and lineage), so you have working hydrology layers ready to plug into the STAC catalog?
```

