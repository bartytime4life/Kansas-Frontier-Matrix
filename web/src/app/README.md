# 🌾 Kansas Frontier Matrix — Web UI (`web/src/app`)

![KFM](https://img.shields.io/badge/Kansas%20Frontier%20Matrix-Living%20Atlas-success)
![Evidence First](https://img.shields.io/badge/Provenance%E2%80%91First-Always%20Citable-blue)
![UI](https://img.shields.io/badge/UI-React%20%7C%20MapLibre-informational)
![Build](https://img.shields.io/badge/Build-Contracts%E2%86%92UI%E2%86%92Trust-brightgreen)
![License](https://img.shields.io/badge/License-Open%20Source-lightgrey)

> 🧭 **Mission (UI translation):** turn Kansas’s spatial truth into something **searchable, mappable, auditable, and modelable** — where every layer, story, and AI answer is **traceable** to evidence.  
> ✨ In KFM, *citations are not an afterthought* — they’re a UI feature.

---

## 📌 What this folder is

This directory is the **App Router / route-surface** for the KFM web app. It’s where we define:

- 🧩 **Routes & layouts** (pages, nested layouts, route groups)
- 🗺️ The **Map + Timeline** experience surfaces
- 📚 **Catalog** and **Story Node** presentation
- 🤖 **Focus Mode** (AI assistant UI) — *evidence-backed, citation-first*
- 🧱 UI scaffolding that enforces KFM’s **contract-first** architecture

> 🧠 If you’re here to “just add a button,” you still need to respect the system rules below.  
> KFM’s core promise is **trust** — and UI is where trust is either kept… or broken.

---

## 🧱 Non‑negotiables (KFM UI Contract)

These are **not preferences** — they are “don’t break the system” constraints:

- ✅ **No unsourced claims** in the UI  
  - If text asserts a fact, it must link to a source record, dataset, Story Node, or provenance bundle.
- ✅ **Never bypass the canonical pipeline**  
  - UI only renders what has passed through governance + contracts (catalogs + APIs).
- ✅ **AI output must include citations**  
  - If Focus Mode can’t cite it, it should say “Not enough evidence in KFM.”
- ✅ **Evidence is inspectable** (one click away)  
  - Users must be able to open: dataset metadata, lineage/provenance, source docs, and processing steps.
- ✅ **Provenance is first-class UI**  
  - “Where did this come from?” is a core interaction, not a hidden debug panel.

---

## 🗺️ Core Experiences (the stuff we’re building the UI around)

### 1) 🧭 Map + Timeline Explorer
**Goal:** fast, fluid exploration of spatial layers + time-based change.

Key UI primitives:
- 🧱 Layer panel (grouped, searchable, with metadata peek)
- ⏳ Timeline control (year range / time scrub)
- 🔎 Identify / inspect (click feature → show attributes + provenance)
- 🧩 Compare mode (before/after, swipe, opacity, split view)

Performance expectations:
- 🚀 Smooth pan/zoom even with heavy rasters (COGs / tiles)
- 🧊 Cached metadata + lazy loading for big catalogs

---

### 2) 🗂️ Dataset Catalog + Search
**Goal:** browse *governed* datasets, not random files.

Catalog UI should support:
- 🔍 Full-text search (title, tags, places, years)
- 🧾 Dataset cards with:
  - name + summary
  - spatial extent + time extent
  - license / access
  - **lineage/provenance link**
- 🧩 “Add to map” from the catalog
- 🧠 “Explain this dataset” (Focus Mode, with citations)

---

### 3) 📖 Story Mode (Narrative + Map choreography)
**Goal:** make KFM teachable and explorable as a “living atlas storybook.”

Story Nodes are:
- 📝 Markdown narrative + 🧩 JSON config steps
- Each step can drive:
  - active layers
  - camera position (lon/lat/zoom)
  - timeline state
  - highlights / callouts

UI expectations:
- ⏭️ Stepper controls and/or scroll-driven playback
- 🧷 Map actions synchronized to story steps
- 🧯 Always allow exit back to free exploration

---

### 4) 🤖 Focus Mode (AI Assistant)
**Goal:** answer questions *only* using KFM evidence — and show receipts.

UI expectations:
- 🧠 Chat panel docked to map context
- 🎯 Context hooks:
  - “Use current viewport”
  - “Use selected feature”
  - “Use active layers”
- 📎 Answers **must** show citations as clickable chips:
  - dataset refs, story refs, doc refs
- ⚠️ Clear labeling: “AI‑generated summary” vs “raw data”

> Focus Mode is **advisory**, not autonomous.  
> It helps users *interpret* evidence, not replace it.

---

## 🔁 Data Flow (why the UI stays trustworthy)

KFM’s “trust chain” is a pipeline — the UI is downstream of governance.

```mermaid
flowchart LR
  A[ETL / Pipelines] --> B[STAC + DCAT + PROV Catalogs]
  B --> C[Knowledge Graph (Neo4j)]
  C --> D[Contracted APIs]
  D --> E[Web UI (Map + Catalog + Story)]
  E --> F[Story Nodes + Focus Mode]
```

### 🧾 UI rule of thumb
If the UI can’t point to **(Catalog → Provenance → Source)**, it’s not shippable.

---

## 🗂️ What lives in `src/app` (conventions)

> The exact route tree may evolve — but the **shape** should stay consistent.

```text
📁 src/app/
├── 📄 README.md                      ← you are here 🙂
├── 📄 layout.tsx                     ← app shell (nav, providers, theme)
├── 📄 page.tsx                       ← landing (or redirect)
├── 📁 (app)/                         ← authenticated / main experience
│   ├── 📁 map/                        ← 🗺️ Map + Timeline
│   ├── 📁 catalog/                    ← 🗂️ datasets, layers, provenance browsing
│   ├── 📁 stories/                    ← 📖 Story Node player & index
│   ├── 📁 focus/                      ← 🤖 Focus Mode (AI panel + routes)
│   └── 📁 settings/                   ← ⚙️ user preferences (units, basemaps, etc.)
├── 📁 (marketing)/                   ← public pages (optional)
└── 📁 api/                           ← (if used) route handlers / proxy endpoints
```

### 🧩 UI module pattern (recommended)
- `src/app/**/_components/` → route-local components
- `src/app/**/_lib/` → route-local helpers (fetchers, parsers)
- `src/app/**/_schemas/` → UI-side contract validation (zod/jsonschema)
- `src/app/**/_styles/` → route-scoped styles (avoid global leaks)

---

## 📦 Contracts the UI must respect

The UI should treat these as **interfaces**, not suggestions:

- 🗺️ **STAC** → spatial assets (rasters, vectors, collections, items)
- 🧾 **DCAT** → dataset catalog semantics (publisher, license, distribution)
- 🧬 **PROV** → lineage + auditability (what produced what, when, how)
- 📖 **Story Node schema** → narrative + map choreography
- 📊 **Telemetry schema** → performance + UX metrics (privacy-aware)

> ✅ “Contract-first” means: UI validates and fails *loudly* when contracts drift.

---

## 🧩 Map rendering stack (performance & clarity)

### 🎛️ Baseline
- **MapLibre** (2D) for interactive mapping
- Optional: **3D / WebGL overlays** when the data truly needs it (avoid novelty 3D)

### 🧱 Raster strategy (big data friendly)
Prefer:
- 🧊 **Cloud‑Optimized GeoTIFFs (COGs)** for partial reads / tile-like access
- 🧱 Pre-generated tiles (TileJSON / MBTiles / tile folders) for heavy “always-on” layers

Avoid:
- ❌ shipping multi‑GB rasters directly to the browser without tiling/COG strategy

### 🧾 Vector strategy
- Small layers: GeoJSON (bounded size)
- Large layers: vector tiles (server or prebuilt) + on-demand feature fetch

### 🗺️ Cartography rules (UI-level guardrails)
- 🎨 Color ramps must be interpretable & accessible
- 🧭 Always explain symbology (legend!)
- 🧱 Never hide uncertainty: show confidence/quality metadata when available

---

## 📖 Story Nodes (how UI should load & render)

**Stories are authored, governed content.** UI behavior:
- Load Story Node markdown and render as safe HTML
- Load Story Node step config (JSON) and apply deterministic map actions:
  - layers on/off
  - camera move
  - timeline update
  - highlight geometry / features

> 🧯 Security note: treat story markdown as untrusted input → sanitize render.

---

## 🤖 Focus Mode (AI) — UI responsibilities

UI must:
- ✅ visibly label AI text as an AI-generated synthesis
- ✅ require citations and show them as clickable sources
- ✅ provide context controls (viewport/selection/layers)
- ✅ let users open cited evidence quickly
- ✅ provide an “export answer with citations” affordance (copy/share)

UI must not:
- ❌ imply AI is authoritative
- ❌ allow uncited answers
- ❌ auto-trigger “actions” (policy decisions, alerts, etc.)

---

## ⚡ Performance & scale checklist

Because KFM spans **maps + time + big data**:

- 🧊 Cache catalogs (STAC/DCAT) aggressively
- 🧠 Lazy-load heavy UI chunks (map controls, story player, search index)
- 🧵 Use Web Workers for heavy parsing / indexing
- 🪟 Virtualize big lists (datasets, layers, features)
- 🧱 Avoid rendering full-geometry vectors at high zoom levels unless needed
- 📉 Establish performance budgets:
  - initial load ≤ “feels instant”
  - map interaction stays at “smooth”

---

## ♿ Accessibility (a must, not a stretch goal)

- ⌨️ Keyboard navigation for map controls (focus states must be obvious)
- 🗣️ ARIA labels for toolbars and controls
- 🌓 Theme contrast that respects WCAG
- 📍 “You are here” state for story stepper + timeline
- 🧠 Reduce motion option for story transitions

---

## 🔐 Security & trust (front-end basics we don’t skip)

- 🔑 Never ship secrets to the client
- 🧼 Sanitize any markdown/HTML rendering
- 🧯 Treat all query params as untrusted
- 🧊 Prefer read-only access patterns for public deployments
- 🧾 Show licensing & attribution on every dataset view

> 🛡️ KFM’s trust story collapses if the UI is exploitable or misleading.

---

## 🧑‍💻 Local development (typical)

> Your repo root may define the authoritative commands — this is a sane default.

```bash
# from /web
npm install

# run dev server
npm run dev

# build
npm run build

# lint
npm run lint

# tests (if configured)
npm test
```

### 🔧 Environment variables (example)
Create `web/.env.local`:

```bash
# Core
NEXT_PUBLIC_APP_NAME="Kansas Frontier Matrix"

# API boundary (optional if running fully static)
NEXT_PUBLIC_KFM_API_BASE_URL="http://localhost:8080"

# Catalog roots (static hosting, S3, etc.)
NEXT_PUBLIC_STAC_ROOT_URL="http://localhost:8080/catalog/stac"
NEXT_PUBLIC_DCAT_ROOT_URL="http://localhost:8080/catalog/dcat"
NEXT_PUBLIC_PROV_ROOT_URL="http://localhost:8080/prov"

# Map tiles / styles
NEXT_PUBLIC_MAP_STYLE_URL="http://localhost:8080/styles/kfm.json"
NEXT_PUBLIC_TILE_BASE_URL="http://localhost:8080/tiles"
```

---

## ✅ PR checklist (keep us honest)

- [ ] New UI text is citable (links to evidence)
- [ ] Story steps are deterministic and replayable
- [ ] Focus Mode answers show citations, and citations open correctly
- [ ] Performance: no obvious regressions (bundle size, map FPS)
- [ ] Accessibility: keyboard + screen reader basics checked
- [ ] Mobile: layout doesn’t collapse into sadness 📱😅

---

## 📚 Reference Shelf (project library → UI decisions)

These docs are part of the project’s “knowledge toolbox.” They inform how we build a UI that’s
**usable**, **correct**, and **scalable**.

### 🗺️ Mapping, cartography, mobile & 3D
- **Making Maps: A Visual Guide to Map Design for GIS** (symbology, layout, readability)
- **Mobile Mapping: Space, Cartography and the Digital** (map UX in real-world contexts)
- **Archaeological 3D GIS** (3D interpretation + spatial storytelling patterns)
- **WebGL Programming Guide** (custom rendering & GPU mental models)

### 🛰️ Remote sensing & imagery
- **Cloud-Based Remote Sensing with Google Earth Engine** (big raster workflows + analysis patterns)
- **Compressed Image File Formats** (pragmatic tradeoffs for web delivery)

### 🧬 Data, databases & scale
- **PostgreSQL Notes for Professionals** (practical DB patterns)
- **Database Performance at Scale** (latency, throughput, indexing, scale thinking)
- **Scalable Data Management for Future Hardware** (system-level performance perspectives)
- **Data Spaces** (interoperability + multi-source integration mindset)

### 📊 Stats, modeling, simulation & uncertainty (for analytics panels + evidence language)
- **Understanding Statistics & Experimental Design**
- **Regression Analysis with Python** + *(slides)*
- **Graphical Data Analysis with R**
- **Think Bayes**
- **Scientific Modeling & Simulation (NASA-grade guide)**

### 🧠 AI, governance, and human-centered responsibility
- **Introduction to Digital Humanism** (transparency, accountability, humane design)
- **On the path to AI Law’s prophecies…** (conceptual + legal framing for ML-era systems)
- **Deep Learning for Coders (fastai + PyTorch)** (model literacy for the team)

### 🔐 Security awareness (UI + API boundary hygiene)
- **Ethical Hacking and Countermeasures**
- **Gray Hat Python**

### 📚 General programming compendiums (team reference)
- **A / B‑C / D‑E / F‑H / I‑L / M‑N / O‑R / S‑T / U‑X programming Books** (broad patterns & snippets)

---

## 🔗 Related KFM docs (start here)
From this folder, you’ll usually want to jump to:

- 📘 `../../../docs/MASTER_GUIDE_v13.md` (canonical repo structure + rules)
- 🧭 `../../../docs/architecture/` (blueprints, ADRs)
- 📖 `../../../docs/reports/story_nodes/` (draft + published story content)
- 🧾 `../../../schemas/` (STAC/DCAT/PROV/story/telemetry schemas)

---

<details>
<summary><strong>🧠 Design mantra (repeat until it’s instinct)</strong></summary>

- “If it can’t be cited, it can’t be shipped.”
- “One fact, one place.”
- “Provenance is a feature.”
- “Maps tell stories — stories must be auditable.”

</details>
