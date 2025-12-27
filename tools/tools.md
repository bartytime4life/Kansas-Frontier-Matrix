---
title: "Tools — KFM Operational Tooling and Deployment Scaffolding"
path: "tools/README.md"
version: "v1.0.2"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:tools:readme:v1.0.2"
semantic_document_id: "kfm-tools-readme-v1.0.2"
event_source_id: "ledger:kfm:doc:tools:readme:v1.0.2"
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

# Tools — KFM Operational Tooling and Deployment Scaffolding

Operational tooling and deployment scaffolding that **supports** the Kansas Frontier Matrix (KFM) pipeline without replacing any canonical subsystem roots.

## 📘 Overview

### Purpose
- Provide a canonical home for **operational tooling** that supports building, validating, packaging, and operating the KFM pipeline.
- Hold **deployment-oriented scaffolding** and ops glue that is intentionally out of scope for core architecture docs.
- Serve as the “ops + orchestration edge” while preserving the canonical pipeline ordering and artifact placement rules.

> Cloud deployment specifics belong under `tools/` and/or a separate ops repository (if adopted). This folder is where repo-contained deployment scaffolding should live.

### Scope
| In Scope | Out of Scope |
|---|---|
| Deployment/runbooks and environment scaffolding that supports the system | Core pipeline implementations (canonical home: `src/pipelines/`) |
| Wrapper scripts that orchestrate canonical subsystems (ETL/catalog/graph/API/UI/story) | Production graph build/migrations (canonical home: `src/graph/`) |
| CI/build helpers that call canonical validators | Production API/server code (canonical home: `src/server/`) |
| Operational utilities that are not data outputs | UI application code (canonical home: `web/`) |
| Release packaging helpers (manifests/SBOM/checksum scaffolding) that write into canonical release roots | Schemas/specs (canonical home: `schemas/`) |
| “Promotion” tooling that moves/validates artifacts into canonical locations (when adopted) | Derived datasets or catalog/provenance outputs committed under `tools/` (canonical homes: `data/**`, `releases/`) |

### Audience
- KFM maintainers (data engineering, catalog, graph/ontology, API, UI, narrative/story)
- Contributors running builds locally or in CI
- Deployment/ops owners

### Definitions
- Glossary: `docs/glossary.md` *(v13 target; not confirmed in repo — add or repair link if the glossary lives elsewhere)*

Terms used in this document:
- **Contract artifact**: a machine-validated schema/spec (JSON Schema, OpenAPI, GraphQL SDL, UI registry schema).
- **Evidence artifact**: catalog + provenance outputs consumed downstream (STAC/DCAT/PROV and derived evidence products).
- **Run manifest**: a small record that captures how to reproduce a run (inputs, config, commit SHA, versions, parameters). Recommended location: `mcp/runs/` (as pointers + hashes, not duplicated data).
- **Domain pack**: the minimal set that lets a domain participate in the pipeline (staging + mapping + tests + docs).
- **Tool (KFM sense)**: code/config under `tools/` that wraps, validates, packages, or deploys canonical subsystems and writes outputs only to canonical destinations.

### Key artifacts (what this folder should link to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Canonical pipeline ordering + invariants + expected top-level layout |
| v13 Redesign Blueprint (draft; if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Core Team | Canonical roots + readiness gates; states deployment specifics belong in `tools/` |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs maintainers | Default for governed guides/runbooks/READMEs |
| Story Node Template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative maintainers | Story nodes consumed by Focus Mode |
| API Contract Extension Template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Contract-first API changes |
| API contracts (boundary) | `src/server/contracts/` | API maintainers | Contract-first boundary between UI and graph/catalogs *(if present)* |
| CI workflows | `.github/workflows/` | CI owners | CI entrypoints that may call tools/validators *(if present)* |
| CI workflows overview | `.github/workflows/README.md` | CI owners | How CI is organized and how to run checks locally *(if present)* |
| Reproducibility kit | `.github/repro-kit/README.md` | CI owners | Repro guidance + hashing/manifest patterns *(if present)* |
| Releases | `releases/` | Release owners | Manifests, SBOMs, signed bundles, telemetry snapshots *(if adopted)* |
| Data lifecycle + canonical outputs | `data/README.md` | Data maintainers | Raw/work/processed + catalog/provenance + graph import layout *(if present)* |

### Definition of done (for this README)
- [x] Front-matter complete and `path` matches `tools/README.md`.
- [x] Scope clearly distinguishes what belongs in `tools/` vs canonical subsystem roots.
- [x] The “add a tool” pattern is documented and repeatable.
- [x] Contains approved headings for **Story Node & Focus Mode integration** and **Validation & CI/CD**.
- [x] No pipeline outputs are committed under `tools/` unless they are tool source/config (pipeline outputs belong in `data/**` and other canonical roots).
- [ ] Repo lint / Markdown protocol checks run (CI or local).
- [ ] Maintainer review.

## 🗂️ Directory Layout

### This document
- `path`: `tools/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| **Repo metadata + policy** | `.github/` | Workflows, security policy, contribution templates |
| **CI workflows** | `.github/workflows/` | Build/test/validate gates *(if present)* |
| **Repro kit** | `.github/repro-kit/` | CI-equivalent reproducibility wrappers *(if present)* |
| **Releases** | `releases/` | Bundles (SBOMs/manifests/attestations) and release metadata *(if adopted)* |
| **MCP / experiments** | `mcp/` | Run manifests, experiment logs, model cards, evaluation artifacts |
| **Data domains + catalogs** | `data/` | Domain staging + processed data; global catalog/provenance outputs |
| **Domain mapping/docs** | `docs/data/` | Domain documentation and mapping guidance *(if present)* |
| **Documentation** | `docs/` | Governed docs, standards, templates, reports |
| **Schemas** | `schemas/` | Machine-validated schemas/specs (STAC/DCAT/PROV/story nodes/telemetry/etc.) |
| **Pipelines** | `src/pipelines/` | ETL, transforms, catalog builders (writes outputs to `data/**`) |
| **Graph** | `src/graph/` | Ontology, constraints, migrations, ingest code |
| **API boundary** | `src/server/` | Contracted access layer (REST/GraphQL), redaction, query services |
| **Frontend** | `web/` | React-based UI (map + Focus Mode UX) |
| **Story Nodes** | `docs/reports/story_nodes/` | Narrative artifacts consumed by Focus Mode *(draft/published split not confirmed in repo)* |
| **Tests** | `tests/` | Automated tests for contracts and behaviors |
| **Tools** | `tools/` | Operational tooling and deployment scaffolding |

> Some paths are “v13 target layout” references. If a path is missing in the current repo state, treat it as **not confirmed in repo** and repair links once canonical locations are finalized.

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

### Add a new tool (repeatable pattern)
When introducing `tools/<tool-name>/`, follow this pattern:

1) **Create the tool folder + README**
- `tools/<tool-name>/README.md` must include: Usage (local + CI), Inputs, Outputs (canonical destinations), Validation (pass/fail), Security (secrets/PII/sovereignty notes).

2) **Define a minimal interface**
- Prefer a single entrypoint under `bin/` or `scripts/` (or a thin wrapper that calls a canonical module under `src/**`).

3) **Keep outputs out of `tools/`**
- Data + evidence outputs go to canonical roots: `data/<domain>/{raw,work,processed}/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/`, `data/graph/`, and/or `releases/`.

4) **Emit reproducibility pointers**
- Record a run manifest or pointer under `mcp/runs/` that references produced artifacts by stable IDs and/or checksums (no duplicated datasets).

5) **Wire validation into CI (if applicable)**
- If the tool is a validator, add it to CI workflows so invalid artifacts fail fast.
- If CI wiring is not yet present, document the intended CI hook location (e.g., `.github/workflows/…`).

6) **Add tests where appropriate**
- Put tool-specific tests under `tools/<tool-name>/tests/` and/or `tests/` depending on project conventions.

## 🧭 Context

### How this fits the canonical pipeline
KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

`tools/` supports that flow, but does not replace any canonical subsystem root.

### Constraints and invariants
- **One canonical home per subsystem:** avoid “mystery duplicates” (tools wrap; subsystems implement).
- **Canonical pipeline logic lives in `src/**`:** put pipeline logic in `src/pipelines/`; use `tools/` for wrappers/orchestration and ops utilities.
- **Contracts are canonical:** schemas/specs belong in `schemas/` and API contracts live at the API boundary (commonly `src/server/contracts/` if present).
- **No UI direct-to-graph reads:** `web/` must never query Neo4j directly; all graph access is via the contracted API boundary in `src/server/`.
- **Provenance is first-class:** if a tool triggers artifact generation, provenance should be captured (directly or via the underlying subsystem).
- **Outputs go to canonical destinations:** derived datasets, catalogs, provenance bundles, and graph fixtures belong under `data/**` (and release bundles under `releases/`), not under `tools/`.
- **Governance is not bypassed:** tools must not weaken redaction/sensitivity enforcement or publish unsourced narrative.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  T[tools operational tooling] --> P[src/pipelines]
  P --> C[data catalogs STAC DCAT PROV]
  C --> X[data graph fixtures csv and cypher]
  X --> G[graph Neo4j via src/graph]
  G --> A[api boundary src/server]
  A --> U[ui web]
  U --> S[story nodes docs/reports/story_nodes]
  S --> F[focus mode]
  T --> R[release packaging releases]
~~~

## 🧠 Story Node & Focus Mode Integration

Tools may touch narrative artifacts in two ways:
1) **Validating** Story Nodes and their evidence links.
2) Generating **draft** scaffolds for human review (never auto-publish).

Rules of engagement:
- **No unsourced narrative:** tools must not “publish” or auto-promote story content that lacks citations to governed sources (datasets, documents, or evidence artifacts).
- **Draft vs published separation:** if a tool generates story content, it must clearly mark it as draft and keep it out of end-user visibility until reviewed.
- **Evidence linkage:** Story Nodes should reference stable identifiers (STAC Item IDs, DCAT dataset IDs, PROV bundle/activity IDs, graph entity IDs) that resolve in canonical roots.
- **Safety posture:** tools should avoid logging sensitive locations or raw restricted coordinates; prefer generalized/synthetic fixtures in tests.

## 🧪 Validation & CI/CD

### What tools should validate
When applicable, tooling should provide repeatable validators that CI can run deterministically:

- **Docs hygiene:** Markdown protocol checks and link integrity for governed docs.
- **Schema integrity:** STAC/DCAT/PROV JSON validation (and Story Node schema validation where applicable).
- **Catalog integrity rules:** STAC item↔collection integrity and broken-link checks (as adopted).
- **Graph ingest readiness:** validate `data/graph/**` fixtures (required columns/IDs, referential integrity).
- **API boundary:** contract tests for `src/server/` (OpenAPI/GraphQL as adopted) and redaction rules.
- **Security & secrets:** secret scanning and license attribution checks (CI integration is implementation-defined).
- **CI gate behavior:** validate artifacts when present; fail if invalid; skip only when a stage/artifact is not applicable.

### Validation steps (checklist)
- [ ] Markdown protocol validation (front-matter keys, paths, required headings)
- [ ] STAC validation (if STAC artifacts exist)
- [ ] DCAT validation (if DCAT artifacts exist)
- [ ] PROV validation (if PROV bundles exist)
- [ ] Story Node validation (if Story Nodes exist)
- [ ] Graph fixture integrity (if `data/graph/**` is used)
- [ ] API contract tests (if API contracts are touched)
- [ ] Secret scanning / license checks (as adopted)

### Suggested CLI pattern (tool-level contract)
Each tool directory should document a minimal interface in `tools/<tool-name>/README.md`:
- **Usage** (local + CI)
- **Inputs** (paths/env vars; no secrets committed)
- **Outputs** (canonical destinations only)
- **Validation** (what constitutes pass/fail)
- **Security** (secrets/PII/sovereignty notes)

### Example commands (placeholders)
Replace these with repo-accurate commands/scripts (or clearly mark “not confirmed in repo” at the tool level):

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

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Run ID / run manifest pointer | tool wrapper / CI | `mcp/runs/` (recommended) or CI artifacts |
| Schema validation summary | validators | CI logs |
| Artifact checksums | packaging tools | `releases/` (if adopted) or CI artifacts |
| Sovereignty/redaction gate status | policy checks | CI logs + governance review notes |

## 📦 Data & Metadata

### Inputs
| Input | Source | Notes |
|---|---|---|
| Tool-specific config | `tools/**` | Each tool must document required config and defaults (no secrets committed) |
| Canonical subsystem artifacts | `src/**`, `schemas/**`, `docs/**`, `data/**`, `releases/**` | Tools should call canonical modules and validate outputs |
| CI environment variables | `.github/**` | Secrets must come from CI secret stores; never commit secrets into repo |

### Outputs (canonical destinations)
| Output | Canonical destination | Notes |
|---|---|---|
| Derived domain datasets | `data/<domain>/processed/` | Never store derived datasets under `tools/` |
| Catalog + provenance artifacts | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Required for datasets/evidence products |
| Graph import fixtures | `data/graph/csv/`, `data/graph/cypher/` | Import-ready graph artifacts (if used) |
| Release artifacts | `releases/` | Manifests/SBOMs/signed bundles (if adopted) |
| Run logs / run metadata pointers | `mcp/runs/` (recommended) | Prefer pointers/hashes to canonical outputs, not duplicated data |

## 🌐 STAC, DCAT & PROV Alignment

STAC/DCAT/PROV are first-class evidence artifacts. If a tool generates or validates them, it must enforce integrity checks appropriate to each layer.

Canonical global output locations:
- **STAC**: `data/stac/collections/` and `data/stac/items/`
- **DCAT**: `data/catalog/dcat/`
- **PROV**: `data/prov/`
- **Graph fixtures (if used)**: `data/graph/csv/` and `data/graph/cypher/`

## 🧱 Architecture

### Components and contracts
| Component | Contract artifact | Notes |
|---|---|---|
| Deployment scaffolding | Runbook/README + validation steps | Must not bypass security or governance standards |
| CI/build helpers | Repeatable commands + references to canonical schemas/contracts | Prefer calling canonical validators rather than re-implementing |
| Orchestration wrappers | CLI entrypoints + documented inputs/outputs | Must route outputs to canonical destinations |
| Release packaging | Release manifest + SBOM references | Artifacts belong under `releases/` |
| Policy/security gates | Checklists + (optional) machine-enforced validators | Changes may require governance/security review |

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
- [ ] **Telemetry:** if emitting governed telemetry, align with telemetry schemas and docs (if present).

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
| v1.0.2 | 2025-12-27 | Align Tools README to Universal template patterns; add explicit “add a tool” workflow; tighten CI/validation + run manifest guidance; standardize footer style | TBD |
| v1.0.1 | 2025-12-24 | Align `tools/` README to Master Guide v12 + v13 canonical roots; add Story/CI sections; remove non-repo citations | TBD |
| v1.0.0 | 2025-12-23 | Initial `tools/` README | TBD |

---

Footer refs (do not remove):
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

---
