---
title: "🧪 Tests — Kansas Frontier Matrix (KFM) / Kansas‑Matrix‑System"
path: "tests/README.md"
version: "v1.6.0"
last_updated: "2026-01-26"
review_cycle: "90 days"
status: "active"
doc_kind: "Directory README"
license: "CC-BY-4.0"

# Protocol / contracts (KFM v13)
markdown_protocol_version: "1.0"
pipeline_contract_version: "v13"

# Governance references (repo paths; update if your layout differs)
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_ref: "docs/governance/SOVEREIGNTY.md"

# FAIR+CARE / sensitivity (this doc is public)
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

# Integrity & traceability (filled by tooling in governed lanes)
doc_uuid: "urn:kfm:doc:tests:readme:v1.6.0"
commit_sha: "<commit-sha>"
doc_integrity_checksum: "sha256:<to-be-filled>"

owners:
  - "KFM Engineering"
  - "KFM QA"

tags:
  - tests
  - ci
  - determinism
  - contract-first
  - catalog-first
  - evidence-triplet
  - stac
  - dcat
  - prov
  - receipts
  - run-manifest
  - policy-as-code
  - opa
  - conftest
  - governance
  - sovereignty
  - security
  - postgis
  - neo4j
  - elasticsearch
  - api
  - graphql
  - fastapi
  - ui
  - react
  - typescript
  - maplibre
  - cesium
  - story-nodes
  - focus-mode
  - ollama
  - rag
  - prompt-gate
  - embeddings
  - vector
  - drift
  - scenario
  - offline
  - ar
  - supply-chain
  - oras
  - oci
  - cosign
  - sbom
  - dvc
  - pdf
  - accessibility
---

<!--
📌 This README defines the repo-wide testing & verification surface for KFM / Kansas‑Matrix‑System.
🗓️ Last updated: 2026-01-26
🔁 Review cycle: 90 days (or anytime pipeline order / catalogs / policy pack / CI lanes change)
✅ Principle: evidence-first, fail-closed gates
🧾 According to KFM v13 docs (2026-era design set): “catalog triplet” metadata, clean layering, and provenance-linked AI outputs are non-negotiable.
-->

<div align="center">

# 🧪 Tests — Kansas Frontier Matrix (KFM) / Kansas‑Matrix‑System

**Trust-first testing for a contract‑first, catalog‑first geospatial + knowledge + modeling stack** 🧾🗺️🧬  
Determinism • Contracts • Governance • Evidence receipts • “Fail closed” gates ✅🔒

![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2ea44f?logo=githubactions&logoColor=white)
![CodeQL](https://img.shields.io/badge/Security-CodeQL-0b7285?logo=github&logoColor=white)
![Pytest](https://img.shields.io/badge/Python-pytest-blue?logo=python&logoColor=white)
![Node](https://img.shields.io/badge/Node.js-tests-brightgreen?logo=node.js&logoColor=white)
![Playwright](https://img.shields.io/badge/E2E-Playwright-0b7285?logo=playwright&logoColor=white)
![Docker](https://img.shields.io/badge/Integration-Docker%20Compose-2496ed?logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/DB-PostgreSQL%20%2B%20PostGIS-316192?logo=postgresql&logoColor=white)
![Neo4j](https://img.shields.io/badge/Graph-Neo4j-008CC1?logo=neo4j&logoColor=white)
![Elastic](https://img.shields.io/badge/Search-Elasticsearch-005571?logo=elasticsearch&logoColor=white)
![Contracts](https://img.shields.io/badge/Contracts-OpenAPI%20%7C%20GraphQL-ff6b6b)
![Catalogs](https://img.shields.io/badge/Catalogs-STAC%20%7C%20DCAT%20%7C%20PROV-6f42c1)
![Policy%20as%20Code](https://img.shields.io/badge/Policy-OPA%20%2B%20Conftest-1f6feb)
![AI](https://img.shields.io/badge/Focus%20Mode-Ollama%20RAG-8a2be2)
![Supply%20Chain](https://img.shields.io/badge/Supply%20Chain-OCI%20%2B%20Cosign%20%2B%20SBOM-8a2be2)
![Fail%20Closed](https://img.shields.io/badge/Quality%20Gates-Fail%20Closed-red)

</div>

> KFM tests don’t just check “it runs.”  
> They prove that our **pipelines**, **catalogs**, **graph**, **APIs**, **docs/story nodes**, **Focus Mode**, and **UI behaviors** are:
>
> ✅ **Correct** • ✅ **Reproducible** • ✅ **Governance‑compliant** • ✅ **Honest about uncertainty**  
>
> We test the **seams (boundaries + contracts)** and treat metadata/provenance as **first‑class artifacts** 🗂️🧬

> [!IMPORTANT]
> **tests/** is part of KFM’s *governed surface*.  
> If a change can affect what users see, what the system asserts as “truth”, or what users can infer, it must be **testable**, **traceable**, and **fail‑closed** when requirements aren’t met.

---

## 📘 Overview

### Purpose
This README defines **how KFM proves trust** through automated checks: contracts, catalogs, provenance, policy gates, and user-journey verification.

### Scope
| ✅ In scope | 🚫 Out of scope |
|---|---|
| Unit/integration/E2E tests across **Raw → ETL → catalogs → graph → API → UI → story → Focus Mode** | Offensive security guidance or penetration steps |
| Contract validation (schemas, OpenAPI/GraphQL, Story Node scripts, Focus Mode output schema) | “Manual-only” governance decisions (but we *do* automate triggers + blockers) |
| Determinism, receipts, evidence artifacts, and **evidence triplets** (STAC+DCAT+PROV) | Live network calls inside unit tests |
| Governance & “no downgrade” classification enforcement (including AI output policy checks) | Shipping unverified release artifacts |
| Optional AI regression tests (Ollama + smaller CI model / CPU mode) | “Freeform AI” without citations |

### Audience
- 👩‍💻 Engineers (pipelines, backend, UI)
- 🧪 QA + reviewers (governance/policy gates)
- 🧑‍⚖️ Data stewards (licensing, sovereignty, classification)
- 🤝 Contributors (how to add safe tests + fixtures)

### Definitions (fast)
- **Contract-first** 🧾: schemas + API contracts are first-class artifacts; changes are versioned and tested.
- **Catalog-first** 🗂️: nothing is “real” until it’s represented in STAC/DCAT and traced via PROV.
- **Evidence triplet** 🧬🗂️: **STAC + DCAT + PROV** emitted for every publish-grade dataset (boundary artifacts).
- **Receipt** 🧾📎: run manifest + hashes + linkage (what produced this, from what, with what config).
- **Fail-closed** 🔒: if policy/validation can’t run, the governed lane **halts**.
- **No mystery nodes** 🕸️: graph entities must trace back to catalog entries (no undocumented facts).
- **Prompt Gate** 🧼🧯: input filtering/sanitization layer that runs before Focus Mode calls an LLM.

### Definition of done (for this README)
- [x] Front-matter complete + aligned to v13 protocols
- [x] Pipeline ordering stated and testable
- [x] Evidence triplet + staging rules stated and testable
- [x] CI gates listed and repeatable
- [x] Governance + FAIR/CARE + sovereignty posture is explicit
- [x] Focus Mode (Ollama) tests/policies described (citations + safety)
- [x] Test lanes documented with runnable commands

---

<details>
<summary><b>🧭 Table of contents</b></summary>

- [🔗 Quick links](#-quick-links)
- [🚦 Non‑negotiables](#-non-negotiables)
- [🚀 Quickstart](#-quickstart)
- [🧩 KFM test matrix](#-kfm-test-matrix-subsystems--what-to-assert)
- [🧠 Core invariant: governed ordering](#-core-invariant-governed-ordering)
- [🗂️ Evidence triplet & staging invariants](#️-evidence-triplet--staging-invariants-raw--work--processed)
- [🧱 Architecture boundary tests](#-architecture-boundary-tests-clean-architecture)
- [🤖 Agentic QA workflows](#-agentic-qa-workflows-watcherplannerexecutor)
- [🔺 Test pyramid](#-test-pyramid-how-we-keep-velocity--confidence)
- [🏷️ Test categories & markers](#️-test-categories--markers-suggested)
- [🧰 Tool & CLI contract tests](#-tool--cli-contract-tests)
- [📄 Docs, Story Nodes, & Focus Mode validation](#-docs-story-nodes--focus-mode-validation)
- [🧠 Focus Mode (Ollama) regression suite](#-focus-mode-ollama-regression-suite-rag--policy-gates)
- [📄 PDF & doc-portfolio hygiene](#-pdf--doc-portfolio-hygiene)
- [🧾 Contract & metadata tests](#-contract--metadata-tests)
- [🧾 Evidence manifests & run receipts](#-evidence-manifests--run-receipts-run_manifestjson)
- [🧷 Stable IDs & versioning tests](#-stable-ids--versioning-tests-dont-break-links)
- [📦 Packaging parity tests](#-packaging-parity-tests-geoparquet--pmtiles--cog)
- [📜 License, citation, & redistribution tests](#-license-citation--redistribution-tests)
- [✅ Data validation gates](#-data-validation-gates-fail-fast)
- [📡 Streaming & schema-drift tests](#-streaming--schema-drift-tests-watchers-planner)
- [🗺️ Geospatial tests](#️-geospatial-tests-gis-correctness)
- [🛰️ Remote sensing tests](#️-remote-sensing-tests-earth-engine--imagery)
- [🧊 3D / WebGL / 3D GIS tests](#-3d--webgl--3d-gis-tests)
- [🧠 Scientific & simulation validation](#-scientific--simulation-validation-scenario-runs)
- [📊 ML / stats tests](#-ml--stats-tests-dont-fool-yourself)
- [🧭 Ontology & semantic layer tests](#-ontology--semantic-layer-tests-prov-o--domain-ontologies)
- [🕸️ Graph tests](#️-graph-tests-neo4j--integrity)
- [🔎 Search/index tests](#-searchindex-tests-elasticsearch)
- [🛡️ API tests](#️-api-tests-fastapi--graphql)
- [🌐 Web / frontend tests](#-web--frontend-test-guidance)
- [📦 Offline packs & AR tests](#-offline-packs--ar-tests)
- [📦 Supply chain & artifact integrity](#-supply-chain--artifact-integrity-oci-oras-cosign-sbom)
- [📈 Performance & capacity tests](#-performance--capacity-tests-latency-throughput-cost)
- [🔐 Security, governance, & ethics tests](#-security-governance--ethics-tests-defensive)
- [🧾 Test artifacts & receipts](#-test-artifacts--receipts)
- [🗂️ Suggested folder layout](#️-suggested-folder-layout)
- [✅ CI gates](#-ci-gates-non-negotiable)
- [✅ PR checklist](#-pr-checklist-copypaste)
- [🧯 Troubleshooting](#-troubleshooting)
- [📚 Reference pointers](#-reference-pointers-project--library-index)
- [🕰️ Version history](#️-version-history)

</details>

---

## 🔗 Quick links

> Paths are relative to `tests/`. If your repo differs, treat these as the **target map** and document any deltas.

- 🧭 Repo overview: `../README.md`
- 📘 Master Guide (v13, canonical): `../docs/MASTER_GUIDE_v13.md`
- 🧾 Markdown protocol + staging rules (v13): `../docs/MARKDOWN_GUIDE_v13.md`
- 🧱 Architecture blueprints: `../docs/architecture/`
- ⚖️ Governance + ethics + sovereignty:
  - `../docs/governance/ROOT_GOVERNANCE.md`
  - `../docs/governance/ETHICS.md`
  - `../docs/governance/SOVEREIGNTY.md`
- 📦 Data lifecycle + catalogs (canonical locations per v13):
  - `../data/raw/` (immutable sources)
  - `../data/work/` (intermediate outputs)
  - `../data/processed/` (publishable outputs)
  - `../data/stac/{collections,items}/` (STAC boundary artifacts)
  - `../data/catalog/dcat/` (DCAT boundary artifacts)
  - `../data/prov/` (PROV lineage bundles)
- 🧬 Schemas registry: `../schemas/` *(STAC/DCAT/PROV/Story/UI/Telemetry contracts)*
- 🧰 Tools/validators (governed command surface): `../tools/` *(if present)*
- 📜 Policy pack (OPA/Conftest): `../tools/validation/policy/` *(if present)*
- 🧾 Run receipts / audits: `../data/audits/` *(run manifests, checksums — if present)*
- 🧠 Pipelines: `../src/pipelines/` *(ETL + transforms — canonical home)*
- 🕸️ Graph: `../src/graph/` *(Neo4j ingest, constraints, ontology bindings)*
- 🛡️ API boundary: `../src/server/` *(FastAPI + GraphQL; contracts live nearby)*
- 🤖 AI module (Focus Mode): `../src/ai/` *(retrieval, prompt templates, policy checks — if present)*
- 🌐 Web UI: `../web/` *(React/TS; MapLibre; Cesium — if enabled)*
- 📚 Story Nodes: `../docs/reports/story_nodes/{draft|published}/`
- 🧪 Methods & experiments (MCP): `../mcp/`

---

## 🚦 Non‑negotiables

These are KFM’s “must not regress” invariants. If any becomes false, **CI must block merge** 🚫✅

1) **Contract‑first:** schemas + API contracts are first‑class repo artifacts 🧾  
   - Breaking changes must be explicit, versioned, and tested.

2) **Catalog‑first:** nothing is “real” unless it’s cataloged (STAC/DCAT) and traceable (PROV) 🗂️🧬  
   - Catalogs are **boundary artifacts** consumed by graph/API/UI.

3) **Evidence triplet required (publish-grade):** **STAC + DCAT + PROV** must exist **before** downstream use 🧾🗂️  
   - If any piece is missing, the lane **fails closed**.

4) **Canonical ordering is enforced in tests** 🧱  
   **Raw → ETL → STAC/DCAT/PROV → Neo4j graph → APIs → UI → Story Nodes → Focus Mode**

5) **Raw data is immutable** 🧊  
   - Never overwrite `data/raw/**`. New versions are new files + new receipts.

6) **API boundary rule:** UI must never query PostGIS/Neo4j/Elastic directly 🔐  
   - Everything user-facing flows through the API boundary for redaction + policy enforcement.

7) **Determinism by default:** reruns should match unless inputs/configs change 🔁  
   - Stochastic code must be seeded and tested by **properties** (not exact values).

8) **Sovereignty + classification propagation:** outputs can’t be *less restricted* than inputs 🏷️🛡️  
   - “No downgrade” is a **gate**.

9) **Policy-as-code is a gate:** governance rules execute automatically (OPA/Conftest or equivalent) 📜🧱  
   - If policy evaluation is unavailable, the pipeline **fails closed**.

10) **No mystery nodes:** every graph node/edge traces back to catalog evidence IDs 🕸️🧾  
   - No undocumented facts in Neo4j.

11) **Focus Mode is advisory-only and evidence-backed** 🧠🧾  
   - Answers must include citations; prompt injection defenses must work; “no tools” is enforced by default.

12) **Run receipts exist for publish‑grade outputs:** publishable artifacts require receipts (manifests + hashes + PROV link) 🧾📎  
   - If you can’t answer “what produced this?”, you can’t publish it.

13) **No network in unit tests** 🚫🌐  
   - Record/replay, mock adapters, or cached fixtures only.

14) **Evidence over vibes:** failures must produce inspectable artifacts (logs, diffs, screenshots, receipts) 📎

15) **Docs are linkable + searchable:** governed docs must pass front‑matter + link checks 📄🔍  
   - PDF portfolios require extraction manifests (see below).

16) **Supply chain verifiable (release lane):** signatures + SBOMs must verify 🔏📦  
   - If verification can’t run, **do not ship**.

---

## 🚀 Quickstart

### 0) Preconditions (one‑time)
- 🐍 Python env ready (`venv`, `uv`, `conda`, etc.)
- 🌐 Node env ready (`npm`, `pnpm`, or `yarn`)
- 🐳 Docker installed *(recommended for integration parity)*
- 📜 Policy tooling *(optional but recommended)*: `conftest` / `opa`
- 🔏 Release tooling *(release lane)*: `cosign` + SBOM tools *(if enabled)*
- 🤖 Optional (AI lane): `ollama` runtime available *(or CI runs a smaller containerized model)*

### 1) Fast checks (developer loop ⚡)
```bash
# Python (fast)
pytest -q -m "not integration and not e2e and not slow and not perf"

# Web (fast — adapt to your repo)
npm test
```

### 2) Full suite (feature branch ✅)
```bash
pytest -q
pytest -q -m integration
npm run test:e2e
```

### 3) Integration tests with containers (preferred 🐳)
```bash
docker compose up -d --build
pytest -q -m integration
docker compose down -v
```

<details>
<summary>🧾 Command cheat sheet (copy/paste)</summary>

```bash
# Contracts only (API + schemas + catalogs)
pytest -q -m contracts

# Evidence triplet (STAC/DCAT/PROV) + staging rules
pytest -q -m catalogs

# Docs/story lint + story-node schema checks
pytest -q -m docs

# Policy pack (if enabled)
pytest -q -m policy

# Evidence receipts / run manifests
pytest -q -m receipts

# Geo sanity (CRS/geometry/raster)
pytest -q -m geo

# WebGL/3D sanity
pytest -q -m webgl

# Scientific + scenario validation (tolerance-based; deterministic)
pytest -q -m validation
pytest -q -m scenario

# Ontology / semantic layer
pytest -q -m ontology

# Graph slice
pytest -q -m graph

# Search/index (Elastic) contract checks
pytest -q -m search

# Streaming/watchers + schema drift
pytest -q -m streaming
pytest -q -m drift

# Offline packs / AR
pytest -q -m offline
pytest -q -m ar

# Supply chain verification (release-lane tests)
pytest -q -m supplychain

# Performance/capacity (usually scheduled)
pytest -q -m perf

# Defensive security + governance checks
pytest -q -m security
pytest -q -m governance

# Focus Mode / AI contract tests
pytest -q -m focus
pytest -q -m ollama
pytest -q -m promptgate
```
</details>

---

## 🧩 KFM test matrix (subsystems + what to assert)

KFM is layered (clean boundaries). Tests should **pin the seams** 🔩:

| 🧱 Subsystem | 🎯 What must never break | 🧪 Best test types | 🧰 Typical tools |
|---|---|---|---|
| 🧰 Tools/CLIs | governed command surface: `--help`, safe defaults, stable exit codes, structured logs | unit ✅ + smoke ✅ | pytest, subprocess, snapshot tests |
| 🧪 ETL / pipelines | deterministic outputs, idempotent reruns, schema+CRS correctness | unit ✅ + integration 🔌 + QA gates ✅ | pytest, GeoPandas, GDAL, validators |
| 🧊 Raw intake | raw immutable + source manifest present | contracts 🧾 + integration 🔌 | hashing, manifest validators |
| 🗂️ Catalogs (STAC/DCAT/PROV) | boundary artifacts exist *before* graph/UI uses data; links resolve; provenance complete | contracts 🧾 + integration 🔌 | jsonschema, jq, custom validators |
| 🧾 Receipts (run manifests) | publish-grade outputs have manifest + hashes + PROV link | contracts 🧾 + integration 🔌 | pydantic, canonicalization, hashing |
| 📜 Policy pack | governance rules executable + fail closed (including AI answer checks) | unit ✅ + integration 🔌 | OPA, Conftest, Rego tests |
| 🗃️ Data stores | PostGIS/Neo4j/Elastic integration is gated + reproducible | integration 🔌 | Docker, migrations, fixtures |
| 🕸️ Graph (Neo4j) | derived truth from catalogs; constraints + “no mystery nodes” | integration 🔌 + property tests 🧪 | Neo4j container, Cypher assertions |
| 🔎 Search index | results always cite sources; stable doc IDs + offsets | contracts 🧾 + integration 🔌 | Elastic test container, fixtures |
| 🛡️ API (REST/GraphQL) | contract stability, authz, deterministic pagination | contracts 🧾 + integration 🔌 | OpenAPI/GraphQL validation, TestClient |
| 🌐 UI (SPA) | map/timeline/story correctness, a11y, bookmarkable state | unit 🧩 + component 🧱 + e2e 🧭 | Vitest/Jest, Playwright |
| 🧊 Maps / 3D | symbology + overlays don’t silently shift; perf budgets | visual 🖼️ + e2e 🧭 | screenshot diffs, WebGL harness |
| 📚 Story Nodes | citations resolve; narrative ordering consistent; no unsourced claims | docs ✅ + contracts 🧾 | markdown/link validators, schema checks |
| 🎯 Focus Mode (AI) | provenance-linked outputs; safe refusals; uncertainty honesty | eval ✅ + contract-like 🧾 | golden prompts, retrieval tests |
| 🤖 Agents (W‑P‑E) | agents never bypass policy; kill-switch works; PRs traceable | integration 🔌 + security ✅ | sandboxed runners, policy gates |
| 📦 Offline packs | pack integrity, included licenses, sensitivity enforcement | integration 🔌 + contracts 🧾 | manifest validation, hashing |
| 🔏 Supply chain | released artifacts are verifiable (signatures + SBOM) | integration 🔌 + release lane ✅ | cosign, SBOM tools, ORAS |
| 📈 Performance | latency/throughput regressions visible & explainable | perf ⏱️ + scheduled ✅ | pytest-benchmark, k6, Locust |

---

## 🧠 Core invariant: governed ordering

> [!IMPORTANT]
> KFM enforces a **non‑negotiable** pipeline order with a “Detect → Validate → Promote” mentality:
>
> **Raw Sources → ETL → STAC/DCAT/PROV → Neo4j graph → APIs → UI → Story Nodes → Focus Mode**

```mermaid
flowchart LR
  subgraph Data
    A[🧊 Raw Sources] --> B[🧪 ETL + Normalization]
    B --> C[🗂️ STAC Items + Collections]
    C --> D[🏷️ DCAT Dataset Views]
    C --> E[🧬 PROV Lineage Bundles]
  end

  C --> G[🕸️ Neo4j Graph (references back to catalogs)]
  G --> H[🛡️ API Layer (contracts + redaction)]
  H --> I[🌐 Map UI — React · MapLibre · (optional) Cesium]
  I --> J[📚 Story Nodes (governed narratives)]
  J --> K[🎯 Focus Mode (provenance-linked context bundle)]

  C --> R[🧾 Run Receipts]
  R --> G
```

### ✅ What tests should enforce (practically)
- 🧊 Raw immutability + source manifests present
- 🧪 ETL determinism (stable IDs/hashes; idempotent reruns; explicit versions)
- 🗂️ Catalog records exist **before** graph/UI uses them
- 🧾 Evidence triplet exists for publish-grade datasets (STAC/DCAT/PROV)
- 🧾 Run receipts exist for publish-grade outputs (run manifests + hashes + PROV link)
- 🕸️ Graph loads only from catalogs (no ad‑hoc inserts in prod paths)
- 🕸️ Graph has **no mystery nodes** (every node/edge has a catalog reference)
- 🛡️ API is the only client boundary (UI never queries DB/search directly)
- 📜 Policy pack enforces governance (licenses, classification, access controls)
- 🔐 Classification/sensitivity never downgrades silently (requires audited redaction)
- 📚 Story Nodes are governed (no uncited “facts”)
- 🎯 Focus Mode is advisory, evidence-backed, refusal-capable, policy-checked

---

## 🗂️ Evidence triplet & staging invariants (raw → work → processed)

Per v13, KFM’s data lifecycle must be explicit and testable:

- `data/raw/<domain>/...` 🧊 immutable source intake  
- `data/work/<domain>/...` 🧪 intermediate reproducible steps  
- `data/processed/<domain>/...` ✅ publish-grade outputs  
- Catalog “boundary artifacts” must land in canonical paths:
  - `data/stac/{collections,items}/` 🗂️
  - `data/catalog/dcat/` 🏷️
  - `data/prov/` 🧬

> [!IMPORTANT]
> A dataset is not considered “published” in KFM until the **evidence triplet** exists:
> **STAC + DCAT + PROV** (and it passes policy + schema checks).  [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-Qj23Z329hf1Q1WD86hXYfL)

### ✅ Test assertions (recommended)
- `test_raw_never_overwritten()` 🧊
- `test_raw_has_source_manifest()` *(e.g., `source.json` / source inventory)* 🧾
- `test_processed_has_evidence_triplet()` *(STAC/DCAT/PROV present + linked)* 🧬
- `test_triplet_links_resolve()` *(STAC assets exist, DCAT distributions real, PROV references inputs)* 🔗
- `test_no_publish_without_triplet()` *(fail-closed gate)* 🔒

### 🧪 Example (high-value fixture)
Use a tiny “toy domain” fixture (safe + synthetic) that produces:
- 1 GeoParquet vector output
- 1 PMTiles vector tiles output
- 1 STAC Item + DCAT record + PROV bundle
- 1 run receipt with hashes

This lets you test the entire boundary without big data costs.

---

## 🧱 Architecture boundary tests (clean architecture)

KFM stays maintainable only if boundaries are enforced 🧱✨

### ✅ What to test
- **Dependency direction rules** (domain → service → adapters; never reverse)
- **No cross-layer shortcuts** (UI never imports DB clients; pipelines don’t import UI)
- **API boundary is the redaction/policy choke‑point** (UI never bypasses it)  [oai_citation:2‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-P4zHoJicw1HG6bXmqFygG8)
- **“Independently testable components” stays true** (isolated unit tests remain possible)

### 🔧 Suggested patterns
- 🧭 Import-lints that fail forbidden imports (Python)
- 🧱 TS boundary rules so UI can’t reach server internals
- 🔌 Contract-only integration tests so adapters can be swapped

> [!TIP]
> Boundary tests are cheap insurance. They prevent “just this once” coupling that becomes permanent. 🧯

---

## 🤖 Agentic QA workflows (Watcher–Planner–Executor)

KFM supports agent-assisted maintenance (data QA, catalog hygiene, doc/story validation).  
Treat agents as **high-risk boundaries** that must be fenced by tests.

### 🧠 Mental model
- 👀 **Watcher** detects drift (missing metadata, failing links, policy violations, stale indexes, schema mismatches)
- 🧩 **Planner** proposes tasks (ranked + scoped + governed)
- 🛠️ **Executor** makes changes **only through PRs** (never direct writes to protected branches)

### ✅ Non‑negotiable agent controls (testable)
- 🧯 Kill-switch disables all agent actions
- 🧾 Receipt-first: every action emits a structured receipt (inputs + decision + outputs)
- 🧱 Policy-first: agent outputs run through the same contract + policy gates as humans
- 🧑‍⚖️ No autonomous merge
- 🧰 Scoped diffs: PRs limited to declared scope

### 🧪 Test patterns (suggested)
- `test_agent_kill_switch_blocks_actions()`
- `test_agent_only_opens_prs_never_pushes_main()`
- `test_agent_receipt_schema_valid()`
- `test_agent_changes_fail_when_policy_fails()`
- `test_agent_does_not_weaken_classification()` *(no downgrade)*

> [!CAUTION]
> Agents must never become a “back door” around governance.  
> If the policy pack can’t run, **agents must halt** (fail closed). 🔒

---

## 🔺 Test pyramid (how we keep velocity + confidence)

```text
          🔺 E2E (few)          → critical user journeys (UI + API + DB)
        🔺🔺 Integration (some)  → services together (DB, API, pipelines, AI policy checks)
      🔺🔺🔺 Unit (many)          → pure logic, transforms, validators
```

---

## 🏷️ Test categories & markers (suggested)

### Python (`pytest`) markers
Keep markers stable so devs can run focused slices quickly:

```ini
# pytest.ini (example)
[pytest]
markers =
  unit: fast pure logic
  integration: hits db/services/filesystem
  e2e: end-to-end journeys (rare for python)
  slow: long-running tests (non-gating)
  perf: benchmarks/capacity (usually scheduled)

  contracts: schemas + catalogs + API contract validation
  catalogs: evidence triplet (STAC/DCAT/PROV) + staging rules
  docs: markdown/front-matter/story-node validation
  pdf: PDF hygiene (searchable text layer / portfolios)

  receipts: run_manifest + hashes + receipts validation
  policy: OPA/Conftest policy pack execution and tests
  governance: license/classification/redaction/sov enforcement checks

  geo: GIS correctness checks
  eo: earth-observation / remote-sensing checks
  webgl: WebGL context + render sanity checks
  ar: AR overlay checks (if enabled)
  offline: offline pack packaging + integrity
  supplychain: artifact signature/SBOM/OCI verification (release lane)
  oci: ORAS/OCI artifact registry checks

  graph: Neo4j integrity + constraints + rebuild invariants
  ontology: semantic/ontology coherence checks (if used)
  search: Elasticsearch/index coherence checks (if used)

  streaming: watchers / real-time ingestion checks
  drift: schema drift detection + migration plan checks
  scenario: deterministic scenario simulator / replay lane

  api: API behavior checks (beyond schema)
  security: defensive security checks (no offensive testing)
  focus: Focus Mode contract tests (provenance + safety + uncertainty)
  ollama: Focus Mode regression tests using Ollama backend (optional in CI)
  promptgate: input filtering/prompt-injection defenses
  rag: retrieval pipeline correctness (graph+search+vectors)
  a11y: accessibility checks (docs + UI where applicable)
```

### Web tags (examples)
- Jest/Vitest: `test`, `test:unit`, `test:component`
- Playwright/Cypress: `test:e2e`
- Visual regression: `test:visual`
- Accessibility: `test:a11y`

---

## 🧰 Tool & CLI contract tests

KFM’s **governed toolchain** (`tools/`) is part of the contract surface. Tools must behave predictably.

### ✅ What to assert for every CLI tool
- `--help` exists + includes **≥2 examples**
- `--version` returns stable value (semver or git SHA)
- safe-by-default (no writes unless `--apply`, or `--dry-run` default)
- stable exit codes (usage vs validation failure vs runtime failure)
- structured logs available (human + JSONL mode)
- **idempotency for ingest/watchers:** reruns do not duplicate outputs
- if tool emits artifacts: **receipt + hashes** are written

### 🔧 Suggested tests (patterns)
- `test_tools_help_smoke()`
- `test_tools_version_smoke()`
- `test_tools_dry_run_does_not_mutate()`
- `test_tools_exit_codes_are_stable()`
- `test_tools_json_logs_valid_jsonl()`
- `test_watchers_are_idempotent()`

> [!TIP]
> Core logic should live in `src/`; `tools/` should be a predictable wrapper layer 🛠️

---

## 📄 Docs, Story Nodes, & Focus Mode validation

KFM treats docs + narrative as governed artifacts (not “freeform notes”).

### ✅ Docs validation should cover
- YAML front‑matter present + valid (per Markdown Protocol)
- required sections exist (template compliance where applicable)
- internal link checks (`docs/**`, `data/**`, `schemas/**`)
- images/assets exist + have alt text (a11y)
- citations/refs resolve (story exports + layer attributions)

### ✅ Story Nodes validation should cover
Story Nodes are a **paired artifact**:
- a Markdown narrative (text/media/citations)
- a JSON “script” describing map/timeline state per slide/section  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-VgLA7nv34M5muqZ5MQxBLG)

**Checks we enforce:**
- lives under `docs/reports/story_nodes/{draft|published}/...`
- Markdown front-matter + Story Node schema fields validate
- JSON script validates (schema + required keys)
- **timeline correctness:** JSON slide times align with dataset temporal extents
- citations resolve to cataloged sources (STAC/DCAT/PROV IDs)
- narrative claims do **not** introduce uncited “facts”
- published stories have stricter gates than drafts (policy + link + citation)

### ✅ Focus Mode contract tests should cover
- UI sends question + map context; server returns **structured answers with citations**  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide).pdf](file-service://file-MbEYbsLWBmpXVYXVF79c38)
- retrieval uses governed sources (Neo4j + search index + catalogs)
- refusal behavior works when evidence is missing
- uncertainty is surfaced (“unknown”, intervals, or confidence notes)
- no sensitive leakage (classification enforcement end-to-end)
- explainability hooks: “audit” panel shows evidence set used (where implemented)

> [!CAUTION]
> If a Story Node (or Focus Mode output) could expose sensitive locations or culturally sensitive information:  
> CI should flag it for governance review and block publish until review completes 🔒

---

## 🧠 Focus Mode (Ollama) regression suite (RAG + policy gates)

Focus Mode’s backend pipeline is explicitly staged:

**Parse Intent → Retrieve Knowledge (Neo4j/PostGIS/Search/Vectors) → LLM Generate (Ollama) → Governance Check (OPA) → Answer (with citations)**  [oai_citation:5‡KFM AI Infrastructure – Ollama Integration Overview.pdf](file-service://file-HCn72HddNvaaXqpJL4svTv)

### ✅ What to test (must-pass for governed lanes)
#### 1) Prompt Gate (input sanitization) 🧼🧯
- strips/escapes prompt-injection patterns
- blocks disallowed requests (e.g., private data requests)
- normalizes inputs safely (no control chars / unsafe markdown)

Suggested tests:
- `test_prompt_gate_strips_ignore_instructions()`
- `test_prompt_gate_blocks_sensitive_requests()`
- `test_prompt_gate_is_deterministic()`

#### 2) “No tools by default” sandbox 🔒
- model has **no direct internet/filesystem/tool access** unless explicitly enabled
- allow/deny lists enforced (default deny)  [oai_citation:6‡KFM AI Infrastructure – Ollama Integration Overview.pdf](file-service://file-HCn72HddNvaaXqpJL4svTv)

Suggested tests:
- `test_focus_mode_default_toollist_empty()`
- `test_focus_mode_rejects_tool_call_syntax()`

#### 3) Evidence + citation enforcement 🧾
- answers include citation markers (e.g., `[1] [2]`) mapped to a reference list
- policy check fails/rewrites/blocks if citations missing
- every referenced source resolves to catalog/graph/document IDs  [oai_citation:7‡KFM AI Infrastructure – Ollama Integration Overview.pdf](file-service://file-HCn72HddNvaaXqpJL4svTv)

Suggested tests:
- `test_ai_answer_has_citations()`
- `test_ai_answer_citations_resolve()`
- `test_ai_answer_blocked_when_no_citations()`

#### 4) Role-aware governance 🔐
- restricted sources never appear in public answers
- redaction/generalization rules apply consistently
- caching does **not** leak restricted context between sessions/users  [oai_citation:8‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-P4zHoJicw1HG6bXmqFygG8)

Suggested tests:
- `test_focus_mode_public_role_filters_sensitive_sources()`
- `test_focus_mode_cache_partitioned_by_role()`

#### 5) Retrieval correctness (RAG) 🧠🔎
- graph grounding works (multi-hop chains are **from retrieved facts**, not hallucinated)
- search results include traceable pointers (doc IDs + offsets)
- vector embeddings index reproducible (idempotent ingestion)

Suggested tests:
- `test_retrieval_returns_expected_evidence_bundle()`
- `test_retrieval_multi_hop_is_traceable()`
- `test_vector_index_idempotent()`

> [!TIP]
> For CI: run **small** models or CPU-only Ollama mode for regression checks (smoke + policy), and keep “full model evals” as nightly.  [oai_citation:9‡KFM AI Infrastructure – Ollama Integration Overview.pdf](file-service://file-HCn72HddNvaaXqpJL4svTv)

---

## 📄 PDF & doc-portfolio hygiene

Some KFM PDFs are **PDF portfolios** (container PDFs with embedded files). Portfolios are convenient for distribution, but hostile to repo search/governance unless extracted.

### ✅ What to enforce
- PDFs in governed docs must be:
  - searchable (text layer present)
  - link-stable (file name + path stable)
  - extractable (no portfolio-only docs in governed paths unless accompanied by an extraction manifest)

### 🧪 Suggested tests
- `test_pdf_has_text_layer()` *(sample pages contain extractable text)*
- `test_pdf_portfolio_requires_extraction_manifest()` *(portfolio PDFs must ship with `*.extract.json`)*  
- `test_doc_assets_exist_and_are_linked()` *(no broken embeds)*

> [!NOTE]
> Several “library shelf” PDFs are portfolios (Adobe Reader hint inside). Treat them as **libraries** and keep them out of governed lanes unless extracted & indexed.  
> (See reference section for the current shelf list.) 📚🗂️

---

## 🧾 Contract & metadata tests

KFM is contract-first and catalog-first. Tests must protect:

- 🛡️ OpenAPI / GraphQL contracts (breaking changes explicit + versioned)  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-Qj23Z329hf1Q1WD86hXYfL)
- 🗂️ STAC validity (collections/items required fields)
- 🏷️ DCAT validity (distributions point to real assets/endpoints)
- 🧬 PROV completeness (inputs → activities → outputs with run IDs/configs)
- 🔗 Cross-layer linkage (Graph references catalogs; UI references API; Story references catalogs)
- 🧑‍⚖️ Governance fields (license, sensitivity/classification, access constraints, FAIR/CARE notes)

### ✅ What to validate
- JSON parses + schema passes
- links resolve (STAC assets exist; DCAT distributions point somewhere real)
- provenance completeness (raw → work → processed trace exists)
- stable IDs/hashes present where required
- time metadata plausible + consistent (windows applied; no impossible intervals)
- “no deprecations” (policy can reject deprecated endpoints/layers)

---

## 🧾 Evidence manifests & run receipts (`run_manifest.json`)

KFM treats runs as first-class, auditable events.  
If an output can be published, it should have a machine-validated receipt.

### ✅ Minimum receipt contents
- `run_id` (stable unique ID)
- `pipeline_id` / `stage`
- `git_sha` / build identifier
- `started_at` / `ended_at`
- `inputs[]` with stable IDs + checksums
- `outputs[]` with stable IDs + checksums
- `config` (or hash of config)
- `environment` (recommended: versions, container digest)
- `canonical_digest` (recommended): digest of canonicalized manifest JSON
- `idempotency_key` (recommended for watchers + streaming)

### 🧪 Suggested tests
- `test_run_manifest_schema_valid()`
- `test_run_manifest_references_real_catalog_entities()`
- `test_run_manifest_outputs_have_hashes()`
- `test_run_manifest_canonical_digest_matches()`
- `test_streaming_idempotency_key_prevents_duplicates()`

---

## 🧷 Stable IDs & versioning tests (don’t break links)

Stable IDs keep KFM citable, reversible, and auditable 🧷🧾

### ✅ What to test
- IDs remain stable across refactors
- IDs don’t depend on display names alone
- dedup/merge doesn’t silently rewrite public identifiers (requires migration record)
- published artifacts remain fetchable by prior IDs (redirect or alias map)

### 🔧 Suggested patterns
- golden ID fixtures (expected IDs must not change)
- migration tests (schema bumps include migrations + compatibility tests)
- round-trip tests (catalog → graph → API → UI uses same stable IDs everywhere)

---

## 📦 Packaging parity tests (GeoParquet + PMTiles + COG)

Many KFM layers are expected to ship in **multiple publish formats** (example pattern: GeoParquet for analysis + PMTiles for UI performance) plus catalogs + receipts.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap.pdf](file-service://file-J9i6fUc35zPWB2U62zUnEN)

### ✅ What to test
- **Schema parity:** GeoParquet columns == PMTiles feature properties (allowed deltas must be documented)
- **Extent parity:** bbox/time range match across outputs (within tolerance)
- **ID parity:** stable dataset IDs shared across formats and referenced by STAC/DCAT/PROV
- **Tile sanity (PMTiles):** expected min/max zoom, tile bounds, metadata present
- **Raster sanity (COG):** overviews present, internal tiling, nodata metadata, predictable compression
- **Round-trips:** load GeoParquet → derive tiles → compare sample features ↔ tiles

Suggested tests:
- `test_geoparquet_schema_stable()`
- `test_pmtiles_metadata_present()`
- `test_geoparquet_pmtiles_parity_sampled()`
- `test_cog_has_overviews_and_is_cloud_optimized()`

> [!TIP]
> Keep parity tests sampled + deterministic (e.g., fixed feature IDs) so CI stays fast ✅

---

## 📜 License, citation, & redistribution tests

Licensing is a publish gate 📜✅

### ✅ What to test (gating)
- every dataset/distribution has a license before publish
- license terms aren’t contradictory across STAC/DCAT/local metadata
- restricted/non-commercial datasets trigger warnings + access controls
- attribution/citation generation works (story export includes sources)
- `CITATION.cff` exists for software releases (recommended)

### 🔧 Suggested patterns
- `test_license_required_before_publish()`
- `test_noncommercial_blocks_public_download()`
- `test_story_export_includes_attributions()`
- `test_layer_provenance_panel_has_license()` *(UI/contract test if implemented)*

> [!IMPORTANT]
> If a license is unclear, treat it as **restricted** until governance resolves it. 🧯

---

## ✅ Data validation gates (fail fast)

These gates are your “no‑bad‑data firewall” 🧱🔥 — especially for **GeoParquet + PMTiles/COG publish flows**.

### Ring model (recommended)

**Ring 0: Structure**
- parses (JSON/GeoJSON/Parquet/TIFF/PMTiles)
- schema validation (STAC/DCAT/PROV + local schemas)
- required files exist

**Ring 1: Integrity**
- checksums/manifest inventory
- deterministic IDs present
- atomic publish (no half-state)

**Ring 2: Semantics**
- CRS correctness + axis order
- geometry validity (and repair policy)
- raster sanity (nodata, overviews, alignment)
- time/bounds sanity

**Ring 3: Governance & safety**
- license required before publish
- classification propagation (no downgrade)
- sensitive fields redaction rules
- policy checks (OPA/Conftest)
- secrets + dependency hygiene

---

## 📡 Streaming & schema-drift tests (watchers, planner)

KFM supports “Watcher” patterns (polling feeds with ETag/Last‑Modified, producing immutable events and catalog entries) and planner-driven schema drift detection.

### ✅ What to test
- **Idempotency:** rerun does not duplicate observations
- **Caching correctness:** ETag/Last‑Modified prevents redundant pulls
- **Immutable event log:** unique event IDs; timestamped; source metadata
- **Catalog-first streaming:** streaming outputs still produce STAC Items (+ PROV)
- **Timeline replay correctness:** ordered, consistent replays
- **Governance propagation:** outputs inherit classification + license constraints
- **Schema drift handling:** planner produces migration plan or fails safely (no silent ingest)

### 🧪 Suggested patterns
- fixture feed snapshots with known ETag sequences
- property tests for time monotonicity + dedup keys
- drift fixtures where input schema changes across versions

---

## 🗺️ Geospatial tests (GIS correctness)

Geospatial pipelines fail in predictable ways—test them explicitly:

- 🌍 CRS sanity: EPSG correctness; meters vs degrees; axis order
- 🧱 topology: geometry validity; self-intersections per policy
- 🧩 overlay correctness: clip/intersect/union behaviors
- 🧭 buffer correctness: distance units + projection correctness
- 🧊 raster alignment: resolution, nodata handling, resampling method
- 📦 format IO: GeoJSON/GeoPackage/GeoParquet/COG/PMTiles round-trips
- 🧭 coordinate range checks: latitude/longitude valid ranges
- 🫥 sensitive geometry policy: generalization (point→hex/area) correct & enforced

---

## 🛰️ Remote sensing tests (Earth Engine & imagery)

Remote sensing workflows fail quietly unless assumptions are tested:
- band availability & naming
- scale/resolution
- cloud masking logic (QA bits)
- compositing rules
- index calculations (e.g., NDVI range sanity)

> [!CAUTION]
> Unit tests should not call live services. Prefer recorded fixtures or cached exports. ✅

---

## 🧊 3D / WebGL / 3D GIS tests

### ✅ What to test
- WebGL context sanity (creates reliably; fails gracefully)
- coordinate conventions (ECEF vs local ENU vs EPSG; axis order; units)
- LOD/tiling rules (no runaway payloads)
- georeferenced mesh validation (mesh ↔ CRS ↔ metadata alignment)
- visual regressions (snapshot diffs with tolerance)

> [!TIP]
> 3D can leak sensitive locations faster than 2D. Keep fixtures coarse + safe. 🫥🔒

---

## 🧠 Scientific / simulation validation (scenario runs)

Treat simulation code like a scientific instrument 🔬  
(KFM also adopts MCP-style experiment discipline: documented protocols, no raw overwrite, reproducible environments.)  [oai_citation:12‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

### ✅ Patterns
- analytical solution comparisons (tiny known cases)
- convergence tests (refinement reduces error)
- invariant checks (symmetry, conservation)
- tolerance-based golden files (with metadata + tolerances)
- uncertainty reporting checks (intervals, credible bands)

### 🎛️ Deterministic scenario runner (recommended lane)
If you implement a `kfm-sim-run` / scenario runner:
- freeze time
- seed RNG
- record/replay external calls (fixtures only)
- produce a run receipt + diff report (what changed + why)

> [!TIP]
> Stochastic tests should assert properties (ranges, quantiles), not exact numbers. 🎲✅

---

## 📊 ML / stats tests (don’t fool yourself)

- leak‑free splits (train/val/test)
- metrics stable within tolerance
- baselines exist (simple model beats random)
- diagnostics exist (calibration, residuals, drift)
- uncertainty reporting when relevant

📎 On failure, attach plots as CI artifacts:
- confusion matrix
- residual plots
- calibration curve
- drift dashboards

---

## 🧭 Ontology & semantic layer tests (PROV-O + domain ontologies)

### ✅ What to test
- PROV completeness: published dataset nodes link to PROV Activities with `run_id` + config hash
- temporal modeling consistency (no impossible intervals)
- geospatial semantics consistent/typed
- domain ontology alignment stays coherent

---

## 🕸️ Graph tests (Neo4j + integrity)

KFM treats the graph as **derived truth** (built from catalogs + provenance), not a write-anywhere scratchpad.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-P4zHoJicw1HG6bXmqFygG8)

### ✅ Test categories
- graph rebuild from catalogs is reproducible
- constraints: uniqueness, required properties, relationship rules
- “no mystery nodes”: every node/edge has catalog refs
- deterministic pagination & stable ordering at query layer
- bounded traversals (guardrails enforced)
- tiny deterministic graphs for algorithm sanity
- scheduled health checks produce a report artifact

Example assertions:
- “Graph contains only entities referenced by STAC/DCAT/PROV”
- “Every published dataset node links to a PROV Activity with run_id”
- “Ontology label set is from allowed registry (no mystery labels)”

---

## 🔎 Search/index tests (Elasticsearch)

If KFM uses full-text indexing (Elastic or equivalent), treat search as a governed surface.

### ✅ What to test
- indexed documents have stable IDs + source pointers (doc path, dataset IDs, offsets)
- search results include citations/refs (no “untraceable” snippets)
- filters respect classification (restricted docs do not appear for public roles)
- deterministic ranking where required (or stable tie-breakers)
- ingestion is idempotent (re-index doesn’t duplicate)

### 🧪 Suggested patterns
- small fixture corpus (docs + story nodes + catalog snippets)
- snapshot tests for query results (with stable ordering)

---

## 🛡️ API tests (FastAPI + GraphQL)

What to test:
- OpenAPI schema validation (breaking changes explicit)
- GraphQL schema validation + query safety (depth/complexity limits)
- AuthN/AuthZ: role-based access, classification enforcement
- pagination determinism: stable ordering, cursor correctness
- Geo correctness: GeoJSON validity; bbox correctness; CRS behavior
- CORS headers correct
- fail-closed for missing provenance/license (no ungoverned outputs)
- sensitive outputs: coordinate generalization/redaction enforced
- provenance surfaced: endpoints return source links (datasets/docs) where applicable  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-Qj23Z329hf1Q1WD86hXYfL)

---

## 🌐 Web / frontend test guidance

### 🧱 Component tests (fast)
- render correctness given props/state
- event handling correctness
- accessibility checks (labels, keyboard nav, contrast)

### 🔖 Bookmarkable URLs (reproducibility)
Because the UI represents state in URLs:
- test URL ↔ state round-trips (map view, time slider, active layers, story step)
- test share/reload reproduces the same view deterministically

### 🧭 E2E tests (few but powerful)
Focus on “money paths” 💸:
- auth/login
- load a layer **from catalog**
- timeline navigation updates map + panels (4D: space + time)  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-VgLA7nv34M5muqZ5MQxBLG)
- select feature → details panel updates
- provenance panel shows sources/licenses (if implemented)
- story playback drives map transitions correctly (Markdown + JSON script)  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-VgLA7nv34M5muqZ5MQxBLG)
- Focus Mode response renders with citations (footnotes clickable)  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide).pdf](file-service://file-MbEYbsLWBmpXVYXVF79c38)

### 🖼️ Visual regression (maps + WebGL)
Maps can regress visually while logic tests pass. Use screenshot diffs for:
- symbology stability
- overlay legibility at common zooms
- dark/light contrast
- Cesium/WebGL render sanity (tolerance diffs)

---

## 📦 Offline packs & AR tests

### ✅ Offline pack tests
- pack manifest schema valid
- included datasets have licenses + provenance
- hashing/integrity verifies (no tampering)
- sensitivity enforcement (restricted layers excluded/generalized)
- deterministic rebuild produces stable pack hash (within expected variance)

### ✅ AR overlay tests (if implemented)
- coordinate alignment sanity (CRS/units)
- graceful degradation on poor GPS (UX shows uncertainty)
- restricted location policies apply (AR must not reveal sensitive points)
- offline mode consistent with governance (no hidden restricted caches)

---

## 📦 Supply chain & artifact integrity (OCI, ORAS, Cosign, SBOM)

When KFM ships artifacts (containers, offline packs, published datasets, *and even models*), releases must be verifiable.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap.pdf](file-service://file-J9i6fUc35zPWB2U62zUnEN)

### ✅ What to test (release lane)
- signed artifacts verify (cosign or equivalent)
- SBOM exists for software artifacts (and optionally for data pack manifests)
- optional attestations/provenance exist (SLSA/Sigstore if enabled)
- artifact storage is content-addressable and reproducible:
  - ORAS/OCI registry pulls reproduce exact bytes
  - DVC pointers resolve to expected hashes
  - container images are versioned so old runs are reproducible

Suggested tests:
- `test_cosign_verify_image_digest()` 🔏
- `test_sbom_present_for_release_artifacts()` 📜
- `test_oras_manifest_includes_data_and_metadata()` 📦
- `test_dvc_pointers_resolve_to_expected_hashes()` 🧾

> [!IMPORTANT]
> Supply chain checks are not optional once you publish. If verification can’t run, **do not ship**. 🔒

---

## 📈 Performance & capacity tests (latency, throughput, cost)

### ✅ Minimum measurements
- latency distributions (p50/p95/p99)
- throughput under realistic concurrency
- error rates under load
- resource cost (CPU/RAM/IO) per request / per pipeline run
- DB query stability (EXPLAIN plan snapshots)
- (Optional) AI latency budgets (Focus Mode: retrieval + generation breakdown)  [oai_citation:19‡KFM AI Infrastructure – Ollama Integration Overview.pdf](file-service://file-HCn72HddNvaaXqpJL4svTv)

### 🕛 Where these run
- PRs: tiny perf smoke
- Nightly: full benchmarks + trend checks
- Release: publish-grade load profile

---

## 🔐 Security, governance, & ethics tests (defensive)

KFM’s security stance is defensive: prevent leaks, enforce policy, keep audit trails.

### ✅ What to test (defensive)
- classification boundaries & redaction rules enforced end-to-end
- secrets scanning (prevent committed tokens/keys)
- dependency scanning (vulns flagged)
- container scanning (base image CVEs flagged)
- FAIR/CARE gates (required metadata present; access constraints honored)
- auditability (publish actions produce receipts)
- sensitive location checks (no leakage via aggregations)
- safe subprocess usage (avoid `shell=True` with untrusted input)
- AI governance checks (citations required; disallowed content blocked)  [oai_citation:20‡KFM AI Infrastructure – Ollama Integration Overview.pdf](file-service://file-HCn72HddNvaaXqpJL4svTv)

> [!IMPORTANT]
> Do **not** add offensive security instructions here.  
> Security tests are for hardening, verification, and prevention. 🛡️✅

---

## 🧾 Test artifacts & receipts

When tests fail, make failures inspectable:

### ✅ CI artifacts to upload on failure
- structured logs (`.jsonl` / `.txt`)
- diffs (schema diffs, snapshot diffs)
- screenshots (UI E2E + map diffs)
- minimal STAC/DCAT/PROV bundles from fixtures
- performance traces (if relevant)
- run receipts (`run_manifest.json`, checksums, “what changed” summary)
- policy evaluation output (conftest/OPA logs)
- Focus Mode debug bundle *(retrieved context hash + prompt hash + policy decision — no sensitive text in public lanes)*

---

## 🗂️ Suggested folder layout

Adapt as needed, but keep intent obvious:

```text
📦 repo-root/
├─ 🧪 tests/
│  ├─ 📄 README.md
│  ├─ 🧷 fixtures/
│  │  ├─ 🧊 raw_intake/
│  │  ├─ 🗺️ geo/
│  │  ├─ 🛰️ eo/
│  │  ├─ 📡 streaming/
│  │  ├─ 🧊 3d/
│  │  ├─ 🔎 search/
│  │  ├─ 🧬 ml/
│  │  ├─ 🧾 catalogs/         # STAC/DCAT/PROV fixture triplets
│  │  ├─ 🧾 receipts/
│  │  ├─ 🤖 focus_mode/       # golden prompts + expected citation structure
│  │  └─ 📘 FIXTURES.md
│  ├─ 📄 docs/
│  ├─ 📄 pdf/
│  ├─ 🧱 architecture/
│  ├─ 🧰 tools_contract/
│  ├─ 📜 policy/
│  ├─ 🤖 agents/
│  ├─ 🧾 receipts/
│  ├─ 🧪 scenario/
│  ├─ 🐍 python/
│  │  ├─ 🧩 unit/
│  │  ├─ 🔌 integration/
│  │  ├─ ✅ validation/
│  │  ├─ ⏱️ perf/
│  │  ├─ 🔐 security/
│  │  ├─ 🤖 focus_mode/
│  │  └─ 🧱 conftest.py
│  ├─ 🕸️ graph/
│  │  ├─ 🔌 integration/
│  │  └─ 🧭 ontology/
│  ├─ 🔎 search/
│  ├─ 🌐 web/
│  │  ├─ 🧩 unit/
│  │  ├─ 🧱 component/
│  │  ├─ 🧭 e2e/
│  │  ├─ 🖼️ visual/
│  │  └─ ♿ a11y/
│  ├─ 📦 offline/
│  ├─ 🧊 ar/
│  ├─ 🔏 supply_chain/
│  │  ├─ 📦 oci/
│  │  ├─ 🔏 cosign/
│  │  └─ 📜 sbom/
│  └─ 📘 TEST_POLICY.md
└─ 📁 .github/
```

---

## ✅ CI gates (non-negotiable)

**Policy:** pipeline must be green before merge 🤖✅

### ✅ Minimum PR gates (recommended)
1) 🧹 format + lint (Python + JS/TS)
2) 🧱 build (frontend + backend; container build if applicable)
3) 🧪 unit tests
4) 📄 Markdown protocol checks (front‑matter + required sections)  [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
5) 🔗 link/reference validation (docs + story nodes)
6) 🧾 schema validation (STAC/DCAT/PROV + story schemas + telemetry/UI schemas)
7) 🧾 evidence triplet gate (STAC+DCAT+PROV present + linked) 🧬
8) 🧾 receipts validation (run manifests for publish outputs)
9) 📜 policy pack checks (OPA/Conftest) *(if enabled)*
10) ✅ data validation gates (CRS + geometry + raster sanity + license required)
11) 🔌 integration tests (ephemeral DB/services via Compose)
12) 🕸️ graph integrity tests (constraints + rebuild invariants + ontology checks)
13) 🛡️ API contract tests (OpenAPI/GraphQL + deterministic pagination)
14) 🔎 search index integrity (if enabled)
15) 🔐 security & governance scans (secrets + PII + sensitive location + “no downgrade”)
16) 🤖 Focus Mode policy checks *(citations required; prompt gate; no tools by default)*  
17) 🧑‍⚖️ CodeQL/static analysis lane (recommended)

### 🕛 Nightly / scheduled checks (recommended)
- perf benchmarks + trends
- deeper graph consistency (full rebuild + diff)
- streaming replay checks (24h timeline replay on fixtures)
- deeper security scanning
- supply-chain verification lane (release candidates)
- full-model Focus Mode evals (bigger models, broader golden set)

---

## ✅ PR checklist (copy/paste)

- [ ] Unit tests added/updated
- [ ] Integration tests added (if behavior crosses boundaries)
- [ ] Boundary tests updated (if you touched architecture seams)
- [ ] Raw intake rules respected (no overwrite; source manifest updated) 🧊🧾
- [ ] Evidence triplet produced/validated (STAC+DCAT+PROV) 🧬
- [ ] Determinism confirmed (seeds + stable outputs) if ML/sim/scenario
- [ ] Tools/CLI contract checks updated (if adding/modifying tools/)
- [ ] Docs/story checks updated (front‑matter, links, templates) if docs changed
- [ ] Contracts updated + verified (OpenAPI/GraphQL) if API changed
- [ ] Catalog/metadata tests updated (STAC/DCAT/PROV) if outputs changed
- [ ] Packaging parity checked (GeoParquet ↔ PMTiles ↔ COG where relevant) 📦
- [ ] Run receipts updated/validated (run_manifest + hashes) if publish outputs changed
- [ ] Policy pack checks pass (OPA/Conftest) if enabled
- [ ] Stable IDs preserved (or migration + ADR added) if identifiers changed
- [ ] Data validation gates updated (schema/CRS/geometry) if ETL changed
- [ ] License + governance checks pass (block publish if missing license)
- [ ] Sensitive location / “no downgrade” checks pass (or governance review requested)
- [ ] Focus Mode tests updated (prompt gate + citations + policy checks) 🤖🧾
- [ ] UI changes include component tests + (if visual) snapshot updates
- [ ] Bookmarkable URL/state round-trip tests updated (if map/story routing changed)
- [ ] Search/index tests updated (if indexing changed)
- [ ] Offline/AR tests updated *(if affected)*
- [ ] CI is green (required)

---

## 🧯 Troubleshooting

### ❌ Tests fail only in CI?
- check lockfiles & pinned versions
- confirm containers match local versions
- eliminate reliance on local paths, locale, timezone, GPU availability

### 🎲 Flaky tests?
- remove sleeps; wait on conditions
- fix randomness (seed)
- mock/record external services

### 🐳 Docker stack won’t start?
```bash
docker compose logs -f
docker compose config
docker compose up -d --build
```

### 🤖 Ollama lane failures?
- run policy-only Focus Mode tests first (`-m "focus and not ollama"`)
- use smaller model for CI smoke
- validate Prompt Gate and citation enforcement before model debugging  [oai_citation:22‡KFM AI Infrastructure – Ollama Integration Overview.pdf](file-service://file-HCn72HddNvaaXqpJL4svTv)

---

## 📚 Reference pointers (project + library index)

These project docs define what tests must protect (contracts, governance, UI trust surfaces, AI guardrails, and reproducible pipelines). Keep this list aligned with `docs/MASTER_GUIDE_v13.md`.

### 🧭 Authoritative KFM design docs (trust surface)
- 📚 Expanded Technical & Design Guide (architecture + onboarding)  [oai_citation:23‡📚 Kansas Frontier Matrix (KFM) – Expanded Technical & Design Guide.pdf](file-service://file-Tjmzn5F3sT5VNvVFhqj1Vo)
- 🧱 Architecture, Features, and Design (layering + evidence triplet)  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-Qj23Z329hf1Q1WD86hXYfL)
- 🧰 Comprehensive Technical Documentation (Story Nodes, 4D time slider, UI behaviors)  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-VgLA7nv34M5muqZ5MQxBLG)
- 🖥️ UI System Overview (Focus Mode UI workflow + map context injection)  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide).pdf](file-service://file-MbEYbsLWBmpXVYXVF79c38)
- 🧭 AI System Overview (governed graph + API boundary + policy enforcement)  [oai_citation:27‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-P4zHoJicw1HG6bXmqFygG8)
- 🤖 Ollama Integration Overview (Focus Mode pipeline + Prompt Gate + citation enforcement)  [oai_citation:28‡KFM AI Infrastructure – Ollama Integration Overview.pdf](file-service://file-HCn72HddNvaaXqpJL4svTv)
- 🧭 Platform Overview & Roadmap (OCI artifacts, reproducible pipeline images)  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap.pdf](file-service://file-J9i6fUc35zPWB2U62zUnEN)
- 🧾 Markdown Guide v13 (canonical staging + boundary artifact locations)  [oai_citation:30‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🧪 Research & reproducibility protocols (MCP-friendly)
- 🧪 Scientific Method / Research / Master Coder Protocol (experiment protocols, “never overwrite raw”, reproducibility checklists)  [oai_citation:31‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- 🗺️ Kansas-Frontier-Matrix Open-Source Design (georeferencing → COGs, OCR → knowledge base, MapLibre time slider)  [oai_citation:32‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

### 📚 Library shelf portfolios (extract before governance)
> These are useful “shelves” 📚 but many are **PDF portfolios** (embedded docs).  
> For governed usage: extract embedded PDFs and commit an extraction manifest.

- 🧠 AI Concepts & more (portfolio)  [oai_citation:33‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- 🗺️ Maps / Virtual Worlds / Archaeological / WebGL (portfolio)  [oai_citation:34‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- 🧰 Mapping + Modeling + Python + Git + Docker + GraphQL + Security (portfolio)  [oai_citation:35‡Mapping-Modeling-Python-Git-HTTP-CSS-Docker-GraphQL-Data Compression-Linux-Security.pdf](file-service://file-2QvRgQbts8ENJQSRC6oGme)
- 🧭 GIS + Security + R + SciPy + MATLAB + ArcGIS + Spark + TypeScript (portfolio)  [oai_citation:36‡Geographic Information-Security-Git-R coding-SciPy-MATLAB-ArcGIS-Apache Spark-Type Script-Web Applications.pdf](file-service://file-TH7HttQXn8Bh1hVhcj858V)
- 🧠 Data Management + Data Science + Bayesian Methods (portfolio)  [oai_citation:37‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
- 🧩 Various programming languages & resources (portfolio)  [oai_citation:38‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)

### 🧭 Doc-to-test crosswalk (what each doc changes in CI) ✅
| Doc / file | What it implies we must test | Where it lands |
|---|---|---|
| Expanded Technical & Design Guide | evidence-first + layering + “advisory-only AI” | `contracts/`, `governance/`, `focus/` |
| Architecture, Features, and Design | evidence triplet (STAC+DCAT+PROV) is required | `catalogs/`, `receipts/` |
| Comprehensive Technical Documentation | Story Nodes = Markdown + JSON; timeline/3D/AR behaviors | `docs/`, `web/e2e/`, `webgl/` |
| UI System Overview | Focus Mode UI sends map context; UI renders citations as footnotes | `web/e2e/`, `api/`, `focus/` |
| AI System Overview | API boundary + “no mystery nodes” + role-based redaction | `graph/`, `api/`, `policy/` |
| Ollama Integration Overview | Prompt Gate, citation enforcement, OPA governance check | `promptgate/`, `ollama/`, `policy/` |
| Platform Roadmap | OCI artifacts + reproducible pipeline images | `supply_chain/oci/`, `supplychain/` |
| Markdown Guide v13 | canonical staging paths + boundary artifact locations | `catalogs/`, `docs/` |
| MCP / Research Protocol | experiment protocols, repeatability, no raw overwrite | `scenario/`, `ml/`, `receipts/` |
| Library portfolios | must be extractable + searchable to be governable | `pdf/`, `docs/` |

<!--
Required tool citations (do not remove):
 [oai_citation:39‡📚 Kansas Frontier Matrix (KFM) – Expanded Technical & Design Guide.pdf](file-service://file-Tjmzn5F3sT5VNvVFhqj1Vo)  [oai_citation:40‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-VgLA7nv34M5muqZ5MQxBLG)  [oai_citation:41‡KFM AI Infrastructure – Ollama Integration Overview.pdf](file-service://file-HCn72HddNvaaXqpJL4svTv)
-->

---

## 🕰️ Version history

| Version | Date | Summary | Author |
|---:|---|---|---|
| v1.6.0 | 2026-01-26 | Integrated v13 staging rules (raw/work/processed) + “evidence triplet” (STAC+DCAT+PROV) gates; added Focus Mode (Ollama) regression lane (Prompt Gate, citation enforcement, OPA governance checks); added packaging parity guidance (GeoParquet ↔ PMTiles ↔ COG); expanded OCI/ORAS supply-chain tests; added doc-to-test crosswalk referencing core KFM design docs + MCP protocol + library portfolio hygiene. | KFM Engineering + KFM QA |
| v1.5.0 | 2026-01-26 | Aligned to v13 Markdown Protocol front‑matter; added PostGIS/Neo4j/Elasticsearch lanes; introduced search/index + drift + scenario markers; strengthened “no mystery nodes” graph invariant; expanded bookmarkable URL reproducibility tests; clarified CI gates (docs protocol + link validation + schema validation + governance scans); tightened defensive security notes (safe subprocess). | KFM Engineering + KFM QA |
| v1.4.0 | 2026-01-20 | Added agentic QA guardrails (Watcher–Planner–Executor), policy-pack lane (OPA/Conftest), run receipts (`run_manifest.json`) + canonical determinism guidance, streaming/watchers test lane, ontology/semantic layer checks, offline pack + AR test guidance, supply-chain verification lane (Cosign/SBOM), and PDF portfolio hygiene gates. | KFM Engineering |
| v1.3.0 | 2026-01-13 | Added architecture boundary tests, stable ID/versioning lane, explicit license/citation gates, 3D/WebGL/3D‑GIS testing guidance, and performance/capacity test lane. | KFM Engineering |
| v1.2.0 | 2026-01-11 | Aligned tests with Master Guide v13: contract-first + catalog-first gates, docs/story-node validation lane, governance trigger guidance, and tool/CLI contract testing. | KFM Engineering |
| v1.1.0 | 2026-01-09 | Tightened catalog-first & data QA gates; added receipts/artifacts section; clarified defensive security stance; aligned CI gates with KFM engineering/testing guidance. | KFM Engineering |
| v1.0.0 | 2026-01-07 | Initial repo-wide testing README: pyramid, markers, subsystem matrix, validation + governance posture. | KFM Engineering |