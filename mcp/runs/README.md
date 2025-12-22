---
title: "MCP Runs — Run Records and Reproducibility Logbook"
path: "mcp/runs/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

doc_uuid: "urn:kfm:doc:mcp:runs:readme:v1.0.0"
semantic_document_id: "kfm-mcp-runs-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:mcp:runs:readme:v1.0.0"
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
`mcp/runs/` is the **run logbook** for KFM’s MCP (Master Coder Protocol) work: a place to capture **human-readable, reviewable run records** that make experimentation and pipeline execution **traceable and repeatable**.

This directory is intended to complement (not replace) the repository’s **canonical artifact locations** for pipeline outputs, catalogs, and provenance.

### Scope

| In Scope | Out of Scope |
|---|---|
| Run records for experiments, validations, and analysis work (what was run, why, with what inputs/params, and what happened). | Canonical STAC/DCAT/PROV outputs (these live under `data/…` as defined in the system architecture). |
| Pointers to canonical artifacts: PROV bundle paths, dataset IDs, STAC item IDs, API contract versions, etc. | Large binary artifacts, raw dumps, or datasets that belong under `data/` (or an external artifact store). |
| Lightweight run metadata: parameters, config snapshots, metrics summaries, known limitations, next actions. | Secrets/credentials, private keys, tokens, or any sensitive/regulated content. |
| Reproducibility breadcrumbs: commit SHA, environment notes, deterministic seed notes (when applicable). | “Unsourced narrative” claims: conclusions must be backed by cited datasets/doc IDs elsewhere. |

### Audience
- **Primary:** maintainers and contributors running ETL, analysis, or AI experiments.
- **Secondary:** reviewers/auditors validating provenance, reproducibility, and governance compliance.

### Definitions (link to glossary)
- Link: `../../docs/glossary.md`

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| **MASTER_GUIDE_v12.md** | `../../docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline invariants and repo rules. |
| **KFM_REDESIGN_BLUEPRINT_v13.md** | `../../docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Canonical homes-by-stage + provenance-first rules. |

### Definition of done (for this document)
- [x] Front-matter complete + valid
- [x] Clear scope + boundaries (what goes here vs. canonical homes)
- [x] Provides a minimal, repeatable run-record pattern
- [x] Includes sensitivity/redaction guidance
- [ ] Linked run-record schema (if/when `schemas/telemetry/` is introduced)

## 🗂️ Directory Layout

### This document
- `path`: `mcp/runs/README.md` (must match front-matter)

### Related repository paths

| Area | Canonical home | What lives there |
|---|---|---|
| MCP docs | `mcp/` | Experiments, model cards, SOPs, and MCP resources. |
| **Run logbook** | `mcp/runs/` | **Run records** (this directory). |
| ETL / pipelines | `src/pipelines/` | Deterministic transforms and pipeline-run mechanics. |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV artifacts (canonical). |
| Graph | `src/graph/` + `data/graph/` | Graph ingest + fixtures. |
| API boundary | `src/server/` | API contracts + redaction/query services. |
| UI | `web/` | Map layers, focus mode UI, citation rendering. |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published Story Nodes and assets. |

### Expected file tree for this sub-area
~~~text
📁 mcp/
└── 📁 runs/
    ├── 📄 README.md
    ├── 📁 <run_id>/
    │   ├── 📄 README.md              # run record (recommended)
    │   ├── 📄 params.yaml            # optional: parameters snapshot (small text)
    │   ├── 📄 metrics.json           # optional: metrics summary (small text)
    │   ├── 📄 artifacts.md           # optional: pointers to large artifacts stored elsewhere
    │   └── 📁 logs/                  # optional: small logs (no secrets)
    └── 📁 _templates/
        └── 📄 RUN_RECORD_TEMPLATE.md # optional: shared skeleton
~~~

## 🧭 Context

### Background
KFM emphasizes **reproducibility** and **provenance-first** workflows. Run records are the “glue” that connects:
- why we ran something,
- what inputs/versions we used,
- what artifacts we produced (and where the canonical copies live),
- and how to reproduce or audit the result later.

### Assumptions
- Runs may be manual (developer executed) or automated (CI / scheduled).
- Canonical artifacts (catalogs + PROV) live under `data/…` per the architecture blueprint.
- `mcp/runs/` is optimized for **readability + traceability**, not bulk storage.

### Constraints / invariants
- Preserve the canonical ordering: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- **UI must never connect to Neo4j directly**; all graph access is via APIs (boundary enforced at `src/server/`).
- No secrets, no PII leakage, no sensitive-location inference in run notes.

### Open questions
- Should KFM formalize a JSON Schema for run records under `schemas/telemetry/`?
- Should `mcp/runs/` be strictly “human-readable markdown,” or allow machine-readable manifests as first-class citizens?

### Future extensions
- Add a validated run-record schema (JSON Schema) + CI gate for minimum metadata completeness.
- Add automated tooling to generate run folders with consistent IDs and pre-filled metadata.

## 🗺️ Diagrams

### Run record relationship to canonical artifacts
~~~mermaid
flowchart LR
  A["Run execution<br/>(manual or CI)"] --> B["Run record<br/>mcp/runs/&lt;run_id&gt;/README.md"]
  A --> C["Pipeline code<br/>src/pipelines/"]
  C --> D["Outputs<br/>data/**"]
  D --> E["Catalogs<br/>data/stac + data/catalog/dcat"]
  D --> F["Provenance bundles<br/>data/prov/"]
  E --> G["Graph ingest fixture<br/>data/graph/"]
  G --> H["API boundary<br/>src/server/"]
  H --> I["UI<br/>web/"]
  I --> J["Story Nodes<br/>docs/reports/story_nodes/"]
~~~

## 📥 Inputs

| Input artifact | Where it lives | Required? | Notes |
|---|---:|:---:|---|
| Code version | Git commit SHA / tag | ✅ | Always record the commit SHA. |
| Pipeline config / parameters | `src/pipelines/` and/or this run folder | ✅ | Capture parameter snapshots (text). |
| Dataset identifiers | `data/<domain>/…` + catalog IDs | ✅ | Use stable IDs/paths; avoid copying large files into `mcp/runs/`. |
| Environment snapshot | lockfile / container tag / python version | ◻ | Recommended for high-value runs. |

## 📤 Outputs

| Output artifact | Where it lives | Required? | Notes |
|---|---:|:---:|---|
| Run record | `mcp/runs/<run_id>/README.md` | ✅ | Human-readable summary of intent + results. |
| PROV bundle reference | `data/prov/...` (canonical) | ◻ | Add a pointer to the generated PROV bundle if applicable. |
| STAC/DCAT references | `data/stac/...`, `data/catalog/dcat/...` | ◻ | If a run produced new/updated datasets, cite the relevant IDs/paths. |
| Metrics summary | `mcp/runs/<run_id>/metrics.json` | ◻ | Keep small; store large outputs elsewhere and link. |

## 🔐 Sensitivity & redaction notes
- Do **not** include tokens, API keys, credentials, private URLs, or personal data.
- Avoid listing sensitive coordinates or restricted locations; use generalized references when needed.
- If you must reference sensitive materials for reproducibility, reference **access-controlled identifiers** (not raw content).

## ✅ Quality signals
A “high quality” run record:
- includes commit SHA + parameter snapshot,
- references canonical outputs (PROV/STAC/DCAT) instead of duplicating them,
- includes enough context to rerun deterministically,
- states limitations and what changed vs prior runs,
- avoids unsourced claims; results should be tied to evidence artifacts.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
If the run produced/updated geospatial assets, reference the relevant:
- STAC Collection(s): `data/stac/collections/...`
- STAC Item(s): `data/stac/items/...`

### DCAT
If the run produced/updated dataset-level metadata, reference:
- DCAT dataset record(s): `data/catalog/dcat/...` (JSON-LD)

### PROV-O
If the run produced derivations or transformations, reference:
- PROV bundle(s): `data/prov/...` (canonical home)

### Versioning
- Run records should record:
  - the run ID,
  - the commit SHA,
  - and any dataset/catalog version identifiers used or produced.

## 🧩 Architecture

### Components touched

| Component | Path | Change type |
|---|---|---|
| Run logbook | `mcp/runs/` | Documentation / provenance pointers |
| ETL / pipelines | `src/pipelines/` | Referenced (canonical) |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Referenced (canonical) |

### Interfaces/contracts
- This directory does not define APIs; it documents runs and references canonical artifacts and contracts elsewhere.

### Extension points checklist (for future work)
- [ ] Add run-record schema under `schemas/telemetry/`
- [ ] Add CI check: run record minimum metadata
- [ ] Add a generator script for new run folders

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Run records are **supporting evidence** and should be referenced when a Story Node depends on a derived dataset/model result.

### Provenance-linked narrative rule
If a Story Node references a result produced by a run, it should reference:
- the dataset/document IDs used,
- the run ID (this folder),
- and the canonical PROV bundle path (if generated).

### Optional structured controls (if relevant)
~~~yaml
focus_mode_controls:
  include_run_records: false
  run_record_resolution: "by_id"
~~~

## 🧪 Validation & CI/CD

### Validation steps
- Ensure Markdown passes the repo’s markdown protocol validation.
- Ensure internal links resolve (if link checking is enabled).
- Ensure no secrets or sensitive data were accidentally committed.

### Reproduction
~~~bash
# (Replace with repo-specific commands)
# 1) Checkout the recorded commit SHA
# 2) Re-run the pipeline/experiment with recorded params
# 3) Confirm artifacts match referenced PROV/STAC/DCAT outputs
~~~

### Telemetry signals (optional future schema)

| Field | Example | Notes |
|---|---|---|
| run_id | `2025-12-22__example__abc1234` | Stable, unique ID |
| stage | `ETL` / `AI` / `Catalog` | KFM stage(s) touched |
| commit_sha | `abc1234...` | Required |
| inputs | list of dataset IDs/paths | Avoid embedding raw data |
| outputs | list of canonical artifact refs | Prefer `data/...` pointers |
| status | `success` / `failed` | Optional but useful |

## ⚖ FAIR+CARE & Governance

### Review gates
- Any run record that references restricted/sensitive materials requires human review.
- Any run record that implies new narrative conclusions should be paired with sourced Story Nodes.

### CARE / sovereignty considerations
- Respect sovereignty constraints and cultural sensitivity when describing datasets, places, or people.
- Prefer generalized descriptions over sensitive specifics when necessary.

### AI usage constraints
- Allowed: summarization, structuring, translation, keyword indexing.
- Prohibited: policy generation, inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Author | Change summary |
|---:|---:|---|---|
| v1.0.0 | 2025-12-22 | ChatGPT | Initial `mcp/runs/` README scaffold (template-aligned). |

---

### Footer refs
Governance: `docs/governance/ROOT_GOVERNANCE.md`  
Ethics: `docs/governance/ETHICS.md`  
Sovereignty: `docs/governance/SOVEREIGNTY.md`
