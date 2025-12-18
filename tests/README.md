---
title: "KFM Tests — README"
path: "tests/README.md"
version: "v1.0.0"
last_updated: "2025-12-18"
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
- Define **how automated tests are organized, written, and run** in KFM.
- Ensure the KFM pipeline remains **deterministic, reproducible, and contract-safe** across:
  ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode.

### Scope
| In Scope | Out of Scope |
|---|---|
| Unit/integration/contract tests for KFM pipeline stages, schema validation, and contract protection. | Manual QA checklists, load testing at scale, security penetration testing, or vendor-specific infra tests (unless explicitly added + governed). |

### Audience
- Primary: KFM developers, data engineers, and maintainers.
- Secondary: Contributors adding new datasets, catalog validators, graph constraints, API endpoints, or UI features.

### Definitions (link to glossary)
- Link: `../docs/glossary.md`
- Terms used in this doc: unit test, integration test, contract test, fixture, golden file/snapshot, schema validation, STAC, DCAT, PROV(-O), run ID, provenance.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Test directory | `tests/` | Maintainers | This README governs conventions + layout. |
| Test runner entrypoint | `Makefile` (repo root) | Maintainers | Expected to include a `make test` target. (Confirm in repo.) |
| CI workflows | `.github/` | Maintainers | CI should invoke tests and schema validation gates. |
| Schemas | `schemas/` | Maintainers | STAC/DCAT/PROV + system schemas used by validators. |
| Pipeline code | `src/pipelines/` | Data engineering | ETL/transforms + catalog build + graph build. |
| API code | `src/server/` | Backend | REST/GraphQL contracts + handlers. (Path may vary.) |
| Web UI | `web/` | Frontend | UI tests/smoke checks as applicable. |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Test organization aligns with the canonical pipeline ordering (ETL → catalogs → graph → APIs → UI → narrative)

## 🗂️ Directory Layout

### This document
- `path`: `tests/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac/reports per domain (inputs/outputs tested) |
| Documentation | `docs/` | Master guide, standards, templates, system docs |
| Graph | `src/graph/` + `docs/graph/` | Ontology, constraints, migrations (tested) |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | ETL + transforms + catalog + graph build (tested) |
| Schemas | `schemas/` | STAC/DCAT/PROV + validators + contract schemas (tested) |
| Frontend | `web/` + `docs/design/` | Map layers + Focus Mode UX (tested as applicable) |
| CI | `.github/` | Workflow definitions + gates |

### Expected file tree for this sub-area
~~~text
📁 tests/
├─ 📄 README.md
├─ 📁 unit/                       # Fast, isolated tests (no network; minimal IO)
│  ├─ 📁 pipelines/               # Transform + normalization unit tests
│  ├─ 📁 catalogs/                # STAC/DCAT/PROV helpers + validators
│  ├─ 📁 graph/                   # Ontology helpers + constraint logic
│  ├─ 📁 api/                     # Pure handler/serializer logic (no server)
│  └─ 📁 web/                     # UI utilities (if applicable)
├─ 📁 integration/                # Cross-module tests following pipeline ordering
│  ├─ 📁 etl_to_catalogs/
│  ├─ 📁 catalogs_to_graph/
│  └─ 📁 api_to_ui/
├─ 📁 contract/                   # Machine-checked interface guarantees
│  ├─ 📁 stac/                    # STAC JSON schema conformance
│  ├─ 📁 dcat/                    # DCAT mapping conformance
│  ├─ 📁 prov/                    # PROV bundle conformance
│  ├─ 📁 openapi/                 # REST contract checks (if applicable)
│  └─ 📁 graphql/                 # GraphQL schema + resolver checks (if applicable)
├─ 📁 fixtures/                   # Small, non-sensitive test inputs
│  ├─ 📁 data/
│  ├─ 📁 stac/
│  ├─ 📁 dcat/
│  └─ 📁 prov/
└─ 📁 snapshots/                  # Golden outputs (small, stable, reviewed)
   └─ 📄 README.md
~~~

> Note: Subfolders above are the **recommended** structure. If the repo already uses different names, align this tree to the implemented layout rather than forcing churn.

## 🧭 Context

### Background
KFM is a multi-stage system with governed metadata and narrative surfaces. Tests exist to:
- Prevent regressions in the canonical pipeline ordering and contracts.
- Ensure catalog artifacts (STAC/DCAT/PROV) are **machine-valid** before graph/API/UI consumption.
- Keep narrative experiences (Story Nodes / Focus Mode) evidence-led and provenance-linked.

### Assumptions
- Tests can be run locally and in CI using deterministic settings (fixed seeds where relevant; pinned validators where required).
- The repo provides a single “developer entrypoint” for tests (commonly `make test`). If not, add one and document it here. **(Not confirmed in repo.)**

### Constraints / invariants
- Pipeline ordering is non-negotiable: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- Frontend stays behind APIs (no direct graph access).
- No secrets, credentials, or sensitive locations in fixtures or snapshots.
- Tests should be deterministic: avoid time-dependent behavior, randomized ordering, non-pinned external services, or network IO unless explicitly mocked.

### Open questions
| Question | Owner | Status | Notes |
|---|---|---|---|
| Canonical test runner(s) (pytest/jest/other)? | Maintainers | TBD | Not confirmed in repo; document once validated. |
| How are schema validators invoked (CLI vs library)? | Maintainers | TBD | Pin versions for deterministic CI. |
| Do we maintain golden snapshots for catalog/graph/API outputs? | Maintainers | TBD | Define update workflow if adopted. |
| Are UI tests executed in CI (smoke vs e2e)? | Frontend | TBD | Keep minimal and deterministic. |

### Future extensions
- Property-based testing for key transforms (with fixed seeds).
- Ephemeral integration environments (e.g., temporary graph instance) for graph ingestion tests.
- Coverage + quality dashboards tied to telemetry governance (if adopted).

## 🗺️ Diagrams

### System/dataflow diagram
~~~mermaid
flowchart LR
  subgraph A["Pipeline (canonical ordering)"]
    A1["ETL + Normalization"] --> A2["STAC/DCAT/PROV Catalogs"]
    A2 --> A3["Neo4j Graph"]
    A3 --> A4["API Layer"]
    A4 --> A5["React/Map UI"]
    A5 --> A6["Story Nodes"]
    A6 --> A7["Focus Mode"]
  end

  subgraph T["Tests (mapped to stages)"]
    T1["Unit tests"] --> T2["Integration tests"]
    T2 --> T3["Contract tests (schemas + APIs)"]
  end

  T1 -. protects .-> A1
  T3 -. validates .-> A2
  T2 -. verifies .-> A3
  T3 -. enforces .-> A4
  T2 -. smokes .-> A5
~~~

### Optional sequence diagram
~~~mermaid
sequenceDiagram
  participant Dev as Developer
  participant CI as CI Runner
  participant Val as Validators
  participant API as API Layer
  participant G as Graph

  Dev->>CI: Push / PR
  CI->>Val: Schema validation (STAC/DCAT/PROV)
  CI->>CI: Unit + integration tests
  CI->>API: Contract tests (REST/GraphQL) if applicable
  API->>G: Query (with redaction rules)
  G-->>API: Result + provenance refs
  API-->>CI: Contracted payload
~~~

## 📦 Data & Metadata

### Inputs
| Input | Source | Sensitivity | Notes |
|---|---|---|---|
| Test fixtures | `tests/fixtures/` | public | Must be minimal + non-sensitive; no real private site coordinates. |
| Schema definitions | `schemas/` | public | Used for validators + contract tests. |
| Sample catalogs | `tests/fixtures/stac|dcat|prov` | public | Keep small; stable IDs. |

### Outputs
| Output | Destination | Sensitivity | Notes |
|---|---|---|---|
| Test reports | CI logs / artifacts | public | Store only what is needed; avoid leaking env details. |
| Snapshots/golden files | `tests/snapshots/` | public | Review on change; keep deterministic. |
| Validation results | CI logs | public | Fail fast on schema/contract breaks. |

### Sensitivity & redaction
- Do not commit fixtures containing:
  - precise locations for sensitive or restricted sites,
  - personally identifying information,
  - credentials/tokens or internal endpoints.
- If a domain requires sensitive geometry testing, use:
  - generalized geometry (coarsened polygons / blurred points),
  - synthetic coordinates,
  - or hashed/abstracted identifiers.

### Quality signals
- Tests pass locally and in CI with the same commands.
- Schema validators pass for all generated catalogs.
- Integration tests verify stage-to-stage handoffs (ETL→Catalogs→Graph→API).
- Snapshots are stable and changes are intentional + reviewed.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Tests should validate that generated STAC Items/Collections:
  - match the required STAC profile/version,
  - contain stable IDs,
  - include required spatial/temporal extents and asset links (as applicable).

### DCAT
- Tests should validate that DCAT dataset views:
  - include minimum required fields (title/description/license/keywords),
  - remain consistent with STAC identifiers and lineage.

### PROV-O
- Tests should validate that provenance bundles:
  - identify activities (run IDs) and used/generated entities,
  - can be traced from outputs back to inputs,
  - preserve revision/version linkages when datasets are updated.

### Versioning
- If schema/contract changes are introduced:
  - update contract tests and snapshots,
  - preserve backward compatibility or bump versions as governed,
  - ensure graph mirrors dataset version lineage where applicable.

## 🔌 Extension points checklist (for future work)
- [ ] Additional domain test suites mapped to each domain under `data/<domain>/`
- [ ] Expanded catalog validators (extensions, profiles, link integrity)
- [ ] Additional graph constraints + migrations test harness
- [ ] API contract tests expanded (OpenAPI/GraphQL) as endpoints evolve
- [ ] Story Node validation tests (schema + provenance link checks)

## 🧠 Story Node & Focus Mode Integration
- Tests that touch narrative outputs must enforce:
  - No unsourced narrative: every factual claim maps to a cited dataset/document ID.
  - Provenance refs are present and resolvable (STAC/DCAT/PROV and/or graph lineage).
  - If predictions/uncertainty are surfaced, they are clearly labeled and optional.
  - Sensitivity rules are honored (no “inferred sensitive locations” behavior).

## 🧪 Validation & CI/CD
- [ ] Unit tests updated/added for changed modules
- [ ] Integration tests updated/added for changed cross-stage handoffs
- [ ] Schema validation passes (STAC/DCAT/PROV)
- [ ] Contract tests pass (if API touched)
- [ ] Documentation updated (this README and any subsystem docs)

**Recommended local commands (adjust to your repo tooling):**
~~~bash
# Run the full test suite
make test

# (Optional) Run only unit tests
make test-unit

# (Optional) Run schema validators for catalogs
make validate-catalogs
~~~

> If your Makefile does not expose these targets, update it (or document the correct commands here).
> The repo documentation expects `make test` to run tests. (Confirm current Makefile targets before relying on this.)

## ⚖ FAIR+CARE & Governance
- Required approvals/review:
  - Changes impacting schemas, contracts, or governance gates should be reviewed by maintainers.
  - Changes impacting narrative artifacts should follow Story Node governance and evidence requirements.
- CARE/sovereignty:
  - Do not add fixtures that reveal culturally sensitive sites or restricted locations.
  - Follow `docs/governance/SOVEREIGNTY.md` and related guidance.
- Ethics:
  - Avoid any workflow that encourages “infer sensitive locations” behavior; such inference is prohibited for AI transforms.

## 🕰️ Version History
| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial governed tests README (layout + conventions). | TBD |

## ✅ Footer refs
- Master guide (pipeline + invariants): `../docs/MASTER_GUIDE_v12.md`
- Standards: `../docs/standards/`
- Templates: `../docs/templates/`
- Governance root: `../docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `../docs/governance/ETHICS.md`
- Sovereignty: `../docs/governance/SOVEREIGNTY.md`
- Security: `../.github/SECURITY.md` and/or `../docs/security/` (as applicable)
