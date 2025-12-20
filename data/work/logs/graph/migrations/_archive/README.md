---
title: "README — Graph Migration Logs Archive"
path: "data/work/logs/graph/migrations/_archive/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
status: "draft"
doc_kind: "Readme"
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

doc_uuid: "urn:kfm:doc:data:work:logs:graph:migrations:archive:readme:v1.0.0"
semantic_document_id: "kfm-data-work-logs-graph-migrations-archive-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:logs:graph:migrations:archive:readme:v1.0.0"
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

# data/work/logs/graph/migrations/_archive

## 📘 Overview

### Purpose
This directory is **cold storage** for **archived** Graph migration run artifacts (logs, manifests, and checksums) that are no longer “active” but still useful for audit, debugging, and reproducibility reviews.

Use `_archive/` to keep the primary `data/work/logs/graph/migrations/` directory focused on recent / active work while preserving historical run evidence.

### Scope

| In Scope | Out of Scope |
|---|---|
| Archived migration run logs (stdout/stderr captures) | Migration source code / scripts (belongs in `src/graph/...`) |
| Run manifests (what changed, what was applied) | Secrets, tokens, credentials, private keys |
| Checksums/hashes for integrity verification | Raw datasets (belongs in `data/raw/` / `data/processed/`) |
| Failure artifacts needed for postmortems (redacted) | Any sensitive location inference / uncontrolled PII |

### Audience
- Primary: Graph maintainers / migration authors
- Secondary: CI maintainers, auditors/reviewers, incident responders

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: **migration**, **run_id**, **manifest**, **checksum**, **idempotent**, **rollback**

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Active migration logs | `data/work/logs/graph/migrations/` | Graph | “Current” run outputs live here |
| Archived migration logs | `data/work/logs/graph/migrations/_archive/` | Graph | Historical runs preserved here |
| Graph export logs | `data/work/logs/graph/exports/` | Graph | Related: export and snapshot processes |
| Graph checks | `data/work/logs/graph/checks/` | Graph/CI | Related: integrity/constraint checks |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory purpose and boundaries are explicit (what belongs / does not belong)
- [ ] A minimal archival convention is documented (without asserting repo policy)
- [ ] Validation steps include “no secrets” and “no sensitive inference”

## 🗂️ Directory Layout

### This document
- `path`: `data/work/logs/graph/migrations/_archive/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Work logs | `data/work/logs/` | Pipeline run logs + evidence artifacts |
| Graph logs | `data/work/logs/graph/` | Graph-specific runs (checks/exports/migrations) |
| Migration logs | `data/work/logs/graph/migrations/` | Recent/active migration run outputs |
| Archive | `data/work/logs/graph/migrations/_archive/` | Archived migration run bundles |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 work/
    └── 📁 logs/
        └── 📁 graph/
            └── 📁 migrations/
                └── 📁 _archive/
                    ├── 📄 README.md
                    ├── 📄 <archived-run>.log
                    ├── 📄 <archived-run>.manifest.json
                    └── 📄 <archived-run>.sha256
~~~

## 🧭 Context

### Background
Graph migrations may alter:
- constraints / indexes
- ontology-aligned labels/relationships
- backfills or data-shape corrections

Archived logs support:
- investigating historical behavior
- auditing what ran, when, and with what outcome
- correlating graph state changes with downstream API/UI impacts

### Assumptions
- Migration runs produce deterministic, reviewable artifacts.
- Archived artifacts are treated as immutable evidence once moved here.

### Constraints / invariants
- The canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The UI does **not** read Neo4j directly; all consumption is via API contracts.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the retention window for archived logs? | TBD | TBD |
| Should archives be compressed (e.g., `.gz`) or stored as plain text? | TBD | TBD |
| Do we require a standard `manifest.json` schema? | TBD | TBD |

### Future extensions
- Add a small `schemas/telemetry/graph_migration_run.schema.json` for manifests (requires governance review).
- Add an index file `ARCHIVE_INDEX.md` summarizing archived runs (optional).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Graph Migration Run] --> B[Active logs: data/work/logs/graph/migrations/]
  B --> C[Archive decision]
  C --> D[_archive/: immutable archived bundles]
  D --> E[Audit / Debug / Review]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Migration run output | text | graph migration runner | redaction + integrity checks |
| Migration run manifest | JSON | graph migration runner | schema (TBD) + lint |
| Checksums | sha256 text | generated at archival | checksum verify |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Archived logs | `.log` / `.txt` | `_archive/` | none (human-readable) |
| Archived manifest | `.json` | `_archive/` | **not confirmed in repo** |
| Integrity hashes | `.sha256` | `_archive/` | sha256 text |

### Sensitivity & redaction
- Logs MUST NOT include secrets (tokens, passwords, connection strings).
- If logs include user identifiers or sensitive content, redact before committing.
- Avoid embedding full filesystem paths or hostnames if they reveal internal infrastructure.

### Quality signals
- Each archived run bundle should be traceable to:
  - a `run_id` (or timestamped name)
  - a git commit (or build reference) in the manifest
  - a checksum file for integrity

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not applicable directly (logs are not STAC assets by default).

### DCAT
- Not applicable directly (logs are not published datasets by default).

### PROV-O
- Recommended: manifests should reference:
  - `prov:wasGeneratedBy`: migration activity/run id
  - `prov:wasAssociatedWith`: agent (CI job / operator) identifier
  - `prov:used`: migration plan identifier / migration list

### Versioning
- Archived bundles should reflect the migration runner version and target graph version (if known).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Graph migration runner | Apply schema/data migrations | produces logs + manifests |
| CI / validators | Prevent unsafe commits | secret scan + lint |
| Archive directory | Preserve historical evidence | read-only by convention |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Manifest schema | **not confirmed in repo** | Semver if introduced |

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Indirect only: graph migrations may change what entities/relations are queryable and how provenance is resolved.
- No narrative content should be authored or generated in this directory.

### Provenance-linked narrative rule
- Not applicable here (logs are evidence artifacts, not narratives).

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Secret scanning passes (no tokens/credentials in logs)
- [ ] Filenames are stable and non-colliding
- [ ] Checksums verify (if provided)

### Reproduction
~~~bash
# Placeholder — replace with repo-specific commands
# 1) run graph migration runner
# 2) capture logs + generate manifest
# 3) compute sha256 checksums
# 4) move bundle into _archive/
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- If logs contain sensitive content: requires human review before commit.
- If introducing manifest schema or retention rules: requires governance review.

### CARE / sovereignty considerations
- Do not include culturally sensitive or restricted location details in logs.
- If a run touches restricted layers, ensure logs do not disclose protected coordinates.

### AI usage constraints
- This doc permits summarization/structuring but prohibits generating new policy or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial archive README scaffold | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

