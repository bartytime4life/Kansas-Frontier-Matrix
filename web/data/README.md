# Kansas-Frontier-Matrix — Web Data

This folder holds **JSON and GeoJSON data** used by the **web viewer** (`web/`).  
It provides small demo entities for testing and can later be extended with full STAC-linked datasets.

---

## Files

- **`demo_entities.json`**  
  A lightweight **demo dataset** of historical Kansas entities.  
  Includes sample settlements, treaties, trails, and railroads with:
  - `id`, `type`, `title`, `description`
  - `location` (point) or `path` (polyline)
  - `time.start` / `time.end` (for timeline filtering)
  - `sources` (provenance)

- *(planned)* `demo_entities.geojson`  
  Direct **GeoJSON export** of the same features for MapLibre overlay.  
  Useful for quick map rendering.

---

## Structure

Example entry from `demo_entities.json`:

```json
{
  "id": "settlement_lawrence",
  "type": "settlement",
  "title": "Lawrence",
  "description": "Founded in 1854 by Free-State settlers. Center of Bleeding Kansas conflict.",
  "location": { "lat": 38.9717, "lon": -95.2353 },
  "time": { "start": "1854-01-01", "end": null },
  "sources": ["USGS", "Kansas Historical Society"]
}
````

* **Point features** → `location`
* **Line features** → `path` (array of `[lon, lat]` coordinates)
* **Time** → ISO dates (`YYYY-MM-DD`) for filtering on the time slider

---

## Usage

* In the web viewer (`web/app.js`), load this JSON to:

  * Populate **sidebar lists** of entities
  * Filter by **time** using the global slider
  * Render popups or highlights when entities are clicked

* For **map overlays**:

  * Convert features into **GeoJSON layers** for MapLibre
  * Style by `type` (e.g., settlements = circles, trails = lines, treaties = markers)

---

## Contribution Guidelines

* Keep datasets **small** for web/demo use.
* Larger, authoritative datasets should live under `data/` and be wired into STAC.
* Always include **provenance (`sources`)** for transparency.
* Prefer **lat/lon (WGS84 / EPSG:4326)** coordinates for compatibility.

---

## Roadmap

* [ ] Add `demo_entities.geojson` (map-ready export)
* [ ] Connect to STAC items under `stac/items/`
* [ ] Provide filtered subsets (e.g., county-level)
* [ ] Add support for image overlays (historic scans)

---

🚀 This folder is the **bridge** between structured data (STAC + `data/`) and the **interactive map UI**.

```
