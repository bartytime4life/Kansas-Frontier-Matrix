---
title: "GraphQL Test Fixtures — README"
path: "src/server/graphql/__tests__/fixtures/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Readme"
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

doc_uuid: "urn:kfm:doc:src:server:graphql:tests:fixtures:readme:v1.0.0"
semantic_document_id: "kfm-src-server-graphql-tests-fixtures-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:server:graphql:tests:fixtures:readme:v1.0.0"
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

# GraphQL Test Fixtures — README

## 📘 Overview

### Purpose
This directory contains **static fixture assets** used by GraphQL test suites (unit/integration) to validate API behavior deterministically. Fixtures here should make tests **stable, reviewable, and reproducible**, while respecting KFM governance rules (provenance-first, no sensitive leakage).

### Scope
| In Scope | Out of Scope |
|---|---|
| Sample GraphQL operations (queries/mutations/subscriptions) | Production data exports or “real” datasets |
| Variables payloads for operations | Secrets, credentials, tokens, API keys |
| Expected responses (contract-level) | Large generated artifacts (goldens) that should be rebuilt automatically |
| Mocked graph/service inputs used by resolvers | Any fixture that encodes restricted/sensitive locations without approved generalization |
| Error/edge-case fixtures (authz, validation) | UI-only fixtures (these belong under `web/` or UI test dirs) |

### Audience
- Primary: API/GraphQL developers writing or updating resolvers and contract tests.
- Secondary: Data/governance reviewers auditing test data safety and provenance fields.

### Definitions
- Glossary link: `docs/glossary.md` (not confirmed in repo).
- “Fixture”: A committed static test artifact (query, variables, expected payload, mock input state).
- “Deterministic”: Same inputs → same outputs, across environments and time.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `src/server/graphql/__tests__/fixtures/README.md` | API | Conventions + safety rules |
| GraphQL tests | `src/server/graphql/__tests__/` | API | Test runner/framework not confirmed in repo |
| GraphQL schema | `src/server/graphql/` | API | Exact schema file(s) not confirmed in repo |
| API contract docs | `docs/` | API + Governance | Use governed contract template when changing schema |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Explains what belongs in fixtures vs elsewhere
- [ ] Safety rules documented (no PII, no secrets, no sensitive locations)
- [ ] Validation steps listed and repeatable

## 🗂️ Directory Layout

### This document
- `path`: `src/server/graphql/__tests__/fixtures/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| API (GraphQL) | `src/server/graphql/` | Schema + resolvers (exact layout not confirmed) |
| Tests | `src/server/graphql/__tests__/` | GraphQL tests and harness code |
| Fixtures | `src/server/graphql/__tests__/fixtures/` | Static inputs/expected outputs for tests |
| Schemas | `schemas/` | JSON schemas (if fixtures are schema-validated; not confirmed) |
| Docs | `docs/` | Governed docs + contracts + standards |

### Expected file tree for this sub-area
~~~text
📁 src/
└── 📁 server/
    └── 📁 graphql/
        └── 📁 __tests__/
            └── 📁 fixtures/
                ├── 📄 README.md
                ├── 📁 operations/
                │   ├── 📄 <operation_name>.graphql        # recommended
                │   └── 📄 <operation_name>.md             # optional notes (avoid duplicating README)
                ├── 📁 variables/
                │   └── 📄 <operation_name>.json           # recommended (stable key order)
                ├── 📁 expected/
                │   └── 📄 <operation_name>.json           # recommended (contract-level)
                └── 📁 mocks/
                    └── 📄 <resolver_or_service>.json      # recommended; keep minimal
~~~

> The file names above are **conventions**. The actual fixture set is repository-dependent.

## 🧭 Context

### Background
KFM’s canonical pipeline enforces an API boundary: downstream clients consume **contracted payloads** through APIs (REST/GraphQL), not by directly querying the graph. GraphQL fixtures help ensure that:
- Resolver behavior is stable across refactors.
- Contracted response shapes (including provenance fields) do not regress.
- Redaction/generalization expectations are testable.

### Assumptions
- The test runner can load fixture files from this directory at runtime (framework not confirmed in repo).
- Fixtures are reviewed in code review like any other source artifact.
- If a GraphQL schema change is introduced, fixtures and contract tests are updated in the same change.

### Constraints / invariants
- Preserve canonical ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Fixtures must not bypass the API boundary (i.e., don’t encode “UI reads graph directly” patterns).
- Fixtures must remain deterministic: avoid timestamps, random IDs, environment-specific data.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Which test runner/framework is used (e.g., Jest/Vitest)? | TBD | TBD |
| Do we validate fixture JSON against schemas under `schemas/`? | TBD | TBD |
| Is there a standard redaction/generalization helper for geospatial fixtures? | TBD | TBD |

### Future extensions
- Add fixture schema validation in CI (JSON schema + deterministic ordering).
- Add a fixture linter (no secrets/PII, max size thresholds, required provenance keys for Focus Mode endpoints).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Fixture: operation + variables] --> B[Test harness]
  B --> C[GraphQL API layer]
  C --> D[Resolver(s)]
  D --> E[(Graph adapter / mocked graph)]
  D --> F[Response payload]
  F --> G[Fixture: expected response]
  G --> H[Assertion + contract checks]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| GraphQL operation | `.graphql` (recommended) | authored | query linting (recommended) |
| Variables payload | `.json` (recommended) | authored | JSON parse + stable ordering |
| Mock inputs | `.json` (recommended) | authored/minimal | schema validation (if available) |
| Expected response | `.json` (recommended) | authored or captured | contract tests (required) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Test results | runner-specific | CI output | test runner |
| Coverage / reports | runner-specific | CI artifacts | not confirmed |

### Sensitivity & redaction
Fixtures in this directory must be safe for the repo’s distribution model:
- **No secrets** (tokens, API keys, credentials).
- **No PII** unless explicitly allowed by governance and redacted/anonymized.
- **No sensitive/restricted locations** unless generalized per sovereignty policy (e.g., reduce precision, replace with bounding region) and documented.

### Quality signals
- Small fixtures (prefer minimal fields required to test the behavior).
- Stable IDs (avoid random UUIDs in expected outputs; if unavoidable, assert on patterns rather than exact values).
- Stable JSON key ordering (to reduce noisy diffs).
- Include provenance-related fields **when the API contract requires them** (e.g., links back to STAC/DCAT/PROV identifiers).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- When fixtures represent geospatial assets, expected payloads should include the correct **STAC Item/Collection identifiers** *if that is part of the GraphQL contract*.

### DCAT
- For dataset-level fixtures (catalog/browse behaviors), include dataset identifiers and license metadata if required by contract.

### PROV-O
- If the endpoint is used in Focus Mode or evidence panels, fixtures should include provenance references (e.g., `prov:wasDerivedFrom` / activity IDs) consistent with the API contract.

### Versioning
- If fixtures depend on a versioned contract, update fixtures as part of the same change that bumps/extends the contract.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Test harness | Load fixtures and invoke resolvers/API | runner-specific |
| GraphQL layer | Parse/validate operations; route to resolvers | GraphQL schema |
| Resolver layer | Transform graph/service results into contracted payloads | internal |
| Graph adapter | Fetch from Neo4j (or mock) with redaction rules | internal |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| GraphQL schema | `src/server/graphql/` | backward compat or version bump |
| Fixture conventions | this README | update with fixture structure changes |
| API contract docs | `docs/` | use governed API contract extension template when changing public contract |

### Extension points checklist (for future work)
- [ ] Add `fixtures/<domain>/...` subfolders if fixtures grow large (domain partitioning)
- [ ] Add schema validation for fixtures under `schemas/` (if adopted)
- [ ] Add redaction/generalization helper for geo fixtures and enforce in CI

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Some GraphQL endpoints may feed Story Nodes or Focus Mode context bundles. In those cases:
- Fixtures must include **provenance-linked** fields that the UI/audit panels rely on.
- Predictive content must be opt-in and include uncertainty/confidence metadata (if applicable).

### Provenance-linked narrative rule
If a fixture includes narrative text fields, it must remain clear whether the text is:
- a direct excerpt (should include a source/document ID), or
- a curated summary (should include derivation/provenance references), or
- a test-only placeholder (prefer obvious placeholders and keep out of user-visible paths).

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Fixture JSON is valid (parseable, stable formatting)
- [ ] GraphQL operations are valid for the current schema (recommended)
- [ ] Contract tests pass (required)
- [ ] No secrets / PII / sensitive locations introduced

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run GraphQL tests
# 2) run fixture lint (if available)
# 3) validate GraphQL schema (if available)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Fixture size threshold breaches | CI | `docs/telemetry/` + `schemas/telemetry/` (not confirmed) |
| Secret scan violations | CI/security | CI logs |

## ⚖ FAIR+CARE & Governance

### Review gates
- Any fixture that contains geospatial coordinates, person-like entities, or document excerpts should be reviewed for:
  - redaction/generalization requirements
  - license compatibility
  - provenance linkage expectations

### CARE / sovereignty considerations
- Fixtures must not inadvertently disclose restricted site locations or culturally sensitive details.
- When in doubt, generalize spatial detail and document why.

### AI usage constraints
- Do not add synthetic “historical facts” into fixtures. If the goal is shape-testing, use explicit placeholders.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial fixtures README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

