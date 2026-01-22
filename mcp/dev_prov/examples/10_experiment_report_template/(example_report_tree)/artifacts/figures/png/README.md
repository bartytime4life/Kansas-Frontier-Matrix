# 🟦 PNG Figure Artifacts (Experiment Report)

![Artifact](https://img.shields.io/badge/artifact-figures-blue)
![Format](https://img.shields.io/badge/format-PNG-informational)
![Policy](https://img.shields.io/badge/policy-provenance%E2%80%91first-critical)
![Policy](https://img.shields.io/badge/policy-no%20uncited%20outputs-critical)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-aligned-success)

> 🎯 **Purpose:** This folder holds **PNG** figures used by the **experiment report** in this example report tree.
>
> 🧠 **KFM mindset:** treat every figure as an **evidence artifact**—traceable, citable, and reproducible.  
> This matches KFM’s “no black box” visualization ethos and provenance-first rules.  [oai_citation:0‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 📍 You are here

```text
🧪 mcp/dev_prov/examples/10_experiment_report_template/
└─ (example_report_tree)/
   └─ 🧾 artifacts/
      └─ 🖼️ figures/
         └─ 🟦 png/
            ├─ README.md  👈 you are reading this
            └─ fig_001_example.png  (optional example)
```

---

## ✅ What belongs in this folder

- 📊 **Charts / plots** (metrics, ablations, timelines)
- 🗺️ **Map screenshots / exports** (2D MapLibre or 3D Cesium views)
- 🧱 **Architecture diagrams** (pipelines, trust boundaries, system flow)
- 🧭 **Storytelling / UI screenshots** (Story Nodes, timeline slider states, guided tours)

KFM’s stack explicitly leans on **MapLibre GL JS (2D)** and **CesiumJS (3D)**, so PNG exports/screenshots for both are expected in practice.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🚫 What NOT to commit here

- ❌ Random “mystery” images with no caption, no source, no provenance
- ❌ Sensitive screenshots with exact site locations, PII, or culturally restricted details  
  (see **Sensitive Data** below)  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- ❌ Huge unoptimized PNGs “straight from export” when compression is easy (keep the repo lean 📉)

---

## 🧾 Folder rules (the **contract**)

### 1) Every figure must be citable 📌
KFM’s policy gates explicitly require that AI outputs include citations and **fail closed** if requirements aren’t met—carry that same rigor into figure captions and metadata.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### 2) Every figure should be reproducible ♻️
KFM’s simulation workflow emphasizes reproducibility basics (pin inputs, capture parameters, pin environment, record seeds, CI checks). Even if you don’t implement all of that here, the figure workflow should **aim** at the same standard.  [oai_citation:5‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 3) Units + labeling are not optional 📏
When figures show data, label axes with **quantity + unit** and document uncertainties/error margins where relevant.  [oai_citation:6‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🧷 Naming convention (PNG)

Use **ordered + descriptive** names so reports diff cleanly and stay readable:

✅ **Recommended**
- `fig_001_pipeline_overview.png`
- `fig_010_map_kansas_rivers_1890s.png`
- `fig_020_ui_story_node_step_03.png`

📛 **Rules**
- lowercase + underscores, no spaces
- 3-digit prefix for stable ordering (`001`, `002`, …)
- keep it short but specific

---

## 🧬 Provenance sidecars (recommended → ideally required)

KFM treats derived outputs as “first-class artifacts” and leans on **STAC/DCAT/PROV** patterns for traceability and interoperability. Adopt a lightweight version of that here:  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

For each PNG, add **one** small sidecar:

```text
fig_001_pipeline_overview.png
fig_001_pipeline_overview.meta.json   👈 recommended minimum
```

### ✅ Minimal `*.meta.json` schema (practical + human-friendly)

```json
{
  "id": "fig_001_pipeline_overview",
  "title": "Pipeline Overview",
  "caption": "Raw sources → ETL → STAC/DCAT/PROV → Graph → API → UI",
  "created_utc": "2026-01-22T00:00:00Z",
  "generated_by": {
    "tool": "python",
    "script": "scripts/make_pipeline_overview.py",
    "command": "python scripts/make_pipeline_overview.py --out artifacts/figures/png/fig_001_pipeline_overview.png",
    "git_commit": "<commit-sha>"
  },
  "inputs": [
    {"type": "dcat_dataset", "id": "dcat:usgs-nwis"},
    {"type": "stac_item", "id": "stac:river-gauge:topeka:2026-01-22T00:00:00Z"}
  ],
  "license": "CC-BY-4.0",
  "sensitivity": "public",
  "notes": "If this is a screenshot, include map state JSON (see below)."
}
```

> 💡 Why so strict? Because KFM’s philosophy is that **every visualization must link back to source + metadata**, so users can understand the “map behind the map.”  [oai_citation:9‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) [oai_citation:10‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🗺️ Map & UI screenshots: include a “view state” file (highly recommended)

KFM Story Nodes are designed as **machine-ingestible storytelling** and typically pair **Markdown** with a **JSON config** capturing map layers and camera view. Use the same trick for screenshots so they’re reproducible.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

```text
fig_010_map_kansas_rivers_1890s.png
fig_010_map_kansas_rivers_1890s.view.json
```

### Suggested `*.view.json` fields (keep it simple)

```json
{
  "map_engine": "maplibre",
  "style_id": "kfm_basemap_v1",
  "layers_on": ["rivers", "counties_1890", "railroads_1895"],
  "time_range": {"start": "1890-01-01", "end": "1899-12-31"},
  "camera": {"center_lon": -96.5, "center_lat": 38.5, "zoom": 6.2, "bearing": 0, "pitch": 0},
  "notes": "Exported from UI state; aligns with Story Node-style map configs."
}
```

---

## 🤖 AI / Focus Mode figures: extra rules

If a figure includes AI interpretations (e.g., heatmaps, “insight callouts,” extracted claims):

- ✅ include **citations** to the underlying data/documents
- ✅ include **PROV-like linkage** (what inputs were used, when, and how)

KFM’s “Focus Mode” and evidence-backed AI approach expects answers grounded in sources and provenance logs—even for dynamic queries.  [oai_citation:12‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:13‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

---

## 🔐 Sensitive data & ethics (CARE-aware)

KFM explicitly calls out handling sensitive locations and data by:
- generalizing/coarsening coordinates,
- applying access controls,
- tagging sensitivity and restrictions,
- respecting Indigenous Data Sovereignty (CARE).  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

✅ **Do**
- blur/redact labels
- aggregate to grid/hex
- omit exact points unless permission is explicit

❌ **Don’t**
- publish precise locations of archaeological sites, endangered species habitats, or personal data

---

## 🧪 Draft vs promoted: keep WIP out of the “official” folder

KFM’s simulation guidance stresses a **sandbox → promotion** workflow: experimental outputs live in a work area until reviewed and promoted to official catalogs. Mirror that pattern here:

- 🧪 Keep drafts in a scratch/work area (outside the report tree)
- ✅ Only copy the **final, reviewed** PNGs + sidecars into this folder

 [oai_citation:15‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 📦 Optional: bundle + sign figures as artifacts (OCI-style)

KFM proposes storing artifacts using OCI registry tooling (e.g., **oras**, **cosign**) and attaching provenance (e.g., **PROV JSON-LD**) for strong traceability and distribution. If this template is used in CI, you can apply the same idea to figure bundles.  [oai_citation:16‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧰 Quick quality checklist (copy/paste)

- [ ] File named `fig_###_<slug>.png`
- [ ] PNG optimized (not massive)
- [ ] Axes labeled + units included (if applicable)  [oai_citation:17‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- [ ] Caption has source(s) + method summary
- [ ] `*.meta.json` exists (inputs, tool/script, license, sensitivity)
- [ ] If screenshot/map: `*.view.json` exists (layers/time/camera)  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] Sensitive data reviewed (redaction/generalization applied)  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧩 How to reference a figure in the report

From the report root (example):

```md
![Pipeline overview](artifacts/figures/png/fig_001_pipeline_overview.png)

*Figure 1. Pipeline overview. Sources: …; Generated by: … (see meta sidecar).*
```

---

## 📚 Note on “PDF portfolio” project references (Acrobat required)

Some of the project’s reference PDFs are **PDF portfolios** (collections of embedded docs). If you’re mining them for diagrams/figures, open them in **Acrobat/Adobe Reader** to access the embedded content:

- `AI Concepts & more.pdf` 
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf`  [oai_citation:20‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf`  [oai_citation:21‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
- `Various programming langurages & resources 1.pdf`  [oai_citation:22‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)

---

## 🧾 Sources that shaped this folder’s standards (KFM-aligned)

These conventions are aligned with KFM’s evidence-first, provenance-first design and reporting practices:

- **Data intake + provenance-first publishing**  [oai_citation:23‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Policy gates (schema/metadata/license/sensitivity/provenance; “no uncited outputs”; fail closed)**  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- **UI transparency (“map behind the map” via linked source + metadata)**  [oai_citation:26‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- **Story Nodes structure (Markdown + JSON view config)**  [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- **Boundary artifacts + “evidence artifacts” pattern (STAC/DCAT/PROV)**  [oai_citation:28‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:29‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Sensitive data handling + CARE considerations**  [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Tech stack supports 2D/3D map exports (MapLibre + Cesium)**  [oai_citation:31‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- **Future proposals (Story Nodes tooling, 3D “Kansas From Above”, real-time feeds producing STAC/DCAT)**  [oai_citation:32‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- **Innovations (AR / hybrid 3D storytelling; evidence-based AI assistant)**  [oai_citation:33‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC) [oai_citation:34‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- **AI stewardship & human-in-the-loop metadata support**  [oai_citation:35‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- **Artifact packaging/signing idea (OCI + cosign/oras + PROV attachments)**  [oai_citation:36‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- **Scientific rigor for plots (axes/units/uncertainties)**  [oai_citation:37‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

🧡 If you’re adding new figures: **make them beautiful** *and* **make them provable**.
