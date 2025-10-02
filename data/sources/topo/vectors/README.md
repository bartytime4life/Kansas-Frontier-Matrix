<div align="center">

# 🧩 Kansas-Frontier-Matrix — Topographic Vector Datasets  
`data/sources/topo/vectors/`

**Mission:** Curate **vector-format topographic datasets** (contours, spot elevations, slope/aspect sectors, derived landforms)  
so they are **traceable, reproducible, and discoverable** in the STAC catalog,  
and fully integrated into the Frontier-Matrix **timeline + knowledge graph**.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../../.pre-commit-config.yaml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)  
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../../../../.github/workflows/automerge.yml)  
[![Docs](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/docs.yml/badge.svg)](../../../../.github/workflows/docs.yml)  
[![Coverage](https://img.shields.io/codecov/c/github/bartytime4life/Kansas-Frontier-Matrix)](https://app.codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../../LICENSE)  

</div>

---

## 🎯 Purpose

- Provide **derived vector layers** from DEMs and historic topo data  
- Represent **contours, spot elevations, slope/aspect classes, landform polygons**  
- Enable **cross-era comparison** of terrain representation (historic quads vs LiDAR-derived)  
- Link to **hydrology, land cover, and hazards** for integrated analysis  
- Ensure **schema, provenance, and reproducibility** for all topo-derived vectors  

---

## 📂 Directory Layout

```text
data/sources/topo/vectors/
├── contours_10m.geojson        # Derived 10 m contour lines from DEMs
├── contours_100ft.geojson      # Generalized contours from historic topo sheets
├── spot_elevations.geojson     # Elevation benchmarks, survey points
├── slope_classes.geojson       # Slope bins (0–2%, 2–5%, 5–15%, >15%)
├── aspect_sectors.geojson      # Aspect polygons (N, NE, E, etc.)
├── landforms.geojson           # Landform classification polygons
└── README.md                   # This file

⚠️ Raw rasters/contour shapefiles → data/raw/topo/ (ignored).
✅ Converted/simplified outputs → data/sources/topo/vectors/.
🗄️ Large statewide layers → data/processed/topo/ (LFS).

⸻

🧭 Vector Schema Rules
	•	Format: GeoJSON (.geojson) preferred; TopoJSON optional for light layers
	•	CRS: EPSG:4326 (WGS84 lon/lat)
	•	Attributes:
	•	Contours: elev_m or elev_ft, source, year
	•	Spot Elevations: elev_ft, benchmark_id, source
	•	Slope Classes: slope_pct, class, source_dem
	•	Aspect Sectors: azimuth, sector, source_dem
	•	Landforms: landform_type, method (TPI, geomorphons, etc.)
	•	Metadata: Original CRS, methods, tolerance → _meta.json
	•	Checksums: .sha256 for every file

⸻

🌍 Integration Notes
	•	Contours: from USGS DEMs, 3DEP LiDAR, or historic topo digitization
	•	Spot elevations: tie to GLO/USGS benchmarks, triangulation stations
	•	Slope/aspect: link to hazards (erosion, wildfire spread, agriculture suitability)
	•	Landforms: cross-domain with soils, vegetation, settlement locations
	•	Timeline: compare pre-dam vs post-dam contours; integrate with historic maps

⸻

✅ Best Practices
	•	Convert with ogr2ogr or workflow scripts:

make fetch topo-vectors
make vectors
make stac
make validate-stac


	•	Simplify geometries for statewide datasets
	•	Maintain retrieved timestamps + provenance logs
	•	Flag low-confidence derivations (historic contour digitizations)

⸻

🔍 Debugging & Validation

make validate-sources   # schema compliance
make fetch              # download raw contour/well shapefiles
make vectors            # convert → GeoJSON
make stac               # build STAC items
make validate-stac      # validate STAC 1.0.0
make checksums          # update .sha256 integrity files


⸻

📊 Data Lifecycle

flowchart TD
  S[Topo Vector Descriptors\n(data/sources/topo/*.json)] -->|fetch| R[Raw Shapefiles\n(data/raw/topo/)]
  R -->|convert| V[GeoJSON/TopoJSON\n(data/sources/topo/vectors/)]
  V -->|index| C[STAC Items & Collections\n(stac/)]
  C -->|link| G[Knowledge Graph\n(Neo4j + Ontologies)]
  G --> VWR[MapLibre Viewer\n+ Timeline UI]

<!-- END OF MERMAID -->



⸻

📚 References
	•	USGS Contours & Benchmarks
	•	USGS 3DEP DEM-derived contours
	•	Kansas GIS Archive Hub — digitized topo vector data
	•	Kansas Geological Survey — elevation & slope studies
	•	NRCS — slope & landform classification guides

⸻

✦ Summary

data/sources/topo/vectors/ defines standardized vector layers derived from topographic data — contours, spot elevations, slope/aspect, and landforms.
They are CRS-normalized, provenance-tracked, and integrated into the STAC catalog, Frontier-Matrix knowledge graph, and interactive viewer.