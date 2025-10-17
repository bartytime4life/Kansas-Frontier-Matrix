<div align="center">

# 📓 Kansas Frontier Matrix — **Notebooks**  
`tools/notebooks/`

**Exploration · Prototyping · Analysis Workbench**

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../docs/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Lab-orange)](https://jupyter.org/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

## 🧭 Overview

`tools/notebooks/` is the **sandbox lab** for KFM data scientists, historians, and engineers to **explore, prototype, and analyze** workflows.  
Every notebook is an **executable experiment** that follows **MCP-DL v6.3**: documented intent, reproducible environment, and verifiable provenance.

> *A notebook should explain not just **what** was done, but **why**—with enough detail to do it again.*

---

## 🧱 Directory Structure

```text
tools/notebooks/
├── data_exploration.ipynb     # Dataset inspection & summary statistics
├── gis_processing.ipynb       # Geo transforms (GeoPandas, rasterio)
├── stac_validation.ipynb      # STAC build & schema validation
├── ai_entity_extraction.ipynb # NLP entity extraction prototypes
├── provenance_pipeline.ipynb  # Hashing & provenance capture demo
├── visualization.ipynb        # Map & timeline prototyping
├── requirements.txt           # Notebook-specific deps
└── README.md
```

---

## 🧩 Use Cases

| Notebook                       | Focus                                                     | Libraries                      |
| :----------------------------- | :-------------------------------------------------------- | :----------------------------- |
| **data_exploration.ipynb**     | Explore CSV/GeoJSON/TIFF; profiling & EDA                 | `pandas`, `seaborn`, `matplotlib` |
| **gis_processing.ipynb**       | Reprojection, clipping, raster/vec conversions            | `geopandas`, `rasterio`, `shapely` |
| **stac_validation.ipynb**      | Create/validate STAC Collections/Items                    | `pystac`, `jsonschema`         |
| **ai_entity_extraction.ipynb** | Text OCR→NER→linking experiments                          | `spacy`, `transformers`        |
| **provenance_pipeline.ipynb**  | SHA256 + PROV-O linking for artifacts                     | `hashlib`, `prov`              |
| **visualization.ipynb**        | Maps/timelines, interactive exploration                   | `folium`, `plotly`, `ipyleaflet` |

Each notebook must capture **objectives → method → results → next steps**.

---

## ⚙️ Environment Setup

```bash
conda create -n kfm-notebooks python=3.11 -y
conda activate kfm-notebooks
pip install -r tools/notebooks/requirements.txt
jupyter lab
```

**Example `requirements.txt`:**
```txt
jupyterlab
pandas
geopandas
matplotlib
seaborn
rasterio
folium
pystac
jsonschema
spacy
transformers
prov
```

---

## 🧠 Notebook Standards (MCP-DL)

1. **YAML front matter** in the first cell with title, author, date, inputs, outputs.  
2. **Metadata cell**: environment hash (e.g., `pip freeze | sha256sum`), commit SHA.  
3. **Relative paths** only (e.g., `../../data/raw/...`).  
4. **Summary section** at the end with findings & uncertainties.  
5. **Outputs** saved to `data/work/` or `data/processed/` with checksums.  
6. **Citations**: reference STAC IDs and sources in adjacent markdown.  

Example YAML cell:

```yaml
---
title: "Kansas Floodplain Analysis"
author: "A. Barta"
date: "2025-10-16"
inputs: ["data/processed/hydrology/floodplains.geojson"]
outputs: ["data/work/floodplain_summary.csv"]
description: "Analyzes historical floodplain expansion in the Kansas River Basin."
---
```

---

## 🧪 CI Validation & Provenance

| Step                | Purpose                                      | Tooling                 |
| :------------------ | :------------------------------------------- | :---------------------- |
| Metadata check      | Ensure front matter & required fields exist  | `nbformat` parser       |
| Dependency check    | Verify env meets `requirements.txt`          | `pip check`, `conda list` |
| Repro run           | Execute notebooks for clean runs             | `pytest --nbval`        |
| Output hashing      | Verify artifact hashes match expectations    | `sha256sum`             |
| Style/lint          | Code/markdown quality gates                  | `nbqa black`, `ruff`, `markdownlint` |

CI publishes execution logs, runtime stats, and checksum manifests.

---

## 📊 Example Snippet

```python
import geopandas as gpd
import matplotlib.pyplot as plt

rivers = gpd.read_file("../../data/processed/hydrology/river_network.geojson")
ax = rivers.plot(color="#00b3b3", figsize=(8, 6))
ax.set_title("Kansas River Network — USGS NHD (processed)")
plt.tight_layout()
plt.show()
```

> Always cite data sources (STAC ID/URL) in a markdown cell next to plots.

---

## ♿ Accessibility & Documentation

- Provide **alt-text** for saved figures and screenshots.  
- Use **colorblind-safe** palettes (e.g., `cividis`, `ColorBrewer`).  
- Structure headings for screen-reader navigation.  
- Save figures to `docs/figures/` with captions & context.

---

## 🧾 Provenance & Integrity

| Artifact      | Description                                         |
| :------------ | :-------------------------------------------------- |
| **Inputs**    | Datasets, manifests, STAC references                |
| **Outputs**   | Derived CSV/GeoJSON, figures, logs, metadata        |
| **Integrity** | SHA-256 sidecars; PROV-O relations per notebook     |
| **Traceability** | Link outputs to STAC IDs and commit SHAs        |

---

## 🔗 Related Documentation

- **Tools Overview** — `tools/README.md`  
- **STAC Catalog** — `data/stac/README.md`  
- **Architecture** — `docs/architecture/system-architecture-overview.md`  
- **Design Mockups** — `docs/design/mockups/`

---

## 🧾 Versioning & Metadata

| Field | Value |
| :---- | :---- |
| **Version** | `v1.1.0` |
| **Codename** | *Executable Research Upgrade* |
| **Last Updated** | 2025-10-17 |
| **Maintainers** | @kfm-data · @kfm-research |
| **License** | MIT |
| **Alignment** | FAIR · PROV-O · MCP-DL v6.3 |
| **Maturity** | Stable / Active Lab |

---

## 📜 License

All notebooks are distributed under the **MIT License**.  
© 2025 Kansas Frontier Matrix — *open, traceable, reproducible* research.

> *“Every notebook is a lab on the frontier—where data becomes discovery.”*
