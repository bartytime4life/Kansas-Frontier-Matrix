<!-- .github/ISSUE_TEMPLATE/README.md -->

# 🧩 Issue Templates & Triage Playbook — Kansas Frontier Matrix (KFM) 🗺️🤖

![KFM](https://img.shields.io/badge/KFM-provenance--first-2ea44f)
![Monorepo](https://img.shields.io/badge/monorepo-code%2Bdata%2Bdocs-blue)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-orange)
![AI](https://img.shields.io/badge/AI-no--source%20no--answer-critical)
![Architecture](https://img.shields.io/badge/architecture-contract--first-blueviolet)
![Policy](https://img.shields.io/badge/policy-OPA%20gated-0052cc)
![Contrib](https://img.shields.io/badge/contributions-welcome-brightgreen)

> **KFM issues are mini-contracts**: they describe a problem or change request with enough **evidence, constraints, and acceptance criteria** that anyone can reproduce, implement, and audit the result later.  
> Think: **“the map behind the map”** — but for engineering + data + stories. 🧬🗺️

---

## 🧭 Quick nav

- [🚀 File an issue fast](#-file-an-issue-fast)
- [🧠 Non-negotiables](#-non-negotiables)
- [🧾 How to write a KFM issue](#-how-to-write-a-kfm-issue)
- [🏷️ Routing: scopes, labels, and titles](#️-routing-scopes-labels-and-titles)
- [🧰 Template chooser](#-template-chooser)
- [🔐 Sensitive data & CARE guardrails](#-sensitive-data--care-guardrails)
- [🧱 Repo mental map](#-repo-mental-map)
- [🤝 What happens after you file](#-what-happens-after-you-file)
- [📎 References](#-references)

---

## 🚀 File an issue fast

### 🧭 Open the template picker
➡️ GitHub: **Issues → New issue → Choose a template**

If you’re not sure which one fits, pick the closest match. Maintainers can retag later — **clarity beats perfection**. 🙌

### 🧪 Fast “starter pack” (paste into any issue)
```md
**Goal / Problem**
- …

**Scope**
- [ ] api  [ ] web  [ ] pipelines  [ ] data  [ ] catalog  [ ] provenance  [ ] docs  [ ] ai  [ ] security

**Evidence**
- Links / paths / screenshots / logs:
  - …

**Acceptance criteria**
- [ ] …

**Risks / Governance**
- Sensitivity labels? CARE/FAIR implications?:
  - …
```

---

## 🧠 Non-negotiables

> **KFM has a “truth path.”** If a proposal tries to leapfrog a stage (e.g., “inject directly into UI”), it’s treated as **architecturally risky by default**. 🧱

### 🔁 Canonical “truth path” (non-negotiable ordering)
**Raw → Processed → Catalog (STAC/DCAT/PROV) → Databases → API → UI/AI**

- Data + provenance must flow through the pipeline before it becomes user-facing. 🧾🧬  
- The UI consumes governed APIs; policies are enforced at boundaries (not sprinkled randomly). 🔐  
- AI answers are **evidence-backed** and policy-checked before returning to users. 🤖📎  

> See also: KFM’s contract-first, provenance-first layout guidance. [^kfm_v13]

### 🤖 “No Source, No Answer” (AI)
If Focus Mode can’t cite trusted sources, it should **refuse** or ask for clarification. Evidence isn’t “extra context” — it **is part of the product**. [^kfm_ai]

---

## 🧾 How to write a KFM issue

Good design is problem solving — and the first step is **research**. Bring that mindset into issues: gather evidence, define constraints, then propose changes. [^web_design]

### ✅ The KFM Issue “Brief” (what we want)
A strong issue reads like a compact project brief:

1. **Problem statement** (what’s wrong / missing?)
2. **Context** (where in the system?)
3. **Evidence** (logs, screenshots, dataset IDs, references)
4. **Constraints** (governance, privacy, performance, compatibility)
5. **Acceptance criteria** (how we know it’s done)
6. **Out-of-scope** (what this issue explicitly does *not* do)

### 🎯 Acceptance criteria = fewer surprises
Acceptance criteria should be **testable** (functional + non-functional). They’re foundational to acceptance testing and reduce “works on my machine” outcomes. [^acceptance]

**Examples**
- ✅ “Given dataset `X`, pipeline run produces `data/processed/X.parquet` and updates `data/catalog/…` with valid STAC + PROV.”
- ✅ “Map layer renders at zoom 6–12 under 2s for a cold load on baseline hardware.”
- ✅ “Focus Mode response includes citations for all factual claims; policy gate passes.”

---

## 🏷️ Routing: scopes, labels, and titles

### 🧩 Title format
Use a scope prefix in square brackets:

```text
[scope] short imperative summary — (optional: dataset/story/area)
```

**Examples**
- `[pipelines] Add STAC + PROV emit step for Landsat ingest`
- `[web] Timeline scrubber misaligns at year boundaries`
- `[ai] Focus Mode cites wrong dataset version in answer`
- `[security] CSP blocks MapLibre worker on prod build`

### 🗂️ Scopes (pick the closest)
- `[api]` 🧪 FastAPI boundary (endpoints, validation, policy enforcement)
- `[web]` 🎛️ UI (React/TS, MapLibre/Cesium, rendering, UX)
- `[pipelines]` 🏭 ETL/ingest/transforms/QA
- `[data]` 🧱 Raw/processed datasets + metadata
- `[catalog]` 🗃️ STAC/DCAT discoverability and dataset identity
- `[provenance]` 🧬 Lineage logs, audit trails, reproducibility
- `[docs]` 📚 Architecture docs, story nodes, narratives, diagrams
- `[ai]` 🤖 Focus Mode, retrieval, citations, model behavior
- `[security]` 🔐 Privacy, access control, abuse prevention, supply chain

> Tip: Usability loves consistency (names, navigation, structure). Apply that mindset to scopes + file paths. [^web_design_pro]

### 🏷️ Optional “mini-tags” in the title
Add one if it helps triage:
- `P0/P1/P2` 🔥 priority hint
- `blocked:` 🚧 depends on something else
- `sensitive:` 🛡️ governance review likely

---

## 🧰 Template chooser

Use this table to pick the best starting point:

| Template | Use when | You should include |
|---|---|---|
| 🐞 Bug Report | Something is broken | Repro steps, expected vs actual, logs, environment |
| ✨ Feature Request | New capability / major change | Goal, pipeline impact, acceptance criteria, alternatives |
| 🗺️ Dataset / Ingest Request | Add/update data | Source + license, coverage, pipeline outputs, catalog/prov |
| 📚 Story / Narrative / Docs | Add/adjust narrative content | Outline, citations, related dataset IDs, sensitivity notes |
| 🤖 AI / Focus Mode | Answer quality / citations / retrieval | Prompt, result, expected, source IDs, policy/citation info |
| 🔐 Security / Privacy / Governance | Sensitive info / access / policy gaps | Impact, reproduction, safe handling, advisory flow |

---

<details>
<summary><strong>🐞 Bug Report</strong> — Something is broken</summary>

**Include**
- **Expected vs actual**
- **Exact repro steps** (smallest repro preferred)
- **Logs / console output / stack traces** (sanitize secrets 🔐)
- **Scope + path hints** (`api/...`, `web/...`, `pipelines/...`)
- **Environment**
  - OS / browser
  - Python/Node versions
  - dataset ID(s) + version(s)

**Extra helpful**
- Suspected commit/PR or “last known good”
- Screenshots/video for UI bugs
</details>

<details>
<summary><strong>✨ Feature Request</strong> — New capability or major change</summary>

**Include**
- **User goal** (job-to-be-done)
- **Where it fits the truth path** (Raw → … → UI/AI) [^kfm_v13]
- **Acceptance criteria** ✅ (testable)
- UI/UX notes (sketches welcome 🎨)
- API notes (schemas, versioning, policy)
- Governance implications (FAIR/CARE, privacy, access tiers) [^kfm_governance]

**Helpful**
- Alternatives considered
- Migration plan (if it changes schemas/data contracts)
</details>

<details>
<summary><strong>🗺️ Dataset / Data Ingest Request</strong> — Add or update data</summary>

**Include (required)**
- **Source link(s)** + citation(s)
- **License** (hard requirement)
- Coverage:
  - **Time range**
  - **Spatial extent**
  - **Format** (GeoJSON, COG, CSV, Parquet, etc.)
- **Proposed pipeline steps** (or what you tried)

**Expected outputs**
- `data/raw/` 🧊 immutable snapshot
- `data/processed/` 🧼 standardized outputs
- `data/catalog/` 🗃️ STAC/DCAT metadata
- `data/provenance/` 🧬 lineage (PROV)

> ⚠️ If your request implies “skip metadata/provenance,” it will likely be rejected — metadata + provenance are first-class. [^kfm_v13]
</details>

<details>
<summary><strong>📚 Story / Narrative / Docs</strong> — Add or improve story content</summary>

**Include**
- What story you want to add/change (scope)
- Proposed outline (bullets fine)
- **Sources / citations** (required)
- Related dataset IDs or file paths
- Sensitivity notes / content warnings (if relevant)

> Story content is governed: accuracy, citations, and respectful framing matter as much as code. [^kfm_governance]
</details>

<details>
<summary><strong>🤖 AI / Focus Mode</strong> — Answer quality, citations, retrieval, policy behavior</summary>

**Include**
- The exact prompt you used
- The answer you got (what’s wrong / unsafe / incomplete)
- Expected answer + **which sources should have been used**
- Classify the failure:
  - Retrieval gap (missing docs/data)
  - Citation mismatch / version mismatch
  - Policy gate false-positive/false-negative
  - Hallucination / overreach

**If available**
- Source IDs returned by the system
- UI context (selected place/time/layers)

> Focus Mode is designed as an evidence-first RAG pipeline (retrieval + citation rule + policy gate + provenance logging). [^kfm_ai]
</details>

<details>
<summary><strong>🔐 Security / Privacy / Governance</strong> — Potential harm, sensitive info, access control</summary>

✅ File an issue for:
- Policy gaps
- Access tier logic bugs
- Takedown/withdrawal workflows
- Sensitive-content handling improvements

🚫 Do <em>not</em> post:
- Secrets, tokens, private keys
- Personal info about living people
- Restricted community-controlled data

If you suspect an exploitable vulnerability, use GitHub’s **Security Advisory** flow (if enabled) instead of a public issue. 🛡️

> KFM’s governance includes FAIR+CARE guardrails, sensitivity tags, and policy enforcement at system boundaries. [^kfm_governance] [^ids]
</details>

---

## 🔐 Sensitive data & CARE guardrails

KFM is built to be open *and* safe: **FAIR + CARE** is the standard. [^kfm_governance] [^ids]

### 🛡️ “Sensitive” can mean more than “private”
Treat as sensitive when it involves:
- Exact locations of cultural, sacred, or archaeological sites
- Community-controlled Indigenous knowledge/data
- Personally identifying info (even historical records can create modern harm)
- Small-n disclosure risk (e.g., tiny subgroup counts)

KFM design patterns may include **aggregation / coordinate rounding**, **suppression thresholds**, **query auditing**, and other controls for safe public release. [^kfm_governance]

### 🧭 If you’re unsure: default to *less detail* in public issues
- Use generalized geography (county/region) instead of precise coordinates
- Summarize the sensitive part; let maintainers request details via safer channels
- Add `sensitive:` to the title if governance review is likely

### 🌱 Indigenous data sovereignty (respect-first)
Indigenous data rights emphasize collective benefit, authority to control, responsibility, and ethics (CARE) — not just “open by default.” [^ids]  
If your issue touches Indigenous data governance, flag it early and be explicit about consent, stewardship, and intended use.

---

## ✅ “Good issue” checklist (copy/paste)

- [ ] I searched for duplicates 🔎
- [ ] I used a clear scope prefix (e.g., `[api]`, `[data]`) 🏷️
- [ ] I included evidence (logs/screenshots/paths/dataset IDs) 📎
- [ ] I included acceptance criteria (testable) ✅
- [ ] If data-related: I included **license + source** 📜
- [ ] If story-related: I included **citations** 📚
- [ ] I did **not** include sensitive/private info 🔐
- [ ] I noted governance implications (FAIR/CARE) if relevant 🛡️

---

## 🧱 Repo mental map

> Use this to reference files precisely in issues. (Paths may differ by branch/layout.)

<details>
<summary><strong>📦 Common “classic” layout</strong></summary>

```text
📦 repo/
├── api/          🧪 FastAPI backend
├── web/          🎛️ React + TypeScript UI
├── pipelines/    🏭 ETL pipelines & simulation scripts
├── data/         🧱 Versioned datasets + metadata
│   ├── raw/          🧊 immutable source snapshots
│   ├── processed/    🧼 cleaned/standardized outputs
│   ├── catalog/      🗃️ STAC/DCAT metadata
│   └── provenance/   🧬 lineage logs (PROV)
└── docs/         📚 narratives, architecture, story nodes
```
</details>

<details>
<summary><strong>🧭 v13 “contract-first” layout (reference)</strong></summary>

```text
📦 repo/
├── schemas/                 🧾 JSON Schemas (STAC/DCAT/PROV/story/UI)
├── data/
│   ├── raw/                 🧊 immutable snapshots
│   ├── working/             🧪 intermediate artifacts
│   ├── processed/           🧼 standardized outputs
│   ├── catalog/
│   │   ├── stac/            🗃️ STAC items/collections
│   │   └── dcat/            🗃️ DCAT datasets
│   └── prov/                🧬 PROV lineage
├── src/
│   ├── pipelines/           🏭 ETL jobs
│   ├── graph/               🧠 Neo4j build + ontology bindings
│   └── server/              🧪 API boundary (contracts enforced here)
├── web/                     🎛️ UI (React + Map)
└── docs/
    ├── architecture/        🏗️ blueprints + ADRs
    └── reports/story_nodes/ 🧭 governed narratives (draft/published)
```

> Key idea: **one canonical home per subsystem** + evidence-first workflows. [^kfm_v13]
</details>

---

## 🤝 What happens after you file

Maintainers will typically:

1. 🏷️ **Label + route** (`api/web/data/pipelines/...`)
2. 🧩 Ask for missing info (if needed)
3. 🗺️ Convert to PR checklist / link to tracking issue
4. ✅ Close when fixed — or mark **blocked** with next steps

---

## 📎 References

- **KFM governance & system design** (FAIR+CARE, sensitivity controls, supply-chain posture) — [^kfm_governance]  
- **KFM AI / Focus Mode pipeline** (evidence retrieval + policy gating + provenance logging) — [^kfm_ai]  
- **Indigenous Data Sovereignty & CARE principles** — [^ids]  
- **Design process mindset: research → brief → deliverables** — [^web_design]  
- **Usability: consistency + accessibility** — [^web_design_pro]  
- **Acceptance criteria & acceptance testing mindset** — [^acceptance]

---

[^kfm_ai]: Kansas Frontier Matrix Comprehensive System Documentation — Focus Mode RAG pipeline + citation rule + OPA policy gate.  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
[^kfm_governance]: Kansas Frontier Matrix Comprehensive System Documentation — FAIR+CARE, sensitivity handling patterns, and security posture.  [oai_citation:2‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  [oai_citation:3‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
[^kfm_v13]: MARKDOWN / v13 contract-first layout guidance (canonical pipeline + directory model).  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^ids]: Indigenous Statistics (2nd ed., 2025) — CARE principles + Indigenous Data Sovereignty framing.  [oai_citation:5‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)  [oai_citation:6‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)
[^web_design]: Web Design — design as problem solving; begin with research + briefs.  [oai_citation:7‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)
[^web_design_pro]: Professional Web Design — usability emphasis on consistency, navigation, accessibility.  [oai_citation:8‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  [oai_citation:9‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)
[^acceptance]: Various Programming Concepts — acceptance criteria + acceptance testing framing.  [oai_citation:10‡Various Programming Concepts.pdf](sediment://file_00000000e86c71fd9eceb7eec4bba22e)