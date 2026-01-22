# 🖼️ Figures & Visual Artifacts (📁 `artifacts/figures/`)

![Provenance](https://img.shields.io/badge/Provenance-W3C%20PROV--O-informational)
![Metadata](https://img.shields.io/badge/Metadata-STAC%20%7C%20DCAT-blue)
![Evidence-first](https://img.shields.io/badge/Evidence--First-No%20Mystery%20Layers-critical)
![Reproducible](https://img.shields.io/badge/Reproducible-Deterministic%20Builds-success)
![Accessibility](https://img.shields.io/badge/Accessibility-Alt%20Text%20%2B%20Contrast-important)
![Supply Chain](https://img.shields.io/badge/Supply%20Chain-SBOM%20%2B%20SLSA%20(optional)-yellow)

This folder holds **all static images/diagrams** referenced by the experiment report in this example tree: maps 🗺️, charts 📈, UI screenshots 🧭, architecture diagrams 🧩, simulation renders 🎮, and narrative/story visuals 📜.

> [!IMPORTANT]
> **Evidence-first rule:** if a figure can’t be traced back to a dataset/query/script (or clearly marked as a mock), it **doesn’t ship**. No “mystery figures.” 🧾🔍

---

## ✅ Quick Add Checklist (90 seconds)

1) Drop the file into this folder using the naming convention (see below)  
2) Add a caption + alt text sidecar (`.caption.md`)  
3) Add minimal metadata (`.meta.yaml`) — *license + sensitivity are non-negotiable*  
4) If generated: add provenance (`.prov.jsonld`) + link to the generating script/notebook

> [!TIP]
> If you only do **two** things: **(a)** keep filenames clean + numbered, **(b)** write captions with sources. Everything else scales from there.

---

## 📁 Recommended Structure

```text
artifacts/
  figures/ 🖼️
    README.md
    fig_001_pipeline_overview.svg
    fig_001_pipeline_overview.caption.md
    fig_001_pipeline_overview.meta.yaml
    fig_001_pipeline_overview.prov.jsonld
    fig_002_ui_layer_provenance.png
    fig_002_ui_layer_provenance.caption.md
    fig_002_ui_layer_provenance.meta.yaml
    src/ 🧪 (optional but encouraged)
      fig_001_pipeline_overview.drawio
      fig_003_metrics_plot.ipynb
    thumbs/ 🧷 (optional)
      fig_002_ui_layer_provenance.thumb.png
```

---

## 🧾 Naming & Numbering Convention

### ✅ Standard
Use:

- `fig_{NNN}_{slug}.{ext}`  
- `fig_{NNN}_{slug}.{sidecar_ext}`

Examples:
- `fig_007_drought_index_map.png`
- `fig_007_drought_index_map.caption.md`
- `fig_007_drought_index_map.meta.yaml`
- `fig_007_drought_index_map.prov.jsonld`

### 🧩 Multi-panel figures
Prefer one of:
- `fig_012a_model_drift.png`, `fig_012b_model_bias.png`  
- `fig_012_panel_a_model_drift.png`, `fig_012_panel_b_model_bias.png`

### 📦 File formats
- **SVG** ✅ for diagrams (architecture, pipelines, flowcharts)
- **PNG** ✅ for screenshots / raster maps (lossless preferred)
- **PDF** ✅ when you need print-ready vector output
- **Avoid** JPG for charts/maps unless size constraints require it (JPG artifacts can mislead)

> [!NOTE]
> Keep the **base name identical** across all sidecars. This allows simple validation scripts (and policy gates) to verify completeness automatically.

---

## 🧠 The “Figure Contract” (Metadata + Provenance)

A figure is not just pixels — it’s an artifact with **context**, **license**, **sensitivity**, and **lineage**.

### Minimum requirements (must have)
| Item | Required? | Why |
|---|---:|---|
| `fig_###_*.{png,svg,pdf}` | ✅ | The visual itself |
| `fig_###_*.caption.md` | ✅ | Human caption + alt text + sources |
| `fig_###_*.meta.yaml` | ✅ | License + sensitivity + core metadata |

### Strongly recommended (for generated/analytic figures)
| Item | When | Why |
|---|---|---|
| `fig_###_*.prov.jsonld` | Generated or derived | Machine-readable lineage (W3C PROV-O) |
| `src/` source file(s) | If editable/regenerable | Rebuilds & future edits without “re-drawing” |
| checksums | Always nice | Integrity & cache correctness |

---

## ✍️ Caption Sidecar (`.caption.md`) — Template

> [!IMPORTANT]
> **Captions are part of the evidence chain.** Treat them like mini-citations, not just labels.

<details>
<summary>📄 <code>fig_###_something.caption.md</code> (example template)</summary>

```markdown
## Caption
**Figure X.** One-sentence description of what the reader should learn from this figure.

### What’s shown
- Region / subject:
- Time range:
- Layers / variables:
- Units / aggregation (if chart):

### Sources & attributions
- Dataset(s):
- Documents / archives:
- Basemap / tiles (if any):
- Tooling / pipeline:

### Notes (interpretation & caveats)
- Assumptions:
- Known limitations:
- If AI-assisted: mark clearly what was AI-generated vs. sourced.
  
### Alt text (required)
A short but complete description for screen readers.
```

</details>

---

## 🧷 Metadata Sidecar (`.meta.yaml`) — Template

> [!IMPORTANT]
> **Every figure must declare:**
> - `license` (or “unknown” and a TODO — but ideally never unknown)
> - `sensitivity` (public / restricted / confidential)

<details>
<summary>🧾 <code>fig_###_something.meta.yaml</code> (example template)</summary>

```yaml
id: fig_007
slug: drought_index_map
title: "Drought Index Snapshot with Timeline State"
type: map  # map | chart | diagram | screenshot | photo | simulation | other
created_utc: "2026-01-22T00:00:00Z"

authors:
  - name: "Your Name or Team"
    role: "analyst"

license: "CC-BY-4.0"        # REQUIRED
sensitivity: "public"       # REQUIRED: public | restricted | confidential

# What the figure depends on (high-level, human readable)
inputs:
  datasets:
    - id: "stac:catalog/collections/drought-index"
    - id: "dcat:datasets/usgs-nwis-realtime-water"
  documents:
    - id: "library:news/1930s_dust_bowl_clippings.pdf"

# Map-specific hints (optional but helpful)
map:
  bbox_wgs84: [-102.05, 36.99, -94.59, 40.00]   # [minLon, minLat, maxLon, maxLat]
  time_range: ["1930-01-01", "1939-12-31"]
  projection: "EPSG:4326"
  ui_state:
    zoom: 6
    layers: ["drought_index", "county_boundaries", "rivers"]

# How it was made (link into src/ if reproducible)
generation:
  method: "qgis_export"    # qgis_export | python_script | notebook | screenshot | manual | ai_generated
  source_ref: "../figures/src/fig_007_drought_index_map.qgz"
  git_commit: "REPLACE_WITH_SHA"
  parameters:
    note: "Exported at 300dpi; legend included; high-contrast mode enabled."

integrity:
  sha256: "REPLACE_WITH_SHA256"
```

</details>

---

## ⛓️ Provenance Sidecar (`.prov.jsonld`) — Minimal Pattern

If a figure is derived (from code, a query, a pipeline run, or a model), include provenance.

<details>
<summary>⛓️ <code>fig_###_something.prov.jsonld</code> (tiny sketch)</summary>

```json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "entity": {
    "fig:fig_007_drought_index_map": {
      "prov:label": "Figure 7 - Drought Index Map",
      "prov:type": "kfm:Figure",
      "kfm:sha256": "REPLACE_WITH_SHA256"
    },
    "data:drought_index_v3": {
      "prov:label": "Drought Index Dataset v3",
      "prov:type": "kfm:Dataset"
    }
  },
  "activity": {
    "act:generate_fig_007": {
      "prov:label": "Generate fig_007 (map export)",
      "prov:type": "kfm:FigureBuild",
      "prov:used": ["data:drought_index_v3"],
      "prov:generated": ["fig:fig_007_drought_index_map"]
    }
  }
}
```

</details>

> [!NOTE]
> For **real-time or dynamic queries** (streaming sensors, “latest reading” snapshots), provenance should include the **timestamped input** used to generate the figure. 🕒

---

## 🗺️ Map Figures: “No Mystery Layers” Rules

Map visuals are powerful — and easy to misread. Keep them honest:

- ✅ Include **time range** (especially if a timeline slider exists)
- ✅ Include **what layers were active**, plus **attribution/license** per layer
- ✅ Include **legend**, **units**, and **scale** when applicable
- ✅ Record the **bbox + zoom** (or camera state for 3D)
- ✅ If data was reprojected/processed: describe the transformation in metadata/provenance

> [!IMPORTANT]
> If a map’s appearance depends on UI state (active layers, filters, time slider), capture that state in `meta.yaml` (and/or a small exported UI state JSON). 🧭

### Sensitive locations 🧿
If a map could expose sensitive sites (cultural heritage, protected ecological points, private land, personal info):
- aggregate (county-level)  
- obfuscate (round coordinates / blur)  
- or restrict access entirely  
…and **label the figure’s sensitivity** clearly in metadata.

---

## 🧭 UI Screenshots: Trust-by-Design

UI figures should reinforce transparency:
- Capture the **Layer Info / Provenance panel** when relevant
- Include the **timeline state** if time navigation is central
- Avoid capturing personal user data (emails, tokens, user names)
- Prefer **high-contrast mode** when it improves readability ♿

> [!TIP]
> If the UI supports “export with attributions,” use it. It reduces caption work and prevents attribution drift.

---

## 🤖 AI + Analytics Figures: Make the Model Auditable

For AI-driven outputs (Focus Mode answers, evaluation plots, drift dashboards, bias checks):

Include in `.meta.yaml`:
- model name + version (or hash)
- dataset version(s)
- evaluation configuration (metrics, thresholds)
- what qualifies as “success” (acceptance criteria)
- whether output is **AI-generated**, **AI-assisted**, or **fully sourced**

### Recommended AI figure types 📈
- Drift monitoring (accuracy + citation coverage over time)
- Bias checks summaries
- Retrieval coverage (which sources were used most)
- “Audit panel” style explanations (what evidence influenced results)

> [!IMPORTANT]
> If an AI chart references claims, the caption must point to the underlying datasets/documents. “No citations” = “no publish.”

---

## 🎮 Simulations, 4D, and AR Visuals: Label Assumptions Loudly

For simulation outputs, 4D time-travel views, or AR mockups:
- include the **run ID**, **parameters**, and **random seed** (if any)
- cite the **input datasets** + the **model code version**
- mark speculative visuals as **concept / mock / prototype** (not observed fact)

> [!NOTE]
> AR/4D visuals are awesome — but readers must never confuse them with ground-truth observations. 🧠✅

---

## ♿ Accessibility Requirements (Non-negotiable)

- ✅ Every figure needs **alt text** (in `.caption.md`)
- ✅ Don’t rely on color alone (use labels/patterns)
- ✅ Axis labels + units are mandatory for charts
- ✅ Avoid tiny text; target readable labels at normal zoom

> [!TIP]
> If a figure is too dense, split it into panels or provide a “zoomed” inset.

---

## 🔐 Privacy, FAIR+CARE, and Ethics

Even “derived” visuals can leak sensitive information.

- If a figure is derived from restricted inputs, the figure is also restricted unless explicitly cleared.
- Use aggregation, redaction, or obfuscation for sensitive outputs.
- Respect cultural protocols and permissions for community-contributed content.
- Record ethics decisions in metadata (e.g., why something is blurred or aggregated).

---

## ✅ Suggested Policy Gates (CI-Friendly)

If you add CI checks for this template, start with:

- [ ] Every `fig_*.{png,svg,pdf}` has a matching `.caption.md`
- [ ] Every figure has `.meta.yaml` with `license` + `sensitivity`
- [ ] Generated figures have `.prov.jsonld`
- [ ] Checksums recorded (optional, recommended)
- [ ] No restricted figure is referenced from a public report build

> [!NOTE]
> This aligns well with “fail closed” governance: if required metadata is missing, the pipeline should refuse to publish the figure set.

---

## 🧰 Tooling Suggestions (Pick what fits)

- 🗺️ **GIS & map exports:** QGIS, GDAL, Rasterio, GeoPandas  
- 🌐 **WebGL map context:** MapLibre GL JS, Cesium (2D/3D parity)  
- 📈 **Charts:** matplotlib / plotly (save deterministic outputs)  
- 🧩 **Diagrams:** Mermaid, Draw.io, Excalidraw (store editable source in `src/`)  
- 🧪 **Notebooks:** Jupyter (export scripts or lock outputs for reproducibility)

---

## 📚 Design Inputs (Project Docs Used)

This README’s conventions are aligned with the project’s “provenance-first / evidence-first” direction across:

- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** (contracts, provenance, storage)
- 🏗️ **KFM – Comprehensive Architecture, Features, and Design** (policy gates, FAIR+CARE governance, CI enforcement)
- 🧭🤖 **KFM – AI System Overview** (citations-required AI, drift/bias monitoring, auditability)
- 🧭 **KFM – Comprehensive UI System Overview** (timeline + story nodes + provenance surfaced in UI)
- 📥 **KFM Data Intake – Technical & Design Guide** (streaming data provenance, “snapshot with timestamp” discipline)
- 🚀 **Innovative Concepts to Evolve KFM** (AR/4D storytelling, cultural protocols, sensitivity-aware handling)
- 🌟 **Latest Ideas & Future Proposals** (reproducible research, W-P-E agents, SBOM/SLSA)
- 🧠 **Additional Project Ideas** (concept nodes, narrative pattern detection, detectors & templates)
- 📚 **AI Concepts & more** (reference library for evaluation + modeling concepts)
- 🗄️ **Data Management / Bayesian Methods / Architectures** (uncertainty + rigorous data workflows)
- 🗺️ **Maps / Virtual Worlds / Archaeological 3D / WebGL** (3D GIS + rendering considerations)
- 💻 **Various programming languages & resources** (engineering references for reproducible builds)

---

## 🧪 Optional: Figure Manifest (Nice for bigger reports)

If the report grows, consider adding `figures.yml` (or `index.md`) listing all figures with captions and pointers to provenance.

> [!TIP]
> A manifest makes it easy to generate: a figure gallery, a report appendix, or an automated “attribution page.” 🧾✨
