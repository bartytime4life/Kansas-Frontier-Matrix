---
title: "KFM — Lineage & Provenance (CI)"
path: ".github/lineage/README.md"
version: "v1.1.1"
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

doc_uuid: "urn:kfm:doc:github:lineage:readme:v1.1.1"
semantic_document_id: "kfm-github-lineage-readme-v1.1.1"
event_source_id: "ledger:kfm:doc:github:lineage:readme:v1.1.1"
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

# KFM Lineage & Provenance CI

This directory documents how Kansas Frontier Matrix (KFM) enforces **provenance and lineage expectations** in CI so that:

- evidence artifacts are traceable end-to-end (inputs → transforms → outputs),
- downstream systems can rely on stable identifiers and deterministic outputs,
- Story Nodes and Focus Mode surface **provenance-linked** content only.

This directory does **not** store provenance payloads. Canonical provenance artifacts are published under `data/prov/**`.

## 📘 Overview

### Purpose

- Define minimum lineage and provenance expectations for artifacts that cross KFM pipeline boundaries.
- Document CI “lineage gates” and where they plug into the repo’s canonical subsystem layout.
- Provide contributor guidance to prevent:
  - orphan references,
  - duplicate canonical homes,
  - narrative claims that cannot be traced back to evidence.

### Scope

| In scope | Out of scope |
|---|---|
| CI expectations for validating PROV bundles and their cross-links | Selecting a specific PROV serialization or validator library (maintainer choice) |
| Cross-link policy between STAC, DCAT, PROV, Graph, APIs, UI, Story Nodes, and Focus Mode | Domain-specific ETL logic (lives under `src/pipelines/` + domain data roots) |
| Determinism and “skip vs fail” behavior for lineage gates | Implementing CI workflows themselves (lives under `.github/workflows/`) |

### Audience

- Contributors adding/updating datasets, evidence products, Story Nodes, catalogs, or UI registries.
- Maintainers implementing and evolving CI validation workflows.
- Reviewers auditing provenance coverage, governance compliance, and reproducibility.

### Definitions

> See also: `docs/glossary.md` *(if present; not confirmed in repo).*

- **Catalogs**: KFM metadata catalogs: STAC (assets), DCAT (dataset/distribution discovery), PROV (lineage).
- **Contract artifact**: a machine-validated schema/spec that defines an interface (e.g., JSON Schema, OpenAPI, GraphQL SDL, UI registry schema).
- **Evidence artifact**: any dataset or derived product intended for downstream use that is cataloged (STAC/DCAT) and backed by PROV lineage.
- **Boundary artifacts**: STAC/DCAT/PROV outputs that must exist before data is considered “published” and allowed into downstream stages.
- **PROV bundle**: a provenance record containing activities, entities, agents, and derivations (serialization is implementation-defined).
- **Lineage gate**: a CI check that validates provenance structure and cross-links; fails closed when artifacts exist but are invalid.
- **Orphan reference**: an identifier/citation that does not resolve to an existing artifact/entity (e.g., missing STAC Item, missing PROV Activity, missing graph entity ID).
- **Story Node**: a governed narrative artifact that is machine-ingestible and provenance-linked.
- **Focus Mode**: an experience that consumes only provenance-linked context bundles (no unsourced narrative).
- **Deterministic pipeline**: idempotent, config-driven transforms with logged inputs/outputs and stable IDs.
- **Canonical home**: the single authoritative location for a subsystem/artifact class; duplicates require explicit deprecation markers and links to the canonical home.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline ordering + invariants) | `docs/MASTER_GUIDE_v12.md` | Core | Canonical ordering + “do not break” invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Default governed doc template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Evidence-first narrative + Focus Mode surfacing |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Contract-first API changes |
| v13 redesign blueprint (draft reference) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | “One canonical home”, contract-first, provenance-first expectations |
| KFM STAC profile | `docs/standards/KFM_STAC_PROFILE.md` | Standards | *placeholder/presence varies; not confirmed in repo* |
| KFM DCAT profile | `docs/standards/KFM_DCAT_PROFILE.md` | Standards | *placeholder/presence varies; not confirmed in repo* |
| KFM PROV profile | `docs/standards/KFM_PROV_PROFILE.md` | Standards | *placeholder/presence varies; not confirmed in repo* |
| CI workflows | `.github/workflows/**` | CI | Workflows execute validators and enforce gates |
| STAC outputs | `data/stac/**` | Catalog | Collections/items for evidence discovery |
| DCAT outputs | `data/catalog/dcat/**` | Catalog | Dataset discovery metadata |
| PROV outputs | `data/prov/**` | Catalog/Pipelines | Canonical provenance exports |
| Schemas | `schemas/**` | Core | JSON Schemas and shapes (if present) |
| Story Nodes | `docs/reports/story_nodes/**` | Story | Must be provenance-linked to publish |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |

### Definition of done

- [x] Front-matter complete and matches the governed template structure.
- [x] Canonical homes and “one home per subsystem” rule stated.
- [x] CI behavior contract stated: validate if present → fail if invalid → skip if not applicable.
- [x] Cross-link expectations between STAC/DCAT/PROV and downstream consumers documented.
- [x] Governance, CARE/sovereignty, and sensitivity constraints stated.
- [ ] CI workflow filenames listed (intentionally generic; workflows live under `.github/workflows/**`).

## 🗂️ Directory Layout

### This document

- `path`: `.github/lineage/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI workflows | `.github/workflows/**` | GitHub Actions jobs + policy gates |
| Lineage documentation | `.github/lineage/**` | Expectations, gate definitions, contributor guidance |
| Data staging | `data/raw/**`, `data/work/**`, `data/processed/**` | Canonical staged data roots (domain folders) |
| Catalog outputs | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | Boundary artifacts required for publishing |
| Schemas | `schemas/**` | Structural constraints and validator inputs |
| Pipelines | `src/pipelines/**` | Deterministic transforms producing data + catalogs |
| Graph | `src/graph/**` | Ontology + ingest logic (graph references catalogs) |
| Graph import fixtures | `data/graph/**` | CSV/Cypher fixtures *(if present)* |
| API boundary | `src/server/**` | Contracts + redaction + query services |
| UI | `web/**` | Layer registry + Focus Mode UX (no direct graph calls) |
| Story Nodes | `docs/reports/story_nodes/**` | Draft and published story artifacts |
| Tools | `tools/**` | Validators, utilities, QA scripts *(if present)* |
| Tests | `tests/**` | Unit + integration tests *(if present)* |
| MCP runs | `mcp/runs/**` | Run logs and artifacts *(if present)* |

### Expected file tree for this sub-area

~~~text
📁 .github/
├── 📁 workflows/
│   └── 📄 <ci-workflows>.yml                 # CI entrypoints (not defined here)
└── 📁 lineage/
    ├── 📄 README.md                          # (this file)
    └── 📁 scripts/                           # optional; not confirmed in repo
        └── 📄 validate_lineage.<ext>         # optional; not confirmed in repo
~~~

## 🧭 Context

### Background

KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV catalogs → Graph → API → UI → Story Nodes → Focus Mode**

Lineage and provenance are treated as first-class so that:

- Story Nodes and Focus Mode can only surface provenance-linked content.
- Missing links (evidence IDs, entity references, provenance activities) are caught early via CI.
- Outputs remain deterministic and diffable, supporting audits and reproducible builds.

This `.github/lineage/` area exists so CI rules for provenance stay discoverable and consistent as domains expand.

### Assumptions

- Canonical roots exist (or are being created) for `schemas/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/`, and `src/pipelines/`.
- Validators use schemas in `schemas/**` where available.
- PROV serialization/tooling is selected by maintainers; this guide defines required behavior and cross-links, not a specific library.

### Constraints and invariants

- Pipeline ordering is absolute: **ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**.
- API boundary is mandatory: the UI never queries Neo4j directly; it consumes contracted API responses.
- Provenance-first publishing: boundary artifacts are required before graph ingest, UI exposure, or Story Node publication.
- Deterministic ETL: runs must be idempotent and logged; identical inputs produce identical outputs.
- CI behavior is deterministic:
  - optional root absent → checks may skip,
  - optional root present but invalid → checks fail closed.
- One canonical home per subsystem: avoid duplicates without explicit deprecation markers and a link to the canonical home.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Canonical PROV serialization (PROV-JSON vs JSON-LD vs Turtle)? | TBD | TBD |
| Where should cross-link rules live (schemas vs scripts vs tests)? | TBD | TBD |
| Minimal lineage gate required for a “new domain pack”? | TBD | TBD |
| How should dataset-level versioning links be encoded across STAC/DCAT/PROV? | TBD | TBD |

### Future extensions

- Add a repository-standard validator (script or CLI) that:
  - validates PROV bundles against `schemas/prov/**`,
  - checks cross-links into STAC and DCAT,
  - reports orphan references and missing evidence IDs,
  - emits a machine-readable report suitable for CI artifacts or `mcp/runs/**`.
- Introduce a telemetry schema under `schemas/telemetry/**` to track lineage health trends across PRs/runs.

## 🗺️ Diagrams

### System and dataflow diagram

~~~mermaid
flowchart LR
  A[Raw Sources] --> B[ETL + Normalization<br/>src/pipelines]
  B --> C[STAC Items + Collections<br/>data/stac]
  C --> D[DCAT Dataset Views<br/>data/catalog/dcat]
  C --> E[PROV Lineage Bundles<br/>data/prov]

  C --> G[Neo4j Graph<br/>src/graph]
  G --> H[API Layer<br/>src/server]
  H --> I[Map UI<br/>web]
  I --> J[Story Nodes<br/>docs/reports/story_nodes]
  J --> K[Focus Mode<br/>provenance-linked only]

  PR[Pull Request] --> CI[GitHub Actions CI]
  CI --> L[Lineage gates]
  L -->|pass| M[Merge allowed]
  L -->|fail| X[Block merge + report]

  D --> L
  E --> L
  C --> L
~~~

### Optional sequence diagram

~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant CI as GitHub Actions
  participant Repo as Repo checkout
  participant Val as Lineage validators

  Dev->>CI: Push commit / open PR
  CI->>Repo: Checkout + restore fixtures as configured
  CI->>Val: Validate lineage artifacts when present
  Val-->>CI: Pass or Fail + findings
  CI-->>Dev: Status checks + actionable log output
~~~

## 📦 Data & Metadata

### Data lifecycle

KFM’s required staging layout is stage-first:

- `data/raw/<domain>/` — immutable source snapshots
- `data/work/<domain>/` — intermediate transforms
- `data/processed/<domain>/` — final normalized outputs used for catalogs and graph ingest

At the point of publication, every dataset produces boundary artifacts in canonical locations:

- STAC: `data/stac/collections/` and `data/stac/items/`
- DCAT: `data/catalog/dcat/`
- PROV: `data/prov/`

These boundary artifacts are required before data is considered fully published and allowed into downstream stages.

### Domain expansion pattern

When adding a new domain:

- Place raw sources under `data/raw/<new-domain>/`, write intermediates to `data/work/<new-domain>/`, publish normalized outputs to `data/processed/<new-domain>/`.
- Publish STAC/DCAT/PROV artifacts in the canonical locations above.
- Maintain a concise domain README under `docs/data/<new-domain>/README.md` describing:
  - upstream sources and licenses,
  - ETL/runbook steps,
  - governance and sensitivity notes,
  - and the evidence IDs produced.

### Evidence artifact pattern

KFM treats analysis outputs (including AI-derived outputs) as first-class evidence artifacts:

- Store derived datasets in `data/processed/**` (under a domain or project subfolder).
- Catalog them:
  - STAC Item(s) for geospatial assets (and optionally a Collection),
  - a DCAT dataset entry for discovery,
  - a PROV activity bundle describing the run (inputs, method/config, agents, timestamps).
- Integrate with the graph cautiously:
  - graph entities and edges MUST reference the evidence artifact IDs that justify them.
- Expose to the UI only via governed APIs:
  - API layer enforces redaction and classification rules;
  - the UI must not hard-code or bypass evidence restrictions.

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| PROV bundle(s) | JSON/JSON-LD/Turtle (TBD) | `data/prov/**` | `schemas/prov/**` *(if present)* |
| STAC collections/items | JSON | `data/stac/**` | `schemas/stac/**` *(if present)* |
| DCAT dataset records | RDF/JSON-LD/Turtle (TBD) | `data/catalog/dcat/**` | `schemas/dcat/**` *(if present)* |
| Graph import fixtures | CSV/Cypher | `data/graph/**` *(if present)* | graph integrity tests *(if present)* |
| Story Node references | Markdown + front-matter | `docs/reports/story_nodes/**` | `schemas/story_nodes/**` *(if present)* |
| UI registries | JSON/YAML (repo-defined) | `web/**` | `schemas/ui/**` *(if present)* |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI status | GitHub check | GitHub UI | workflow contract |
| Validation report | JSON/Markdown | CI artifact or `mcp/runs/**` *(TBD)* | `schemas/telemetry/**` *(if present)* |

### Sensitivity and redaction

- Provenance artifacts must not leak restricted locations, culturally sensitive knowledge, or PII.
- Classification must not be downgraded automatically; outputs must not be less restricted than any of their inputs.
- Redaction/generalization must be applied consistently across:
  - processed datasets,
  - STAC/DCAT metadata,
  - PROV lineage records,
  - API responses,
  - UI rendering.

### Quality signals

- Schema validity for all present artifacts (STAC/DCAT/PROV and any applicable Story Node/UI schemas).
- No orphan references:
  - evidence refs resolve (STAC/DCAT/PROV identifiers exist),
  - graph/story refs resolve (entity IDs and citations exist).
- Deterministic, diffable outputs (stable IDs + reproducible generation).

## 🌐 STAC, DCAT & PROV Alignment

### STAC/DCAT/PROV alignment policy

Every dataset or evidence artifact intended for downstream use must have:

- STAC Collection + Item(s)
- DCAT dataset entry (minimum title/description/license/keywords/distributions)
- PROV activity bundle describing lineage, including source and run identifiers

### Cross-layer linkage expectations

To keep catalogs, graph, and narratives in sync:

- STAC Items → data assets:
  - STAC must link to the actual data resources (files under `data/processed/**` or a stable storage reference).
- DCAT → distributions:
  - DCAT distributions should reference STAC records and/or direct downloads.
- PROV end-to-end:
  - PROV must link raw inputs → intermediate work → processed outputs,
  - include a run identifier (and/or commit hash) that can reproduce the output.
- Graph and stories reference catalogs:
  - graph nodes and Story Nodes should reference STAC Item IDs and/or DCAT dataset IDs rather than duplicating payloads.

### Versioning expectations

- Dataset versions should link predecessor/successor where a version model exists.
- Replacements must preserve continuity:
  - lineage points to the prior artifact,
  - catalogs and UI prefer the current artifact.
- Breaking changes to schemas or API contracts require:
  - explicit versioning,
  - compatibility checks and contract tests,
  - clear deprecation markers.

## 🧱 Architecture

### Subsystem contracts

| Subsystem | Contract artifacts | Do not break rule |
|---|---|---|
| ETL | pipeline configs + run logs + validation | deterministic and replayable |
| Catalogs | schemas + validators + profiles | machine-validated |
| Graph | ontology + constraints + migrations | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compatible or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Story and Focus | provenance-linked context bundle | no unsourced narrative |

### Canonical subsystem homes

- Pipelines: `src/pipelines/`
- Catalog build/validation tooling: `tools/` and/or `src/pipelines/` *(keep one canonical home)*
- Graph build: `src/graph/`
- API boundary: `src/server/` *(contracts under `src/server/contracts/**` if present)*
- UI: `web/`

### Next-evolution extension points

- (A) Data: new domain, new STAC extension profiles if required
- (B) AI evidence: artifacts as STAC assets, linked into Focus Mode
- (C) Graph: new entity types with explicit provenance + ontology mapping
- (D) API: new endpoints with contract tests + redaction rules
- (E) UI: new layer registry entries with provenance pointers + CARE gating

### API boundary rule

- The UI does not connect to Neo4j directly.
- The API boundary mediates access and enforces provenance plus redaction/generalization rules.

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as machine-ingestible storytelling

Story Nodes must:

- carry explicit citations to cataloged artifacts,
- connect to graph entities (Place/Person/Event/Document/etc.) via stable identifiers,
- separate fact vs inference vs hypothesis where applicable, especially for AI-assisted text.

### Focus Mode rule

- Focus Mode only consumes provenance-linked content.
- Predictive/suggestive content:
  - must be opt-in,
  - must carry uncertainty/confidence metadata,
  - must not infer or reveal sensitive locations.

## 🧪 Validation & CI/CD

### CI behavior contract

- Validate if present:
  - when a canonical root exists, or when artifacts under it change, run the validator(s).
- Fail if invalid:
  - schema errors, missing links, or orphan references fail deterministically.
- Skip if not applicable:
  - optional roots absent → skip without failing the overall pipeline.

### Minimum CI gates

Workflows implement these under `.github/workflows/**`:

- Markdown protocol validation (front-matter + required sections)
- Link and reference checks (no orphan pointers)
- JSON schema validation (where schemas exist):
  - STAC/DCAT/PROV
  - Story Nodes (if present)
  - UI registries (if present)
  - Telemetry (if present)
- Graph integrity tests (constraints, expected labels/edges)
- API contract tests (OpenAPI/GraphQL schema + resolver tests)
- Security and sovereignty scanning gates (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks

### Repo lint invariants

Enforce where tooling exists (policy-defined):

- no YAML front-matter in code files,
- no `README.me`,
- no duplicate canonical homes without explicit deprecation markers and links to the canonical home.

### Gate-to-artifact mapping

| Gate | Typical trigger | Artifacts | Fails when | Typical fix |
|---|---|---|---|---|
| Markdown protocol gate | PR changes in governed docs | Markdown files with front-matter | malformed front-matter; missing required sections | align to governed template |
| Schema validation gate | PR changes under catalogs/schemas | STAC/DCAT/PROV (+ others) | schema mismatch; missing required fields | update artifacts or schema with review |
| Cross-link resolver gate | catalog/prov/story changes | STAC/DCAT/PROV/story refs | orphan IDs; missing referenced artifact | add missing artifact or correct ref |
| Story Node validation gate | story changes | Story Nodes + assets | missing citations; unresolved entity IDs; redaction violations | fix citations/IDs; redact/generalize; adjust status |
| Graph integrity gate | graph changes | ontology + fixtures | constraints violated; missing evidence refs | update mappings; ensure evidence IDs resolve |
| API contract tests | API changes | contracts + tests | contract break; failing resolver tests | version bump or add compatible fields + tests |
| UI registry checks | UI changes | registries | schema invalid; missing provenance pointers | fix registry entry; add evidence refs |
| Security/sovereignty gate | any PR | repo content | secrets/PII; leakage; classification downgrade | remove secrets; redact/generalize; fix propagation |
| Repo lint gate | any PR | repo structure | forbidden patterns (policy-defined) | relocate; add deprecation markers |

### Telemetry signals

If telemetry schemas exist, CI and runs should be able to emit:

- `classification_assigned` (dataset_id, sensitivity, classification)
- `redaction_applied` (method, fields_removed, geometry_generalization)
- `promotion_blocked` (reason, scan_results_ref)
- `catalog_published` (scope, counts, validation_status)
- `focus_mode_redaction_notice_shown` (layer_id, redaction_method)

### Local reproduction placeholder

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.

# 1) validate schemas
# 2) validate provenance bundles
# 3) check cross-links into STAC/DCAT/PROV
# 4) run unit/integration tests

# make validate-schemas
# make validate-lineage
# make test
~~~

## ⚖ FAIR+CARE & Governance

### Governance review triggers

Changes that typically require elevated review:

- new sensitive layers or content intersecting sovereignty obligations
- new AI narrative behaviors or automated summarization that could be interpreted as fact
- new external data sources (license and provenance review)
- new public-facing endpoints or layer interactions that could reveal sensitive locations
- any classification/sensitivity change or publication derived from restricted inputs

### Sovereignty and safety measures

- Classification must not be downgraded without explicit review.
- Outputs must not be less restricted than any of their inputs.
- Prefer metadata-only redacted catalog entries when policy permits.
- Redaction/generalization must be documented and enforced in:
  - datasets (`data/processed/**`),
  - catalogs (STAC/DCAT),
  - API responses (redaction policies),
  - UI rendering (CARE gating).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.1.1 | 2025-12-29 | Align terminology and sections with governed universal template + Master Guide lineage/CI language; clarify required staging and boundary artifacts; normalize canonical subsystem homes list | (you) |
| v1.1.0 | 2025-12-28 | Align with v12/v13 contract language; add repo lint invariants, gate mapping matrix, telemetry signals, and data lifecycle clarification | (you) |
| v1.0.0 | 2025-12-26 | Initial `.github/lineage/` README establishing lineage gates and cross-link expectations | (you) |

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint (draft reference): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance root: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Markdown work protocol: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` *(not confirmed in repo)*
