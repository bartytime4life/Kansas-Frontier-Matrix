---
title: "KFM Tests — README"
path: "tests/README.md"
version: "v1.0.1"
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

doc_uuid: "urn:kfm:doc:tests:readme:v1.0.1"
semantic_document_id: "kfm-tests-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:tests:readme:v1.0.1"
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
- Map test areas to the **minimum CI gates** required for “v12-ready” contributions.
- Provide patterns for adding new tests that remain **deterministic, hermetic, and CI-safe**.
- Provide a “gate → debug” map so CI failures are **fast to triage**.

### Scope

| In scope | Out of scope |
|---|---|
| Test taxonomy (unit/integration/contract/e2e) and what belongs where | Implementing specific pipelines/features |
| Fixture policy, golden outputs, determinism + hermeticity rules | Selecting a specific test runner/tooling *(use repo-standard runner; not confirmed here)* |
| CI gate mapping + “skip vs fail” behavior | Replacing governance/security policy documents |
| Validation expectations for STAC/DCAT/PROV, Story Nodes, and UI registries | Writing new policy (propose via governance review) |

### Audience

- **Primary:** KFM contributors working on pipelines, schemas, graph ingest, APIs, UI, Story Nodes.
- **Secondary:** maintainers reviewing PRs and debugging CI failures.

### Definitions

- Glossary: `docs/glossary.md` *(expected canonical home; not confirmed in repo — repair link if glossary lives elsewhere)*
- Terms used in this doc include: **unit test**, **integration test**, **contract test**, **schema validation**, **idempotence**, **determinism**, **hermetic test**, **golden file**, **redaction/generalization**, **provenance**.

### Pipeline invariants tests must protect

- Canonical flow is preserved: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- **UI never queries Neo4j directly**; all access is via **contracted APIs**.
- Focus Mode only presents **provenance-linked content** (no uncited facts).
- Determinism: same inputs + config + code ⇒ same outputs.

### Contributor quick checklist

When adding or modifying tests:

- [ ] Choose the correct test type (unit / integration / contract / e2e).
- [ ] Add/extend a **small, synthetic fixture** (no secrets, no PII, no restricted coordinates).
- [ ] Make the test deterministic (fixed seed, stable ordering, no wall-clock timestamps).
- [ ] If you change any interface boundary, add/update **contract tests**:
  - catalog schemas (STAC/DCAT/PROV),
  - API schema/contracts (OpenAPI/GraphQL),
  - UI registry schemas,
  - Story Node validation.
- [ ] Ensure CI behavior is deterministic: **skip if root missing; fail if invalid**.
- [ ] Update this README if you introduce a new test area, fixture type, or gate.

### Key references (canonical)

| Artifact | Path / Identifier | Status | Notes |
|---|---|---|---|
| Master pipeline ordering + minimum CI gates | `docs/MASTER_GUIDE_v12.md` | expected | Canonical ordering + v12 “minimum CI gates” |
| v13 redesign CI mapping + skip/fail rule | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | expected | Adds explicit “validate if present; fail if invalid; skip if not applicable” |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | expected | This README follows Universal template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | expected | Story Node structure + narrative constraints |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | expected | Required for endpoint changes |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | expected | Formatting/linking rules *(not confirmed in repo)* |
| Schemas | `schemas/` | canonical root | Schema validation gates reference this *(root may be missing in current repo)* |
| CI workflows | `.github/workflows/` | canonical root | Gate enforcement *(not confirmed in repo)* |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (path matches file location)
- [ ] Test taxonomy + directory conventions are explicit
- [ ] Minimum CI gates are enumerated + mapped to debug starting points
- [ ] Commands are either repo-accurate or explicitly marked “not confirmed in repo”
- [ ] Governance + CARE/sovereignty constraints explicitly stated for fixtures, logs, and outputs

## 🗂️ Directory Layout

### This document

- `path`: `tests/README.md` (must match front-matter)

### Canonical homes by stage (context)

| Stage | Canonical home | Evidence outputs | Tests should validate |
|---|---|---|---|
| ETL / pipelines | `src/pipelines/` | `data/**` | determinism + idempotence + fixture-driven transforms |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV | schema validity + link integrity + lineage completeness |
| Graph | `src/graph/` (+ `data/graph/`) | graph ingest fixtures | ontology constraints + stable IDs + required edges |
| API boundary | `src/server/` | contracted responses | OpenAPI/GraphQL contract tests + provenance refs |
| UI | `web/` | registries + rendering | schema checks + a11y + no leakage |
| Story Nodes | `docs/reports/story_nodes/` | draft/published nodes | schema + provenance linking + redaction compliance |

### Recommended `tests/` structure

> This is the **recommended** layout. Some subfolders may not exist yet (**not confirmed in repo**).

~~~text
📁 tests/
├─ 📄 README.md
├─ 📁 unit/                         # fast, deterministic, no external deps
│  ├─ 📁 python/                     # optional (only if Python is used)
│  └─ 📁 node/                       # optional (only if Node is used)
├─ 📁 integration/                  # multi-module tests using fixtures
├─ 📁 contract/                     # schema + contract tests
│  ├─ 📁 stac/
│  ├─ 📁 dcat/
│  ├─ 📁 prov/
│  ├─ 📁 storynodes/
│  ├─ 📁 ui/
│  └─ 📁 api/
├─ 📁 e2e/                          # end-to-end flows (may live under `web/`)
├─ 📁 fixtures/                     # small synthetic fixtures only
│  ├─ 📁 data/
│  ├─ 📁 stac/
│  ├─ 📁 dcat/
│  ├─ 📁 prov/
│  ├─ 📁 graph/
│  └─ 📁 api/
└─ 📁 helpers/                      # shared test utilities (pure + deterministic)
~~~

### What belongs where (rules of thumb)

- **Unit:** pure logic and helpers (no network, no DB, no repo writes).
- **Integration:** multiple modules interacting via fixtures; may write to temp directories only.
- **Contract:** validates “what we promise” (schemas, API contracts, registry shapes).
- **E2E:** verifies vertical slice behavior across boundaries (API→UI→Story), using staged fixtures.

## 🧭 Context

### Why tests are first-class in KFM

KFM is contract-first and evidence-first. Most failures are boundary failures:
- a pipeline output stops validating,
- a catalog link breaks,
- a graph ingest violates ontology constraints,
- an API response drifts from contract,
- a UI registry entry becomes invalid,
- a Story Node loses provenance, or leaks sensitive info.

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
  - no culturally sensitive locations unless protected and approved

### Determinism checklist (practical)

If a test touches serialization, IDs, or timestamps, ensure:

- fixed seeds for randomness (no implicit RNG),
- controlled time (no “now” in golden outputs; inject/freeze time),
- stable ordering (sort before writing JSON/CSV),
- explicit version pinning (schema/contract versions recorded where applicable),
- no dependency on environment quirks (TZ/locale/path separators).

### CI gate behavior rule (must hold)

- If a gate depends on a root that does **not** exist, CI should **skip** it.
- If the root exists, validation must be **strict** and must **fail deterministically** when invalid.

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
  B -. "contract (schema)" .- B
  C -. "graph integrity" .- C
  D -. "API contract" .- D
  E -. "UI schema + a11y" .- E
  F -. "Story Node validation" .- F
~~~

## 📦 Data & Metadata

### Data lifecycle (required staging)

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (+ `data/catalog/dcat/` + `data/prov/`)

### Fixture policy

- **Allowed:** small, synthetic, non-sensitive fixtures (minimal rows/features; minimal geometry detail).
- **Disallowed:** production-sized datasets, real raw snapshots, restricted coordinates, culturally sensitive locations (unless generalized + approved), secrets/credentials, PII.

### Golden files (deterministic regression)

Where a test compares outputs across time:

- store “expected” outputs as **small golden files** under `tests/fixtures/**`,
- ensure deterministic serialization (stable ordering, stable timestamps),
- update goldens only as part of an explicit “intentional change” PR (documented in PR notes / changelog).

### Stable IDs and determinism

Where tests touch IDs or keys, they should verify:

- stable ID generation (no randomness without fixed seed),
- deterministic ordering for serialized outputs,
- explicit schema/contract version references where applicable.

## 🌐 STAC, DCAT & PROV Alignment

Contract tests should validate (when relevant roots exist):

- **STAC**
  - collection ↔ item integrity
  - required fields + profile/extension expectations (if used)
  - asset links are valid (no broken references)

- **DCAT**
  - dataset/distribution metadata completeness (title/description/license/keywords at minimum)
  - stable identifiers follow catalog conventions

- **PROV**
  - each transform emits an activity record linking inputs → outputs
  - run identifiers are recorded and referenced where used downstream

## 🧱 Architecture

### Subsystem contracts and what tests must cover

| Subsystem | Contract artifacts | “Do not break” rule | Tests expected |
|---|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable | unit/integration + golden outputs |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated | schema/contract tests |
| Graph | ontology + migrations + constraints | stable labels/edges | graph integrity tests |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump | contract + compatibility tests |
| UI | layer registry + a11y + audit affordances | no hidden data leakage | schema + a11y/smoke |
| Focus Mode | provenance-linked context bundle | no hallucinated sources | provenance + linkage validation |

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

### Optional structured controls (if used)

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Minimum CI gates (baseline)

The baseline gates expected for “v12-ready” contributions include:

- [ ] Markdown protocol validation
- [ ] Schema validation (STAC/DCAT/PROV + telemetry, where applicable)
- [ ] Graph integrity tests
- [ ] API contract tests (OpenAPI/GraphQL)
- [ ] UI layer registry schema checks
- [ ] Security + sovereignty scanning gates (where applicable)

Additional v13-readiness expectations include:

- [ ] Story Node validation gates

### Repo lint rules (recommended)

Enforce:
- no YAML front-matter in code files,
- no `README.me`,
- no duplicate canonical homes without explicit deprecation markers.

### CI behavior principle (must be deterministic)

- If a gate depends on a root that does not exist, CI should **skip** that gate.
- If the root exists, validation must be **strict** and must **fail deterministically** when invalid.

### Gate → debug map (quick orientation)

| CI gate | Primary roots | If it fails, start here |
|---|---|---|
| Markdown protocol validation | `docs/`, governed READMEs | front-matter, headings, links, “not confirmed in repo” markings |
| Schema validation | `schemas/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/` | schema definitions or emitted artifacts (missing required fields/links) |
| Graph integrity tests | `src/graph/` (+ `data/graph/` if present) | ontology constraints, ingest transforms, stable IDs |
| API contract tests | `src/server/` (contracts) | contract schema + response shape + provenance refs |
| UI registry checks | `web/` (+ registry schemas) | registry JSON + schema + build-time validation |
| Story Node validation | `docs/reports/story_nodes/` | missing citations, broken evidence refs, invalid structure |
| Security/sovereignty scanning | repo-wide | remove secrets/PII; generalize/redact restricted material |

### Reproduction

> Commands below are **examples only** (actual commands are **not confirmed in repo**). Replace with repo-specific scripts.

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

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| CI gate results | GitHub Actions | CI artifacts *(repo path not confirmed)* |

## ⚖ FAIR+CARE & Governance

### Review gates

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

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Redesign Blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
