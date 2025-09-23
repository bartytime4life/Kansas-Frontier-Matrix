# STAC Items — Kansas-Frontier-Matrix

This folder contains **STAC 1.0.0 Item JSONs**.  
Each Item represents a single **spatiotemporal asset** (map, raster, vector, document, or event record) in the
Kansas-Frontier-Matrix catalog.

An Item is always linked to a **Collection** (`collection` field + `rel: collection` link).

---

## Item Structure

Each Item must include:

- **id** — unique identifier for the asset (e.g. `larned_topo_1894`, `hillshade_2018_2020`)
- **type** — always `"Feature"`
- **stac_version** — `"1.0.0"`
- **geometry** — footprint (Polygon) or point location
- **bbox** — bounding box `[west, south, east, north]`
- **properties**:
  - `datetime` (ISO 8601) or `start_datetime` / `end_datetime`
  - Optional: `proj:*` (CRS/transform), `raster:*` (bands), `checksum:multihash`
  - Thematic keys: `document:type`, `event:type`, etc.
- **assets** — dictionary of downloadable/visualizable files:
  - e.g. `cog`, `thumbnail`, `metadata`, `kml`
- **links**:
  - `rel: self` → this Item file
  - `rel: collection` → parent collection
  - `rel: root`/`parent` → `catalog.json`

---

## Examples

### Historical Map (Raster)
Item: `usgs_larned_1894.json`

- **Collection**: `base_maps`
- **Geometry**: footprint polygon from georeferencing GCPs
- **Properties**: `datetime: "1894-06-01T00:00:00Z"`
- **Assets**:
  - `cog` → Cloud-Optimized GeoTIFF
  - `thumbnail` → preview PNG
  - `kml` → regionated overlay for Google Earth

### Hillshade (DEM-derived)
Item: `hillshade_2018_2020.json`

- **Collection**: `hillshade`
- **Geometry**: full Kansas bbox
- **Properties**: `start_datetime: "2018-01-01"`, `end_datetime: "2020-12-31"`
- **Assets**:
  - `cog` → statewide hillshade
  - `meta` → JSON metadata with EPSG, source DEM reference

### Archival Document (Text)
Item: `treaty_1854_kansas.json`

- **Collection**: `documents`
- **Geometry**: polygon of treaty boundary (or centroid)
- **Properties**:
  - `datetime: "1854-05-18T00:00:00Z"`
  - `document:type: "treaty"`
- **Assets**:
  - `pdf` → scanned document
  - `txt` → OCR-extracted text
  - `summary` → machine-generated synopsis

### Event Record
Item: `greensburg_tornado_2007.json`

- **Collection**: `events`
- **Geometry**: tornado track line
- **Properties**:
  - `datetime: "2007-05-04T21:45:00Z"`
  - `event:type: "tornado"`
- **Assets**:
  - `geojson` → track polyline
  - `report` → NOAA SPC storm report

---

## Design Notes

- Items capture **atomic data points**; Collections group thematically.
- Use **checksums** (`checksum:multihash`) for reproducibility [oai_citation:5‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-BgUSuffTiRq4qidye2sPwN).
- Include **uncertainty notes** in `properties` if georeferencing or NLP confidence < 1 [oai_citation:6‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-BgUSuffTiRq4qidye2sPwN).
- **Document Items** can be enriched via the Knowledge Hub ingestion pipeline [oai_citation:7‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).
- **Environmental Items** (DEM, climate, hazard events) link to NOAA, USGS, Daymet, FEMA, NIFC datasets [oai_citation:8‡Historical Dataset Integration for Kansas Frontier Matrix.pdf](file-service://file-EG371w17RJTzXWjXvqgsB6).

---

## Adding New Items

1. Copy a template JSON from `templates/`.
2. Fill in `id`, `geometry`, `bbox`, `properties`, and `assets`.
3. Link to the correct `collection`.
4. Run validation:
   ```bash
   stac-validate stac/items/<item>.json

	5.	Open a Pull Request describing the source and provenance.

⸻

References
	•	STAC Spec 1.0.0
	•	Kansas-Frontier-Matrix design and audit docs ￼ ￼ ￼ ￼ ￼

⸻

Tip: Treat Items as the leaves of the STAC tree. Collections are the branches,
the Catalog is the trunk.
