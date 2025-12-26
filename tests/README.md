---
title: "KFM Tests — README"
path: "tests/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
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

- Define the **testing and validation conventions** for KFM.
- Map tests to the **minimum CI gates** required for “v12-ready” contributions.
- Provide a single place to document how to add new tests and keep them deterministic.

### Scope

| In Scope | Out of Scope |
|---|---|
| Test taxonomy (unit/integration/contract/e2e), fixtures, and validation gates | Implementing specific pipelines or features |
| Where new tests belong and how they should behave (determinism, no hidden I/O) | Selecting a specific test framework/tooling (not confirmed in repo) |
| Schema validation expectations for STAC/DCAT/PROV outputs | Replacing governance/security policies |

### Audience

- **Primary:** KFM contributors writing or updating pipelines, schemas, APIs, UI layers, and Story Nodes.
- **Secondary:** Maintainers reviewing PRs and debugging CI failures.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo — add/repair link if glossary lives elsewhere)*
- Terms used in this doc include: **unit test**, **integration test**, **contract test**, **schema validation**, **idempotence**, **deterministic pipeline**, **redaction**, **provenance**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Template used by this README |
| JSON Schemas (STAC/DCAT/PROV/storynodes/ui/telemetry) | `schemas/` | Data/Platform | Schema validation gates should reference these |
| ETL + catalog pipelines | `src/pipelines/` | Data Eng | Determinism + idempotence checks |
| Graph build + ontology bindings | `src/graph/` | Graph Eng | Graph integrity tests |
| API boundary | `src/server/` *(preferred)* or `src/api/` *(legacy; not confirmed in repo)* | API Eng | Contract tests required |
| UI layer registry + map client | `web/` | Frontend | Schema checks + a11y gates |
| Story Nodes + Focus Mode | `docs/reports/story_nodes/` + UI | Narrative | Provenance-linked narrative rule enforcement |
| CI workflows (if present) | `.github/workflows/` | CI Maintainers | Gate enforcement + artifacts |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Test taxonomy + directory conventions are explicit
- [ ] Minimum CI gates are mapped to where failures should be debugged
- [ ] Commands are either repo-accurate or explicitly marked “not confirmed in repo”
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `tests/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Tests | `tests/` | Unit/integration/contract/e2e tests + fixtures |
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| API boundary | `src/server/` | Contracted access layer (REST/GraphQL); redaction + provenance refs |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |
| Tooling | `tools/` | Validators, scripts, developer utilities |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 tests/
├── 📄 README.md
├── 📁 unit/                 # fast, deterministic, no external deps (recommended)
├── 📁 integration/          # multi-module tests (recommended)
├── 📁 contract/             # schema + API contract tests (recommended)
├── 📁 e2e/                  # UI/API end-to-end (recommended; may be split under web/)
├── 📁 fixtures/             # small synthetic fixtures only (recommended)
└── 📁 helpers/              # shared test utilities (recommended)
~~~

## 🧭 Context

### Background

KFM is an evidence-first, provenance-linked system where each stage of the pipeline must remain reproducible and contract-valid:

- **ETL** produces deterministic outputs.
- **STAC/DCAT/PROV** catalogs provide machine-valid evidence and lineage.
- **Graph** integrates semantics in Neo4j (via governed ingest).
- **APIs** are the access boundary (UI never queries Neo4j directly).
- **UI** renders map + narrative views.
- **Story Nodes** + **Focus Mode** are provenance-linked narrative artifacts and experiences.

Tests exist to keep these boundaries **true, enforced, and debug-able**.

### Assumptions

- The pipeline flow is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The UI does not read Neo4j directly; the API boundary mediates access and enforces redaction/generalization.
- Contract and schema validation are treated as first-class build gates.

### Constraints / invariants

- Tests must be:
  - **Deterministic** (same inputs/config/code ⇒ same outputs).
  - **Hermetic by default** (no hidden network I/O; no hidden filesystem dependencies).
  - **CI-safe** (no secrets/PII in fixtures; no restricted coordinates in committed test data).

- “Do not break” rules that tests should enforce:
  - Pipelines are idempotent and deterministic.
  - Catalog artifacts validate against schemas under `schemas/`.
  - UI consumes graph and catalog content through **APIs only** (no direct graph dependency).
  - Focus Mode only presents **provenance-linked** content (no uncited facts).
  - Any predictive/AI-generated content (if present) is opt-in and must include uncertainty/confidence metadata.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the repo’s canonical test runner(s) and command set (Python/Node/etc.)? | TBD | TBD |
| Where is the authoritative Story Node validation schema set located (and how is it invoked in CI)? | TBD | TBD |
| Where is the authoritative run manifest location for this repo: `data/prov/` vs `releases/<version>/`? | TBD | TBD |
| Which fixture datasets are safe to include publicly under `tests/fixtures/`? | TBD | TBD |

### Future extensions

- Add “golden” fixtures + output hashes for deterministic regression tests.
- Add composite actions / scripts to run CI gates locally (kept in sync with workflows).
- Add property-based tests for stable IDs and schema compatibility (tooling not confirmed in repo).

## 🗺️ Diagrams

### System / dataflow diagram (canonical pipeline)

~~~mermaid
flowchart LR
  A["ETL — src/pipelines"] --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph — src/graph (+ data/graph outputs)"]
  C --> D["API Boundary — src/server (contracts + redaction)"]
  D --> E["UI — web/ (React/Map UI; no direct graph reads)"]
  E --> F["Story Nodes — docs/reports/story_nodes/"]
  F --> G["Focus Mode — provenance-linked rendering"]
~~~

## 📦 Data & Metadata

### Data lifecycle (required staging)

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (+ `data/catalog/dcat/` + `data/prov/`)

### Fixture policy

- **Allowed:** small, synthetic, non-sensitive fixtures (minimal rows/features; no real raw snapshots).
- **Disallowed:** production-sized datasets, restricted coordinates, culturally sensitive locations, secrets/credentials, PII.

### Stable IDs and determinism

Where tests touch IDs or keys, they should verify:

- stable ID generation rules (no randomness without fixed seed),
- deterministic ordering for serialized outputs (JSON stable sort, stable timestamps where applicable),
- explicit version pinning for schemas and contracts.

## 🌐 STAC, DCAT & PROV Alignment

Contract tests should validate (when the relevant roots exist):

- **STAC**
  - collection ↔ item integrity
  - required fields + extension profiles (if used)
  - asset links are valid (no broken references)

- **DCAT**
  - dataset/distribution metadata completeness (title/description/license/keywords at minimum)
  - stable identifiers match catalog conventions

- **PROV**
  - every transform emits an activity record and links inputs → outputs
  - run identifiers are recorded and resolvable where used downstream

## 🧱 Architecture

### Subsystem contracts (what must exist for each subsystem)

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

### Test-to-subsystem mapping (recommended)

| Test area | What it validates | Suggested location |
|---|---|---|
| Unit | pure functions, ID helpers, schema helpers | `tests/unit/` |
| Integration | multi-module behavior; pipeline stage outputs using fixtures | `tests/integration/` |
| Contract | schema validation (STAC/DCAT/PROV/story nodes), API contract snapshots | `tests/contract/` |
| E2E | UI/API flows using staged fixtures | `tests/e2e/` *(or `web/` if UI runner lives there — not confirmed in repo)* |

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

Tests should enforce the invariant that **Focus Mode consumes provenance-linked content only**.

Story Node validation checks (for published nodes) should include:

- citations/provenance-linking rules
- entity reference resolution (IDs/links resolve)
- redaction/generalization compliance for restricted material

This supports the KFM invariant that **published narratives must not be unsourced**.

### Provenance-linked narrative rule

- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls (if used)

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Minimum CI gates

The baseline gates workflows should enforce (via local actions and/or workflow steps):

- [ ] Markdown protocol validation (template + front matter + links)
- [ ] Schema validation (STAC/DCAT/PROV + story node schemas)
- [ ] Graph integrity tests
- [ ] API contract tests (OpenAPI/GraphQL)
- [ ] UI layer registry schema checks
- [ ] Security + sovereignty scanning where applicable

### CI behavior principle

CI workflows must be deterministic in “skip vs fail” behavior:

- If a gate depends on a root that does not exist in the current repo snapshot, the workflow should **skip** that gate.
- If the root exists, validation must be **strict** and must **fail deterministically** when invalid.

### Gate → debug map (quick orientation)

| CI gate | Primary roots | If it fails, start here |
|---|---|---|
| Markdown protocol validation | `docs/`, governed READMEs | the doc’s front matter / headings / links |
| Schema validation | `schemas/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/`, story node schemas | schema definition or emitted artifacts |
| Graph integrity tests | `src/graph/` (+ `data/graph/` if present) | ontology bindings / ingest transforms |
| API contract tests | `src/server/contracts/` *(preferred)* | OpenAPI/GraphQL contract + compatibility notes |
| UI registry checks | `web/` (+ any UI registry schemas) | layer registry JSON + schema |
| Security/sovereignty scanning | repo-wide | remove secrets/PII; enforce redaction/generalization |

### Reproduction

> Commands below are **examples only** (actual commands are **not confirmed in repo**). Replace with repo-specific scripts.

~~~bash
# Example placeholders — replace with repo-specific commands/scripts.

# 1) Markdown protocol checks
# <TBD>

# 2) Schema validation (STAC/DCAT/PROV/storynodes/ui/telemetry)
# <TBD>

# 3) Graph integrity tests
# <TBD>

# 4) API contract tests
# <TBD>

# 5) Security + sovereignty scanning
# <TBD>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| CI gate results | GitHub Actions | CI artifacts *(repo path not confirmed)* |

## ⚖ FAIR+CARE & Governance

### Review gates

- CI maintainers approve changes to `.github/workflows/` and local actions (if used).
- Governance owners review anything that:
  - changes sovereignty handling or redaction behavior
  - affects handling of culturally sensitive or restricted locations
  - introduces new automated inference over sensitive content

### CARE / sovereignty considerations

- Tests and fixtures must not introduce leakage of restricted coordinates or culturally sensitive material.
- Any scans must treat restricted outputs as sensitive and avoid publishing them in public logs/artifacts.

### AI usage constraints

This README’s AI transform permissions/prohibitions are defined in front-matter and must remain aligned with repository governance.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial `tests/` README aligned to KFM pipeline + minimum CI gates | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
