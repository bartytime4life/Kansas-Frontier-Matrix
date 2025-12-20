---
title: "KFM — GraphQL Test Fixtures (Mocks)"
path: "src/server/graphql/__tests__/fixtures/mocks/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:src:server:graphql:tests:fixtures:mocks:v1.0.0"
semantic_document_id: "kfm-src-server-graphql-tests-fixtures-mocks-v1.0.0"
event_source_id: "ledger:kfm:doc:src:server:graphql:tests:fixtures:mocks:v1.0.0"
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

# KFM — GraphQL Test Fixtures (Mocks)

## 📘 Overview

### Purpose
This directory stores **mock artifacts** used by GraphQL tests (e.g., resolver/unit/integration-style tests) to provide deterministic inputs and stubbed dependencies.

Typical uses include:
- Mock upstream/downstream service responses (HTTP/SDK calls)
- Mock graph/DB adapter results returned to resolvers
- Mock request context objects (auth/session/tenant context) used by resolvers

> Note: Specific test runners/frameworks and mock loading conventions are **not confirmed in repo**. This README defines recommended, repo-safe conventions for fixtures stored here.

### Scope
| In Scope | Out of Scope |
|---|---|
| Deterministic mock payloads used by GraphQL tests | Golden “expected outputs” (use `../expected/`) |
| Minimal, scenario-focused fixtures | Large real-world datasets |
| Sanitized, non-sensitive example records | Credentials, tokens, secrets, real PII |

### Audience
- Primary: Backend/API engineers writing GraphQL tests
- Secondary: Graph/ETL engineers validating API contracts and provenance handling

### Definitions (link to glossary)
- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc: fixture, mock, expected output, resolver, context, provenance

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Fixtures (mocks) | `src/server/graphql/__tests__/fixtures/mocks/` | API | Inputs + dependency stubs |
| Fixtures (expected) | `src/server/graphql/__tests__/fixtures/expected/` | API | Golden outputs / snapshots |
| Fixtures index | `src/server/graphql/__tests__/fixtures/README.md` | API | Folder-level conventions |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory purpose and boundaries are clear
- [ ] Sensitivity rules stated (no secrets/PII)
- [ ] Repeatable usage guidance for tests (framework-agnostic)

## 🗂️ Directory Layout

### This document
- `path`: `src/server/graphql/__tests__/fixtures/mocks/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| API GraphQL | `src/server/graphql/` | Schema, resolvers, server glue |
| Tests | `src/server/graphql/__tests__/` | GraphQL tests |
| Fixtures root | `src/server/graphql/__tests__/fixtures/` | Shared test assets |
| Expected outputs | `src/server/graphql/__tests__/fixtures/expected/` | Golden assertions |
| Mocks (this dir) | `src/server/graphql/__tests__/fixtures/mocks/` | Stubbed inputs/deps |

### Expected file tree for this sub-area
~~~text
📁 src/
└── 📁 server/
    └── 📁 graphql/
        └── 📁 __tests__/
            └── 📁 fixtures/
                ├── 📄 README.md
                ├── 📁 expected/
                │   └── 📄 README.md
                └── 📁 mocks/
                    ├── 📄 README.md
                    ├── 📁 context/
                    │   └── 📄 <scenario>.<ext>
                    ├── 📁 graph/
                    │   └── 📄 <scenario>.<ext>
                    └── 📁 services/
                        └── 📄 <scenario>.<ext>
~~~

> Folder names like `context/`, `graph/`, `services/` are **recommended** for organizing mocks by dependency boundary. If the repo already uses different names, keep existing structure and only add this grouping when it reduces ambiguity.

## 🧭 Context

### Background
KFM’s canonical pipeline requires a strict separation between stages:
ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → UI → Story Nodes → Focus Mode.

GraphQL tests help enforce the “APIs as contracts” layer by verifying resolver behavior against stable mock inputs, without relying on live external systems.

### Assumptions
- Tests should be deterministic and runnable in CI without network access (**not confirmed in repo**, but recommended).
- Fixtures are stored in-repo to make changes reviewable via diffs.

### Constraints / invariants
- The canonical pipeline ordering is preserved (no shortcutting governance/provenance contracts).
- Frontend does not read the graph directly; API contracts are the boundary.
- Fixtures must not contain:
  - secrets (API keys, tokens)
  - sensitive locations requiring redaction
  - real personal data (PII)

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What fixture naming convention is preferred (kebab/snake/camel)? | TBD | TBD |
| Are fixtures validated against schemas in CI? | TBD | TBD |
| Do tests mock the graph adapter or run against ephemeral graph instances? | TBD | TBD |

### Future extensions
- Add schema validation hooks for any STAC/DCAT/PROV payload fixtures (if used in API responses).
- Add a fixture manifest/index file for quick discovery (optional).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Mock fixtures] --> B[Test runner]
  B --> C[GraphQL resolvers]
  C --> D[Contract assertions]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Mock payloads | JSON/YAML/TS/etc. | This directory | Lint + deterministic diff |

> Exact formats are **not confirmed in repo**. Prefer text-based formats that produce stable diffs.

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Resolver results | GraphQL response payload | test assertions | GraphQL schema + contract tests |

### Sensitivity & redaction
- Use synthetic identifiers (e.g., `person_001`, `place_ks_001`), not real names/addresses.
- If historical sources include sensitive sites, represent them at a generalized level (county/region), not precise coordinates.
- Never include credentials or environment-specific tokens in fixtures.

### Quality signals
- Fixtures are minimal: only include fields required by the test.
- Stable ordering for object keys where feasible (to minimize churn).
- Comments/README references explain why each fixture exists.

## 🌐 STAC, DCAT & PROV Alignment

If mocks include catalog/provenance payloads (e.g., resolver returns STAC Item references):
- Keep IDs stable and realistic (but synthetic).
- Ensure any referenced IDs are clearly marked as fixtures (not production identifiers).
- Optionally validate against schemas (if schema tooling exists in repo — **not confirmed in repo**).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| GraphQL resolvers | Business logic + orchestration | GraphQL schema |
| Dependency adapters | Graph/DB/services boundary | Injected clients or module mocks |
| Test fixtures (mocks) | Deterministic stubs | Loaded by tests |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| GraphQL schema | `src/server/graphql/` | Changes require tests + review |
| Fixture contracts | `__tests__/fixtures/` | Keep backward compatibility for shared fixtures |

### Extension points checklist (for future work)
- [ ] Add a `README.md` per subfolder (`context/`, `graph/`, `services/`) if ambiguity grows
- [ ] Add fixture schema validators (JSON Schema) for common payload types
- [ ] Add CI guardrails for secrets/PII detection in fixtures

## 🧠 Story Node & Focus Mode Integration

Some GraphQL endpoints may feed Story Nodes / Focus Mode via the API layer.
For such tests:
- Include provenance references in responses (IDs that map to catalog entities).
- Ensure tests never assert on uncited narrative content (no “hallucinated” strings).

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Fixtures contain no secrets/credentials (scan)
- [ ] Fixtures contain no real PII (scan/review)
- [ ] Tests pass locally and in CI
- [ ] If schema validation exists: STAC/DCAT/PROV fixtures validate

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run API test suite
# 2) run lint/format checks
# 3) run secret scanning (if configured)
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- If fixtures include culturally sensitive content, require historian/editor review (**not confirmed in repo**, but recommended).
- Any inclusion of real-world coordinates should be reviewed for sovereignty/sensitivity constraints.

### CARE / sovereignty considerations
- Treat fixture creation like publication: avoid disclosing restricted locations or sensitive cultural information.

### AI usage constraints
- Do not use AI to infer or “fill in” sensitive locations or identities in fixtures.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README for GraphQL test mocks fixtures | TBD |

