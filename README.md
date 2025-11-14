---
title: "🌾 Kansas Frontier Matrix — Open-Source Geospatial Historical Mapping Hub (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v10.3.0/sbom.spdx.json"
manifest_ref: "releases/v10.3.0/manifest.zip"
data_contract_ref: "docs/contracts/data-contract-v3.json"
telemetry_ref: "releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/system-architecture-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌾 **Kansas Frontier Matrix — Open-Source Geospatial Historical Mapping Hub**  
`README.md`

**Purpose:**  
Provide the master entry for contributors, historians, developers, and agencies working on KFM — a FAIR+CARE–certified semantic atlas integrating Kansas history, environment, culture, treaties, archives, climate, hydrology, and predictive futures.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](docs/README.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](docs/standards/faircare.md)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)]()

</div>

---

## 📘 Overview
The **Kansas Frontier Matrix (KFM)** is a geospatial knowledge platform merging the state’s historical, cultural, and environmental datasets into a unified, reproducible, ethically governed system.

Technologies:

- LangGraph 1.0 (DAG-first agent architecture)  
- Dynamic Tool Calling (governance firewall)  
- CrewAI 1.4.x MCP stack (Neo4j, STAC, GDAL, OCR, NLP)  
- STAC 1.0 + Versioning Extension  
- DCAT 3.0 dataset catalogs  
- CIDOC-CRM + GeoSPARQL + OWL-Time + PROV-O  
- FAIR+CARE + Diamond⁹ Ω / Crown∞Ω governance  

All datasets are checksummed, versioned, validated, and recorded in AI telemetry.

---

## 🎯 Mission
> “Weave Kansas’s past into a living digital landscape where memory, map, and meaning converge.”

Goals:

- Unify historical, ecological, hydrologic, archaeological, and cultural datasets  
- Empower public research, education, and tribal data sovereignty  
- Guarantee ethical governance via FAIR+CARE  
- Ensure scientific reproducibility and transparent provenance  

---

## ✨ Key Features (v10.3.x)

| Feature | Description |
|--------|-------------|
| 🧠 Agent Architecture v10.3 | LangGraph DAGs + Dynamic Tool Calling + CrewAI MCP gateway |
| 🗺️ Focus Mode v2.4 | Narrative reasoning, SHAP explainability, ethical filters |
| 🧩 Neo4j Knowledge Graph | CIDOC CRM · OWL-Time · GeoSPARQL · PROV-O |
| 🛰️ Raster + Vector Engine | GDAL MCP: slope, hillshade, warp, rasterInfo |
| 🌦️ Climate & Hydrology Pipelines | Anomalies, droughts, floods, composites |
| 🏺 Heritage Protection | H3 r7 masking + CARE cultural governance |
| 🌐 STAC/DCAT Catalogs | Version-aware, lineage-tracked metadata |
| 🧮 Reproducibility Framework | SBOM, SLSA, provenance+telemetry hashes |
| 🧭 3D + Predictive Futures | Cesium viewer (2030–2100) + paleogeography |

---

## 🏗️ System Architecture

~~~~~mermaid
flowchart TD
  A["External Data (NOAA · USGS · KHS · Tribal · Sensors)"]
  B["LangGraph ETL + AI Pipelines (OCR · NER · STAC/DCAT · QA/QC)"]
  C["Neo4j Knowledge Graph (CIDOC CRM · GeoSPARQL · OWL-Time)"]
  D["APIs (FastAPI · GraphQL · Auth/Gov)"]
  E["Frontend (React · MapLibre · Cesium · Focus Mode v2.4)"]
  F["Governance (FAIR+CARE · SBOM · SLSA · Ledger)"]

  A --> B --> C --> D --> E
  B --> F
  D --> F
~~~~~

---

## 🧱 Repository & Filesystem
A modular monorepo governing all pipelines, documentation, UI, ontology, STAC/DCAT catalogs, and governance.

---

### 📁 Directory Layout
~~~~~text
KansasFrontierMatrix/
|-- src/
|   |-- ai/
|   |-- api/
|   |-- graph/
|   |-- pipelines/
|   |-- telemetry/
|-- web/
|   |-- src/
|   |-- public/
|-- data/
|   |-- sources/
|   |-- raw/
|   |-- processed/
|   |-- stac/
|-- docs/
|   |-- architecture/
|   |-- standards/
|   |-- analyses/
|   |-- reports/
|   |-- templates/
|   |-- guides/
|-- tools/
|-- tests/
|-- .github/
|-- LICENSE
|-- CONTRIBUTING.md
|-- Makefile
~~~~~

---

## 🧱 Ontology & Metadata Standards

| Standard | Role |
|---------|------|
| STAC 1.0 + Versioning | Dataset assets, lineage, version navigation |
| DCAT 3.0 | Public metadata catalogs |
| CIDOC-CRM | Cultural + historical ontology model |
| GeoSPARQL | Spatial reasoning |
| OWL-Time | Time reasoning |
| PROV-O | Provenance graph |
| SPDX + SLSA | Supply-chain governance |

---

## 🧠 Focus Mode v2.4 — Narrative Reasoning Engine

Capabilities:

- Entity-aware narrative generation  
- Linked-data reasoning (Neo4j)  
- SHAP explainability overlays  
- Ethical/CARE filters  
- Temporal alignment (OWL-Time)  
- Visual overlays (MapLibre + Cesium)  

Telemetry includes:

- `version_locked`  
- `governance_flags`  
- `explainability_tokens`  
- `symbol_usage`

---

## ⚙️ Quickstart

~~~~~bash
git clone https://github.com/bartytime4life/Kansas-Frontier-Matrix.git
cd Kansas-Frontier-Matrix
docker compose up --build
~~~~~

Manual start:

~~~~~bash
make setup
uvicorn src.api.main:app --reload &
npm --prefix web start
~~~~~

UI: http://localhost:3000  
API: http://localhost:8000/docs  

---

## 🤝 Contributing (MCP-DL v6.3)

1. Update documentation **before coding**.  
2. Run validation:

~~~~~bash
make validate
make test
~~~~~

3. Follow MCP-DL commit conventions.  
4. Sensitive-data PRs require FAIR+CARE governance gating.

---

## ⚖️ Licensing

| Component | License |
|----------|---------|
| Code | MIT |
| Docs & Data | CC-BY 4.0 |
| Security Artifacts | SPDX |

---

## 🧮 Governance (FAIR+CARE)

| Principle | Implementation |
|----------|----------------|
| Findable | STAC/DCAT indexing & search |
| Accessible | Public APIs + documented access rules |
| Interoperable | Open ontologies + standards |
| Reusable | Lineage, hashes, DOIs |
| CARE | Consent · Authority · Responsibility · Ethics |

---

## 🕰️ Version History

| Version | Date       | Summary |
|---------|------------|---------|
| v10.3.1 | 2025-11-13 | Complete MCP-aligned rewrite · Directory Layout added · Badge order fixed · Mermaid corrected · Full compliance with Markdown Output Protocol. |
| v10.2.2 | 2025-11-12 | Expanded telemetry; Focus Mode v2.1; enhanced governance. |
| v10.0.0 | 2025-11-09 | Initial unified v10 architecture + FAIR+CARE alignment. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
Validated under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Documentation Index](docs/README.md) · [Root Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
```
