# 🧪 Simulation Scripts (`api/scripts/simulation/`)

![status](https://img.shields.io/badge/status-active-brightgreen)
![reproducibility](https://img.shields.io/badge/reproducibility-deterministic%20by%20default-6f42c1)
![metadata](https://img.shields.io/badge/metadata-STAC%20%2B%20DCAT%20%2B%20PROV-ff69b4)
![geo](https://img.shields.io/badge/geospatial-PostGIS%20ready-2ea44f)
![python](https://img.shields.io/badge/python-3.10%2B-blue)

> **What this folder is:** the “scenario → run → artifact” backbone for Kansas Frontier Matrix simulations.  
> **What it produces:** versioned geospatial layers + time series + provenance/metadata bundles that the platform can render, compare, and audit.

---

## 🔎 Why this exists (KFM context)

Kansas Frontier Matrix (KFM) includes a **Modeling & Analytics** layer (agent-based + hydrology + forecasting + scenario comparisons) and treats simulations with **NASA-grade discipline** (reproducibility, validation, documentation). This folder is where those ideas become *repeatable scripts* that generate *reviewable artifacts*. ✅  
See:  
- 📄 **KFM Comprehensive Technical Documentation** → modeling/analytics and simulation discipline  
  - [`Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx`](<../../../Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx>)  
- 🌟 **Latest Ideas & Future Proposals** → deterministic simulation runner (“kfm-sim-run” concept: fixed clock, capture inputs/outputs/params, auto PRs)  
  - [`🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx`](<../../../🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx>)

---

## 🧭 Contents

- [✨ Principles](#-principles)
- [🗂️ Folder map](#️-folder-map)
- [⚡ Quickstart](#-quickstart)
- [🧩 Scenario spec](#-scenario-spec)
- [📦 Outputs](#-outputs)
- [🧾 Reproducibility contract](#-reproducibility-contract)
- [🧪 Verification & validation](#-verification--validation)
- [🧱 Adding a new simulation](#-adding-a-new-simulation)
- [🚀 Performance & scaling](#-performance--scaling)
- [🗺️ Visualization handoff](#️-visualization-handoff)
- [🔐 Security](#-security)
- [📚 Project library](#-project-library)

---

## ✨ Principles

### 1) Determinism first 🔁
If you run the same scenario with the same inputs + code revision, you should get the same outputs (or explain why not).

### 2) “Artifacts over opinions” 📦
A simulation run is only “real” if it produces:
- Output dataset(s)
- A run manifest (inputs, outputs, params, timestamps, git commit)
- Provenance + metadata bundles (STAC/DCAT/PROV)

### 3) PR-based publication 🧾➡️🔀
Simulation results should be published via a Pull Request:
- reviewers can inspect diffs
- CI can validate schemas + metadata
- provenance is preserved

### 4) Data staging is non-negotiable 🧱
Follow the KFM staging pattern:
- `data/raw/` → untouched source inputs
- `data/work/` → intermediates (safe to delete)
- `data/processed/` → finalized outputs + metadata/provenance

(See the project staging/metadata guidance in the KFM data lifecycle docs, if present in your repo.)

---

## 🗂️ Folder map

> This is the **intended** structure. If your repo differs, keep the *roles* consistent even if filenames shift.

```text
api/
└─ scripts/
   └─ simulation/
      ├─ README.md                 👈 you are here
      ├─ scenarios/                🧾 scenario YAML/JSON (human-authored)
      ├─ schemas/                  📐 JSON Schemas for scenario + manifest + metadata
      ├─ models/                   🧠 adapters/wrappers around simulation engines
      ├─ postprocess/              🧽 normalize outputs (GeoTIFF/COG, GeoJSON, parquet, etc.)
      ├─ validators/               ✅ preflight checks + plausibility rules
      ├─ runners/                  🏃 CLI + orchestration (deterministic runner)
      └─ examples/                 🧪 minimal reproducible example scenarios
```

---

## ⚡ Quickstart

> Because repo tooling varies (Poetry/uv/pip/conda), keep these steps aligned with your project’s standard Python workflow.

1) **Pick a scenario**
- Start from `scenarios/demo.yaml` (or create one from the template below).

2) **Run in dry-run mode first**
- Validate config
- Resolve inputs
- Print intended outputs
- No writes / no DB mutation

3) **Run for real**
- Generate outputs into `data/processed/...`
- Generate metadata into `data/stac/...`, `data/prov/...`
- Write a run manifest (`run.json`)
- Optionally generate a “graph diff patch” for Neo4j updates (apply separately)

4) **Publish via PR**
- Commit artifacts + metadata
- Open PR with run summary

---

## 🧩 Scenario spec

A scenario should be **human-readable** and **diff-friendly**.

### Minimal example (YAML)

```yaml
id: sim.kfm.demo.drought_sweep.v1
title: "Drought severity sweep (demo)"
description: >
  Demonstration scenario that perturbs precipitation inputs and measures
  downstream risk indices.

clock:
  mode: fixed
  datetime_utc: "2026-01-01T00:00:00Z"   # fixed clock to ensure determinism

seed:
  rng: 1337                              # global seed for stochastic components

inputs:
  - name: precip_timeseries
    kind: stac_item
    uri: "stac://collections/precip/items/precip_ks_1980_2025"
  - name: landcover
    kind: file
    uri: "data/processed/landcover/ks_landcover_2024.tif"

model:
  name: hydrology_proxy
  version: "0.1.0"
  parameters:
    severity_scale: [0.8, 0.9, 1.0, 1.1, 1.2]
    aggregation: "monthly"

outputs:
  base_dir: "data/processed/simulation/"
  products:
    - name: drought_risk_index
      format: geotiff_cog
      crs: "EPSG:4326"
    - name: run_summary
      format: parquet
```

### Recommended: keep schemas close ✅
Store JSON Schema(s) in `schemas/` and validate scenarios before any compute.

---

## 📦 Outputs

A simulation run should output **datasets + metadata + provenance**.

| Artifact | Location (recommended) | Why it matters |
|---|---|---|
| Primary output datasets (rasters, vectors, tables) | `data/processed/simulation/<run_id>/...` | used by the map + analytics |
| Run manifest (`run.json`) | `data/processed/simulation/<run_id>/run.json` | reproducibility “receipt” |
| STAC Item(s)/Collection | `data/stac/items/...` and/or `data/stac/collections/...` | geospatial catalog + discovery |
| PROV bundle | `data/prov/<run_id>/prov.json` (or `.ttl`) | provenance graph for audit |
| Optional graph patch | `data/processed/simulation/<run_id>/graph_patch.json` | controlled Neo4j updates |

### Run manifest fields (minimum)

```json
{
  "run_id": "sim.kfm.demo.drought_sweep.v1__2026-01-01T00-00-00Z__abc1234",
  "git_commit": "abc1234",
  "clock": "2026-01-01T00:00:00Z",
  "inputs": [{"name": "precip_timeseries", "ref": "stac://..."}],
  "parameters": {"severity_scale": [0.8, 0.9, 1.0]},
  "outputs": [{"name": "drought_risk_index", "path": "data/processed/..."}],
  "checksums": {"data/processed/.../file.tif": "sha256:..."}
}
```

---

## 🧾 Reproducibility contract

> Treat this checklist as a “Definition of Done” for simulation scripts.

- [ ] **Fixed clock** supported (no “now()” drifting) ⏱️  
- [ ] **Global seed** supported (document RNG + seed) 🎲  
- [ ] **Pin dependencies** (lockfile + container image tag if used) 📌  
- [ ] **Record commit hash** in run manifest 🧬  
- [ ] **Record exact input versions** (STAC IDs, file hashes, DB snapshots) 🧾  
- [ ] **Record output hashes** (sha256) 🔐  
- [ ] **Write STAC + PROV** alongside outputs 🧭  
- [ ] **Dry-run mode** exists (validate without writes) 🧯  
- [ ] **Idempotent outputs** (re-run doesn’t corrupt state) ♻️  
- [ ] **All side effects are explicit** (no “hidden” DB writes) 🚫🕳️

---

## 🧪 Verification & validation

KFM aims for high-trust simulation: correctness checks, not just “it ran”.

### Levels of validation ✅
- **Schema validation**: scenario + manifest + STAC JSON schema
- **Unit tests**: deterministic components, converters, validators
- **Golden tests**: tiny fixtures with fixed expected outputs
- **Plausibility checks**: ranges, monotonicity, conservation constraints (where applicable)
- **Sensitivity analysis**: confirm expected directional changes
- **Calibration** (optional): fit parameters to historical data and record the method

📚 Recommended references inside the repo:
- NASA-grade modeling & simulation concepts:  
  - [`Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`](<../../../Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf>)
- Regression + diagnostics (for calibration and residual checks):  
  - [`regression-analysis-with-python.pdf`](<../../../regression-analysis-with-python.pdf>)  
  - [`Regression analysis using Python - slides-linear-regression.pdf`](<../../../Regression analysis using Python - slides-linear-regression.pdf>)
- Statistics + experimental design (scenario sweeps / DOE):  
  - [`Understanding Statistics & Experimental Design.pdf`](<../../../Understanding Statistics & Experimental Design.pdf>)
- Bayesian updating (uncertainty & posterior inference):  
  - [`think-bayes-bayesian-statistics-in-python.pdf`](<../../../think-bayes-bayesian-statistics-in-python.pdf>)
- Exploratory diagnostics & visualization:  
  - [`graphical-data-analysis-with-r.pdf`](<../../../graphical-data-analysis-with-r.pdf>)

---

## 🧱 Adding a new simulation

### Step-by-step 🛠️
1) **Define the “thing you simulate”**
- What’s the state?
- What’s the timestep (if any)?
- What are the inputs and outputs?

2) **Create an adapter in `models/`**
- wrap external engines (SWAT, Mesa, custom PDE solver, etc.)
- isolate engine-specific quirks behind a stable interface

3) **Define a scenario schema**
- keep scenario files diff-friendly
- validate early

4) **Implement post-processing**
- normalize geospatial output formats (COG, GeoParquet, GeoJSON)
- attach CRS + bounds + timestamps

5) **Emit boundary artifacts**
- STAC item(s)/collection
- PROV bundle
- run manifest

6) **Add tests**
- unit tests for adapters + converters
- “golden run” with small fixtures

### Naming convention (recommended) 🏷️
- **Scenario ID**: `sim.<domain>.<model>.<scenario>.v#`
- **Run ID**: `<scenario_id>__<fixed_clock>__<git_short_sha>`

---

## 🚀 Performance & scaling

Simulations become expensive fast. Prefer patterns that scale:

- Chunk work by **space** (tiles) or **time** (windows)
- Stream outputs rather than building giant in-memory arrays
- Write intermediates to `data/work/` (delete-safe)
- Keep “big compute” separate from “metadata writing” so retries are safe

📚 For deeper performance thinking (task pools, chunking, compilation-based execution ideas):  
- [`Scalable Data Management for Future Hardware.pdf`](<../../../Scalable Data Management for Future Hardware.pdf>)

---

## 🗺️ Visualization handoff

Simulation outputs should be easy for the UI layer to consume:

- **Raster**: GeoTIFF / Cloud-Optimized GeoTIFF (COG) for time slices
- **Vector**: GeoJSON (small) or GeoParquet (big)
- **3D/advanced**: mesh formats or derived tilesets when needed

📚 UI/visualization references included in the repo:
- WebGL fundamentals (3D rendering concepts):  
  - [`webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`](<../../../webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf>)
- Map design & cartographic communication:  
  - [`making-maps-a-visual-guide-to-map-design-for-gis.pdf`](<../../../making-maps-a-visual-guide-to-map-design-for-gis.pdf>)  
  - [`Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`](<../../../Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf>)
- Responsive UI patterns (scenario toggles, dashboards):  
  - [`responsive-web-design-with-html5-and-css3.pdf`](<../../../responsive-web-design-with-html5-and-css3.pdf>)
- Image/export considerations:  
  - [`compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`](<../../../compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf>)

---

## 🔐 Security

Simulation scripts touch big data + infrastructure—treat them like production code.

- ✅ Use environment variables for credentials (never commit secrets)
- ✅ Validate all file paths / URIs (no arbitrary writes)
- ✅ Avoid executing untrusted code/config
- ✅ Log safely (no tokens/keys in logs)
- ✅ Apply least-privilege DB roles

Security references included in the repo (use ethically; defensive mindset):
- [`ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`](<../../../ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf>)
- [`Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`](<../../../Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf>)

---

## 📚 Project library

<details>
<summary>📖 Click to expand: all project files referenced by this simulation module</summary>

### 🧭 Core KFM docs
- [`Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx`](<../../../Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx>)
- [`🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx`](<../../../🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx>)

### 🧪 Modeling / simulation rigor
- [`Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`](<../../../Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf>)

### 📈 Stats / ML / inference (calibration + uncertainty)
- [`Understanding Statistics & Experimental Design.pdf`](<../../../Understanding Statistics & Experimental Design.pdf>)
- [`regression-analysis-with-python.pdf`](<../../../regression-analysis-with-python.pdf>)
- [`Regression analysis using Python - slides-linear-regression.pdf`](<../../../Regression analysis using Python - slides-linear-regression.pdf>)
- [`think-bayes-bayesian-statistics-in-python.pdf`](<../../../think-bayes-bayesian-statistics-in-python.pdf>)
- [`graphical-data-analysis-with-r.pdf`](<../../../graphical-data-analysis-with-r.pdf>)

### 🌍 Geospatial + remote sensing
- [`python-geospatial-analysis-cookbook.pdf`](<../../../python-geospatial-analysis-cookbook.pdf>)
- [`PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`](<../../../PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf>)
- [`Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`](<../../../Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf>)

### 🗺️ Cartography / visualization / UI
- [`making-maps-a-visual-guide-to-map-design-for-gis.pdf`](<../../../making-maps-a-visual-guide-to-map-design-for-gis.pdf>)
- [`Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`](<../../../Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf>)
- [`webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`](<../../../webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf>)
- [`responsive-web-design-with-html5-and-css3.pdf`](<../../../responsive-web-design-with-html5-and-css3.pdf>)
- [`compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`](<../../../compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf>)

### 🧠 Systems theory / autonomy / human-centered + governance
- [`Principles of Biological Autonomy - book_9780262381833.pdf`](<../../../Principles of Biological Autonomy - book_9780262381833.pdf>)
- [`Introduction to Digital Humanism.pdf`](<../../../Introduction to Digital Humanism.pdf>)
- [`On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`](<../../../On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf>)
- [`Data Spaces.pdf`](<../../../Data Spaces.pdf>)

### 🏗️ Optimization / graphs / advanced math (optional simulation modules)
- [`Generalized Topology Optimization for Structural Design.pdf`](<../../../Generalized Topology Optimization for Structural Design.pdf>)
- [`Spectral Geometry of Graphs.pdf`](<../../../Spectral Geometry of Graphs.pdf>)

### ⚙️ Concurrency / distributed systems (engineering reference)
- [`concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`](<../../../concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf>)
- [`Scalable Data Management for Future Hardware.pdf`](<../../../Scalable Data Management for Future Hardware.pdf>)

### 🔐 Security references (defensive use only)
- [`ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`](<../../../ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf>)
- [`Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`](<../../../Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf>)

### 📦 Programming reference compilations (handy when implementing adapters/runners)
- [`A programming Books.pdf`](<../../../A programming Books.pdf>)
- [`B-C programming Books.pdf`](<../../../B-C programming Books.pdf>)
- [`D-E programming Books.pdf`](<../../../D-E programming Books.pdf>)
- [`F-H programming Books.pdf`](<../../../F-H programming Books.pdf>)
- [`I-L programming Books.pdf`](<../../../I-L programming Books.pdf>)
- [`M-N programming Books.pdf`](<../../../M-N programming Books.pdf>)
- [`O-R programming Books.pdf`](<../../../O-R programming Books.pdf>)
- [`S-T programming Books.pdf`](<../../../S-T programming Books.pdf>)
- [`U-X programming Books.pdf`](<../../../U-X programming Books.pdf>)

### 🧠 Deep learning (note)
- [`Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf`](<../../../Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf>)

</details>

---

## ✅ Suggested PR template (for publishing simulation outputs)

```markdown
## Simulation run
- Scenario ID:
- Run ID:
- Git commit:
- Fixed clock:
- Seed:

## Inputs
- [ ] STAC item IDs / dataset versions listed in manifest

## Outputs
- [ ] Output datasets written to data/processed/...
- [ ] STAC item(s) created/updated
- [ ] PROV bundle created/updated
- [ ] Run manifest attached

## Validation
- [ ] Schema validation passed
- [ ] Golden tests / smoke tests passed
- [ ] Plausibility checks passed

## Notes
- Assumptions:
- Known limitations:
- Next runs to consider:
```

---

### 🧷 TL;DR
If it’s a simulation, it should be **scenario-driven**, **deterministic**, **artifact-backed**, and **auditable**. 🧪📦🧾

