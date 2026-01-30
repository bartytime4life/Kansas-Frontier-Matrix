<!--
📌 File: docs/reports/README.md
🧭 Purpose: Explain what belongs in docs/reports/ (especially Story Nodes) and how it stays governed + evidence-first.
-->

# 🧾 `docs/reports/` — Governed Reports & Story Nodes

![status](https://img.shields.io/badge/status-governed-blue)
![pipeline](https://img.shields.io/badge/pipeline-evidence--first-success)
![content](https://img.shields.io/badge/content-story%20nodes%20%26%20reports-purple)
![review](https://img.shields.io/badge/review-required-orange)

> **This folder is for governed, reviewable narrative + reporting artifacts.**  
> In KFM, narrative is not “freeform docs” — it is **pipeline-attached** and **provenance-linked**.

---

## 🧭 Table of contents

- [📌 What lives here](#-what-lives-here)
- [🔒 Non-negotiables](#-non-negotiables)
- [🗂️ Folder layout](#️-folder-layout)
- [🧠 Story Nodes](#-story-nodes)
  - [✨ Create a new Story Node](#-create-a-new-story-node)
  - [📚 Citations & evidence linking](#-citations--evidence-linking)
  - [🖼️ Assets](#️-assets)
  - [🚦 Draft → Published promotion](#-draft--published-promotion)
- [🧪 “Reports” vs “Evidence Artifacts”](#-reports-vs-evidence-artifacts)
- [✅ Definition of Done](#-definition-of-done)
- [🔗 Related docs](#-related-docs)

---

## 📌 What lives here

### ✅ Primary (canonical)
- **Story Nodes** → governed narrative content that is **machine-ingestible** and **provenance-linked** (used by the UI and Focus Mode).

### ✅ Allowed (when needed)
- **Human-readable reports** that summarize or interpret *already-published evidence artifacts* (datasets, derived layers, model outputs), as long as:
  - they **link** to the cataloged artifacts (STAC/DCAT/PROV), and
  - they **do not bypass** the pipeline (no “new facts” without sources).

> 💡 Think of `docs/reports/` as the “story + explanation layer” — **never the place where raw/processed data is born.**

---

## 🔒 Non-negotiables

These are “hard rules” for anything placed under `docs/reports/`:

1. **Pipeline ordering is absolute**  
   `ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode`

2. **Evidence-first narrative**  
   No unsourced narrative content. Every meaningful claim must cite evidence (dataset IDs, catalog entries, primary sources).

3. **Provenance-first**  
   If you reference a derived dataset (analysis output / AI output), it must have provenance (PROV) and catalog records (DCAT + STAC when applicable).

4. **Governance applies**  
   If content involves sensitive topics, sovereignty concerns, private locations, or culturally sensitive data:
   - label it appropriately in the doc front-matter (per templates),
   - route it through the correct reviewers.

---

## 🗂️ Folder layout

Current canonical layout (v13-style):

```text
docs/reports/
├── README.md
└── story_nodes/
    ├── templates/
    ├── draft/
    │   └── <story_slug>/
    │       ├── story.md
    │       └── assets/
    └── published/
        └── <story_slug>/
            ├── story.md
            └── assets/
```

### 🧩 Conventions
- `<story_slug>` = **kebab-case** and stable (e.g., `dust-bowl-1930s`, `chisholm-trail`).
- Keep **one story per folder**.
- Avoid renaming slugs after publication unless you also update all references and UI bindings.

---

## 🧠 Story Nodes

Story Nodes are governed narratives intended to be **rendered and navigated** (not just read).  
They should be written to support:
- human reading ✅
- machine parsing ✅ (front-matter + structured sections)
- traceability ✅ (citations linked to cataloged evidence)

### ✨ Create a new Story Node

1. Pick a slug:
   - `my-topic-title` ✅
   - `My Topic Title` ❌

2. Create the draft folder:
   - `docs/reports/story_nodes/draft/<story_slug>/`

3. Copy the Story Node template into:
   - `docs/reports/story_nodes/draft/<story_slug>/story.md`

4. Add assets (if needed):
   - `docs/reports/story_nodes/draft/<story_slug>/assets/`

5. Link to evidence:
   - Use citations/footnotes and reference stable IDs (dataset IDs, STAC item/collection IDs, DCAT entries, PROV bundles, archival sources).

> 🧷 Tip: Treat the template as a contract. Don’t invent new fields — extend templates through the governed process.

---

### 📚 Citations & evidence linking

A Story Node is only as strong as its evidence.

Use **at least one** of the following for each factual claim:
- Footnotes (`[^1]`) that point to:
  - dataset identifiers
  - catalog entries (DCAT)
  - STAC Items/Collections
  - PROV run bundles / lineage docs
  - authoritative primary sources (archival scans, official docs, etc.)

Recommended citation patterns:
- **Dataset-backed claim** → cite the dataset’s DCAT entry + link to the artifact
- **Map/layer-backed claim** → cite STAC Item/Collection
- **Derived/AI claim** → cite the derived dataset + the PROV activity that produced it

> ⚠️ If you can’t cite it, don’t claim it.

---

### 🖼️ Assets

Store Story Node assets **next to the story**:

- `.../<story_slug>/assets/`

Examples:
- images (`.png`, `.jpg`, `.svg`)
- small diagrams
- thumbnails
- figure exports that are referenced by `story.md`

Guidelines:
- Prefer **small + optimized** media.
- Use relative links in Markdown:
  - `![Alt text](assets/figure-01.png)`

---

### 🚦 Draft → Published promotion

**Draft** is for iterative writing and reviewer feedback.  
**Published** means “ready for the product.”

Promotion process (recommended):
1. Ensure the Story Node meets the [Definition of Done](#-definition-of-done).
2. Ensure required reviewers have approved (story + governance as needed).
3. Move the folder:
   - from: `docs/reports/story_nodes/draft/<story_slug>/`
   - to:   `docs/reports/story_nodes/published/<story_slug>/`
4. Update any indexes/manifests if the project maintains them (and any UI bindings if required).

> 🔁 Keep history in Git — never “rewrite” published narrative without a PR.

---

## 🧪 “Reports” vs “Evidence Artifacts”

It’s easy to confuse these:

### ✅ Reports (live here)
- human-readable explanation, interpretation, or narrative
- must **reference** evidence artifacts
- must remain **governed + citable**

### ✅ Evidence Artifacts (do **not** live here)
If you produce outputs like:
- derived datasets
- model runs
- simulations
- OCR text corpora
- AI-generated layers

They must be treated like **datasets**:
- stored under `data/processed/...`
- cataloged (STAC/DCAT)
- traced (PROV)
- only then referenced from Story Nodes or reports

> 🧠 Rule of thumb:  
> **Data goes to `data/…`** ✅  
> **Narrative about the data goes to `docs/reports/…`** ✅

---

## ✅ Definition of Done

Before merging or promoting to `published/`, confirm:

- [ ] **Front-matter is complete + valid** (use the template)
- [ ] **All claims link to evidence** (datasets, schemas, or authoritative sources)
- [ ] **Any described process is repeatable** (validation steps or reproduction notes included)
- [ ] **Governance concerns are explicitly addressed** (FAIR/CARE, sovereignty, sensitivity)
- [ ] **Assets render correctly** and paths are valid
- [ ] **No pipeline bypass** (no “new evidence” introduced only inside narrative)

---

## 🔗 Related docs

Use these as your “source of truth” references:

- 📘 `docs/MASTER_GUIDE_v13.md` (canonical structure + pipeline)
- 🧩 `docs/templates/`  
  - `TEMPLATE__KFM_UNIVERSAL_DOC.md`  
  - `TEMPLATE__STORY_NODE_V3.md`
- ⚖️ `docs/governance/` (ethics, sovereignty, review gates)
- 🏗️ `docs/architecture/` (blueprints, ADRs, system vision)
- 🧬 `schemas/` (STAC/DCAT/PROV + Story Node schemas)

---

### 🧯 If you’re unsure…

Open a PR early with a Draft Story Node and ask for:
- **Story review** (clarity + narrative structure)
- **Evidence review** (citations + provenance)
- **Governance review** (sensitivity + sovereignty)

💬 “Drafts are cheap. Provenance retrofits are expensive.”
