# 📚 MCP Knowledge Base (KFM)  
![MCP](https://img.shields.io/badge/MCP-knowledge_base-blue) ![Docs](https://img.shields.io/badge/documentation-first-informational) ![Evidence](https://img.shields.io/badge/evidence--backed-required-success) ![Repro](https://img.shields.io/badge/reproducible-workflows-brightgreen) ![Ethics](https://img.shields.io/badge/FAIR%2FCARE-ethically_grounded-purple)

Welcome to the **MCP Knowledge Base** for **Kansas Frontier Matrix (KFM)** 🧭🗺️  
This folder is the project’s **living, evidence-backed memory**: the place where we store *what we know*, *how we know it*, and *how to reproduce it* — in a form usable by both **humans** and **AI tooling** 🤖📌

---

## 🎯 What this is for

The Knowledge Base exists to:

- **Capture background research** (papers, books, archival notes, GIS/cartography standards) 📚
- **Define shared vocabulary** via a living **Glossary** 📖
- **Document repeatable workflows** via **SOPs** (Standard Operating Procedures) ✅
- **Standardize evidence + provenance** rules (citations, dataset notes, chain-of-custody) 🔍
- **Support MCP workflows** (experiments, model cards, traceability) 🧪🧾
- **Feed retrieval / RAG** safely (small, well-scoped pages with citations) 🧠

> 💡 Rule of thumb: if someone might ask “**why**?” or “**how did you do that**?”, the answer belongs in the Knowledge Base.

---

## 🧭 How to use this folder

### For humans 👩‍🔬👨‍💻
- Start with the **Glossary** if a term is unclear.
- Use **SOPs** to run repeatable tasks (ingest, georeference, QC, deploy).
- Link relevant KB pages inside:
  - experiment reports (`/experiments/`)
  - model cards (`/mcp/model_cards/`)
  - docs (`/docs/`)

### For AI / MCP agents 🤖
- Treat each KB page as a **citation-capable fact unit**.
- Prefer **small pages** over mega-docs.
- Keep pages **self-contained**, with:
  - clear claims
  - linked evidence
  - “known limits / uncertainty”
  - reproducible steps (when applicable)

---

## 🗂️ Recommended structure

> ✅ You can create these folders gradually. The Knowledge Base is meant to grow iteratively.

```text
📁 mcp/
└─ 📁 knowledge_base/                          🧠 project knowledge base (how we think + how we work)
   ├─ 📄 README.md                              👈 you are here
   ├─ 📄 index.md                               🧭 “start here” map of KB topics (recommended)
   ├─ 📁 glossary/                              📖 shared vocabulary & acronyms
   │  ├─ 📄 README.md                            📘 how the glossary is organized
   │  └─ 📁 terms/                               🗂️ individual term entries (one file per term)
   ├─ 📁 primers/                               🧠 short domain introductions (GIS, history, geology, etc.)
   ├─ 📁 sops/                                  ✅ Standard Operating Procedures (step-by-step workflows)
   ├─ 📁 templates/                             🧩 reusable docs (KB entry template, SOP template, etc.)
   ├─ 📁 provenance/                            🔍 citation rules, source registry, licensing notes
   ├─ 📁 ontologies/                            🧬 controlled vocabularies, schemas, mappings, IDs
   ├─ 📁 gazetteer/                             📍 place-name standards + NER support notes
   ├─ 📁 timelines/                             ⏳ time-model notes (periodization, uncertainty, date rules)
   └─ 📁 decisions/                             🏛️ ADR-style architecture decisions + governance notes
```

---

## 🔗 How this connects to the rest of the repo

- **Experiments** (`../../experiments/`) 🧪  
  Every meaningful test or analysis should reference:
  - KB background pages (literature + assumptions)
  - SOPs used
  - datasets + provenance notes

- **Model Cards** (`../model_cards/`) 🧾  
  Any ML / LLM behavior we rely on must be documented with:
  - scope & intended use
  - limitations
  - evaluation notes
  - known failure modes

- **Data catalogs & provenance** (`../../data/…`) 🧱  
  The KB describes the *rules*, while data catalogs store the *instances* (sources, processed outputs, metadata).

---

## 🧪 Canonical pipeline rule

KFM features should follow the canonical flow:

> **Raw → Processed → Catalog/Provenance → Database → API → UI** 🔁

This Knowledge Base supports that rule by storing:
- the **SOPs** for each stage
- the **evidence requirements**
- the **definitions + standards** used by catalogs and schemas

---

## ✅ Quality bar (required)

Before adding or merging a KB change, confirm:

- [ ] **Evidence-backed**: claims are supported by citations, links, or reproducible outputs  
- [ ] **Reproducible**: steps include commands, parameters, and expected outputs (where applicable)  
- [ ] **Scoped**: page answers one question or one workflow (avoid “everything pages”)  
- [ ] **Traceable**: points to data artifacts, experiment IDs, commits, or source registers  
- [ ] **Readable**: clear headings, short paragraphs, minimal jargon  
- [ ] **Ethically grounded**: respects community control, sensitive data handling, FAIR/CARE intent  

---

## 🧩 Templates

Put reusable docs in `templates/` ✍️

Suggested templates to create:

- `templates/kb_entry.md` 🧠
- `templates/sop.md` ✅
- `templates/glossary_term.md` 📖
- `templates/adr.md` 🏛️
- `templates/source_record.md` 🔍

---

## 🧾 Citation & evidence style

We prefer **primary sources** and **verifiable artifacts**:

- 📚 Primary: academic books/papers, archival scans, authoritative datasets  
- 🧱 Artifacts: shapefiles, GeoTIFFs, logs, notebooks, experiment outputs  
- 🧾 Documentation: SOPs, model cards, ADRs, provenance registers

**Do:**
- Cite *what you actually used*
- State uncertainty explicitly
- Record parameters and versions

**Avoid:**
- Unsourced historical claims
- “Trust me” georeferencing steps
- Unlogged manual edits

---

## 🧠 Writing a new Knowledge Base entry

Create a new page (example: `primers/georeferencing.md` or `timelines/date_uncertainty.md`) and include:

1. **Purpose** (what question this answers)
2. **Key claims / rules**
3. **Sources / citations**
4. **How to verify**
5. **Known limitations**
6. **Links out** (SOPs, experiments, datasets)

---

## 🔐 Sensitive data & community ethics

KFM is community-facing and historically grounded 🫱🏽‍🫲🏻  
When documenting sources or datasets:

- Respect **access constraints** and cultural sensitivity
- Avoid publishing private or restricted information
- Prefer **tiered access notes** (public vs restricted vs internal)
- Document why something is restricted, and how to request access

---

## 🗓️ Changelog

Track major KB changes here (or in a repo-level changelog).  
Example format:

- `YYYY-MM-DD` — Added SOP for georeferencing scans ✅
- `YYYY-MM-DD` — Added glossary expansion for cartographic terms 📖

---

## 🙌 Contribution mindset

This knowledge base is never “done.” It grows with every:
- experiment 🧪
- new source 📚
- mapping layer 🗺️
- methodological improvement 🔧

If you’re unsure where something belongs, add it here first — then refactor later ✨

