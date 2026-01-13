<a id="top"></a>

# 🧰 `.github/workflows/` — CI/CD for Kansas Frontier Matrix (KFM)

<div align="left">

<!-- ✅ Existing workflow badges (these should match real workflow filenames) -->
<a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml/badge.svg" /></a>
<a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml"><img alt="CodeQL" src="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg" /></a>
<a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml"><img alt="Pages" src="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml/badge.svg" /></a>

<!-- 🧭 KFM “shape” badges (conceptual) -->
<img alt="KFM-MDP" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-5865F2" />
<img alt="Master Guide" src="https://img.shields.io/badge/Master%20Guide-v13.0.0--draft%20(2025--12--28)-f59e0b" />
<img alt="Contract First" src="https://img.shields.io/badge/contract--first-enforced-2563eb" />
<img alt="Evidence First" src="https://img.shields.io/badge/evidence--first-required-10b981" />
<img alt="Provenance" src="https://img.shields.io/badge/provenance-STAC%20%7C%20DCAT%20%7C%20PROV-6f42c1" />
<img alt="Policy as Code" src="https://img.shields.io/badge/policy-Conftest%20%2B%20Rego-0ea5e9" />
<img alt="Supply Chain" src="https://img.shields.io/badge/supply%20chain-SBOM%20%2B%20Attestations-111827" />
<img alt="DevSecOps" src="https://img.shields.io/badge/DevSecOps-enabled-black" />
<img alt="CI" src="https://img.shields.io/badge/CI-boring%20by%20design-success" />

</div>

> 🧭 This folder contains GitHub Actions workflows that keep KFM **buildable**, **testable**, **secure**, and **shippable** — across **pipelines → catalogs → graph → API → UI → story nodes → focus mode**.  
> ✅ **North Star:** CI/CD protects *trust* (**contracts + provenance + policy**) first, then *speed* (caching + change‑aware gates).  
> 🚦 **KFM canonical order (non‑negotiable):** **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.[^mg13-pipeline]

> [!IMPORTANT]
> CI is intentionally **boring** (predictable, repeatable, least‑privilege, auditable).  
> The data, stories, and models are the interesting part. 🗺️✨

---

## 🧾 Workflow policy metadata

| Field                   | Value                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------ |
| Folder                  | `.github/workflows/`                                                                                   |
| Status                  | Active ✅                                                                                               |
| Last updated            | **2026-01-13**                                                                                         |
| KFM‑MDP baseline        | **v11.2.6** *(STAC/DCAT/PROV profiles v11 referenced in v13 guide)*[^mg13-v13-history]                 |
| Master Guide baseline   | **v13.0.0‑draft (2025‑12‑28)**[^mg13-v13-history]                                                      |
| Governance              | FAIR + CARE (data + people)                                                                            |
| CI philosophy           | PR‑fast lane + scheduled heavy lanes + env‑gated promotion 🚦                                          |
| Runner baseline         | `ubuntu-latest` *(pin images for hermetic lanes)* 🐧                                                   |
| Least‑privilege default | `permissions: { contents: read }` 🔐                                                                   |
| PR‑first promotion      | Promotion happens via **signed PRs**, not direct pushes 🧾                                              |
| Fail‑closed posture     | Promotion‑critical workflows stop on policy/metadata/provenance violations 🧯                          |
| v13 structural target   | `schemas/`, `releases/`, `data/prov/`, `data/catalog/dcat/`, plus canonical homes for subsystems[^mg13-v13-structure] |

---

## ⚡ Quick links

| Action                          | Link                                                                                                                                     |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| ✅ All Action runs              | [https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions)     |
| 📦 Releases                     | [https://github.com/bartytime4life/Kansas-Frontier-Matrix/releases](https://github.com/bartytime4life/Kansas-Frontier-Matrix/releases)   |
| 🐛 Issues                       | [https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues)       |
| 🤝 `.github/` Collaboration hub | [`../README.md`](../README.md)                                                                                                           |
| 🧭 Repo root overview           | [`../../README.md`](../../README.md)                                                                                                     |
| 🔐 Security policy              | [`../../SECURITY.md`](../../SECURITY.md) *(or `../SECURITY.md` if canonical is inside `.github/`)*                                       |

> [!TIP]
> If a badge 404s, that workflow file probably doesn’t exist yet.  
> This README is a **spec + target shape** — update it as you implement workflows to avoid drift. 🧾✅

---

<details>
<summary><b>🧭 Table of contents</b></summary>

* [📺 Mermaid Workflow TV](#mermaid-workflow-tv)
* [🧠 CI/CD principles](#cicd-principles)
* [🧪 Minimum CI gates for v13 contributions](#minimum-ci-gates-for-v13-contributions)
* [🧬 KFM invariants CI must enforce](#kfm-invariants-ci-must-enforce)
* [🗂️ v13 repo layout & path triggers](#v13-repo-layout--path-triggers)
* [📁 What lives here](#what-lives-here)
* [🗂️ Workflow catalog](#workflow-catalog)
* [🚦 Change-aware gate matrix](#change-aware-gate-matrix)
* [🧱 Promotion gates](#promotion-gates)
* [🧑‍⚖️ Policy as code gates](#policy-as-code-gates)
* [🤖 Agent automation lane](#agent-automation-lane)
* [🗺️ Data + catalog gates](#data--catalog-gates)
* [🕸️ Graph + semantics gates](#graph--semantics-gates)
* [🎬 Story Nodes + Focus Mode gates](#story-nodes--focus-mode-gates)
* [🧪 Integration tests](#integration-tests)
* [🌐 Web UI gates](#web-ui-gates)
* [📈 Modeling + simulation gates](#modeling--simulation-gates)
* [⚡ Performance gates](#performance-gates)
* [🔐 Security scanning](#security-scanning)
* [📦 Artifacts & traceability](#artifacts--traceability)
* [🧷 Secrets & environments](#secrets--environments)
* [🧩 Reusable workflows & composite actions](#reusable-workflows--composite-actions)
* [🛠️ Starter templates](#starter-templates)
* [🧰 Debug locally](#debug-locally)
* [🧾 Adding a new workflow checklist](#adding-a-new-workflow-checklist)
* [📚 Reference library & influence map](#reference-library--influence-map)

</details>

---

<a id="mermaid-workflow-tv"></a>

## 📺 Mermaid Workflow TV

A “TV guide” of how work moves through KFM CI/CD (PR fast lane → scheduled heavy lanes → env‑gated publish). 📺🧪

```mermaid
flowchart TB
  subgraph PR["🧪 PR Lane (fast • required)"]
    PR1["ci.yml<br/>lint • unit • typecheck"]
    PR2["ui.yml<br/>web lint • test • build"]
    PR3["markdown-protocol.yml<br/>front-matter + doc sections"]
    PR4["docs-linkcheck.yml<br/>links + citations resolve"]
    PR5["schema-validate.yml<br/>STAC/DCAT/PROV + Story schemas"]
    PR6["catalog-qa.yml<br/>STAC/DCAT quick gate + link safety"]
    PR7["graph-integrity.yml<br/>Neo4j fixture + constraints"]
    PR8["kfm-policy-gate.yml<br/>Conftest/Rego (FAIR+CARE)"]
    PR9["dependency-review.yml<br/>dep diffs + license signal"]
    PR10["actionlint.yml<br/>workflow lint"]
  end

  subgraph SCHEDULE["🌙 Scheduled Lane (slow • trusted)"]
    N1["integration.yml<br/>PostGIS (+ graph) + API contract tests"]
    N2["stac-validate.yml<br/>full STAC schema lane"]
    N3["dcat-validate.yml<br/>DCAT lane"]
    N4["prov-validate.yml<br/>PROV lane"]
    N5["perf.yml<br/>bundle + query budgets"]
    N6["model-regression.yml<br/>metrics + reproducibility"]
  end

  subgraph PROMOTE["🚦 Promotion Lane (env-gated)"]
    P1["publish-catalog.yml<br/>atomic publish + catalogs + PROV"]
    P2["docker.yml<br/>build/push images (GHCR)"]
    P3["pages.yml<br/>docs/viewer deploy (optional)"]
  end

  subgraph RELEASE["🏷️ Release Lane (tags)"]
    R1["release.yml<br/>release assets + notes"]
    R2["sbom.yml<br/>SBOM generation"]
    R3["attest.yml<br/>build provenance attestations"]
    R4["scorecard.yml<br/>OpenSSF scorecard (optional)"]
  end

  subgraph AGENTS["🤖 Agent Lane (optional)"]
    A1["agents-watcher.yml<br/>read-only signals"]
    A2["agents-planner.yml<br/>deterministic plans"]
    A3["agents-executor.yml<br/>PR-only executor (no merge)"]
    A4["detect-validate-promote.yml<br/>changes → lanes → signed PR"]
  end

  PR1 --> SCHEDULE
  PR5 --> SCHEDULE
  PR6 --> P1
  PR8 --> P1
  SCHEDULE --> P1
  P1 --> RELEASE
  P2 --> RELEASE
  AGENTS --> PR
```

**Plain-English summary:**

* PR lane stays fast and blocks obvious breakage.
* Scheduled lanes do real integration, heavy validation, and budget checks.
* Promotion is **env‑gated**, **atomic**, and **audit‑friendly**.
* Optional agents are allowed only if they respect **kill‑switch + determinism + PR‑only**.

> [!TIP]
> Mermaid on GitHub can be picky. To avoid parse errors:
>
> * keep **one edge per line**
> * use simple IDs (`PR1`, `N1`, …)
> * put punctuation/emoji inside quotes if needed 😄

---

<a id="cicd-principles"></a>

## 🧠 CI/CD principles

### ✅ 1) Contracts over vibes

KFM treats key interfaces as contracts (CI enforces drift detection):

* 📜 **API** contracts (OpenAPI + GraphQL schema) — **contract‑first** is the v13 posture.[^mg13-contract-first]
* 🗂️ **Catalog** contracts (STAC / DCAT)
* 🧾 **Lineage** contracts (W3C PROV JSON‑LD)
* 🕸️ **Graph** contracts (stable IDs + relationship shapes + migrations)
* 📈 **Evidence artifacts** (analysis/model/simulation outputs: manifests + seeds + metrics)

> KFM (v13) explicitly frames **schemas + API contracts** as first‑class artifacts and expects strict compatibility checks when they change.[^mg13-contract-first]

### ✅ 2) Layered gates beat mega workflows

CI mirrors KFM’s architecture with layered checks:

1. **Code gate** → lint, unit tests, type checks
2. **Doc gate** → Markdown protocol + links + citations resolve
3. **Schema gate** → STAC/DCAT/PROV/Story schema validation
4. **Policy gate** → FAIR+CARE, sovereignty, license guardrails
5. **Integration gate** → real DBs/services via containers (PostGIS + Neo4j as needed)
6. **Security gate** → SAST, dependency review, secret scanning, container scan
7. **Promotion gate** → env‑gated publish with SBOM + attestations

### ✅ 3) Deterministic, idempotent, auditable 🧾

* Same inputs + config + seed ⇒ same outputs (or diffs are logged and explained)
* Artifacts and logs are uploaded on failure
* Promotion is atomic (no half‑published catalogs)
* Every publishable run emits: run id + inputs + outputs + digests + provenance

> v13 explicitly expects a **deterministic pipeline**: idempotent, config‑driven ETL producing stable outputs for given inputs.[^mg13-contract-first]

### ✅ 4) Least privilege by default 🔐

* Minimal `permissions:` per workflow/job
* No secrets on untrusted PRs (especially forks)
* Avoid `pull_request_target` unless you can justify and review it like production code

---

<a id="minimum-ci-gates-for-v13-contributions"></a>

## 🧪 Minimum CI gates for v13 contributions

The v13 guide defines a “definition of done” *for the repo itself*: every contribution should pass a minimum set of CI validations.[^mg13-ci-min]

### ✅ Gate 1 — Markdown protocol & front‑matter check

* All governed docs (and Story Nodes) must pass front‑matter + required section checks.
* Broken front‑matter or missing required sections fails the build.[^mg13-ci-min]

**Workflow:** `markdown-protocol.yml`  
**Typical trigger paths:** `docs/**`, `docs/reports/story_nodes/**`, `docs/templates/**`

### ✅ Gate 2 — Link/reference validation (docs + Story Nodes)

* CI verifies internal links, citations, and references resolve (no dangling references).
* Prevents “story cites a thing that doesn’t exist” drift.[^mg13-ci-min]

**Workflow:** `docs-linkcheck.yml`

### ✅ Gate 3 — JSON schema validation (STAC/DCAT/PROV + Story Node schema)

* Validate structured outputs against their schemas: STAC Items/Collections, DCAT datasets, PROV JSON‑LD, Story Node metadata (plus telemetry/UI config if schemas exist).[^mg13-ci-min]

**Workflow:** `schema-validate.yml`

### ✅ Gate 4 — Graph integrity tests (Neo4j fixture lane)

* Load a small fixture graph and assert constraints: stable IDs, required properties, relationship validity.
* Catches ontology/data‑model regressions early.[^mg13-ci-min]

**Workflow:** `graph-integrity.yml`

---

<a id="kfm-invariants-ci-must-enforce"></a>

## 🧬 KFM invariants CI must enforce

These are architecture rules that double as security + integrity controls.[^mg13-invariants]

1. 🚦 **Pipeline ordering is absolute**  
   **ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**.[^mg13-invariants]

2. 🔌 **API boundary rule**  
   The frontend must never query the Neo4j graph directly; UI goes through `src/server/` so access control + redaction + schemas stay enforceable.[^mg13-invariants]

3. 🧾 **Provenance-first publishing**  
   If it’s visible, it must be cataloged and traceable (STAC/DCAT + PROV lineage) before graph/UI/story use.[^mg13-invariants]

4. ♻️ **Deterministic ETL + evidence artifacts**  
   ETL and analysis/simulation runs must be replayable (seeded, config‑driven, logged, idempotent).[^mg13-invariants]

5. 🧭 **Sovereignty & classification propagate**  
   Outputs cannot be less restricted than inputs; public releases require redaction/generalization where needed.[^mg13-invariants]

6. ✅ **Validation gates are enforceable**  
   If a rule matters, CI should be able to **fail** for violating it (or block promotion).[^mg13-invariants]

---

<a id="v13-repo-layout--path-triggers"></a>

## 🗂️ v13 repo layout & path triggers

v13 explicitly calls out “one canonical home per subsystem” and highlights the expected directory homes that CI should treat as path‑aware triggers.[^mg13-v13-structure]

```text
📦 Repo top-levels (expected in v13)
├─ 📁 data/                      # raw/working/processed + catalog outputs (STAC/DCAT/PROV)
│  ├─ 📁 sources/                # manifests (URLs, licenses, citations)
│  ├─ 📁 processed/              # standardized outputs
│  ├─ 📁 catalog/                # STAC (+ DCAT subfolder)
│  │  └─ 📁 dcat/
│  └─ 📁 prov/                   # lineage (PROV JSON-LD)
├─ 📁 schemas/                   # JSON schemas: STAC/DCAT/PROV/story/ui/telemetry
├─ 📁 src/
│  ├─ 📁 pipelines/              # ETL jobs (deterministic)
│  ├─ 📁 graph/                  # graph build + constraints
│  └─ 📁 server/                 # API boundary + contracts (OpenAPI/GraphQL)
├─ 📁 web/                       # React/Map UI
├─ 📁 docs/
│  ├─ 📁 templates/              # governed templates
│  ├─ 📁 architecture/           # blueprints + ADRs
│  └─ 📁 reports/
│     └─ 📁 story_nodes/         # governed narrative (draft vs published)
├─ 📁 mcp/                       # Methods & Computational Experiments (runs/model cards)
└─ 📁 tests/                     # unit + integration tests
```

> [!NOTE]
> This workflows README is “CI/CD‑focused”, but it’s still downstream of the v13 layout:  
> **paths are policies** — folder moves change what gates run. 🧭

---

<a id="what-lives-here"></a>

## 📁 What lives here

> Target shape — add as needed, keep intent stable.  
> Use ✅ for “likely exists now” and 🧾 for “spec / planned”.

```text
📁 .github/workflows/
├─ ✅ ci.yml                        # fast PR lane: lint + unit tests + type checks
├─ 🧾 ui.yml                        # web lint/test/build (path-aware)
├─ 🧾 markdown-protocol.yml         # docs: YAML front-matter + required sections gate (v13 minimum)
├─ 🧾 docs-linkcheck.yml            # doc link checker (v13 minimum)
├─ 🧾 schema-validate.yml            # JSON schema lane: STAC/DCAT/PROV + story schema (v13 minimum)
├─ 🧾 graph-integrity.yml           # Neo4j fixture + constraint checks (v13 minimum)
├─ 🧾 api-contract.yml              # OpenAPI/GraphQL diff + contract tests (contract-first)
├─ 🧾 dependency-review.yml         # dependency review for PRs
├─ 🧾 catalog-qa.yml                # fast STAC/DCAT sanity + link safety gate
├─ 🧾 kfm-policy-gate.yml           # Conftest/Rego: governance + supply chain + sovereignty
├─ 🧾 stac-validate.yml             # full STAC schema lane (scheduled/manual)
├─ 🧾 dcat-validate.yml             # DCAT lane (scheduled/manual)
├─ 🧾 prov-validate.yml             # PROV lane (scheduled/manual)
├─ 🧾 integration.yml               # PostGIS (+ graph) + API contract integration tests
├─ 🧾 perf.yml                      # bundle size + query timing budgets (scheduled)
├─ 🧾 model-regression.yml          # metrics drift + reproducibility checks (scheduled)
├─ 🧾 docker.yml                    # build/push images (GHCR)
├─ 🧾 publish-catalog.yml           # env-gated catalog promotion (atomic publish)
├─ ✅ codeql.yml                    # SAST (scheduled + optional PR)
├─ ✅ pages.yml                     # docs/viewer deploy (optional)
├─ 🧾 release.yml                   # release packaging + changelog + provenance
├─ 🧾 sbom.yml                      # SBOM generation (SPDX/CycloneDX)
├─ 🧾 attest.yml                    # build provenance attestations (SLSA-ish)
├─ 🧾 scorecard.yml                 # OpenSSF Scorecard (optional)
├─ 🧾 actionlint.yml                # workflow lint (recommended)
├─ 🧾 agents-watcher.yml            # optional: read-only agent watcher
├─ 🧾 agents-planner.yml            # optional: deterministic planner
├─ 🧾 agents-executor.yml           # optional: PR-only executor (no merge)
├─ 🧾 detect-validate-promote.yml   # optional: change detection → lanes → signed PR
└─ 📄 README.md                     # you are here 👋
```

---

<a id="workflow-catalog"></a>

## 🗂️ Workflow catalog

> If a workflow file isn’t present yet, treat this table as the **spec** for creating it.

| Workflow 📄              | Lane      | Protects ✅                                 | Triggers ⏱️                                                                 | Budget 🎯 | Key outputs 📦                                          |
| ------------------------ | --------- | ------------------------------------------ | --------------------------------------------------------------------------- | --------: | ------------------------------------------------------- |
| `ci.yml`                 | PR        | code integrity                              | `pull_request`, `push main`                                                 |  ≤ 10 min | junit, coverage, logs                                   |
| `ui.yml`                 | PR        | UI build integrity                          | PR paths `web/**`                                                           |  ≤ 12 min | build logs, bundle report                               |
| `markdown-protocol.yml`  | PR        | docs governance                             | PR paths `docs/**`, `docs/reports/story_nodes/**`, templates                |   ≤ 7 min | front-matter report, missing-sections report            |
| `docs-linkcheck.yml`     | PR        | docs reliability                            | PR paths `docs/**`, `**/*.md`                                               |  ≤ 10 min | link report                                             |
| `schema-validate.yml`    | PR        | schema conformance                          | PR paths `schemas/**`, `data/catalog/**`, `data/prov/**`, story metadata    |  ≤ 12 min | schema report (STAC/DCAT/PROV/Story)                    |
| `graph-integrity.yml`    | PR        | ontology + graph shape                      | PR paths `src/graph/**`, ontology docs, story entity refs                   |  ≤ 12 min | constraint report, fixture ingest logs                   |
| `api-contract.yml`       | PR        | contract-first API boundary                  | PR paths `src/server/**`, `src/server/contracts/**`                         |  ≤ 10 min | openapi diff, contract test report                      |
| `dependency-review.yml`  | PR        | dependency risk signal                       | `pull_request` (code changes)                                               |   ≤ 5 min | dependency review output                                |
| `catalog-qa.yml`         | PR        | metadata “foot-guns”                        | PR paths `data/**`, `schemas/**`, `tools/validation/**`                     |   ≤ 7 min | QA report (required fields + link safety)               |
| `kfm-policy-gate.yml`    | PR        | governance + supply chain + sovereignty     | PR paths `data/**`, `docs/**`, `.github/**`, `tools/validation/policy/**`   |   ≤ 7 min | conftest report                                         |
| `codeql.yml`             | schedule  | SAST                                        | schedule (+ optional PR)                                                    |       n/a | SARIF                                                   |
| `integration.yml`        | schedule  | real DB/API                                 | schedule + dispatch                                                         | 10–45 min | logs, junit                                             |
| `stac-validate.yml`      | schedule  | STAC conformance                            | schedule + dispatch                                                         | 10–30 min | schema report                                           |
| `dcat-validate.yml`      | schedule  | DCAT conformance                            | schedule + dispatch                                                         | 10–30 min | schema report                                           |
| `prov-validate.yml`      | schedule  | PROV integrity                              | schedule + dispatch                                                         | 10–30 min | schema report                                           |
| `perf.yml`               | schedule  | perf budgets                                | schedule + dispatch                                                         | 10–30 min | perf report                                             |
| `model-regression.yml`   | schedule  | reproducibility (metrics drift)             | schedule + dispatch                                                         | 10–45 min | metrics + artifacts                                     |
| `publish-catalog.yml`    | env-gated | atomic publish                              | `workflow_dispatch`                                                         |       n/a | catalogs + PROV + digests                               |
| `docker.yml`             | main/tag  | images                                      | `push main`, tags                                                           |  ≤ 30 min | OCI images + digests                                    |
| `release.yml`            | tag       | releases                                    | tags                                                                        |       n/a | release assets                                          |
| `sbom.yml`               | tag/main  | SBOM                                        | tags + main                                                                 |       n/a | SPDX/CycloneDX                                          |
| `attest.yml`             | tag/main  | attestations                                | tags + main                                                                 |       n/a | build provenance attestation                            |
| `agents-*.yml`           | optional  | governed PR automation                      | schedule/dispatch                                                           |  ≤ 15 min | plans + PRs (no merge)                                  |

---

<a id="change-aware-gate-matrix"></a>

## 🚦 Change-aware gate matrix

Make gates **path-aware** so PR checks stay fast and relevant (and align to v13 subsystem homes).[^mg13-v13-structure]

| Change type        | Examples                                                       | Required gates                                                                 |
| ------------------ | -------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| 🧠 Core code       | `src/**` pipelines, parsing, core logic                         | `ci.yml` (+ CodeQL as configured)                                              |
| 🧪 Pipelines       | `src/pipelines/**` + pipeline configs                           | `ci.yml` + `catalog-qa.yml` + `schema-validate.yml`                            |
| 🗺️ Data/catalog   | `data/**`, `data/catalog/**`, `data/prov/**`, `schemas/**`      | `catalog-qa.yml` + `schema-validate.yml` + `kfm-policy-gate.yml`               |
| 🕸️ Graph/ontology | `src/graph/**`, ontology docs, entity ID registries             | `graph-integrity.yml` + `ci.yml` (+ integration optional)                      |
| 🧩 API boundary    | `src/server/**`, `src/server/contracts/**`                      | `ci.yml` + `api-contract.yml` (+ integration optional)                         |
| 🌐 Web UI          | `web/**`                                                       | `ui.yml` + `ci.yml`                                                            |
| 🎬 Story nodes     | `docs/reports/story_nodes/**`                                   | `markdown-protocol.yml` + `docs-linkcheck.yml` + `schema-validate.yml` + policy |
| 🔐 Workflows       | `.github/workflows/**`, `.github/actions/**`                    | `actionlint.yml` + `kfm-policy-gate.yml` + human review                        |
| 📚 Docs-only       | `docs/**`                                                      | `markdown-protocol.yml` + `docs-linkcheck.yml` (+ policy when governance applies) |

> [!CAUTION]
> Workflows are security-sensitive. Treat them like production code. 🔐

---

<a id="promotion-gates"></a>

## 🧱 Promotion gates

KFM uses an intentionally gate‑enforced lifecycle: **stage → validate → (optionally attest) → promote via PR → publish**.

```mermaid
flowchart LR
  RAW["📥 Stage<br/>raw inputs / edits"] --> VAL["🔎 Validate<br/>schema + links + bounds + policy"]
  VAL -->|pass ✅| PR["🧾 PR-first promotion<br/>signed PR + review"]
  VAL -->|fail ❌| STOP["🧯 Stop (fail-closed)<br/>no broken catalogs"]
  PR --> MERGE["🔀 Merge to protected branch<br/>required checks green"]
  MERGE --> PUB["📦 Publish (atomic)<br/>assets + catalogs + provenance"]
  PUB --> FED["🌐 Federation-ready<br/>STAC + DCAT + PROV"]
```

### ✅ What “promotion” means (KFM-shaped)

Promotion is not “copying files somewhere.” It means:

* 🗂️ catalogs are complete (STAC/DCAT)
* 🧾 lineage exists (PROV: inputs → activities → outputs)
* ✅ QA passed (schema, links, bounds, CRS, sensitivity)
* 🔐 access rules are respected (public vs restricted)
* ♻️ publish is atomic (no partial catalogs)

### 🔏 Attestation & provenance (recommended)

For anything published:

* attach an **SBOM** for build artifacts (and optionally data tooling containers)
* emit a **build provenance** record (SLSA-ish / GitHub attestations)
* store PROV JSON‑LD alongside catalogs for audit and rollback

---

<a id="policy-as-code-gates"></a>

## 🧑‍⚖️ Policy as code gates (OPA/Rego + Conftest)

Policy gates are how FAIR+CARE becomes enforceable, not aspirational. ⚖️✅

### 🎯 What policy gates should enforce

**Governance / data integrity**

* license & attribution required for promoted datasets
* sensitive-location rules (generalize/omit/limit precision)
* provenance required (no “mystery layers”)
* catalog conventions (stable IDs, required fields, extension allow/deny lists)
* “classification propagation” (outputs inherit restrictions)

**Catalog safety**

* safe link rules (`links[].href` allow/deny lists; no unsafe schemes)
* metadata profile expectations for STAC/DCAT/PROV
* policy outcomes must be human-readable (“what failed” + “how to fix”)

**Supply chain safety**

* workflow permissions least‑privilege
* GitHub Actions pinning rules (prefer pinned versions; migrate toward SHA pinning)
* promotion jobs are kill‑switch protected

### 📁 Canonical policy layout

> ✅ Matches the KFM policy structure under `tools/validation/policy/` (with Rego grouped by domain, plus tests and samples).  
> *(If you don’t have it yet: treat this as the target shape.)*

```text
📁 tools/validation/policy/
├─ 📄 README.md
├─ 📁 rego/
│  ├─ 📁 common/
│  │  ├─ 📄 helpers.rego
│  │  ├─ 📄 license_allowlist.rego
│  │  └─ 📄 url_allowlist.rego
│  ├─ 📁 catalogs/
│  │  ├─ 📄 stac_required.rego
│  │  ├─ 📄 dcat_required.rego
│  │  ├─ 📄 prov_required.rego
│  │  └─ 📄 link_safety.rego
│  ├─ 📁 governance/
│  │  ├─ 📄 classification_propagation.rego
│  │  ├─ 📄 sensitive_locations.rego
│  │  └─ 📄 attribution.rego
│  ├─ 📁 supply_chain/
│  │  ├─ 📄 workflows_least_privilege.rego
│  │  └─ 📄 actions_pinning.rego
│  └─ 📄 bundles.rego
└─ 📁 tests/
   ├─ 📄 *_test.rego
   └─ 📁 samples/
      ├─ 📁 good/
      └─ 📁 bad/
```

### ✅ Conftest workflow pattern (PR gate)

**When to run**

* PR touches `data/**`, `docs/**`, `schemas/**`, `.github/**`, `tools/validation/policy/**`

**How to run**

* no secrets
* `permissions: contents: read`
* short timeout
* upload report artifact on failure
* run Rego tests in CI (`conftest verify` / `opa test` via conftest patterns)

Example command shapes:

```bash
# policy checks against repo content
conftest test \
  -p tools/validation/policy/rego \
  --all-namespaces \
  .

# policy unit tests (Rego tests)
conftest verify \
  -p tools/validation/policy/rego \
  tools/validation/policy/tests
```

> [!TIP]
> Keep policy rules “deny by default” and explain failures clearly (“what failed” + “how to fix”). 🧯

---

<a id="agent-automation-lane"></a>

## 🤖 Agent automation lane (optional) — Watcher · Planner · Executor

KFM supports optional agent automation only if it stays **governed**, **deterministic**, and **PR‑first**.

### ✅ Allowed agent behaviors

* 👀 **Watcher**: read‑only signals (facts/alerts), no side effects
* 🧠 **Planner**: deterministic planning (seeded, repeatable), no network by default
* 🧰 **Executor**: runs gates and opens/updates PRs **without merge permissions**

### 🧯 Kill-switch (non-negotiable)

Agents and promotion workflows must honor a central kill switch:

* 📄 `.kfm/kill-switch.yml` *(file-based; fail‑closed)*
* plus a repo variable/secret (example): `KFM_KILL_SWITCH=true`

Recommended pattern:

* every workflow that can publish/sign calls a shared step/action first
* if enabled: stop **before** any publish/sign step

> ✅ Preferred: a composite action like `/.github/actions/check-kill-switch` so logic stays consistent everywhere.

### 🔐 Token scopes (non-negotiable)

* Watcher/Planner: **read-only** tokens (or none)
* Executor: short‑lived token that can **open PRs**, but **cannot merge**
* Branch protections remain the human safety rail ✅

### 🧾 Artifact expectations

Agent runs should emit:

* a plan (`plan.yml`) + deterministic diff (`diff.patch`)
* gate results (`reports/gates.json`)
* provenance (`prov.jsonld`) + (optional) OpenLineage event JSON
* a PR body that links to evidence artifacts (no vibes)

> [!IMPORTANT]
> If any gate fails, Executor **does not** open/update a PR. It emits evidence and stops. 🚦

---

<a id="data--catalog-gates"></a>

## 🗺️ Data + catalog gates (KFM-specific)

KFM’s pipelines are expected to be deterministic and to emit standardized outputs under `data/processed/` along with catalog + provenance updates.[^kfm-tech-pipeline]

### ✅ STAC/DCAT quick gate (fast PR filter)

Runs on PRs that touch `data/**` (and validator code). Prevents broken catalogs from merging.

**Checks (fast):**

* required fields present (`license`, `providers`, ids, titles) ✅
* critical `links[].href` checked (safe schemes + allowlists; no SSRF foot-guns) ✅
* schema sanity on a small fixture subset ✅
* policy gate alignment (classification + attribution + link safety) ✅

### 🧭 CRS + bounds sanity

Geospatial bugs often come from silent CRS drift:

* required EPSG values present where expected
* bbox/footprint valid
* Kansas bounds sanity (when claiming Kansas scope)
* geometry validity checks (self-intersections, empties)

> [!CAUTION]
> PR gates should be fast (fixtures + metadata). Deep checks belong in scheduled lanes. 🌙

### 🧰 `tools/validation/` (Catalog QA)

KFM’s technical documentation calls out a **Catalog QA** tool under `tools/validation/` that scans catalog JSON for required fields and integrity checks.[^kfm-tech-validation]

---

<a id="graph--semantics-gates"></a>

## 🕸️ Graph + semantics gates

KFM’s graph is the “semantic backbone” for Story Nodes and Focus Mode (and for any AI‑assist that relies on governed graph context).[^kfm-tech-graph]

### ✅ Graph integrity gates should enforce

* stable entity IDs (no renaming without migration notes)
* relationship shape validation (allowed edge types)
* reference integrity (Story Node entity IDs exist)
* fixture build + constraints tests (unique IDs, required properties, etc.)[^mg13-ci-min]

> Why this matters: Story Nodes + Focus Mode depend on stable entity IDs and traceable links, not ad‑hoc strings.[^mg13-story-focus]

---

<a id="story-nodes--focus-mode-gates"></a>

## 🎬 Story Nodes + Focus Mode gates

Story Nodes and Focus Mode are **trust-sensitive** because they look authoritative.

### ✅ Story Node lint should enforce (evidence-first)

From the v13 guide, Story Nodes must:[^mg13-story-focus]

* include provenance/citations for every claim
* reference graph entities via stable identifiers
* distinguish fact vs interpretation (especially with AI assistance)
* honor sensitivity rules (precision, sovereignty)
* only reference assets that exist and are licensed

### ✅ Focus Mode rules (hard gate)

Focus Mode has strict “trust rules” — CI should treat these as non‑negotiable invariants:[^mg13-focus-mode]

* **only provenance‑linked content** is allowed to render
* **AI contributions must be opt‑in** and clearly labeled with uncertainty/confidence
* **no sensitive location leaks** — maps must generalize/omit sensitive points

### 🧾 Audit trail expectation (telemetry)

The v13 guide explicitly calls for audit trails for sensitive/withheld content events (e.g., emitting `focus_mode_redaction_notice_shown`).[^mg13-audit]

> [!TIP]
> Consider a small UI integration test that asserts: “sensitive layer rendered → redaction notice shown → telemetry event emitted”.

---

<a id="integration-tests"></a>

## 🧪 Integration tests

KFM’s spatial correctness depends on real PostGIS (and optionally a graph DB). Prefer containerized integration tests.

### Option A: GitHub Actions service containers (fast + simple)

**PostGIS service**

```yaml
services:
  db:
    image: postgis/postgis:15-3.4
    env:
      POSTGRES_DB: kfm_test
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - 5432:5432
    options: >-
      --health-cmd="pg_isready -U postgres -d kfm_test"
      --health-interval=10s
      --health-timeout=5s
      --health-retries=10
```

**Neo4j (optional)**

```yaml
services:
  neo4j:
    image: neo4j:5
    env:
      NEO4J_AUTH: neo4j/testpass
    ports:
      - 7474:7474
      - 7687:7687
```

> [!CAUTION]
> The #1 cause of CI flake is “tests started before DB was ready.”  
> Always add health checks + explicit waits. ✅

### Option B: Docker Compose (multi-service parity)

Best when you need API + workers + DB + cache for realistic end‑to‑end tests.

---

<a id="web-ui-gates"></a>

## 🌐 Web UI gates (responsive + WebGL + 3D)

KFM’s UI is map‑first and may include WebGL/3D content. v13 explicitly treats the UI as downstream of governed APIs and catalogs.[^mg13-invariants]

Recommended CI checks:

* ✅ `npm ci` (lockfile respected)
* ✅ lint (`eslint`) + format (`prettier`)
* ✅ typecheck (`tsc --noEmit`)
* ✅ tests (unit/component)
* ✅ build (`npm run build`) + size budgets (optional)

### 🧊 3D Web GIS realism check

3D web GIS platforms are widely used to store/manage/display/analyze spatial info via the web on a 3D visualization canvas, enabling broader collaboration without desktop installs.[^arch-3d-web]  
Real-world examples combine **WebGL + JavaScript + PostgreSQL**, which is a useful mental model for KFM’s 3D future lanes and integration tests.[^arch-3d-web]

WebGL/3D hygiene:

* treat 3D assets (tilesets/models) as **untrusted inputs**
* avoid unsafe HTML injection patterns in popups/tooltips
* validate/limit asset sizes (prevent “one model = one outage”)
* keep bundle size predictable (budgets catch bloat early)

---

<a id="modeling--simulation-gates"></a>

## 📈 Modeling + simulation gates (analysis discipline)

KFM treats model outputs as governed artifacts (not screenshots).

Recommended gates for published analysis:

* deterministic seeds + pinned inputs
* train/test split & leakage checks (where relevant)
* uncertainty reporting / sensitivity notes
* artifacts stored (plots, metrics, model cards)
* provenance linking inputs → transforms → outputs

> [!TIP]
> Put heavy modeling checks in scheduled lanes; keep PR smoke tests tiny. 🧪

---

<a id="performance-gates"></a>

## ⚡ Performance gates (budgeted, scheduled)

Performance regressions are easier to prevent than to debug.

Recommended budgets:

* web bundle size ceilings
* API p95 latency budgets on a small fixture dataset
* expensive query guardrails (rate limits / timeouts / “explain analyze” thresholds)
* pipeline runtime budgets on representative fixtures

### 🧠 Graph query budgets (inspired by modern graph engines)

Research on graph execution emphasizes push‑based pipelines, graph‑specific operators (e.g., scans/expands), and “pipeline breaker” materialization points.[^scalable-data-push]  
That maps cleanly to a practical KFM CI budget strategy:

* maintain a small set of “known expensive” Cypher queries
* run them on a fixture graph nightly
* fail if p95 or max crosses a budget threshold
* keep explain plans as artifacts for diffing

✅ Run perf checks on schedule and/or manual dispatch to avoid slowing PRs.

---

<a id="security-scanning"></a>

## 🔐 Security scanning (SAST, deps, secrets, containers)

Baseline expectations:

* ✅ Dependency Review on PRs
* ✅ CodeQL scanning (Python + JS/TS + Actions as applicable)
* ✅ Secret scanning + push protection (GitHub features)
* ✅ Container scan on `main` + tags (recommended)

Supply chain hardening (recommended):

* SBOM generation (SPDX/CycloneDX)
* build attestations (SLSA‑ish / GitHub attestations)
* pin GitHub Actions (major version now; migrate toward SHA pinning)

> [!NOTE]
> For forks: publishing workflows must not run with secrets on untrusted PRs.  
> Keep publish steps on `push main`, tags, or `workflow_dispatch`.

---

<a id="artifacts--traceability"></a>

## 📦 Artifacts & traceability (standardize outputs)

Standardize artifact names across workflows for debuggability + audit:

* `unit-test-results.xml` / `pytest.xml`
* `coverage.xml` (+ optional HTML coverage)
* `frontmatter-report.json` *(Markdown protocol outputs)*
* `linkcheck-report.json`
* `schema-report.json` *(STAC/DCAT/PROV/Story validation)*
* `catalog-qa-report.json`
* `policy-report.txt` *(conftest output)*
* `graph-integrity-report.json` *(constraints + fixture checks)*
* `api-contract-report.json` *(OpenAPI diff + contract tests)*
* `reports/gates.json` *(machine-readable gate results)*
* `prov.jsonld` *(W3C PROV; run lineage)*
* `build-info.json` *(build metadata + inputs + digests)*
* `sbom.spdx.json` *(or CycloneDX equivalent)*
* `build_provenance.json` *(SLSA-ish attestation payload)*
* zipped logs on failure (`logs.zip`)

💡 Naming tip: include workflow + sha → `catalog-qa-${{ github.sha }}`

---

<a id="secrets--environments"></a>

## 🧷 Secrets & environments (least privilege by default)

Common secrets:

* `GITHUB_TOKEN` (often enough for GHCR with `packages: write`)
* deploy credentials (only in protected environments)
* third-party tokens (scoped + rotated)

✅ Use GitHub **Environments** (`dev`, `stage`, `prod`) to:

* scope secrets safely
* require approvals for `prod`
* attach deploy history to commits

Recommended permissions default:

```yaml
permissions:
  contents: read
```

Escalate only when needed:

* `packages: write` for GHCR push
* `security-events: write` for SARIF upload
* `id-token: write` for OIDC to cloud / Sigstore-style attestations

---

<a id="reusable-workflows--composite-actions"></a>

## 🧩 Reusable workflows & composite actions

When workflows multiply, duplication becomes entropy. Prefer:

* ✅ **Reusable workflows** (`workflow_call`) for common CI building blocks
* ✅ **Composite actions** for tiny shared step sets (setup + caching + standardized reporting)

### 🧩 Suggested composite actions layout (KFM-aligned)

```text
📁 .github/actions/
├─ 📁 setup-kfm/                  # 🧰 shared env setup (python/node/tools) (optional)
├─ 📁 setup-conftest/             # 🧑‍⚖️ conftest/OPA install + cache
├─ 📁 check-kill-switch/          # 🧯 centralized kill-switch gate (read-only)
├─ 📁 markdown-protocol/          # 🧾 front-matter + required sections
├─ 📁 docs-linkcheck/             # 🔗 link + citation validation
├─ 📁 schema-validate/            # 🧷 schema validation wrapper (STAC/DCAT/PROV/story)
├─ 📁 catalog-qa/                 # 🗃️ fast STAC/DCAT QA + link safety
├─ 📁 policy-gate/                # ⚖️ conftest execution wrapper + reporting
├─ 📁 graph-integrity/            # 🕸️ fixture ingest + constraint checks
├─ 📁 api-contract/               # 📜 OpenAPI diff + GraphQL schema check
├─ 📁 sbom/                       # 📦 generate SBOM (SPDX/CycloneDX)
├─ 📁 attest/                     # 🖊️ attest build provenance (OIDC / GitHub attestation)
├─ 📁 build-info/                 # 🧾 emit build-info.json (inputs/digests)
└─ 📁 docker-build/               # 🐳 docker build/push with labels + digests
```

### ♻️ Suggested reusable workflows layout

```text
📁 .github/workflows/
└─ 📁 reusables/
   ├─ 📄 kfm-reusable-ci.yml
   ├─ 📄 kfm-reusable-policy.yml
   ├─ 📄 kfm-reusable-catalog-qa.yml
   ├─ 📄 kfm-reusable-ui.yml
   └─ 📄 kfm-reusable-schema-validate.yml
```

Example: call a reusable workflow

```yaml
jobs:
  python:
    uses: ./.github/workflows/reusables/kfm-reusable-ci.yml
    with:
      python-version: "3.12"
```

---

<a id="starter-templates"></a>

## 🛠️ Starter templates (copy / paste)

> Keep PR checks fast, make heavy lanes scheduled, and always upload logs on failure. 🥇  
> These examples show *shape*, not your repo’s final truth — adjust paths for your actual layout.

<details>
<summary><strong>🧪 <code>ci.yml</code> — Python lint + unit tests (fast PR lane)</strong></summary>

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true

jobs:
  python:
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"

      - name: Install deps
        run: |
          python -m pip install -U pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
          if [ -f requirements-dev.txt ]; then pip install -r requirements-dev.txt; fi
          if [ -f src/server/requirements.txt ]; then pip install -r src/server/requirements.txt; fi

      - name: Lint
        run: |
          ruff check .
          ruff format --check .

      - name: Unit tests
        run: |
          pytest -q --junitxml=unit-test-results.xml --cov=. --cov-report=xml

      - name: Upload test artifacts
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: ci-python-${{ github.sha }}
          path: |
            unit-test-results.xml
            coverage.xml
```

</details>

<details>
<summary><strong>🧾 <code>markdown-protocol.yml</code> — Front-matter + required doc sections gate</strong></summary>

```yaml
name: Markdown Protocol (KFM)

on:
  pull_request:
    paths:
      - "docs/**"
      - "docs/reports/story_nodes/**"
      - "docs/templates/**"
      - ".github/workflows/markdown-protocol.yml"

permissions:
  contents: read

jobs:
  markdown-protocol:
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - uses: actions/checkout@v4

      # Replace with your actual validator (python/node) implementation
      - name: Validate governed markdown
        run: |
          python tools/validation/markdown_protocol.py \
            --paths docs docs/reports/story_nodes docs/templates \
            --out frontmatter-report.json

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: markdown-protocol-${{ github.sha }}
          path: |
            frontmatter-report.json
```

</details>

<details>
<summary><strong>🧷 <code>schema-validate.yml</code> — STAC/DCAT/PROV/Story schema validation</strong></summary>

```yaml
name: Schema Validate

on:
  pull_request:
    paths:
      - "schemas/**"
      - "data/catalog/**"
      - "data/prov/**"
      - "docs/reports/story_nodes/**"
      - ".github/workflows/schema-validate.yml"
  workflow_dispatch:

permissions:
  contents: read

jobs:
  schema:
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - uses: actions/checkout@v4

      # Replace with your preferred validator tooling:
      # - python-jsonschema
      # - stac-validator
      # - custom KFM profile checker
      - name: Validate schemas (shape)
        run: |
          python tools/validation/schema_validate.py \
            --schemas schemas \
            --stac data/catalog \
            --dcat data/catalog/dcat \
            --prov data/prov \
            --story docs/reports/story_nodes \
            --out schema-report.json

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: schema-validate-${{ github.sha }}
          path: |
            schema-report.json
```

</details>

<details>
<summary><strong>🌐 <code>ui.yml</code> — Web UI lint + test + build</strong></summary>

```yaml
name: UI

on:
  pull_request:
    paths:
      - "web/**"
      - ".github/workflows/ui.yml"
  push:
    branches: [main]
    paths:
      - "web/**"

permissions:
  contents: read

concurrency:
  group: ui-${{ github.ref }}
  cancel-in-progress: true

jobs:
  web:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    defaults:
      run:
        working-directory: web

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"
          cache-dependency-path: web/package-lock.json

      - name: Install
        run: npm ci

      - name: Lint
        run: npm run lint --if-present

      - name: Typecheck
        run: npm run typecheck --if-present

      - name: Test
        run: npm test --if-present

      - name: Build
        run: npm run build

      - name: Upload build artifacts (optional)
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: ui-${{ github.sha }}
          path: |
            web/dist/**
```

</details>

<details>
<summary><strong>⚖️ <code>kfm-policy-gate.yml</code> — Conftest/Rego policy checks</strong></summary>

```yaml
name: KFM Policy Gate (Conftest)

on:
  pull_request:
    paths:
      - "data/**"
      - "docs/**"
      - "schemas/**"
      - ".github/**"
      - "tools/validation/policy/**"
      - ".github/workflows/kfm-policy-gate.yml"

permissions:
  contents: read

jobs:
  policy:
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - uses: actions/checkout@v4

      - name: Setup conftest (composite)
        uses: ./.github/actions/setup-conftest

      - name: Run policy checks
        run: |
          set -euo pipefail
          conftest test \
            -p tools/validation/policy/rego \
            --all-namespaces \
            .

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: policy-gate-${{ github.sha }}
          path: |
            policy-report.txt
            tools/validation/policy/tests/**
```

</details>

<details>
<summary><strong>🧬 <code>integration.yml</code> — PostGIS + integration tests (scheduled)</strong></summary>

```yaml
name: Integration

on:
  workflow_dispatch:
  schedule:
    - cron: "0 4 * * *" # daily @ 04:00 UTC (adjust)

permissions:
  contents: read

jobs:
  integration:
    runs-on: ubuntu-latest
    timeout-minutes: 45

    services:
      db:
        image: postgis/postgis:15-3.4
        env:
          POSTGRES_DB: kfm_test
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        ports:
          - 5432:5432
        options: >-
          --health-cmd="pg_isready -U postgres -d kfm_test"
          --health-interval=10s
          --health-timeout=5s
          --health-retries=10

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"

      - name: Install deps
        run: |
          python -m pip install -U pip
          if [ -f requirements-dev.txt ]; then pip install -r requirements-dev.txt; fi
          if [ -f src/server/requirements.txt ]; then pip install -r src/server/requirements.txt; fi

      - name: Run integration tests
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/kfm_test
        run: |
          pytest -q -m "integration" --junitxml=integration-results.xml

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: integration-${{ github.sha }}
          path: |
            integration-results.xml
            logs/**
```

</details>

---

<a id="debug-locally"></a>

## 🧰 Debug locally

Preferred order:

1. ✅ run the same commands CI runs (best parity)
2. 🐳 use Compose profiles to mimic integration dependencies
3. 🧪 use `act` to simulate Actions locally *(helpful, not perfect)*

---

<a id="adding-a-new-workflow-checklist"></a>

## 🧾 Adding a new workflow checklist

* [ ] Name jobs after outcomes (`lint`, `unit-tests`, `catalog-qa`, `schema-validate`, `graph-integrity`, `build-image`)
* [ ] Keep PR checks fast (aim ≤ ~10–12 minutes)
* [ ] Put heavy jobs behind schedules or manual dispatch
* [ ] Cache dependencies (pip/npm) and Docker layers
* [ ] Upload artifacts on failure (logs are gold 🥇)
* [ ] Avoid secrets on `pull_request` from forks
* [ ] Use minimal `permissions:` and elevate only when needed
* [ ] Add `concurrency:` cancellation to reduce queue noise
* [ ] Keep the KFM order intact: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**[^mg13-pipeline]
* [ ] If data/model outputs ship: require **PROV + digests + policy gates**
* [ ] Ensure v13 minimum gates are covered: **Markdown protocol, links, schemas, graph integrity**[^mg13-ci-min]
* [ ] For automation/agents: honor **kill-switch + determinism + PR‑only** 🧯🤖

---

<a id="reference-library--influence-map"></a>

## 📚 Reference library & influence map

> ⚠️ Reference materials may have different licenses than repo code.  
> Prefer storing large PDFs under `docs/library/` (or outside the repo) and respecting upstream terms (or use Git LFS). 🧾

<details>
<summary><strong>🧠 Why CI/CD mentions the “reading pack”</strong></summary>

KFM is a hybrid platform: **GIS + data engineering + web + modeling + governance**.  
CI/CD is where those disciplines become repeatable guardrails:

* ✅ data integrity gates (catalogs, provenance, digests)
* ✅ modeling hygiene (V&V, uncertainty, experimental design)
* ✅ secure-by-default workflows (DevSecOps + supply chain)
* ✅ performance budgets (caching, parallelism, scheduled lanes)
* ✅ map/UI constraints (responsive + WebGL realities)

</details>

<details>
<summary><strong>🧭 Canonical KFM specs used by this CI/CD README</strong></summary>

* **Master Guide v13 (draft):** `MARKDOWN_GUIDE_v13.md.gdoc`  [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
* **System technical documentation:** `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  

</details>

<details>
<summary><strong>📚 Project files that influence CI/CD (full inventory)</strong></summary>

### 🧾 Governance + system shape (contracts + evidence)

* `MARKDOWN_GUIDE_v13.md.gdoc`  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
* `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 🗺️ GIS + cartography + spatial databases

* `python-geospatial-analysis-cookbook.pdf`
* `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
* `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
* `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`

### 🧱 3D / Web GIS & visualization (WebGL / 3D)

* `Archaeological 3D GIS_26_01_12_17_53_09.pdf`  [oai_citation:4‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)
* `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
* `responsive-web-design-with-html5-and-css3.pdf`
* `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### 🛰️ Remote sensing workflows

* `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`

### 📈 Statistics, experiments, modeling discipline

*️* `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
* `Understanding Statistics & Experimental Design.pdf`
* `regression-analysis-with-python.pdf`
* `Regression analysis using Python - slides-linear-regression.pdf`
* `graphical-data-analysis-with-r.pdf`
* `think-bayes-bayesian-statistics-in-python.pdf`

### ⚙️ Systems, scalability, and performance

* `Database Performance at Scale.pdf`  [oai_citation:5‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)
* `Scalable Data Management for Future Hardware.pdf`  [oai_citation:6‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)
* `Data Spaces.pdf`  [oai_citation:7‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a)
* `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`

### 🧮 Graphs, optimization, and advanced math

* `Spectral Geometry of Graphs.pdf`
* `Generalized Topology Optimization for Structural Design.pdf`
* `Basics of Linear Algebra for Machine Learning (…pdf)`  [oai_citation:8‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

### ❤️ Ethics, autonomy, governance, and AI/legal framing

* `Introduction to Digital Humanism.pdf`
* `Principles of Biological Autonomy - book_9780262381833.pdf`
* `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`

### 🛡️ Security (defensive references)

* `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
* `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

### 🧰 General programming shelf (bundles + utilities)

* `Bash Notes for Professionals.pdf`  [oai_citation:9‡Database Performance at Scale.pdf](file-service://file-36z8qyiVJRtrSs6QG7Epen)
* `Understanding Machine Learning_ From Theory to Algorithms.pdf`  [oai_citation:10‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)
* `Flexible Software Design_ Systems Development for Computational Science.pdf`  [oai_citation:11‡U-X programming Books.pdf](file-service://file-3hYtSGHtHmb6wyTtavym6M)
* `A programming Books.pdf`  [oai_citation:12‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ)
* `B-C programming Books.pdf`  [oai_citation:13‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ)
* `D-E programming Books.pdf`
* `F-H programming Books.pdf`
* `I-L programming Books.pdf`
* `M-N programming Books.pdf`
* `O-R programming Books.pdf`
* `S-T programming Books.pdf`
* `U-X programming Books.pdf`

> [!NOTE]
> `Deep Learning for Coders with fastai and PyTorch - …` exists in the project set but may not be indexable in all tooling contexts.

</details>

---

## 🧾 Evidence notes (citations)

[^mg13-pipeline]: Canonical pipeline ordering in the v13 guide.  [oai_citation:14‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^mg13-contract-first]: “Contract-first” + deterministic pipeline framing.  [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^mg13-invariants]: v13 invariants: ordering, API boundary, provenance-first, deterministic ETL, evidence-first narrative, classification propagation, enforceable gates.  [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^mg13-ci-min]: v13 minimum CI gates (front-matter, link validation, schema validation, graph integrity).  [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^mg13-story-focus]: Story Node requirements and Focus Mode positioning.  [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^mg13-focus-mode]: Focus Mode hard-gate rules: provenance-only, AI opt-in + labeled, no sensitive location leaks.  [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^mg13-audit]: Audit trail expectation (example telemetry event).  [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^mg13-v13-structure]: v13 restructure notes: canonical subsystem homes + new top-level dirs (`schemas/`, `releases/`, `data/prov/`, `data/catalog/dcat/`).  [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^mg13-v13-history]: v13 draft date + profile references + CI/validation gates.  [oai_citation:22‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^kfm-tech-pipeline]: Pipeline behavior and outputs: deterministic pipeline scripts, standardized outputs, catalog/provenance updates.  [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm-tech-validation]: `tools/validation/` called out for catalog QA scanning required fields/integrity.  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm-tech-graph]: Graph supports Focus Mode AI and story/data linking.  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^scalable-data-push]: Push-based query execution with graph-specific operators + pipeline breakers (inspiration for graph perf budgets).  [oai_citation:26‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)
[^arch-3d-web]: Web 3D GIS framing and example stack (WebGL + JS + PostgreSQL).  [oai_citation:27‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2) [oai_citation:28‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

<p align="right"><a href="#top">⬆️ Back to top</a></p>