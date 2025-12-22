---
title: "KFM Dev Fixtures — README"
path: "tools/dev/fixtures/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

doc_uuid: "urn:kfm:doc:tools:dev-fixtures-readme:v1.0.0"
semantic_document_id: "kfm-tools-dev-fixtures-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:dev-fixtures-readme:v1.0.0"
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

# KFM Dev Fixtures — README

## 📘 Overview

### Purpose

This directory holds **development/test fixtures**: small, curated inputs and “golden” expected outputs used to validate KFM behavior across the canonical pipeline (**ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**).

Fixtures exist to make tests **deterministic, replayable, and reviewable** without relying on external services or large production datasets.

### Scope

| In Scope | Out of Scope |
|---|---|
| Minimal sample datasets and records used by unit/integration tests | Production datasets or anything required for production runtime |
| Golden outputs (e.g., expected STAC Item JSON, expected DCAT JSON-LD, expected PROV bundle) | Secrets, credentials, `.env`, API keys, tokens |
| Small graph ingest samples (e.g., import CSV snippets, minimal Cypher migrations for tests) | Full Neo4j dumps / exports (unless explicitly approved; **not confirmed in repo**) |
| Sample API responses used for contract tests (REST/GraphQL) | Live network snapshots that can rot without version pinning |
| UI config or registry samples for local dev/demo | Any “shadow” canonical configuration that competes with `schemas/` or API-layer contracts |

### Audience

- Primary: KFM developers writing/maintaining pipelines, validators, graph ingest, API contracts, and UI.
- Secondary: reviewers/curators validating correctness, provenance, and governance; CI maintainers.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc include: **fixture**, **golden file**, **contract artifact**, **evidence artifact**, **provenance**, **redaction/generalization**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline ordering + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Governs structure + required sections |
| API contract template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | KFM Core | Use when fixture updates require API contract changes |
| Fixtures root | `tools/dev/fixtures/` | Dev Team | This folder |
| Tests root | `tests/` | Dev Team | Prefer tests consuming fixtures from here |
| Schemas | `schemas/` | Dev Team | Validators for STAC/DCAT/PROV/UI/etc |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Clear distinction between **fixture** vs **canonical artifact**
- [ ] Conventions documented for naming, structure, provenance, and sensitivity
- [ ] Validation steps listed and repeatable (even if commands are “fill in”)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `tools/dev/fixtures/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs (canonical data lifecycle) |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Canonical STAC/DCAT/PROV outputs (not fixtures) |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog builders |
| Graph | `src/graph/` | Ontology bindings, migrations, ingest code |
| API boundary | `src/server/` | Contracted access layer (REST/GraphQL) |
| Frontend | `web/` | React + map UI + Focus Mode UI |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published story artifacts (canonical narratives) |
| Tests | `tests/` | Unit/integration tests that SHOULD consume fixtures |
| Dev tooling | `tools/` | Developer utilities (this folder lives under `tools/`) |

### Expected file tree for this sub-area

This is the **recommended** structure for fixture packs. If your repo currently differs, treat this as the target layout and migrate incrementally.

~~~text
📁 tools/
└── 📁 dev/
    └── 📁 fixtures/
        ├── 📄 README.md
        ├── 📁 packs/
        │   ├── 📁 etl__<pack_slug>/
        │   │   ├── 📄 manifest.json
        │   │   ├── 📁 input/
        │   │   └── 📁 expected/
        │   ├── 📁 catalogs__<pack_slug>/
        │   │   ├── 📄 manifest.json
        │   │   ├── 📁 stac/
        │   │   ├── 📁 dcat/
        │   │   └── 📁 prov/
        │   ├── 📁 graph__<pack_slug>/
        │   │   ├── 📄 manifest.json
        │   │   ├── 📁 import_csv/
        │   │   └── 📁 cypher/
        │   ├── 📁 api__<pack_slug>/
        │   │   ├── 📄 manifest.json
        │   │   ├── 📁 requests/
        │   │   └── 📁 responses/
        │   └── 📁 ui__<pack_slug>/
        │       ├── 📄 manifest.json
        │       └── 📁 registry/
        └── 📁 _scratch/                      # Optional local-only workspace (should be gitignored)
~~~

## 🧭 Context

### Background

KFM is contract-driven and provenance-first. Tests that depend on external networks, volatile upstream sources, or large datasets tend to become flaky and unreviewable. Fixtures provide:

- **Determinism:** stable files + stable ordering
- **Speed:** small payloads
- **Auditability:** easy review in PRs
- **Reproducibility:** “same input → same output” across machines

### Assumptions

- Fixtures are consumed by tests in `tests/` (exact harness/tools are **not confirmed in repo**).
- Some fixtures may represent outputs of governed standards (STAC/DCAT/PROV), and therefore should be schema-validated where possible.
- Fixtures do **not** replace canonical outputs under `data/**`; they only support development and tests.

### Constraints / invariants

- The canonical ordering **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode** is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Fixtures must not introduce “shadow canon” (i.e., do not treat fixtures as authoritative outputs).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we standardize a JSON Schema for `manifest.json` in fixture packs? | TBD | TBD |
| Do we add a CI gate that scans fixtures for PII/secrets? | TBD | TBD |
| Do we enforce max fixture size (bytes) and/or max count per PR? | TBD | TBD |

### Future extensions

- Add a fixture “pack” linter/validator in `tools/dev/` (not confirmed in repo).
- Add golden snapshot testing for UI registry and API responses (not confirmed in repo).
- Add a domain pack scaffolder that emits a minimal vertical slice fixture set.

## 🗺️ Diagrams

### How fixtures relate to the canonical pipeline

~~~mermaid
flowchart LR
  subgraph FixturePacks[tools/dev/fixtures/packs/*]
    F1[ETL inputs] --> F2[Catalog golden outputs]
    F2 --> F3[Graph ingest samples]
    F3 --> F4[API contract fixtures]
    F4 --> F5[UI registry fixtures]
  end

  subgraph CanonicalPipeline[Canonical Pipeline]
    A[ETL] --> B[STAC/DCAT/PROV Catalogs]
    B --> C[Neo4j Graph]
    C --> D[APIs]
    D --> E[React/Map UI]
    E --> S[Story Nodes]
    S --> M[Focus Mode]
  end

  FixturePacks --> T[tests/]
  T --> CanonicalPipeline
~~~

### Optional: sequence diagram (golden contract test)

~~~mermaid
sequenceDiagram
  participant Test as Test Runner
  participant API as API Layer (src/server/)
  participant Graph as Graph Layer (src/graph/)
  Test->>API: Request (from fixture requests/)
  API->>Graph: Query (with redaction rules)
  Graph-->>API: Result + provenance refs
  API-->>Test: Contracted response
  Test->>Test: Compare with golden response fixture
~~~

## 📦 Data & Metadata

### Fixture lifecycle (recommended)

Fixtures can mirror the canonical lifecycle but are **not** the canonical lifecycle.

- Canonical lifecycle: `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (+ reports)
- Fixture lifecycle (recommended):
  - `tools/dev/fixtures/packs/*/input/` (minimal samples)
  - `tools/dev/fixtures/packs/*/expected/` (goldens / snapshots)
  - `manifest.json` describing origin + license + sensitivity

### `manifest.json` (recommended fields)

This manifest is recommended for each pack; if not used today, add it when you touch the pack.

- `id`: stable pack id (e.g., `catalogs__kansas_counties_min_v1`)
- `description`: one sentence
- `stage_coverage`: e.g., `["etl","stac","dcat","prov"]`
- `source`: where the sample came from (dataset id, URL, or “synthetic”)
- `license`: license identifier and/or pointer
- `sensitivity`: `public|restricted|redacted`
- `notes`: anything reviewers should know
- `expected_outputs`: list of key golden files
- `hashes`: optional mapping of filename → sha256

## 🌐 STAC, DCAT & PROV Alignment

If a fixture pack includes catalog artifacts (STAC/DCAT/PROV), it must be treated as a **contract artifact**:

- Keep IDs stable.
- Keep JSON deterministic (sorting, stable arrays where applicable).
- Prefer “minimal valid” objects that still exercise the rules.

Recommended consistency checks for catalog fixtures:

- STAC Items reference existing Collections (if included).
- DCAT dataset identifiers match the dataset/stage context.
- PROV activity/run IDs are consistent within the pack.

## 🧱 Architecture

### Subsystem contracts (fixture expectations)

| Subsystem | Fixture contents | “Do not break” rule |
|---|---|---|
| ETL | minimal raw-ish input + expected normalized output | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV goldens | machine-validatable |
| Graph | minimal import CSVs / Cypher snippets | stable labels/edges; deterministic ingest |
| APIs | request/response samples | backward compat or version bump |
| UI | registry/config samples | no hidden data leakage; a11y-safe patterns |
| Focus Mode | (optional) example context bundle payload | no unsourced narrative |

## 🧠 Story Node & Focus Mode Integration

Fixtures may include **example Story Nodes or Focus Mode context bundles** for UI/dev previews. If included:

- They must be clearly marked **example-only** and must not be treated as “published.”
- They must include provenance pointers (even if pointing to fixture-local ids).

If you are creating/altering canonical Story Nodes, use:
- `docs/reports/story_nodes/` (draft/published workflow)
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`

## 🧪 Validation & CI/CD

### Minimum CI gates relevant to fixtures (recommended)

- Markdown protocol validation (this README and any fixture pack READMEs)
- JSON schema validation (STAC/DCAT/PROV/UI registry) when fixtures include those formats
- Graph integrity tests when fixtures include ingest/imports
- API contract tests when fixtures include request/response snapshots
- Security scanning (secrets/PII) for any added fixture payloads

### Local validation steps (fill in repo-specific commands)

Replace the placeholders below with actual project commands once confirmed in repo.

- `make test` (not confirmed in repo)
- `python -m pytest` (not confirmed in repo)
- `node …` UI checks (not confirmed in repo)
- `stac-validator …` (not confirmed in repo)
- `jsonschema …` (not confirmed in repo)

## ⚖ FAIR+CARE & Governance

### Governance review triggers for fixtures

Request governance/security review if a fixture pack includes:

- Real personal data (PII) or anything that could re-identify individuals
- Sensitive site locations or culturally sensitive information
- Restricted layers that require generalization/redaction rules
- API payloads that could expose internal-only fields

### Sovereignty safety (fixtures)

Fixtures must follow the same sovereignty/CARE constraints as canonical data:

- Prefer synthetic or heavily minimized samples.
- If locations are sensitive: generalize (coarser geometry) or redact.
- Never include secrets/credentials in fixtures.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial fixtures README scaffold | TBD |

---

Footer refs:
- `docs/MASTER_GUIDE_v12.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`
