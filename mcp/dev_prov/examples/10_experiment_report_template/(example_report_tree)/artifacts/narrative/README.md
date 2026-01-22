# 🧾 Narrative Artifact (Experiment Report) — README

![Provenance First](https://img.shields.io/badge/Provenance--First-✅-informational)
![Evidence](https://img.shields.io/badge/Evidence--First-📎-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-🧭-success)
![STAC/DCAT/PROV](https://img.shields.io/badge/STAC%20%2F%20DCAT%20%2F%20PROV-🛰️-purple)
![No Black Boxes](https://img.shields.io/badge/No%20Black%20Boxes-🚫-critical)

Welcome to `artifacts/narrative/` ✍️ — the **human-readable story** of the experiment.  
This narrative is **not** a vibe-check blog post; it’s the *auditable explanation* that connects *question → method → results → decision* with **evidence links** and **provenance**.

> [!IMPORTANT]
> KFM’s ethos is strict: **no unsourced outputs** (including narratives and AI text). If it can’t be cited, it shouldn’t ship.  [oai_citation:0‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 📦 What lives in this folder?

Typical contents (adjust as needed):

```text
📁 artifacts/
  └─ 📁 narrative/
     ├─ 📄 README.md                 # you are here
     ├─ 📄 report.md                 # main narrative report (required)
     ├─ 📄 executive_summary.md      # optional: 1–2 pages for stakeholders
     ├─ 📄 decisions.md              # optional: key calls + why
     └─ 📄 changelog.md              # optional: narrative edits over time
```

This folder should **reference** (not duplicate) other artifacts:
- 📁 `artifacts/data/` (raw/processed outputs)
- 📁 `artifacts/metrics/` (tables, scores, evals)
- 📁 `artifacts/figures/` (plots, screenshots)
- 📁 `artifacts/prov/` (PROV bundles)
- 📁 `artifacts/evidence/` (evidence manifest YAML)
- 📁 `artifacts/catalog/` (STAC/DCAT records)

KFM’s standard “evidence triplet” pattern is **STAC + DCAT + PROV** for what you produced and how it was produced.  [oai_citation:1‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧠 Narrative rules (KFM-style)

### 1) Evidence-first (always)
- **Raw inputs are immutable evidence**; do not rewrite them in-place.  [oai_citation:2‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **Deterministic, config-driven ETL** only (no “manual mystery edits”).  [oai_citation:3‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- Every claim that matters should point to *something concrete*: dataset IDs, run IDs, file hashes, citations, screenshots, or query receipts.

### 2) “Fail closed” governance
KFM enforces **policy gates** (schema validation, STAC/DCAT/PROV completeness, license presence, sensitivity classification, provenance completeness).  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
Your narrative should explicitly note any gate failures, waivers, or exceptions—and *why*.

### 3) AI text ≠ magic (label it & cite it)
Focus Mode is designed to be **advisory-only** and **always cites sources**; if it can’t cite, it should refuse/express uncertainty.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
Architecturally, a typical pipeline is: `Question → Retrieval → LLM draft → Governance check → AnswerWithCitations`.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

> [!TIP]
> If you used any AI help (summaries, labeling, extraction), write it down and include the **evidence trail** (inputs used + output review), so it stays auditable.  [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧪 What the narrative MUST cover (Scientific Method alignment)

Use this as the minimum skeleton. It maps cleanly to the required scientific-method documentation steps.  [oai_citation:8‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

### ✅ Required sections (for `report.md`)
1. **Question / Problem Statement**
2. **Background**
3. **Hypothesis / Expectations**
4. **Experimental Design (Methods)**
5. **Execution Notes (what actually happened)**
6. **Data Collection & Labeling**
7. **Analysis**
8. **Results**
9. **Conclusion**
10. **Limitations / Risks / Ethics**
11. **Next Steps**

---

## 🧷 Provenance hookups (how to link narrative ↔ artifacts)

### A) Add report front-matter (recommended)
Put this at the top of `report.md`:

```yaml
---
report_id: EXP-000
title: "Short, specific, testable title"
date: 2026-01-22
status: draft            # draft | review | published
owners: ["@you", "@team"]
run_ids: ["run-20260122-1230Z"]
scope:
  subsystem: "ingestion|ui|ai|graph|pipeline|policy"
  region: "Kansas"
evidence:
  manifest: ../evidence/EM-000.yaml
  prov_bundle: ../prov/PROV-EXP-000.jsonld
  stac_items: ["stac:item:kfm.example.asset.v1"]
  dcat_datasets: ["dcat:kfm.example.dataset.v1"]
policy:
  gates_run: true
  exceptions: []
---
```

Why: KFM treats narratives as first-class, governed artifacts, and expects cross-links into evidence/provenance.  [oai_citation:9‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### B) Evidence Manifest (required when claims matter)
Pulse/Story patterns in KFM emphasize an **evidence manifest** listing the raw references (IDs, query params, timestamps, checksums) behind the narrative.  [oai_citation:10‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

Minimum example (`artifacts/evidence/EM-000.yaml`):

```yaml
id: EM-000
for_report: EXP-000
evidence:
  - id: E-001
    type: dataset
    ref: dcat:kfm.example.dataset.v1
    query: "SELECT count(*) WHERE condition=true"
    timestamp_utc: "2026-01-22T12:30:00Z"
    checksum: "sha256:..."
    note: "Used for baseline count"
  - id: E-002
    type: figure
    ref: ../figures/F-001.png
    checksum: "sha256:..."
    note: "Shows pre/post comparison"
```

This gives reviewers a compact “what backs this?” inventory (similar to Story Node evidence patterns).  [oai_citation:11‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🗺️ If your narrative is map/story driven (Story Nodes style)

KFM story content is commonly created via **Markdown + JSON** (with templates), reviewed via Git, and checked for correct references and citations.  [oai_citation:12‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
Stories synchronize narrative steps with map state (pan/zoom, layers, timeline).  [oai_citation:13‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

> [!NOTE]
> If you are building a “story-like” experiment report, keep the narrative readable, but still make every factual claim traceable.  [oai_citation:14‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

---

## ⚡ If your narrative is time-sensitive (Pulse Threads style)

If the experiment produces timely, location-linked insights, consider a Pulse-like write-up:
- geotagged to places/regions
- linked into the graph (`:PulseThread` → `:Place/:Region/:Dataset`)
- shipped with provenance + evidence manifest so users can drill down.  [oai_citation:15‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧯 If this experiment involved sims/models (sandbox → promotion)

KFM simulation workflows emphasize:
- sandbox runs in a workbench area (not “official”)
- promotion only after review
- promotion requires STAC/DCAT/PROV, stable IDs, sensitivity review, no bypassing to UI.  [oai_citation:16‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
And a reproducibility checklist (pin inputs/hashes, capture params, pin environment, record seeds, verify/validate).  [oai_citation:17‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🤖 Automation notes (Watcher–Planner–Executor alignment)

If the experiment used automation agents or CI:
- Watcher: records trigger/events as immutable alerts
- Planner: produces a structured, reviewable plan
- Executor: opens PRs / runs steps, but routes through review & policy gates.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
This pattern supports safe, auditable maintenance and updates.  [oai_citation:19‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🔐 Optional (but 🔥): artifact integrity via OCI registry

For large or externalized artifacts, KFM proposals include storing artifacts in an OCI registry (ORAS) and signing them (Cosign), keeping provenance attachable and verifiable.  [oai_citation:20‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## ✅ PR-ready checklist (quick sanity)

Before you mark the report “review”:
- [ ] Question + hypothesis are explicit.  [oai_citation:21‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- [ ] Methods are reproducible; deviations documented.  [oai_citation:22‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- [ ] Results link to artifacts (metrics/figures/data).  [oai_citation:23‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- [ ] Evidence Manifest exists for key claims.  [oai_citation:24‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- [ ] PROV exists and points to inputs + activities.  [oai_citation:25‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- [ ] Policy gates passed (or exceptions documented).  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- [ ] Any AI assistance is labeled + backed by citations.  [oai_citation:27‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

---

## 🧭 Helpful repo orientation (where this fits)

KFM’s documented layout expects **MCP** (Methods & Computational Experiments) to live under `mcp/`, and data domains + catalogs/provenance to live in standard places (raw/work/processed + STAC/DCAT/PROV).  [oai_citation:28‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

### 🏁 Bottom line

A great narrative makes it effortless to answer:
- **What did we try?**
- **Why did we try it?**
- **What happened?**
- **Can someone else reproduce it?**
- **Should we ship it / promote it / roll it back?**

…and it does so with **receipts** 🧾.
