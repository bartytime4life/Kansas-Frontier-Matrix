---
title: "KFM Tooling — AI Provenance"
path: "tools/ai/provenance/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "Tooling"
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

doc_uuid: "urn:kfm:doc:tools:ai-provenance:v1.0.0"
semantic_document_id: "kfm-tools-ai-provenance-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:ai-provenance:v1.0.0"
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

# KFM Tooling — AI Provenance

## 📘 Overview

### Purpose

This folder documents how KFM records **provenance (PROV-O)** for **AI-assisted transformations** so every derived artifact (and any downstream narrative use) can be traced back to evidence via stable identifiers.

This README governs the *expected behavior* of AI provenance emission and how it fits into KFM’s canonical pipeline: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Provenance capture for AI transforms (extraction, classification, linking, summarization) used anywhere in the pipeline | Defining new governance policy (must live in governance docs) |
| Run-level PROV bundles and links to inputs/outputs | Model training workflows |
| Linking AI artifacts to STAC assets / graph nodes / API responses | UI design details beyond provenance references |
| Redaction guidance for sensitive prompts/outputs | “Unsourced narrative” generation |

### Audience

- Primary: pipeline authors (ETL/catalog), AI tooling maintainers, provenance/catalog maintainers.
- Secondary: graph/API developers who need provenance references in contracted payloads; reviewers validating Focus Mode sourcing.

### Definitions

- Link: `docs/glossary.md` (if missing, create under `docs/`)
- Terms used in this doc:
  - **PROV-O**: W3C Provenance Ontology; used to express `Entity`, `Activity`, `Agent` and relationships.
  - **Evidence product**: any artifact (raw or derived) that can be referenced and audited (e.g., extracted entities, embeddings, model outputs).
  - **AI transform**: a deterministic/recorded transformation step using an LLM/ML component, producing an evidence product.
  - **Run**: one execution of a pipeline or tool step that generates artifacts and provenance.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical ordering + invariants |
| Redesign blueprint (canonical paths, provenance-first) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Core maintainers | Establishes `data/prov/` as canonical PROV home |
| PROV outputs | `data/prov/` | Catalog maintainers | PROV bundles per run / per dataset |
| STAC outputs | `data/stac/` | Catalog maintainers | Items/collections that reference assets and provenance |
| DCAT outputs | `data/catalog/dcat/` | Catalog maintainers | Dataset catalog as JSON-LD |
| Pipelines | `src/pipelines/` | Data engineering | Where AI transforms may be invoked |
| Graph build | `src/graph/` | Graph maintainers | Graph nodes should link to provenance refs |
| API layer | `src/server/` | API maintainers | UI must consume provenance via APIs |
| MCP runs & model artifacts | `mcp/` | AI/tooling | Experiments, model cards, SOPs (if present) |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] This README states where PROV bundles live and how they link to artifacts
- [ ] Focus Mode provenance rule is explicitly supported (no unsourced narrative)
- [ ] Validation steps listed and repeatable (even if placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `tools/ai/provenance/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed + domain readmes |
| PROV bundles | `data/prov/` | Run/dataset provenance bundles |
| Catalogs | `data/stac/` + `data/catalog/dcat/` | STAC items/collections + DCAT dataset catalog |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog build |
| Graph | `src/graph/` | Ontology bindings + import/export |
| APIs | `src/server/` | Contracted access layer for UI |
| Frontend | `web/` | UI (must not query Neo4j directly) |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area

~~~text
📁 tools/
├── 📁 ai/
│   ├── 📁 provenance/
│   │   ├── 📄 README.md
│   │   ├── 📁 schemas/                 # (not confirmed in repo) JSON Schema for tool outputs
│   │   ├── 📁 examples/                # (not confirmed in repo) sample PROV bundles
│   │   └── 📄 cli.py                   # (not confirmed in repo) CLI entrypoint / wrapper
~~~

## 🧭 Context

### Background

KFM is an evidence-first system: **catalogs and provenance are first-class**, and Focus Mode must only consume provenance-linked content. AI transforms can produce useful evidence products, but they must be recorded as auditable derivations rather than “free-floating” text.

### Assumptions

- KFM emits PROV bundles in **JSON-LD** form (or an equivalent machine-readable form aligned to PROV-O).
- Derived AI artifacts can be treated as first-class evidence products and linked from STAC assets and/or graph entities.
- The canonical pipeline ordering remains unchanged.

### Constraints and invariants

- Canonical ordering preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Focus Mode consumes provenance-linked content only; predictive/AI content (if exposed) must be opt-in and carry uncertainty / confidence metadata.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where should AI-specific PROV bundles live under `data/prov/` (flat vs `data/prov/ai/`)? | TBD | TBD |
| What is the canonical run identifier format (UUID, timestamped slug, content hash)? | TBD | TBD |
| Should prompts be stored (redacted) or only hashed + referenced? | TBD | TBD |
| What minimal confidence/uncertainty fields are required for AI outputs? | TBD | TBD |

### Future extensions

- Integrate provenance generation into `src/pipelines/` so every AI step automatically emits a PROV activity.
- Add JSON Schemas for AI provenance bundles under `schemas/` and validate in CI.
- Add telemetry signals (provenance coverage, missing links, redaction counts).

## 🗺️ Diagrams

### System dataflow with provenance emphasis

~~~mermaid
flowchart LR
  A[ETL + AI transforms] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  A --> P[AI Provenance Tooling]
  P --> B
~~~

### AI transform provenance (conceptual)

~~~mermaid
flowchart TB
  IN[Input evidence entity/entities] --> ACT[AI Transform Activity]
  AG[Agent: tool + model] --> ACT
  ACT --> OUT[Output evidence product]
  OUT --> LINK[Referenced by STAC asset / Graph node / API payload]
~~~

## 📦 Data and Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Input evidence references | IDs/URIs | STAC item IDs, dataset record IDs, graph IDs | Must resolve to an existing artifact |
| Transform configuration | YAML/JSON | pipeline config / tool flags | Schema-validated (recommended) |
| Model/tool identity | strings | model cards / env | Must include version + hash (recommended) |
| Redaction rules | policy refs | governance/sovereignty docs | Must be applied before writing outputs |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| PROV bundle | JSON-LD | `data/prov/…` | KFM-PROV profile (see standards) |
| Run manifest | JSON/YAML | `mcp/runs/…` or `data/prov/…` | (not confirmed in repo) |
| Optional derived artifact | varies | `data/processed/…` | STAC asset references recommended |

### Sensitivity and redaction

- Do not write sensitive raw prompts/inputs to provenance logs if they may reveal restricted locations or personal data.
- Prefer: store **hashes** (prompt hash, input bundle hash) + stable IDs, and keep any raw content in governed datasets with proper redaction/generalization.

### Quality signals

- Record (at minimum): transform status, input/output counts, validation outcome.
- If the transform produces predictions or classifications: record uncertainty/confidence fields (exact schema not confirmed in repo).

## 🌐 STAC, DCAT and PROV Alignment

### STAC

- Derived AI artifacts should be linkable as STAC assets (recommended) so they are discoverable and versioned alongside other evidence products.
- STAC items that reference AI-derived assets should also reference the corresponding PROV activity/run identifier.

### DCAT

- DCAT dataset identifiers should remain stable even as derived AI artifacts are regenerated.
- If AI artifacts are published as datasets, they must have explicit publisher/contact/license mapping (per DCAT profile).

### PROV-O

At minimum, each AI transform should express:

- `prov:Activity` — the AI transform execution (with run ID)
- `prov:Agent` — tool + model identity (and optionally operator identity if permitted)
- `prov:Entity` — inputs and outputs
- `prov:wasDerivedFrom` — output entity derived from input entity
- `prov:wasGeneratedBy` — output entity generated by the AI transform activity
- `prov:wasAssociatedWith` — activity associated with agent

### Versioning

- Prefer deterministic regeneration and stable IDs.
- Use predecessor/successor links where appropriate (STAC versioning and/or graph relationships).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| AI Provenance Tooling | Emit PROV bundles for AI transforms | Library/CLI called by pipelines |
| Catalogs | Persist and validate STAC/DCAT/PROV outputs | JSON + validators |
| Graph | Link entities to evidence and provenance refs | Graph import + API access |
| APIs | Serve contracted payloads with provenance refs | REST/GraphQL |
| UI | Display evidence + provenance affordances | API calls only |
| Story Nodes | Curated narrative; must carry provenance annotations | Markdown + graph links |
| Focus Mode | Contextual synthesis over provenance-linked content | Provenance refs required |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| PROV profile | `docs/standards/KFM_PROV_PROFILE.md` | Versioned standard (not confirmed in repo) |

### Extension points checklist

- [ ] PROV: activity + agent identifiers recorded for each AI transform
- [ ] STAC: derived artifacts optionally represented as assets
- [ ] Graph: derived artifacts linked to entities via provenance refs
- [ ] APIs: provenance refs included in responses
- [ ] UI: provenance pointers visible (no hidden data leakage)
- [ ] Focus Mode: provenance references enforced; predictive content opt-in

## 🧠 Story Node and Focus Mode Integration

### How this work surfaces in Focus Mode

- Any AI-derived evidence product used in Story Nodes or Focus Mode must carry:
  - a stable identifier
  - a provenance reference (PROV activity/run)
  - links to underlying source evidence IDs

### Provenance-linked narrative rule

- Every claim must trace to a dataset / record / asset ID.
- AI outputs do not become “facts” by default; they are evidence products with traceable derivation.

## 🧪 Validation and CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV) where applicable
- [ ] Graph integrity checks (if provenance refs are imported)
- [ ] API contract tests (if provenance fields are surfaced)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Validate generated PROV bundles (JSON-LD / schema)
# <command>

# 2) Run pipeline step that emits AI provenance
# <command>

# 3) Run markdown lint / protocol validation
# <command>
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Provenance coverage (% AI outputs with PROV) | pipelines/tools | `docs/telemetry/` + `schemas/telemetry/` (not confirmed in repo) |
| Redaction events count | provenance tool | `docs/telemetry/` + `schemas/telemetry/` (not confirmed in repo) |
| Validation failures | CI / validators | CI logs |

## ⚖ FAIR+CARE and Governance

### Review gates

- Any change that affects:
  - provenance schema or required fields
  - exposure of AI/predictive content in public UI
  - handling of sensitive locations or culturally sensitive sites
  - new external data sources
  should receive human review per governance docs.

### CARE and sovereignty considerations

- Ensure provenance does not leak restricted locations or sensitive personal data.
- Prefer hashing + governed references over raw content storage for prompts/inputs.

### AI usage constraints

- This doc permits summarization/structure extraction/translation/keyword indexing for maintenance workflows.
- This doc prohibits generating policy or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for AI provenance tooling | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`