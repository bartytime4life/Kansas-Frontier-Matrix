# 🧰 Tool Manifests (KFM / Kansas-Matrix-System)

![Status](https://img.shields.io/badge/status-alpha-orange)
![Manifests](https://img.shields.io/badge/manifests-YAML%20%7C%20JSON-blue)
![Provenance](https://img.shields.io/badge/provenance-first-success)
![Citations](https://img.shields.io/badge/citations-required-critical)
![Schema](https://img.shields.io/badge/schema-JSON%20Schema-informational)
![License](https://img.shields.io/badge/license-TBD-lightgrey)

Manifests make every **tool, dataset, map layer, pipeline, model, and UI module** in KFM:
- ✅ **Discoverable** (searchable & indexable)
- ✅ **Reproducible** (inputs, parameters, environments, seeds)
- ✅ **Auditable** (lineage + “why/where did this come from?”)
- ✅ **Citable** (sources + licenses as first-class data)
- ✅ **Maintainable** (clean boundaries, explicit dependencies)

> [!IMPORTANT]
> KFM is *provenance-first*: manifests are the contract that prevents “black box layers” and “mystery answers.”
> If it can’t be traced, it can’t ship. 🧾🧭

---

## 📌 Contents

- [Why manifests exist](#-why-manifests-exist)
- [Folder layout](#-folder-layout)
- [Manifest taxonomy](#-manifest-taxonomy)
- [Base manifest shape](#-base-manifest-shape)
- [Type-specific fields](#-type-specific-fields)
- [Provenance and citations](#-provenance-and-citations)
- [Validation and CI](#-validation-and-ci)
- [Examples](#-examples)
- [Project reference library](#-project-reference-library)

---

## 🎯 Why manifests exist

KFM connects **historical archives + GIS + remote sensing + data science + AI** into a single “living atlas.”  
Manifests are how we keep that ecosystem:
- **transparent** (sources + processing steps),
- **modular** (clean architecture boundaries),
- **scalable** (performance-aware),
- **human-centered** (ethical + explainable by design).

Think of a manifest as:
- a **nutritional label** 🥗 (what it contains),
- a **receipt** 🧾 (where it came from),
- a **build recipe** 🧪 (how to reproduce it),
- and a **warranty** 🛡️ (tests + constraints + governance).

---

## 🗂 Folder layout

Recommended structure (adjust to your repo conventions):

```text
tools/ 🧰
└─ 📦 manifests/                  # governed manifests for datasets/models/pipelines/UI
   ├─ 📁 registry/                # registry/index files that power search & UI
   │  └─ 🗂️ registry.yaml         # canonical registry index
   ├─ 📐 schemas/                 # JSON Schema for validation (base + kinds)
   │  ├─ 📄 base.schema.json
   │  ├─ 📄 dataset.schema.json
   │  ├─ 📄 layer.schema.json
   │  ├─ 📄 pipeline.schema.json
   │  ├─ 📄 model.schema.json
   │  ├─ 📄 service.schema.json
   │  └─ 📄 ui.schema.json
   ├─ 🧩 templates/               # copy/paste starters
   │  ├─ 🧾 dataset.manifest.yaml
   │  ├─ 🧾 pipeline.manifest.yaml
   │  └─ 🧾 model.manifest.yaml
   ├─ 🧪 examples/                # real manifests used by the project
   ├─ 🛠️ scripts/                 # lint/index/graph tools (optional, recommended)
   │  ├─ ✅ manifest_lint.py       # validate + fail-fast checks
   │  ├─ 🗂️ manifest_index.py      # build/update registry index
   │  └─ 🕸️ manifest_graph.py      # emit graph-ready views
   └─ 📘 README.md                # you are here
```

> [!TIP]
> Treat `schemas/` + `templates/` as **product features**. They are the easiest way to enforce consistency without meetings. 😄

---

## 🧬 Manifest taxonomy

KFM uses a small set of “kinds” that cover most of the system:

| Kind | What it describes | Examples |
|---|---|---|
| `Dataset` | A dataset artifact (raw or derived) | GeoTIFF, GeoJSON, Parquet, CSV, point cloud |
| `Layer` | A map layer as presented (style + source) | Choropleth layer, vector tiles, raster overlay |
| `Pipeline` | A repeatable workflow | ETL, remote sensing processing, geocoding, tiling |
| `Model` | A statistical/ML/simulation model | regression, Bayesian model, topology optimization |
| `Service` | Backend/API capability | tile service, search service, provenance service |
| `UI` | Frontend module | timeline explorer, 3D viewer, WebGL layer renderer |
| `Tool` | A CLI/app/script used by the system | GDAL tool, Python script, SQL job, notebook |

---

## 🧱 Base manifest shape

We aim for a stable “base” that every kind shares.

**Base keys (YAML or JSON):**
- `apiVersion` — version of the manifest format
- `kind` — one of the types above
- `metadata` — identity + ownership + lifecycle
- `spec` — kind-specific content
- `provenance` — lineage + citations + trace IDs
- `validation` — tests, checksums, acceptance gates
- `governance` — license, privacy, security, ethics notes

### Minimal base example

```yaml
apiVersion: kfm.dev/v1alpha1
kind: Dataset

metadata:
  id: kfm.dataset.example.dem_10m_ks
  name: "Example: Kansas DEM 10m"
  description: "Elevation raster clipped to Kansas boundaries."
  owners:
    - name: "KFM Data Team"
      contact: "TBD"
  tags: [kansas, elevation, raster, dem]
  version: 0.1.0
  status: draft
  created: 2026-01-14
  updated: 2026-01-14

spec: {}

provenance:
  sources: []
  steps: []
  citations: []

validation:
  artifacts: []
  checks: []

governance:
  license: "TBD"
  privacy: { classification: public }
  security: { risk: low }
  ethics:
    human_review_required: true
```

---

## 🧩 Type-specific fields

Below are recommended fields per kind. Keep it practical: add only what helps reproduce, audit, or operate.

### 🗃 Dataset (`kind: Dataset`)
Recommended `spec` fields:
- `format`: `GeoTIFF | GeoJSON | Parquet | CSV | LAS | ...`
- `storage`: `path`, `bucket`, `db_table`, `tile_set_id`
- `schema`: column definitions + types
- `spatial`: `crs`, `bbox`, `resolution`, `geometry_type`
- `temporal`: `start`, `end`, `cadence`
- `quality`: null rates, accuracy, validation summaries
- `lineageRef`: pointer to upstream pipeline/model manifests

### 🗺 Layer (`kind: Layer`)
Recommended `spec` fields:
- `sourceDatasetId`
- `rendering`: style rules, symbology, color ramps, labels
- `scaleRules`: min/max zoom, generalization
- `projectionRules`: how to reproject or constrain
- `legend`: human-readable meaning
- `interaction`: popups/fields, filters, time slider mappings

### ⚙️ Pipeline (`kind: Pipeline`)
Recommended `spec` fields:
- `inputs`: dataset IDs + versions + checksums
- `outputs`: dataset IDs + versions + checksums
- `steps`: ordered, named, parameterized steps
- `runtime`: docker/conda/node/java versions, GPU needs
- `scheduling`: cron, triggers, sensor feeds, manual
- `observability`: logs/metrics/traces + SLOs

### 🧠 Model (`kind: Model`)
Recommended `spec` fields:
- `problem`: objective, targets, constraints
- `data`: training/validation splits, sampling rules
- `method`: algorithm family (regression/Bayes/NN/simulation)
- `metrics`: error metrics + acceptance thresholds
- `assumptions`: explicit modeling assumptions
- `verification_validation`: V&V notes for simulation models
- `risk_notes`: known failure modes, biases, domain limits

### 🔌 Service (`kind: Service`)
Recommended `spec` fields:
- `api`: endpoints, contracts, auth
- `dependencies`: DBs, caches, external APIs
- `performance`: expected load, p95 latency targets
- `reliability`: retries, timeouts, rate limits

### 🖥 UI (`kind: UI`)
Recommended `spec` fields:
- `routes`: paths, feature flags
- `bundles`: build outputs, versions
- `rendering`: WebGL settings, tiles, shader references
- `accessibility`: keyboard support, contrast targets
- `dataBindings`: which layer/model/service IDs it uses

---

## 🧾 Provenance and citations

### Provenance: what we record

A manifest should answer:
1. **What is it?**
2. **Where did it come from?**
3. **What happened to it?**
4. **How do I reproduce it?**
5. **How do I cite it?**
6. **What are the known constraints/risks?**

Recommended provenance keys:
- `sources[]` — raw materials (files, APIs, archives, sensors)
- `steps[]` — transformations (tools + parameters + environment)
- `artifacts[]` — outputs with `sha256` and paths
- `citations[]` — bibliographic citations (papers/books/datasets)
- `traceIds[]` — optional (run IDs, pipeline run hashes)

### Citation entry example

```yaml
provenance:
  citations:
    - id: "ref.kfm.maps.design"
      title: "Making Maps: A Visual Guide to Map Design for GIS"
      type: book
      localFile: "making-maps-a-visual-guide-to-map-design-for-gis.pdf"
      usage: "Cartographic rules for symbology & legends"
```

> [!NOTE]
> We treat citations as “data dependencies.” If a layer’s meaning depends on a definition, that definition must be referenced. 📚

---

## ✅ Validation and CI

Validation should be automated *and* human-friendly.

### Recommended gates
- ✅ Manifest is valid YAML/JSON
- ✅ Matches JSON Schema for its `kind`
- ✅ `metadata.id` is unique
- ✅ Inputs/outputs are resolvable (exist in registry)
- ✅ Checksums exist for produced artifacts
- ✅ License + privacy classification is present
- ✅ “No black boxes” rule: provenance has at least 1 source for derived artifacts

> [!TIP]
> Add “manifest lint” to CI early. It prevents drift and unlocks search/index features immediately.

---

## 🧪 Examples

### Example: Pipeline manifest (compact)

```yaml
apiVersion: kfm.dev/v1alpha1
kind: Pipeline
metadata:
  id: kfm.pipeline.example.clip_reproject
  name: "Clip + Reproject Raster"
  version: 0.1.0
  status: draft
spec:
  inputs:
    - datasetId: kfm.dataset.raw.dem_source
      version: "2026.01"
  outputs:
    - datasetId: kfm.dataset.derived.dem_ks_epsg26914
      version: "0.1.0"
  steps:
    - id: "step.1"
      tool: "gdalwarp"
      params:
        dst_crs: "EPSG:26914"
        resampling: "bilinear"
    - id: "step.2"
      tool: "gdal_translate"
      params:
        compress: "LZW"
provenance:
  steps:
    - runId: "TBD"
      executedBy: "ci"
validation:
  checks:
    - id: "sha256.outputs.present"
      severity: "error"
governance:
  license: "TBD"
  privacy: { classification: public }
```

---

## 📚 Project reference library

This repo includes a **library of books/notes** that directly inform manifest fields, schema rules, and implementation standards.

<details>
<summary><strong>📦 Library-to-Manifest Map (click to expand)</strong></summary>

> Each entry below is “used” by mapping it to a manifest concern (data, modeling, performance, UI, security, governance, etc.).  
> If you add a new reference file, also add it here so it becomes part of the project’s shared vocabulary. 🗺️

### 🗺️ Geospatial, Mapping, Remote Sensing, 3D
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf** → project mission, provenance-first rules, clean architecture boundaries  
- **making-maps-a-visual-guide-to-map-design-for-gis.pdf** → layer styling, legends, cartographic clarity  
- **python-geospatial-analysis-cookbook.pdf** → geoprocessing steps, reproducible GIS workflows  
- **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf** → remote sensing pipeline manifests (bands, masking, composites)  
- **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf** → mobile data provenance, location accuracy, participatory mapping notes  
- **Archaeological 3D GIS_26_01_12_17_53_09.pdf** → 3D/volumetric layer manifests, LoD, interpretative vs realistic models

### 🧮 Statistics, Experimental Design, Data Analysis
- **Understanding Statistics & Experimental Design.pdf** → experiment manifests: hypotheses, randomization, replication, validity  
- **regression-analysis-with-python.pdf** → regression workflow manifests: assumptions, residual checks, metrics  
- **Regression analysis using Python - slides-linear-regression.pdf** → teaching-friendly regression checklists & pipeline documentation  
- **graphical-data-analysis-with-r.pdf** → EDA manifests: plots, anomaly checks, exploratory summaries  
- **think-bayes-bayesian-statistics-in-python.pdf** → Bayesian manifests: priors, likelihoods, inference method, posterior checks

### 🤖 Machine Learning, Data Mining, Linear Algebra
- **Understanding Machine Learning: From Theory to Algorithms** → model manifests: learning objective, generalization, complexity considerations  
- **Data Mining (concepts/applications)** → feature engineering + evaluation manifests, mining workflow patterns  
- **(Embedded) Basics of Linear Algebra for Machine Learning** → matrix-focused computations, factorization references for model manifests

### 🛰️ Modeling, Simulation, Optimization, Graphs
- **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf** → simulation manifests: assumptions, discretization, V&V, uncertainty  
- **Generalized Topology Optimization for Structural Design.pdf** → optimization manifests: constraints, solvers, convergence criteria  
- **Spectral Geometry of Graphs.pdf** → graph analytics manifests: spectral features, invariants, algorithm selection notes

### 🗄️ Data Systems, Performance, Databases
- **Database Performance at Scale.pdf** → service + DB manifests: workload mix, indexing, caching, benchmarking, incident notes  
- **Scalable Data Management for Future Hardware.pdf** → storage/compute manifests: memory tiers, concurrency, data placement  
- **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf** → operational DB checklists: schema/index conventions, query tuning notes  
- **Data Spaces.pdf** → data sharing + interoperability manifests: domains, trust, governance metadata

### 🧩 Architecture, Humanism, Law, Flexibility
- **Flexible Software Design (changing requirements)** → manifest system design principles: stable identifiers, regulation, change tolerance  
- **Introduction to Digital Humanism.pdf** → governance manifests: human-centered safeguards, transparency norms  
- **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf** → policy-aware manifests: risk notes, accountability, auditability  
- **Principles of Biological Autonomy - book_9780262381833.pdf** → “systems thinking” framing for autonomy, feedback loops, agent models

### 🧑‍💻 Frontend, Web, Visualization
- **responsive-web-design-with-html5-and-css3.pdf** → UI manifests: accessibility, responsive breakpoints, layout rules  
- **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf** → WebGL UI manifests: render pipeline, shaders, buffers  
- **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf** → media manifests: compression choices, quality/perf tradeoffs

### 🧵 Concurrency, Tooling, Languages, DevOps
- **concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf** → service manifests: threading model, real-time constraints  
- **Bash Notes for Professionals (and embedded multi-book refs)** → tooling manifests: CLI scripts, env assumptions  
- **MATLAB Notes for Professionals** → analysis manifests for MATLAB-based steps  
- **Objective-C Notes for Professionals** → native/mobile module manifests (if needed)  
- **Implementing Programming Languages (Compilers/Interpreters)** → DSL manifests: grammar, parser, codegen pipelines  
- **A programming Books.pdf / B-C / D-E / F-H / I-L / M-N / O-R / S-T / U-X programming Books.pdf** → language reference compendiums for polyglot tool manifests

### 🛡️ Security (defensive posture)
- **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf** → security manifests: threat modeling, hardening checklists (defense)  
- **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf** → secure coding awareness manifests (defense-focused notes)

### 🧠 Deep Learning practice
- **Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf** → training pipeline manifests: experiments, metrics, reproducibility

</details>

---

## 🧭 Next actions (recommended)

- [ ] Add JSON Schemas under `tools/manifests/schemas/`
- [ ] Add templates under `tools/manifests/templates/`
- [ ] Add a `registry.yaml` and enforce “registered before used”
- [ ] Add CI lint: `manifest validate` + uniqueness checks
- [ ] Add a simple manifest indexer that outputs:
  - search index for UI
  - dependency graph (lineage)
  - citation list (bibliography export)

---

## 🧠 Design motto

**“If it matters, it gets a manifest.”**  
Because KFM is a living atlas, *everything changes*—and manifests let us change safely. 🌾🗺️✨

