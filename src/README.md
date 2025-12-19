---
title: "KFM — src/ Source Code Guide"
path: "src/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Guide"
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

doc_uuid: "urn:kfm:doc:src:readme:v1.0.0"
semantic_document_id: "kfm-src-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:readme:v1.0.0"
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

# src/ — KFM Source Code (Developer Guide)

## 📘 Overview

This README is the navigation and “rules of the road” for the `src/` subtree.

### What lives here
- **Pipeline code** that ingests/transforms data and produces catalog artifacts (STAC/DCAT/PROV).
- **Graph code** that maps governed data + catalogs into the Neo4j knowledge graph.
- **Server/API code** that exposes contracted access to the system (REST/GraphQL), enforcing sensitivity rules and provenance requirements.

### What does *not* live here
- **Raw or derived datasets** (use `data/`).
- **Governed documentation and templates** (use `docs/`).
- **Frontend UI** (canonical location is `web/`).

### Canonical flow (non‑negotiable ordering)
ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

## 🗂️ Directory Layout

### Related repository paths (orientation)
| Area | Canonical path | Notes |
|---|---|---|
| Pipelines | `src/pipelines/` | ETL, transforms, catalog build, graph build helpers |
| Graph | `src/graph/` | Ontology bindings, migrations, constraints, graph build |
| APIs / server | `src/server/` | Contracted access layer (REST/GraphQL); redaction + audit |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/telemetry/etc.) |
| Data (inputs/outputs) | `data/` | raw/work/processed/stac organization per domain |
| Docs | `docs/` | Master guide, subsystem docs, templates |
| UI | `web/` | React + map clients (MapLibre or equivalent) |
| Tests | `tests/` | Unit/integration/contract tests |

### Expected file tree for this sub-area
~~~text
📁 src/
├── 📄 README.md
├── 📁 pipelines/
│   ├── 📁 etl/
│   ├── 📁 catalog/
│   └── 📄 README.md   (optional, subsystem-specific)
├── 📁 graph/
│   ├── 📁 ontology/
│   ├── 📁 migrations/
│   ├── 📁 build/
│   └── 📄 README.md   (optional, subsystem-specific)
└── 📁 server/
    ├── 📁 routes/
    ├── 📁 middleware/
    ├── 📁 contracts/
    └── 📄 README.md   (optional, subsystem-specific)
~~~

## 🧭 Context

### Background
KFM is a governed geospatial + historical knowledge system. `src/` is where the code that enforces the system’s ordering, standards compliance, and contract boundaries lives.

### Assumptions
- Catalogs (STAC/DCAT/PROV) are the **interface between ETL outputs and graph ingestion**.
- The API layer is the **only supported boundary** for UI access to graph-backed data.

### Constraints / invariants
- The canonical ordering is preserved: **ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs (**no direct graph dependency**).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical “layer registry” file path for the current UI stack? | TBD | TBD |
| What command(s) are the single source of truth for running schema + contract validation? | TBD | TBD |

### Future extensions
- Additional pipeline modules for new data domains (with accompanying schema + catalog mappings).
- New graph entity types/relations (with explicit provenance, migration plan, and API support).
- New API endpoints that feed Focus Mode, with contract tests and sensitivity handling.

## 🗺️ Diagrams

### System / dataflow diagram (how `src/` fits)
~~~mermaid
flowchart LR
  subgraph Data
    A["Raw Sources (data/raw, data/sources)"] --> B["ETL + Normalization (src/pipelines)"]
    B --> C["Catalogs: STAC/DCAT/PROV (data/stac, data/catalog/dcat, data/prov)"]
  end

  C --> D["Neo4j Graph Build (src/graph)"]
  D --> E["APIs / Contracts (src/server)"]
  E --> F["React/Map UI (web/)"]
  F --> G["Story Nodes (docs/reports/.../story_nodes + graph)"]
  G --> H["Focus Mode (UI view + provenance-linked bundles)"]
~~~

### Optional: sequence diagram (Focus Mode fetch)
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs (with redaction rules)
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs (typical)
| Input | Format | Where from | Validation |
|---|---|---|---|
| Raw sources | mixed | `data/raw/` or `data/sources/` | checksums + type validators |
| Pipeline configs | yaml/json | `src/pipelines/**` or `docs/**` | schema + lint |
| Schemas | json | `schemas/` | JSON schema validation |

### Outputs (typical)
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| ETL outputs | mixed | `data/work/` / `data/processed/` | domain-specific schema |
| STAC catalogs | json | `data/stac/collections/`, `data/stac/items/` | STAC profile + schema |
| DCAT catalog | json/turtle | `data/catalog/dcat/` | DCAT profile + schema |
| PROV bundles | json/turtle | `data/prov/` | PROV profile + schema |
| API payloads | json | served from `src/server/` | OpenAPI/GraphQL + tests |

### Sensitivity & redaction
- If inputs/outputs include sensitive locations, apply governance-defined generalization/redaction before exposure.
- Sensitivity classifications should be reflected in catalog metadata and enforced in API responses.

### Quality signals
- Geometry validity, temporal coverage, completeness, schema conformance, provenance completeness.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: TBD
- Items involved: TBD
- Extension(s): TBD

### DCAT
- Dataset identifiers: TBD
- License mapping: TBD
- Contact / publisher mapping: TBD

### PROV‑O
- `prov:wasDerivedFrom`: source IDs (STAC/DCAT identifiers)
- `prov:wasGeneratedBy`: pipeline activity/run IDs
- Activity / Agent identities: pipeline module + operator IDs

### Versioning
- Use STAC versioning links and graph predecessor/successor relationships as applicable.

## 🧱 Architecture

### Components (what `src/` implements)
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV generation | JSON + validators |
| Graph | Neo4j build + ontology bindings | Cypher + API layer |
| APIs | Serve contracts + enforce redaction | REST/GraphQL |
| UI (external to `src/`) | Map + narrative | API calls |
| Story Nodes (external to `src/`) | Curated narrative artifacts | Graph + docs |
| Focus Mode (external to `src/`) | Contextual synthesis | Provenance‑linked bundles |

### Interfaces / contracts (do-not-break)
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Catalog profiles | `docs/data/` (and/or `schemas/`) | Profile bump when breaking |
| Graph constraints/migrations | `src/graph/` + docs | Stable labels/edges unless migrated |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/.`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How code changes in `src/` surface in Focus Mode
- API endpoints may feed Focus Mode context bundles.
- Graph changes can add/remove focusable entities and relationships.
- Pipeline changes can create new evidence assets (STAC items) used in story nodes.

### Provenance‑linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- Predictive content (if any) must be opt‑in and carry uncertainty/confidence metadata.

### Optional structured controls (example)
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps (minimum)
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV and other JSON schemas)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- New sensitive layers
- New AI narrative behaviors
- New external data sources
- New public-facing endpoints

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.
- Apply generalization/redaction to restricted locations as required by governance.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions match intended use.
- Do not imply prohibited actions (e.g., inferring sensitive locations).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `src/` README (governed) | TBD |

---
Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`