---
title: "Tests — Unit"
path: "tests/unit/README.md"
version: "v1.0.0"
last_updated: "2025-12-18"
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

doc_uuid: "urn:kfm:doc:tests:unit-readme:v1.0.0"
semantic_document_id: "kfm-tests-unit-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tests:unit-readme:v1.0.0"
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

# Tests — Unit

## 📘 Overview

### Purpose
This folder contains **unit tests**: fast, deterministic tests for small units of behavior (functions, modules, schema helpers). Unit tests are intended to run on every PR/commit as part of CI to keep the canonical pipeline stable.

### Scope

| In Scope | Out of Scope |
|---|---|
| Pure logic helpers (parsers, transforms, validators) | End-to-end pipeline rebuilds (`make all`) |
| Schema and contract checks on *small* fixtures | Long-running ETL jobs / network downloads |
| Redaction/generalization rules for sensitive outputs | Full graph ingestion + UI smoke tests |
| Determinism/regression on known inputs | Performance benchmarks (unless explicitly added) |

### Audience
- Primary: contributors adding/changing code in `src/`, `schemas/`, `tools/`
- Secondary: reviewers and CI maintainers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: unit test, fixture, contract test, determinism, provenance

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Test entrypoint | `Makefile` (target: `make test`) | TBD | Preferred top-level invocation if present |
| Pipeline invariants | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical stage ordering must remain intact |
| Schemas | `schemas/` | TBD | JSON Schemas, telemetry schemas, etc. |
| Source code | `src/` | TBD | Pipelines, graph tooling, API layer, etc. |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Test expectations match current contracts (schemas, APIs, ontology bindings)
- [ ] Determinism rules documented (seeds, clocks, ordering)
- [ ] Sensitivity and redaction expectations noted (no leaking restricted locations)

## 🗂️ Directory Layout

### This document
- `path`: `tests/unit/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Unit tests | `tests/unit/` | Fast, deterministic tests for small behaviors |
| Integration tests | `tests/` (varies) | Slower, cross-component tests (if present) |
| Pipelines | `src/pipelines/` | ETL + transforms |
| Graph | `src/graph/` | Ontology bindings, ingest helpers |
| APIs | `src/server/` | REST/GraphQL access layer |
| Schemas | `schemas/` | Contract and validation schemas |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
~~~text
🧪 tests/
├── 🧭 README.md
└── ✅ unit/
    ├── 📄 README.md
    ├── 🧩 <module-or-domain>/
    │   ├── ✅ <test files...>
    │   └── 🧰 fixtures/            # optional; keep tiny and non-sensitive
    └── 🧰 fixtures/                # optional; shared unit fixtures
~~~

## 🧭 Context

### Background
KFM’s pipeline is deliberately staged and contract-governed. Unit tests are the “shift-left” guardrail: they catch broken transforms, schema drift, and accidental sensitivity leaks early—before integration and release workflows.

### Assumptions
- Tests should be runnable locally and in CI.
- Unit tests should avoid requiring external services (databases, network), unless explicitly mocked.

### Constraints / invariants
- The canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The frontend stays behind APIs (no direct graph dependency).
- No unit test should introduce or expose sensitive coordinates or restricted identifiers in logs or fixtures.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Primary test runner(s) and naming conventions (e.g., Python vs Node) | TBD | TBD |
| Standard location for fixtures in this repo (`tests/unit/fixtures/` vs per-module) | TBD | TBD |
| Required report formats in CI (JUnit XML, coverage artifacts, etc.) | TBD | TBD |

> If any of the above is unknown during implementation, mark it as **not confirmed in repo** and keep tests framework-agnostic.

## 🗺️ Diagrams

### Unit-test fit within the pipeline
~~~mermaid
flowchart LR
  A[Code / Schemas change] --> B[Unit tests (this folder)]
  B --> C[Catalog + Graph + API integration checks]
  C --> D[Release / Deploy]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source modules | code | `src/**` | Lint + unit assertions |
| Schemas | JSON | `schemas/**` | Schema validation tests (small fixtures) |
| Tiny fixtures | small files | `tests/unit/**/fixtures` (if used) | Size limits, no sensitive data |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Pass/fail | CI logs | CI artifact | N/A |
| Optional coverage | tool-specific | CI artifact | not confirmed in repo |

### Sensitivity & redaction
- Never commit fixtures containing restricted site coordinates or sensitive identifiers.
- Prefer synthetic or heavily generalized fixtures where location is involved.

## 🌐 STAC, DCAT & PROV Alignment

Unit tests may validate:
- **STAC**: required fields exist and invariants hold for generated items (when tested via fixtures).
- **DCAT**: mapping outputs are present and minimally well-formed (where applicable).
- **PROV-O**: lineage blocks include expected relationships (e.g., generated-by / used / derived-from) at the unit level.

## 🧱 Architecture

### How to run
From repo root, prefer the Makefile target if available:
~~~bash
make test
~~~

If a narrower target exists (e.g., `make test-unit`), use it — **not confirmed in repo**.

### Test design rules (unit)
- Deterministic: fixed seeds, stable ordering, no wall-clock dependence (or clock injected/mocked).
- Hermetic: no network calls; no real DB required; keep I/O minimal.
- Small fixtures: keep runtime fast and repo size reasonable.
- Clear failures: assert the contract you care about (schema, invariants, redaction behavior).

## 🧪 Validation & CI/CD

### Validation checklist
- [ ] Tests run locally and in CI with the same result (deterministic)
- [ ] No network access required for unit tests
- [ ] Any schema fixtures are minimal and validated
- [ ] No sensitive data in fixtures, logs, or snapshots
- [ ] New/changed behavior has at least one unit test

## ⚖ FAIR+CARE & Governance

### Governance approvals required (if any)
- FAIR+CARE council review: no (unless tests introduce sensitive domain data)
- Security council review: no (unless fixtures/logging touch security-sensitive content)
- Historian/editor review: no

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial unit test README | TBD |
