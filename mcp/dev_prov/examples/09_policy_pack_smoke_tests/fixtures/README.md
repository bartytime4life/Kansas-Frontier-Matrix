# ❌ Policy Pack Smoke Test Fixtures — FAIL

![OPA](https://img.shields.io/badge/OPA-Rego%20Policies-blue) ![Conftest](https://img.shields.io/badge/Conftest-Policy%20Testing-informational) ![Smoke Tests](https://img.shields.io/badge/Smoke-Tests-success) ![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governance-orange) ![PROV](https://img.shields.io/badge/W3C-PROV--O-purple) ![STAC](https://img.shields.io/badge/STAC-Catalog-brightgreen) ![DCAT](https://img.shields.io/badge/DCAT-Metadata-yellowgreen)

> 🚨 **Intentionally broken on purpose.**  
> If anything in this folder starts passing, our policy gates are lying to us.

⬅️ Back to: [`09_policy_pack_smoke_tests`](../../README.md)  
✅ Looking for “good” examples? See: [`../pass/`](../pass/)

---

## 🎯 What this folder is

This directory contains **negative fixtures** used by the **Policy Pack Smoke Tests**.

- Each fixture is a **minimal, targeted reproduction** of a governance violation.
- The smoke test harness should run the **OPA (Rego) Policy Pack** (via Conftest or an equivalent runner) against these fixtures.
- Every fixture here **must produce at least one `deny`** outcome.

### ✅ Success criteria (for this folder)
- **FAIL fixtures** ⇒ must **fail** policy evaluation (deny).
- If a fixture passes, it’s not “fixed” — it’s **broken** (either the policy regressed or the fixture no longer represents the violation).

---

## 🧠 Why FAIL fixtures exist (KFM governance recap)

KFM’s governance model is **evidence-first** and **policy-enforced**. This folder exists to keep those guarantees real, not aspirational:

- **Policy-as-Code**: rules live in the repo and are executed in CI (and sometimes at runtime).
- **Fail-closed**: missing lineage / missing metadata / missing approvals should **block merge**.
- **Evidence triplet** (DCAT + STAC + PROV): publishing without the metadata + provenance backbone is not allowed.
- **No “mystery nodes”**: nothing enters the knowledge graph without traceable catalog/provenance references.
- **UI ↔ API boundaries**: the UI must not bypass governance by querying databases directly.
- **AI needs citations**: Focus Mode / AI outputs must carry provenance/citation context, or refuse.

Smoke tests are the “tripwire” that ensures these non‑negotiables stay enforced across refactors, new policies, and new contributors. 🧯

---

## 📁 Fixture conventions (recommended)

> Your harness may already define a structure — follow that first.  
> If you’re adding new fixtures, this is the suggested pattern.

```
📁 fixtures/
  ✅ pass/
  ❌ fail/
    📁 01_<policy_or_theme>_<short_slug>/
      📄 README.md                 # what is violated + why
      📄 input.*                   # the artifact(s) under test (json/yaml/md/etc)
      📄 expected_denies.*         # optional: stable deny IDs asserted by tests
```

### 🧩 Naming guidelines
- Start with a sortable prefix: `01_`, `02_`, `03_`…
- Include the **policy ID** *or* a governance theme:
  - `KFM-CAT-*` catalog/metadata
  - `KFM-PROV-*` provenance
  - `KFM-SEC-*` security/secrets
  - `KFM-STORY-*` narratives/evidence
  - `KFM-API-*` boundary rules
- Keep fixture slugs short and readable: `missing_license`, `no_prov_chain`, `downgrade_classification`, etc.

---

## 🧪 What kinds of failures belong here

Below is the **intent** of the FAIL suite. Your actual deny IDs / rule names may differ — but the themes are stable.

| 🧭 Governance Theme | 💥 Example violation (fixture should model) | ✅ What the policy gate is protecting |
|---|---|---|
| 📚 Catalog completeness (DCAT/STAC) | dataset missing required fields (e.g., license/contact/title) | FAIR compliance + discoverability + reuse rights |
| ⛓ Provenance integrity (PROV-O) | processed asset has no PROV, or PROV missing `used/generatedBy` links | chain-of-custody + auditability |
| 🧾 Evidence-first narratives | story text cites sources but no structured manifest / unresolved refs | “research‑paper discipline” + reviewability |
| ⚖ Sensitivity & sovereignty | sensitive layer lacks classification tag / uses restricted coords without obfuscation | CARE + community authority + harm reduction |
| 🚧 Pipeline order invariants | “processed” data introduced without raw → catalog → prov steps | reproducibility + trustworthy transformation |
| 🔌 UI/API boundary | UI config points to DB directly / bypasses authz gate | policy enforcement consistency + security |
| 🤖 AI governance | AI output metadata lacks citations / provenance summary | explainability + trust |
| 🔐 Secrets & supply-chain hygiene | secret-like token committed (even in test data) | protect infra + prevent leaks |
| ♻️ Determinism & reproducibility | pipeline manifest lacks checksums/pins; floating versions | rebuildability + consistent outputs |
| 🧬 Dev provenance | PR/merge provenance record missing required entities/agents | “code history as provenance” + traceable builds |
| 🕸 Graph integrity checks | ingestion would create orphan nodes / violates constraints | knowledge graph health + query correctness |

---

## ✅ Expectations for the smoke test harness

A robust smoke test runner should, at minimum:

- Assert **FAIL fixtures produce `deny`** (fail-closed).
- Prefer asserting on **stable rule IDs** (e.g., `KFM-PROV-001`) rather than brittle message strings.
- Support **multiple denies** per fixture (but keep fixtures targeted to one primary violation).
- Reject attempts to “paper over” failures via waivers here:
  - ❌ FAIL fixtures should not include waiver files
  - ❌ FAIL fixtures should not depend on environment-specific toggles

> Tip: If your policy pack supports waivers with expirations, keep those exclusively in real workflows — not in smoke tests. 🧪

---

## ➕ Adding a new FAIL fixture

1. **Pick one policy** (or one governance invariant) you want a tripwire for.
2. Create a new folder under `fixtures/fail/`.
3. Add the smallest possible artifact that triggers the deny (avoid giant datasets).
4. Run the policy runner locally and capture the deny output.
5. Record expected deny IDs in `expected_denies.*` (if your harness supports it).
6. Add a short `README.md` in the fixture folder:
   - what you’re violating
   - why it matters
   - which deny IDs are expected

### 🧰 Minimal fixture README template
```md
# ❌ <short title>

## Violates
- <policy id(s)>

## Why it matters
- <one sentence>

## Expected denies
- <deny id(s)>
```

---

## 🧯 Safety & hygiene rules (don’t create new problems)

- **Never** include real secrets. If a fixture needs to trigger secret scanners, use **obviously fake** tokens and/or patterns designed for testing.
- Don’t include real sensitive site coordinates, private landowner info, or restricted material.
- Prefer synthetic geometries and placeholder metadata.
- Keep fixtures deterministic: no timestamps, random IDs, or “latest” URLs unless the policy is explicitly about freshness rules.

---

## 🔗 Design references used for these FAIL scenarios

This folder’s failure themes are grounded in the KFM design + reference libraries:

### 🧱 Core KFM architecture & governance docs
- **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design** — policy packs, FAIR/CARE, automated policy gates, provenance-first enforcement
- **📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide** — pipeline order invariants, evidence triplet (DCAT/STAC/PROV), API boundary rules, fail-closed CI concepts
- **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖** — citation-linked AI retrieval, governance ledger, bias/drift monitoring expectations
- **Kansas Frontier Matrix – Comprehensive UI System Overview** — UI/API decoupling, provenance surfaced in UI, Focus Mode explainability patterns
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** — implementation realities: CI/CD, scaling, observability, APIs, data services
- **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals** — devops↔provenance integration (PR→PROV), CI invariants, rollback/kill-switch concepts
- **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)** — cultural protocols, sovereignty, sensitivity-aware access models
- **Additional Project Ideas** — evidence manifests for stories, graph health checks as routine “unit tests” for the KG

### 📦 Reference portfolios (embedded libraries that inform policy themes)
- **AI Concepts & more (portfolio)** — AI governance, human-centered AI framing, and broader AI reference material
- **Maps / GoogleMaps / Virtual Worlds / Archaeological / Geospatial / WebGL (portfolio)** — geospatial pipelines, projections, WebGL map visualization references that justify strict metadata/projection rules
- **Data Management / Architectures / Data Science / Bayesian Methods (portfolio)** — reproducibility, CI/CD rigor, data quality, and scalable data system practices
- **Various programming languages & resources 1 (portfolio)** — coding hygiene, tooling familiarity, and implementation references across the stack

---

## 🧭 One last reminder

> ✅ **PASS** fixtures are for “golden paths.”  
> ❌ **FAIL** fixtures are for “tripwires.”  
> We need both — otherwise governance is just vibes. 🧱✨

