---
title: "Lineage Scripts Library README"
path: ".github/lineage/scripts/lib/README.md"
version: "v1.0.0"
last_updated: "2025-12-29"
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

doc_uuid: "urn:kfm:doc:ci:lineage-scripts-lib-readme:v1.0.0"
semantic_document_id: "kfm-ci-lineage-scripts-lib-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:lineage-scripts-lib-readme:v1.0.0"
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

# Lineage Scripts Library

## 📘 Overview

### Purpose

This directory contains shared library code used by CI lineage entrypoints under `.github/lineage/scripts/`.

It exists to keep KFM’s provenance and catalog rules **enforced in automation**: every dataset/build step must remain traceable through STAC/DCAT/PROV artifacts and must respect governance controls (FAIR+CARE, sovereignty, sensitivity).

### Scope

| In Scope | Out of Scope |
|---|---|
| CI-friendly helpers for validating and producing lineage artifacts (STAC/DCAT/PROV) | Domain ETL business logic (belongs in `src/pipelines/`) |
| Deterministic helpers (stable IDs, checksums, diff-friendly output) | Direct Neo4j access from UI or CI-only “shortcuts” that bypass the API boundary |
| Validation wrappers (schema validation, link checks, “provenance present” checks) | Any policy invention beyond what governed docs + schemas already specify |
| Redaction/generalization utilities that *apply* declared governance rules | Storing secrets/credentials, or calling external network services by default |

### Audience

- Primary: CI maintainers, pipeline developers, data engineering stewards
- Secondary: graph/API/UI maintainers who need to interpret lineage failures and provenance outputs

### Definitions

- Glossary: `docs/glossary.md` (not confirmed in repo)
- Terms used here:
  - **Lineage / provenance**: a record of what inputs produced what outputs, by which activity/agent.
  - **Catalog artifacts**: STAC Items/Collections, DCAT datasets, PROV records.
  - **Run**: an execution of a pipeline or validation workflow (may emit run logs under `mcp/runs/`).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline ordering and CI gates |
| Ingestion architecture | `docs/architecture/KFM_INGEST_ARCHITECTURE.md` | Data Eng | Defines ingestion patterns and catalog paths |
| STAC outputs | `data/stac/` | Data Eng | Collections + Items |
| DCAT outputs | `data/catalog/dcat/` | Data Eng | JSON-LD DCAT datasets |
| PROV outputs | `data/prov/` | Data Eng | PROV JSON-LD/Turtle lineage records |
| Schemas | `schemas/` | Data Eng | JSON schema validation for STAC/DCAT/PROV + docs |
| Graph ingest tooling | `src/graph/` | Graph | Loads catalogs into Neo4j |
| API boundary | `src/server/` | API | Contracted access; UI does not read graph directly |
| UI | `web/` | UI | React/MapLibre; consumes only via APIs |
| Story node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story | Narrative artifacts must be provenance-linked |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Governs API changes |

### Definition of done

- [ ] Front-matter complete and valid
- [ ] All claims point to governed docs / schemas / tickets / commits as applicable
- [ ] Validation expectations and failure modes are documented and repeatable
- [ ] Governance, sensitivity, sovereignty considerations are explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/lineage/scripts/lib/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI workflows | `.github/workflows/` | GitHub Actions pipelines that call lineage scripts |
| Lineage entrypoints | `.github/lineage/scripts/` | Small CLI entrypoints invoked by workflows |
| Lineage library | `.github/lineage/scripts/lib/` | Shared helpers used by lineage entrypoints |
| Data domains | `data/` | Raw/work/processed, plus catalog outputs |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV artifacts |
| Pipelines | `src/pipelines/` | ETL and catalog build code (canonical home) |
| Graph | `src/graph/` | Graph build + ontology mappings |
| Schemas | `schemas/` | Validation schemas for artifacts |
| API | `src/server/` | Contracted API boundary |
| UI | `web/` | React/MapLibre frontend |
| Story Nodes | `docs/reports/story_nodes/` | Story artifacts (draft/published split not confirmed in repo) |

### Expected structure

~~~text
.github/
└─ ⚙️ lineage/
   └─ 🧬 scripts/
      ├─ 📚 lib/
      │  └─ 📄 README.md
      └─ 🚀 <entrypoints> (not confirmed in repo)
~~~

## 🧱 Architecture fit

KFM’s non-negotiable pipeline ordering is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

This library exists to help CI enforce that ordering (no shortcuts) and to ensure “Focus Mode only consumes provenance-linked content.”

~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines/] --> B[Catalog artifacts<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph ingest<br/>src/graph/]
  C --> D[API boundary<br/>src/server/]
  D --> E[UI<br/>web/]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  subgraph CI[CI lineage guardrails]
    L[.github/lineage/scripts] --> H[validate + emit lineage signals]
  end

  H -. pass/fail gate .-> B
~~~

## 🧰 What this library should do

This folder should hold **small, testable, deterministic** helpers that entrypoint scripts can reuse.

Recommended capability buckets:

1. **Catalog validation wrappers**
   - Validate STAC Items/Collections, DCAT JSON-LD, and PROV records against `schemas/` profiles.
   - Enforce that every published dataset has the triad: STAC + DCAT + PROV.

2. **Provenance enforcement**
   - Assert `prov:wasDerivedFrom` and `prov:wasGeneratedBy` are present for produced Entities.
   - Assert every dataset generation step has a PROV Activity.

3. **Stable identifiers and checksums**
   - Provide helpers for stable dataset IDs, activity IDs, and content hashing (sha256).
   - Ensure outputs are diff-friendly: stable ordering, normalized formatting.

4. **Governance and safety gates**
   - Provide helpers to propagate `sensitivity`/`classification` tags across artifacts.
   - Support redaction/generalization hooks for sensitive geometry or sovereign datasets.
   - Never infer or reveal sensitive locations.

5. **Telemetry hooks**
   - Emit (or format) events like: `classification_assigned`, `redaction_applied`, `promotion_blocked`, `catalog_published`.
   - If telemetry schema exists, validate emitted telemetry payloads.

## 🧾 PROV conventions

KFM’s conventions treat:

- **Activities** as ETL jobs or sub-steps (each should have a unique Activity ID).
- **Agents** as software and optionally humans associated with Activities.
- **Entities** as inputs/outputs (files, datasets, documents, derived artifacts).

Recommended ID pattern (example):

- Activity: `urn:kfm:activity:ingest:<domain>:<datasetX>:v1`
- Software agent: `urn:kfm:agent:software:<pipeline-name>:v1`
- Entity: `urn:kfm:entity:<kind>:<domain>:<datasetX>:v1`

When a dataset is superseded, treat the new version as a new Entity/Activity and relate versions via PROV revision/derivation and catalog version pointers.

Example shape (illustrative only):

~~~json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "entity": {
    "urn:kfm:entity:dataset:domain:datasetX:v1": {
      "prov:label": "datasetX processed outputs v1",
      "prov:wasGeneratedBy": "urn:kfm:activity:ingest:domain:datasetX:v1"
    }
  },
  "activity": {
    "urn:kfm:activity:ingest:domain:datasetX:v1": {
      "prov:startTime": "YYYY-MM-DDThh:mm:ssZ",
      "prov:endTime": "YYYY-MM-DDThh:mm:ssZ",
      "prov:used": [
        "urn:kfm:entity:source:domain:sourceA:v1",
        "urn:kfm:entity:source:domain:sourceB:v1"
      ],
      "prov:wasAssociatedWith": "urn:kfm:agent:software:etl:datasetX:v1"
    }
  }
}
~~~

## 🧪 Validation and CI expectations

Lineage workflows should support (at minimum):

- Markdown protocol validation for governed docs (front-matter + required sections)
- Link and reference checks (no orphan pointers; “not confirmed in repo” where appropriate)
- Schema validation:
  - STAC/DCAT/PROV
  - story node schemas (if present)
  - telemetry schemas (if present)
  - UI layer registry schemas (if present)
- Graph integrity tests (constraints/labels/edges)
- API contract tests (OpenAPI/GraphQL)
- Security and sovereignty scanning gates:
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks

## 🔐 Security, sensitivity, and sovereignty

Non-negotiables:

- Do not embed credentials in scripts or logs.
- Do not call out to external networks unless explicitly allowed by workflow policy.
- Any redaction/generalization must be enforced consistently:
  - in `data/processed/**`
  - in catalogs (STAC/DCAT)
  - in API responses (redaction policies)
  - in UI rendering (CARE gating)

If you are unsure whether a dataset/location is sensitive, treat it as sensitive until reviewed.

## 🧩 Contributing guidelines

- Prefer pure functions and explicit inputs/outputs.
- Prefer “library in `tools/` or `src/pipelines/`” for reusable logic; keep `.github/` code as CI glue where possible.
- If you must reference a file/path that may not exist yet, explicitly label it `not confirmed in repo` and add a ticket to create/align it.
- Add tests for anything that can break determinism or leak sensitive data.

## 📚 Project reference shelf

This README was authored to align with KFM’s governed documents, templates, and reference pack.

<details>
  <summary>Canonical KFM docs and templates</summary>

- `docs/MASTER_GUIDE_v12.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- `docs/architecture/KFM_INGEST_ARCHITECTURE.md`
- Kansas Frontier Matrix (KFM) Implementation Guide (PDF)
- Kansas Frontier Matrix — System Structure and Scope (PDF)
- Kansas Frontier Matrix — Visual and Functional Overview (PDF)
- KFM Reference Data (PDF)
- Elevating the Kansas Frontier Matrix: Gaps and Proposed Enhancements (PDF)
- Expanding the Kansas Frontier Matrix Knowledge Base (PDF)
- Expanding the Kansas Frontier Matrix: External Data, Tools, and Frameworks (PDF)
- Comprehensive Guide to Markdown in Programming and Documentation (PDF)
- The Comprehensive Markdown Guide (PDF)
- KFM 1.0 System Documentation (PDF) — not confirmed in repo

</details>

<details>
  <summary>Optional technical references in the project pack</summary>

- Git Notes for Professionals (PDF)
- Node.js Notes for Professionals (PDF)
- PostgreSQL Notes for Professionals (PDF)
- MySQL Notes for Professionals (PDF)
- Geoprocessing with Python (PDF)
- Spatial Data Analysis and Visualisation in R (PDF)
- Graphical Data Analysis with R (PDF)
- CSS Notes for Professionals (PDF)
- Responsive Web Design with HTML5 and CSS3 (PDF)
- WebGL Programming Guide (PDF)
- Computer Graphics using Java 2D & 3D (PDF)
- Bayesian computational methods (PDF)
- Regression analysis with Python (PDF)
- Data Mining concepts & applications (PDF)
- AI Foundations of Computational Agents (PDF)
- Artificial neural networks introduction (PDF)
- Deep learning in Python prerequisites (PDF)
- Data Science & Machine Learning methods (PDF)
- Scalable Data Management for Future Hardware (PDF)
- Scientific Modeling and Simulation NASA-grade guide (PDF)
- Designing Virtual Worlds (PDF)

</details>

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-29 | Initial README for `.github/lineage/scripts/lib/` | TBD |
