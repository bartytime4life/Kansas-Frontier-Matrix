# 🧪 MCP — Master Coder Protocol  
### *Methods & Computational Experiments* 🧾⚙️

![Docs-first](https://img.shields.io/badge/docs-documentation--first-blue)
![Reproducible](https://img.shields.io/badge/reproducible-audit--ready-success)
![Evidence](https://img.shields.io/badge/evidence-traceable-informational)
![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-orange)

> **TL;DR:** `mcp/` is the project’s **lab notebook + playbook** 📓🧠  
> It holds experiment reports, run receipts, SOPs, notebooks, and model cards—so every result can be **re-run, reviewed, and trusted** ✅

> [!IMPORTANT]
> In this repo, **MCP = Master Coder Protocol** (not “Model Context Protocol”).  
> Keep this distinction consistent in docs, PRs, and issues.

---

## 🧭 Quick Start (do this when you run anything “real”)

**Create an experiment report** 🧪  
- Add: `mcp/experiments/EXP-YYYY-MM-DD-<slug>.md`

**Create a run receipt** 🏃  
- Add: `mcp/runs/RUN-YYYY-MM-DD-<slug>/` with config, env snapshot, logs, metrics, and a `MANIFEST.md`

**Store evidence outputs elsewhere** 📦  
- Put artifacts in: `data/processed/...` (not in `mcp/`)
- Catalog + provenance: **STAC/DCAT/PROV** 🧾🧬

> **Bar:** “If I can’t reproduce it in 30 minutes, it’s not done.” ⏱️

---

## 🎯 Why this folder exists

Kansas Frontier Matrix (KFM) is built to be:

- **Evidence-first** 🧾
- **Reproducible** 🔁
- **Audit-ready** ✅
- **Human-reviewable** 👀

`mcp/` keeps the “how we did it” artifacts in one place:

- 🧪 **Experiments:** what we tried + why + what happened  
- 🏃 **Runs:** concrete run metadata/artifacts (configs, seeds, logs, metrics)  
- 🧰 **SOPs:** repeatable procedures for recurring tasks  
- 🧠 **Model Cards:** responsible documentation for ML models  
- 📓 **Notebooks:** exploratory work that should be readable & reproducible  
- 🧩 **Templates:** optional local templates (if not using `docs/templates/`)

If you’re new, start here:
- `../docs/MASTER_GUIDE_v13.md` 📌 *(canonical pipeline & repo structure)*
- `../CONTRIBUTING.md` 🤝 *(how to contribute safely & consistently)*

---

## 🗂️ Directory layout

```text
mcp/
├── README.md                 # you are here 👋
├── experiments/              # human-readable experiment reports 🧾
├── runs/                     # run artifacts + metadata (configs, logs, metrics) 🏃
├── sops/                     # Standard Operating Procedures (SOPs) 🧰
├── model_cards/              # model cards for any ML/AI used or trained 🧠
├── notebooks/                # exploratory notebooks (kept tidy & reproducible) 📓
└── templates/                # optional: local templates 🧩
```

> [!NOTE]
> **Rule of thumb:** `mcp/` documents *methods & decisions*.  
> **Data products** (including AI/analysis outputs) belong in `data/processed/...` and must be cataloged (STAC/DCAT/PROV).

---

## 🔁 The MCP workflow loop

When you do *anything* that affects evidence (data, analysis outputs, models), follow this loop:

1. **Ask a question** ❓ *(What are we trying to learn or improve?)*  
2. **Write the protocol** 🧾 *(What exactly will we do? Variables? Controls?)*  
3. **Run it** 🏃 *(Capture configs, versions, seeds, environment)*  
4. **Publish evidence artifacts** 📦 *(store outputs as datasets + catalogs + provenance)*  
5. **Write the report** 🧪 *(interpret results; record limitations & next steps)*  
6. **Review** ✅ *(someone else can reproduce it from your documentation)*

---

## ✅ Minimum required artifacts (for any “real” experiment)

When an experiment goes beyond a quick local poke, it must include:

- 🧾 **Experiment Report** in `mcp/experiments/…`
- 🏃 **Run Record** in `mcp/runs/…` *(or a link to an external run folder)*
- 🔗 **Code pointer:** commit hash + main entrypoint script/notebook
- 🧱 **Environment pointer:** Docker image tag/digest OR `requirements*.txt` / `environment.yml`
- 🎲 **Randomness controls:** seeds + deterministic flags (when applicable)
- 📦 **Evidence outputs:** stored under `data/processed/...` *(not inside `mcp/`)*
- 🧬 **Provenance links:** STAC/DCAT/PROV IDs/paths for inputs + outputs

> [!WARNING]
> Avoid committing large binaries to `mcp/`.  
> Keep `mcp/` lightweight and human-readable. Evidence belongs in governed data storage.

---

## 🧪 Experiment reports

### 📛 Naming convention
Pick one and be consistent:

- `EXP-YYYY-MM-DD-<short-slug>.md`  
  Example: `EXP-2026-01-02-ocr-ner-baseline.md`
- or numeric: `EXP-001-<short-slug>.md`

### 🏷️ Status definitions (recommended)
- `draft` 📝: in progress; may be missing evidence links
- `complete` ✅: reproducible; evidence + run receipts linked
- `superseded` 🧯: replaced by a newer experiment

### 🧾 Experiment report template (copy/paste)

```md
---
id: EXP-YYYY-MM-DD-<slug>
title: "<short, explicit title>"
date: YYYY-MM-DD
owner: "@github-handle"
status: draft | complete | superseded
supersedes: []          # optional: [EXP-...]
superseded_by: []       # optional: [EXP-...]
tags: [gis, ocr, nlp, stac, dcat, prov, web, graph]
---

# Objective / Question ❓
- What are we trying to learn or improve?

# Background / Prior Art 📚
- Links to prior experiments, issues, papers, or notes.

# Hypothesis ✅/❌
- What do we expect and why?

# Data Used 🗃️
- Inputs (STAC/DCAT references, dataset IDs, checksums if available).
- Any sampling/filter criteria.

# Method / Protocol 🧾
- Step-by-step procedure.
- Parameters and configs.
- Tools + versions (including OS/GPU if relevant).

# Run Record 🏃
- Code commit: `abcdef1`
- Entrypoint: `src/pipelines/...` or notebook path
- Run folder: `mcp/runs/RUN-YYYY-MM-DD-.../`
- Seeds: `...`
- Duration: `...`

# Results 📈
- Metrics, charts, qualitative examples.
- Link to produced evidence artifacts under `data/processed/...`

# Uncertainty & Validation 🔍
- What could be wrong?
- Sanity checks, cross-validation, spot-check counts, error bounds, etc.

# Interpretation 🧠
- What do the results mean for KFM?

# Decision / Next Steps 🧭
- What do we do next?
- What should be repeated, scaled, or abandoned?

# Reproducibility Checklist ✅
- [ ] All parameters & configs documented
- [ ] Code committed + hash recorded
- [ ] Environment captured (Docker/lockfile)
- [ ] Seeds recorded (if applicable)
- [ ] Inputs/outputs linked via STAC/DCAT/PROV
- [ ] Another person can re-run it using this doc
```

---

## 🏃 Runs

Runs are the **receipt** for an experiment: configs, logs, and machine outputs needed to reproduce.

### 📛 Naming convention
`RUN-YYYY-MM-DD-<slug>/`

### 📦 Suggested run folder contents
- `config/` 🧾 *(YAML/JSON config used for the run)*
- `env/` 🧱 *(pip freeze / conda export / docker image digest)*
- `logs/` 🪵 *(structured logs)*
- `metrics/` 📈 *(CSV/JSON metrics, eval outputs)*
- `artifacts/` 🧩 *(small artifacts like thumbnails, sample outputs)*
- `MANIFEST.md` 🧾 *(human-readable summary + links to evidence in `data/processed/...`)*

### 🧾 Minimal `MANIFEST.md` template (copy/paste)

```md
---
run_id: RUN-YYYY-MM-DD-<slug>
related_experiment: EXP-YYYY-MM-DD-<slug>
date: YYYY-MM-DD
owner: "@github-handle"
code_commit: abcdef1
entrypoint: "src/pipelines/..."
environment:
  docker_image: "ghcr.io/org/project:tag@sha256:..."
  # or:
  requirements: "requirements.txt"
randomness:
  seeds: [123, 456]
  deterministic_flags: ["torch.use_deterministic_algorithms=True"]
inputs:
  - stac: "..."
  - dcat: "..."
outputs:
  - path: "data/processed/<dataset-id>/..."
    stac_item: "..."
    prov: "..."
notes: ""
---

# Summary 🧾
- What did this run do?

# Where to find outputs 📦
- `data/processed/...` links + catalog IDs

# How to reproduce 🔁
1. Checkout commit: `abcdef1`
2. Restore env: ...
3. Run: ...
4. Validate: ...
```

> [!TIP]
> Treat run folders as immutable receipts. If you change parameters, make a new run folder.

---

## 🧰 SOPs

SOPs turn “tribal knowledge” into a reproducible procedure.  
Write an SOP whenever a task is repeated or has meaningful risk (data integrity, georeferencing, catalog publishing, etc.).

### SOP template (copy/paste)

```md
---
id: SOP-<topic>-v1
title: "<clear title>"
owner: "@github-handle"
last_updated: YYYY-MM-DD
---

# Purpose 🎯
What this SOP accomplishes and when to use it.

# Scope ✅
What’s included / excluded.

# Prerequisites 🧱
Accounts, tools, data access, permissions.

# Tools & Versions 🧰
List software + versions.

# Procedure 🧭
1. Step...
2. Step...
3. Step...

# Verification ✅
How to confirm it worked (checks, expected outputs).

# Troubleshooting 🧯
Common failure modes + fixes.

# Audit Trail 🧾
- Links to example PRs, experiment reports, or run folders that used this SOP.
```

**High-value SOPs for KFM (starter set):**
- `sops/georeference_map.md` 🗺️
- `sops/build_cog_tiles.md` 🧱
- `sops/ocr_pipeline.md` 🔎
- `sops/publish_stac_dcat_prov.md` 🌐
- `sops/train_or_update_model.md` 🧠

---

## 🧠 Model Cards

Any ML/AI model used in the pipeline (trained or adopted) needs a model card:
- what it is
- what it was trained on (or sourced from)
- what it should be used for ✅
- what it should **not** be used for 🚫
- known limitations, bias risks, and failure modes ⚠️

### Model card template (copy/paste)

```md
---
model_id: MODEL-<name>-v<semver>
owner: "@github-handle"
date: YYYY-MM-DD
source:
  type: trained | third_party
  license: "..."
  reference: "paper/link/registry id"
---

# Model overview 🧠
- What problem does it solve?

# Intended use ✅
- Supported use-cases

# Out-of-scope / prohibited use 🚫
- What it must not be used for

# Training data 🗃️
- Datasets used (STAC/DCAT references), sampling, labeling notes

# Evaluation 📈
- Metrics, test sets, qualitative examples

# Limitations & biases ⚠️
- Known failure modes, bias risks, uncertainty notes

# Reproducibility 🧪
- Training code commit hash
- Environment / hardware notes
- Hyperparameters / config
- Seeds
```

---

## 📓 Notebooks

Notebooks are welcome—**but must be readable and reproducible**:

- Start with a markdown cell: **purpose + inputs + outputs**
- Keep output cells small *(no giant embedded blobs)*
- Prefer parameterized notebooks (or export to scripts) when a notebook becomes “real”
- If a notebook produces evidence artifacts: store outputs in `data/processed/...` and link them from an experiment report 🧾

---

## 🔗 MCP ↔ KFM pipeline (non-negotiable)

KFM uses a strict evidence pipeline:

**ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes**

So for MCP work:

- ✅ Experiment reports live here: `mcp/experiments/…`
- ✅ Run receipts live here: `mcp/runs/…`
- ✅ Evidence artifacts live here: `data/processed/...`
- ✅ Evidence artifacts must be:
  - cataloged in **STAC/DCAT** 🧾
  - linked with **PROV** lineage 🧬
  - integrated into graph/UI only through governed contracts 🔒

This keeps “cool experiments” from turning into untraceable claims.

---

## 🧩 Domain checklists

Use the checklist that matches your work:

### 🗺️ GIS / Remote Sensing
- [ ] CRS documented (EPSG code + axis order)
- [ ] Georeferencing method + control points documented
- [ ] RMS / fit error recorded (if applicable)
- [ ] Raster outputs are COGs / tiled in a documented way
- [ ] Vector outputs validate (topology, geometry validity)

### 🔎 OCR / NLP
- [ ] Input corpus + sampling documented
- [ ] Labeling rules / evaluation rubric included
- [ ] Precision/recall (or at least spot-check protocol) documented
- [ ] Known failure classes logged (fonts, scan quality, place-name ambiguity)

### 📊 Statistics / Inference
- [ ] Outcome variables + units defined
- [ ] Assumptions checked (normality, independence, etc.)
- [ ] Effect sizes reported (not just p-values)
- [ ] Multiple comparisons / researcher degrees of freedom handled

### 🛰️ Modeling & Simulation
- [ ] Assumptions enumerated explicitly
- [ ] Validation approach documented (comparisons, back-to-back tests)
- [ ] Uncertainty quantified or bounded where possible
- [ ] Results reported with error/uncertainty context (not just point estimates)

---

## 🔐 Safety & hygiene rules

- 🚫 Don’t store secrets, tokens, private keys, or sensitive PII in `mcp/`
- 🧽 Redact logs before committing if they contain identifiers or confidential paths
- 🧊 Prefer immutable receipts: new run folder > editing old run folder
- 🧭 If an experiment is superseded, mark it as `superseded` and link the successor

---

## 🤝 Contributing

- See `../CONTRIBUTING.md`
- Security concerns: see `../.github/SECURITY.md`
- When in doubt: open an issue with an MCP stub (question + proposed experiment) 🧾

---

🧭 **Goal:** Make every output auditable and every method teachable.  
🧾 **Promise:** If it’s in production, it has a paper trail.
