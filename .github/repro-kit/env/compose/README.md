---
title: "Repro Kit — Docker Compose Environment"
path: ".github/repro-kit/env/compose/README.md"
version: "v1.0.0"
last_updated: "2025-12-30"
status: "draft"
doc_kind: "Runbook"
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
care_label: "public-infra"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:repro-kit:env:compose:readme:v1.0.0"
semantic_document_id: "kfm-repro-kit-compose-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:repro-kit:env:compose:readme:v1.0.0"
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

# Repro Kit — Docker Compose Environment

## 📘 Overview

### Purpose
- Provide a **deterministic, CI-parity** Docker Compose environment for running KFM’s core services locally (or in CI) to reproduce pipeline, graph, API, and UI behaviors.
- Document the **operational contract** for standing up/down the stack, wiring environment variables and volumes, and running the minimum validation gates.

### Scope

| In Scope | Out of Scope |
|---|---|
| Local + CI reproduction of the KFM stack via Docker Compose | Production deployment, scaling, and hardening |
| Bootstrapping core dependencies and running API/UI against them | Managing long-lived production data or secrets |
| Reproducing validation gates (schemas/tests/docs) that depend on the stack | Defining new governance policy |

### Audience
- Primary: Contributors debugging CI failures; maintainers of `.github/workflows/`
- Secondary: Reviewers verifying reproducibility / determinism claims; stewards running local previews

### Definitions
- Link: `docs/glossary.md`
- Terms used in this doc: Docker Compose, project directory, env file, profiles, healthcheck, idempotent run, contract tests

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This runbook | `.github/repro-kit/env/compose/README.md` | CI / DevEx | How to run this Compose repro environment |
| CI workflows | `.github/workflows/` | CI | Should reference this repro kit for CI parity |
| Pipelines | `src/pipelines/` | Data Eng | Deterministic ETL + catalog generation |
| Graph build | `src/graph/` | Graph | Neo4j ingest/migrations/live graph build |
| API boundary | `src/server/` | API | Contract-first interface; redaction rules |
| UI | `web/` | UI | React + map client; consumes APIs only |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Data Eng | Governed metadata outputs |

### Definition of done
- [ ] Front-matter complete + valid (path matches file location)
- [ ] Compose usage documented for local + CI reproduction
- [ ] Validation steps listed and repeatable (placeholders clearly marked)
- [ ] Security + sovereignty considerations explicitly stated (no secrets; no sensitive-location leakage)
- [ ] Links point to real repo paths or are explicitly marked “not confirmed in repo”

## 🗂️ Directory Layout

### This document
- `path`: `.github/repro-kit/env/compose/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI | `.github/` | Workflows + policy gates |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | API service + contracts + redaction logic |
| UI | `web/` | React + map client + Focus Mode UI |
| Data lifecycle | `data/raw/`, `data/work/`, `data/processed/` | Raw → intermediate → processed datasets |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV outputs |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 repro-kit/
    └── 📁 env/
        └── 📁 compose/
            ├── 📄 README.md
            ├── 📄 compose.yaml                      # not confirmed in repo; expected Compose entrypoint
            ├── 📄 docker-compose.yml                # not confirmed in repo; legacy alt name (if used)
            ├── 📄 compose.override.yaml             # optional; local-only overrides (do not commit secrets)
            ├── 📄 .env.example                      # optional; may delegate to repo root .env.example
            └── 📁 scripts/                          # optional helpers for CI/local parity
                ├── 📄 up.sh
                ├── 📄 down.sh
                └── 📄 wait-for-health.sh
~~~

## 🧭 Context

### Background
KFM’s architecture is intentionally modular and contract-first: ETL produces governed catalogs (STAC/DCAT/PROV), the graph layer builds a Neo4j knowledge graph from those catalogs, and the API layer is the only supported interface for the UI (no direct UI access to Neo4j). This separation enables provenance, redaction, and sovereignty checks to be enforced at the API boundary.

A Compose-based repro kit reduces “works on my machine” drift by pinning service versions and allowing contributors to reproduce CI behavior locally (including integration tests and validation gates).

### Assumptions
- Docker Engine + Compose plugin are available (`docker compose ...`).
- Service configuration is provided via an `.env` file (or explicit environment variables) rather than hard-coded secrets.
- The Compose environment is **not production** and should be safe to run on a contributor laptop.

### Constraints and invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The UI consumes only contracted APIs (no direct graph database access).
- Repro runs should be deterministic when input data and pinned dependencies are identical.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical Compose file name in this directory? | CI | TBD |
| Which services are “core” for CI parity (Graph only vs Graph + API + UI)? | CI / Maintainers | TBD |
| Does the Compose file expect paths relative to repo root or this directory? | CI / Maintainers | TBD |

### Future extensions
- Add Compose `profiles` (e.g., `core`, `ui`, `full`, `ci`) to make CI and local use explicit.
- Provide `make repro-up / repro-test / repro-down` wrappers (if Make is used in repo).

## 🗺️ Diagrams

### System and dataflow

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React and Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Compose runtime view

~~~mermaid
flowchart LR
  subgraph Compose
    N[Graph service: Neo4j]
    S[API service]
    W[Web UI service]
    T[One-off jobs: ETL and validators]
  end

  T -->|writes| CATS[data stac dcat prov]
  CATS -->|ingest| N
  S -->|drivers| N
  W -->|HTTP| S
~~~

## 🧩 Data model

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Compose config | YAML | `.github/repro-kit/env/compose/` | `docker compose config` |
| Environment configuration | `.env` / env vars | repo root and or this directory | secret scan; no committed secrets |
| Source datasets | files | `data/raw/` | dataset-level checks per pipeline |
| Derived catalogs | JSON | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | schema validation |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Running services | containers | local Docker runtime | Compose config is the contract |
| Service logs | text | docker logs | must not contain secrets |
| Derived data | files + JSON | `data/work/`, `data/processed/`, catalogs | KFM profiles + schemas |
| Test outputs | logs and artifacts | CI and or local | CI workflow contract |

### Sensitivity and redaction
- Do not mount or publish sensitive datasets in public CI contexts unless governance explicitly allows it.
- Treat location-bearing Indigenous or culturally sensitive data as high-risk by default; ensure redaction or generalization is enforced through catalogs, API responses, and UI gating.

### Quality signals
- Determinism: same raw input + pinned versions should yield identical outputs where feasible (timestamps excluded).
- Integrity: catalogs validate against schemas; provenance links resolve; graph constraints pass; API contracts pass.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections: `data/stac/collections/`
- Items: `data/stac/items/`
- Extensions: per `stac_profile` in front-matter, when relevant

### DCAT
- Dataset records: `data/catalog/dcat/`
- License mapping: governed in dataset modules and catalogs

### PROV-O
- Lineage: raw → work → processed + catalogs recorded under `data/prov/`
- Activity and Agent identities: referenced by pipeline run IDs and telemetry (if present)

### Versioning
- Prefer pinned image tags and pinned dependency versions.
- Breaking contract changes require version bumping and compatibility tests.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Compose repro kit | Orchestrate reproducible services for local and CI | `docker compose` CLI |
| ETL | Ingest + normalize | config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | drivers via API layer |
| APIs | Serve contracts + redaction | REST/GraphQL |
| UI | Map + narrative | API calls only |
| Story Nodes | Curated narrative artifacts | docs + provenance links |
| Focus Mode | Provenance-linked synthesis | context bundles |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Compose environment contract | `.github/repro-kit/env/compose/` | breaking changes require CI update |
| JSON schemas | `schemas/` | semver + changelog |
| API schemas | `src/server/` + docs | contract tests required |
| UI layer registry | `web/` | schema-validated; no leakage |

### Extension points checklist
- [ ] Add CI services as Compose profiles (avoid forcing heavy services for every run)
- [ ] Add smoke tests validating API-to-graph connectivity
- [ ] Add a seed job to load minimal fixture data for deterministic tests
- [ ] Add an opt-in UI container for visual QA on PRs

## 🧠 Story Node & Focus Mode Integration

### How this environment surfaces in Focus Mode
- Enables running the API + UI against a local graph instance with provenance-linked catalogs, so Story Nodes can be previewed with evidence-first behavior.

### Provenance-linked narrative rule
- Story content should trace to cataloged artifacts and should separate fact vs inference vs hypothesis where applicable.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Compose config renders cleanly: `docker compose config`
- [ ] Schema validation: STAC/DCAT/PROV
- [ ] Graph integrity checks (constraints, expected labels/edges)
- [ ] API contract tests (OpenAPI/GraphQL schema + resolver tests)
- [ ] UI schema checks (layer registry; accessibility)
- [ ] Security + sovereignty scanning gates (secret scan, PII scan, sensitive-location leakage checks)

### Reproduction

~~~bash
# Run from repo root unless CI uses a different working directory.

# 0) Choose the Compose file that exists in your branch:
# - compose.yaml (preferred) OR docker-compose.yml (legacy)
KFM_COMPOSE_FILE=".github/repro-kit/env/compose/compose.yaml"

# If the Compose file expects paths relative to the repo root, add:
#   --project-directory .
# If it expects paths relative to the Compose file folder, omit --project-directory.

# 1) Start the repro stack
docker compose --project-directory . -f "$KFM_COMPOSE_FILE" up -d

# 2) Tail logs for a specific service (replace <service> with an actual service name)
docker compose --project-directory . -f "$KFM_COMPOSE_FILE" logs -f <service>

# 3) Run validation gates (EXAMPLE placeholders — replace with repo-specific commands)
./scripts/validate_all_catalogs.sh
pytest -q
markdownlint docs/ && ./scripts/check_provenance_links.py

# 4) Tear down and remove volumes
docker compose --project-directory . -f "$KFM_COMPOSE_FILE" down -v
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| `catalog_published` | pipeline runs | `docs/telemetry/` + `schemas/telemetry/` |
| `classification_assigned` | governance assignment | `docs/telemetry/` |
| `redaction_applied` | API + pipeline | `docs/telemetry/` |
| `promotion_blocked` | CI gates | workflow logs and telemetry |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes to this repro kit should be reviewed by CI maintainers and, when relevant, domain stewards.
- Any change that could alter public outputs, redaction behavior, or sensitive-data handling requires governance review.

### CARE and sovereignty considerations
- Never encode sensitive locations or restricted datasets into default Compose fixtures.
- Keep fixtures minimal and synthetic unless dataset governance explicitly permits real data in CI.

### AI usage constraints
- This doc allows structural extraction and summarization but prohibits policy generation and sensitive-location inference.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-30 | Initial Compose repro kit runbook | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

