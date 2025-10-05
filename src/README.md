<div align="center">

# 🧩 Kansas Frontier Matrix — `src/` Codebase

**ETL · AI/ML · Knowledge Graph · API Services**  
_The beating heart of the Kansas Frontier Matrix stack._

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/hooks-pre--commit-orange)](https://pre-commit.com)
[![Docs · MCP](https://img.shields.io/badge/docs-MCP-blue.svg)](../docs/)
[![License: MIT/CC-BY](https://img.shields.io/badge/license-MIT%20%7C%20CC--BY-green)](../LICENSE)

</div>

---

## 📚 Purpose
The `src/` directory contains all **core logic** for the Kansas Frontier Matrix:

- ⚙️ **ETL Pipelines** → reproducible ingestion & transformation (COGs, GeoJSON, Parquet)  
- 🤖 **AI/ML Modules** → NLP, entity linking, summarization, confidence scoring  
- 🕸 **Knowledge Graph** → Neo4j integration (CIDOC CRM, OWL-Time, PeriodO)  
- 🔌 **API Layer** → FastAPI / GraphQL endpoints powering the web app + KML exports  

> Think of `src/` as the **engine room** where raw data becomes structured, searchable knowledge.

---

## 🏗 Directory Structure
```text
src/
├─ pipelines/      # ETL jobs: fetch, transform, load (scans, rasters, vectors, docs)
├─ nlp/            # NLP + AI/ML enrichment (NER, linking, summarization)
├─ graph/          # Graph schema + Neo4j integration (Cypher utils, entity upserts)
├─ api/            # FastAPI/GraphQL services (REST endpoints, resolvers)
├─ utils/          # Shared helpers (logging, config, checksum validation)
└─ __tests__/      # Optional inline unit tests
````

🧭 For architectural context see [`src/ARCHITECTURE.md`](./ARCHITECTURE.md).

---

## 🚀 Quickstart (Dev Setup)

```bash
# 1. create environment
python -m venv .venv && source .venv/bin/activate
# 2. install deps
pip install -r requirements.txt
# 3. run ETL (example: DEMs)
make fetch cogs stac
# 4. launch API
uvicorn src.api.main:app --reload --port 8000
```

Visit → **[http://localhost:8000/docs](http://localhost:8000/docs)** for interactive Swagger UI.

---

## 🧭 Data Flow

```mermaid
flowchart LR
  A["Raw Sources<br/>Scans · Rasters · Vectors · Documents"] --> B["pipelines/<br/>ETL → COG · GeoJSON · Parquet"]
  B --> C["nlp/<br/>NER · Geocoding · Summaries"]
  C --> D["kg/<br/>Neo4j · Entities · Relations"]
  D --> E["api/<br/>FastAPI + GraphQL · /events · /entity · /search"]
  E --> F["Frontend<br/>React + MapLibreGL · Timeline · Map · Story Mode"]

  %% Styles (GitHub-safe)
  classDef src fill:#d7ebff,stroke:#0078d4,color:#111;
  classDef ai fill:#eafaf1,stroke:#1a7f37,color:#111;
  classDef kg fill:#fff8e1,stroke:#ffb300,color:#111;
  classDef api fill:#ede7f6,stroke:#6a1b9a,color:#111;
  classDef ui fill:#d1ffd7,stroke:#1a7f37,color:#111;

  class A,B src;
  class C ai;
  class D kg;
  class E api;
  class F ui;
```

---

## 🔬 Core Technologies

| Domain             | Library / Framework                   |
| ------------------ | ------------------------------------- |
| API                | **FastAPI**, **GraphQL (Strawberry)** |
| Graph              | **Neo4j / Cypher**, `py2neo`          |
| NLP / ML           | **spaCy**, Transformers (BART / T5)   |
| Geospatial         | **rasterio**, **rio-cogeo**, **GDAL** |
| Catalog / Metadata | **pystac**, **jsonschema**            |
| Language           | **Python 3.11 +**                     |

---

## 🧪 Testing

```bash
pytest src --maxfail=1 --disable-warnings -v --cov=src
```

Tests live in `tests/python/` and optional inline `src/__tests__/`.

---

## 🛡 Quality & Security

* 🧹 **Pre-commit hooks:** `ruff`, `black`, `mypy`
* 🧠 **CodeQL:** static analysis via GitHub Actions
* 🧱 **Trivy:** dependency & container scan
* 🧾 **STAC Validation:** verifies geospatial metadata compliance

---

## 🎯 Developer Workflows

### Adding a New Dataset

1. Add manifest → `data/sources/{id}.json`
2. Run ETL:

   ```bash
   make fetch cogs stac
   ```
3. Add pipeline → `src/pipelines/{new_source}.py`
4. Extend graph → `src/graph/schema.py`
5. Document in `docs/sop.md` + add tests.

### Adding a New API Endpoint

1. Create route → `src/api/routes/{endpoint}.py`
2. Annotate with OpenAPI decorators
3. Add tests → `tests/api/test_{endpoint}.py`

---

## 📦 Example API Calls

```http
GET /events?start=1850-01-01&end=1870-12-31&bbox=-100,37,-94,40
```

Returns all Kansas events in range as GeoJSON + AI summaries.

```http
GET /entity/fort-larned
```

Returns linked events, documents, and geospatial context.

---

## 🎨 Layer & Timeline Integration

Color tokens and time windows for the frontend reside in
[`web/config/layers.json`](../web/config/layers.json).
See **[Layer Timeline Legend](./ARCHITECTURE.md#-layer-timeline-legend)**
for canonical visualization styles.

---

## 🗂 Documentation

* 📖 [`ARCHITECTURE.md`](./ARCHITECTURE.md) — component relationships
* 🧭 [`../docs/`](../docs/) — SOPs · experiments · model cards
* 🧪 [`../tests/`](../tests/) — test suites & coverage
* ⚙️ `.github/workflows/` — CI/CD automation

---

## 🤝 Contributing

Follow **MCP (Master Coder Protocol)**:

1. Document before code (SOP / experiment / architecture).
2. Reproduce everything (checksum · schema · logs).
3. Add tests for every change.
4. Include provenance metadata in PR descriptions.

See [`CONTRIBUTING.md`](../CONTRIBUTING.md).

---

## 📖 References

* **STAC 1.0.0** — SpatioTemporal Asset Catalog standard
* **CIDOC CRM + OWL-Time + PeriodO** — semantic and temporal ontologies
* **Kansas GIS Hub · USGS 3DEP · NOAA NCEI · FEMA OpenFEMA · KSHS** — primary data sources

---

<div align="center">

✨ *“The `src/` directory is where Kansas history is translated into a living, queryable atlas.”* ✨

</div>
