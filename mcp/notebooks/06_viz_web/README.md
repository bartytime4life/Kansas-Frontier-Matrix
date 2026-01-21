# 06_viz_web — Web Visualization Notebook 🗺️🌐

![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Web](https://img.shields.io/badge/Web-Visualization-blue)
![MapLibre](https://img.shields.io/badge/MapLibre-2D%20Map-informational)
![Cesium](https://img.shields.io/badge/CesiumJS-3D%20Globe-success)
![Provenance](https://img.shields.io/badge/Provenance-first-purple)
![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-black)

> **🎯 Goal:** Prototype KFM’s **browser-first mapping experience** (2D/3D map + timeline + story nodes + AI “Focus Mode”) in a way that stays **provenance-first** and **MCP-reproducible**.  
> KFM’s UI direction explicitly includes MapLibre (2D), Cesium (3D), a timeline slider, story nodes, and Focus Mode UX patterns.  [oai_citation:0‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) [oai_citation:1‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🧭 Where this lives in the repo

This folder is part of **MCP notebooks**: exploratory work that can mature into scripts/pipelines, while remaining **living documentation** (notebook-first prototyping). The project repo structure explicitly calls out notebooks as living docs and the `mcp/` directory as **Master Coder Protocol** resources (experiments, SOPs, glossary, model cards).  [oai_citation:2‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA) [oai_citation:3‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)

---

## 🧩 What this notebook should deliver

✅ By the end of `06_viz_web.ipynb`, you should have:

- **A working web map demo plan**:
  - 2D **MapLibre** view + optional 3D **Cesium** view (or Cesium-ready artifacts)  [oai_citation:4‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
  - **Timeline slider** wiring (temporal filtering + UI hooks) — explicitly called out as MVP in future proposals  [oai_citation:5‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
  - **Story Nodes**: narrative “cards” that bind map state + timeline + citations  [oai_citation:6‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
  - **Focus Mode overlay** pattern (AI answers must cite sources)  [oai_citation:8‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

- **Artifacts you can commit** (even if the final front-end isn’t built yet):
  - `layers.registry.json` (layer manifest)
  - `timeline.config.json` (time domain, ticks, presets)
  - `style.json` (MapLibre style seed)
  - `story_nodes/<id>/` skeleton(s)
  - `catalog/` pointers (STAC/DCAT/PROV references)

---

## 🚫 Non‑negotiables (KFM contracts)

> These are “guardrails” across KFM docs — treat them like compile-time errors 🧱

### 1) No bypassing the intake pipeline
Data intake is **linear**. Raw data is treated as immutable/read-only, and transformation steps must be deterministic with auditability.  [oai_citation:9‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:10‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 2) Provenance-first publishing (every layer is explainable)
Every published layer should be traceable with an **evidence triplet**: **STAC item + DCAT dataset + PROV activity**.  [oai_citation:11‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 3) “No mystery layers” in the UI
KFM emphasizes a contract-first, provenance-first experience so the UI can trust what it displays (and users can inspect it).  [oai_citation:12‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

### 4) Focus Mode must cite sources
Focus Mode is described as a context-aware research agent that **always cites sources** and makes reasoning inspectable.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🧠 Feature map (what we’re prototyping)

| Capability | What it means in practice | Why it matters |
|---|---|---|
| 🗺️ 2D Map | MapLibre-based layers, legends, popups | Fast, browser-first map UX  [oai_citation:14‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) |
| 🌍 3D Globe | Cesium-based 3D terrain + time-aware overlays | 4D storytelling & spatial context  [oai_citation:15‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) |
| ⏳ Timeline | Slider filters layers + story nodes by time | “Time-travel” is core to KFM narrative UX  [oai_citation:16‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe) |
| 📚 Story Nodes | Markdown/JSON narrative modules tied to map state | Guided exploration & citations  [oai_citation:17‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) |
| 🤖 Focus Mode | AI assistant panel grounded in sources | Research + explainability in-app  [oai_citation:18‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) |
| 🧾 “Map behind the map” | Layer metadata, citations, trust tags | Transparency + auditability  [oai_citation:19‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) |

---

## 📁 Suggested folder layout (for this notebook’s outputs)

> Adjust to your repo conventions — but keep the *idea*: **notebook → reproducible artifacts → web demo**.

```text
mcp/
└─ 📓 notebooks/
   └─ 🖥️ 06_viz_web/
      ├─ 📄 README.md                      # 📘 Notebook goals, how to run, and how outputs map to web registries
      ├─ 📓📄 06_viz_web.ipynb              # Primary notebook (builds demo registries + story stubs + screenshots)
      ├─ 📦 output/                        # Generated, shareable outputs from the notebook (small + reproducible)
      │  ├─ 🗂️🧾 layers.registry.json       # Layer registry produced for the demo (UI-friendly index)
      │  ├─ ⏳🧾 timeline.config.json       # Timeline configuration (dates/steps/constraints for demo playback)
      │  ├─ 🎨🧾 style.base.json            # Base map/style config used by the demo viewer
      │  ├─ 📚 story_nodes/                # Story Node stubs produced by the notebook
      │  │  └─ 🧩 node_0001/
      │  │     ├─ 📝📄 node.md              # Narrative markdown for the demo node
      │  │     └─ 🧭🧾 node.json             # Step/config JSON for the demo node
      │  ├─ 🧾 catalog_refs/               # References/pointers to catalogs used (not full catalogs)
      │  │  ├─ 🛰️🧾 stac_refs.json          # STAC references (collections/items/assets pointers)
      │  │  ├─ 🗂️🧾 dcat_refs.json          # DCAT references (datasets/distributions pointers)
      │  │  └─ 🧬🧾 prov_refs.json          # PROV references (run/activity/entity pointers)
      │  └─ 📸 screenshots/                # Demo screenshots produced for docs/PRs (redact if needed)
      │     ├─ 🗺️🖼️ map_2d.png              # 2D map capture
      │     └─ 🧊🖼️ map_3d.png              # 3D map capture
      └─ 🧪 web_demo/                      # Tiny runnable web demo (static build inputs)
         ├─ 🧾📄 index.html                 # Demo page scaffold (loads the registries/output)
         ├─ 🧠📄 app.ts                     # Demo app logic (wires layers/timeline/story nodes)
         └─ 🎨📄 styles.css                 # Demo styling (minimal; uses tokens where possible)
```

---

## 🧪 Notebook roadmap (recommended sections)

### 0) Problem statement + hypothesis (MCP style)
Follow a “lab notebook” structure: define the question, hypothesis, methods, results, and conclusion.  [oai_citation:20‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

> **Copy/paste template** (put this at the top of `06_viz_web.ipynb`):
```markdown
## Objective
## Background / Prior Art
## Hypothesis
## Data & Tools
## Method / Procedure
## Results (tables, screenshots, metrics)
## Interpretation
## Limitations
## Next Steps
## Repro Notes (versions, seeds, hashes, run id)
```

### 1) Pick a “thin slice” dataset ✅
Pick one layer you can fully publish end-to-end:
- vector (GeoJSON/GeoParquet → PMTiles)
- raster (COG → hillshade/tiles)
- points/events (CSV → GeoJSON → tile layer)

> Keep it small. This notebook is about the **web viz contract**, not a full migration.

### 2) Normalize + time-encode the layer
Define:
- `time.start`, `time.end`, `precision` (year/season/day)
- missing-time behavior
- temporal validity vs. observation-time

### 3) Generate web-facing artifacts
Future proposals highlight **PMTiles + GeoParquet** as “best bets” for browser-first performance and offline packaging.  [oai_citation:21‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### 4) Build layer registry + provenance pointers
Every layer entry in your registry should point at:
- **STAC** (assets, footprints)
- **DCAT** (dataset catalog metadata)
- **PROV** (activity + inputs + outputs)  
Evidence-triplet requirement is explicitly stated in intake guidance.  [oai_citation:22‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 5) Timeline slider wiring (UI behavior)
Timeline is explicitly highlighted as an MVP feature; design this notebook to output a clean `timeline.config.json` for the front-end.  [oai_citation:23‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### 6) Story node prototype
KFM’s architecture expects story nodes living under `web/story_nodes/` (Markdown narrative + configuration) for the UI to load.  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### 7) Focus Mode overlay “contract”
In this notebook:
- define the UI contract for AI responses (citations required, link back to evidence)
- decide what “context” gets sent (map bbox, time slice, selected layers, story node id)  
Focus Mode’s “always cite sources” framing is explicit.  [oai_citation:25‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 8) Performance + UX sanity checks
Technical docs emphasize scalability via caching and architecture that supports many users.  [oai_citation:26‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

---

## 🧾 Minimal “layer manifest” schema (recommended)

> Not a strict standard yet — treat as a **local contract** for the notebook.

```json
{
  "layer_id": "kfm:railroads_1880",
  "title": "Railroads (c. 1880)",
  "description": "Digitized rail lines derived from historical maps.",
  "geometry_type": "LineString",
  "time": { "start": "1875-01-01", "end": "1890-12-31", "precision": "year" },
  "web_assets": {
    "pmtiles": "output/railroads_1880.pmtiles",
    "style_hint": { "type": "line", "width": 2 }
  },
  "provenance": {
    "stac": "catalog/stac/railroads_1880.json",
    "dcat": "catalog/dcat/railroads_1880.json",
    "prov": "catalog/prov/run_2026_01_20.json"
  },
  "access": { "classification": "public", "license": "CC-BY" }
}
```

---

## 📚 Story Nodes (minimum viable format)

KFM UI docs describe story content as loadable narrative units (Markdown and/or JSON) shown in a preview panel and tied to map exploration.  [oai_citation:27‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

**Recommended structure**
```text
📁 story_nodes/
  📁 node_0001/
    📄 node.md        # narrative + citations
    📄 node.json      # map state + timeline state
    📄 media/...
```

**Frontmatter suggestion (`node.md`)**
```markdown
---
id: node_0001
title: "Rail expansion & settlement"
time:
  start: 1870
  end: 1890
layers:
  - kfm:railroads_1880
camera:
  mode: "2d"
  center: [-98.0, 38.5]
  zoom: 5.3
citations:
  - dcat:railroads_1880
---
```

---

## 🤖 Focus Mode integration notes (web UX)

Focus Mode is positioned as a research agent that:
- is context-aware,
- cites sources,
- and supports explainability.  [oai_citation:28‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

**Web UX pattern we want:**
- **Answer card** with:
  - short response
  - citations (STAC/DCAT/PROV IDs)
  - “Why this is relevant” section
- **Map action buttons**:
  - “Zoom to evidence”
  - “Highlight cited layer”
  - “Open provenance panel”
- **Audit affordance**:
  - show which layers + timeframe were in context

---

## 🧵 Experimental web layers (from project ideas)

These are optional “stretch goals” that fit naturally into web viz:

### 📍 Pulse Threads (geo-social timeline feed)
Pulse Threads are proposed as geotagged, time-indexed narrative posts tied to places.  [oai_citation:29‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 🧠 Conceptual Attention Nodes (graph-first UX overlay)
Conceptual Attention Nodes are proposed as interactive anchors on the map/graph for “living research trails.”  [oai_citation:30‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 🧬 Narrative Pattern Detection
Proposed as an AI-assisted analysis layer that detects repeating motifs across time/space — useful for story generation and exploration cues.  [oai_citation:31‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🕶️ Future-facing viz ideas (AR / 4D)

Innovative concepts propose **4D digital twins** and **AR storytelling**, letting users “time travel” through layered historical reconstructions.  [oai_citation:32‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

> If you add a “future hook” in this notebook, keep it as a **separate section** + **separate output folder** so the MVP stays clean.

---

## ✅ Quality gates (what “done” means)

### Provenance & catalog checks
- [ ] Layer manifest contains STAC/DCAT/PROV pointers  [oai_citation:33‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Story nodes include citations (or references to catalog IDs)  [oai_citation:34‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- [ ] No “mystery layers” (UI can show what it is + where it came from)  [oai_citation:35‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

### MCP reproducibility checks
- [ ] Notebook has hypothesis → method → results → conclusion structure  [oai_citation:36‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- [ ] Environment setup is documented (requirements / container notes)  [oai_citation:37‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- [ ] Outputs have a run id / timestamp and are version-controlled (or DVC-tracked)  [oai_citation:38‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)

---

## 📦 Real-time layers (optional test case)

The intake guide includes a concrete example: a **GTFS-RT watcher** that ingests live transit feeds, validates, publishes, and marks the layer as real-time with provenance and policy checks.  [oai_citation:39‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

If you want a modern “stress test” for the web viz stack:
- treat it as a separate layer category
- ensure attribution + freshness metadata are visible in the UI

---

## 📚 Resource packs (PDF portfolios) included in the project

Some project PDFs are **PDF Portfolios** (they contain embedded documents) and recommend opening in Acrobat.  [oai_citation:40‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2) [oai_citation:41‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)

### 🔧 Extract embedded PDFs locally
If you want to explore the embedded docs from a portfolio:

```bash
# list embedded files
pdfdetach -list "Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf"

# extract all (example)
mkdir -p extracted/maps_pack
pdfdetach -saveall -o extracted/maps_pack "Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf"
```

Portfolios in this project:
- 🧠 AI reading pack (portfolio)  [oai_citation:42‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- 🗺️ Maps + WebGL pack (portfolio)  [oai_citation:43‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
- 🧰 Programming resources pack (portfolio)  [oai_citation:44‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
- 🧱 Data management + data science pack (portfolio)  [oai_citation:45‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

---

## 📚 Project documents used for this notebook

> Links below use the project’s attached source files (where available).

### Core KFM system docs
- **KFM UI System Overview**  [oai_citation:46‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  [oai_citation:47‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  [oai_citation:48‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- **KFM AI System Overview (Focus Mode)**  [oai_citation:49‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:50‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- **KFM Comprehensive Architecture / Features / Design**  [oai_citation:51‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:52‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- **KFM Comprehensive Technical Documentation**  [oai_citation:53‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:54‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
- **KFM Data Intake Guide (STAC/DCAT/PROV rules)**  [oai_citation:55‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:56‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  [oai_citation:57‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Latest Ideas & Future Proposals (timeline/PMTiles/offline)**  [oai_citation:58‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:59‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- **Innovative Concepts to Evolve KFM (AR/4D)**  [oai_citation:60‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  [oai_citation:61‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  [oai_citation:62‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- **Additional Project Ideas (Pulse Threads, Conceptual Nodes)**  [oai_citation:63‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:64‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:65‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### MCP / methodology docs
- **Scientific Method / Research / Master Coder Protocol Documentation**  [oai_citation:66‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  [oai_citation:67‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- **Open-Source Mapping Hub Design (repo layout: notebooks, web, mcp)**  [oai_citation:68‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)  [oai_citation:69‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA) [oai_citation:70‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)

### Portfolio resource packs (embedded PDFs)
- **AI Concepts & more (portfolio)**  [oai_citation:71‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:72‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- **Maps / Virtual Worlds / Geospatial WebGL (portfolio)**  [oai_citation:73‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:74‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
- **Programming Languages & Resources (portfolio)**  [oai_citation:75‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  [oai_citation:76‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
- **Data Management / Data Science (portfolio)**  [oai_citation:77‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  [oai_citation:78‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

---

## 🧭 Next steps (good “follow-on” notebooks)

- `07_viz_timeline/` — deep dive into temporal indexing + uncertainty in dates
- `08_viz_story_nodes/` — authoring workflow + story-node CI validation
- `09_viz_focus_mode/` — interaction design + citation UX + “audit panel”
- `10_viz_offline_packs/` — PMTiles/COG/GeoParquet packaging + offline service worker experiments

---

### 🧡 Reminder
This notebook is **not** “just charts.” It’s the **web-facing contract layer** between:
- the provenance-first intake pipeline,
- the KFM data catalogs,
- and the map UX that the public/researchers will actually use.  [oai_citation:79‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:80‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
