<div align="center">

# 🧭 Kansas Frontier Matrix — **Root Architecture Overview**

*“Time · Terrain · History · Knowledge Graphs”*

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](./.github/workflows/site.yml)
[![Pages Deploy](https://img.shields.io/github/deployments/bartytime4life/Kansas-Frontier-Matrix/github-pages?label=Pages%20Deploy)](https://bartytime4life.github.io/Kansas-Frontier-Matrix/)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](./.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](./.github/workflows/codeql.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![License: MIT | CC-BY](https://img.shields.io/badge/License-MIT%20(code)%20%7C%20CC--BY%20(data)-blue)](./LICENSE)

</div>

---

## 📚 Table of Contents
- [Mission](#mission)
- [Architecture at a Glance](#architecture-at-a-glance)
- [Layered Design](#layered-design)
  - [1) Data Ingestion (ETL)](#1-data-ingestion-etl)
  - [2) AI/ML Enrichment](#2-aiml-enrichment)
  - [3) Knowledge Graph](#3-knowledge-graph)
  - [4) API Layer](#4-api-layer)
  - [5) Frontend Web App](#5-frontend-web-app)
- [Reproducibility & Observability](#reproducibility--observability)
- [Open Science & Semantic Interoperability](#open-science--semantic-interoperability)
- [Extending the System](#extending-the-system)
- [Quickstart Snippets](#quickstart-snippets)
- [Repository & Data Layout (Monorepo)](#repository--data-layout-monorepo)
- [Status & Roadmap](#status--roadmap)
- [References & Further Reading](#references--further-reading)

---

## Mission

**Kansas Frontier Matrix** is a multi-disciplinary, open-source spatiotemporal knowledge hub for Kansas—  
integrating geography, climate, culture, and events into a unified map + timeline + knowledge-graph  
experience designed for researchers, educators, and the public.

---

## Architecture at a Glance

```mermaid
flowchart TD
  A["Sources<br/>scans · rasters · vectors · documents"] --> B["ETL Pipeline<br/>Makefile · Python · checksums"]
  B --> C["Processed Layers<br/>COGs · GeoJSON · Parquet"]
  B --> I["AI/ML Enrichment<br/>NER · geocoding · summarization · linking"]
  C --> D["STAC Catalog<br/>collections · items · assets"]
  D --> E["Config Build<br/>app.config.json · layers.json"]
  D --> H["Knowledge Graph<br/>Neo4j · CIDOC CRM · OWL-Time"]
  I --> H
  H --> J["API Layer<br/>FastAPI · GraphQL"]
  D --> J
  J --> F["Frontend (React + MapLibreGL)<br/>timeline · search · filters"]
  E --> F
  E --> G["Google Earth Exports<br/>KML · KMZ"]
````

*This end-to-end flow transforms heterogeneous historical assets into reproducible geospatial layers, a semantically rich graph, and an interactive UI (timeline + map).*

---

## Layered Design

### 1) Data Ingestion (ETL)

* **Sources:** historical maps, climate tables, vectors, scanned documents, REST APIs (USGS, NOAA, FEMA, state archives).
* **Pipeline:** Makefile-orchestrated Python ETL normalizes to open formats (COG GeoTIFF, GeoJSON), creates provenance checksums, and emits **STAC** metadata.
* **Catalog:** `data/sources/*.json` manifests point to remote data—no heavy binaries in Git.

> **Why STAC / COG / GeoJSON?** Portable, cache-friendly, open, and discoverable by both humans and machines.

---

### 2) AI / ML Enrichment

* **NLP (spaCy + Transformers):** NER for People / Places / Events / Dates; geoparsing + geocoding (GNIS); summarization (BART / T5) for tooltips & story panels.
* **Entity Linking:** fuzzy + context scoring aligns mentions to canonical graph nodes (e.g. “Fort Larned”) and logs confidence.
* **Multi-source correlation:** cross-checks maps, texts, and time-series to surface credible “change” insights (e.g. river-channel shifts or ghost-town emergence).

---

### 3) Knowledge Graph

* **Store:** Neo4j / RDF with `Person`, `Place`, `Event`, `Document` nodes; relations like `OCCURRED_AT`, `MENTIONS`, `PARTICIPATED_IN`.
* **Semantics:** aligned to **CIDOC CRM** (cultural heritage) + **OWL-Time** (temporal intervals); can tag historical periods via **PeriodO**.
* **Provenance:** each fact records source + confidence; supports rule-based inference and uncertainty visualization.

---

### 4) API Layer

* **FastAPI + GraphQL** endpoints expose time-filtered events, spatial queries, entity dossiers, and search.
* Designed for lightweight clients—heavy traversals resolve server-side for speed & clarity.

---

### 5) Frontend Web App

* **React SPA** with **MapLibre GL JS** + **Canvas timeline** for performant visualization.
* **UI features:** layer toggles, legends, search, AI-summary panels, “story mode”; responsive + accessible.
* **Overlays:** topo/DRG maps, treaties & cessions, hydrology, DEM hillshade, hazards—all STAC-driven.

---

## Reproducibility & Observability

* **Docs-first (MCP):** architecture / SOPs / experiments / model cards under `docs/`.
* **CI/CD:** pre-commit, tests (Python + JS), STAC validation, site build; atomic monorepo updates.
* **Integrity:** DVC / LFS pointers for large artifacts; deterministic ETL; JSON Schema + STAC checks enforced in CI.

---

## Open Science & Semantic Interoperability

* **Open formats:** COG, GeoJSON, STAC; optionally exportable as DCAT or JSON-LD catalogs.
* **Ontologies:** CIDOC CRM + OWL-Time + PeriodO enable cross-domain linking (treaties ↔ places ↔ events).

---

## Extending the System

1. **Plan & Document:** add `data/sources/my_new_dataset.json` with id, title, urls, temporal, bbox, license.
2. **Fetch & Convert:** `make fetch` → create COG / GeoJSON, reproject WGS84, generate STAC item.
3. **Graph Ingest:** run ETL to upsert places/events/docs; NLP-enrich if textual.
4. **Expose & Style:** edit `web/config/layers.json` → add legend / popup fields.

> **Tip:** For Kansas GIS Archive data (parcels, soils, historic maps) prefer GeoTIFF/COG for rasters, GeoJSON for vectors; include map year for the time slider.

---

## Quickstart Snippets

**Fetch & Build Data**

```bash
make fetch          # pull remote sources from data/sources/*.json
make cogs vectors   # convert rasters→COGs, vectors→GeoJSON (EPSG:4326)
make stac           # generate STAC items & validate
```

**Minimal STAC Item**

```json
{
  "type": "Feature",
  "id": "usgs_topo_larned_1894",
  "properties": { "datetime": "1894-01-01T00:00:00Z", "proj:epsg": 4326 },
  "assets": {
    "cog": {
      "href": "data/cogs/overlays/usgs_topo_larned_1894.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  },
  "bbox": [-99.4, 38.1, -99.0, 38.4]
}
```

**API Sketch**

```http
GET /api/events?start=1850-01-01&end=1870-12-31&bbox=-100,37,-94,40
GET /api/entity/fort-larned
GET /api/search?q=cheyenne%20bottoms
```

---

## Repository & Data Layout (Monorepo)

```
Kansas-Frontier-Matrix/
├─ src/            # ETL, AI/ML, graph code
├─ web/            # React app (MapLibre + Canvas timeline)
├─ data/
│  ├─ sources/     # dataset manifests (JSON pointers)
│  ├─ raw/         # fetched raw data (DVC/LFS pointers)
│  ├─ processed/   # COG, GeoJSON, CSV outputs
│  └─ stac/        # STAC catalog (collections/items)
├─ docs/           # architecture, SOPs, model cards, experiments
├─ tools/          # helper scripts (fetch, georef, STAC gen)
└─ .github/        # Actions, issue & PR templates
```

---

## Status & Roadmap

| Stage                                                        | Status         |
| ------------------------------------------------------------ | -------------- |
| Baseline ETL & STAC Catalog                                  | ✅ Complete     |
| Web UI skeleton (map + timeline)                             | ✅ Stable       |
| Expanded datasets (treaties, hazards, soils, historic topos) | 🚧 In Progress |
| AI “site dossiers” / Q&A assistant                           | 🚧 Prototype   |
| Google Earth exports / story maps / classroom modules        | 🎯 Planned     |

> Contributions welcome — documentation-first, reproducible PRs, and dataset manifests with clear licenses.

---

## References & Further Reading

* **System overview:** *Kansas Frontier Matrix – Hub Design*
* **AI / ML internals:** *Developer Documentation*
* **Web UI:** *Web UI Design Document*
* **File / Data & STAC:** *File and Data Architecture*
* **Monorepo & CI/CD:** *Monorepo Repository Design*
* **Docs-First (MCP):** *Scientific Method / Master Coder Protocol*

---

<div align="center">

**Made with ❤️ for Kansas history, cartography, climate, and community.**
*Automation with Integrity — Every Workflow Proven.*

</div>
```
