---
title: "KFM Tests — Integration"
path: "tests/integration/README.md"
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

doc_uuid: "urn:kfm:doc:tests:integration:readme:v1.0.0"
semantic_document_id: "kfm-tests-integration-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tests:integration:readme:v1.0.0"
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

# KFM Tests — Integration

## 📘 Overview

### Purpose
- Define **what counts as an integration test** in KFM and where these tests live.
- Standardize **how integration tests exercise the canonical pipeline** (ETL → catalogs → graph → API) without breaking determinism and governance.
- Provide **repeatable patterns** for building integration fixtures, spinning up dependencies (when needed), and validating outputs.

### Scope
| In Scope | Out of Scope |
|---|---|
| Multi-module tests that cross at least **two** subsystems (e.g., pipeline→catalog, catalog→graph, graph→API) | Unit tests that isolate a single function/module (see `tests/unit/`) |
| “Vertical slice” smoke tests for a representative domain fixture (small synthetic data) | Full end-to-end UI browser tests (see `tests/e2e/` or `web/` tooling) |
| Integration checks for deterministic outputs, stable IDs, schema validity, provenance linkage | Deciding the project’s primary test framework / runner (**not confirmed in repo**) |
| Tests that require a real service boundary (e.g., API server talking to a test graph DB) | Performance/load testing (belongs under tooling/benchmarks — **not confirmed in repo**) |

### Audience
- **Primary:** contributors touching `src/pipelines/`, `src/graph/`, `src/server/` (or legacy API location), `schemas/`, and domain data.
- **Secondary:** maintainers triaging CI failures and reviewing changes that impact cross-stage contracts.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc include: **integration test**, **fixture**, **idempotence**, **schema validation**, **contract test**, **provenance**, **redaction**, **canonical pipeline**.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Defines ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode |
| Tests taxonomy (unit/integration/contract/e2e) | `tests/README.md` | KFM Core | Parent README for this directory |
| Schemas for catalogs + UI + story | `schemas/` | Data/Platform | Integration tests should validate against these where applicable |
| STAC outputs | `data/stac/` | Data/Platform | Collections + items used as evidence products |
| DCAT outputs | `data/catalog/dcat/` | Data/Platform | Dataset records |
| PROV outputs | `data/prov/` | Data/Platform | Provenance bundles |
| Graph build + ingest | `src/graph/` + `data/graph/` | Graph Eng | Ingest uses catalog outputs |
| API boundary | `src/server/` (v13 target) or `src/api/` (legacy) | API Eng | UI consumes via contracts; never direct Neo4j |
| Story Nodes | `docs/reports/story_nodes/` | Narrative | Integration tests may validate provenance-linked narrative behavior |

### Definition of done (for this document)
- [ ] Front-matter complete + `path` matches `tests/integration/README.md`
- [ ] Integration test definition + placement rules are explicit
- [ ] Determinism rules are explicit (no hidden I/O, pinned randomness, time control)
- [ ] Minimal “vertical slice” expectations are described
- [ ] Reproduction commands are either repo-accurate or marked “not confirmed in repo”
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `tests/integration/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Tests root | `tests/` | Taxonomy and shared fixtures/helpers |
| Unit tests | `tests/unit/` | Fast, isolated tests |
| Contract tests | `tests/contract/` | Schema & API contract tests (recommended) |
| E2E tests | `tests/e2e/` | UI/API end-to-end tests (may live under `web/`) |
| Shared fixtures | `tests/fixtures/` | Small synthetic fixtures only |
| Helpers | `tests/helpers/` | Shared test utilities |
| Pipelines | `src/pipelines/` | ETL + catalog builders |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Evidence + lineage artifacts |
| Graph | `src/graph/` + `data/graph/` | Ontology + import fixtures |
| API boundary | `src/server/` *(v13 target)* or `src/api/` *(legacy; not confirmed in repo)* | Contracts + redaction |
| UI | `web/` | React/MapLibre; consumes APIs only |

### Expected file tree for this sub-area
> This is the **recommended** structure. Some subdirectories may not exist yet (**not confirmed in repo**).

~~~text
📁 tests/
├── 📄 README.md
├── 📁 integration/
│   ├── 📄 README.md                           # (this file)
│   ├── 📁 pipeline/                           # pipeline↔catalog integration (recommended)
│   │   └── 📄 test_pipeline_smoke.<ext>        # run small fixture → produces catalogs
│   ├── 📁 catalogs/                            # STAC/DCAT/PROV schema + cross-link checks
│   │   └── 📄 test_catalog_integrity.<ext>
│   ├── 📁 graph/                               # ingest catalogs → graph integrity checks
│   │   └── 📄 test_graph_ingest.<ext>
│   ├── 📁 api/                                 # API server ↔ graph integration checks
│   │   └── 📄 test_api_smoke.<ext>
│   ├── 📁 story_nodes/                         # optional: Story Node ↔ graph ↔ api checks
│   │   └── 📄 test_storynode_resolution.<ext>
│   ├── 📁 fixtures/                            # integration-specific fixtures (small only)
│   │   └── 📁 <fixture_name>/
│   └── 📁 helpers/                             # integration harness utilities
│       └── 📄 <helper>.<ext>
└── …
~~~

## 🧭 Context

### Background
KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Integration tests exist to keep *cross-stage contracts* stable and to prevent “silent drift” where each stage still “works” in isolation but the end-to-end pipeline no longer composes.

### Assumptions
- The repo’s exact integration test runner(s) and CLI commands are **not confirmed in repo**. This README provides runner-agnostic expectations.
- Integration tests may need ephemeral services (e.g., Neo4j, API server). Local and CI harness strategy is **not confirmed in repo** (Docker Compose, Testcontainers, etc.).
- Integration fixtures must remain **small** and **synthetic** unless an explicit governance exception is documented.

### Constraints / invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- **API boundary is mandatory:** the UI never queries Neo4j directly; it consumes contracted API responses.
- Tests must be deterministic and diffable:
  - no network calls by default (unless explicitly sandboxed and replayed)
  - no reliance on local machine state (time, locale, installed tools, working directory)
  - randomness must be pinned (seeded) and recorded
  - all temp outputs must land in temp directories and be cleaned up
- Fixtures must not contain secrets, PII, or culturally sensitive locations. If a fixture represents sensitive geography, it must be generalized and reviewed per `docs/governance/SOVEREIGNTY.md`.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical integration test harness (Docker Compose / Testcontainers / CI service containers)? | TBD | TBD |
| Where do schema validators live (scripts, CI actions, test utilities)? | TBD | TBD |
| Do we keep “golden” catalogs (STAC/DCAT/PROV) for diff-based tests, and where? | TBD | TBD |
| How are Neo4j migrations/versioning handled for integration tests? | TBD | TBD |

### Future extensions
- Golden-file tests for catalog outputs (STAC/DCAT/PROV), including orphan-link detection
- Graph ingest smoke tests that validate label/relationship invariants against a fixture ontology
- API contract + integration pairing: contract tests for shape + integration tests for behavior
- Optional Focus Mode “context bundle” regression tests (provenance links, redaction, uncertainty flags)

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  T[Test runner] --> F[Integration fixtures<br/>tests/fixtures + tests/integration/fixtures]

  F --> P[ETL/Pipeline run<br/>src/pipelines]
  P --> C[Catalog outputs<br/>STAC/DCAT/PROV]
  C --> G[Graph ingest<br/>src/graph + data/graph]
  G --> A[API boundary<br/>src/server (target) / src/api (legacy)]
  A --> Assert[Assertions<br/>schema + links + redaction + provenance]

  Assert -. does not call .-> UI[UI (web) uses API only]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Test as Integration test
  participant API
  participant Graph
  Test->>API: Request contracted endpoint
  API->>Graph: Query with redaction + provenance refs
  Graph-->>API: Result subgraph + provenance IDs
  API-->>Test: Payload + audit/provenance fields
  Test->>Test: Assert schema + provenance linkage
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Integration fixture dataset | files (CSV/GeoJSON/etc.) | `tests/fixtures/` or `tests/integration/fixtures/` | Size limits + no-PII review |
| Pipeline configuration | YAML/JSON/env | repo configs (location not confirmed) | Schema-validated where possible |
| Schema sets | JSON Schema | `schemas/` | Must validate; version pinned |
| Service harness (optional) | compose/yaml | `tests/integration/` or `tools/` (not confirmed) | Deterministic startup + health checks |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Test report | JUnit/JSON/text | CI artifacts (location not confirmed) | Runner-defined |
| Temporary catalogs | JSON | temp dir (do not commit) | STAC/DCAT/PROV schemas |
| Temporary graph import | CSV/Cypher | temp dir (do not commit) | graph ingest constraints |
| Telemetry (optional) | JSON | `docs/telemetry/` + `schemas/telemetry/` | telemetry schema |

### Sensitivity & redaction
- Integration tests must not “leak” restricted geometry or cultural knowledge in:
  - committed fixtures,
  - snapshots/golden files,
  - CI logs.
- If a behavior depends on redaction rules, the test must assert both:
  - what is returned for **public** access, and
  - what is returned for **authorized** access (if such a concept exists; not confirmed in repo).

### Quality signals
- **Determinism:** integration suite produces the same outputs given the same inputs (stable IDs, sorted outputs, fixed timestamps where needed).
- **Schema compliance:** STAC/DCAT/PROV artifacts validate against `schemas/`.
- **Link integrity:** no orphan references (IDs referenced by one stage exist in the producing stage).
- **Runtime budget:** integration suite remains bounded (target budgets are project-defined; not confirmed in repo).
- **Flake rate:** integration tests should not depend on timing races; readiness checks must be explicit.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: test fixture collection(s) used by integration suite *(name/IDs are suite-defined; not confirmed in repo)*.
- Items involved: fixture items produced by the pipeline and validated before graph ingest.
- Extension(s): any KFM custom fields used in fixtures must be documented and schema-validated.

### DCAT
- Dataset identifiers: integration fixture should include a minimal DCAT dataset record if catalog stage generates it.
- License mapping: fixture datasets must declare license consistent with governance defaults.
- Contact / publisher mapping: if required by schema, use a synthetic/test publisher identity (no personal emails).

### PROV-O
- `prov:wasDerivedFrom`: fixture raw inputs → derived outputs should be linkable.
- `prov:wasGeneratedBy`: integration runs should emit an activity/run identifier.
- Activity / Agent identities: tests may use a “test agent” identity to avoid attributing to individuals.

### Versioning
- If integration tests exercise versioned outputs, they must validate:
  - STAC predecessor/successor links (where used),
  - graph mirrors of version lineage (if ingest supports it).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Integration test harness | Orchestrate cross-stage run and assertions | Test runner + helpers |
| ETL / pipelines | Produce normalized outputs and catalogs | configs + run logs |
| Catalogs | Produce/validate STAC/DCAT/PROV | JSON + schema validators |
| Graph | Ingest catalogs and preserve semantics | importer + constraints |
| APIs | Serve contracts and enforce redaction | REST/GraphQL (not confirmed) |
| Story Nodes (optional) | Prove narrative linkage to evidence | schema + entity resolution |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog (recommended) |
| API schemas/contracts | `src/server/` + `docs/` *(target)* | Contract tests required |
| Graph ingest constraints | `src/graph/` + `data/graph/` | Stable labels/edges; migration plan |
| UI config schema (if validated here) | `schemas/ui/` | Schema version bump when breaking |

### Extension points checklist (for future work)
- [ ] Fixture: added under `tests/fixtures/` (small, synthetic, no secrets)
- [ ] Pipeline: fixture run produces STAC/DCAT/PROV and validates
- [ ] PROV: run/activity ID recorded and linked to outputs
- [ ] Graph: ingest test validates labels/relations + key queries
- [ ] API: integration test exercises endpoint + redaction expectations
- [ ] Story/Focus Mode: provenance references enforced (when applicable)
- [ ] Telemetry: integration run records signals (optional but recommended)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Integration tests should ensure that any “focusable” entity produced by the graph ingest can be:
  - resolved via API calls (not direct Neo4j access),
  - linked to evidence IDs (STAC/DCAT/PROV),
  - filtered/redacted appropriately.

### Provenance-linked narrative rule
- Any integration test that touches Story Nodes or Focus Mode must assert:
  - every surfaced claim links to an evidence ID (dataset/item/activity),
  - predictive/AI-generated content (if any) is opt-in and clearly labeled with uncertainty metadata.

### Optional structured controls
~~~yaml
# Optional controls for Focus Mode regression fixtures (if used)
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter, fencing, etc.)
- [ ] Schema validation (STAC/DCAT/PROV + any domain schemas)
- [ ] Cross-link validation (STAC↔DCAT↔PROV↔Graph references)
- [ ] Graph integrity checks (labels/relationships/constraints)
- [ ] API integration checks (contracted payloads + redaction)
- [ ] Security and sovereignty checks (fixtures + outputs)

> Determinism rule used in CI elsewhere: if an optional root is absent, jobs may skip; if present but invalid, jobs fail.

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 0) (optional) start service harness (Neo4j/API) for integration tests
# docker compose -f tests/integration/compose.yml up -d

# 1) validate schemas
# <schema-validator-command>

# 2) run integration tests
# <test-runner> tests/integration

# 3) collect artifacts / reports
# <report-export-command>

# 4) teardown harness
# docker compose -f tests/integration/compose.yml down -v
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| integration_run_id | test harness | CI logs + optional telemetry bundle |
| schema_validation_summary | validators | `docs/telemetry/` (optional) |
| flake_rate | CI history | CI dashboard (not confirmed in repo) |
| orphan_reference_count | link checker | telemetry bundle (optional) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes to integration fixtures or harness that touch:
  - restricted geographies,
  - Indigenous data,
  - redaction behavior,
  - API boundary/security rules,
  require maintainer + governance review.

### CARE / sovereignty considerations
- If a test fixture represents Indigenous lands, culturally sensitive locations, or restricted heritage sites:
  - do not commit raw coordinates unless explicitly permitted,
  - prefer generalized geometry or synthetic stand-ins,
  - document the rule and the reviewer outcome.

### AI usage constraints
- This README inherits AI permissions/prohibitions from front-matter. Do not generate or infer sensitive locations in tests or documentation.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial integration test README | TBD |

---
Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Tests root: `tests/README.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

