# 🧪 Simulation Scripts (KFM) — `api/scripts/simulation`

![Python](https://img.shields.io/badge/Python-3.x-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-API-success) ![Reproducible](https://img.shields.io/badge/Reproducible-✅-brightgreen) ![Geospatial](https://img.shields.io/badge/Geospatial-PostGIS%20%7C%20STAC%20%7C%20PROV-9cf) ![Status](https://img.shields.io/badge/KFM-Simulation%20Pipeline-ff69b4)

> [!NOTE]
> This folder contains **simulation + analysis runners** used by the Kansas Frontier Matrix (KFM) backend and/or pipeline tooling. These scripts should behave like **scientific instruments**: config-driven, deterministic when seeded, and emitting provenance + metadata alongside results.  
> <!-- Context: API has simulation/analysis endpoints; data folder includes raw/processed/prov with STAC/DCAT/PROV. :contentReference[oaicite:0]{index=0} -->

---

## 🧭 Contents

- [🧩 What lives here](#-what-lives-here)
- [🗺️ Where simulations fit in the KFM pipeline](#️-where-simulations-fit-in-the-kfm-pipeline)
- [🚀 Quick start](#-quick-start)
- [🧱 Folder conventions](#-folder-conventions)
- [🧾 Run outputs, metadata, and provenance](#-run-outputs-metadata-and-provenance)
- [🧠 Simulation contract](#-simulation-contract)
- [✅ Verification, validation, and uncertainty](#-verification-validation-and-uncertainty)
- [🛰️ Geospatial & remote-sensing patterns](#️-geospatial--remote-sensing-patterns)
- [⚡ Performance patterns](#-performance-patterns)
- [🛡️ Security, governance, and ethics](#️-security-governance-and-ethics)
- [🧩 Add a new simulation](#-add-a-new-simulation)
- [🧰 Troubleshooting](#-troubleshooting)
- [📚 Reference shelf](#-reference-shelf)

---

## 🧩 What lives here

Think of this directory as **“the lab bench”** for KFM simulations:

- 🧪 **Scenario simulators** (deterministic + stochastic)
- 📈 **Analysis jobs** (regression, Bayesian updates, calibration runs, sensitivity sweeps)
- 🛰️ **Geo / remote-sensing jobs** (PostGIS-derived features, Earth Engine exports)
- 🧾 **Provenance & catalog emitters** (STAC/DCAT/PROV JSON written next to outputs)

These scripts are designed to be invoked by:
- 🌐 **FastAPI endpoints** (e.g., “run a simulation and return results / run_id”), and/or
- 🧵 **Background workers / schedulers**, and/or
- 🧰 **CLI / developer runs** in local environments.

<!-- FastAPI + simulation endpoints mention: :contentReference[oaicite:2]{index=2} -->

---

## 🗺️ Where simulations fit in the KFM pipeline

KFM’s pipeline is intentionally **ordered**: raw → processed → catalogs → graph → APIs → UI → narratives. Simulations are **analysis artifacts** that should re-enter the same catalog + provenance flow (don’t “shortcut” them straight into UI).  
<!-- Canonical pipeline ordering + extension point for analysis artifacts: :contentReference[oaicite:3]{index=3} -->

```mermaid
flowchart LR
  A["📥 data/raw"] --> B["🧼 ETL • normalize"]
  B --> C["📦 data/processed"]
  C --> D["🧾 data/prov<br/>STAC • DCAT • PROV"]
  D --> E["🕸️ Graph build<br/>Neo4j • relationships"]
  E --> F["🛰️ APIs<br/>FastAPI • contracts"]
  F --> G["🗺️ UI maps • 3D • stories"]
  C --> S["🧪 Simulation scripts<br/>this folder"]
  S --> C
  S --> D
```

> [!TIP]
> If your simulation generates a new “dataset” (raster/vector/table/graph), treat it as **first-class evidence**: publish it to `data/processed`, describe it in `data/prov`, and (optionally) ingest into the graph.

---

## 🚀 Quick start

### ✅ Prereqs

- 🐍 Python 3.x (venv/conda ok)
- 🗄️ Postgres + PostGIS (for geospatial simulations)
- 🌍 Optional: Google Earth Engine credentials (for remote-sensing jobs)
- 🐳 Optional: Docker (recommended for parity runs)

### 🏁 Common run patterns

> Because script entrypoints vary, every runner should support `--help` and be runnable from repo root.

```bash
# (example) list available simulations
python -m api.scripts.simulation.run --list

# (example) run a simulation from a YAML spec
python -m api.scripts.simulation.run \
  --spec api/scripts/simulation/specs/flood_extent.yml \
  --seed 42 \
  --out data/processed/simulations

# (example) dry-run to validate config + I/O plan
python -m api.scripts.simulation.run --spec ... --dry-run
```

### 🔑 Environment variables (recommended baseline)

```bash
# paths
export KFM_DATA_DIR="data"
export KFM_PROV_DIR="data/prov"

# database (if used)
export KFM_DB_URL="postgresql://user:pass@localhost:5432/kfm"

# remote sensing (if used)
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
```

---

## 🧱 Folder conventions

Suggested internal layout (adapt as needed, but keep it consistent):

```text
api/scripts/simulation/
├─ README.md  ✅ (you are here)
├─ run.py / run_simulation.py      # main dispatcher (recommended)
├─ registry.yaml                   # "simulation_name" → module entrypoint
├─ specs/                          # YAML/JSON run specifications (inputs/params/outputs)
├─ models/                         # model implementations (pure functions where possible)
├─ adapters/                       # PostGIS / Neo4j / EarthEngine / file IO wrappers
├─ schemas/                        # JSONSchema / Pydantic models for validation
├─ notebooks/                      # exploratory work (keep outputs out of git)
├─ tests/                          # unit + golden + regression tests
└─ utils/                          # logging, hashing, id generation, etc
```

> [!IMPORTANT]
> Keep **domain math** in `models/` and keep **side effects** (DB/network/filesystem) in `adapters/`. This makes verification + testing dramatically easier (and makes provenance cleaner).

---

## 🧾 Run outputs, metadata, and provenance

### 🆔 Run IDs

Every execution produces a `run_id` (UUID or deterministic hash). A run is a **folder**:

```text
data/processed/simulations/<simulation_name>/<run_id>/
├─ outputs/...
├─ metrics.json
├─ plots/...
├─ manifest.yaml
├─ stac-item.json
├─ dcat.json
└─ prov.jsonld
```

### 📦 Required artifacts

At minimum, a run should emit:

- `manifest.yaml` 🧾  
  - spec hash
  - git commit (if available)
  - python env / lockfile reference
  - seed + RNG details
  - input dataset fingerprints (checksums, versions)
- `prov.jsonld` 🧬  
  - **PROV** graph linking inputs → activity → outputs  
- `stac-item.json` 🛰️ (for geospatial assets, or STAC-like items for non-geo evidence)
- `dcat.json` 🗂️ (dataset-level catalog metadata where applicable)

KFM’s documentation explicitly calls out keeping **raw / processed / provenance** separated and maintaining **STAC/DCAT/PROV bundles** for reproducibility.  
<!-- Data folder raw/processed/prov and STAC/DCAT/PROV:  -->

### 🧪 MCP experiment log (recommended)

When runs represent “experiments,” also write a record under:

```text
mcp/runs/<run_id>/
├─ hypothesis.md
├─ spec.snapshot.yml
├─ notes.md
└─ results.summary.md
```

This aligns with the project’s MCP discipline around repeatability, review, and consistent research documentation.  
<!-- MCP discipline: peer review + reproducibility guidance: :contentReference[oaicite:5]{index=5} -->

---

## 🧠 Simulation contract

### Input spec (example)

```yaml
simulation:
  name: flood_extent
  version: "0.3.0"
  description: "Estimate flood extent under scenario X"

inputs:
  aoi:
    type: geojson
    path: data/processed/aoi/kansas_county.geojson
  dem:
    type: raster
    path: data/raw/elevation/dem_cog.tif
  hydro:
    type: table
    path: data/raw/hydro/streamflow.parquet

parameters:
  return_period_years: 100
  roughness_n: 0.035
  method: "monte_carlo"
  n_samples: 1000

runtime:
  seed: 42
  threads: 8
  time_limit_s: 900

outputs:
  write_geojson: true
  write_cog: true
  write_summary_table: true
```

### Output contract (minimum)

A successful run should return (to API or CLI):

```json
{
  "run_id": "2026-01-12T...-uuid",
  "simulation_name": "flood_extent",
  "status": "completed",
  "outputs": [
    {"type": "raster", "path": "data/processed/simulations/.../flood_extent_cog.tif"},
    {"type": "vector", "path": "data/processed/simulations/.../flood_polygon.geojson"},
    {"type": "table",  "path": "data/processed/simulations/.../summary.parquet"}
  ],
  "metadata": {
    "seed": 42,
    "duration_s": 12.31,
    "warnings": []
  }
}
```

> [!TIP]
> The *contract* (schemas) should also live in `contracts/` when results are exposed via API, to keep server/client aligned.  
> <!-- Repo structure expects contracts and shared schemas: :contentReference[oaicite:6]{index=6} -->

---

## ✅ Verification, validation, and uncertainty

KFM simulation outputs are only as credible as their V&V. The NASA-grade modeling guidance emphasizes:
- clear model purpose
- verification + validation
- uncertainty quantification (UQ)
- sensitivity analysis and careful Monte Carlo use  
<!-- NASA-grade modeling/simulation + VVUQ + Monte Carlo:  -->

### ✅ Minimum V&V checklist (per simulation)

- [ ] **Unit tests** for model core (`models/`)
- [ ] **Golden test** (small fixed dataset + seed → stable outputs)
- [ ] **Regression test** (new changes don’t shift outputs beyond tolerance)
- [ ] **Calibration** notes: what was tuned, against what, and why
- [ ] **Sensitivity sweep** for at least top 3 parameters
- [ ] **Uncertainty report**:
  - seeds / distributions
  - confidence intervals or posterior intervals
  - caveats + failure modes

### 📈 Statistical hygiene (don’t skip)

Use standard regression + experimental design guardrails:
- validate assumptions (residuals, heteroscedasticity, outliers)
- avoid “optional stopping” / p-hacking patterns
- document multiple comparisons if doing many scenario tests  
<!-- Regression diagnostics + pitfalls:  -->

### 🧠 Bayesian updates (when appropriate)

Bayesian workflows can be ideal for incremental evidence updates, posterior predictive checks, and uncertainty reporting.  
<!-- Bayesian update framing:  -->

---

## 🛰️ Geospatial & remote-sensing patterns

### 🗺️ PostGIS / pgRouting

When simulations depend on networks, routing, or spatial selection, prefer **PostGIS-side primitives** and export GeoJSON cleanly.

- Use PostGIS for transforms (`ST_Transform`) and GeoJSON serialization (`ST_AsGeoJSON`)  
- For routing, pgRouting’s Dijkstra output can be converted to GeoJSON segments  
<!-- pgRouting + GeoJSON patterns: :contentReference[oaicite:12]{index=12} -->
<!-- PostGIS export & feature collection assembly: :contentReference[oaicite:13]{index=13} -->

> [!NOTE]
> Keep CRS handling explicit. If the output is intended for web maps, emit WGS84 (EPSG:4326) GeoJSON or tiles.

### ☁️ Earth Engine (GEE)

For remote-sensing driven simulations:
- keep Earth Engine operations server-side as long as possible
- avoid client-side `.getInfo()` on big collections
- export artifacts (GeoTIFF/COG, tables) and catalog them like any other evidence  
<!-- GEE scale/exports patterns:  -->

### 🧩 Map design + storytelling handoff

Simulation outputs should be readable, not just correct:
- label units
- include uncertainty overlays
- choose symbolization intentionally (visual hierarchy matters)  
<!-- Map design principles + GIS visualization: :contentReference[oaicite:16]{index=16} -->

---

## ⚡ Performance patterns

### 🧠 Practical defaults

- 🔁 cache intermediate results (especially expensive raster ops)
- 🧩 chunk by AOI tiles or time windows
- 🧮 vectorize math (NumPy), avoid Python loops in hot paths
- 🧵 parallelize at coarse level (per tile / per sample), not inside tiny loops
- 🗄️ push heavy spatial filtering into PostGIS + indexed geometries
  - use `EXPLAIN (ANALYZE, BUFFERS)` to understand query plans  
  <!-- Query plan analysis:  -->

### 🚀 Advanced (optional): streaming + compiled execution ideas

For large, graph-heavy, or streaming workloads, modern scalable data engines emphasize:
- push-based operator pipelines
- morsel-driven parallelism
- adaptive / JIT compilation to hide memory latency  
<!-- Push-based, morsel-driven, and adaptive compilation: :contentReference[oaicite:18]{index=18}:contentReference[oaicite:19]{index=19} -->

> [!TIP]
> You don’t need to implement JIT compilers here 😄 — but you *can* adopt the principles: chunking, pipelining, and minimizing materialization.

---

## 🛡️ Security, governance, and ethics

### 🔐 Input safety

- Treat run specs as **untrusted input** when invoked via API.
- Validate with schemas; never `eval()` configs.
- Restrict file access to known directories.
- Use parameterized DB queries (avoid injection risks).  
<!-- SQL injection risk described (without payload): :contentReference[oaicite:20]{index=20} -->

### 🧭 Governance & provenance

- Every run should be traceable: *what data, what parameters, what code version, what seed*.
- Keep outputs and catalogs aligned with the KFM evidence pipeline (STAC/DCAT/PROV).  
<!-- Pipeline + evidence artifacts + provenance: :contentReference[oaicite:21]{index=21} -->

### 🧑‍🤝‍🧑 Human-centered & legal awareness

KFM simulations often influence narratives and interpretations. Keep them:
- transparent
- explainable
- respectful of privacy and communities

Digital Humanism and related scholarship emphasize the social context and the non-neutrality of computational systems.  
<!-- Digital humanism context: :contentReference[oaicite:23]{index=23} -->
<!-- AI law / conceptual framing: :contentReference[oaicite:24]{index=24} -->
<!-- Mobile mapping & cultural/political framing:  -->

---

## 🧩 Add a new simulation

1) **Create a module**
- `models/<name>.py` for core logic
- `adapters/<name>_io.py` for I/O glue

2) **Define a spec + schema**
- `specs/<name>.yml`
- `schemas/<name>.schema.json` (or Pydantic model)

3) **Register it**
- add to `registry.yaml` (name → entrypoint)

4) **Write tests**
- `tests/test_<name>_unit.py`
- `tests/test_<name>_golden.py`

5) **Emit provenance + catalogs**
- write `manifest.yaml`, `prov.jsonld`, `stac-item.json`, `dcat.json`

6) **Document it**
- add a short section below in this README (or a `docs/<name>.md`)

> [!TIP]
> If you’re feeling architecture pain, revisit modularity + plugin recommendations from the project audit docs.  
> <!-- Modularity/plugin architecture emphasis: :contentReference[oaicite:26]{index=26} -->

---

## 🧰 Troubleshooting

**“My run produced files but nothing shows up in the UI.”**  
✅ Ensure you created/updated:
- STAC/DCAT entries (`data/prov/...`)
- any required graph ingestion step (if UI relies on graph edges)

**“GeoJSON renders wrong / flipped.”**  
✅ Confirm CRS:
- store analysis in projected CRS when needed
- export for web in EPSG:4326

**“Earth Engine export is slow / failing.”**  
✅ Reduce region size, avoid client-side evaluation, export in chunks, and prefer server-side reducers.  
<!-- GEE scaling reminders:  -->

---

## 📚 Reference shelf

<details>
<summary><b>📚 Project library used to shape this simulation README (click to expand)</b></summary>

### Core KFM docs 🧭
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx** — overall architecture, API + data/provenance conventions.  
  <!-- :contentReference[oaicite:28]{index=28} -->
- **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx** — future modeling/simulation directions & integration ideas.  
  <!--  -->
- **MARKDOWN guide for GPT or humans v13.txt** — repo structure + pipeline ordering + “analysis artifacts are evidence” rule.  
  <!-- :contentReference[oaicite:31]{index=31} -->
- **Scientific Method _ Research _ Master Coder Protocol Documentation.pdf** — MCP experiment discipline & reproducibility habits.  
  <!-- :contentReference[oaicite:32]{index=32} -->
- **Kansas Frontier Matrix Design Audit – Gaps and Enhancement Opportunities.pdf** — modularity / plugin architecture / governance improvements.  
  <!-- :contentReference[oaicite:33]{index=33} -->
- **Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf** — STAC-like evidence catalog + geospatial publishing patterns.  
  <!-- :contentReference[oaicite:34]{index=34} -->

### Modeling, simulation, and uncertainty 🧪
- **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf** — V&V + UQ + Monte Carlo discipline.  
  <!--  -->
- **Understanding Statistics & Experimental Design.pdf** — experimental design pitfalls & statistical rigor.  
  <!--  -->
- **regression-analysis-with-python.pdf** + **Regression analysis using Python - slides-linear-regression.pdf** — regression diagnostics and applied workflows.  
  <!-- :contentReference[oaicite:38]{index=38} -->
- **think-bayes-bayesian-statistics-in-python.pdf** — Bayesian updating patterns.  
  <!--  -->
- **graphical-data-analysis-with-r.pdf** — exploratory diagnostics mindset.  
  <!-- (not directly cited above; used as reference for EDA conventions) -->

### Geospatial + visualization 🗺️
- **python-geospatial-analysis-cookbook.pdf** — PostGIS/pgRouting → GeoJSON flows.  
  <!-- :contentReference[oaicite:40]{index=40} -->
- **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf** — indexing + planning reference (Postgres fundamentals).  
- **making-maps-a-visual-guide-to-map-design-for-gis.pdf** — map design principles for communication.  
  <!-- :contentReference[oaicite:41]{index=41} -->
- **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf** — mobile mapping is cultural/political; consider implications.  
  <!--  -->
- **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf** — 3D rendering foundations for simulation visualization.
- **responsive-web-design-with-html5-and-css3.pdf** — responsive presentation of results.

### Remote sensing ☁️🛰️
- **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf** — scalable remote sensing workflows.  
  <!--  -->

### Data engineering & interoperability 🧱
- **Scalable Data Management for Future Hardware.pdf** — pipelining, chunking, adaptive compilation concepts.  
  <!-- :contentReference[oaicite:44]{index=44} -->
- **Data Spaces.pdf** — interoperability + federation mental model for cross-org data sharing.  
  <!-- :contentReference[oaicite:45]{index=45} -->

### Ethics, governance, and security 🛡️
- **Introduction to Digital Humanism.pdf** — human-centered computing context.  
  <!-- :contentReference[oaicite:46]{index=46} -->
- **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf** — legal framing around ML.  
  <!-- :contentReference[oaicite:47]{index=47} -->
- **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf** + **Gray Hat Python (2009).pdf** — security awareness references (defense-focused).
- **S-T programming Books.pdf** — example security pitfalls (SQL injection awareness).  
  <!-- :contentReference[oaicite:48]{index=48} -->

### Advanced/adjacent theory 🧠
- **Spectral Geometry of Graphs.pdf** — graph Laplacians & spectral methods (useful for network simulations).  
  <!-- :contentReference[oaicite:49]{index=49} -->
- **Generalized Topology Optimization for Structural Design.pdf** — optimization patterns for structural simulations.  
  <!-- :contentReference[oaicite:50]{index=50} -->
- **Principles of Biological Autonomy - book_9780262381833.pdf** — autonomy and systems thinking backdrop.
- **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf** — practical image/raster format tradeoffs.

### Programming reference bundles 📦
- **A programming Books.pdf**
- **B-C programming Books.pdf**  
  <!-- :contentReference[oaicite:51]{index=51} -->
- **D-E programming Books.pdf**
- **F-H programming Books.pdf**  
  <!-- :contentReference[oaicite:52]{index=52} -->
- **I-L programming Books.pdf**
- **M-N programming Books.pdf**
- **O-R programming Books.pdf**  
  <!-- :contentReference[oaicite:53]{index=53} -->
- **S-T programming Books.pdf**  
  <!-- :contentReference[oaicite:54]{index=54} -->
- **U-X programming Books.pdf**
- **Deep Learning for Coders with fastai and PyTorch** — ML implementation reference (note: file access may vary in tooling).

</details>

---

### ✅ One-line principle (print this on the lab wall 🧷)

> **A simulation that can’t be reproduced, validated, and explained is not an artifact — it’s an anecdote.**


