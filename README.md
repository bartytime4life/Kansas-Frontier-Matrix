---
title: "🌌 Kansas Frontier Matrix — v11 System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "README.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Annual · FAIR+CARE Council & Architecture Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v11.0.0/sbom.spdx.json"
manifest_ref: "releases/v11.0.0/manifest.zip"
telemetry_ref: "releases/v11.0.0/system-telemetry.json"
telemetry_schema: "schemas/telemetry/system-v11.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "kfm-root-overview"
semantic_document_id: "kfm-doc-root-overview"
doc_uuid: "urn:kfm:readme:root:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I2-R3"
care_label: "Mixed / Multi-Domain"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
jurisdiction: "Kansas / United States"
classification: "Public"
lifecycle_stage: "stable"
ttl_policy: "48 months"
sunset_policy: "Superseded by KFM v12 Root Overview"
---

<div align="center">

# 🌌 **Kansas Frontier Matrix (KFM v11)**  
### **Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
### *A State-Scale Knowledge System for Kansas — Environment, History, Culture, AI, and Time*  

`README.md`

**Purpose:**  
Provide the **canonical, high-level overview** of the Kansas Frontier Matrix v11 — a fully-governed, reproducible, state-scale knowledge system unifying environment, history, culture, and AI into one coherent, semantic geospatial platform.

</div>

---

# 🌐 1. What the System Is

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
- FAIR+CARE · MCP-DL v6.3 · KFM-MDP v11  

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

---

# 🌍 2. State-Scale Environmental Knowledge Engine

KFM unifies major **environmental and geophysical domains** for Kansas:

- 🌧️ **Climate**  
  - PRISM, NOAA, ERA5, NOAA NCEI, Mesonet, drought indices, anomaly fields  
- 💧 **Hydrology**  
  - Rivers, lakes, USGS gauges, reservoir inflow/outflow, groundwater, WID & sedimentation  
- 🌱 **Ecology & Land Systems**  
  - Landcover, NDVI, biome maps, GAP species ranges, wetlands, fire regimes  
- 🏞️ **Terrain & Subsurface**  
  - DEMs (1m → coarse), bathymetry, lidar, geomorphology, geologic units  
- 🌪️ **Hazards & Energy**  
  - Wildfire risk, severe storms, tornado tracks, floodplains, drought, grid / pipeline overlays  

Each dataset is:

- Reprojected via standardized CRS pipelines (EPSG:4326 ↔ 3857 ↔ native CRS)  
- Harmonized with CF conventions (vertical datum, units, axis naming)  
- Registered as **STAC Collections & Items** in `data/stac/`  
- Linked to **DCAT Dataset** and **PROV-O** activity chain  
- Integrated into the **KFM Neo4j graph** as entities, events, and observations  

---

# 🧠 3. Multi-Layer AI & Autonomous Pipelines

KFM v11 uses a layered AI/ETL architecture that is **deterministic, logged, and governed**.

## 🔷 3.1 LangGraph v11 Deterministic DAG ETL

- Directed acyclic graphs (DAG) for all ETL flows  
- Write-ahead logs (WAL) for reproducibility and replay  
- Automatic retry / rollback with lineage tracking  
- Schema validation against **Data Contracts v3**  
- FAIR+CARE screening at every boundary (raw → work → processed → releases)  
- Time-indexed tasks (e.g., “rebuild climate anomalies 1900–2025”) with versioned outputs  

## 🔶 3.2 CrewAI Cooperative Workers (v2.5 → v3)

- Geospatial inference (fill gaps, align shapes)  
- Harmonization of heterogeneous datasets  
- Climate downscaling and bias-correction experiments (logged as MCP experiments)  
- Hydrology reconstruction (e.g., extend streamflow time series)  
- Automated metadata and STAC catalog generation  
- Story Node candidate generation (AI suggests nodes, humans approve)  

## 🔵 3.3 Predictive & Reconstructive Pipelines

- Climate anomaly detection and regime shifts (PDO, ENSO, drought)  
- Hydrology series reconstruction (1900–2100)  
- Hazard overlays (tornado, hail, flood risk, wildfire potential)  
- Future scenario layers (e.g., 2050 climate/hydrology envelopes, with uncertainty)  

All AI components:

- Are **seeded** for deterministic runs where possible  
- Carry **model cards** and **experiment logs** in `mcp/`  
- Emit **OpenLineage** events and PROV-O RDF describing every inference step  

---

# 🧭 4. Knowledge Graph (Neo4j / CIDOC-CRM / GeoSPARQL / OWL-Time)

The **KFM knowledge graph** fuses:

- People, places, events, features, datasets, observations  
- Spatial relationships (GeoSPARQL geometries, topologies)  
- Temporal relations (OWL-Time instants, intervals, periods)  
- Cultural layers and interaction spheres (e.g., Protohistoric Wichita)  
- Environmental and hydrologic lineages (e.g., dataset A derived-from dataset B)  
- Provenance chains (PROV-O activities, agents, entities)  
- Story Nodes v3 (narrative units with `spacetime` + `relations`)  

Graph API surfaces:

- 🚀 **FastAPI** for REST-style graph queries  
- 🧵 **GraphQL** for typed graph traversal and retrieval  
- 🌍 **Geospatial endpoints** for bounding-box, AOI, and path queries  
- 🔍 **Temporal & lineage queries**  
  - e.g., “show all events along the Kansas River between 1870–1900 with flood risk > X”  

All schemas are documented in `docs/graph/` and validated with automated tests.

---

# 🗺️ 5. Web Experience — React + MapLibre + Cesium + Focus Mode

## 🗺️ 5.1 2D Overview (MapLibre)

A React + MapLibre application provides:

- Layer toggles for hydrology, climate, archaeology, hazards, landcover, historical basemaps  
- Time-animated visualizations via the **timeline bar** (year/period scrubbing)  
- Popup panels tied to **Story Nodes** and Focus Mode summaries  
- Basemap configuration for dark/light, hillshade, and historical maps  

## 🛰️ 5.2 3D View (Cesium)

- 3D terrain with elevation and draped imagery  
- Extruded cultural and environmental layers (e.g., story elevation, hazard magnitude)  
- Camera paths for narrative tours (timeline-controlled flythroughs)  
- Time-dynamic visualization (era → scenes)  

## 🎛️ 5.3 Focus Mode v3

Focus Mode v3 is an AI-assisted narrative engine that:

1. Accepts an entity (place, event, dataset, person, treaty, etc.)  
2. Queries the knowledge graph for all relevant context (2–3 hop neighborhood)  
3. Binds spatial, temporal, cultural, and environmental factors  
4. Generates a **3-panel narrative**:
   - **Context panel** (where/when/what)  
   - **Timeline panel** (how it evolved over time)  
   - **Map panel** (H3-safe geography and overlays)  
5. Emits provenance for every statement:
   - Source datasets, Story Nodes, archives, and AI experiments  

All Focus Mode outputs respect:

- CARE constraints (no sensitive coordinates)  
- Narrative safety rules for heritage sites  
- Strict logging for later audits  

---

# 📚 6. Archives & Cultural Knowledge

KFM integrates **Kansas historical and cultural heritage** via:

- Historical newspapers (Chronicling America, Kansas Memory, etc.)  
- 19th–20th century archives (letters, diaries, plats, atlases)  
- Historical maps (topographic, cadastral, railroad, treaties)  
- Archaeological datasets and site inventories (properly masked)  
- Protohistoric Wichita interaction spheres (trade, travel, settlement patterns)  
- Museum catalogs and artifact metadata (KU, KGS, local museums)  
- Tribal heritage datasets (with explicit CARE governance and community approvals)  

All sensitive locations are handled via:

- 🛡️ **H3 spatial generalization Super-Standard v11** (`docs/standards/heritage/h3-generalization.md`)  
- 🧩 Dynamic H3 + CARE screening (`docs/standards/heritage/dynamic-h3-generalization.md`)  
- 🔏 Provenance logs in `data/provenance/`  
- ⚖️ Multi-layer governance (Tribal authorities · FAIR+CARE Council · Sensitive-Site Super-Standards)  

---

# 🌱 7. Standards, Governance, and Ethics

KFM v11 adheres to a **strict governance architecture**:

## 🏛️ 7.1 FAIR+CARE Council

Responsible for:

- Indigenous data sovereignty and authority  
- Ethics review of new datasets / features  
- Approval of sensitive-site publication policies  
- Oversight of AI narrative behavior and Focus Mode output  

## 📜 7.2 KFM-MDP v11 Markdown Protocol

- Single-file, GitHub-safe, **YAML front-matter** for all docs  
- Strict heading, emoji, directory tree, and footer rules  
- One H1 per file inside a `<div align="center">`  
- Mandatory version history and provenance references  
- Linting and CI-blocking on violations  

## 🧾 7.3 Data Contracts v3

- Enforced via validation pipelines in `src/pipelines/`  
- Required fields for each domain (climate, hydrology, archaeology, hazards, etc.)  
- Versioned JSON/YAML contract specs in `docs/contracts/`  
- Linked to STAC/DCAT metadata and Neo4j schema entities  

## 🔒 7.4 Security & Safety

- Confidentiality tiers (Tier-1 secure vs Tier-2 internal vs Tier-3 public)  
- Reprojection sanitation to avoid coordinate leakage  
- AI output governance (blocked phrases, narrative filters, hazard disclaimers)  
- Sensitive heritage: no raw coordinates outside Tier-1; mandatory H3 masking  

---

# 🗂 8. Repository Architecture (High-Level)

```text
Kansas-Frontier-Matrix/                 # Monorepo root
│
├── data/                               # Raw → work → processed → releases
│   ├── raw/                            # Immutable external inputs (not committed; DVC/LFS pointers)
│   ├── work/                           # ETL staging and intermediate workspaces
│   ├── processed/                      # Cleaned and analysis-ready outputs
│   ├── stac/                           # STAC Items/Collections for all spatiotemporal assets
│   ├── provenance/                     # PROV-O, OpenLineage, FAIR+CARE records
│   └── releases/                       # Versioned data bundles and public artifacts
│
├── src/                                # Python and backend sources
│   ├── pipelines/                      # LangGraph DAGs and data/AI pipelines
│   ├── ai/                             # CrewAI workers, models, prompt configs, explainers
│   ├── graph/                          # Neo4j ingestion code, schema management
│   ├── server/                         # FastAPI / GraphQL API services
│   └── telemetry/                      # Energy, IO, carbon, performance metrics collectors
│
├── web/                                # React + MapLibre + Cesium front-end
│   ├── components/                     # Shared UI components
│   ├── map/                            # MapLibre map configuration and layers
│   ├── 3d/                             # Cesium 3D scenes and time-dynamic views
│   └── api/                            # Front-end API clients and hooks
│
├── docs/                               # Standards, analyses, architecture, governance
│   ├── standards/                      # All KFM standards (markdown)
│   ├── analyses/                       # Analytical reports and case studies
│   ├── governance/                     # Governance charters and policies
│   ├── pipelines/                      # Pipeline design docs and SOPs
│   └── templates/                      # Documentation templates and MCP forms
│
└── mcp/                                # Master Coder Protocol assets (experiments, SOPs, model cards)
    ├── experiments/                    # Experiment logs and results (timestamped)
    ├── sops/                           # Standard Operating Procedures
    ├── model_cards/                    # AI/ML model cards
    └── MCP-README.md                   # MCP usage in this project
````

---

# 🔍 9. Provenance, Audit, & Telemetry

Every artifact in KFM is **provenance-first**:

* **Checksums:** SHA-256 for all significant files and bundles
* **STAC Extensions:** include privacy, CARE status, and lineage fields
* **PROV-O Lineage:** datasets link to activities and agents (who, what, when, how)
* **OpenLineage v2.5 events:** for all pipelines and AI runs
* **Energy & carbon telemetry:** via OpenTelemetry and energy/carbon attribution
* **Data contract references:** each dataset declares which contract it conforms to
* **SLSA & SBOM attestations:** supply chain and dependency transparency

No dataset enters KFM without:

1. Checksum creation
2. Schema validation (Data Contracts)
3. CARE review (if cultural / sensitive)
4. Explicit lineage entries
5. Deterministic build reproducibility

---

# 🧩 10. Feature Highlights

Some representative capabilities:

* 🔮 **AI Explainability Overlays** (SHAP/LIME)
* 🧭 **Historical Time Travel** (temporal graph + timeline queries)
* 🌾 **Cultural Landscape Reconstruction** (story nodes + map layers)
* ⚡ **Hazard & Energy Grid Integration** (storms vs infrastructure)
* ⛵ **Reservoir Sedimentation Modeling** (WID / bathymetry + inflows)
* 🛰️ **Remote-Sensing Change Detection** (NDVI, landcover, water extent)
* 📊 **Climate Index Reconstruction** (regional indices from historic data)
* 🔄 **Autonomous Nightly Data Refresh** (LangGraph + CrewAI orchestrated)

---

# 🚀 11. Getting Started

Clone the repository:

```bash
git clone https://github.com/<your-org>/kansas-frontier-matrix.git
cd kansas-frontier-matrix
```

Install and run the web app:

```bash
npm install
npm run dev
```

Run pipelines:

```bash
uv run src/pipelines/autonomous/run_all.py
```

Build / refresh the knowledge graph:

```bash
uv run src/graph/build_graph.py
```

(Exact commands may vary; see `docs/pipelines/` and `docs/architecture/` for up-to-date instructions.)

---

# 🧑‍💻 12. Contribution & Governance

KFM uses:

* GitHub PR templates aligned with **KFM-MDP v11**
* Prompt integrity hashing (LSH + Hamming threshold) to detect prompt drift
* Branch protection and required reviews
* Governance approvals for standards and sensitive changes
* Quarterly ethics audits and FAIR+CARE reviews

Every PR **must** include:

* Version bump where appropriate
* Updated metadata / YAML front-matter
* FAIR+CARE compliance for new data or AI behavior
* OpenLineage event emission where pipelines change
* Checksum / SBOM updates for new releases

See `docs/governance/ROOT-GOVERNANCE.md` and `docs/standards/` for full contribution rules.

---

# 🕰 13. Version History

| Version |       Date | Summary                                                    |
| ------: | ---------: | ---------------------------------------------------------- |
| v11.0.0 | 2025-11-23 | Initial v11 root overview README aligned with KFM-MDP v11. |

---

[Docs Home](docs/README.md) · [Standards Index](docs/standards/ROOT-STANDARDS.md) · [Governance](docs/standards/governance/ROOT-GOVERNANCE.md)

```
