<div align="center">

# ✅ Kansas Frontier Matrix — Tests (`/tests/`)

**Mission:** Ensure the **robustness, reproducibility, and scientific integrity**  
of all components in the Kansas Frontier Matrix (KFM) stack.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)  
[![Test Suite](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../.github/workflows/tests.yml)  
[![Coverage](https://img.shields.io/codecov/c/github/bartytime4life/Kansas-Frontier-Matrix)](https://codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../.github/workflows/pre-commit.yml)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../docs/)  

</div>

---

## 🎯 Purpose

The `/tests/` directory holds **unit, integration, and system-level test suites** for  
all Kansas Frontier Matrix modules — from **Python ETL pipelines** to the  
**React/MapLibre web UI**.  

Following **Master Coder Protocol (MCP)**, all tests must be:
- **Reproducible** — deterministic results, no hidden state.  
- **Transparent** — logs, assertions, and provenance recorded.  
- **Cross-disciplinary** — cover history, GIS, climate, and AI pipelines.  
- **CI/CD integrated** — every commit must pass before merging.  

---

## 📚 Structure

tests/
├── python/          # Pytest-based unit + integration tests for ETL, AI/ML, graph DB
│   ├── test_ingest.py
│   ├── test_nlp.py
│   ├── test_graph.py
│   └── conftest.py
├── js/              # Jest/React Testing Library tests for Web UI
│   ├── timeline.test.js
│   ├── mapview.test.js
│   └── search.test.js
├── schemas/         # JSON Schema validation tests (STAC, configs, descriptors)
│   ├── test_stac_validation.py
│   └── test_schema_compliance.py
├── data/            # Golden test datasets (small, reproducible)
│   ├── sample_diary.txt
│   ├── ks_county_sample.geojson
│   └── dem_sample.tif
└── e2e/             # End-to-end system tests (API + UI integration)
├── test_api_endpoints.py
├── test_graphql_queries.py
└── test_browser_flows.js

---

## 🧪 Types of Tests

### 🔹 Unit Tests
- Python ETL: verify date parsing, geocoding, STAC generation.  
- NLP: check NER extraction of people, places, events.  
- Graph DB: validate Cypher queries & schema consistency.  

### 🔹 Integration Tests
- ETL pipeline end-to-end on sample datasets.  
- UI: timeline ↔ map synchronization.  
- API: FastAPI/GraphQL endpoints returning expected structures.  

### 🔹 Schema Validation
- Every dataset descriptor (`data/sources/*.json`) checked against JSON Schema.  
- STAC collections/items validated against **STAC 1.0.0 spec** [oai_citation:0‡File and Data Architecture for the Kansas Frontier Matrix Project.pdf](file-service://file-3dXLjptkFjdMerKJTvzzW7).  

### 🔹 End-to-End
- Spin up containers (ETL, Neo4j, API, Web UI).  
- Run simulated user flows:  
  1. Ingest sample treaty → Graph DB.  
  2. Query treaty → Displayed on timeline + map.  
  3. AI summary generated → Shown in UI panel.  

---

## ⚙️ Running Tests

### Python
```bash
pytest tests/python -v --cov=src

JavaScript (Web UI)

cd web && npm test

Schema Validation

pytest tests/schemas

End-to-End

make test-e2e


⸻

🔄 CI/CD Integration
	•	GitHub Actions runs full test suite on every PR (.github/workflows/tests.yml).
	•	Coverage reports uploaded to Codecov.
	•	Security scans via Trivy & CodeQL.
	•	Pre-commit hooks enforce linting & black/ruff/eslint before tests.

⸻

🧭 Guidelines for Contributors
	•	Write tests before/with code (TDD encouraged).
	•	Use small deterministic datasets under tests/data/.
	•	Mark slow tests with @pytest.mark.slow.
	•	Document unusual test cases in /docs/experiment.md.
	•	All new datasets must include schema validation tests.

⸻

🚀 Roadmap
	•	Add browser-based Cypress tests for UI workflows.
	•	Expand property-based testing (Hypothesis for Python).
	•	Integrate load testing (Locust) for API endpoints.
	•	Add snapshot testing for timeline render states.

⸻

🔗 Related Docs:
	•	Architecture Overview ￼
	•	Web UI Design ￼
	•	Data & File Architecture ￼

⸻


<div align="center">


🧪 Testing isn’t an afterthought. It’s the backbone of trust in KFM’s knowledge graph.

</div>
```