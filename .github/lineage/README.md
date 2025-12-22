---
title: "KFM — Lineage & Provenance (CI)"
path: ".github/lineage/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

This folder documents how KFM enforces provenance/lineage expectations in CI, and how contributors should wire new pipeline outputs into *traceable* evidence artifacts.

> Important: **This folder is not the canonical home of lineage data.**  
> Canonical lineage artifacts live in `data/prov/**` and are consumed downstream (audits, graph provenance, Focus Mode). This directory exists to keep the *CI and contribution rules* close to GitHub automation.

## 📘 Overview

### Purpose

- Define the CI “lineage gates” that keep KFM evidence-first and reproducible.
- Describe how provenance artifacts (PROV bundles) connect to STAC/DCAT outputs and downstream consumers.
- Provide contributor guidance for adding new data/evidence products without creating orphaned or uncitable content.

### Scope

| In Scope | Out of Scope |
|---|---|
| CI validation rules for lineage artifacts and cross-links | Implementing full ETL logic for every domain |
| Expected locations of PROV/STAC/DCAT artifacts | Cloud deployment / ops infrastructure |
| Minimal contribution checklist for provenance completeness | Writing/authoring Story Nodes (see Story Node template) |

### Audience

- Primary: pipeline + catalog maintainers; CI/automation maintainers
- Secondary: graph/API maintainers; curators reviewing evidence readiness

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **Lineage**: the traceable chain from raw inputs → transforms → outputs (datasets/evidence products).
  - **PROV bundle**: a provenance record (W3C PROV-O aligned) describing activities/agents/derivations for outputs.
  - **Evidence artifact**: a cataloged + provenance-linked output consumed downstream (e.g., STAC/DCAT/PROV).
  - **Lineage gate**: a CI check that validates provenance completeness + referential integrity.
  - **No orphan data**: any output lacking source/provenance is treated as invalid for Focus Mode and/or blocks promotion.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | core maintainers | Canonical pipeline + repo invariants |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | architecture | Evidence-first + CI gate expectations |
| PROV bundles | `data/prov/**` | pipeline + catalog | Canonical lineage artifacts; consumed downstream |
| STAC catalogs | `data/stac/**` | catalog | STAC items/collections referenced by graph/story |
| DCAT records | `data/catalog/dcat/**` | catalog | Dataset identifiers for external export + API |
| PROV schemas | `schemas/prov/**` | schema maintainers | Constraints/profiles *(may be placeholder)* |
| PROV profile doc | `docs/standards/KFM_PROV_PROFILE.md` | standards | Placeholder/empty *(not confirmed)* |
| Repo structure standard | `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md` | standards | Not confirmed in repo |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Clearly states canonical lineage artifact locations (`data/prov/**`)
- [ ] CI behavior documented (validate if present; fail if invalid; skip if not applicable)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/lineage/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub automation | `.github/workflows/` | CI workflows (schema lint, tests, lineage gates) |
| Lineage CI docs | `.github/lineage/` | This README + optional lineage helper scripts |
| Data domains | `data/<domain>/**` | `raw/`, `work/`, `processed/` per domain |
| STAC outputs | `data/stac/**` | STAC items/collections |
| DCAT outputs | `data/catalog/dcat/**` | DCAT dataset records |
| PROV outputs | `data/prov/**` | Provenance bundles (lineage) |
| Schemas | `schemas/**` | JSON Schemas + optional shapes |
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
- Any missing links (e.g., evidence IDs, entity references, provenance activities) are caught early via CI.
- Outputs remain **deterministic and diffable**, supporting audits and reproducible builds.

This `.github/lineage/` area exists so CI rules for provenance stay discoverable and consistent as domains expand.

### Assumptions

- Canonical roots exist (or are being created) for `schemas/`, `data/catalog/dcat/`, and `data/prov/`.
- The project validates artifacts against schemas in `schemas/` where available.
- PROV bundle serialization and validation toolchain are selected by maintainers *(tooling not specified here)*.

### Constraints / invariants

- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- **API boundary is mandatory**: the UI never queries Neo4j directly; it consumes contracted API responses.
- CI must be deterministic: if an optional root is absent, jobs may skip; if present but invalid, jobs fail.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical PROV bundle format (e.g., JSON-LD vs TTL vs PROV-JSON)? | TBD | TBD |
| Where should cross-link rules live (schemas vs scripts vs graph tests)? | TBD | TBD |
| What is the minimal “lineage gate” for new domains (MVP)? | TBD | TBD |

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
  A[ETL runs] --> B[STAC/DCAT/PROV outputs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

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
  CI->>Repo: Checkout + restore fixtures (as configured)
  CI->>Val: Validate lineage artifacts (STAC/DCAT/PROV) if present
  Val-->>CI: Pass/Fail + findings (missing links, schema errors)
  CI-->>Dev: Status checks + actionable log output
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| PROV bundle(s) | JSON/JSON-LD/Turtle (TBD) | `data/prov/**` | `schemas/prov/**` (if present) |
| STAC collections/items | JSON | `data/stac/**` | `schemas/stac/**` (if present) |
| DCAT dataset records | RDF/JSON-LD/Turtle (TBD) | `data/catalog/dcat/**` | `schemas/dcat/**` (if present) |
| Story Node refs (optional) | Markdown + front-matter | `docs/reports/story_nodes/**` | `schemas/storynodes/**` (if present) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI status | GitHub check | GitHub UI | workflow contract |
| Validation report (optional) | JSON/Markdown | CI artifact (TBD) | `schemas/telemetry/**` (optional) |

### Sensitivity & redaction

- Provenance artifacts must not leak restricted locations or culturally sensitive knowledge.
- If a dataset is restricted, ensure provenance logs follow governance rules (e.g., redaction/generalization rules are applied consistently).

### Quality signals

- Schema validity for all present artifacts (STAC/DCAT/PROV).
- No orphan references:
  - evidence refs resolve (STAC/DCAT/PROV identifiers exist)
  - Story Node refs resolve (entity IDs exist; citations exist)
- Deterministic, diffable outputs (stable IDs + reproducible generation)

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: *(domain-specific; see `data/stac/collections/`)*
- Items involved: *(domain-specific; see `data/stac/items/`)*
- Extension(s): *(TBD / domain-specific)*

**Lineage checks should confirm:**
- STAC IDs referenced by PROV (and by graph/story) exist and are unique.
- Any declared STAC assets referenced by provenance exist at the expected paths (or are resolvable via catalogs).

### DCAT

- Dataset identifiers: *(domain-specific; see `data/catalog/dcat/`)*
- License mapping: *(TBD)*
- Contact / publisher mapping: *(TBD)*

**Lineage checks should confirm:**
- DCAT dataset IDs referenced by PROV (and by graph/story) exist and are stable.

### PROV-O

- `prov:wasDerivedFrom`: required to link outputs → inputs (source snapshots, upstream artifacts)
- `prov:wasGeneratedBy`: required to link outputs → the generating activity
- Activity / Agent identities: stable identifiers for:
  - pipeline activities (runs)
  - agents (pipelines, maintainers, systems) as appropriate

**Lineage checks should confirm:**
- Every public-facing evidence artifact has provenance metadata.
- Activities and derivations form a consistent chain (no dangling references).

### Versioning

- Use STAC versioning links and graph predecessor/successor relationships as applicable.
- If a dataset is replaced, lineage must point to both:
  - the prior artifact (for continuity)
  - the new artifact (for current consumption)

## 🧱 Architecture

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
| JSON schemas | `schemas/**` | Semver + changelog |
| CI validation behavior | `.github/workflows/**` | deterministic behavior required |
| Provenance reference fields | API contracts (TBD) | Contract tests required |

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

- Story Nodes must carry provenance annotations and connect to graph entities.
- Story Nodes should link to evidence IDs (STAC/DCAT/PROV) whenever possible.

### Focus Mode rule

- Focus Mode only consumes provenance-linked content.
- Any predictive content must be opt-in and carry uncertainty / confidence metadata.

## 🧪 Validation & CI/CD

### CI behavior contract (lineage gates)

- **Validate if present**: if `data/prov/**` exists (or changes), validate it.
- **Fail if invalid**: schema errors, missing links, or orphan refs fail the job deterministically.
- **Skip if not applicable**: optional roots absent → skip without failing the overall pipeline.

### Minimum CI gates (baseline)

- Markdown protocol validation
- JSON schema validation (STAC/DCAT/telemetry)
- Graph integrity tests (no broken links)
- API contract tests
- UI registry schema checks
- Security + sovereignty scanning gates (where applicable)

### Local reproduction (placeholder)

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.
# Example intent:
# 1) validate schemas
# 2) validate provenance bundles
# 3) check cross-links into STAC/DCAT

# make validate-schemas
# make validate-lineage
~~~

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes that touch provenance rules, redaction behavior, or public-facing evidence exports require human review.

### CARE / sovereignty considerations

- Identify impacted communities and protection rules for sensitive/restricted locations.
- Ensure provenance and audit logs don’t re-expose restricted geometry or identifiers.

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions match intended use.
- No “generate policy” behavior should be derived from this README.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial `.github/lineage/` README scaffold | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
