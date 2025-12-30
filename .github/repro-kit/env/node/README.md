---
title: "KFM Repro Kit — Node Environment"
path: ".github/repro-kit/env/node/README.md"
version: "v1.0.0"
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

doc_uuid: "urn:kfm:doc:repro-kit:env:node:v1.0.0"
semantic_document_id: "kfm-repro-kit-env-node-v1.0.0"
event_source_id: "ledger:kfm:doc:repro-kit:env:node:v1.0.0"
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

# KFM Repro Kit — Node Environment

## 📘 Overview

### Purpose

- Provide a reproducible Node.js environment definition for KFM contributors and CI workflows.
- Ensure deterministic installs/builds for Node-based parts of the system, with primary focus on the UI in `web/`.

### Scope

| In Scope | Out of Scope |
|---|---|
| Node runtime selection and pinning | Python tooling and environments |
| Package manager and lockfile policy | Infrastructure provisioning (cloud, k8s, etc.) |
| Deterministic install/build/test steps | Neo4j operations and graph ingestion |
| CI caching guidance for Node dependencies | Dataset ingestion and catalog generation |
| Handling environment variables and secrets safely | Story Node authoring guidance (see Story templates) |

### Audience

- Primary: UI engineers, CI maintainers, and contributors running Node tooling locally.
- Secondary: API engineers when Node tooling is used for contract validation or UI build integration.

### Definitions

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Lockfile**: A dependency resolution snapshot (e.g., `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`).
  - **Frozen install**: An install that fails if the lockfile and requested dependencies disagree.
  - **Corepack**: Node’s package-manager shim used to pin `pnpm`/`yarn` versions when those are used.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline and repo layout |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Structure used by this README |
| CI workflows | `.github/workflows/` | CI | Node setup typically lives here |
| UI source | `web/` | UI | React and map UI implementation |
| Repro Kit | `.github/repro-kit/` | CI | Reproducible environment runbooks |
| Node reference (project file) | `NodeJSNotesForProfessionals.pdf` | TBD | Reference only; repo placement not confirmed |
| Git reference (project file) | `GitNotesForProfessionals.pdf` | TBD | Reference only; repo placement not confirmed |

### Definition of done

- [ ] Front-matter complete and `path` matches the file location
- [ ] Node version selection is documented and enforced in CI
- [ ] Lockfile strategy is documented and CI uses a frozen install
- [ ] Reproduction steps work on a clean checkout
- [ ] Security guidance covers secrets and build artifact handling

## 🗂️ Directory Layout

### This document

- `path`: `.github/repro-kit/env/node/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI | `.github/` | Workflows and policy gates |
| UI | `web/` | React and map client (Node-built) |
| API boundary | `src/server/` | API service plus contracts and redaction logic |
| Graph | `src/graph/` | Ontology bindings and graph build/migrations |
| Pipelines | `src/pipelines/` | ETL, catalogs, transforms |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 repro-kit/
    └── 📁 env/
        └── 📁 node/
            └── 📄 README.md
~~~

## 🧭 Context

### Background

- KFM’s UI is built as a separate subsystem (`web/`) and must be reproducible in CI and on contributor machines.
- Deterministic builds require pinned runtime versions and frozen dependency installs so behavior does not drift between runs.

### Assumptions

- The repository contains at least one Node project (commonly `web/`) with a lockfile.
- CI executes Node-based steps (install, lint/test/build, and optionally contract/schema checks).

### Constraints / invariants

- The canonical pipeline ordering is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- The UI never reads Neo4j directly; it only calls contracted APIs.
- Builds must not embed restricted data into static bundles. All sensitive access is gated at the API and UI layer.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which package manager is canonical (npm, pnpm, yarn)? | TBD | TBD |
| Where is the Node version pinned (`.nvmrc`, `package.json#engines`, other)? | TBD | TBD |
| What is the UI build output dir (`dist/`, `build/`, etc.)? | TBD | TBD |
| Do we generate SBOM/attestations for Node artifacts in CI? | TBD | TBD |

### Future extensions

- Add sibling env runbooks (e.g., `.github/repro-kit/env/python/`) as needed.
- Add a small script to emit an environment fingerprint into `mcp/runs/<run_id>/...` for reproducibility.
- Add a containerized Node build image if CI/runtime drift becomes a recurring issue.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[UI built with Node]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Sequence diagram

~~~mermaid
sequenceDiagram
  participant Dev as Dev/CI (Node env)
  participant UI as UI (web/)
  participant API as API layer
  participant Graph as Graph/Catalog refs

  Dev->>UI: install + build + test
  UI->>API: fetch contracted data + narratives
  API->>Graph: query graph + catalog references
  Graph-->>API: context bundle (with provenance refs)
  API-->>UI: renderable payload (with redaction/audit flags)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| UI source | JS/TS | `web/` | lint/test/typecheck (repo-defined) |
| Dependency manifest | `package.json` | Node project root (e.g., `web/`) | package manager validation |
| Lockfile | JSON/YAML | Node project root | frozen install required |
| Runtime version spec | text/json | `.nvmrc` / `package.json#engines` / tool config | CI must enforce |
| Environment variables | `.env` / CI vars | developer machine plus CI secrets | do not commit secrets |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Build artifacts | static files | `web/<build-output>/` | UI deployment contract (repo-defined) |
| Dependency tree | directory | `node_modules/` | local/CI only (never committed) |
| Test/lint reports | text/json | CI artifacts | CI policy gates (repo-defined) |
| Environment fingerprint | json | `mcp/runs/<run_id>/env/node.json` | proposed (not confirmed in repo) |

### Sensitivity & redaction

- Treat `.env` files, API keys, tokens, and any credentials as secrets. Do not commit them.
- CI logs should avoid printing environment variables or full request payloads.
- If the UI is statically deployed, ensure runtime data access is via APIs that enforce redaction and classification rules.

### Quality signals

- Lockfile present and unchanged during CI.
- Frozen installs enforced (CI fails if lockfile drift occurs).
- Lint, tests, typecheck, and build complete without warnings that indicate nondeterminism.
- Dependency vulnerability checks run according to repo policy.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- This Node environment guide does not define STAC artifacts.
- UI code should treat STAC IDs and asset URLs as boundary artifacts served via APIs, not embed raw datasets into bundles.

### DCAT

- This Node environment guide does not define DCAT artifacts.
- UI views should surface DCAT dataset metadata via APIs to support discovery and provenance display.

### PROV-O

- This Node environment guide does not define PROV bundles.
- Build/run provenance for UI artifacts can be captured in CI as run metadata (recommended), but is not required by this doc.

### Versioning

- Node dependencies are versioned via lockfiles; changes should be reviewed as carefully as schema/API changes.
- When UI behavior changes, ensure any contract implications are captured via API contract tests.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest and normalize | Config plus run logs |
| Catalogs | STAC/DCAT/PROV | JSON plus validator |
| Graph | Neo4j | Cypher plus API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map and narrative | API calls |
| Story Nodes | Curated narrative | Graph plus docs |
| Focus Mode | Contextual synthesis | Provenance-linked |
| Node env | Build and test UI/tooling | package manager plus CI |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver plus changelog |
| API schemas | `src/server/` plus docs | Contract tests required |
| UI layer registry | `web/` | Schema-validated (if registry exists) |
| Node runtime and deps | lockfile plus version pin | Changes must be reviewed; CI enforces |

### Extension points checklist

- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection plus item schema validation
- [ ] PROV: activity plus agent identifiers recorded
- [ ] Graph: new labels/relations mapped plus migration plan
- [ ] APIs: contract version bump plus tests
- [ ] UI: layer registry entry plus access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals plus schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Node tooling enables the UI to render Story Nodes and Focus Mode panels.
- Any UI change that alters how citations/provenance are displayed should be treated as a governed change.

### Provenance-linked narrative rule

- Every claim must trace to a dataset, record, or asset identifier and be displayable in the UI via citations.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Node version is pinned and enforced in CI
- [ ] Install step uses a frozen lockfile mode
- [ ] UI lint/test/build steps run in CI (repo-defined scripts)
- [ ] Markdown protocol checks run (front-matter plus required sections)
- [ ] Security scans run (secret scan, dependency scan, PII scan as applicable)
- [ ] Accessibility checks run for UI changes (if a11y tooling exists)

### Reproduction

~~~bash
# 0) Identify which Node project you are building (commonly ./web)
# 1) Ensure a clean working tree
git status
git rev-parse HEAD

# 2) Select Node version
# Prefer repo-pinned version files when present:
#   - .nvmrc
#   - package.json "engines"
#   - toolchain files (e.g., .tool-versions)
#
# Example (if you use nvm):
#   nvm install
#   nvm use

# 3) Install dependencies (pick the command that matches the lockfile you have)
# npm:
#   npm ci
# pnpm:
#   corepack enable
#   pnpm install --frozen-lockfile
# yarn:
#   corepack enable
#   yarn install --immutable

# 4) Run repo-defined scripts (inspect package.json for exact names)
#   npm run lint
#   npm test
#   npm run build
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| ui_build_completed | CI | `mcp/runs/` (if telemetry is implemented) |
| dependency_lockfile_changed | CI | CI logs plus PR review |
| secret_scan_failed | CI | CI logs |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes to Node runtime/version pinning or lockfile policy require CI maintainer review.
- UI changes that impact provenance display, redaction, or audit affordances require governance review according to the Master Guide.

### CARE / sovereignty considerations

- Do not introduce UI behavior that could reveal sensitive locations or restricted datasets.
- Ensure any cached/static artifacts do not contain restricted content; enforce access controls via APIs and UI gating.

### AI usage constraints

- This document inherits the AI transform permissions/prohibitions in front-matter.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-30 | Initial Node environment repro runbook | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

