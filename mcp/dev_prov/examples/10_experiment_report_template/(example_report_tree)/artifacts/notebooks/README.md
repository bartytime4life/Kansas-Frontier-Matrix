---
title: "📓 Notebooks (Artifacts) — Experiment Report Template"
scope: "mcp/dev_prov/examples/10_experiment_report_template/(example_report_tree)/artifacts/notebooks"
status: "template"
---

<div align="center">

# 📓 Notebooks (Artifacts) — Experiment Report Template

**This folder contains the *executed, provenance-backed notebooks* that generated the figures/tables/data referenced by the experiment report.**

![Template](https://img.shields.io/badge/template-✅-success)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Reproducible](https://img.shields.io/badge/reproducible-🔁-blue)
![Provenance](https://img.shields.io/badge/provenance-PROV--O-7b2cbf)
![FAIR+CARE](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-0b7285)

</div>

---

## 🧭 What belongs here?

KFM treats notebooks as **living documentation** and an on-ramp from exploration → repeatable pipelines.  [oai_citation:0‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

In this *experiment report* template, the notebooks in `artifacts/notebooks/` should be:

- ✅ **Directly tied to report claims** (a figure, a table, a derived dataset, a metric).
- ✅ **Runnable top-to-bottom** (no hidden state), per MCP reproducibility guidance.  [oai_citation:2‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- ✅ **Provenance-first**: everything outputs a run manifest + PROV so we can answer “what produced what, with which inputs + assumptions?”  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:4‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

> 💡 Why? KFM’s core trust rule is contract-first + provenance-first: anything shown to users (UI / reports / Focus Mode) must be traceable back to cataloged sources—no “mystery layers.”  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🗂️ Directory contract (recommended)

```text
(example_report_tree)/
  🧾 report.md
  📦 artifacts/
    📓 notebooks/
      README.md
      NB-001__<short_slug>.ipynb
      NB-001__<short_slug>.run_manifest.json
      NB-001__<short_slug>.prov.jsonld
      NB-001__<short_slug>.evidence.yml   (optional but 🔥)
      NB-002__...
    🖼️ figures/
    📊 tables/
    🧱 data/
    🧰 logs/
```

### 🔗 Outputs should land *outside* the notebook folder
Keep the notebook folder “thin”: notebooks + their sidecars. Put actual deliverables in `../figures`, `../tables`, `../data`, and reference them from the report.

---

## 🧪 Notebook types we expect (and why)

| Type | Purpose | When to “graduate” it |
|---|---|---|
| 🔎 EDA / sanity | Understand shape, quality, outliers, joins | When the steps stabilize and should be automated |
| 🧼 Data QC / validation | Enforce contract assumptions; produce QA artifacts | When you need CI to enforce it continuously  [oai_citation:7‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) |
| 🧠 Model / analysis | Derive metrics, train/evaluate, run statistical tests | When it becomes a repeatable pipeline; optionally PR-first outputs  [oai_citation:8‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) |
| 🗺️ Geo visualization | Map overlays, temporal slices, story-ready visuals | When it becomes a reusable “story node kit”  [oai_citation:9‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) |
| 🧾 Report reproduction | One-button regeneration of report figures/tables | Always keep one of these if the report makes claims |

KFM explicitly expects notebooks to be used for exploratory analyses and prototypes, and encourages running them in CI to ensure they execute from scratch.  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🏷️ Naming conventions (keep it boring ✨)

### Notebook filename
- `NB-###__short_slug.ipynb`  
  Example: `NB-010__drought_index_validation.ipynb`

### Sidecars (same basename)
- `NB-010__drought_index_validation.run_manifest.json`
- `NB-010__drought_index_validation.prov.jsonld`
- `NB-010__drought_index_validation.evidence.yml` *(optional but strongly encouraged)*  [oai_citation:11‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

> 📌 Tip: Use emoji shortcodes sparingly in markdown docs (GFM supports them), and don’t over-style notebooks.  [oai_citation:12‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

---

## ✅ “Must-have” reproducibility rules

These rules mirror the project’s Scientific Method + Master Coder Protocol emphasis on **traceable, repeatable experiments**.  [oai_citation:13‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

### 1) Determinism (when possible)
- Set random seeds and record them.  [oai_citation:14‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- If something is *not* deterministic (GPU kernels, stochastic training), **document drift tolerances**.

### 2) Environment pinning
- Record tool + library versions (or a container digest).  [oai_citation:15‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

### 3) No hidden state
- Run all cells in order; avoid “works on my kernel.”  [oai_citation:16‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

### 4) Inputs/outputs are explicit
KFM’s intake + modeling workflows emphasize pinning inputs (hashes), capturing parameters, pinning environments, and recording seeds.  [oai_citation:17‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧾 Provenance: what to emit (minimum viable)

KFM operates on **open standards** (STAC/DCAT/PROV) and requires provenance to persist from raw inputs → derived outputs.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:19‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### ✅ Required: `run_manifest.json`
A run manifest is a structured audit trail: who/what/when, inputs/outputs, tool versions, and a canonical digest / idempotency key pattern.  [oai_citation:20‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

**Minimal skeleton (example):**
```json
{
  "run_id": "RUN-2026-01-22T12-34-56Z__NB-010",
  "notebook": "NB-010__drought_index_validation.ipynb",
  "run_time": "2026-01-22T12:34:56Z",
  "inputs": [
    {"id": "dcat:dataset/...", "sha256": "...", "notes": "pinned"}
  ],
  "outputs": [
    {"path": "../figures/fig_010_drought_trend.png", "sha256": "..."}
  ],
  "tool_versions": {"python": "3.x", "geopandas": "x.y.z"},
  "random_seeds": {"python": 42, "numpy": 42},
  "canonical_digest": "sha256:..."
}
```

### ✅ Required: `prov.jsonld`
At minimum, connect:
- `prov:Entity` (inputs, outputs)
- `prov:Activity` (the notebook run)
- `prov:Agent` (author / runner / CI)

This is the same “receipt” approach used for story/evidence linkage: statements and outputs are graph-traversable, not just text blobs.  [oai_citation:21‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### ⭐ Optional (but recommended): `evidence.yml`
Evidence manifests formalize citations/sources in a machine-readable way (checksums, query params, timestamps), enabling audit + re-run.  [oai_citation:22‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧰 “Notebook header” template (copy/paste)

Put this **as the first Markdown cell** in every notebook:

```markdown
# NB-### — <Title>

## 🎯 Goal
- Question / hypothesis:
- Why it matters (1–2 lines):

## 📦 Inputs (Pinned)
- Dataset(s): <IDs/paths + hash/digest>
- Time window / AOI:
- Sensitivity tags (if any):

## 🔁 Method
- Steps (high level):
- Key parameters:
- Expected outputs:

## 🧾 Provenance
- run_manifest: `NB-###__<slug>.run_manifest.json`
- prov bundle: `NB-###__<slug>.prov.jsonld`
- evidence manifest (optional): `NB-###__<slug>.evidence.yml`

## ✅ Repro notes
- Seeds:
- Environment pin:
- Known non-determinism + tolerances:
```

This aligns with the project’s scientific-method discipline: define the problem, methods, data collection, analysis, results, and conclusions.  [oai_citation:23‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🚀 Running notebooks (local + “one-click”)

### Local
- Execute notebooks *from the report root* (so relative output paths land in `artifacts/` cleanly).
- Prefer “restart kernel + run all” for correctness.

### One-click / education mode (KFM vision)
KFM aims for “Open in Notebook” style flows via **JupyterHub/Binder**, letting users launch notebooks with data + libraries preloaded.  [oai_citation:24‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
This template keeps that door open by enforcing:
- deterministic runs,
- pinned inputs,
- portable paths,
- provenance sidecars.

---

## 🔁 Promotion path: notebook → pipeline (when it’s ready)

Notebooks are often the **first step** toward a formal pipeline or scheduled job; once validated, convert into scripts/pipelines and run via CI.  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

KFM’s intake tooling also anticipates template-driven pipeline generation (cookiecutter-style), with standard structure, CLI, and tests.  [oai_citation:26‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

> 🧠 Pattern match: KFM’s “PR-first modeling” treats model outputs like code contributions (a run can open a PR with outputs + PROV for review).  [oai_citation:27‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🔐 Governance & safety (FAIR + CARE)

KFM governance requires:
- mandatory metadata + provenance,
- explicit handling of sensitive data,
- policy-as-code gates in CI.  [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:29‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Sensitive geo data
If a notebook touches sensitive locations, consider **generalization/obfuscation** (e.g., rounding coordinates) and document the rule in outputs + provenance.  [oai_citation:30‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

---

## 📦 Optional: OCI artifact packaging (advanced 🔥)

If your notebook produces heavy artifacts (PMTiles, GeoParquet, COGs), KFM explores storing them in OCI registries via **ORAS**, verified via **Cosign**, referenced by immutable digests.  [oai_citation:31‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

- ORAS push/pull workflows and keyless Cosign signing are described as a reproducibility + integrity layer.  [oai_citation:32‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- Catalog records can include OCI distribution entries so artifacts remain discoverable via STAC/DCAT metadata.  [oai_citation:33‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧩 UI + narrative alignment (when notebooks feed stories)

KFM’s UI includes story-driven exploration (Story Nodes) and emerging “Pulse Threads” concepts; both benefit from evidence manifests and PROV.  [oai_citation:34‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  [oai_citation:35‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

If your notebook supports a narrative claim, consider outputting:
- `evidence.yml` for sources + transformations,  [oai_citation:36‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- a compact PROV fragment that links claims → evidence items.  [oai_citation:37‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## ✅ PR checklist (fast but strict)

- [ ] Notebook runs **restart + run all** cleanly.
- [ ] Outputs are written to `../figures`, `../tables`, `../data` (not sprinkled around).
- [ ] `run_manifest.json` exists + lists inputs/outputs + versions + seeds.  [oai_citation:38‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- [ ] `prov.jsonld` exists + links entities/activities/agents.
- [ ] Sensitive content is tagged and handled appropriately.  [oai_citation:39‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] If this notebook is now “stable,” open an issue/PR to convert it into a pipeline.  [oai_citation:40‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 📚 Source pack (project files used to design this README)

> These documents define the philosophy and mechanics behind notebooks-as-artifacts, provenance-first reporting, and KFM’s reproducible workflows.

- 🧭 **KFM AI System Overview** (JupyterHub/Binder, PR-first modeling).  [oai_citation:41‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:42‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- 🏛️ **KFM Comprehensive Architecture / Features / Design** (notebooks as prototypes; CI execution; binder/JupyterHub integration).  [oai_citation:43‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- 📥 **KFM Data Intake – Technical & Design Guide** (provenance-first philosophy; sims + promotion; reproducibility rules).  [oai_citation:44‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:45‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- 🧾 **KFM Comprehensive Technical Documentation** (contract-first + provenance-first; STAC/DCAT/PROV; no mystery layers).  [oai_citation:46‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- 🗺️ **KFM Comprehensive UI System Overview** (story nodes & narrative UI context).  [oai_citation:47‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- 🌟 **Latest Ideas & Future Proposals** (reproducible research integration + one-click environments).  [oai_citation:48‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- 💡 **Innovative Concepts to Evolve KFM** (AR/4D digital twin ideas; cultural protocols; sensitivity-aware handling).  [oai_citation:49‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  [oai_citation:50‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- 🧪 **Scientific Method / Research / Master Coder Protocol** (experiment structure; determinism; notebooks best practices).  [oai_citation:51‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  [oai_citation:52‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- 🧱 **Open-Source Geospatial Historical Mapping Hub Design** (notebooks as living documentation).  [oai_citation:53‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)
- 🧠 **Additional Project Ideas** (evidence manifests; run manifests; OCI artifacts; policy gates; pulse threads).   [oai_citation:54‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:55‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- ✍️ **Comprehensive Markdown Guide (docx)** (emoji + front-matter + advanced GFM patterns).  [oai_citation:56‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- 📚 **AI Concepts & more (PDF portfolio)** (background reading bundle; open via Acrobat/Reader).  [oai_citation:57‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- 🧰 **Various programming languages & resources (PDF portfolio)** (background reading bundle; open via Acrobat/Reader).  [oai_citation:58‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
- 🗺️ **Maps / GoogleMaps / VirtualWorlds / Archaeological / WebGL (PDF portfolio)** (visualization references; open via Acrobat/Reader).  [oai_citation:59‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- 🧮 **Data Management / Architectures / Bayesian / Programming Ideas (PDF portfolio)** (background reading bundle; open via Acrobat/Reader).  [oai_citation:60‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
- ⛏️ **Data Mining Concepts & Applications** (dynamic data + repeatable mining considerations).  [oai_citation:61‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)
- 🐍 **Python Geospatial Analysis Cookbook** (PostGIS/GeoJSON patterns useful for geo notebooks).  [oai_citation:62‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

---

<details>
<summary>🧠 Bonus: “Pulse Threads” & conceptual lenses (future-facing)</summary>

KFM’s “Pulse Threads” aim to publish short, geotagged narratives tied to real data events, backed by evidence manifests and provenance.  [oai_citation:63‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
“Conceptual Attention Nodes” add a theme-layer (“drought”, “biodiversity”, etc.) that can guide analysis + UI filtering and make AI reasoning more transparent.  [oai_citation:64‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

If your experiment report is meant to become a story, this folder’s notebook outputs are the *receipts* that make that story trustworthy. 🧾✨

</details>
