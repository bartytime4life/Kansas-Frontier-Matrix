---
title: "🌌 Kansas Frontier Matrix — v11 System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
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
Provide the **canonical, high-level overview** of the Kansas Frontier Matrix v11 — a fully-governed, reproducible, state-scale knowledge system unifying environment, history, culture, AI, and time into one coherent, semantic geospatial platform.

</div>

---

## 📘 1. What the System Is

The **Kansas Frontier Matrix (KFM)** is a unified, multi-layer, multi-epoch knowledge system integrating:

- 🗺️ **Geospatial data** (2D/3D, map tiles, vector layers, rasters, H3 cells)  
- 🧠 **AI pipelines & autonomous ETL** (LangGraph DAGs, CrewAI workers, MLOps)  
- 📜 **Historical archives & newspapers** (Kansas Memory, Chronicling America, etc.)  
- 💧 **Environmental & hydrological models** (climate, rivers, groundwater, drought)  
- 🏺 **Archaeology & cultural landscapes** (Protohistoric Wichita, trails, forts, sites)  
- ⚡ **Hazards & infrastructure** (tornadoes, floods, wildfire, energy grids, pipelines)  
- 🌿 **Ecology & land systems** (grasslands, wetlands, species distributions)  
- 📖 **Narrative layers** (Story Nodes & Focus Mode v3)  

All stitched together through a **Neo4j knowledge graph** and a **governed CI/CD + governance stack** that enforce:

- Ontologies: CIDOC-CRM · GeoSPARQL · OWL-Time · PROV-O · ISO 19115  
- Catalogs: STAC 1.x · DCAT 3.0 · CF conventions  
- Governance: FAIR+CARE · Indigenous Data Sovereignty · KFM-MDP v11.2.2  
- Pipelines: KFM-PDC v11 · deterministic LangGraph DAGs · OpenLineage v2.5  

KFM v11 merges:

- 🛰️ **Remote sensing** (satellite, aerial, radar, lidar)  
- 💧 **Hydrology & climate chronologies** (USGS, NOAA, Mesonet, drought indices)  
- 🗺️ **GIS + MapLibre + Cesium 3D digital twin**  
- 🧬 **AI-assisted ETL & autonomous refresh pipelines** (auto-update patterns)  
- 🏺 **Archaeology & heritage** (masked via H3 and CARE policies)  
- 📚 **Archives, documents, newspapers, photos**  
- 🌪️ **Hazards: storm, flood, drought, wildfire, seismic, climate extremes**  
- 🐾 **Ecology & biodiversity** (GAP, GBIF, eBird, wetlands, landcover)  
- 📦 **STAC / DCAT / PROV-O provenance across data products**  
- 📖 **Story Nodes & Focus Mode v3** as AI-assisted narrative layers  
- 🏛️ **FAIR+CARE governance & Indigenous data sovereignty** baked into CI/CD  

The result is a **state-scale digital twin** of Kansas across time: physical, cultural, environmental, and narrative.

---

## 🌍 2. State-Scale Environmental Knowledge Engine

KFM unifies major **environmental and geophysical domains** for Kansas:

- 🌧️ **Climate**  
  - Historical station records (NOAA NCEI, Mesonet), gridded products (PRISM, Daymet, ERA5), climate normals, drought indices, anomaly fields.  

- 💧 **Hydrology**  
  - Rivers and streams (NHD), lakes and reservoirs, USGS gauges, groundwater levels, flood histories, WID & sedimentation, water rights and withdrawals.  

- 🌱 **Ecology & Land Systems**  
  - Landcover (historical and modern), NDVI/remote sensing, GAP species habitat, wetlands (NWI), fire regimes, prairie dynamics (Konza, LTER).  

- 🏞️ **Terrain & Subsurface**  
  - DEMs (1 m → 30 m → coarse), lidar-derived terrain, geomorphology, surficial and bedrock geology, aquifers, structural features.  

- 🌪️ **Hazards & Energy**  
  - Tornado & severe storm tracks (SPC), floodplains and events (FEMA, USGS), drought chronologies, wildfire risk, critical infrastructure, grid and pipeline overlays.  

Each dataset is:

- Harmonized via standardized CRS pipelines (EPSG:4326 ↔ 3857 ↔ native CRS).  
- Conformed to CF / units / vertical datums (NAVD88, GEOID18, sign conventions).  
- Registered as **STAC Collections & Items** in `data/stac/`.  
- Linked to **DCAT Datasets** and PROV-O activity chains for lineage.  
- Integrated into the **Neo4j graph** as entities, events, observations, and Story Node contexts.  

This enables **cross-domain analysis and storytelling**, e.g.:

> “Show all drought events that coincide with documented agricultural failures and a spike in out-migration from western Kansas counties.”

---

## 🧠 3. Multi-Layer AI & Autonomous Pipelines

KFM v11 uses a layered AI/ETL architecture that is **deterministic, logged, and governed**.

### 🔷 3.1 LangGraph v11 Deterministic DAG ETL

- All ETL flows modeled as **LangGraph DAGs** (batch + streaming).  
- Write-ahead logs (WAL) & lineage for replay and recovery.  
- Automatic retry/rollback with idempotent upserts to the graph and data lake.  
- Data Contracts (KFM-PDC v11) for schemas, ranges, units, and quality.  
- FAIR+CARE screening at boundaries: `raw → work → processed → releases`.  
- Pipeline telemetry exported via OpenTelemetry and OpenLineage.

### 🔶 3.2 CrewAI Cooperative Workers (v3)

- Surface-level tasks: geospatial snapping, unit harmonization, deduplication.  
- Domain tasks: climate downscaling experiments, hydrology reconstructions, hazard overlays.  
- Metadata tasks: STAC/DCAT authoring, text extraction & NER, Story Node candidate generation.  
- All runs captured in `mcp/experiments/` with model cards in `mcp/model_cards/`.

### 🔵 3.3 Predictive & Reconstructive Pipelines

- Climate anomaly detection & regime shifts (ENSO/PDO) with scenario projections.  
- Hydrology time-series reconstruction (pre-instrumental estimates → 2100 scenarios).  
- Hazard risk layers (e.g., probability of severe storms, compound flooding, drought vulnerability).  
- Scenario-based predictions for landcover, water stress, and hazard frequency.  

All AI components:

- Are **seeded and parameterized** for deterministic behavior where possible.  
- Are documented with **Model Cards** and experiment logs (MCP v2.0 style).  
- Emit OpenLineage events + PROV-O RDF statements for each inference.  
- Are gated by **AI behavior & narrative safety workflows** in `.github/workflows/`.

---

## 🧭 4. Knowledge Graph & Ontology Layer

KFM’s **graph** is implemented in Neo4j v5.x and aligned with:

- **CIDOC-CRM** — cultural heritage & historical events  
- **GeoSPARQL** — geometries, topologies, and spatial relationships  
- **OWL-Time** — time instants, intervals, and temporal relations  
- **PROV-O** — provenance for data, models, pipelines, and narratives  

### 4.1 Core Entity Types

- **Place** — counties, towns, rivers, reservoirs, trails, forts, archaeological landscapes, H3 cells.  
- **Event** — floods, droughts, storms, construction, treaties, conflicts, WID operations, model runs.  
- **Dataset** — climate fields, hydrology products, ecological layers, archive corpora, hazard layers.  
- **Observation** — time-series samples, raster pixels, vector features, derived metrics.  
- **Agent** — people, organizations, AI agents, councils, pipelines.  
- **StoryNode** — narrative unit combining `geometry + time + text + links` (Story Node schema v3).  

### 4.2 Relationships (Sketch)

- `geo:hasGeometry` (Place → Geometry)  
- `time:hasTime` (Event → Interval)  
- `prov:wasGeneratedBy` (Dataset → Activity/Workflow)  
- `prov:used` (Activity → Input Dataset/Model)  
- `crm:P7_took_place_at` (Event → Place)  
- `crm:P70_documents` (Document → Event/Place)  
- `story:links_to` (StoryNode → {Place, Event, Dataset})  

These relationships power **Focus Mode v3**, enabling:

> “Focus on Fort Larned” → return all related events, Story Nodes, datasets, hazards, ecological context, and narratives.

---

## 🗂️ 5. Repository Layout (KFM v11.2.2 · Emoji Profile A)

```text
Kansas-Frontier-Matrix/
├── 📄 README.md                         # Root system overview (this file)
│
├── 📂 data/                             # Data lifecycle & catalogs
│   ├── 📂 sources/                      # External source manifests (no large files)
│   ├── 📂 raw/                          # Downloaded raw data (DVC/LFS, ignored by git)
│   ├── 📂 work/                         # Intermediate artifacts (ephemeral/regen)
│   ├── 📂 processed/                    # Canonical processed outputs (GeoTIFF, GeoJSON, CSV)
│   ├── 📂 stac/                         # STAC 1.x catalog (Collections + Items)
│   ├── 📂 provenance/                   # PROV-O / lineage records (JSON-LD, RDF)
│   └── 📂 releases/                     # Versioned release bundles (SBOM, manifest, telemetry)
│
├── 🧪 src/                              # Backend, ETL, AI/ML, graph integration, telemetry
│   ├── 📂 pipelines/                    # LangGraph DAGs, ETL, reconciliation
│   ├── 📂 ai/                           # Models, feature extractors, Focus Mode logic
│   ├── 📂 graph/                        # Neo4j schema, queries, loaders
│   ├── 📂 server/                       # API services (FastAPI/GraphQL, etc.)
│   └── 📂 instrumentation/             # OpenLineage + OpenTelemetry helpers
│
├── 🌐 web/                              # Frontend (React + MapLibre + Cesium)
│   ├── 📂 src/                          # Components (map, timeline, Focus Mode UI)
│   ├── 📂 public/                       # Static assets
│   └── 📂 meta/                         # SEO, link cards, manifest/config
│
├── 📚 docs/                             # Documentation (user, developer, governance)
│   ├── 📂 standards/                    # KFM-MDP, FAIR+CARE, heritage, sovereignty policies
│   ├── 📂 architecture/                 # System design, pipelines, web, graph
│   ├── 📂 analyses/                     # Domain analyses and reports
│   ├── 📂 governance/                   # Council processes, charters, decision logs
│   └── 📂 templates/                    # Document & MCP templates
│
├── 🧬 mcp/                              # Master Coder Protocol (documentation-first assets)
│   ├── 📂 experiments/                  # Experiment logs (ETL, AI, modeling)
│   ├── 📂 sops/                         # Standard Operating Procedures
│   ├── 📂 model_cards/                  # Model cards for AI & statistical models
│   └── 📄 MCP-README.md                # MCP usage guide for KFM
│
├── 🧪 tests/                            # Unit, integration, and E2E tests
│   ├── 📂 backend/
│   ├── 📂 pipelines/
│   ├── 📂 web/
│   └── 📂 graph/
│
├── 🛠 tools/                            # Utility scripts & notebooks (non-core code)
│   ├── 📂 scripts/
│   └── 📂 notebooks/
│
└── ⚙️ .github/                          # GitHub infrastructure, CI/CD & governance
    ├── 📄 README.md                     # GitHub infra overview
    ├── 🏗️ ARCHITECTURE.md               # CI/CD architecture spec
    ├── 🤖 workflows/                    # CI/CD workflows (ci, docs, stac, dcat, AI, security, telemetry)
    └── 🧱 actions/                      # Composite actions (markdown-lint, schema-validate, etc.)
```

---

## 🏛️ 6. Governance, Standards & Ethics

KFM v11 is governed by:

- **FAIR+CARE Council** — data ethics, Indigenous data sovereignty, community interests.  
- **Architecture Board** — system design, performance, modularity, sustainability.  
- **Data & Heritage Working Groups** — archaeology, archives, hydrology, ecology.  
- **AI Safety & Narrative Governance Board** — Focus Mode, Story Nodes, model usage.

Key standards:

- `docs/standards/kfm_markdown_protocol_v11.2.2.md` — KFM-MDP v11.2.2 (Markdown Protocol)  
- `docs/standards/governance/ROOT-GOVERNANCE.md` — governance & council definitions  
- `docs/standards/faircare/FAIRCARE-GUIDE.md` — FAIR+CARE enforcement in data & narratives  
- `docs/standards/heritage/dynamic-h3-generalization.md` — dynamic H3 masking/aggregation  
- `docs/contracts/data-contract-v3.json` — KFM-PDC v11 data contracts  

All changes to **core architecture, data contracts, AI behaviors, or governance docs**:

- MUST pass CI/CD governance checks in `.github/workflows/`.  
- MUST update documentation & front-matter metadata.  
- MUST be recorded in provenance logs and, where applicable, governance minutes.  
- MUST comply with CARE and sovereignty policies.

---

## 🚀 7. Getting Started (High-Level)

### 7.1 Clone the Repository

```bash
git clone https://github.com/<org>/Kansas-Frontier-Matrix.git
cd Kansas-Frontier-Matrix
```

### 7.2 Backend / ETL (Dev Setup)

```bash
# Example: bootstrap a local ETL run
uv run src/pipelines/run_all.py
```

### 7.3 Web App (Dev Mode)

```bash
cd web
npm install
npm run dev
```

Open the URL printed by the dev server to explore the map + timeline + Focus Mode UI.

### 7.4 Graph Build (Local Neo4j)

```bash
uv run src/graph/build_graph.py
```

See:

- `docs/architecture/system_overview.md`  
- `docs/architecture/pipelines/`  
- `docs/architecture/web/`  
- `docs/architecture/graph/`  

for detailed setup and dependency notes.

---

## 🧑‍💻 8. Contribution & Governance Rules

To contribute:

- Use `.github/PULL_REQUEST_TEMPLATE.md` and fill all required sections:
  - Scope, tests, SBOM impact, telemetry impact, FAIR+CARE/sovereignty assessment.  
- Ensure **documentation-first**:
  - Update relevant docs and YAML front-matter (`version`, `last_updated`, `doc_uuid` if needed).  
- For new datasets:
  - Add `data/sources/` manifest entries.  
  - Include STAC Items/Collections and DCAT Dataset records.  
  - Provide checksums and provenance metadata.  
  - Add FAIR+CARE labels and sovereignty flags.

PRs must pass:

- Core CI (`ci.yml`)  
- Documentation validation (`docs_validate.yml`)  
- STAC/DCAT/JSON-LD checks (`stac_validate.yml`, `dcat_validate.yml`, `jsonld_validate.yml`)  
- FAIR+CARE & sovereignty (`faircare_validate.yml`, `h3_generalization.yml`)  
- Security & SBOM (`security_audit.yml`, `sbom_verify.yml`)  
- AI governance (if AI changes: `ai_behavior_check.yml`, `focusmode_mlops.yml`)  

And must be **approved by relevant CODEOWNERS**.

---

## 🕰️ 9. Version History

| Version | Date       | Summary                                                                                                             |
|--------:|------------|---------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Aligned root README with updated CI/CD, composite actions, Focus Mode v3, monorepo layout, and governance metadata. |
| v11.1.2 | 2025-11-27 | Prior v11 root overview; established digital twin framing and multi-domain scope.                                  |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](docs/README.md) · [📏 Standards Index](docs/standards/ROOT-STANDARDS.md) · [🛡 Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>