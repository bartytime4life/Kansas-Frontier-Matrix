---
title: "KFM Tests — README"
path: "tests/README.md"
version: "v1.2.1"
last_updated: "2025-12-29"
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

doc_uuid: "urn:kfm:doc:tests:readme:v1.2.1"
semantic_document_id: "kfm-tests-readme-v1.2.1"
event_source_id: "ledger:kfm:doc:tests:readme:v1.2.1"
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
- Map test areas to the **minimum CI gates** required for “v12-ready” contributions and the additional gates for **v13 readiness**.
- Provide patterns for writing tests that are **deterministic, hermetic, and CI-safe**.
- Provide a “gate → debug” map so failures are **fast to triage** and never “mysterious”.

### Scope

| In scope | Out of scope |
|---|---|
| Test taxonomy (unit/integration/contract/e2e) and what belongs where | Implementing specific pipelines/features |
| Fixture policy, golden outputs, determinism + hermeticity rules | Selecting a specific test runner/tooling *(use repo-standard runner)* |
| CI gate mapping + “skip vs fail” behavior | Replacing governance/security policy documents |
| Validation expectations for STAC/DCAT/PROV, schemas, graph, APIs, UI registries, releases, and Story Nodes | Writing new policy *(propose via governance review)* |

### Audience

- **Primary:** contributors working on pipelines, schemas, graph ingest, APIs, UI, Story Nodes, Focus Mode.
- **Secondary:** maintainers reviewing PRs and debugging CI failures.

### Definitions

- Glossary link: `docs/glossary.md` *(not confirmed in repo; recommended)*.

Terms used in this doc:

- **Unit test**: fast, pure, no external deps.
- **Integration test**: multi-module behavior using fixtures.
- **Contract test**: validates “what we promise” at boundaries (schemas/contracts/registry shapes).
- **E2E test**: vertical slice across boundaries (API→UI→Story).
- **Deterministic**: same inputs/config/code ⇒ same outputs.
- **Hermetic**: no hidden network/DB/filesystem dependencies (beyond temp dirs).
- **Golden file / snapshot**: committed expected output used for regression tests.

### Pipeline invariants tests must protect

Tests are guardians of KFM’s non-negotiables (see Master Guide for canonical ordering and invariants):

- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- **One canonical home per subsystem** (no duplicate “mystery” implementations).
- **UI never queries Neo4j directly**; all access is via **contracted APIs**.
- Focus Mode consumes **provenance-linked** content only (no unsourced narrative).
- Deterministic outputs with **stable IDs** and repeatable lineage (PROV).
- **No output may be less restricted than any upstream input** in its lineage (classification propagation).

### CI decision rule (must hold)

All gates should follow one consistent decision rule:

| Condition | Example | Expected CI behavior |
|---|---|---|
| Root missing / gate not applicable | `releases/` does not exist | **Skip** (explicit “not applicable”) |
| Root present and valid | `data/stac/` exists and validates | **Pass** |
| Root present but invalid | `data/stac/` exists, invalid STAC item | **Fail deterministically** |

> “Skip” means “not applicable”; it must not be used to hide invalid artifacts.

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
  - releases (manifests/SBOM/attestations if present),
  - Story Node structure + provenance/citation requirements.
- [ ] CI behavior follows the same decision rule everywhere:
  - **skip** if the root is not applicable / missing,
  - **fail** if present but invalid.
- [ ] Update this README if you introduce a new test area, fixture type, validator, or CI gate.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + minimum CI gates | `docs/MASTER_GUIDE_v12.md` | Architecture | System + pipeline source of truth |
| v13 redesign blueprint (draft reference) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Consolidates “one canonical home”, contract-first, evidence-first |
| Next stages blueprint | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | Architecture | Roadmap + gap closure plan |
| Full architecture & vision | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | Architecture | End-to-end vision |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Baseline governed doc structure |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Narrative constraints + validation expectations |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Required for endpoint/contract changes |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |
| Repo structure standard | `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md` | Docs | *not confirmed in repo; propose adding under `docs/standards/` if governance approves* |
| Schemas | `schemas/` | Schema owners | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| CI workflows | `.github/workflows/` | Maintainers | Gate enforcement |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (path matches file location)
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Test taxonomy + directory conventions are explicit
- [ ] Minimum CI gates are enumerated + mapped to debug starting points
- [ ] Commands are either repo-accurate or explicitly marked “not confirmed in repo”
- [ ] Governance + CARE/sovereignty constraints explicitly stated for fixtures, logs, and outputs

## 🗂️ Directory Layout

### This document

- `path`: `tests/README.md` *(must match front-matter)*

### Related repository paths (canonical homes)

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Staged data + catalog outputs (STAC/DCAT/PROV) |
| Documentation | `docs/` | Canonical governed docs (guides, designs, domain notes) |
| Templates | `docs/templates/` | Governed doc templates (universal/story/API) |
| Architecture | `docs/architecture/` | System designs, roadmaps, ADRs (if present) |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Catalog build/validation tooling | `tools/` and/or `src/pipelines/` | Validators + QA scripts *(keep one canonical home)* |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | API service + contracts + redaction logic |
| UI | `web/` | React + map client + Focus Mode UI |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs |
| Tests | `tests/` | Unit + integration tests (baseline) + optional contract/e2e suites |
| Releases | `releases/` | Versioned packaged artifacts (if used) |
| CI | `.github/` | Workflows + policy gates |

### Canonical homes by stage (context)

| Stage | Canonical home | Primary evidence outputs | Tests should validate |
|---|---|---|---|
| ETL / pipelines | `src/pipelines/` | `data/**` | determinism + idempotence + fixture-driven transforms |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV artifacts | schema validity + link integrity + lineage completeness |
| Graph | `src/graph/` + `data/graph/` *(if present)* | ingest fixtures + constraints | ontology constraints + stable IDs + required edges |
| API boundary | `src/server/` | contracted responses | OpenAPI/GraphQL contracts + provenance + redaction |
| UI | `web/` | registries + rendering | registry schema checks + a11y + no leakage |
| Story Nodes | `docs/reports/story_nodes/` | draft/published nodes | structure + provenance linking + redaction compliance |
| Releases | `releases/` | manifests/SBOM/attestations *(if present)* | artifact schema checks + integrity + presence rules |

### Recommended `tests/` structure

> This is the **recommended** layout. Some subfolders may not exist yet; gates should **skip if absent** and **fail if invalid when present**.

~~~text
📁 tests/
├── 📄 README.md
├── 📁 unit/                          # fast, deterministic, no external deps
├── 📁 integration/                   # multi-module tests using fixtures
├── 📁 contract/                      # schemas + boundary contracts (schemas, APIs, registries, releases)
│   ├── 📁 schemas/                   # validate JSON Schemas themselves (and optional SHACL shapes if used)
│   ├── 📁 catalogs/                  # validate STAC/DCAT/PROV artifacts + link integrity
│   ├── 📁 graph/                     # ontology + ingest invariants
│   ├── 📁 api/                       # OpenAPI/GraphQL contract snapshots
│   ├── 📁 ui/                        # UI registry schemas
│   ├── 📁 storynodes/                # Story Node structure + provenance rules
│   ├── 📁 releases/                  # manifests/SBOM/attestations (if present)
│   └── 📁 repolint/                  # repo structure lint rules (paths + naming + duplication)
├── 📁 e2e/                           # vertical slice flows (may live under `web/`)
├── 📁 fixtures/                      # small synthetic fixtures only
│   ├── 📁 data/
│   ├── 📁 catalogs/                  # minimal STAC/DCAT/PROV examples (if needed)
│   ├── 📁 graph/
│   ├── 📁 api/
│   ├── 📁 ui/
│   └── 📁 releases/
└── 📁 helpers/                       # shared test utilities (pure + deterministic)
~~~

### What belongs where (rules of thumb)

- **Unit:** pure logic and helpers (no network, no DB, no repo writes).
- **Integration:** multiple modules interacting via fixtures; may write to temp directories only.
- **Contract:** validates “what we promise” (schemas, API contracts, registry shapes, Story Node requirements).
- **E2E:** verifies vertical slice behavior across boundaries (API→UI→Story), using staged fixtures.

## 🧭 Context

### What KFM is (briefly)

KFM is an open-source **geospatial + historical** knowledge system (a “living atlas” of Kansas) that ingests heterogeneous sources, publishes governed metadata catalogs (STAC/DCAT/PROV), builds a semantically structured Neo4j graph, and serves evidence through contracted APIs into a map + narrative UI. KFM is designed so that **every narrative claim can be traced to versioned evidence**, and every derived product has explicit lineage.

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

### Stable IDs and classification propagation

Where tests touch IDs, keys, or sensitivity:

- stable ID generation (no randomness without fixed seed),
- deterministic ordering for serialized outputs,
- explicit schema/contract version references where applicable,
- no classification “downgrades” along provenance chains (enforced by CI scanning gates).

### CI logs and artifacts (safety rule)

- CI logs and uploaded artifacts must not contain restricted coordinates, culturally sensitive locations, secrets, or PII.
- Prefer **summary diagnostics** (counts, failing IDs, schema paths) over raw record dumps.
- If a failure requires showing example records, use **synthetic fixtures** or redact/generalize before printing.

## 🌐 STAC, DCAT & PROV Alignment

Contract tests should validate (when relevant roots exist):

### STAC

- collection ↔ item integrity
- required fields + profile/extension expectations (if used)
- asset links are valid (no broken references)
- stable identifiers (no regenerated IDs on rerun)

### DCAT

- dataset/distribution metadata completeness (title/description/license/keywords at minimum)
- distributions reference underlying assets or STAC catalogs (where applicable)
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
| Releases | manifests/SBOM/attestations (if present) | integrity + traceability | artifact contract checks |

### Interfaces / contracts (what tests defend)

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog; contract tests required |
| API contracts | `src/server/` (+ `src/server/contracts/**` if present) | backward compat or version bump + tests |
| UI layer registry schemas | `web/` | schema-validated; no leakage |
| Story Node template + validation | `docs/templates/` + `docs/reports/story_nodes/` | structure + provenance rules; published nodes must validate |
| Release artifacts | `releases/` | schema + integrity checks (if present) |

### Test-to-subsystem mapping (recommended)

| Test area | What it validates | Suggested location |
|---|---|---|
| Unit | pure functions, ID helpers, schema helpers | `tests/unit/` |
| Integration | multi-module behavior; stage outputs using fixtures | `tests/integration/` |
| Contract | schema validation (STAC/DCAT/PROV/story nodes/UI/telemetry), API contract snapshots, release artifacts | `tests/contract/` |
| E2E | vertical slice flows across boundaries (API→UI→Story) | `tests/e2e/` *(or under `web/` if UI runner lives there)* |

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
- redaction/generalization compliance for restricted material,
- explicit separation of **fact vs inference vs hypothesis** where applicable.

### Focus Mode rule (hard gate)

- Focus Mode only consumes **provenance-linked** content.
- Predictive/AI-generated content (if present) must be opt-in and include uncertainty/confidence metadata.
- AI must not infer or reveal sensitive locations.

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
  - no duplicate canonical homes without explicit deprecation markers,
  - references to missing files must be marked **“not confirmed in repo”** (or the missing artifact must be added).
- [ ] (If `releases/` exists) release artifact validation:
  - manifests/SBOMs/attestations validate and are internally consistent.

### v13 migration phases (tests relevance)

- **Phase 0 (structure first):** if canonical roots are missing, add placeholders so CI can reason about “skip vs validate” consistently.
- **Phase 1 (contracts + validators):** add/expand schema + contract tests; ensure gates **skip** when optional roots are absent and **fail deterministically** when present but invalid.
- **Phase 2 (vertical slice):** implement one domain end-to-end and lock it with a vertical slice E2E test.
- **Phase 3 (scale out):** add domains iteratively with contract tests + provenance checks and governance triggers for sensitive content and AI narrative behaviors.

### Gate → debug map (quick orientation)

| CI gate | Primary roots | If it fails, start here |
|---|---|---|
| Markdown protocol validation | `docs/`, governed READMEs | front-matter, headings, links, “not confirmed in repo” markings |
| Repo lint rules | repo-wide | duplicate canonical homes, disallowed filenames, YAML front-matter in code files |
| Link/reference checks | repo-wide | broken paths/IDs; moved assets; dangling references |
| Schema validation | `schemas/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/`, `web/` registries | schema definitions or emitted artifacts (missing required fields/links) |
| Graph integrity tests | `src/graph/` (+ `data/graph/` if present) | ontology constraints, ingest transforms, stable IDs |
| API contract tests | `src/server/` (contracts) | contract schema + response shape + provenance + redaction |
| UI registry checks | `web/` | registry JSON + schema + build-time validation |
| Story Node validation | `docs/reports/story_nodes/` | missing citations, broken evidence refs, invalid structure, redaction issues |
| Release artifact checks | `releases/` | manifests/SBOMs/attestations schema + integrity |
| Security/sovereignty scanning | repo-wide | remove secrets/PII; generalize/redact restricted material; check classification propagation |

### Reproduction

> Commands below are **examples only** (actual commands are repo-specific). Replace with repository scripts.

~~~bash
# Example placeholders — replace with repo-specific commands/scripts.

# 1) Run unit + integration tests
# <TBD>

# 2) Run contract/schema validation (STAC/DCAT/PROV/storynodes/ui/telemetry/releases)
# <TBD>

# 3) Run graph integrity checks
# <TBD>

# 4) Run API contract tests
# <TBD>

# 5) Run repo lint rules + link checks
# <TBD>

# 6) Run security + sovereignty scans
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
- adds/changes a public-facing API endpoint,
- changes classification/sensitivity or publication behavior.

### CARE / sovereignty considerations

- Tests and fixtures must not leak restricted coordinates or culturally sensitive material.
- CI logs/artifacts must avoid publishing restricted content (prefer summary errors over raw dumps).
- Classification must propagate: outputs must not be less restricted than upstream lineage inputs.

### AI usage constraints

This README’s AI transform permissions/prohibitions are defined in front-matter and must remain aligned with repository governance.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.2.1 | 2025-12-29 | Aligned language and “not confirmed in repo” marking with Master Guide v12 patterns; clarified CI log/artifact safety and link-check expectations; minor structural cleanup | TBD |
| v1.2.0 | 2025-12-28 | Aligned with Master Guide v12 and v13 redesign blueprint: added releases + repo lint gates, clarified canonical homes and Phase 0/1/2 mapping, tightened DoD to include “claims link to evidence” | TBD |
| v1.1.0 | 2025-12-28 | Aligned minimum CI gates to Master Guide; normalized Key Artifacts table to Universal template; added link checks, detailed security scans, and repo lint rules | TBD |
| v1.0.1 | 2025-12-27 | Strengthened determinism + fixture rules, clarified CI skip/fail principle, expanded gate→debug map | TBD |
| v1.0.0 | 2025-12-26 | Initial `tests/` README aligned to KFM pipeline + minimum CI gates | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Redesign Blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Next Stages Blueprint: `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md`
- Full Architecture & Vision: `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Standards (if present): `docs/standards/`