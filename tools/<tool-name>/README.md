---
title: "Tool — <tool-name> (README)"
path: "tools/<tool-name>/README.md"
version: "v1.0.0"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:tools:<tool-name>:readme:v1.0.0"
semantic_document_id: "kfm-tools-<tool-name>-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:<tool-name>:readme:v1.0.0"
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

# <tool-name>

[⬅️ Back to Tools index](../README.md) *(not confirmed in repo — create `tools/README.md` if missing)*  
[📘 Master Guide](../../docs/MASTER_GUIDE_v12.md)

## 📘 Overview

### Purpose

- Provide **operational tooling** for: `<one-line tool purpose>`.
- This tool lives under `tools/` and **supports** (does not replace) the canonical KFM pipeline:

  **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

- This tool must **route any produced artifacts** to canonical destinations (`data/**`, `docs/**`, etc.) rather than storing derived outputs under `tools/`.

### Scope

| In Scope | Out of Scope |
|---|---|
| Repeatable local/CI commands that wrap or validate canonical subsystems | Re-implementing core ETL / graph / API logic that belongs in `src/**` |
| Tool-specific configs, runbooks, and safety checks (secret/PII leakage, determinism) | Storing derived datasets under `tools/` |
| Helper scripts that invoke canonical validators and schema checks | Changing governance/policy via automation (policy is authored in `docs/governance/**`) |

### Audience

- Primary: Contributors running/validating KFM pipelines, catalogs, graph, API, UI in dev/CI
- Secondary: Governance/security reviewers checking that tooling does not bypass safeguards

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **Canonical destination**: the approved repo root for a given artifact class (`data/**`, `schemas/**`, `docs/**`, etc.)
  - **Deterministic**: same inputs + config → same outputs (byte-stable where required)
  - **Idempotent**: re-running does not create duplicates or inconsistent state
  - **Evidence product**: any dataset/analysis output that must ship with STAC/DCAT/PROV

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `tools/<tool-name>/README.md` | TBD | Tool-specific contract + runbook |
| Tools index | `tools/README.md` | TBD | Shared tooling conventions |
| Canonical pipeline guide | `docs/MASTER_GUIDE_v12.md` | TBD | Non-negotiable pipeline ordering |
| Universal template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Structure + governance requirements |
| Schemas | `schemas/` | TBD | Schemas are canonical here (do not fork under tools) |
| Pipelines | `src/pipelines/` | TBD | Tool should call into canonical pipeline code (if applicable) |
| Graph | `src/graph/` | TBD | Ontology bindings, migrations, ingest |
| Server | `src/server/` | TBD | API boundary; UI must not bypass |
| UI | `web/` | TBD | Frontend; must not query Neo4j directly |
| Story Nodes | `docs/reports/story_nodes/` | TBD | Narrative artifacts; provenance-first |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Tool purpose, inputs, outputs, and canonical destinations documented
- [ ] Any data/product outputs explicitly mapped to `data/**` and catalogs (`data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`) where applicable
- [ ] Validation steps listed and repeatable (CI + local)
- [ ] Security + sovereignty/CARE considerations explicitly stated
- [ ] Footer refs present (governance + ethics + sovereignty + master guide + template)

## 🗂️ Directory Layout

### This document

- `path`: `tools/<tool-name>/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Top-level tooling | `tools/` | Operational wrappers, helpers, runbooks (no derived datasets) |
| Data lifecycle | `data/` | Raw/work/processed datasets and published/derived outputs |
| Catalog outputs | `data/stac/` | STAC Collections + Items |
| Catalog outputs | `data/catalog/dcat/` | DCAT dataset/distribution records |
| Provenance outputs | `data/prov/` | PROV bundles and lineage artifacts |
| Schemas/specs | `schemas/` | JSONSchema/SHACL/etc (canonical) |
| Pipelines | `src/pipelines/` | ETL + catalog generation logic |
| Graph | `src/graph/` | Ontology + ingest + migrations |
| API boundary | `src/server/` | Contracted API access layer |
| UI | `web/` | React/Map UI (no direct graph reads) |
| Tests | `tests/` | Unit/integration tests |
| Experiments/runs | `mcp/` | Experiments, run logs, model/evidence metadata |

### Expected file tree (tool-local)

~~~text
📁 tools/
└── 📁 <tool-name>/
    ├── 📄 README.md                          # 📌 This file
    │
    ├── 📁 configs/                           # (optional) tool config templates — NO SECRETS
    │   └── 📄 example.<ext>                  # (optional) example config
    │
    ├── 📁 scripts/                           # (optional) entrypoints/wrappers
    │   └── 📄 run.<ext>                      # (optional) run script (documented below)
    │
    └── 📁 fixtures/                          # (optional) small synthetic fixtures for tests (no sensitive data)
        └── 📄 README.md                      # (optional) what fixtures are + how generated
~~~

> **Rule:** Do not commit large outputs, derived datasets, or provenance bundles under `tools/`. Route outputs to canonical destinations (`data/**`, `docs/**`, `mcp/**`) as defined below.

## 🧭 Context

### Background

`tools/<tool-name>/` exists to provide a repeatable, documented way to run or validate a specific workflow **without** bypassing the KFM architecture boundaries.

### Assumptions

- The tool is a wrapper/helper; **core logic** remains in canonical roots (`src/**`, `schemas/**`, `data/**`, `docs/**`).
- If the tool creates dataset/evidence outputs, it also creates or updates:
  - STAC Items/Collections
  - DCAT dataset/distribution records
  - PROV run/activity lineage

### Constraints / invariants (non-negotiable)

- **No UI direct-to-graph reads:** `web/` must never query Neo4j directly; all graph access is via `src/server/`.
- **Contracts are canonical:** schemas/specs must live in `schemas/`, and API contracts must validate in CI.
- **Data outputs are not code:** derived datasets belong under `data/<domain>/processed/`, not under `src/` and not under `tools/`.
- **Secrets never committed:** configs in `tools/**` must be secret-free (use env/secret store instead).

### Open questions

| Question | Owner | Status |
|---|---|---|
| What runtime does this tool use (Python/Node/etc.)? | TBD | not confirmed in repo |
| Does this tool generate STAC/DCAT/PROV, or only validate? | TBD | TBD |
| Where should run logs/telemetry be recorded for this tool? | TBD | Prefer `mcp/runs/` or an existing governed location (avoid inventing new roots) |

### Future extensions

- Add schema-validated config format for this tool *(schemas live in `schemas/`)*.
- Add CI job that runs this tool in “validate-only” mode and fails on contract drift.
- Add a run manifest output (checksums + inputs + outputs) for reproducibility.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  T["tools/<tool-name>"] --> P["src/pipelines/* (ETL + catalogs)"]
  P --> C["Catalogs<br/>data/stac + data/catalog/dcat + data/prov"]
  C --> G["Graph<br/>src/graph → Neo4j"]
  G --> A["API Boundary<br/>src/server"]
  A --> U["UI<br/>web"]
  U --> S["Story Nodes<br/>docs/reports/story_nodes"]
  S --> F["Focus Mode"]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Source | Notes |
|---|---|---|
| Tool config | `tools/<tool-name>/configs/` | Must be secret-free; document defaults |
| Schemas/contracts | `schemas/**` | Canonical; tool references these |
| Pipeline/graph/api code | `src/**` | Tool should call canonical modules |
| Domain data | `data/**` | Reads from canonical lifecycle roots (raw/work/processed) |

### Outputs (map to canonical destinations)

| Output | Canonical destination | Notes |
|---|---|---|
| Derived datasets | `data/<domain>/processed/` | Never store under `tools/` |
| STAC Collections/Items | `data/stac/collections/` + `data/stac/items/` | Required for datasets/evidence products |
| DCAT records | `data/catalog/dcat/` | Minimum title/description/license/keywords |
| PROV bundles | `data/prov/` | Must link sources + run/activity IDs |
| Run logs / metadata | Prefer `mcp/runs/` | Use existing governed location; avoid inventing new roots |

### Sensitivity, redaction, and safe outputs

- If the tool touches restricted/sensitive locations or culturally sensitive content:
  - apply redaction/generalization rules,
  - prefer aggregate outputs for public artifacts,
  - document decisions and flags in provenance + governance notes.

## 🌐 STAC, DCAT & PROV Alignment

### Policy for every dataset / evidence product

For each dataset or evidence product produced or updated by this tool:

- STAC Collection + Item(s)
- DCAT mapping record (minimum title/description/license/keywords)
- PROV activity describing lineage (sources + run/activity identifiers)
- Version lineage links reflected in catalogs and (where applicable) the graph

### Provenance requirements (minimum)

- `prov:wasDerivedFrom`: list source IDs
- `prov:wasGeneratedBy`: pipeline activity/run ID
- Record checksums for:
  - input packs / source snapshots (where applicable)
  - outputs (STAC/DCAT/PROV bundles, processed datasets)

### Identifier linkage expectation

Graph nodes and APIs should reference:

- STAC Item IDs
- DCAT dataset ID
- PROV activity ID

This enables Focus Mode to resolve “what is this data?” into a traceable lineage bundle.

## 🧱 Architecture

### Responsibilities

- Provide a repeatable CLI/workflow for `<tool-name>` that:
  - invokes canonical code paths,
  - validates outputs against canonical schemas,
  - produces governance-safe artifacts.

### Interfaces / contracts

| Interface | Contract artifact | Notes |
|---|---|---|
| Tool config | `schemas/**` (preferred) | Tool config schema should live in `schemas/` |
| Catalog generation/validation | STAC/DCAT/PROV schemas | Required when emitting dataset artifacts |
| Graph boundary | `src/graph/**` | Keep label/edge stability; migrations required for breaking changes |
| API boundary | `src/server/**` contracts | UI must not bypass API |
| UI integration | `web/**` + UI registry schemas | Avoid data leakage via map interactions |

### Extension points checklist (for future work)

- [ ] Data: outputs land in canonical `data/**` roots; no derived outputs committed under `tools/`
- [ ] STAC: if generating STAC, create/validate collections + items
- [ ] DCAT: if generating DCAT, ensure dataset metadata + license/attribution present
- [ ] PROV: if generating PROV, include sources + activity/run identifiers + checksums
- [ ] Graph: if touching graph schema, update ontology + migrations; keep stable identifiers
- [ ] API/UI: if adding exposure, update API contracts + tests; ensure UI uses API only

## 🧪 Validation & CI/CD

### Minimum checks (expected)

- [ ] Markdown lint + required sections present
- [ ] Schema validation (STAC/DCAT/PROV; tool config schema if applicable)
- [ ] Link integrity (docs + references)
- [ ] Secret scan + PII scan (configs and logs must be safe)
- [ ] Determinism checks (stable ordering, fixed seeds if used, checksums recorded)
- [ ] Unit/integration tests (if tool has executable logic)

### Local reproduction (placeholders)

~~~bash
# NOTE: Commands are placeholders; replace with repo-approved tooling.

# A) Show help
# <tool-command> --help

# B) Validate-only mode (recommended)
# <tool-command> validate --config tools/<tool-name>/configs/example.<ext>

# C) Run (writes outputs ONLY to canonical destinations)
# <tool-command> run --config tools/<tool-name>/configs/example.<ext>

# D) Verify catalogs + provenance
# <repo-command> validate-stac
# <repo-command> validate-dcat
# <repo-command> validate-prov
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Tool run start/end + status | CLI logs / CI logs | `mcp/runs/` (preferred) or existing subsystem telemetry |
| Schema failures | Validator output | CI logs + governed telemetry location |
| Governance gate outcomes | Tool run manifest | `data/prov/` (if provenance emitted) |

## ⚖ FAIR+CARE & Governance

### Review gates

Changes that typically require elevated review:

- Any output that increases access to sensitive/restricted information
- Any tool behavior that publishes new public artifacts (datasets, catalogs, story nodes)
- Any permission/scope increase (if this tool authenticates to external systems)

> Review roles/process are **not confirmed in repo** — follow `docs/governance/ROOT_GOVERNANCE.md`.

### CARE / sovereignty considerations

- If this tool processes Indigenous, culturally sensitive, or sovereignty-controlled data:
  - follow `docs/governance/SOVEREIGNTY.md`,
  - prefer aggregation/generalization in public products,
  - fail closed when classification is unclear (require human review).

### AI usage constraints

- Allowed (doc-level): summarize, structure extraction, translation, keyword indexing
- Prohibited: generating policy; inferring sensitive locations (directly or indirectly)
- Any AI-assisted outputs must remain evidence-linked (STAC/DCAT/PROV and/or graph IDs)

## 🕰️ Version History

| Version | Date | Summary | Author | PR / Issue |
|---|---:|---|---|---|
| v1.0.0 | 2025-12-27 | Initial scaffold for `tools/<tool-name>` README | TBD | TBD |

---

Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Tools index: `tools/README.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---

