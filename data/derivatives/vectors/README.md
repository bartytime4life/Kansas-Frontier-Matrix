<div align="center">

# 🧭 Kansas-Frontier-Matrix — Vector Derivatives  
`data/derivatives/vectors/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)

**Mission:** Hold **derived vector datasets** built from canonical sources —  
including **boundaries, networks, parcels, hazards, and historical overlays** —  
to support Kansas **timeline analysis, map overlays, and web visualization**.  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Inputs\n(data/sources, data/cogs)"] --> B["Vector Processing\n(make vectors-*)"]
  B --> C["Vector Derivatives\n(data/derivatives/vectors)"]
  C --> D["STAC Items\n(stac/items/vectors_*)"]
  D --> E["Validate\n(stac-validate)"]
  C --> F["Tiles / PMTiles\n(data/derivatives/tiles/vector)"]

<!-- END OF MERMAID -->



⸻

📂 Directory Layout

data/
└─ derivatives/
   └─ vectors/
      ├─ boundaries/            # Derived admin/treaty/parcel boundaries
      │  └─ counties_1930.geojson
      ├─ networks/              # Transportation / utility networks
      │  └─ railroads_1900.geojson
      ├─ hazards/               # Hazard vectors (tornado, fire, flood)
      │  └─ tornado_tracks_decadal_1950_2020.geojson
      ├─ archaeology/           # Archaeological site polygons/points
      │  └─ kansas_sites_curated.geojson
      ├─ qc/                    # QA checks & reports
      │  └─ vectors_qc_report.md
      └─ README.md


⸻

✅ What Belongs Here
	•	Derived boundaries → county/parcel changes, treaty transitions, reservation boundaries.
	•	Networks → railroads, highways, canals, trails, powerlines.
	•	Hazards → tornado paths, wildfire perimeters, flood outlines.
	•	Archaeology/cultural → site vectors, survey overlays.

🚫 Does Not Belong
	•	Raw shapefiles/GeoJSON sources (data/sources/).
	•	DEM or raster derivatives (data/derivatives/terrain/, .../hydrology/).
	•	Ephemeral tiles (data/tiles/).

⸻

🛠 Workflow & Make Targets

# General vector processing
make vectors-boundaries      # build derived county/parcel/treaty boundaries
make vectors-networks        # build transport/utility networks
make vectors-hazards         # hazard vectors (tornado/fire/flood)
make vectors-archaeology     # derived archaeological site layers

# Register and validate in STAC
make stac stac-validate

# Build vector tiles for web
make tiles-vectors


⸻

📜 Naming & Metadata

Filename pattern

<theme>_<region|period|year>.geojson|parquet|pmtiles

Examples:
	•	counties_1930.geojson
	•	railroads_1900.geojson
	•	tornado_tracks_decadal_1950_2020.geojson

STAC Item requirements
	•	properties.theme → boundaries, networks, hazards, archaeology
	•	proj:epsg → 4326 for published outputs
	•	kfm:method → method/tool used (ogr2ogr, custom script, etc.)
	•	kfm:lineage → source datasets + commit ref
	•	qa:status → draft, provisional, verified

⸻

🔬 QA & Uncertainty
	•	Boundaries → validate topology, snap to known PLSS/parcel grids.
	•	Networks → cross-check against historical maps/scans.
	•	Hazards → confirm temporal attribution (decadal bins, event dates).
	•	Archaeology → ensure sensitive sites flagged with confidence + generalization.
	•	Always provide confidence levels (kfm:uncertainty) where appropriate.

⸻

🚀 Publishing
	•	Preferred formats → GeoJSON, Parquet, PMTiles.
	•	Partition large datasets (by decade, county, or theme) for efficiency.
	•	Register as STAC Items in stac/items/vectors/.
	•	Validate with CI (stac-validate.yml).
	•	Add to web/config/layers.json for viewer integration.

⸻

📑 Example STAC Item (Railroads, 1900)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_vectors_railroads_1900",
  "properties": {
    "title": "Kansas Railroads (1900)",
    "description": "Derived railroad network for Kansas circa 1900 from historic maps and GIS archive.",
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "1900-12-31T23:59:59Z",
    "proj:epsg": 4326,
    "kfm:method": "digitized + snapped to PLSS grid",
    "kfm:lineage": [
      "data/sources/networks/railroads_historic_maps.tif",
      "data/sources/networks/railroads_index.geojson"
    ],
    "processing:software": "QGIS 3.34 (Docker image ghcr.io/bartytime4life/kfm-qgis:3.34)",
    "qa:status": "provisional"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.05, 36.99],
      [-102.05, 40.00],
      [-94.59, 40.00],
      [-94.59, 36.99],
      [-102.05, 36.99]
    ]]
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../../stac/collections/vectors.json"
    }
  ],
  "assets": {
    "geojson": {
      "href": "../../../data/derivatives/vectors/networks/railroads_1900.geojson",
      "title": "Railroads 1900 (GeoJSON)",
      "type": "application/geo+json",
      "roles": ["data", "vector"]
    },
    "pmtiles": {
      "href": "../../../data/derivatives/tiles/vector/railroads_1900.pmtiles",
      "title": "Railroads 1900 (PMTiles)",
      "type": "application/vnd.pmtiles",
      "roles": ["data", "tiles"]
    }
  }
}


⸻

👩‍💻 Contributor Notes
	•	Place vector-processing scripts in scripts/vectors/.
	•	Document workflows in docs/methods/vectors.md.
	•	Generate .sha256 checksums for provenance.
	•	Use EPSG:4326 for published outputs; retain local CRS only for QA.
	•	Update STAC Items + viewer configs when new datasets are added.