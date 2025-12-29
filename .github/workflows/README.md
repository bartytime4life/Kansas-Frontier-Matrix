---
title: "KFM — GitHub Actions Workflows (CI/CD) README"
path: ".github/workflows/README.md"
version: "v1.1.1"
last_updated: "2025-12-29"
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

doc_uuid: "urn:kfm:doc:ci:workflows-readme:v1.1.1"
semantic_document_id: "kfm-ci-workflows-readme-v1.1.1"
event_source_id: "ledger:kfm:doc:ci:workflows-readme:v1.1.1"
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

**ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**

CI is not limited to code-quality validation. It is **contract enforcement**: schema-valid catalogs, provenance integrity, graph constraints, API boundary compliance, and governed Story Node outputs.

Workflows are treated as **policy gates**: if a required contract/invariant is violated, CI must fail.

**Note:** This README intentionally does **not** enumerate specific workflow filenames or job names. The canonical source of truth for “what exists” is the set of files under `.github/workflows/*.yml|*.yaml`.

### Scope

| In Scope | Out of Scope |
|---|---|
| GitHub Actions workflows in `.github/workflows/*.yml|*.yaml` (CI, validation, packaging, scheduled verification) | Writing / redefining governance policy text (see `docs/governance/*`) |
| CI gates for docs, schemas, catalogs (STAC/DCAT/PROV), graph, API, UI, Story Nodes | Storing secrets, credentials, tokens, or private keys in the repo |
| Determinism and reproducibility expectations for validations | Replacing the canonical pipeline ordering |
| Path-filter mapping (what runs when specific roots change) | Bypassing required human review for sensitive content |

### Audience

- Primary: CI maintainers and repo maintainers.
- Secondary: contributors who modify data, catalogs, schemas, graph ingest, API contracts, UI layers, and Story Nodes.

### Definitions

#### Link to glossary
- Link: `docs/glossary.md` *(not confirmed in repo; if absent, add it or define terms in the relevant domain docs)*

Terms used in this doc:
- **Workflow**: a GitHub Actions workflow YAML file under `.github/workflows/`.
- **Gate**: a validation step that fails CI if a required contract/invariant is violated.
- **Contract boundary**: the rule that the UI never talks to Neo4j directly; access is via contracted APIs.
- **Provenance-linked**: an output can be traced to evidence IDs (datasets/docs) via STAC/DCAT/PROV + (where applicable) graph references.
- **Optional subsystem**: a repo area that may not exist yet; CI should skip with an informative message rather than fail.
- **Path-filtered**: jobs are conditionally executed based on which repo roots changed in a PR.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | KFM core maintainers | Canonical pipeline ordering + invariants + minimum CI gates |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs maintainers | Required doc structure (front matter + section set) |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story maintainers | Governed narrative format + provenance/citation requirements |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Contract change proposal template |
| Architecture blueprint (draft reference) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture maintainers | Draft reference; adoption not guaranteed |
| Schemas | `schemas/` | Contract owners | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) *(expected root; confirm in repo)* |
| Catalog outputs | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | Data maintainers | Catalog + lineage artifacts validated before graph ingest |
| Graph build/ingest | `src/graph/**` | Graph maintainers | Ontology bindings + graph build/migrations |
| API boundary | `src/server/**` | API maintainers | API service + contracts + redaction logic |
| UI | `web/**` | Frontend maintainers | React/map client + Focus Mode UI; never talks to Neo4j directly |
| CI workflows | `.github/workflows/**` | CI maintainers | Workflow YAML + gates + artifacts |

### Definition of done (for this document)

- [ ] Front matter complete + valid
- [ ] Mermaid diagrams render (no parse errors)
- [ ] “Minimum CI gates” section aligns with `docs/MASTER_GUIDE_v12.md`
- [ ] Path → gate mapping is clear (docs / schemas / catalogs / graph / API / UI / story)
- [ ] Security + sovereignty constraints explicitly stated (secrets, PII, sensitive locations, classification propagation)
- [ ] Optional subsystems are explicitly handled as skip-with-message (not silent pass/fail)
- [ ] No “invented structure”: anything uncertain is marked **not confirmed in repo**

---

## 🗂️ Directory Layout

### This document

- `path`: `.github/workflows/README.md` *(must match front matter)*

### Related repository paths (expected)

| Area | Path | What lives here |
|---|---|---|
| CI | `.github/` | Workflows + policy gates |
| Data domains | `data/` | Staged data + catalog outputs (STAC/DCAT/PROV) |
| Documentation | `docs/` | Canonical governed docs |
| Templates | `docs/templates/` | Governed doc templates (universal/story/API) |
| Architecture | `docs/architecture/` | System designs, roadmaps, ADRs *(if present)* |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) *(if present)* |
| Pipelines | `src/pipelines/` | ETL + catalog generation code *(if present)* |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations *(if present)* |
| API boundary | `src/server/` | API service + contracts + redaction logic *(if present)* |
| UI | `web/` | React + map client + Focus Mode UI *(if present)* |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs *(if present)* |
| Tests | `tests/` | Unit + integration tests *(if present)* |
| Tools | `tools/` | Validators, utilities, QA scripts *(if present)* |
| Releases | `releases/` | Versioned packaged artifacts *(if used)* |

### Expected file tree for this sub-area

~~~text
📁 .github/
├── 📁 workflows/
│   ├── 📄 README.md
│   ├── 📄 *.yml
│   └── 📄 *.yaml
└── 📄 SECURITY.md                         # if present
~~~

Note: Workflow filenames and job layouts should not be hard-coded in this README unless they exist in-repo and are kept synchronized.

---

## 🧭 Context

### Background

KFM’s credibility depends on **deterministic, governed, provenance-first publishing**: data and narratives must remain traceable, auditable, and contract-compliant across the full pipeline. CI is the enforcement mechanism that makes these guarantees continuous, not aspirational.

This README exists to help maintainers and contributors understand:
- what CI is responsible for (gates)
- when gates run (triggers + path filters)
- what is required vs optional (skips vs failures)
- how to add checks without breaking pipeline ordering

### Assumptions

- Branch protection rules require a subset of CI checks on the default branch.
- The repo follows canonical top-level roots unless explicitly versioned otherwise.
- Some subsystems may be incomplete; CI should skip subsystem-specific gates when required roots are absent, while still enforcing global governance and security checks.

### Constraints / invariants

- **Pipeline ordering is non-negotiable:** ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode.
- **API boundary is non-negotiable:** UI never connects to Neo4j directly; it consumes contracted APIs.
- **Provenance-first:** STAC/DCAT/PROV are produced and validated before graph ingest and before UI/narrative surfacing.
- **Determinism:** transforms are config-driven, idempotent, logged, and reproducible (hash inputs/outputs).
- **Sovereignty and classification propagation:** no output is less restricted than any input in its lineage; interactive UI must not leak sensitive locations by zoom/interaction.

### Design principles for workflows

- **Contract-first:** gates validate explicit schemas/contracts; failures should point to the contract violated.
- **Path-filtered by default:** avoid running heavy jobs when unrelated roots change.
- **Explainable failures:** every gate should emit an actionable summary (what failed, where, how to reproduce).
- **Deterministic artifacts:** artifacts (reports) must be stable across reruns of the same commit.
- **Safe outputs:** workflow logs/artifacts must not leak secrets, PII, or sensitive locations.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which workflow checks are required in branch protection (by name) for the default branch? | CI maintainers | TBD |
| Where are the authoritative validators located (e.g., `tools/`, `schemas/`, `src/`)? | Maintainers | TBD |
| Is the API service rooted at `src/server/` or an equivalent (`src/api/`)? | API maintainers | TBD |
| Do we maintain `data/graph/` exports/import fixtures yet, or skip those gates for now? | Graph maintainers | TBD |
| Are Story Nodes split into draft/published subfolders (governed publishing), or a single tree? | Story maintainers | TBD |

### Future extensions

- Add reusable workflows (via `workflow_call`) for repeatable gates across modules.
- Add nightly scheduled “deep validation” runs (catalog link integrity + graph consistency + provenance closure).
- Add “repo-structure lint” to detect unsanctioned new roots and out-of-repo references in governed docs.
- Add typed CI artifacts: machine-readable validation reports for downstream governance review.

---

## 🗺️ Diagrams

### Canonical pipeline and where CI gates apply

~~~mermaid
flowchart LR
  subgraph Data
    A[Raw Sources<br/>data/raw/&lt;domain&gt;] --> B[ETL + Normalization<br/>src/pipelines]
    B --> C[STAC Items + Collections<br/>data/stac]
    C --> D[DCAT Dataset Views<br/>data/catalog/dcat]
    C --> E[PROV Lineage Bundles<br/>data/prov]
  end

  C --> G[Graph<br/>src/graph]
  D --> G
  E --> G

  G --> H[API Boundary<br/>src/server]
  H --> I[UI<br/>web]
  I --> J[Story Nodes<br/>docs/reports/story_nodes]
  J --> K[Focus Mode<br/>provenance-linked only]

  CI[CI Gates<br/>.github/workflows] -. validates .-> B
  CI -. validates .-> C
  CI -. validates .-> D
  CI -. validates .-> E
  CI -. validates .-> G
  CI -. validates .-> H
  CI -. validates .-> I
  CI -. validates .-> J
~~~

### CI gate flow on Pull Requests

~~~mermaid
flowchart TB
  PR[Pull Request] --> CI[GitHub Actions CI]
  CI --> D[Detect changed paths]
  D --> DOCS[Docs gates]
  D --> SCHEMA[Schema gates]
  D --> DATA[Catalog gates]
  D --> GRAPH[Graph gates]
  D --> API[API contract gates]
  D --> UI[UI gates]
  D --> STORY[Story Node gates]
  D --> SEC[Security + sovereignty gates]

  DOCS --> MERGE[Check status aggregation]
  SCHEMA --> MERGE
  DATA --> MERGE
  GRAPH --> MERGE
  API --> MERGE
  UI --> MERGE
  STORY --> MERGE
  SEC --> MERGE

  MERGE --> PASS[Merge allowed]
  MERGE --> FAIL[Fail if required gates fail]

  STYLE[Markdown protocol + lint] --> DOCS
  LINKS[Link/reference checks] --> DOCS
  JSON[JSON schema validation] --> SCHEMA
  STAC[STAC validate + links] --> DATA
  DCAT[DCAT validate] --> DATA
  PROV[PROV validate + cross-links] --> DATA
  NEO4J[Graph integrity tests] --> GRAPH
  CONTRACTS[API contract tests] --> API
  A11Y[UI accessibility checks] --> UI
  STORYVAL[Story schema + citations] --> STORY
  SECRETS[Secret scanning] --> SEC
  PII[PII scan] --> SEC
  SENS[Sensitive-location leakage checks] --> SEC
  CLASS[Classification propagation checks] --> SEC
~~~

---

## 📦 Data & Metadata

### Inputs (what triggers / what gets validated)

| Input type | Examples | Typical file roots |
|---|---|---|
| Documentation | READMEs, Story Nodes, governance docs | `docs/**`, `.github/**` |
| Schemas | JSON Schema, contract definitions | `schemas/**`, `src/server/**` |
| Catalog outputs | STAC/DCAT/PROV bundles | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` |
| Source code | ETL, graph build, API, UI | `src/**`, `web/**` |
| Graph fixtures | CSV/Cypher import artifacts | `data/graph/**` *(if present)* |

### Outputs (what workflows should produce)

| Output type | Examples | Where stored |
|---|---|---|
| CI status checks | docs/schema/catalog/graph/api/ui/security checks | GitHub Checks UI |
| Validation reports | JSON/HTML summaries, logs | Workflow artifacts |
| Deterministic build artifacts | Optional: schema bundles, generated reports | Artifacts or versioned repo locations (if governance allows) |
| Release artifacts (optional) | Tagged bundles, packaged datasets | GitHub Releases + artifacts |

### Sensitivity & redaction

- CI should treat sensitivity/redaction violations as **blocking**.
- Workflows must not emit sensitive raw coordinates or internal-only datasets into public artifacts.
- Classification propagation rule of thumb: **outputs must not be less restricted than inputs**.

### Quality signals

- Schema validation pass/fail is a minimum quality gate.
- Domain-specific checks (geometry validity, temporal range checks, ID stability) belong in ETL and should be reflected in CI checks.

---

## 🌐 STAC, DCAT & PROV Alignment

Workflows should validate that:

- STAC catalogs under `data/stac/` are schema-valid and link-consistent.
- DCAT outputs under `data/catalog/dcat/` meet DCAT minimums (license, title, description, keywords).
- PROV bundles under `data/prov/` form complete lineage chains and cross-link to STAC/DCAT identifiers.
- Where graph export/import outputs exist, they reference valid evidence IDs and maintain stable identifiers.

Schema locations are expected under `schemas/` (e.g., `schemas/stac/`, `schemas/dcat/`, `schemas/prov/`) **if present**. If schemas are embedded in code instead, CI should still validate against the same profiles.

---

## 🧱 Architecture

### Required CI gates (baseline: v12-ready)

Minimum CI gates (baseline):

- Markdown protocol validation (front matter + required sections)
- Link/reference checks (no orphan pointers)
- JSON schema validation:
  - STAC/DCAT/PROV
  - story node schemas *(if present)*
  - telemetry schemas *(if present)*
  - UI layer registry schemas *(if present)*
- Graph integrity tests (constraints, expected labels/edges)
- API contract tests (OpenAPI/GraphQL schema + resolver tests)
- Security + sovereignty scanning gates (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Path-based gate selection (recommended)

Use path filters so PRs only run the gates they affect, while keeping a small set of global checks always-on.

| If PR changes… | Required gates |
|---|---|
| `.github/**` | Docs lint (for Markdown), workflow YAML lint *(if implemented)*, security checks |
| `docs/**` | Markdown protocol validation + link checks + story validation when applicable |
| `schemas/**` | JSON schema validation (schemas themselves + impacted artifacts) |
| `data/stac/**` / `data/catalog/dcat/**` / `data/prov/**` | STAC/DCAT/PROV validation + cross-link integrity |
| `src/pipelines/**` | ETL tests + catalog validation + determinism checks (where implemented) |
| `src/graph/**` or `data/graph/**` | Graph integrity tests + evidence reference checks |
| `src/server/**` | API contract tests + security checks |
| `web/**` | UI tests + accessibility checks + “no direct graph calls” checks |

### Skip behavior for optional subsystems

Determinism rule:

- If a **required** directory exists (e.g., `data/stac/`), validation must run and fail if invalid.
- If an **optional** root does not exist (e.g., `web/` in an early stage), the corresponding jobs should **skip with an informative message**, not fail CI.

### Repo-structure lint (v13-aligned recommendation)

To prevent “one-off” structures that break discoverability and governance, CI should eventually enforce:

- No new top-level directories outside canonical roots without approval
- No out-of-repo references for governed docs (e.g., `file-service://` links)
- No silent relocation of governed artifacts (Story Nodes, catalogs, schemas) without updating canonical docs

### Extension points checklist (for future work)

When adding new workflows or new gates, check:

- [ ] Does the change preserve canonical ordering (ETL → Catalogs → Graph → API → UI → Story → Focus)?
- [ ] Is there a schema/contract this gate validates? If yes, where is it versioned?
- [ ] Are validation artifacts deterministic and safe to publish (no sensitive content)?
- [ ] Are required checks documented and added to branch protection rules?
- [ ] Do path filters ensure we don’t run heavy jobs unnecessarily?
- [ ] Do we skip optional subsystem gates safely when directories are absent?
- [ ] If this change affects a subsystem contract, did we update the relevant template-based doc (universal/story/API contract)?

---

## 🧠 Story Node & Focus Mode Integration

### Why workflows matter for Story Nodes

Story Nodes and Focus Mode outputs are governed artifacts with strong provenance requirements. CI workflows enforce that:

- Story Nodes reference valid evidence (dataset IDs, doc UUIDs)
- Sensitive content is redacted per sovereignty and ethics rules
- Graph exports (if used) match ontology constraints and provenance references

### When to run Story Node validation

- On PRs touching `docs/reports/story_nodes/`
- On PRs touching story schemas under `schemas/**` *(if present)*
- On release tags if story bundles are published

### Provenance-linked narrative rule

Focus Mode must consume only provenance-linked context bundles (no unsourced narrative). If a Story Node claim cannot be traced to evidence, it must be rewritten as an open question or explicitly marked “source data not yet integrated.”

---

## 🧪 Validation & CI/CD

### Validation steps

At minimum, workflows should:

1. Detect changed paths (PR diff)
2. Run required validations for impacted roots (docs/schemas/catalogs/graph/api/ui/story)
3. Publish machine-readable reports as artifacts (JSON preferred)
4. Fail the run if any required gate fails
5. Provide actionable failure summaries (what failed, where, and how to reproduce)

### Reproduction (local)

Replace the placeholders below with repo-specific commands (do not invent new tooling paths):

~~~bash
# Docs protocol + lint (placeholder)
# <cmd> tools/validate_markdown_protocol <paths>

# Catalog validation (placeholder)
# <cmd> tools/validate_stac data/stac
# <cmd> tools/validate_dcat data/catalog/dcat
# <cmd> tools/validate_prov data/prov

# Graph integrity (placeholder)
# <cmd> tests/graph_integrity

# API contract tests (placeholder)
# <cmd> tests/api_contracts

# UI tests + a11y (placeholder)
# <cmd> web/test
~~~

### Telemetry signals (recommended, if implemented)

If CI publishes structured outputs, prefer stable, machine-readable signals that can be referenced in governance review:

| Signal | Source | Where recorded |
|---|---|---|
| `classification_assigned` | ETL / catalog validation | Workflow artifact; PROV (if recorded) |
| `redaction_applied` | ETL / API redaction | Workflow artifact; PROV (if recorded) |
| `promotion_blocked` | CI gating | Workflow artifact (gate name + reason + scan refs) |
| `catalog_published` | Catalog pipeline | Workflow artifact; STAC/DCAT outputs |
| `focus_mode_redaction_notice_shown` | UI (if telemetry exists) | Telemetry logs *(not confirmed in repo)* |

---

## ⚖ FAIR+CARE & Governance

### Review gates

CI is part of governance enforcement. CI must fail on:

- Missing provenance for Story Node claims (where enforceable)
- Violations of CARE/sovereignty rules (e.g., exposing sensitive locations)
- Secret/credential leakage, PII leakage, or classification downgrades
- Missing license metadata for new datasets (DCAT minimums)

### CARE / sovereignty considerations

Treat culturally sensitive content as high-risk by default:
- Prefer redaction or abstraction over exposing precise locations
- Require human review for sensitive domains and any ambiguity in classification/consent

### AI usage constraints

This README’s AI transform permissions/prohibitions are defined in front matter and must remain aligned with repo governance. Do not add new AI permissions here without governance review.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.1.1 | 2025-12-29 | Sync with Universal template: clarify “expected vs not confirmed”, align CI gate list with Master Guide v12-ready minimums, refine pipeline diagram, add telemetry signal table | TBD |
| v1.1.0 | 2025-12-28 | Align with Universal template + Master Guide CI gates; add path→gate mapping + v13-aligned structure notes | TBD |
| v1.0.0 | 2025-12-22 | Initial workflows README scaffold | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
