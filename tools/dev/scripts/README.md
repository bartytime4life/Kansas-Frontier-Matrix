---
title: "Tools — Dev Scripts"
path: "tools/dev/scripts/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "README"
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

doc_uuid: "urn:kfm:doc:tools:dev-scripts-readme:v1.0.0"
semantic_document_id: "kfm-tools-dev-scripts-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:dev-scripts-readme:v1.0.0"
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

# Tools — Dev Scripts

## 📘 Overview

### Purpose
This folder contains **developer-facing helper scripts** used to:
- run or orchestrate common KFM workflows locally,
- validate schemas/contracts/catalog outputs,
- reduce “tribal knowledge” for repeatable dev operations,
- provide safe wrappers around tasks that touch `data/`, catalogs, or graph loads.

These scripts are *tooling*; they must **not** replace canonical pipeline code under `src/pipelines/`.

### Scope
In scope:
- local dev automation (setup, validation, smoke checks)
- repeatable wrappers around pipeline steps (ETL → catalogs → graph loads), **without changing** the canonical ordering
- utility scripts for repo hygiene (formatting, lint, checks) if they do not duplicate CI

Out of scope:
- production runtime services
- API/UI code (belongs in `src/server/` and `web/`)
- “one-off” ad hoc scripts without docs/help (if it must exist, park it in a draft/experimental subfolder and document it)

### Audience
- maintainers
- data engineers / pipeline authors
- graph and catalog maintainers
- contributors running local validation and reproduction steps

### Definitions (link to glossary)
- Link: `docs/glossary.md`

### Key artifacts (what this doc points to)
| Artifact | Where | Why it matters |
|---|---|---|
| Dev scripts | `tools/dev/scripts/` | Entry points for repeatable dev tasks |
| Canonical pipeline code | `src/pipelines/` | Source of truth for ETL/transforms |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence metadata products |
| Graph layer | `src/graph/` (and imports under `data/graph/`) | Governed semantics + ingestion |
| API boundary | `src/server/` | UI must not read Neo4j directly |
| UI | `web/` | Map + narrative experience |
| Schemas | `schemas/` | Canonical validation + contract checking |

### Definition of done (for this document)
- [ ] Explains what belongs in this folder (and what does not)
- [ ] Provides a safe “how to run” pattern
- [ ] States the invariants that scripts must not violate
- [ ] Defines output locations (data vs code) and basic provenance expectations
- [ ] Provides a minimal checklist for adding a new script

---

## 🗂️ Directory Layout

### This document
- `tools/dev/scripts/README.md`

### Related repository paths
- `src/pipelines/` — canonical ETL + transforms
- `data/<domain>/{raw,work,processed}/` — pipeline outputs
- `data/stac/collections/` + `data/stac/items/` — STAC artifacts
- `data/catalog/dcat/` — DCAT artifacts
- `data/prov/` — PROV artifacts and run manifests
- `src/graph/` — graph code + ontology bindings
- `src/server/` — API boundary (REST/GraphQL)
- `web/` — React + map UI
- `docs/reports/story_nodes/` — Story Nodes (published/draft)
- `schemas/` — schema + contract validation

### Expected file tree for this sub-area
~~~text
📁 tools/
└── 📁 dev/
    └── 📁 scripts/
        ├── 📄 README.md
        ├── 📄 <script-name>.(sh|py|js)
        └── 📁 <optional-subarea>/
            └── 📄 <script-name>.(sh|py|js)
~~~

> Note: Script inventory is intentionally not enumerated here—prefer discoverability via `--help` and consistent naming.

---

## 🧭 Context

### Background
KFM has a **non-negotiable canonical pipeline ordering**:

ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

Developer scripts may orchestrate steps, but they **must preserve this order** and keep contracts/provenance intact.

### Assumptions
- Scripts are run from the **repo root** (recommended), unless documented otherwise.
- Scripts are expected to be safe by default (no destructive actions without explicit confirmation).
- Any script that writes outputs does so in the correct **data locations**, not under `src/`.

### Constraints / invariants
The following constraints apply to *any script* that touches pipeline outputs, catalogs, graph operations, or story nodes:

1. **No UI direct-to-graph reads**
   - `web/` must not query Neo4j directly; graph access is via the API boundary.

2. **No unsourced narrative**
   - Story Nodes must be provenance-linked and validate before “published.”

3. **Contracts are canonical**
   - Schemas/specs live in `schemas/`, and API contracts live under the API contract area.

4. **Data outputs are not code**
   - Derived datasets belong under `data/<domain>/processed/`, not under `src/`.

5. **Idempotence + determinism (when producing governed outputs)**
   - Scripts that run pipeline steps must be repeatable and deterministic (given the same inputs).
   - Runs should emit provenance artifacts (e.g., under `data/prov/`) and any run manifest required by the pipeline contract.

### Open questions
- Should this folder adopt a single standard runner (e.g., `make` targets) with scripts as thin wrappers?
- Do we want a simple “script registry” file (e.g., `tools/dev/scripts/index.md`) to list stable entrypoints?

### Future extensions
- A small “task taxonomy” (validate / build / ingest / release) to encourage consistent naming and help text.
- Optional CI hooks to ensure every script supports `--help` and has a short header docstring.

---

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  DEV[tools/dev/scripts] --> ETL[src/pipelines]
  ETL --> CAT[Catalogs: data/stac + data/catalog/dcat + data/prov]
  CAT --> GRAPH[src/graph + data/graph imports]
  GRAPH --> API[src/server]
  API --> UI[web]
  UI --> STORY[docs/reports/story_nodes]
  STORY --> FOCUS[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Dev as Developer
  participant Script as Dev Script
  participant Pipe as src/pipelines
  participant Cat as Catalog Outputs
  Dev->>Script: run script (with args)
  Script->>Pipe: invoke pipeline step(s)
  Pipe-->>Cat: write outputs + provenance
  Script-->>Dev: print summary + next steps
~~~

---

## 📦 Data & Metadata

### Inputs
Common input types for scripts in this folder:
- local configuration (paths, domain selection, run parameters)
- existing datasets under `data/`
- schemas/contracts under `schemas/`
- environment variables for local development (never commit secrets)

### Outputs
Scripts should write outputs only to the appropriate locations:
- Derived data: `data/<domain>/work/` and `data/<domain>/processed/`
- Catalogs: `data/stac/` and `data/catalog/dcat/`
- Lineage/provenance: `data/prov/`
- Logs: prefer structured logs to stdout; persist only if there is a governed location for run logs

### Sensitivity & redaction
- Treat any location data, culturally sensitive sites, or personal identifiers as potentially sensitive.
- Do not export raw sensitive content into shared/public folders without applying governance rules.
- Avoid printing secrets or access tokens to stdout.

### Quality signals
For scripts that produce governed artifacts:
- deterministic outputs (stable IDs/keys where applicable)
- idempotent behavior (re-running should not corrupt or duplicate outputs)
- schema validation passes (STAC/DCAT/PROV and/or contract schemas)
- provenance emitted/updated for reproducibility

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
If a script generates or updates STAC:
- Emit to `data/stac/collections/` and `data/stac/items/`
- Validate against `schemas/` and the configured STAC profile

### DCAT
If a script generates or updates DCAT:
- Emit to `data/catalog/dcat/`
- Ensure dataset identifiers match the pipeline contract and remain stable

### PROV-O
If a script runs ETL or generates evidence products:
- Emit provenance bundles to `data/prov/`
- Include run identifiers and enough context to reproduce inputs/outputs

### Versioning
- Avoid encoding “current time” into identifiers unless explicitly part of the contract.
- Prefer stable dataset IDs and explicit version fields rather than random or ad hoc naming.

---

## 🧱 Architecture

### Components
- **Dev scripts (this folder):** wrappers / helpers / local automation
- **Pipeline code:** `src/pipelines/` (canonical transformations)
- **Catalog builders:** produce STAC/DCAT/PROV outputs under `data/`
- **Graph tooling:** loads processed + catalog artifacts into graph layer
- **Contracts & validation:** schemas under `schemas/`, checked in CI

### Interfaces / contracts
- Scripts should provide a discoverable CLI interface:
  - `--help` should explain arguments and outputs
  - `--dry-run` is recommended for scripts with side effects
  - use explicit flags for destructive behavior (e.g., `--force`, `--confirm`)
- The API boundary remains the only supported path for UI consumption of graph/catalog data.

### Extension points checklist (for future work)
When adding a new script:
- [ ] Provide a clear name and `--help`
- [ ] Document inputs, outputs, and where outputs are written
- [ ] Ensure safe defaults (no destructive actions by default)
- [ ] If it writes governed outputs, ensure determinism + provenance emission
- [ ] Add tests if logic exceeds trivial “glue”
- [ ] Update this README if you introduce a new sub-area taxonomy

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
This folder itself does not surface in Focus Mode. However, scripts may:
- generate or validate evidence artifacts referenced by Story Nodes
- assist in Story Node lint/validation workflows
- produce provenance bundles required for publishable narrative content

### Provenance-linked narrative rule
If a script generates Story Nodes or modifies publishable narrative content:
- every claim must map to a cited dataset/document ID
- Story Nodes must validate before publish

### Optional structured controls
- Consider a “publish guard” (lint + validation) script that must pass before any Story Node moves to a `published/` area.

---

## 🧪 Validation & CI/CD

### Validation steps
Recommended checks for scripts (as applicable):
- schema validation for any produced STAC/DCAT/PROV artifacts
- contract tests for API changes (if the script touches contracts)
- linting/formatting for script languages used (shell/python/js)
- link-checking for any documentation generated/updated

### Reproduction
Scripts that run pipelines should:
- print the effective inputs/parameters
- record a run ID (or accept one)
- point to emitted provenance artifacts and output paths
- avoid hidden “magic defaults” that make runs non-reproducible

# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint

### Telemetry signals (if applicable)
| Signal | Where recorded | Purpose |
|---|---|---|
| run_id | `data/prov/` (or run manifest) | reproduction + audit |
| inputs hash | provenance bundle | determinism check |
| outputs list | provenance bundle | traceability |

---

## ⚖ FAIR+CARE & Governance

### Review gates
- Scripts that can delete, overwrite, or redact artifacts should require:
  - explicit flags (`--confirm`, `--force`)
  - code review (requires human review)

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.
- Do not output precise sensitive locations unless governance permits.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial dev-scripts README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
