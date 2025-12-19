---
title: "Kansas Frontier Matrix — Architecture (Repo Overview)"
path: ".github/ARCHITECTURE.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Architecture"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:github:architecture:v1.0.0"
semantic_document_id: "kfm-github-architecture-v1.0.0"
event_source_id: "ledger:kfm:doc:github:architecture:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Kansas Frontier Matrix — Architecture

## 📘 Overview

### Purpose
- Provide a **GitHub-friendly architecture map** of Kansas Frontier Matrix (KFM): pipeline ordering, module boundaries, and “where things live” in the repo.
- This document is an **index + contract reminder**. Deep subsystem docs live under `docs/` (and are the canonical source of truth).

### Scope
| In Scope | Out of Scope |
|---|---|
| Canonical pipeline ordering; component boundaries; repo directory map; governance/validation expectations | Detailed deployment runbooks; full API reference; per-dataset ETL implementation details |

### Audience
- Primary: contributors and maintainers
- Secondary: reviewers, data stewards, and downstream integrators

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: ETL, STAC, DCAT, PROV-O, Neo4j, Story Nodes, Focus Mode

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline invariants + repo map) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline ordering + extension matrix |
| System architecture reference (PDF) | `docs/architecture/` | Maintainers | KFM 1.0 System Documentation PDF (filename not confirmed in repo) |
| Doc templates | `docs/templates/` | Maintainers | Universal doc, Story Node, API contract templates |
| Security baseline | `.github/SECURITY.md` | Maintainers | Security + disclosure expectations (not confirmed in repo) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Canonical pipeline ordering is stated and preserved
- [ ] Repository locations match the Master Guide / system docs (or “not confirmed in repo” is recorded)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `.github/ARCHITECTURE.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| GitHub governance + CI | `.github/` | SECURITY, workflows, repo-level standards |
| Data domains | `data/` | Raw/work/processed data + catalogs |
| STAC catalogs | `data/stac/` | STAC Collections + Items |
| DCAT catalogs | `data/catalog/dcat/` | DCAT dataset views (JSON-LD/Turtle) |
| PROV lineage | `data/prov/` | PROV-O bundles for runs/derivations |
| Pipelines | `src/pipelines/` | ETL + catalog generation |
| Graph | `src/graph/` | Neo4j ingest + ontology bindings |
| APIs | `src/server/` | REST/GraphQL serving layer (not confirmed in repo) |
| Frontend | `web/` | React map UI, layers, Focus Mode UX |
| Schemas | `schemas/` | JSON schema for catalogs/telemetry/etc. |
| Tests | `tests/` | Unit/integration/E2E tests |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
~~~text
📁 .github/
├── 📄 ARCHITECTURE.md
├── 📄 SECURITY.md
└── 📁 workflows/
    └── 📄 <ci-workflows>.yml

📁 data/
├── 📁 sources/
├── 📁 raw/
├── 📁 work/
├── 📁 processed/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/

📁 docs/
├── 📄 MASTER_GUIDE_v12.md
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
└── 📁 architecture/
    └── 📄 KFM_1_0_SYSTEM_DOCUMENTATION.pdf

📁 src/
├── 📁 pipelines/
│   ├── 📁 etl/
│   └── 📁 catalog/
├── 📁 graph/
└── 📁 server/

📁 web/
📁 schemas/
📁 tests/
📁 tools/
📁 mcp/
~~~

## 🧭 Context

### Background
KFM is designed as a governed, provenance-first system that:
- Ingests heterogeneous historical + geospatial sources
- Normalizes and catalogs them using open standards (STAC/DCAT/PROV-O)
- Loads semantics into a Neo4j knowledge graph
- Serves data to a React map/timeline UI via contracted APIs
- Curates narrative “Story Nodes” and Focus Mode experiences with explicit evidence links

### Assumptions
- The system is modular: each stage can evolve independently so long as it respects data contracts and schemas.
- “Public UI” access is mediated by an API layer (no direct graph access from the frontend).
- Provenance is first-class: catalog + graph objects must trace to sources and transforms.

### Constraints / invariants
- **Canonical pipeline ordering is preserved:**
  - ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode
- **API boundary is enforced:**
  - UI consumes contracted endpoints; it must not query Neo4j directly.
- **Determinism and replayability:**
  - ETL and catalog builds should be idempotent, logged, and reproducible.
- **Governance and sensitivity:**
  - Restricted/sensitive material is filtered, generalized, or flagged before it becomes public.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical API implementation stack (FastAPI vs Node.js vs other)? | TBD | TBD |
| What orchestration is used for ETL runs (Airflow/Prefect/custom/GitHub Actions)? | TBD | TBD |
| Where are large assets hosted (git vs object storage + CDN)? | TBD | TBD |
| What is the authn/authz model for write endpoints and contributor workflows? | TBD | TBD |

### Future extensions
- New data domains under `data/<domain>/...`
- AI evidence artifacts treated as cataloged assets and linked into Focus Mode
- New story node types and narrative UX controls (with provenance constraints)
- New CI “policy gates” for schema, integrity, security, and sovereignty

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  subgraph Data
    A[Raw Sources] --> B[ETL + Normalization]
    B --> C[Processed Data]
    C --> D[STAC/DCAT/PROV Catalogs]
  end

  D --> E[Neo4j Graph]
  E --> F[API Layer]
  F --> G[React/Map UI]
  G --> H[Story Nodes]
  H --> I[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI as UI (React/Map)
  participant API as API (REST/GraphQL)
  participant Graph as Neo4j
  participant Catalog as STAC/DCAT/PROV

  UI->>API: Request focus context(entity_id, time_range, layers)
  API->>Graph: Query subgraph + provenance refs
  Graph-->>API: Entities + relations + IDs
  API->>Catalog: Resolve STAC/DCAT/PROV refs
  Catalog-->>API: Assets + lineage + licenses
  API-->>UI: Context bundle + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Historical documents | PDF/TXT/DOCX/images | Archives, contributor uploads | Parse + OCR checks; completeness |
| Tabular datasets | CSV/XLSX | Agencies, curated extracts | Schema + range checks |
| Web sources | HTML | Public pages/APIs | Fetch integrity + content extraction |
| Geospatial files | SHP/GeoJSON/GeoTIFF | Portals, digitized maps | CRS + geometry validity |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Processed datasets | files (domain-specific) | `data/processed/` | Domain schemas (where defined) |
| STAC catalog | JSON | `data/stac/` | STAC 1.0 + KFM profile |
| DCAT catalog | JSON-LD/Turtle | `data/catalog/dcat/` | DCAT 3 + KFM profile |
| PROV bundles | JSON-LD (or equivalent) | `data/prov/` | PROV-O + KFM profile |
| Graph | Neo4j DB | (runtime) | Ontology + constraints |
| API payloads | JSON / GeoJSON | (runtime) | OpenAPI/GraphQL contracts |
| Story nodes | Markdown/JSON | `docs/reports/.../story_nodes/` | Story Node template + provenance rules |

### Sensitivity & redaction
- Any sensitive locations, culturally restricted content, or protected site data must:
  - be generalized (spatially/temporally) or omitted from public outputs
  - carry clear “restriction” flags and provenance pointers
  - be enforced at the API contract layer

### Quality signals
- Catalog schema validation (STAC/DCAT/PROV)
- Referential integrity (STAC items ↔ collections, link checks)
- Geometry validity + CRS normalization
- Entity resolution confidence scores (for merges/links)
- Audit trail completeness (source + run IDs)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- STAC Collections: `data/stac/collections/`
- STAC Items: `data/stac/items/`
- Each asset should include spatial/temporal extents, licensing, and source attribution.

### DCAT
- DCAT datasets: `data/catalog/dcat/`
- Dataset identifiers must remain stable across versions; distributions should link to STAC items and/or download artifacts.

### PROV-O
- PROV bundles: `data/prov/`
- Minimum lineage expectations:
  - `prov:wasDerivedFrom`: source IDs (raw assets / prior versions)
  - `prov:wasGeneratedBy`: pipeline run/activity ID
  - Activity + agent identities for human + automated steps

### Versioning
- Prefer explicit predecessor/successor links in catalogs and mirrored lineage relationships in the graph.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + extract + normalize; deterministic outputs | Config + run logs + validated outputs |
| Catalogs | Generate STAC/DCAT/PROV; schema validation | JSON / JSON-LD / Turtle |
| Graph (Neo4j) | Semantic integration + entity linking + provenance representation | Accessed via API layer |
| AI (cross-cutting) | Entity extraction, summarization, linking suggestions; human review support | Evidence products + logs |
| APIs | Serve contracted access; enforce governance and redaction | REST/GraphQL |
| UI | Map + timeline + Focus Mode UX; accessibility | API calls only |
| Story Nodes | Curated narrative artifacts with provenance | API + docs ingestion |
| Focus Mode | Context synthesis with citations + audit panel | Provenance-linked bundles |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas/docs | `src/server/` + `docs/` | Contract tests required |
| UI layer registry | `web/` | Schema-validated (exact path not confirmed in repo) |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump (if applicable)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focusable entities commonly include: `Place`, `Person`, `Event`, `Document`, `Organization`, `Artifact`.
- UI must render:
  - citations / source links
  - data usage restrictions
  - provenance and version context
  - uncertainty/confidence metadata when applicable

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- Predictive content (if any) must be opt-in and include uncertainty metadata.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Referential integrity checks (catalog links, items ↔ collections)
- [ ] Graph integrity checks (constraints, required labels/edges)
- [ ] API contract tests (OpenAPI/GraphQL)
- [ ] UI build + lint + a11y checks (where configured)
- [ ] Security scanning (dependencies + static checks)

### Reproduction
~~~bash
# Placeholder: replace with repo-specific commands
# 1) validate STAC/DCAT/PROV schemas
# 2) run unit/integration tests
# 3) run doc lint / markdown protocol validation
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| CI pass/fail + artifact hashes | GitHub Actions | `docs/telemetry/` + `schemas/telemetry/` |
| Data validation summaries | ETL/Catalog pipeline | `mcp/runs/` (or equivalent) |

## ⚖ FAIR+CARE & Governance

### Review gates
- New sensitive layers: requires governance review
- New AI narrative behaviors: requires ethics + review
- New external data sources: requires license + provenance review
- New public endpoints: requires security + contract review

### CARE / sovereignty considerations
- Identify communities impacted and ensure protection rules are applied before public release.
- Avoid exposing sensitive locations; use generalization/redaction.

### AI usage constraints
- AI must not introduce speculative policy or infer sensitive locations.
- AI-assisted outputs must be traceable and reviewable.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `.github/ARCHITECTURE.md` | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
