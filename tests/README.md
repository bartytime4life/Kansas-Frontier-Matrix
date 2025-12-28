---
title: "KFM Tests — README"
path: "tests/README.md"
version: "v1.1.0"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:tests:readme:v1.1.0"
semantic_document_id: "kfm-tests-readme-v1.1.0"
event_source_id: "ledger:kfm:doc:tests:readme:v1.1.0"
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

> Contract-first tests for an evidence-first pipeline.  
> Goal: make every stage **deterministic**, **schema-valid**, **provenance-linked**, and **safe to publish**.

## 📘 Overview

### Purpose

- Define **testing and validation conventions** across the KFM pipeline.
- Map test areas to the **minimum CI gates** required for “v12-ready” contributions (and the additional gates for v13 readiness).
- Provide patterns for writing tests that are **deterministic, hermetic, and CI-safe**.
- Provide a “gate → debug” map so failures are **fast to triage**.

### Scope

| In scope | Out of scope |
|---|---|
| Test taxonomy (unit/integration/contract/e2e) and what belongs where | Implementing specific pipelines/features |
| Fixture policy, golden outputs, determinism + hermeticity rules | Selecting a specific test runner/tooling *(use repo-standard runner; not confirmed in repo)* |
| CI gate mapping + “skip vs fail” behavior | Replacing governance/security policy documents |
| Validation expectations for STAC/DCAT/PROV, schemas, graph, APIs, UI registries, and Story Nodes | Writing new policy *(propose via governance review)* |

### Audience

- **Primary:** KFM contributors working on pipelines, schemas, graph ingest, APIs, UI, Story Nodes, Focus Mode.
- **Secondary:** maintainers reviewing PRs and debugging CI failures.

### Definitions (link to glossary)

- Glossary: `docs/glossary.md` *(not confirmed in repo; recommended canonical home)*
- Terms used in this doc:
  - **Unit test**: fast, pure, no external deps.
  - **Integration test**: multi-module behavior using fixtures.
  - **Contract test**: validates “what we promise” at boundaries (schemas/contracts/registry shapes).
  - **E2E test**: vertical slice across boundaries (API→UI→Story).
  - **Deterministic**: same inputs/config/code ⇒ same outputs.
  - **Hermetic**: no hidden network/DB/filesystem dependencies (beyond temp dirs).
  - **Golden file / snapshot**: committed expected output used for regression tests.

### Pipeline invariants tests must protect

Tests are also guardians of KFM’s non-negotiables:

- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- **One canonical home per subsystem** (no duplicate “mystery” implementations).
- **UI never queries Neo4j directly**; all access is via **contracted APIs**.
- Focus Mode consumes **provenance-linked** content only (no uncited narrative).
- Deterministic pipeline outputs with **stable IDs** and repeatable lineage (PROV).

### Contributor quick checklist

When adding or modifying tests:

- [ ] Choose the correct test type (unit / integration / contract / e2e).
- [ ] Use **small, synthetic fixtures** (no secrets, no PII, no restricted coordinates).
- [ ] Make the test deterministic (fixed seed, stable ordering, no wall-clock timestamps).
- [ ] If you touch a boundary, add/update contract coverage:
  - schemas (`schemas/**`) and emitted catalogs (`data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`),
  - graph ingest and ontology constraints,
  - API contracts (OpenAPI/GraphQL),
  - UI registries (layer definitions, config schemas),
  - Story Node structure + provenance/citation requirements.
- [ ] CI behavior is deterministic:
  - **skip if root is not applicable / missing**,
  - **fail if present but invalid**.
- [ ] Update this README if you introduce a new test area, fixture type, or CI gate.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + minimum CI gates | `docs/MASTER_GUIDE_v12.md` | Architecture | Canonical ordering + “v12-ready” minimum gates |
| v13 redesign blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | “One canonical home” + CI skip/fail semantics + repo lint rules |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Baseline governed doc structure |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Narrative constraints + validation expectations |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Required for endpoint/contract changes |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |
| Schemas | `schemas/` | Schema owners | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| CI workflows | `.github/workflows/` | Maintainers | Gate enforcement *(not confirmed in repo)* |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (path matches file location)
- [ ] Test taxonomy + directory conventions are explicit
- [ ] Minimum CI gates are enumerated + mapped to debug starting points
- [ ] Commands are either repo-accurate or explicitly marked “not confirmed in repo”
- [ ] Governance + CARE/sovereignty constraints explicitly stated for fixtures, logs, and outputs

## 🗂️ Directory Layout

### This document

- `path`: `tests/README.md` (must match front-matter)

### Related repository paths (canonical homes)

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Staged data + catalog outputs (STAC/DCAT/PROV) |
| Documentation | `docs/` | Canonical governed docs (guides, designs, domain notes) |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | API service + contracts + redaction logic |
| UI | `web/` | React + map client + Focus Mode UI |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs |
| Tests | `tests/` | Unit + integration + contract tests (this doc) |
| Tools | `tools/` | Validators, utilities, QA scripts |
| CI | `.github/` | Workflows + policy gates |
| Releases | `releases/` | Versioned packaged artifacts (if used) |

### Canonical homes by stage (context)

| Stage | Canonical home | Primary evidence outputs | Tests should validate |
|---|---|---|---|
| ETL / pipelines | `src/pipelines/` | `data/**` | determinism + idempotence + fixture-driven transforms |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV artifacts | schema validity + link integrity + lineage completeness |
| Graph | `src/graph/` (+ `data/graph/` if present) | ingest fixtures + constraints | ontology constraints + stable IDs + required edges |
| API boundary | `src/server/` | contracted responses | OpenAPI/GraphQL contract tests + provenance + redaction |
| UI | `web/` | registries + rendering | registry schema checks + a11y + no leakage |
| Story Nodes | `docs/reports/story_nodes/` | draft/published nodes | structure + provenance linking + redaction compliance |

### Recommended `tests/` structure

> This is the **recommended** layout. Some subfolders may not exist yet (*not confirmed in repo*).

~~~text
📁 tests/
├─ 📄 README.md
├─ 📁 unit/                         # fast, deterministic, no external deps
├─ 📁 integration/                  # multi-module tests using fixtures
├─ 📁 contract/                     # schema + contract tests (schemas, APIs, registries)
│  ├─ 📁 schemas/                   # validate JSON Schemas themselves (and optional SHACL shapes if used)
│  ├─ 📁 catalogs/                  # validate STAC/DCAT/PROV artifacts + link integrity
│  ├─ 📁 graph/                     # ontology + ingest invariants
│  ├─ 📁 api/                       # OpenAPI/GraphQL contract snapshots
│  ├─ 📁 ui/                        # UI registry schemas
│  └─ 📁 storynodes/                # Story Node structure + provenance rules
├─ 📁 e2e/                          # vertical slice flows (may live under `web/`)
├─ 📁 fixtures/                     # small synthetic fixtures only
│  ├─ 📁 data/
│  ├─ 📁 catalogs/                  # minimal STAC/DCAT/PROV examples (if needed)
│  ├─ 📁 graph/
│  ├─ 📁 api/
│  └─ 📁 ui/
└─ 📁 helpers/                      # shared test utilities (pure + deterministic)
~~~

### What belongs where (rules of thumb)

- **Unit:** pure logic and helpers (no network, no DB, no repo writes).
- **Integration:** multiple modules interacting via fixtures; may write to temp directories only.
- **Contract:** validates “what we promise” (schemas, API contracts, registry shapes, Story Node requirements).
- **E2E:** verifies vertical slice behavior across boundaries (API→UI→Story), using staged fixtures.

## 🧭 Context

### Why tests are first-class in KFM

KFM is contract-first and evidence-first. Most failures are boundary failures:

- a pipeline output stops validating (schema drift),
- a catalog link breaks (asset moves, broken href),
- a graph ingest violates ontology constraints,
- an API response drifts from contract or drops provenance fields,
- a UI registry entry becomes invalid (or leaks restricted detail),
- a Story Node loses provenance or violates redaction constraints.

Tests exist to keep these failures **detectable, localizable, and fixable**.

### Core constraints / invariants

All tests must be:

- **Deterministic**
  - same inputs/config/code ⇒ same outputs
- **Hermetic by default**
  - no hidden network I/O
  - no reliance on developer machine state
- **CI-safe**
  - no secrets, no PII
  - no restricted coordinates in committed fixtures
  - no culturally sensitive locations unless generalized + approved

### CI gate behavior rule (must hold)

CI gates should follow the same decision rule everywhere:

| Condition | Example | Expected CI behavior |
|---|---|---|
| Root missing / gate not applicable | `schemas/` does not exist | **Skip** (do not fail just because a subsystem is not yet present) |
| Root present and valid | `data/stac/` exists and validates | **Pass** |
| Root present but invalid | `data/stac/` exists, invalid STAC item | **Fail deterministically** |

> “Skip” means “not applicable”; it must not be used to hide invalid artifacts.

### Determinism checklist (practical)

If a test touches serialization, IDs, or timestamps, ensure:

- fixed seeds for randomness (no implicit RNG),
- controlled time (no “now” in golden outputs; inject/freeze time),
- stable ordering (sort before writing JSON/CSV),
- explicit version pinning (schema/contract versions recorded where applicable),
- no dependency on environment quirks (TZ/locale/path separators).

## 🗺️ Diagrams

### Pipeline + validation boundaries

~~~mermaid
flowchart LR
  A["ETL — src/pipelines/"] --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph — src/graph (+ data/graph)"]
  C --> D["API Boundary — src/server (contracts + redaction)"]
  D --> E["UI — web/ (no direct graph reads)"]
  E --> F["Story Nodes — docs/reports/story_nodes/"]
  F --> G["Focus Mode — provenance-linked rendering"]

  A -. "unit + integration" .- A
  B -. "contract (schemas + link checks)" .- B
  C -. "graph integrity" .- C
  D -. "API contract" .- D
  E -. "UI schema + a11y" .- E
  F -. "Story Node validation" .- F
~~~

## 📦 Data & Metadata

### Data lifecycle (required staging)

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (+ `data/catalog/dcat/` + `data/prov/`)

### Fixture policy

Fixtures must be safe to publish and safe to review.

- **Allowed:** small, synthetic, non-sensitive fixtures (minimal rows/features; minimal geometry detail).
- **Disallowed:** production-sized datasets, real raw snapshots, restricted coordinates, culturally sensitive locations (unless generalized + approved), secrets/credentials, PII.

### Golden files (deterministic regression)

Where a test compares outputs across time:

- store “expected” outputs as small golden files under `tests/fixtures/**`,
- ensure deterministic serialization (stable ordering, stable timestamps),
- update goldens only as part of an explicit “intentional change” PR (explain in PR notes/changelog).

### Stable IDs and determinism

Where tests touch IDs or keys, they should verify:

- stable ID generation (no randomness without fixed seed),
- deterministic ordering for serialized outputs,
- explicit schema/contract version references where applicable.

## 🌐 STAC, DCAT & PROV Alignment

Contract tests should validate (when relevant roots exist):

### STAC

- collection ↔ item integrity
- required fields + profile/extension expectations (if used)
- asset links are valid (no broken references)
- stable identifiers (no regenerated IDs on rerun)

### DCAT

- dataset/distribution metadata completeness (title/description/license/keywords at minimum)
- distributions reference the underlying assets or STAC catalog (where applicable)
- stable identifiers follow catalog conventions

### PROV

- each transform emits an activity record linking inputs → outputs
- run identifiers are recorded and referenced where used downstream
- raw → work → processed lineage is present for published artifacts

## 🧱 Architecture

### Subsystem contracts and what tests must cover

| Subsystem | Contract artifacts | “Do not break” rule | Tests expected |
|---|---|---|---|
| ETL | configs + run logs + validation notes | deterministic + replayable | unit/integration + golden outputs |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated outputs | schema/contract + link checks |
| Graph | ontology + migrations + constraints | stable labels/edges (unless migrated) | graph integrity tests |
| APIs | OpenAPI/GraphQL schema + contract tests | backwards compatible or version bump | contract + compatibility tests |
| UI | layer registry + a11y + audit affordances | no hidden data leakage | registry schema + a11y/smoke |
| Story/Focus | provenance-linked context bundle | no hallucinated/unsourced claims | provenance + linkage validation |

### Test-to-subsystem mapping (recommended)

| Test area | What it validates | Suggested location |
|---|---|---|
| Unit | pure functions, ID helpers, schema helpers | `tests/unit/` |
| Integration | multi-module behavior; stage outputs using fixtures | `tests/integration/` |
| Contract | schema validation (STAC/DCAT/PROV/story nodes/UI), API contract snapshots | `tests/contract/` |
| E2E | vertical slice flows across boundaries (API→UI→Story) | `tests/e2e/` *(or under `web/` if UI runner lives there — not confirmed in repo)* |

### Vertical slice (recommended E2E focus)

To prevent “everything passes except the actual user flow,” prefer at least one vertical slice test per domain:

- minimal ETL producing a processed fixture,
- STAC collection + items,
- DCAT dataset record,
- PROV bundle,
- graph ingest fixture,
- one API endpoint and one map layer,
- one published Story Node.

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as machine-ingestible storytelling

Story Node validation (for published nodes) should include:

- structure validation (template + required fields),
- citations/provenance-linking rules,
- entity reference resolution (IDs/links resolve),
- redaction/generalization compliance for restricted material.

### Focus Mode rule

- Focus Mode only consumes **provenance-linked** content.
- Predictive/AI-generated content (if present) must be opt-in and include uncertainty/confidence metadata.

## 🧪 Validation & CI/CD

### Minimum CI gates (v12-ready baseline)

The baseline gates expected for “v12-ready” contributions include:

- [ ] Markdown protocol validation (front-matter + required sections)
- [ ] Link/reference checks (no orphan pointers)
- [ ] JSON schema validation:
  - STAC/DCAT/PROV
  - story node schemas (if present)
  - telemetry schemas (if present)
  - UI layer registry schemas (if present)
- [ ] Graph integrity tests (constraints, expected labels/edges)
- [ ] API contract tests (OpenAPI/GraphQL schema + resolver tests)
- [ ] Security + sovereignty scanning gates (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Additional v13-readiness expectations

- [ ] Story Node validation gates (draft vs published as defined)
- [ ] Repo lint rules:
  - no YAML front-matter in code files,
  - no `README.me`,
  - no duplicate canonical homes without explicit deprecation markers.

### Gate → debug map (quick orientation)

| CI gate | Primary roots | If it fails, start here |
|---|---|---|
| Markdown protocol validation | `docs/`, governed READMEs | front-matter, headings, links, “not confirmed in repo” markings |
| Link/reference checks | repo-wide | broken paths/IDs; moved assets; dangling references |
| Schema validation | `schemas/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/` | schema definitions or emitted artifacts (missing required fields/links) |
| Graph integrity tests | `src/graph/` (+ `data/graph/` if present) | ontology constraints, ingest transforms, stable IDs |
| API contract tests | `src/server/` (contracts) | contract schema + response shape + provenance + redaction |
| UI registry checks | `web/` (+ registry schemas) | registry JSON + schema + build-time validation |
| Story Node validation | `docs/reports/story_nodes/` | missing citations, broken evidence refs, invalid structure |
| Security/sovereignty scanning | repo-wide | remove secrets/PII; generalize/redact restricted material; check classification propagation |

### Reproduction

> Commands below are **examples only** (actual commands are *not confirmed in repo*). Replace with repo-specific scripts.

~~~bash
# Example placeholders — replace with repo-specific commands/scripts.

# 1) Run unit + integration tests
# <TBD>

# 2) Run contract/schema validation (STAC/DCAT/PROV/storynodes/ui/telemetry)
# <TBD>

# 3) Run graph integrity checks
# <TBD>

# 4) Run API contract tests
# <TBD>

# 5) Run security + sovereignty scans
# <TBD>
~~~

### Telemetry signals (recommended, if telemetry exists)

| Signal | What it indicates |
|---|---|
| `classification_assigned` | dataset_id → sensitivity/classification set |
| `redaction_applied` | redaction/generalization performed and recorded |
| `promotion_blocked` | publish blocked by scan/validation failure |
| `catalog_published` | catalog outputs validated + published |
| `focus_mode_redaction_notice_shown` | UI displayed a required redaction notice |

## ⚖ FAIR+CARE & Governance

### Governance review triggers

Governance owners should review any change that:

- introduces new sensitive layers or restricted geographies,
- changes redaction/generalization logic,
- adds new AI narrative behaviors,
- adds a new external data source,
- adds/changes a public-facing API endpoint.

### CARE / sovereignty considerations

- Tests and fixtures must not leak restricted coordinates or culturally sensitive material.
- CI logs/artifacts must avoid publishing restricted content (prefer summary errors over raw dumps).

### AI usage constraints

This README’s AI transform permissions/prohibitions are defined in front-matter and must remain aligned with repository governance.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial `tests/` README aligned to KFM pipeline + minimum CI gates | TBD |
| v1.0.1 | 2025-12-27 | Strengthened determinism + fixture rules, clarified CI skip/fail principle, expanded gate→debug map | TBD |
| v1.1.0 | 2025-12-28 | Aligned minimum CI gates to Master Guide; normalized Key Artifacts table to Universal template; added link checks, detailed security scans, and repo lint rules | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Redesign Blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
