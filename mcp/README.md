<!--
📌 MCP is KFM’s canonical “methods + receipts” boundary (not a data store, not runtime code).
🗓️ Last updated: 2026-01-13
-->

# 🧪 MCP — Master Coder Protocol  
### *Methods, Controls & Processes* 🧾⚙️

![README](https://img.shields.io/badge/README-v1.4.0-8957e5)
![Docs-first](https://img.shields.io/badge/docs-documentation--first-blue)
![Contract-first](https://img.shields.io/badge/contracts-schema--first-1f6feb)
![Provenance-first](https://img.shields.io/badge/provenance-first-7b42f6)
![Reproducible](https://img.shields.io/badge/reproducible-audit--ready-success)
![Evidence](https://img.shields.io/badge/evidence-catalog--linked-informational)
![PROV](https://img.shields.io/badge/lineage-W3C%20PROV-7b42f6)
![Governance](https://img.shields.io/badge/governance-FAIR%2BCARE%20%2B%20Sovereignty-2ea043)
![Security](https://img.shields.io/badge/security-hostile--inputs%20%2B%20deny--by--default-red)
![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-orange)

> **TL;DR:** `mcp/` is KFM’s **methods + receipts** layer 📓🧠  
> It holds **protocols**, **run receipts**, **SOPs**, **model cards**, and **review artifacts**—so every result can be **re-run, reviewed, and trusted** ✅  
>
> **Naming note:** Some internal docs expand MCP as **Methods, Controls & Processes**.  
> In *this repo*, we keep the canonical expansion **Master Coder Protocol** ✅ (same intent, same discipline).

> [!IMPORTANT]
> In this repo, **MCP = Master Coder Protocol** ✅  
> **MCP ≠ Model Context Protocol** 🚫 *(not what we mean here)*  
> Keep this distinction consistent in docs, PRs, issues, and commit messages.

---

## 🔗 Quick links
- 🧭 Repo overview: **[`../README.md`](../README.md)**
- 🧬 Pipelines boundary (contract portal): **[`../pipelines/README.md`](../pipelines/README.md)** *(if present)*
- 🧰 Scripts boundary (automation): **[`../scripts/README.md`](../scripts/README.md)** *(if present)*
- 🧩 Executable source boundary: **[`../src/README.md`](../src/README.md)**
- 📦 Data + metadata boundary: **[`../data/README.md`](../data/README.md)**
- 🧪 Notebooks boundary (lab bench): **[`../notebooks/README.md`](../notebooks/README.md)** *(if present)*
- 🧰 Validators & tooling: **[`../tools/README.md`](../tools/README.md)** *(if present)*
- ✅ Tests & CI gates: **[`../tests/README.md`](../tests/README.md)** *(if present)*
- 🤝 CI/CD & policies: **[`../.github/`](../.github/)** *(workflows, security policy, automation)*

---

## ⚡ Quick Nav
- [🧾 Doc metadata](#doc-metadata)
- [🧭 What MCP is](#what-mcp-is)
- [🧷 Repo invariants](#repo-invariants)
- [🧱 MCP artifacts](#mcp-artifacts-types-ids-and-immutability)
- [🚦 Non‑negotiables](#non-negotiables)
- [🏁 Quick Start](#quick-start)
- [🗂️ Directory layout](#directory-layout)
- [🔁 The MCP workflow loop](#the-mcp-workflow-loop)
- [🚥 Detect → Validate → Promote](#detect--validate--promote)
- [🧾 Front matter + schemas](#front-matter--schemas-machine-readable-mcp)
- [✅ Definition of done](#definition-of-done)
- [📦 Required artifacts](#required-artifacts)
- [🧪 Experiment reports](#experiment-reports)
- [🏃 Run receipts](#run-receipts)
- [📈 Performance & scalability experiments](#performance--scalability-experiments)
- [🧰 SOPs](#sops)
- [🧠 Model cards](#model-cards)
- [📓 Notebooks](#notebooks)
- [🧭 Traceability matrix](#traceability-matrix)
- [🧯 Bad evidence protocol](#bad-evidence-protocol)
- [🔗 MCP ↔ KFM evidence pipeline](#mcp--kfm-evidence-pipeline)
- [🧩 Domain checklists](#domain-checklists)
- [🔐 Safety, privacy, licensing](#safety-privacy-licensing)
- [🛡️ Threat model & hostile inputs](#threat-model--hostile-inputs)
- [✅ QA, audits, and CI hooks](#qa-audits-and-ci-hooks)
- [🤝 PR / review checklist](#pr--review-checklist)
- [📚 Project reference library influence map](#project-reference-library-influence-map)
- [🧾 Reference library index](#reference-library-index)
- [🕰️ Version history](#version-history)

---

## 🧾 Doc metadata

| Field | Value |
|---|---|
| Doc | `mcp/README.md` |
| Status | Active ✅ |
| Last updated | **2026-01-13** |
| Audience | Contributors writing experiments, running jobs, training models, shipping evidence artifacts |
| Prime directive | If it changes “spatial truth,” it must be **traceable + reproducible + reviewable** |
| KFM canon | **ETL → Catalogs (STAC/DCAT/PROV) → Graph → APIs → UI → Story Nodes → Focus Mode** |
| Backbone docs | KFM architecture + evidence doctrine + doc standards (see influence map) |

---

## 🧭 What MCP is

### ✅ MCP is…
A **governed method layer** that turns “we tried something” into **auditable science**:

- 🧪 **Protocols** (what we intended to do + why)
- 🏃 **Receipts** (what we actually ran + how)
- 🧰 **SOPs** (repeatable procedures for risky/repeated work)
- 🧠 **Model cards** (responsible AI/ML usage)
- 👀 **Review artifacts** (what was checked, by whom, and what failed)
- 🧭 **Traceability** (decision ↔ evidence ↔ catalogs ↔ provenance)

### 🚫 MCP is not…
- ❌ A data lake (that’s `data/`)
- ❌ A code dump (that’s `src/` and `web/`)
- ❌ A place for large outputs (store in `data/processed/**` + catalogs)
- ❌ A place for “unsourced narrative” (that belongs in Story Nodes with explicit evidence links)

> [!TIP]
> MCP exists to make “results” **explainable and replayable**—not merely impressive. 🧾✅

---

## 🧷 Repo invariants

These are the “you can build anything, but not *like that*” constraints. They come from KFM’s evidence doctrine and the v13 repo-level guide.

### 🧱 Invariant 1 — Pipeline ordering is absolute
**ETL → Catalogs (STAC/DCAT/PROV) → Graph → APIs → UI → Story Nodes → Focus Mode**  
No skipping steps. No “temporary UI demo” without catalogs + lineage.  [oai_citation:0‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 🧬 Invariant 2 — Provenance-first publishing
Anything “published” (meaning: referenced by graph, APIs, UI, Story Nodes, or Focus Mode) must have:
- a **catalog record** (STAC/DCAT) 🗂️  
- a **PROV lineage record** 🧬  
…**before** it is used downstream.  [oai_citation:2‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

### 🧾 Invariant 3 — Contracts are first-class
Schemas, profiles, and data contracts are not “nice-to-have.” They are the interface.  
If the artifact can’t validate, it can’t ship.  [oai_citation:3‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 🔁 Invariant 4 — ETL must be deterministic + idempotent
If inputs + config are unchanged, reruns must be stable:
- same IDs, same hashes, same catalogs
- safe to rerun without double-writing or corrupting state  [oai_citation:5‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

### 🧾 Invariant 5 — Runs are fully logged + hash-addressable
Every decision-worthy run captures:
- input checksums/hashes
- output checksums/hashes
- config + environment snapshot
- commit hash and entrypoint  [oai_citation:6‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

### 🤖 Invariant 6 — Focus Mode is advisory-only
Focus Mode can **suggest**. It cannot “declare truth” unless it points to evidence artifacts + catalogs.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:8‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)

---

## 🧱 MCP artifacts (types, IDs, and immutability)

MCP stays reliable because artifacts are **typed**, **named**, and **treated correctly**.

| Artifact | Prefix / ID pattern | Where | Immutable? | Purpose |
|---|---|---|---:|---|
| 🧪 Experiment protocol | `EXP-YYYY-MM-DD-<slug>` | `mcp/experiments/` | ⚠️ *Mutable while `draft`* | Pre-register intent, assumptions, and validation plan |
| 🏃 Run receipt | `RUN-YYYY-MM-DD-<slug>/` | `mcp/runs/` | ✅ **Yes** | What was executed + how to reproduce |
| 📈 Benchmark / perf run *(optional)* | `RUN-...` with `run_type: benchmark` | `mcp/runs/` | ✅ **Yes** | Performance experiments with workload + resource receipts |
| 🧰 SOP | `SOP-<topic>-v<semver>` | `mcp/sops/` | ✅ *Versioned* | Repeatable procedures (risky or frequent tasks) |
| 🧠 Model card | `MODEL-<name>-v<semver>` | `mcp/model_cards/` | ✅ *Versioned* | Intended use, limits, datasets, governance for ML/AI |
| 👀 Review note | `REV-YYYY-MM-DD-<slug>.md` | `mcp/reviews/` *(recommended)* | ✅ **Yes** | Independent reproduction and governance sign-off |
| 🧭 Traceability | `TRACEABILITY.md` *(or `TRACE-*.md`)* | `mcp/traceability/` | ✅ *Append-only mindset* | Decision/feature → EXP/RUN → evidence + catalogs |
| 🧯 Incident / anomaly | `INC-YYYY-MM-DD-<slug>.md` *(optional)* | `mcp/incidents/` *(optional)* | ✅ **Yes** | When something shipped wrong: what happened + fix + new gates |

> [!IMPORTANT]
> **Run receipts are immutable.**  
> If anything changes (inputs, params, code, environment), create a **new** run folder. ✅

---

## 🚦 Non‑negotiables

These rules keep KFM **scientific**, **auditable**, and **governed**:

1) **Evidence lives in `data/` — not in `mcp/`.** 📦  
   - `mcp/` = methods, decisions, receipts, checklists  
   - `data/processed/...` = outputs (**and they must be cataloged**)

2) **Contract-first by default.** 🧾🧱  
   If you publish an artifact, you must also publish the contract it conforms to (schema/profile/version).  [oai_citation:9‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

3) **Provenance-first publishing.** 🧬  
   If it’s referenced by graph/APIs/UI/Story/Focus, it must have STAC/DCAT + PROV before use.  [oai_citation:10‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

4) **Protocol before run (when it matters).** 🧾➡️🏃  
   If results could influence product decisions, public narratives, pipelines, or models: write an **EXP** first.

5) **No “magic results.”** 🪄🚫  
   If you can’t reproduce it using:
   - a commit hash
   - an environment snapshot
   - a config
   - linked inputs/outputs (**catalog IDs**)
   - input/output hashes  
   …then it’s not “done.”  [oai_citation:11‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

6) **Immutable receipts.** 🧾  
   Don’t edit a run receipt to “fix history.”  
   Make a **new** run folder and link it.

7) **Label AI involvement.** 🤖  
   Any AI-assisted outputs must be labeled and provenance-linked.  
   Focus Mode remains **advisory-only** and must be evidence-backed.  [oai_citation:12‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  [oai_citation:13‡Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf](file-service://file-Mu6zixTqF9Lubf5QMjepRg)

8) **KFM pipeline order is sacred.** 🧱  
   **ETL → Catalogs (STAC/DCAT/PROV) → Graph → APIs → UI → Story Nodes → Focus Mode**  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:15‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

9) **No privacy / sensitivity downgrade.** 🔒  
   Outputs cannot be less restricted than inputs without an explicit, reviewed redaction step.

10) **Licensing isn’t optional.** 🧾⚖️  
   Every dataset / artifact must carry license + attribution requirements through catalogs and narratives.

11) **Stable IDs are a correctness feature.** 🏷️  
   IDs should be *invariant* across reruns when inputs haven’t changed—treat IDs like API contracts.  [oai_citation:16‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)

> [!TIP]
> Motto: **“If I can’t reproduce it in 30 minutes, it’s not complete.”** ⏱️✅

---

## 🏁 Quick Start

### 1) Create an experiment report 🧪
Add:
- `mcp/experiments/EXP-YYYY-MM-DD-<slug>.md`

### 2) Create a run receipt 🏃
Add:
- `mcp/runs/RUN-YYYY-MM-DD-<slug>/`
  - config, env snapshot, logs, metrics, and `MANIFEST.md`

### 3) Store evidence outputs in the governed data layer 📦
Put evidence artifacts in:
- `data/processed/...` ✅  
Then publish metadata + lineage:
- `data/stac/**` + `data/catalog/dcat/**` + `data/prov/**` 🗂️🧬

### 4) Link it to decisions 🧭
Update traceability (recommended):
- `mcp/traceability/TRACEABILITY.md`

> [!IMPORTANT]
> `mcp/` should stay **lightweight** and human-readable.  
> Large artifacts go to `data/processed/` (or object storage) and get catalog records.

---

## 🗂️ Directory layout

```text
📁 mcp/
├── 📄 README.md                 # you are here 👋
├── 📁 experiments/              # human-readable experiment protocols 🧪🧾
├── 📁 runs/                     # immutable run receipts (configs, env, logs, metrics) 🏃🧾
├── 📁 sops/                     # Standard Operating Procedures (repeatable tasks) 🧰
├── 📁 model_cards/              # model cards for any ML/AI used or trained 🧠
├── 📁 notebooks/                # tidy, reproducible notebooks 📓
├── 📁 traceability/             # decision ↔ evidence mapping 🧭 (recommended)
├── 📁 reviews/                  # peer reproduction notes / governance sign-offs 👀 (recommended)
├── 📁 incidents/                # post-mortems / anomaly reports 🧯 (optional)
└── 📁 templates/                # local templates 🧩 (or use docs/templates/)
```

> [!NOTE]
> Repo implementations vary. If `traceability/` or `reviews/` doesn’t exist yet, consider adding them—  
> the KFM design audit calls out traceability + modular documentation as a core MCP promise.  [oai_citation:17‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH)

---

## 🔁 The MCP workflow loop

KFM work is **question → protocol → run → evidence → report → review → iterate**:

```mermaid
flowchart LR
  Q["❓ Question"] --> P["🧾 Protocol (EXP)"]
  P --> R["🏃 Run (RUN receipt)"]
  R --> E["📦 Evidence (data/processed + catalogs)"]
  E --> S["🧪 Summary report (interpretation + limits)"]
  S --> V["👀 Review (repro + governance)"]
  V --> Q
```

### 🔬 Scientific method alignment (what we document)
MCP is a practical “scientific method adapter” for software + data work. (Also: simulation V&V, uncertainty, and bias discipline.)  [oai_citation:18‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:20‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

- **Observation / question** → Why are we doing this?
- **Hypothesis** → What do we expect to see?
- **Method** → Exact procedure + configuration
- **Experiment** → The run receipt (what happened)
- **Analysis** → Metrics, plots, error checks
- **Conclusion** → What we learned (with limits)
- **Iteration** → Next experiment / pipeline change

---

## 🚥 Detect → Validate → Promote

A lot of KFM risk comes from “half-published” artifacts. MCP encourages a controlled publishing rhythm:

1) **Detect** 🕵️  
   Identify new inputs / changes (sources updated, new scans, schema drift, new tiles).

2) **Validate** ✅  
   Run fast gates:
   - schema & bounds checks (**contracts**)  [oai_citation:21‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
   - catalog validity (STAC/DCAT)
   - PROV lineage presence & link integrity (inputs/outputs resolve)
   - governance propagation (no downgrade)
   - security scans (secrets / sensitive patterns)

3) **Promote** 🚀  
   Only after validation:
   - write evidence to `data/processed/**`
   - write STAC/DCAT/PROV (provenance-first)  [oai_citation:22‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
   - (optionally) export graph ingest bundles
   - add MCP RUN receipt + traceability update

> [!TIP]
> Treat “promotion” like a release: **atomic publish or nothing.** 🧾✅

---

## 🧾 Front matter + schemas (machine-readable MCP)

MCP documents are **human-first**, but they should also be **machine-readable** for dashboards, validation, and CI gates.

### ✅ Front matter conventions (recommended)
All MCP artifacts should start with YAML front matter (or equivalent), including:

- stable ID (`EXP-...`, `RUN-...`, `SOP-...`, `MODEL-...`)
- date
- owner
- status
- tags
- AI involvement (if applicable)
- links to evidence (catalog IDs or paths)
- contracts + lineage pointers (STAC/DCAT/PROV)

This aligns with KFM’s doc standards and contract-first guidance.  [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:24‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

### ⭐ Recommended “governed doc” fields (additive)
From our internal markdown/documentation standards, these extra fields improve audits and automation:  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

- `doc_uuid` (stable UUID for the document)
- `commit_sha` (when doc corresponds to a code/data release)
- `doc_integrity_checksum` (optional: hash of the doc body for audit trails)
- `care_label` (governance label for sensitivity/sovereignty expectations)
- `related_docs` / `mcp_refs` (explicit cross-links)
- `data_sources` (STAC/DCAT IDs, not just filesystem paths)

### 🔎 Minimal example (recommended baseline)
```yaml
---
id: EXP-2026-01-13-example
doc_uuid: "b0b6d0a5-4f4e-4e5b-9f25-1a2b1b9b0a7e"
title: "Example MCP artifact"
date: 2026-01-13
owner: "@github-handle"
status: draft
repro_level: L1
risk_level: medium
care_label: restricted
ai_used: false

contracts:
  - "schemas/mcp/exp.schema.json"
catalog_pointers:
  stac: ["stac://collection-id", "stac://item-id"]
  dcat: ["data/catalog/dcat/dataset.jsonld"]
  prov: ["data/prov/PROV-2026-01-13-example.jsonld"]
---
```

> [!NOTE]
> If your repo includes schemas under `schemas/mcp/`, validate MCP front matter in CI (treat it like an API).  [oai_citation:26‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

---

## ✅ Definition of done

### ✅ MCP “done” means: reproducible + governed
For any EXP/RUN that influences production pipelines, APIs, UI layers, Story Nodes, or Focus Mode:

- [ ] Front-matter complete + consistent (IDs, dates, owner, status)
- [ ] Claims link to evidence inputs/outputs (**catalog pointers**)
- [ ] Contracts + lineage pointers present (STAC/DCAT/PROV)
- [ ] Validation steps are listed and repeatable
- [ ] Governance + FAIR/CARE + sovereignty considerations stated (when applicable)
- [ ] Another contributor can reproduce results without tribal knowledge

### 🧱 Reproducibility levels (recommended)
- **L0** 🟡: exploratory note (not decision-worthy)
- **L1** 🟠: reproducible by author (config + env captured)
- **L2** 🟢: reproducible by reviewer (independent re-run)
- **L3** 🏆: CI-backed / automated rerun (pipeline job + validators)

---

## 📦 Required artifacts

### ✅ “Real work” minimum bar
If an experiment influences decisions, pipelines, or published results, it must include:

- 🧪 **Experiment report** → `mcp/experiments/...`
- 🏃 **Run receipt** → `mcp/runs/...`
- 🔗 **Code pointer** → commit hash + entrypoint
- 🧱 **Environment snapshot** → Docker image digest **or** lockfile/requirements
- 🎲 **Seeds / determinism flags** (where applicable)
- 🔢 **Input/output hashes** (recommended for decision-relevant work)  [oai_citation:27‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- 📦 **Outputs stored as evidence** → `data/processed/...`
- 🗂️ **Catalog records** → STAC/DCAT
- 🧬 **Lineage** → PROV pointers (inputs + outputs)
- 👀 **Review notes** → reproduction sign-off for L2/L3 work (recommended)
- 🔐 **Policy checks evidence** → list which gates ran (recommended)
- 🧾 **(Optional) CI attestation** → if your repo signs artifacts / builds
- 🧷 **(Optional) DVC pointers** → for metric/version tracking workflows (if used)  [oai_citation:28‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

> [!WARNING]
> Avoid committing large binaries to `mcp/`.  
> If it’s an “output,” it probably belongs in `data/processed/` with catalogs + lineage.

---

## 🧪 Experiment reports

### 📛 Naming convention
Use one pattern consistently:

- `EXP-YYYY-MM-DD-<short-slug>.md`  
  Example: `EXP-2026-01-02-ocr-ner-baseline.md`

### 🏷️ Status values
- `draft` 📝 — in progress
- `complete` ✅ — reproducible; linked receipts + evidence
- `superseded` 🧯 — replaced by a newer experiment

### 🧾 Experiment template (copy/paste)

```md
---
id: EXP-YYYY-MM-DD-<slug>
title: "<short, explicit title>"
date: YYYY-MM-DD
owner: "@github-handle"
status: draft | complete | superseded
repro_level: L0 | L1 | L2 | L3
risk_level: low | medium | high
ai_used: true | false
care_label: public | restricted | confidential   # recommended
supersedes: []          # optional: [EXP-...]
superseded_by: []       # optional: [EXP-...]
tags: [gis, ocr, nlp, stac, dcat, prov, graph, sim, stats, web, security]

contracts:              # recommended
  - "schemas/mcp/exp.schema.json"
---

# Objective / Question ❓
- What are we trying to learn or improve?

# Background / Prior Art 📚
- Links to prior experiments, issues, papers, notes, or domain docs.

# Hypothesis ✅/❌
- What do we expect and why?

# Variables & Controls 🎛️
- Key variables you’re changing.
- Controls / baselines.
- What stays fixed.

# Inputs (Evidence In) 🗃️
- Dataset IDs + STAC/DCAT pointers.
- Sampling rules, inclusion/exclusion, time range, bbox.
- Licensing + sensitivity notes (if applicable).

# Method / Protocol 🧾
- Step-by-step procedure.
- Parameters + configs (link to run receipt config).
- Tools + versions (OS/GPU/driver notes if relevant).

# Validation Plan ✅
- What fails fast?
- What warns?
- What “sanity checks” must pass?

# Run Receipt 🏃
- Code commit: `abcdef1`
- Entrypoint: `src/...` or notebook path
- Run folder: `mcp/runs/RUN-YYYY-MM-DD-.../`
- Seeds: `...`
- Determinism flags: `...`

# Outputs (Evidence Out) 📦
- Where outputs live (paths under `data/processed/...`)
- Catalog pointers:
  - STAC item(s): `...`
  - DCAT dataset: `...`
  - PROV bundle: `...`

# Results 📈
- Metrics, charts, qualitative examples (keep small).
- Add 1–3 “sanity check” examples.

# Uncertainty, Bias, and Validation 🔍
- What could be wrong?
- Checks performed (spot checks, CV, error bounds, leakage checks).
- Bias risks / perspective gaps (especially for historical corpora).

# Interpretation 🧠
- What do results mean for KFM decisions?

# Decision / Next Steps 🧭
- Adopt / iterate / abandon (and why).

# Reproducibility Checklist ✅
- [ ] Parameters & configs documented
- [ ] Code committed + hash recorded
- [ ] Environment captured (Docker/lockfile)
- [ ] Seeds recorded (if applicable)
- [ ] Inputs/outputs linked via STAC/DCAT/PROV
- [ ] Input/output hashes recorded (recommended)
- [ ] Reviewer can reproduce (for L2/L3)
```

> [!TIP]
> If you can’t write the “Uncertainty, Bias, and Validation” section honestly, the experiment isn’t finished. 🔍✅

---

## 🏃 Run receipts

Runs are the **receipt** for an experiment: what you ran, how you ran it, where outputs went, and what changed.

### 📛 Naming convention
- `RUN-YYYY-MM-DD-<slug>/`

### 📦 Suggested run folder contents
- `config/` 🧾 — YAML/JSON config used for the run
- `env/` 🧱 — `pip freeze`, lockfiles, Docker digest, OS info
- `logs/` 🪵 — structured logs (**redacted if needed**)
- `metrics/` 📈 — CSV/JSON metrics, evaluations
- `artifacts/` 🧩 — *small* artifacts (thumbnails, sample outputs)
- `MANIFEST.md` 🧾 — reproduction instructions + evidence links + checks performed
- `hashes/` 🔢 *(recommended)* — input/output checksums for audit-grade reruns

### 🧾 Minimal `MANIFEST.md` template (copy/paste)

```md
---
run_id: RUN-YYYY-MM-DD-<slug>
run_type: standard | benchmark | backfill | hotfix   # recommended
related_experiment: EXP-YYYY-MM-DD-<slug>
date: YYYY-MM-DD
owner: "@github-handle"
env: dev | staging | prod
care_label: public | restricted | confidential

code:
  commit: abcdef1
  entrypoint: "src/pipelines/..."
  args: ["--config", "config/run.yml"]
  dirty_worktree: false  # recommended

environment:
  docker_image: "ghcr.io/org/project:tag@sha256:..."     # preferred
  # or:
  requirements: "env/requirements.lock.txt"
  os: "..."
  cpu: "..."
  gpu: "..."  # optional

randomness:
  seeds: [123, 456]
  deterministic_flags: ["..."]

contracts:                 # contract-first
  - "schemas/<domain>/...schema.json"
  - "schemas/mcp/run.schema.json"

inputs:
  - catalog_ref: "stac://<collection_or_item_id>"
    sha256: "..."          # recommended
  - dcat: "data/catalog/dcat/<dataset>.jsonld"
  - prov: "data/prov/<prior-run>.jsonld"

outputs:
  - path: "data/processed/<domain>/<dataset>/..."
    sha256: "..."          # recommended
    stac_item: "data/stac/items/..."
    dcat: "data/catalog/dcat/..."
    prov: "data/prov/<run-id>.jsonld"

validation:
  - "contract validation: pass/fail"
  - "schema validation (STAC/DCAT/PROV): pass/fail"
  - "link checks: pass/fail"
  - "classification propagation: pass/fail"
  - "spot checks: ..."

policy_checks:               # optional, recommended
  - "secrets scan: pass/fail"
  - "sensitive patterns scan: pass/fail"
  - "sbom generated: yes/no"
  - "attestation present: yes/no"

notes: ""
---

# Summary 🧾
- What did this run do?

# Evidence outputs 📦
- Where outputs are stored (`data/processed/...`) + catalog IDs

# How to reproduce 🔁
1. Checkout commit: `abcdef1`
2. Restore environment: ...
3. Run: ...
4. Validate (contracts + catalogs + lineage): ...
```

> [!TIP]
> Treat run folders as **immutable receipts**.  
> New parameters → new run folder ✅

---

## 📈 Performance & scalability experiments

Some work isn’t “new evidence,” it’s “can we serve/process evidence safely at scale?”  
Performance work still needs receipts—because performance claims can change decisions and architecture.  [oai_citation:29‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf)  [oai_citation:30‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)

### ✅ When to treat a run as a benchmark
- new PostGIS index/migration affecting query latency 🐘  [oai_citation:31‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- tile generation tuning (COG params, overviews, compression) 🧊  [oai_citation:32‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)
- graph ingest optimizations / new analytics jobs 🕸️  [oai_citation:33‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf)
- stream/near-real-time pipelines (windowing, caching, batching) ⚙️  [oai_citation:34‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)

### 🧾 Benchmark add-ons (recommended in `MANIFEST.md`)
Add a `performance:` section:

```yaml
performance:
  workload:
    description: "API tile requests @ zoom 6–12 for 3 AOIs"
    concurrency: 25
    warm_cache: true
    duration_s: 600
  dataset:
    size_bytes: 123456789
    feature_count: 987654
  system:
    cpu_cores: 16
    ram_gb: 64
    storage: "nvme"
  results:
    p50_ms: 120
    p95_ms: 410
    p99_ms: 900
    throughput_rps: 85
  artifacts:
    - "metrics/latency_histogram.csv"
    - "logs/explain_analyze.txt"
```

> [!TIP]
> “Fast on my laptop” isn’t a result. Benchmark runs should state workload, cache conditions, and resources. 🧾✅

---

## 🧰 SOPs

SOPs turn “tribal knowledge” into a repeatable, reviewable procedure.  
Write an SOP whenever a task is repeated or risky: georeferencing, catalog publishing, redaction, OCR, tile generation, secure parsing, performance tuning, etc. 🧯

### SOP template (copy/paste)

```md
---
id: SOP-<topic>-v1.0.0
title: "<clear title>"
owner: "@github-handle"
last_updated: YYYY-MM-DD
risk_level: low | medium | high
care_label: public | restricted | confidential
---

# Purpose 🎯
What this SOP accomplishes and when to use it.

# Scope ✅
What’s included / excluded.

# Prerequisites 🧱
Accounts, tools, access, permissions.

# Tools & Versions 🧰
Software + versions.

# Procedure 🧭
1. Step...
2. Step...
3. Step...

# Verification ✅
How to confirm it worked (checks + expected outputs).

# Troubleshooting 🧯
Common failure modes + fixes.

# Audit Trail 🧾
Example PRs / runs / experiments that used this SOP.
```

### ⭐ High-value SOPs to add (starter set)
- `sops/georeference_map.md` 🗺️ (control points, RMS error, CRS discipline)  [oai_citation:35‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)
- `sops/build_cog_and_tiles.md` 🧊 (COG params, overviews, compression, thumbnails)  [oai_citation:36‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)
- `sops/ocr_pipeline.md` 🔎 (scan QA, language assumptions, error classes)
- `sops/publish_stac_dcat_prov.md` 🗂️🧬 (profiles, validation, link checks)  [oai_citation:37‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- `sops/catalog_qa_gate.md` ✅ (how to run CI-like catalog QA locally)
- `sops/postgis_import_index.md` 🐘 (schemas, indexes, vacuum/analyze, explain)  [oai_citation:38‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- `sops/redaction_and_sensitive_locations.md` 🔐 (coarsen/offset rules, approvals)  [oai_citation:39‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)
- `sops/detect_validate_promote.md` 🚥 (release discipline for evidence publishing)  [oai_citation:40‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- `sops/performance_benchmarking.md` 📈 (workloads, cache conditions, regression budgets)  [oai_citation:41‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf)
- `sops/secure_parsing_and_sandboxing.md` 🛡️ (hostile PDFs/images; deny-by-default)  [oai_citation:42‡Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf](file-service://file-Mu6zixTqF9Lubf5QMjepRg)  [oai_citation:43‡On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf](file-service://file-NtashtRjti9J1THyYXkhAv)  [oai_citation:44‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)
- `sops/streaming_windowing_and_replay.md` ⚙️ (windowing, watermarking, replay safety)  [oai_citation:45‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)
- `sops/3d_coordinate_conventions.md` 🧊 (units, handedness, LOD rules for WebGL/3D GIS)  [oai_citation:46‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd)  [oai_citation:47‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)
- `sops/ai_governance_and_raci.md` 🤝 (roles, accountability, labeling rules, escalation)  [oai_citation:48‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  [oai_citation:49‡Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf](file-service://file-Mu6zixTqF9Lubf5QMjepRg)
- `sops/rollback_and_prov_repair.md` 🧯 (how to revert + repair provenance safely)
- `sops/story_node_evidence_bundle.md` 📚 (evidence pack for narratives + Focus Mode)  [oai_citation:50‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

---

## 🧠 Model cards

Any ML/AI model used in KFM (trained or adopted) needs a model card:

- what it is
- what it was trained on / sourced from
- what it should be used for ✅
- what it must **not** be used for 🚫
- known limitations, bias risks, failure modes ⚠️
- provenance + licensing + governance labels 🧾🔒

This aligns with the repo’s “human-centered accountability” posture.  [oai_citation:51‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  [oai_citation:52‡Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf](file-service://file-Mu6zixTqF9Lubf5QMjepRg)

### Model card template (copy/paste)

```md
---
model_id: MODEL-<name>-v<semver>
owner: "@github-handle"
date: YYYY-MM-DD
ai_used: true
source:
  type: trained | third_party
  license: "..."
  reference: "paper/link/registry id"
datasets:
  - "stac://<collection_or_item_id>"
  - "dcat://<dataset_id>"
governance:
  care_label: public | restricted | confidential
  human_in_the_loop: required | recommended | optional
  redaction_required: yes | no
legal_and_policy:
  notes: ""   # when relevant (regulatory/ethical constraints)
---

# Model overview 🧠
- What problem does it solve?

# Intended use ✅
- Supported use-cases.

# Out-of-scope / prohibited use 🚫
- What it must not be used for.

# Training data 🗃️
- Datasets used (STAC/DCAT pointers), sampling, labeling notes.
- Known gaps / perspective bias notes.

# Evaluation 📈
- Metrics, test sets, qualitative examples.
- Calibration / uncertainty notes when applicable.

# Limitations & biases ⚠️
- Known failure modes, bias risks, uncertainty notes.

# Governance & safety 🔐
- Any redaction rules or sensitivity constraints.
- How outputs are labeled in UI / Focus Mode.

# Reproducibility 🧪
- Training code commit hash
- Environment / hardware notes
- Hyperparameters / config
- Seeds
- Artifact pointers (weights, charts) stored under `data/processed/...` with catalogs
```

> [!TIP]
> Use “learning theory” and “uncertainty reporting” concepts to keep claims honest—especially for generalization and out-of-distribution behavior.  [oai_citation:53‡U-X programming Books.pdf](file-service://file-3hYtSGHtHmb6wyTtavym6M)  [oai_citation:54‡Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf](file-service://file-GqygtUWf5Xyi3AjEaqEdQB)  [oai_citation:55‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)

---

## 📓 Notebooks

Notebooks are welcome—**but must be readable and reproducible**:

- Start with a markdown cell: **purpose + inputs + outputs**
- Keep outputs small *(no huge embedded blobs)*
- Prefer parameterized notebooks or export to scripts when it becomes “real”
- If a notebook produces evidence artifacts:
  - store outputs in `data/processed/...`
  - link them from an experiment report + run receipt

> [!CAUTION]
> Notebooks that silently write files without catalogs + provenance are **not shippable**.

---

## 🧭 Traceability matrix

Traceability is how MCP connects “work” to “why it matters”:

- ❓ Question / requirement  
- 🧪 EXP protocol  
- 🏃 RUN receipt  
- 📦 Evidence artifacts (+ STAC/DCAT/PROV)  
- 🕸️ Graph IDs (if applicable)  
- 🛡️ API endpoints (if applicable)  
- 📚 Story Node(s) / Focus Mode (if applicable)

### ✅ Recommended traceability table (copy/paste)

```md
| Decision / Feature | EXP | RUN | Evidence outputs (data/processed) | Catalog pointers (STAC/DCAT/PROV) | Reviewer repro | Notes |
|---|---|---|---|---|---|---|
| "OCR treaties baseline for Land Treaties domain" | EXP-2026-01-02-... | RUN-2026-01-02-... | data/processed/historical/land-treaties/ocr/... | STAC: ... / DCAT: ... / PROV: ... | @reviewer ✅ | error classes logged |
```

> [!TIP]
> If a Story Node makes a claim, traceability must point to the evidence artifacts that support it. 📚🧾

---

## 🧯 Bad evidence protocol

KFM must be resilient to “bad evidence” (messy scans, biased corpora, incomplete sensor data, uncertain geocoding).

When evidence is questionable, MCP requires **restraint**:

1) **Data pruning** ✂️  
   Exclude known-bad inputs (or flag them as “quarantined” until fixed).

2) **Inferential restraint** 🧠⬇️  
   Reduce the strength/scope of conclusions; report uncertainty explicitly.

3) **Executional restraint** 🛑  
   Limit downstream actions: don’t ship to UI/Story/Focus until reviewed, or serve only aggregated/redacted views.

### ✅ Minimum “bad evidence” documentation
- What’s wrong?
- How do we know?
- What we changed (or refused to change)
- What remains uncertain
- Who reviewed the restraint decision

---

## 🔗 MCP ↔ KFM evidence pipeline

KFM uses a strict evidence pipeline:

**ETL → Catalogs (STAC/DCAT/PROV) → Graph → APIs → UI → Story Nodes → Focus Mode**

So for MCP work:

- ✅ Protocols live here: `mcp/experiments/...`
- ✅ Receipts live here: `mcp/runs/...`
- ✅ Evidence artifacts live here: `data/processed/...`
- ✅ Evidence artifacts must be:
  - cataloged (STAC/DCAT) 🗂️
  - lineage-linked (PROV) 🧬
  - integrated through governed contracts (API boundary) 🔒  [oai_citation:56‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

```mermaid
flowchart LR
  EXP["🧪 EXP report"] --> RUN["🏃 RUN receipt"]
  RUN --> OUT["📦 data/processed outputs"]
  OUT --> CAT["🗂️ STAC/DCAT/PROV"]
  CAT --> GR["🕸️ Graph"]
  GR --> API["🛡️ APIs"]
  API --> UI["🗺️ UI / Story / Focus"]
```

---

## 🧩 Domain checklists

Use the checklist that matches your work:

### 🗺️ GIS / Remote Sensing
- [ ] CRS documented (EPSG + axis order)
- [ ] Georeferencing method + control points documented
- [ ] Fit error/RMS recorded (if applicable)
- [ ] Raster outputs are COGs / tiled (with parameters)
- [ ] Vector outputs validate (geometry validity, topology as needed)
- [ ] Index/derivation logic documented for EO products (band math, QA masks, temporal compositing)  [oai_citation:57‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)
- [ ] Symbology/aggregation choices documented if they change interpretation 🎨  [oai_citation:58‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Catalog pointers included (STAC/DCAT) + lineage (PROV) 🗂️🧬

### 🔎 OCR / NLP
- [ ] Input corpus + sampling documented
- [ ] Labeling rules / evaluation rubric included
- [ ] Precision/recall (or spot-check protocol) documented
- [ ] Failure classes logged (scan quality, fonts, ambiguity)
- [ ] Geoparsing uncertainty documented (ambiguous place names, gazetteer limits)

### 🕸️ Graph analytics
- [ ] Graph schema/ontology version noted
- [ ] Metrics treated as **signals**, not facts (avoid over-interpretation)
- [ ] Provenance links from derived relations to source evidence
- [ ] No orphan IDs / referential integrity checks pass ✅
- [ ] Spectral / structural metrics documented with interpretation caveats  [oai_citation:59‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf)

### 📊 Statistics / Inference
- [ ] Outcomes + units defined
- [ ] Assumptions checked (independence, distribution, etc.)  [oai_citation:60‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- [ ] Effect sizes + uncertainty reported (not just p-values)  [oai_citation:61‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- [ ] Regression diagnostics recorded when relevant (residuals, leverage/influence, multicollinearity)  [oai_citation:62‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:63‡Generalized Topology Optimization for Structural Design.pdf](file-service://file-PzydVyvSPdXWqYrXeFCNzj)
- [ ] Multiple comparisons handled (or explicitly scoped)
- [ ] Guardrails against optional stopping / publication bias documented 🧯  [oai_citation:64‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- [ ] Bayesian choices explicit when used (priors, posterior predictive checks) 🎲  [oai_citation:65‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)

### 🛰️ Modeling & Simulation
- [ ] Assumptions enumerated explicitly
- [ ] Verification & validation approach documented (V&V mindset)  [oai_citation:66‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Sensitivity analysis for key parameters  [oai_citation:67‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Uncertainty quantified or bounded  [oai_citation:68‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Results reported with uncertainty context (not single “truth” numbers)

### 🧮 Optimization workflows
- [ ] Objective function stated in plain language
- [ ] Constraints & feasibility checks defined
- [ ] Stopping criteria and convergence diagnostics recorded
- [ ] Sensitivity to hyperparameters explored
- [ ] Results accompanied by failure modes + interpretation limits  [oai_citation:69‡Generalized Topology Optimization for Structural Design.pdf](file-service://file-PzydVyvSPdXWqYrXeFCNzj)

### 🧊 3D GIS / WebGL / Spatial UX
- [ ] Coordinate conventions documented (units, axis order, handedness)  [oai_citation:70‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd)  [oai_citation:71‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)
- [ ] LOD strategy documented (tiling, mesh simplification, instancing)
- [ ] GPU budgets noted (texture sizes, draw calls, mobile constraints)  [oai_citation:72‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd)
- [ ] Any 3D storytelling claim points to evidence artifacts (no “pretty renders” without receipts)

### 🐘 Databases / PostGIS / Query systems
- [ ] Schema/migrations versioned + reversible
- [ ] Index strategy documented (and why)
- [ ] `EXPLAIN (ANALYZE, BUFFERS)` captured for key queries
- [ ] Vacuum/analyze expectations stated for benchmark runs
- [ ] Data access policies enforced (no sensitive downgrade)  [oai_citation:73‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  [oai_citation:74‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf)

### 🌐 Web UI / Visualization (when experiments affect front-end behavior)
- [ ] Payload budgets considered (tiles, vector sizes, images)  [oai_citation:75‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)  [oai_citation:76‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj)
- [ ] Offline/low-bandwidth considerations documented (if relevant) 📱  [oai_citation:77‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj)
- [ ] Accessibility and audit logging expectations noted ♿️🧾
- [ ] Focus/Story evidence bundle is explicit (no unsourced claims) 📚🧾

---

## 🔐 Safety, privacy, licensing

- 🚫 Don’t store secrets, tokens, keys, or sensitive PII in `mcp/`
- 🧽 Redact logs before committing if they contain identifiers, endpoints, or sensitive paths
- 🧊 Prefer immutable receipts: new run folder > editing old run folder
- 🧭 If superseded, mark as `superseded` and link the replacement
- 🗺️ Sensitive locations: if a dataset could expose culturally sensitive or personal location data:
  - coarsen/offset/omit coordinates
  - require explicit permission & review before publishing
  - propagate sensitivity tags through catalogs and UI
- ⚖️ Licensing must travel with evidence (and derived artifacts must honor upstream constraints)

> [!IMPORTANT]
> Licensing must travel with evidence. If you combine layers, the resulting artifact must still honor attribution and license constraints. ⚖️🧾

---

## 🛡️ Threat model & hostile inputs

KFM handles *hostile-by-default* artifacts: PDFs, images, archives, and scraped web content. Treat every input as potentially malicious—even when it “looks like a map.” 🧨

### ✅ Minimum defensive posture
- 🧷 **Deny-by-default parsing:** only allow expected MIME types and structures
- 🧪 **Sandbox execution:** run risky parsers in constrained environments (no network, least privilege)
- 🧊 **Decompression bomb awareness:** set limits for image decode, ZIP expansion, PDF object counts
- 🔎 **Metadata stripping:** ensure thumbnails/exports don’t leak sensitive EXIF/paths
- 🧾 **Log redaction:** never commit secrets/URLs/tokens in logs
- ✅ **Dependency hygiene:** SBOMs, pinned versions, security scanning

Security references that inform this posture:  [oai_citation:78‡Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf](file-service://file-Mu6zixTqF9Lubf5QMjepRg)  [oai_citation:79‡On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf](file-service://file-NtashtRjti9J1THyYXkhAv)  [oai_citation:80‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)  [oai_citation:81‡concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf](file-service://file-Y45SvXbmLoZL1MNmrcyqz6)

> [!TIP]
> If the pipeline consumes untrusted PDFs/images, a security SOP is not optional—it’s part of “reproducible science.” 🧾🛡️

---

## ✅ QA, audits, and CI hooks

### CI intent (minimum bar)
- 🧹 lint + formatting (docs + code)
- ✅ unit tests (where applicable)
- 🧾 contract validation (schemas/profiles)  [oai_citation:82‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- 🗂️ schema validation (STAC/DCAT/PROV)
- 🔗 link checks (assets exist; IDs resolve)
- 🔐 security scans (secrets; sensitive patterns; dependency risk)
- 🧷 governance checks (classification propagation; redaction regressions)

### Periodic audits (recommended)
- Quarterly: sample 3 completed EXP/RUN pairs → verify re-run works end-to-end
- Before release: audit “high-impact” artifacts (models, major new datasets, story bundles)
- After incidents: add an SOP + regression checks  [oai_citation:83‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH)

> [!TIP]
> A good system becomes safer over time: every incident should produce a new gate. 🧯✅

---

## 🤝 PR / review checklist

When your PR includes experiments, runs, or evidence:

- [ ] EXP report added/updated (`mcp/experiments/...`) *(if decision-relevant)*
- [ ] RUN receipt folder added (`mcp/runs/...`) with `MANIFEST.md`
- [ ] Evidence outputs stored under `data/processed/...` (or linked object storage)
- [ ] STAC/DCAT/PROV pointers added (IDs or paths)
- [ ] Contracts validated (schema/profile versions recorded)  [oai_citation:84‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- [ ] AI involvement labeled (if applicable)
- [ ] Reproduction steps included (1–4 steps; copy/paste runnable)
- [ ] No secrets / no sensitive leaks in logs or outputs
- [ ] Reviewer can reproduce (required for L2/L3 work)

> [!TIP]
> A great review comment is: **“I reproduced this and got the same outputs.”** ✅

---

## 📚 Project reference library influence map

> These project files inform *how we design and review* MCP artifacts: reproducibility, governance, security, modeling rigor, statistical discipline, scaling, and visualization constraints.

<details>
<summary><strong>📦 Expand: Reference library → what it influences in <code>mcp/</code></strong></summary>

| Project file | Primary lens | How it upgrades MCP |
|---|---|---|
| `MARKDOWN_GUIDE_v13.md.gdoc`  [oai_citation:85‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz) | 🧾 Repo invariants | Makes pipeline ordering + provenance-first + contract-first non-negotiable; pushes deterministic/idempotent ETL and hash-addressable run receipts. |
| `Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx`  [oai_citation:86‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) | ✍️ Doc quality | Strengthens front matter, metadata discipline, and machine-readability without sacrificing human clarity. |
| `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf`  [oai_citation:87‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) | 🔬 Scientific method | Reinforces protocol-first workflow, transparency, peer review, modular domain protocols. |
| `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`  [oai_citation:88‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) | 🧭 System blueprint | Aligns MCP with KFM’s governed evidence pipeline (catalogs/lineage), Focus discipline, and contract-first portal thinking. |
| `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`  [oai_citation:89‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw) | 🏗️ Platform design | Clarifies end-to-end architecture (ingest → catalogs → analysis → UI) and why experiment tracking/model cards are first-class; encourages templates + doc UX. |
| `Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf`  [oai_citation:90‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH) | 🧯 Reality check | Calls out where MCP must be operational (actual SOPs, glossary, checklists, review notes)—not just “paper MCP.” |
| `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`  [oai_citation:91‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) | 🛰️ V&V discipline | Shapes simulation experiment logging, V&V framing, uncertainty, sensitivity analysis, and “claims with bounds.” |
| `Understanding Statistics & Experimental Design.pdf`  [oai_citation:92‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) | 📊 Rigor + bias | Guards against optional stopping/publication bias; enforces assumptions + effect sizes + multiple comparisons discipline. |
| `regression-analysis-with-python.pdf`  [oai_citation:93‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) + `Regression analysis using Python - slides-linear-regression.pdf`  [oai_citation:94‡Generalized Topology Optimization for Structural Design.pdf](file-service://file-PzydVyvSPdXWqYrXeFCNzj) | 📈 Baselines + diagnostics | Improves reproducible modeling baselines and diagnostic reporting (residuals, influence, leakage checks) in EXP/RUN artifacts. |
| `think-bayes-bayesian-statistics-in-python.pdf`  [oai_citation:95‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu) | 🎲 Uncertainty | Encourages explicit priors, posterior uncertainty, and calibrated decisions under uncertainty. |
| `graphical-data-analysis-with-r.pdf`  [oai_citation:96‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) | 📉 EDA instincts | Reinforces visual sanity checks, anomaly detection, and “show the distribution” before publishing evidence. |
| `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`  [oai_citation:97‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE) | 🛰️ EO workflows | Informs remote sensing SOPs (export patterns, time-series handling) and treating derived indices as evidence artifacts. |
| `python-geospatial-analysis-cookbook.pdf`  [oai_citation:98‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu) | 🗺️ GIS engineering | Guides CRS hygiene, vector/raster IO, PostGIS integration, and safe geoprocessing SOPs. |
| `making-maps-a-visual-guide-to-map-design-for-gis.pdf`  [oai_citation:99‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) | 🎨 Cartography ethics | Reminds that visualization choices shape meaning; demands documentation of map design decisions. |
| `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`  [oai_citation:100‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj) | 📱 Mobile/offline constraints | Encourages tiling, caching, offline-aware documentation, and awareness that digital maps are socio-technical. |
| `responsive-web-design-with-html5-and-css3.pdf`  [oai_citation:101‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M) | 🌐 Real-device constraints | Pushes MCP to capture payload/latency constraints and test on realistic device assumptions. |
| `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`  [oai_citation:102‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd) | 🧊 GPU/3D | Motivates explicit coordinate conventions, LOD/tiling decisions, and 3D evidence display constraints. |
| `Archaeological 3D GIS_26_01_12_17_53_09.pdf`  [oai_citation:103‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2) | 🏛️ 3D GIS rigor | Encourages explicit spatial/temporal assumptions and careful interpretation for 3D/historical reconstructions. |
| `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`  [oai_citation:104‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY) | 🖼️ Image pipelines | Shapes SOPs for thumbnails, compression, and safe handling of complex formats/metadata. |
| `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`  [oai_citation:105‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) | 🐘 Data store discipline | Informs SOPs around schemas, indexing, migrations, vacuum/analyze, and reproducible data loading. |
| `Database Performance at Scale.pdf`  [oai_citation:106‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf) | ⚙️ Performance receipts | Encourages documenting workload mix, query plans, regression budgets, and realistic performance constraints in receipts. |
| `Scalable Data Management for Future Hardware.pdf`  [oai_citation:107‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE) | ⚙️ Acceleration + batching | Encourages documenting query batching, caching windows, pushdown/accelerators, and resource assumptions for long-running/streaming workloads. |
| `Data Spaces.pdf`  [oai_citation:108‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) | 🔗 Interop & federation | Supports catalog-as-interface thinking and future federated evidence workflows. |
| `Spectral Geometry of Graphs.pdf`  [oai_citation:109‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf) | 🕸️ Graph theory | Encourages careful interpretation of graph metrics and provenance for derived relations. |
| `Generalized Topology Optimization for Structural Design.pdf`  [oai_citation:110‡Generalized Topology Optimization for Structural Design.pdf](file-service://file-PzydVyvSPdXWqYrXeFCNzj) | 🧮 Optimization workflows | Suggests structuring optimization experiments as reproducible jobs with clear objectives/constraints and convergence receipts. |
| `Principles of Biological Autonomy - book_9780262381833.pdf`  [oai_citation:111‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf) | 🧠 Systems thinking | Promotes feedback-loop awareness and stability thinking when documenting pipelines and governance loops. |
| `Introduction to Digital Humanism.pdf`  [oai_citation:112‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ) | ❤️ Human-centered ethics | Reinforces transparency, accountability, dignity, and role clarity (RACI-like governance). |
| `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`  [oai_citation:113‡Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf](file-service://file-Mu6zixTqF9Lubf5QMjepRg) | ⚖️ AI governance | Encourages explicit policy/legal context, risk framing, and careful claims around ML outputs. |
| Security & concurrency refs: `Gray Hat Python...pdf`  [oai_citation:114‡Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf](file-service://file-Mu6zixTqF9Lubf5QMjepRg), `ethical-hacking-and-countermeasures...pdf`  [oai_citation:115‡On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf](file-service://file-NtashtRjti9J1THyYXkhAv), `concurrent-real-time-and-distributed-programming-in-java...pdf`  [oai_citation:116‡concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf](file-service://file-Y45SvXbmLoZL1MNmrcyqz6) | 🛡️ Adversarial mindset | Guides hostile-input posture, threat modeling, secure parsing, and defensive review of services/pipelines. |
| ML practice refs: `Deep Learning for Coders with fastai and PyTorch...pdf`  [oai_citation:117‡Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf](file-service://file-GqygtUWf5Xyi3AjEaqEdQB), `Understanding Machine Learning: From Theory to Algorithms`  [oai_citation:118‡U-X programming Books.pdf](file-service://file-3hYtSGHtHmb6wyTtavym6M), `Basics of Linear Algebra for Machine Learning`  [oai_citation:119‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ) | 🤖 ML discipline | Improves dataset/label transparency, evaluation hygiene, and foundational rigor for model card claims. |
| Engineering refs: `Flexible Software Design...pdf`  [oai_citation:120‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY), `Bash Notes for Professionals`  [oai_citation:121‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ) | 🧰 Engineering quality | Strengthens stable IDs, change-friendly design, and safe, reproducible shell-based workflows in receipts. |
| Programming bundles (polyglot): `B-C...pdf`  [oai_citation:122‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ), `F-H...pdf`  [oai_citation:123‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY), `I-L...pdf`  [oai_citation:124‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a), `O-R...pdf`  [oai_citation:125‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M), `S-T...pdf`  [oai_citation:126‡S-T programming Books.pdf](file-service://file-NT32tqqzGW9RvfcNZmMH1K) | 🧰 Polyglot reference | Supports language/tooling best practices while keeping KFM boundary invariants intact. |

</details>

---

## 🧾 Reference library index

This is the **local** reference library currently shaping MCP.  
Use it as “how we think” scaffolding—**not** as a substitute for evidence artifacts.

<details>
<summary><strong>📚 Expand: Full index of consulted project files</strong></summary>

### 🧭 KFM doctrine & documentation standards
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`  [oai_citation:127‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`  [oai_citation:128‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)  
- `Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf`  [oai_citation:129‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH)  
- `MARKDOWN_GUIDE_v13.md.gdoc`  [oai_citation:130‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  
- `Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx`  [oai_citation:131‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf`  [oai_citation:132‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  

### 🛰️ Modeling, statistics, and inference
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`  [oai_citation:133‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- `Understanding Statistics & Experimental Design.pdf`  [oai_citation:134‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- `regression-analysis-with-python.pdf`  [oai_citation:135‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- `Regression analysis using Python - slides-linear-regression.pdf`  [oai_citation:136‡Generalized Topology Optimization for Structural Design.pdf](file-service://file-PzydVyvSPdXWqYrXeFCNzj)  
- `think-bayes-bayesian-statistics-in-python.pdf`  [oai_citation:137‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)  
- `graphical-data-analysis-with-r.pdf`  [oai_citation:138‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  

### 🗺️ Geospatial, cartography, remote sensing, and 3D
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`  [oai_citation:139‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)  
- `python-geospatial-analysis-cookbook.pdf`  [oai_citation:140‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)  
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`  [oai_citation:141‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`  [oai_citation:142‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj)  
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`  [oai_citation:143‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd)  
- `Archaeological 3D GIS_26_01_12_17_53_09.pdf`  [oai_citation:144‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  

### ⚙️ Data systems, scaling, interoperability
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`  [oai_citation:145‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- `Database Performance at Scale.pdf`  [oai_citation:146‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf)  
- `Scalable Data Management for Future Hardware.pdf`  [oai_citation:147‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)  
- `Data Spaces.pdf`  [oai_citation:148‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  

### 🕸️ Graph + optimization theory
- `Spectral Geometry of Graphs.pdf`  [oai_citation:149‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf)  
- `Generalized Topology Optimization for Structural Design.pdf`  [oai_citation:150‡Generalized Topology Optimization for Structural Design.pdf](file-service://file-PzydVyvSPdXWqYrXeFCNzj)  

### ❤️ Ethics, humanism, AI governance
- `Introduction to Digital Humanism.pdf`  [oai_citation:151‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`  [oai_citation:152‡Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf](file-service://file-Mu6zixTqF9Lubf5QMjepRg)  
- `Principles of Biological Autonomy - book_9780262381833.pdf`  [oai_citation:153‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf)  

### 🛡️ Security, adversarial thinking, concurrency
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`  [oai_citation:154‡On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf](file-service://file-NtashtRjti9J1THyYXkhAv)  
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`  [oai_citation:155‡Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf](file-service://file-Mu6zixTqF9Lubf5QMjepRg)  
- `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`  [oai_citation:156‡concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf](file-service://file-Y45SvXbmLoZL1MNmrcyqz6)  
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`  [oai_citation:157‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)  

### 🌐 Web + product constraints
- `responsive-web-design-with-html5-and-css3.pdf`  [oai_citation:158‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)  

### 🤖 ML practice + foundations
- `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf`  [oai_citation:159‡Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf](file-service://file-GqygtUWf5Xyi3AjEaqEdQB)  
- `Understanding Machine Learning: From Theory to Algorithms`  [oai_citation:160‡U-X programming Books.pdf](file-service://file-3hYtSGHtHmb6wyTtavym6M)  
- `Bash Notes for Professionals` + `Basics of Linear Algebra for Machine Learning`  [oai_citation:161‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ)  
- `Flexible Software Design: Systems Development for Change`  [oai_citation:162‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)  

### 🧰 Polyglot programming bundles (multi-book compilations)
- `B-C programming Books.pdf`  [oai_citation:163‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ)  
- `F-H programming Books.pdf`  [oai_citation:164‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)  
- `I-L programming Books.pdf`  [oai_citation:165‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a)  
- `O-R programming Books.pdf`  [oai_citation:166‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)  
- `S-T programming Books.pdf`  [oai_citation:167‡S-T programming Books.pdf](file-service://file-NT32tqqzGW9RvfcNZmMH1K)  
- `A programming Books.pdf` *(local bundle; large multi-book PDF — include in repo library index)*  
- `D-E programming Books.pdf` *(local bundle; large multi-book PDF — include in repo library index)*  
- `M-N programming Books.pdf` *(local bundle; large multi-book PDF — include in repo library index)*  
- `U-X programming Books.pdf` *(local bundle; large multi-book PDF — include in repo library index)*  

</details>

---

## 🕰️ Version history

| Version | Date | Summary | Author |
|---:|---|---|---|
| v1.4.0 | 2026-01-13 | Brought MCP in line with **contract-first + provenance-first** doctrine: added repo invariants, strengthened front matter (doc UUID + care_label), expanded run receipts to include input/output hashes + contract validation, added benchmark/performance receipt guidance, and added threat-model/hostile-input section. Updated influence map + reference index to reflect current project library. | KFM Engineering |
| v1.3.0 | 2026-01-11 | Tightened MCP into a typed, machine-readable “methods + receipts” layer: added artifact/ID table, Detect→Validate→Promote guidance, front matter + schema notes, expanded run manifest to include policy checks/attestation hooks, added incident/review artifact guidance, and aligned reference map with current project docs. | KFM Engineering |
| v1.2.0 | 2026-01-09 | Upgraded MCP to align with v13 evidence-first/contract-first doctrine: added definition-of-done, reproducibility levels, traceability matrix, bad-evidence restraint protocol, expanded governance/licensing/sensitive-location guidance, and an updated reference-library influence map. | KFM Engineering |
| v1.1.0 | 2026-01-06 | Clarified non‑negotiables + pipeline linkage; added run receipt template, PR checklist, and workflow diagram. | KFM Engineering |
| v1.0.0 | 2025-12-31 | Initial MCP README: experiments, runs, SOPs, model cards, notebooks, safety rules. | KFM Engineering |

---

🧭 **Goal:** Make every output auditable and every method teachable.  
🧾 **Promise:** If it’s in production, it has a paper trail. ✅