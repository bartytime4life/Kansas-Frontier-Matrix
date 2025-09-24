# Kansas-Frontier-Matrix — Test Suite

This directory contains the automated test suite for the **Kansas-Frontier-Matrix** stack.  
The tests provide **mission-grade validation** of data, metadata, and code wiring. They are written in
**pytest** and designed to skip gracefully when files are not yet present (scaffolding stage).

---

## Objectives

- Validate **STAC 1.0.0** metadata (`stac/catalog.json`, `stac/collections/*.json`, `stac/items/*.json`) for conformance.  
- Cross-check **data provenance**: filenames ↔ IDs, bbox ↔ geometry, temporal intervals.  
- Confirm **geospatial source configs** (YAML/JSON in `data/`) parse correctly and contain required keys.  
- Ensure **core web assets** (`web/app.js`, CSS, logos, favicon) exist for the public site.  
- Validate **web configs** (`web/app.config.json`, `web/layers.json`) against JSON Schemas.  
- Quantify potential **gaps or uncertainty** in datasets as they’re added (audit-aligned).  
- Provide hooks for **multi-modal ingestion tests** — historical texts, maps, hydrology, oral histories.

---

## Test Flow

```mermaid
flowchart TD
  %% --- Inputs ---
  subgraph Repo
    A1["stac/catalog.json"]
    A2["stac/collections/*.json"]
    A3["stac/items/*.json"]
    B1["data/sources/*.yml"]
    C1["web/app.js, CSS, assets"]
    C2["web/app.config.json, web/layers.json"]
  end

  %% --- Test runners ---
  subgraph Pytest
    T1["test_stac.py"]
    T2["test_sources.py"]
    T3["test_web.py\n(planned)"]
    T4["test_web_configs.py"]
  end

  A1 --> T1
  A2 --> T1
  A3 --> T1
  B1 --> T2
  C1 --> T3
  C2 --> T4

  %% --- Outputs ---
  subgraph Results
    R1["Clear Failures"]
    R2["Graceful Skips"]
    R3["Green → Site Build Ready"]
  end

  T1 --> R1 & R2 & R3
  T2 --> R1 & R2 & R3
  T3 --> R1 & R2 & R3
  T4 --> R1 & R2 & R3

  R3 --> Site["Static Site / Map UI"]
````

---

## Current Test Modules

* **`test_stac.py` — Validates STAC Collections and Items**

  * `type`, `stac_version`, `id`
  * bbox containment vs. geometry
  * `datetime` / `start_datetime` / `end_datetime`
  * asset media types (prefer COG/GeoTIFF where applicable)
  * collection ↔ item link integrity

* **`test_sources.py` — Sanity checks for `data/sources/**`**

  * JSON/YAML validity
  * required fields present
  * paths/URLs plausibility

* **`test_web_configs.py` — Schema validation for web configs**

  * Validates `web/app.config.json` against `web/config/app.config.schema.json`
  * Validates `web/layers.json` against `web/config/layers.schema.json`
  * Ensures **unique** layer IDs

* **`test_web.py` (planned)** — Frontend smoke checks

  * Existence of critical assets before site build/deploy (`web/app.js`, CSS, icons)

---

## Test ↔ Architecture Map (Knowledge Hub)

| Test file (status)                            | Knowledge-hub layer(s)                     | Primary intent                                                               |
| --------------------------------------------- | ------------------------------------------ | ---------------------------------------------------------------------------- |
| `test_stac.py`                                | Data Repositories (STAC-like catalog)      | Schema conformance; spatial/temporal sanity; collection↔item linkage         |
| `test_sources.py`                             | Ingestion & Processing (source configs)    | Source config validity; required keys; URL/path plausibility                 |
| `test_web_configs.py`                         | Frontend Config Layer (viewer + layers)    | JSON Schema conformance; property names; unique IDs                          |
| `test_web.py` *(planned)*                     | Frontend Application (static site assets)  | Presence of required assets before build/deploy                              |
| *(future)* `test_ingest_texts.py`             | Ingestion → NLP extraction                 | OCR/NLP smoke on sample texts; provenance stubs                              |
| *(future)* `test_graph_entities_relations.py` | Knowledge Graph DB                         | Node/edge label policy; required properties (date/place normalization)       |
| *(future)* `test_graph_query_api.py`          | Query API (REST/GraphQL)                   | Basic graph queries: by time, place, entity type, confidence                 |
| *(future)* `test_uncertainty_qc.py`           | Pipeline ↔ Graph ↔ UI (confidence tagging) | Confidence fields present; rendering rules (opacity/error bars)              |
| *(future)* `test_layers_catalog_integrity.py` | Data Repositories (layer catalog)          | Each layer has source URL, license, CRS, temporal coverage, processing notes |
| *(future)* `test_storymap_hooks.py`           | Frontend Application (story-map mode)      | Narrative/chapters schema and hooks                                          |
| *(future)* `test_hydrology_models_io.py`      | Ingestion + Data Repos (hydrology)         | Endpoints present; model I/O manifests                                       |

Use this table to align new tests with the correct architectural layer(s) and reviewers.

---

## Running Tests

From the repo root:

```bash
pytest -q
```

Common options:

* `-k "stac"` → run only STAC validation tests
* `-s` → show stdout/logs
* `--maxfail=1` → stop after first failure
* `-vv` → verbose mode (helpful for parametric cases)

---

## Debugging & Skips

* If no STAC items/collections exist yet, tests **skip** to avoid noise (scaffolding-friendly).
* JSON/YAML parse errors raise **assertions** with file path + parser message.
* Skips are expected during early scaffolding; **failures** indicate required corrections.

---

## Adding New Tests

1. Place new tests in this directory, naming files `test_*.py`.
2. Reuse helpers from existing tests (path loaders, JSON readers).
3. Prefer `@pytest.mark.parametrize` to scale checks over many files.
4. Keep dependencies minimal (**stdlib + pytest**; add `jsonschema` only where needed).
5. If a dataset is optional, mark tests to **skip gracefully** when inputs are missing.

---

## CI Integration

Minimal GitHub Actions step:

```yaml
- name: Run tests
  run: |
    pytest -q --junitxml=pytest-report.xml
```

Upload `pytest-report.xml` to CI dashboards or badges as desired.

---

## Philosophy

These tests implement a **Master Coder Protocol** approach — they’re not just guardrails.
They enforce **reproducibility, transparency, and cross-disciplinary rigor**, helping us connect
maps, texts, hydrology, geology, and archives into a cohesive Kansas knowledge base — with
clear provenance and automated validation at every layer.

---
