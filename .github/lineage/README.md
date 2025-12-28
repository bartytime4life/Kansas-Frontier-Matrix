---
title: "KFM — Lineage & Provenance (CI)"
path: ".github/lineage/README.md"
version: "v1.1.0"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:github:lineage:readme:v1.1.0"
semantic_document_id: "kfm-github-lineage-readme-v1.1.0"
event_source_id: "ledger:kfm:doc:github:lineage:readme:v1.1.0"
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
- Story Nodes and Focus Mode only surface **provenance-linked** content.

This directory does **not** store provenance payloads. Canonical provenance artifacts are published under `data/prov/**`.

---

## 📘 Overview

### Purpose

- Define the minimum lineage/provenance expectations for artifacts that move through the KFM pipeline.
- Document CI “lineage gates” and where they plug in.
- Provide contributor guidance to prevent:
  - orphan references,
  - duplicate “canonical homes”,
  - and unsourced narrative that can’t be traced back to evidence.

### Scope

| In scope | Out of scope |
|---|---|
| CI expectations for validating PROV bundles and their cross-links | Selecting a specific PROV serialization or validator tool (maintainer choice) |
| Cross-link policy between STAC, DCAT, PROV, Graph, APIs, UI, and Story Nodes | Domain-specific ETL logic (lives under `src/pipelines/` + domain data roots) |
| Determinism and “skip vs fail” behavior for lineage gates | Implementing CI workflows themselves (lives under `.github/workflows/`) |

### Audience

- Contributors adding or updating datasets, “evidence products,” Story Nodes, or catalogs.
- Maintainers who implement and evolve CI validation workflows.
- Reviewers auditing provenance coverage, governance compliance, and reproducibility.

### Definitions

> See also: `docs/glossary.md` *(if present; not confirmed in repo).*

- **Evidence artifact**: a dataset or derived product meant for downstream use, represented via STAC/DCAT and backed by PROV lineage.
- **PROV bundle**: a provenance record containing activities, entities, agents, and derivations (serialization is implementation-defined).
- **Lineage gate**: a CI check that validates provenance structure and cross-links (**fail closed** when artifacts exist but are invalid).
- **Orphan reference**: an identifier or citation that does not resolve to an existing artifact/entity (e.g., missing STAC item, missing PROV activity, missing graph entity).
- **Canonical home**: the single authoritative location for a subsystem/artifact class (duplicates require explicit deprecation markers and links to the canonical home).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline ordering) | `docs/MASTER_GUIDE_v12.md` | Core | Canonical non-negotiable ordering + invariants |
| v13 redesign blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | “One canonical home”, contract-first, provenance-first expectations |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Default governed doc template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Evidence-first narrative + Focus Mode surfacing |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Contract-first API changes |
| CI entrypoints | `.github/workflows/**` | CI | Workflows run validators and enforce gates |
| PROV bundles | `data/prov/**` | Catalog/Pipelines | Canonical provenance exports |
| STAC outputs | `data/stac/**` | Catalog | Collections/items for evidence discovery |
| DCAT outputs | `data/catalog/dcat/**` | Catalog | Dataset discovery metadata |
| Schemas | `schemas/**` | Core | JSON Schemas and optional shapes (if present) |
| Story Nodes | `docs/reports/story_nodes/**` | Story | Must be provenance-linked for publication |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |

### Definition of done for this document

- [x] Uses the governed Markdown protocol and approved headings.
- [x] States canonical homes and “one home per subsystem” rule.
- [x] Defines CI behavior contract: **validate if present → fail if invalid → skip if not applicable**.
- [x] Defines cross-link expectations between STAC/DCAT/PROV and downstream consumers.
- [x] Captures “repo lint” invariants relevant to provenance and discoverability.
- [ ] Names specific workflow filenames (intentionally left generic; workflows live under `.github/workflows/**`).

---

## 🗂️ Directory Layout

### This document

- `path`: `.github/lineage/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI workflows | `.github/workflows/**` | Validation jobs and policy gates |
| Lineage documentation | `.github/lineage/**` | Expectations, gate definitions, contributor guidance |
| STAC outputs | `data/stac/**` | Evidence discovery artifacts |
| DCAT outputs | `data/catalog/dcat/**` | Dataset discovery artifacts |
| PROV outputs | `data/prov/**` | Provenance bundles and lineage exports |
| Schemas | `schemas/**` | Structural constraints and validator inputs |
| Pipelines | `src/pipelines/**` | Deterministic transforms producing outputs |
| Graph | `src/graph/**` + `data/graph/**` | Ontology + ingest fixtures |
| API boundary | `src/server/**` | Contracts + redaction + query services |
| UI | `web/**` | Layer registry + Focus Mode UX |
| Story Nodes | `docs/reports/story_nodes/**` | Draft and published story artifacts |

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

---

## 🧭 Context

### Background

KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Lineage and provenance are treated as first-class so that:

- Story Nodes and Focus Mode can only surface **provenance-linked content**.
- Missing links (evidence IDs, entity references, provenance activities) are caught early via CI.
- Outputs remain **deterministic and diffable**, supporting audits and reproducible builds.

This `.github/lineage/` area exists so CI rules for provenance stay discoverable and consistent as domains expand.

### Assumptions

- Canonical roots exist (or are being created) for `schemas/`, `data/catalog/dcat/`, `data/prov/`, and `data/graph/` (some may be added during migration).
- Validators use schemas in `schemas/**` where available.
- PROV serialization/tooling is selected by maintainers (the CI contract is about behavior + outcomes, not a specific library).

### Constraints / invariants

- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- **API boundary is mandatory**: the UI never queries Neo4j directly; it consumes contracted API responses.
- **Provenance-first**: downstream surfacing (especially Focus Mode) requires provenance-linked context.
- CI is deterministic:
  - optional root absent → checks may skip,
  - optional root present but invalid → checks fail closed.
- One canonical home per subsystem:
  - avoid duplicate canonical homes without explicit deprecation markers + link to canonical.
- Repo lint invariants (CI should enforce where tooling exists):
  - no YAML front-matter in code files,
  - no `README.me`,
  - no duplicate canonical homes without explicit deprecation markers.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Canonical PROV serialization (PROV-JSON vs JSON-LD vs Turtle)? | TBD | TBD |
| Where should cross-link rules live (schemas vs scripts vs tests)? | TBD | TBD |
| What is the minimal lineage gate required for a “new domain pack”? | TBD | TBD |
| Which data staging layout is canonical during migration (stage-first vs domain-first)? | TBD | TBD |

### Future extensions

- Add a repository-standard validator script under `.github/lineage/scripts/` *(optional; not confirmed in repo)* that:
  - validates PROV bundles against `schemas/prov/**`,
  - checks cross-links into STAC/DCAT,
  - reports orphan references and missing evidence IDs.
- Emit a machine-readable CI report (telemetry schema) for lineage health trends and governance signals.

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL runs<br/>src/pipelines] --> B[STAC/DCAT/PROV outputs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Neo4j Graph<br/>src/graph + data/graph]
  C --> D[API boundary<br/>src/server]
  D --> E[React/Map UI<br/>web]
  E --> F[Story Nodes<br/>docs/reports/story_nodes]
  F --> G[Focus Mode<br/>provenance-linked only]

  PR[Pull Request] --> CI[GitHub Actions CI]
  CI --> L[Lineage gates]
  L -->|pass| M[Merge allowed]
  L -->|fail| X[Block merge + report]

  B --> L
~~~

### Optional: sequence diagram

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

---

## 📦 Data & Metadata

### Data lifecycle

KFM’s governed docs reference two staging layout concepts; CI should treat the **repo’s selected canonical layout** as authoritative and flag mixed patterns unless an explicit migration plan exists.

**Stage-first (v12-style) staging roots:**

- `data/raw/<domain>/` — immutable source snapshots
- `data/work/<domain>/` — intermediate transforms
- `data/processed/<domain>/` — normalized outputs used for catalogs and graph ingest

**Domain-first (v13 draft) staging roots:**

- `data/<domain>/raw/` — immutable source snapshots
- `data/<domain>/work/` — intermediate transforms
- `data/<domain>/processed/` — normalized outputs used for catalogs and graph ingest

**Global metadata outputs (canonical locations):**

- STAC: `data/stac/collections/` and `data/stac/items/`
- DCAT: `data/catalog/dcat/`
- PROV: `data/prov/`
- Graph import: `data/graph/csv/` and `data/graph/cypher/` *(if present)*

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| PROV bundle(s) | JSON/JSON-LD/Turtle (TBD) | `data/prov/**` | `schemas/prov/**` *(if present)* |
| STAC collections/items | JSON | `data/stac/**` | `schemas/stac/**` *(if present)* |
| DCAT dataset records | RDF/JSON-LD/Turtle (TBD) | `data/catalog/dcat/**` | `schemas/dcat/**` *(if present)* |
| Graph import fixtures | CSV/Cypher | `data/graph/**` | graph integrity tests *(if present)* |
| Story Node references | Markdown + front-matter | `docs/reports/story_nodes/**` | `schemas/storynodes/**` *(if present)* |
| UI registries | JSON/YAML (repo-defined) | `web/**` | `schemas/ui/**` *(if present)* |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI status | GitHub check | GitHub UI | workflow contract |
| Validation report | JSON/Markdown | CI artifact (TBD) | `schemas/telemetry/**` *(optional)* |

### Sensitivity & redaction

- Provenance artifacts must not leak restricted locations or culturally sensitive knowledge.
- If a dataset is restricted, provenance logs must follow governance rules and apply redaction/generalization consistently.
- Outputs must not be less restricted than any of their inputs (classification propagation rule).

### Quality signals

- Schema validity for all present artifacts (STAC/DCAT/PROV, plus Story Nodes/UI registries if applicable).
- No orphan references:
  - evidence refs resolve (STAC/DCAT/PROV identifiers exist),
  - graph/story refs resolve (entity IDs exist; citations exist).
- Deterministic, diffable outputs (stable IDs + reproducible generation).

---

## 🌐 STAC, DCAT & PROV Alignment

### Policy for every dataset / evidence product

For each dataset or evidence product intended for downstream use:

- STAC Collection + Item(s)
- DCAT dataset record (minimum title/description/license/keywords)
- PROV activity describing lineage with source and run identifiers
- Version lineage links reflected in catalogs and, where applicable, the graph

### Identifier linkage expectation

Graph nodes and APIs should reference:

- STAC Item IDs
- DCAT dataset ID
- PROV activity ID

This enables Focus Mode to resolve “what is this data” into a traceable lineage bundle.

### STAC (what CI should confirm)

- IDs referenced by PROV / graph / story exist and are unique.
- Declared assets referenced by provenance exist at expected paths or are resolvable via catalogs.
- Collections and items maintain integrity (item ↔ collection relationships).

### DCAT (what CI should confirm)

- Dataset identifiers referenced by PROV and by graph/story exist and remain stable.
- Licensing fields are present for open/public artifacts (when applicable).
- Distributions are consistent with the actual published artifacts (when modeled).

### PROV-O (what CI should confirm)

- Derivation links connect outputs → inputs (source snapshots, upstream artifacts).
- Generated-by links connect outputs → the generating activity.
- Activities and agents use stable identifiers for:
  - pipeline activities and runs,
  - agents such as pipelines, maintainers, systems as appropriate.

### Versioning expectations

- New versions link predecessor/successor (where a version model exists).
- If a dataset is replaced, lineage must point to:
  - the prior artifact for continuity,
  - the new artifact for current consumption.

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as evidence-first narrative

- Story Nodes should cite:
  - graph entity IDs,
  - STAC/DCAT/PROV evidence IDs.
- Story Nodes may reference local assets with attribution, but the source of truth remains catalog + provenance artifacts.
- Story Nodes must separate fact vs inference vs hypothesis where applicable (especially for AI-generated text).

### Focus Mode rule

- Focus Mode must only consume provenance-linked content.
- Any predictive or AI content must be:
  - opt-in,
  - accompanied by uncertainty metadata,
  - and never presented as unmarked fact.
- No workflows or narratives should infer or reveal sensitive locations.

---

## 🧪 Validation & CI/CD

### CI behavior contract

- Validate if present: if a canonical root exists or changes, validate its artifacts.
- Fail if invalid: schema errors, missing links, or orphan references fail deterministically.
- Skip if not applicable: optional roots absent → skip without failing the overall pipeline.

### Minimum CI gates

This list describes the minimum expected gates (workflows implement these under `.github/workflows/**`):

- Markdown protocol validation (front-matter + required sections)
- Link/reference checks (no orphan pointers)
- Schema validation (where schemas exist):
  - STAC / DCAT / PROV
  - Story Nodes
  - UI registries
  - Telemetry
- Graph integrity checks (constraints, expected labels/edges)
- API contract tests (OpenAPI/GraphQL schema + resolver/integration tests)
- Security + sovereignty scanning gates (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Repo lint rules (structural invariants)

Enforce (where tooling exists):

- no YAML front-matter in code files,
- no `README.me`,
- no duplicate canonical homes without explicit deprecation markers.

### Gate-to-artifact mapping (recommended)

| Gate | Typical trigger | Artifacts | Fails when | Typical fix |
|---|---|---|---|---|
| Markdown protocol gate | PR changes in `docs/**` or governed markdown | Markdown files w/ front-matter | missing required sections / malformed front-matter | align to the governed template |
| Schema validation gate | PR changes under `data/stac/`, `data/catalog/dcat/`, `data/prov/`, `schemas/` | JSON/RDF/PROV artifacts | schema mismatch, missing required fields, invalid structure | update artifact to satisfy schema or bump schema with review |
| Cross-link resolver gate | any catalog/prov/story changes | STAC/DCAT/PROV/Story Node refs | orphan IDs; missing referenced artifact | add missing artifact or correct reference |
| Story Node validation gate | PR changes under `docs/reports/story_nodes/` | Story Nodes + assets | missing citations; unresolved entity IDs; redaction rules violated | fix citations/IDs; add redaction/generalization; adjust status |
| Graph integrity gate | PR changes under `src/graph/` or `data/graph/` | graph fixtures + ontology bindings | constraints violated; missing evidence refs | update ingest fixtures + ensure evidence IDs resolve |
| API contract tests | PR changes under `src/server/` | OpenAPI/GraphQL contracts + tests | contract breaks; failing resolver tests | version bump or add compatible fields + tests |
| UI registry checks | PR changes under `web/**` | layer registries | schema invalid; missing provenance pointers | fix registry entry + add provenance/evidence refs |
| Security/sovereignty gate | any PR | repo content | secrets/PII; sensitive location leakage; classification downgrade | remove secrets; redact/generalize; fix classification propagation |
| Repo lint gate | any PR | repo structure | forbidden patterns (e.g., code-file front-matter, duplicate canonical homes) | relocate content; add deprecation markers + links |

### Telemetry signals (recommended)

If telemetry schemas exist, CI and runs should be able to emit (examples):

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

---

## 🧱 Architecture

### Subsystem contracts

| Subsystem | Contract artifacts | Do not break rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compatible or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Story/Focus | provenance-linked context bundle | no hallucinated/unsourced claims |

### API boundary rule

- The UI does not connect to Neo4j directly.
- The API boundary mediates access and enforces provenance plus redaction/generalization rules.

### Components

| Component | Responsibility | Interface |
|---|---|---|
| CI workflow(s) | Run validators on PR/push | GitHub Actions YAML |
| Lineage validator | Validate PROV + cross-links | CLI/script (TBD) |
| Schemas | Define structural constraints | `schemas/**` |
| Catalog outputs | Provide evidence artifacts | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` |
| Graph | Consume evidence refs; enforce ontology | `src/graph/**`, `data/graph/**` |
| API boundary | Serve contracted payloads + provenance refs | `src/server/**` |
| UI | Render provenance-linked content | `web/**` |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/**` | semver + changelog |
| CI validation behavior | `.github/workflows/**` | deterministic behavior required |
| Provenance reference fields | API contracts (TBD) | contract tests required |

---

## ⚖ FAIR+CARE & Governance

### Review gates

Changes that typically require elevated review:

- Adding new sensitive layers (restricted locations, cultural knowledge, PII)
- Introducing or changing AI-generated narrative behavior visible to users
- Adding new external data sources (license + provenance review)
- Adding new public-facing endpoints
- Changing provenance rules, redaction behavior, or public-facing evidence exports
- Any classification/sensitivity change or publication derived from restricted inputs

### CARE / sovereignty considerations

- Classification must not be automatically downgraded without explicit review.
- Outputs must not be less restricted than any of their inputs.
- If sensitive datasets appear in discovery catalogs, prefer metadata-only redacted entries when policy permits.
- Redaction/generalization rules must be enforced consistently across:
  - processed datasets,
  - catalogs,
  - API responses,
  - UI rendering (including Focus Mode).

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.1.0 | 2025-12-28 | Align with v12/v13 contract language; add repo lint invariants, gate mapping matrix, telemetry signals, and data lifecycle clarification | (you) |
| v1.0.0 | 2025-12-26 | Initial `.github/lineage/` README establishing lineage gates and cross-link expectations | (you) |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint (draft): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance root: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Markdown work protocol: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` *(not confirmed in repo)*
