STAC Item Template Guide — Kansas-Frontier-Matrix

This guide explains how to fill the map, document, and event Item templates under stac/items/.
Items are leaves in the STAC tree: they must link to a parent Collection and the Catalog.

Reference architecture: STAC catalog + document knowledge hub + time/space UI ￼ ￼
Data domains & sources: hazards, DEM/LiDAR, maps, documents ￼
Gaps: uncertainty, oral histories, proxies, story layers ￼

⸻

1) ID & File Naming
	•	Lowercase, kebab or snake case.
	•	Unique across repo.
	•	Prefer <theme>_<place>_<yyyy> or <theme>_<yyyy_yyyy>.

Examples
	•	usgs_larned_1894
	•	hillshade_2018_2020
	•	treaty_kansas_1854
	•	greensburg_tornado_2007

👉 Why: readability + reproducibility + graph cross-linking ￼.

⸻

2) Spatial Fields (bbox, geometry)

Kansas statewide bbox:
[-102.05, 36.99, -94.59, 40.00]
	•	Polygon → map sheets, rasters, treaty boundaries
	•	Point → document centroid, fort/town, POI
	•	LineString → trails, tornado tracks, routes

Tips:
	•	Maps → warped footprint; fallback = sheet rectangle.
	•	Docs → centroid of referenced place (use buffer if uncertainty high ￼).

👉 Why: consistent geometry = better map rendering, queries ￼.

⸻

3) Temporal Fields

Use ISO 8601 (datetime or start_datetime/end_datetime).
	•	Maps → publication/survey date
	•	DEM/Hillshade → acquisition range
	•	Events → start (and end if multi-day)
	•	Documents → publication or earliest credible date

Examples

"datetime": "1894-06-01T00:00:00Z"
"start_datetime": "2018-01-01T00:00:00Z",
"end_datetime": "2020-12-31T23:59:59Z"

👉 Why: timeline & slider queries rely on precise dates ￼.

⸻

4) Properties

Required
	•	title — human readable
	•	description — concise, contextual
	•	proj:epsg — 4326 baseline
	•	datetime or start/end_datetime

Recommended
	•	Maps/rasters: raster:bands, gsd, checksum:multihash
	•	Documents: document:type, document:source
	•	Events: event:type (tornado, flood, treaty, etc.)

Uncertainty (strongly encouraged)
	•	uncertainty:georef_m — RMS error (maps)
	•	uncertainty:nlp_conf — 0–1 NLP confidence (docs)
	•	uncertainty:notes — rationale ￼

👉 Why: audit flagged uncertainty handling as a missing layer ￼.

⸻

5) Assets

Maps/rasters
	•	cog → GeoTIFF (COG)
	•	thumbnail → PNG
	•	optional: kml, style

Documents
	•	pdf → scan
	•	txt → OCR/transcription
	•	summary → plain text or JSON

Events
	•	geojson → geometry (track/extent)
	•	report → PDF/CSV support

👉 Why: predictable asset roles = seamless MapLibre, Earth, and hub wiring ￼.

⸻

6) Links

Every Item must include:

{ "rel": "collection", "href": "../collections/<collection>.json", "type": "application/json" },
{ "rel": "root", "href": "../catalog.json", "type": "application/json" },
{ "rel": "parent", "href": "../catalog.json", "type": "application/json" },
{ "rel": "self", "href": "<this-file>.json", "type": "application/json" }


⸻

7) Uncertainty & Confidence

Capture uncertainty explicitly:
	•	Maps → RMS, GCP notes
	•	Docs → NLP confidence, toponym ambiguity
	•	Events → geometry margin, source reliability (e.g. FEMA class) ￼

👉 UI should surface uncertainty visually (e.g. shading, error bands).

⸻

8) Thematic Conventions

Maps (historical topo)
	•	Collection: base_maps
	•	Assets: cog under data/cogs/overlays/
	•	Time: publication/survey date

DEM/Hillshade
	•	Collections: dem, hillshade
	•	Describe source (1-m DEM, 3DEP)
	•	Assets: COG, optional derivatives

Documents
	•	Collection: documents
	•	document:type: treaty, diary, newspaper, letter, report
	•	Geometry: centroid or boundary
	•	Assets: pdf, txt, summary ￼

Events
	•	Collection: events
	•	event:type: tornado, battle, treaty_signing, flood
	•	Geometry: path/polygon
	•	Align with SPC/FEMA/NCEI IDs ￼

⸻

9) Mini Examples

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

10) Quality Checklist
	•	Valid JSON (linted)
	•	Passes stac-validate stac/items/<item>.json
	•	Collection + links correct
	•	Geometry matches asset
	•	Time fields correct
	•	Assets exist at referenced paths
	•	Uncertainty fields present (maps/docs/events)
	•	Provenance: cite source dataset/provider ￼

⸻

11) Contributor Tips
	•	Use COG for rasters; always include thumbnail
	•	Keep titles short; detail in description
	•	Use statewide bbox only when truly statewide
	•	For multi-place docs, choose primary place or small multipolygon
	•	When in doubt: add uncertainty:notes

⸻

12) References
	•	System design & map UI ￼
	•	Knowledge Hub ingestion & graph ￼
	•	Dataset integration (hazards, DEM, climate) ￼
	•	Design audit: uncertainty, oral histories, story layers ￼

⸻
