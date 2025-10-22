---
title: "📓 Kansas Frontier Matrix — Notebooks Suite"
path: "tools/notebooks/README.md"
version: "v1.5.0"
last_updated: "2025-10-22"
review_cycle: "Quarterly / Per-Experiment"
sandbox_mode: "research / experimental"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v1.5.0/sbom.spdx.json"
manifest_ref: "releases/v1.5.0/manifest.zip"
data_contract_ref: "docs/contracts/data-contract-v3.json"
telemetry_ref: "releases/v1.5.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/focus-notebooks-v1.json"
data_products: ["data/work/", "reports/notebooks/"]
architecture_ref: "docs/architecture/repo-focus.md"
governance_ref: "docs/standards/governance.md"
doc_id: "KFM-NOTEBOOKS-RMD-v1.5.0"
maintainers: ["@kfm-data", "@kfm-research"]
approvers: ["@kfm-qa", "@kfm-architecture", "@kfm-ai", "@kfm-security"]
reviewed_by: ["@kfm-governance", "@kfm-ai", "@kfm-security"]
ci_required_checks: ["docs-validate", "nbval", "checksum-verify", "focus-telemetry", "stac-validate"]
ci_pipelines: ["nbval.yml", "docs-validate.yml", "checksum-verify.yml"]
license: "MIT"
design_stage: "Operational / Research Sandbox"
mcp_version: "MCP-DL v6.3"
alignment: ["FAIR", "CARE", "PROV-O", "STAC/DCAT-R3", "CIDOC CRM", "OWL-Time"]
status: "Platinum+ / Research Sandbox"
tags: ["research", "jupyter", "prototype", "etl", "ai", "analysis", "provenance", "focus-mode"]
---

<div align="center">

# 📓 Kansas Frontier Matrix — **Notebooks Suite**  
`tools/notebooks/`

**Exploration · Prototyping · Analysis Workbench**

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../docs/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Lab-orange)](https://jupyter.org/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Open%20Science-green)](https://www.go-fair.org/fair-principles/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

<details open>
<summary><b>📘 Table of Contents</b></summary>

- [🧭 Overview](#-overview)
- [🧬 Experiment Lifecycle](#-experiment-lifecycle)
- [🧱 Directory Structure](#-directory-structure)
- [🧩 Use Cases](#-use-cases)
- [⚙️ Environment Setup](#️-environment-setup)
- [🐳 Environment & Containerization](#-environment--containerization)
- [🧱 Data Contract & Schema Validation](#-data-contract--schema-validation)
- [🧠 Notebook Standards (MCP-DL)](#-notebook-standards-mcp-dl)
- [🧪 CI Validation & Provenance](#-ci-validation--provenance)
- [🧾 Provenance & Integrity](#-provenance--integrity)
- [🧬 Data Lineage & FAIR/CARE Declaration](#-data-lineage--faircare-declaration)
- [🌐 Interoperability & Linked Data](#-interoperability--linked-data)
- [🧠 Focus Mode Provenance Pipeline](#-focus-mode-provenance-pipeline)
- [📊 Example Snippet](#-example-snippet)
- [♿ Accessibility & Documentation](#-accessibility--documentation)
- [🔐 Security & Integrity Policy](#-security--integrity-policy)
- [🧪 Testing & Validation](#-testing--validation)
- [📈 Data Dependencies](#-data-dependencies)
- [🧩 Governance Metadata](#-governance-metadata)
- [🧮 Compliance Summary](#-compliance-summary)
- [🔗 Related Documentation](#-related-documentation)
- [🧾 Versioning & Metadata](#-versioning--metadata)
- [📜 License](#-license)
- [🧩 Version History](#-version-history)
- [🪶 Acknowledgments](#-acknowledgments)

</details>

---

## 🧭 Overview

`tools/notebooks/` is the **exploratory research lab** of the **Kansas Frontier Matrix (KFM)** — a living workspace for open, reproducible, and AI-assisted scientific inquiry.  
Each notebook is a reproducible, versioned artifact linked to the global data and provenance graph.

> *“Notebooks are experiments with memory — designed to be rerun, verified, and reused.”*

---

## 🧬 Experiment Lifecycle

```mermaid
graph LR
A[Idea / Research Question] --> B[Notebook Prototype]
B --> C[Processed Output Data]
C --> D[STAC/DCAT Metadata]
D --> E[Knowledge Graph (Neo4j)]
E --> F[AI Focus Telemetry]
F --> G[Insight Visualization / Web UI]
```

---

## 🧱 Directory Structure

```text
tools/notebooks/
├── data_exploration.ipynb
├── gis_processing.ipynb
├── stac_validation.ipynb
├── ai_entity_extraction.ipynb
├── provenance_pipeline.ipynb
├── visualization.ipynb
├── requirements.txt
└── README.md
```

---

## 🧩 Use Cases

| Notebook | Focus | Libraries |
| :--------| :------| :----------|
| **data_exploration.ipynb** | Dataset profiling & visualization | `pandas`, `matplotlib`, `seaborn` |
| **gis_processing.ipynb** | Raster/vector geoprocessing | `geopandas`, `rasterio`, `shapely` |
| **stac_validation.ipynb** | STAC/DCAT metadata generation | `pystac`, `jsonschema` |
| **ai_entity_extraction.ipynb** | NLP pipeline development | `spacy`, `transformers` |
| **provenance_pipeline.ipynb** | PROV-O graph generation | `prov`, `rdflib`, `hashlib` |
| **visualization.ipynb** | Interactive mapping prototypes | `folium`, `plotly`, `ipyleaflet` |

---

## ⚙️ Environment Setup

```bash
conda create -n kfm-notebooks python=3.11 -y
conda activate kfm-notebooks
pip install -r tools/notebooks/requirements.txt
jupyter lab
```

---

## 🐳 Environment & Containerization

```bash
docker build -f Dockerfile.notebooks -t kfm-notebooks .
docker run -p 8888:8888 -v $(pwd):/workspace kfm-notebooks
```

Provides a portable, deterministic environment containing all analysis libraries and telemetry hooks.

---

## 🧱 Data Contract & Schema Validation

| Schema | Description | Used In |
| :------| :------------| :--------|
| `stac-item.schema.json` | STAC item validation | `stac_validation.ipynb` |
| `telemetry.schema.json` | Focus telemetry logging | `provenance_pipeline.ipynb` |
| `notebook-metadata.schema.json` | YAML metadata check | all notebooks |

---

## 🧠 Notebook Standards (MCP-DL)

- Each notebook begins with a YAML metadata cell.  
- Environment & dependency hashes logged in the first code cell.  
- Output files stored in `data/work/` or `data/processed/` with sidecar checksums.  
- Provenance automatically serialized to RDF and indexed by STAC ID.

---

## 🧪 CI Validation & Provenance

| Step | Purpose | Tool |
|------|----------|------|
| Metadata Verification | Ensure YAML completeness | `nbformat`, `pyyaml` |
| Dependency Check | Verify versions match manifest | `pip check`, `conda list` |
| Reproduction Run | Execute notebooks in CI | `pytest --nbval` |
| Output Hashing | Verify artifacts | `sha256sum`, `prov` |
| Style/Lint | Maintain readability | `nbqa black`, `ruff`, `markdownlint` |

---

## 🧾 Provenance & Integrity

| Artifact | Description |
|-----------|-------------|
| **Inputs** | Source datasets & STAC metadata |
| **Outputs** | Derived files, logs, and figures |
| **Integrity** | SHA-256 & RDF provenance |
| **Traceability** | Linked to commit SHAs & dataset IDs |

---

## 🧬 Data Lineage & FAIR/CARE Declaration

All notebooks inherit FAIR+CARE governance ensuring Findability, Accessibility, Interoperability, and Reusability.  
Ethical handling of Indigenous and local knowledge adheres to CARE: Collective Benefit · Authority to Control · Responsibility · Ethics.

---

## 🌐 Interoperability & Linked Data

All notebook outputs are:
- Mapped to **CIDOC CRM / PROV-O** classes  
- Indexed under STAC/DCAT for dataset discoverability  
- Exposed via the project SPARQL endpoint (`/api/query`)

---

## 🧠 Focus Mode Provenance Pipeline

Every notebook produces a telemetry entry in `focus-telemetry.json`, linking research runs to AI Focus Mode:  
**Notebook → Summary → Provenance RDF → AI Insight → Web Visualization**

---

## 📊 Example Snippet

```python
import geopandas as gpd
import matplotlib.pyplot as plt
rivers = gpd.read_file("../../data/processed/hydrology/river_network.geojson")
ax = rivers.plot(color="#0096c7", figsize=(8, 6))
ax.set_title("Kansas River Network — Processed USGS NHD Data")
plt.tight_layout()
plt.show()
```

---

## ♿ Accessibility & Documentation

- Alt-text for all figures  
- Accessible color palettes (`cividis`, `viridis`)  
- Hierarchical markdown for screen readers  
- Figures stored under `docs/figures/`  

---

## 🔐 Security & Integrity Policy

- No writes outside repository control  
- Secrets masked in output cells  
- Random seeds fixed for reproducibility  
- CI validation for checksums & logs  

---

## 🧪 Testing & Validation

| Validation Type | Tool | Coverage | Trigger |
|------------------|------|-----------|----------|
| Notebook Execution | `pytest-nbval` | 100% success | `nbval.yml` |
| Schema Validation | `jsonschema` | 100% | `docs-validate.yml` |
| Checksum Audit | `sha256sum` | 100% | `checksum-verify.yml` |
| AI Telemetry QA | `focus-telemetry.json` | ≥95% | nightly job |

---

## 📈 Data Dependencies

| Dataset | Description | Source |
|----------|--------------|---------|
| **USGS NHD** | Hydrology network | USGS |
| **NOAA GHCN** | Historical climate | NOAA NCEI |
| **FEMA Declarations** | Disasters data | OpenFEMA |
| **Kansas GIS Archive** | Historic topographic maps | DASC / KSGeoPortal |

---

## 🧩 Governance Metadata

| Role | Responsibility | Owner | Frequency | Scope |
|------|----------------|--------|------------|-------|
| **Lead Research Architect** | Notebook reproducibility | @kfm-research | Quarterly | Research Lab |
| **Data Steward** | FAIR/DCAT compliance | @kfm-data | Bi-Monthly | Data |
| **AI Reviewer** | Focus Mode & ethics | @kfm-ai | Quarterly | AI |
| **Security Lead** | Environment integrity | @kfm-security | As Needed | Infrastructure |
| **QA Manager** | CI validation | @kfm-qa | Monthly | Validation |

---

## 🧮 Compliance Summary

| Standard | Validation Source | Status |
|-----------|------------------|---------|
| **MCP-DL v6.3** | `docs/standards/mcp-validation.yml` | ✅ |
| **FAIR+CARE** | `docs/standards/fair.md` | ✅ |
| **STAC/DCAT-R3** | `data/stac/schema/` | ✅ |
| **PROV-O / CIDOC CRM** | `ontology/` | ✅ |
| **Security Review** | `docs/standards/governance.md` | ✅ |

---

## 🔗 Related Documentation

- **Tools Overview** — `tools/README.md`  
- **AI System** — `docs/architecture/ai-system.md`  
- **Data Architecture** — `docs/architecture/data-architecture.md`  
- **Focus Mode** — `docs/features/focus-mode.md`  
- **Governance** — `