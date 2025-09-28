## `stac/items/vectors/README.md`

# Kansas-Frontier-Matrix — Vector STAC Items

This folder holds **STAC Item JSON descriptors** for **vector datasets**
integrated into the Kansas-Frontier-Matrix timeline-map system.
Each item corresponds to a **GeoJSON (or vector tile)** layer, tagged with
spatial, temporal, and provenance metadata.

---

## Purpose

* Provide **machine-readable STAC Items** for all vector overlays (e.g. trails, forts, towns, parcels, treaty boundaries).

* Enable **automatic config generation** via:

  ```bash
  make stac
  make stac-validate
  kgt render-config --stac stac/items --output web/app.config.json --pretty
  ```

* Ensure **traceability** of vector data (source URLs, lineage, licensing).

* Support **timeline slider** integration by defining `properties.start_datetime` / `end_datetime`.

---

## Directory Layout

```
stac/items/vectors/
├── trails_santafe.json        # Santa Fe Trail vector overlay
├── forts.json                 # Fort locations
├── towns.json                 # Settlements, trading posts
├── treaties.json              # Tribal land cessions / boundaries
├── parcels_county_x.json      # Sample county parcel vectors
└── README.md                  # This file
```

---

## STAC Conventions for Vectors

Each Item must include:

* **id**: unique stable identifier (`vectors_trails_santafe`).
* **collection**: `"topo"`, `"land"`, `"culture"`, etc. depending on grouping.
* **properties**:

  * `start_datetime` / `end_datetime` → timeline attributes.
  * `proj:epsg` → spatial reference (use EPSG:4326 for web).
  * optional `kfm:source`, `kfm:lineage`, `kfm:confidence`.
* **geometry** / **bbox**: bounding box of features.
* **assets**:

  * `"vector"` → path to processed GeoJSON.
  * optional `"thumbnail"` PNG for UI previews.

---

## Example Item

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "vectors_trails_santafe",
  "collection": "culture",
  "properties": {
    "start_datetime": "1821-01-01T00:00:00Z",
    "end_datetime": "1880-12-31T23:59:59Z",
    "proj:epsg": 4326,
    "kfm:source": "National Park Service / Kansas GIS Archive"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[-102.05,36.99],[-94.61,36.99],[-94.61,40.00],[-102.05,40.00],[-102.05,36.99]]]
  },
  "bbox": [-102.05, 36.99, -94.61, 40.00],
  "assets": {
    "vector": {
      "href": "data/processed/vectors/trails_santafe.json",
      "type": "application/geo+json",
      "roles": ["data", "overlay"],
      "title": "Santa Fe Trail (vector overlay)"
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../collections/culture.json",
      "type": "application/json"
    }
  ]
}
```

---

## Notes

* Store **raw scans** or shapefiles in `data/sources/land/vectors/` and keep **processed GeoJSON** in `data/processed/`.
* Run conversion with `ogr2ogr -f GeoJSON -t_srs EPSG:4326`.
* Validate with `make stac-validate` to ensure Items conform to schema.
* Use **confidence flags** where coverage is incomplete or uncertain.

---
