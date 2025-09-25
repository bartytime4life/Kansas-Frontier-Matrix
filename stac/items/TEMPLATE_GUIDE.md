# STAC Item Template Guide — Kansas-Frontier-Matrix

This guide explains how to fill the **map**, **document**, and **event** Item templates under `stac/items/`.
Items are **leaves** in the STAC tree and **must** link to a parent **Collection** and the **Catalog**.

**Reference architecture:** STAC catalog + document knowledge hub + time/space UI
**Data domains:** hazards, hydrology, DEM/LiDAR, historic maps, documents
**Known gaps:** explicit uncertainty fields, oral histories, proxies, story layers

---

## 1) ID & file naming

* Lowercase; kebab or snake case.
* Unique across the repository.
* Prefer `theme_place_yyyy` or `theme_yyyy_yyyy`.

**Examples**

* `usgs_larned_1894`
* `hillshade_2018_2020`
* `treaty_kansas_1854`
* `greensburg_tornado_2007`

**Why:** human-readable IDs improve reproducibility and cross-linking.

---

## 2) Spatial fields (`bbox`, `geometry`)

**Kansas statewide bbox:** `[-102.05, 36.99, -94.59, 40.00]`

* **Polygon** → map sheets, rasters, treaty boundaries
* **Point** → document centroid, fort/town, POI
* **LineString** → trails, tornado tracks, routes

**Tips**

* **Maps** → use the warped footprint polygon; fallback to a sheet rectangle.
* **Docs** → point at referenced place centroid (consider buffered visualization if uncertainty is high).
* Ensure **winding/order** is consistent:
  `[minX,minY] → [maxX,minY] → [maxX,maxY] → [minX,maxY] → back to start`.
* Keep `bbox` **in sync** with `geometry`.

**Why:** consistent geometry = better map rendering and spatial queries.

---

## 3) Temporal fields

Use ISO-8601 (Zulu). Choose **either** an instant `datetime` **or** an interval.

* **Maps** → publication/survey date
* **DEM/Hillshade** → acquisition range
* **Events** → start (and end if multi-day)
* **Documents** → publication or earliest credible date

**Examples**

```json
"datetime": "1894-06-01T00:00:00Z"

"datetime": null,
"start_datetime": "2018-01-01T00:00:00Z",
"end_datetime":   "2020-12-31T23:59:59Z"
```

**Why:** the time slider and timeline queries rely on precise dates.

---

## 4) Properties (minimum + recommended)

**Required**

* `title` — human-readable
* `description` — concise, with context
* `proj:epsg` — `4326` baseline
* `datetime` **or** `start_datetime`/`end_datetime`

**Recommended (by theme)**

* **Maps/Rasters:** `raster:bands`, `gsd` (meters), `checksum:sha256` (asset), `file:size` (asset)
* **Documents:** `document:type` (`treaty`, `diary`, `newspaper`, `letter`, `report`, …), optional `document:source`
* **Events:** `event:type` (`tornado`, `flood`, `battle`, `treaty_signing`, …)

**Uncertainty (strongly encouraged)**

* `uncertainty:georef_m` — RMS georeference error (maps)
* `uncertainty:nlp_conf` — 0–1 NLP/OCR confidence (docs)
* `uncertainty:notes` — short rationale

**Why:** the design audit flagged uncertainty handling as a missing layer.

---

## 5) Assets (roles & paths)

**Maps/Rasters**

* `cog` → GeoTIFF (COG) — `roles: ["data","visual"]`
* `thumbnail` → PNG — `roles: ["thumbnail","overview"]`
* optional: `kml`, `style`

**Documents**

* `pdf` → scan — `roles: ["data"]`
* `txt` → OCR/transcript — `roles: ["metadata"]`
* optional: `summary` (TXT or JSON)

**Events**

* `geojson` → event geometry (track/extent) — `roles: ["data"]`
* `report` → PDF/CSV — `roles: ["metadata"]`

**Paths**

* From `stac/items/<…>.json`, assets typically start with `../../data/...`.

**Checksum/size**

* Avoid `null`. Use numbers for `file:size` and strings for `checksum:sha256`.
* Fill via CI (see snippet in §10).

---

## 6) Links (always include these four)

Each Item **must** include:

```json
{ "rel": "self",       "href": "./<this-file>.json",              "type": "application/json" },
{ "rel": "collection", "href": "../collections/<collection>.json","type": "application/json" },
{ "rel": "parent",     "href": "../collections/<collection>.json","type": "application/json" },
{ "rel": "root",       "href": "../catalog.json",                 "type": "application/json" }
```

> `parent` should point to the **Collection** (not the Catalog).

---

## 7) Thematic conventions (Collections)

* **Elevation (DEM + Hillshade)**

  * **Collection:** `elevation`
  * **DEM Items:** asset key `dem` (COG)
  * **Hillshade Items:** asset key `cog` or `hillshade` (COG), `derived_from` link to DEM Item
  * **Time:** acquisition interval

* **Historic base maps (USGS, atlases)**

  * **Collection:** `base_maps`
  * **Assets:** `cog` under `data/cogs/overlays/`
  * **Time:** publication/survey date

* **Hydrology (gauges, channels, floodplains, Kansas River set)**

  * **Collection:** `hydrology` (or `ks_kansas_river` if you maintain a dedicated sub-collection)
  * **Geometry:** points/lines/polygons; Item geometry may be a representative sample; the asset can hold the full dataset

* **Documents (treaties, diaries, newspapers, letters)**

  * **Collection:** `documents`
  * **Geometry:** centroid of place or boundary polygon
  * **Assets:** `pdf`, `txt`, optional `summary`

* **Events (tornadoes, floods, battles, treaty signing)**

  * **Collection:** `events`
  * **Geometry:** track polygon/line; align IDs with authoritative sources (SPC/NCEI/FEMA/etc. when available)
  * **Time:** instant or interval

---

## 8) Mini examples

**Map**

```json
"id": "usgs_larned_1894",
"collection": "base_maps",
"properties": {
  "datetime": "1894-06-01T00:00:00Z",
  "title": "Historical Topo — Larned (1894)",
  "proj:epsg": 4326,
  "uncertainty:georef_m": 12.3
}
```

**Document**

```json
"id": "treaty_kansas_1854",
"collection": "documents",
"properties": {
  "datetime": "1854-05-18T00:00:00Z",
  "title": "Treaty of 1854 — Kansas",
  "document:type": "treaty",
  "uncertainty:nlp_conf": 0.92
}
```

**Event**

```json
"id": "greensburg_tornado_2007",
"collection": "events",
"properties": {
  "datetime": "2007-05-04T21:45:00Z",
  "title": "Greensburg Tornado (EF5)",
  "event:type": "tornado"
}
```

---

## 9) Extensions to declare (per need)

Add to `stac_extensions` **only** when fields from that extension are used:

* Projection: `https://stac-extensions.github.io/projection/v1.0.0/schema.json`
* Raster: `https://stac-extensions.github.io/raster/v1.1.0/schema.json`
* File: `https://stac-extensions.github.io/file/v2.0.0/schema.json`
* Checksum: `https://stac-extensions.github.io/checksum/v1.0.0/schema.json`
* Version: `https://stac-extensions.github.io/version/v1.0.0/schema.json`

**Placement tips**

* `raster:bands` → usually under the **asset** that carries pixels (tool-friendly)
* `file:size`, `checksum:sha256` → always under the **asset**

---

## 10) Quality checklist

* [ ] Valid JSON (linted)
* [ ] Passes `stac-validate stac/items/<item>.json`
* [ ] `collection` and all `links` correct (`parent` → Collection)
* [ ] `geometry` matches `bbox` and dataset footprint
* [ ] Time fields correct (instant **or** interval with `datetime: null`)
* [ ] Assets exist at referenced paths; roles set (`data`, `visual`, `thumbnail`, `metadata`)
* [ ] Uncertainty fields present where applicable
* [ ] Provenance captured (`links[].rel="via"` to source service; cite provider in Collection)

---

## 11) CI snippets (size & checksum autofill)

Fill `file:size` and `checksum:sha256` for an Item’s asset(s) and bump `updated`:

```bash
J="stac/items/<your_item>.json"
for A in cog dem image data pdf txt; do
  F=$(jq -r ".assets[\"$A\"].href // empty" "$J")
  [ -n "$F" ] || continue
  SIZE=$(wc -c < "$F" | tr -d ' ')
  SHA=$(sha256sum "$F" | awk '{print $1}')
  jq --arg a "$A" --argjson s "$SIZE" --arg sha "$SHA" \
     '.assets[$a]["file:size"]=$s | .assets[$a]["checksum:sha256"]=$sha' \
     "$J" > "$J.tmp" && mv "$J.tmp" "$J"
done
jq '.properties.updated=(now|toiso8601)' "$J" > "$J.tmp" && mv "$J.tmp" "$J"
```

> Adjust the asset keys loop (`cog dem image data pdf txt …`) to the actual keys present.

---

## 12) Contributor tips

* Use **COG** for rasters; include a **thumbnail** for quick previews.
* Keep **titles short**; move details to `description`.
* Use the **statewide bbox only when truly statewide**.
* For multi-place documents, pick a primary place or use a small **MultiPolygon**.
* When in doubt, add `uncertainty:notes`.
* Prefer **relative paths** from `stac/items/` to data (`../../data/...`).
* For derived products, add a `links[].rel="derived_from"` pointing to the source Item.

---

### Appendix: Minimal Item skeletons

**Raster (hillshade)**

```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v2.0.0/schema.json",
    "https://stac-extensions.github.io/checksum/v1.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "hillshade_2018_2020",
  "collection": "elevation",
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "geometry": { "type": "Polygon", "coordinates": [[[ -102.05, 36.99 ], [ -94.59, 36.99 ], [ -94.59, 40.00 ], [ -102.05, 40.00 ], [ -102.05, 36.99 ]]] },
  "properties": {
    "title": "Kansas Hillshade (1 m DEM derived, 2018–2020)",
    "description": "Statewide hillshade derived from 1 m DEM.",
    "datetime": null,
    "start_datetime": "2018-01-01T00:00:00Z",
    "end_datetime": "2020-12-31T23:59:59Z",
    "proj:epsg": 4326
  },
  "assets": {
    "cog": {
      "href": "../../data/cogs/hillshade/ks_hillshade_2018_2020.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data","visual"],
      "file:size": 0,
      "checksum:sha256": "REPLACE_SHA256",
      "raster:bands": [{ "name": "hillshade", "data_type": "uint8" }]
    }
  },
  "links": [
    { "rel": "self", "href": "./hillshade_2018_2020.json", "type": "application/json" },
    { "rel": "collection", "href": "../collections/elevation.json", "type": "application/json" },
    { "rel": "parent", "href": "../collections/elevation.json", "type": "application/json" },
    { "rel": "root", "href": "../catalog.json", "type": "application/json" }
  ]
}
```

**Document**

```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
    "https://stac-extensions.github.io/file/v2.0.0/schema.json",
    "https://stac-extensions.github.io/checksum/v1.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "documents_PLACE_TITLE_YYYY",
  "collection": "documents",
  "bbox": [-98.0, 38.5, -98.0, 38.5],
  "geometry": { "type": "Point", "coordinates": [ -98.0, 38.5 ] },
  "properties": {
    "title": "Archival Document — TITLE (YYYY)",
    "description": "Scanned or transcribed archival record.",
    "document:type": "treaty",
    "datetime": "YYYY-01-01T00:00:00Z",
    "proj:epsg": 4326
  },
  "assets": {
    "pdf": { "href": "../../data/docs/REPLACE_FILE.pdf", "type": "application/pdf", "roles": ["data"], "file:size": 0, "checksum:sha256": "REPLACE_SHA256" },
    "txt": { "href": "../../data/docs/REPLACE_FILE.txt", "type": "text/plain", "roles": ["metadata"], "file:size": 0, "checksum:sha256": "REPLACE_SHA256" }
  },
  "links": [
    { "rel": "self", "href": "./document_item.json", "type": "application/json" },
    { "rel": "collection", "href": "../collections/documents.json", "type": "application/json" },
    { "rel": "parent", "href": "../collections/documents.json", "type": "application/json" },
    { "rel": "root", "href": "../catalog.json", "type": "application/json" }
  ]
}
```

**Event (interval)**

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "events_PLACE_EVENT_YYYY",
  "collection": "events",
  "bbox": [-100.0, 38.0, -98.0, 39.0],
  "geometry": { "type": "LineString", "coordinates": [[ -100.0, 38.0 ], [ -98.0, 39.0 ]] },
  "properties": {
    "title": "Event — NAME (YYYY)",
    "description": "Historical event description.",
    "event:type": "tornado",
    "datetime": null,
    "start_datetime": "YYYY-05-01T00:00:00Z",
    "end_datetime":   "YYYY-05-02T23:59:59Z",
    "proj:epsg": 4326
  },
  "assets": {
    "geojson": { "href": "../../data/events/REPLACE_FILE.geojson", "type": "application/geo+json", "roles": ["data"] }
  },
  "links": [
    { "rel": "self", "href": "./event_item.json", "type": "application/json" },
    { "rel": "collection", "href": "../collections/events.json", "type": "application/json" },
    { "rel": "parent", "href": "../collections/events.json", "type": "application/json" },
    { "rel": "root", "href": "../catalog.json", "type": "application/json" }
  ]
}
```
