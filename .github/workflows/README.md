---
title: "KFM — GitHub Actions Workflows (CI/CD) README"
path: ".github/workflows/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "Reference"
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

doc_uuid: "urn:kfm:doc:ci:workflows-readme:v1.0.0"
semantic_document_id: "kfm-ci-workflows-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:workflows-readme:v1.0.0"
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

# .github/workflows — GitHub Actions for KFM

## 📘 Overview

### Purpose

This README documents how KFM uses GitHub Actions to enforce repository-wide contracts, validation gates, and “repo lint” rules across the canonical pipeline:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

The goal is to keep CI aligned with KFM’s contract-first, evidence-first, provenance-first architecture.

### Scope

| In Scope | Out of Scope |
|---|---|
| GitHub Actions workflows in `.github/workflows/*.yml` (CI checks, validations, scans, scheduled jobs) | Cloud deployment specifics and infra provisioning (belongs under `tools/` and/or separate ops repos) |
| CI gate alignment to KFM contracts and canonical paths | Implementing ETL/domain pipelines (tracked in subsystem docs/runbooks) |
| Workflow determinism rules (skip vs fail behavior) | Adding datasets or story content (handled under `data/` / `docs/`) |

### Audience

- Primary: repo maintainers + contributors authoring/editing CI workflows.
- Secondary: data/catalog/graph/API/UI/story maintainers who depend on CI guarantees.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **CI gate**, **repo lint**, **canonical path**, **schema validation**, **Story Node validation**, **API contract tests**, **security/sovereignty scans**, **deterministic runs**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | KFM core maintainers | Defines canonical pipeline and invariants |
| Redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture maintainers | Defines CI mapping + minimum gates |
| Schemas | `schemas/**` | Schema maintainers | STAC/DCAT/PROV/StoryNodes/UI/Telemetry schemas |
| Catalog outputs | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | Catalog maintainers | Validated artifacts |
| Graph import outputs | `data/graph/csv/**`, `data/graph/cypher/**` | Graph maintainers | Inputs to Neo4j loader |
| API contracts | `src/server/contracts/**` | API maintainers | Contract-first boundary to graph |
| UI code + layer registry | `web/**` (incl. `**/layers/**`) | UI maintainers | UI consumes API; layer registry schema-validates |
| Story Nodes | `docs/reports/story_nodes/**` | Curators + reviewers | Published nodes must validate |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] CI gate list matches the repo’s current workflows (update this doc when workflows change)
- [ ] “Skip vs fail” behavior documented
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Validation expectations are repeatable (at least at a high level)

---

## 🗂️ Directory Layout

### This document

- `path`: `.github/workflows/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub workflows | `.github/workflows/` | GitHub Actions workflows for tests, data updates, and deployments |
| Schemas | `schemas/` | JSON Schemas and constraint bundles used by CI + runs |
| Data domains | `data/<domain>/` | `raw/`, `work/`, `processed/` per domain |
| STAC | `data/stac/` | `collections/` + `items/` outputs |
| DCAT | `data/catalog/dcat/` | dataset catalog records |
| PROV | `data/prov/` | lineage bundles |
| Graph import | `data/graph/` | CSV + Cypher outputs for Neo4j ingest |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog builders |
| Graph build | `src/graph/` | ontology bindings + build scripts |
| API | `src/server/` | API boundary (REST/GraphQL) |
| UI | `web/` | React/MapLibre/Cesium front-end; layer registry lives under `web/**/layers/**` |
| Story Nodes | `docs/reports/story_nodes/` | governed narrative artifacts + metadata |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | observability + governance signals |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 workflows/
    ├── 📄 README.md
    └── 📄 *.yml
~~~

> Note: The specific workflow filenames and job layouts are intentionally not enumerated here unless they exist in-repo. Keep this README synchronized with the actual `.yml` files present.

---

## 🧭 Context

KFM’s CI is a **pipeline contract enforcement layer**, not just “unit tests.” It exists to keep the system aligned to:

- canonical pipeline ordering and invariants,
- contract-first API boundaries,
- provenance-first content rules,
- schema-valid catalogs and story outputs.

KFM’s design rules also include: **the UI must not connect to Neo4j directly**; it must access the graph via the API contracts and enforce provenance and redaction rules at the boundary.

GitHub repository conventions place CI configuration in `.github/` (often hidden), including GitHub Actions workflows used for tests, data updates, and deployments (as applicable). [oai_citation:5‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

## 🗺️ Diagrams

### Canonical pipeline and where CI gates apply

~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph<br/>data/graph + src/graph]
  C --> D[API Boundary<br/>src/server + contracts]
  D --> E[UI<br/>web]
  E --> F[Story Nodes<br/>docs/reports/story_nodes]
  F --> G[Focus Mode<br/>provenance-linked only]

  CI[CI Gates<br/>.github/workflows] -. validates .-> A
  CI -. validates .-> B
  CI -. validates .-> C
  CI -. validates .-> D
  CI -. validates .-> E
  CI -. validates .-> F
~~~

### CI gate flow on Pull Requests

~~~mermaid
flowchart TB
  PR[Pull Request] --> CI[GitHub Actions]
  CI --> MD[Markdown protocol validation]
  CI --> SC[Schema validation]
  CI --> SN[Story Node validation]
  CI --> API[API contract tests]
  CI --> SEC[Security + sovereignty scanning]
  MD --> OK[Merge allowed]
  SC --> OK
  SN --> OK
  API --> OK
  SEC --> OK
~~~

---

## 📦 Data & Metadata

### CI inputs

- The repository content under canonical roots (e.g., `schemas/`, `data/`, `src/`, `web/`, `docs/`).
- A PR diff or branch tip on push.
- Optional: cached dependencies and/or precomputed validation artifacts.

### CI outputs

- Status checks on PRs/branches.
- Optional artifacts (test reports, schema validation reports, lint summaries).

### Quality signals

CI should provide (at minimum) signals that:

- STAC/DCAT/PROV artifacts validate against schemas in `schemas/`.
- No orphan references (entity refs, evidence refs, Story Node refs resolve).
- Runs are deterministic and outputs are diffable.

---

## 🌐 STAC, DCAT & PROV Alignment

CI workflows are expected to validate that catalog and lineage outputs adhere to KFM’s canonical layout:

- STAC outputs in `data/stac/**`
- DCAT outputs in `data/catalog/dcat/**`
- PROV outputs in `data/prov/**`

Schemas for these live under `schemas/stac/`, `schemas/dcat/`, and `schemas/prov/` (plus additional schema families for Story Nodes, UI, telemetry). When these artifacts exist in the repo, CI must validate them against the canonical schemas.

---

## 🧱 Architecture

### CI gates required for v13 readiness

Minimum CI gates (v13 readiness):

- Markdown protocol validation
- Schema validation
- Story Node validation
- API contract tests
- Security and sovereignty scanning gates

CI should also enforce basic “repo lint” rules:

- No YAML front-matter in code files (split into docs or metadata files).
- No duplicate canonical homes for the same subsystem without explicit deprecation markers.
- No typo-paths (e.g., `README.me`).

### Determinism rule for validations

CI workflows must be deterministic in “skip vs fail” behavior:

- If an **optional root** is absent, the corresponding validation may **skip**.
- If the root is **present** but invalid, CI must **fail deterministically**.

> Keep this behavior consistent so contributor expectations match actual CI outcomes.

### Canonical contract roots CI may depend on

The v13 contract set expects (at minimum) these canonical roots to exist and remain stable:

- `schemas/` (STAC/DCAT/PROV/StoryNodes/UI/telemetry)
- `data/stac/`, `data/catalog/dcat/`, `data/prov/`
- `data/graph/` outputs for ingest
- `src/server/contracts/` for API boundary
- `docs/reports/story_nodes/` for published narrative artifacts

If CI workflows reference other roots (e.g., `releases/`, `scripts/`, `.github/actions/`), ensure those roots exist and are kept in sync with docs and workflow expectations.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes are a governed artifact and must live at:

- `docs/reports/story_nodes/`

Design rules that CI should enforce for published Story Nodes:

- validate front-matter, citations, entity references, redaction compliance.
- Focus Mode consumes only provenance-linked content.
- Predictive/AI-generated content is opt-in and includes uncertainty metadata; it must never appear as unmarked fact.

---

## 🧪 Validation & CI/CD

### What CI must enforce (conceptual checklist)

- [ ] Markdown protocol validation for governed docs that require it (templates, story nodes, selected policies)
- [ ] Schema validation for any STAC/DCAT/PROV outputs present
- [ ] Story Node validation for published nodes
- [ ] API contract tests for `src/server/contracts/**`
- [ ] Security + sovereignty scanning gates (especially for sensitive locations, restricted knowledge, and redaction expectations)

### Local validation

Not confirmed in repo: the exact local commands/scripts/Make targets. If local tooling exists, document it here (and keep it in sync with CI).

~~~bash
# not confirmed in repo — replace with repo’s actual validation commands
# make lint
# make validate-schemas
# make validate-story-nodes
# make test-api-contracts
# make scan-security
~~~

---

## ⚖ FAIR+CARE & Governance

### Sensitivity and redaction enforcement

Any restricted locations or culturally sensitive knowledge must be protected via:

- generalization of geometry where required,
- API-level redaction,
- Story Node asset review gates.

CI should treat sensitivity and redaction violations as **blocking** for merges when the relevant artifacts are present.

### Governance approvals required (if any)

- FAIR+CARE council review: yes/no
- Security council review: yes/no
- Historian/editor review: yes/no

### AI usage constraints

This README’s AI transform permissions/prohibitions are defined in front-matter and should remain aligned with repo governance.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial workflows README scaffold | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
