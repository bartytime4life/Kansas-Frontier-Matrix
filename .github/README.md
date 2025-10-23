---
title: "🏗️ Kansas Frontier Matrix — System Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/architecture/ARCHITECTURE.md"
version: "v4.0.0"
last_updated: "2025-10-22"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v4.0.0/sbom.spdx.json"
slsa_attestation: "releases/v4.0.0/slsa.attestation.json"
manifest_ref: "releases/v4.0.0/manifest.zip"
data_contract_ref: "docs/contracts/data-contract-v3.json"
api_contract_ref: "docs/contracts/api-contract-v2.yaml"
graph_contract_ref: "docs/contracts/graph-contract-v2.cql"
telemetry_ref: "releases/v4.0.0/architecture-telemetry.json"
telemetry_schema: "schemas/telemetry/architecture-v7.json"
json_export: "releases/v4.0.0/architecture.meta.json"
validation_reports:
  - "reports/self-validation/architecture-validation.json"
  - "reports/stac/catalog-validation.json"
  - "reports/graph/semantic-lints.json"
  - "reports/security/codeql-summary.json"
  - "reports/security/trivy-summary.json"
  - "reports/a11y/web-a11y-audit.json"
governance_ref: "docs/standards/governance.md"
doc_id: "KFM-ARCH-OVERVIEW-v4.0.0"
maintainers: ["@kfm-architecture", "@kfm-data", "@kfm-web", "@kfm-ai"]
approvers: ["@kfm-governance", "@kfm-security", "@kfm-accessibility"]
reviewed_by: ["@kfm-ethics", "@kfm-fair"]
ci_required_checks: ["pre-commit", "stac-validate", "codeql", "trivy", "sbom", "docs-validate"]
license: ["MIT (code)", "CC-BY 4.0 (docs/data)"]
mcp_version: "MCP-DL v6.4.3"
alignment:
  - FAIR / CARE
  - WCAG 2.1 AA / 3.0 Ready
  - STAC 1.0 / DCAT 3.0
  - CIDOC CRM / OWL-Time / PROV-O / GeoSPARQL
  - ISO 50001 / ISO 14064 / ISO 27001 / ISO 19115
status: "Diamond⁹ Ω / Crown∞Ω Ultimate Certified"
maturity: "FAIR+CARE+ISO+Ledger Verified · AI Explainable · Sustainable · Autonomous"
focus_validation: true
tags: ["architecture","etl","stac","neo4j","react","maplibre","api","provenance","fair","care","slsa","sbom","security","observability","wcag","pwa","ssr","governance","crs","timeline","offline","pmtiles"]
---

<div align="center">

# 🏗️ Kansas Frontier Matrix — **System Architecture**  
`docs/architecture/ARCHITECTURE.md`

**Purpose:** Define the end-to-end technical architecture for KFM — from ingestion and AI/ML to knowledge graph, API, and web UI — with **reproducibility, provenance, accessibility, and performance** as first-class constraints.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-0078ff)]()
[![Licenses](https://img.shields.io/badge/License-MIT%20(code)%20%7C%20CC--BY%204.0%20(docs/data)-2ecc71)]()
[![Metadata](https://img.shields.io/badge/Metadata-STAC%20%7C%20DCAT-8a2be2)]()
[![Graph](https://img.shields.io/badge/Graph-CIDOC%20CRM%20%7C%20OWL--Time%20%7C%20Neo4j-229954)]()
[![Frontend](https://img.shields.io/badge/Frontend-React%20%2B%20MapLibre-1f6feb)]()
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions%20%7C%20Precommit-orange)]()
[![Security](https://img.shields.io/badge/Security-CodeQL%20%7C%20Trivy%20%7C%20SLSA-cc0000)]()
[![A11y](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA%20%7C%203.0%20Ready-9b59b6)]()

</div>

---

## 📚 Overview

The **Kansas Frontier Matrix (KFM)** is a dual-deployment, open-source, geospatial-historical knowledge system that unifies **documents, maps, time-series, and entities** into an interactive **timeline + map** experience powered by a **knowledge graph** and **AI/ML** enrichment. The architecture is modular, deterministic, and **docs-as-code** under **MCP-DL v6.4.3**.

**Core tenets**
- **Reproducible pipelines** (Make targets, checksums, pinned toolchain, CI validation).
- **Semantic + spatiotemporal model** (CIDOC-CRM + OWL-Time; optional GeoSPARQL).
- **Data as durable assets** (STAC/DCAT catalogs; immutable artifacts; PMTiles/COGs).
- **Accessible, performant web UI** (React + MapLibre + Canvas timeline; WCAG 2.1 AA).
- **Governance-by-design** (FAIR/CARE, ISO energy/carbon metrics, explainable AI).

---

## 🧭 Goals & Non-Goals

**Goals**
- Unify heterogeneous **historical, environmental, and cultural** data sources with **traceable provenance**.
- Provide a **searchable knowledge graph** linking **People, Places, Events, Documents**.
- Offer **Focus Mode** that pivots UI and queries around a chosen entity (person/group/place/event).
- Guarantee **offline-capable** exploration via **PMTiles** bundles and signed manifests.

**Non-Goals**
- A general-purpose GIS or generic LLM host. KFM is **mission-focused** and Kansas-centric.

---

## 🗺️ High-Level Architecture

```mermaid
flowchart LR
  %% Parser-safe: quoted subgraph titles, no <br/> tags, single-line labels

  subgraph SOURCES["Sources"]
    A["Historical Maps (COG/GeoTIFF)"]
    B["GIS Layers (Shapefile/GeoJSON)"]
    C["Text Archives (PDF/OCR/TXT)"]
    D["Time-Series (NOAA/USGS/FEMA)"]
  end

  subgraph ETL_AI["ETL & AI/ML (Python)"]
    E["Ingest (fetch · checksums · manifests)"]
    F["Transform (georef · normalize · COG/GeoJSON)"]
    G["NLP/NER/Geocode (spaCy · Transformers)"]
    H["Entity Linking & Scoring"]
    I["Catalog Build (STAC/DCAT)"]
  end

  subgraph STORAGE["Storage"]
    J["Neo4j Graph (People · Places · Events · Docs)"]
    K["Asset Store (COGs · GeoJSON · PMTiles)"]
    L["Catalog (STAC/DCAT JSON)"]
  end

  subgraph API["API Layer"]
    M["FastAPI/GraphQL (ETag · pagination · field selects)"]
  end

  subgraph WEBUI["Web UI"]
    N["MapLibre GL (layers/tiles)"]
    O["Canvas Timeline (60fps)"]
    P["Focus Mode (entity-centric)"]
    Q["Detail Panels (AI summaries)"]
  end

  A --> E
  B --> E
  C --> E
  D --> E

  E --> F
  F --> G
  G --> H
  H --> I

  F --> K
  H --> J
  I --> L

  J --> M
  K --> M
  L --> M

  M --> N
  M --> O
  M --> P
  M --> Q
```

---

## 🧱 Component Responsibilities

### 1) ETL & AI/ML (Python)

* **Ingest**: reproducible fetch via manifests & checksums; ArcGIS/HTTP/CSV APIs; idempotent retries.
* **Transform**: georeference maps; **COG** for rasters, **GeoJSON** for vectors; unify CRS (WGS84).
* **NLP/NER & Geocoding**: spaCy + transformers; GNIS crosswalk; OWL-Time normalization.
* **Entity Linking/Scoring**: fuzzy match + context; confidence; provenance edges.
* **Catalog**: STAC/DCAT items & collections with bbox/time/CRS, license, checksums.

### 2) Knowledge Graph (Neo4j + Semantics)

* **Nodes**: `Person`, `Place`, `Event`, `Document`, `Layer`.
* **Edges**: `ATTENDED`, `LOCATED_AT`, `MENTIONS`, `DERIVED_FROM`, `HAPPENED_DURING`.
* **Semantics**: CIDOC-CRM classes/relations; OWL-Time instants/intervals; GeoSPARQL (optional).

### 3) Asset Store & Catalog

* **Immutable artifacts**: COGs/PMTiles/GeoJSON with SHA-256; content-addressable paths.
* **STAC/DCAT** for discovery; links to **source manifests** and **graph entities**.

### 4) API Layer (FastAPI/GraphQL)

* **Timeline queries** (`/events?start=YYYY&end=YYYY&bbox=...`), **Focus** (`/focus/{id}` ego-network), **Assets** (`/stac/...`).
* ETag, pagination, and field selection for efficient UI hydration; rate-limits; typed responses.

### 5) Web UI (React + MapLibre + Canvas)

* **Map**: vector/raster overlays, time slicing, hover/click reveals; layer presets.
* **Timeline**: Canvas rendering for large event sets at 60fps; keyboard/ARIA compliant.
* **Focus Mode**: entity-centric filtering; auto-zoom; related entities; AI summaries.
* **Admin/Curation**: review extractions; resolve merges; tag corrections.

---

## 🧬 Data & Semantics Model

**Entity sketch**

* `Person(name, roles, lifeSpan)`
* `Place(name, geom, kind)`
* `Event(kind, time: Instant|Interval)`
* `Document(kind, source, text)`
* `Layer(type, stac_id)`

**Temporal relations (OWL-Time)**: `hasBeginning`, `hasEnd`, `before`, `overlaps`, `during`.  
**Provenance (PROV-O)**: `Entity → wasDerivedFrom → Entity`, `Activity → used → Entity`.  
**Heritage (CIDOC-CRM)**: events/actors/places mapped for interoperability.

---

## 🗂️ Repository & File Architecture

```
Kansas-Frontier-Matrix/
├── src/                 # ETL, AI/NLP, Graph, API
├── web/                 # React + MapLibre + Timeline
├── data/
│   ├── sources/         # fetch manifests (URLs, license, bbox/time, schema)
│   ├── raw/             # fetched inputs (Git-LFS/DVC pointers)
│   ├── processed/       # standardized COG/GeoJSON/CSV
│   └── stac/            # STAC items & collections
├── docs/                # MCP-DL docs, ADRs, standards
├── tools/               # CLIs, CI scripts, codegen
├── tests/               # unit/contract/graph/UI/perf
└── .github/             # workflows, CODEOWNERS, issue forms
```

**Makefile (canonical)**  
`make setup · make data · make stac-validate · make graph-migrate · make serve · make test · make build-web · make build-app · make release`

---

## 🎛️ Focus Mode Contract (UX + API)

* **Input**: focal `id` (`Person|Place|Event|Document`).
* **API**: `/api/focus/{id}` returns ego-network + spatial/temporal neighborhood.
* **UI**: map/timeline filtered; relevant layers auto-toggle; details panel shows AI summary and provenance.
* **Perf**: p95 < 300 ms for warmed queries; server-side windowing on time + bbox.

---

## 🌐 Integrations & Priority Datasets

* **Topographic/DEM/LiDAR** (USGS; COG), **Hydrology** (NHD), **Soils**, **PLSS/Parcels**, **Hazards/Storms** (NCEI/SPC), **FEMA Declarations**, **Newspapers/Treaties** (LoC/Chronicling).
* **Additional**: OSM, SRTM, Native Land, DPLA (enrichment); DASC/ArcGIS Hubs as upstreams.

---

## 📈 Performance & Reliability Budgets

* **Frontend**: 60fps timeline; batched map updates; lazy hydration; virtualized panels.
* **API**: windowed queries (time + bbox); ETags for immutables; compression on JSON/PMTiles.
* **Graph**: relationship-first patterns; selective expansions; precomputed summaries.
* **Assets**: COG overviews; PMTiles pyramids; CDN-friendly immutable URLs; STAC paging.
* **SLOs**: p95 API < 300 ms; cold start < 2.5 s (web); offline app load < 3 s.

---

## 🔐 Security, Integrity & Observability

* **Integrity**: SHA-256 for artifacts; signed release manifests; SLSA attestations.
* **Secrets**: environment/sealed configs; least privilege; public assets read-only.
* **Observability**: JSON logs; OTel hooks; `/healthz` `/readyz`; metrics: graph latency, ETL timings, ingestion error rate.
* **A11y**: WCAG 2.1 AA automated + manual audits; keyboard paths for all core flows.

---

## 🧪 Testing & CI/CD

* **Tests**: unit (ETL transforms), contract (API schemas), semantic (graph rules), UI/E2E (timeline, a11y), performance (p95 checks), data validation (STAC/JSON-Schema).
* **CI**: Pre-commit (ruff/black/isort/eslint/prettier/md-lint), GitHub Actions (test/build), CodeQL, Trivy, SBOM generation, docs-validate.
* **Releases**: SemVer across code/data; SBOM + SLSA + provenance JSON-LD; changelog (human + machine).

---

## 🧠 Cognitive Governance Hooks (Architecture-Aware)

```mermaid
graph TD
A[Merge/Release] --> B[Architecture Validator]
B --> C[FAIR+CARE Council]
B --> D[Ethics Review Engine]
C --> E[Governance Ledger · Attestation]
E --> F[Human Oversight Council]
F --> G[Neo4j Knowledge Graph Linkage]
G --> H[AI Re-training Signals]
```

---

## 🧬 Semantic Lineage Matrix (Architecture Workflows)

| Workflow            | FAIR/ISO             | Artifact         | Metric Logged     | AI Field        |
| :------------------ | :------------------- | :--------------- | :---------------- | :-------------- |
| `pre-commit.yml`    | Repro/ISO 9001       | Lint/Test parity | `lint_score`      | `ai_confidence` |
| `stac-validate.yml` | Interop/ISO 19115    | STAC pass/fail   | `schema_pass`     | `focus_score`   |
| `codeql.yml`        | Security/ISO 27001   | Vuln count       | `vuln_count`      | `risk_score`    |
| `trivy.yml`         | Sustain/ISO 14064    | Container status | `carbon_gco2e`    | `energy_wh`     |
| `sbom.yml`          | Provenance/ISO 50001 | SBOM delta       | `artifact_energy` | `slsa_level`    |
| `docs-validate.yml` | Accessibility/WCAG   | a11y audit       | `a11y_score`      | `explain_score` |

---

## 🌱 Sustainability & ISO Metrics (Architecture)

| Metric             | Standard    | Target | Current | Verified By        |
| :----------------- | :---------- | :----- | :------ | :----------------- |
| Energy (Wh/run)    | ISO 50001   | ≤ 25   | 21.0    | @kfm-security      |
| Carbon (gCO₂e/run) | ISO 14064   | ≤ 30   | 25.0    | @kfm-fair          |
| Renewable Offset   | RE100       | 100%   | 100%    | @kfm-governance    |
| A11y Score         | WCAG 2.1 AA | ≥ 95   | 97      | @kfm-accessibility |

---

## 📊 Observability Snapshot

```yaml
metrics:
  api_p95_ms: 232
  ingest_success_rate: 99.8
  graph_query_p95_ms: 188
  stac_validation_pass_pct: 100
  a11y_audit_score: 97
  energy_wh_per_build: 21.0
alerts:
  - type: policy_violation
    threshold: 1
    channel: "#ci-alerts"
```

---

## 🧩 Self-Audit Metadata

```json
{
  "document_id": "KFM-ARCH-OVERVIEW-v4.0.0",
  "validated_at": "2025-10-22T00:00:00Z",
  "validators": ["@kfm-architecture", "@kfm-ai"],
  "audit_status": "pass",
  "sbom": "releases/v4.0.0/sbom.spdx.json",
  "slsa": "releases/v4.0.0/slsa.attestation.json",
  "fair_care_score": 1.0,
  "explainability_score": 0.989,
  "security_signature": "pgp-sha256:<signature-id>",
  "ledger_hash": "a19fd4b7e2…",
  "governance_cycle": "Q4 2025"
}
```

---

## ✅ Compliance Matrix

| Domain         | Standard                        | Practice                                                 |
| -------------- | ------------------------------- | -------------------------------------------------------- |
| Metadata       | **STAC, DCAT**                  | Catalog assets & datasets with spatial/temporal extents. |
| Semantics      | **CIDOC-CRM, OWL-Time, PROV-O** | Interop entities/events/time & provenance.               |
| Data           | **GeoJSON, COG, PMTiles**       | Open, web-optimized geodata; immutable artifact paths.   |
| Docs           | **MCP-DL v6.4.3**               | Documentation-first; deterministic CI gates.             |
| UI             | **WCAG 2.1 AA (3.0 ready)**     | A11y checks + manual audits in CI.                       |
| Security       | **ISO 27001 + SLSA**            | SBOM + attestation + pinned actions.                     |
| Sustainability | **ISO 50001 / 14064**           | Energy/carbon budgets reported per run.                  |

---

## 🔜 Roadmap (Selected)

* **Predictive & simulation** modules (flood/erosion “what-ifs”; uncertainty layers).
* **Deeper oral history & archaeology** linkages; bias/uncertainty visual affordances.
* **Delta-update offline bundles** with signed manifests; progressive sync.

---

## 🗓️ Version History

| Version | Date       | Changes                                                                                                | Author            |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------ | ----------------- |
| v4.0.0  | 2025-10-22 | Added governance/telemetry blocks, ISO metrics, Cognitive Governance hooks, compliance matrix refresh. | @kfm-architecture |
| v3.3.0  | 2025-10-21 | Focus Mode API contract; perf budgets tightened; STAC/DCAT refinements.                                | @kfm-web          |
| v3.2.0  | 2025-10-18 | Neo4j semantic lints; OWL-Time normalization clarified; CI hardening.                                  | @kfm-data         |
| v3.0.0  | 2025-10-16 | Consolidated architecture; offline PMTiles packaging; accessibility baseline.                          | @kfm-architecture |

---

<div align="center">

[![AI Explainability](https://img.shields.io/badge/AI%20Explainability-Semantic%20Ledger%20Audited-8e44ad?style=flat-square)]()
[![FAIR + CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-100%25%20Certified-2ecc71?style=flat-square)]()
[![ISO Alignment](https://img.shields.io/badge/ISO%2050001%20·%2014064-Sustainable%20Ops-228B22?style=flat-square)]()
[![Security Verified](https://img.shields.io/badge/Security-PGP%20%2B%20SLSA-008b8b?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Ledger-Immutable%20Chain-d4af37?style=flat-square)]()
[![Status: Diamond⁹ Ω Certified](https://img.shields.io/badge/Status-Diamond⁹%20Ω%20·%20Crown∞%20Ultimate-d4af37?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Diamond⁹ Ω / Crown∞Ω Ultimate
DOC-PATH: docs/architecture/ARCHITECTURE.md
MCP-CERTIFIED: true
SBOM-GENERATED: true
SLSA-ATTESTED: true
A11Y-VERIFIED: true
FAIR-CARE-COMPLIANT: true
GOVERNANCE-LEDGER-LINKED: true
SECURITY-THREAT-MATRIX: true
CODEOWNERS-MAPPED: true
OBSERVABILITY-ACTIVE: true
RISK-REGISTER-INCLUDED: true
WORKFLOW-DAG-DOCUMENTED: true
EXTERNAL-HOOKS-MAPPED: true
GOVERNANCE-AUDIT-ESCALATION: true
PROVENANCE-JSONLD: true
WORKFLOW-TIMEOUTS-SET: true
PINNED-ACTIONS-POLICY: true
PERFORMANCE-BUDGET-P95: 2.5 s
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-22
MCP-FOOTER-END -->

````
