---
title: "KFM Contract Tests — README"
path: "tests/contract/README.md"
version: "v1.0.0"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:tests:contract:readme:v1.0.0"
semantic_document_id: "kfm-tests-contract-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tests:contract:readme:v1.0.0"
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

# KFM Contract Tests — README

> **Purpose (required):** Define the **contract testing conventions** for KFM and where those tests live so we can detect **breaking changes, schema drift, leakage risks, and provenance omissions** *before* they reach the graph, APIs, UI, Story Nodes, or Focus Mode.

## 📘 Overview

### Purpose

- Define what “contract tests” mean in KFM and how they differ from unit/integration/E2E tests.
- Map contract tests to **KFM subsystem contracts** and “do not break” rules:
  - catalog outputs must be machine-validated (STAC/DCAT/PROV),
  - APIs must be backward compatible **or** version-bumped,
  - UI must not cause hidden data leakage,
  - Focus Mode must only consume provenance-linked content. *(See `docs/MASTER_GUIDE_v12.md`.)*
- Provide directory conventions so contributors can add/maintain contract tests without guessing.

### Scope

| In Scope | Out of Scope |
|---|---|
| Contract tests for **schemas**, **API contracts**, and **machine-consumed content shapes** | Choosing a specific test framework/tooling (**not confirmed in repo**) |
| Tests that validate **public-facing payloads** (OpenAPI/GraphQL, UI registries, Story Node structures) | Full end-to-end UI automation (belongs in `tests/e2e/` or under `web/` if split) |
| Contract change “rules of engagement” (versioning, redaction, provenance requirements) | Writing new governance policy (see `docs/governance/*`) |

### Audience

- **Primary:** Contributors changing schemas, pipelines, graph-export shapes, API responses, UI layer registries, or Story Nodes.
- **Secondary:** Reviewers/maintainers enforcing CI gates and governance rules.

### Definitions (link to glossary)

- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc:
  - **Contract test:** A test that asserts a **boundary promise**: “producer output” conforms to “consumer expectations.”
  - **Contract artifact:** A machine-readable specification or schema (OpenAPI, GraphQL SDL, JSON Schema, Story Node structure, registry schemas).
  - **Backward compatible change:** A change that does not break existing consumers.
  - **Breaking change:** Requires a version bump and migration path.
  - **Redaction/generalization:** Rules to prevent exposing restricted locations, sensitive attributes, or other protected content.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline + minimum CI gates + subsystem contracts) | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical invariants + minimum gates |
| Tests index (taxonomy + expectations) | `tests/README.md` | TBD | Parent README (**not confirmed in repo**) |
| Schema registry | `schemas/` | TBD | Contract schemas (STAC/DCAT/PROV/story nodes/telemetry) |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | TBD | Use when changing REST/GraphQL contracts |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Structure used by this README |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Story Node contract expectations |
| Workflows / CI gates | `.github/workflows/` | TBD | CI entrypoints (**not confirmed in repo**) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid, and `path:` matches file location.
- [ ] Directory layout and test placement rules are explicit.
- [ ] Contract test triggers are documented (when you must add/update tests).
- [ ] CI behavior contract is stated (**validate if present / fail if invalid / skip if not applicable**).
- [ ] Governance + CARE/sovereignty considerations explicitly stated for redaction/leakage-sensitive changes.

## 🗂️ Directory Layout

### This document

- `path`: `tests/contract/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Tests | `tests/` | Unit/integration/contract/e2e tests + fixtures |
| Schemas | `schemas/` | JSON schemas + telemetry schemas + validators |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Generated STAC/DCAT/PROV artifacts (if present) |
| Graph | `src/graph/` | Graph build + ontology bindings + constraints |
| Pipelines | `src/pipelines/` | Deterministic ETL + catalog generation |
| API boundary | `src/server/` (or `src/api/` — **not confirmed in repo**) | Contracted access layer (OpenAPI/GraphQL) |
| UI | `web/` | React/MapLibre UI + layer registry |
| Docs | `docs/` | Governed docs, templates, standards, governance |
| CI | `.github/` | Workflows + local actions |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 tests/
└── 📁 contract/
    ├── 📄 README.md
    ├── 📁 api/                 # OpenAPI/GraphQL contract conformance + compatibility checks (recommended)
    ├── 📁 schemas/             # JSON-schema contract validation (STAC/DCAT/PROV/story nodes/telemetry) (recommended)
    ├── 📁 ui/                  # UI registry schema contracts (recommended)
    ├── 📁 story_nodes/         # Story Node structure + provenance rules (if machine-consumed) (optional)
    ├── 📁 fixtures/            # synthetic, minimal fixtures only (recommended)
    └── 📁 helpers/             # shared assertions/utilities (recommended)
~~~

### What belongs where (quick mapping)

| Contract type | Producer → Consumer | Where the test belongs (recommended) |
|---|---|---|
| STAC/DCAT/PROV schema conformance | Pipelines/catalog builders → Graph/API/UI | `tests/contract/schemas/` |
| API response contract conformance | API boundary → UI/clients/Focus Mode | `tests/contract/api/` |
| UI registry schema conformance | UI config → UI runtime | `tests/contract/ui/` |
| Story Node structural contract | Story Node docs → UI narrative rendering / Focus Mode surfacing | `tests/contract/story_nodes/` |
| Redaction / leakage invariants | Any producer → Public outputs | Co-locate with affected contract (`api/`, `schemas/`, `ui/`) |

## 🧭 Context

### Background

KFM is a governed geospatial + historical knowledge system with a canonical pipeline ordering:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Contract tests exist to prevent “silent drift” across subsystem boundaries, and to ensure that:

- **Schemas and contracts are treated as first-class artifacts.**
- **APIs remain backward compatible (or version-bumped).**
- **Frontend consumption stays behind the API boundary (no direct graph calls).**
- **Focus Mode remains provenance-linked (no uncited facts).**

### Assumptions

- The repo’s exact test runner(s) and commands are **not confirmed in repo**.
- Contract artifacts exist or will exist (e.g., OpenAPI/GraphQL schemas; JSON Schemas under `schemas/`).
- CI workflows may skip gates if the referenced canonical roots are not present in the repo snapshot.

### Constraints / invariants (must not break)

- Contract tests must be **deterministic**:
  - no network calls by default,
  - no reliance on local machine state,
  - no unpinned randomness (seed if needed).
- Fixtures must not include secrets, PII, or restricted coordinates.
- Any contract change that impacts public payloads must be:
  - documented (use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` for API changes),
  - validated by contract tests,
  - versioned appropriately (semver + migration notes when breaking).

### When you must add or update a contract test

Add/update a contract test whenever you change:

- A JSON schema in `schemas/**` (or a generated output that claims conformance to it).
- A public API payload, shape, field meaning, or version.
- Redaction/generalization behavior for restricted or sensitive fields.
- Any machine-consumed UI registry/config (e.g., layer registry JSON).
- Story Node structure, front-matter requirements, or provenance fields (if machine-validated/ingested).

## 🗺️ Diagrams

### Contract boundaries in the canonical pipeline

~~~mermaid
flowchart LR
  A["ETL (src/pipelines/)"] --> B["Catalogs (STAC/DCAT/PROV)"]
  B --> C["Graph (Neo4j via src/graph/)"]
  C --> D["API boundary (src/server/ or src/api/)"]
  D --> E["UI (web/)"]
  E --> F["Story Nodes (docs/reports/.../story_nodes/)"]
  F --> G["Focus Mode"]

  subgraph CT["Contract Tests (tests/contract/)"]
    T1["schemas/: STAC/DCAT/PROV + telemetry + story nodes"]
    T2["api/: OpenAPI/GraphQL conformance + compatibility"]
    T3["ui/: layer registry schema + leakage guardrails"]
  end

  T1 -. "validates" .-> B
  T2 -. "validates" .-> D
  T3 -. "validates" .-> E
~~~

## 🧠 Story Node & Focus Mode Integration

### How contract tests protect Focus Mode

Focus Mode is a downstream synthesis layer and must only consume **provenance-linked** content.

Contract tests should enforce (where applicable):

- API responses include **stable identifiers** and **provenance references** required for auditability.
- Story Nodes include the required structure and provenance annotations expected by the UI/Focus Mode.
- Redaction/generalization rules prevent restricted/sensitive leakage in:
  - API payloads,
  - UI registries,
  - published narrative artifacts.

### Provenance-linked narrative rule

- Every factual claim surfaced in Story Nodes / Focus Mode must trace to a dataset/record/asset identifier.
- Predictive/AI content (if present) must be clearly marked, opt-in, and include uncertainty metadata.

## 🧪 Validation & CI/CD

### CI behavior contract (non-negotiable)

- **Validate if present:** if a canonical root exists (or changes), validate its artifacts.
- **Fail if invalid:** schema errors, contract violations, missing links, or orphan references fail deterministically.
- **Skip if not applicable:** optional roots absent → skip without failing the overall pipeline.

### Minimum checks (contract-test relevant)

- [ ] JSON schema validation (STAC/DCAT/PROV + story node schemas + telemetry schemas if present)
- [ ] API contract tests (OpenAPI/GraphQL) for any changed endpoints/payloads
- [ ] UI registry schema checks (layer registry + access rules if schema’d)
- [ ] Redaction/leakage guardrails (no restricted coordinates in public artifacts/logs)
- [ ] Link/reference integrity for machine-consumed artifacts (IDs resolve; no orphan references)

### Local reproduction (placeholders)

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.

# Run contract tests (if configured)
# <TBD>

# Example patterns (do not assume these exist):
# python -m pytest tests/contract
# npm test -- tests/contract
# make test-contract
~~~

### Debug map (where to look when a contract test fails)

| Failure type | Likely cause | First place to check |
|---|---|---|
| Schema validation failure | Output no longer matches JSON Schema | `schemas/**` + the changed output under `data/**` |
| OpenAPI/GraphQL contract failure | API response shape drift | API contract artifacts under `src/server/**` or `src/api/**` (**not confirmed**) |
| Provenance contract failure | Missing/invalid evidence references | API response serializer + provenance mapping docs |
| UI registry schema failure | Registry JSON drift or missing fields | `web/**` registry config + schema (**not confirmed**) |
| Redaction/leakage failure | Restricted fields exposed | Redaction layer at API boundary + governance docs |

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Contract artifacts | OpenAPI/GraphQL/JSON Schema | `src/**`, `schemas/**` | Contract tests |
| Golden/synthetic fixtures | JSON/CSV/GeoJSON/MD | `tests/contract/fixtures/` | Must be synthetic + safe |
| Story Node artifacts (if validated) | Markdown | `docs/**` (canonical story node root not confirmed) | Markdown protocol + story node schema |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Contract test reports | CI logs/artifacts | CI system | Deterministic pass/fail |
| Snapshot diffs (if used) | text/JSON | CI artifacts | Must not leak restricted data |
| Optional hash manifests | sha256 | `mcp/runs/**` or CI artifacts (**not confirmed**) | Used to ensure reproducibility |

### Sensitivity & redaction

- Do not commit fixtures with:
  - secrets/tokens,
  - PII,
  - restricted exact coordinates,
  - culturally sensitive content without governance approval.
- Treat CI logs and artifacts as a potential leakage path; redact/avoid printing sensitive payloads.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- If a change impacts STAC outputs, contract tests should validate:
  - Collections + Items conform to STAC expectations and any KFM profiles under `schemas/stac/**` (if present).
  - IDs remain stable or versioned with clear predecessor/successor linkage.

### DCAT

- If a change impacts DCAT outputs, contract tests should validate:
  - Minimum required mapping fields (title/description/license/keywords) are present.
  - Dataset identifiers remain stable or are versioned properly.

### PROV-O

- If a change impacts provenance outputs, contract tests should validate:
  - A PROV activity exists for the transform that generated the artifact.
  - Lineage is sufficient to trace downstream narrative claims back to evidence.

## 🧱 Architecture

### Subsystem contracts (boundary summary)

| Boundary | Contract artifacts | “Do not break” rule |
|---|---|---|
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no uncited facts / no hallucinated sources |

### Versioning expectations (practical rule)

- If a change is **breaking**, bump the contract version and provide migration notes.
- If a change is **non-breaking**, update tests and ensure existing clients still pass.

## ⚖ FAIR+CARE & Governance

### Review gates

Contract changes typically require elevated review when they introduce or alter:

- public-facing endpoints or payloads,
- redaction/generalization behavior,
- handling of restricted locations or culturally sensitive content,
- user-visible AI narrative behavior.

### CARE / sovereignty considerations

- Do not commit fixtures that reveal restricted locations or culturally sensitive details.
- Prefer synthetic test data and generalized coordinates where needed.
- Ensure contract tests do not re-expose restricted geometry via logs, snapshots, or diffs.

### AI usage constraints

- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy text; inferring sensitive locations (directly or indirectly).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial `tests/contract/README.md` scaffold (contract testing conventions + placement rules) | TBD |

---

Footer refs (do not remove):

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Tests index: `tests/README.md` *(not confirmed in repo)*
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

