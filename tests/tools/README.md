# 🧪🛠️ KFM Tests + Tools Hub (`tests/tools/`)

> **Goal:** keep Kansas Frontier Matrix (KFM) _provable_ — every dataset, map, story, and AI answer must be **traceable**, **reproducible**, and **governed** by automated checks (and humans when it matters).  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 📌 What lives here?

This folder documents (and often hosts) the **test suites** + **QA tooling** that power KFM’s “Detect → Validate → Promote” workflow.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### ✅ Tests (`tests/`)
Automated checks that prove code + pipelines behave correctly:
- **Unit tests** (small, fast, deterministic) — core functions, adapters, schema utilities
- **Integration tests** — PostGIS/Neo4j/API interplay, end-to-end pipeline stages
- **Data & contract tests** — metadata schemas, spatial sanity, provenance completeness

> KFM expects layered testing: unit + integration + end-to-end, backed by CI.  [oai_citation:2‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

### 🛠️ Tools (`tools/`)
Utilities that enforce **governance & data quality**:
- **Catalog QA**: scans catalog metadata for required fields, broken links, and basic data validity (e.g., geometries, ranges), and is wired into CI to fail PRs that would break trust.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Policy Pack (OPA + Conftest)**: Rego rules that “fail closed” during CI (and optionally at runtime), ensuring standards like **license required**, **sensitivity declared**, and **AI outputs cite sources**.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🧭 Why KFM is “test-heavy” (the philosophy)

KFM is built around a **provenance-first** and **metadata-first** system: pipelines are expected to be **reproducible/deterministic**, producing outputs plus catalog/provenance updates.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
The UI and AI are designed to avoid “pretty black boxes”: users can inspect layer provenance and sources.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

That only works if we constantly validate:
- **FAIR + CARE constraints** (especially for sensitive/cultural data)  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **Sensitivity labeling** (public vs sensitive/confidential) and correct handling  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **Evidence-backed AI** (governance check + citations before output)  [oai_citation:9‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🗂️ Recommended structure (convention)

> Your repo may differ — treat this as the **golden layout** we’re standardizing toward.

```text
tests/
  unit/                     # fast, isolated
  integration/              # DB/API/pipeline integration
  e2e/                      # full flows (optional; heavier)
  data_contracts/           # STAC/DCAT/PROV schema + invariants
  spatial/                  # CRS/geometry validity/range checks
  fixtures/                 # small canonical datasets + golden outputs
  snapshots/                # expected diffs/patches (esp. sims)

tools/
  validation/
    catalog_qa/             # catalog scanning + link/data checks  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
    policy/                 # OPA Rego policy pack (*.rego)  [oai_citation:11‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
    schema/                 # JSON Schema / SHACL helpers  [oai_citation:12‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
    spatial/                # CRS, bbox, geometry validators
  graph_health/             # Neo4j integrity checks (weekly suite)
  metrics/                  # QA trend metrics, summaries, dashboards
  scripts/                  # one-off “safe” helpers (no ad-hoc edits)
```

---

## 🧰 Core toolchain (what we validate)

### 1) 🧾 Catalog QA (metadata + integrity)
Catalog QA exists to keep the platform **auditable**:
- scans catalog JSON for required fields (license, spatial extent, etc.)
- checks for broken links/file references
- can run basic data checks (geometry validity, value ranges)
- **CI runs it automatically** and blocks merges on failure  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Why it matters:
- KFM’s catalog is the “source of truth” for what the API/UI can safely publish  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 2) ⚖️ Policy-as-code (OPA + Conftest)
KFM codifies governance rules in Rego under `tools/validation/policy/*.rego`.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
Examples include:
- “Every dataset must have a license.”
- “AI outputs must include at least one citation.”
- “No deprecated endpoints.”  [oai_citation:16‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

Design goals:
- **Fail-closed** by default: if required metadata is missing, the PR fails.  [oai_citation:17‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- Extend vocabularies/rules only via PR review (governance is explicit, not ad-hoc).  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### 3) 🧬 Data governance checks (sensitivity + ethics)
KFM includes sensitivity classification in metadata, with automated checks to ensure fields like **license** and **sensitivity** exist — and that sensitive data is handled properly.  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
Watcher/Planner/Executor agents are expected to refuse unsafe changes and prevent promotion without proof of redaction/approval.  [oai_citation:20‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### 4) 🗺️ Spatial correctness (CRS, geometry, bounds)
KFM’s CI includes spatial data quality checks (e.g., CRS validity, expected ranges).  [oai_citation:21‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
PostGIS is the “heavy lifting” store, so integration tests should verify:
- indices exist, queries behave, and tile/summarization endpoints remain stable  [oai_citation:22‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- data remains consistent with Neo4j IDs where applicable  [oai_citation:23‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 5) 🕸️ Graph integrity (Neo4j health checks)
KFM treats the living graph like code: run “unit-test-like” integrity suites to detect schema drift, orphaned metadata nodes, constraint failures, etc.  [oai_citation:24‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

> If you implement this, store timestamped reports under something like `docs/reports/qa/graph_health/` (so health history is auditable).

### 6) 🧪 Simulations & models: deterministic runners
For simulations and modeling, KFM favors a deterministic runner pattern (`kfm-sim-run`) that:
- fixes random seeds and uses a well-defined environment
- freezes time (“virtual clock”) where needed
- emits **diff/patch** output vs previous runs for review  [oai_citation:25‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

This unlocks “reviewable science” (PRs show how results changed, not just that they changed).

### 7) 🔐 Supply chain integrity (artifacts)
KFM ideas include treating **data artifacts like packages**:
- store artifacts in OCI registries, fetch by immutable digest
- verify origin/integrity with Cosign signatures  [oai_citation:26‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- enforce via policy gates (“no unsigned artifacts”)  [oai_citation:27‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🚦CI workflow (Detect → Validate → Promote)

KFM’s CI aims to:
1. **Detect**: what changed (code? catalog? data?)
2. **Validate**: run tests + policy gates + schema/spatial checks
3. **Promote**: merge/deploy only if everything passes  [oai_citation:28‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### Suggested CI stages (minimal but strong)
- ✅ Unit tests (fast)
- ✅ Catalog QA (metadata + integrity)  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- ✅ Policy pack (OPA + Conftest)  [oai_citation:30‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- ✅ Schema checks for STAC/DCAT/PROV (treat metadata as code)  [oai_citation:31‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- ✅ Spatial checks (CRS/geometries/ranges)  [oai_citation:32‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- ✅ Integration tests (PostGIS + Neo4j + API)  [oai_citation:33‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- ✅ (Optional) Graph health suite  [oai_citation:34‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- ✅ (Optional) Simulation diffs (`kfm-sim-run`)  [oai_citation:35‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🏃 Running checks locally (typical patterns)

> Exact commands depend on your repo wiring; these are common, safe patterns.

### 🐍 Python tests
```bash
pytest -q
```

### 📦 Policy pack (Conftest against a folder)
```bash
conftest test -p tools/validation/policy path/to/changed/files
```

### 🧾 Catalog QA
```bash
# Run the Catalog QA tool located under tools/validation/ (see that tool’s README in-repo)
# Goal: confirm required metadata fields + link integrity + basic data checks
```

### 🧪 Simulation reproducibility (runner pattern)
```bash
# Run simulation with fixed seed + frozen time; compare diff/patch artifacts vs last run
```

---

## 🧩 Adding a new check (rules of the road)

### ✅ Add a test when…
- you’re validating **behavior** (function output, adapter mapping, API response)
- you want confidence that refactors won’t change results

### ✅ Add a Catalog QA rule when…
- you’re validating **metadata completeness**, link integrity, or “data sanity” constraints  
  (licenses, extents, required fields, value ranges)  [oai_citation:36‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### ✅ Add a Policy Pack (Rego) rule when…
- you want a **non-negotiable governance gate** (fail closed)  
  e.g., “no dataset without license”, “AI must cite sources”, “sensitivity required”  [oai_citation:37‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### ✅ Add a graph health check when…
- a failure would create **silent corruption** (orphans, broken lineage, constraint/index issues)  [oai_citation:39‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧠 AI-specific QA (Focus Mode & narratives)

Focus Mode’s pipeline explicitly includes:
- parse question → retrieve evidence → generate answer → **governance check** → deliver with citations  [oai_citation:40‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
And policy gates can require: “AI outputs must include citations” (otherwise refuse).  [oai_citation:41‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

Recommended AI QA checks:
- ✅ “All non-trivial claims have a dataset/document citation”
- ✅ “Answer is blocked if retrieval returns no evidence”
- ✅ “Sensitive datasets are redacted/role-gated”  [oai_citation:42‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🔎 Design references (project docs)

These docs define the intent behind the test + tools system:

- 📘 **Comprehensive Technical Documentation** (Catalog QA, deterministic pipelines, tool roles)  [oai_citation:43‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- 📥 **Data Intake – Technical & Design Guide** (STAC/DCAT/PROV validation, PostGIS+Neo4j integration)  [oai_citation:44‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:45‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- 🤖 **AI System Overview** (Policy pack, Detect→Validate→Promote CI, evidence-backed AI)  [oai_citation:46‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:47‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- 🧭 **Architecture / Features / Design** (automated policy gates, required metadata, citations, sensitivity checks)  [oai_citation:48‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- 🧷 **UI System Overview** (front-end transparency + provenance-first UI principles)  [oai_citation:49‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- 🧪 **Scientific Method / Master Coder Protocol** (test tiers + CI expectations)  [oai_citation:50‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- 🧱 **Future Proposals / Ideas** (supply chain attestations, governance automation)  [oai_citation:51‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  
- 🌱 **Innovative Concepts** (future-facing surfaces that will need QA: AR, storytelling co-pilots, explainability)  [oai_citation:52‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- 🧵 **Pulse / Refinement Ideas** (graph health checks, provenance-first artifact storage, narrative automation)  [oai_citation:53‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- 📚 **Data Intake Guide (full)** (end-to-end intake + QA patterns)  [oai_citation:54‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

---

## ✅ Quick checklist (PR author)

Before you open a PR that touches **data**, **catalog**, **pipelines**, **AI**, or **graph**:

- [ ] Ran unit tests (or added new ones)  [oai_citation:55‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- [ ] Ran Catalog QA on changed metadata/data  [oai_citation:56‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- [ ] Passed policy gates (license + sensitivity + citations where applicable)  [oai_citation:57‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- [ ] For sims/models: produced reproducible output + diff/patch artifacts  [oai_citation:58‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- [ ] For AI changes: verified evidence-backed outputs + governance check path  [oai_citation:59‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- [ ] If graph schema/import touched: ran graph health checks  [oai_citation:60‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

---

### 🧡 Final note
KFM is a “living atlas,” but it’s only valuable if it stays **trustworthy**. The mission of `tests/` + `tools/` is to make correctness the default and governance enforceable — so the platform can scale without becoming a black box.  [oai_citation:61‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
