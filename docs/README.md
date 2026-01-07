<!--
📌 This README documents the *canonical* executable code boundary for KFM.
🗓️ Last updated: 2026-01-07
-->

# 🧩 `src/` — Kansas Frontier Matrix (KFM) Executable Source Code 🧭🗺️

![KFM](https://img.shields.io/badge/KFM-src%2F%20canonical-1f6feb)
![README](https://img.shields.io/badge/README-v1.2.0-8957e5)
![Order](https://img.shields.io/badge/invariant-ETL%E2%86%92Catalog%E2%86%92Graph%E2%86%92API%E2%86%92UI%E2%86%92Story%E2%86%92Focus-critical)
![Contracts](https://img.shields.io/badge/contracts-contract--first-0aa3a3)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE%20%2B%20Sovereignty-2ea043)
![Security](https://img.shields.io/badge/security-hostile--inputs%20%2B%20deny--by--default-red)

> Canonical home for **auditable**, **reproducible**, **governed** KFM executable code:  
> **🧪 ETL Pipelines → 🗂️ Catalogs (STAC/DCAT/PROV) → 🕸️ Graph → 🛡️ APIs** ✅  
> Everything else (docs, data assets, UI) lives outside this boundary.

> [!IMPORTANT]
> **KFM’s non‑negotiable order:**  
> **ETL → STAC/DCAT/PROV Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**  
> If your change breaks this ordering (even “temporarily”), it’s not mergeable.

---

## 🔗 Quick links
- 🧭 Repo overview: **[`../README.md`](../README.md)**
- 📦 Data + metadata boundary: **[`../data/README.md`](../data/README.md)**
- 🛰️ API boundary (backend): **[`../api/README.md`](../api/README.md)** *(if present)*
- 🌐 Web UI boundary: **[`../web/README.md`](../web/README.md)** *(if present)*
- 🧠 Governance + SOPs: **[`../mcp/MCP-README.md`](../mcp/MCP-README.md)** *(recommended)*
- 🤝 Collaboration & automation: **[`../.github/README.md`](../.github/README.md)** *(if present)*

---

## 🧭 Quick navigation
- [📘 Overview](#-overview)
- [🧠 Core invariants](#-core-invariants)
- [📌 Repository boundaries](#-repository-boundaries-what-goes-where)
- [🧱 Architecture](#-architecture)
  - [🧪 Pipelines](#-pipelines-srcpipelines)
  - [🏷️ Catalog writers & validators](#-catalog-writers--validators-stacdcatprov)
  - [🕸️ Graph](#-graph-srcgraph)
  - [🛡️ Server](#-server-srcserver)
  - [📜 Contracts](#-contracts-srcservercontracts)
- [🗂️ Directory layout](#️-directory-layout)
- [🏁 Golden paths](#-golden-paths-most-common-workflows)
- [🧪 Local dev norms](#-local-dev-norms)
- [✅ Validation & CI/CD](#-validation--cicd)
- [🔒 Security & hostile inputs](#-security--hostile-inputs)
- [📈 Modeling & simulation discipline](#-modeling--simulation-discipline)
- [⚙️ Scaling & data management](#️-scaling--data-management)
- [📚 Project reference library influence map](#-project-reference-library-influence-map)
- [🕰️ Version history](#️-version-history)

---

## 🧾 Doc metadata

| Field | Value |
|---|---|
| Doc | `src/README.md` |
| Status | Active ✅ |
| Last updated | **2026-01-07** |
| Audience | Contributors shipping pipelines, catalogs, graph loaders, API services |
| Prime directive | If it changes “spatial truth,” it must be **traceable + contractable + testable** |

---

## 📘 Overview

### ✅ Purpose
`src/` is the canonical home for KFM **executable source code** that must remain:

- 🧾 **auditable** (what changed, why, by whom)
- 🧬 **reproducible** (same inputs + config → same outputs)
- 🧷 **contracted** (explicit interfaces between stages)
- 🔐 **governed** (classification propagation, redaction readiness, evidence links)

### 🎯 What belongs in `src/`
- 🧪 ETL/pipeline code that turns **`data/raw/ → data/work/ → data/processed/`**
- 🏷️ Catalog emitters & validators that produce **STAC/DCAT/PROV**
- 🕸️ Graph build/load utilities **from catalog outputs** (never from ad‑hoc “mystery data”)
- 🛡️ API boundary code (or equivalent server layer) that enforces contracts + governance

### 🚫 What does *not* belong in `src/`
- 📚 governed docs → `docs/`
- 📦 data assets & metadata outputs → `data/`
- 🌐 UI/web client → `web/`
- 📓 experiments → `notebooks/` *(and anything “real” must graduate back into `src/` + catalogs + tests)*

> [!TIP]
> If you can’t explain the lineage (inputs → transforms → outputs) in one paragraph, your code probably isn’t ready to live in `src/`. 🧾

---

## 🧠 Core invariants

> [!IMPORTANT]
> KFM enforces this pipeline ordering end‑to‑end:
>
> **ETL → STAC/DCAT/PROV Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**

```mermaid
flowchart LR
  A[🧪 ETL Pipelines] --> B[🗂️ STAC/DCAT/PROV Catalogs]
  B --> C[🕸️ Graph Build/Load]
  C --> D[🛡️ APIs]
  D --> E[🖥️ UI]
  E --> F[📚 Story Nodes]
  F --> G[🎯 Focus Mode]
```

### ✅ What this means for contributors
- ✅ **Nothing enters the graph/UI unless it has catalog records.**
- ✅ **UI never queries internal stores directly** — only via governed APIs.
- ✅ **Derived products** (joins, AI/ML outputs, simulations) are treated as datasets:
  - stored in `data/processed/**`
  - cataloged (STAC/DCAT)
  - traced (PROV)
- ✅ **No privacy downgrade:** outputs cannot be less restricted than inputs without an explicit, reviewed redaction step.

### 🚫 Things you must not do
- ❌ “Quick hack” ETL outputs without catalogs/PROV
- ❌ Manual graph inserts that bypass catalog IDs
- ❌ Contract-breaking API changes without versioning
- ❌ Silent projection/unit changes (CRS + units must be explicit)

---

## 📌 Repository boundaries: what goes where?

Use this when you’re unsure:

| You are adding… | Put it in… | Why |
|---|---|---|
| ETL + transforms + QA validators | `src/pipelines/` | Reproducible outputs + catalog emission |
| STAC/DCAT/PROV writers | `src/pipelines/` | Catalogs are the “gate” to graph & UI |
| Graph build/load + ontology mapping | `src/graph/` | Graph is a derived reference index |
| API services + policy enforcement | `src/server/` | Single client boundary (auth/redaction/contracts) |
| Contracts (OpenAPI/GraphQL) | `src/server/contracts/` | Stable integration surface |
| Docs/runbooks/standards | `docs/` | Governed writing lives here |
| Data & metadata artifacts | `data/` | Canonical lifecycle + publication boundary |
| Schemas/profiles | `schemas/` | Machine validation registry |
| UI client | `web/` | View + interaction boundary |

---

## 🧱 Architecture

KFM is “clean boundaries first”: domain logic stays pure; IO and frameworks stay at the edges.

```mermaid
flowchart TB
  subgraph Data["📦 Data & Metadata Boundary"]
    RAW["data/raw/**"] --> WORK["data/work/**"] --> PROC["data/processed/**"]
    PROC --> STAC["data/stac/**"]
    PROC --> DCAT["data/catalog/dcat/**"]
    PROC --> PROV["data/prov/**"]
  end

  subgraph SRC["🧩 src/ (Executable Code)"]
    PIPES["🧪 pipelines/"]
    GRAPH["🕸️ graph/"]
    SERVER["🛡️ server/"]
  end

  RAW --> PIPES --> WORK --> PIPES --> PROC
  PIPES --> STAC
  PIPES --> DCAT
  PIPES --> PROV
  STAC --> GRAPH
  DCAT --> GRAPH
  PROV --> GRAPH
  GRAPH --> SERVER
  STAC --> SERVER
  DCAT --> SERVER
  PROV --> SERVER
```

### 🧪 Pipelines (`src/pipelines/`)
What goes here:
- 🔌 connectors (downloaders, scrapers, importers)
- 🧼 transforms (CRS fixes, cleaning, normalization, georeferencing)
- 🧾 catalog writers: STAC/DCAT/PROV
- ✅ validation gates (schema, links, determinism, QA reports)

**Hard rule:** outputs are not “publishable” unless catalogs + PROV exist.

### 🏷️ Catalog writers & validators (STAC/DCAT/PROV)
Catalogs are *interfaces* downstream systems trust:
- STAC: spatial/temporal + asset indexing
- DCAT: dataset discovery + distributions
- PROV: lineage (inputs → activity → outputs) + config + run identity

**Hard rule:** graph and API must reference catalog IDs, not local ad-hoc paths.

### 🕸️ Graph (`src/graph/`)
What goes here:
- graph-ready artifact builders from **catalogs**
- idempotent loaders/migrations
- validation utilities (referential integrity, ontology alignment)

Graph is:
- ✅ a relationship index + navigation accelerator  
- ❌ not a second data warehouse

### 🛡️ Server (`src/server/`)
What goes here:
- API boundary (REST/GraphQL)
- authn/authz + redaction + classification propagation
- evidence bundles for Story Nodes & Focus Mode
- telemetry at the boundary

**Hard rule:** clients integrate via contracts; they don’t bind to DB/graph schemas.

### 📜 Contracts (`src/server/contracts/`)
Contracts are the stable interface between KFM internals and the outside world:
- versioned
- reviewed
- testable
- explicit about error semantics and provenance pointers

> [!TIP]
> Contract change → tests → implementation.  
> If you can’t write a contract test, it’s not ready to ship. ✅

---

## 🗂️ Directory layout

### 🧭 Repo context (target shape)
```text
📁 docs/                 # 📚 governed docs (policies, standards, architecture)
📁 src/                  # 🧩 executable source (this folder)
📁 data/                 # 📦 raw → work → processed + STAC/DCAT/PROV
📁 schemas/              # 📐 machine-validated profiles/schemas (STAC/DCAT/PROV)
📁 web/                  # 🌐 UI (maps + timeline + Focus Mode)
📁 .github/              # 🤝 CI/CD + templates + CODEOWNERS + automation
```

### 🧩 `src/` (canonical homes)
```text
📁 src/
├── 🧪 pipelines/            # ETL + catalog writers/validators (STAC/DCAT/PROV)
├── 🕸️ graph/                # graph build/load tools (from cataloged outputs)
└── 🛡️ server/               # API boundary (policy + services)
    └── 📜 contracts/         # OpenAPI/GraphQL contracts (source of truth)
```

### ⭐ Recommended internal layering (clean boundaries)
```text
src/server/
  domain/                    # 💠 types + invariants (no framework imports)
  application/               # 🧠 use-cases/services (calls ports)
  adapters/                  # 🔌 db/http/graph adapters (translation layer)
  infrastructure/            # 🧱 framework glue (FastAPI, auth, DI, config)
  contracts/                 # 📜 OpenAPI/GraphQL (source of truth)
```

---

## 🏁 Golden paths (most common workflows)

### 1) Add a new pipeline job ✅
1. 🧾 Define inputs + outputs + classification expectations (document in code + README)
2. 🧪 Implement transforms (deterministic, config-driven)
3. 📦 Write outputs to `data/processed/<domain>/...`
4. 🏷️ Emit:
   - STAC (Collection + Items)
   - DCAT dataset entry
   - PROV run bundle
5. ✅ Add validators (schema + link checks + “no downgrade” checks)
6. 🧪 Add tests (unit + fixtures + at least one end-to-end “mini run”)

### 2) Add a new graph relationship type ✅
1. 🏷️ Confirm catalog IDs represent what you need (STAC/DCAT/PROV links exist)
2. 🕸️ Update graph schema/ontology layer
3. 🔁 Update loader to ingest references (idempotent)
4. ✅ Validate referential integrity (no orphan IDs)
5. 🧪 Add graph validation tests

### 3) Add or change an API endpoint ✅
1. 📜 Update contracts **first** (`src/server/contracts/`)
2. 🧠 Add/modify use-case in `application/`
3. 🔌 Implement adapters/repositories if needed
4. 🛡️ Enforce auth + redaction + classification
5. 🧪 Add tests (contract + route + auth regression)
6. 📈 Add telemetry (request IDs, safe logs)

---

## 🧪 Local dev norms

> Goal: **“If it runs in CI, it should run locally.”** 🐳

### ✅ Suggested command surface
```bash
# quality gates
make lint
make test

# pipelines
make pipeline-run JOB=<job-id>
make pipeline-validate

# graph
make graph-build
make graph-load

# server
make serve
```

### 🧭 Reproducibility defaults
- pin dependency versions where feasible
- record run configs + hashes
- seed randomness for modeling/simulation paths
- keep environments consistent (Docker recommended)

---

## ✅ Validation & CI/CD

### CI intent (minimum bar)
- 🧹 lint + formatting
- ✅ unit tests
- 🤝 contract tests (OpenAPI/GraphQL)
- 🧾 schema validation (STAC/DCAT/PROV)
- 🔗 link checks (assets exist; IDs resolve)
- 🔐 security scans (secrets; common foot-guns)
- 🧷 governance checks (classification propagation; redaction regressions)

### PR self-check (before opening)
- [ ] outputs deterministic (stable IDs + hashes)
- [ ] outputs land correctly (`raw/` → `work/` → `processed/`)
- [ ] STAC/DCAT/PROV emitted + validated
- [ ] graph loads driven from catalogs (no ad-hoc inserts)
- [ ] contract updated first (if API surface changed)
- [ ] tests added/updated
- [ ] classification propagates end-to-end

> [!CAUTION]
> “Green CI” is a merge requirement. If CI fails, fix the root cause — don’t ship flaky behavior. 🤖🚫

---

## 🔒 Security & hostile inputs

KFM processes a lot of “files from the world” (maps, documents, imagery, exports). Assume inputs are hostile by default. 🧯

### ✅ Required safety posture
- 🔐 Never commit secrets; never log secrets
- 🧼 Validate and sanitize all untrusted inputs (files, URLs, metadata)
- 🧯 Guard against:
  - path traversal (uploads/extractors)
  - SSRF (any URL fetching)
  - decompression bombs (archives / images)
  - parser exploitation (complex formats, 3D models, PDFs)
- 🧷 Deny-by-default classification: if unsure, treat as restricted until proven otherwise
- 🧪 Add security regression tests for every “new surface”

### “Worst-case” question to ask
> “If someone malicious controls this input, what’s the maximum harm?”  
If the answer is “exfiltrate data / run code / crash the system,” add guards **before** merging.

---

## 📈 Modeling & simulation discipline

KFM treats models as **decision-support**, not truth generators.

### ✅ Minimum expectations for any model/simulation code in `src/`
- define objective + assumptions explicitly
- record parameters + seeds
- report uncertainty (not just point estimates)
- validate (unit tests + sanity checks) and verify (V&V mindset)
- publish outputs as governed evidence artifacts:
  - store in `data/processed/**`
  - catalog (STAC/DCAT)
  - trace (PROV)

### 🧪 “Model hygiene” checklist
- [ ] train/test split recorded (or reason why not)
- [ ] diagnostics captured (residuals, calibration, error bars)
- [ ] sensitivity analysis for key parameters
- [ ] artifacts versioned (plots/metrics/model cards)
- [ ] provenance pointers included in outputs

---

## ⚙️ Scaling & data management

The KFM stack should scale from “small demo” to “Kansas-wide spatiotemporal workloads” without architectural rewrites.

### ✅ Practical scaling rules
- keep data formats web-friendly (COG, tiles, compact GeoJSON/TopoJSON)
- index spatial data (PostGIS) rather than brute-force scanning
- separate compute from serving (jobs/workers for heavy work)
- keep metadata as the interface (catalogs are first-class)

---

## 📚 Project reference library influence map

> [!NOTE]
> These project files inform *how we design and review* `src/` code: reproducibility, governance, security, data management, modeling rigor, and visualization constraints.

<details>
<summary><strong>📦 Expand: All project files → what they influence in <code>src/</code></strong></summary>

| Project file | Primary lens | How it upgrades `src/` decisions |
|---|---|---|
| `Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx` | 🧭 System blueprint | Defines the platform ordering (ETL→catalog→graph→API→UI→story→focus) and “governed boundary” mindset. |
| `Latest Ideas.docx` | 💡 Roadmap seed | Captures experiments/features that should graduate into contracts + pipelines instead of living as one-offs. |
| `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` | 🛰️ RS pipelines | Informs ETL patterns for EO time-series, export workflows, and how to treat derived indices as publishable datasets (with provenance). |
| `python-geospatial-analysis-cookbook.pdf` | 🗺️ GIS engineering | Guides CRS hygiene, vector/raster IO, PostGIS integration, and “do transforms at boundaries” discipline. |
| `making-maps-a-visual-guide-to-map-design-for-gis.pdf` | 🎨 Cartography | Reminds that symbology/aggregation choices shape meaning; pipeline outputs should be designed for honest downstream visualization. |
| `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` | 📱 Mobile/offline | Reinforces constraints that matter upstream: simplify, tile, cache, and support offline/low-bandwidth workflows. |
| `responsive-web-design-with-html5-and-css3.pdf` | 🌐 Web constraints | Encourages producing web-friendly assets (sizes, payload budgets, progressive loading) and documentation that respects real devices. |
| `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` | 🧊 GPU/3D | Informs how dense spatial data should be prepared (tiling/LOD) and why coordinate conventions must be explicit. |
| `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` | 🖼️ Image pipelines | Helps upstream choices for thumbnails, QA screenshots, compression, and avoiding bloated repos/artifacts. |
| `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` | 🐘 Data store | Shapes Postgres conventions: schema discipline, indexes, migrations, role separation, and export/import patterns. |
| `Scalable Data Management for Future Hardware.pdf` | ⚙️ Performance | Encourages thinking in partitions, locality, concurrency, and “metadata-driven” access patterns that scale with new hardware. |
| `Data Spaces.pdf` | 🔗 Interop & federation | Supports the “catalogs as interfaces” mentality and treating data products as discoverable, governed assets across domains. |
| `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` | 🧪 V&V discipline | Brings verification/validation, sensitivity analysis, and simulation ethics into pipeline + modeling code reviews. |
| `Understanding Statistics & Experimental Design.pdf` | 📊 Rigor | Reminds about bias, confounders, experimental design, and when “pretty results” are misleading. |
| `regression-analysis-with-python.pdf` | 📈 Regression | Guides baseline modeling, diagnostics, reproducible regression workflows, and careful interpretation. |
| `Regression analysis using Python - slides-linear-regression.pdf` | 📈 Quick reference | Handy reminders for linear regression assumptions, feature scaling, and evaluation conventions. |
| `graphical-data-analysis-with-r.pdf` | 📉 EDA instincts | Encourages visualization-driven sanity checks and spotting artifacts early (before publishing outputs). |
| `think-bayes-bayesian-statistics-in-python.pdf` | 🎲 Uncertainty | Encourages Bayesian thinking, posterior uncertainty reporting, and explicit priors when appropriate. |
| `Spectral Geometry of Graphs.pdf` | 🕸️ Graph analytics | Supports graph feature engineering and cautious interpretation of network metrics as “evidence signals,” not facts. |
| `Generalized Topology Optimization for Structural Design.pdf` | 🧮 Optimization | Informs how to structure optimization jobs as reproducible workflows with constraints, objectives, and audit trails. |
| `Principles of Biological Autonomy - book_9780262381833.pdf` | 🧠 Systems thinking | Encourages feedback-loop awareness, stability, and resilience in pipeline + governance design. |
| `Introduction to Digital Humanism.pdf` | ❤️ Human-centered | Reinforces accountability, transparency, and dignity in governance decisions and “human-in-the-loop” defaults. |
| `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` | ⚖️ AI governance | Encourages documentation and labeling of AI-assisted outputs, traceability, and risk framing (esp. for decision support). |
| `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` | 🛡️ Security mindset | Reinforces hostile-input handling, secure coding posture, and understanding exploit mechanics when building parsers/pipelines. |
| `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` | 🧯 Threat modeling | Informs network/service hardening thinking, privilege boundaries, and defensive assumptions for ingest/integration code. |
| `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` | 🧵 Concurrency | Reminds that concurrency is hard; supports careful design of worker/job orchestration and avoiding race conditions. |
| `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` | 🤖 ML practice | Encourages pragmatic baselines, data-centric iteration, and evaluation discipline before “fancy models.” |
| `A programming Books.pdf` | 🧰 Polyglot reference | General language/tooling reference; supports choosing the right tool while maintaining boundaries and code quality. |
| `B-C programming Books.pdf` | 🧰 Polyglot reference | General reference for foundational languages/patterns and interoperability thinking. |
| `D-E programming Books.pdf` | 🧰 Polyglot reference | General reference; supports standardized engineering practices across stacks. |
| `F-H programming Books.pdf` | 🧰 Polyglot reference | General reference; supports careful API/interface thinking and tooling discipline. |
| `I-L programming Books.pdf` | 🧰 Polyglot reference | General reference; supports maintainability and stable interfaces in shared systems. |
| `M-N programming Books.pdf` | 🧰 Polyglot reference | General reference; supports systems + networking awareness where needed. |
| `O-R programming Books.pdf` | 🧰 Polyglot reference | General reference; supports practical engineering across languages and ecosystems. |
| `S-T programming Books.pdf` | 🧰 Polyglot reference | General reference; supports testing, tooling, and software craftsmanship culture. |
| `U-X programming Books.pdf` | 🧰 Polyglot reference | General reference; supports cross-discipline integration and long-term maintainability. |

</details>

---

## 🕰️ Version history

| Version | Date | Summary of changes | Author |
|---:|---|---|---|
| v1.2.0 | 2026-01-07 | Strengthened `src/` as an executable governance boundary; added “golden paths,” hostile-input security posture, modeling/simulation discipline, scaling notes, and a full project-file influence map. | KFM Engineering |
| v1.1.0 | 2026-01-06 | Aligned `src/` doc with contract-first + provenance-first rules; added clean-boundary layout guidance; added local dev norms; strengthened governance guardrails. | KFM Engineering |
| v1.0.1 | 2026-01-06 | Polished structure + navigation; added contributor checklist; clarified contract-first + governance guardrails. | KFM Engineering |
| v1.0.0 | 2025-12-31 | Initial `src/README.md` created from Master Guide v13 + KFM docs; added emoji directory layout and subsystem guide. | KFM Engineering |