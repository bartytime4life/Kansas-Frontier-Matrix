---
title: "KFM CI Toolkit — tools/ci"
path: "tools/ci/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:tools:ci:readme:v1.0.0"
semantic_document_id: "kfm-tools-ci-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:ci:readme:v1.0.0"
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

# KFM CI Toolkit — tools/ci

## 📘 Overview

### Purpose

- Define how KFM CI “gates” are expected to run locally and in CI, and how they map to the canonical KFM pipeline ordering.
- Provide a single place to document CI entrypoints, failure modes, and how to add or modify checks without breaking contracts.

### Scope

| In Scope | Out of Scope |
|---|---|
| CI gate definitions and local reproduction patterns | CI provider-specific implementation details (e.g., exact GitHub Actions YAML), unless mirrored here by reference |
| Guidance on where CI scripts/config should live in-repo | Writing/implementing the CI scripts themselves (unless added under `tools/ci/`) |
| Mapping checks to KFM pipeline stages and contracts | Changing governance/security policies (belongs in governance/security docs) |

### Audience

- Primary: KFM maintainers and contributors who run checks locally or debug CI.
- Secondary: reviewers who need to understand what a “green build” means for v12 readiness.

### Definitions

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **CI gate**: a required automated check that must pass before merge/release.
  - **Markdown protocol validation**: validation that markdown docs adhere to KFM-MDP (front-matter, structure, links, etc.).
  - **Schema validation**: validation that JSON artifacts (STAC/DCAT/PROV/telemetry) conform to schemas in `schemas/`.
  - **Contract tests**: tests ensuring API behavior matches OpenAPI/GraphQL contracts and remains backward compatible or properly versioned.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline ordering + minimum CI gates |
| Markdown Protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | TBD | Defines markdown structure requirements (not confirmed in repo) |
| Schemas | `schemas/` | TBD | JSON Schema bundles for validation |
| Story Nodes | `docs/reports/story_nodes/` | TBD | Validated as governed docs (paths may vary; not confirmed in repo) |
| CI wrappers | `tools/ci/` | TBD | This directory hosts local entrypoints/wrappers (scripts not confirmed in repo) |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] CI gates listed match Master Guide v12 requirements
- [ ] Local reproduction steps are provided (even if placeholders) and clearly labeled
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `tools/ci/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Graph | `src/graph/` | Graph build + ontology bindings |
| APIs | `src/server/` or `src/api/` | Contracted access layer (REST/GraphQL) *(path not confirmed in repo)* |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area

~~~text
tools/
└── ci/
    └── README.md

# Target (recommended) expansion (examples — not confirmed in repo):
# ├── run_all.(sh|py)
# ├── validate_markdown.(sh|py)
# ├── validate_schemas.(sh|py)
# ├── test_graph.(sh|py)
# ├── test_api_contracts.(sh|py)
# ├── check_ui_registry.(sh|py)
# └── scan_security.(sh|py)
~~~

## 🧭 Context

### Background

KFM treats documentation, schemas, catalogs, graph semantics, and API/UI contracts as *governed artifacts*. CI is responsible for preventing drift between these contracts and the implementation and for blocking changes that break provenance rules, schema validity, or security/sovereignty constraints.

### Assumptions

- CI should be deterministic and repeatable (same inputs → same outputs).
- CI gates should be runnable locally via repository scripts/wrappers to reduce “works in CI only” debugging.
- Validation is a first-class part of KFM’s workflow (docs and metadata are “contracts,” not informal notes).

### Constraints / invariants

- Canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- UI consumes contracts via APIs (no direct graph dependency).
- CI gates must cover both *structure* (schemas, contracts) and *governance* (sensitivity, sovereignty, prohibited AI actions) where applicable.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What are the canonical local entrypoint commands for each gate (Make targets / scripts)? | TBD | TBD |
| Where are CI workflow definitions stored (`.github/workflows/` expected; not confirmed in repo)? | TBD | TBD |
| Are there standardized telemetry schemas for CI runs (e.g., `schemas/telemetry/ci_run.json`)? | TBD | TBD |

### Future extensions

- Add a single “one command” local runner that mirrors CI exactly (containerized or pinned toolchain).
- Add machine-readable CI result outputs (JUnit/JSON) to enable dashboards and long-term regression tracking.
- Add explicit Story Node publish gates (draft vs published) if not already enforced by markdown protocol validation.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[Repo change] --> B[CI gates]
  B --> C[ETL/Catalog validations]
  B --> D[Graph integrity]
  B --> E[API contract tests]
  B --> F[UI schema checks]
  B --> G[Security + sovereignty scans]
  C --> H[Merge allowed]
  D --> H
  E --> H
  F --> H
  G --> H
~~~

### Optional: sequence diagram (debugging loop)

~~~mermaid
sequenceDiagram
  participant Dev as Developer
  participant Local as Local runner (tools/ci)
  participant CI as CI pipeline
  Dev->>Local: Run gate(s)
  Local-->>Dev: Pass/fail + logs
  Dev->>CI: Open PR
  CI-->>Dev: Pass/fail + artifacts
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Markdown docs | `.md` | `docs/`, `tools/`, etc. | Markdown protocol validation |
| Schemas | JSON Schema / SHACL (if used) | `schemas/` | Schema lint + validation |
| Catalog outputs | JSON (STAC/DCAT/PROV) | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | JSON schema validation |
| Code | language-specific | `src/`, `web/` | Unit/integration tests + contract tests |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI logs | text/JSON | CI provider artifacts | TBD |
| Validation reports | JSON/JUnit | CI artifacts or `mcp/runs/` | TBD |
| Failing diff context | text | CI logs | N/A |

### Sensitivity & redaction

- Any checks that handle sensitive information must:
  - avoid printing secrets/PII in logs,
  - follow redaction/generalization rules for restricted locations,
  - enforce that prohibited AI actions are not implied or embedded in artifacts.

### Quality signals

- No schema-invalid STAC/DCAT/PROV artifacts.
- No broken internal references (links, IDs, referenced entities/evidence).
- Contract tests pass for APIs and UI schema registries.
- Security scans report no secret leakage and no policy violations (where applicable).

## 🌐 STAC, DCAT & PROV Alignment

### Provenance requirements

- CI should ensure:
  - STAC/DCAT/PROV artifacts validate against the repository schema profiles.
  - Generated artifacts and transformations are traceable via run IDs / activity IDs where applicable.

### Versioning

- Changes to schema/contract artifacts should follow semver + changelog expectations.
- When catalogs are regenerated, outputs should be diffable and deterministic (avoid nondeterministic ordering, timestamps without reason, etc.).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | configs + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas/contracts | `src/server/` + docs | Contract tests required |
| Layer registry | `web/**/layers/**` | Schema-validated *(path pattern not confirmed in repo)* |

### Extension points checklist (for future work)

- [ ] Add/modify a CI gate → update this README + CI workflow definitions
- [ ] Add new schemas → ensure validators run in CI
- [ ] Add new API endpoint → add/extend contract tests
- [ ] Add new UI layer registry entry → ensure schema validation + provenance rules

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- CI enforces that Story Nodes remain provenance-linked and structurally valid as governed docs.
- Any predictive content (if present) must be opt-in, explicitly labeled, and include uncertainty metadata.

### Provenance-linked narrative rule

- Every claim must trace to a dataset / record / asset ID.
- Any narrative surfaced to Focus Mode must be grounded in catalog/graph references (no unsourced narrative).

## 🧪 Validation & CI/CD

### Minimum CI gates for “v12-ready” contributions

- Markdown protocol validation
- JSON schema validation (STAC/DCAT/telemetry)
- Graph integrity tests
- API contract tests
- UI layer registry schema checks
- Security + sovereignty scanning gates (where applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands/scripts (not confirmed in repo)

# 1) Run all gates locally
./tools/ci/run_all.sh

# 2) Markdown protocol validation
./tools/ci/validate_markdown.sh

# 3) Schema validation (STAC/DCAT/PROV/telemetry)
./tools/ci/validate_schemas.sh

# 4) Graph integrity tests
./tools/ci/test_graph.sh

# 5) API contract tests
./tools/ci/test_api_contracts.sh

# 6) UI registry schema checks
./tools/ci/check_ui_registry.sh

# 7) Security + sovereignty scanning
./tools/ci/scan_security.sh
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| TBD | CI runner | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- CI changes that alter security scanning, redaction behavior, or governance enforcement **require human review**.
- CI changes that affect public-facing endpoints, sensitive layers, or story publication paths **require governance review**.

### CARE / sovereignty considerations

- CI must prevent accidental publication of restricted locations or culturally sensitive knowledge.
- Any new checks that touch sensitive data must document:
  - redaction/generalization behavior,
  - log/audit behavior,
  - approval requirements.

### AI usage constraints

- This document’s AI permissions/prohibitions must remain consistent with project governance.
- CI should fail if artifacts imply prohibited AI transformations (e.g., inferring sensitive locations).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial `tools/ci` README scaffold | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`