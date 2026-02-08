<div align="center">

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="../docs/assets/branding/kfm-seal-320.png">
  <img src="../docs/assets/branding/kfm-seal-animated-320.gif" width="220" alt="Kansas Frontier Matrix (KFM) — seal (animated)" />
</picture>

# 🧰 `.github` — Governance-as-Code, Community Health & Automation for **Kansas Frontier Matrix (KFM)** 🚧

<br/>

<!-- Status / Safety -->
<img alt="Status: Under Construction" src="https://img.shields.io/badge/status-under_construction-orange?style=for-the-badge&logo=github">
<img alt="Governance: Evidence-First" src="https://img.shields.io/badge/governance-evidence--first-0b7285?style=for-the-badge">
<img alt="Policy: Fail-Closed" src="https://img.shields.io/badge/policy-fail--closed-8a2be2?style=for-the-badge">
<img alt="Aligned: Master Guide v13.0.0" src="https://img.shields.io/badge/aligned-master_guide_v13.0.0-1f6feb?style=for-the-badge">
<br/>
<img alt="Metadata: STAC/DCAT/PROV" src="https://img.shields.io/badge/metadata-STAC%2FDCAT%2FPROV-005bbb?style=for-the-badge">
<img alt="Policy Engine: OPA/Conftest" src="https://img.shields.io/badge/policy_engine-OPA%2FConftest-6f42c1?style=for-the-badge">

<br/>

<!-- Repo badges -->
<img alt="License" src="https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix?style=for-the-badge">
<img alt="Last Commit" src="https://img.shields.io/github/last-commit/bartytime4life/Kansas-Frontier-Matrix?style=for-the-badge">
<img alt="Repo Size" src="https://img.shields.io/github/repo-size/bartytime4life/Kansas-Frontier-Matrix?style=for-the-badge">
<img alt="Issues" src="https://img.shields.io/github/issues/bartytime4life/Kansas-Frontier-Matrix?style=for-the-badge">

</div>

> 🧭 **Start here:** this folder is where we codify *how we collaborate* and *what must be true before anything ships*.  
> ✅ Templates + ✅ CI/CD + ✅ Policy gates = **governed contributions** (no “trust me” merges).

---

## 🧱 Alignment: KFM v13 — “One Canonical Home per Subsystem” 📍

KFM v13 enforces a **single canonical home** for each subsystem (data, catalogs, provenance, schemas, contracts, story content, CI).  
**`.github/` does not define truth — it enforces truth** by running checks against the v13 “truth anchors”:

- 📚 **Master Guide & structure rules:** `docs/MASTER_GUIDE_v13.md`, `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md`
- 📐 **Schemas:** `schemas/` (STAC/DCAT/PROV + Story Nodes + UI + telemetry)
- ⚖️ **Governance:** `docs/governance/` (ethics, sovereignty, review gates)
- 🧾 **Catalog outputs (governed):**
  - STAC: `data/stac/collections/`, `data/stac/items/`
  - DCAT: `data/catalog/dcat/`
  - PROV: `data/prov/`
  - Graph exports: `data/graph/csv/`, `data/graph/cypher/`
- 🧩 **Pipelines:** `src/pipelines/` (ETL)
- 🕸️ **Graph build:** `src/graph/` (Neo4j build/import tooling)
- 🌐 **API boundary:** `src/server/` (contracted interfaces; “trust membrane”)
- 🗺️ **UI:** `web/` (React + map UI)
- 📚 **Story Nodes (governed narratives):** `docs/reports/story_nodes/` (`templates/`, `draft/`, `published/`)

> 🔥 **Rule of thumb:** if a folder is “truth,” `.github/` should *validate it*, not *duplicate it*.

---

## 🔗 Quick Links (Repo Truth Anchors)

- ⬅️ **Project Overview:** [`../README.md`](../README.md)
- 🧭 **Master Guide v13:** [`../docs/MASTER_GUIDE_v13.md`](../docs/MASTER_GUIDE_v13.md)
- 🧱 **Repo structure standard:** [`../docs/standards/KFM_REPO_STRUCTURE_STANDARD.md`](../docs/standards/KFM_REPO_STRUCTURE_STANDARD.md)
- 🏗️ **Architecture (blueprints + ADRs):** [`../docs/architecture/`](../docs/architecture/)
- 📜 **Standards (profiles + work protocol):** [`../docs/standards/`](../docs/standards/)
- ⚖️ **Governance (ethics + sovereignty + review gates):** [`../docs/governance/`](../docs/governance/)
- 🧰 **Templates (universal doc + story node + contracts):** [`../docs/templates/`](../docs/templates/)
- 📚 **Story Nodes:** [`../docs/reports/story_nodes/`](../docs/reports/story_nodes/)
- 📐 **Schemas:** [`../schemas/`](../schemas/)
- ⚖️ **OPA Policy Pack:** [`../policy/`](../policy/)
- 🧪 **Tests:** [`../tests/`](../tests/)
- 🔧 **Tools & Validators:** [`../tools/`](../tools/)
- 🗂️ **STAC:** [`../data/stac/`](../data/stac/)
- 🌐 **DCAT:** [`../data/catalog/dcat/`](../data/catalog/dcat/)
- 🧾 **PROV:** [`../data/prov/`](../data/prov/)
- 🕸️ **Graph exports (imports + cypher):** [`../data/graph/`](../data/graph/)
- 🔐 **Security Policy:** [`../SECURITY.md`](../SECURITY.md) *(or `.github/SECURITY.md` if used)*

---

## 🚧 Under Construction

This `.github/` directory is being assembled into **Governance-as-Code**. Expect churn while we lock:

- ✅ contribution templates that **ask for evidence**
- ✅ workflows that validate **catalogs + provenance + schemas**
- ✅ policy checks that **fail closed** (no silent bypasses)
- ✅ security automation (scanning + SBOM) 🔐

> Treat changes here like production infrastructure.  
> A tiny YAML change can unblock—or break—every PR.

### ✅ Roadmap Checklist (Governed Contributions)

- [x] Baseline `.github/README.md` aligned to v13 structure 📘  
- [ ] `PULL_REQUEST_TEMPLATE.md` with governance gates ✅  
- [ ] Issue Forms (`ISSUE_TEMPLATE/*.yml`) for ingest / map / contract / story node / bug 🧾  
- [ ] `CODEOWNERS` rules for “high blast radius” areas 👀  
- [ ] `dependabot.yml` for dependency hygiene 🔄  
- [ ] CI workflows (lint/test/build) ⚙️  
- [ ] Repo structure guardrail (v13 path checks; no duplicate “truth” folders) 🧱  
- [ ] Contract + schema validation (OpenAPI / JSON Schema / GraphQL SDL) 📜  
- [ ] Catalog validation (**STAC / DCAT**) 🗂️  
- [ ] Provenance validation (**PROV / JSON‑LD**) 🧾  
- [ ] Security scanning (CodeQL / secret scanning / SBOM) 🔐  
- [ ] Policy-as-code gates (OPA + Conftest) ⚖️  
- [ ] Release gating (signed manifests + reproducible bundles) 📦  

---

## 📁 What Lives in `.github/` (and why it matters)

This directory holds GitHub-native **community health + automation**. In v13 terms: **it enforces the repo’s truth contracts**.

```text
.github/
├─ README.md                     📘 This document
├─ workflows/                    ⚙️ GitHub Actions (CI/CD + governance checks)
├─ actions/                      🧩 Composite actions shared across workflows (optional)
├─ ISSUE_TEMPLATE/               🧾 Issue forms & templates
├─ PULL_REQUEST_TEMPLATE.md      ✅ PR checklist + governance gates
├─ CODEOWNERS                    👀 Review ownership rules
├─ dependabot.yml                🔄 Automated dependency updates
├─ SECURITY.md                   🔐 Security policy (optional, GitHub-recognized)
└─ FUNDING.yml                   💖 Sponsorship links (optional)
```

### 🖼️ Assets: Where visuals should live
- ✅ **Global branding** (used across docs + UI): `docs/assets/branding/`  
- ✅ **Community-only visuals** (used only in `.github/*` docs): `.github/assets/` *(optional)*  
- ✅ Keep assets small + optimized (mobile-friendly) 📱

---

## 🧭 KFM “Truth Path” (Why GitHub Automation Matters)

KFM is built around a non‑negotiable ordering of evidence → governed artifacts → user experiences:

```mermaid
flowchart LR
  raw["Raw 📥 data/{domain}/raw"] --> work["Work 🧪 data/{domain}/work"]
  work --> proc["Processed ✅ data/{domain}/processed"]

  proc --> catalogs["Catalogs 🗂️ STAC + DCAT + PROV — data/stac • data/catalog/dcat • data/prov"]
  catalogs --> kg["Graph refs 🕸️ Neo4j (refs, not payloads)"]
  kg --> api["API boundary 🌐 src/server"]

  api --> ui["UI 🗺️ web/"]
  ui --> story["Story Nodes 📚 docs/reports/story_nodes"]
  story --> focus["Focus Mode 🎯"]
```

### ✅ Non‑Negotiables enforced via `.github/` gates

- 🧾 **Provenance-first**: no publishable output without **STAC + DCAT + PROV** alignment.
- 🛑 **Fail‑closed by default**: missing requirements block merges.
- 🔒 **Classification propagation**: outputs can’t be less restricted than inputs.
- ♻️ **Deterministic pipelines**: idempotent, config‑driven, logged, re‑runnable.
- 🧱 **API boundary**: UI/AI does **not** query PostGIS/Neo4j directly.
- 🧠 **Focus Mode constraints**: AI outputs must be traceable to cataloged evidence and governed citations.

---

## ⚖️ Governance Gates (What Workflows Must Prove)

Workflows should validate *claims* **and** *shape*.

### 🗂️ Metadata + Catalog Gates
- STAC JSON validates against `schemas/stac/` and the project STAC profile (`docs/standards/KFM_STAC_PROFILE.md`)
- DCAT JSON‑LD validates against `schemas/dcat/` and the DCAT profile (`docs/standards/KFM_DCAT_PROFILE.md`)
- PROV bundles validate against `schemas/prov/` and the PROV profile (`docs/standards/KFM_PROV_PROFILE.md`)

### 📐 Contract + Schema Gates
- Any change to API/UI contracts must validate against versioned schemas:
  - `schemas/storynodes/` (Story Node format + fields)
  - `schemas/ui/` (UI config, layer specs)
  - `schemas/telemetry/` (if/when telemetry is used)
  - API specs and extensions (OpenAPI / GraphQL SDL / JSON Schema)

### 🧾 Provenance + Audit Gates
- PROV must link raw inputs → processes → outputs
- Checksums/manifests (where used) must match referenced assets
- Policy decisions should be traceable to a **policy bundle hash/version** (auditability)

### 🔐 Security Gates
- CodeQL + dependency scanning (and optional SBOM generation)
- Secret scanning (fail on leaked credentials)
- Dependency hygiene (Dependabot + pinned actions)

> 💡 Recommended GitHub Actions hygiene:
> - pin third-party actions by SHA
> - default workflow permissions to read-only
> - keep secrets in environments with protection rules

---

## 🧪 Local “Run It Like CI” (Developer Workflow)

CI should never surprise you. Typical local checks:

```bash
# Policy gates (OPA/Conftest)
conftest test policy/

# Schema + catalog validation (project-specific; typically lives in tools/)
# tools/validate_schemas.sh
# tools/validate_catalogs.sh

# Backend tests (if using docker-compose dev stack)
docker-compose exec api pytest

# Frontend tests (depending on tooling)
npm test
# or: pnpm test
```

> Prefer “thin workflows”: keep logic in `tools/` scripts and call them from Actions.  
> Workflows should orchestrate, not become a second codebase.

---

## 🧾 Issues: The “Front Door” for Work

Work should start as an issue when it touches:

- 📥 new dataset ingest / cataloging
- 🗺 map layer additions or styling changes
- 🧠 Focus Mode / AI behavior changes
- 📐 contract / schema changes
- ⚖️ policy pack / governance rules
- 🔥 anything with high blast radius

### 🧷 Issue Writing Rules (Keeps us fast)
- ✅ one problem per issue
- 🧩 include context + expected outcome
- 🧾 include evidence links (datasets, docs, screenshots)
- 🏷️ add labels to route review

---

## ✅ Pull Requests: What “Good” Looks Like

### 🏷️ PR Title Style
Use a clear prefix + short summary:

- `feat(api): add dataset search filter for bbox + time`
- `fix(pipeline): make ingest idempotent for ks_hydrology_1880`
- `docs(governance): clarify classification propagation rules`
- `data(catalog): register new STAC collection + DCAT dataset`
- `policy(opa): tighten citation enforcement for focus-mode`

### 📦 Minimum PR Payload
Your PR should include:
- **What changed** and **why**
- **Proof** (tests, screenshots, sample outputs, validation logs)
- **Risk notes** (breaking changes, migrations, data backfills)
- **Docs updates** when behavior/contracts change

> If it changes a **contract** (schema/API/UI config), it must include:  
> ✅ version bump, ✅ validator updates, ✅ migration notes (if needed)

---

## 👀 CODEOWNERS: “High Blast Radius” Review Routing

CODEOWNERS should require additional review for:

- `policy/**` ⚖️ (OPA policy pack)
- `schemas/**` 📐 (schema changes ripple everywhere)
- `.github/workflows/**` ⚙️ (governance enforcement)
- `src/pipelines/**` ♻️ (ETL and transforms)
- `src/graph/**` 🕸️ (ontology bindings + graph build)
- `src/server/**` 🌐 (API boundary / auth / contracts)
- `web/**` 🗺️ (UI map experience)
- `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`, `data/graph/**` 🗂️🧾🕸️ (catalog + lineage + graph exports)
- `docs/governance/**` ⚖️ (ethics/sovereignty/review gates)
- `docs/reports/story_nodes/**` 📚 (narratives; publication gates)
- `releases/**` 📦 (shipping artifacts, manifests, SBOM)

---

## 🏷️ Labels Taxonomy (Recommended)

<details>
<summary><b>Click to expand label guide</b> 🏷️</summary>

### Type
- `type:bug` 🐛
- `type:feature` ✨
- `type:docs` 📚
- `type:data` 🧱
- `type:security` 🔐
- `type:policy` ⚖️
- `type:schema` 📐
- `type:release` 📦
- `type:chore` 🧹

### Area
- `area:api` ⚙️
- `area:web` 🗺️
- `area:pipelines` ♻️
- `area:catalog` 🗂️
- `area:provenance` 🧾
- `area:graph` 🕸️
- `area:governance` ⚖️
- `area:ai` 🎯
- `area:data-sovereignty` 🪶 *(CARE-aligned work)*

### Priority / Status
- `priority:p0` 🔥 / `priority:p1` ⚡ / `priority:p2` 🧊
- `status:blocked` ⛔ / `status:needs-review` 👀 / `status:ready` ✅

</details>

---

## 🔐 Secrets & Sensitive Data

- 🚫 never commit secrets (API keys, tokens, private URLs, credentials)
- ✅ use `.env.example` as the only commit-safe env reference
- ✅ store secrets in GitHub Secrets / environment protection rules
- 🧯 if you accidentally commit a secret:
  1) rotate it immediately  
  2) open a security issue (or private report)  
  3) scrub history if required  

---

## 🧠 Focus Mode & AI Governance

When AI/Focus Mode is involved:
- ✅ AI output must be traceable to cataloged sources (dataset IDs / document refs)
- ✅ citation enforcement is **policy-backed** (fail if missing)
- ✅ restricted inputs remain restricted in derived outputs (classification propagation)
- ✅ AI answers should be logged as audit artifacts (question + sources + model + policy decision)

---

## 🪶 Data Ethics & Indigenous Data Sovereignty (When Applicable)

KFM includes Indigenous history and land-related materials. When work touches Indigenous data:

- ✅ prefer community-backed context over deficit framing
- ✅ document permissions/terms clearly (licenses + access boundaries)
- ✅ treat “open” ≠ “unrestricted” (governance still applies)
- ✅ label and route review via `area:data-sovereignty` 🪶
- ✅ when applicable, align handling + stewardship with **CARE Principles** alongside FAIR

> Goal: **fast collaboration without sacrificing trust.**  
> If it can’t be traced, validated, and reproduced… it doesn’t merge. ✅
