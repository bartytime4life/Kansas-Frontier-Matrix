---
title: "🌌 Kansas Frontier Matrix — v11 System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "README.md"
version: "v11.2.2"
last_updated: "2025-11-27"
review_cycle: "Annual · FAIR+CARE Council & Architecture Board"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:readme:root:v11.2.2"
semantic_document_id: "kfm-doc-root-overview"
event_source_id: "ledger:README.md"
immutability_status: "version-pinned"

sbom_ref: "releases/v11.2.2/sbom.spdx.json"
manifest_ref: "releases/v11.2.2/manifest.zip"
telemetry_ref: "releases/v11.2.2/system-telemetry.json"
telemetry_schema: "schemas/telemetry/system-v11.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "kfm-root-overview"
lifecycle_stage: "stable"

fair_category: "F1-A1-I2-R3"
care_label: "Mixed / Multi-Domain"
classification: "Public"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded by KFM v12 Root Overview"
---

<div align="center">

# 🌌 **Kansas Frontier Matrix (KFM v11)**  
### **Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
### *A State-Scale Knowledge System for Kansas — Environment, History, Culture, AI, and Time*  

`README.md`

**Purpose**  
Provide the **canonical, high-level overview** of the Kansas Frontier Matrix v11 — a fully-governed, reproducible, state-scale knowledge system unifying environment, history, culture, and AI into one coherent, semantic geospatial platform.

</div>

---

## 📘 1. What the System Is

The **Kansas Frontier Matrix (KFM)** is a unified, multi-layer, multi-epoch knowledge system integrating:

- **Geospatial data** (2D/3D)  
- **AI pipelines** and autonomous ETL  
- **Historical archives** and newspapers  
- **Environmental and hydrological models**  
- **Archaeology & cultural landscapes**  
- **Hazards and infrastructure**  
- **Narrative layers (Story Nodes & Focus Mode)**  

All under a coherent **Neo4j knowledge graph**, fully versioned, fully governed, and aligned with:

- CIDOC-CRM · GeoSPARQL · OWL-Time  
- STAC 1.x · DCAT 3.0 · PROV-O · ISO 19115  
- FAIR+CARE · MCP-DL v6.3 · KFM-MDP v11.2.2  

KFM v11 merges:

- 🛰️ **Remote sensing** (satellite, aerial, radar, lidar)  
- 💧 **Hydrology & climate chronologies** (rivers, reservoirs, droughts, storms)  
- 🗺️ **GIS + MapLibre + Cesium 3D**  
- 🧬 **AI-assisted ETL & autonomous refresh pipelines**  
- 🏺 **Archaeology & cultural landscapes** (Protohistoric Wichita, trails, forts, sites)  
- 📚 **Archives, documents, newspapers, photos**  
- 🔥 **Hazards, energy, wildfire, drought, flood, severe weather**  
- 🌿 **Ecology & landcover (past → present)**  
- 📦 **STAC / DCAT / PROV-O provenance across data products**  
- 📖 **Story Nodes & Focus Mode v3**  
- 🏛️ **FAIR+CARE governance & Indigenous data sovereignty**  

The result is a **state-scale digital twin** of Kansas across time: physical, cultural, environmental, and narrative.

---

## 🌍 2. State-Scale Environmental Knowledge Engine

KFM unifies major **environmental and geophysical domains** for Kansas:

- 🌧️ **Climate**  
  - PRISM, NOAA, ERA5, NCEI, Mesonet, drought indices, anomaly fields.  

- 💧 **Hydrology**  
  - Rivers, lakes, USGS gauges, reservoir inflow/outflow, groundwater, WID & sedimentation.  

- 🌱 **Ecology & Land Systems**  
  - Landcover, NDVI, biome maps, GAP species ranges, wetlands, fire regimes.  

- 🏞️ **Terrain & Subsurface**  
  - DEMs (1 m → coarse), bathymetry, lidar, geomorphology, geologic units.  

- 🌪️ **Hazards & Energy**  
  - Wildfire risk, severe storms, tornado tracks, floodplains, drought, grid/pipeline overlays.  

Each dataset is:

- Reprojected via standardized CRS pipelines (EPSG:4326 ↔ 3857 ↔ native CRS).  
- Harmonized with **CF conventions** (vertical datums, units, axis naming).  
- Registered as **STAC Collections & Items** in `data/stac/`.  
- Linked to **DCAT Datasets** and **PROV-O** activity chains.  
- Integrated into the **KFM Neo4j graph** as entities, events, and observations.  

This allows **queries, overlays, and model runs** across climate, hydrology, ecology, and hazards in a single, consistent environment.

---

## 🧠 3. Multi-Layer AI & Autonomous Pipelines

KFM v11 uses a layered AI/ETL architecture that is **deterministic, logged, and governed**.

### 🔷 3.1 LangGraph v11 Deterministic DAG ETL

- Directed acyclic graphs (DAGs) for all ETL flows (batch + streaming).  
- Write-ahead logs (WAL) for reproducibility and replay.  
- Automatic retry / rollback with lineage tracking.  
- Schema validation against **Data Contracts v3**.  
- FAIR+CARE screening at every boundary (raw → work → processed → releases).  
- Time-indexed tasks (e.g., “rebuild climate anomalies 1900–2025”) with versioned outputs.  

### 🔶 3.2 CrewAI Cooperative Workers (v2.5 → v3)

- Geospatial inference (fill gaps, align shapes, deduplicate geometries).  
- Harmonization of heterogeneous datasets and units.  
- Climate downscaling and bias-correction experiments (logged as MCP experiments).  
- Hydrology reconstruction (e.g., extend streamflow time series).  
- Automated metadata and STAC catalog generation.  
- Story Node candidate generation (AI suggests nodes; humans review and approve).  

### 🔵 3.3 Predictive & Reconstructive Pipelines

- Climate anomaly detection and regime shifts (PDO, ENSO, drought).  
- Hydrology series reconstruction (1900–2100).  
- Hazard overlays (tornado, hail, flood risk, wildfire potential).  
- Future scenario layers (e.g., 2050 climate/hydrology envelopes, with uncertainty).  

All AI components:

- Are **seeded** for deterministic runs where possible.  
- Carry **model cards** and **experiment logs** in `mcp/`.  
- Emit **OpenLineage v2.5** events and **PROV-O** RDF describing every inference step.  
- Are governed by **FAIR+CARE** and AI safety rules to prevent harmful or misleading outputs.  

---

## 🧭 4. Knowledge Graph & Ontology

KFM’s graph layer (Neo4j v5.x) is aligned with:

- **CIDOC-CRM** (cultural heritage & events)  
- **GeoSPARQL** (spatial relationships and geometries)  
- **OWL-Time** (temporal instants and intervals)  
- **PROV-O** (provenance of datasets, models, and transformations)  

### 4.1 Entities

- **Places** — towns, rivers, reservoirs, archaeological landscapes, H3 cells  
- **Events** — floods, droughts, WID operations, treaties, conflicts, infrastructure changes  
- **Datasets** — climate, hydrology, hazards, ecology, archaeology, landcover  
- **Observations** — time-series points, raster cells, vector features  
- **Story Nodes** — narrative units combining time, space, and text  
- **Agents** — people, organizations, councils, pipelines, AI agents  

### 4.2 Relations

- `geo:hasGeometry` — binds entities to geometries (with masking for sensitive sites)  
- `time:hasTime` — binds events and states to temporal intervals  
- `prov:wasGeneratedBy` — pipeline/model that produced a dataset  
- `prov:wasDerivedFrom` — data transformation lineage  
- `P70_documents` — dataset/document relations  
- `P7_took_place_at` — event-place relations  

These graph relations power **Focus Mode v3**, Story Node linking, and provenance-backed queries.

---

## 🗂️ 5. Repository Layout (Emoji Style A)

```text
Kansas-Frontier-Matrix/
├── 📄 README.md                         # This file (root overview)
│
├── 📂 data/                             # Data lifecycle (raw → work → processed → releases)
│   ├── 📂 raw/
│   ├── 📂 work/
│   ├── 📂 processed/
│   ├── 📂 stac/
│   ├── 📂 provenance/
│   └── 📂 releases/
│
├── 🧪 src/                              # Backend, ETL, AI, graph, telemetry
│   ├── 📂 pipelines/
│   ├── 📂 ai/
│   ├── 📂 graph/
│   ├── 📂 server/
│   └── 📂 telemetry/
│
├── 🌐 web/                              # Frontend (React + MapLibre + Cesium)
│   ├── 📂 src/
│   ├── 📂 public/
│   └── 📂 meta/
│
├── 📚 docs/                             # Standards, architecture, governance, analyses
│   ├── 📂 standards/
│   ├── 📂 architecture/
│   ├── 📂 analyses/
│   ├── 📂 governance/
│   └── 📂 templates/
│
├── 🧬 mcp/                              # Master Coder Protocol artifacts
│   ├── 📂 experiments/
│   ├── 📂 sops/
│   ├── 📂 model_cards/
│   └── 📄 MCP-README.md
│
└── ⚙️ .github/                          # CI/CD, automation, and GitHub infra
    ├── 📄 README.md
    ├── 🏗️ ARCHITECTURE.md
    └── 🤖 workflows/
```

---

## 🏛️ 6. Governance, Standards, & Ethics

KFM’s governance framework includes:

- **FAIR+CARE Council** — ensures data use respects Indigenous/ community rights and global ethics.  
- **Architecture Board** — guides technical design, performance, and sustainability.  
- **Heritage & Sovereignty policies** — protect sacred sites and cultural materials.  

Key standards:

- `docs/standards/kfm_markdown_protocol_v11.2.2.md` — KFM-MDP v11.2.2  
- `docs/standards/faircare/FAIRCARE-GUIDE.md` — FAIR+CARE implementation  
- `docs/standards/heritage/dynamic-h3-generalization.md` — dynamic H3 masking rules  
- `docs/contracts/data-contract-v3.json` — data contracts for dataset validation  

All changes to core architecture, data, or AI behaviors must:

- Pass required CI checks  
- Update docs + YAML front-matter  
- Be logged in provenance and audit ledgers  
- Comply with FAIR+CARE and sovereignty policies  

---

## 🚀 7. Getting Started (High-Level)

Clone and explore:

```bash
git clone https://github.com/<org>/Kansas-Frontier-Matrix.git
cd Kansas-Frontier-Matrix
```

### Backend / ETL

```bash
uv run src/pipelines/run_all.py
```

### Web App

```bash
cd web
npm install
npm run dev
```

### Graph Build

```bash
uv run src/graph/build_graph.py
```

See:

- `docs/architecture/system_overview.md`  
- `docs/architecture/pipelines/`  
- `docs/architecture/web/`  

for detailed instructions.

---

## 🧑‍💻 8. Contribution & Governance Rules

To contribute:

- Use the PR template in `.github/PULL_REQUEST_TEMPLATE.md`.  
- Fill in FAIR+CARE, a11y, and provenance sections.  
- Add or update YAML front-matter and version history in any touched doc.  
- Ensure new datasets have:
  - Checksum entries (`data/checksums/**`)  
  - STAC/DCAT metadata  
  - FAIR+CARE decisions/flags  

PRs must pass:

- Linting & tests  
- Schema & contract validation  
- FAIR+CARE validation  
- Security & SBOM checks  
- Governance approvals for sensitive changes  

---

## 🕰️ 9. Version History

| Version | Date       | Summary                                                                                         |
|--------:|-----------:|-------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Upgraded metadata & layout to strict KFM-MDP v11.2.2; added emoji repo layout; aligned references & governance hooks. |
| v11.1.2 | 2025-11-27 | Prior v11 root overview; defined mission, domains, and initial architecture summary.          |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](docs/README.md) · [📏 Standards Index](docs/standards/ROOT-STANDARDS.md) · [🛡 Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>