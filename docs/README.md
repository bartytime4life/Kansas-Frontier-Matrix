---
title: "🌾 Kansas Frontier Matrix — Monorepo Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "README.md"

version: "v11.2.3"
last_updated: "2025-12-04"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"
backward_compatibility: "Full v10.x → v11.x compatibility"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
signature_ref: "releases/v11.2.3/signature.sig"
attestation_ref: "releases/v11.2.3/slsa-attestation.json"
sbom_ref: "releases/v11.2.3/sbom.spdx.json"
manifest_ref: "releases/v11.2.3/manifest.zip"
telemetry_ref: "releases/v11.2.3/root-readme-telemetry.json"
telemetry_schema: "schemas/telemetry/root-readme-v11.2.3.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

status: "Active / Enforced"
doc_kind: "Monorepo Overview"
intent: "root-readme"
category: "Monorepo · Overview · Architecture"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "Annual review"
sunset_policy: "Superseded by Monorepo Overview v12"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 🌾 **Kansas Frontier Matrix**

`README.md`

**A semantic historical–geospatial platform weaving Kansas data into an interactive map, timeline, and narrative knowledge graph.**  
**A unified geospatial, historical, environmental, and cultural knowledge system for Kansas.**

<!-- Badge Row -->
<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.3-purple" />
<img src="https://img.shields.io/badge/Data-FAIR%2BCARE-gold" />
<img src="https://img.shields.io/badge/License-MIT-green" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🧭 1. Purpose

Kansas Frontier Matrix (KFM) is a large-scale, open-source knowledge architecture that integrates the natural, cultural, archaeological, environmental, and historical dimensions of Kansas into a single, interoperable system.

KFM exists to:

- Integrate fragmented datasets across soil, water, climate, archaeology, ecology, land use, infrastructure, and historical archives.
- Preserve cultural and environmental knowledge through robust metadata, long-term governance, and sovereignty-aware access controls.
- Model and simulate change across time — hydrology, climate, erosion, settlement patterns, ecosystem shifts, and more.
- Support researchers, agencies, tribal governments, historians, and the public through transparent, well-structured data.
- Empower advanced AI workflows with traceable lineage, ethical controls, and deterministic pipelines.

KFM is not just a database — it is a framework for **interdisciplinary understanding** and a governed **digital twin of Kansas**.

---

## 🗂️ 2. Monorepo Layout (Canonical · Emoji-Prefix Standard)

High-level canonical layout of the KFM monorepo, using the emoji-prefix directory convention:

    📁 KansasFrontierMatrix/                    — Monorepo root
    │
    ├── 📄 README.md                            — This file (monorepo overview)
    │
    ├── 📚 docs/                                — Documentation (standards, guides, analyses)
    │   ├── 📄 README.md                        — Documentation index & system overview
    │   ├── 🧭 overview/                        — High-level KFM system docs
    │   ├── 🏛️ architecture/                   — System & subsystem architecture
    │   ├── 📏 standards/                       — Governance, Markdown, FAIR+CARE, ontology, security
    │   ├── 📘 data/                            — Data contracts, STAC/DCAT catalogs, provenance docs
    │   └── 🧪 analyses/                        — Domain analyses and case studies
    │
    ├── 🧩 src/                                 — Application & ETL code
    │   ├── 🔁 pipelines/                       — ETL, watchers, updaters, domain pipelines
    │   │   ├── 👁️ watchers/                   — “Watchers” for upstream sources
    │   │   ├── 🔄 updaters/                    — Updater runners (schedulers, webhooks)
    │   │   ├── 🌤️ meteorology/                — HRRR, NODD, atmospheric ETL
    │   │   ├── 💧 hydrology/                   — Streamflow, reservoirs, WID, bathymetry ETL
    │   │   ├── ⚠️ hazards/                     — Severe weather, wildfire, drought ETL
    │   │   └── 🏺 archaeology/                 — Geophysics & archaeological spatial ETL
    │   ├── 🕸️ graph/                           — Neo4j schema, load scripts, graph APIs
    │   ├── 🔌 api/                             — FastAPI apps, GraphQL gateway, REST endpoints
    │   └── 🛠️ tools/                           — CLI utilities and helper scripts
    │
    ├── 🗺️ web/                                 — Frontend (React + MapLibre + Cesium)
    │   ├── 📁 src/                             — UI components, Focus Mode, Story Node viewers
    │   └── 📁 public/                          — Static assets
    │
    ├── 🗂️ data/                                — Data lifecycle (raw → work → processed → catalogs)
    │   ├── 📄 README.md                        — Data directory overview
    │   ├── 📄 ARCHITECTURE.md                  — Data system architecture
    │   ├── 📁 sources/                         — Source manifests (URLs, providers, policies)
    │   ├── 📁 raw/                             — Immutable source data (DVC/LFS tracked)
    │   ├── 📁 work/                            — Normalized & enriched intermediates
    │   ├── 📁 processed/                       — Analysis-ready outputs
    │   ├── 📁 stac/                            — STAC catalog, collections, items
    │   ├── 📁 dcat/                            — DCAT datasets & distributions
    │   ├── 📁 archive/                         — Retired/snapshotted data
    │   ├── 📁 checksums/                       — SHA-256 lineage registries
    │   ├── 📁 reports/                         — Validation, FAIR+CARE, audit reports
    │   └── 📁 tmp/                             — Scratch (ignored for production)
    │
    ├── 🧾 schemas/                             — JSON, SHACL, telemetry, & ontology schemas
    │   ├── 📁 json/
    │   └── 📁 telemetry/
    │
    ├── 📊 telemetry/                           — CI/CD, runtime, energy & carbon telemetry
    │   └── 📄 README.md
    │
    ├── 🛡️ governance/                          — Policies, FAIR+CARE, sovereignty rules
    │   └── 📄 README.md
    │
    ├── ⚙️ .github/                             — CI/CD workflows, policy-as-code
    │   └── 📁 workflows/
    │
    ├── 📄 LICENSE                              — MIT License for code
    ├── 📄 CONTRIBUTING.md                      — Contribution guidelines
    └── 📄 CODE_OF_CONDUCT.md                   — Community expectations

This layout ensures every pipeline, dataset, model, and document has a **predictable, FAIR+CARE-aligned home**.

---

## 🗺️ 3. System Overview (Layered Architecture)

KFM functions as:

- A statewide **knowledge graph**.
- A high-resolution **geospatial platform**.
- An **AI-assisted research environment**.

These are implemented as tightly integrated layers:

### 3.1 🌍 Geospatial & Sensor Data Layer

Includes:

- Hydrography (rivers, streams, reservoirs, diversions).
- Soil systems (SDA, SSURGO, gNATSGO, custom field datasets).
- Climate and weather (HRRR, GOES, NEXRAD, other NODD products).
- Satellite and aerial imagery (Sentinel-1/2, NAIP, Landsat).
- Elevation, bathymetry, DEM/DTM/LiDAR.
- Land cover, vegetation, and habitat maps.
- Infrastructure layers (roads, utilities, municipalities).

All assets are organized into machine-readable **STAC catalogs** and **DCAT datasets** using KFM profiles.

---

### 3.2 🏺 Historical, Archaeological, & Cultural Layer

Captures:

- Archaeological survey data and provenience records.
- Cultural landscape documentation and site narratives.
- Indigenous land use timelines and cultural geographies.
- Historical maps, plats, and cadastral datasets.
- Newspaper corpora and archival text collections.
- Settlement patterns, trails, trade networks, and routes.
- Artifact typologies, site stratigraphy, and geophysical survey data.

Sensitive locations can be generalized automatically using **dynamic H3-based redaction** and sovereignty-aware access tiers.

---

### 3.3 🧠 Knowledge Graph Layer (Neo4j + RDF Export)

Implements:

- Entity–relationship models for people, places, events, artifacts, hydrologic features, soils, climate periods, datasets, and Story Nodes.
- Semantic standards:
  - **CIDOC-CRM** for cultural heritage and events.
  - **GeoSPARQL** for spatial features and geometries.
  - **PROV-O** for provenance and lineage.
  - **OWL-Time** for temporal entities and periods.
- Full provenance chains for every ingest, transformation, and AI-assisted interpretation.

The graph connects environmental, cultural, and historical timelines into a unified, queryable structure.

---

### 3.4 🔁 Pipeline Layer (ETL + AI Pipelines)

Automated ingestion and processing pipelines handle:

- Weekly soil pulls from SDA / soilDB.
- Daily atmospheric updates via NOAA SNS → SQS and other event-driven feeds.
- Hydrology updates and derived metrics.
- Remote sensing change detection.
- Climate downscaling and anomaly detection.
- Archaeological metadata processing and generalization.
- Story Node and interpretation pipelines feeding Focus Mode.

Pipelines include:

- **Idempotent upserts** and contract-driven data models.
- **WAL-backed replay** and deterministic recovery.
- **Deterministic retry logic** and backoff.
- **Extensive metrics plus energy/CO₂ telemetry**.
- **FAIR+CARE and sovereignty-aware governance checks** at key stages.

---

### 3.5 🕸️ Web Platform Layer

Interactive frontend using:

- **React** for the UI.
- **MapLibre** for 2D web mapping.
- **CesiumJS** for 3D scenes and globe.
- A **timeline UI** for temporal navigation.
- A **graph viewer** for exploring entities and relationships.

Users can:

- Navigate and overlay multiple layers.
- Compare eras across historical and environmental timelines.
- Load historical imagery and map series.
- Explore archaeological contexts with appropriate sovereignty controls.
- Run simulations or narrative reconstructions grounded in the graph.

---

### 3.6 🤖 AI Layer (“Focus Mode”, Story Nodes, Analysis Models)

Supports:

- Automated summarization of complex spatial–temporal contexts.
- Interpretive archaeology workflows.
- Hydrologic trend detection and anomaly surfacing.
- Soil system classification and derived indices.
- Climate anomaly tagging and event linkage.
- Map-based question answering anchored to graph entities and datasets.
- Narrative reconstructions that cite graph entities, datasets, and provenance.

Every AI output is tied to:

- **Provenance** (PROV-O chains and source records).
- **Versioned models** with documented training data and parameters.
- **Input dataset references** (STAC Items, DCAT datasets, graph entities).

---

## 🗺 4. Interactive Map & Timeline

At the core of KFM is the **linked map + timeline**:

- **Map (MapLibre GL)**  
  - Base layers: modern basemaps, Kansas boundaries, elevation, hydrology.  
  - Historical overlays: topographic maps, county atlases, treaty boundaries, trails, land surveys.  
  - Themed layers: forts, towns, reservations, railroads, archaeological sites, wildlife distributions.

- **Timeline**  
  - Zoomable time axis from deep past to present (and scenario futures).  
  - Events grouped and color-coded by theme.  
  - Fully synchronized:
    - Moving the timeline filters visible features.  
    - Selecting an event highlights its spatial footprint.

Example interactions:

- Drag across **1854–1861** → see Kansas Territory, forts, early towns, and “Bleeding Kansas” events.  
- Select **Dust Bowl (1930s)** → vegetation, soil erosion proxies, and historical news overlays appear.  
- Explore **Cretaceous Kansas** → Western Interior Seaway shorelines and fossil discovery sites.

---

## 🎯 5. Focus Mode (v3)

**Focus Mode v3** is a context lens:

- You pick a **focus entity** (`Place`, `Person`, `Event`, `Tribe`, `Trail`, `Treaty`, `StoryNode`, etc.).  
- The backend pulls the **subgraph neighborhood**, including linked entities, datasets, and Story Nodes.  
- The UI reconfigures:
  - Timeline zooms to relevant intervals.  
  - Map highlights associated locations.  
  - Focus panel shows:
    - Data-grounded summary.  
    - Linked events, documents, people, datasets.  
    - Navigable “edges” across time and space.

All Focus Mode outputs:

- Are backed by underlying graph data.  
- Carry PROV-O provenance references.  
- Obey FAIR+CARE, sovereignty policies, and AI guardrails (no unsupported facts).

---

## 📚 6. Story Nodes — Narrative Layer

**Story Nodes** encode curated narratives that weave together space, time, and evidence.

Each Story Node combines:

- **Spatiotemporal envelopes** (GeoJSON + OWL-Time intervals).  
- **Linked graph entities** (people, places, events, datasets).  
- **Narrative text** (human-authored with optional AI assistance, documented).  

Examples:

- **“Santa Fe Trail”** — route-focused narrative linking diaries, forts, maps.  
- **“Bleeding Kansas”** — political violence and abolitionist history.  
- **“Ecological Change on the Plains”** — prairies, agriculture, and wildlife.

Story Nodes are:

- Versioned, with explicit lineage.  
- Designed to be exportable and reusable in other platforms.  
- Fully integrated into Focus Mode and the map + timeline.

---

## 🌐 7. Standards & Governance

KFM is driven by:

- **MCP-DL v6.3** — Master Coder Protocol (documentation-led workflows).  
- **KFM-MDP v11.2.3** — Markdown protocol and document profiles.  
- **KFM-OP v11** — Ontology protocol (CIDOC-CRM, OWL-Time, GeoSPARQL, PROV-O alignment).  
- **KFM-STAC v11** — STAC profile for Kansas geospatial assets.  
- **KFM-DCAT v11** — DCAT profile for dataset catalogs.  
- **FAIR + CARE** — Findable, Accessible, Interoperable, Reusable + ethical, sovereign use.

Governance is enforced by:

- FAIR+CARE Council.  
- Focus Mode Board.  
- Geo Standards, Pipelines, and Security working groups.  
- CI/CD workflows that validate:
  - Markdown and docs.  
  - STAC/DCAT records.  
  - Data contracts and schemas.  
  - Sovereignty and CARE labels.  
  - Supply-chain security (SLSA, SBOM, signatures).

---

## 🤝 8. Contributions & Community

We welcome contributions from:

- Historians, archaeologists, tribal historians.  
- Geographers, ecologists, hydrologists, climate scientists.  
- Data and software engineers.  
- Students, educators, and interested community members.

To contribute:

- Read `CONTRIBUTING.md`.  
- Follow Markdown and data standards in `docs/standards/`.  
- Open issues with clear context and goals.  
- Use **MCP-DL v6.3** patterns:  
  **doc → design → code → tests → lineage**.

---

## 🕰 9. Version History

| Version  | Date       | Summary                                                                                               |
|---------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Upgraded to KFM-MDP v11.2.3; aligned emoji-prefix monorepo layout; added telemetry/governance dirs.  |
| v11.2.2  | 2025-11-27 | Canonical monorepo layout; badge/footer alignment; telemetry schema updates; FAIR+CARE refinements.  |
| v11.0.0  | 2025-11-18 | Initial v11 root README; established monorepo overview and system architecture narrative.             |

---

<div align="center">

### 🌾 Kansas Frontier Matrix — Monorepo Overview (v11.2.3)  
_Ad astra per data — to the stars through Kansas data._

  
<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.3-purple" />
<img src="https://img.shields.io/badge/Data-FAIR%2BCARE-gold" />
<img src="https://img.shields.io/badge/License-MIT-green" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

  
© 2025 Kansas Frontier Matrix — MIT License  
MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[📚 Documentation Home](docs/README.md) ·  
[📐 System Architecture](docs/architecture/README.md) ·  
[⚖ Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>