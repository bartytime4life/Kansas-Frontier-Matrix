# 🧰 `data/work/` — Workbench & Experiment Sandbox

![Scope](https://img.shields.io/badge/scope-data%2Fwork-blue?style=flat-square)
![Mode](https://img.shields.io/badge/mode-WIP%20%2F%20sandbox-yellow?style=flat-square)
![Principle](https://img.shields.io/badge/principle-reproducible-success?style=flat-square)
![Docs](https://img.shields.io/badge/docs-documentation--first-informational?style=flat-square)

> If it can’t be reproduced, it doesn’t count. 🔬  
> This folder is our **controlled chaos**: where ideas become evidence, prototypes, and artifacts — **before** they’re promoted into “canonical” datasets or production pipelines.

---

## 🎯 What belongs in `data/work/`?

✅ Put **work-in-progress** artifacts here:

- 🧪 Experiment runs (ML training, Bayesian inference, regression studies, simulation sweeps)
- 🗺️ GIS/remote sensing scratch work (clipping, reprojection, NDVI derivations, tiles)
- 📓 Notebooks + exploratory analysis (EDA) that is *narrative + traceable*
- 🧱 Intermediate data products (staging → processed → features), **with manifests**
- 📊 Reports and plots created from a specific run (linked to data + code)
- 🌐 UI map prototypes (WebGL demos, Google Maps JS experiments, responsive layout tests)

🚫 **Do not** treat `data/work/` as a permanent source of truth:

- 🔑 Secrets, tokens, credentials (never)
- 🧍 Personally identifying or sensitive data (unless policy explicitly permits & is documented)
- 🧨 Unversioned “mystery files” with no provenance
- 🏛️ Final/published datasets (promote them out after validation)

---

## 🧭 The “KFM-grade” pipeline mindset

Our system documentation pushes a staged pipeline philosophy (ingest → process → store → publish/serve) and emphasizes reliability patterns like **atomic file writes** and **transactional database writes**. 📦🗄️  
Use `data/work/` to **prototype and validate** each stage before promoting.

**In practice, `data/work/` is where we:**
1. 📥 **Ingest** (pull raw inputs from sensors/APIs/files)
2. ✅ **Validate** (schema, CRS, ranges, missingness, checksums)
3. 🧹 **Transform** (clean, join, enrich, feature engineer, resample)
4. 🗄️ **Store** (GeoPackage/Parquet/COG/PostGIS/etc.)
5. 🌐 **Serve** (tiles, APIs, dashboards, map UIs)

📘 Primary reference: KFM Technical Documentation  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)  
🧱 Documentation style guide: MARKDOWN guide v13  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
🔬 Scientific rigor protocol: Master Coder / Scientific Method  [oai_citation:2‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  

---

## 🗂️ Suggested layout (flexible, but consistent)

> You can adapt the exact folders — the **non‑negotiable** is: every meaningful output is traceable to inputs + code + parameters.

```text
📁 data/work/
├── 📁 _templates/              # ✅ copy/paste starter templates (manifests, cards)
├── 📁 _scratch/                # ⚠️ truly temporary throwaway (safe to delete)
├── 📁 experiments/             # 🧪 repeatable runs (preferred home)
│   ├── 📁 2026-01-02__ndvi__landsat8/
│   │   ├── 📄 README.md
│   │   ├── 📄 manifest.yaml
│   │   ├── 📁 raw/
│   │   ├── 📁 notebooks/
│   │   ├── 📁 src/
│   │   ├── 📁 processed/
│   │   ├── 📁 features/
│   │   ├── 📁 models/
│   │   ├── 📁 viz/
│   │   └── 📁 exports/
│   └── 📁 2026-01-05__ml__yield_forecast_v01/
├── 📁 datasets/                # 📦 curated WIP datasets (still not “released”)
├── 📁 sims/                    # 🛰️ simulation campaigns (parameter sweeps, V&V)
├── 📁 viz/                     # 🌐 prototypes: maps, WebGL, dashboards
└── 📄 README.md                # 👈 you are here
```

---

## 🧾 Work Package Standard (WPS)

Every folder under `data/work/` that you want others (or future-you) to trust should be a **Work Package**.

### ✅ Naming convention

Use a timestamp + domain + slug:

- `YYYY-MM-DD__domain__short_slug/`
- Optional: `__v01`, `__v02` as it stabilizes

Examples:
- `2026-01-02__remote_sensing__ndvi_landsat8/`
- `2026-01-04__stats__soil_moisture_regression_v02/`
- `2026-01-10__viz__webgl_tileset_prototype/`

### ✅ Required files (minimum)

- `README.md` — **purpose + hypotheses + results + next steps**
- `manifest.yaml` — inputs, outputs, parameters, environment, hashes
- `raw/` — immutable raw inputs (or pointers if too large)
- `src/` or `notebooks/` — code that produces outputs

### 🧩 Recommended files (strongly encouraged)

- `data_dictionary.md` — field meanings, units, codes
- `schema/` — JSON schema / SQL schema / GeoPackage schema notes
- `environment/` — `requirements.txt`, `environment.yml`, `pip-freeze.txt`, `Dockerfile`
- `provenance.md` — “how we got here”, especially if multiple sources

---

## 🧬 Templates (copy into `_templates/`)

### `manifest.yaml` (starter)

```yaml
id: 2026-01-02__remote_sensing__ndvi_landsat8
owner: "@your-handle"
created_at: "2026-01-02"
status: wip # wip | review | archived | promoted

goal:
  question: "What is the NDVI trend over region X during time range Y?"
  hypothesis: "NDVI decreases in drought weeks and rebounds after rainfall."

inputs:
  - name: landsat8_scene_collection
    type: raster
    source: "external"
    pointer: "SEE sources.md or a data catalog id"
    notes: "Never overwrite raw. Store checksums."

process:
  pipeline: ingest->validate->transform->store->serve
  steps:
    - validate_crs: "EPSG:xxxx"
    - compute_index: "NDVI = (NIR - RED) / (NIR + RED)"
    - resample: "10m"
    - tile: "xyz"

parameters:
  region: "ROI definition or file reference"
  date_range: ["YYYY-MM-DD", "YYYY-MM-DD"]
  random_seed: 1337

outputs:
  - name: ndvi_timeseries
    path: processed/ndvi_timeseries.parquet
  - name: ndvi_raster
    path: processed/ndvi_cog.tif
  - name: quicklook_plot
    path: viz/ndvi_trend.png

environment:
  runtime: "python"
  lockfiles:
    - environment/requirements.txt
    - environment/pip-freeze.txt

validation:
  checks:
    - "no null geometry"
    - "value range sanity"
    - "reprojection verified"
```

### `README.md` (Scientific Method friendly)

```markdown
# Work Package: <id>

## 🧠 Question / Problem
...

## 📚 Background
...

## 🧪 Hypothesis
...

## 🧰 Method (Protocol)
- Data sources:
- Tools:
- Steps:

## 📦 Data & Provenance
- Raw:
- Processed:
- Checksums:

## 📊 Analysis
...

## ✅ Results
...

## 🧾 Conclusion
...

## 🔁 Next Steps
...
```

*(Template philosophy aligns with the scientific-method + reproducibility protocol.)*  [oai_citation:3‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## ✅ Quality checklists (fast, practical)

### 🗺️ Geospatial sanity checklist
- [ ] CRS is explicitly stated (and consistent across layers)
- [ ] Units make sense (meters vs degrees)
- [ ] Geometry validity checks pass (no self-intersections)
- [ ] Raster nodata is defined and preserved
- [ ] Map outputs include legends, scalebars (when relevant), and clear symbology decisions

Helpful refs:
- GIS basics  [oai_citation:4‡Geographic Information System Basics - geographic-information-system-basics.pdf](file-service://file-Kjn2enYFqXQtK3J4zN2DWz)  
- Geoprocessing with Python  [oai_citation:5‡geoprocessing-with-python.pdf](file-service://file-NkXrdB4FwTruwhQ9Ggn53T)  
- Making Maps (design)  [oai_citation:6‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)  
- Python Geospatial Analysis Cookbook  [oai_citation:7‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)  

### 📈 Statistics sanity checklist (avoid self‑inflicted wounds)
- [ ] Are we doing **exploration** or **confirmation**? (label it)
- [ ] Multiple comparisons accounted for (or explicitly scoped)
- [ ] Train/validation/test leakage avoided (if predictive)
- [ ] Effect sizes + uncertainty reported (not just “significance”)
- [ ] Assumptions checked (residuals, heteroskedasticity, independence)

Helpful refs:
- Understanding Statistics & Experimental Design  [oai_citation:8‡Understanding Statistics & Experimental Design.pdf](file-service://file-SdX6LMgi1uDRk5kd4H4Bg3)  
- Statistics Done Wrong  [oai_citation:9‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd)  
- Regression Analysis with Python  [oai_citation:10‡regression-analysis-with-python.pdf](file-service://file-NCS6ThhvajwNUm4crVVcGM)  
- Graphical Data Analysis with R  [oai_citation:11‡graphical-data-analysis-with-r.pdf](file-service://file-K7oxq5mFmdE9HrPPev6c7L)  

### 🤖 ML / Deep Learning sanity checklist
- [ ] Dataset documented (biases, limitations, splits, hashes)
- [ ] Random seeds recorded (when possible)
- [ ] Metrics logged per run + saved to `outputs/metrics.json`
- [ ] Model artifacts include a **Model Card** (intent, limits, evaluation)
- [ ] Baselines included (simple model first)

Helpful refs:
- Deep Learning in Python — Prerequisites  [oai_citation:12‡deep-learning-in-python-prerequisites.pdf](file-service://file-9pQhD3FNUGoYzmKrdm26cg)  
- Artificial Neural Networks: An Introduction  [oai_citation:13‡Artificial-neural-networks-an-introduction.pdf](file-service://file-DhnuQ12UtyRb9q5u5CptWo)  
- AI Foundations of Computational Agents  [oai_citation:14‡AI Foundations of Computational Agents 3rd Ed.pdf](file-service://file-BYuPtX8r1doBaqdetoMxC7)  
- Data Mining Concepts & Applications  [oai_citation:15‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  
- Applied Data Science with Python & Jupyter  [oai_citation:16‡applied-data-science-with-python-and-jupyter.pdf](file-service://file-2PdBHtR24Wq7MYWfG8agQo)  

### 🛰️ Simulation / modeling sanity checklist
- [ ] Inputs/initial conditions captured
- [ ] Validation strategy described (what would falsify the model?)
- [ ] Uncertainty quantified (at least sensitivity sweeps)
- [ ] Results are reproducible (config + environment + seed)
- [ ] Outputs include clear units and metadata

Helpful refs:
- Scientific Modeling & Simulation (NASA-grade)  [oai_citation:17‡Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf](file-service://file-THLZMx2BnXCR4bvvPJsMQm)  
- Bayesian Computational Methods (UQ)  [oai_citation:18‡Bayesian computational methods.pdf](file-service://file-6NmuxfJsrfDTxQmEi8A7jo)  
- MATLAB Programming for Engineers  [oai_citation:19‡MATLAB Programming for Engineers Stephen J. Chapman.pdf](file-service://file-GVz6J2tWsQSJL4sFY1Niqe)  
- Generalized Topology Optimization  [oai_citation:20‡Generalized Topology Optimization for Structural Design.pdf](file-service://file-PzydVyvSPdXWqYrXeFCNzj)  
- Spectral Geometry of Graphs  [oai_citation:21‡Spectral Geometry of Graphs.pdf](file-service://file-DWxRbQDZGktGtiWtzAQxs8)  

---

## 🌐 Serving & visualization prototypes (maps + WebGL)

When prototyping dashboards/maps:
- Keep a `viz/` folder inside the work package
- Save screenshots + a short “what this proves” note
- Prefer responsive layouts early (mobile constraints reveal design problems fast)

Helpful refs:
- Responsive Web Design (HTML5/CSS3)  [oai_citation:22‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)  
- WebGL Programming Guide  [oai_citation:23‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)  
- Computer Graphics (Java 2D/3D)  [oai_citation:24‡Computer Graphics using JAVA 2D & 3D.pdf](file-service://file-Qgv1x2d8RuqkEwVmNXFT1B)  
- Google Maps JavaScript API Cookbook  [oai_citation:25‡google-maps-javascript-api-cookbook.pdf](file-service://file-6w897pmf6KhF1cHXFQ1zdf)  

---

## 🗄️ Data engineering & storage notes (practical)

- Prefer **append-only** patterns for raw data
- Prefer **atomic writes** for files (write temp → rename) and **transactions** for DB
- Document indexes/partitions when performance matters
- Keep “big stuff” out of Git unless LFS or external storage is defined

Helpful refs:
- Scalable Data Management for Future Hardware  [oai_citation:26‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)  
- PostgreSQL Notes  [oai_citation:27‡PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf](file-service://file-742sw3gADJniEdmC19JeAC)  
- MySQL Notes  [oai_citation:28‡MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf](file-service://file-GQ5jWwmLZCFb6enxwykaRh)  
- Node.js Notes  [oai_citation:29‡Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf](file-service://file-9qS1yEFvCBXbDdtTfpt3Ye)  
- Clean Architectures in Python  [oai_citation:30‡clean-architectures-in-python.pdf](file-service://file-6YHot4AqfpdbcrdfiYfpHM)  
- Implementing Programming Languages  [oai_citation:31‡implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf](file-service://file-JaNsY7yoyJTAzMJSwt9LDA)  
- Docker (reproducible runtimes)  [oai_citation:32‡Introduction-to-Docker.pdf](file-service://file-5SALje8G4GDUXHUM3P3LuU)  

---

## 🧠 Ethics & human context (don’t skip this)

Even “just data work” shapes outcomes. Document:
- What the system is optimizing for
- Who could be harmed by errors or bias
- What is **out of scope** and why

Helpful refs:
- Introduction to Digital Humanism  [oai_citation:33‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  
- Principles of Biological Autonomy  [oai_citation:34‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf)  

---

## 📚 Reference Shelf (all project files)

> This is the project’s **local knowledge library**. Use it to justify decisions, choose methods, and keep a consistent engineering + research standard across the team.

<details>
<summary>🧭 Core system docs & protocols</summary>

- 📘 Kansas Frontier Matrix (KFM) — Comprehensive Technical Documentation  [oai_citation:35‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)  
- 🧱 MARKDOWN Guide v13 (documentation style + deterministic pipelines)  [oai_citation:36‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- 🔬 Scientific Method / Research / Master Coder Protocol  [oai_citation:37‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  

</details>

<details>
<summary>📈 Statistics, experiment design, regression</summary>

- 🧪 Understanding Statistics & Experimental Design  [oai_citation:38‡Understanding Statistics & Experimental Design.pdf](file-service://file-SdX6LMgi1uDRk5kd4H4Bg3)  
- ⚠️ Statistics Done Wrong  [oai_citation:39‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd)  
- 📉 Regression Analysis with Python  [oai_citation:40‡regression-analysis-with-python.pdf](file-service://file-NCS6ThhvajwNUm4crVVcGM)  
- 📊 Graphical Data Analysis with R  [oai_citation:41‡graphical-data-analysis-with-r.pdf](file-service://file-K7oxq5mFmdE9HrPPev6c7L)  
- 📚 Data Science & Machine Learning (Mathematical & Statistical Methods)  [oai_citation:42‡Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf](file-service://file-MRNb2uGPEwpkSDsxF983PC)  
- 🎲 Bayesian Computational Methods  [oai_citation:43‡Bayesian computational methods.pdf](file-service://file-6NmuxfJsrfDTxQmEi8A7jo)  

</details>

<details>
<summary>🤖 AI / ML / Agents</summary>

- 🧠 Deep Learning in Python — Prerequisites  [oai_citation:44‡deep-learning-in-python-prerequisites.pdf](file-service://file-9pQhD3FNUGoYzmKrdm26cg)  
- 🕸️ Artificial Neural Networks: An Introduction  [oai_citation:45‡Artificial-neural-networks-an-introduction.pdf](file-service://file-DhnuQ12UtyRb9q5u5CptWo)  
- 🧩 AI Foundations of Computational Agents (3rd Ed.)  [oai_citation:46‡AI Foundations of Computational Agents 3rd Ed.pdf](file-service://file-BYuPtX8r1doBaqdetoMxC7)  
- ⛏️ Data Mining Concepts & Applications  [oai_citation:47‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  
- 📓 Applied Data Science with Python & Jupyter  [oai_citation:48‡applied-data-science-with-python-and-jupyter.pdf](file-service://file-2PdBHtR24Wq7MYWfG8agQo)  

</details>

<details>
<summary>🛰️ Modeling, simulation, optimization, graphs</summary>

- 🛰️ Scientific Modeling & Simulation (NASA-grade guide)  [oai_citation:49‡Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf](file-service://file-THLZMx2BnXCR4bvvPJsMQm)  
- 🧮 MATLAB Programming for Engineers  [oai_citation:50‡MATLAB Programming for Engineers Stephen J. Chapman.pdf](file-service://file-GVz6J2tWsQSJL4sFY1Niqe)  
- 🏗️ Generalized Topology Optimization for Structural Design  [oai_citation:51‡Generalized Topology Optimization for Structural Design.pdf](file-service://file-PzydVyvSPdXWqYrXeFCNzj)  
- 🕸️ Spectral Geometry of Graphs  [oai_citation:52‡Spectral Geometry of Graphs.pdf](file-service://file-DWxRbQDZGktGtiWtzAQxs8)  
- 🗄️ Scalable Data Management for Future Hardware  [oai_citation:53‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)  

</details>

<details>
<summary>🗺️ GIS, mapping, remote sensing (Python + GEE)</summary>

- 🧭 Geographic Information System Basics  [oai_citation:54‡Geographic Information System Basics - geographic-information-system-basics.pdf](file-service://file-Kjn2enYFqXQtK3J4zN2DWz)  
- 🧰 Geoprocessing with Python  [oai_citation:55‡geoprocessing-with-python.pdf](file-service://file-NkXrdB4FwTruwhQ9Ggn53T)  
- 🎨 Making Maps (Map design for GIS)  [oai_citation:56‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)  
- 🐍 Python Geospatial Analysis Cookbook  [oai_citation:57‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)  
- ☁️ Cloud‑Based Remote Sensing with Google Earth Engine  [oai_citation:58‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-CXGLTw8wpR4uKWWqjrGkyk)  
- 🛰️ Google Earth Engine Applications  [oai_citation:59‡Google Earth Engine Applications.pdf](file-service://file-SmoZrQ3nZSAdHHNqcVzYCq)  

</details>

<details>
<summary>🌐 Web, maps, graphics & visualization</summary>

- 📱 Responsive Web Design (HTML5/CSS3)  [oai_citation:60‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)  
- 🎮 WebGL Programming Guide  [oai_citation:61‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)  
- 🗺️ Google Maps JavaScript API Cookbook  [oai_citation:62‡google-maps-javascript-api-cookbook.pdf](file-service://file-6w897pmf6KhF1cHXFQ1zdf)  
- 🧊 Computer Graphics (Java 2D/3D)  [oai_citation:63‡Computer Graphics using JAVA 2D & 3D.pdf](file-service://file-Qgv1x2d8RuqkEwVmNXFT1B)  

</details>

<details>
<summary>🏗️ Architecture, languages, databases, DevOps</summary>

- 🧼 Clean Architectures in Python  [oai_citation:64‡clean-architectures-in-python.pdf](file-service://file-6YHot4AqfpdbcrdfiYfpHM)  
- 🧠 Implementing Programming Languages (Compilers/Interpreters)  [oai_citation:65‡implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf](file-service://file-JaNsY7yoyJTAzMJSwt9LDA)  
- 🟩 Node.js Notes for Professionals  [oai_citation:66‡Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf](file-service://file-9qS1yEFvCBXbDdtTfpt3Ye)  
- 🐘 PostgreSQL Notes for Professionals  [oai_citation:67‡PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf](file-service://file-742sw3gADJniEdmC19JeAC)  
- 🐬 MySQL Notes for Professionals  [oai_citation:68‡MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf](file-service://file-GQ5jWwmLZCFb6enxwykaRh)  
- 🐳 Introduction to Docker  [oai_citation:69‡Introduction-to-Docker.pdf](file-service://file-5SALje8G4GDUXHUM3P3LuU)  

</details>

<details>
<summary>🧭 Ethics & systems thinking</summary>

- 🌍 Introduction to Digital Humanism  [oai_citation:70‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  
- 🧬 Principles of Biological Autonomy  [oai_citation:71‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf)  

</details>

<details>
<summary>⚠️ Files present but currently unreadable (replace with a clean copy)</summary>

- 🥋 Command Line Kung Fu (Bash scripting tricks / one‑liners) — PDF appears corrupted in this repo copy  
- 🗺️ Google Maps API Succinctly — PDF appears corrupted in this repo copy  

</details>

---

## 🧹 Cleanup & promotion rules

When something becomes **useful beyond the experiment**:

1. ✅ Add or update `manifest.yaml` + provenance
2. ✅ Re-run from scratch (prove it’s reproducible)
3. ✅ Promote outputs into the repo’s “canonical” data/artifact location (team-defined)
4. ✅ Leave behind a **thin pointer** here (README + links + commit hash)

When something is **dead**:
- Move to `archived/` or delete it.
- Keep a tiny README explaining why it was dropped (prevents future rework).

---

## 📎 Glossary (quick)
- **CRS**: Coordinate Reference System
- **ETL**: Extract → Transform → Load
- **NDVI**: Normalized Difference Vegetation Index
- **UQ / V&V**: Uncertainty Quantification / Verification & Validation
- **COG**: Cloud-Optimized GeoTIFF
- **WMS/WFS**: Web map services (common GIS serving patterns)

---

🧠 **Rule of thumb:** if you can’t answer “where did this come from?” in 10 seconds… it doesn’t belong in `data/work/` yet.