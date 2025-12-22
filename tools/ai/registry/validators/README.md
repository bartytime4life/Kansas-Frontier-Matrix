---
title: "KFM AI Registry Validators — README"
path: "tools/ai/registry/validators/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

doc_uuid: "urn:kfm:doc:tools:ai:registry:validators:readme:v1.0.0"
semantic_document_id: "kfm-tools-ai-registry-validators-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:ai:registry:validators:readme:v1.0.0"
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

# KFM AI Registry Validators — README

## 📘 Overview

### Purpose

- Define the **validator layer** for the AI registry so registry entries and AI evidence products remain:
  - **contracted** (schema-valid),
  - **provenance-linked** (traceable to STAC/DCAT/PROV identifiers where applicable),
  - **governance-safe** (redaction/sensitivity rules enforceable at the API boundary and in Focus Mode contexts).
- This README is the canonical place to document:
  - what the validators *must* check,
  - where validation reports should land,
  - how failures should be interpreted by CI and/or operators.

### Scope

| In Scope | Out of Scope |
|---|---|
| Validation rules for AI registry objects and related evidence artifacts | Training model code and hyperparameter optimization details |
| Schema validation for structured inputs/outputs that become “registry facts” | UI design/UX implementation |
| Provenance and sensitivity checks that protect Focus Mode requirements | External policy creation (governance docs define policy) |

### Audience

- Primary: maintainers of `tools/ai/registry/` and CI maintainers responsible for gating merges.
- Secondary: data/graph/API/UI engineers consuming AI evidence artifacts; curators using AI outputs.

### Definitions

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Registry entry:** a structured record describing an AI artifact (model, evaluation, drift report, etc.).
  - **Evidence artifact:** a derived product that can be cataloged and cited (often STAC/DCAT/PROV-linked).
  - **Provenance-linked:** resolvable identifiers to STAC Items/Collections, DCAT datasets, and/or PROV activities.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Validators README | `tools/ai/registry/validators/README.md` | AI tooling | This document |
| Registry root | `tools/ai/registry/` | AI tooling | See parent README (not included here) |
| Telemetry schemas | `schemas/telemetry/` | Platform | Used for validator run reporting (expected; not confirmed in repo) |
| Run logs / manifests | `mcp/runs/` | MCP | Likely storage for validator run reports (expected; not confirmed in repo) |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] Validator responsibilities clearly enumerated and mapped to artifacts
- [ ] Inputs/outputs documented with “where from” + “contract/schema” pointers
- [ ] Validation steps listed and repeatable (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] “not confirmed in repo” markers used wherever implementation details are unknown

## 🗂️ Directory Layout

### This document

- `path`: `tools/ai/registry/validators/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Tools | `tools/` | Operational tooling and automation entrypoints |
| AI registry | `tools/ai/registry/` | Registry manifests, tooling, and validators |
| Schemas | `schemas/` | JSON schemas + telemetry schemas (as governed contracts) |
| MCP | `mcp/` | Experiments, model cards, SOPs (may emit registry artifacts) |
| API boundary | `src/server/` | Contracted access; redaction/generalization enforced here |

### Expected file tree for this sub-area

~~~text
📁 tools/
└── 📁 ai/
    └── 📁 registry/
        └── 📁 validators/
            └── 📄 README.md
~~~

## 🧭 Context

### Background

- KFM’s governed architecture requires that anything surfaced in narrative contexts remains **provenance-linked** and avoids unsourced claims.
- AI-produced artifacts (summaries, drift reports, model evaluations) are especially prone to “silent contract drift” (fields change, provenance drops, sensitivity flags omitted).
- Validators are the enforcement mechanism that turns “rules” into **repeatable gates**.

### Assumptions

- Registry entries are represented as structured data (YAML/JSON/JSON-LD) and/or as governed Markdown front-matter + structured blocks (not confirmed in repo).
- AI evidence products can be represented as catalogable artifacts (STAC assets) and linked into graph + Focus Mode contexts (not confirmed in repo).

### Constraints / invariants

- The canonical system ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The frontend consumes all graph/catalog content via APIs (no direct graph dependency).
- Validators must never “invent” missing provenance or fill sensitive fields heuristically.
- If an artifact cannot be provenanced, it is either:
  - blocked from publication, or
  - explicitly labeled as non-authoritative and kept out of default Focus Mode contexts (policy defined elsewhere).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the canonical registry store (files vs DB vs hybrid)? | TBD | TBD |
| What is the minimum schema set for registry objects? | TBD | TBD |
| Which validator outputs are publishable vs internal-only? | TBD | TBD |
| How are sovereignty/redaction rules expressed for AI evidence products? | TBD | TBD |

### Future extensions

- Add validators for drift/evaluation products emitted by scheduled jobs.
- Add telemetry schema + dashboards for “validator health” and governance signals.
- Add “contract compatibility” checks across versions (registry schema semver).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[AI / MCP Runs] --> B[Registry Entries + Evidence Artifacts]
  B --> V[Validators]
  V -->|pass| C[Catalog: STAC/DCAT/PROV refs]
  V -->|fail| R[Validation report + CI gate]
  C --> D[Graph linkage]
  D --> E[API boundary]
  E --> F[UI + Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant CI as CI/Runner
  participant VAL as Validators
  participant CAT as Catalog Artifacts
  CI->>VAL: validate(registry_entry_set)
  VAL-->>CI: pass/fail + report
  VAL->>CAT: (optional) verify referenced STAC/DCAT/PROV IDs exist
  CAT-->>VAL: resolution results
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Registry entry set | JSON/YAML/MD front-matter (not confirmed in repo) | `tools/ai/registry/` and/or `mcp/` | Schema + required fields + versioning |
| Evidence artifact references | IDs/URIs | Catalog outputs and/or run manifests | Existence + resolvability checks |
| Sensitivity annotations | fields/labels | registry entries and/or governance tags | Required if content could reach UI/Story/Focus |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validation report | JSON (recommended) | `mcp/runs/<run_id>/...` (not confirmed in repo) | `schemas/telemetry/` or dedicated validator schema (not confirmed in repo) |
| CI-friendly summary | text/markdown | CI logs | Must not leak sensitive fields |

### Sensitivity & redaction

- Validators must detect and fail artifacts that:
  - include restricted locations without redaction/generalization flags,
  - include PII fields without explicit policy allowance,
  - attempt to infer sensitive locations (explicitly prohibited).
- Validators must treat “missing sensitivity classification” as a failure for any artifact intended for UI/Story/Focus surfacing.

### Quality signals

- 100% schema-valid registry entries for published artifacts.
- No orphan references:
  - referenced STAC/DCAT/PROV IDs resolve (if applicable),
  - referenced graph entity IDs resolve (if applicable).
- Deterministic validation:
  - same input → same failures/warnings.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: AI evidence collections (not confirmed in repo).
- Items involved: evidence items linked to model runs/drift/evaluations (not confirmed in repo).
- Extension(s): any KFM STAC extension profile used for AI artifacts (not confirmed in repo).

### DCAT

- Dataset identifiers: DCAT records corresponding to evidence products (not confirmed in repo).
- License mapping: registry entries must carry license/attribution compatible with catalog policy.
- Contact / publisher mapping: registry should record producing agent/service where appropriate.

### PROV-O

- `prov:wasDerivedFrom`: evidence artifacts must link to input datasets or upstream evidence where applicable.
- `prov:wasGeneratedBy`: evidence artifacts should link to a run/activity identifier (e.g., MCP run).
- Activity / Agent identities: prefer stable IDs for pipeline job + model version + operator agent.

### Versioning

- Use semver for registry schema evolution.
- Where artifacts are versioned:
  - provide predecessor/successor links in metadata,
  - ensure graph mirrors lineage where consumed.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Registry | Store AI artifact metadata | Files/DB (not confirmed in repo) |
| Validators | Enforce schema + provenance + governance constraints | CLI/library entrypoints (not confirmed in repo) |
| Catalog artifacts | Provide resolvable STAC/DCAT/PROV IDs | JSON/JSON-LD in `data/` (canonical) |
| API boundary | Serve contracted access; enforce redaction | REST/GraphQL (per API layer) |
| UI/Story/Focus | Render provenance-linked context only | API calls |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| Telemetry schemas | `schemas/telemetry/` | Semver + CI enforcement |
| API schemas | `src/server/` + docs | Contract tests required |

### Extension points checklist

- [ ] Data: new evidence domain under `data/<domain>/...` (if validators emit/consume datasets)
- [ ] STAC: new collection/item schema validation
- [ ] PROV: activity + agent identifiers recorded for validator runs
- [ ] Graph: new entity/edge types for AI artifacts (explicit provenance)
- [ ] APIs: endpoints to query registry status/drift/evaluations (contract tests)
- [ ] UI: curated surfaces for AI evidence (provenance pointers + CARE gating)
- [ ] Focus Mode: provenance references enforced for any AI surfaced content
- [ ] Telemetry: validator signals emitted + schema version bumps

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Default behavior: registry validator outputs should **not** appear in public Focus Mode contexts unless explicitly modeled as evidence artifacts with provenance and policy clearance.
- Curator behavior (expected): validator results may be visible to curators for review gates (not confirmed in repo).

### Provenance-linked narrative rule

- Every claim that could influence narrative presentation must trace to a dataset/record/asset ID.
- Validators are responsible for ensuring those IDs exist and are preserved in outputs.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (for governed Markdown artifacts)
- [ ] Schema validation (registry schemas; STAC/DCAT/PROV where referenced)
- [ ] Graph integrity checks (if registry entries reference graph IDs)
- [ ] API contract tests (if registry is exposed via API)
- [ ] Security and sovereignty checks (sensitive fields, restricted locations)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate registry entries
# <command> tools/ai/registry/validators ...

# 2) validate referenced schemas (STAC/DCAT/PROV/telemetry)
# <command> ...

# 3) run unit/integration tests
# <command> ...

# 4) run doc lint
# <command> ...
~~~

### Telemetry signals

- Count of registry entries validated / failed
- Failure categories (schema/provenance/sensitivity/versioning)
- Drift in schema versions across runs (compatibility warnings)
- Governance flags triggered (redaction required, restricted geometry, etc.)

## ⚖ FAIR+CARE & Governance

### Governance review triggers

- New AI narrative behaviors
- New evidence products intended to surface in UI/Focus Mode
- New external data sources used by AI tooling
- New public-facing endpoints exposing registry content

### Sovereignty safety

- Do not publish restricted locations or culturally sensitive knowledge without explicit policy clearance.
- Document redaction/generalization behavior for any geometry-bearing AI outputs.
- Ensure validator outputs avoid leaking sensitive inputs in logs and CI artifacts.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial validators README scaffolding | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
