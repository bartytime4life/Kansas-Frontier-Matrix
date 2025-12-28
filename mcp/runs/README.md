---
title: "MCP Runs — Run Records and Reproducibility Logbook"
path: "mcp/runs/README.md"
version: "v1.1.0"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:mcp:runs:readme:v1.1.0"
semantic_document_id: "kfm-mcp-runs-readme-v1.1.0"
event_source_id: "ledger:kfm:doc:mcp:runs:readme:v1.1.0"
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

# MCP Runs — Run Records and Reproducibility Logbook

## 📘 Overview

### Purpose
`mcp/runs/` is KFM’s **run logbook**: a human-readable, reviewable record of *what ran*, *why*, *with what inputs/config*, *what changed*, and *where the canonical artifacts landed*. It is designed to make pipeline executions, experiments, and validations **auditable and reproducible**.

This directory **complements** (does not replace) KFM’s canonical artifact homes: `data/**` for outputs and catalogs, `src/**` for code, and `docs/**` for governed narrative.

### Scope

| In Scope | Out of Scope |
|---|---|
| Run records for experiments, validations, and analysis work (intent → setup → steps → results → pointers). | Canonical STAC/DCAT/PROV outputs (these live under `data/…`). |
| Pointers to evidence artifacts (STAC Item IDs, DCAT dataset IDs, PROV bundle paths, graph ingest fixtures, API contract versions). | Large binary artifacts, raw data dumps, or duplicate copies of processed datasets. |
| Minimal reproducibility breadcrumbs (commit SHA, config snapshot refs, deterministic seeds, environment notes). | Secrets/credentials, private keys, tokens, sensitive coordinates, or regulated content. |
| Failure records (what failed, where, why, and how to reproduce the failure). | Unsourced narrative conclusions (belongs in Story Nodes with evidence IDs). |

### Audience
- **Primary:** maintainers/contributors running ETL, catalog builds, graph ingest, API contract tests, UI checks, or AI experiments.
- **Secondary:** reviewers/auditors validating provenance, reproducibility, governance, and CI gate behavior.

### Definitions (link to glossary)
- Link: `../../docs/glossary.md` *(not confirmed in repo; recommended)*

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `../../docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical ordering + invariants (non-negotiable). |
| v13 Redesign Blueprint | `../../docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | “One canonical home”, contract-first, evidence-first. |
| Universal Doc Template | `../../docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Baseline governed doc structure. |

### Definition of done (for this document)
- [x] Front-matter complete + valid
- [x] Clear scope boundaries (run logbook vs canonical homes)
- [x] Run record conventions (IDs, required fields, redaction rules)
- [x] Repro pointers to STAC/DCAT/PROV/Graph/API artifacts
- [ ] Optional: linked run-record schema in `schemas/telemetry/` *(not confirmed in repo)*

## 🗂️ Directory Layout

### This document
- `path`: `mcp/runs/README.md` *(must match front-matter)*

### Related repository paths

| Area | Canonical home | What lives there |
|---|---|---|
| MCP root | `mcp/` | Experiments, model cards, SOPs, run logbook. |
| **Run logbook** | `mcp/runs/` | **Run records + small support files** (this directory). |
| Pipelines | `src/pipelines/` | Deterministic ETL + catalog builders + run mechanics. |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Canonical STAC/DCAT/PROV artifacts. |
| Graph | `src/graph/` (+ optional fixtures in `data/graph/`) | Ontology bindings + ingest/migrations + fixtures. |
| API boundary | `src/server/` | REST/GraphQL contracts, redaction, query services. |
| UI | `web/` | Map + Focus Mode UI consuming APIs only. |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published Story Nodes + narrative assets. |

### Expected file tree for this sub-area
~~~text
📁 mcp/
└── 📁 runs/
    ├── 📄 README.md
    ├── 📁 RUN_ID/
    │   ├── 📄 README.md                # REQUIRED: run record (human-readable)
    │   ├── 📄 run.yaml                 # RECOMMENDED: small machine-readable manifest
    │   ├── 📄 params.yaml              # OPTIONAL: parameter snapshot (text)
    │   ├── 📄 metrics.json             # OPTIONAL: metrics summary (small)
    │   ├── 📄 artifacts.md             # OPTIONAL: pointers to canonical outputs + external blobs
    │   └── 📁 logs/                    # OPTIONAL: small logs (no secrets)
    └── 📁 _templates/
        └── 📄 RUN_RECORD_TEMPLATE.md   # OPTIONAL: shared skeleton (if you want one)
~~~

## 🧭 Context

### Background
KFM is **evidence-first** and **provenance-first**: the run record is the “glue” connecting:
- intent (why we ran it),
- execution context (what code/config/environment),
- evidence artifacts (what was produced),
- and auditability (how to reproduce/verify).

### Constraints / invariants (non-negotiable)
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- **No UI direct-to-graph reads** (UI consumes contracts via API only).
- Run records contain **no secrets**, **no PII**, and **no sensitive-location inference**.
- Run records **do not become narrative truth**: any conclusions must be surfaced as Story Nodes with evidence IDs.

### Run ID conventions
Run IDs must be:
- unique within `mcp/runs/`,
- stable enough to reference in PROV and Story Nodes,
- filesystem-safe (ASCII, no spaces).

Recommended patterns:
- `YYYY-MM-DD__<area>__<slug>__<shortsha>`
- `YYYYMMDDTHHMMSSZ__<area>__<slug>__<shortsha>`

Examples:
- `2025-12-28__etl__air-quality-refresh__a1b2c3d`
- `20251228T173012Z__ai__focus-bundle-eval__a1b2c3d`

## 🗺️ Diagrams

### Run record relationship to canonical artifacts
~~~mermaid
flowchart LR
  A["Run execution (manual or CI)"] --> B["Run record: mcp/runs/RUN_ID/README.md"]
  A --> C["Code + configs: src/**"]
  C --> D["Outputs: data/{raw,work,processed}/..."]
  D --> E["Catalogs: data/stac + data/catalog/dcat"]
  D --> F["Provenance bundles: data/prov/..."]
  E --> G["Graph ingest fixtures (optional): data/graph/..."]
  G --> H["API boundary: src/server/..."]
  H --> I["UI: web/..."]
  I --> J["Story Nodes: docs/reports/story_nodes/..."]
~~~

## 📦 Data & Metadata

### Inputs (what a run record must reference)
| Input | Where | Required? | Notes |
|---|---|:---:|---|
| Code version | Git `commit_sha` | ✅ | Always record commit SHA and branch/tag if relevant. |
| Run intent | Run record `README.md` | ✅ | What question/task, what changed, why now. |
| Parameters/config | `run.yaml` and/or `params.yaml` | ✅ | Keep small; prefer linking to canonical config in `src/**`. |
| Dataset/source IDs | STAC/DCAT IDs or stable paths | ✅ | Prefer IDs over copying data into `mcp/runs/`. |
| Environment snapshot | container tag / lockfiles / runtime | ◻ | Recommended for high-value runs and reproducibility audits. |

### Outputs (what a run record must point to)
| Output | Where | Required? | Notes |
|---|---|:---:|---|
| Run record | `mcp/runs/RUN_ID/README.md` | ✅ | The canonical log entry for the run. |
| Evidence artifacts | `data/**` | ◻ | Prefer pointers (STAC/DCAT/PROV refs) over duplication. |
| PROV bundle references | `data/prov/...` | ◻ | Strongly recommended for ETL/catalog/graph-affecting runs. |
| Metrics summary | `mcp/runs/RUN_ID/metrics.json` | ◻ | Keep small; store big results elsewhere, link in `artifacts.md`. |

### Recommended minimal run manifest (`run.yaml`)
~~~yaml
run_id: "2025-12-28__etl__example__a1b2c3d"
run_kind: "etl"          # etl | catalog | graph | api | ui | ai | validation | ad_hoc
status: "success"        # success | failed | partial | cancelled
started_at: "2025-12-28T17:30:12Z"
ended_at: "2025-12-28T17:46:03Z"

commit_sha: "a1b2c3d4e5f6..."
branch: "main"
runner: "manual"         # manual | ci
actor: "TBD"             # human or service principal (no secrets)

inputs:
  - kind: "stac-item"
    id: "TBD"
  - kind: "source"
    id: "TBD"

outputs:
  - kind: "prov-bundle"
    path: "data/prov/TBD"
  - kind: "stac-item"
    path: "data/stac/items/TBD.json"

notes:
  limitations: []
  followups: []
~~~

### Sensitivity & redaction
- **Never** include secrets (tokens, keys, private URLs), private data, or embargoed content.
- Avoid sensitive coordinates or restricted locations; reference generalized IDs (tile/H3 bucket) or access-controlled identifiers.
- If a run must reference restricted material for reproducibility, store details in the canonical restricted system (not here) and link by **opaque identifier**.

### Quality signals (what “good” looks like)
A high-quality run record:
- captures `commit_sha` + a parameter snapshot,
- points to canonical STAC/DCAT/PROV artifacts (does not duplicate them),
- is reproducible (explicit steps + stable IDs + deterministic seed notes where applicable),
- documents deltas vs prior runs and known limitations,
- avoids narrative claims without evidence links.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
If the run produces/updates spatiotemporal assets, reference:
- STAC Collections: `data/stac/collections/...`
- STAC Items: `data/stac/items/...`

### DCAT
If dataset-level discovery metadata changes, reference:
- DCAT datasets/distributions: `data/catalog/dcat/...` (JSON-LD)

### PROV-O
If the run transforms or derives outputs, reference:
- PROV bundles: `data/prov/...` (canonical home)

### Versioning
Run records should record:
- `run_id`
- `commit_sha`
- relevant dataset/catalog versions (if your domain pack uses them)
- predecessor/successor links when runs supersede prior evidence

## 🧱 Architecture

### What this directory is (and is not)
- **Is:** a traceable logbook for MCP activity with pointers to canonical artifacts.
- **Is not:** a data lake, an artifact store, or a narrative publication surface.

### Interfaces / contracts
This directory defines **no APIs**. It documents runs and references contracts elsewhere (OpenAPI/GraphQL, schemas, catalogs).

### Extension points (future work)
- Run-record schema + CI gate under `schemas/telemetry/` *(not confirmed in repo)*.
- A generator script to create `RUN_ID/` skeletons deterministically *(not confirmed in repo)*.
- Optional cross-linking into PROV as a first-class `prov:Activity` ID (run → activity mapping).

## 🧠 Story Node & Focus Mode Integration

### How run records surface in Focus Mode
Run records are **supporting evidence** and should be referenced when:
- a Story Node depends on a derived dataset or model output,
- an audit panel needs reproducibility breadcrumbs (run ID, commit, PROV bundle).

### Provenance-linked narrative rule
If a Story Node references a result from a run, it should reference:
- dataset/document IDs used,
- `run_id` (this folder),
- canonical PROV bundle path (if generated),
- and any redaction constraints (if applicable).

### Optional structured controls (if relevant)
~~~yaml
focus_mode_controls:
  include_run_records: false
  run_record_resolution: "by_id"
~~~

## 🧪 Validation & CI/CD

### Validation steps (recommended)
- [ ] Markdown protocol checks (KFM-MDP)
- [ ] Link check (internal links resolve)
- [ ] Secret scanning / credential detection (must be clean)
- [ ] If referenced: STAC/DCAT/PROV schemas validate
- [ ] If referenced: API contract tests pass

### Reproduction (pattern)
~~~bash
# 1) checkout the recorded commit SHA
# 2) run the recorded command(s) with recorded params/config
# 3) validate STAC/DCAT/PROV outputs referenced by the run record
# 4) compare expected vs observed outputs (hashes/IDs where applicable)
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- Any run referencing **restricted/sensitive** materials requires human review.
- Any run implying interpretive conclusions should be paired with governed Story Nodes.

### CARE / sovereignty considerations
- Respect sovereignty constraints and cultural sensitivity when describing datasets, places, or people.
- Prefer generalized descriptions when precise locations or identifiers could create harm.

### AI usage constraints
- Allowed: summarization, structuring, translation, keyword indexing.
- Prohibited: policy generation, inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Author | Change summary |
|---:|---:|---|---|
| v1.0.0 | 2025-12-22 | ChatGPT | Initial `mcp/runs/` README scaffold. |
| v1.1.0 | 2025-12-28 | ChatGPT | Tightened run ID + manifest conventions; clarified canonical pointers, redaction rules, and CI expectations. |

---

### Footer refs
- 🧭 Master Guide: `../../docs/MASTER_GUIDE_v12.md`
- 🏛️ Governance: `../../docs/governance/ROOT_GOVERNANCE.md`
- 🧾 Ethics: `../../docs/governance/ETHICS.md`
- 🪶 Sovereignty: `../../docs/governance/SOVEREIGNTY.md`
