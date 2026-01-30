<!-- According to a document from 2026-01-30 (KFM blueprint + repo master guide): this MCP is aligned to the non-negotiable KFM pipeline, boundary artifacts (STAC/DCAT/PROV), and fail-closed governance. -->

---
title: "MCP — Master Coder Protocol (Docs • Rigor • Reproducibility)"
path: "mcp/README.md"
version: "v1.1.0"
last_updated: "2026-01-30"
status: "active"
doc_kind: "Protocol"
mcp_protocol_version: "1.1"
pipeline_contract: "ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode"
---

# 🧠 MCP — Master Coder Protocol (Docs • Rigor • Reproducibility)

![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-111827?style=for-the-badge)
![Docs-as-Code](https://img.shields.io/badge/docs-as--code-✅-2563eb?style=for-the-badge)
![Provenance](https://img.shields.io/badge/provenance-first-🧾-16a34a?style=for-the-badge)
![Reproducible](https://img.shields.io/badge/reproducible-🧪-a855f7?style=for-the-badge)
![Fail%20Closed](https://img.shields.io/badge/fail--closed-🛑-ef4444?style=for-the-badge)
![STAC%2FDCAT%2FPROV](https://img.shields.io/badge/STAC%2FDCAT%2FPROV-📦🔗-f97316?style=for-the-badge)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-🌍-10b981?style=for-the-badge)

> **MCP = Master Coder Protocol** (for *this* repo).  
> It’s the **lab notebook + operating manual layer** that keeps Kansas Frontier Matrix work **traceable, repeatable, and reviewable**. 🧾✨  
> *(Not to be confused with other “MCP” acronyms elsewhere.)*

---

## 🧭 Quick Navigation

- [📌 TL;DR — Non‑negotiables](#tldr)
- [🗺️ Canonical pipeline (contract)](#pipeline)
- [🗂️ What belongs in `mcp/`](#belongs)
- [📁 Folder layout (repo + MCP)](#layout)
- [🏷️ IDs & naming conventions](#naming)
- [🧪 Experiments: minimum bar](#experiments)
- [🤖 Model cards + 💬 prompt cards](#modelcards)
- [🧾 Data: STAC/DCAT/PROV boundary artifacts](#boundary)
- [🏛️ Governance: FAIR/CARE + Fail Closed](#governance)
- [✅ Quality gates & checklists](#gates)
- [🧰 Templates](#templates)
- [📚 Knowledge base + reading shelf](#reading)

---

<a id="tldr"></a>

## 📌 TL;DR — Non‑negotiables 🔒

- **If it isn’t documented, it didn’t happen.** 🧠  
- **No pipeline shortcuts:** *ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode* 🚫⚡  
- **Every dataset (including AI/analysis “evidence artifacts”) ships with:**  
  - **License + metadata** ✅  
  - **STAC/DCAT/PROV** boundary artifacts 📦🔗  
- **Every meaningful experiment gets an EXP report + repro pack.** 🧪  
- **Every deployed or decision‑influencing model/prompt gets a card + evaluation.** 🤖💬  
- **Docs change with code (same PR/commit whenever possible).** 🔁  
- **Fail closed:** missing metadata/policy violation **blocks merge**. 🛑

> [!IMPORTANT]
> Any proposal that *leapfrogs* catalog/provenance or bypasses the API boundary is a **design bug**, not a “speed optimization.” 🧨

---

<a id="pipeline"></a>

## 🗺️ Canonical pipeline (contract-first)

KFM is built so that **every claim** and **every derived artifact** can be traced back to **versioned evidence**.  
MCP exists to ensure the **human workflow** matches the **system workflow**.

```mermaid
flowchart LR
  raw[📥 Raw sources] --> etl[🧪 ETL / Pipelines]
  etl --> processed[📦 Processed outputs]
  processed --> catalogs[🗂️ Catalogs: STAC / DCAT / PROV]
  catalogs --> graph[🕸️ Graph: Neo4j]
  graph --> api[🔌 API boundary (contracts + governance)]
  api --> ui[🗺️ UI: Map + Narrative]
  ui --> story[📝 Story Nodes]
  story --> focus[🎯 Focus Mode (grounded + citeable)]
```

### ✅ MCP interpretation of this contract

- **Catalogs (STAC/DCAT/PROV) are the boundary artifacts** between data processing and downstream systems.
- **The API is a governance boundary** (redaction, classification, access rules).
- **Story Nodes never skip evidence.** Story ≠ opinion; story = **claims + citations to evidence**.

---

<a id="belongs"></a>

## 🗂️ What belongs in `mcp/`

MCP is the project’s **reproducibility spine** 🦴—focused on methods, runs, audits, and operational clarity:

- 🧪 **Experiments** (reports, runs, artifacts, comparisons)
- 🧬 **Protocols** (pre-run plans, variables, risks)
- 🤖 **Model cards** (model purpose, evals, failure modes)
- 💬 **Prompt cards** (system prompts + test cases + constraints)
- 🧾 **Templates** (reduce drift, raise quality)
- ✅ **Checklists** (PR gates, ingest gates, release gates)
- 🛠️ **Runbooks** (when X breaks, do Y)
- 🏛️ **Governance** (MCP-scoped policies; global policies belong in `docs/`)

> [!TIP]
> If you’re wondering “where does this live?”—put it where a future contributor will look **at 2am**. That’s the real taxonomy. 🌙🛠️

---

<a id="layout"></a>

## 📁 Folder layout (recommended)

> Names should be stable and boring. **Boring scales.** 😌  
> Emojis below are *visual annotations* only—keep folder names ASCII.

```text
mcp/
├─ README.md                          # 🧠 this document
├─ templates/                         # 🧰 canonical templates (copy-paste starters)
├─ experiments/                       # 🧪 EXP-### writeups + repro packs
├─ protocols/                         # 🧬 reusable protocols (“before you run it”)
├─ model_cards/                       # 🤖 model cards (deployment-relevant)
├─ prompt_cards/                      # 💬 prompt cards (system prompts + test cases)
├─ ai_sessions/                       # 🧠📎 AI session logs + context bundles
├─ checklists/                        # ✅ PR/ingest/release checklists
├─ runbooks/                          # 🛠️ ops + incident + recovery runbooks
├─ governance/                        # 🏛️ MCP-scoped policies (AI usage, review rules)
└─ knowledge_base/                    # 📚 curated notes + reading summaries
```

### 🧭 Repo-level directories MCP expects to interlock with

```text
docs/
├─ architecture/                      # 🏗️ system design docs + ADRs
├─ governance/                        # 🏛️ global policies, permissions, ethics
├─ data/                              # 🗂️ domain runbooks + datasheets
└─ reports/
   └─ story_nodes/                    # 📝 governed narrative content (draft/published)

data/
├─ raw/                               # 📥 immutable source snapshots
├─ work/                              # 🧱 intermediate (optional; often gitignored)
├─ processed/                         # 📦 standardized outputs
├─ stac/                              # 🗺️ STAC collections/items (spatial assets)
├─ catalog/
│  └─ dcat/                           # 🧾 DCAT dataset records
└─ prov/                              # 🔗 PROV lineage bundles (runs/datasets)

schemas/                               # 📐 JSON Schemas (STAC/DCAT/PROV/story nodes/etc.)
tests/                                 # ✅ unit + integration
tools/                                 # 🛠️ validators, linters, helpers
.github/                               # 🤖 CI, security policies
releases/                              # 📦 packaged releases (manifests, SBOM, bundles)
```

> [!NOTE]
> Some repo versions may use `data/catalog/` + `data/provenance/`. If so, document the mapping and keep it consistent (and preferably add a small README explaining the “why”). 🧭

---

## 🚦Where do I put *this* doc?

| You are creating… | Put it in… | Why |
|---|---|---|
| 🧪 A new experiment write-up | `mcp/experiments/` | searchable experiment history + repro packs |
| 🧬 A “do this before you run it” protocol | `mcp/protocols/` | repeatability + fewer “mystery runs” |
| 🤖 A model definition | `mcp/model_cards/` | transparency + evaluation |
| 💬 A prompt / agent definition | `mcp/prompt_cards/` | prompt provenance + testability |
| ✅ A quality gate | `mcp/checklists/` | prevents drift |
| 🛠️ An incident / ops guide | `mcp/runbooks/` | operational sanity |
| 🏛️ A policy (methods/AI/review rules) | `mcp/governance/` *(or `docs/governance/` if global)* | accountability |

---

<a id="naming"></a>

## 🏷️ IDs & naming conventions (make it searchable)

### ✅ Slug rules (default)

- lower-case
- hyphen-separated
- no spaces
- no “final_v2_reallyfinal”

### 📌 Recommended IDs

| Type | Prefix | Example |
|---|---:|---|
| Experiment | `EXP-###` | `EXP-012_place-name-extraction.md` |
| Protocol | `PRO-###` | `PRO-004_ocr-to-text-pipeline.md` |
| Dataset | `DS-<domain>-<slug>` | `DS-land_treaties-1854-kansa.md` |
| Model card | `MC-<component>-<ver>` | `MC-focusmode-llmrouter-v0.3.md` |
| Prompt card | `PC-<component>-<ver>` | `PC-storynode-drafter-v0.2.md` |
| Runbook | `RB-<system>-<issue>` | `RB-api-neo4j-connection.md` |
| Incident | `INC-YYYY-MM-DD-<slug>` | `INC-2026-01-28-catalog-validation.md` |
| Decision record | `ADR-####-<slug>` | `ADR-0012-catalogs-are-boundaries.md` |

> [!TIP]
> Make IDs appear in commits, PR titles, filenames, and report headers. Search is a superpower. 🔍✨

---

<a id="experiments"></a>

## 🧪 Experiments (minimum bar)

Every meaningful experiment should be written up as a **version-controlled report**—with enough detail that someone else can reproduce it.

### ✅ Preferred structure (folder-per-experiment)

```text
mcp/experiments/EXP-012_short-title/
├─ README.md                # 🧪 experiment report
├─ protocol.md              # 🧬 optional (or link to PRO-###)
├─ env/                     # 🧪 environment lockfiles + docker/conda
│  ├─ requirements.txt
│  ├─ poetry.lock
│  ├─ environment.yml
│  └─ Dockerfile
├─ src/                     # 🧰 scripts, notebooks (end-to-end runnable)
├─ artifacts/               # 📦 small outputs (tables, tiny figs)
└─ REFERENCES.md            # 🧾 citations + data pointers
```

### 🧾 Minimum required sections (report)

- **Goal / Question** 🎯  
- **Data used** (IDs, versions, hashes where possible) 🧾  
- **Method** (steps, parameters, code entrypoints) 🧰  
- **Results** (tables/figures + artifact locations) 📈  
- **Interpretation** 🧠  
- **Limitations / failure modes** 🧯  
- **Next steps** 🧭  
- **Repro steps** (exact commands + environment notes) 🔁  

> [!IMPORTANT]
> Notebooks must be runnable **top-to-bottom**. “Mystery kernel state” is not reproducible science. 📓🚫

---

<a id="modelcards"></a>

## 🤖 Model Cards + 💬 Prompt Cards (AI + ML)

If an AI component is **deployed**, **user-facing**, **decision-influencing**, or **used repeatedly**, it needs documentation.

### 🤖 Model Card (MC-*)

**Minimum fields**

- **Purpose / intended use**
- **Not intended use**
- **Data notes** (training/tuning sources, limitations, known biases)
- **Evaluation** (quant + scenario-based tests)
- **Safety & ethics** (bias risks, sensitive data handling, redaction behavior)
- **Operational** (how to run, hardware, versioning, rollback)
- **Change log**

### 💬 Prompt Card (PC-*)

Prompts are code. Treat them like code. 🧠➡️🧰

**Minimum fields**

- **System prompt / role instructions**
- **Inputs & outputs** (schemas, formats)
- **Tooling + constraints** (what tools it may use, what it must never do)
- **Test cases** (golden inputs + expected outputs)
- **Known failure modes** (hallucinations, overreach, bias, unsafe leakage)
- **Changelog + version tags**

> [!TIP]
> If you can’t write a test case for a prompt, it’s not stable enough to rely on. ✅

---

<a id="boundary"></a>

## 🧾 Data: STAC/DCAT/PROV boundary artifacts (required) 📦🔗

### 🥇 Golden rule

**Data is not “published” until the boundary artifacts exist.**

Minimum set:

- **STAC** (spatial assets)
- **DCAT** (dataset record)
- **PROV** (lineage: inputs → transforms → outputs + agents)
- **License** (explicit; no guessing)

### 🧠 Evidence artifacts (AI/analysis outputs)

AI outputs that produce datasets (OCR corpora, predicted layers, simulations) are treated as **first-class datasets**:

- stored under `data/processed/...`
- cataloged in STAC/DCAT
- traced in PROV
- exposed **only via API** (governance boundary) 🔌

---

<a id="governance"></a>

## 🏛️ Governance: FAIR/CARE + Fail Closed 🛑

### Fail Closed (default)

If a policy check fails, we block the action (CI fails, merge blocked, deploy blocked).  
This prevents non-compliant contributions from slipping in “just this once.”

### FAIR + CARE (by design)

- **FAIR** → findable, accessible, interoperable, reusable data practices  
- **CARE** → especially important for sensitive/sovereign/community-owned data

**Practical implications**

- Data classification labels exist and are enforced
- Licenses must be explicit
- Sensitive outputs must go through the API boundary for redaction/labeling
- Policies are enforced via **policy-as-code** in CI

---

<a id="gates"></a>

## ✅ Quality gates (don’t skip)

### ✅ Review + testing gates

- Unit tests where possible ✅  
- Integration checks for pipelines ✅  
- Peer review for major experiments ✅  
- CI must be green before merge ✅  
- Policy checks must pass (licenses, metadata, required artifacts) 🛑  

### 🔁 Reproducible coding habits

- Set random seeds when applicable 🎲
- Log parameters + environment 🔎
- Pin dependencies (lockfiles) 📌
- Record entrypoints (Make targets / CLI commands) ⌨️
- Avoid “works on my machine” setups 🧯

---

## 🙌 Checklists (fast)

<details>
  <summary><strong>✅ MCP PR checklist (click to expand)</strong></summary>

- [ ] I updated **docs** in the same PR as code changes  
- [ ] I added/updated an **experiment report** (if I ran one)  
- [ ] I added/updated a **protocol** (if this is a reusable method)  
- [ ] I added/updated a **model card** (if I changed an AI/ML component)  
- [ ] I added/updated a **prompt card** (if prompts/agents changed)  
- [ ] I linked artifacts/metrics (or stored small ones under `mcp/experiments/.../artifacts/`)  
- [ ] I included exact **repro steps** (commands + env)  
- [ ] CI is green  
- [ ] No pipeline shortcuts introduced  

</details>

<details>
  <summary><strong>📦 Data ingest checklist (STAC/DCAT/PROV)</strong></summary>

- [ ] Raw source snapshot stored under `data/raw/...` (immutable)  
- [ ] Processing steps live in `src/pipelines/...` (or equivalent)  
- [ ] Output stored under `data/processed/...`  
- [ ] STAC item/collection created/updated under `data/stac/...`  
- [ ] DCAT record created/updated under `data/catalog/dcat/...`  
- [ ] PROV bundle captured under `data/prov/...`  
- [ ] License declared explicitly (metadata + datasheet)  
- [ ] Domain README updated under `docs/data/<domain>/README.md`  
- [ ] Any sensitive fields are labeled and gated by API policies  
- [ ] Validation/policy checks pass (schemas + CI)

</details>

<details>
  <summary><strong>🤖 Model / prompt update checklist</strong></summary>

- [ ] Model card updated with version + change log  
- [ ] Prompt card updated with test cases + constraints  
- [ ] Evaluation re-run (and linked)  
- [ ] Bias/safety notes reviewed  
- [ ] Rollback plan documented (what version is “last known good”)  
- [ ] If user-facing: update UI/UX copy + warnings accordingly

</details>

---

<a id="templates"></a>

## 🧰 Copy-paste starter templates (recommended set)

Create these as you need them (and keep them canonical):

- `mcp/templates/experiment_report.md`
- `mcp/templates/protocol.md`
- `mcp/templates/model_card.md`
- `mcp/templates/prompt_card.md`
- `mcp/templates/dataset_datasheet.md`
- `mcp/templates/ai_session_log.md`
- `mcp/templates/runbook.md`
- `mcp/templates/checklist_pr.md`
- `mcp/templates/checklist_data_ingest.md`

### ✅ Optional: YAML front-matter (machine-readable docs)

```yaml
---
id: "EXP-012"
title: "Place-name extraction: spaCy vs regex"
status: "active"
owners: ["@your-handle"]
last_updated: "2026-01-30"
inputs:
  - dataset_id: "DS-places-gazetteer-v1"
    sha256: "..."
outputs:
  - artifact: "data/processed/places/extracted_places.parquet"
    sha256: "..."
repro:
  entrypoint: "make exp EXP=EXP-012"
  env: "mcp/experiments/EXP-012_short-title/env/"
---
```

---

<a id="reading"></a>

## 📚 Knowledge base + reading shelf (project PDFs)

- Put **summaries + notes** in: `mcp/knowledge_base/`
- Put **source PDFs** in: `docs/library/` (recommended) 📚
- Keep **domain runbooks** in: `docs/data/<domain>/README.md`

Suggested library categories:

- 🗺️ GIS & mapping (projections, map design, geocomputation, remote sensing)
- 📊 Visualization & stats (EDA, time-oriented visualization, experimental design)
- 🧱 Data systems & performance (scalable DBs, caching, hardware-aware data mgmt)
- 🤖 AI ops & local LLM runtime (Ollama, model inventories, deployment notes)
- 🧭 Ethics & digital humanism (human values + governance framing)

---

## 🔗 Related docs to cross-link

- `docs/architecture/` — system overview, blueprints, ADRs 🏗️  
- `docs/governance/` — global policies (security, ethics, access) 🏛️  
- `docs/data/` — domain runbooks + datasheets 🗂️  
- `docs/reports/story_nodes/` — governed narrative content 📝  
- `data/` — raw/processed + catalogs + provenance 📦🔗  

---

## 🧠 Closing note

MCP is how we scale trust:

**repeatable work → reviewable work → trustworthy work** 🧾✅  
…and that’s how Kansas Frontier Matrix stays a *living atlas* instead of a pile of untraceable files. 🗺️✨