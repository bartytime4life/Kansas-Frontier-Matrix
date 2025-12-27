---
title: "Tools — KFM Operational Tooling and Deployment Scaffolding"
path: "tools/README.md"
version: "v1.0.3"
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

doc_uuid: "urn:kfm:doc:tools:readme:v1.0.3"
semantic_document_id: "kfm-tools-readme-v1.0.3"
event_source_id: "ledger:kfm:doc:tools:readme:v1.0.3"
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

**At a glance**
- `tools/` is where we keep **wrappers, runbooks, validators, packaging helpers, and deployment scaffolding** that operate *around* the canonical pipeline.
- `tools/` must not become a second implementation home for ETL, graph, API, UI, or story publishing.
- Tools may **validate** and **orchestrate**; canonical subsystems **implement**.

---

## 📘 Overview

### Purpose
- Provide a canonical home for **operational tooling** that supports building, validating, packaging, and operating the KFM pipeline.
- Hold **deployment-oriented scaffolding** and ops glue that is intentionally out of scope for core architecture docs.
- Serve as the “ops + orchestration edge” while preserving the canonical pipeline ordering and artifact placement rules.

> Cloud deployment specifics belong under `tools/` and/or a separate ops repository (if adopted). This folder is where repo-contained deployment scaffolding should live.

### Scope

**In scope**
- Deployment/runbooks and environment scaffolding that supports the system (local dev, CI parity, staging scaffolds).
- Validators that enforce Markdown protocol, schema integrity (STAC/DCAT/PROV/story nodes), repo lint, and release packaging checks.
- Wrapper scripts that orchestrate canonical subsystems (ETL/catalog/graph/API/UI/story) **without** duplicating subsystem logic.
- Release packaging helpers (manifests/SBOM/checksum scaffolding) that write into canonical release roots.
- “Promotion” tooling that moves/validates artifacts into canonical locations (when adopted), e.g., `work/ → processed/` with provenance pointers.

**Out of scope**
- Core pipeline implementations (canonical home: `src/pipelines/`).
- Graph build/migrations and ontology enforcement logic (canonical home: `src/graph/`).
- Production API/server implementation code (canonical home: `src/server/`).
- UI application code (canonical home: `web/`).
- Schemas/specs (canonical home: `schemas/`).
- Derived datasets or catalog/provenance outputs committed under `tools/` (canonical homes: `data/**`, `releases/`).

### Audience
- KFM maintainers (data engineering, catalogs, graph/ontology, API, UI, narrative/story).
- Contributors running builds locally or in CI.
- Deployment/ops owners.

### Definitions
- Glossary: `docs/glossary.md` *(not confirmed in repo — repair link once glossary location is finalized)*

Key terms used in this document:
- **Contract artifact**: a machine-validated schema/spec (JSON Schema, OpenAPI, GraphQL SDL, UI registry schema).
- **Evidence artifact**: catalog + provenance outputs consumed downstream (STAC/DCAT/PROV and derived evidence products).
- **Domain pack**: minimal set that lets a domain participate in the pipeline (staging + mapping + tests + docs).
- **Run manifest**: a small record that captures how to reproduce a run (inputs, config, commit SHA, versions, parameters). Recommended location: `mcp/runs/` (as pointers + hashes, not duplicated data).
- **Repo lint**: deterministic checks that enforce naming/placement rules and prevent drift (e.g., duplicate subsystem homes).
- **Tool (KFM sense)**: code/config under `tools/` that wraps, validates, packages, or deploys canonical subsystems and writes outputs only to canonical destinations.

### Key artifacts (what this folder should link to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Canonical pipeline ordering + invariants + expected top-level layout |
| v13 Redesign Blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Core Team | Canonical roots + CI readiness gates; notes deployment specifics belong in `tools/` |
| Repo structure standard (v12) | `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md` | KFM Core Team | Not confirmed in repo; add/repair once standardized |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs maintainers | Not confirmed in repo; governs tildes/code fences, headings, front-matter checks |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs maintainers | Default for governed guides/runbooks/READMEs |
| Story Node Template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative maintainers | Story nodes consumed by Focus Mode |
| API Contract Extension Template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Contract-first API changes |
| Schemas (contracts) | `schemas/` | Contract owners | STAC/DCAT/PROV/story nodes/UI/telemetry schemas (as adopted) |
| API boundary | `src/server/` | API maintainers | Contracted boundary between UI and graph/catalogs |
| API contracts | `src/server/contracts/` | API maintainers | Canonical home if present; must validate in CI |
| CI workflows | `.github/workflows/` | CI owners | Workflows that may call tools/validators (if present) |
| Releases | `releases/` | Release owners | Manifests, SBOMs, signed bundles, telemetry snapshots (if adopted) |
| Data lifecycle + outputs | `data/` + `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Data maintainers | Canonical destinations for datasets + evidence artifacts |

### Definition of done (for this README)
- [x] Front-matter complete and `path` matches `tools/README.md`.
- [x] Scope clearly distinguishes what belongs in `tools/` vs canonical subsystem roots.
- [x] The “add a tool” pattern is documented and repeatable.
- [x] Contains approved headings for **Story Node & Focus Mode integration** and **Validation & CI/CD**.
- [x] Uses canonical pipeline ordering and invariants; avoids introducing duplicate subsystem homes.
- [ ] Repo lint / Markdown protocol checks run (CI or local).
- [ ] Maintainer review.

---

## 🗂️ Directory Layout

### This document
- `path`: `tools/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| **Repo metadata + policy** | `.github/` | Workflows, security policy, contribution templates |
| **CI workflows** | `.github/workflows/` | Build/test/validate gates *(if present)* |
| **Releases** | `releases/` | Bundles (SBOMs/manifests/attestations) and release metadata *(if adopted)* |
| **MCP / experiments** | `mcp/` | Run manifests, experiment logs, model cards, evaluation artifacts |
| **Data domains + catalogs** | `data/` | Domain staging + processed data; global catalog/provenance outputs |
| **Documentation** | `docs/` | Governed docs, standards, templates, reports |
| **Schemas** | `schemas/` | Machine-validated schemas/specs (STAC/DCAT/PROV/story nodes/ui/telemetry/etc.) |
| **Pipelines** | `src/pipelines/` | ETL, transforms, catalog builders (writes outputs to `data/**`) |
| **Graph** | `src/graph/` | Ontology, constraints, migrations, ingest code |
| **API boundary** | `src/server/` | Contracted access layer (REST/GraphQL), redaction, query services |
| **Frontend** | `web/` | React-based UI (map + Focus Mode UX) |
| **Story Nodes** | `docs/reports/story_nodes/` | Narrative artifacts consumed by Focus Mode *(draft/published split not confirmed in repo)* |
| **Tests** | `tests/` | Automated tests for contracts and behaviors |
| **Tools** | `tools/` | Operational tooling and deployment scaffolding |

> Some paths above reflect target/standardized structure; if a path is missing in the current repo state, treat it as **not confirmed in repo** and repair links once canonical locations are finalized.

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
- `tools/<tool-name>/README.md` must include:
  - Usage (local + CI)
  - Inputs (paths/env vars; no secrets committed)
  - Outputs (canonical destinations only)
  - Validation (what constitutes pass/fail)
  - Security (secrets/PII/sovereignty notes)
  - Reproducibility (manifest pointer + checksums)

2) **Define a minimal interface**
- Prefer a single entrypoint under `bin/` or `scripts/`.
- Tool entrypoints should be CI-friendly:
  - deterministic behavior
  - non-zero exit code on failure
  - structured logs where practical

3) **Keep outputs out of `tools/`**
- Data + evidence outputs go to canonical roots:
  - `data/<domain>/{raw,work,processed}/`
  - `data/stac/`, `data/catalog/dcat/`, `data/prov/`
  - `data/graph/` (fixtures)
  - `releases/` (packaging artifacts, if adopted)

4) **Emit reproducibility pointers**
- Record a run manifest (or pointer) under `mcp/runs/` that references produced artifacts by stable IDs and/or checksums (no duplicated datasets).
- If provenance is generated, ensure PROV bundles land under `data/prov/`.

5) **Wire validation into CI (if applicable)**
- Validators should be callable in CI, with deterministic outcomes:
  - validate if present
  - fail if invalid
  - skip if not applicable (when inputs/roots are absent)

6) **Add tests where appropriate**
- Put tool-specific tests under `tools/<tool-name>/tests/` and/or `tests/` depending on project conventions.

---

## 🧭 Context

### Background
KFM’s architecture is intentionally split into canonical subsystem homes (ETL, catalogs, graph, API, UI, story). `tools/` exists so we can run, validate, package, and deploy **without** blurring those boundaries.

The canonical flow is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

`tools/` supports that flow, but does not replace any canonical subsystem root.

### Assumptions
- Operational work should prefer **thin wrappers** that call canonical modules (rather than duplicating implementations).
- Contracts and evidence artifacts must be validated consistently in CI and local dev.
- Governance and redaction rules apply across all stages; operational convenience must not bypass them.

### Constraints and invariants (non-negotiables)
- **One canonical home per subsystem:** avoid “mystery duplicates.”
- **No UI direct-to-graph reads:** `web/` must never query Neo4j directly; all graph access is via `src/server/`.
- **No unsourced narrative:** published Story Nodes must be provenance-linked and must validate; Focus Mode consumes provenance-linked content only.
- **Contracts are canonical:** schemas/specs live in `schemas/` and API contracts (if used) live under the API boundary (commonly `src/server/contracts/`).
- **Data outputs are not code:** derived datasets belong under `data/<domain>/processed/`, not in `src/` or `tools/`.
- **Repo lint discipline:** avoid drift patterns (e.g., duplicate subsystem homes; malformed README names; YAML front-matter where it doesn’t belong).

### Open questions
| Question | Owner | Target |
|---|---|---|
| Do we standardize a common tool interface (e.g., `make`, `task`, `python -m`, `node`) for local + CI execution? | Maintainers | v13.0.0 |
| Where is the single canonical “run manifest” home: `mcp/runs/` vs `data/prov/` vs `releases/<version>/`? | Provenance + CI owners | v13.0.0 |
| What is the minimum contract set required for CI green (stac/dcat/prov/storynodes/ui/telemetry)? | Contract owners | v13.0.0 |
| Do we adopt SHACL validation for JSON-LD bundles now or later? | Catalog + graph owners | v13.1.0 |
| Do we want “promotion tooling” standardized (work → processed + catalog + prov) as a first-class tool family? | Data engineering | v13.1.0 |

### Future extensions
- Reproducible “domain pack generator” tooling (scaffolds domain staging + mapping + tests + docs).
- Release attestation tooling (SBOMs, signing, verification) under `releases/` (if adopted).
- Optional contract enforcement for UI registries, telemetry, and story node assets when those roots exist.

---

## 🗺️ Diagrams

### Tooling placement in the canonical flow
~~~mermaid
flowchart LR
  T[tools wrappers + scaffolding] --> P[src/pipelines]
  P --> C[data catalogs stac dcat prov]
  C --> X[data graph fixtures]
  X --> G[src/graph -> neo4j]
  G --> A[src/server api boundary]
  A --> U[web ui]
  U --> S[docs/reports/story_nodes]
  S --> F[focus mode]
  T --> R[releases packaging]
  T --> M[mcp/runs manifests]
~~~

### Typical validation execution (local or CI)
~~~mermaid
sequenceDiagram
  participant Dev as Developer / CI
  participant Tool as tools/<tool>
  participant Pipe as src/pipelines
  participant Data as data/**
  participant Val as validators (schemas/tests)

  Dev->>Tool: run tool (validate/build/package)
  Tool->>Pipe: call canonical module (if applicable)
  Pipe->>Data: write outputs to canonical destinations
  Tool->>Val: run protocol + schema + contract checks
  Val-->>Tool: pass/fail + summary
  Tool-->>Dev: exit code + report (CI gate)
~~~

---

## 📦 Data & Metadata

### Data lifecycle (required staging)
For each domain under `data/<domain>/`:
- `raw/` — immutable source snapshots
- `work/` — intermediate transforms
- `processed/` — normalized outputs used for catalogs and graph ingest

Global metadata outputs:
- STAC: `data/stac/collections/` and `data/stac/items/`
- DCAT: `data/catalog/dcat/`
- PROV: `data/prov/`
- Graph import: `data/graph/csv/` and `data/graph/cypher/`

### Inputs
| Input | Source | Notes |
|---|---|---|
| Tool config (examples only) | `tools/**` | No secrets committed; use `.env.example` patterns if adopted |
| Canonical subsystem code | `src/**` | Tools should call canonical modules rather than re-implement |
| Contracts/schemas | `schemas/**` | Tools validate outputs against these schemas |
| Docs/templates | `docs/**` | Tools may validate doc structure/links/protocol |
| CI environment variables | `.github/**` | Secrets must come from CI secret stores |

### Outputs (canonical destinations only)
| Output | Canonical destination | Notes |
|---|---|---|
| Derived domain datasets | `data/<domain>/processed/` | Never store derived datasets under `tools/` |
| Catalog + provenance artifacts | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Required for datasets/evidence products |
| Graph import fixtures | `data/graph/csv/`, `data/graph/cypher/` | Import-ready graph artifacts (if used) |
| Release artifacts | `releases/` | Manifests/SBOMs/signed bundles (if adopted) |
| Run metadata pointers | `mcp/runs/` (recommended) | Prefer pointers/hashes; avoid duplicating data |

---

## 🌐 STAC, DCAT & PROV Alignment

STAC/DCAT/PROV are first-class evidence artifacts. If a tool generates or validates them, it must enforce integrity checks appropriate to each layer.

Canonical global output locations:
- **STAC**: `data/stac/collections/` and `data/stac/items/`
- **DCAT**: `data/catalog/dcat/`
- **PROV**: `data/prov/`
- **Graph fixtures (if used)**: `data/graph/csv/` and `data/graph/cypher/`

Minimum expectations when artifacts exist:
- STAC item↔collection integrity holds.
- DCAT records include license/attribution and stable IDs.
- PROV bundles identify activities/agents and link raw → work → processed → evidence.

---

## 🧱 Architecture

### Components and contracts
| Component | Contract artifact | Notes |
|---|---|---|
| Deployment scaffolding | Runbook/README + validation steps | Must not bypass security or governance standards |
| CI/build helpers | Repeatable commands + canonical references | Prefer calling canonical validators rather than re-implementing |
| Orchestration wrappers | CLI entrypoints + documented IO | Outputs must route to canonical destinations |
| Release packaging | Release manifest + SBOM references | Artifacts belong under `releases/` |
| Policy/security gates | Checklists + machine validators (optional) | Changes may require governance/security review |

### Extension points checklist (tooling-safe)
When adding new tooling under `tools/`, ensure pipeline alignment:

- [ ] **Placement:** tool source/config stays in `tools/`; outputs go to canonical roots (`data/**`, `releases/`, `mcp/runs/`).
- [ ] **Determinism:** repeatable behavior in CI (stable IDs, pinned deps, fixed seeds if relevant).
- [ ] **Catalogs:** if generating STAC/DCAT/PROV, enforce schema validation and integrity checks.
- [ ] **Graph:** do not introduce UI-to-graph coupling; keep graph access behind the API boundary.
- [ ] **API:** if tooling depends on endpoints, link to the relevant contract docs and tests.
- [ ] **UI:** tools must not create direct Neo4j access paths for `web/`.
- [ ] **Story:** if tooling affects story publication, enforce provenance/citation validation workflows.
- [ ] **Telemetry:** if emitting governed telemetry, align with telemetry schemas/docs (if present).

---

## 🧠 Story Node & Focus Mode Integration

Tools may touch narrative artifacts in two ways:
1) **Validating** Story Nodes and their evidence links.
2) Generating **draft** scaffolds for human review (never auto-publish).

Rules of engagement:
- **No unsourced narrative:** tools must not “publish” or auto-promote story content that lacks citations to governed sources (datasets, documents, evidence artifacts).
- **Draft vs published separation:** if a tool generates story content, it must clearly mark it as draft and keep it out of end-user visibility until reviewed.
- **Evidence linkage:** Story Nodes should reference stable identifiers (STAC Item IDs, DCAT dataset IDs, PROV bundle/activity IDs, graph entity IDs) that resolve in canonical roots.
- **Safety posture:** tools should avoid logging sensitive locations or raw restricted coordinates; prefer generalized/synthetic fixtures in tests.

Optional structured controls (Story Node hints that tools may validate):
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### What tools should validate
When applicable, tooling should provide repeatable validators that CI can run deterministically:

- **Docs hygiene:** Markdown protocol checks and link integrity for governed docs.
- **Schema integrity:** STAC/DCAT/PROV JSON validation (and Story Node schema validation where applicable).
- **Catalog integrity rules:** STAC item↔collection integrity and broken-link checks (as adopted).
- **Graph ingest readiness:** validate `data/graph/**` fixtures (required columns/IDs, referential integrity).
- **API boundary:** contract tests for `src/server/` (OpenAPI/GraphQL as adopted) and redaction rules.
- **Security & sovereignty:** secret scanning and policy-aligned checks (implementation-defined).
- **CI gate behavior:** validate artifacts when present; fail if invalid; skip only when not applicable.

### Validation steps (checklist)
- [ ] Markdown protocol validation (front-matter keys, paths, required headings)
- [ ] Repo lint rules (naming + duplicate canonical homes + prohibited patterns)
- [ ] Schema validation (STAC/DCAT/PROV, Story Nodes, UI registries — as applicable)
- [ ] Graph fixture integrity (if `data/graph/**` is used)
- [ ] API contract tests (if API contracts are touched)
- [ ] Security & sovereignty scanning gates (as applicable)

### Reproduction (placeholders)
Replace these with repo-accurate commands/scripts (or clearly mark “not confirmed in repo” at the tool level):

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate docs (markdown protocol / links)
# 2) validate schemas (stac/dcat/prov/storynodes)
# 3) run tests (unit/integration)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Run ID / manifest pointer | tool wrapper / CI | `mcp/runs/` (recommended) or CI artifacts |
| Schema validation summary | validators | CI logs |
| Artifact checksums | packaging tools | `releases/` (if adopted) or CI artifacts |
| Sovereignty/redaction gate status | policy checks | CI logs + governance review notes |

---

## ⚖ FAIR+CARE & Governance

### Review gates
- Follow the governance, ethics, and sovereignty references in this file’s front-matter for any tool that affects:
  - data handling or publication,
  - access control, redaction/generalization,
  - story publication workflows,
  - contract/schema changes,
  - CI enforcement behavior.

### CARE / sovereignty considerations
- If tooling processes culturally sensitive content or restricted locations, it must align with sovereignty policy and domain-specific redaction requirements.
- Prefer synthetic fixtures and generalized coordinates for tests when sensitive locations are involved.
- Ensure operational logs do not leak restricted coordinates, identifiers, or assets.

### AI usage constraints
- This document permits summarization/structure extraction/translation/keyword indexing.
- This document prohibits generating policy or inferring sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.3 | 2025-12-27 | Universal-template alignment pass; clarified invariants, reordered sections to match governed structure, added open questions + repo lint discipline | TBD |
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
