---
title: "KFM — GitHub Actions Workflows (CI/CD) README"
path: ".github/workflows/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "Reference"
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

doc_uuid: "urn:kfm:doc:ci:workflows-readme:v1.0.0"
semantic_document_id: "kfm-ci-workflows-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:workflows-readme:v1.0.0"
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

# .github/workflows — GitHub Actions for KFM

## 📘 Overview

### Purpose

This directory contains GitHub Actions workflows that enforce CI gates across the Kansas Frontier Matrix (KFM) canonical pipeline:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

The intent is not just code-quality validation, but contract enforcement: schema-valid catalogs, provenance integrity, graph constraints, API boundary compliance, and governed story outputs.

### Scope

| In Scope | Out of Scope |
|---|---|
| GitHub Actions workflows in `.github/workflows/*.yml` (CI, validation, packaging) | Defining governance policy text (see `docs/governance/*`) |
| CI gates for docs, schemas, data catalogs, graph, API, UI, and story nodes | Storing secrets or credentials in the repo |
| Determinism and reproducibility expectations for validations | Replacing the canonical pipeline ordering |

### Audience

- Primary: CI maintainers and repo maintainers.
- Secondary: contributors who modify data, catalogs, schemas, graph ingest, API contracts, UI layers, and story nodes.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Workflow**: a GitHub Actions workflow YAML file under `.github/workflows/`.
  - **Gate**: a validation step that fails CI if a required contract/invariant is violated.
  - **Contract boundary**: the rule that the UI never talks to Neo4j directly; access is via APIs.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | KFM core maintainers | Defines canonical pipeline and invariants |
| Redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture maintainers | Defines CI mapping + minimum gates |
| Schemas | `schemas/` | Contracts owners | Canonical validation targets *(not confirmed in repo)* |
| Catalog outputs | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | Data maintainers | Catalog + lineage artifacts |
| Graph import outputs | `data/graph/csv/**`, `data/graph/cypher/**` | Graph maintainers | Graph import fixtures |
| API contracts | `src/server/contracts/**` | API maintainers | Contract boundary for UI *(if present)* |
| UI code + layer registry | `web/**` (incl. `**/layers/**`) | Frontend maintainers | Map layers + Focus Mode inputs *(if present)* |
| Story Nodes | `docs/reports/story_nodes/**` | Story maintainers | Governed narrative outputs |

### Definition of done (for this document)

- [ ] Front matter complete + valid
- [ ] Mermaid diagram renders (no parse errors)
- [ ] CI gates list aligns with `docs/MASTER_GUIDE_v12.md`
- [ ] Workflow mapping to gates is clear (docs/data/schemas/graph/api/ui/story)
- [ ] Security constraints explicitly stated (secrets, supply chain, provenance)

## 🗂️ Directory Layout

### This document

- `path`: `.github/workflows/README.md` (must match front matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub workflows | `.github/workflows/` | GitHub Actions workflows (tests, validation, deploy) |
| Local actions | `.github/actions/` | Reusable actions invoked by workflows |
| Scripts/tools | `tools/` | Repo utilities used by CI *(if present)* |
| Schemas | `schemas/` | Validation targets (STAC/DCAT/PROV, Story Nodes, API, UI) |
| Data | `data/` | Raw/work/processed + stac/catalog/prov |
| Docs | `docs/` | Governed docs and Story Nodes |
| Source | `src/` | ETL/pipeline + graph + API code *(if present)* |
| UI | `web/` | React/MapLibre UI *(if present)* |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 workflows/
    ├── 📄 README.md
    └── 📄 *.yml
~~~

Note: The specific workflow filenames and job layouts are intentionally not enumerated here unless they exist in-repo. Keep this README synchronized with actual `.yml` files present.

---

## 🧭 Context

KFM’s CI and workflow conventions are anchored to the Master Guide and the v13 redesign blueprint:

- canonical pipeline ordering and invariants
- contract-first API boundaries
- provenance-first content rules
- schema-valid catalogs and story outputs

KFM’s design rules also include: **the UI must not connect to Neo4j directly**; it must access the graph via the API contracts and enforce provenance and redaction rules at the boundary.

GitHub repository conventions place CI configuration in `.github/` (often hidden), including GitHub Actions workflows used for tests, data updates, and deployments (as applicable).

---

## 🗺️ Diagrams

### Canonical pipeline and where CI gates apply

~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph<br/>data/graph + src/graph]
  C --> D[API Boundary<br/>src/server + contracts]
  D --> E[UI<br/>web]
  E --> F[Story Nodes<br/>docs/reports/story_nodes]
  F --> G[Focus Mode<br/>provenance-linked only]

  CI[CI Gates<br/>.github/workflows] -. validates .-> A
  CI -. validates .-> B
  CI -. validates .-> C
  CI -. validates .-> D
  CI -. validates .-> E
  CI -. validates .-> F
~~~

### CI gate flow on Pull Requests

~~~mermaid
flowchart TB
  PR[Pull Request] --> CI[GitHub Actions CI]
  CI --> D[Detect changed paths]
  D --> DOCS[Docs gates]
  D --> SCHEMA[Schema gates]
  D --> DATA[Data catalog gates]
  D --> GRAPH[Graph gates]
  D --> API[API contract gates]
  D --> UI[UI gates]
  D --> STORY[Story Node gates]

  DOCS --> MERGE[Check status aggregation]
  SCHEMA --> MERGE
  DATA --> MERGE
  GRAPH --> MERGE
  API --> MERGE
  UI --> MERGE
  STORY --> MERGE

  MERGE --> PASS[Merge allowed]
  MERGE --> FAIL[Fail if required gates fail]

  STYLE[Style: Markdown protocol + lint] --> DOCS
  JSON[JSON schema validation] --> SCHEMA
  STAC[STAC validate + links] --> DATA
  DCAT[DCAT validate] --> DATA
  PROV[PROV validate + cross-links] --> DATA
  NEO4J[Neo4j ingest tests] --> GRAPH
  CONTRACTS[API contract tests] --> API
  A11Y[UI accessibility checks] --> UI
  STORYVAL[Story schema + citations] --> STORY
~~~

---

## 📦 Data & Metadata

### Inputs (what triggers / what gets validated)

| Input type | Examples | Typical file roots |
|---|---|---|
| Documentation | README updates, Story Nodes, governance docs | `docs/**`, `.github/**` |
| Schemas | JSON Schema, contract definitions | `schemas/**`, `src/server/contracts/**` |
| Data outputs | STAC/DCAT/PROV catalogs, raw/work/processed data | `data/**` |
| Source code | ETL, graph build, API, UI | `src/**`, `web/**` |

### Outputs (what workflows should produce)

| Output type | Examples | Where stored |
|---|---|---|
| CI status checks | “docs-lint”, “schema-validate”, “catalog-validate” | GitHub checks UI |
| Validation reports | JSON/HTML summaries, logs | Workflow artifacts |
| Deterministic build artifacts | graph import CSVs/Cypher, schema bundles | `data/graph/**`, `schemas/**` |
| Release artifacts (optional) | tagged bundles, packaged datasets | Releases + artifacts |

### Sensitivity & redaction

- CI should treat sensitivity and redaction violations as **blocking**.
- Do not allow workflows to emit sensitive raw coordinates or internal-only datasets into public artifacts.

### Quality signals

- Schema validation pass/fail is a minimum quality gate.
- Domain-specific checks (geometry validity, temporal range checks, ID stability) belong in ETL and should be reflected in CI checks.

## 🌐 STAC, DCAT & PROV Alignment

Workflows should validate that:

- STAC catalogs under `data/stac/` are schema-valid and link-consistent.
- DCAT outputs under `data/catalog/dcat/` meet DCAT 3 minimums (license, title, description, keywords).
- PROV bundles under `data/prov/` form complete lineage chains and cross-link to STAC/DCAT IDs.
- Where graph import outputs exist, they reference valid evidence IDs and maintain stable identifiers.

Schemas for these live under `schemas/stac/`, `schemas/dcat/`, and `schemas/prov/`.

---

## 🧱 Architecture

### CI gates required for v13 readiness

Minimum CI gates (v13 readiness):

- Markdown protocol lint (front matter + approved H2 headings + fencing style)
- Schema validation (STAC/DCAT/PROV JSON Schema + Story Node schema)
- Provenance integrity checks (no orphan entities; prov refs resolve)
- API boundary checks (UI does not access graph directly; API contracts are versioned)
- Security / secret scanning (no keys, no tokens, no secrets committed)
- Accessibility checks for docs and UI (where relevant)
- Determinism checks (optional but recommended): stable IDs, fixed seeds, diffable outputs

Workflow determinism rule: If required directories exist (e.g. `data/stac/`), validation must run and fail if invalid. If an optional root doesn’t exist (e.g. `web/`), the corresponding workflow jobs should skip with an informative message, not fail CI.

CI should also enforce basic “repo lint” rules:

- No whitespace-only commits in governed docs
- No new top-level directories outside canonical roots without approval
- No use of `file-service://` links or other out-of-repo references in governed docs

Contract-first API boundary enforcement:

- UI cannot call Neo4j; all graph access goes through APIs (`src/server/` / contracted interfaces)
- Story Nodes must cite dataset/document IDs; CI should verify referenced IDs exist where possible

## 🧠 Story Node & Focus Mode Integration

### Why workflows matter for Story Nodes

Story Nodes and Focus Mode outputs are governed artifacts with strong provenance requirements. CI workflows enforce that:

- Story Nodes reference valid evidence (dataset IDs, doc UUIDs)
- Sensitive content is redacted per sovereignty and ethics rules
- Graph exports match ontology constraints

### When to run Story Node validation

- On PRs touching `docs/reports/story_nodes/`
- On PRs touching schemas under `schemas/story_nodes/` *(if present)*
- On release tags if story bundles are published

## 🧪 Validation & CI/CD

- Use path filters to avoid running heavy jobs on unrelated PRs
- Prefer small, deterministic fixtures for schema validation tests
- Store reports as workflow artifacts
- Enforce branch protection with required checks

## ⚖ FAIR+CARE & Governance

CI is part of governance enforcement. CI must fail on:

- Missing provenance for Story Node claims
- Violations of CARE/sovereignty rules (e.g., exposing sensitive locations)
- Missing license metadata for new datasets (DCAT)

CI should treat sensitivity and redaction violations as blocking.

This README’s AI transform permissions/prohibitions are defined in front-matter and should remain aligned with repo governance.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial workflows README scaffold | TBD |

---

## 📎 Footer refs (do not remove)

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
