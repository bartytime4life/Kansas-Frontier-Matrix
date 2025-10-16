<div align="center">

# 📓 Kansas Frontier Matrix — **Notebooks**  
`tools/notebooks/`

**Exploration · Prototyping · Analysis Workbench**

[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../docs/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Lab-orange)](https://jupyter.org/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Notebooks (tools/notebooks/)"
version: "v1.0.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-research"]
tags: ["notebooks","jupyter","exploration","prototyping","analysis","mcp"]
license: "MIT"
semantic_alignment:
  - FAIR Principles (Findable, Accessible, Interoperable, Reusable)
  - PROV-O (Provenance Tracking)
  - MCP-DL v6.2 Reproducible Experimentation
---
```

---

## 🧭 Overview

The `tools/notebooks/` directory provides a **sandbox environment** for data scientists, historians, and engineers
working on the **Kansas Frontier Matrix (KFM)** project to explore, analyze, and prototype workflows.

Each notebook serves as a **documented experiment** — following the **Master Coder Protocol (MCP-DL v6.2)** principles
of transparency, provenance, and reproducibility.

> Every notebook is a bridge between data and discovery — an executable document that explains not just *what* was done, but *why*.

---

## 🧱 Directory Structure

```text
tools/notebooks/
├── data_exploration.ipynb     # Basic dataset inspection and summary statistics
├── gis_processing.ipynb       # Geospatial transformation examples (GeoPandas, rasterio)
├── stac_validation.ipynb      # STAC item creation and schema validation
├── ai_entity_extraction.ipynb # NLP-based entity extraction from documents
├── provenance_pipeline.ipynb  # Provenance capture and checksum verification
├── visualization.ipynb        # Interactive map and timeline prototyping
├── requirements.txt           # Notebook-specific dependencies
└── README.md                  # This documentation file
```

---

## 🧩 Purpose & Use Cases

| Notebook                       | Focus                                                       | Tools / Libraries                  |
| :----------------------------- | :---------------------------------------------------------- | :--------------------------------- |
| **data_exploration.ipynb**     | Explore raw and processed datasets (CSV, GeoJSON, TIFF)     | `pandas`, `matplotlib`, `seaborn`  |
| **gis_processing.ipynb**       | Coordinate reprojection, clipping, and conversion workflows | `geopandas`, `rasterio`, `shapely` |
| **stac_validation.ipynb**      | Build and validate STAC Collections & Items                 | `pystac`, `jsonschema`             |
| **ai_entity_extraction.ipynb** | Prototype entity extraction from text archives              | `spacy`, `transformers`, `openai`  |
| **provenance_pipeline.ipynb**  | Demonstrate hash generation and provenance linking          | `hashlib`, `prov`, `json`          |
| **visualization.ipynb**        | Map & timeline visualization experiments                    | `folium`, `plotly`, `ipyleaflet`   |

Each notebook documents **objectives**, **methods**, **data sources**, **results**, and **next steps**, serving as both
a research artifact and an onboarding guide for future collaborators.

---

## ⚙️ Environment Setup

KFM uses **JupyterLab** and **Conda** to manage reproducible notebook environments.

### 🧩 Installation

```bash
# Create environment
conda create -n kfm-notebooks python=3.11 -y
conda activate kfm-notebooks

# Install dependencies
pip install -r tools/notebooks/requirements.txt

# Launch Jupyter
jupyter lab
```

**Example requirements.txt:**

```txt
jupyterlab
pandas
geopandas
matplotlib
rasterio
folium
pystac
spacy
transformers
prov
```

---

## 🧠 Notebook Standards

To ensure reproducibility and MCP compliance, every notebook must:

1. Start with a **YAML front matter** block (`---`) describing purpose, inputs, and outputs.
2. Contain **metadata cells** (author, date, dataset references, environment hash).
3. Use **relative file paths** (e.g., `../../data/raw/filename.csv`) for portability.
4. End with a **Summary / Conclusions** section describing insights and next steps.
5. Export results (plots, tables, JSON, logs) to `/data/work/` or `/data/processed/`.
6. Include a reproducibility badge or checksum (optional cell with `!sha256sum`).

Example YAML cell:

```yaml
---
title: "Kansas Floodplain Analysis"
author: "A. Barta"
date: "2025-10-16"
inputs: ["data/processed/hydrology/floodplains.geojson"]
outputs: ["data/work/floodplain_summary.csv"]
description: "Analyzes historical floodplain expansion in Kansas River Basin."
---
```

---

## 🧪 Validation & Provenance

Each notebook is validated for **reproducibility** and **metadata completeness** using CI workflows:

| Validation Step     | Description                                       | Tool                       |
| :------------------ | :------------------------------------------------ | :------------------------- |
| Metadata Extraction | Ensures all notebooks include front matter        | Python `nbformat` parser   |
| Dependency Check    | Validates required libraries exist in environment | `pip check`, `conda list`  |
| Output Tracking     | Confirms reproducible outputs (hash consistency)  | `sha256sum`, `prov`        |
| Execution Test      | Executes notebook to verify clean runs            | `pytest --nbval`           |
| Lint & Style        | Validates PEP8 + markdown cell formatting         | `black-nb`, `ruff`, `nbqa` |

CI reports include execution logs, runtime duration, and hash comparison results.

---

## 📊 Example Notebook Snippet

```python
import geopandas as gpd
from matplotlib import pyplot as plt

# Load and preview Kansas hydrology data
rivers = gpd.read_file("../../data/processed/hydrology/river_network.geojson")
rivers.plot(color="#00b3b3", figsize=(8, 6))
plt.title("Kansas River Network — Processed from USGS NHD")
plt.show()
```

> Every visualization or result cell must cite its data source in an adjacent markdown cell.

---

## ♿ Accessibility & Documentation

* All visual outputs include **alt-text descriptions** for screenshots or figures.
* Notebooks include headings and logical structure for **screen reader navigation**.
* Color palettes conform to **WCAG 2.1 AA** contrast guidelines.
* Plots must use **colorblind-safe palettes** (e.g., `colorcet`, `cividis`).
* All generated figures are saved in `/docs/figures/` with contextual captions.

---

## 🧾 Provenance & Integrity

| Artifact         | Description                                                        |
| :--------------- | :----------------------------------------------------------------- |
| **Inputs**       | Datasets, configuration files, environment manifests               |
| **Outputs**      | Derived data, charts, tables, provenance metadata                  |
| **Dependencies** | JupyterLab, Python 3.11+, GeoPandas, PySTAC                        |
| **Integrity**    | CI reproduces notebooks and validates SHA256 checksums for outputs |
| **Traceability** | Each notebook linked to dataset STAC IDs and commit SHA            |

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                        |
| :------------------ | :---------------------------------------------------- |
| Documentation-first | YAML metadata and in-notebook docstrings              |
| Reproducibility     | Conda environment, deterministic results              |
| Provenance          | Data lineage recorded in metadata and STAC references |
| Accessibility       | WCAG 2.1 AA visual and structural compliance          |
| Open Standards      | STAC, GeoJSON, FAIR-aligned metadata                  |
| Auditability        | Notebooks validated via CI execution pipeline         |

---

## 🔗 Related Documentation

* **Tools Overview** — `tools/README.md`
* **Data Exploration Notebooks** — `docs/notebooks/overview.md`
* **STAC Catalog Reference** — `data/stac/README.md`
* **Design Mockups** — `docs/design/mockups/`

---

## 📜 License

All notebooks and associated scripts are distributed under the **MIT License**.  
© 2025 Kansas Frontier Matrix — developed under **MCP-DL v6.2** for open, traceable, and reproducible research.

> *“Every notebook is a lab in the frontier — where data becomes discovery, and discovery becomes documentation.”*