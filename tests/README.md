# Kansas-Frontier-Matrix — Test Suite

This directory contains the automated test suite for the **Kansas-Frontier-Matrix** stack.  
The tests provide **mission-grade validation** of data, metadata, and code wiring. They are written in
**pytest** and designed to skip gracefully when files are not yet present (scaffolding stage).

---

## Objectives

- Validate **STAC 1.0.0** metadata (`catalog.json`, `collections/*.json`, `items/*.json`) for conformance.  
- Cross-check **data provenance**: filenames vs. IDs, bbox vs. geometry, temporal intervals [oai_citation:0‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).  
- Confirm **geospatial source configs** (YAML/JSON in `data/`) parse correctly and contain required keys [oai_citation:1‡Data resource analysis.pdf](file-service://file-GdS9Kcw7Xbfqpy4xwwdqWS).  
- Ensure **core web assets** (`web/app.js`, `web/app.css`, logos, favicon) exist for the public site.  
- Provide **reproducible, transparent checks** consistent with the MCP Scientific Method templates [oai_citation:2‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).  
- Quantify potential **gaps or uncertainty** in datasets (audit-aligned) [oai_citation:3‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-BgUSuffTiRq4qidye2sPwN).  
- Build hooks for **multi-modal ingestion tests** — historical texts, maps, hydrology, oral histories [oai_citation:4‡Historical Dataset Integration for Kansas Frontier Matrix.pdf](file-service://file-EG371w17RJTzXWjXvqgsB6).

---

## Test Flow

```mermaid
flowchart TD
  %% --- Inputs ---
  subgraph Repo
    A1[stac/catalog.json]
    A2[stac/collections/*.json]
    A3[stac/items/*.json]
    B1[data/sources/*.yml]
    C1[web/app.js, CSS, assets]
  end

  %% --- Test runners ---
  subgraph Pytest
    T1[test_stac.py]
    T2[test_sources.py]
    T3[test_web.py - planned]
  end

  A1 --> T1
  A2 --> T1
  A3 --> T1
  B1 --> T2
  C1 --> T3

  %% --- Outputs ---
  subgraph Results
    R1[Clear Failures]
    R2[Graceful Skips]
    R3[Green -> Site Build Ready]
  end

  T1 --> R1
  T1 --> R2
  T2 --> R1
  T2 --> R2
  T3 --> R1
  T3 --> R2
  T1 --> R3
  T2 --> R3
  T3 --> R3

  R3 --> Site[Static Site / Map UI]


⸻

Current Test Modules
	•	test_stac.py — Validates STAC Collections and Items:
	•	type, stac_version, id fields
	•	bbox vs. geometry enclosure
	•	datetime / start_datetime / end_datetime
	•	asset media types (GeoTIFF/COG best practices)
	•	collection ↔ item link integrity
	•	test_sources.py — Sanity checks for data source files under data/:
	•	JSON/YAML validity
	•	required fields present
	•	paths/URLs plausibility
	•	(planned) test_web.py — Checks existence of critical frontend assets before site build/deploy.

⸻

Test ↔ Architecture Map (Knowledge Hub)

This shows exactly where each test lands in the Kansas Historical Knowledge Hub architecture ￼.

Test file / planned test	Knowledge Hub layer(s)	Primary intent
test_stac.py	Data Repositories (Geo-spatial Data Catalog, STAC-like JSON) ￼	Schema conformance; spatial/temporal extent sanity; collection↔item linkage; asset media types
test_sources.py	Ingestion & Processing Pipeline (source config inputs) ￼ ￼	Source config validity; required keys; URL/path plausibility for fetch/ETL
(planned) test_web.py	Frontend Application (static site assets) ￼	Presence of required assets before build/deploy
(future) test_ingest_texts.py	Ingestion & Processing Pipeline → NLP extraction ￼ ￼	Minimal smoke tests for OCR/NLP passes on sample texts; provenance stubs
(future) test_graph_entities_relations.py	Knowledge Graph Database (entity/edge shape) ￼	Node/edge label policy, required properties (date/place normalization)
(future) test_graph_query_api.py	Query API Layer (REST/GraphQL) ￼	Basic graph queries: by time, place, entity type, confidence
(future) test_uncertainty_qc.py	Pipeline ↔ Graph ↔ UI (confidence tagging) ￼	Confidence scores present for NLP/georef; rendering rules (opacity/error bars)
(future) test_layers_catalog_integrity.py	Data Repositories (STAC-like catalog of layers) ￼	Each layer has source URL, license, CRS, temporal coverage, processing notes
(future) test_storymap_hooks.py	Frontend Application (story-map mode) ￼	Ensure narrative/chapters schema and content hooks exist (when feature lands)
(future) test_hydrology_models_io.py	Ingestion + Data Repos (hydrology endpoints/models) ￼	Check documented endpoints exist; model I/O manifests present

Use this table when adding tests to pin your PR to the right architectural layer(s) and reviewers.

⸻

Running Tests

From the repo root:

pytest -q

Options:
	•	-k "stac" → run only STAC validation tests
	•	-s → show stdout/logs
	•	--maxfail=1 → stop after first failure
	•	-vv → verbose mode (useful for parametric cases)

⸻

Debugging & Skips
	•	If no STAC items/collections exist yet, pytest will skip module-wide to avoid noise.
	•	JSON parse errors raise AssertionErrors with file + error details.
	•	Skips are expected during scaffolding; failures indicate required corrections.

⸻

Adding New Tests
	1.	Place tests in this directory, naming files test_*.py.
	2.	Reuse shared helpers from test_stac.py / test_sources.py.
	3.	Use @pytest.mark.parametrize to scale across many files consistently.
	4.	Keep dependencies minimal (stdlib + pytest).

Future extensions may add:
	•	ETL/ingest validation (checking derivative COGs, KMLs, etc.) ￼
	•	Uncertainty checks (bounding confidence on georeferencing or NLP extraction) ￼
	•	Simulation/model integration tests (aligned with NASA-grade reproducibility protocols) ￼
	•	Cross-disciplinary hooks (archaeology, oral histories, climate proxies, hydrology datasets) ￼ ￼

⸻

CI Integration

Add a GitHub Actions step:

- name: Run tests
  run: |
    pytest -q --junitxml=pytest-report.xml

Upload pytest-report.xml for CI dashboards or Shields.io badges.

⸻

Philosophy

These tests are not just guardrails. They implement a Master Coder Protocol (MCP) approach — ensuring
reproducibility, transparency, and cross-disciplinary rigor across Kansas-Frontier-Matrix datasets ￼.

The suite evolves from simple file existence checks → to integrated reasoning that links maps, texts,
oral histories, geology, and archives into a cohesive Kansas knowledge base ￼ ￼.

If you want, I can also stub the *future* tests listed in the mapping table as no-op `pytest.skip` modules so they’re visible in CI now and easy to flesh out later.
