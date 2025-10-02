<div align="center">

# 📖 Glossary — Kansas Frontier Matrix (MCP Standard)

**Mission:** Provide **canonical definitions** for cross-disciplinary terms used in the  
Kansas Frontier Matrix project. This glossary unifies historical, cartographic, geological, archaeological,  
and computational vocabularies to ensure clarity across experiments, datasets, pipelines, and workflows.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)  
[![Coverage](https://codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix/branch/main/graph/badge.svg)](https://codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)  
[![Ontology](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20+%20OWL--Time-purple)](https://www.cidoc-crm.org/)  
[![STAC](https://img.shields.io/badge/STAC-1.0.0-blue)](https://stacspec.org/)  
[![Simulation](https://img.shields.io/badge/Simulation-NASA--grade-green)](./templates/experiment.md)  
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)  

</div>

---

## 🔤 Alphabetical Quick Index

<!-- INDEX_START -->
<!-- INDEX_END -->

> ⚙️ The A–Z index above is **auto-generated** by `scripts/update_glossary_index.py`.  
> Do not edit between the markers; run `make update-glossary-index` to refresh.

---

## 📑 Core Scientific & MCP Terms
- **Experiment (MCP)** — Structured activity with **Problem, Hypothesis, Method, Variables, Data, Results, Conclusion**. Ensures **reproducibility and transparency**.  
- **Hypothesis** — Testable prediction framed as *If X, then Y*.  
- **Independent Variable (IV)** — Manipulated factor.  
- **Dependent Variable (DV)** — Observed/response factor.  
- **Control Variable** — Held constant to reduce bias and confounding.  
- **Reproducibility** — Ability to replicate results with the same methods, data, and configs.  
- **Uncertainty** — Degree of error/variability in measurement, interpretation, or model output.  

---

## 📜 Historical & Archival Terms
- **Primary Source** — Contemporary record of an event (e.g., diaries, treaties, maps).  
- **Secondary Source** — Interpretation produced later (e.g., history books, retrospectives).  
- **Oral History** — Indigenous/community narratives preserved and shared through speech.  
- **Treaty Boundary** — Legal demarcation of land agreements between the U.S. and Native tribes.  
- **Archival Document** — Digitized/ingested letters, deeds, journals, plats, or maps used by the Knowledge Hub.  

---

## 🗺️ Cartographic & GIS Terms
- **Cartography** — Science & art of map-making (scale, projection, symbology, generalization).  
- **Georeferencing** — Aligning scans or imagery to a coordinate system for GIS use.  
- **STAC (SpatioTemporal Asset Catalog)** — JSON metadata standard describing geospatial datasets (spatiotemporal extent, provenance).  
- **COG (Cloud-Optimized GeoTIFF)** — Raster format optimized for HTTP range requests and tiled access on the web.  
- **Vector Data** — Points, lines, polygons representing discrete features (towns, rivers, parcels).  
- **Raster Data** — Grid-based data (DEM, landcover, scanned imagery).  
- **DEM (Digital Elevation Model)** — Raster of terrain elevation (often LiDAR-derived).  
- **Hillshade** — Shaded-relief visualization derived from DEMs to highlight terrain.  

---

## 🌍 Geological & Environmental Terms
- **Stratigraphy** — Study of layered sediments/rocks to reconstruct Earth or site history.  
- **Uniformitarianism** — Principle that present-day geological processes also operated in the past.  
- **Paleoclimate Proxy** — Natural record (tree rings, pollen, cores, isotopes) used to infer past climates.  
- **Alluvial Soil** — River-deposited sediment; often fertile and settlement-associated.  
- **Erosion Model** — Computational tool simulating soil loss (e.g., hillslope or watershed erosion).  
- **Core Sample** — Cylindrical section extracted for geological/paleoenvironmental analysis.  

---

## 🏺 Archaeological Terms
- **Excavation Unit** — Defined trench/square systematically dug during fieldwork.  
- **Stratum (plural: strata)** — Distinct soil or cultural layer in archaeological context.  
- **Provenience** — Exact **3D** location of an artifact within an excavation.  
- **Context** — Association of finds within a layer; critical for interpretation.  
- **Harris Matrix** — Diagram showing stratigraphic relationships of archaeological layers.  
- **Radiocarbon Dating (C-14)** — Method for dating organic remains up to ~50,000 years.  
- **Dendrochronology** — Tree-ring dating; also yields climate signals.  

---

## 🤖 AI, Data, and Modeling Terms
- **Knowledge Graph** — Graph database of entities (**People, Places, Events, Documents**) and their relationships; core of the KFM system.  
- **Entity Recognition (NER)** — AI process that extracts people, places, dates from unstructured text.  
- **Entity Linking** — Aligns extracted mentions with canonical graph entries (e.g., “Ft. Leavenworth” → “Fort Leavenworth, KS”).  
- **Geocoding** — Converts place names to geographic coordinates.  
- **Summarization (AI)** — Condenses long historical text into concise descriptions.  
- **Simulation** — Computational model of processes/events (deterministic or stochastic).  
- **Agent-Based Model (ABM)** — Simulation of individual agents to observe emergent behavior.  
- **System Dynamics (SD)** — Aggregate modeling of stocks/flows via differential equations.  
- **Hybrid Modeling** — Integrates multiple paradigms (e.g., ABM + SD) to capture multi-scale processes.  

---

## 🌾 Kansas-Specific Terms
- **PLSS (Public Land Survey System)** — Township-range-section grid that organizes Kansas land surveys.  
- **Homestead Act (1862)** — U.S. land grant policy that shaped Kansas settlement patterns.  
- **Dust Bowl** — 1930s ecological disaster in the Great Plains driven by drought and land practices.  
- **Santa Fe Trail** — Historic 19th-century trade route crossing Kansas.  
- **Cheyenne Bottoms** — Major Kansas wetland altered by hydrologic engineering and land use.  

---

## 🔗 Cross-Disciplinary Connections
- **History ↔ GIS** — Treaty boundaries × PLSS/county overlays; time-aware maps.  
- **Geology ↔ Archaeology** — Stratigraphy informs cultural sequences and site formation.  
- **Climate ↔ Society** — Dust Bowl dynamics linked to landcover and settlement shifts.  
- **AI ↔ Archives** — OCR + NLP turn newspapers/treaties into searchable graph knowledge.  
- **Ontology ↔ MCP** — CIDOC CRM + OWL-Time harmonize semantics and temporal reasoning across datasets.  

---

✅ **Living document:**  
- Expand as new domains/datasets/methods are integrated.  
- Cross-link terms in **experiments, SOPs, STAC Items, and documentation**.  
- Treat changes as **MCP-governed, peer-reviewed, versioned artifacts**.
