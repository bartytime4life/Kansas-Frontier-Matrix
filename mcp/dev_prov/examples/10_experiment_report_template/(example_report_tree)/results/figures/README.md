# 🖼️ Results → Figures

![template](https://img.shields.io/badge/template-experiment%20report-blue)
![artifacts](https://img.shields.io/badge/artifacts-visual%20evidence-6f42c1)
![provenance](https://img.shields.io/badge/provenance-required-brightgreen)
![reproducible](https://img.shields.io/badge/reproducible-by%20script%2Fconfig-orange)

This folder contains **all visual outputs** (plots, maps, screenshots, diagrams) produced by the experiment and referenced by the report.

> 🧬 **KFM principle applied here:** figures are *evidence artifacts* — no “mystery visuals.”  
> If a figure can’t be traced back to inputs + code + parameters, it doesn’t belong in the report.

---

## ✅ What belongs in `results/figures/`

- 📈 **Charts & plots** (metrics, ablations, confusion matrices, timelines, distributions)
- 🗺️ **Map exports** (static map renders, annotated map snapshots, layer comparisons)
- 🧩 **Architecture & pipeline diagrams** (component diagrams, dataflows, provenance graphs)
- 🧪 **Experiment visuals** (before/after, qualitative samples, failure cases)
- 🖥️ **UI screenshots** (Focus Mode outputs, Story Nodes, Pulse Threads, etc.)

## ❌ What does *not* belong here

- 📦 Raw datasets (put those in `data/` / DVC / artifact storage)
- 📝 Tables (use `results/tables/`)
- 🧾 Logs & telemetry (use `results/logs/` or equivalent)
- 🧨 “Random screenshots” with no context/provenance

---

## 📁 Recommended mini-structure (inside this folder)

```text
results/figures/
├─ README.md                 🧭 you are here
├─ index.md                  🗂️ optional: human-friendly figure gallery
├─ figures.manifest.yaml     🧾 optional: one manifest to rule them all
├─ raw/                      🧪 direct, machine-generated exports (no manual edits)
├─ pub/                      📰 publication-ready outputs (cropped/annotated/compressed)
├─ src/                      🛠️ editable sources (drawio, pptx, svg originals, etc.)
└─ meta/                     🧬 sidecar metadata files (per-figure provenance)
```

> Tip: If you keep only one extra thing, keep **`meta/`**.  
> It keeps the “provenance-first” promise without cluttering filenames.

---

## 🏷️ Naming convention (stable + report-friendly)

Use **stable IDs** so the report doesn’t churn when you regenerate.

**Pattern**
```text
fig-<NNN>__<short_slug>[__<variant>].<ext>
```

**Examples**
```text
fig-001__system_overview.svg
fig-002__tile_perf_vs_zoom.png
fig-003__focus_mode_citations__v2.png
fig-004__drought_trend_1930s.pdf
```

**Rules of thumb**
- `NNN` = order of appearance in the report (001, 002, 003…)
- `short_slug` = lowercase + `snake_case`
- `variant` = optional (`v2`, `mobile`, `dark_mode`, `baseline`, `ablation_a`)
- Prefer **SVG/PDF** for diagrams & plots; **PNG** for screenshots/maps

---

## 🧬 Provenance sidecar (required for “official” figures)

For each `fig-###...`, add a metadata file in `meta/`:

```text
meta/fig-001__system_overview.meta.yaml
meta/fig-002__tile_perf_vs_zoom.meta.yaml
```

### ✅ Minimum required fields

- `id` (matches the filename’s `fig-###`)
- `title` + `caption`
- `generated_by` (script/notebook + command)
- `inputs` (datasets, queries, or source artifacts)
- `parameters` (config reference, key flags, random seed if relevant)
- `commit` (git SHA or version tag)
- `created_utc`
- `license/attribution` (if applicable)
- `changes` (if anything was manually edited)

<details>
<summary>📄 Example <code>.meta.yaml</code> (copy/paste template)</summary>

```yaml
id: fig-002
file:
  path: "../pub/fig-002__tile_perf_vs_zoom.png"
  format: "png"
  width_px: 1600
  height_px: 900
  dpi: 200
title: "Tile performance vs zoom level"
caption: >
  Render latency (ms) by zoom for baseline vs optimized PMTiles pipeline.
  Error bars show 95% CI across 10 runs.

created_utc: "2026-01-22T00:00:00Z"

generated_by:
  script: "../../src/benchmarks/tiles/plot_perf.py"
  command: "python plot_perf.py --input ../metrics/tiles.json --out ../figures/pub/"
  environment:
    lockfile: "../../poetry.lock"
  git:
    commit: "REPLACE_WITH_SHA"
    dirty: false

inputs:
  datasets:
    - id: "dcat:REPLACE_IF_APPLICABLE"
    - id: "stac:REPLACE_IF_APPLICABLE"
  artifacts:
    - path: "../metrics/tiles.json"
  queries:
    - "SELECT ... (if relevant; otherwise omit)"

parameters:
  seed: 1337
  notes: "baseline=MapLibre vX; optimized=PMTiles cache warm"

provenance:
  # Optional but encouraged: map to PROV-style semantics
  activity_id: "prov:activity:tiles-bench-2026-01-22"
  used:
    - "prov:entity:tiles-json"
  generated:
    - "prov:entity:fig-002"

attribution:
  - name: "KFM pipeline benchmark harness"
    license: "MIT (project license)"
  - name: "External dataset source (if any)"
    license: "REPLACE"

ai_assistance:
  used: false
  model: null
  prompt_ref: null

changes:
  - step: "none"
    by: null
    tool: null
    reason: null

review:
  reviewed: false
  reviewer: null
  notes: null
```

</details>

---

## 🔁 Generation flow (how figures should be produced)

Figures should be reproducible from code + config (not manual screenshots that can’t be repeated).

```mermaid
flowchart LR
  A[Inputs\n(data, docs, metrics)] --> B[Analysis/Processing\nscripts + notebooks]
  B --> C[Figure export\nraw/]
  C --> D[Publication prep\npub/]
  D --> E[Report references\nMarkdown/LaTeX]
  C --> M[meta/*.meta.yaml]
  D --> M
```

### 🧪 Recommended workflow
1. **Generate** into `raw/` (direct output of code).
2. **Derive** publishable versions into `pub/` (cropping/labels/compression).
3. **Write provenance** in `meta/`.
4. **Reference** the stable filename in the report.
5. **Lock** large binaries with DVC/LFS if needed.

---

## 🔗 How to reference figures in the report

### Markdown
```md
![Fig. 2 — Tile performance vs zoom level](./results/figures/pub/fig-002__tile_perf_vs_zoom.png)
```

### HTML (controlling width)
```html
<img src="./results/figures/pub/fig-002__tile_perf_vs_zoom.png" width="720" alt="Tile performance vs zoom level">
```

### LaTeX
```tex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{results/figures/pub/fig-002__tile_perf_vs_zoom.pdf}
  \caption{Tile performance vs zoom level.}
  \label{fig:tile-perf}
\end{figure}
```

---

## 🗺️ Map figure checklist (KFM-style)

When exporting map-based figures, capture enough context to be verifiable:

- 🧭 **Extent** (bbox/region) + **time** (date/range)
- 🗂️ Layer list (what’s visible) + styling notes
- 🧾 Attribution/credits visible OR recorded in `.meta.yaml`
- 🌐 CRS / projection (if relevant)
- 🔎 If zoom-dependent: include zoom level + tile source

---

## 🧼 Quality & accessibility checklist

Before promoting a figure into `pub/`:

- [ ] Text readable at the report’s expected width (don’t ship 8pt labels)
- [ ] Avoid red/green-only encodings (colorblind safety)
- [ ] Include units + axis labels + legends
- [ ] If showing uncertainty: include CI/credible interval bands when applicable
- [ ] PNG screenshots are crisp (no JPEG artifacts unless truly needed)
- [ ] Caption explains what changed vs baseline (especially in comparisons)

---

## 🔐 Governance / privacy guardrails

- If a figure includes potentially sensitive coordinates, private sites, or personal data:
  - ✅ aggregate, anonymize, or generalize
  - ✅ record the transformation in `changes:` and `parameters:`
  - ✅ ensure the report doesn’t leak restricted details

---

## 🗂️ Optional: `figures.manifest.yaml` (one-stop index)

If you want CI or tooling to validate “no orphan figures,” keep a manifest:

```yaml
figures:
  - id: fig-001
    file: "pub/fig-001__system_overview.svg"
    meta: "meta/fig-001__system_overview.meta.yaml"
    used_in: ["../../report.md"]
  - id: fig-002
    file: "pub/fig-002__tile_perf_vs_zoom.png"
    meta: "meta/fig-002__tile_perf_vs_zoom.meta.yaml"
    used_in: ["../../report.md"]
```

---

## 🧾 Template: Figure gallery table (drop into `index.md`)

| ID | Preview | File | Notes |
|---:|:--|:--|:--|
| fig-001 | _(optional)_ | `pub/fig-001__system_overview.svg` | High-level system diagram |
| fig-002 | _(optional)_ | `pub/fig-002__tile_perf_vs_zoom.png` | Benchmark plot |

---

## ✨ Bottom line

If someone clones the repo, they should be able to answer:

- **What is this figure?**
- **How was it generated?**
- **What data did it use?**
- **What exact version of code/config produced it?**

When in doubt: **add provenance, not prose.** 🧬📌
