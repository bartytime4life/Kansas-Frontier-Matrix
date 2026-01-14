# 🧰 `tools/_lib` — Shared Tooling Library (KFM Core Utilities)

<div align="left">

![Scope](https://img.shields.io/badge/scope-tools%2F__lib-0ea5e9)
![Internal](https://img.shields.io/badge/package-internal%20only-111827)
![Fail-Closed](https://img.shields.io/badge/posture-fail--closed-red)
![Provenance](https://img.shields.io/badge/metadata-STAC%20%2B%20DCAT%20%2B%20PROV-7c3aed)
![Policy as Code](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-111827)
![Integrity](https://img.shields.io/badge/integrity-checksums%20%2B%20manifests-purple)
![No Secrets](https://img.shields.io/badge/security-no%20secrets%20in%20repo-critical)

</div>

**`tools/_lib/` is the “boring on purpose” toolbox** used by KFM scripts, validators, CI gates, and promotion lanes.  
It exists to prevent copy/paste utilities, enforce KFM invariants, and make **Detect → Validate → Promote** repeatable. ✅

> [!IMPORTANT]
> This folder is **security-critical**. It touches:
> - catalog/provenance boundaries (STAC/DCAT/PROV) 🧾🧬  
> - validation and governance gates ✅  
> - integrity, checksums, manifests 🔏  
> - sensitive-location handling 🗺️  
> Treat changes as *production-impacting*.

---

## 📌 Table of contents

- [⚡ Quickstart](#-quickstart)
- [🎯 What belongs in `_lib`](#-what-belongs-in-_lib)
- [🧱 KFM invariants this library must enforce](#-kfm-invariants-this-library-must-enforce)
- [🗂️ Expected layout](#️-expected-layout)
- [🧩 Core capability areas](#-core-capability-areas)
- [🧪 CI + gates integration](#-ci--gates-integration)
- [🤖 Automation patterns](#-automation-patterns)
- [🔐 Governance + sensitive locations](#-governance--sensitive-locations)
- [📈 Performance + scalability notes](#-performance--scalability-notes)
- [🧠 Modeling, statistics, and “NASA-grade” discipline](#-modeling-statistics-and-nasa-grade-discipline)
- [🧯 Secure coding rules for `_lib`](#-secure-coding-rules-for-_lib)
- [🧑‍💻 Contributing checklist](#-contributing-checklist)
- [📚 Reference shelf](#-reference-shelf)

---

## ⚡ Quickstart

> Pick the path that matches what you’re doing 👇

### 🧾 If you’re building a validator / QA tool
- Put the **CLI entry** in `tools/<tool-name>/` (or `tools/<tool-name>.py`)
- Put the **reusable logic** in `tools/_lib/`
- Make it **deterministic**, **idempotent**, and **fail-closed** for promotion lanes

### 📦 If you’re publishing data/artifacts
- Use `_lib` helpers for:
  - staging → atomic commit (no partial publishes) ♻️
  - checksums/manifests 🔏
  - STAC/DCAT/PROV generation 🧾🧬
  - classification propagation 🔐

### 🧯 If you’re responding to an incident
- Ensure every publish lane and agent honors the **kill switch**
- `_lib` should provide one canonical function for kill-switch evaluation

---

## 🎯 What belongs in `_lib`

✅ **Belongs here**
- Small, composable utilities that are reused across tools
- Validation primitives (schema checks, link safety, geometry guards)
- Catalog + provenance builders (STAC/DCAT/PROV)
- Integrity helpers (hashes, manifests, deterministic IDs)
- Safe I/O wrappers (atomic writes, size limits, path normalization)
- Policy wrappers (OPA/Conftest invocation + result parsing)
- “Governed defaults” (deny-by-default behaviors)

❌ **Does not belong here**
- One-off scripts and notebooks (put in `tools/` or `notebooks/`)
- “Quick hacks” that mutate state without provenance
- Environment-specific secrets, credentials, or hardcoded endpoints
- UI components (keep UI in the frontend app; `_lib` is tooling)

---

## 🧱 KFM invariants this library must enforce

KFM’s pipeline is **ordered and gated**. `_lib` exists to make that enforceable.

### ✅ Pipeline boundary rule

```mermaid
flowchart LR
  A[Raw Sources] --> B[ETL + Normalization]
  B --> C[STAC Items + Collections]
  C --> D[DCAT Dataset Views]
  C --> E[PROV Lineage Bundles]
  C --> G[Graph references catalogs]
  G --> H[API Layer (contracts + redaction)]
  H --> I[Map UI / 3D]
  I --> J[Story Nodes]
  J --> K[Focus Mode]
```

**If it’s visible downstream, it must be cataloged + traceable.** 🧾🧬

### ✅ Contract-first + provenance-first

- Schemas and contracts are first-class artifacts 📜  
- Every transformation/run produces provenance (inputs → activity → outputs) 🧬  
- Evidence artifacts (AI/analysis outputs) are treated like datasets ✅

### ✅ Fail-closed promotion

If any of the following are true, `_lib`-powered gates must block promotion:
- provenance missing or malformed
- catalogs invalid or unsafe links exist
- classification propagation violated
- integrity signals missing (when required)
- sensitive precision leaked (exact coordinates) 🧯

---

## 🗂️ Expected layout

> This is the **recommended** layout (v13-friendly). Adjust names to the repo’s language choices, but keep the separation.

<details>
<summary><strong>📁 Suggested folder tree</strong></summary>

```text
📁 tools/_lib/
├─ 📄 README.md                      # you are here ✅
├─ 📁 core/                          # config, logging, types, paths
│  ├─ 📄 config.py
│  ├─ 📄 logging.py
│  ├─ 📄 paths.py
│  └─ 📄 errors.py
├─ 📁 io/                            # safe I/O, atomic writes, size guards
│  ├─ 📄 atomic.py
│  ├─ 📄 json.py
│  └─ 📄 fs.py
├─ 📁 geo/                           # CRS, bounds, geometry validation
│  ├─ 📄 crs.py
│  ├─ 📄 bounds.py
│  └─ 📄 geometry.py
├─ 📁 catalogs/                      # STAC/DCAT builders + validators
│  ├─ 📄 stac.py
│  ├─ 📄 dcat.py
│  ├─ 📄 link_safety.py
│  └─ 📄 catalog_qa.py
├─ 📁 prov/                          # PROV generation + normalization
│  ├─ 📄 prov_bundle.py
│  └─ 📄 agents.py
├─ 📁 integrity/                     # checksums, manifests, reproducibility
│  ├─ 📄 hashes.py
│  ├─ 📄 manifest.py
│  └─ 📄 ids.py
├─ 📁 policy/                        # policy-as-code wrappers (OPA/Conftest)
│  ├─ 📄 conftest.py
│  └─ 📄 results.py
├─ 📁 security/                      # kill switch, allowlists, secret-safe utils
│  ├─ 📄 kill_switch.py
│  ├─ 📄 allowlists.py
│  └─ 📄 safe_subprocess.py
├─ 📁 db/                            # Postgres/PostGIS helpers (safe + pooled)
│  ├─ 📄 pg.py
│  ├─ 📄 postgis.py
│  └─ 📄 migrations.py
├─ 📁 graph/                         # graph import/export + safe query helpers
│  ├─ 📄 neo4j.py
│  └─ 📄 rdf.py
├─ 📁 modeling/                      # analytics + simulation utilities
│  ├─ 📄 stats.py
│  ├─ 📄 regression.py
│  └─ 📄 uncertainty.py
└─ 📁 tests/                         # unit tests + golden fixtures
   ├─ 📁 fixtures/
   └─ 📄 test_*.py
```

</details>

---

## 🧩 Core capability areas

### 🧾 Catalog QA (STAC/DCAT/PROV)
`tools/_lib/catalogs/` should provide:
- required-field validation (licenses, extents, keywords, distributions)
- **link safety** checks (no unsafe `href`, no unexpected schemes, optional allowlists)
- broken link detection (local references + remote policy)
- geometry and CRS sanity checks for spatial assets
- “metadata like code” experience: local CLI validate, CI fail on violations ✅

> [!TIP]
> The KFM roadmap explicitly calls for a **dataset schema & validator CLI** and for **CI Catalog QA gate integration**—this library is where the reusable parts should live. 🧾✅

---

### 🔏 Integrity + reproducibility
`tools/_lib/integrity/` is responsible for:
- checksums/digests (file-level and/or chunked)
- deterministic run IDs and dataset IDs
- manifest generation (inputs + outputs + hashes + tool versions)
- “re-run safety”: idempotent pipelines and atomic publish patterns ♻️

Common patterns:
- write to `.../staging/` → validate → rename/move to final location
- record run config + tool version in PROV + manifest

---

### 🔐 Policy-as-code wrappers (OPA / Conftest)
`tools/_lib/policy/` should **not** contain policies; it contains wrappers:
- run Conftest/OPA in a consistent way
- normalize results for CI annotations
- provide “deny-by-default” behavior for promotion

---

### 🗺️ Geo safety + correctness
`tools/_lib/geo/` should cover:
- CRS validation + normalization (explicit SRIDs)
- Kansas bounding checks (when relevant)
- geometry validity guards (self-intersections, invalid rings)
- “geospatial DoS” protection:
  - max feature counts
  - max vertex counts
  - size/time limits for operations

---

### 🗄️ Database + graph helpers
`tools/_lib/db/` and `tools/_lib/graph/` are where we keep:
- connection hygiene (pooling, timeouts, read/write separation)
- parameterized queries only (no string-built SQL)
- query “budgeting” hooks (timeouts, row limits, paging)
- safe export patterns (no accidental full-table dumps)

---

### 🧠 Modeling + analytics utilities
`tools/_lib/modeling/` exists so analysis work can be:
- reproducible (same input/config ⇒ same output)
- provenance-linked (model runs are PROV activities)
- uncertainty-aware (confidence intervals, caveats, limitations)

---

### 🌐 UI + rendering adjacent (tooling only)
`tools/_lib` may include **tooling for UI assets** (not UI code):
- tile/COG generation helpers
- safe 3D asset validation (size limits, format checks)
- map style linting (where applicable)

---

## 🧪 CI + gates integration

This folder should make CI lanes easy to compose:

### ✅ “Detect → Validate → Promote” (canonical)
- **Detect** changes (diffs, checksums, file events)
- **Validate** with fast + strict gates
- **Promote** only after validation + attestations (release lanes)

### 🧾 Typical gates powered by `_lib`
- schema validation for metadata JSON
- STAC/DCAT required fields
- PROV presence + shape checks
- link safety allowlists
- geometry/CRS validation
- classification propagation (no output less restricted than input)
- artifact integrity (checksums/manifests)

---

## 🤖 Automation patterns

### ✅ WPE: Watcher → Planner → Executor (PR-only)
If we add agentic automation, `_lib` should provide:
- canonical plan format + hashing (deterministic planning)
- evidence bundle emission (what changed and why)
- a **hard prohibition** on auto-merge (executor opens PR only)

### 🧯 Kill switch
Every publish lane must stop when kill-switch is enabled.

Recommended interface:
- env var: `KFM_KILL_SWITCH=true`
- optional file: `.kfm/kill-switch.yml`

> [!IMPORTANT]
> `_lib` should expose **one** kill-switch check function used everywhere—no drift.

---

## 🔐 Governance + sensitive locations

KFM is “mostly open,” but not everything is public. `_lib` must support:

### 📚 Classification levels (recommended)
| Classification | Who can access | Typical examples |
|---|---|---|
| **Public** 🌍 | Everyone | Published layers with clear licensing |
| **Internal** 🏢 | Maintainers/collaborators | Draft catalogs, staging pipelines |
| **Confidential** 🔐 | Explicitly approved | Controlled layers, limited sharing |
| **Restricted** 🧨 | Admin/Owners only | Secrets, security logs, exact protected coordinates |

### 🗺️ Sensitive precision tiers (recommended)
| Precision tier | Examples | Allowed in Public? |
|---|---|---|
| **Exact** 🎯 | point GPS, parcel centroid, address-level | ❌ unless explicitly permitted |
| **Neighborhood** 🧭 | 0.5–2km buffers | ⚠️ governance approval |
| **County/Region** 🗺️ | polygons, broad bbox | ✅ typically safe |
| **Grid/Index** 🧊 | H3/geohash cells | ✅ if cell size is appropriate |
| **Redacted** 🕳️ | “location protected” | ✅ preferred for cultural sensitivity |

---

## 📈 Performance + scalability notes

This library should default to **safe performance**:
- never load entire datasets into memory unless explicitly intended
- stream when possible; page when not
- avoid giant geometries and unbounded graph traversals

### 🗄️ Postgres/PostGIS (practical defaults)
- always parameterize queries
- index spatial joins intentionally
- rate-limit expensive endpoints and exports
- separate read vs write creds (and migrations)

### 🕸️ Graph query hygiene
- prefer query patterns that avoid huge intermediate materialization
- limit traversal depth; require explicit “budget”
- treat “graph expansion” as a costed operation

---

## 🧠 Modeling, statistics, and “NASA-grade” discipline

KFM includes simulations/analytics and may publish derived outputs. `_lib` should encourage:

- validation & verification mindset (tests + known baselines)
- experimental design discipline (controls, leakage prevention)
- model outputs that include uncertainty/limits
- reproducible runs (config + seed + versions recorded)

> [!NOTE]
> If an analysis output is published, it becomes a **first-class dataset**: cataloged (STAC/DCAT), traced (PROV), and governed (classification + redaction).

---

## 🧯 Secure coding rules for `_lib`

### ✅ Non-negotiables
- **No secrets** in code, tests, or fixtures
- **No implicit network** access  
  - network must be opt-in and allowlisted (SSRF-safe)
- **No import-time side effects** (no filesystem writes at import)
- **Deterministic defaults** (explicit seeds, stable ordering)
- **Fail-closed for promotion** (validators block on uncertainty)

### 🧨 Defensive-only security posture
KFM may include security references in the project library. That’s for:
- threat modeling
- defensive awareness
- safe-by-default engineering  
Not for offensive tooling contributions.

---

## 🧑‍💻 Contributing checklist

When you change or add `_lib` code:

- [ ] Added/updated unit tests ✅
- [ ] Documented public functions (docstrings) 🧾
- [ ] No secrets or sensitive data in fixtures 🔐
- [ ] Deterministic behavior verified (seed/config captured) ♻️
- [ ] Validation results are machine-readable (CI-friendly) 🤖
- [ ] If touching catalogs/provenance: updated golden samples + schema checks 🧬
- [ ] If touching governance: updated policy tests (good/bad samples) ⚖️
- [ ] If touching publish paths: kill-switch honored 🧯

---

## 📚 Reference shelf

These project files inform design decisions and guardrails for `_lib` (data engineering, GIS, modeling discipline, governance, performance, and defensive security awareness). 📚✨

<details>
<summary><strong>📚 Library map (grouped by how it influences tooling)</strong></summary>

### 🧾 KFM core specs & workflows
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** — architecture, roadmap, “metadata like code,” QA culture, and system boundaries
- **MARKDOWN_GUIDE_v13** + **Comprehensive Markdown Guide** — contract-first docs + evidence-first narrative standards

### 🗺️ GIS, remote sensing, and cartography
- *Python Geospatial Analysis Cookbook* — practical geoprocessing patterns and tooling
- *Cloud-Based Remote Sensing with Google Earth Engine* — remote sensing pipeline patterns and reproducibility
- *Making Maps (GIS design)* + *Mobile Mapping* — map design choices that influence validation + presentation tooling
- *Archaeological 3D GIS* — 3D GIS constraints, formats, and visualization considerations

### 📈 Statistics, regression, and Bayesian methods
- *Understanding Statistics & Experimental Design* — evaluation discipline and experiment design
- *Regression Analysis with Python* + linear regression slides — reproducible regression workflows and diagnostics
- *Think Bayes* — Bayesian uncertainty and decision support framing
- *Graphical Data Analysis with R* — exploratory analysis patterns that can be productized as repeatable reports

### 🧪 Modeling & simulation (rigor + reproducibility)
- *Scientific Modeling and Simulation (NASA-grade guide)* — V&V mindset and reproducibility expectations
- *Generalized Topology Optimization* — advanced modeling/simulation methods (future-facing)
- *Spectral Geometry of Graphs* — graph analytics methods that may inform future graph tooling

### 🗄️ Data engineering, databases, and performance
- *Database Performance at Scale* — latency-aware design + scaling patterns
- *PostgreSQL Notes for Professionals* — Postgres basics and operational patterns
- *Scalable Data Management for Future Hardware* — query execution/pipeline ideas relevant for graph workloads
- *Data Spaces* — policy-aware data sharing concepts (classification + access controls)

### 🌐 Frontend + visualization tooling
- *WebGL Programming Guide* — WebGL constraints that inform 3D asset validation and build tooling
- *Responsive Web Design with HTML5 and CSS3* — UI constraints and packaging concerns (tooling side)

### 🔐 Security awareness (defensive use only)
- *Ethical Hacking & Countermeasures* — threat awareness for validation/hardening
- *Gray Hat Python* — defensive understanding of attack surfaces (not a tooling goal)
- *Compressed Image File Formats* — safe decoding and format pitfalls (DoS risks, parsing issues)
- *Concurrent Real-Time and Distributed Programming in Java* — concurrency patterns that inform worker safety

### 🧠 Governance, ethics, and societal framing
- *Introduction to Digital Humanism* — human-centered governance, accountability, and sovereignty framing
- *On the path to AI Law…* — expectations for AI-era systems: transparency, traceability, and responsible use
- *Principles of Biological Autonomy* — autonomy constraints and systems thinking (useful for agent design)

### 🧱 Programming compendiums (general engineering patterns)
- **A, B–C, D–E, F–H, I–L, M–N, O–R, S–T, U–X programming books** — broad reference shelf for patterns, languages, and implementations

</details>

---

> [!TIP]
> If you’re adding a new “capability slice” (e.g., catalog QA, provenance builders, policy wrapper):
> - start with **contracts + samples**
> - add **tests + golden fixtures**
> - wire into CI as a **fail-closed** gate ✅
