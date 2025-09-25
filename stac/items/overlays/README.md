# Kansas-Frontier-Matrix — STAC Items (Overlays)

This directory stores **STAC Items** for *overlay maps* — mainly **historical topographic sheets, survey maps, flood maps, shaded relief, and other georeferenced scans**.  
Overlays are distinct from elevation DEM/hillshade: they are raster documents, scanned maps, or imagery layers that can be draped on top of terrain.

---

## Organization

- Each Item JSON corresponds to a single **overlay map or layer**.  
- Items live under `stac/items/overlays/` and must link to:
  - Their **Collection** (usually `historic_topo`, `ks_kansas_river`, or `elevation`)  
  - The repo **catalog** (`stac/catalog.json`)  

---

## ID & File Naming

- Use `<theme>_<place>_<year>` or `<theme>_<year>`  
- Lowercase, snake case, unique within repo.  

**Examples**
- `usgs_topo_larned_1894.json`  
- `ks_state_geology_1905.json`  
- `ks_kansas_river_flood_1951.json`  

---

## Required Fields

See the [Item Template Guide](../TEMPLATE_GUIDE.md) for details.  
Minimum requirements:

- `id` — unique ID (matches filename stem)  
- `collection` — e.g. `"historic_topo"` or `"ks_kansas_river"`  
- `bbox` and `geometry` — extent (polygon bounding the overlay)  
- `properties.datetime` — publication, survey, or event date  
- `proj:epsg` — EPSG:4326 (baseline); include transforms if known  
- **Links**: must include `self`, `collection`, `parent`, and `root`  

---

## Assets (Conventions)

- `cog` — Cloud-Optimized GeoTIFF (primary georeferenced raster)  
- `thumbnail` — PNG for previews  
- optional:  
  - `kml` — styled Earth overlay (for Google Earth/Globe use)  
  - `style` — QML/SLD for GIS symbology  
  - `pdf` — original scanned source if relevant  

---

## Uncertainty (Strongly Recommended)

- `uncertainty:georef_m` — RMS error of georeferencing (in meters)  
- `uncertainty:notes` — description of control points, rectification method, or scan quality  

Overlay maps often have distortions; documenting this improves downstream analysis and reproducibility.  

---

## Example (Mini)

```json
{
  "id": "usgs_topo_larned_1894",
  "collection": "historic_topo",
  "type": "Feature",
  "stac_version": "1.0.0",
  "bbox": [-99.401, 38.000, -99.000, 38.217],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-99.401, 38.000], [-99.000, 38.000],
      [-99.000, 38.217], [-99.401, 38.217],
      [-99.401, 38.000]
    ]]
  },
  "properties": {
    "datetime": "1894-01-01T00:00:00Z",
    "title": "USGS Historic Topo — Larned (1894)",
    "proj:epsg": 4326,
    "uncertainty:georef_m": 12.3
  },
  "assets": {
    "cog": {
      "href": "../../../data/cogs/overlays/usgs_topo_larned_1894.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "COG — Larned 1894"
    },
    "thumbnail": {
      "href": "../../../data/cogs/overlays/usgs_topo_larned_1894_preview.png",
      "type": "image/png",
      "title": "Thumbnail — Larned 1894"
    }
  },
  "links": [
    { "rel": "collection", "href": "../../collections/historic_topo.json", "type": "application/json" },
    { "rel": "parent", "href": "../../collections/historic_topo.json", "type": "application/json" },
    { "rel": "root", "href": "../../catalog.json", "type": "application/json" },
    { "rel": "self", "href": "usgs_topo_larned_1894.json", "type": "application/json" }
  ]
}
````

---

## Contributor Checklist

* [ ] JSON validates with `make stac-validate`
* [ ] Geometry matches the overlay’s COG footprint
* [ ] Assets exist at referenced paths (`data/cogs/overlays/...`)
* [ ] Time fields use full ISO 8601 Zulu format
* [ ] Uncertainty fields (`uncertainty:georef_m`, `uncertainty:notes`) added if applicable
* [ ] Provenance/source cited in `properties.description` or `providers`

---

## References

* [STAC Item Template Guide](../TEMPLATE_GUIDE.md)
* [Kansas-Frontier-Matrix — Open-Source Geospatial Historical Mapping Hub Design](../../../docs/Kansas-Frontier-Matrix_Design.pdf)
* [Historical Dataset Integration for Kansas Frontier Matrix](../../../docs/Historical_Dataset_Integration.pdf)

---

```

---

This version fixes:  
- **Collection wiring** → `historic_topo` (not `base_maps`).  
- **Relative links** → clean paths from `overlays/`.  
- **Checklist** explicitly enforces provenance + uncertainty.  
- **References** point to your `docs/` folder for design docs, not dangling paths.  
