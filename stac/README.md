# Kansas-Frontier-Matrix — STAC Catalog

This directory contains the **SpatioTemporal Asset Catalog (STAC) v1.0.0**  
for the Kansas-Frontier-Matrix project.  
It provides a machine-readable index of geospatial and historical assets —  
maps, imagery, vectors, documents, and derivative products — all wired into  
the project’s open-source Knowledge Hub [oai_citation:2‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).

---

## Purpose

- Ensure **provenance and reproducibility** of all geospatial assets.  
- Enable **time-aware queries** (maps, datasets, events across Kansas history).  
- Provide a **structured entry point** for pipelines (Makefile, CI, ingest).  
- Interconnect with the **Knowledge Graph** of events, people, and places [oai_citation:3‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).  
- Align with **MCP scientific method templates** for validation and uncertainty scoring [oai_citation:4‡Historical Dataset Integration for Kansas Frontier Matrix.pdf](file-service://file-EG371w17RJTzXWjXvqgsB6).  

---

## Layout

stac/
├── catalog.json             # Root STAC Catalog
├── collections/             # Collections of related assets
│   ├── basemaps.json        # e.g., topographic/quads
│   ├── vectors.json         # e.g., trails, treaties, railroads
│   ├── rasters.json         # e.g., DEMs, COGs, hillshades
│   └── historical_maps.json # e.g., scanned 19th c. sheets
└── items/                   # Individual items (assets)
├── LAWRENCE_1885.json   # Example georeferenced historic map
├── ks_1m_dem_2018.json  # Example raster DEM
└── usgs_topo_larned_1894.json

- **`catalog.json`** — Root catalog; points to collections.  
- **`collections/*.json`** — Defines thematic collections (basemaps, vectors, rasters, etc.).  
- **`items/*.json`** — Defines specific assets, with metadata, bbox, time range, and asset links.  

---

## Validation

Tests ensure conformance to STAC 1.0.0 and project-specific policies:

- `tests/test_stac.py` — schema checks (id, type, stac_version).  
- `tests/test_sources.py` — verifies linked source configs exist.  
- `tests/test_web.py` (planned) — ensures linked web assets exist before site build.  

Run from repo root:

```bash
pytest -q -k "stac"


⸻

Conventions
	•	IDs: Use uppercase for historic maps (e.g. LAWRENCE_1885), lowercase for derived rasters (e.g. ks_1m_dem_2018).
	•	Datetime fields: Use full RFC3339 where possible (YYYY-MM-DDTHH:MM:SSZ).
	•	BBox & Geometry: Ensure bbox encloses geometry exactly.
	•	Assets: Prefer COG (Cloud-Optimized GeoTIFF) and vector formats (GeoJSON, Shapefile).
	•	Licenses: Default to public-domain unless otherwise required.

⸻

Example: Item (LAWRENCE_1885)

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "LAWRENCE_1885",
  "collection": "historical_maps",
  "properties": {
    "datetime": "1885-01-01T00:00:00Z"
  },
  "bbox": [-95.3, 38.9, -95.1, 39.0],
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "assets": {
    "image": {
      "href": "../data/raw/ut_pcl/LAWRENCE_1885.jpg",
      "type": "image/jpeg",
      "roles": ["data"]
    }
  }
}


⸻

Integration
	•	Pipelines: Makefile targets validate and publish STAC before site build.
	•	Web Viewer: MapLibre time slider fetches assets from items/*.json.
	•	Knowledge Hub: Entities (places, events, people) are linked via STAC metadata ￼.
	•	CI/CD: .github/workflows/stac-validate.yml runs STAC validation automatically.

⸻

References
	•	STAC 1.0.0 Spec
	•	MCP design docs: [Scientific Method Protocols] ￼, [Knowledge Hub System Design] ￼
	•	Kansas-Frontier-Matrix [Design Audit & Mapping Hub] ￼

⸻
