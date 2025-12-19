---
title: "KFM — data/work/logs (README)"
path: "data/work/logs/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:data:work:logs:readme:v1.0.0"
semantic_document_id: "kfm-data-work-logs-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:logs:readme:v1.0.0"
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

# KFM — `data/work/logs/` README

## 📘 Overview

### Purpose
This directory is a **workspace** for logs produced during pipeline execution (especially ETL and validation).
It exists to make pipeline runs **observable**, **debuggable**, and **auditable** during active work.

This folder is **not** a canonical long-term archive of run artifacts.
If a run output must be retained as an evidence artifact, a release artifact, or for governance review, promote it to the appropriate governed location (commonly `mcp/runs/`), and reference it from PROV where applicable.

### Scope

| In Scope | Out of Scope |
|---|---|
| Ephemeral per-run logs (stdout/stderr), warnings, validation reports, small manifests | Secrets/credentials, raw PII, long-term archival logs as a system of record |
| “Work” visibility while iterating on ingestion/transforms | Any UI-facing data product (those must be cataloged + versioned) |
| Debug + trace material that can be safely deleted after successful runs | Anything required for STAC/DCAT/PROV publication (those live under `data/stac/`, `data/catalog/`, `data/prov/`) |

### Audience
- Primary: pipeline developers, data engineers, catalog builders
- Secondary: reviewers troubleshooting ingestion or validation failures

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo — create or update link if a glossary exists elsewhere)*
- Terms used in this doc:
  - **run_id**: stable identifier for a single pipeline execution (prefer timestamp + short hash).
  - **stage**: pipeline segment that produced the log (`etl`, `catalog`, `graph`, etc.).
  - **manifest**: small structured summary of a run (inputs, outputs, config refs, counts).
  - **redaction**: removal/generalization of sensitive strings (tokens, emails, exact addresses).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `data/work/logs/README.md` | Repo | Governs how logs are organized in this folder |
| Example run folder | `data/work/logs/<stage>/<run_id>/...` | Pipeline | Workspace layout convention (recommended) |
| Persisted run archive | `mcp/runs/<run_id>/...` | MCP | Use when a run must be retained beyond “work” (recommended) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory purpose clearly separated from canonical artifacts (`data/processed/`, `data/stac/`, `data/prov/`)
- [ ] Redaction / no-secrets expectations stated
- [ ] Naming + layout conventions documented

## 🗂️ Directory Layout

### This document
- `path`: `data/work/logs/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Raw sources | `data/raw/` | Unmodified ingested sources (as allowed) |
| Work area | `data/work/` | Intermediate working artifacts (not canonical) |
| Processed data | `data/processed/` | Reproducible processed outputs |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Canonical metadata + lineage bundles |
| Persisted run artifacts | `mcp/runs/` | Long-lived run logs/evidence (recommended) |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 work/
    └── 📁 logs/
        ├── 📄 README.md
        ├── 📁 etl/
        │   └── 📁 <run_id>/
        │       ├── 📄 run_manifest.json
        │       ├── 📄 stdout.log
        │       ├── 📄 stderr.log
        │       ├── 📄 warnings.ndjson
        │       └── 📄 validation_report.json
        ├── 📁 catalog/
        │   └── 📁 <run_id>/
        │       ├── 📄 stac_validation.json
        │       ├── 📄 dcat_validation.json
        │       └── 📄 prov_validation.json
        └── 📁 graph/
            └── 📁 <run_id>/
                ├── 📄 graph_build.log
                └── 📄 constraints_report.json
~~~

## 🧭 Context

### Background
KFM’s canonical pipeline is:
**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.

Observability is critical because pipeline steps are expected to be **deterministic and reproducible**.
Logs in this folder provide *work-time traceability* for:
- parse warnings / extraction errors
- schema validation failures
- graph build issues
- input/output hash mismatches or unexpected deltas

### Assumptions
- This directory may be cleaned between runs.
- Anything committed from here should be small, sanitized, and intentional (e.g., fixtures for tests or minimal repro logs).

### Constraints / invariants
- This folder is **not** a substitute for STAC/DCAT/PROV catalogs or for `data/processed/` outputs.
- No UI component should depend on files in `data/work/` (work area is not stable or versioned as a product).
- Frontend consumes data via APIs; logs are not a frontend data source.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should a standard `run_manifest.json` schema be formalized under `schemas/telemetry/`? | TBD | TBD |
| Should `data/work/logs/` be gitignored by default except `README.md`? | TBD | TBD |

### Future extensions
- Extension point A: standardize a **run manifest** schema + validators
- Extension point B: automated redaction of known secret patterns before writing logs

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Pipeline execution] --> B[data/work/logs/<stage>/<run_id>/]
  B --> C{Keep?}
  C -- "No (ephemeral)" --> D[Delete/clean workspace]
  C -- "Yes (evidence/record)" --> E[mcp/runs/<run_id>/]
  E --> F[data/prov/ (prov:Activity references)]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Pipeline config reference | YAML/JSON | `src/pipelines/...` or config bundle | Lint + schema (as applicable) |
| Source identifiers | strings/paths | `data/raw/` + external refs | Must resolve + be stable |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Standard output log | `.log` | `data/work/logs/<stage>/<run_id>/stdout.log` | none (text) |
| Standard error log | `.log` | `.../stderr.log` | none (text) |
| Warnings stream | `.ndjson` | `.../warnings.ndjson` | recommended (not yet enforced) |
| Validation report | `.json` | `.../validation_report.json` | recommended (not yet enforced) |
| Run manifest | `.json` | `.../run_manifest.json` | recommended (not yet enforced) |

### Sensitivity & redaction
Logs can accidentally capture sensitive values (tokens, emails, exact addresses, internal URLs).
Rules for this folder:
- **Do not write secrets** to logs (prevent at source where possible).
- If sensitive content is discovered, **treat it as a security incident**: remove/redact, rotate credentials, and document remediation in the appropriate security workflow.
- Prefer storing *identifiers and hashes* over raw payloads.

### Quality signals
- Presence of a single `run_manifest.json` per run folder
- Clear start/end timestamps and stage labeling
- Validation reports are machine-readable (JSON) when possible
- Errors are actionable (include file references + exception type)

## 🌐 STAC, DCAT & PROV Alignment

### Provenance requirements (work-time)
Where helpful, logs should enable creation of canonical provenance:
- Capture/echo the **run_id** used as a PROV `prov:Activity` identifier.
- Record input artifact identifiers and checksums when available.
- Record where canonical outputs were written (e.g., `data/processed/...`, `data/stac/...`, `data/prov/...`).

> Note: The canonical PROV bundle belongs under `data/prov/`. Logs here are supporting evidence only.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize + extract | Config + run logs |
| Catalogs | STAC/DCAT/PROV build + validation | JSON/JSON-LD + validators |
| Graph | Build + constraints + integrity checks | Graph build logs + reports |
| MCP | Retained run artifacts | `mcp/runs/` |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Run manifest schema (recommended) | `schemas/telemetry/` | Semver + changelog (if created) |
| Validation report structure (recommended) | `schemas/telemetry/` | Semver + changelog (if created) |

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Directly: it should not.
- Indirectly: improved pipeline reliability leads to higher-quality catalogs/graph content that Focus Mode consumes via APIs.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Confirm no secrets/credentials are present in any committed log artifact
- [ ] Ensure any committed log artifacts are minimal + sanitized
- [ ] Ensure canonical outputs (if any) are stored under `data/processed/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/` (not under `data/work/`)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run pipeline stage (etl/catalog/graph)
# 2) run schema validation for STAC/DCAT/PROV
# 3) run secret scan on workspace artifacts
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- If logs include any culturally sensitive, restricted, or identifying details:
  - requires human review before publication/commit
  - redact/generalize as required by governance/sovereignty guidance

### CARE / sovereignty considerations
- Treat location-identifying strings as potentially sensitive when associated with protected communities or restricted sites.
- Prefer generalized references in logs intended to be committed.

### AI usage constraints
- Do not use AI to infer sensitive locations from partial log content.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for `data/work/logs/` conventions | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
