---
id: DOC-DOCS-README
title: "docs/ — Kansas Frontier Matrix (KFM) Governed Documentation"
status: active
version: v1.1.0
last_updated: 2026-01-11
owners:
  - KFM Engineering
tags:
  - kfm
  - documentation
  - governance
  - standards
  - runbooks
  - story-nodes
  - focus-mode
---

<!--
📌 This README documents the *canonical governed documentation boundary* for KFM.
🗓️ Last updated: 2026-01-11
✅ Note: KFM’s v13 docs discipline assumes docs are validated (front‑matter + links + schemas) and treated as shippable system artifacts.
-->

# 📚 `docs/` — Kansas Frontier Matrix (KFM) Governed Documentation 📜🧭

![KFM](https://img.shields.io/badge/KFM-docs%2F%20canonical-1f6feb)
![README](https://img.shields.io/badge/README-v1.1.0-8957e5)
![Evidence](https://img.shields.io/badge/evidence--first-STAC%20%2B%20DCAT%20%2B%20PROV-0aa3a3)
![Contract-first](https://img.shields.io/badge/contract--first-schemas%20%2B%20API%20contracts-0aa3a3)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE%20%2B%20Sovereignty-2ea043)
![Accessibility](https://img.shields.io/badge/docs-accessible%20%2B%20scannable%20%2B%20citable-8250df)
![Security](https://img.shields.io/badge/security-no%20secrets%20%2B%20no%20side--channels-red)

> Canonical home for KFM’s **governed documentation**:  
> **architecture + standards + templates + runbooks + governance + story nodes** — written so that decisions are **auditable**, claims are **citable**, and change is **reviewable**.  
> This is where KFM stays explainable as it scales. 🧠🗺️

> [!IMPORTANT]
> **KFM’s non‑negotiable order (docs must reinforce it):**  
> **ETL → STAC/DCAT/PROV Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**  
> If a doc encourages bypassing the ordering (even as a “temporary shortcut”), it’s wrong.

---

## 🔗 Quick links
- 🧭 Repo overview: **[`../README.md`](../README.md)**
- 📦 Data + metadata boundary: **[`../data/README.md`](../data/README.md)**
- 🧪 MCP (methods + receipts): **[`../mcp/README.md`](../mcp/README.md)** *(if present)*
- 🧩 Executable code boundary: **[`../src/README.md`](../src/README.md)** *(if present)*
- 🧾 Pipelines boundary: **[`../src/pipelines/README.md`](../src/pipelines/README.md)** *(if present)*
- 🧪 Tests boundary: **[`../tests/README.md`](../tests/README.md)** *(if present)*
- 📓 Notebooks boundary: **[`../notebooks/README.md`](../notebooks/README.md)** *(if present)*
- 📐 Schemas registry: **[`../schemas/README.md`](../schemas/README.md)** *(if present)*
- 🌐 Web UI boundary: **[`../web/README.md`](../web/README.md)** *(if present)*
- 🤝 CI/CD + templates: **[`../.github/README.md`](../.github/README.md)** *(if present)*

---

## 🧭 Quick navigation
- [📘 Overview](#-overview)
- [🧾 Doc metadata](#-doc-metadata)
- [🧠 Core invariants](#-core-invariants)
- [📖 Glossary](#-glossary-kfm-terms-used-in-docs)
- [🗂️ What goes in `docs/`](#️-what-goes-in-docs)
- [🧱 Directory layout](#-directory-layout)
- [🏁 Golden paths](#-golden-paths-most-common-doc-workflows)
- [✅ Doc quality gates](#-doc-quality-gates-definition-of-done)
- [🧾 Evidence, citations, and provenance pointers](#-evidence-citations-and-provenance-pointers)
- [📚 Story Nodes and Focus Mode rules](#-story-nodes-and-focus-mode-rules)
- [🔒 Security, sovereignty, and sensitive info](#-security-sovereignty-and-sensitive-info)
- [🧪 Modeling and simulation documentation](#-modeling-and-simulation-documentation)
- [⚙️ Scaling and data management documentation](#️-scaling-and-data-management-documentation)
- [🎨 Visualization and UX documentation](#-visualization-and-ux-documentation)
- [📚 Project reference library influence map](#-project-reference-library-influence-map)
- [🕰️ Version history](#️-version-history)

---

## 🧾 Doc metadata

| Field | Value |
|---|---|
| Doc | `docs/README.md` |
| Status | Active ✅ |
| Last updated | **2026-01-11** |
| Audience | Contributors writing standards, runbooks, story nodes, ADRs, and governance policies |
| Prime directive | If it changes what people *believe* about the map/story/data, it must be **reviewable + citable + reversible** |
| Repo posture | **Evidence-first** + **Contract-first** + **Sovereignty-aware** |

---

## 📘 Overview

### ✅ Purpose
`docs/` exists so KFM remains:
- **understandable** (clear architecture + vocabulary)
- **governable** (policy and review gates are explicit)
- **auditable** (why a decision happened, and when)
- **evidence-first** (claims point to cataloged evidence)
- **humane** (transparent impacts, consent, dignity, and accountability)
- **change-friendly** (structured docs that evolve with requirements instead of becoming fossilized)

### 🚫 What `docs/` is not
- not a dumping ground for generated outputs *(those belong under `data/**` and catalogs)*
- not a substitute for contracts *(schemas and API contracts live under `schemas/**` and `src/server/**`)*
- not a place for secrets, tokens, credentials, internal hostnames, or private URLs 🚫

---

## 🧠 Core invariants

> [!IMPORTANT]
> **Docs are part of the system boundary.**  
> When a subsystem changes, docs should change **in the same PR** whenever feasible. Docs are “shipped,” not “updated later.”

```mermaid
flowchart LR
  A[🧪 ETL Pipelines] --> B[🗂️ STAC/DCAT/PROV Catalogs]
  B --> C[🕸️ Graph]
  C --> D[🛡️ APIs]
  D --> E[🖥️ UI]
  E --> F[📚 Story Nodes]
  F --> G[🎯 Focus Mode]
````

### ✅ Docs must reinforce these rules

* ✅ **Pipeline ordering is absolute:** no leapfrogging stages.
* ✅ **Evidence-first narrative:** no unsourced claims in Story Nodes or Focus Mode.
* ✅ **Contract-first changes:** schemas and API contracts are first-class; docs must link to them and respect versioning.
* ✅ **One canonical home per thing:** avoid duplicate “shadow docs”; archive deprecated docs instead of copy/pasting.
* ✅ **Sovereignty-aware behavior:** docs must not leak sensitive locations (including via screenshots, tiles, or “helpful examples”).
* ✅ **Deny-by-default mindset:** treat user-provided files and internet metadata as hostile inputs; recommend validation, not trust-by-assumption.

### ✅ Minimum validation intent (v13 discipline)

KFM’s documentation posture assumes (or aspires to) automated validation gates such as:

* **Markdown protocol checks** (YAML front-matter + required sections)
* **Link/reference validation** (no broken internal links or unresolved citations)
* **Schema validation** for structured artifacts referenced by docs (STAC/DCAT/PROV, Story Node metadata)
* **Security/governance scans** (secrets, PII, sensitive location leakage, classification downgrades)

> [!NOTE]
> If CI isn’t fully wired yet, treat these as *required local checks* for doc changes that influence decisions or public meaning.

---

## 📖 Glossary (KFM terms used in docs)

**Catalog artifacts (STAC/DCAT/PROV)**
Machine-readable metadata + lineage that makes datasets *discoverable, traceable, and governable*.

**Contract artifacts**
Schemas and API contracts that define what the system accepts/serves (e.g., JSON Schemas in `schemas/`, API contracts under `src/server/`).

**Evidence artifacts**
Any derived output that can influence decisions (models, simulations, OCR corpora, derived rasters). Evidence artifacts must live in `data/processed/**` and be cataloged + provenance-linked.

**Story Node**
A governed narrative unit that is machine-ingestible and evidence-linked. It references evidence (catalog IDs) and graph entities (stable IDs) and separates fact from interpretation.

**Focus Mode**
The trust-preserving reading context where users experience story + map + timeline together. Focus Mode hard-gates provenance and sensitivity: *no new narrative without sources; no data without provenance; no sensitive location leaks.*

---

## 🗂️ What goes in `docs/`

KFM expects `docs/` to be organized by **governed intent** (not by author preference).

### ✅ Belongs here

* 🧱 **Architecture**: designs, diagrams, ADRs, blueprints (`docs/architecture/`)
* 📏 **Standards**: profiles + conventions (STAC/DCAT/PROV profiles, ontology rules, naming, CRS/unit rules) (`docs/standards/`)
* 🔐 **Security**: threat models, incident response, secure ingestion guidance (`docs/security/`)
* 🧭 **Governance**: FAIR/CARE/sovereignty policy, review gates, ethics, redaction rules (`docs/governance/`)
* 🧰 **Templates**: universal doc, ADR, Story Node, API contract extension (`docs/templates/`)
* 🧑‍🔧 **Runbooks**: “how to operate / debug / recover” (`docs/runbooks/`)
* 📰 **Reports & Story Nodes**: curated narrative content, with draft vs published separation (`docs/reports/story_nodes/`)
* 🗺️ **Domain modules**: per-domain documentation (sources, caveats, risks, ETL expectations) (`docs/data/<domain>/`)
* 📚 **Reference library**: books/papers that influence standards and decisions (`docs/library/` or equivalent)

### 🚫 Does not belong here

* generated dataset outputs → `data/**`
* executable code → `src/**`
* schema definitions → `schemas/**` *(docs explain; schemas enforce)*
* private credentials / internal endpoints → nowhere in git 🚫

---

## 🧱 Directory layout

### 🧭 Expected shape (v13-aligned)

> [!NOTE]
> Not all repos have every file yet. This is the **target** that the v13 doc protocol assumes.

```text
📁 docs/
├── 📄 README.md                          # you are here ✅
├── 📘 MASTER_GUIDE_v13.md                # canonical system map (must match front-matter)
│
├── 🧱 architecture/
│   ├── 📄 README.md
│   ├── 📄 ADR/                           # Architecture Decision Records
│   ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md   # v13 blueprint (draft/active)
│   ├── 📄 KFM_NEXT_STAGES_BLUEPRINT.md    # roadmap beyond v13
│   ├── 📄 KFM_VISION_FULL_ARCHITECTURE.md # long-term system vision
│   └── 🗺️ diagrams/                      # mermaid / svg / drawio exports (no secrets)
│
├── 📏 standards/
│   ├── 📄 README.md
│   ├── 📄 KFM_STAC_PROFILE.md
│   ├── 📄 KFM_DCAT_PROFILE.md
│   ├── 📄 KFM_PROV_PROFILE.md
│   ├── 📄 KFM_MARKDOWN_WORK_PROTOCOL.md   # doc authoring conventions (front-matter, required sections)
│   └── 🕸️ ontology/                      # graph/ontology conventions + mapping rules
│
├── 🧭 governance/
│   ├── 📄 ROOT_GOVERNANCE.md              # what requires review, by whom, and why
│   ├── 📄 ETHICS.md
│   ├── 📄 SOVEREIGNTY.md
│   └── 📄 REVIEW_GATES.md                 # optional: explicit review triggers
│
├── 🔐 security/
│   ├── 📄 README.md
│   ├── 📄 threat-model.md
│   └── 📄 incident-response.md
│
├── 🧰 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__ADR.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
│
├── 🧑‍🔧 runbooks/
│   ├── 📄 README.md
│   ├── 📄 pipeline-ops.md
│   ├── 📄 graph-ops.md
│   ├── 📄 api-ops.md
│   └── 📄 ui-ops.md
│
├── 📰 reports/
│   └── 📚 story_nodes/
│       ├── 🧪 draft/
│       ├── ✅ published/
│       └── 🖼️ assets/                     # images/maps used by story nodes (no sensitive leaks)
│
├── 🗺️ data/
│   └── <domain>/
│       └── 📄 README.md                   # domain module (sources, caveats, ETL expectations)
│
├── 📚 library/                            # optional: curated reference pack (license-aware)
│
└── 🗃️ 99_archive/                         # deprecated docs retained for traceability
```

> [!TIP]
> If you can’t decide where a new doc goes:
> **Does it define behavior?** → `standards/` or `governance/`
> **Does it explain structure?** → `architecture/`
> **Does it teach action steps?** → `runbooks/`
> **Is it narrative evidence?** → `reports/story_nodes/`
> **Is it domain-specific context + caveats?** → `data/<domain>/`

---

## 🏁 Golden paths (most common doc workflows)

### 1) Add a new data domain (doc + evidence alignment) ✅

When you add a new domain, create:

* `docs/data/<domain>/README.md` *(scope, sources, licensing, sensitivity, known caveats)*
* links/pointers to the domain’s catalog artifacts *(STAC/DCAT/PROV paths or IDs)*
* updates to `docs/standards/` **only** if the domain introduces new conventions

**Rule:** the domain becomes “real” only after `data/processed/**` + catalogs + provenance exist.

### 2) Add an ADR (Architecture Decision Record) ✅

Use an ADR when you decide something that affects:

* pipeline ordering or evidence boundaries
* metadata/provenance standards
* ontology/graph model changes
* API boundary behavior (authZ, redaction, classification propagation)
* public-facing meaning (maps, metrics, interpretations)

ADR should include: **context → decision → alternatives → consequences → rollback plan**.

### 3) Add or change a standard (profiles + conventions) ✅

Standards are **normative**. They must:

* be explicit and testable
* link to the machine schema (in `schemas/`)
* define versioning rules and migration expectations
* clarify what breaks downstream (graph/API/UI/story)

### 4) Add a Story Node (governed narrative) ✅

Story Nodes are treated like data products:

* template-driven
* evidence-linked (catalog pointers)
* graph-aware (stable IDs)
* fact vs interpretation separated
* published only after review gates pass

### 5) Add/modify an API contract (contract-first) ✅

If you add or change an endpoint:

* update the contract first (OpenAPI/GraphQL + examples)
* document authZ/redaction/classification behavior
* update tests and release notes where applicable

---

## ✅ Doc quality gates (Definition of Done)

> [!CAUTION]
> Docs can break trust just as fast as broken code.
> **Uncited claims** and **ambiguous language** are defects.

### ✅ Minimum DoD (for any doc PR)

* [ ] correct folder placement (matches doc intent)
* [ ] YAML front-matter present and valid *(id/title/status/last_updated/owners at minimum)*
* [ ] clear audience + scope + non-goals
* [ ] glossary/definitions for new terms (or link to canonical glossary)
* [ ] evidence pointers for factual claims (prefer STAC/DCAT/PROV and stable IDs)
* [ ] explicit assumptions (especially modeling, projections, CRS, units)
* [ ] “safety review” note if content touches sensitive locations, identities, or sovereignty
* [ ] no secrets, tokens, internal URLs, or exposed system internals
* [ ] links work (relative links preferred)
* [ ] updated “Last updated” date (and version history when relevant)

### 🔍 Recommended automation checks for docs

* markdown lint + style checks (headings, lists, code fences)
* link checker (relative links + anchors)
* YAML front-matter validation + required-sections check
* mermaid render check
* “no secrets / no PII” scanners
* optional spell check (domain dictionary)

---

## 🧾 Evidence, citations, and provenance pointers

### ✅ Rule: cite with *system-native pointers*

Prefer citing:

1. **Catalog artifacts** (STAC Item/Collection, DCAT dataset, PROV bundle)
2. **Graph entity IDs** (stable node IDs)
3. **External sources** only if they are also referenced in catalogs or the project library

### ✅ Footnotes pattern (recommended)

```markdown
The 1870–1875 corridor shows increased settlement density.[^e1]

[^e1]: Evidence: DCAT `kfm.ks.historical.settlement_density`; STAC `kfm.ks.historical.settlement_density`; PROV `kfm.prov.etl_1875_...`
```

> [!TIP]
> If a reader can’t click from a claim → evidence → lineage, the doc is incomplete.

---

## 📚 Story Nodes and Focus Mode rules

Story Nodes turn narrative into a governed data product: machine-ingestible, evidence-linked, and graph-aware.

### ✅ Story Node requirements

* **Provenance for every claim** (citations to evidence)
* **Graph entity references** (stable IDs for people/places/events/docs)
* **Fact vs interpretation** separation (especially for AI-assisted narrative)
* **Draft vs published** separation (don’t mix)

### 🎯 Focus Mode hard gates (trust preservation)

* Only provenance-linked content can appear
* AI content must be **opt-in**, clearly labeled, and paired with uncertainty/confidence
* No sensitive location leaks (generalize/omit where required)
* No side-channel bypass of sovereignty/classification rules

> [!IMPORTANT]
> Focus Mode is where users *experience* KFM. If it’s not traceable there, it doesn’t belong there.

---

## 🔒 Security, sovereignty, and sensitive info

Docs are a security surface. Treat them as if they could become public.

### ✅ Required posture

* 🚫 no secrets, tokens, private endpoints, internal hostnames
* 🧭 sovereignty-aware: avoid exposing exact coordinates for sensitive sites
* 🧯 no “how to exploit” instructions or vulnerable configuration examples
* 🧾 do not paste raw sensitive data into docs — reference catalog IDs instead
* 🧊 use screenshots carefully: they can leak coordinates, filenames, user accounts, or private tiles

---

## 🧪 Modeling and simulation documentation

KFM treats models as decision-support, not truth generators. Documentation must:

* state assumptions clearly
* define objectives + constraints
* report uncertainty (not just point estimates)
* record parameters + seeds
* define verification/validation (V&V) checks
* document bias risks and failure modes when models touch human narratives

---

## ⚙️ Scaling and data management documentation

When documenting performance/scaling behavior:

* specify data sizes, partitions, and indexing assumptions
* document storage formats and query patterns
* document concurrency and operational risks (race conditions, idempotency)
* document database conventions and migration strategy

---

## 🎨 Visualization and UX documentation

Maps and UI are meaning-making machines. Docs should capture:

* symbology decisions and aggregation choices (and why)
* web performance constraints (payload budgets, progressive loading)
* tiling/LOD considerations for dense spatial data
* image compression rules for doc assets (avoid repo bloat; keep renders readable)

---

## 📚 Project reference library influence map

> [!NOTE]
> These project files inform how we write and review KFM documentation: governance, evidence, security, modeling rigor, scaling discipline, and visualization honesty.

<details>
<summary><strong>📦 Expand: Reference library → what it influences in <code>docs/</code></strong></summary>

### 🧭 Core KFM system + documentation protocols

| Project file                                                                                       | Primary lens              | How it upgrades `docs/` decisions                                                                                                        |
| -------------------------------------------------------------------------------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx`                        | 🧭 System blueprint       | Reinforces repo boundaries, pipeline ordering, governance posture, Story Nodes + Focus Mode constraints.                                 |
| `MARKDOWN_GUIDE_v13.md.gdoc`                                                                       | 🧾 v13 doc protocol       | Defines “evidence-first + contract-first,” required doc structure (front-matter/sections), doc layout targets, and CI gate expectations. |
| `Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx`                        | ✍️ Craft + maintenance    | Pushes living-doc practice (update docs with code changes), scannable structure, accessibility habits, and disciplined Markdown usage.   |
| `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`                 | 🏗️ Architecture          | Strengthens architecture docs and clarifies the end-to-end flow (ingest → catalogs → graph → API → UI → story).                          |
| `Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf`                     | 🧯 Reality check          | Keeps docs operational: explicit gaps, missing runbooks/templates, and areas where “paper governance” must become enforced practice.     |
| `Latest Ideas.docx`                                                                                | 🧪 Roadmap notes          | Encourages clear draft-vs-canonical separation; capture ideas without letting them masquerade as standards.                              |
| `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf`                           | 🔬 Method discipline      | Improves doc expectations around experiments, traceability, and reproducible reasoning (aligns with MCP).                                |
| `Foundational Templates and Glossary for Scientific Method _ Research _ Master Coder Protocol.pdf` | 🧾 Templates + glossary   | Encourages consistent templates, shared vocabulary, and structured reporting of assumptions/limits.                                      |
| `Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf`                | 🧭 Cross-domain synthesis | Improves domain documentation by requiring explicit cross-source triangulation and careful treatment of uncertainty across disciplines.  |
| `Flexible Software Design: Systems Development for Changing Requirements.pdf`                      | 🔁 Change-resilience      | Encourages docs that are modular, versioned, and migration-aware (avoid brittle “one-off” rules).                                        |
| `Patterns, Algorithms, and Fractals_ A Cross-Disciplinary Technical Reference.pdf`                 | 🧠 Patterns               | Promotes documenting reusable patterns and anti-patterns (especially for complex spatial/temporal phenomena).                            |
| `Understanding Machine Learning: From Theory to Algorithms.pdf`                                    | 🤖 ML rigor               | Raises the bar for ML documentation: assumptions, generalization risks, validation discipline, and avoiding over-claiming.               |

### 🛰️ Geospatial, EO/RS, cartography, and web mapping

| Project file                                                                            | Primary lens          | How it upgrades `docs/` decisions                                                                   |
| --------------------------------------------------------------------------------------- | --------------------- | --------------------------------------------------------------------------------------------------- |
| `python-geospatial-analysis-cookbook.pdf` *(and any KFM-labeled variants)*              | 🗺️ GIS engineering   | Promotes CRS/unit hygiene, IO discipline, PostGIS patterns, and testable geoprocessing conventions. |
| `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` | 🛰️ EO workflows      | Informs RS domain docs: exports, time-series, and derived raster governance.                        |
| `making-maps-a-visual-guide-to-map-design-for-gis.pdf`                                  | 🎨 Cartography ethics | Forces documentation of symbology/aggregation as “meaning decisions,” not just styling.             |
| `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`                | 📱 Field constraints  | Drives doc guidance for offline/low-bandwidth UX constraints and upstream asset preparation.        |
| `responsive-web-design-with-html5-and-css3.pdf`                                         | 🌐 Web reality        | Encourages realistic device constraints, progressive loading, and accessible UI documentation.      |
| `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`            | 🧊 3D constraints     | Promotes documenting coordinate conventions, LOD/tiling rules, and GPU-friendly asset prep.         |
| `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`                                | 🖼️ Media hygiene     | Sets expectations for doc assets: compression, thumbnails, and avoiding repo bloat.                 |

### 📊 Statistics, modeling, simulation, and inference hygiene

| Project file                                                               | Primary lens       | How it upgrades `docs/` decisions                                                                 |
| -------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------- |
| `Understanding Statistics & Experimental Design.pdf`                       | 📊 Rigor           | Strengthens claims: confounders, bias, experimental design, and uncertainty framing.              |
| `graphical-data-analysis-with-r.pdf`                                       | 📉 EDA instincts   | Encourages pre-publication sanity checks, visual diagnostics, and surfacing anomalies.            |
| `regression-analysis-with-python.pdf`                                      | 📈 Baselines       | Normalizes reproducible modeling writeups: diagnostics, leakage checks, assumptions.              |
| `Regression analysis using Python - slides-linear-regression.pdf`          | 📈 Quick checks    | Reinforces what must be documented for regressions (residuals, scaling, assumptions).             |
| `think-bayes-bayesian-statistics-in-python.pdf`                            | 🎲 Uncertainty     | Promotes explicit priors, posterior uncertainty reporting, and calibrated decisions.              |
| `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` | 🧪 V&V discipline  | Elevates simulation docs with verification/validation, sensitivity analysis, and UQ expectations. |
| `Generalized Topology Optimization for Structural Design.pdf`              | 🧮 Optimization    | Improves optimization run documentation: objectives, constraints, reproducibility, audit trails.  |
| `Spectral Geometry of Graphs.pdf`                                          | 🕸️ Graph thinking | Encourages careful interpretation of graph metrics (signal vs fact) and provenance expectations.  |

### 🗄️ Data systems, scaling, and interoperability

| Project file                                                               | Primary lens             | How it upgrades `docs/` decisions                                                                      |
| -------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------ |
| `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` | 🐘 Data store discipline | Strengthens database runbooks: schema discipline, indexing, migrations, operational conventions.       |
| `Scalable Data Management for Future Hardware.pdf`                         | ⚙️ Performance           | Promotes documentation that captures partitions/locality, concurrency assumptions, and scaling risks.  |
| `Data Spaces.pdf`                                                          | 🔗 Interop               | Reinforces metadata-as-interface mindset: stable IDs, provenance, and pointer-over-payload discipline. |

### 🤖 AI governance + human-centered practice + security mindset

| Project file                                                                                             | Primary lens       | How it upgrades `docs/` decisions                                                                      |
| -------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------ |
| `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` | 🤖 Practical ML    | Encourages documenting training/eval artifacts, reproducibility, and model usage constraints.          |
| `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`      | ⚖️ AI governance   | Strengthens labeling of AI-assisted outputs, provenance expectations, and restraint under uncertainty. |
| `Introduction to Digital Humanism.pdf`                                                                   | ❤️ Human impact    | Improves transparency/accountability language and keeps humans in control of meaning-making.           |
| `Principles of Biological Autonomy - book_9780262381833.pdf`                                             | 🧠 Systems         | Encourages feedback-loop awareness and resilience thinking in governance/architecture docs.            |
| `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`                                 | 🧯 Threat modeling | Improves defensive documentation: least privilege, incident thinking, safe operational posture.        |
| `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`                      | 🛡️ Hostile inputs | Reinforces secure-ingestion posture and parser skepticism (without teaching exploitation).             |
| `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`                      | 🧵 Concurrency     | Encourages docs that warn about race conditions and enforce idempotent operational patterns.           |

### 📚 Programming reference shelves (supporting craft across the stack)

| Project file                | Lens                        | How it upgrades `docs/` decisions                                                    |
| --------------------------- | --------------------------- | ------------------------------------------------------------------------------------ |
| `A programming Books.pdf`   | 🧰 Polyglot craft           | Broad reference support for maintainable examples and tooling clarity.               |
| `B-C programming Books.pdf` | 🧰 Shell + systems          | Encourages safe scripting patterns and reproducible command surfaces in runbooks.    |
| `D-E programming Books.pdf` | 🧰 Engineering fundamentals | Supports consistent debugging, environments, and cross-stack documentation patterns. |
| `F-H programming Books.pdf` | 🧰 Tooling literacy         | Helps keep operational/runbook guidance grounded and practical.                      |
| `I-L programming Books.pdf` | 🧰 Implementation detail    | Reinforces disciplined code examples and configuration hygiene.                      |
| `M-N programming Books.pdf` | 🧰 Systems + networking     | Supports documenting reliability, failure modes, and interfaces.                     |
| `O-R programming Books.pdf` | 🧰 Breadth                  | Reinforces broader tooling awareness and documentation patterns.                     |
| `S-T programming Books.pdf` | 🧰 Testing + tooling        | Encourages documenting verification methods and test strategy explicitly.            |
| `U-X programming Books.pdf` | 🧰 Breadth                  | Supports documentation for less-common tools and edge-case workflows.                |

</details>

---

## 🕰️ Version history

| Version | Date       | Summary of changes                                                                                                                                                                                                                                                                                                                                                   | Author          |
| ------: | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
|  v1.1.0 | 2026-01-11 | Added YAML front‑matter; aligned directory layout + templates to v13 doc protocol; clarified catalog/contract/evidence terms; strengthened Focus Mode hard gates; expanded influence map to include all known project reference files (including v13 markdown protocol + design audit + scientific method/MCP template pack + software design/ML theory references). | KFM Engineering |
|  v1.0.0 | 2026-01-09 | Created canonical `docs/README.md` defining governed documentation boundaries, directory layout, doc quality gates, evidence/citation norms, Story Node + Focus Mode rules, and reference-library influence mapping.                                                                                                                                                 | KFM Engineering |

```
