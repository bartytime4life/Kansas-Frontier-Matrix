---
title: "KFM Unit Tests — README"
path: "tests/unit/README.md"
version: "v1.0.0"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:tests:unit:readme:v1.0.0"
semantic_document_id: "kfm-tests-unit-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tests:unit:readme:v1.0.0"
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

# KFM Unit Tests — README

- ⬅ Back to tests index: `../README.md` *(not confirmed in repo)*

> **Purpose (required):** Define conventions for **fast, deterministic unit tests** in KFM so CI can catch drift early (logic errors, schema breaks, redaction regressions) without requiring external services or full pipeline runs.

## 📘 Overview

### Purpose

- Define what qualifies as a **unit test** in KFM.
- Standardize where unit tests live under `tests/unit/`.
- Enforce determinism and governance constraints (no hidden I/O, no sensitive data in fixtures).

### Scope

| In Scope | Out of Scope |
|---|---|
| Pure functions and small modules (parsers, normalizers, ID builders, mappers) | Full ETL runs, end-to-end domain ingest, large-data integration |
| Deterministic behavior rules (no network, no clock dependence, pinned randomness) | Spinning up Neo4j / containers / external services |
| Unit validation of schema-building helpers (e.g., “STAC item builder returns required fields”) | Full schema validation gates across `data/stac/`, `data/catalog/dcat/`, `data/prov/` (belongs in contract/integration tests) |
| Unit checks for redaction/sanitization helpers | Governance decisions and policy changes (must be handled in governed docs + human review) |

### Audience

- **Primary:** Contributors writing/updating code in pipelines, graph ingest, API services, UI utilities.
- **Secondary:** Maintainers debugging CI failures and enforcing governance/ethics invariants.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc include: **unit test**, **deterministic**, **idempotent**, **fixture**, **mock/fake**, **schema validation**, **redaction**, **provenance**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Governed doc structure |
| Tests taxonomy | `tests/README.md` | KFM Core | Test types + CI gates *(not confirmed in repo)* |
| Schemas | `schemas/` | Data/Platform | Validation targets for contract/schema tests |
| Pipelines | `src/pipelines/` | Data Eng | ETL + catalog builders |
| Graph | `src/graph/` | Graph Eng | Ontology + ingest tooling |
| API boundary | `src/server/` | API Eng | Contracts + redaction + services *(path not confirmed in repo)* |
| UI | `web/` | Frontend | Map + narrative clients |

### Definition of done (for this document)

- [ ] Front-matter complete + valid, and `path:` matches file location
- [ ] Unit-test constraints are explicit (deterministic, no network, no hidden I/O)
- [ ] Directory conventions are documented with an emoji-safe tree
- [ ] Commands are either repo-accurate **or explicitly marked “not confirmed in repo”**
- [ ] Governance + CARE/sovereignty considerations are explicitly stated
- [ ] Version history present

## 🗂️ Directory Layout

### This document

- `path`: `tests/unit/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Tests | `tests/` | Unit/integration/contract/e2e tests + fixtures |
| Schemas | `schemas/` | JSON Schemas + validation specs |
| Data domains | `data/` | Raw/work/processed outputs + catalogs |
| Pipelines | `src/pipelines/` | Deterministic ETL + catalog generation |
| Graph | `src/graph/` | Ontology + ingest + graph build |
| API | `src/server/` | Contracted access boundary *(not confirmed in repo)* |
| UI | `web/` | React/Map UI *(not confirmed in repo)* |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 tests/
│
├── 📄 README.md                      # test taxonomy + global CI gates (not confirmed in repo)
│
└── 📁 unit/
    │
    ├── 📄 README.md                  # this file
    │
    ├── 📁 pipelines/                 # pure transforms (parsers, normalizers, ID builders)
    │
    ├── 📁 graph/                     # mapping/query-builder helpers (NO DB required)
    │
    ├── 📁 server/                    # serialization, validation, redaction helpers
    │
    ├── 📁 web/                       # UI utilities/components tests (optional; not confirmed in repo)
    │
    ├── 📁 helpers/                   # shared fakes/mocks/stubs
    │
    └── 📁 fixtures/                  # synthetic fixtures only (small, non-sensitive)
~~~

## 🧭 Context

### Background

KFM is a governed geospatial + historical knowledge system with a non-negotiable pipeline ordering:

**ETL → STAC/DCAT/PROV → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

Unit tests exist to prevent “silent drift” by enforcing correctness and determinism at the smallest practical scope.

### Assumptions

- The repo’s exact unit-test runner(s) and commands are **not confirmed in repo**.
- KFM is likely multi-language (pipelines + web), so unit tests may exist in multiple runtimes.
- CI executes unit tests in a restricted environment (no secrets, limited/no egress).

### Constraints / invariants

- **Determinism required**
  - No network calls by default.
  - No reliance on local machine state (home directories, environment quirks).
  - No unpinned randomness (seed if randomness is unavoidable).
  - No dependency on wall-clock time (freeze time or inject clocks).
- **Fast**
  - Unit tests should run quickly and avoid large fixtures.
- **No external services**
  - Do not start Neo4j, call external APIs, or require Docker in unit tests.
- **API boundary is mandatory**
  - UI code should never depend on direct Neo4j access; it must use contracted APIs.

## 🗺️ Diagrams

### Where unit tests sit relative to the pipeline

~~~mermaid
flowchart LR
  UT[Unit tests<br/>(tests/unit)] --> C[Code correctness<br/>pure functions]
  C --> ETL[ETL]
  C --> CAT[STAC/DCAT/PROV builders]
  C --> G[Graph ingest helpers]
  C --> API[API services/helpers]
  C --> UI[UI utilities]

  ETL --> CAT --> G --> API --> UI --> SN[Story Nodes] --> FM[Focus Mode]
~~~

## 🧠 Story Node & Focus Mode Integration

Unit tests do **not** typically validate complete Story Node publication (that belongs in contract/integration checks), but unit tests **should** cover:

- parsers/validators used to load Story Node metadata (front-matter parsing, ID normalization),
- sanitization and redaction helpers used before content reaches Story/Focus surfaces.

If a unit test touches narrative content structures, it must not introduce unsourced claims or embed sensitive locations in fixtures.

## 🧪 Validation & CI/CD

### What belongs in unit tests (examples)

| Area | Example unit-test targets | Must avoid |
|---|---|---|
| Pipelines | parsing, normalization, stable ID generation, schema field mapping | downloading datasets, full ETL runs |
| Catalog helpers | STAC/DCAT/PROV object builders return required keys | validating entire `data/**` trees |
| Graph helpers | mapping from records → nodes/edges, query-builder correctness | live DB connections |
| API helpers | serialization, redaction logic, input validation | live API calls, real credentials |
| UI helpers | pure utilities, rendering logic (if applicable) | end-to-end browser automation |

### Reproduction (deterministic)

> Example placeholders — replace with repo-specific commands (**not confirmed in repo**).

~~~bash
# Example (Python)
# python -m pytest tests/unit -q

# Example (Node)
# npm test

# Example (mono-repo)
# make test-unit
~~~

### CI expectations (if configured)

- Unit tests are expected to run on every PR affecting code.
- Failures should be actionable and point to a single module/function.
- If a unit test requires network, DB, or heavy I/O, it should be moved to `tests/integration/` or `tests/e2e/` (not confirmed in repo).

## 📦 Data & Metadata

### Fixtures rules

- Fixtures must be **synthetic** and **minimal**.
- Do not include:
  - secrets/tokens/keys,
  - PII,
  - culturally sensitive/restricted locations,
  - large raw datasets.
- Prefer fixtures that are:
  - small JSON/CSV snippets,
  - geometry-free unless essential,
  - stable and deterministic (sorted keys, pinned values).

### Where fixtures should live

- `tests/unit/fixtures/` (recommended)
- If a shared fixture is used across test types, consider `tests/fixtures/` *(not confirmed in repo)*.

## 🌐 STAC, DCAT & PROV Alignment

Unit tests can (and should) validate **helpers** that build STAC/DCAT/PROV structures by checking:

- required fields exist,
- stable IDs/keys are produced deterministically,
- serialization is stable (ordering/normalization).

Full schema validation against `schemas/**` and validation across `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` is typically handled in **contract** or **integration** tests.

## 🧱 Architecture

### Architecture-synced testing rule

KFM’s architecture is layered. Unit tests should target **one layer’s code at a time**, and mock boundaries rather than crossing them.

| Layer | Unit test focus | Boundary reminder |
|---|---|---|
| ETL (`src/pipelines/`) | pure transforms + mapping logic | no network, no raw data pulls |
| Catalog builders | object construction + deterministic IDs | schema validation elsewhere |
| Graph (`src/graph/`) | mapping logic + constraint helpers | no Neo4j in unit tests |
| API (`src/server/`) | redaction + contracts helpers | UI consumes APIs only |
| UI (`web/`) | pure utilities/components | never reads Neo4j directly |

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when unit tests change or introduce logic that could:

- reduce redaction/generalization,
- change classification propagation behavior,
- add fixtures that encode sensitive location patterns.

### CARE / sovereignty considerations

- Even test fixtures can leak sensitive information.
- Keep fixtures coarse, synthetic, and non-identifying.
- Follow `docs/governance/SOVEREIGNTY.md` for any content that could intersect with protected knowledge or locations.

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions match intended use.
- Do not use AI outputs to infer sensitive locations or generate new governance policy.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial `tests/unit/` README establishing unit-test conventions | (you) |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Tests index: `tests/README.md` *(not confirmed in repo)*
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
---
