# 🗂️ Tools ▸ Catalogs

<kbd>KFM</kbd> <kbd>provenance-first</kbd> <kbd>catalog-driven</kbd> <kbd>source-of-truth</kbd> <kbd>WIP</kbd>

This folder is the **registry brain** 🧠 of the Kansas Frontier Matrix (KFM): small, structured “catalog” files that keep the platform **searchable 🔎, mappable 🗺️, auditable 🧾, and modelable 🧪** without hard-coding knowledge into pipelines or UI.

> 💡 If it changes (datasets, layers, sources, sensors, models, rules)… it belongs in a **catalog**.

---

## 📌 Jump table

- [🧭 Why catalogs exist](#-why-catalogs-exist)
- [📁 Recommended folder layout](#-recommended-folder-layout)
- [🧾 Catalog schemas](#-catalog-schemas)
- [🧬 Provenance and citation rules](#-provenance-and-citation-rules)
- [📚 Reference library](#-reference-library)
- [🧑‍🔧 Role-based “what to read” routes](#-role-based-what-to-read-routes)
- [🛠️ Contribution workflow](#️-contribution-workflow)

---

## 🧭 Why catalogs exist

KFM’s mission centers on a **provenance-first** worldview: every dataset, map layer, and AI output should be traceable to its **sources + processing steps** (no black boxes) and remain inspectable in the UI.  
<!--  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) -->

Catalogs make that doable at scale by acting as:
- ✅ **Human-readable specs** (reviewable in PRs)
- ✅ **Machine-validated manifests** (lintable in CI)
- ✅ **Stable IDs** (so layers/models don’t break when filenames change)
- ✅ **Reproducibility anchors** (inputs → transforms → outputs)

---

## 📁 Recommended folder layout

> 🧩 You can adopt this incrementally. Start with `datasets/` + `sources/` and grow from there.

```text
🧰 tools/
  🗂️ catalogs/
    📄 README.md            ← you are here
    📁 datasets/            ← dataset registry (raw + curated)
    📁 sources/             ← primary sources + citation metadata
    📁 layers/              ← map layer registry (styling + defaults)
    📁 sensors/             ← real-time feeds registry
    📁 models/              ← model registry (inputs/outputs/metrics)
    📁 pipelines/           ← pipeline registry (ETL + QA steps)
    📁 governance/          ← policy + ethics + access rules
    📁 reference-library/   ← library index files (optional)
```

---

## 🧾 Catalog schemas

Below are **starter templates**. Keep them boring, consistent, and easy to validate.

### 📚 Dataset entry (YAML)

```yaml
id: ks.usgs.nhd.hr.2024
title: "USGS NHD High-Resolution (Kansas subset)"
type: vector               # vector | raster | tabular | text | graph
status: raw                # raw | curated | derived | deprecated
license: "Public Domain"   # or SPDX-like short name when possible
source_id: usgs.nhd
provenance:
  acquired_at: "2026-01-13"
  transform_chain:
    - step: download
      tool: "wget"
    - step: reproject
      tool: "gdalwarp"
      params: { to_crs: "EPSG:26914" }
spatial:
  crs: "EPSG:26914"
  extent_bbox: [-102.05, 36.99, -94.59, 40.00]
temporal:
  start: null
  end: null
storage:
  canonical_path: "data/curated/hydro/nhd_hr_ks.gpkg"
  format: gpkg
quality:
  checks:
    - geometry_valid
    - schema_expected
tags: [hydrology, kansas, usgs]
notes: "Canonical hydro network layer used for routing + watershed context."
```

### 🗺️ Layer entry (YAML)

```yaml
id: layer.hydro.nhd_hr
dataset_id: ks.usgs.nhd.hr.2024
title: "Hydrography (NHD HR)"
default_visible: true
rendering:
  style: "styles/hydro/nhd_hr.json"   # Mapbox style / custom style pointer
  min_zoom: 7
  max_zoom: 18
query:
  searchable_fields: ["GNIS_NAME", "FTYPE"]
ui:
  legend_group: "Hydrology"
  inspect_panel: true
provenance:
  citation_ids: ["cite.usgs.nhd"]
```

### 🧠 Model entry (YAML)

```yaml
id: model.drought_risk.v1
title: "Drought Risk (Baseline)"
type: statistical          # statistical | ml | simulation | rules
inputs:
  - ks.noaa.precip.daily
  - ks.usda.soil_moisture
outputs:
  - ks.kfm.drought_risk_grid
metrics:
  - name: rmse
  - name: calibration_error
reproducibility:
  code_ref: "models/drought_risk/"
  seed: 1337
  environment: "conda:kfm-models"
governance:
  human_in_the_loop: true
  explanation_required: true
notes: "Designed for interpretability first; production ML can follow later."
```

### 🔧 Pipeline entry (YAML)

```yaml
id: pipe.ingest.nhd_hr
owner: "data-eng"
triggers: ["manual", "quarterly"]
steps:
  - id: fetch
    tool: "wget"
  - id: validate
    tool: "kfm-qa"
    checks: ["checksum", "schema", "geometry_valid"]
  - id: load
    tool: "ogr2ogr"
    target: "postgis"
outputs:
  - dataset_id: ks.usgs.nhd.hr.2024
    artifact: "data/curated/hydro/nhd_hr_ks.gpkg"
```

---

## 🧬 Provenance and citation rules

**Non-negotiables** (KFM design intent):
- 📎 Every catalog entry should link back to a **source** (or a chain of sources).
- 🧾 Every derived dataset should record its **transform chain** (tools + parameters).
- 🔍 UI-facing layers should expose **inspectable citations**.
- 🤖 AI features should remain **advisory + evidence-backed** (no autonomous decisions).  
  <!--  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) -->

---

## 📚 Reference library

This repo currently includes a substantial **PDF knowledge library** spanning GIS, remote sensing, modeling, stats, databases, software design, and security.

> ⚖️ Reminder: treat this library as *reference material*. Respect licenses/terms—don’t redistribute unless permitted.

### 🧠 Core project doc (start here)

- 📄 [Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation](<../../Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf>)  
  <!--  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) -->

---

### 🗺️ GIS, cartography, and spatial analysis

- 📄 [Making Maps: A Visual Guide to Map Design for GIS](<../../making-maps-a-visual-guide-to-map-design-for-gis.pdf>)
- 📄 [Python Geospatial Analysis Cookbook](<../../python-geospatial-analysis-cookbook.pdf>)
- 📄 [Mobile Mapping: Space, Cartography and the Digital](<../../Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf>)
- 📄 [Archaeological 3D GIS](<../../Archaeological 3D GIS_26_01_12_17_53_09.pdf>)  
  <!--  [oai_citation:3‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2) -->

---

### 🛰️ Remote sensing + Earth Engine

- 📄 [Cloud-Based Remote Sensing with Google Earth Engine: Fundamentals and Applications](<../../Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf>)

---

### 📊 Statistics, regression, Bayesian thinking

- 📄 [Understanding Statistics & Experimental Design](<../../Understanding Statistics & Experimental Design.pdf>)
- 📄 [Regression Analysis with Python](<../../regression-analysis-with-python.pdf>)
- 📄 [Regression Analysis using Python (slides)](<../../Regression analysis using Python - slides-linear-regression.pdf>)
- 📄 [Graphical Data Analysis with R](<../../graphical-data-analysis-with-r.pdf>)
- 📄 [Think Bayes: Bayesian Statistics in Python](<../../think-bayes-bayesian-statistics-in-python.pdf>)

---

### 🧪 Scientific modeling & simulation

- 📄 [Scientific Modeling and Simulation: A Comprehensive NASA-Grade Guide](<../../Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf>)

---

### 🧮 ML foundations + theory (math-forward)

- 📄 [Spectral Geometry of Graphs](<../../Spectral Geometry of Graphs.pdf>)
- 📄 [Generalized Topology Optimization for Structural Design](<../../Generalized Topology Optimization for Structural Design.pdf>)

---

### 🗄️ Data management, databases, performance

- 📄 [PostgreSQL Notes for Professionals](<../../PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf>)
- 📄 [Database Performance at Scale: A Practical Guide](<../../Database Performance at Scale.pdf>)  
  <!--  [oai_citation:4‡Database Performance at Scale.pdf](file-service://file-36z8qyiVJRtrSs6QG7Epen) -->
- 📄 [Scalable Data Management for Future Hardware](<../../Scalable Data Management for Future Hardware.pdf>)
- 📄 [Data Spaces](<../../Data Spaces.pdf>)

---

### 🌐 Web + UI + 3D visualization

- 📄 [Responsive Web Design with HTML5 and CSS3](<../../responsive-web-design-with-html5-and-css3.pdf>)
- 📄 [WebGL Programming Guide: Interactive 3D Graphics](<../../webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf>)

---

### 🧵 Concurrency + distributed systems

- 📄 [Concurrent, Real-Time and Distributed Programming in Java (Threads, RTSJ, RMI)](<../../concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf>)

---

### 🛡️ Security, adversarial thinking, and file formats

- 📄 [Ethical Hacking and Countermeasures: Secure Network Infrastructures](<../../ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf>)
- 📄 [Gray Hat Python: Python Programming for Hackers and Reverse Engineers (2009)](<../../Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf>)
- 📄 [Compressed Image File Formats: JPEG, PNG, GIF, XBM, BMP](<../../compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf>)

---

### ⚖️ Digital humanism, AI governance, autonomy

- 📄 [Introduction to Digital Humanism](<../../Introduction to Digital Humanism.pdf>)
- 📄 [On the Path to AI Law’s Prophecies and the Conceptual Foundations of the Machine Learning Age](<../../On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf>)
- 📄 [Principles of Biological Autonomy](<../../Principles of Biological Autonomy - book_9780262381833.pdf>)

---

## 🧱 Programming “mega-volumes” (A→X)

These are **multi-book compendium PDFs** grouped by alphabet range. They’re useful as a quick, offline “standard library” 📚 for tools, languages, and engineering practices.

- 📘 [A programming Books](<../../A programming Books.pdf>)
- 📘 [B–C programming Books](<../../B-C programming Books.pdf>)  
  _Contains (examples): Bash Notes for Professionals, Basics of Linear Algebra for ML…_  
  <!--  [oai_citation:5‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ) -->
- 📘 [D–E programming Books](<../../D-E programming Books.pdf>)  
  _Contains (example): Data Mining – Concepts and Applications…_  
  <!--  [oai_citation:6‡D-E programming Books.pdf](file-service://file-6Lmmw9aqHnfP2mo9cSrNeg) -->
- 📘 [F–H programming Books](<../../F-H programming Books.pdf>)  
  _Contains (example): Flexible Software Design…_  
  <!--  [oai_citation:7‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY) -->
- 📘 [I–L programming Books](<../../I-L programming Books.pdf>)  
  _Contains (example): Implementing Programming Languages…_  
  <!--  [oai_citation:8‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a) -->
- 📘 [M–N programming Books](<../../M-N programming Books.pdf>)  
  _Contains (example): MATLAB Notes for Professionals…_  
  <!--  [oai_citation:9‡M-N programming Books.pdf](file-service://file-EYCp5md89QY2cy5PCYS18e) -->
- 📘 [O–R programming Books](<../../O-R programming Books.pdf>)  
  _Contains (example): Objective‑C Notes for Professionals…_  
  <!--  [oai_citation:10‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M) -->
- 📘 [S–T programming Books](<../../S-T programming Books.pdf>)  
  _Contains (example): SciPy Lecture Notes…_  
  <!--  [oai_citation:11‡S-T programming Books.pdf](file-service://file-NT32tqqzGW9RvfcNZmMH1K) -->
- 📘 [U–X programming Books](<../../U-X programming Books.pdf>)  
  _Contains (example): Understanding Machine Learning (theory→algorithms)…_  
  <!--  [oai_citation:12‡U-X programming Books.pdf](file-service://file-3hYtSGHtHmb6wyTtavym6M) -->

---

## 🧠 Deep learning (note)

- 📄 [Deep Learning for Coders with fastai and PyTorch](<../../Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf>)  
  ⚠️ *This file exists in the project files but is not currently searchable via the file-browser index in this workspace.*

---

## 🧾 Full inventory (all project PDFs in this workspace)

<details>
<summary><strong>📦 Show complete library manifest (37 files)</strong></summary>

| Resource | Primary focus | Where it helps KFM |
|---|---|---|
| [A programming Books](<../../A programming Books.pdf>) | General dev references | Broad “offline toolbox” |
| [Archaeological 3D GIS](<../../Archaeological 3D GIS_26_01_12_17_53_09.pdf>) | 3D GIS practice | 3D layers, stratigraphy, volumetrics |
| [B–C programming Books](<../../B-C programming Books.pdf>) | General dev references | Bash + foundational math + more |
| [Cloud-Based Remote Sensing with Google Earth Engine](<../../Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf>) | Remote sensing | GEE pipelines, satellite-derived products |
| [D–E programming Books](<../../D-E programming Books.pdf>) | General dev references | Data mining + related references |
| [Data Spaces](<../../Data Spaces.pdf>) | Data sharing architectures | Interop, governance, cross-org exchange |
| [Database Performance at Scale](<../../Database Performance at Scale.pdf>) | DB performance | Query tuning, workload thinking |
| [Deep Learning for Coders with fastai and PyTorch](<../../Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf>) | Deep learning | ML prototyping + practical training loops |
| [F–H programming Books](<../../F-H programming Books.pdf>) | General dev references | Flexible design + engineering practice |
| [Generalized Topology Optimization for Structural Design](<../../Generalized Topology Optimization for Structural Design.pdf>) | Optimization | Optimization patterns + numerical thinking |
| [Gray Hat Python](<../../Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf>) | Security | Adversarial mindset + Python tooling |
| [I–L programming Books](<../../I-L programming Books.pdf>) | General dev references | Compilers, interpreters, language tooling |
| [Introduction to Digital Humanism](<../../Introduction to Digital Humanism.pdf>) | Ethics & society | Human-centered + accountable systems |
| [Kansas Frontier Matrix (KFM) – Technical Documentation](<../../Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf>) | KFM architecture | System vision, layers, provenance-first design |
| [M–N programming Books](<../../M-N programming Books.pdf>) | General dev references | MATLAB + applied computing notes |
| [Mobile Mapping](<../../Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf>) | Mobile cartography | Field UX + map communication |
| [O–R programming Books](<../../O-R programming Books.pdf>) | General dev references | Objective‑C + various O–R topics |
| [On the path to AI Law’s prophecies…](<../../On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf>) | AI law & concepts | Governance language + legal framing |
| [PostgreSQL Notes for Professionals](<../../PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf>) | PostgreSQL | PostGIS-friendly ops + SQL patterns |
| [Principles of Biological Autonomy](<../../Principles of Biological Autonomy - book_9780262381833.pdf>) | Systems/autonomy | Feedback loops, autonomy metaphors |
| [Regression analysis (slides)](<../../Regression analysis using Python - slides-linear-regression.pdf>) | Regression | Quick refresh / teaching aid |
| [S–T programming Books](<../../S-T programming Books.pdf>) | General dev references | SciPy notes + S–T topics |
| [Scalable Data Management for Future Hardware](<../../Scalable Data Management for Future Hardware.pdf>) | Data systems research | Next-gen infra mental models |
| [Scientific Modeling and Simulation (NASA-grade)](<../../Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf>) | Simulation | Modeling discipline + reproducibility |
| [Spectral Geometry of Graphs](<../../Spectral Geometry of Graphs.pdf>) | Graph theory | Network + spectral methods for spatial graphs |
| [U–X programming Books](<../../U-X programming Books.pdf>) | General dev references | ML theory + U–X topics |
| [Understanding Statistics & Experimental Design](<../../Understanding Statistics & Experimental Design.pdf>) | Experiment design | QA, validation, evaluation frameworks |
| [Compressed Image File Formats](<../../compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf>) | Image formats | Raster ingestion, compression tradeoffs |
| [Concurrent/Real-Time/Distributed Java](<../../concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf>) | Concurrency | Pipelines, streaming, safe parallelism |
| [Ethical Hacking and Countermeasures](<../../ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf>) | Security | Threat modeling + infra hardening |
| [Graphical Data Analysis with R](<../../graphical-data-analysis-with-r.pdf>) | EDA + plots | QA plots, anomaly checks |
| [Making Maps (GIS design)](<../../making-maps-a-visual-guide-to-map-design-for-gis.pdf>) | Cartography | Layer design + visual trust |
| [Python Geospatial Analysis Cookbook](<../../python-geospatial-analysis-cookbook.pdf>) | Geo Python | ETL, analysis recipes |
| [Regression Analysis with Python](<../../regression-analysis-with-python.pdf>) | Regression | Baseline modeling + diagnostics |
| [Responsive Web Design (HTML5/CSS3)](<../../responsive-web-design-with-html5-and-css3.pdf>) | Web UI | KFM frontend layout + components |
| [Think Bayes](<../../think-bayes-bayesian-statistics-in-python.pdf>) | Bayesian stats | Uncertainty-aware layers + inference |
| [WebGL Programming Guide](<../../webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf>) | 3D graphics | 3D GIS + interactive visualization |
</details>

---

## 🧑‍🔧 Role-based “what to read” routes

Pick a lane 🚦 and go deep.

### 🗺️ GIS / cartography lane
- Making Maps (design)  
- Python Geospatial Analysis Cookbook (implementation)  
- Mobile Mapping + Archaeological 3D GIS (UX + 3D workflows)

### 🛰️ Remote sensing lane
- Cloud-Based Remote Sensing with Google Earth Engine  
- Compressed Image Formats (raster/compression fundamentals)

### 📊 Data science lane
- Understanding Statistics & Experimental Design  
- Regression Analysis with Python + slides  
- Graphical Data Analysis with R  
- Think Bayes (uncertainty + inference)

### 🗄️ Data engineering lane
- PostgreSQL Notes + Database Performance at Scale  
- Data Spaces + Scalable Data Management for Future Hardware  
- Concurrency/Distributed Java (if you’re building streaming/real-time services)

### 🌐 Frontend + 3D visualization lane
- Responsive Web Design (HTML5/CSS3)  
- WebGL Programming Guide  
- Archaeological 3D GIS (inspiration for 3D spatial UX)

### 🛡️ Security + resilience lane
- Ethical Hacking and Countermeasures  
- Gray Hat Python  
- (Plus DB performance + concurrency for operational stability)

### ⚖️ Ethics + governance lane
- Introduction to Digital Humanism  
- On the path to AI Law’s prophecies…  
- KFM technical documentation (provenance-first + advisory AI intent)

---

## 🛠️ Contribution workflow

1. **Add / update a catalog entry** (datasets, sources, layers, models, pipelines). ✅  
2. Keep IDs stable: prefer `namespace.category.name.version` patterns.  
3. Record provenance: *tools + parameters + dates* (even if rough at first).  
4. If you add a new PDF reference, also add it to the **Reference library** section above. 📚  
5. In PRs: reviewers should be able to answer “Where did this come from?” in under 30 seconds. 🧾

---

## ✅ TODOs (suggested next files)

- [ ] `tools/catalogs/datasets/README.md` (how dataset catalogs are structured)
- [ ] `tools/catalogs/sources/README.md` (citation formats + licensing notes)
- [ ] `tools/catalogs/layers/README.md` (styling + legend conventions)
- [ ] `tools/catalogs/models/README.md` (evaluation + reproducibility rules)
- [ ] `tools/catalogs/pipelines/README.md` (pipeline registry + QA checks)
