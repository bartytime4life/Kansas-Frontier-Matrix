---
title: "tools/ — Tooling & Operations"
path: "tools/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:tools:readme:v1.0.0"
semantic_document_id: "kfm-tools-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:readme:v1.0.0"
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

# tools/ — Tooling & Operations

## 📘 Overview

### Purpose

- Define what belongs in `tools/` and how tooling should be organized so it supports (and does not bypass) KFM’s governed pipeline and contracts.
- Provide an index + conventions for operational tooling, developer utilities, and deployment/environment specifics (when present).

### Scope

| In Scope | Out of Scope |
|---|---|
| Operational tooling (runbooks, environment bootstrapping, deployment-specific assets, backup/restore helpers). | Production subsystem code. Keep canonical code under: `src/pipelines/`, `src/graph/`, `src/server/`, `web/`. |
| Validation helpers (schema checks for catalogs, story nodes, UI registries). | Canonical data artifacts (STAC/DCAT/PROV, processed datasets). These must live under `data/**` (not under `tools/`). |
| Developer utilities (local setup scripts, repo hygiene helpers). | Governed design/narrative documentation (belongs under `docs/**`). |
| Release/packaging helpers (if used). | Secrets/credentials and any sensitive tokens (never committed). |

### Audience

- Primary: maintainers (data engineering, catalog maintainers, graph/ontology, API, UI, ops).
- Secondary: contributors adding new tools, validators, or operational workflows.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: tool, run manifest, validation, canonical home, deployment specifics.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Tooling README | `tools/README.md` | KFM Maintainers | This file |
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Maintainers | Canonical pipeline ordering + system inventory |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Maintainers | Canonical homes + contract-first rules |
| Repo Structure Standard v12 | `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md` | KFM Maintainers | not confirmed in repo |
| Tool-specific docs | `tools/**/README.md` | Tool owner | Required for any non-trivial tool |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (and `path` matches file location)
- [ ] Directory layout reflects current `tools/` contents (or clearly marks “recommended” structure)
- [ ] Tool index updated when new tooling is added
- [ ] Security + sovereignty constraints stated (no secrets, no sensitive leakage)
- [ ] Validation expectations stated (schemas/contracts/provenance where applicable)

## 🗂️ Directory Layout

### This document

- `path`: `tools/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Tooling & ops | `tools/` | Operational tooling + helper scripts + deployment specifics (when present) |
| ETL / pipelines | `src/pipelines/` | Deterministic transforms; outputs in `data/**` |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV artifacts (contract outputs) |
| Graph | `src/graph/` + `data/graph/` | Ontology-governed ingest + import artifacts |
| API boundary | `src/server/` | Contracts, redaction/generalization, query services |
| Web UI | `web/` | React/Map UI, Focus Mode UX |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/storynodes/ui/telemetry, etc.) |
| Tests | `tests/` | Unit/integration/contract tests |
| Releases | `releases/` | Manifests, SBOMs, signed bundles, telemetry snapshots (if used) |

### Repo root structure (context)

~~~text
📁 .
├── 📁 .github/
├── 📁 data/
├── 📁 docs/
├── 📁 mcp/
├── 📁 schemas/
├── 📁 src/
├── 📁 tests/
├── 📁 tools/
├── 📁 web/
└── 📁 releases/
~~~

### `tools/` structure (recommended; create folders only as needed)

> This is a recommended convention for future organization. Do not create empty directories.

~~~text
📁 tools/
├── 📄 README.md
├── 📁 ops/                 # deployment + runtime operations (optional)
│   └── 📄 README.md         # runbooks + entry points
├── 📁 dev/                 # local developer helpers (optional)
├── 📁 validate/            # schema/catalog/story validators (optional)
└── 📁 ci/                  # CI helper scripts (optional)
~~~

### Tool index

Maintain this table as tools are added so contributors can discover entry points quickly.

| Tool | Stage(s) | Entry point | Writes to | Notes |
|---|---|---|---|---|
| (add tool) | ETL / Catalog / Graph / API / UI / Ops | `tools/<area>/<tool>/...` | `data/**` / `releases/**` / reports | Must document inputs/outputs + safety constraints |

## 📦 Data & Contracts

### Inputs

Tooling must explicitly document (in its own `tools/**/README.md`) any inputs it consumes, including:

- Data inputs under `data/<domain>/{raw,work,processed}/` (and whether it reads `raw` vs `processed`)
- Catalog artifacts under `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`
- Schemas under `schemas/**`
- Configuration files checked into the repo (never secrets)
- Environment variables required at runtime (documented via `.env.example` or equivalent, if used)

### Outputs

As a rule:

- **Persistent outputs** go to canonical homes (never to `tools/`):
  - data products → `data/**`
  - catalogs/provenance → `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`
  - graph import artifacts → `data/graph/**`
  - release bundles → `releases/**`
- **Ephemeral outputs** (temp files) must be kept out of Git and placed under a local temp directory (tool-defined).

### Contract alignment

If a tool produces or modifies governed artifacts, it must align with the matching contract:

- STAC output must validate against `schemas/stac/**`
- DCAT output must validate against `schemas/dcat/**`
- PROV output must validate against `schemas/prov/**`
- UI registries must validate against `schemas/ui/**`
- Story Node artifacts must validate against Story Node rules/templates under `docs/templates/**` and `schemas/storynodes/**` (if present)
- Any API contract changes must be documented using the API Contract Extension template and backed by contract tests

## 🔗 Architecture & Pipeline Alignment

### Canonical flow (must be preserved)

Tools exist to support the canonical pipeline; they should not create alternate “shadow” paths.

~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph<br/>src/graph + data/graph]
  C --> D[API boundary<br/>src/server]
  D --> E[UI<br/>web]
  E --> F[Story Nodes<br/>docs/reports/story_nodes]
  F --> G[Focus Mode<br/>provenance-linked only]
~~~

### Subsystem dependencies (tooling rules of thumb)

| If your tool touches… | Then it must… | Notes |
|---|---|---|
| ETL runs | be deterministic/idempotent; clearly declare inputs; write outputs to `data/**` | Promote repeatable ETL logic into `src/pipelines/` |
| Catalog generation | emit stable IDs; validate catalogs against `schemas/**` | Catalog artifacts are evidence products |
| Graph ingest | consume only processed + catalog + provenance artifacts | Graph nodes reference STAC/DCAT/PROV IDs |
| API boundary | respect redaction/generalization; keep contracts in `src/server/contracts/` | UI should consume only via API endpoints |
| UI layer registries | validate against `schemas/ui/**` | Avoid “magic” unvalidated config |

### Integration points

- Tools may **wrap** or **invoke** canonical subsystems (pipelines, validators, packaging).
- Tools should not become “the only way” a subsystem can run; prefer promoting stable logic into canonical homes and using tools as thin wrappers/runbooks.

## 🧭 Story Node & Focus Mode Integration

### How `tools/` can contribute to Story Nodes

`tools/` may contain:

- Generators that scaffold Story Node markdown from evidence bundles (optional)
- Validators that check Story Node constraints (front-matter, citations, redaction compliance) (optional)

**But** Story Nodes themselves live under `docs/reports/story_nodes/` (not under `tools/`).

### Evidence + citation hooks

If a tool helps produce narrative content, it must ensure:

- every claim is traceable to STAC/DCAT/PROV identifiers (or other governed evidence IDs),
- sensitive locations are handled per governance rules,
- any AI/predictive output is clearly labeled, opt-in, and includes uncertainty metadata.

## ✅ Validation & CI/CD Expectations

### Validation steps

When adding or changing a tool:

- [ ] Tool has a `tools/**/README.md` that documents: purpose, inputs, outputs, and safety constraints
- [ ] Tool does **not** commit secrets or require credentials in-repo
- [ ] Tool writes persistent outputs only to canonical homes (`data/**`, `releases/**`, etc.)
- [ ] If tool produces governed artifacts, those artifacts validate against `schemas/**`
- [ ] If tool affects API contracts, contract tests exist and pass
- [ ] Tool is deterministic where determinism is required (seeded; pinned versions; stable IDs)

### Telemetry signals (if relevant)

| Signal | Source | Where recorded |
|---|---|---|
| Tool run manifest (if used) | Tool | `data/prov/` or `releases/<version>/` |
| Validation report | Tool | Tool-defined report location (must be documented) |
| CI summary | CI | CI logs + optional repo snapshot location |

## ⚖ FAIR+CARE & Governance

### Sensitivity & sovereignty

Tool authors must explicitly consider:

- Does this tool handle culturally sensitive or restricted data?
- Could outputs leak sensitive locations or personally identifying information?
- If redaction/generalization is required, is it enforced before outputs are persisted?

### Review gates

At minimum, changes that affect any of the following should be treated as **requires human review**:

- deployment/infrastructure tooling
- redaction/generalization behavior
- schema or contract validation logic
- any process that publishes Story Nodes or modifies evidence outputs

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions match intended use.
- Tools that generate text must not create “unsourced narrative.”

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `tools/` README (purpose + conventions + placeholder index) | KFM Maintainers |

---

**Template used:** `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`  
**Pipeline stage(s):** Tooling (cross-cutting across ETL/Catalog/Graph/API/UI/Story)  
**Related standards:** STAC 1.0, DCAT 3, W3C PROV-O (via KFM profiles)  
**See also:**  
- Governance: `docs/governance/ROOT_GOVERNANCE.md`  
- Ethics: `docs/governance/ETHICS.md`  
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
