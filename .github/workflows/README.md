<a id="top"></a>

# 🧰 `.github/workflows/` — CI/CD for Kansas Frontier Matrix (KFM)

<div align="left">

<!-- ✅ Existing workflow badges (these should match real workflow filenames) -->
<a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml/badge.svg" /></a>
<a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml"><img alt="CodeQL" src="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg" /></a>
<a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml"><img alt="Pages" src="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml/badge.svg" /></a>

<!-- 🧭 KFM “shape” badges (conceptual, but grounded in project specs) -->
<img alt="KFM-v13" src="https://img.shields.io/badge/KFM-v13%20blueprint-5865F2" />
<img alt="Master Guide" src="https://img.shields.io/badge/Master%20Guide-v13.0.0--draft%20(2025--12--28)-f59e0b" />
<img alt="Pipeline" src="https://img.shields.io/badge/pipeline-ETL%E2%86%92STAC%2FDCAT%2FPROV%E2%86%92Graph%E2%86%92API%E2%86%92UI%E2%86%92Story%E2%86%92Focus-0ea5e9" />
<img alt="Contract First" src="https://img.shields.io/badge/contract--first-enforced-2563eb" />
<img alt="Evidence First" src="https://img.shields.io/badge/evidence--first-required-10b981" />
<img alt="Policy Pack" src="https://img.shields.io/badge/policy%20pack-Conftest%20%2B%20Rego-0ea5e9" />
<img alt="Provenance" src="https://img.shields.io/badge/provenance-STAC%20%7C%20DCAT%20%7C%20PROV-6f42c1" />
<img alt="Stack" src="https://img.shields.io/badge/stack-PostGIS%20%2B%20Neo4j%20%2B%20FastAPI-111827" />
<img alt="UI" src="https://img.shields.io/badge/UI-React%20%2B%20MapLibre%20(%2B%20Cesium%20optional)-22c55e" />
<img alt="DevSecOps" src="https://img.shields.io/badge/DevSecOps-enabled-black" />
<img alt="CI" src="https://img.shields.io/badge/CI-boring%20by%20design-success" />

</div>

> 🧭 This folder contains GitHub Actions workflows that keep KFM **buildable**, **testable**, **secure**, and **shippable** — across **pipelines → catalogs → graph → API → UI → story nodes → focus mode**.  
> ✅ **North Star:** CI/CD protects *trust* (**contracts + provenance + policy**) first, then *speed* (caching + change‑aware gates).  
> 🚦 **KFM canonical order (non‑negotiable):** **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/MapLibre UI (Cesium optional) → Story Nodes → Focus Mode**.[^mg13-pipeline]

> [!IMPORTANT]
> CI is intentionally **boring** (predictable, repeatable, least‑privilege, auditable).  
> The data, stories, and models are the interesting part. 🗺️✨

---

## 🧾 Workflow policy metadata

| Field | Value |
| --- | --- |
| Folder | `.github/workflows/` |
| Status | Active ✅ |
| Last updated | **2026-01-19** |
| Master Guide baseline | **v13.0.0‑draft (2025‑12‑28)**[^mg13-v13-history] |
| Canonical pipeline invariant | **ETL → STAC/DCAT/PROV → Graph → API → UI → Story → Focus**[^mg13-invariants] |
| Governance | FAIR + CARE (data + people) 🧭[^kfm-arch-governance] |
| CI philosophy | PR‑fast lane + scheduled heavy lanes + env‑gated promotion 🚦 |
| Runner baseline | `ubuntu-latest` *(pin images for hermetic lanes)* 🐧 |
| Least‑privilege default | `permissions: { contents: read }` 🔐 |
| PR‑first promotion | Promotion happens via **signed PRs**, not direct pushes 🧾 |
| Fail‑closed posture | Promotion‑critical workflows stop on policy/metadata/provenance violations 🧯 |
| Canonical catalog paths (v13) | `data/stac/collections/`, `data/stac/items/`, `data/catalog/dcat/`, `data/prov/` 🧾[^mg13-structure] |
| Policy Pack location (today) | `api/scripts/policy/` *(policy pack, Rego + waivers + CI usage)* ⚖️[^kfm-policy-pack] |
| v13 structural target | `schemas/`, `releases/`, `src/server/`, and v13 canonical catalog paths 🧱[^mg13-structure] |

> [!NOTE]
> Some older docs (and legacy repo paths) mention `data/catalog/` and `data/provenance/`.  
> v13 standardizes to `data/stac/…`, `data/catalog/dcat/…`, and `data/prov/…` as the canonical publish boundary.[^mg13-structure]

---

## ⚡ Quick links

| Action | Link |
| --- | --- |
| ✅ All Action runs | https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions |
| 📦 Releases | https://github.com/bartytime4life/Kansas-Frontier-Matrix/releases |
| 🐛 Issues | https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues |
| 🤝 `.github/` Collaboration hub | [`../README.md`](../README.md) |
| 🧭 Repo root overview | [`../../README.md`](../../README.md) |
| 🔐 Security policy | [`../../SECURITY.md`](../../SECURITY.md) *(or `../SECURITY.md` if canonical is inside `.github/`)* |

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
* [🧾 Policy Pack — rule IDs + waivers](#policy-pack--rule-ids--waivers)
* [🧬 Repo provenance lane](#repo-provenance-lane)
* [🤖 Agent automation lane](#agent-automation-lane)
* [🗺️ Data + catalog gates](#data--catalog-gates)
* [🕸️ Graph + semantics gates](#graph--semantics-gates)
* [🎬 Story Nodes + Focus Mode gates](#story-nodes--focus-mode-gates)
* [🧪 Integration tests](#integration-tests)
* [🌐 Web UI gates](#web-ui-gates)
* [📦 Offline packs + AR gates](#offline-packs--ar-gates)
* [📈 Modeling + simulation gates](#modeling--simulation-gates)
* [⚡ Performance gates](#performance-gates)
* [🔐 Security scanning](#security-scanning)
* [🔭 Observability & telemetry](#observability--telemetry)
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
    PR6["catalog-qa.yml<br/>catalog sanity + link safety"]
    PR7["graph-integrity.yml<br/>Neo4j fixture + constraints"]
    PR8["kfm-policy-gate.yml<br/>Policy Pack (Rego/Conftest)"]
    PR9["dependency-review.yml<br/>dep diffs + license signal"]
    PR10["actionlint.yml<br/>workflow lint"]
  end

  subgraph SCHEDULE["🌙 Scheduled Lane (slow • trusted)"]
    N1["integration.yml<br/>PostGIS + Neo4j + API contract tests"]
    N2["stac-validate.yml<br/>full STAC lane"]
    N3["dcat-validate.yml<br/>DCAT lane"]
    N4["prov-validate.yml<br/>PROV lane"]
    N5["perf.yml<br/>bundle + query budgets"]
    N6["model-regression.yml<br/>metrics + reproducibility"]
    N7["repo-provenance.yml<br/>DevOps→PROV ledger"]
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

  subgraph AGENTS["🤖 Agent Lane (optional, PR-only)"]
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
* Optional agents are allowed only if they respect **kill‑switch + determinism + PR‑only**.[^kfm-wpe]

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
* 📈 **Evidence artifacts** (analysis/model/simulation outputs: manifests + seeds + metrics)[^mg13-evidence-artifacts]

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
* Every publishable run emits: run id + inputs + outputs + digests + provenance[^kfm-arch-observability]

> v13 explicitly expects a **deterministic pipeline**: idempotent, config‑driven ETL producing stable outputs for given inputs.[^mg13-invariants]

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
   The frontend must never query Neo4j directly; UI goes through the governed API layer so access control + redaction + schemas stay enforceable.[^mg13-invariants]

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

v13 calls out “one canonical home per subsystem” and standardizes where published boundary artifacts live (STAC/DCAT/PROV).[^mg13-structure]

```text
📦 Repo top-levels (v13 target)
├─ 📁 data/
│  ├─ 📁 raw/                     # staged raw inputs (domain-scoped)
│  ├─ 📁 work/                    # intermediate processing (domain-scoped)
│  ├─ 📁 processed/               # final standardized outputs (domain-scoped)
│  ├─ 📁 stac/
│  │  ├─ 📁 collections/          # STAC collections (published boundary)
│  │  └─ 📁 items/                # STAC items (published boundary)
│  ├─ 📁 catalog/
│  │  └─ 📁 dcat/                 # DCAT JSON-LD (published boundary)
│  └─ 📁 prov/                    # PROV JSON-LD (published boundary)
├─ 📁 schemas/                    # JSON schemas: stac/dcat/prov/storynodes/ui/telemetry
├─ 📁 src/
│  ├─ 📁 pipelines/               # deterministic ETL & normalization
│  ├─ 📁 graph/                   # graph build + constraints + migrations
│  └─ 📁 server/                  # API boundary + contracts + redaction
├─ 📁 web/                        # React UI (MapLibre; optional Cesium)
├─ 📁 docs/
│  ├─ 📁 templates/               # governed templates
│  ├─ 📁 standards/               # governed standards & profiles
│  ├─ 📁 governance/              # FAIR+CARE + sovereignty rules
│  └─ 📁 reports/
│     └─ 📁 story_nodes/          # governed narrative (draft vs published)
├─ 📁 releases/                   # release manifests + bundles (repo-discoverable)
└─ 📁 tests/                      # unit + integration tests
```

### 🧭 Legacy → v13 mapping (practical CI hint)

> CI can support both during migration, but v13 should be treated as canonical.

```text
🧩 Legacy paths sometimes referenced in older docs
- data/catalog/            -> data/stac/ (STAC) + data/catalog/dcat/ (DCAT)
- data/provenance/         -> data/prov/
- api/                     -> src/server/ (v13 consolidation target)
```

---

<a id="what-lives-here"></a>

## 📁 What lives here

> Target shape — add as needed, keep intent stable.  
> Use ✅ for “likely exists now” and 🧾 for “spec / planned”.

```text
📁 .github/workflows/
├─ ✅ ci.yml                        # fast PR lane: lint + unit tests + type checks
├─ 🧾 ui.yml                        # web lint/test/build (path-aware)
├─ 🧾 markdown-protocol.yml         # docs: YAML front-matter + required sections (v13 minimum)
├─ 🧾 docs-linkcheck.yml            # doc link checker (v13 minimum)
├─ 🧾 schema-validate.yml           # JSON schema lane: STAC/DCAT/PROV + story schema (v13 minimum)
├─ 🧾 graph-integrity.yml           # Neo4j fixture + constraint checks (v13 minimum)
├─ 🧾 api-contract.yml              # OpenAPI/GraphQL diff + contract tests (contract-first)
├─ 🧾 dependency-review.yml         # dependency review for PRs
├─ 🧾 catalog-qa.yml                # fast STAC/DCAT sanity + link safety gate
├─ 🧾 kfm-policy-gate.yml           # Policy Pack: Conftest/Rego + waivers.yml handling
├─ 🧾 repo-provenance.yml           # DevOps→PROV ledger (PRs/merges/releases as PROV)
├─ 🧾 stac-validate.yml             # full STAC schema lane (scheduled/manual)
├─ 🧾 dcat-validate.yml             # DCAT lane (scheduled/manual)
├─ 🧾 prov-validate.yml             # PROV lane (scheduled/manual)
├─ 🧾 integration.yml               # PostGIS (+ Neo4j) + API contract integration tests
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

| Workflow 📄 | Lane | Protects ✅ | Triggers ⏱️ | Budget 🎯 | Key outputs 📦 |
| --- | --- | --- | --- | ---: | --- |
| `ci.yml` | PR | code integrity | `pull_request`, `push main` | ≤ 10 min | junit, coverage, logs |
| `ui.yml` | PR | UI build integrity | PR paths `web/**` | ≤ 12 min | build logs, bundle report |
| `markdown-protocol.yml` | PR | docs governance | PR paths `docs/**`, `docs/reports/story_nodes/**`, templates | ≤ 7 min | front-matter report, missing-sections report |
| `docs-linkcheck.yml` | PR | docs reliability | PR paths `docs/**`, `**/*.md` | ≤ 10 min | link report |
| `schema-validate.yml` | PR | schema conformance | PR paths `schemas/**`, `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`, story metadata | ≤ 12 min | schema report (STAC/DCAT/PROV/Story) |
| `graph-integrity.yml` | PR | ontology + graph shape | PR paths `src/graph/**`, ontology docs, story entity refs | ≤ 12 min | constraint report, fixture ingest logs |
| `api-contract.yml` | PR | contract-first API boundary | PR paths `src/server/**` *(and/or legacy `api/**`)* | ≤ 10 min | openapi diff, contract test report |
| `dependency-review.yml` | PR | dependency risk signal | `pull_request` (code changes) | ≤ 5 min | dependency review output |
| `catalog-qa.yml` | PR | metadata “foot-guns” | PR paths `data/**`, `schemas/**`, validator tools | ≤ 7 min | QA report (required fields + link safety) |
| `kfm-policy-gate.yml` | PR | governance + sovereignty + supply chain | PR paths `data/**`, `docs/**`, `.github/**`, `api/scripts/policy/**` | ≤ 7 min | policy report + waiver decisions |
| `repo-provenance.yml` | schedule/main | “repo as dataset” ledger | schedule + `push main` + tags | ≤ 10 min | `devops-prov.jsonld`, digests |
| `codeql.yml` | schedule | SAST | schedule (+ optional PR) | n/a | SARIF |
| `integration.yml` | schedule | real DB/API | schedule + dispatch | 10–45 min | logs, junit |
| `stac-validate.yml` | schedule | STAC conformance | schedule + dispatch | 10–30 min | schema report |
| `dcat-validate.yml` | schedule | DCAT conformance | schedule + dispatch | 10–30 min | schema report |
| `prov-validate.yml` | schedule | PROV integrity | schedule + dispatch | 10–30 min | schema report |
| `perf.yml` | schedule | perf budgets | schedule + dispatch | 10–30 min | perf report |
| `model-regression.yml` | schedule | reproducibility (metrics drift) | schedule + dispatch | 10–45 min | metrics + artifacts |
| `publish-catalog.yml` | env-gated | atomic publish | `workflow_dispatch` | n/a | catalogs + PROV + digests |
| `docker.yml` | main/tag | images | `push main`, tags | ≤ 30 min | OCI images + digests |
| `release.yml` | tag | releases | tags | n/a | release assets |
| `sbom.yml` | tag/main | SBOM | tags + main | n/a | SPDX/CycloneDX |
| `attest.yml` | tag/main | attestations | tags + main | n/a | build provenance attestation |
| `agents-*.yml` | optional | governed PR automation | schedule/dispatch | ≤ 15 min | plans + PRs (no merge) |

---

<a id="change-aware-gate-matrix"></a>

## 🚦 Change-aware gate matrix

Make gates **path-aware** so PR checks stay fast and relevant (and align to v13 subsystem homes).[^mg13-structure]

| Change type | Examples | Required gates |
| --- | --- | --- |
| 🧠 Core code | `src/**` pipelines, parsing, core logic | `ci.yml` (+ CodeQL as configured) |
| 🧪 Pipelines | `src/pipelines/**` + pipeline configs | `ci.yml` + `catalog-qa.yml` + `schema-validate.yml` |
| 🗺️ Data/catalog | `data/**`, `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`, `schemas/**` | `catalog-qa.yml` + `schema-validate.yml` + `kfm-policy-gate.yml` |
| 🕸️ Graph/ontology | `src/graph/**`, ontology docs, entity ID registries | `graph-integrity.yml` + `ci.yml` (+ integration optional) |
| 🧩 API boundary | `src/server/**` *(and/or legacy `api/**`)* | `ci.yml` + `api-contract.yml` (+ integration optional) |
| 🌐 Web UI | `web/**` | `ui.yml` + `ci.yml` |
| 🎬 Story nodes | `docs/reports/story_nodes/**` | `markdown-protocol.yml` + `docs-linkcheck.yml` + `schema-validate.yml` + policy |
| 🔐 Workflows | `.github/workflows/**`, `.github/actions/**` | `actionlint.yml` + `kfm-policy-gate.yml` + human review |
| 📚 Docs-only | `docs/**` | `markdown-protocol.yml` + `docs-linkcheck.yml` (+ policy when governance applies) |

> [!CAUTION]
> Workflows are security-sensitive. Treat them like production code. 🔐

---

<a id="promotion-gates"></a>

## 🧱 Promotion gates

KFM uses an intentionally gate‑enforced lifecycle: **stage → validate → (optionally attest) → promote via PR → publish**.[^mg13-invariants]

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

KFM’s **Policy Pack** is explicitly used to validate:
* catalog completeness (STAC/DCAT)
* provenance completeness (PROV)
* sovereignty/classification propagation
* and other “fail closed” guardrails that block unsafe publishing.[^kfm-policy-pack][^kfm-arch-policy-gates]

### 🎯 What policy gates should enforce

**Governance / data integrity**

* license & attribution required for promoted datasets
* sensitive-location rules (generalize/omit/limit precision)
* provenance required (no “mystery layers”)
* catalog conventions (stable IDs, required fields, extension allow/deny lists)
* “classification propagation” (outputs inherit restrictions)[^mg13-invariants]

**Catalog safety**

* safe link rules (`links[].href` allow/deny lists; no unsafe schemes)
* metadata profile expectations for STAC/DCAT/PROV
* policy outcomes must be human-readable (“what failed” + “how to fix”)

**Supply chain safety**

* workflow permissions least‑privilege
* GitHub Actions pinning rules (prefer pinned versions; migrate toward SHA pinning)
* promotion jobs are kill‑switch protected

### ✅ Conftest workflow pattern (PR gate)

**When to run**

* PR touches `data/**`, `docs/**`, `schemas/**`, `.github/**`, `api/scripts/policy/**`

**How to run**

* no secrets
* `permissions: contents: read`
* short timeout
* upload report artifact on failure
* run Rego tests in CI (Conftest/OPA test)

Example command shapes:

```bash
# policy checks against repo content
conftest test \
  -p api/scripts/policy/rego \
  --all-namespaces \
  .

# policy unit tests (Rego tests)
conftest verify \
  -p api/scripts/policy/rego \
  api/scripts/policy/tests
```

> [!TIP]
> Keep policy rules “deny by default” and explain failures clearly (“what failed” + “how to fix”). 🧯

---

<a id="policy-pack--rule-ids--waivers"></a>

## 🧾 Policy Pack — rule IDs + waivers

KFM’s Policy Pack is designed to be **auditable** and **operationally practical** — which means:
* every rule has an ID
* exceptions are time‑bounded
* and waiver usage is visible in CI artifacts.[^kfm-policy-pack]

### 🏷️ Rule ID convention (examples)

> These are “shape examples” aligned to KFM’s described policy pack usage and should match how your policy README documents IDs.

* `KFM-CAT-*` → catalog requirements (STAC/DCAT)
* `KFM-PROV-*` → provenance requirements (PROV JSON‑LD)
* `KFM-SOV-*` → sovereignty/classification propagation
* `KFM-LINK-*` → link safety / URL allowlists
* `KFM-AI-*` → Focus Mode evidence/citation requirements
* `KFM-SC-*` → supply chain hardening rules (workflow perms, pinning)

### 🧾 Waivers

KFM’s policy pack supports a `waivers.yml` mechanism for **time-bound exceptions** (example: a partner dataset temporarily lacks a license field but is under active remediation). Waivers must include:
* the rule ID(s)
* a reason
* an owner
* an expiry date/time
* and (ideally) the mitigation plan.[^kfm-policy-pack]

**CI behavior (target posture):**
* expired waiver → **fail closed**
* waiver present → allowed **with loud artifacts** (`waiver-decisions.json`)
* waiver never bypasses “hard safety” rules (e.g., sensitive location leaks)

---

<a id="repo-provenance-lane"></a>

## 🧬 Repo provenance lane

KFM explicitly treats its own evolution as traceable: *you should be able to ask “which PR produced this dataset?”* and answer it with provenance records.[^kfm-devops-prov]

### ✅ What this lane should do

A `repo-provenance.yml` workflow (scheduled + on merge/tag) should emit:

* a **PROV JSON‑LD** record describing the CI run as an Activity
* the merged PR (and reviewers) as Agents/Activities
* digests of publish boundary artifacts (STAC/DCAT/PROV files)
* links to artifacts: SBOM, attestations, build-info.json

This makes KFM’s DevOps pipeline “first-class evidence” — aligned with the system’s broader provenance-first architecture.[^kfm-devops-prov][^mg13-invariants]

---

<a id="agent-automation-lane"></a>

## 🤖 Agent automation lane (optional) — Watcher · Planner · Executor

KFM supports optional agent automation only if it stays **governed**, **deterministic**, and **PR‑first**.[^kfm-wpe]

### ✅ Allowed agent behaviors

* 👀 **Watcher**: read‑only signals (facts/alerts), no side effects
* 🧠 **Planner**: deterministic planning (seeded, repeatable), no network by default
* 🧰 **Executor**: runs gates and opens/updates PRs **without merge permissions**[^kfm-wpe]

### 🧯 Kill-switch (non-negotiable)

Agents and promotion workflows must honor a central kill switch.

KFM docs describe a file-based “freeze” pattern for agents (e.g., a `.agent-freeze` flag), plus environment-level controls.[^kfm-policy-pack][^kfm-wpe]

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

KFM’s pipelines are expected to be deterministic and to emit standardized outputs under `data/processed/` along with catalog + provenance updates (STAC/DCAT/PROV).[^mg13-structure][^kfm-data-intake]

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

### 🧰 “Catalog QA” tool (mentioned in architecture)

KFM’s architecture documentation explicitly calls out specialized checks like a **Catalog QA** tool that scans metadata files for required fields/license info and can be invoked as part of CI.[^kfm-arch-cicd]

---

<a id="graph--semantics-gates"></a>

## 🕸️ Graph + semantics gates

KFM’s graph is the “semantic backbone” for Story Nodes and Focus Mode (and for AI assist that relies on governed graph context).[^kfm-ai-graph]

### ✅ Graph integrity gates should enforce

* stable entity IDs (no renaming without migration notes)
* relationship shape validation (allowed edge types)
* reference integrity (Story Node entity IDs exist)
* fixture build + constraints tests (unique IDs, required properties, etc.)[^mg13-ci-min]

### 🧠 Ontology-aware regression safety (practical)

KFM’s AI design references graph-driven context and ontologies commonly used for history + time modeling (e.g., CIDOC-CRM, OWL-Time).[^kfm-ai-graph]  
CI should protect:
* constraint migrations (`src/graph/migrations/**`)
* ontology docs (`docs/standards/**`)
* mapping scripts (STAC/DCAT → graph import)

---

<a id="story-nodes--focus-mode-gates"></a>

## 🎬 Story Nodes + Focus Mode gates

Story Nodes and Focus Mode are **trust-sensitive** because they look authoritative.[^mg13-invariants]

### ✅ Story Node lint should enforce (evidence-first)

From the v13 guide, Story Nodes must:[^mg13-story-focus]

* include provenance/citations for every claim
* reference graph entities via stable identifiers
* distinguish fact vs interpretation (especially with AI assistance)
* honor sensitivity rules (precision, sovereignty)
* only reference assets that exist and are licensed

### ✅ Focus Mode rules (hard gate)

Focus Mode has strict “trust rules” — CI should treat these as non‑negotiable invariants:[^mg13-focus-mode][^kfm-ui-focus]

* **only provenance‑linked content** is allowed to render
* **AI contributions must be opt‑in** and clearly labeled with uncertainty/confidence
* **no sensitive location leaks** — maps must generalize/omit sensitive points

### 🧾 Audit trail expectation (telemetry)

KFM’s architecture and UI guidance expect traceability and telemetry for key events (including redaction / trust‑critical UI actions).[^kfm-arch-observability][^kfm-ui-focus]

> [!TIP]
> Consider a small UI integration test that asserts: “sensitive layer rendered → redaction notice shown → telemetry event emitted”.

---

<a id="integration-tests"></a>

## 🧪 Integration tests

KFM’s spatial correctness depends on real PostGIS (and optionally a graph DB). Prefer containerized integration tests.

KFM also documents the **division of labor** at query time:
* Neo4j provides semantic context and dataset/entity linking
* PostGIS does the heavy spatial/aggregation work
* the API coordinates them (especially for Focus Mode flows).[^kfm-data-intake]

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

KFM’s UI is designed as a React-based web app with map-first interaction, plus optional 3D/globe support (MapLibre first; Cesium optional) and a strong emphasis on provenance surfaced in UI.[^mg13-pipeline][^kfm-ui-overview]

Recommended CI checks:

* ✅ `npm ci` (lockfile respected)
* ✅ lint (`eslint`) + format (`prettier`)
* ✅ typecheck (`tsc --noEmit`)
* ✅ tests (unit/component)
* ✅ build (`npm run build`) + size budgets (optional)

### 🧊 3D Web GIS realism check

KFM explicitly imagines 2D+3D map interfaces, timelines, and future simulation views in the UI.[^kfm-ui-overview]  
To keep CI practical:

* treat 3D assets (tilesets/models) as **untrusted inputs**
* validate/limit asset sizes (prevent “one model = one outage”)
* keep bundle size predictable (budgets catch bloat early)
* add a small E2E smoke test for map boot + layer toggles + citations visible

> [!NOTE]
> The project includes a reference portfolio covering WebGL / geospatial visualization and virtual world concepts; it’s useful context for future UI lanes and performance budgets.  [oai_citation:0‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

---

<a id="offline-packs--ar-gates"></a>

## 📦 Offline packs + AR gates

KFM’s UI roadmap includes:
* **Offline packs** for field/low-connectivity use
* **AR integration** (likely via a mobile app module using ARCore/ARKit).[^kfm-ui-offline-ar]

### ✅ CI should protect offline packs

Suggested gates (future):

* verify offline pack manifest schema (what’s included, versions, digests)
* validate licensing/attribution is preserved offline
* ensure redaction rules still apply when offline (no sensitive leaks)

### ✅ CI should protect AR content

Suggested gates (future):

* AR scene configs validate (geo anchors, time ranges, story references)
* asset budgets enforced (size, polygon counts, texture limits)
* “AR uses governed APIs” invariant: AR client is just another frontend (no bypass).[^kfm-ui-offline-ar][^mg13-invariants]

> [!TIP]
> Treat “offline pack build” and “AR assets validate” as **scheduled/manual lanes** at first, then promote to PR-required once stable.

---

<a id="modeling--simulation-gates"></a>

## 📈 Modeling + simulation gates (analysis discipline)

KFM treats model outputs as governed artifacts (not screenshots). That includes reproducibility, deterministic runs, and proper documentation.[^mg13-evidence-artifacts]

Recommended gates for published analysis:

* deterministic seeds + pinned inputs
* train/test split & leakage checks (where relevant)
* uncertainty reporting / sensitivity notes
* artifacts stored (plots, metrics, model cards)
* provenance linking inputs → transforms → outputs

> [!NOTE]
> The project’s simulation/methods reference material supports a “NASA-grade” modeling discipline mindset; CI should keep heavy checks scheduled and make PR smoke tests tiny.  [oai_citation:1‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

> [!NOTE]
> The AI reference portfolio (concepts + techniques) is included in the project library and can inform what “model-regression” checks look like over time.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

<a id="performance-gates"></a>

## ⚡ Performance gates (budgeted, scheduled)

Performance regressions are easier to prevent than to debug.

KFM’s documentation emphasizes responsive queries (PostGIS/Neo4j indexes + caching) and keeping expensive operations offline or scheduled.[^kfm-tech-perf][^kfm-ai-perf]

Recommended budgets:

* web bundle size ceilings
* API p95 latency budgets on a small fixture dataset
* expensive query guardrails (rate limits / timeouts / “explain analyze” thresholds)
* pipeline runtime budgets on representative fixtures

### 🧠 Graph query budgets (practical)

Focus Mode and graph-driven retrieval can create “multi-hop” query costs; keep a known set of Cypher queries and run them nightly on a fixture graph.[^kfm-ai-perf]

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

<a id="observability--telemetry"></a>

## 🔭 Observability & telemetry

KFM is designed to be instrumented:
* pipeline runs and major operations emit telemetry (timing, success/failure, volumes)
* runs have unique IDs + configuration hashes for replay and audit
* “Focus Telemetry” tracks AI/analytics behavior (latency, usage, etc.).[^kfm-arch-observability]

CI should support this by standardizing:
* `run_id`, `config_hash`, `inputs_digest`, `outputs_digest` in artifacts
* machine-readable `reports/gates.json` everywhere
* telemetry schema validation (if/when `schemas/telemetry/**` is introduced)

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
* `waiver-decisions.json` *(policy pack waiver outcomes)*
* `graph-integrity-report.json` *(constraints + fixture checks)*
* `api-contract-report.json` *(OpenAPI diff + contract tests)*
* `reports/gates.json` *(machine-readable gate results)*
* `prov.jsonld` *(W3C PROV; run lineage)*
* `devops-prov.jsonld` *(DevOps provenance ledger)*[^kfm-devops-prov]
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
├─ 📁 catalog-qa/                 # 🗃️ fast catalog QA + link safety
├─ 📁 policy-gate/                # ⚖️ policy pack execution wrapper + waiver logic
├─ 📁 graph-integrity/            # 🕸️ fixture ingest + constraint checks
├─ 📁 api-contract/               # 📜 OpenAPI diff + GraphQL schema check
├─ 📁 repo-provenance/            # 🧬 DevOps→PROV ledger emitter
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
          if [ -f api/requirements.txt ]; then pip install -r api/requirements.txt; fi

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
      - "data/stac/**"
      - "data/catalog/dcat/**"
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
            --stac data/stac \
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
<summary><strong>⚖️ <code>kfm-policy-gate.yml</code> — Policy Pack (Conftest/Rego + waivers)</strong></summary>

```yaml
name: KFM Policy Gate (Policy Pack)

on:
  pull_request:
    paths:
      - "data/**"
      - "docs/**"
      - "schemas/**"
      - ".github/**"
      - "api/scripts/policy/**"
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
            -p api/scripts/policy/rego \
            --all-namespaces \
            .

      - name: Evaluate waivers (shape)
        run: |
          python api/scripts/policy/evaluate_waivers.py \
            --waivers api/scripts/policy/waivers.yml \
            --out waiver-decisions.json

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: policy-gate-${{ github.sha }}
          path: |
            policy-report.txt
            waiver-decisions.json
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
          if [ -f api/requirements.txt ]; then pip install -r api/requirements.txt; fi

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

> [!NOTE]
> The project includes a polyglot programming reference bundle (useful for future multi-language linters and build lanes).  [oai_citation:3‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

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
* ✅ map/UI constraints (responsive + WebGL/3D realities)

</details>

<details>
<summary><strong>🧭 Canonical KFM specs used by this CI/CD README</strong></summary>

* **Master Guide v13 (draft):**  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
* **Data Intake guide (STAC/DCAT/PROV + Policy Pack):**  [oai_citation:5‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
* **System architecture (policy gates + CI/CD posture):**  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
* **AI system overview (Focus Mode + DevOps→PROV traceability):**  [oai_citation:7‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
* **UI system overview (provenance surfaced in UI + offline/AR roadmap):**  [oai_citation:8‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  

</details>

<details>
<summary><strong>📚 Project files that influence CI/CD (inventory)</strong></summary>

### 🧾 Core specs & blueprints (contracts + evidence)

* **Master Guide v13 (draft)** — structure, invariants, pipeline ordering:  [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
* **📚 Data Intake – Technical & Design Guide** — STAC/DCAT/PROV mechanics + Policy Pack usage:  [oai_citation:10‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
* **Comprehensive Architecture, Features, and Design** — CI/CD posture + stack + policy gates:  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
* **Comprehensive Technical Documentation** — QA/perf expectations + testing culture:  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
* **AI System Overview 🧭🤖** — Focus Mode + graph integration + DevOps provenance:  [oai_citation:13‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
* **Comprehensive UI System Overview** — provenance-first UI, 2D/3D/timeline/story/focus, offline/AR:  [oai_citation:14‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  

### 🌱 Roadmap & future proposals (informs future CI lanes)

* **🌟 Latest Ideas & Future Proposals** — W‑P‑E automation patterns & governance posture:  [oai_citation:15‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  
* **Innovative Concepts to Evolve KFM** — 4D digital twins, AR storytelling, crowdsourced verification:  [oai_citation:16‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  

### 🧰 Reference bundles (portfolios / multi-doc packs)

* **AI Concepts & more (portfolio)** — AI/ML concepts to inform modeling gates:  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
* **Maps / GoogleMaps / Virtual Worlds / WebGL (portfolio)** — geospatial + visualization context:  [oai_citation:18‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
* **Data Management / Theories / Bayesian / Data Science (portfolio)** — data + perf context:  [oai_citation:19‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  
* **Various programming languages & resources (portfolio)** — polyglot lint/build context:  [oai_citation:20‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  

### 🧾 Docs & methods discipline

* **Comprehensive Markdown Guide (best practices)** — informs markdown protocol expectations:  [oai_citation:21‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  
* **Scientific Modeling & Simulation (NASA-grade guide)** — informs reproducibility & V&V lanes:  [oai_citation:22‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

</details>

---

## 🧾 Evidence notes (citations)

[^mg13-pipeline]: Canonical pipeline ordering and stage boundaries (ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode).  [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
[^mg13-contract-first]: “Contract-first” posture + first-class schemas/contracts framing.  [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
[^mg13-invariants]: v13 invariants: ordering, API boundary, provenance-first, deterministic ETL, evidence-first narrative, classification propagation, enforceable gates.  [oai_citation:25‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
[^mg13-ci-min]: v13 minimum CI gates (front-matter, link validation, schema validation, graph integrity).  [oai_citation:26‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
[^mg13-story-focus]: Story Node requirements and Focus Mode positioning.  [oai_citation:27‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
[^mg13-focus-mode]: Focus Mode hard-gate rules: provenance-only, AI opt-in + labeled, no sensitive location leaks.  [oai_citation:28‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
[^mg13-structure]: v13 canonical catalog/prov paths (`data/stac/...`, `data/catalog/dcat/...`, `data/prov/...`) + “one canonical home per subsystem.”  [oai_citation:29‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
[^mg13-v13-history]: v13 draft date + blueprint references.  [oai_citation:30‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
[^mg13-evidence-artifacts]: Evidence artifact pattern (analysis/AI outputs treated as datasets with provenance).  [oai_citation:31‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  

[^kfm-policy-pack]: Policy Pack location (`api/scripts/policy/`), rules, waivers, and CI usage patterns.  [oai_citation:32‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
[^kfm-data-intake]: PostGIS+Neo4j query-time integration and STAC/DCAT/PROV backbone in intake workflows.  [oai_citation:33‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
[^kfm-ui-overview]: UI architecture: React-based, provenance surfaced, decoupled via APIs.  [oai_citation:34‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
[^kfm-ui-offline-ar]: Offline packs + AR integration concepts and constraints (mobile/ARCore/ARKit).  [oai_citation:35‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
[^kfm-ui-focus]: Focus Mode UI must show citations and differentiate AI output to preserve trust.  [oai_citation:36‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  

[^kfm-arch-governance]: Architecture emphasizes FAIR + CARE and governance.  [oai_citation:37‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
[^kfm-arch-policy-gates]: “Automated Policy Gates” (schema, STAC/DCAT/PROV, license, sensitivity, provenance) enforced in code and CI; fail-closed posture.  [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
[^kfm-arch-cicd]: Architecture notes CI workflows under `.github/workflows/` and specialized checks like Catalog QA invoked in CI.  [oai_citation:39‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
[^kfm-arch-observability]: Architecture describes observability, telemetry, run IDs, config hashes for audit/replay.  [oai_citation:40‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

[^kfm-tech-perf]: Technical documentation on performance expectations (indexes, caching, expensive ops offline) and CI reliability posture.  [oai_citation:41‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
[^kfm-ai-graph]: AI system overview: knowledge graph integration, ontology-driven context, RAG hybrid retrieval.  [oai_citation:42‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
[^kfm-ai-perf]: AI system overview: caching and performance strategies for responsive Q&A.  [oai_citation:43‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
[^kfm-devops-prov]: AI system overview describes DevOps transparency and linking datasets to code versions/PRs via provenance concepts.  [oai_citation:44‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
[^kfm-wpe]: W‑P‑E agent automation pattern and “never auto-merge” PR-first constraint.  [oai_citation:45‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:46‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  

<p align="right"><a href="#top">⬆️ Back to top</a></p>