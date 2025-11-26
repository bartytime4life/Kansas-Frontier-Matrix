---
title: "🌌 Kansas Frontier Matrix — v11 System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "README.md"
version: "v11.1.1"
last_updated: "2025-11-27"
review_cycle: "Annual · FAIR+CARE Council & Architecture Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v11.0.0/sbom.spdx.json"
manifest_ref: "releases/v11.0.0/manifest.zip"
telemetry_ref: "releases/v11.0.0/system-telemetry.json"
telemetry_schema: "schemas/telemetry/system-v11.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "kfm-root-overview"
semantic_document_id: "kfm-doc-root-overview"
doc_uuid: "urn:kfm:readme:root:v11.1.1"
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

## 🧭 4. Knowledge Graph (Neo4j / CIDOC-CRM / GeoSPARQL / OWL-Time)

The **KFM knowledge graph** fuses:

- People, places, events, features, datasets, observations.  
- Spatial relationships (GeoSPARQL geometries/topologies, H3 cells for sensitive sites).  
- Temporal relations (OWL-Time instants, intervals, periods).  
- Cultural layers and interaction spheres (e.g., Protohistoric Wichita).  
- Environmental and hydrologic lineages (e.g., dataset A `prov:wasDerivedFrom` dataset B).  
- Provenance chains (PROV-O activities, agents, entities).  
- Story Nodes v3 (narrative units with `spacetime` + typed `relations`).  

Graph APIs:

- 🚀 **FastAPI** for REST-style graph queries.  
- 🧵 **GraphQL** for typed graph traversal and retrieval.  
- 🌍 **Geospatial endpoints** (bounded queries, AOI intersection, network traces).  
- 🔍 **Temporal & lineage queries** (e.g., “events along the Kansas River between 1870–1900 with flood risk > X”).  

Schemas and constraints are documented in `docs/graph/` and enforced via automated tests and migrations.

---

## 🗺️ 5. Web Experience — React + MapLibre + Cesium + Focus Mode

### 🗺️ 5.1 2D Overview (MapLibre)

React + MapLibre application:

- Layer toggles for hydrology, climate, archaeology, hazards, landcover, historical basemaps.  
- Time-animated visualizations via the **timeline bar** (year/period scrubbing).  
- Popup panels tied to **Story Nodes** and Focus Mode summaries.  
- Basemap configuration for dark/light, hillshade, and historical maps.  
- H3-aware generalization for sensitive locations (heritage, graves, sacred sites).  

### 🛰️ 5.2 3D View (Cesium)

- 3D terrain with elevation and draped imagery.  
- Extruded cultural and environmental layers (e.g., hazard magnitude, narrative intensity).  
- Camera paths for narrative tours (timeline-controlled flythroughs).  
- Time-dynamic visualizations (e.g., reservoir filling curves, drought sequences).  

### 🎛️ 5.3 Focus Mode v3

Focus Mode v3 is an AI-assisted narrative engine that:

1. Accepts an entity (place, event, dataset, person, treaty, etc.).  
2. Queries the knowledge graph for all relevant context (2–3 hop neighborhood).  
3. Binds spatial, temporal, cultural, and environmental factors.  
4. Generates a **3-panel narrative**:

   - **Context** — where/when/what.  
   - **Timeline** — how it evolves over time.  
   - **Map** — geography & overlays (H3-masked when needed).  

5. Emits provenance for every statement:

   - Source datasets, Story Nodes, archives, and AI experiments.  

Focus Mode is:

- Deterministic where possible (seeded runs).  
- Constrained by **FAIR+CARE** and narrative style/ethics rules.  
- Logged for audit and reproducibility.  

---

## 📚 6. Archives & Cultural Knowledge

KFM integrates **Kansas historical and cultural heritage** via:

- Historical newspapers (Chronicling America, Kansas Memory, regional archives).  
- 19th–20th century archives (letters, diaries, plats, atlases, photos).  
- Historical maps (topographic, cadastral, railroad, treaty maps).  
- Archaeological datasets and site inventories (masked at appropriate H3 resolutions).  
- Protohistoric Wichita interaction spheres (trade, travel, settlement patterns).  
- Museum catalogs and artifact metadata (KU, KGS, local museums).  
- Tribal heritage datasets (subject to CARE and sovereignty policies).  

Sensitive locations are handled via:

- 🛡️ **H3 spatial generalization Super-Standard v11** (`docs/standards/heritage/h3-generalization.md`).  
- 🧩 **Dynamic H3 + CARE screening** (`docs/standards/heritage/dynamic-h3-generalization.md`).  
- 🔏 Provenance logs in `data/provenance/`.  
- ⚖️ Multi-layer governance (Tribal authorities · FAIR+CARE Council · Sensitive-heritage standards).  

---

## 🌱 7. Standards, Governance, and Ethics

KFM v11 uses a **strong standards and governance framework**.

### 🏛️ 7.1 FAIR+CARE Council

Responsible for:

- Indigenous data sovereignty and authority.  
- Ethics review of new datasets and features.  
- Approval of sensitive-site publication policies.  
- Oversight of AI narrative behavior and Focus Mode outputs.  

### 📜 7.2 KFM-MDP v11 Markdown Protocol

- Single-file, GitHub-safe, **YAML front-matter** for all docs.  
- Strict heading, emoji, directory tree, and footer rules.  
- One H1 per file inside a centered `<div>`.  
- Mandatory version history and provenance references (for Standards).  
- Linting and CI-blocking on violations via `.github/docs_validate.yml`.  

### 🧾 7.3 Data Contracts v3

- Enforced via validation pipelines in `src/pipelines/`.  
- Required fields and contracts per domain (climate, hydrology, archaeology, hazards, etc.).  
- Versioned JSON/YAML contract specs in `docs/contracts/`.  
- Linked to STAC/DCAT metadata and Neo4j schema entities.  

### 🔒 7.4 Security & Safety

- Confidentiality tiers (Tier-1 secure vs Tier-2 internal vs Tier-3 public).  
- Reprojection sanitation to avoid coordinate leakage.  
- AI output governance (blocked phrases, narrative filters, hazard disclaimers).  
- Sensitive heritage: no raw coordinates in public; mandatory H3 masking.  
- Security policies and branch protections defined in `.github/`.  

---

## 🗂 8. Repository Architecture (High-Level)

```text
Kansas-Frontier-Matrix/                 # Monorepo root
│
├── data/                               # Raw → work → processed → releases
│   ├── raw/                            # Immutable external inputs (DVC/LFS; not committed)
│   ├── work/                           # ETL staging / intermediate workspaces
│   ├── processed/                      # Cleaned and analysis-ready outputs
│   ├── stac/                           # STAC Items/Collections for spatiotemporal assets
│   ├── provenance/                     # PROV-O, OpenLineage, FAIR+CARE records
│   └── releases/                       # Versioned data bundles and public artifacts
│
├── src/                                # Python and backend sources
│   ├── pipelines/                      # LangGraph DAGs and data/AI pipelines
│   ├── ai/                             # CrewAI workers, models, prompts, explainers
│   ├── graph/                          # Neo4j ingestion code, schema migrations
│   ├── server/                         # FastAPI / GraphQL API services
│   └── telemetry/                      # Energy, IO, carbon, performance metrics collectors
│
├── web/                                # React + MapLibre + Cesium frontend
│   ├── components/                     # Core UI components
│   ├── map/                            # 2D map configuration and layers
│   ├── three_d/                        # Cesium 3D scenes and time-dynamic views
│   └── api/                            # Frontend API clients and hooks
│
├── docs/                               # Standards, analyses, architecture, governance
│   ├── standards/                      # All KFM standards (markdown)
│   ├── architecture/                   # System, pipelines, CI/CD, graph, UI design docs
│   ├── analyses/                       # Analytical reports and case studies
│   ├── governance/                     # Governance charters and policies
│   └── templates/                      # Documentation templates and MCP forms
│
├── mcp/                                # Master Coder Protocol artifacts
│   ├── experiments/                    # Experiment logs and results (timestamped)
│   ├── sops/                           # Standard Operating Procedures
│   ├── model_cards/                    # AI/ML model cards
│   └── MCP-README.md                   # MCP usage and rules in KFM
│
└── .github/                            # GitHub CI/CD & governance automation
    ├── README.md                       # GitHub infrastructure overview
    ├── ARCHITECTURE.md                 # CI/CD architecture and governance blueprint
    └── workflows/                      # Actions for CI/CD, FAIR+CARE, security, telemetry
```

---

## 🔍 9. Provenance, Audit, & Telemetry

Every artifact in KFM is **provenance-first**:

- Checksums (e.g., SHA-256) for release bundles and key inputs.  
- STAC extensions for privacy/CARE status and lineage references.  
- PROV-O annotations linking data, activities, and agents.  
- **OpenLineage v2.5** events for all pipeline and AI runs.  
- Energy and carbon telemetry attributed per ETL job / workflow.  
- Data contract references in metadata and schema definitions.  
- SLSA & SBOM attestations for supply-chain transparency.  

No dataset or model enters KFM without:

1. Checksum generation.  
2. Contract/schema validation.  
3. CARE review (if cultural/sensitive).  
4. Provenance graph linkage.  
5. Deterministic build / run reproducibility.  

---

## 🧩 10. Feature Highlights

Representative capabilities:

- 🔮 **AI Explainability Overlays** (SHAP/LIME) on climate/hydrology models.  
- 🧭 **Historical Time Travel** — timeline + graph queries across centuries.  
- 🌾 **Cultural Landscape Reconstruction** — Story Nodes + spatial layers.  
- ⚡ **Hazard vs. Infrastructure** — storms, drought, wildfire vs. grid and pipelines.  
- ⛵ **Reservoir Sedimentation Modeling** — WID / bathymetry + inflow series.  
- 🛰️ **Remote-Sensing Change Detection** — NDVI, landcover, water extent.  
- 📊 **Climate Index Reconstruction** — indices derived from historical observations.  
- 🔄 **Autonomous Nightly Data Refresh** — orchestrated by LangGraph and CrewAI.  
- 📚 **Narrative Storytelling** — Focus Mode v3 and Story Nodes v3 integrated into UI.  

---

## 🚀 11. Getting Started

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

Run pipelines (example):

```bash
uv run src/pipelines/autonomous/run_all.py
```

Rebuild the knowledge graph (example):

```bash
uv run src/graph/build_graph.py
```

For detailed instructions, see:

- `docs/architecture/system_overview.md`  
- `docs/pipelines/reliable-pipelines.md`  
- `docs/standards/`  

---

## 🧑‍💻 12. Contribution & Governance

KFM uses a **documentation-first, governance-first** contribution model:

- PRs must comply with **KFM-MDP v11.2.2** markdown rules.  
- Issue and PR templates capture CARE, provenance, and a11y metadata.  
- Branch protections enforce required checks (lint, tests, FAIR+CARE, security).  
- Prompt integrity hashing and governance rules protect core AI prompts.  
- Quarterly ethics audits and FAIR+CARE reviews keep policies up-to-date.  

Each contribution must:

- Bump versions and dates where needed.  
- Update YAML front-matter and version history.  
- Declare data sensitivity and licensing for new datasets.  
- Emit OpenLineage events when pipelines are changed.  
- Respect Indigenous data sovereignty and governance documents.  

See:

- `docs/standards/governance/ROOT-GOVERNANCE.md`  
- `docs/standards/faircare/FAIRCARE-GUIDE.md`  
- `.github/README.md` and `.github/ARCHITECTURE.md`  

for full participation details.

---

## 🕰 13. Version History

| Version | Date       | Summary                                                                                     |
|--------:|------------|---------------------------------------------------------------------------------------------|
| v11.1.1 | 2025-11-27 | Aligned root README with KFM-MDP v11.2.2 header semantics; minor metadata and CI notes tuned. |
| v11.1.0 | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; clarified repo architecture, provenance/telemetry, and governance hooks. |
| v11.0.1 | 2025-11-23 | Enriched with repository layout, governance, and AI/ETL descriptions.                       |
| v11.0.0 | 2025-11-23 | Initial v11 root overview; defined KFM v11 mission, domains, and high-level architecture.   |

---

<div align="center">

[📚 Docs Home](docs/README.md) · [📏 Standards Index](docs/standards/ROOT-STANDARDS.md) · [⚖ Governance](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
