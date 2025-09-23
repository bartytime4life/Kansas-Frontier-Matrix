# STAC Item Template Guide — Kansas-Frontier-Matrix

This guide shows how to fill the **map**, **document**, and **event** Item templates under `stac/items/`.
Items are *leaves* in the STAC tree; they must link to a parent **Collection** and the **Catalog**.

> Reference design: STAC-like catalog + doc knowledge hub + time/space UI [oai_citation:4‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv) [oai_citation:5‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB)  
> Data domains & sources: hazards, climate, DEM/LiDAR, maps, docs [oai_citation:6‡Historical Dataset Integration for Kansas Frontier Matrix.pdf](file-service://file-EG371w17RJTzXWjXvqgsB6)  
> Gaps to track: uncertainty, oral histories, proxies, story layers [oai_citation:7‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-BgUSuffTiRq4qidye2sPwN)

---

## 1) ID & File Naming

**Rules**
- Lowercase, kebab or snake case; include type + year(s).
- Unique within repo. Prefer `<theme>_<place>_<yyyy>` or `<theme>_<yyyy_yyyy>`.

**Examples**
- `usgs_larned_1894`
- `hillshade_2018_2020`
- `treaty_kansas_1854`
- `greensburg_tornado_2007`

**Why**  
Uniqueness + readability helps curation, reproducibility, and cross-linking to docs/graph [oai_citation:8‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).

---

## 2) Spatial Fields (bbox, geometry)

**Kansas bbox (statewide)**

[-102.05, 36.99, -94.59, 40.00]

**Geometry choices**
- **Polygon**: map sheets, statewide rasters (COG), treaty boundaries.
- **Point**: document centroid (fort, town) or a POI when exact extent unknown.
- **LineString**: tracks (e.g., tornado), trails, route segments.

**Tips**
- For georeferenced maps, use the warped footprint; else the sheet rectangle.
- For documents, you can use centroid of a place or small buffer polygon if uncertainty warrants (see §7).

**Why**  
Consistent geometry improves map rendering and spatial filtering in the UI & graph queries [oai_citation:9‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv) [oai_citation:10‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).

---

## 3) Temporal Fields

- Use `properties.datetime` **or** `start_datetime`/`end_datetime` (ISO 8601).
- **Maps**: publication or survey date.  
- **DEM/Hillshade**: range of source acquisition.  
- **Events**: start (and end if multi-day).  
- **Documents**: publication or earliest credible date.

**Examples**
```json
"datetime": "1894-06-01T00:00:00Z"
"start_datetime": "2018-01-01T00:00:00Z",
"end_datetime": "2020-12-31T23:59:59Z"

Why
The time slider & timeline queries depend on precise datetimes ￼.

⸻

4) Properties (required + recommended)

Required
	•	title — human friendly.
	•	description — concise but informative.
	•	proj:epsg — use 4326 (and include transform where available).
	•	One of datetime or (start_datetime + end_datetime).

Suggested keys
	•	Rasters: raster:bands, gsd, checksum:multihash.
	•	Docs: document:type (treaty, diary, newspaper, survey, letter, report), document:source.
	•	Events: event:type (tornado, flood, battle, treaty_signing).

Uncertainty (see §7)
	•	uncertainty:georef_m — RMS or estimated horizontal error.
	•	uncertainty:nlp_conf — 0–1 confidence for NLP place/date extraction (docs).
	•	uncertainty:notes — brief rationale.

Why
Audit calls for explicit uncertainty and provenance; STAC properties are the contract for UI/analysis ￼.

⸻

5) Assets (files)

Keep asset names simple and roles clear:
	•	Maps/rasters
	•	cog — image/tiff; application=geotiff; profile=cloud-optimized
	•	thumbnail — image/png
	•	optional: kml — Earth overlay, style — SLD/QML
	•	Documents
	•	pdf — scanned original (application/pdf)
	•	txt — OCR or transcription (text/plain)
	•	summary — brief synopsis (text/plain or application/json)
	•	Events
	•	geojson — path/extent (application/geo+json)
	•	report — supporting PDF or CSV

Why
Predictable asset roles make it trivial to wire into MapLibre + Earth + knowledge hub pipelines ￼ ￼.

⸻

6) Links (STAC)

Every Item must include:

{ "rel": "collection", "href": "../collections/<collection>.json", "type": "application/json" },
{ "rel": "root", "href": "../catalog.json", "type": "application/json" },
{ "rel": "parent", "href": "../catalog.json", "type": "application/json" },
{ "rel": "self", "href": "<this-file>.json", "type": "application/json" }

Why
Keeps the STAC graph navigable for validators and clients.

⸻

7) Uncertainty & Confidence (strongly recommended)

Because georeferencing and NLP extraction introduce error, capture it:
	•	Maps: uncertainty:georef_m (RMS), uncertainty:notes (GCP count, source).
	•	Docs: uncertainty:nlp_conf (0–1), uncertainty:notes (toponym ambiguity).
	•	Events: uncertainty:geom_m (track or flood edge uncertainty), uncertainty:source (SPC/FEMA class).

The design audit flags explicit uncertainty handling as a key gap—surface it in Items so the UI can convey data quality ￼.

⸻

8) Thematic Conventions

Maps (historical topographic)
	•	Collection: base_maps
	•	title: Historical Topo — <Place>, <Year>
	•	description: mention scale, edition, georef method.
	•	assets.cog: path under data/cogs/overlays/
	•	Time: publication/survey date.

DEM/Hillshade
	•	Collection: dem or hillshade
	•	description: DEM source (1-m, 3DEP), processing chain (warp → gdaldem → COG).
	•	Time: acquisition range; link to upstream DEM.

Documents (treaties, diaries, newspapers)
	•	Collection: documents
	•	document:type: from controlled list (see §4).
	•	Geometry: centroid of relevant place or boundary polygon.
	•	Assets: pdf, txt, summary.

Events
	•	Collection: events
	•	event:type: tornado, flood, battle, treaty_signing, etc.
	•	Geometry: path or area.
	•	Source alignment: SPC/FEMA/NCEI IDs for hazards; archival refs for historical events ￼.

⸻

9) Examples (mini)

Map

"id": "usgs_larned_1894",
"collection": "base_maps",
"properties": {
  "datetime": "1894-06-01T00:00:00Z",
  "title": "Historical Topo — Larned, 1894",
  "proj:epsg": 4326,
  "uncertainty:georef_m": 12.3
}

Document

"id": "treaty_kansas_1854",
"collection": "documents",
"properties": {
  "datetime": "1854-05-18T00:00:00Z",
  "title": "Treaty of 1854 — Kansas",
  "document:type": "treaty",
  "uncertainty:nlp_conf": 0.92
}

Event

"id": "greensburg_tornado_2007",
"collection": "events",
"properties": {
  "datetime": "2007-05-04T21:45:00Z",
  "title": "Greensburg Tornado (EF5)",
  "event:type": "tornado"
}


⸻

10) Quality Checklist (before PR)
	•	Valid JSON (linted).
	•	STAC validation passes:

stac-validate stac/items/<item>.json


	•	collection and links correct.
	•	Geometry matches asset extent.
	•	Time fields present & correct precision.
	•	Assets exist at referenced paths.
	•	Uncertainty fields present when applicable (maps/docs/events) ￼.
	•	Provenance: mention upstream dataset/provider (USGS/NOAA/etc.) ￼.

⸻

11) Contributor Tips
	•	Prefer COG for rasters; include a small thumbnail.
	•	Keep titles short; push detail to description.
	•	Use statewide bbox only when appropriate (e.g., statewide hillshade).
	•	For multi-place documents, pick the primary place (or use a small multi-polygon, noting uncertainty).
	•	When in doubt, add a brief uncertainty:notes.

⸻

12) References
	•	System architecture & layers (catalog, map UI, Earth/KML) ￼
	•	Design audit: uncertainty, oral histories, story layers ￼
	•	Hazards/climate datasets (NOAA SPC/NCEI, FEMA, Daymet) ￼
	•	Knowledge Hub ingestion & graph (entities/links/confidence) ￼
