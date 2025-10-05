<div align="center">

# 🧩 Kansas Frontier Matrix — Data Pipelines  
`src/pipelines/README.md`

**Time · Terrain · History · Knowledge Graphs**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)

</div>

---

## 🎯 Purpose

The `src/pipelines/` module houses the **ETL (Extract-Transform-Load)** and **AI/ML enrichment** pipelines that power the Kansas Frontier Matrix (KFM).  
These scripts transform heterogeneous Kansas datasets—maps, climate series, land records, and historical texts—into standardized, provenance-tracked layers ready for:

- 🗺 **Spatiotemporal mapping** (GeoJSON + COG GeoTIFF)  
- 🧠 **Knowledge-graph ingestion** (Neo4j / RDF)  
- ⚙️ **Semantic linking** via CIDOC CRM + OWL-Time  
- 🔍 **Interactive discovery** through the web UI and API  

The directory implements MCP’s *documentation-first* and *reproducibility* principles: every script logs inputs, outputs, parameters, and checksums.

---

## 🏗 Pipeline Architecture

```mermaid
flowchart TD
    A["Raw Sources (scans · rasters · vectors · texts)"]
      --> B["Extract → download / fetch / OCR"]
      --> C["Transform → clean · normalize · geocode"]
      --> D["Load → GeoJSON · COG · Parquet · Graph DB"]

    C --> I["AI / ML Enrichment (NER · summarization · linking)"]
    I --> H["Knowledge Graph (Neo4j · CIDOC CRM · OWL-Time)"]
    D --> H
    H --> J["API Layer → FastAPI / GraphQL"]
    J --> F["Frontend → React / MapLibre timeline map"]
````

<!-- END OF MERMAID -->

Each ETL stage is modular and reproducible:

| Stage                | Description                                                                                                        | Key Tools                                               |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------ |
| **Extract**          | Fetch raw data from external APIs or archives (USGS, NOAA, FEMA, KHS, etc.).  Handles OCR for scanned PDFs / maps. | `requests`, `aiohttp`, `pytesseract`, `pdfplumber`      |
| **Transform**        | Standardize formats → GeoJSON, CSV, COG; clean fields; geocode places; normalize dates.                            | `pandas`, `geopandas`, `rasterio`, `rio-cogeo`, `geopy` |
| **Load**             | Upsert processed outputs to data/processed and Neo4j graph; generate STAC items + checksums.                       | `neo4j-driver`, `jsonschema`, `hashlib`                 |
| **AI/ML Enrichment** | Apply NLP (entity extraction, summarization, fuzzy linking) and cross-source correlation.                          | `spaCy`, `transformers`, `sentence-transformers`        |

---

## 📂 Directory Layout

```
src/pipelines/
├── __init__.py
├── fetch/                 # data-source connectors (USGS, NOAA, FEMA, KHS etc.)
│   ├── noaa_ingest.py
│   ├── usgs_ingest.py
│   ├── fema_ingest.py
│   └── kansas_memory_ingest.py
├── transform/             # normalization & conversion utilities
│   ├── geocode_utils.py
│   ├── raster_to_cog.py
│   ├── vector_to_geojson.py
│   └── text_cleaner.py
├── enrich/                # AI / ML processing modules
│   ├── nlp_entities.py
│   ├── summarizer.py
│   ├── entity_linker.py
│   └── correlate_sources.py
├── load/                  # loaders → Neo4j & STAC
│   ├── stac_writer.py
│   ├── graph_loader.py
│   └── checksum_utils.py
└── pipeline_runner.py     # orchestrator · Makefile entrypoint
```

Each submodule can be executed standalone for testing, or orchestrated via the project-level `Makefile`:

```bash
# Rebuild all pipelines
make pipelines

# Or run a single stage
python src/pipelines/fetch/noaa_ingest.py --year 2020
```

---

## 🔬 AI / ML Workflow Summary

1. **Named Entity Recognition (NER)** – `spaCy` model fine-tuned on Kansas texts to extract `PERSON`, `PLACE`, `DATE`, `EVENT`.
2. **Geocoding** – Resolve place names via USGS GNIS API; attach lat/long & county context.
3. **Summarization** – `BART-large-CNN` / `T5` models create concise summaries for documents and site dossiers.
4. **Entity Linking & Scoring** – Fuzzy matching + context windowing align mentions to canonical graph nodes with confidence scores.
5. **Cross-Modal Correlation** – Compare text vs map vs sensor data to flag verified historical changes (e.g., floodplain shift).

---

## 🧱 Data Outputs & Standards

| Output          | Format                  | Destination               | Standard                  |
| :-------------- | :---------------------- | :------------------------ | :------------------------ |
| Raster Layers   | Cloud-Optimized GeoTIFF | `data/processed/rasters/` | STAC 1.0 · OGC COG        |
| Vector Layers   | GeoJSON / TopoJSON      | `data/processed/vectors/` | GeoJSON 1.0               |
| Tables          | CSV / Parquet           | `data/processed/tables/`  | CSVW · DCAT               |
| Knowledge Graph | Neo4j DB                | `graph/`                  | CIDOC CRM · OWL-Time      |
| Metadata        | JSON                    | `data/stac/`              | STAC · schema.org Dataset |

All assets include **SHA-256** checksums and provenance metadata (source URL, license, ETL timestamp).

---

## 🧰 Configuration & Logging

* **Config** files live in `config/` (YAML/JSON) defining paths, API keys, CRS codes, and STAC templates.
* **Logging** uses Python’s `logging` module with rotating file handlers → `logs/pipelines/*.log`.
* **Error Handling** wraps each task with try/except to ensure a failure in one source does not halt the entire ETL.

Example log line:

```
[2025-10-05 14:22:01] INFO | usgs_ingest | Fetched 12 new DEM tiles (2.3 GB) in 214 s ✔
```

---

## 🔁 Reproducibility · CI/CD Integration

* **Makefile** targets link directly into GitHub Actions: every commit runs `make validate` and `make stac-check`.
* **STAC Validation** ensures metadata compliance before merge.
* **Containerized runs** (Docker + Compose) guarantee identical environments across contributors.
* **DVC integration** (coming soon) adds data version hashes to each ETL artifact.

---

## 📘 Developer Notes

* Follow PEP-8 style and Google-style docstrings for functions and modules.
* Each script begins with a `@MCP-LOG` header summarizing its purpose, inputs, outputs, and expected runtime.
* Add unit tests in `tests/pipelines/` whenever you extend a module.
* When introducing a new data source, create a matching manifest under `data/sources/` and cite its license and URL.

---

## 📈 Example Workflow

```bash
# 1 · Fetch raw data from registered sources
make fetch

# 2 · Process raster + vector data → standard formats
make process

# 3 · Run AI enrichment (NER + summary)
make enrich

# 4 · Update STAC catalog and load graph database
make stac graph
```

Each step logs provenance → `logs/pipelines/` and outputs reproducible artifacts in `data/processed/`.

---

## 📎 References & Further Reading

* *Kansas Frontier Matrix — AI System Developer Docs*
* *File & Data Architecture Guide*
* *Scientific Modeling & Simulation (NASA-Grade Guide)*
* *Integrating Historical, Cartographic, and Geological Research (MCP Reference)*

---

<div align="center">

**Kansas Frontier Matrix © 2025 · Open Knowledge · MIT License (code) | CC-BY 4.0 (data)**
*“Document the past so the future can reproduce it.”*

</div>

