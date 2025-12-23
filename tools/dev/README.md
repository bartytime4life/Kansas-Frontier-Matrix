---
title: "KFM — Dev Tooling Guide (tools/dev/)"
path: "tools/dev/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:tools:dev-readme:v1.0.0"
semantic_document_id: "kfm-tools-dev-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:dev-readme:v1.0.0"
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

# KFM Dev Tooling (`tools/dev/`)

## 📘 Overview

### Purpose

- Provide a **single, predictable home** for developer-focused helpers that make it easier to work on KFM locally:
  - validation (schemas, docs, contracts),
  - repeatable “run this stage” wrappers,
  - developer-only bootstrap tooling.
- Keep dev tooling **separate from runtime subsystems** (ETL, catalogs, graph, API, UI) while still supporting the canonical pipeline:

  **ETL → STAC/DCAT/PROV → Neo4j graph → APIs → UI → Story Nodes → Focus Mode**

### Scope

| In Scope | Out of Scope |
|---|---|
| Local dev helpers (scripts, wrappers, small fixtures) | Production deployment + infrastructure-as-code (belongs elsewhere under `tools/` and/or an ops repo) |
| Local validation steps that mirror CI gates | Large datasets or derived products (must live under `data/…`) |
| Developer experience improvements (repeatable commands, docs) | Any tool that bypasses the API boundary (e.g., UI reading Neo4j directly) |

### Audience

- Primary: KFM developers / maintainers (data, graph, API, web)
- Secondary: Contributors running local checks before PRs

### Definitions

- Glossary: `docs/glossary.md`
- Terms used in this doc:
  - **Dev tooling**: scripts/config intended for local workflows (not production runtime).
  - **Contract artifact**: machine-validated schema/spec (JSON Schema, OpenAPI, GraphQL SDL, UI registry schema).
  - **Evidence artifact**: catalog + provenance outputs consumed downstream (STAC/DCAT/PROV and derived evidence products).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 (Draft) | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline + invariants |
| v13 Redesign Blueprint (Draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Core maintainers | Canonical repo structure direction |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Governed doc structure used here |
| Story Node Template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Maintainers | Narrative artifact structure |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] `path` in front-matter matches repository path
- [ ] Describes what belongs in `tools/dev/` vs elsewhere
- [ ] Provides a safe “recommended layout” that does not assume specific scripts exist
- [ ] Validation guidance included (with clearly labeled placeholders)

## 🗂️ Directory Layout

### This document

- `path`: `tools/dev/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Dev tooling (this area) | `tools/dev/` | Local helpers, validation wrappers, dev-only bootstrap |
| Tooling (broader) | `tools/` | Cross-cutting tooling; may include ops/deploy tooling in separate subdirs |
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Schemas | `schemas/` | JSON Schema (STAC/DCAT/PROV, storynodes, UI registry, telemetry) |
| Pipelines | `src/pipelines/` | ETL + catalog build + graph build code |
| Graph | `src/graph/` | Ontology bindings + migrations + constraints |
| API layer | `src/server/` | Contracted access layer (REST/GraphQL) |
| Frontend | `web/` | Map + Focus Mode UI (React/MapLibre/Cesium) |
| Story nodes | `docs/reports/story_nodes/` | Draft/published narratives with provenance linkage |
| Experiments/SOPs | `mcp/` | Run logs, experiment artifacts, SOPs |

### Recommended (minimal) layout for `tools/dev/`

~~~text
📁 tools/
└── 📁 dev/
    ├── 📄 README.md
    ├── 📁 scripts/        # optional — small local helpers (validation, wrappers)
    ├── 📁 docker/         # optional — dev-only compose fragments / service stubs
    └── 📁 fixtures/       # optional — tiny, non-sensitive test fixtures
~~~

## 🧭 Context

### Why `tools/dev/` exists

KFM is a contract-first, evidence-first system. Local developer workflows should make it easy to:

- run validations early (before CI),
- keep pipelines deterministic and replayable,
- preserve boundaries:
  - **UI does not read Neo4j directly** (contracts live at the API layer),
  - catalogs are machine-validated (STAC/DCAT/PROV),
  - story outputs must avoid unsourced narrative in Focus Mode contexts.

### What belongs here (guiding rules)

- ✅ Small, composable helpers that:
  - validate schema outputs,
  - run doc checks,
  - run unit/integration tests,
  - spin up dev-only services (if applicable) without embedding secrets.
- ❌ Anything that:
  - writes to `src/` with generated data,
  - stores derived datasets outside `data/processed/`,
  - embeds credentials, tokens, or PII,
  - shortcuts the API boundary.

### Conventions for new dev tools

- **Idempotent**: safe to re-run without requiring manual cleanup.
- **Deterministic outputs**: stable file ordering, stable IDs where applicable.
- **Controlled writes**:
  - write outputs to `mcp/runs/…` (logs) or to explicit `data/…` staging paths (pipeline artifacts),
  - avoid scattering outputs across the repo root.
- **Document the contract**: any script that produces artifacts should document:
  - inputs, outputs, validation rules, and where outputs live.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  Dev[Developer] --> Tools[tools/dev/ helpers]
  Tools --> Validate[Validate: docs + schemas + tests]
  Validate --> RunStage[Run stage: ETL / Catalog / Graph / API / UI]
  RunStage --> Artifacts[Artifacts: data/ + schemas/ + docs/ + web/]
  Artifacts --> PR[PR + CI gates]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Local config | env / yaml / json | developer machine | lint + schema checks (if applicable) |
| Schemas | JSON Schema | `schemas/` | schema validators |
| Docs | Markdown | repo | markdown protocol validation |
| Test fixtures (optional) | files | `tools/dev/fixtures/` | keep minimal + non-sensitive |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Local logs (optional) | text/json | `mcp/runs/…` (recommended) | N/A |
| Validation reports (optional) | json/md | `mcp/runs/…` or `data/reports/…` | N/A |
| Build artifacts (dev-only) | varies | dev temp dirs | N/A |

### Sensitivity & redaction

- Do not place sensitive data (PII, culturally sensitive locations, credentials) in `tools/dev/fixtures/`.
- Prefer **synthetic or minimized** fixtures that are safe to publish.

### Quality signals

- Scripts should fail fast with clear error messages.
- Prefer machine-readable outputs for validators when feasible (JSON reports).

## 🌐 STAC, DCAT & PROV Alignment

Dev tooling may include helpers to validate or regenerate:

- STAC collections/items under `data/stac/…`
- DCAT views under `data/catalog/dcat/…`
- PROV bundles under `data/prov/…`

Any validator wrapper should:
- run schema validation,
- run integrity checks (link resolution, item↔collection consistency),
- produce a reproducible report/log.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Dev scripts | Convenience wrappers for local work | CLI scripts under `tools/dev/scripts/` |
| Validators | Mirror CI checks locally | schemas + docs + tests |
| Dev-only stack helpers | Optional local services | docker-compose fragments, local configs |
| Fixtures | Minimal reproducible inputs | small, non-sensitive files |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | SemVer + changelog where applicable |
| API schemas | `src/server/` + docs | contract tests required |
| UI registries | `web/…` | schema-validated |

### Extension points checklist (for future work)

- [ ] Add a validator wrapper for STAC/DCAT/PROV outputs
- [ ] Add a local doc/protocol linter wrapper
- [ ] Add a single “dev quickcheck” wrapper that runs the subset of CI checks feasible locally
- [ ] Ensure all scripts document inputs/outputs + safe paths

## 🧠 Story Node & Focus Mode Integration

Dev tooling can support story workflows by providing local checks that help enforce:

- provenance-linked narrative rules (no unsourced claims),
- schema validation for story node front-matter (if schema exists),
- link checks for dataset/document IDs referenced from narratives.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (governed docs)
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks (constraints/migrations, if runnable locally)
- [ ] API contract tests (OpenAPI/GraphQL, if runnable locally)
- [ ] UI schema checks (layer registries, if applicable)
- [ ] Security + sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate schemas (STAC/DCAT/PROV)
# ./tools/dev/scripts/validate_catalogs.sh

# 2) run unit/integration tests
# ./tools/dev/scripts/test.sh

# 3) run doc lint / markdown protocol validation
# ./tools/dev/scripts/lint_docs.sh
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Dev validation run metadata | local script wrappers | `mcp/runs/…` |

## ⚖ FAIR+CARE & Governance

### Review gates

- Any change that affects governed contracts, schema profiles, or sovereignty rules should follow the repo’s review gates (see governance refs in front-matter).

### CARE / sovereignty considerations

- Tools must not infer or publish sensitive locations.
- Tools that touch culturally sensitive materials should implement redaction/generalization steps upstream (documented in the relevant domain runbooks).

### AI usage constraints

- This doc’s AI permissions/prohibitions are declared in front-matter. Do not use tooling to generate new policy.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial `tools/dev/README.md` scaffold | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`