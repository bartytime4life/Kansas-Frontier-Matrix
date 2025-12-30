---
title: "KFM Repro Kit — Neo4j Environment"
path: ".github/repro-kit/env/neo4j/README.md"
version: "v1.0.0-draft"
last_updated: "2025-12-30"
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

doc_uuid: "urn:kfm:doc:repro-kit:env:neo4j:v1.0.0-draft"
semantic_document_id: "kfm-repro-kit-env-neo4j-v1.0.0-draft"
event_source_id: "ledger:kfm:doc:repro-kit:env:neo4j:v1.0.0-draft"
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

# KFM Repro Kit — Neo4j Environment

## 📘 Overview

### Purpose

Provide a **repeatable, local Neo4j environment** for the Kansas Frontier Matrix (KFM) Graph subsystem, suitable for:

- local development and debugging of graph ingest + Cypher queries
- running **graph integrity tests** in CI with a fixture dataset
- validating graph-facing API behavior without requiring a hosted database

This doc governs the **runtime contract** for a repro-friendly Neo4j instance (ports, volumes, credentials handling, and expected inputs).

### Scope

| In Scope | Out of Scope |
|---|---|
| Docker-first Neo4j runtime for dev/CI | Production Neo4j sizing, clustering, HA, and ops runbooks |
| Minimal security posture for local-only use | Public internet exposure or hosted credentials |
| Plugin guidance for KFM graph ingest/queries | Selecting or maintaining enterprise licensing |
| Graph schema hygiene guidance | Full ontology specification |

### Audience

- Primary: contributors working on `src/graph/`, `src/server/`, and test/CI validation
- Secondary: domain stewards validating ingestion outputs and provenance linkage

### Definitions

- Glossary: `docs/glossary.md`
- Terms used in this doc:
  - **Bolt**: Neo4j binary protocol on port `7687`
  - **Cypher**: Neo4j query language
  - **Fixture dataset**: small, safe dataset loaded in CI to validate constraints
  - **STAC/DCAT/PROV**: catalog + provenance outputs that feed the graph

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline + invariants | `docs/MASTER_GUIDE_v12.md` | Architecture | Pipeline ordering and CI gates |
| Ingest architecture | `docs/architecture/KFM_INGEST_ARCHITECTURE.md` | Data Engineering | Staging + catalog outputs |
| Graph ontology | `docs/graph/ontology.md` (or similar) | Graph | Not confirmed in repo: path may differ |
| Graph ingest scripts | `src/graph/ingest_stac_to_neo4j.py` (and related) | Graph | Reads STAC/DCAT/PROV and builds graph |
| Graph migrations | `src/graph/migrations/` | Graph | Cypher migrations with stable IDs |
| This environment doc | `.github/repro-kit/env/neo4j/README.md` | Repro Kit | This file |

### Definition of done

- [ ] Front-matter complete and valid
- [ ] Startup steps are repeatable on a clean machine
- [ ] No secrets are embedded in repo-tracked files
- [ ] Ports, volumes, and plugin expectations are documented
- [ ] CI-friendly “fixture load + integrity checks” workflow is described
- [ ] Governance and sovereignty constraints for data loaded into graph are stated

### What this environment supports

KFM’s non-negotiable ordering is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → UI → Story Nodes → Focus Mode**

This environment exists specifically for the **Neo4j graph** stage, and should be treated as a *derived store* rebuilt from governed catalogs.

## 🗂️ Directory Layout

### This document

- `path`: `.github/repro-kit/env/neo4j/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Repro kit envs | `.github/repro-kit/env/` | Local reproducibility environments |
| Graph build | `src/graph/` | Graph ingest + ontology bindings + migrations |
| API boundary | `src/server/` | Graph-access APIs and contracts |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Governed metadata + lineage that feed the graph |
| Test fixtures | `tests/` (and/or `data/`) | Fixture datasets and CI checks |

### Expected file tree

This sub-area is expected to remain **small and deterministic**.

~~~text
📁 .github/
└── 📁 repro-kit/
    └── 📁 env/
        └── 📁 neo4j/
            ├── 📄 README.md
            ├── 📄 docker-compose.yml            # not confirmed in repo
            ├── 📄 .env.example                  # not confirmed in repo
            └── 📁 scripts/                      # not confirmed in repo
                └── 📄 wait-for-neo4j.sh         # not confirmed in repo
~~~

## 🧭 Context

### Background

Neo4j is the central property graph store for KFM, representing **entities** (people, places, events, documents, organizations, artifacts) and their relationships, with explicit alignment to provenance and geospatial semantics.

KFM graph ingest is driven by governed outputs:

- STAC Items/Collections for assets
- DCAT dataset records for dataset discovery/grouping
- PROV JSON-LD records for lineage (activity/agent/output)

### Assumptions

- Contributors have Docker and Docker Compose available.
- This environment is for **local-only** or **CI** use.
- The UI never talks to Neo4j directly; it goes through APIs.

### Constraints and invariants

- Preserve ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**
- Enforce the API boundary: **no direct Neo4j access from the frontend**
- Favor determinism:
  - pinned container image versions in committed compose files
  - stable IDs for entities
  - idempotent ingest scripts

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which Neo4j image tag is pinned for KFM CI? | TBD | TBD |
| Which plugins are required by default for ingest and validation? | TBD | TBD |
| Where is the canonical fixture dataset located? | TBD | TBD |

### Future extensions

- Add a small fixture dataset with explicit licensing and redaction metadata.
- Add scripted “smoke test” Cypher queries to validate labels, constraints, and provenance linkage.

## 🗺️ Diagrams

### System dataflow

~~~mermaid
flowchart LR
  A[ETL pipelines] --> B[STAC/DCAT/PROV catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional sequence

~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph as Neo4j
  UI->>API: Focus query(entity_id)
  API->>Neo4j: fetch subgraph + provenance refs
  Neo4j-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC Items/Collections | JSON | `data/stac/` | STAC profile schema validation |
| DCAT dataset records | JSON/RDF | `data/catalog/dcat/` | DCAT profile validation |
| PROV activity records | JSON-LD | `data/prov/` | PROV profile validation |
| Graph constraints/migrations | Cypher | `src/graph/` | Graph integrity tests |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Neo4j database store | Neo4j store | Docker volume | Graph ontology + constraints |
| Graph integrity signals | logs / test output | CI artifacts | CI gates |
| Provenance-linked subgraphs | Cypher results | API responses | API contracts |

### Sensitivity and redaction

- Do not load restricted or sensitive raw datasets into this local graph unless governance allows it.
- Use fixture datasets that are already **redacted/generalized** and carry classification metadata.
- Any redaction method must be reflected in:
  - datasets (`data/processed/**`)
  - catalogs (STAC/DCAT)
  - API responses (redaction rules)
  - UI affordances (CARE gating)

### Quality signals

Recommended checks:

- required properties exist on required labels (e.g., `Person.name`)
- stable IDs are unique
- provenance links exist for derived entities (`DERIVED_FROM` and `WAS_GENERATED_BY` patterns)
- no orphaned nodes for governed entity types

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Graph ingest should preserve STAC identifiers and link graph entities back to STAC Items.
- A single STAC Item may materialize as multiple graph nodes (e.g., `Document`, `Place`, `Event`) when appropriate.

### DCAT

- DCAT dataset records should map to dataset-level graph constructs:
  - grouping nodes (e.g., `Dataset`)
  - annotations/relationships that connect related STAC Items and their derived entities

### PROV-O

- PROV records should be represented in the graph as:
  - `Activity` and `Agent` nodes
  - edges linking generated entities to inputs and activities (lineage)

### Versioning

- Dataset versions should link predecessor/successor in metadata.
- The graph should mirror version relationships so users can trace evolution across time.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Neo4j container | Store/query property graph | Bolt + HTTP |
| Graph ingest | Load STAC/DCAT/PROV into graph | Neo4j driver + Cypher |
| Graph migrations | Evolve schema safely | Cypher scripts |
| APIs | Contracted access to graph | REST/GraphQL |
| CI harness | Validate graph constraints | fixture load + Cypher tests |

### Neo4j runtime contract

Baseline expectations for a local repro instance:

- Ports:
  - HTTP UI: `7474`
  - Bolt: `7687`
- Storage:
  - persistent Docker volume for the DB store
  - optional bind mounts for import/export
- Security:
  - credentials provided via environment variables or untracked `.env`
  - bind to localhost unless explicitly needed for CI containers

### Example docker-compose service

Use placeholders below; choose pinned versions per repo policy.

~~~yaml
services:
  neo4j:
    image: neo4j:<pin-version-here>
    container_name: kfm-neo4j
    ports:
      - "7474:7474"
      - "7687:7687"
    environment:
      - NEO4J_AUTH=neo4j/${NEO4J_PASSWORD}
    volumes:
      - neo4j_data:/data
      - neo4j_logs:/logs
volumes:
  neo4j_data:
  neo4j_logs:
~~~

### Plugins

Common KFM-relevant plugin categories include:

- **APOC** for utility procedures during ingest (merging, transforms)
- **n10s (Neosemantics)** if round-tripping RDF and PROV-O mappings is required

Treat plugins as part of the environment contract:

- document exactly which plugins are required
- pin plugin versions where possible
- avoid enabling unrestricted procedures in shared environments unless reviewed

### Constraints and migrations

- Treat the graph schema like a codebase.
- When adding labels/properties/relationships:
  - update the ontology documentation
  - add a migration in `src/graph/migrations/` with a stable ID
  - update graph integrity tests to reflect the new constraints

Example constraint pattern:

~~~cypher
CREATE CONSTRAINT kfm_entity_id_unique IF NOT EXISTS
FOR (n:Entity)
REQUIRE n.id IS UNIQUE;
~~~

## 🧪 Validation & CI/CD

### Local smoke test

1) Start Neo4j

~~~bash
docker compose up -d neo4j
~~~

2) Confirm it is reachable

~~~bash
curl -I http://localhost:7474
docker exec -it kfm-neo4j cypher-shell -u neo4j -p "$NEO4J_PASSWORD" "RETURN 1 AS ok;"
~~~

### Fixture load and integrity checks

CI should:

1) Start Neo4j  
2) Load a **small fixture dataset** via ingest scripts  
3) Run Cypher queries/tests that validate:
   - constraints (uniqueness, required properties)
   - expected labels and relationship types
   - provenance links (Activity/Agent where required)

### Other CI gates

KFM contributions are expected to pass:

- markdown protocol validation (front-matter + required sections)
- link/reference checks
- STAC/DCAT/PROV schema validation
- API contract tests
- security and sovereignty scanning gates (secrets, PII, sensitive-location leakage)

## ⚖ FAIR+CARE & Governance

### Review gates

Changes that affect this environment may require governance review when they:

- enable new plugins/procedures that expand data access
- alter redaction/classification behavior in ingest or APIs
- introduce new external datasets or change licenses/provenance assumptions
- risk exposing sensitive locations via ports, logging, or exports

### CARE and sovereignty considerations

- Default to fixture datasets that are safe for public/dev use.
- If a dataset is sensitive or sovereign:
  - do not store it in repro-kit defaults
  - document handling rules and enforce redaction/generalization upstream
  - propagate classification through catalogs, graph, APIs, and UI

### AI usage constraints

This doc is governed by front-matter AI permissions/prohibitions. In particular:

- do not infer or reveal sensitive locations
- do not introduce new policy text in generated outputs

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0-draft | 2025-12-30 | Initial Neo4j repro environment README | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

