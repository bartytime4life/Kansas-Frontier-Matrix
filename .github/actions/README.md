---
title: "🧩 KFM GitHub Actions — Local Composite Actions & Reusable Workflows"
file: ".github/actions/README.md"
status: "Active ✅"
version: "v13"
last_updated: "2026-01-26"
classification: "public"
care_label: "none"
sensitivity: "low"
tags:
  - github-actions
  - composite-actions
  - reusable-workflows
  - provenance-first
  - stac
  - dcat
  - prov
  - sbom
  - sigstore
  - slsa
  - dsse
  - oras
  - policy-as-code
  - opa
  - conftest
  - dvc
  - geoparquet
  - pmtiles
  - ollama
  - rag
---

<a id="top"></a>

# 🧩 `.github/actions/` — Reusable GitHub Actions for Kansas Frontier Matrix (KFM)

[![CI](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)
[![Pages](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml)

![Composite Actions](https://img.shields.io/badge/actions-composite%20actions-informational)
![Reusable Workflows](https://img.shields.io/badge/actions-reusable%20workflows-informational)
![KFM v13](https://img.shields.io/badge/KFM-v13%20contract-6f42c1)
![Contract First](https://img.shields.io/badge/docs-contract--first-2ea44f)
![Evidence First](https://img.shields.io/badge/docs-evidence--first-0aa)
![VVUQ](https://img.shields.io/badge/science-V%26V%20%2B%20UQ-blue)
![FAIR%20%2B%20CARE](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-ff69b4)
![Provenance](https://img.shields.io/badge/provenance-STAC%20%7C%20DCAT%20%7C%20PROV-6f42c1)
![Supply Chain](https://img.shields.io/badge/supply--chain-SBOM%20%2B%20attestations-black)
![SLSA](https://img.shields.io/badge/supply--chain-SLSA%20provenance-blue)
![Sigstore](https://img.shields.io/badge/sigstore-cosign%20ready-brightgreen)
![OCI%20Artifacts](https://img.shields.io/badge/artifacts-OCI%20%2B%20ORAS-informational)
![Ollama](https://img.shields.io/badge/AI-Ollama%20%2B%20RAG-orange)
![Fail Closed](https://img.shields.io/badge/gates-default--deny%20%2B%20fail--closed-critical)

> 🧭 **What this folder is:** repo-local GitHub Actions (mostly **composite actions**) that standardize KFM’s CI/CD step-bundles so lanes stay consistent, auditable, and boring.  
> 🧾 **KFM north star:** trust first (**provenance + integrity**), then speed (**caching + parallel lanes**).  
> 🧬 **KFM evidence rule:** every dataset is a first-class citizen with a **catalog triplet** (**STAC + DCAT + PROV**) and intake is blocked when provenance/metadata is missing.  
> 🧱 **KFM v13 pipeline order (non‑negotiable):** **ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode**. Pipelines and actions must not “skip stages” or bypass governance.

> [!IMPORTANT]
> **Composite actions are infrastructure.** Treat them like production code:
> - least privilege 🔐
> - deterministic & idempotent outputs ♻️ *(same inputs/config → same outputs; reruns are no-ops)*
> - contract-first validation 🧾 *(schemas + profiles + API contracts)*
> - provenance-first artifacts 🔎 *(PROV + checksums + lineage)*
> - evidence-first narrative 📚 *(citations required; fact vs interpretation)*
> - sovereignty + classification propagation 🛂 *(no downgrades without review)*
> - default-deny promotion 🚦 *(fail-closed gates)*
> - PR-mediated automation only 🧯 *(no “agent writes to main”)*

---

## 🧾 Policy metadata

| Field | Value |
|---|---|
| File | `.github/actions/README.md` |
| Status | Active ✅ *(spec + operating guide)* |
| Last updated | **2026-01-26** |
| Canonical workflow docs | `.github/workflows/README.md` |
| Canonical security policy | `SECURITY.md` *(repo root)* or `.github/SECURITY.md` *(mirror)* |
| Canonical repository contract | `docs/MASTER_GUIDE_v13.md` *(expected path; v13 contract)* |
| Canonical docs protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` *(front-matter + DoD)* |
| Policy engine | `tools/validation/policy/` *(OPA/Conftest; default-deny)* |
| Evidence metadata (v13 canonical) | `data/stac/**` + `data/catalog/dcat/**` + `data/prov/**` *(STAC/DCAT/PROV)* |
| Evidence metadata (legacy/alias) | `data/catalog/stac/**` or `data/catalog/**` + `data/provenance/**` *(allowed only as migration targets; prefer v13 canonical)* |
| Large artifact versioning | `data/**` + `.dvc/**` *(DVC pointers; “no giant binaries in git”)* |
| AI infrastructure (local) | `docs/ai/` *(expected)* + `KFM AI Infrastructure – Ollama Integration Overview.pdf` *(library)* |
| Artifact publishing | `releases/**` + `tools/release/**` + OCI registry config *(ORAS/Cosign; signed artifacts)* |
| Automation posture | W‑P‑E (Watcher → Planner → Executor) under PR gates + kill-switch |

---

## ⚡ Quick links

| Need | Go |
|---|---|
| 🧭 Project overview | [`../../README.md`](../../README.md) |
| 🧪 Workflows hub (lanes + templates) | [`../workflows/README.md`](../workflows/README.md) |
| 🤝 GitHub ops hub | [`../README.md`](../README.md) |
| 🛡️ Security policy | [`../../SECURITY.md`](../../SECURITY.md) *(or* [`../SECURITY.md`](../SECURITY.md)*)* |
| 🧱 Master guide (repo contract) | `../../docs/MASTER_GUIDE_v13.md` *(expected path)* |
| 🧾 Standards & profiles | `../../docs/standards/` *(STAC/DCAT/PROV + markdown protocol)* |
| 🗃️ Library manifest | `../../docs/library/MANIFEST.yml` *(recommended; prevents “lost PDFs” drift)* |
| 🗂️ Data lifecycle roots | `../../data/raw/` · `../../data/work/` · `../../data/processed/` *(v13 canonical)* |
| 🧬 Catalog roots | `../../data/stac/` · `../../data/catalog/dcat/` · `../../data/prov/` |
| 🧑‍⚖️ Policy gates (OPA/Conftest) | `../../tools/validation/policy/` *(expected)* |
| 🤖 AI infra (Ollama) | `../../docs/ai/` *(expected)* |
| 🧬 SBOM action | [`./sbom/README.md`](./sbom/README.md) *(expected)* |
| 🖊️ Attest action | [`./attest/README.md`](./attest/README.md) *(expected)* |

> [!TIP]
> If a link 404s, this README still defines the **contract/spec** for what we expect to implement.  
> Please open an issue tagged `type:pipeline` + `area:ci` (+ `area:security` if relevant).

---

<details>
<summary><strong>📌 Table of contents</strong></summary>

- [🧭 Why <code>.github/actions/</code> exists](#why)
- [🧱 Where actions fit](#where)
- [🧭 Canonical pipeline ordering (v13 non‑negotiable)](#pipeline)
- [🧬 Detect → Validate → Promote (lane pattern)](#lane-pattern)
- [🧠 W‑P‑E automation contract (Watcher → Planner → Executor)](#wpe)
- [🤖 Focus Mode & Ollama guardrails (CI-aware)](#ollama)
- [🧭 KFM invariants (actions must not break)](#invariants)
- [🏗️ Layer boundaries & isolation](#layers)
- [🗺️ Repo structure alignment (v13 map)](#repo-map)
- [🗺️ Geospatial toolchain & runner strategy](#toolchain)
- [🔢 Versioning & compatibility contract](#versioning)
- [🧪 Scientific rigor (V&V + UQ + reproducibility)](#vvuq)
- [🔐 Threat model & trust boundaries (actions edition)](#threat-model)
- [🛂 Data classification & access control](#classification)
- [🧪 Minimum CI gates (v13 “hard rails”)](#ci-gates)
- [🗂️ Action catalog (recommended set)](#action-catalog)
- [✅ Action contract (inputs, outputs, artifacts)](#action-contract)
- [🎛️ Kill switch & safe defaults](#kill-switch)
- [🧾 Provenance, checksums, lineage, signing](#provenance)
- [📦 OCI artifacts & signed releases (ORAS + Cosign)](#oci)
- [🧪 Testing local actions](#testing)
- [🧷 Templates (copy/paste)](#templates)
- [🧑‍⚖️ Review checklist](#review-checklist)
- [📚 Project reference library](#reference-library)

</details>

---

<a id="why"></a>

## 🧭 Why `.github/actions/` exists

KFM workflows cover **code + data + metadata + graph semantics + narrative artifacts**. The same steps repeat everywhere:

- setup Python + Node (often with GIS deps like GDAL/PROJ)
- run lint/tests and emit artifacts
- validate governed **Markdown protocol** (front-matter + DoD)
- validate **STAC/DCAT/PROV** profiles (metadata is the contract)
- enforce “no mystery data”:
  - read from `data/raw/**`
  - write to `data/processed/**`
  - record lineage to `data/prov/**`
  - prohibit “ad‑hoc edits” to governed outputs
- enforce governed publishing (stage → validate → promote)
- capture run provenance (inputs → transforms → outputs)
- produce supply-chain evidence (SBOM + attestations + SLSA provenance)
- enforce classification propagation (no “public outputs” from restricted inputs)
- optionally package artifacts as **OCI** (ORAS) and sign them (Cosign)

**Composite actions standardize those sequences once** and reuse them across workflows without YAML drift.

> [!NOTE]
> Design rule:
> - ✅ **Composite action** = repeatable *step bundle* (“setup + run tool + upload report”)
> - ✅ **Reusable workflow** = repeatable *lane/pipeline* (“PR lane”, “nightly integration”, “release lane”)
> - ✅ **Tool/CLI (in `tools/` or `src/`)** = repeatable *domain logic* (ETL, catalog QA, provenance emission)

---

<a id="where"></a>

## 🧱 Where actions fit

```mermaid
flowchart LR
  PR[📦 PR / commit] --> WF[🧪 workflow lane]
  WF --> ACT[🧩 local composite actions]
  ACT --> TOOLS[🧰 repo tools & scripts]
  TOOLS --> OUT[📦 artifacts / reports / catalogs]
  WF --> ENV[🔐 environments & publish controls]
```

**Text version:** PR triggers workflow → workflow calls local actions → actions call repo tools/scripts → tools produce artifacts → workflow publishes artifacts *(only in protected lanes)*.

> [!IMPORTANT]
> Actions are “glue.” Keep KFM domain logic in `tools/` / `src/` so it can be unit-tested and reused outside GitHub Actions.

---

<a id="pipeline"></a>

## 🧭 Canonical pipeline ordering (v13 non‑negotiable)

KFM is intentionally staged so **governance is enforceable and testable**.

```mermaid
flowchart TD
  RAW[📥 ETL<br/>data/raw/**] --> CAT[🗂️ Catalogs<br/>STAC + DCAT + PROV]
  CAT --> GRAPH[🧠 Graph ingest<br/>refs, not duplicates]
  GRAPH --> API[🔌 API boundary<br/>permissions + redaction + provenance injection]
  API --> UI[🗺️ UI<br/>Map + Story + Search]
  UI --> STORY[📚 Story Nodes<br/>structured narrative]
  STORY --> FOCUS[🤖 Focus Mode<br/>RAG + policy checks]
```

### What actions must enforce ✅
- **Catalogs before graph:** graph nodes reference canonical catalog records; don’t “invent” metadata downstream.
- **API as last-mile governance:** UI (and AI) consume APIs only; no direct DB/file access.
- **Story Nodes are ingestible artifacts:** narrative is structured, versioned, and validated like data.
- **Focus Mode is advisory-only:** it reads governed sources and returns answers with citations/links, but does not mutate state.

> [!TIP]
> Treat each stage boundary like a *sealed lab instrument* 🔬: the stage emits artifacts, hashes them, and records provenance so the next stage cannot quietly change history.

---

<a id="lane-pattern"></a>

## 🧬 Detect → Validate → Promote (lane pattern)

KFM treats pipelines like scientific instrumentation: **observe → record → verify → publish** 🔬🧾

```mermaid
sequenceDiagram
  participant D as 👀 Detect
  participant V as ✅ Validate
  participant P as 🚦 Promote
  participant R as 🏷️ Release/Publish

  D->>V: open PR with proposed changes + evidence artifacts
  V->>V: run schema + policy + QA gates (default deny)
  V-->>P: only if gates pass ✅
  P->>R: publish artifacts (protected lane only)
```

### What this means for actions ✅
- Actions must be safe in PR lanes (**no secrets**, least privilege).
- Validation actions must be **fail-closed** when used as promotion gates.
- Promotion lanes should require evidence artifacts (minimum set):
  - SBOM present 🧬
  - provenance present 🧾
  - checksums present 🔒
  - SLSA provenance present 🧷
  - policy gate pass ✅ (OPA/Conftest)
  - classification checks pass 🛂
  - (optional) OCI packaging + signature verified 🧾🔏

> [!CAUTION]
> Any automation (human or agent) must flow through PRs and validation gates.  
> **No direct writes to `main`** for governed outputs.

---

<a id="wpe"></a>

## 🧠 W‑P‑E automation contract (Watcher → Planner → Executor)

KFM uses a **Watcher–Planner–Executor** mindset for safe automation:
- **Watcher** detects new data/changes (prefer ETag/Last-Modified; avoid redundant downloads).
- **Planner** decides *what to run*, and checks it won’t violate policy.
- **Executor** runs in an isolated environment, produces artifacts + evidence, and reports status.

### Guardrails that actions must support 🧯
- A global **kill switch** (fail closed for publish lanes).
- Policy packs are **versioned + auditable** (no “silent rule changes”).
- Outputs always include: `report.json` + `summary.md` + checksums + provenance hooks.
- (If AI is involved) **input filtering** + **tool allow/deny lists** + **output policy checks**.

---

<a id="ollama"></a>

## 🤖 Focus Mode & Ollama guardrails (CI-aware)

KFM’s AI layer is designed to be **local-first** and **policy-controlled** (Ollama as the model runtime), with RAG anchored in governed catalogs/graph/story content.

### 🧠 Focus Mode pipeline (high level)
1) **Parse / classify intent** (question type, scope, classification)
2) **Retrieve** context (graph + catalogs + story nodes + documents)
3) **Generate** response (LLM)
4) **Governance check** output (OPA policy evaluation + citation requirements)
5) **Return** answer with **citations/links** to sources (and disclaimers when needed)

### ✅ What CI should test (minimal)
- **Prompt gate** / input filtering blocks obviously unsafe requests (and prompt-injection patterns).
- **Tool allow/deny lists** are enforced (no internet, no filesystem mutation, no “exfil tools”).
- **Output policy checks** pass/fail deterministically (e.g., citation rules, classification constraints).
- **AI regression tests** for “known questions” produce:
  - required citations ✅
  - no restricted data leaks 🛂
  - stable formatting expectations (within tolerance) ♻️

> [!NOTE]
> The goal is not “perfect AI.” The goal is **bounded automation** with provable rails.

---

<a id="invariants"></a>

## 🧭 KFM invariants (actions must not break)

These are enforceable guardrails. If an action violates one, CI should fail loudly.

1) 🧱 **Pipeline order is mandatory (v13)**  
**ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode**. No stage skipping.

2) 🧬 **Evidence-first ingestion is mandatory**  
Each dataset run emits a **catalog triplet** (**STAC + DCAT + PROV**) and missing provenance blocks intake.

3) ♻️ **Deterministic & idempotent**  
Pipelines are deterministic and idempotent; actions must preserve this property (no hidden mutable state).

4) 🧠 **Graph references catalogs (don’t duplicate)**  
Graph nodes reference canonical STAC/DCAT/PROV records and store **IDs/links**, not shadow copies of full data.

5) 🔌 **API boundary rule**  
UI consumes APIs only; last-mile governance happens in the API (permissions, redaction, provenance injection).

6) 🤖 **AI is advisory-only + evidence-backed**  
Focus Mode must not publish or mutate state autonomously; AI outputs must remain provenance-linked and policy-checked.

7) 🛂 **Sovereignty + classification propagation**  
Outputs inherit the strictest classification of inputs unless an approved redaction/generalization step is recorded in PROV and passes policy.

8) 🚦 **Default-deny promotion**  
Promotion lanes fail closed for missing SBOM/provenance/checksums/SLSA or policy violations.

---

<a id="layers"></a>

## 🏗️ Layer boundaries & isolation (closed layers ≈ safer change)

KFM is intentionally layered: UI is at the end of the pipeline and consumes a governed API that filters sensitive data and injects provenance details.

### Closed layers rule of thumb 🔒
Treat core subsystems as *closed layers* unless explicitly documented otherwise:

- UI → API → storage/graph
- Story/Focus → (reads) API/catalogs/graph only
- ETL → catalogs/prov → (then) graph ingest

> [!NOTE]
> Closed layers aren’t about speed—they’re about **governance + testability + auditability**.

---

<a id="repo-map"></a>

## 🗺️ Repo structure alignment (v13 map)

This is the **expected** KFM “v13” shape that actions/workflows should assume.

```text
📁 .github/
├── 📁 actions/                 # ✅ you are here (composite actions)
└── 📁 workflows/               # reusable lanes + job templates

📁 data/
├── 📁 raw/                     # 🔒 immutable inputs (prefer DVC pointers for large blobs)
│  └── 📁 <domain>/
├── 📁 work/                    # ♻️ intermediate scratch (not authoritative)
│  └── 📁 <domain>/
└── 📁 processed/               # ✅ governed outputs (analytics + UI packaging)
   └── 📁 <domain>/
      ├── 📄 *.parquet          # 🧱 analytics-friendly (GeoParquet)
      ├── 📄 *.pmtiles          # 🗺️ UI-friendly (PMTiles)
      └── 📄 README.md          # domain runbook (optional mirror; canonical lives in docs/data/)

📁 data/stac/
├── 📁 collections/             # 🗂️ STAC collections
└── 📁 items/                   # 🧾 STAC items

📁 data/catalog/
└── 📁 dcat/                    # 🏷️ DCAT records + distributions

📁 data/prov/                   # 🧬 PROV bundles (JSON-LD)

📁 docs/
├── 📄 MASTER_GUIDE_v13.md
├── 📁 standards/               # markdown protocol + profiles
├── 📁 templates/
├── 📁 architecture/
├── 📁 governance/
├── 📁 data/
│  └── 📁 <domain>/             # ✅ canonical domain runbooks
│     └── 📄 README.md
└── 📁 library/
   └── 📄 MANIFEST.yml          # ✅ index: title/license/source/location

📁 schemas/                     # machine-readable schemas used by validation actions
📁 src/                         # pipelines + graph + server
📁 tools/                       # validation, policy, QA, release tooling
📁 web/                         # UI (React/TS/MapLibre/Cesium/WebGL)
📁 mcp/                         # methods & computational experiments (runs, notebooks, model cards)

📄 CITATION.cff  📄 SECURITY.md  📄 CHANGELOG.md  📄 CONTRIBUTING.md
```

> [!TIP]
> **Legacy paths** (allowed only for migration): `data/catalog/stac/**`, `data/provenance/**`, `data/interim/**`.  
> New actions should default to v13 canonical, but may support legacy via `KFM_DATA_LAYOUT=legacy|v13`.

---

<a id="toolchain"></a>

## 🗺️ Geospatial toolchain & runner strategy

KFM CI often touches:
- GIS libs (GDAL/PROJ/GEOS) 🧭
- vector tiles + PMTiles 📦
- analytics formats (GeoParquet) 🧱
- WebGL UI builds (MapLibre/Cesium) 🗺️
- hybrid DB + graph contracts (PostGIS + Neo4j + Search) 🧠

### 🧰 Runner design rules (keep lanes reproducible)
- Prefer **containerized toolchains** (pinned image digest) for GIS-heavy jobs.
- If installing system packages, pin versions where possible and record versions in `build-info.json`.
- Cache responsibly:
  - Python: `pip` cache + `venv` keyed on lockfile hash
  - Node: `npm`/`pnpm` cache keyed on lockfile hash
  - GIS: avoid caching compiled GDAL builds unless pinned and validated

### 📦 Dual-format outputs (analytics + UI)
KFM commonly emits **two “views” of the same dataset**:
- **GeoParquet** for analysis and efficient querying
- **PMTiles** for fast map visualization in the browser

> [!NOTE]
> Dual-format is a performance optimization **without** sacrificing provenance: both formats share the same catalog + lineage and must be traceable back to raw inputs.

### ✅ What actions should standardize
- `pmtiles-build` produces: tiles + metadata + checksums
- `geoparquet-build` produces: parquet + schema report + checksums
- `catalog-qa` enforces that both are represented in STAC/DCAT distributions

---

<a id="versioning"></a>

## 🔢 Versioning & compatibility contract

KFM treats versioning as part of the contract (especially for graph + APIs + releases).

### Required checks in CI lanes ✅
- **Graph/Ontology**: ontology/schema version bumps require migrations + validation fixtures.
- **API contracts**: OpenAPI/GraphQL diffs must be reviewed + tested; breaking changes require explicit versioning.
- **Release artifacts**: releases bundle checksums + SBOM + provenance and are traceable to code + inputs.
- **GraphQL consumer protection**: run example queries from `api/contracts/examples/graphql/**` as contract tests (schema changes must not silently break clients).

---

<a id="vvuq"></a>

## 🧪 Scientific rigor (V&V + UQ + reproducibility)

KFM ships evidence and derived analysis artifacts, so CI must support scientific workflow expectations:
- write the research question / objective
- document methods + parameters
- collect data with traceability
- present results with reproducible linkage to code + inputs
- capture uncertainty / limitations
- iterate with a recorded trail (electronic lab notebook style)

### What actions should enforce ✅
- Every modeling/analysis run emits:
  - `run_uuid` + `build-info.json`
  - inputs manifest (paths + hashes)
  - outputs manifest (paths + hashes)
  - parameters + seeds record
  - PROV activity bundle linking inputs → activities → outputs
- Scenario work (“what-if”) runs must behave like real pipelines:
  - deterministic
  - provenance-linked
  - promoted only through gates
  - labeled as **simulation** (never confused with “observed truth”)

> [!TIP]
> Roadmap hook: a deterministic `kfm-sim-run` lane can generate PR-ready artifact bundles (reports + catalogs + summaries) without polluting production.

---

<a id="threat-model"></a>

## 🔐 Threat model & trust boundaries (actions edition)

### 🧨 Common risks we design around
- **Supply chain:** unpinned third-party actions; unsafe `curl | bash`
- **Secrets exposure:** leaking tokens in logs/artifacts
- **Catalog poisoning:** malformed STAC/DCAT fields or links
- **Artifact tampering:** publishing without checksums + attestations
- **Untrusted PR execution:** forks attempting exfiltration
- **Classification leakage:** “public” workflows processing restricted artifacts
- **Policy drift:** rules changed without review (must be versioned/audited)
- **Prompt injection:** malicious text in docs/story nodes attempting to steer Focus Mode
- **AI overreach:** model tries to take actions outside its allowlist (must be blocked)

### 🔐 Boundary rules (non-negotiable)
- No secrets in PR lanes (especially forks).
- No “download arbitrary URL from PR input.”
- Promotion lanes require explicit environment protection.
- Prefer digest-pinned images and commit-SHA pinned actions.
- AI runs must be **sandboxed** (no filesystem mutation outside `.artifacts/`, no network unless explicitly allowed).

---

<a id="classification"></a>

## 🛂 Data classification & access control (Data Spaces mindset)

KFM assumes governance is not optional:
- provenance-first + FAIR/CARE-aligned stewardship are core platform principles
- sensitive entities can be flagged and filtered/generalized at the API boundary

### Classification propagation rule 🧷
**Outputs inherit the strictest classification of their inputs** unless:
- an approved redaction/de-identification step exists **and**
- the step is recorded in PROV **and**
- policy gates approve promotion.

### Markdown/doc metadata hook 🏷️
KFM doc templates support explicit fields (e.g., `classification`, `care_label`, `sensitivity`) so governance signals travel with artifacts.

---

<a id="ci-gates"></a>

## 🧪 Minimum CI gates (v13 “hard rails”)

These gates are the “trust backbone” of KFM. Most are implemented as local composite actions calling repo tools.

### ✅ Gate set (recommended baseline)
1) 🧾 **Markdown protocol + DoD validation** (front-matter, required sections, checklists)
2) 🔗 **Link/reference validation** (internal links + citations resolve)
3) 📦 **Schema validation** (STAC/DCAT/PROV + story metadata)
4) 🧠 **Graph integrity checks** (no mystery nodes; governance properties)
5) 🔌 **API contract tests** (OpenAPI + GraphQL schema lint + example-query contract tests)
6) 🛡️ **Policy-as-code** (OPA/Conftest; default deny)
7) 🧬 **Supply chain evidence** (SBOM + SLSA provenance + signed attestations)
8) 🧱 **Large data hygiene** (DVC pointers required; block giant binaries)
9) 🗺️ **UI build + tests** (unit + smoke + optional E2E: Cypress/Playwright)
10) 🤖 **AI regression & policy checks** (prompt gate + citation rules + classification)

> [!IMPORTANT]
> “If it’s not validated in CI, it’s not real.”  
> Any lane that publishes must run the full gate set **fail-closed**.

---

<a id="action-catalog"></a>

## 🗂️ Action catalog (recommended set)

> Keep actions small and composable. Avoid “mega actions.”  
> Convention: **one machine-readable report + one human summary** per action.

### 🧩 Foundation actions
| Action | Purpose | Typical workflows |
|---|---|---|
| `setup-kfm` | Python + Node toolchain + caches (+ optional GIS deps) | `ci.yml`, `ui.yml`, `integration.yml` |
| `toolchain-pin` | verify pinned tool versions / lockfiles / digests | all lanes |
| `build-info` | emit `build-info.json` + tool versions + environment fingerprint | integration/release |
| `kill-switch` | global stop button for publish/promotion lanes | publish/release |
| `link-check` | fail on broken internal links & missing references | docs/story lanes |
| `dvc-guard` | enforce DVC pointers for large artifacts | data lanes |

### ✅ Validation & governance actions
| Action | Purpose | Typical workflows |
|---|---|---|
| `markdown-protocol` | validate governed Markdown (front-matter + DoD) | docs/story lanes |
| `catalog-qa` | fast STAC/DCAT checks + link checks (PR lane) | `catalog-qa.yml` |
| `metadata-validate` | schema/profile validation: STAC/DCAT/PROV | nightly/full lanes |
| `graph-integrity` | graph schema + invariant checks | graph lanes |
| `api-contract-test` | OpenAPI + GraphQL schema lint + **example query contract tests** | server lanes |
| `governance-scan` | secrets/PII/sensitive-location scan (configurable) | PR + nightly |
| `classification-gate` | block classification downgrades | promotion lanes |
| `policy-gate` | OPA/Conftest evaluation (default deny) | promotion lanes |
| `provenance-guard` | require PROV completeness + checksums | promotion lanes |

### 🗺️ Geospatial build actions (formats that matter)
| Action | Purpose | Typical workflows |
|---|---|---|
| `geoparquet-build` | generate GeoParquet outputs + schema report | data lanes |
| `pmtiles-build` | generate PMTiles vector tile archives | data + UI lanes |
| `tileset-qa` | validate tile metadata + bounds + zoom policy | nightly + release |
| `reprojection-guard` | enforce EPSG rules + CRS declarations | data lanes |

### 🤖 AI / Focus Mode actions (Ollama-first)
| Action | Purpose | Typical workflows |
|---|---|---|
| `ollama-setup` | start Ollama + pull pinned model(s) for CI | ai lanes |
| `rag-index-smoke` | build tiny vector index from fixtures | ai lanes |
| `ai-policy-regression` | run prompt-gate + output policy checks | PR + nightly |
| `focus-mode-regression` | golden tests for “known questions” w/ citation expectations | nightly |
| `model-card-check` | ensure model cards + safety notes exist for promoted models | release |

### 🧪 Scientific & modeling actions (VVUQ-ready)
| Action | Purpose | Typical workflows |
|---|---|---|
| `experiment-protocol` | emit run protocol (params + seeds + assumptions) | modeling lanes |
| `vvuq-report` | verification/validation + uncertainty summaries | modeling lanes |
| `stats-sanity` | regression/EDA baselines + drift checks | analysis lanes |
| `sim-run` | deterministic scenario run → PR-ready bundle | simulation lanes |

### 🧬 Supply-chain & publishing actions
| Action | Purpose | Typical workflows |
|---|---|---|
| `docker-build` | buildx + caching + labels + digests | `docker.yml` |
| `sbom` | generate SBOM (SPDX/CycloneDX) | `release.yml` |
| `slsa-provenance` | emit SLSA/in-toto provenance attestation | `release.yml` |
| `attest` | create/attach attestations (OIDC-based where possible) | `release.yml` |
| `sign-artifact` | Sigstore Cosign signing for promoted artifacts | release/publish lanes |
| `oras-publish` | publish datasets/models/notebooks as OCI artifacts (ORAS) | federation/release lanes |
| `release-bundle` | assemble `releases/<tag>/` + checksums | tags/releases |

### 🧠 Lineage & automation support
| Action | Purpose | Typical workflows |
|---|---|---|
| `prov-emit` | emit PROV JSON-LD bundle (inputs → activity → outputs) | integration/release |
| `detect-changes` | compute stable fingerprints (ETag/Last-Modified/hash) | scheduled lanes |
| `pr-compose` | assemble PR-ready artifact bundle + summaries | automation lanes |

---

<a id="action-contract"></a>

## ✅ Action contract (inputs, outputs, artifacts)

### ✅ Inputs (strings only)
GitHub Actions inputs are strings. For booleans, accept:
- `"true" | "false"`

Recommended common inputs across KFM actions:
- `fail_on_warn` → `"true"` in promotion lanes
- `out_dir` → default `.artifacts/out/<action>`
- `summary_to_step` → `"true"` (append to `$GITHUB_STEP_SUMMARY`)
- `run_uuid` → optional override (otherwise generated)
- `classification` → optional override **only if validated** (never downgrade silently)
- `data_layout` → `"v13" | "legacy"` *(default `"v13"`; support migration paths explicitly)*
- `policy_bundle` → path/ref to policy bundle (actions should record its hash)

### ✅ Outputs (standard keys)
Recommended outputs across actions:
- `ok` → `"true" | "false"`
- `report_path` → JSON report path
- `summary_path` → Markdown summary path
- `artifact_dir` → directory containing outputs
- `run_uuid` → stable run UUID for correlation
- `classification` → resolved classification (post-policy)
- `policy_bundle_sha` → hash of policy bundle used
- `checksums_path` → where checksums were written (if produced)
- `sbom_path` → SBOM path (if produced)
- `provenance_path` → PROV bundle path (if produced)
- `slsa_path` → SLSA/in-toto provenance path (if produced)

> [!IMPORTANT]
> Do **not** pass secrets via action outputs. Outputs can leak into logs and downstream steps.

### 📦 Artifact layout (default expectation)
```text
📁 .artifacts/
├─ 📁 out/
│  └─ 📁 <action-name>/
│     ├─ 📄 report.json
│     ├─ 📄 summary.md
│     ├─ 📄 build-info.json
│     ├─ 📄 inputs.manifest.json
│     ├─ 📄 outputs.manifest.json
│     ├─ 📄 policy.manifest.json        # bundle hash + decision ids (if applicable)
│     └─ 📁 logs/
├─ 📁 attestations/
│  ├─ 📄 materials.sbom.spdx.json
│  ├─ 📄 provenance.dsse.json
│  ├─ 📄 slsa.provenance.intoto.jsonl
│  └─ 📄 checksums.sha256
└─ 📁 lineage/
   └─ 📄 prov.jsonld
```

---

<a id="kill-switch"></a>

## 🎛️ Kill switch & safe defaults

KFM automation is powerful **without being autonomous**. A global kill-switch is a required safety valve, especially for publish lanes.

### 🧯 Kill switch behavior
- If `KFM_KILL_SWITCH=true` → fail closed for publish/promotion jobs
- For non-publish jobs, “skip heavy lanes” is acceptable only if baseline safety checks still run

Recommended signal sources:
- env var: `KFM_KILL_SWITCH`
- config file: `.kfm/kill-switch.yml` *(or `ops/feature_flags/agents.yml`)*

---

<a id="provenance"></a>

## 🧾 Provenance, checksums, lineage, signing

KFM treats provenance as both a **scientific integrity control** and a **security control**:
- datasets carry the STAC/DCAT/PROV triplet
- AI outputs can be captured as PROV activities and logged in an append-only ledger
- promoted artifacts can be signed (Sigstore Cosign) for authenticity checks
- containerized pipelines avoid “it worked on my machine” drift (GIS libs matter)

### ✅ Minimum expectation for any promoted artifact
- `build-info.json` (who/what/when/where ran)
- `checksums.sha256`
- PROV JSON-LD record(s): inputs → activities → outputs
- SBOM snapshot (SPDX JSON recommended)
- SLSA/in-toto provenance attestation
- optional signing/attestations (OIDC + Sigstore)

---

<a id="oci"></a>

## 📦 OCI artifacts & signed releases (ORAS + Cosign)

KFM is designed to publish datasets/models/notebooks as **artifacts** that can be:
- discovered via catalogs (DCAT distributions),
- pulled by reference (hash/tag),
- verified cryptographically (Cosign),
- and reproduced from source inputs + containerized pipelines.

### ✅ What “OCI-ready” means for an action
- emits an OCI manifest-friendly artifact directory
- writes content-addressed checksums
- (optional) pushes via ORAS to a registry namespace
- signs + verifies in protected lanes
- records the registry reference in DCAT distributions

> [!TIP]
> Treat OCI references like immutable citations: a story node can link a claim to an artifact digest 🔏📚

---

<a id="testing"></a>

## 🧪 Testing local actions

### ✅ Minimum expectation
Every local action should include:
- `README.md` describing purpose, inputs, outputs, examples
- smoke workflow: `.github/workflows/actions-smoke.yml`
- fixture inputs (tiny STAC/DCAT/PROV, tiny policy pack)
- artifact upload on failure (`.artifacts/**`)

### 🧪 Suggested smoke workflow coverage
- run `setup-kfm`
- run `markdown-protocol` on templates
- run `link-check` on docs/story fixtures
- run `catalog-qa` on fixture catalogs
- run `graph-integrity` on fixture graph
- run `api-contract-test` on mock/fixture API + GraphQL example queries
- run `policy-gate` on allow/deny cases
- run `classification-gate` on downgrade scenarios
- run `dvc-guard` on fixture large files
- run `ollama-setup` + `ai-policy-regression` on fixture prompts
- run `build-info` and upload `.artifacts/**`

> [!TIP]
> If you want to run actions locally, consider a dedicated dev lane using `act` (or a container-based harness) so results match CI more closely.

---

<a id="templates"></a>

## 🧷 Templates (copy/paste)

<details>
<summary><strong>🧩 Composite action skeleton — <code>.github/actions/&lt;name&gt;/action.yml</code></strong></summary>

```yaml
name: "kfm/<name>"
description: "Reusable step bundle for Kansas Frontier Matrix workflows."

inputs:
  out_dir:
    description: "Artifact output directory"
    required: false
    default: ".artifacts/out/<name>"
  fail_on_warn:
    description: "Fail if warnings are present"
    required: false
    default: "true"
  summary_to_step:
    description: "Append summary.md to GitHub step summary"
    required: false
    default: "true"
  run_uuid:
    description: "Optional run UUID (otherwise derived from run_id + sha)"
    required: false
    default: ""
  data_layout:
    description: "v13|legacy (default v13)"
    required: false
    default: "v13"

outputs:
  ok:
    description: "Whether the action succeeded logically"
    value: ${{ steps.meta.outputs.ok }}
  report_path:
    description: "Path to the generated report artifact"
    value: ${{ steps.meta.outputs.report_path }}
  summary_path:
    description: "Path to the generated markdown summary"
    value: ${{ steps.meta.outputs.summary_path }}
  artifact_dir:
    description: "Directory containing outputs"
    value: ${{ steps.meta.outputs.artifact_dir }}
  run_uuid:
    description: "Run UUID used to correlate artifacts"
    value: ${{ steps.meta.outputs.run_uuid }}

runs:
  using: "composite"
  steps:
    - name: 🧾 Context (safe)
      shell: bash
      run: |
        set -euo pipefail
        echo "action=kfm/<name>"
        echo "repo=$GITHUB_REPOSITORY"
        echo "sha=$GITHUB_SHA"
        echo "run_id=$GITHUB_RUN_ID"

    - name: ✅ Run task
      shell: bash
      run: |
        set -euo pipefail
        OUT="${{ inputs.out_dir }}"
        mkdir -p "$OUT/logs"

        RUN_UUID="${{ inputs.run_uuid }}"
        if [ -z "$RUN_UUID" ]; then
          RUN_UUID="${GITHUB_RUN_ID}-${GITHUB_SHA::8}"
        fi

        # TODO: call repo tool(s) here
        cat > "$OUT/report.json" <<JSON
        {
          "ok": true,
          "warnings": [],
          "errors": [],
          "run_uuid": "${RUN_UUID}",
          "artifact_dir": "${OUT}",
          "data_layout": "${{ inputs.data_layout }}"
        }
JSON

        echo "✅ kfm/<name> ok" > "$OUT/summary.md"
        echo "" >> "$OUT/summary.md"
        echo "- run_uuid: \`${RUN_UUID}\`" >> "$OUT/summary.md"
        echo "- artifact_dir: \`${OUT}\`" >> "$OUT/summary.md"
        echo "- data_layout: \`${{ inputs.data_layout }}\`" >> "$OUT/summary.md"

        if [ "${{ inputs.summary_to_step }}" = "true" ]; then
          cat "$OUT/summary.md" >> "$GITHUB_STEP_SUMMARY"
        fi

        # Optional: fail on warnings in promotion lanes
        if [ "${{ inputs.fail_on_warn }}" = "true" ]; then
          # replace with real jq checks once report has warnings
          true
        fi

    - name: 📦 Set outputs
      id: meta
      shell: bash
      run: |
        set -euo pipefail
        OUT="${{ inputs.out_dir }}"
        RUN_UUID="${{ inputs.run_uuid }}"
        if [ -z "$RUN_UUID" ]; then
          RUN_UUID="${GITHUB_RUN_ID}-${GITHUB_SHA::8}"
        fi

        echo "ok=true" >> "$GITHUB_OUTPUT"
        echo "report_path=$OUT/report.json" >> "$GITHUB_OUTPUT"
        echo "summary_path=$OUT/summary.md" >> "$GITHUB_OUTPUT"
        echo "artifact_dir=$OUT" >> "$GITHUB_OUTPUT"
        echo "run_uuid=$RUN_UUID" >> "$GITHUB_OUTPUT"
```

</details>

<details>
<summary><strong>🧯 Kill switch action — fail closed in publish lanes</strong></summary>

```yaml
name: "kfm/kill-switch"
description: "Fail-closed stop button for promotion/publish jobs."

inputs:
  mode:
    description: "fail|skip (prefer fail for publish lanes)"
    required: false
    default: "fail"
  flag_env:
    description: "Env var name for kill switch"
    required: false
    default: "KFM_KILL_SWITCH"

runs:
  using: "composite"
  steps:
    - name: 🧯 Check kill switch
      shell: bash
      run: |
        set -euo pipefail
        FLAG_NAME="${{ inputs.flag_env }}"
        FLAG_VALUE="${!FLAG_NAME:-false}"

        echo "kill_switch=${FLAG_VALUE}" >> "$GITHUB_STEP_SUMMARY"

        if [ "$FLAG_VALUE" = "true" ]; then
          echo "🧯 Kill switch is ON (${FLAG_NAME}=true)." >> "$GITHUB_STEP_SUMMARY"
          if [ "${{ inputs.mode }}" = "skip" ]; then
            echo "Skipping as requested." >> "$GITHUB_STEP_SUMMARY"
            exit 0
          fi
          echo "Failing closed." >> "$GITHUB_STEP_SUMMARY"
          exit 1
        fi

        echo "✅ Kill switch is OFF." >> "$GITHUB_STEP_SUMMARY"
```

</details>

<details>
<summary><strong>🧑‍⚖️ Policy gate snippet — Conftest / OPA (default deny)</strong></summary>

```yaml
- name: 🧑‍⚖️ Policy Gate (OPA/Conftest)
  shell: bash
  run: |
    set -euo pipefail
    # Example: evaluate artifacts + metadata against repo policies
    conftest test .artifacts/out --policy tools/validation/policy --all-namespaces
```

</details>

<details>
<summary><strong>📦 ORAS + Cosign snippet — publish + sign (protected lanes only)</strong></summary>

```yaml
- name: 📦 ORAS publish (OCI artifact)
  if: ${{ github.ref_type == 'tag' }}
  shell: bash
  run: |
    set -euo pipefail
    # Example: push a dataset bundle as an OCI artifact
    oras push "$REGISTRY/kfm/datasets:${GITHUB_SHA::8}" \
      .artifacts/out/release-bundle/:application/vnd.kfm.dataset.layer.v1+tar

- name: 🔏 Cosign sign
  if: ${{ github.ref_type == 'tag' }}
  shell: bash
  run: |
    set -euo pipefail
    cosign sign --yes "$REGISTRY/kfm/datasets:${GITHUB_SHA::8}"
```

</details>

<details>
<summary><strong>✅ Example usage — call a local action from a workflow</strong></summary>

```yaml
jobs:
  catalog_gate:
    runs-on: ubuntu-latest
    permissions:
      contents: read

    steps:
      - uses: actions/checkout@v4

      - name: ✅ Run Catalog QA
        uses: ./.github/actions/catalog-qa
        with:
          fail_on_warn: "true"
```

</details>

---

<a id="review-checklist"></a>

## 🧑‍⚖️ Review checklist

Use this checklist for new actions and major changes:

- [ ] Deterministic & idempotent (no hidden mutable state) ♻️
- [ ] Inputs validated (string booleans handled explicitly)
- [ ] Outputs standardized (`ok`, `report_path`, `summary_path`, `run_uuid`, etc.)
- [ ] No secrets printed or passed via outputs
- [ ] Minimal permissions documented; workflows enforce least privilege
- [ ] Produces a JSON report + Step Summary
- [ ] Schema validation included if touching STAC/DCAT/PROV/story metadata
- [ ] Policy gate (OPA/Conftest) included if used for promotion lanes
- [ ] Classification propagation enforced if touching `data/**`
- [ ] If publishing: checksums + provenance + SBOM + SLSA + signing expectations present
- [ ] Pin external actions by commit SHA; pin container images by digest 🔏
- [ ] DVC pointers enforced for large data artifacts
- [ ] Smoke workflow exists; logs/artifacts uploaded on failure
- [ ] Local README exists next to the action
- [ ] (If AI) prompt gate + output policy checks + regression fixtures exist 🤖

---

<a id="reference-library"></a>

## 📚 Project reference library

> ⚠️ Reference materials may have licenses different from repo code.  
> Index them in `docs/library/MANIFEST.yml` and respect upstream terms.

<details>
<summary><strong>🧱 Canonical KFM specs (must-read)</strong></summary>

- `Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap.pdf`
- `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`
- `Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide).pdf`
- `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`
- `📚 Kansas Frontier Matrix (KFM) – Expanded Technical & Design Guide.pdf`
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `KFM AI Infrastructure – Ollama Integration Overview.pdf`

</details>

<details>
<summary><strong>🧾 Documentation standards (protocol + DoD)</strong></summary>

- `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` *(expected path)*
- `docs/MASTER_GUIDE_v13.md` *(repo contract)*
- `Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx`

</details>

<details>
<summary><strong>🔬 Scientific method + reproducibility protocols</strong></summary>

- `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf`

</details>

<details>
<summary><strong>🗺️ Foundational architecture origins</strong></summary>

- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`

</details>

<details>
<summary><strong>📦 Library bundles & “PDF portfolio” inputs (extract + index)</strong></summary>

> Some uploaded references are **PDF portfolios** (Acrobat containers). Extract them into individual PDFs so search/indexing works, then add entries to `docs/library/MANIFEST.yml`.

- `AI Concepts & more.pdf`
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf`
- `Various programming langurages & resources 1.pdf`
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf`
- `Mapping-Modeling-Python-Git-HTTP-CSS-Docker-GraphQL-Data Compression-Linux-Security.pdf`
- `Geographic Information-Security-Git-R coding-SciPy-MATLAB-ArcGIS-Apache Spark-Type Script-Web Applications.pdf`
- `KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf` *(geospatial dev recipes)*

</details>

---

<p align="right"><a href="#top">⬆️ Back to top</a></p>