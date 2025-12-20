---
title: "KFM — data/work/tmp/text/logs — README"
path: "data/work/tmp/text/logs/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:data:work:tmp:text:logs:readme:v1.0.0"
semantic_document_id: "kfm-data-work-tmp-text-logs-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:tmp:text:logs:readme:v1.0.0"
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

# data/work/tmp/text/logs

## 📘 Overview

### Purpose
This directory stores **temporary, non-canonical logs** produced while running **text-oriented pipeline steps** (e.g., text extraction, parsing, chunking, entity detection, validation checks) during local development or ad-hoc troubleshooting.

These logs are **debug artifacts** and are:
- safe to delete,
- not considered authoritative run records,
- not intended for long-term retention or cataloging.

### Scope
| In Scope | Out of Scope |
|---|---|
| Temporary debug logs for text pipelines | Official run logs for repeatable ETL runs (use `data/work/logs/`) |
| Local validation traces and warnings | Any dataset outputs intended for `data/processed/` or `data/stac/` |
| Small, human-readable diagnostics | Secrets, credentials, or raw sensitive text dumps |

### Audience
- Primary: pipeline developers, data engineers, QA reviewers
- Secondary: maintainers performing incident/debug review

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(create if missing)*
- Terms used in this doc: ETL, validation run, redaction, provenance, PII

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Temp text logs | `data/work/tmp/text/logs/` | ETL | Non-canonical debug output |
| Validation runs | `data/work/tmp/text/validation/runs/` | ETL/QA | Structured validation artifacts per run |
| Durable logs | `data/work/logs/` | ETL | Canonical run logging (preferred for retention) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory purpose is unambiguous
- [ ] Sensitivity guidance prevents accidental PII/secret retention
- [ ] Clear handoff to durable locations is documented

## 🗂️ Directory Layout

### This document
- `path`: `data/work/tmp/text/logs/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Work root | `data/work/` | Work-in-progress artifacts (non-authoritative) |
| Temp root | `data/work/tmp/` | Safe-to-delete transient artifacts |
| Text temp root | `data/work/tmp/text/` | Transient text extraction + validation artifacts |
| Text validation | `data/work/tmp/text/validation/` | Validation configs + intermediate checks |
| Validation runs | `data/work/tmp/text/validation/runs/` | Per-run structured outputs |
| Durable logs | `data/work/logs/` | Canonical, retained run logs |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 work/
    └── 📁 tmp/
        └── 📁 text/
            └── 📁 logs/
                ├── 📄 README.md
                ├── 📄 .gitkeep                (optional)
                ├── 📄 <run_or_session>.log    (optional)
                ├── 📄 <run_or_session>.jsonl  (optional)
                └── 📁 <YYYY-MM-DD>/           (optional date partition)
                    └── 📄 <tool>__<run>.log
~~~

## 🧭 Context

### Background
Text pipelines often require iterative debugging (parser errors, OCR anomalies, encoding issues, chunk boundary checks, entity extraction misses). Keeping these diagnostics in a predictable temporary location reduces clutter elsewhere and avoids mixing debug artifacts with canonical outputs.

### Assumptions
- Artifacts in `data/work/tmp/` are **transient** and may be removed without breaking reproducibility.
- Authoritative outputs flow through the canonical lifecycle:
  `data/raw/ → data/work/ → data/processed/ → data/stac/` (with DCAT/PROV as applicable).

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend must not read from `data/work/tmp/` directly; tmp content is not a contract surface.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should we standardize a JSONL log schema for text steps? | TBD | TBD |
| What is the preferred retention window for tmp logs (days)? | TBD | TBD |

### Future extensions
- Add a structured log schema under `schemas/telemetry/` if/when tmp logs become part of repeatable diagnostics.
- Provide a small helper script under `tools/` to purge tmp logs safely.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Text ETL step: extract/parse/chunk] --> B[Temp debug logs]
  B --> C[data/work/tmp/text/logs/]
  A --> D[Canonical outputs]
  D --> E[data/processed/]
  E --> F[data/stac/]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Text extraction runtime context | env/config | local run / pipeline runner | basic sanity checks |
| Source identifiers | string | derived from ETL input | must not expose secrets |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Debug log (human-readable) | `.log` / `.txt` | `data/work/tmp/text/logs/` | none (ad hoc) |
| Debug log (structured) | `.jsonl` | `data/work/tmp/text/logs/` | none *(optional; avoid drift)* |

### Sensitivity & redaction
Treat tmp logs as **potentially sensitive by default**:
- Do **not** store credentials, tokens, cookies, API keys, or connection strings.
- Avoid dumping full raw text if it may contain PII or restricted content.
- Prefer logging **hashes/IDs**, counts, and short excerpts that are already public or have been redacted.

### Quality signals
- Logs should include enough context to reproduce: step name, tool name, timestamp, and a run/session identifier.
- If structured logs are used, keep one JSON object per line to support grep/jq-style workflows.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- No STAC Items should reference tmp logs as durable assets.
- If a log must be preserved as evidence for an analysis artifact, copy it to an approved retained location and catalog it there.

### DCAT
- Tmp logs are not datasets and should not be exposed as DCAT distributions.

### PROV-O
- Tmp logs may reference run identifiers, but they are not a substitute for canonical provenance bundles under `data/prov/`.

### Versioning
- This directory has no versioning semantics. If a diagnostic artifact must be versioned, treat it as a retained run artifact elsewhere.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL text steps | extract/parse/normalize text | configs + run context |
| Tmp log sink | capture debug output | filesystem writes |
| Durable logging | retained run logs | `data/work/logs/` |

### Interfaces / contracts
- This directory is **not** an API surface and should not be depended upon by services or UI components.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- It does not. Tmp logs should never be directly consumed in Focus Mode narratives.

### Provenance-linked narrative rule
- Any narrative/evidence used in Story Nodes must come from cataloged assets (STAC/DCAT/PROV), not from tmp logs.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Ensure no secrets/credentials are written into tmp logs
- [ ] Ensure tmp logs are not required for deterministic reproduction
- [ ] Keep tmp logs out of PRs unless explicitly requested for debugging

### Reproduction
~~~bash
# Placeholder examples; replace with repo-specific commands.
# run text extraction step and write debug logs here
# validate outputs under data/work/tmp/text/validation/
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes to this README generally require maintainer review only.
- If introducing retained logging schemas or publishing diagnostics, governance review may be required.

### CARE / sovereignty considerations
- Do not include restricted locations or culturally sensitive details in tmp logs.
- If unavoidable during debugging, keep artifacts local and purge promptly.

### AI usage constraints
- No inference of sensitive locations from log content.
- No auto-publishing of tmp artifacts.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README for tmp text logs | TBD |
