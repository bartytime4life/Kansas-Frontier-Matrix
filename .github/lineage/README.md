---
title: "KFM — Lineage & Provenance (CI)"
path: ".github/lineage/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
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

doc_uuid: "urn:kfm:doc:github:lineage:readme:v1.0.0"
semantic_document_id: "kfm-github-lineage-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:lineage:readme:v1.0.0"
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

This directory documents how KFM enforces **provenance and lineage expectations** in CI so that:
- evidence artifacts are traceable end-to-end (inputs → transforms → outputs),
- downstream systems can rely on stable identifiers,
- Focus Mode only surfaces **provenance-linked** content.

This directory does **not** store provenance payloads. Canonical provenance artifacts are published under `data/prov/**`.

## 📘 Overview

### Purpose
- Define the minimum lineage/provenance expectations for artifacts that move through the KFM pipeline.
- Document CI “lineage gates” and where they plug in.
- Provide contributor guidance to avoid “orphan” content (uncited narrative, unlinked datasets, dangling identifiers).

### Scope
| In scope | Out of scope |
|---|---|
| CI expectations for validating PROV bundles and their cross-links | Selecting a specific PROV serialization or validator tool |
| Cross-link policy between STAC, DCAT, PROV, Graph, and Story Nodes | Defining domain-specific ETL logic (lives under `src/pipelines/` + `data/<domain>/`) |
| Determinism principles for lineage gates | Implementing CI workflows themselves (lives under `.github/workflows/`) |

### Audience
- Contributors adding or updating datasets, “evidence products,” Story Nodes, or catalogs.
- Maintainers who implement and evolve CI validation workflows.
- Reviewers auditing provenance coverage and governance compliance.

### Definitions
- **Evidence artifact**: a dataset or derived product meant for downstream use, represented via STAC/DCAT and backed by PROV lineage.
- **PROV bundle**: a provenance record (format TBD) containing activities, entities, agents, and derivations.
- **Lineage gate**: a CI check that validates provenance structure and cross-links (fail closed when artifacts exist but are invalid).
- **Orphan reference**: an identifier or citation that does not resolve to an existing artifact/entity (e.g., missing STAC item, missing PROV activity, missing graph entity).

### Key artifacts
| Artifact | Canonical location | Notes |
|---|---|---|
| Master Guide (pipeline ordering) | `docs/MASTER_GUIDE_v12.md` | Canonical non-negotiable pipeline ordering |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Defines required roots and CI behavior expectations |
| CI entrypoints | `.github/workflows/**` | Workflows call validators and enforce gates |
| PROV bundles | `data/prov/**` | Canonical provenance exports |
| STAC outputs | `data/stac/**` | Collections/items for evidence discovery |
| DCAT outputs | `data/catalog/dcat/**` | Dataset discovery metadata |
| Schemas | `schemas/**` | JSON Schemas and optional shapes (if present) |
| Story Nodes | `docs/reports/story_nodes/**` | Must be provenance-linked for publication |

### Definition of done for this document
- [x] Uses the governed Markdown protocol and approved headings.
- [x] Describes where lineage artifacts live and how they are validated.
- [x] States CI behavior contract for “present vs absent” optional roots.
- [x] Defines cross-link expectations between STAC/DCAT/PROV and downstream consumers.

## 🗂️ Directory Layout

### This document
- `path`: `.github/lineage/README.md` (must match front-matter)

### Related repository paths
| Area | Path | Responsibility |
|---|---|---|
| CI workflows | `.github/workflows/**` | Execute validators and publish status checks |
| Lineage documentation | `.github/lineage/**` | Explain provenance gates and expectations |
| STAC outputs | `data/stac/**` | Evidence discovery artifacts |
| DCAT outputs | `data/catalog/dcat/**` | Dataset discovery artifacts |
| PROV outputs | `data/prov/**` | Provenance bundles and lineage exports |
| Schemas | `schemas/**` | Structural constraints and validator inputs |
| Pipelines | `src/pipelines/**` | Deterministic transforms producing outputs |
| Graph | `src/graph/**` + `data/graph/**` | Ontology + ingest fixtures |
| API boundary | `src/server/**` | Contracts + redaction + query services |
| UI | `web/**` | Layer registry + Focus Mode UX |

### Expected file tree for this sub-area
~~~text
📁 .github/
├── 📁 workflows/
│   └── 📄 <ci-workflows>.yml                 # CI entrypoints (not documented here)
└── 📁 lineage/
    ├── 📄 README.md                          # (this file)
    └── 📁 scripts/                           # optional; not confirmed in repo
        └── 📄 validate_lineage.<ext>         # optional; not confirmed in repo
~~~

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
- Canonical roots exist (or are being created) for `schemas/`, `data/catalog/dcat/`, and `data/prov/`.
- The project validates artifacts against schemas in `schemas/` where available.
- PROV bundle serialization and validation toolchain are selected by maintainers.

### Constraints / invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- **API boundary is mandatory**: the UI never queries Neo4j directly; it consumes contracted API responses.
- CI must be deterministic: optional root absent → jobs may skip; root present but invalid → jobs fail.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical PROV bundle format (JSON-LD vs Turtle vs PROV-JSON)? | TBD | TBD |
| Where should cross-link rules live (schemas vs scripts vs graph tests)? | TBD | TBD |
| What is the minimal lineage gate for new domains | TBD | TBD |

### Future extensions
- Add a repository-standard validator script under `.github/lineage/scripts/` (optional) that:
  - validates PROV bundles against `schemas/prov/**`
  - checks cross-links into STAC/DCAT
  - reports orphan references and missing evidence IDs
- Emit a machine-readable CI report (telemetry schema) for lineage health trends.

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

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| PROV bundle(s) | JSON/JSON-LD/Turtle (TBD) | `data/prov/**` | `schemas/prov/**` (if present) |
| STAC collections/items | JSON | `data/stac/**` | `schemas/stac/**` (if present) |
| DCAT dataset records | RDF/JSON-LD/Turtle (TBD) | `data/catalog/dcat/**` | `schemas/dcat/**` (if present) |
| Story Node references | Markdown + front-matter | `docs/reports/story_nodes/**` | `schemas/storynodes/**` (if present) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI status | GitHub check | GitHub UI | workflow contract |
| Validation report | JSON/Markdown | CI artifact (TBD) | `schemas/telemetry/**` (optional) |

### Sensitivity & redaction
- Provenance artifacts must not leak restricted locations or culturally sensitive knowledge.
- If a dataset is restricted, ensure provenance logs follow governance rules and apply redaction/generalization consistently.

### Quality signals
- Schema validity for all present artifacts (STAC/DCAT/PROV).
- No orphan references:
  - evidence refs resolve (STAC/DCAT/PROV identifiers exist)
  - Story Node refs resolve (entity IDs exist; citations exist)
- Deterministic, diffable outputs (stable IDs + reproducible generation)

## 🌐 STAC, DCAT & PROV Alignment

### Policy for every dataset / evidence product
For each dataset or evidence product:
- STAC Collection + Item(s)
- DCAT mapping record with minimum title/description/license/keywords
- PROV activity describing lineage with source and run identifiers
- Version lineage links reflected in catalogs and, where applicable, the graph

### Identifier linkage expectation
Graph nodes and APIs should reference:
- STAC Item IDs
- DCAT dataset ID
- PROV activity ID

This enables Focus Mode to resolve “what is this data” into a traceable lineage bundle.

### STAC
- Collections involved: domain-specific; see `data/stac/collections/`
- Items involved: domain-specific; see `data/stac/items/`
- Extension(s): domain-specific

Lineage checks should confirm:
- STAC IDs referenced by PROV and by graph/story exist and are unique.
- Any declared STAC assets referenced by provenance exist at expected paths or are resolvable via catalogs.

### DCAT
- Dataset identifiers: domain-specific; see `data/catalog/dcat/`
- License mapping: TBD
- Contact / publisher mapping: TBD

Lineage checks should confirm:
- DCAT dataset IDs referenced by PROV and by graph/story exist and are stable.

### PROV-O
- `prov:wasDerivedFrom` links outputs to inputs (source snapshots, upstream artifacts).
- `prov:wasGeneratedBy` links outputs to the generating activity.
- Activity and agent identities should be stable identifiers for:
  - pipeline activities and runs
  - agents such as pipelines, maintainers, systems as appropriate

Lineage checks should confirm:
- Every public-facing evidence artifact has provenance metadata.
- Activities and derivations form a consistent chain with no dangling references.

### Versioning
- Use STAC versioning links and graph predecessor/successor relationships as applicable.
- If a dataset is replaced, lineage must point to both:
  - the prior artifact for continuity
  - the new artifact for current consumption

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as evidence-first narrative
- Story Nodes should cite graph entity IDs and STAC/DCAT/PROV evidence IDs.
- Story Nodes may reference local assets with attribution, but the source of truth remains catalog + provenance artifacts.

### Focus Mode rule
- Focus Mode must only consume provenance-linked content.
- Any predictive or AI content must be clearly marked, opt-in, and include uncertainty metadata.

## 🧪 Validation & CI/CD

### CI behavior contract
- Validate if present: if a canonical root exists or changes, validate its artifacts.
- Fail if invalid: schema errors, missing links, or orphan references fail deterministically.
- Skip if not applicable: optional roots absent → skip without failing the overall pipeline.

### Minimum checks
- [ ] Markdown protocol checks for governed docs
- [ ] Schema validation for STAC, DCAT, PROV, Story Nodes, UI registries, telemetry
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI registry checks
- [ ] Link integrity checks for docs when tooling exists
- [ ] Security and sovereignty checks as applicable

### Local reproduction placeholder
~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.

# 1) validate schemas
# 2) validate provenance bundles
# 3) check cross-links into STAC/DCAT
# 4) run unit/integration tests

# make validate-schemas
# make validate-lineage
# make test
~~~

## 🧱 Architecture

### Subsystem contracts
| Subsystem | Contract artifacts | Do not break rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compatible or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

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

## ⚖ FAIR+CARE & Governance

### Review gates
Changes that typically require elevated review:
- Adding new sensitive layers (restricted locations, cultural knowledge, PII)
- Introducing or changing AI-generated narrative behavior visible to users
- Adding new external data sources
- Adding new public-facing endpoints
- Changing provenance rules, redaction behavior, or public-facing evidence exports

### CARE / sovereignty considerations
- Classification must not be automatically downgraded without explicit review.
- Outputs must not be less restricted than any of their inputs.
- If sensitive datasets appear in discovery catalogs, prefer metadata-only redacted entries when policy permits.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial `.github/lineage/` README establishing lineage gates and cross-link expectations | (you) |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance root: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
