<div align="center">

# 🌾 Kansas Geo Timeline  
### **Time · Terrain · History**

**An interactive, reproducible knowledge hub for Kansas’s layered history**  
Where **terrain, climate, culture, and events** intersect across centuries.

---

## 📛 Status & Governance Badges

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../actions/workflows/codeql.yml)  
[![Trivy Scan](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../actions/workflows/trivy.yml)  
[![Pre-commit Hooks](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](../.pre-commit-config.yaml)  
[![Lint](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/lint.yml/badge.svg)](../../actions/workflows/lint.yml)  
[![Test Suite](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../actions/workflows/tests.yml)  
[![Coverage](https://img.shields.io/codecov/c/github/bartytime4life/Kansas-Frontier-Matrix)](https://codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)  
[![Docs](https://img.shields.io/badge/docs-MCP-blue.svg)](../docs/)  
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](../LICENSE)  
[![Python](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)](../pyproject.toml)  
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg?logo=docker)](../docker/)  
[![Release](https://img.shields.io/github/v/release/bartytime4life/Kansas-Frontier-Matrix)](../../releases)  

</div>

---

## 🌐 Live Demo

- **Web Viewer (MapLibre + Timeline)** → [View Demo](https://bartytime4life.github.io/Kansas-Frontier-Matrix/web/)  
- **Google Earth KMZ (progressive loading)** → [Kansas_Terrain.kmz](https://bartytime4life.github.io/Kansas-Frontier-Matrix/earth/Kansas_Terrain.kmz)  

---

## 📊 Coverage Dashboard (Per-Layer Checklist)

| Domain / Layer             | Source JSON                                | STAC Item(s)                               | Status |
|-----------------------------|--------------------------------------------|--------------------------------------------|--------|
| 🏔 **DEM & Terrain**        | [`ks_dem.json`](data/sources/dem/ks_dem.json) | [`stac/items/ks_dem.json`](stac/items/ks_dem.json) | ✅ Complete |
| 🗺 **Historic Topo Maps**   | [`usgs_historic_topo.json`](data/sources/maps/usgs_historic_topo.json) | [`stac/items/usgs_topo_1894.json`](stac/items/usgs_topo_1894.json) | 🚧 In Progress |
| 🌊 **Hydrology**            | [`ks_hydro.json`](data/sources/hydro/ks_hydro.json) | [`stac/items/ks_hydro_floods.json`](stac/items/ks_hydro_floods.json) | 🚧 In Progress |
| 🌱 **Land Cover & Soils**   | [`usda_soils.json`](data/sources/land/usda_soils.json) | [`stac/items/ks_soils_1967.json`](stac/items/ks_soils_1967.json) | ✅ Complete |
| 🪶 **Treaties & Land**      | [`treaties_index.json`](data/sources/treaties/treaties_index.json) | [`stac/items/treaty_1854.json`](stac/items/treaty_1854.json) | 🚧 In Progress |
| 🌪 **Hazards & Disasters**  | [`hazards_index.json`](data/sources/hazards/hazards_index.json) | [`stac/items/fema_disasters.json`](stac/items/fema_disasters.json) | 🚧 In Progress |
| ⛏ **Archaeology & Geology**| [`archaeology.json`](data/sources/archaeology/archaeology.json) | [`stac/items/geo_cores.json`](stac/items/geo_cores.json) | 🕒 Planned |
| 📜 **Oral Histories**       | [`oral_histories.json`](data/sources/oral/oral_histories.json) | [`stac/items/diary_snippets.json`](stac/items/diary_snippets.json) | 🕒 Planned |
| ☁ **Climate & Simulation** | [`climate_daymet.json`](data/sources/climate/climate_daymet.json) | [`stac/items/daymet_1980_2020.json`](stac/items/daymet_1980_2020.json) | 🚧 In Progress |

---

### ✅ Legend

- **✅ Complete** → Source JSON + STAC Item validated & passing CI.  
- **🚧 In Progress** → Descriptor exists, but STAC validation or assets incomplete.  
- **🕒 Planned** → Slot reserved in schema, no active JSON/Items yet.  

---

## 🧭 MCP Alignment

- **Traceability**: every dataset has a JSON descriptor (`data/sources/*.json`) and STAC item.  
- **Reproducibility**: CI validates descriptors + runs `make stac-validate`.  
- **Cross-linking**: Entities tied into the knowledge graph (Neo4j) with provenance:contentReference[oaicite:4]{index=4}.  
- **Uncertainty tracking**: Confidence values logged for NLP-extracted events:contentReference[oaicite:5]{index=5}.  

---

## 🚀 Next Steps

- [ ] Expand **Historic Topo Maps** → ingest Perry–Castañeda & KGS archives.  
- [ ] Complete **Hazards STAC** → link FEMA, NOAA, Wildfire perimeters.  
- [ ] Wire in **Oral Histories** → diarist + tribal narrative ingestion pipeline.  
- [ ] Add **Archaeology** → site excavations + stratigraphy cores:contentReference[oaicite:6]{index=6}.  
- [ ] Enrich **Climate** → paleoclimate proxies + scenario simulation datasets:contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}.  

---

<div align="center">

🔗 **Explore · Analyze · Reproduce**  
A **Kansas Frontier Matrix** project.  

</div>
```
