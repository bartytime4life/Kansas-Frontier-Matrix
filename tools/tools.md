---
title: "Tools — KFM Operational Tooling and Deployment Scaffolding"
path: "tools/README.md"
version: "v1.0.1"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:tools:readme:v1.0.1"
semantic_document_id: "kfm-tools-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:tools:readme:v1.0.1"
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

# Tools

## 📘 Overview

### Purpose
- Provide a canonical home for operational tooling that supports building, validating, and operating the Kansas Frontier Matrix (KFM) pipeline.
- Hold deployment-oriented scaffolding and ops glue that is intentionally *out of scope* for core architecture docs (cloud deployment specifics belong here and/or in a separate ops repo).

### Scope
| In Scope | Out of Scope |
|---|---|
| Deployment/runbooks and environment scaffolding that *supports* the system | Core pipeline implementations (canonical home: `src/pipelines/`) |
| Wrapper scripts that orchestrate canonical subsystems (ETL/catalog/graph/API/UI/story) | Production API/server code (canonical home: `src/server/`) |
| CI/build helpers that call canonical validators | UI application code (canonical home: `web/`) |
| Operational utilities that are not data outputs | Derived datasets or catalog/provenance outputs (canonical homes: `data/<domain>/processed/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/`, `data/graph/`) |
| Release packaging helpers (manifests/SBOM generation) that write into canonical release roots | Release artifacts stored under `tools/` (canonical home: `releases/`) |

### Audience
- KFM maintainers (data engineering, catalog, graph/ontology, API, UI, narrative/story)
- Contributors running builds locally or in CI
- Deployment/ops owners

### Definitions
- Glossary: `docs/glossary.md` (v13 target; if missing, add per repo structure standards)

### Key artifacts (what this folder should link to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Canonical pipeline ordering + invariants + system inventory |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Core Team | Canonical roots + readiness gates; identifies `tools/` as home for deployment specifics |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs maintainers | Default for runbooks/README-style docs |
| Story Node Template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative maintainers | Story nodes consumed by Focus Mode |
| API Contract Extension Template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Contract-first API changes |
| Security standards | `.github/SECURITY.md` + `docs/security/` | Security owners | Security posture + review triggers (if present) |
| Telemetry standards | `docs/telemetry/` + `schemas/telemetry/` | Telemetry owners | Observability/governance metrics emitted by tools and services (if present) |
| CI workflows | `.github/workflows/` | CI owners | CI entrypoints that call tools/validators (if present) |
| CI workflows overview | `.github/workflows/README.md` | CI owners | How CI is organized and how to run checks locally (if present) |
| Reproducibility kit | `.github/repro-kit/README.md` | CI owners | Reproducibility guidance + hashing/manifest patterns (if present) |
| Repo root README | `README.md` | KFM Core Team | Canonical high-level orientation and root inventory |
| Releases | `releases/` | Release owners | Manifests, SBOMs, signed bundles, telemetry snapshots (if adopted) |

### Definition of done (for this README)
- [ ] Front-matter complete and `path` matches `tools/README.md`.
- [ ] Scope clearly distinguishes what belongs in `tools/` vs canonical subsystem roots.
- [ ] The “add a tool” pattern is documented and repeatable.
- [ ] Contains approved headings for **Story Node & Focus Mode integration** and **Validation & CI/CD**.
- [ ] No pipeline outputs are committed under `tools/` unless they are tool source/config (pipeline outputs belong in `data/**` and other canonical roots).

## 🗂️ Directory Layout

### This document
- `path`: `tools/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| **Repo metadata + policy** | `.github/` | Workflows, security policy, contribution templates |
| **Releases** | `releases/` | Bundles (SBOMs/manifests/attestations) and release metadata |
| **MCP / experiments** | `mcp/` | Run manifests, experiment logs, model cards, evaluation artifacts |
| **Data domains + catalogs** | `data/` | Domain staging + processed data; catalog/provenance outputs |
| **Documentation** | `docs/` | Governed docs, standards, templates, reports |
| **Schemas** | `schemas/` | Machine-validated schemas/specs (STAC/DCAT/PROV/story nodes/telemetry/etc.) |
| **Pipelines** | `src/pipelines/` | ETL, transforms, catalog builders (writes outputs to `data/**`) |
| **Graph** | `src/graph/` | Ontology, constraints, migrations, ingest code |
| **API boundary** | `src/server/` | Contracted access layer (REST/GraphQL), redaction, query services |
| **Frontend** | `web/` | React-based UI (map + Focus Mode UX) |
| **Tests** | `tests/` | Automated tests for contracts and behaviors |
| **Tools** | `tools/` | Operational tooling and deployment scaffolding |

> Note: Some legacy branches may still contain `src/api/` or `src/web/`. The v13 canonical homes are `src/server/` and `web/` (one canonical home per subsystem).

### Expected file tree for this sub-area (recommended)
~~~text
📁 tools/
├── 📄 README.md
├── 📁 <tool-name>/
│   ├── 📄 README.md
│   ├── 📁 bin/              # entrypoints (optional)
│   ├── 📁 configs/          # example configs (no secrets)
│   ├── 📁 scripts/          # operational scripts/wrappers
│   └── 📁 tests/            # tool tests (optional)
└── 📁 shared/               # shared helpers (optional; avoid duplicating `src/**`)
~~~

## 🧭 Context

### How this fits the canonical pipeline
KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

`tools/` supports that flow, but does not replace any canonical subsystem root.

### Constraints and invariants
- **Canonical pipeline scripts live in `src/pipelines/`:** put *pipeline logic* in `src/pipelines/`; use `tools/` for wrappers/orchestration and non-core utilities.
- **No UI direct-to-graph reads:** `web/` must never query Neo4j directly; all graph access is via `src/server/` (API boundary).
- **Contracts are canonical:** schemas/specs must live in `schemas/` and API contracts must validate in CI.
- **Repo lint expectations:** do not add YAML front-matter to code files; reserve front-matter for governed Markdown docs.
- **Data outputs are not code:** derived datasets and catalog/provenance outputs belong under `data/**`, not under `tools/` (and not under `src/`).

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  T[tools/* wrappers & ops] --> P[src/pipelines/*]
  P --> C[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  C --> X[Graph fixtures<br/>data/graph/csv + data/graph/cypher]
  X --> G[Graph<br/>Neo4j]
  G --> A[API boundary<br/>src/server]
  A --> U[UI<br/>web]
  U --> S[Story Nodes<br/>docs/reports/story_nodes]
  S --> F[Focus Mode]
~~~

## 🧠 Story Node & Focus Mode Integration

Tools may touch narrative artifacts in two ways: (1) validating Story Nodes and their citations, and/or (2) generating **draft** story scaffolds for human review.

Rules of engagement:
- **No unsourced narrative:** tools must not “publish” or auto-promote story content that lacks citations to governed sources (datasets, documents, or evidence artifacts).
- **Draft vs published separation:** if a tool generates story content, it should clearly mark it as draft and keep it out of end-user visibility until reviewed (workflow location is implementation-defined).
- **Evidence linkage:** Story Nodes should reference stable identifiers (dataset IDs, STAC Item IDs, DCAT dataset records, PROV bundles, graph entity IDs) that exist in canonical roots.

## 🧪 Validation & CI/CD

### What tools should validate
When applicable, tooling should provide repeatable validators that CI can run deterministically. The project’s implementation guidance assumes a "docs + tests + provenance" discipline (no new code without tests/docs; no narrative without sources; no data without provenance).

- **Docs hygiene:** Markdown protocol checks and link integrity for governed docs.
- **Schema integrity:** STAC/DCAT/PROV JSON validation (and Story Node schema validation where applicable).
- **Graph ingest readiness:** validate `data/graph/**` fixtures (required columns/IDs, referential integrity).
- **API boundary:** contract tests for `src/server/` (OpenAPI/GraphQL as adopted) and redaction rules.
- **Security & secrets:** secret scanning and license attribution checks (CI integration is implementation-defined).
- **CI gate behavior:** validate artifacts when present; fail if invalid; skip only when a stage/artifact is not applicable.

### Suggested CLI pattern (example)
Each tool directory should document a minimal interface:

- `tools/<tool-name>/README.md` with:
  - **Usage** (local + CI)
  - **Inputs** (paths/env vars)
  - **Outputs** (canonical destinations)
  - **Validation** (what constitutes pass/fail)
  - **Security** (secrets/PII/sovereignty notes)

### Example commands (placeholders)
Replace these with the repo’s real commands/scripts:

~~~bash
# Validate STAC outputs (if present)
python tools/validate_stac.py data/stac/

# Validate DCAT outputs (if present)
python tools/validate_dcat.py data/catalog/dcat/

# Validate PROV bundles (if present)
python tools/validate_prov.py data/prov/

# Validate Story Nodes (if present)
python tools/validate_story_nodes.py docs/reports/story_nodes/
~~~

## 📦 Data & Metadata

### Inputs
| Input | Source | Notes |
|---|---|---|
| Tool-specific config | `tools/**` | Each tool must document required config and defaults (no secrets committed) |
| Canonical subsystem artifacts | `src/**`, `schemas/**`, `docs/**`, `data/**`, `releases/**` | Tools should call into canonical modules and validate outputs |

### Outputs
| Output | Canonical destination | Notes |
|---|---|---|
| Derived domain datasets | `data/<domain>/processed/` | Never store derived datasets under `tools/` |
| Catalog + provenance artifacts | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Required for datasets/evidence products |
| Graph import fixtures | `data/graph/csv/`, `data/graph/cypher/` | Import-ready graph artifacts (if used) |
| Release artifacts | `releases/` | Manifests/SBOMs/signed bundles (if adopted) |
| Run logs / run metadata pointers | `mcp/runs/` (recommended) | Prefer pointers/hashes to canonical outputs, not duplicated data |

## 🌐 STAC, DCAT & PROV Alignment

- STAC/DCAT/PROV are first-class and required for datasets and evidence products.
- Canonical global output locations:
  - STAC: `data/stac/collections/` and `data/stac/items/`
  - DCAT: `data/catalog/dcat/`
  - PROV: `data/prov/`
  - Graph fixtures (if used): `data/graph/csv/` and `data/graph/cypher/`

## 🧱 Architecture

### Components and contracts
| Component | Contract artifact | Notes |
|---|---|---|
| Deployment scaffolding | Runbook/README + validation steps | Must not bypass security or governance standards |
| CI/build helpers | Repeatable commands + references to canonical schemas/contracts | Should call canonical validators rather than re-implementing |
| Orchestration wrappers | CLI entrypoints + documented inputs/outputs | Must route outputs to canonical destinations |
| Release packaging | Release manifest + SBOM references | Artifacts belong under `releases/` |
| Policy/security gates | Checklists + (optional) machine-enforced validators | Changes may require governance/security review (routing not confirmed in repo) |

### Extension points checklist (for future work)
When adding new tooling under `tools/`, ensure it does not break pipeline alignment:

- [ ] **Placement:** tool source/config stays in `tools/`; outputs go to canonical roots (`data/**`, `releases/`, `mcp/runs/`).
- [ ] **Determinism:** repeatable behavior in CI (stable IDs, pinned deps, fixed seeds if relevant).
- [ ] **STAC:** if generating STAC, create/validate collections + items.
- [ ] **DCAT:** if generating DCAT, ensure dataset metadata and license/attribution are present.
- [ ] **PROV:** if generating provenance, capture activities + agents.
- [ ] **Graph:** do not introduce UI-to-graph coupling; keep graph access behind the API boundary.
- [ ] **API:** if a tool depends on endpoints, link to the relevant contract docs and validation.
- [ ] **UI:** tools must not cause `web/` to query Neo4j directly.
- [ ] **Story:** if tooling affects story publication, ensure provenance/citations/validation workflows exist.
- [ ] **Telemetry:** if emitting governed telemetry, align with telemetry schemas and docs.

## ⚖ FAIR+CARE & Governance

### Review gates
- Follow the governance, ethics, and sovereignty references in this file’s front-matter for any tool that affects data handling, publication, access control, redaction, or CI enforcement.

### CARE / sovereignty considerations
- If tooling processes culturally sensitive content or locations, it must align with the sovereignty policy and any domain-specific redaction requirements.
- Prefer synthetic fixtures and generalized coordinates for tests when sensitive locations are involved.

### AI usage constraints
- This document permits summarization/structure extraction/translation/keyword indexing, and prohibits generating policy or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.1 | 2025-12-24 | Align `tools/` README to Master Guide v12 + v13 canonical roots; add Story/CI sections; remove non-repo citations | TBD |
| v1.0.0 | 2025-12-23 | Initial `tools/` README | TBD |

## Footer refs (do not remove)
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
