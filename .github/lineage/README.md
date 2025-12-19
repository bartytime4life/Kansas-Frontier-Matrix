---
title: "KFM Lineage & Provenance — GitHub Lineage Area"
path: ".github/lineage/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:github:lineage-readme:v1.0.0"
semantic_document_id: "kfm-github-lineage-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:lineage-readme:v1.0.0"
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

# KFM Lineage & Provenance — GitHub Lineage Area

## 📘 Overview

### Purpose
This directory documents how Kansas Frontier Matrix (KFM) contributors keep **lineage** (a.k.a. provenance)
complete and reviewable when code/data/docs change.
It is intended to support repeatable reviews and CI gates by pointing to where the *actual* provenance
artifacts live (STAC/DCAT/PROV + graph lineage), and what “done” looks like for a lineage-complete PR.

### Scope

| In Scope | Out of Scope |
|---|---|
| Contributor-facing lineage expectations for PRs that change data, catalogs, graph ingestion, APIs, UI layers, or story nodes | Implementing the pipelines or CI workflows themselves |
| Where to put lineage artifacts (STAC/DCAT/PROV) and what they must reference | Defining or changing governance policy documents |
| A review checklist for provenance completeness and sensitivity handling | Adding new ontology labels/relationships (handled in graph docs + migrations) |

### Audience
- Primary: Contributors and reviewers who touch data pipelines, catalogs, graph ingestion, or narrative outputs
- Secondary: Maintainers who define CI gates and repo standards

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Lineage / Provenance**: Traceability of outputs back to inputs via activities, agents, and derivations (PROV-O).
  - **Catalogs**: STAC (assets), DCAT (dataset views), PROV (lineage bundles).
  - **Run ID**: Stable identifier for a pipeline execution (ETL/catalog build/graph build), referenced from outputs.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical ordering + “no unsourced narrative” rule |
| PROV lineage bundles | `data/prov/` | Pipelines / Catalog owners | PROV records for major transforms and loads |
| STAC catalogs | `data/stac/` | Catalog owners | Items + Collections for spatiotemporal assets |
| DCAT dataset records | `data/catalog/dcat/` | Catalog owners | Dataset-level metadata + aggregation views |
| Security + governance references | `.github/SECURITY.md` + `docs/security/` | Security / Maintainers | Review triggers + secure practices |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Lineage expectations map to KFM pipeline invariants (ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode)
- [ ] Explicitly states where provenance artifacts live and what must be updated for data-affecting changes
- [ ] Validation steps are listed and repeatable (even if repo-specific commands are placeholders)
- [ ] Sensitivity/sovereignty expectations are called out (no restricted location leakage)
- [ ] No implied “UI reads Neo4j directly” behavior (API boundary preserved)

## 🗂️ Directory Layout

### This document
- `path`: `.github/lineage/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub controls | `.github/` | Security docs, CI workflows, contribution templates |
| Provenance bundles | `data/prov/` | PROV JSON-LD describing activities/agents/derivations |
| STAC catalogs | `data/stac/` | STAC collections/items for assets |
| DCAT catalogs | `data/catalog/dcat/` | Dataset-level catalog records |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | ETL + catalog generation + transforms |
| Graph | `src/graph/` + `docs/graph/` | Ontology bindings, ingestion, migrations |
| APIs | `src/server/` + docs | Contracted access layer (REST/GraphQL) |
| UI | `web/` + `docs/design/` | Map layers + Focus Mode UX |

### Expected file tree for this sub-area
~~~text
📁 .github/
├── 📄 SECURITY.md
└── 📁 lineage/
    └── 📄 README.md
~~~

## 🧭 Context

### Background
KFM’s core invariant is that **provenance is first-class** and narratives shown to users must not be
unsourced. Lineage is captured via **STAC/DCAT/PROV metadata** and mirrored in the graph as lineage links.
This repo area exists to keep contributor workflow aligned with those requirements.

### Assumptions
- Pipelines are deterministic and replayable (same inputs + config → same outputs).
- Data products are cataloged before graph ingestion (catalogs are the handoff contract).
- Provenance is expressed in PROV-O (JSON-LD or equivalent) and links inputs → activities → outputs.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Focus Mode consumes provenance-linked content only; any predictive/inferential content must be opt-in and carry uncertainty metadata.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should CI block merges when a data-affecting PR lacks updated PROV bundles? | Maintainers | TBD |
| What is the canonical “run_id” schema (format, stability rules)? | Pipelines | TBD |
| Where should “example” lineage bundles live for onboarding (docs vs .github)? | Maintainers | TBD |

### Future extensions
- Add a PR checklist template under `.github/` that links here for lineage expectations.
- Add a small set of example PROV bundles under `data/prov/examples/` (if governance allows).
- Add a CI job that validates STAC/DCAT/PROV schemas and fails on broken internal references.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  PR[Pull Request] --> CI[CI gates: validate docs + catalogs + lineage]
  CI -->|pass| Merge[Merge]
  Merge --> ETL[ETL]
  ETL --> Catalogs[STAC/DCAT/PROV Catalogs]
  Catalogs --> Graph[Neo4j Graph]
  Graph --> API[API Layer]
  API --> UI[React/Map UI]
  UI --> Story[Story Nodes]
  Story --> Focus[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant CI as CI/Checks
  participant Repo as Repo Artifacts

  Dev->>Repo: Modify data/code/docs
  Dev->>Repo: Update STAC/DCAT/PROV outputs (as needed)
  Dev->>CI: Open PR
  CI->>Repo: Validate markdown + schemas + link integrity
  CI-->>Dev: Pass/Fail with actionable errors
  Dev->>Repo: Fix issues until lineage is complete
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC items/collections | JSON | `data/stac/` | STAC schema + link checks |
| DCAT dataset records | JSON-LD/Turtle | `data/catalog/dcat/` | DCAT profile validation |
| PROV lineage bundles | JSON-LD | `data/prov/` | PROV profile validation + internal reference checks |
| Pipeline run logs (optional) | text/JSON | `mcp/runs/` or pipeline outputs | Consistency checks; no secrets |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Lineage-complete change set | Git diff | PR | Must include required catalog + provenance updates |
| Validated catalogs | JSON / JSON-LD | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | KFM-STAC / KFM-DCAT / KFM-PROV profiles |
| Review evidence | Markdown | PR description + links | Must cite dataset/document IDs as applicable |

### Sensitivity & redaction
- Ensure dataset records carry classification/sensitivity tags as applicable.
- If a dataset contains restricted locations, document generalization/redaction rules and ensure outputs do not expose precise coordinates.

### Quality signals
- Stable IDs (dataset IDs, item IDs, run IDs) and consistent versioning links.
- Deterministic pipeline behavior and reproducible outputs.
- Hashes/checksums for inputs/outputs where feasible.
- No broken references between STAC/DCAT/PROV and graph ingestion expectations.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Use STAC Collections + Items to describe assets with spatial/temporal coverage and links to source material.
- Keep Item links consistent and validate that referenced assets exist.

### DCAT
- Use DCAT dataset records for dataset-level discovery (title/description/license/keywords at minimum).
- Maintain dataset identifiers and version lineage where applicable.

### PROV-O
- `prov:wasDerivedFrom`: enumerate input entities (source items, prior dataset versions).
- `prov:wasGeneratedBy`: reference the producing activity (pipeline run ID).
- Activity / Agent identities: activities identify transforms/loads; agents identify scripts/services/people as allowed by governance.

### Versioning
- New versions link predecessor/successor.
- Graph mirrors version lineage.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| CI gates | Enforce schema + doc + integrity checks on PRs | GitHub checks / workflows |
| ETL | Ingest + normalize sources | Config + run logs |
| Catalogs | Generate STAC/DCAT/PROV outputs | JSON/JSON-LD + validators |
| Graph | Ingest catalogs into Neo4j with provenance links | API-mediated graph queries |
| APIs | Serve contracted access to graph + catalogs | REST/GraphQL |
| UI | Map + narrative UX | API calls only |
| Story Nodes | Curated narrative artifacts with provenance | Docs + graph pointers |
| Focus Mode | Provenance-linked contextual synthesis | Provenance refs + audit flags |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Catalog schemas/validators | `schemas/` + pipeline validators | Semver + changelog |
| API schemas | `src/server/` + docs | Backward compat or version bump |
| UI layer registry | `web/` (see UI docs) | Schema-validated; no hidden data leakage |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focus Mode should only render context that can be traced to dataset/document IDs.
- Provenance references must be available for audit panels and citation rendering.

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
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks
- [ ] API contract tests (if APIs changed)
- [ ] UI schema checks (layer registry, if UI changed)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate STAC JSON
# 2) validate DCAT records
# 3) validate PROV JSON-LD
# 4) run graph integrity checks (if graph ingestion changed)
# 5) run API/UI tests as needed
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| pipeline_run_id | ETL/catalog/graph run | `mcp/runs/` (or pipeline logs) |
| artifact_hashes | catalogs/prov outputs | catalog/prov metadata fields |
| validation_status | CI | CI logs + PR checks |

## ⚖ FAIR+CARE & Governance

### Review gates
Changes typically require additional review when they involve:
- New sensitive layers
- New AI narrative behaviors
- New external data sources
- New public-facing endpoints

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.
- Redact/generalize restricted locations as required by sovereignty policy.

### AI usage constraints
- No unsourced narrative for user-facing contexts.
- Any AI-derived or inferential output must be clearly marked, opt-in where required, and must not infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial lineage README scaffolding | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`