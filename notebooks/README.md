# 📓 Notebooks — Kansas Frontier Matrix System (KFM)

![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![GIS](https://img.shields.io/badge/GIS-Geospatial-success)
![Remote%20Sensing](https://img.shields.io/badge/Remote%20Sensing-GEE%20%26%20EO-informational)
![Docker](https://img.shields.io/badge/Docker-Recommended-2496ED)

Welcome to the **KFM notebooks workspace** 🧭 — a practical lab for:
- 🧪 exploratory research & rapid prototyping  
- 🗺️ geospatial + remote sensing experiments  
- 📊 statistics, modeling, validation, and “don’t fool yourself” checks  
- 🤖 ML/AI baselines, agent-style decision logic, and model eval  
- 🌐 map/UI visualization spikes (Google Maps, WebGL)  
- 🧱 architecture proof-of-concepts before productionizing into `src/` / services  

> ✅ **Rule of thumb:** notebooks are for *learning, exploration, and reproducible experiments*.  
> 🏭 Anything that becomes “real” should graduate into production modules, tests, pipelines, and docs.

---

## 🧭 Where this fits in the repo

- **Production code**: lives in `src/` / services (not here).
- **Notebooks**: are the *sandbox + research journal* with repeatable outputs.
- **Artifacts**: notebooks should export clean outputs into an `artifacts/`-style folder (gitignored).

---

## 🗂️ Suggested folder layout

```text
📁 notebooks/
├─ 📄 README.md
├─ 📁 _templates/              🧩 notebook templates (EDA, modeling, mapping, report)
├─ 📁 _data/                   🚫 local-only datasets (gitignored)
├─ 📁 _artifacts/              📦 exported plots/tables/models (gitignored)
├─ 📁 _figures/                🖼️ committed figures used in docs
├─ 🧭 00_orientation/
├─ 🧰 01_tooling/
├─ 🗺️ 02_gis_core/
├─ 🛰️ 03_remote_sensing/
├─ 📊 04_stats/
├─ 🤖 05_ml_agents/
├─ 🧪 06_simulation_optimization/
├─ 🌐 07_web_mapping_viz/
├─ 🧬 08_language_tools/
└─ 🧠 09_human_factors/
```

---

## 🧩 Notebook Tracks (what to expect)

| Track | Folder | Focus | Reference anchors 📚 |
|---|---|---|---|
| 🧭 Foundations | `00_orientation/` | KFM context, architecture, glossary, “how we work” | KFM Technical Docs • Clean Architecture • Digital Humanism |
| 🧰 Tooling | `01_tooling/` | CLI, Docker, DB quickstarts, runtime hygiene | Docker • Bash • Postgres/MySQL • Node.js |
| 🗺️ GIS Core | `02_gis_core/` | projections, vector/raster, geoprocessing | GIS Basics • Geoprocessing w/ Python • Python Geospatial recipes |
| 🛰️ Remote Sensing | `03_remote_sensing/` | Earth Engine workflows, time-series, change detection | Cloud-based RS w/ GEE • GEE Applications |
| 📊 Statistics | `04_stats/` | EDA, regression, Bayesian, experimental design, pitfalls | Stats/Exp Design • Regression • Bayesian Methods • Stats Done Wrong • Graphical Data Analysis (R) |
| 🤖 ML + Agents | `05_ml_agents/` | mining, agents, deep learning prerequisites, ANN baselines | Data Mining • Computational Agents • Deep Learning prereqs • ANN intro • Math/Stats for ML |
| 🧪 Simulation + Optimization | `06_simulation_optimization/` | simulation patterns, model validation, optimization, graphs | NASA-grade modeling/sim • Topology optimization • Spectral graphs • Scalable data mgmt • MATLAB |
| 🌐 Web Maps + Viz | `07_web_mapping_viz/` | cartography, UI spikes, browser rendering | Making Maps • Google Maps API (succinct + cookbook) • WebGL • Responsive Web Design • Java 2D/3D Graphics |
| 🧬 Language Tools | `08_language_tools/` | DSLs, parsers, compilers for domain workflows | Implementing Programming Languages |
| 🧠 Human Factors | `09_human_factors/` | autonomy, ethics, governance constraints | Biological Autonomy • Digital Humanism |

---

## 🚀 Quick start

### Option A — Local (fastest)
```bash
cd notebooks
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

### Option B — Docker (recommended for reproducibility 🐳)
If the repo includes a Docker setup, prefer running notebooks in a container to keep geospatial dependencies sane (GDAL, PROJ, GEOS, etc.).

Typical pattern:
```bash
docker compose up --build
# then open the Jupyter URL printed in the logs
```

> 🔐 Never bake secrets (tokens/keys) into images. Use `.env` + runtime environment variables.

---

## ✅ Notebook conventions (KFM standard)

### 🏷️ Naming
Use a **two-digit prefix** for ordering + a short, verb-first slug:
- `00_intro_kfm_context.ipynb`
- `02_vector_overlay_clip.ipynb`
- `03_gee_ndvi_timeseries.ipynb`
- `04_regression_baselines.ipynb`

### 🧼 Reproducibility checklist
- [ ] “Parameters” cell at the top (paths, region AOI, dates, EPSG, seeds)
- [ ] deterministic random seeds (`numpy`, `random`, frameworks)
- [ ] record environment info (python version, key packages)
- [ ] write outputs to `notebooks/_artifacts/` (gitignored) or `notebooks/_figures/` (committed)
- [ ] keep notebooks readable: markdown + headings + short code cells
- [ ] avoid giant outputs; prefer saved artifacts (CSV/GeoJSON/Parquet/PNG)

### 🗺️ Geospatial hygiene
- Always store CRS metadata (EPSG) and document reprojection steps.
- Keep AOIs explicit (geometry + CRS + intended resolution).
- Prefer “analysis-ready” layers; document QA steps (cloud masking, filtering).

---

## 🧪 Notebook roadmap (starter set)

> These are **recommended** notebooks to build/maintain as the project evolves.

### 🧭 00_orientation/
- [ ] `00_project_overview_and_goals.ipynb`
- [ ] `01_architecture_walkthrough_clean_layers.ipynb`
- [ ] `02_data_dictionary_and_entities.ipynb`

### 🧰 01_tooling/
- [ ] `00_cli_basics_and_project_scripts.ipynb`
- [ ] `01_docker_dev_workflow.ipynb`
- [ ] `02_postgres_postgis_quickstart.ipynb`
- [ ] `03_node_service_spike_optional.ipynb`

### 🗺️ 02_gis_core/
- [ ] `00_gis_basics_raster_vs_vector.ipynb`
- [ ] `01_projections_reprojection_crs.ipynb`
- [ ] `02_geoprocessing_buffer_intersect_clip.ipynb`
- [ ] `03_zonal_stats_and_feature_engineering.ipynb`

### 🛰️ 03_remote_sensing/
- [ ] `00_gee_setup_and_first_map.ipynb`
- [ ] `01_gee_image_collection_filter_map_reduce.ipynb`
- [ ] `02_cloud_masking_and_composites.ipynb`
- [ ] `03_change_detection_two_date.ipynb`
- [ ] `04_timeseries_metrics_and_exports.ipynb`

### 📊 04_stats/
- [ ] `00_eda_playbook.ipynb`
- [ ] `01_regression_baselines_and_diagnostics.ipynb`
- [ ] `02_experimental_design_templates.ipynb`
- [ ] `03_bayesian_modeling_intro.ipynb`
- [ ] `04_common_stats_failures_and_fixes.ipynb`

### 🤖 05_ml_agents/
- [ ] `00_data_mining_feature_selection.ipynb`
- [ ] `01_agents_decision_rules_and_simulation_hooks.ipynb`
- [ ] `02_deep_learning_prereqs_math_checks.ipynb`
- [ ] `03_neural_networks_baseline_classifier.ipynb`

### 🧪 06_simulation_optimization/
- [ ] `00_simulation_validation_and_uncertainty.ipynb`
- [ ] `01_topology_optimization_concepts.ipynb`
- [ ] `02_spectral_graph_features_and_clustering.ipynb`
- [ ] `03_scalability_patterns_for_big_geodata.ipynb`
- [ ] `04_matlab_to_python_bridge_notes_optional.ipynb`

### 🌐 07_web_mapping_viz/
- [ ] `00_cartography_and_map_design_checklist.ipynb`
- [ ] `01_google_maps_basics_overlay_layers.ipynb`
- [ ] `02_google_maps_advanced_recipes.ipynb`
- [ ] `03_webgl_rendering_spike.ipynb`
- [ ] `04_responsive_ui_layout_notes.ipynb`

### 🧬 08_language_tools/
- [ ] `00_dsl_sketch_for_kfm_pipelines.ipynb`
- [ ] `01_parsing_and_ast_basics.ipynb`

### 🧠 09_human_factors/
- [ ] `00_digital_humanism_risks_controls_checklist.ipynb`
- [ ] `01_autonomy_systems_feedback_loops_notes.ipynb`

---

## 🔐 Data, licensing, and ethics notes

- 🧾 Many PDFs in the reference library are **copyrighted** (education/internal use).  
  Do **not** redistribute them publicly unless licensing allows it.
- 🌍 Some references are **Open Access** (e.g., Springer OA / CC licenses). Still cite properly.
- 🧠 Ethics is not a “nice-to-have.” KFM explicitly includes **human-centered** and **governance** concerns (privacy, bias, autonomy, accountability).

---

## 📚 Reference library (all project PDFs)

> Recommended location: `docs/library/` (or similar).  
> If your repo stores these elsewhere, update paths and links.

### 🧭 KFM Core & Architecture
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** (`Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`)
- **Clean Architectures in Python** (`clean-architectures-in-python.pdf`)

### 🧰 Dev Workflow & Infrastructure
- **Introduction to Docker** (`Introduction-to-Docker.pdf`)
- **Command Line Kung Fu (Bash scripting & one-liners)** (`Command Line Kung Fu_ Bash Scripting Tricks, Linux Shell Programming Tips, and Bash One-liners - Command_Line_Kung_Fu_Bash_Scripting_Tricks,_Linux_Shell_Program.pdf`)
- **Node.js Notes for Professionals** (`Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf`)
- **PostgreSQL Notes for Professionals** (`PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`)
- **MySQL Notes for Professionals** (`MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf`)
- **Scalable Data Management for Future Hardware** (`Scalable Data Management for Future Hardware.pdf`)

### 🗺️ GIS & Geoprocessing
- **Geographic Information System Basics** (`Geographic Information System Basics - geographic-information-system-basics.pdf`)
- **Geoprocessing with Python** (`geoprocessing-with-python.pdf`)
- **Python Geospatial Analysis Cookbook** (`python-geospatial-analysis-cookbook.pdf`)
- **Making Maps (visual guide to map design for GIS)** (`making-maps-a-visual-guide-to-map-design-for-gis.pdf`)

### 🛰️ Remote Sensing & Earth Engine
- **Cloud-Based Remote Sensing with Google Earth Engine (Fundamentals & Applications)** (`Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`)
- **Google Earth Engine Applications** (`Google Earth Engine Applications.pdf`)

### 🌐 Web Mapping & Visualization
- **Google Maps API Succinctly** (`Google Maps API Succinctly - google_maps_api_succinctly.pdf`)
- **Google Maps JavaScript API Cookbook** (`google-maps-javascript-api-cookbook.pdf`)
- **WebGL Programming Guide** (`webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`)
- **Responsive Web Design with HTML5 and CSS3** (`responsive-web-design-with-html5-and-css3.pdf`)
- **Computer Graphics using JAVA 2D & 3D** (`Computer Graphics using JAVA 2D & 3D.pdf`)

### 📊 Statistics, Experimentation, and Analysis
- **Applied Data Science with Python and Jupyter** (`applied-data-science-with-python-and-jupyter.pdf`)
- **Understanding Statistics & Experimental Design** (`Understanding Statistics & Experimental Design.pdf`)
- **Regression Analysis with Python** (`regression-analysis-with-python.pdf`)
- **Bayesian Computational Methods** (`Bayesian computational methods.pdf`)
- **Statistics Done Wrong** (`Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf`)
- **Graphical Data Analysis with R** (`graphical-data-analysis-with-r.pdf`)

### 🤖 AI / ML Foundations
- **Data Science & Machine Learning (Mathematical & Statistical Methods)** (`Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf`)
- **Data Mining Concepts & Applications** (`Data Mining Concepts & applictions.pdf`)
- **AI Foundations of Computational Agents (3rd Ed.)** (`AI Foundations of Computational Agents 3rd Ed.pdf`)
- **Deep Learning in Python — Prerequisites** (`deep-learning-in-python-prerequisites.pdf`)
- **Artificial Neural Networks — An Introduction** (`Artificial-neural-networks-an-introduction.pdf`)

### 🧪 Simulation, Optimization, and Modeling
- **Scientific Modeling and Simulation — NASA-Grade Guide** (`Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`)
- **Generalized Topology Optimization for Structural Design** (`Generalized Topology Optimization for Structural Design.pdf`)
- **Spectral Geometry of Graphs** (`Spectral Geometry of Graphs.pdf`)
- **MATLAB Programming for Engineers** (`MATLAB Programming for Engineers Stephen J. Chapman.pdf`)

### 🧬 Languages & Tooling (advanced)
- **Implementing Programming Languages (Compilers & Interpreters)** (`implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf`)

### 🧠 Human-Centered + Ethics
- **Introduction to Digital Humanism** (`Introduction to Digital Humanism.pdf`)
- **Principles of Biological Autonomy** (`Principles of Biological Autonomy - book_9780262381833.pdf`)

---

<details>
<summary>📎 ChatGPT attachment link tokens (safe to remove for GitHub)</summary>

These are conversation-specific links that help surface the PDFs in ChatGPT UI.

- geoprocessing-with-python.pdf —  [oai_citation:0‡geoprocessing-with-python.pdf](file-service://file-NkXrdB4FwTruwhQ9Ggn53T)  
- making-maps-a-visual-guide-to-map-design-for-gis.pdf —  [oai_citation:1‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)  
- google-maps-javascript-api-cookbook.pdf —  [oai_citation:2‡google-maps-javascript-api-cookbook.pdf](file-service://file-6w897pmf6KhF1cHXFQ1zdf)  
- Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf —  [oai_citation:3‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-CXGLTw8wpR4uKWWqjrGkyk)  
- Google Earth Engine Applications.pdf —  [oai_citation:4‡Google Earth Engine Applications.pdf](file-service://file-SmoZrQ3nZSAdHHNqcVzYCq)  
- Geographic Information System Basics - geographic-information-system-basics.pdf —  [oai_citation:5‡Geographic Information System Basics - geographic-information-system-basics.pdf](file-service://file-Kjn2enYFqXQtK3J4zN2DWz)  
- responsive-web-design-with-html5-and-css3.pdf —  [oai_citation:6‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)  
- webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf —  [oai_citation:7‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)  
- python-geospatial-analysis-cookbook.pdf —  [oai_citation:8‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)  
- clean-architectures-in-python.pdf —  [oai_citation:9‡clean-architectures-in-python.pdf](file-service://file-6YHot4AqfpdbcrdfiYfpHM)  
- implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf —  [oai_citation:10‡implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf](file-service://file-JaNsY7yoyJTAzMJSwt9LDA)  
- Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf —  [oai_citation:11‡Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf](file-service://file-9qS1yEFvCBXbDdtTfpt3Ye)  
- PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf —  [oai_citation:12‡PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf](file-service://file-742sw3gADJniEdmC19JeAC)  
- MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf —  [oai_citation:13‡MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf](file-service://file-GQ5jWwmLZCFb6enxwykaRh)  
- Principles of Biological Autonomy - book_9780262381833.pdf —  [oai_citation:14‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf)  
- Introduction to Digital Humanism.pdf —  [oai_citation:15‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  
- MATLAB Programming for Engineers Stephen J. Chapman.pdf —  [oai_citation:16‡MATLAB Programming for Engineers Stephen J. Chapman.pdf](file-service://file-GVz6J2tWsQSJL4sFY1Niqe)  
- applied-data-science-with-python-and-jupyter.pdf —  [oai_citation:17‡applied-data-science-with-python-and-jupyter.pdf](file-service://file-2PdBHtR24Wq7MYWfG8agQo)  
- Introduction-to-Docker.pdf —  [oai_citation:18‡Introduction-to-Docker.pdf](file-service://file-5SALje8G4GDUXHUM3P3LuU)  
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf —  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)  

</details>