# Kansas-Frontier-Matrix — STAC Items (Overlays)

This directory stores **STAC Items** for *overlay maps* — mainly **historical topographic sheets, survey maps, and other georeferenced scans**.  
Overlays are distinct from base DEM/hillshade: they are raster documents, scanned maps, or imagery layers that can be draped on top of terrain.

---

## Organization

- Each Item JSON corresponds to a single **overlay map**.
- Items live under `stac/items/overlays/` and must link to:
  - Their **Collection** (usually `base_maps` or `overlays`)
  - The repo **catalog** (`stac/catalog.json`)

---

## ID & File Naming

- Use `<theme>_<place>_<year>` or `<theme>_<year>`  
- Lowercase, snake/kebab case, unique within repo.

**Examples**
- `usgs_larned_1894.json`
- `ks_state_geology_1905.json`
- `plss_township_map_1867.json`

---

## Required Fields

See the [Item Template Guide](../TEMPLATE_GUIDE.md) for details.  
Minimum requirements:

- `id` — unique ID (matches filename stem)  
- `collection` — e.g. `"base_maps"`  
- `bbox` and `geometry` — map extent (polygon or sheet rectangle)  
- `properties.datetime` — publication or survey date  
- `proj:epsg` — EPSG:4326 (baseline); include transforms if known  
- Links to collection, parent, root, and self

---

## Assets (Conventions)

- `cog` — Cloud-Optimized GeoTIFF of warped overlay
- `thumbnail` — PNG for previews
- optional:  
  - `kml` — styled Earth overlay  
  - `style` — QML/SLD for GIS styling  
  - `pdf` — original scanned source if relevant

---

## Uncertainty (Strongly Recommended)

- `uncertainty:georef_m` — RMS error of georeferencing  
- `uncertainty:notes` — how control points or rectification were derived  

Overlay maps often have distortions; documenting this improves downstream analysis.

---

## Example (Mini)

```json
{
  "id": "usgs_larned_1894",
  "collection": "base_maps",
  "type": "Feature",
  "stac_version": "1.0.0",
  "bbox": [-99.25, 38.15, -98.75, 38.45],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-99.25, 38.15], [-98.75, 38.15],
      [-98.75, 38.45], [-99.25, 38.45],
      [-99.25, 38.15]
    ]]
  },
  "properties": {
    "datetime": "1894-06-01T00:00:00Z",
    "title": "Historical Topo — Larned, 1894",
    "proj:epsg": 4326,
    "uncertainty:georef_m": 12.3
  },
  "assets": {
    "cog": {
      "href": "../../../data/cogs/overlays/usgs_topo_larned_1894.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "COG Georeferenced Overlay"
    },
    "thumbnail": {
      "href": "../../../data/cogs/overlays/usgs_topo_larned_1894.png",
      "type": "image/png",
      "title": "Thumbnail"
    }
  },
  "links": [
    { "rel": "collection", "href": "../../collections/base_maps.json", "type": "application/json" },
    { "rel": "root", "href": "../../catalog.json", "type": "application/json" },
    { "rel": "parent", "href": "../../catalog.json", "type": "application/json" },
    { "rel": "self", "href": "usgs_larned_1894.json", "type": "application/json" }
  ]
}


⸻

Contributor Checklist
	•	JSON validates with stac-validate
	•	Geometry matches COG footprint
	•	Assets exist at referenced paths (data/cogs/overlays/...)
	•	Time fields correct (ISO 8601, Zulu)
	•	Uncertainty fields added if applicable
	•	Provenance/source documented in description or properties

⸻

References
	•	STAC Item Template Guide
	•	[Kansas-Frontier-Matrix Hub Design](../../Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf)
	•	[Historical Dataset Integration](../../Historical Dataset Integration for Kansas Frontier Matrix.pdf)

---
