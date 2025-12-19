---
title: "AI Work Logs (data/work/logs/ai)"
path: "data/work/logs/ai/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "active"
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

doc_uuid: "urn:kfm:doc:data:work:logs:ai:readme:v1.0.0"
semantic_document_id: "kfm-data-work-logs-ai-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:logs:ai:readme:v1.0.0"
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

# AI Work Logs (data/work/logs/ai)

## 📘 Overview

### Purpose
This directory is a **work-area log sink** for **AI-stage run artifacts** produced during development, QA, and operational pipelines (e.g., extraction, linking, summarization, validation checks).
It exists to support **auditability, reproducibility, and human review** of AI-assisted steps.

### Scope
| In Scope | Out of Scope |
|---|---|
| AI run manifests (inputs/outputs metadata), validation summaries, redaction notes, evaluation metrics, run-level provenance pointers | Canonical datasets (`data/raw`, `data/processed`), canonical catalogs (`data/stac`, `data/catalog/dcat`, `data/prov`), production graph exports/dumps, secrets/credentials |

### Audience
- Primary: Pipeline/ETL engineers, AI/ML engineers, maintainers running or debugging AI steps
- Secondary: Reviewers/auditors validating provenance, governance, and human-in-the-loop decisions

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **run_id**: A unique identifier for one AI execution (recommended stable naming convention).
  - **AI validation report**: A human-readable summary of checks and reasoning/audit signals for a run.
  - **trace**: A redacted prompt/response record sufficient to reproduce behavior (where permitted).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `data/work/logs/ai/README.md` | Repo maintainers | Directory contract + conventions |
| Example run folder | `data/work/logs/ai/<run_id>/` | Pipeline operator | One folder per AI run (recommended) |
| AI validation report | `data/work/logs/ai/<run_id>/validation_report.md` | Pipeline operator | Summary for reviewers |
| Run manifest | `data/work/logs/ai/<run_id>/run.json` | Pipeline operator | Parameters + environment + model IDs |
| Trace (redacted) | `data/work/logs/ai/<run_id>/trace.jsonl` | Pipeline operator | Optional; do **not** store secrets/PII |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory purpose + scope clearly defined
- [ ] Storage rules documented (no secrets/PII; no canonical datasets)
- [ ] Naming + layout conventions documented
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `data/work/logs/ai/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Raw sources | `data/raw/` | Immutable raw ingests (not logs) |
| Work area | `data/work/` | Intermediate processing outputs |
| Logs root | `data/work/logs/` | Run logs by category |
| AI logs | `data/work/logs/ai/` | **This folder**: AI-stage run artifacts |
| Checks logs | `data/work/logs/checks/` | Validation/check outputs (schema, integrity, etc.) |
| Provenance | `data/prov/` | Canonical PROV outputs (W3C PROV-O) |
| Experiments | `mcp/runs/` / `mcp/experiments/` | Experiment artifacts and long-form run records |

### Suggested folder structure (recommended convention)
~~~text
📁 data/
└── 📁 work/
    └── 📁 logs/
        ├── 📁 ai/
        │   ├── 📄 README.md
        │   └── 📁 <run_id>/
        │       ├── 📄 run.json
        │       ├── 📄 validation_report.md
        │       ├── 📄 metrics.json
        │       ├── 📄 trace.jsonl
        │       └── 📄 redaction_notes.md
        └── 📁 checks/
            └── 📄 README.md
~~~

## 🧭 Context
KFM’s canonical flow is **ETL → STAC/DCAT/PROV → Neo4j → APIs → React/Map UI → Story Nodes → Focus Mode**.
This directory supports the **AI-stage portions** of ETL and Story Node generation by preserving an **audit trail** of model behavior and review outcomes.

## 🗺️ Diagrams

### Where these logs sit in the pipeline
~~~mermaid
flowchart LR
  A[ETL + AI transforms] --> B[data/work/logs/ai]
  A --> C[Catalogs: STAC/DCAT/PROV]
  C --> D[Graph: Neo4j]
  D --> E[APIs]
  E --> F[UI + Story Nodes + Focus Mode]
~~~

## 📦 Data & Metadata

### What may be stored here
- **Manifests**: model identifiers, prompt templates (non-secret), dataset/record IDs referenced, run timestamps, code version pointers.
- **Validation**: pass/fail checks, bias/consistency checks, explainability summaries (if used), reviewer notes.
- **Redaction**: what was removed/hashed and why.

### What must NOT be stored here
- Credentials, API keys, access tokens, private keys
- Raw sensitive data (PII, protected site coordinates, restricted cultural knowledge)
- Canonical catalog outputs (STAC/DCAT/PROV) that belong in their designated directories

### Recommended run folder naming
Use a stable, sortable `run_id`:
- `YYYY-MM-DDThhmmssZ__<pipeline-step>__<model-or-config-tag>`
- Example: `2025-12-19T184500Z__entity-linking__llm-vX`

### Quality signals (recommended)
- Coverage: % records processed, % records flagged for human review
- Provenance completeness: % outputs with dataset/asset IDs
- Consistency: duplicate detection counts, entity merge conflict counts
- Safety: redaction count, restricted-field detection count

## 🌐 STAC, DCAT & PROV Alignment

### STAC / DCAT
AI logs are **not** canonical catalogs.
If a run produces catalog-ready outputs, write them to:
- STAC: `data/stac/...`
- DCAT: `data/catalog/dcat/...`

### PROV
If the run emits provenance:
- Store canonical PROV documents under `data/prov/...`
- In this directory, store only **pointers** (e.g., `prov_activity_id`, `prov_agent_id`) in `run.json`

### Versioning
- Treat each `<run_id>/` folder as **append-only** (do not rewrite history; create a new run).
- If a rerun is required, generate a new `run_id` and cross-reference prior runs in the manifest.

## 🧱 Architecture Sync

### API boundary
This directory is **not an API** and must not be a direct dependency of the UI.
If any UI surface needs audit evidence, it should be exposed through an **API contract** (or surfaced via Story Nodes) rather than reading these logs directly.

### Determinism expectations
When possible, capture in `run.json`:
- Model name/version
- Prompt/template version
- Seed/config flags (if used)
- Input dataset identifiers and filter criteria
- Code version pointer (commit SHA)

## 🧩 Extension points checklist (for future work)
- [ ] Data: new log subtype documented + directory added
- [ ] PROV: activity + agent identifiers recorded and linked
- [ ] Graph: any AI-derived edges/nodes mapped + review workflow defined
- [ ] APIs: audit evidence contract (if surfaced) + tests
- [ ] UI: audit display rules and access policy (if applicable)
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- If AI assists in creating or editing Story Nodes, the Story Node should reference the **run_id** (and/or PROV activity) that produced the suggestion.
- Review outcomes (approve/correct/reject) should be recorded as provenance and reflected in narrative confidence/limitations where applicable.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (lint)
- [ ] Secret scanning / credential detection
- [ ] Size / binary artifact checks (avoid committing large logs unless explicitly intended)
- [ ] Governance checks for restricted/sensitive fields (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run the AI step locally (or in CI)
# 2) verify the run manifest and validation report are created
# 3) run markdown lint / checks
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| ai.run_id | pipeline | `data/work/logs/ai/<run_id>/run.json` |
| ai.review.outcome | reviewer/admin tool | `data/work/logs/ai/<run_id>/validation_report.md` |
| ai.redaction.count | pipeline | `data/work/logs/ai/<run_id>/redaction_notes.md` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Any log content containing restricted/sensitive indicators requires human review before sharing or publishing.
- If uncertainty exists about cultural sensitivity or protected locations, treat as restricted until reviewed.

### CARE / sovereignty considerations
- Identify communities potentially impacted by extracted or inferred content.
- Do not store or surface precise coordinates or culturally sensitive knowledge unless governance explicitly allows.

### AI usage constraints
- Ensure this directory’s artifacts follow the repository’s AI permissions/prohibitions and do not enable prohibited inference (e.g., sensitive location inference).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for AI work logs directory | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

