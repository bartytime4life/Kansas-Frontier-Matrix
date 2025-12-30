---
title: "Repro Kit — Docker Environment"
path: ".github/repro-kit/env/docker/README.md"
version: "v0.1.0"
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
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:repro-kit:env:docker:readme:v0.1.0"
semantic_document_id: "kfm-repro-kit-docker-env-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:repro-kit:env:docker:readme:v0.1.0"
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

# Repro Kit — Docker Environment

## 📘 Overview

### Purpose

- Provide a deterministic, containerized environment for running Kansas Frontier Matrix (KFM) pipelines, validators, and tests locally and in CI.
- Reduce “works on my machine” drift by standardizing execution inputs (pinned dependencies, stable IDs, repeatable validation steps) and capturing provenance for every run.

### Scope

| In Scope | Out of Scope |
|---|---|
| Local/CI execution of ETL + catalog generation + validation in a consistent container environment | Production deployment / uptime / scaling |
| Repeatable gates: schema validation (STAC/DCAT/PROV), tests, doc lint, provenance-link checks | Managing real secrets (use secrets tooling in CI; do not bake into images) |
| Optional: standing services used by the pipeline (e.g., Neo4j) for integration tests | GPU acceleration and performance tuning (unless explicitly added later) |
| Writing artifacts to canonical repo locations (`data/**`, `mcp/runs/**`) | Publishing outputs to external registries (handled elsewhere) |

### Audience

- Primary: contributors and CI maintainers who need “one-step reproduction” of runs.
- Secondary: domain stewards/reviewers validating that changes are deterministic and governed.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo; add if missing)*
- Terms used in this doc:
  - **Repro Kit**: a constrained, repeatable environment and workflow for reproducing KFM outputs.
  - **Runner**: the container/service that executes pipelines, validators, and tests.
  - **Run ID**: a stable identifier used to group logs + provenance outputs for a single execution (recommended).
  - **Stateful services**: databases/graph stores used in integration tests (e.g., Neo4j).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/repro-kit/env/docker/README.md` | Docs/CI | Runbook for the Docker repro environment |
| Docker Compose file | `.github/repro-kit/env/docker/docker-compose.yml` | CI | **Recommended**; *not confirmed in repo* |
| Runner image definition | `.github/repro-kit/env/docker/Dockerfile` | CI | **Recommended**; *not confirmed in repo* |
| Environment defaults | `.github/repro-kit/env/docker/.env.example` | CI | **Recommended**; never commit real secrets |
| Run artifacts | `mcp/runs/<run_id>/...` | CI/MCP | Recommended location for logs/manifests |
| Catalog outputs | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | Data Eng | Canonical output paths |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] All referenced repo paths are canonical (no “shadow” homes)
- [ ] Commands are repeatable and do not require hidden state
- [ ] Validation steps listed and aligned to v12 minimum CI gates
- [ ] Governance + CARE/sovereignty considerations explicitly stated (even if “N/A”)

## 🗂️ Directory Layout

### This document

- `path`: `.github/repro-kit/env/docker/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI / policy gates | `.github/` | Workflows, reusable actions, security/policy checks |
| Data lifecycle | `data/` | `raw/`, `work/`, `processed/`, plus `stac/`, `catalog/dcat/`, `prov/` outputs |
| Documentation | `docs/` | Canonical governed docs (guides, designs, domain notes) |
| Templates | `docs/templates/` | Universal/Story/API templates |
| Schemas | `schemas/` | JSON schemas for STAC/DCAT/PROV/story/ui/telemetry |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | API service + contracts + redaction logic |
| UI | `web/` | React + map client + Focus Mode UI |
| Tests | `tests/` | Unit + integration tests |
| Tools | `tools/` | Validators/utilities/QA scripts |
| MCP runs | `mcp/` | `runs/` and `experiments/` (repro artifacts, model cards, SOPs) |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 repro-kit/
    └── 📁 env/
        └── 📁 docker/
            ├── 📄 README.md
            ├── 📄 docker-compose.yml                 # recommended (not confirmed in repo)
            ├── 📄 Dockerfile                         # recommended (not confirmed in repo)
            ├── 📄 .env.example                       # recommended (not confirmed in repo)
            ├── 📁 scripts/                           # recommended (not confirmed in repo)
            │   ├── 📄 up.sh
            │   ├── 📄 down.sh
            │   ├── 📄 validate.sh
            │   └── 📄 smoke-test.sh
            └── 📁 volumes/                           # optional (do not commit sensitive data)
                └── 📄 .gitkeep
~~~

## 🧭 Context

### Background

- KFM’s core expectation is a **deterministic pipeline** and **contract-first** development: schemas and API contracts are first-class artifacts, and outputs must be reproducible for the same inputs.
- The design guidance for ingestion emphasizes “one-step reproduction” and recommends **containerized execution (e.g., Docker Compose)** with pinned dependencies to reduce environment drift.

### Assumptions

- Docker + Docker Compose are installed for local use (or available in CI runners).
- You are running commands from the repository root.
- The repo follows canonical homes (no direct UI → Neo4j access; all graph access via APIs).
- Any required datasets for reproduction are present under `data/raw/**` (or staged appropriately).

### Constraints / invariants

- **Canonical pipeline ordering is preserved:** ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **API boundary is enforced:** UI consumes contracts via APIs (no direct graph dependency).
- Repro runs must be **idempotent**: same inputs → identical outputs (except timestamp fields).
- Secrets must not be baked into images or committed; use `.env.example` + CI secrets.
- Outputs must land in canonical directories:
  - datasets: `data/processed/**`
  - catalogs: `data/stac/**`, `data/catalog/dcat/**`
  - provenance: `data/prov/**`
  - run artifacts: `mcp/runs/**` (recommended)

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which stateful services are required for integration tests (Neo4j only? also Postgres, etc.)? | TBD | TBD |
| Should images be pinned by digest (recommended) vs tag (convenience)? | TBD | TBD |
| Do we support ARM/Apple Silicon builds for contributors? | TBD | TBD |
| Standard run manifest schema for `mcp/runs/<run_id>/manifest.json`? | TBD | TBD |

### Future extensions

- Add a Dev Container / Codespaces profile reusing the same Dockerfile/Compose.
- Add a CI matrix for Linux/ARM (where feasible).
- Add artifact caching (pip/npm) while preserving determinism guarantees.
- Add signed SBOM generation for the runner image (supply-chain hardening).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  Host[Repo checkout<br/>code + data volumes] --> Runner[Runner<br/>(ETL + validators + tests)]
  Runner --> Catalogs[STAC/DCAT/PROV outputs<br/>data/stac + data/catalog/dcat + data/prov]
  Catalogs --> Graph[Neo4j Graph<br/>(optional service for integration)]
  Graph --> API[API boundary<br/>(src/server)]
  API --> UI[UI<br/>(web/ React + Map)]
  UI --> Story[Story Nodes<br/>(docs/reports/story_nodes)]
  Story --> Focus[Focus Mode<br/>(provenance-linked only)]
~~~  

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph

  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Repo source | Git checkout | CI or local | commit SHA + clean tree |
| Raw datasets | varies | `data/raw/<domain>/...` | checksums (recommended) + domain validators |
| Schemas | JSON Schema | `schemas/**` | schema lint + semver rules |
| Pipeline code | Python/Node/etc | `src/pipelines/**` | unit/integration tests |
| Runtime config | env / yaml | `.env` / config files | must not include secrets in repo |
| Graph config | env | compose + `.env` | connectivity + constraints checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Processed datasets | CSV/GeoJSON/Parquet/etc | `data/processed/<domain>/...` | domain schema + quality checks |
| STAC catalogs | JSON | `data/stac/**` | STAC + KFM-STAC profile |
| DCAT catalogs | JSON-LD/RDF/etc | `data/catalog/dcat/**` | DCAT + KFM-DCAT profile |
| Provenance | JSON-LD/RDF/etc | `data/prov/**` | PROV-O + KFM-PROV profile |
| Run logs + manifests | JSON/text | `mcp/runs/<run_id>/...` | repo-defined (recommended) |

### Sensitivity & redaction

- Do not mount or publish restricted datasets without approved governance.
- If outputs require generalization (e.g., geometry simplification), ensure redaction is applied consistently:
  - in processed outputs (`data/processed/**`),
  - in catalogs (STAC/DCAT fields),
  - in API responses (redaction policies),
  - and in UI rendering (CARE gating).

### Quality signals

- Bit-for-bit reproducible outputs for identical inputs (except timestamp fields).
- All catalogs validate against schemas (STAC/DCAT/PROV).
- Graph integrity checks pass (constraints + expected labels/edges).
- API contract tests pass.
- No secrets/PII/sensitive-location leakage detected by CI scans.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: `data/stac/collections/**`
- Items involved: `data/stac/items/**`
- Extension(s): repo-defined KFM STAC profile (`KFM-STAC v11.0.0`)

### DCAT

- Dataset identifiers: `data/catalog/dcat/**`
- License mapping: must match dataset license terms
- Publisher/contact mapping: repo-defined (do not invent without governance review)

### PROV-O

- `prov:wasDerivedFrom`: raw inputs (`data/raw/**`) → processed outputs (`data/processed/**`)
- `prov:wasGeneratedBy`: pipeline activity for the run (recommend a stable `run_id`)
- Activity / Agent identities: include pipeline script version + container image reference (tag/digest)

### Versioning

- Record the runner image version and the repo commit SHA in run manifests; use predecessor/successor links (as applicable) for datasets and catalogs.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Repro kit (Compose) | Orchestrate runner + optional services | `docker compose -f ...` |
| Runner | Execute ETL, catalog builds, validators, tests | CLI entrypoints + mounted volumes |
| Catalog outputs | Emit STAC/DCAT/PROV artifacts | File system (`data/**`) |
| Graph service (optional) | Provide Neo4j for integration tests | Bolt/HTTP (ports repo-defined) |
| API service (optional) | Serve contracted endpoints | REST/GraphQL (repo-defined) |
| UI service (optional) | Local UI smoke tests | HTTP (repo-defined) |
| Run artifacts | Store logs/manifests/provenance bundles | `mcp/runs/**` (recommended) |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Docker environment contract | `.github/repro-kit/env/docker/docker-compose.yml` | Treat as semver; breaking changes require version bump |
| Runner build spec | `.github/repro-kit/env/docker/Dockerfile` | Pin base versions; prefer digests for determinism |
| JSON schemas | `schemas/` | Semver + changelog; validate in CI |
| API schemas | `src/server/` + docs | Contract tests required; breaking changes versioned |
| UI registries/schemas | `web/` | Schema-validated; no hidden data leakage |

### Extension points checklist (for future work)

- [ ] Docker: add new service with explicit ports/volumes and security notes
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- This repro environment enables consistent local/CI verification that Focus Mode consumes only provenance-linked context bundles.
- It does not define narratives; it ensures pipelines/validators can build and verify the evidence artifacts that narratives reference.

### Provenance-linked narrative rule

- Every claim must trace to a dataset / record / asset ID (and be reachable via catalogs and provenance records).

### Optional structured controls

~~~yaml
# This runbook does not define Focus Mode behavior.
# Keep as a placeholder for future “repro focus bundle” automation if adopted.

focus_layers: []
focus_time: "N/A"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (front-matter + required sections)
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks (if graph build/test runs here)
- [ ] API contract tests (if API service is included)
- [ ] UI schema checks (layer registry / a11y gates, if present)
- [ ] Security and sovereignty checks (as applicable): secret/PII scans, sensitive-location leakage, classification propagation

### Reproduction

~~~bash
# Run from repo root.
# Example placeholders — replace service names/paths with repo-specific ones.

COMPOSE_FILE=".github/repro-kit/env/docker/docker-compose.yml"

# 0) Build the runner (and any services) deterministically
docker compose -f "${COMPOSE_FILE}" build

# 1) Start stateful services (if any; e.g., graph DB)
docker compose -f "${COMPOSE_FILE}" up -d

# 2) Validate catalogs/schemas (example placeholder)
docker compose -f "${COMPOSE_FILE}" run --rm runner ./scripts/validate_all_catalogs.sh

# 3) Run unit/integration tests (example placeholder)
docker compose -f "${COMPOSE_FILE}" run --rm runner pytest -q

# 4) Lint/verify docs + provenance links (example placeholder)
docker compose -f "${COMPOSE_FILE}" run --rm runner \
  bash -lc "markdownlint docs/ && ./scripts/check_provenance_links.py"

# 5) Tear down (optionally remove volumes)
docker compose -f "${COMPOSE_FILE}" down -v
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| `repro_run_started` | runner | `mcp/runs/<run_id>/run.json` (recommended) |
| `container_image_ref` | runner | `mcp/runs/<run_id>/manifest.json` (recommended) |
| `catalog_validation_status` | validators | `mcp/runs/<run_id>/validation.json` (recommended) |
| `classification_assigned` | ingest/scan | `mcp/runs/<run_id>/signals.json` (recommended) |
| `redaction_applied` | processing | `mcp/runs/<run_id>/signals.json` (recommended) |

## ⚖ FAIR+CARE & Governance

### Review gates

- Routine changes (non-sensitive pipelines/docs): standard code review + domain steward review.
- Higher-risk changes require governance sign-off:
  - new sensitive datasets or sovereignty-impacted content,
  - new AI narrative behaviors that could be interpreted as “fact,”
  - new external data sources (license/provenance review),
  - any classification/sensitivity change, or publication derived from restricted inputs.

### CARE / sovereignty considerations

- Treat culturally sensitive content as high-risk by default.
- Ensure redaction/generalization is enforced end-to-end (data → catalogs → API → UI) before any public release.
- Avoid embedding sensitive sample data into images or committed volumes.

### AI usage constraints

- This document permits non-policy transformations like `summarize` and `structure_extract`.
- Prohibited: generating governance policy text, or inferring sensitive locations from data/context.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-30 | Initial Docker repro environment README | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

