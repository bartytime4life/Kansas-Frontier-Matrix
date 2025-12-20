---
title: "Data Ops — Data Quality Checks — API"
path: "docs/data-ops/data-quality/checks/api/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:data-ops:data-quality:checks:api:readme:v1.0.0"
semantic_document_id: "kfm-data-ops-data-quality-checks-api-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data-ops:data-quality:checks:api:readme:v1.0.0"
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

# Data Ops — Data Quality Checks — API

## 📘 Overview

### Purpose
This README defines the **API-layer** data quality checks used to keep KFM’s API responses:
- contract-conformant (REST/GraphQL schemas + behavior),
- traceable (provenance links back to catalogs and sources),
- safe (sensitivity-aware exposure + redaction/generalization where required),
- stable (deterministic and backward-compatible for UI and Focus Mode consumers).

This document is **documentation + checklist**. If you are changing an endpoint contract, use the governed contract template referenced below.

### Scope
| In Scope | Out of Scope |
|---|---|
| API contract checks (REST/GraphQL) | ETL extraction/transform checks (see pipeline docs) |
| Response schema validation and error envelope consistency | Graph ontology changes and migrations |
| Provenance reference presence and integrity | UI rendering/regression tests |
| Access control, redaction/generalization expectations for sensitive fields | Performance tuning details beyond minimum budgets |

### Audience
- Primary: API developers, CI/QA maintainers, Data Ops maintainers
- Secondary: UI developers, Story/Focus Mode curators, catalog/graph maintainers

### Definitions
- Glossary link: `docs/glossary.md` (if present)
- Terms used in this doc:
  - **Contract test**: Test that validates an endpoint’s observable behavior against a documented contract.
  - **Provenance reference**: A stable identifier that links an API response back to STAC/DCAT/PROV assets or source documents.
  - **Generalization**: Reducing precision/detail to prevent unsafe disclosure (e.g., coarse location).
  - **Redaction**: Removing fields/attributes from responses based on sensitivity rules.

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Data Ops root | `docs/data-ops/README.md` | Data Ops | Parent index |
| Data Quality overview | `docs/data-ops/data-quality/README.md` | Data Ops | Parent index |
| Checks overview | `docs/data-ops/data-quality/checks/README.md` | Data Ops | Cross-check categories |
| API checks | `docs/data-ops/data-quality/checks/api/README.md` | Data Ops + API | This document |
| Master pipeline + invariants | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical order + constraints |
| API contract change template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Maintainers | Use for REST/GraphQL changes |
| Schemas | `schemas/` | Platform | OpenAPI/GraphQL/JSON schema locations (confirm exact paths) |
| API code | `src/server/` | API | Implementation location (confirm module layout) |
| Tests | `tests/` | API + QA | Contract, integration, and resolver tests |

### Definition of done
- [ ] Front-matter complete and `path` matches this file location
- [ ] “Confirmed” checks below have a clear enforcement location (CI job and/or test suite path)
- [ ] Every check has an owner and a remediation note
- [ ] Validation steps are listed and repeatable
- [ ] Governance and sovereignty considerations are explicitly stated for endpoints that expose sensitive content

## 🗂️ Directory Layout

### This document
- `path`: `docs/data-ops/data-quality/checks/api/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data Ops docs | `docs/data-ops/` | Operational docs for pipeline/quality |
| API checks docs | `docs/data-ops/data-quality/checks/api/` | API-specific check catalog and conventions |
| API implementation | `src/server/` | API routes/controllers/resolvers/middleware |
| Schemas | `schemas/` | OpenAPI/GraphQL/JSON schema, telemetry schemas |
| Tests | `tests/` | Contract tests, integration tests, schema lint |
| CI workflows | `.github/workflows/` | CI job definitions (confirm names) |

### Expected file tree for this sub-area
~~~text
📁 docs/
├── 📁 data-ops/
│   ├── 📄 README.md
│   └── 📁 data-quality/
│       ├── 📄 README.md
│       └── 📁 checks/
│           ├── 📄 README.md
│           └── 📁 api/
│               └── 📄 README.md
~~~

## 🧭 Context

### Why API data quality checks exist
In KFM, the API layer is the **contract boundary** between internal representations (catalogs + graph) and external consumers (UI, story rendering, Focus Mode). API quality checks prevent:
- breaking UI or downstream clients with silent contract drift,
- losing traceability required for provenance-led narratives,
- leaking sensitive attributes.

### Constraints and invariants
The following invariants must remain true for v12-aligned work:
- Preserve the canonical pipeline ordering: **ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The UI must not read the graph database directly; it consumes API contracts only.
- Contract changes require contract updates and tests (use the API Contract Extension template).

### Open questions to confirm in-repo
| Question | Why it matters | Where to confirm |
|---|---|---|
| Where is the canonical OpenAPI spec stored | Enables schema lint + contract verification | `schemas/` or `docs/` |
| Where is the GraphQL schema stored | Enables resolver/shape tests | `schemas/` or `src/server/` |
| What is the standard error envelope | Consistent client handling and retries | API docs / existing handlers |
| What is the required provenance payload shape | Ensures traceability for Focus Mode | API contract docs + story docs |
| What CI job names enforce these checks | Repeatable validation | `.github/workflows/` |

## 🗺️ Diagrams

### API quality gates in the KFM flow
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React + Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  subgraph Q[API Data Quality Checks]
    Q1[Contract tests\nREST/GraphQL]
    Q2[Schema lint\nOpenAPI/GraphQL/JSON]
    Q3[Provenance refs present\nSTAC/DCAT/PROV links]
    Q4[Sensitivity rules\nredaction/generalization]
    Q5[Stability\npagination/determinism]
  end

  Q1 -.enforced in CI.-> D
  Q2 -.enforced in CI.-> D
  Q3 -.verified in tests.-> D
  Q4 -.verified in tests.-> D
  Q5 -.verified in tests.-> D
~~~

## 📦 Data and Metadata

### Inputs checked at the API layer
| Input | Description | Source of truth |
|---|---|---|
| API contract definition | REST/GraphQL schema and documentation | `schemas/` / `docs/` (confirm) |
| Backend query results | Graph query outputs and derived joins | Graph layer |
| Catalog identifiers | STAC/DCAT/PROV IDs referenced by responses | `data/stac/`, `data/catalog/dcat/`, `data/prov/` |
| Sensitivity labels | Field/entity classification and governance tags | governance docs + data metadata |

### Outputs and artifacts
| Output | Where it lands | Used for |
|---|---|---|
| Contract test results | CI logs/artifacts | merge gating + regression control |
| Schema validation report | CI logs/artifacts | detect drift or invalid specs |
| Coverage summaries | CI logs/artifacts | track which endpoints are protected |
| Failure playbooks | docs (future) | remediation and triage |

### API check catalog
This section is a **checklist**. Items are grouped as:
- **Confirmed**: explicitly expected by canonical KFM docs.
- **Candidate**: recommended additions; confirm enforcement and update CI accordingly.

#### Confirmed checks
| Check | What it ensures | Enforcement | Owner | Remediation |
|---|---|---|---|---|
| Contract tests for REST and GraphQL | Endpoints behave as documented; changes don’t silently break clients | CI gate | API + QA | Update contract + tests together; version/deprecate if breaking |
| Docs and schema validation | Schemas and docs remain well-formed and consistent | CI gate | Platform | Fix lint/schema errors before merge |
| Provenance links in responses | Clients can trace results back to source catalogs and documents | Tests + review | API + Data Ops | Add/repair provenance references; prevent “floating” claims |

#### Candidate checks
| Check | What it ensures | Enforcement | Owner | Notes |
|---|---|---|---|---|
| Error envelope consistency | Stable client behavior on errors | Tests | API | Confirm standard structure in repo |
| Pagination determinism | Stable ordering and repeatable paging | Tests | API | Avoid nondeterministic ordering |
| Geometry validity | No invalid geometries; correct coordinate order | Tests | API | Particularly for map outputs |
| Range/type sanity | Detects wildly out-of-range values and wrong types | Tests | API | Depends on domain constraints |
| Backward compatibility scan | Detects breaking changes across versions | CI | Platform | Confirm versioning policy in repo |
| Sensitivity regression | Prevents accidental exposure of restricted fields | CI + review | Security + API | Requires explicit ruleset |

### Sensitivity considerations
If an endpoint includes fields that could be sensitive, the contract must document:
- authorization behavior,
- redaction/generalization behavior,
- logging/audit behavior.

Do not embed sensitive examples in this repository unless governance explicitly permits it.

## 🧾 STAC, DCAT, and PROV alignment

### Traceability expectation
API responses should be traceable to the KFM catalogs and lineage artifacts:
- **STAC**: for geospatial assets and their metadata (items/collections).
- **DCAT**: for dataset-level catalog records.
- **PROV**: for lineage from sources → derivations → products.

Field names for provenance references are **not standardized here**; use the API contract as the source of truth and document them consistently.

### Integrity checks for provenance references
- References must be stable identifiers, not fragile filenames.
- References must resolve to existing catalog entries in `data/stac/`, `data/catalog/dcat/`, and `data/prov/` where applicable.
- Derived outputs should link to the generating PROV activity (when applicable).

## 🧱 Architecture

### Components involved in API checks
| Component | Role | Notes |
|---|---|---|
| API router/controllers/resolvers | Generates contract payloads | `src/server/` |
| Redaction/generalization middleware | Applies sensitivity rules | confirm implementation location |
| Contract schemas | Defines the contract to test against | `schemas/` (confirm) |
| Test harness | Executes contract and integration tests | `tests/` |

### Contract boundaries
- API is the only supported boundary for UI consumption.
- If the graph schema changes, API contracts must remain stable or versioned.

## ✅ Operations

### When adding a new endpoint
- Add or extend the API contract definition.
- Add contract tests for the new endpoint.
- Ensure responses include required provenance references.
- Document sensitivity behavior if applicable.

### When changing an existing endpoint
Use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` and ensure:
- backward compatibility is explicitly stated,
- deprecations are documented,
- contract tests are updated in the same change.

## 🧪 Testing and Validation

### Local validation
TBD — confirm the repo’s standard commands. Add concrete commands once the test harness is confirmed.

~~~bash
# Example placeholders — replace with repo-confirmed commands
# make test-api
# make lint-api
# make schema-validate
~~~

### CI validation
TBD — link to the specific workflow/job names once confirmed in `.github/workflows/`.

## ⚠️ Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Silent contract drift | UI breaks or misrenders data | Enforce contract tests as CI gate |
| Missing provenance references | Focus Mode narratives become untraceable | Require provenance checks for relevant endpoints |
| Sensitive field leakage | Governance and trust violation | Document and test redaction/generalization rules |
| Non-deterministic pagination | Unstable results across clients | Enforce deterministic ordering + pagination tests |

## 📎 Appendix

### Related governed templates
- Universal governed doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

### Next edits recommended
- Replace TBDs with repo-confirmed schema/test paths and CI job names.
- Promote “Candidate checks” to “Confirmed” only after CI enforcement is in place.
---


