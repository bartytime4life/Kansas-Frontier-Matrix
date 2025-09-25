# Kansas-Frontier-Matrix — STAC Catalog

This directory contains the **SpatioTemporal Asset Catalog (STAC) v1.0.0**  
for the Kansas-Frontier-Matrix project.  
It provides a machine-readable index of geospatial and historical assets —  
maps, imagery, vectors, documents, and derivative products — all wired into  
the project’s open-source Knowledge Hub [Kansas Historical Knowledge Hub – System Design.pdf](../docs/Kansas%20Historical%20Knowledge%20Hub%20–%20System%20Design.pdf).

---

## Purpose

- Ensure **provenance and reproducibility** of all geospatial assets.  
- Enable **time-aware queries** (maps, datasets, events across Kansas history).  
- Provide a **structured entry point** for pipelines (`Makefile`, CI, ingest).  
- Interconnect with the **Knowledge Graph** of events, people, and places.  
- Align with **MCP scientific method templates** for validation and uncertainty scoring.  

---

## Layout

```

stac/
├── catalog.json                 # Root STAC Catalog
├── collections/                 # Collections of related assets
│   ├── elevation.json            # DEMs, LiDAR, terrain derivatives
│   ├── historic_topo.json        # USGS & related historic topographic sheets
│   ├── vectors.json              # Trails, treaties, railroads, infrastructure
│   └── ks_kansas_river.json      # Kansas River — Hydro, Floods, Historical Layers
└── items/                        # Individual items (assets)
├── LAWRENCE_1885.json        # Example georeferenced historic map
├── ks_1m_dem_2018.json       # Example DEM raster
├── usgs_topo_larned_1894.json# Example USGS topo sheet
└── ks_kansas_river_flood_1951.json # Example flood overlay (COG)

````

- **`catalog.json`** — Root catalog; points to thematic collections.  
- **`collections/*.json`** — Defines grouped assets (elevation, maps, vectors, rivers).  
- **`items/*.json`** — Defines specific assets, with metadata, bbox, time range, and asset links.  

---

## Validation

Automated tests ensure conformance to **STAC 1.0.0** and project-specific policies:

- `tests/test_stac.py` — schema checks (id, type, stac_version, bbox, datetime).  
- `tests/test_sources.py` — verifies linked source configs exist.  
- `tests/test_web.py` (planned) — ensures linked web assets exist before site build.  

Run from repo root:

```bash
pytest -q -k "stac"
````

---

## Conventions

* **IDs**:

  * Uppercase for historic maps (e.g., `LAWRENCE_1885`)
  * Lowercase for derived rasters (e.g., `ks_1m_dem_2018`)
  * Prefix by theme if needed (`ks_kansas_river_flood_1951`).
* **Datetime fields**:

  * Use RFC3339 (Zulu): `YYYY-MM-DDTHH:MM:SSZ`.
  * Use `start_datetime` / `end_datetime` for intervals.
* **BBox & Geometry**:

  * Ensure bbox encloses geometry exactly.
* **Assets**:

  * Prefer COG (Cloud-Optimized GeoTIFF) for rasters.
  * GeoJSON (WGS84) for vectors.
* **Licenses**:

  * Default to public domain (PDDL-1.0) unless otherwise required.
* **Links**:

  * Every collection links back to `../catalog.json` as `root` and `parent`.
  * Every item links to its `collection` and `../catalog.json`.

---

## Example Item — LAWRENCE_1885

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "LAWRENCE_1885",
  "collection": "historic_topo",
  "properties": {
    "datetime": "1885-01-01T00:00:00Z"
  },
  "bbox": [-95.3, 38.9, -95.1, 39.0],
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "assets": {
    "image": {
      "href": "../data/raw/ut_pcl/LAWRENCE_1885.jpg",
      "type": "image/jpeg",
      "roles": ["data"],
      "title": "Lawrence, Kansas (1885) historic map scan"
    }
  },
  "links": [
    { "rel": "collection", "href": "../collections/historic_topo.json", "type": "application/json" },
    { "rel": "root", "href": "../catalog.json", "type": "application/json" }
  ]
}
```

---

## Integration

* **Pipelines**:
  `make stac` builds/patches → `make stac-validate` ensures conformance before site build.
* **Web Viewer**:
  MapLibre + time slider auto-pulls from `items/*.json`.
* **Knowledge Hub**:
  Entities (places, events, people) linked via STAC metadata.
* **CI/CD**:
  `.github/workflows/stac-validate.yml` runs STAC validation on every push/PR.

---

## References

* [STAC 1.0.0 Specification](https://stacspec.org)
* Kansas Frontier Matrix design docs:

  * *Scientific Method Protocols*
  * *Knowledge Hub System Design*
  * *Historical Dataset Integration*
  * *Design Audit & Mapping Hub*

---

```

---

This version:
- Updates the **Layout** to match your current collections (adds `ks_kansas_river.json`).
- Fixes `items/` indentation and paths for clarity.
- Expands **Conventions** with explicit linking rules so navigation doesn’t break.
- Adds **Integration** notes tying STAC → Makefile → MapLibre → CI/CD.

