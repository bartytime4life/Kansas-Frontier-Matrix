<div align="center">

# 🧩 Kansas-Frontier-Matrix — Hydrology Vector Datasets  
`data/sources/hydro/vectors/`

**Mission:** Curate **vector-format hydrological datasets**  
(rivers, lakes, reservoirs, wetlands, aquifers, wells, water quality stations)  
so they are **traceable, reproducible, and discoverable** in the STAC catalog,  
and linked into the Frontier-Matrix **timeline + knowledge graph**.  

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

- Store **processed vector hydrology layers** (GeoJSON/TopoJSON)  
- Provide canonical **geometry + attributes** for rivers, streams, reservoirs, wetlands, wells  
- Support **time-aware layers** (reservoir construction, well records, monitoring sites)  
- Maintain **provenance, licensing, and reproducibility** per MCP standards  
- Enable **cross-domain linking**: water ↔ hazards ↔ settlements ↔ documents  

---

## 📂 Directory Layout

```text
data/sources/hydro/vectors/
├── rivers_streams.geojson      # Kansas NHD rivers/streams subset
├── lakes_reservoirs.geojson    # Reservoir & lake polygons (USACE/KDHE)
├── wetlands.geojson            # USFWS NWI wetlands
├── aquifers.geojson            # Kansas aquifer extents (KGS/USGS)
├── wells_groundwater.geojson   # KGS groundwater-level monitoring wells
├── water_quality_stations.geojson # KDHE stream/lake monitoring sites
└── README.md                   # This file

⚠️ Raw shapefiles, File Geodatabases, and CAD sources → data/raw/hydro/ (ignored).
✅ Converted, simplified, and standardized outputs → data/sources/hydro/vectors/.
🗄️ Large/archival versions → data/processed/hydro/ (tracked via LFS).

⸻

🧭 Vector Schema Rules
	•	Format: GeoJSON (.geojson) preferred; TopoJSON allowed for compactness
	•	CRS: EPSG:4326 (WGS84 lon/lat) for all distributed files
	•	Attributes:
	•	Rivers/Streams: name, flow, fcode, order
	•	Reservoirs/Lakes: name, usace_id, year_built, capacity_acft
	•	Wetlands: class, system, area_ha
	•	Aquifers: name, system, extent
	•	Wells: well_id, aquifer, depth_ft, start_year, end_year
	•	Water Quality: station_id, waterbody, parameters, agency
	•	Provenance: retain original CRS/field names in _meta.json
	•	Checksums: every file accompanied by .sha256

⸻

🌍 Integration Notes
	•	Reservoirs: join with construction years → timeline animations
	•	Floodplains: integrate with scanned maps (FEMA FIRMs, 1951 flood surveys)
	•	Aquifers: linked to depletion & irrigation expansion events
	•	Wells: support long-term groundwater decline visualization
	•	Water Quality: cross-linked with KDHE/EPA advisories & hazards (e.g. HABs)

⸻

✅ Best Practices
	•	Use ogr2ogr or make vectors to convert shapefiles → GeoJSON
	•	Simplify overly complex geometries (e.g., wetlands polygons) with tolerance where needed
	•	Maintain retrieved timestamps in metadata
	•	Group time-enabled layers into STAC Collections for browsing
	•	Automate updates:

make fetch hydro-vectors
make vectors
make stac
make validate-stac


⸻

🔍 Debugging & Validation

make validate-sources   # schema JSON validation
make fetch              # fetch raw shapefiles
make vectors            # convert → GeoJSON
make stac               # build STAC items
make validate-stac      # ensure STAC 1.0.0 compliance
make checksums          # update .sha256 files


⸻

📊 Data Lifecycle

flowchart TD
  S[Vector Descriptors\n(data/sources/hydro/*.json)] -->|fetch| R[Raw Shapefiles\n(data/raw/hydro/)]
  R -->|convert| V[GeoJSON/TopoJSON\n(data/sources/hydro/vectors/)]
  V -->|index| C[STAC Items & Collections\n(stac/)]
  C -->|link| G[Knowledge Graph\n(Neo4j + Ontologies)]
  G --> VWR[MapLibre Viewer\n+ Timeline UI]

<!-- END OF MERMAID -->



⸻

📚 References
	•	USGS National Hydrography Dataset (NHD)
	•	USFWS National Wetlands Inventory (NWI)
	•	USACE Reservoir Data
	•	Kansas Geological Survey (KGS) Aquifers & Wells
	•	Kansas Department of Health & Environment (KDHE) Water Monitoring
	•	FEMA Flood Insurance Rate Maps

⸻

✦ Summary

data/sources/hydro/vectors/ provides standardized vector layers for Kansas hydrology:
rivers, reservoirs, wetlands, aquifers, wells, and water-quality stations.
They are normalized, CRS-consistent, provenance-tracked, and integrated into the
STAC catalog, knowledge graph, and Frontier-Matrix interactive viewer.