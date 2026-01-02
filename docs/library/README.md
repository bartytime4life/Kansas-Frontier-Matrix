# 📚 KFM Library

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-2ea44f) ![Docs](https://img.shields.io/badge/docs-library-blue) ![Focus](https://img.shields.io/badge/focus-GIS%20%7C%20ML%20%7C%20Simulation-orange) ![Status](https://img.shields.io/badge/status-active-success) ![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)

A curated “bookshelf” 📖 for the **Kansas Frontier Matrix (KFM)** / **Kansas-Matrix-System** project.  
This folder exists to keep the team aligned on **shared vocabulary**, **best practices**, and **deep reference material** across architecture, data science, GIS, remote sensing, web mapping, and ethics.

> ⚠️ **License + usage note:** Some PDFs in this library are open access, others are copyrighted or have special restrictions. Treat this README as the **index** 🧭, and store/ship PDFs according to their license terms.

---

## 🎯 What this library is for

- **Onboarding** new contributors fast (what to read, in what order)
- **Implementation guidance** (patterns + pitfalls across KFM subsystems)
- **Decision support** (“why did we build it this way?”)
- **Quality gates** (stats/ML evaluation, experiment design, reproducibility)
- **Human-centered guardrails** (digital humanism + autonomy)

---

## 🗂️ Recommended folder layout

> This repo can be configured either with PDFs committed via Git LFS, or with PDFs kept in private artifact storage and only referenced here.

```text
docs/
  library/
    README.md                  👈 you are here
    pdfs/                      📦 (optional) large PDFs (Git LFS recommended)
      ... .pdf
    notes/                     📝 summaries + highlights per resource
      _template.md
      ...
    bib/                       🧾 citations (BibTeX/CSL)
      library.bib
```

---

## 🚀 How to use this library (the “notes-first” workflow)

1) **Start here** → pick a track 🧭  
2) **Skim purposefully** → extract key patterns into `docs/library/notes/` 📝  
3) **Apply immediately** → link notes into feature docs, PRs, and ADRs ✅

Helpful CLI snippet (optional) 🔧:
```bash
# Convert a PDF to text for local searching (macOS/Linux)
pdftotext "docs/library/pdfs/Some Book.pdf" /tmp/book.txt
rg -n "keyword" /tmp/book.txt
```

---

## 🧭 Choose your path (fast)

### If you’re building…
- 🧱 **Architecture / backend services** → start with *KFM Technical Documentation* + *Clean Architectures in Python*
- 🛰️ **GIS / remote sensing workflows** → start with *GIS Basics* + *Geoprocessing with Python* + *Earth Engine*
- 🤖 **ML / modeling** → start with *Data Science & ML Methods* + *Regression Analysis* + *Stats Done Wrong*
- 🎨 **Web UI + maps + 3D** → start with *Responsive Web Design* + *Google Maps JS API* + *WebGL*
- 🧪 **Simulation / optimization** → start with *Scientific Modeling & Simulation* + *MATLAB* + *Topology Optimization*
- 🧭 **Ethics / governance** → start with *Digital Humanism* + *Principles of Biological Autonomy*

---

## 📚 Catalog (all library PDFs)

> PDFs are expected at: `docs/library/pdfs/`  
> If your project stores them elsewhere, keep the filenames the same and update the paths in this README.

---

<details>
<summary><strong>🧩 Core Project Reference</strong> (start here)</summary>

- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** 🧠  
  Canonical end-to-end reference for KFM architecture, workflows, and principles.  
  File: [Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](<./pdfs/Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf>)

</details>

---

<details>
<summary><strong>🏗️ Architecture, DevOps, Backend, Systems</strong></summary>

- **Clean Architectures in Python** 🧱  
  Clean architecture patterns for modular, testable, maintainable systems.  
  File: [clean-architectures-in-python.pdf](<./pdfs/clean-architectures-in-python.pdf>)

- **Introduction to Docker** 🐳  
  Containers, images, Dockerfiles, Compose, production concerns.  
  File: [Introduction-to-Docker.pdf](<./pdfs/Introduction-to-Docker.pdf>)

- **Command Line Kung Fu** 🥷  
  Bash one-liners + shell scripting tricks for automation and ops.  
  File: [Command Line Kung Fu_ Bash Scripting Tricks, Linux Shell Programming Tips, and Bash One-liners - Command_Line_Kung_Fu_Bash_Scripting_Tricks,_Linux_Shell_Program.pdf](<./pdfs/Command Line Kung Fu_ Bash Scripting Tricks, Linux Shell Programming Tips, and Bash One-liners - Command_Line_Kung_Fu_Bash_Scripting_Tricks,_Linux_Shell_Program.pdf>)

- **Scalable Data Management for Future Hardware** 🗄️  
  Systems thinking for scalable data pipelines and compute/storage patterns.  
  File: [Scalable Data Management for Future Hardware.pdf](<./pdfs/Scalable Data Management for Future Hardware.pdf>)

- **Implementing Programming Languages: An Introduction to Compilers and Interpreters** 🧠  
  Useful for DSLs, parsers, and language tooling (even lightweight).  
  File: [implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf](<./pdfs/implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf>)

- **Node.js Notes for Professionals** 🌐  
  Fast reference for Node runtime, npm, HTTP, Express patterns.  
  File: [Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf](<./pdfs/Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf>)

- **PostgreSQL Notes for Professionals** 🐘  
  Practical SQL reference + patterns; pairs well with PostGIS in KFM.  
  File: [PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf](<./pdfs/PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf>)

- **MySQL Notes for Professionals** 🐬  
  Practical SQL reference (useful for interoperability / migrations).  
  File: [MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf](<./pdfs/MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf>)

</details>

---

<details>
<summary><strong>📊 Statistics, Experiment Design, Bayesian, EDA</strong></summary>

- **Understanding Statistics & Experimental Design** 🧪  
  Grounding for experiments, metrics, and evaluation workflows.  
  File: [Understanding Statistics & Experimental Design.pdf](<./pdfs/Understanding Statistics & Experimental Design.pdf>)

- **Statistics Done Wrong** 🚫📈  
  A “pitfall radar” for common statistical mistakes in real projects.  
  File: [Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf](<./pdfs/Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf>)

- **Regression Analysis with Python** 📉🐍  
  Regression workflows, diagnostics, interpretation, and practice patterns.  
  File: [regression-analysis-with-python.pdf](<./pdfs/regression-analysis-with-python.pdf>)

- **Bayesian Computational Methods** 🎲  
  Bayesian inference tools and computational approaches.  
  File: [Bayesian computational methods.pdf](<./pdfs/Bayesian computational methods.pdf>)

- **Graphical Data Analysis with R** 📊🧰  
  Exploratory plotting patterns and statistical visualization thinking.  
  File: [graphical-data-analysis-with-r.pdf](<./pdfs/graphical-data-analysis-with-r.pdf>)

- **Data Science & Machine Learning (Mathematical & Statistical Methods)** 🧮  
  Math/stats backbone for ML, evaluation, and assumptions.  
  File: [Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf](<./pdfs/Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf>)

- **Applied Data Science with Python and Jupyter** 🧑‍🔬📓  
  Hands-on analysis workflow with notebooks + practical ML.  
  File: [applied-data-science-with-python-and-jupyter.pdf](<./pdfs/applied-data-science-with-python-and-jupyter.pdf>)

</details>

---

<details>
<summary><strong>🤖 AI, ML, Data Mining Foundations</strong></summary>

- **AI Foundations of Computational Agents (3rd Ed.)** 🤖  
  Core AI concepts: agents, planning, reasoning, constraints.  
  File: [AI Foundations of Computational Agents 3rd Ed.pdf](<./pdfs/AI Foundations of Computational Agents 3rd Ed.pdf>)

- **Artificial Neural Networks: An Introduction** 🧠  
  Neural network concepts and core intuition.  
  File: [Artificial-neural-networks-an-introduction.pdf](<./pdfs/Artificial-neural-networks-an-introduction.pdf>)

- **Deep Learning in Python (Prerequisites)** 🐍🧠  
  Python + math prerequisites for DL workflows.  
  File: [deep-learning-in-python-prerequisites.pdf](<./pdfs/deep-learning-in-python-prerequisites.pdf>)

- **Data Mining: Concepts & Applications** ⛏️  
  Classic data mining workflows: features, clustering, classification, evaluation.  
  File: [Data Mining Concepts & applictions.pdf](<./pdfs/Data Mining Concepts & applictions.pdf>)

</details>

---

<details>
<summary><strong>🗺️ GIS, Remote Sensing, Earth Engine, Web Mapping</strong></summary>

- **Geographic Information System Basics** 🧭  
  GIS fundamentals: raster/vector, projections, geodata management, cartography.  
  File: [Geographic Information System Basics - geographic-information-system-basics.pdf](<./pdfs/Geographic Information System Basics - geographic-information-system-basics.pdf>)

- **Making Maps: A Visual Guide to Map Design for GIS** 🗺️🎨  
  Cartographic design and map communication (critical for user trust).  
  File: [making-maps-a-visual-guide-to-map-design-for-gis.pdf](<./pdfs/making-maps-a-visual-guide-to-map-design-for-gis.pdf>)

- **Geoprocessing with Python** 🐍🛰️  
  Python-first geoprocessing workflows (automation + repeatability).  
  File: [geoprocessing-with-python.pdf](<./pdfs/geoprocessing-with-python.pdf>)

- **Python Geospatial Analysis Cookbook** 🧑‍🍳🌍  
  Recipes for projections, overlays, PostGIS, routing, and visualization.  
  File: [python-geospatial-analysis-cookbook.pdf](<./pdfs/python-geospatial-analysis-cookbook.pdf>)

- **Cloud-Based Remote Sensing with Google Earth Engine (Fundamentals and Applications)** ☁️🛰️  
  Earth Engine fundamentals + applied labs for planetary-scale analysis.  
  File: [Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](<./pdfs/Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf>)

- **Google Earth Engine Applications** 🌎⚙️  
  Application examples across land cover, vegetation, floods, drought, etc.  
  File: [Google Earth Engine Applications.pdf](<./pdfs/Google Earth Engine Applications.pdf>)

- **Google Maps API Succinctly** 🧭📍  
  Quick-start mental model for Maps API usage.  
  File: [Google Maps API Succinctly - google_maps_api_succinctly.pdf](<./pdfs/Google Maps API Succinctly - google_maps_api_succinctly.pdf>)

- **Google Maps JavaScript API Cookbook** 🥘🗺️  
  Practical recipes for building map UI + layers + interactions.  
  File: [google-maps-javascript-api-cookbook.pdf](<./pdfs/google-maps-javascript-api-cookbook.pdf>)

</details>

---

<details>
<summary><strong>🎨 Frontend, UI, Visualization, Graphics</strong></summary>

- **Responsive Web Design with HTML5 and CSS3** 📱💻  
  Responsive layouts and modern frontend fundamentals.  
  File: [responsive-web-design-with-html5-and-css3.pdf](<./pdfs/responsive-web-design-with-html5-and-css3.pdf>)

- **WebGL Programming Guide: Interactive 3D Graphics Programming with WebGL** 🧊  
  Low-level WebGL + shaders + 3D math foundations.  
  File: [webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](<./pdfs/webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf>)

- **Computer Graphics using JAVA 2D & 3D** 🎮☕  
  Graphics fundamentals and rendering concepts (portable intuition).  
  File: [Computer Graphics using JAVA 2D & 3D.pdf](<./pdfs/Computer Graphics using JAVA 2D & 3D.pdf>)

</details>

---

<details>
<summary><strong>🧮 Modeling, Simulation, Optimization, Math</strong></summary>

- **Scientific Modeling and Simulation (NASA-grade guide)** 🧪🚀  
  Modeling foundations: verification, validation, uncertainty, modeling lifecycle.  
  File: [Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](<./pdfs/Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf>)

- **MATLAB Programming for Engineers** 🧰  
  MATLAB workflow for numerical computing, prototyping, and engineering scripts.  
  File: [MATLAB Programming for Engineers Stephen J. Chapman.pdf](<./pdfs/MATLAB Programming for Engineers Stephen J. Chapman.pdf>)

- **Generalized Topology Optimization for Structural Design** 🏗️🧠  
  Optimization thinking useful for design under constraints (also transferable to ML).  
  File: [Generalized Topology Optimization for Structural Design.pdf](<./pdfs/Generalized Topology Optimization for Structural Design.pdf>)

- **Spectral Geometry of Graphs** 🧊📈  
  Graph theory + spectral methods (useful for network analysis + embeddings intuition).  
  File: [Spectral Geometry of Graphs.pdf](<./pdfs/Spectral Geometry of Graphs.pdf>)

</details>

---

<details>
<summary><strong>🧭 Ethics, Autonomy, Digital Humanism</strong></summary>

- **Introduction to Digital Humanism** 🧭  
  Sociotechnical grounding for building human-centered digital systems.  
  File: [Introduction to Digital Humanism.pdf](<./pdfs/Introduction to Digital Humanism.pdf>)

- **Principles of Biological Autonomy (New annotated edition)** 🧬  
  Deep foundations on autonomy, systems, and circular causality (conceptual compass).  
  File: [Principles of Biological Autonomy - book_9780262381833.pdf](<./pdfs/Principles of Biological Autonomy - book_9780262381833.pdf>)

</details>

---

## 🧩 Crosswalk: KFM workstreams → go-to references

### 🛰️ Remote sensing ingestion & analysis
- *Cloud-Based Remote Sensing with Google Earth Engine…*
- *Google Earth Engine Applications*
- *Geoprocessing with Python*
- *Python Geospatial Analysis Cookbook*
- *GIS Basics* + *Making Maps*

### 🗄️ Data modeling, storage, and pipelines
- *Scalable Data Management for Future Hardware*
- *PostgreSQL Notes for Professionals* (plus PostGIS knowledge)
- *Docker* + *Command Line Kung Fu*
- *Clean Architectures in Python*

### 🤖 Model training, evaluation, and deployment
- *Data Science & ML (Math & Stats Methods)*
- *Regression Analysis with Python*
- *Statistics Done Wrong*
- *Bayesian Computational Methods*
- *Deep Learning in Python (Prerequisites)*
- *Artificial Neural Networks: An Introduction*
- *Applied Data Science with Python & Jupyter*

### 🌐 Web mapping UI + visualization
- *Google Maps JavaScript API Cookbook*
- *Google Maps API Succinctly*
- *Responsive Web Design with HTML5 and CSS3*
- *WebGL Programming Guide* (for 3D overlays / advanced viz)

### 🧪 Simulation, verification, and optimization
- *Scientific Modeling and Simulation (NASA-grade guide)*
- *MATLAB Programming for Engineers*
- *Generalized Topology Optimization…*
- *Spectral Geometry of Graphs*

### 🧭 Human-centered governance & ethics
- *Introduction to Digital Humanism*
- *Principles of Biological Autonomy*

---

## ✅ Contributing to the library (team workflow)

When adding a new resource 📦:
1. Put the PDF in `docs/library/pdfs/` **or** store it in approved artifact storage and link it here.
2. Add a short note file in `docs/library/notes/<slug>.md` 📝:
   - What it’s for (KFM touchpoints)
   - Key takeaways (3–7 bullets)
   - “Use it when…” triggers
3. Update this README catalog entry ✅
4. Confirm license constraints (open vs restricted) 🔒

---

## 🔒 License & responsible use

- Always check the first pages of each PDF for its specific license/terms.
- Prefer **open access** where possible for anything we want broadly shareable.
- If a resource is **copyrighted or restricted**, do **not** redistribute it publicly.
- If a resource contains restrictions related to AI training or redistribution, follow them exactly.

---

## 🧾 Suggested citation format (optional)

If you’re writing internal docs/ADRs and want a quick citation style, use:
- **Title**, author(s), year, and file reference under `docs/library/pdfs/`.

(If we standardize later, add BibTeX entries to `docs/library/bib/library.bib`.)

---

## 🙌 Maintenance

If something is missing, outdated, or duplicated:
- Update the catalog entry ✍️
- Add/refresh notes 📝
- Prefer “one source of truth” and cross-link instead of duplicating content 🔁