---
title: "KFM Tests — README"
path: "tests/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:tests:readme:v1.0.0"
semantic_document_id: "kfm-tests-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tests:readme:v1.0.0"
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

# KFM Tests — README

## 📘 Overview

### Purpose
- Define the **testing and validation conventions** for KFM.
- Map tests to the **minimum CI gates** required for “v12-ready” contributions.
- Provide a single place to document how to add new tests and keep them deterministic.

### Scope

| In Scope | Out of Scope |
|---|---|
| Test taxonomy (unit/integration/contract/e2e), fixtures, and validation gates | Implementing specific pipelines or features |
| Where new tests belong and how they should behave (determinism, no hidden I/O) | Selecting a specific test framework/tooling (not confirmed in repo) |
| Schema validation expectations for STAC/DCAT/PROV outputs | Replacing governance/security policies |

### Audience
- **Primary:** KFM contributors writing or updating pipelines, schemas, APIs, or UI.
- **Secondary:** Maintainers reviewing PRs and CI failures.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc include: **unit test**, **integration test**, **contract test**, **schema validation**, **idempotence**, **deterministic pipeline**, **redaction**, **provenance**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| Markdown protocol + governed doc structure | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Template used by this README |
| JSON Schemas (STAC/DCAT/PROV/telemetry) | `schemas/` | Data/Platform | Schema validation gates should reference these |
| ETL + catalog pipelines | `src/pipelines/` | Data Eng | Determinism + idempotence checks |
| Graph build + ontology bindings | `src/graph/` | Graph Eng | Graph integrity tests |
| API layer | `src/api/` (or `src/server/` — not confirmed in repo) | API Eng | Contract tests required |
| UI layer registry + map client | `web/` | Frontend | Schema checks + a11y gates |
| Story Nodes + Focus Mode | `docs/` + UI | Narrative | Provenance-linked narrative rule enforcement |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Test taxonomy + directory conventions are explicit
- [ ] Minimum CI gates are mapped to where failures should be debugged
- [ ] Commands are either repo-accurate or explicitly marked “not confirmed in repo”
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `tests/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Tests | `tests/` | Unit/integration/contract/e2e tests + fixtures |
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
> This is the **recommended** structure. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 tests/
├── 📄 README.md
├── 📁 unit/                 # fast, deterministic, no external deps (recommended)
├── 📁 integration/          # multi-module tests (recommended)
├── 📁 contract/             # schema + API contract tests (recommended)
├── 📁 e2e/                  # UI/API end-to-end (recommended; may be split under web/)
├── 📁 fixtures/             # small synthetic fixtures only (recommended)
└── 📁 helpers/              # shared test utilities (recommended)
~~~

## 🧭 Context

### Background
KFM is a governed geospatial + historical knowledge system. The canonical pipeline ordering is:
**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.
Tests exist to keep these subsystem contracts stable and prevent “silent drift” across outputs.

### Assumptions
- The repo’s exact test runner(s) and commands are **not confirmed in repo**.
- KFM is likely multi-language (pipelines + web), so tests may be split by subsystem.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (**no direct graph dependency**).
- Tests must be deterministic:
  - no network calls by default
  - no reliance on local machine state
  - no non-pinned randomness (seed if needed)
- Fixtures must not contain secrets or personally identifying information (PII).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical test runner per subsystem (Python/Node/etc.)? | TBD | TBD |
| Where are schema validators implemented (scripts, CI actions, or test suite)? | TBD | TBD |
| Are there existing “golden” fixtures for STAC/DCAT/PROV outputs? | TBD | TBD |

### Future extensions
- Golden-file tests for catalog outputs (STAC/DCAT/PROV)
- Property-based tests for parsers/normalizers (where appropriate)
- Snapshot tests for UI layer registry validation (if registry is JSON-schema’d)

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  T[Tests + CI Gates] --> A
  T --> B
  T --> C
  T --> D
  T --> E
  T --> F
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Dev as Developer
  participant CI as CI
  participant API as API
  participant Graph as Graph

  Dev->>CI: Push PR
  CI->>CI: Schema + doc lint + tests
  CI->>API: (contract tests) request/response validation
  API->>Graph: Query (with redaction rules)
  Graph-->>API: Result + provenance refs
  API-->>CI: Contracted payload
  CI-->>Dev: Pass/Fail + reports
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Source code | mixed | `src/`, `web/` | lint + unit/integration tests |
| Catalog outputs | JSON | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | JSON Schema validation |
| Ontology + migrations | mixed | `src/graph/` + `docs/graph/` | graph integrity tests |
| Fixtures | files | `tests/fixtures/` | checksum + schema as needed |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Test results | tool-defined | CI artifacts | must be machine-readable (where possible) |
| Schema validation reports | tool-defined | CI artifacts | must point to failing file + schema |
| Coverage reports (optional) | tool-defined | CI artifacts | thresholds (not confirmed in repo) |

### Sensitivity & redaction
- Fixtures must be **synthetic** or appropriately redacted/generalized.
- Do not commit API keys, tokens, credentials, or sensitive location coordinates.

### Quality signals
- Determinism: rerun the same tests twice → identical results.
- Schema correctness: all generated STAC/DCAT/PROV outputs validate against `schemas/`.
- Idempotence: running the same pipeline twice yields no diffs (when applicable).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: `data/stac/collections/...` (validate all collections)
- Items involved: `data/stac/items/...` (validate all items)
- Extension(s): project profile(s) (not confirmed in repo)

### DCAT
- Dataset identifiers: `data/catalog/dcat/...` (validate all datasets)
- License mapping: ensure license fields are present where required
- Contact / publisher mapping: ensure required fields are present per profile

### PROV-O
- `prov:wasDerivedFrom`: ensure lineage links exist for derived outputs
- `prov:wasGeneratedBy`: ensure each generation activity is recorded
- Activity / Agent identities: ensure stable IDs (pattern defined elsewhere)

### Versioning
- Use STAC Versioning links and graph predecessor/successor relationships as applicable.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |
| Tests | Verify contracts | CI gates + local runner |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/api/` (or `src/server/` — not confirmed in repo) + docs | Contract tests required |
| Layer registry | `web/...` (exact path not confirmed in repo) | Schema-validated |

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
- Tests should enforce that **Focus Mode consumes provenance-linked content only**.
- Story Node JSON/YAML (or markdown) should be checked for:
  - resolvable dataset IDs (STAC/DCAT/PROV references)
  - resolvable entity IDs (graph or creation tickets)
  - no prohibited AI actions implied

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

### Minimum CI gates for “v12-ready” contributions
The following CI gates are expected at minimum:
- Markdown protocol validation
- JSON schema validation (STAC/DCAT/telemetry)
- Graph integrity tests
- API contract tests
- UI layer registry schema checks
- Security + sovereignty scanning gates (where applicable)

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
> Commands below are **examples only** (actual commands are **not confirmed in repo**). Replace with repo-specific scripts.

~~~bash
# 1) validate schemas (STAC/DCAT/PROV)
# (not confirmed in repo) e.g.:
#   python -m tools.validate_schemas
#   node tools/validate-schemas.js

# 2) run unit/integration tests
# (not confirmed in repo) e.g.:
#   pytest -q
#   npm test

# 3) run doc lint / markdown protocol validation
# (not confirmed in repo) e.g.:
#   python -m tools.lint_markdown_protocol
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| CI test results | CI runner | CI artifacts |
| Schema validation report | validator | CI artifacts |
| Graph integrity report | graph test suite | CI artifacts |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes to schema validation rules, redaction rules, or CI gates may require governance review (**approval routing not confirmed in repo**).

### CARE / sovereignty considerations
- Do not commit fixtures that reveal restricted locations or culturally sensitive details.
- Prefer synthetic test data and generalized coordinates where needed.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions match intended use.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `tests/README.md` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
