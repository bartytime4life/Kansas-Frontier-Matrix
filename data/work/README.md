---
title: "KFM — data/work Staging Area (README)"
path: "data/work/README.md"
version: "v1.0.0"
last_updated: "2025-12-17"
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

doc_uuid: "urn:kfm:doc:data:work:readme:v1.0.0"
semantic_document_id: "kfm-data-work-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:readme:v1.0.0"
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

# KFM `data/work/` — Staging Workspace (README)

## 📘 Overview

### Purpose
- Define what belongs in `data/work/` and what does **not**, as part of KFM’s governed ETL → catalog → graph → API → UI pipeline.
- Establish a **directory contract**: `data/work/` is for **intermediate / staging artifacts** produced during ETL runs (i.e., between `data/raw/` and `data/processed/`), and is **not** a stable interface for downstream consumers.

### Scope
| In Scope | Out of Scope |
|---|---|
| Intermediate transformation outputs (e.g., temporary normalized tables, clipped rasters, intermediate joins/derivatives) | Authoritative “source of truth” raw drops (use `data/raw/`) |
| Per-run staging artifacts used to produce `data/processed/` outputs | Final, validated outputs intended for ingestion (use `data/processed/`) |
| Small manifests/notes that help reproduce or debug a run (non-sensitive) | Secrets, credentials, tokens, private keys |
| Temporary exports used for validation and QA before promotion | Public-facing datasets without STAC/DCAT/PROV metadata |

### Audience
- Primary: ETL/pipeline maintainers, data engineers, CI maintainers
- Secondary: contributors reviewing a pipeline PR, governance reviewers (when a run introduces sensitive materials)

### Definitions
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **raw / work / processed**
  - **ETL run**
  - **staging artifact**
  - **promotion** (moving an output from `work/` to `processed/`)
  - **cataloging** (STAC/DCAT/PROV)
  - **provenance** (PROV-O)
  - **deterministic / replayable**

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `data/work/README.md` | TBD | Directory contract for `data/work/` |
| Raw inputs | `data/raw/` | TBD | Source drops (avoid mutating; treat as inputs) |
| Work staging | `data/work/` | TBD | Intermediate outputs; may be cleaned/regenerated |
| Processed outputs | `data/processed/` | TBD | Validated outputs intended for catalog + ingestion |
| Catalogs | `data/stac/` (+ associated docs) | TBD | Cataloged assets (STAC/DCAT/PROV) |
| ETL configs / code | `src/pipelines/` (or repo-defined equivalent) | TBD | Deterministic transforms |
| Run logs | `mcp/runs/` or `mcp/experiments/` | TBD | Replay + audit trail (path may vary by repo) |
| Schemas / validators | `schemas/` | TBD | STAC/DCAT/PROV + other schema checks |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] `data/work/` purpose is explicitly distinguished from `data/raw/` and `data/processed/`
- [ ] Promotion criteria to `data/processed/` documented (at a minimum, validation + provenance expectations)
- [ ] Governance + CARE/sovereignty considerations explicitly stated (esp. for sensitive locations)
- [ ] Validation / reproduction steps are listed (even if placeholders pending repo command names)

## 🗂️ Directory Layout

### This document
- `path`: `data/work/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Raw sources | `data/raw/` | Original ingested sources / downloads (inputs) |
| Work staging | `data/work/` | Intermediate artifacts generated during transforms |
| Final outputs | `data/processed/` | Final cleaned/normalized assets ready for catalogs + ingestion |
| Catalogs | `data/stac/` | STAC Collections/Items and related metadata |
| Provenance | `data/stac/` + graph | PROV activities/entities/agents linked to generated outputs |
| Schemas | `schemas/` | JSON schema / validators used by CI |
| Runs & telemetry | `mcp/runs/` / `docs/telemetry/` | Replay logs, run metadata, audit/telemetry (paths may vary) |

### Expected file tree for this sub-area
~~~text
🗂️ data/
├── 🧱 raw/
├── 🧪 work/
│   ├── 📄 README.md
│   ├── 📁 <domain-or-pipeline>/         # optional (pattern; not guaranteed)
│   │   ├── 📁 <run-id>/                 # optional (pattern; not guaranteed)
│   │   │   ├── 🧾 manifest.json         # recommended: small provenance stub / inputs list
│   │   │   ├── 🧩 intermediate/         # intermediate outputs (may be large/binary)
│   │   │   └── 📝 notes.md              # debug notes (non-sensitive)
│   │   └── 🧹 _tmp/                     # local-only scratch (recommend gitignored)
│   └── 🧹 _tmp/
└── 🏁 processed/
~~~

## 🧭 Context

### Background
- KFM’s pipeline is ordered and contract-driven: ETL produces deterministic, replayable transforms; artifacts move through `data/raw/ → data/work/ → data/processed/`.
- `data/work/` exists to keep **in-progress** ETL outputs separate from:
  - **inputs** (`data/raw/`)
  - **publishable outputs** (`data/processed/` + catalogs)

### Assumptions
- ETL runs are intended to be **deterministic** and **replayable** given the same inputs/configs.
- Processed outputs (not work artifacts) are the ones that get:
  - STAC Collection/Item representation
  - DCAT mapping
  - PROV activity record linking inputs → outputs

### Constraints / invariants
- `data/work/` is **not** a stable public contract:
  - Don’t build downstream dependencies (UI, API, catalog loaders) that require `data/work/`.
- Promotion boundary:
  - If an output is meant to be consumed downstream (catalog → graph → API → UI), it must be promoted to `data/processed/` and cataloged/validated.
- Governance boundary:
  - If staging artifacts contain potentially sensitive cultural sites/locations, apply redaction/generalization rules before any publishing/export; consult `docs/governance/SOVEREIGNTY.md` and related governance docs.
- No secrets:
  - Never store credentials, tokens, or private keys in `data/work/` (or anywhere in the repo).

### Open questions
| Question | Why it matters | Proposed owner | Status |
|---|---|---|---|
| Should we standardize a required `data/work/<domain>/<run-id>/manifest.json` schema? | Improves reproducibility + automated promotion | TBD | Open |
| What is the official retention/cleanup policy for `data/work/` artifacts? | Prevents unbounded repo growth | TBD | Open |
| Are large `data/work/` artifacts tracked via DVC/object storage or excluded via `.gitignore`? | Keeps Git history manageable | TBD | Open |

### Future extensions
- Define a minimal “work manifest” schema that can be auto-generated by ETL and later converted into PROV and/or STAC assets.
- Add CI checks that prevent accidental commits of sensitive/binary staging artifacts (size thresholds + file-type denylist).
- Add a “promotion tool” that:
  1) validates, 2) stamps checksums, 3) writes STAC/DCAT/PROV, 4) moves outputs to `data/processed/`.

## 🗺️ Diagrams

### KFM data flow positioning for `data/work/`
~~~mermaid
flowchart TD
  A["data/raw/ — inputs"] --> B["data/work/ — staging"]
  B --> C["data/processed/ — final outputs"]

  C --> D["data/stac/ — STAC + DCAT + PROV catalogs"]
  D --> E["Neo4j graph"]
  E --> F["APIs"]
  F --> G["UI"]
  E --> H["Story Nodes / Focus Mode"]
~~~

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/` (and staged via `data/work/` as needed)
- [ ] STAC: new collection + item schema validation (for promoted outputs)
- [ ] PROV: activity + agent identifiers recorded (for promoted outputs)
- [ ] Graph: new labels/relations mapped + migration plan (if outputs introduce new entities)
- [ ] APIs: contract version bump + tests (if new outputs require new endpoints)
- [ ] UI: layer registry entry + access rules (if new outputs become visual layers)
- [ ] Focus Mode: provenance references enforced (no claims without linked evidence)
- [ ] Telemetry: new signals + schema version bump (if new runs introduce new metrics)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- `data/work/` artifacts should **not** be referenced directly in Story Nodes / Focus Mode.
- Only outputs that have been promoted to `data/processed/` **and** cataloged (STAC/DCAT/PROV) should surface as evidence for narrative generation.

### Provenance-linked narrative rule
- Every factual claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV) for any outputs promoted beyond `data/work/`
- [ ] Graph integrity checks (if new processed outputs are ingested)
- [ ] API contract tests (if behavior changes)
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) Run ETL deterministically (same inputs/configs => same outputs)
# 2) Validate schemas
# 3) Run tests + lint docs
#
# e.g.
# make etl
# make validate-schemas
# make test
# make docs-lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD / N-A | ETL runner | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes that introduce any of the following should trigger governance review:
  - New sensitive layers
  - New AI narrative behaviors
  - New external data sources
  - New public-facing endpoints

### CARE / sovereignty considerations
- `data/work/` may temporarily contain sensitive location-derived artifacts during processing.
- Before promotion/publishing:
  - apply redaction/generalization rules where required,
  - ensure any restricted coordinates are protected per sovereignty policy.

### AI usage constraints
- Ensure this doc’s `ai_transform_permissions` / `ai_transform_prohibited` align with intended use.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial `data/work/` README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
