# 🧠 MCP — Master Coder Protocol (Docs • Rigor • Reproducibility)

![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-111827?style=for-the-badge)
![Docs-as-Code](https://img.shields.io/badge/docs-as--code-✅-2563eb?style=for-the-badge)
![Provenance](https://img.shields.io/badge/provenance-first-🧾-16a34a?style=for-the-badge)
![Reproducible](https://img.shields.io/badge/reproducible-🧪-a855f7?style=for-the-badge)

> **MCP = Master Coder Protocol** (for *this* repo).  
> It’s the “lab notebook + operating manual” layer that keeps Kansas Frontier Matrix work **traceable, repeatable, and reviewable**. 🧾✨  
> *(Not to be confused with other “MCP” acronyms in the wider ecosystem.)*

---

## 📌 TL;DR

- **If it isn’t documented, it didn’t happen.** 🧠
- **Every experiment gets a report.** 🧪
- **Every important model gets a model card.** 🤖
- **Every dataset/process gets provenance + metadata.** 🧾
- **Docs change with code (same PR/commit whenever possible).** 🔁
- **No pipeline shortcuts.** 🚫⚡

---

## 🧭 What belongs in `mcp/`

MCP is where we keep the project’s **reproducibility spine**:

- 🧪 **Experiment protocols & reports** (what we tried, with what data, how, and what happened)
- 🤖 **Model cards / prompt cards** (what an AI component is, what it’s for, how it was evaluated)
- 🧾 **Templates** (copy-paste starting points that reduce drift and raise quality)
- ✅ **Checklists** (PR gates, data ingest gates, release gates)
- 🛠️ **Runbooks** (operational “when X breaks, do Y”)
- 🏛️ **Governance** (policies for data access, AI usage, ethics, citations, and review)

---

## 🧩 MCP in the bigger KFM picture

Kansas Frontier Matrix is built around a provenance-first workflow: raw inputs → processed outputs → catalog/provenance → database caches → API → UI. MCP exists to ensure the **human process** matches the **system design**:

- Decisions stay auditable 🕵️
- Results stay reproducible 🔁
- Collaboration stays sane 🤝
- “Focus Mode” AI stays grounded & citeable 🧠📎

---

## 🗺️ Suggested folder layout (create as-needed)

> The exact layout can evolve, but try to keep names stable and boring. Boring scales. 🙂

```text
mcp/
├─ README.md
├─ 🧰 templates/              # canonical templates (protocols, experiment reports, model cards…)
├─ 🧪 experiments/            # experiment reports (EXP-###) if not stored elsewhere
├─ 🤖 model_cards/            # model + prompt cards (deployment-relevant)
├─ 🧾 protocols/              # standardized protocols (Objective/Materials/Procedure/Variables…)
├─ ✅ checklists/             # PR/release/ingest checklists
├─ 🛠️ runbooks/               # ops + incident + recovery runbooks
├─ 🏛️ governance/             # policies, permissions, safety, review rules
└─ 📚 knowledge_base/         # curated notes, reading summaries, research context
```

---

## 🚦Where do I put *this* doc?

| You are creating… | Put it in… | Why |
|---|---|---|
| 🧪 A new experiment write-up | `mcp/experiments/` *(or repo-level `experiments/`)* | searchable experiment history |
| 📋 A “do this every time” procedure | `mcp/protocols/` or `mcp/runbooks/` | repeatability |
| 🤖 A model / prompt definition | `mcp/model_cards/` | transparency + evaluation |
| ✅ A quality gate | `mcp/checklists/` | prevents drift |
| 🏛️ A policy / rule | `mcp/governance/` | accountability |

---

## 🧪 Experiments (minimum bar)

Every meaningful experiment should be written up as a **version-controlled report**.

### ✅ Naming convention

- `EXP-001_short-title.md`
- `EXP-002_place-name-extraction-spacy-vs-regex.md`
- If time-based naming is helpful: `EXP-2026-01-28_short-title.md`

### 🧾 Minimum required sections (report)

- **Goal / Question**
- **Data used** (with identifiers, versions, hashes where possible)
- **Method** (steps + parameters + code entrypoints)
- **Results** (tables/figures + where artifacts are stored)
- **Interpretation**
- **Next steps**
- **Repro steps** (exact commands, environment notes)

> Tip: If you track artifacts/metrics (e.g., DVC), always link the artifact IDs in the report.

---

## 🧬 Protocols (Scientific Method “before you run it”)

Before running something “for real”, write the protocol. The protocol is the contract that makes reproduction possible.

### Protocol template fields (minimum)

- 🎯 **Objective**
- 🧰 **Materials / Tools**
- 🧪 **Procedure**
- 🧷 **Variables** (what changes, what’s controlled, what’s measured)
- 📈 **Expected outcome**
- 🧯 **Risks / failure modes** (what could break and how we’ll notice)

---

## 🤖 Model Cards (AI + ML)

If an AI component is **deployed**, **user-facing**, **decision-influencing**, or **used repeatedly**, it needs a model card.

### ✅ What a model card should include

- **Purpose / intended use**
- **Not intended use**
- **Training / tuning data notes** (what, where from, known limitations/biases)
- **Evaluation results** (overall + scenario-based)
- **Safety & ethics notes** (bias risks, sensitive data handling)
- **Operational details** (how to run, hardware notes, how it’s versioned)
- **Change log** (what changed since last version)

> Keep model cards honest: *what it can’t do* matters as much as what it can.

---

## 🧾 Provenance & versioning rules of thumb

### Golden rules 🥇

1. **Every artifact has provenance** (inputs, transforms, outputs).
2. **Git is the source of truth** for structured metadata + provenance records.
3. If the DB cache can’t be rebuilt from repo state, it’s a bug (or a missing doc).
4. **Cite versions** (commit hash / tag) when sharing results.

---

## ✅ Quality gates (don’t skip)

### Testing & review

- Unit tests where possible ✅  
- Integration checks for pipelines ✅  
- Peer review for major experiments ✅  
- CI must be green before merge ✅

### Reproducible coding habits

- Set random seeds when applicable 🎲
- Log parameters + environment 🔎
- Avoid “mystery notebook state” (make notebooks runnable end-to-end) 📓

---

## 🔁 Living documentation (docs don’t drift)

Documentation must be treated as a **first-class deliverable**:

- Update docs in the **same commit/PR** as the code change whenever possible.
- Reviewers should check docs as part of code review.
- Do periodic doc audits (monthly / per sprint) and file issues for gaps.

---

## ✅ Copy-paste starter templates (recommended set)

If these don’t exist yet, create them as you need them:

- `mcp/templates/experiment_report.md`
- `mcp/templates/protocol.md`
- `mcp/templates/model_card.md`
- `mcp/templates/dataset_datasheet.md`
- `mcp/templates/runbook.md`
- `mcp/templates/checklist_pr.md`

---

## 📚 Project reading shelf (curated PDFs)

Use these as background references when writing protocols, experiments, and model cards:

- 🗺️ GIS & mapping: projections, map design, geocomputation, remote sensing
- 📊 Data viz & stats: time-oriented visualization, statistics & experimental design
- 🧱 Data systems: database performance at scale, scalable data management
- 🤖 AI ops: local LLM runtime + model inventories (Ollama-focused materials)

*(Keep deeper notes/summaries in `mcp/knowledge_base/`.)*

---

## 🙌 Contribution checklist (fast)

<details>
  <summary><strong>✅ MCP PR checklist (click to expand)</strong></summary>

- [ ] I added/updated the relevant **docs** for my change  
- [ ] I added/updated an **experiment report** (if I ran one)  
- [ ] I added/updated a **model card** (if I changed an AI component)  
- [ ] I linked to **artifacts/metrics** (if generated)  
- [ ] I included **repro steps**  
- [ ] CI is green  
- [ ] No pipeline shortcuts introduced

</details>

---

## 🔗 Related (repo-level) docs to cross-link

- `docs/architecture/` (system overview & boundaries)
- `data/` (sources, processed outputs, catalogs, provenance)
- `experiments/` (if experiments live at repo root)

---

## 🧠 Closing note

MCP is how we scale trust:  
**repeatable work → reviewable work → trustworthy work**. 🧾✅