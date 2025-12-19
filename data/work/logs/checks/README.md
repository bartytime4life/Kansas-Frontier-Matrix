---
title: "KFM — Validation Check Logs (data/work/logs/checks)"
path: "data/work/logs/checks/README.md"
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

doc_uuid: "urn:kfm:doc:data:work:logs:checks:readme:v1.0.0"
semantic_document_id: "kfm-data-work-logs-checks-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:logs:checks:readme:v1.0.0"
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

# Validation check logs

## 📘 Overview

### Purpose
This folder holds **machine-produced evidence artifacts** (logs, reports, JSON summaries) created by validation and QA checks across the KFM pipeline. The intent is to make it easier to:
- diagnose failed CI runs,
- compare runs over time,
- and preserve provenance-adjacent artifacts that explain *why* a build passed or failed.

This area is part of KFM’s broader requirement that the system stays reproducible and auditable across the canonical pipeline:
**ETL → STAC/DCAT/PROV → Neo4j → APIs → UI → Story Nodes → Focus Mode**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Schema validation logs (STAC/DCAT/PROV) | Raw source datasets |
| Markdown lint outputs and doc checks | Processed datasets (belongs in `data/processed/`) |
| Test run logs (unit/integration) summaries | Secrets, tokens, credentials |
| Security/safety scan summaries (sanitized) | Large binary artifacts (prefer CI artifacts storage) |

### Audience
- Primary: CI maintainers, DataOps / pipeline maintainers, reviewers
- Secondary: contributors debugging local runs

### Definitions (link to glossary)
- Glossary link: `docs/glossary.md` (**not confirmed in repo**; if absent, create or link the canonical glossary location)
- Terms used here: “check”, “run”, “report”, “artifact”, “redaction”

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Check reports | `data/work/logs/checks/<run_id>/...` | CI + maintainers | Recommended per-run grouping |
| Schema validator output | `.../stac/`, `.../dcat/`, `.../prov/` | Catalog maintainers | Prefer machine-readable JSON alongside text |
| Markdown lint output | `.../markdown/` | Docs maintainers | Keep line/filename references, avoid huge dumps |
| Test summaries | `.../tests/` | Backend/frontend maintainers | Store summaries; full logs as CI artifacts if large |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Folder purpose and boundaries are explicit
- [ ] No secrets/PII guidance included
- [ ] Recommended naming/layout is described
- [ ] Validation steps and reproduction notes are present (even if commands are placeholders)

## 🗂️ Directory layout

### This document
- `path`: `data/work/logs/checks/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Work area | `data/work/` | Intermediate artifacts used during runs |
| Work logs | `data/work/logs/` | General logs (by tool/run) |
| Checks logs | `data/work/logs/checks/` | Validation outputs and QA evidence artifacts |
| CI actions | `.github/actions/` | Composite actions that may emit check outputs (e.g., validators, lint, tests) |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 work/
    └── 📁 logs/
        └── 📁 checks/
            └── 📄 README.md
~~~

## 🧭 Context

### Background
KFM relies on “tight contracts” between pipeline stages (catalog schemas, graph integrity, API contracts, UI layer registries, and governed docs). When a check fails, contributors need *repeatable evidence* explaining what broke and where.

This folder is a stable landing zone for **check artifacts** that are safe to retain and useful for debugging.

### Assumptions
- CI systems and local runs will produce logs in a consistent structure (recommended below).
- Large outputs should be stored as CI artifacts rather than committed to git (**not confirmed in repo**; verify project policy).

### Constraints / invariants
- The canonical pipeline ordering is preserved; checks should not encourage “shortcuts” that bypass catalogs or APIs.
- Do **not** store secrets, API keys, access tokens, private URLs, or any sensitive content in this directory.
- Do **not** store raw or restricted-location coordinates in plaintext logs. If a tool emits sensitive info, redact or generalize before saving.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Are `data/work/` logs committed or ignored via `.gitignore`? | Maintainers | TBD |
| What retention policy applies (how many runs)? | Maintainers | TBD |
| Do we standardize a run ID format (`run_YYYYMMDDTHHMMSSZ`, CI run number, etc.)? | Maintainers | TBD |

### Future extensions
- Add a tiny “index.json” summary per run for quick UI display in an audit panel.
- Align log schemas with `schemas/telemetry/` (**not confirmed in repo**) to support machine analysis.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Pipeline run] --> B[Validators + tests + linters]
  B --> C[data/work/logs/checks/<run_id>/...]
  B --> D[CI artifacts / build logs]
  C --> E[Human review + debugging]
~~~

## 📦 Data & metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC/DCAT/PROV validation output | text + json | catalog validators | schema-validated where applicable |
| Markdown lint output | text | markdown lint action/tool | n/a |
| Test summaries | junit/xml, text | pytest / other runners | test framework validation |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Per-run reports | text/json | `data/work/logs/checks/<run_id>/` | recommended structure (below) |
| Optional per-run index | json | `.../<run_id>/index.json` | **not confirmed in repo** |

### Recommended structure (non-binding)
Use a per-run directory and keep files small and readable:

~~~text
data/work/logs/checks/
└── <run_id>/
    ├── index.json                # optional high-level summary
    ├── stac/
    │   ├── validate.txt
    │   └── validate.json
    ├── dcat/
    │   ├── validate.txt
    │   └── validate.json
    ├── prov/
    │   ├── validate.txt
    │   └── validate.json
    ├── markdown/
    │   └── markdownlint.txt
    └── tests/
        └── pytest.txt
~~~

### Sensitivity & redaction
- Treat logs as potentially sensitive if they include file paths, dataset excerpts, or coordinates.
- If a tool outputs sensitive content, store only a summary and move full detail to secured CI artifacts.

### Quality signals
A “good” check artifact is:
- small enough to read in a PR,
- includes tool version + command/config reference (when safe),
- and points to the exact file(s) and line(s) involved.

## 🌐 STAC, DCAT & PROV alignment

### STAC
If STAC validation is recorded here, prefer logs that include:
- the STAC Collection/Item IDs involved,
- the failing schema/extension,
- and any broken-link checks results.

### DCAT
If DCAT validation is recorded here, prefer logs that include:
- dataset identifiers,
- missing required fields,
- and JSON-LD/Turtle parse errors (if relevant).

### PROV-O
If PROV validation is recorded here, prefer logs that include:
- activity/run identifiers (`prov:wasGeneratedBy` references),
- source identifiers (`prov:wasDerivedFrom` references),
- and any missing agent/activity metadata.

### Versioning
If multiple runs are kept, use stable run IDs and avoid overwriting prior reports.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| CI validators | run checks | configs + stdout/stderr |
| Repo log area | store sanitized check outputs | filesystem paths |
| Reviewers | read/interpret check outputs | PR + logs |

### Interfaces / contracts
- This directory should not define new runtime contracts.
- If any machine-readable summaries are adopted (e.g., `index.json`), create/extend a schema under `schemas/` (**not confirmed in repo**) and add a CI check to validate it.

## 🧠 Story Node & Focus Mode integration

### How this work surfaces in Focus Mode
Indirectly: checks help ensure that story nodes and any narrative-serving components remain provenance-linked and schema-valid.

### Provenance-linked narrative rule
Any narrative that depends on catalogs/graph should be backed by validation evidence; this directory can store the evidence outputs that support such claims.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (where applicable)
- [ ] STAC schema validation
- [ ] DCAT mapping validation
- [ ] PROV lineage validation
- [ ] Graph integrity checks (if run produces safe outputs)
- [ ] API contract tests (if run produces safe outputs)
- [ ] UI registry/schema checks (if run produces safe outputs)
- [ ] Security and sovereignty checks (store only sanitized summaries)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)
# 1) run schema validators
# 2) run tests
# 3) run markdown lint
~~~

## ⚖ FAIR+CARE & governance

### Review gates
- If logs include any potentially sensitive content, treat it as **requires human review** before committing.

### CARE / sovereignty considerations
- Avoid copying location data that could reveal sensitive sites.
- Prefer “generalize/redact by default” for outputs saved under version control.

### AI usage constraints
- Do not use this directory as a source for generating new “policy” text.
- AI transforms must not infer sensitive locations from log content.

## 🕰️ Version history

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for checks logs directory | TBD |
---
Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

