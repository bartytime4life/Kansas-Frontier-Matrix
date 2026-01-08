<!-- web/story_nodes/README.md -->

# 🧩 Story Nodes — `web/story_nodes`

![KFM](https://img.shields.io/badge/KFM-System-blue)
![Pipeline](https://img.shields.io/badge/Pipeline-ETL→Catalogs→Graph→API→UI→Story%20Nodes→Focus%20Mode-brightgreen)
![Evidence](https://img.shields.io/badge/Trust-Evidence--First-yellow)
![FAIR+CARE](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-orange)
![UX](https://img.shields.io/badge/UX-Focus%20Mode-9cf)

> **Story Nodes** are the “governed narrative layer” of Kansas Frontier Matrix (KFM):  
> **markdown + semantics + citations + map/timeline/3D state**, designed to be both **human-readable** and **machine-ingestible**. 🧠🗺️

This folder focuses on **web runtime** concerns: how the UI **loads, validates, renders, version-locks, and visualizes** Story Nodes (and their assets) in **Focus Mode**.

---

<details>
<summary><strong>📚 Contents</strong> (click to expand)</summary>

- [Why this folder exists](#why-this-folder-exists)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [What is a Story Node](#what-is-a-story-node)
- [Focus Mode contract](#focus-mode-contract)
- [Recommended folder layout](#recommended-folder-layout)
- [Story Node anatomy](#story-node-anatomy)
- [Versioning & reproducibility](#versioning--reproducibility)
- [Visualization assets & overlays](#visualization-assets--overlays)
- [Validation & CI gates](#validation--ci-gates)
- [Security & safety notes](#security--safety-notes)
- [PR checklist](#pr-checklist)
- [Project library mapping](#project-library-mapping)
- [Glossary](#glossary)

</details>

---

## Why this folder exists

Story Nodes sit **after** the UI in the canonical pipeline, but the **web client** is responsible for:

- ✅ Fetching Story Nodes via **API contracts** (never directly from the graph)
- ✅ Rendering Story Nodes with **trust cues** (citations, provenance badges, “fact vs interpretation”)
- ✅ Driving the **map/timeline/3D** state from the node metadata
- ✅ Enforcing **version locks** so a reader can reproduce what they saw
- ✅ Respecting **FAIR+CARE** and redaction rules (especially for sensitive locations)

---

## Non-negotiable invariants

These are “hard rails” that keep the whole system defensible 🔒:

1. **Pipeline ordering is absolute**  
   `ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode`

2. **API boundary rule**  
   The web app must not query Neo4j directly. Everything comes through contracted endpoints.

3. **Provenance-first narrative**  
   No Story Node should ship with “trust me” content. Every claim needs traceable evidence.

4. **Deterministic + reproducible UX**  
   A Story Node view should be reconstructible via:
   - node id + version id  
   - map state + layer versions  
   - asset checksums  
   - provenance bundle references

---

## What is a Story Node

A Story Node is a **markdown document with embedded structure**:

- **Provenance for every claim** (citations to cataloged evidence, not just secondary summaries)
- **Graph entity references** (stable IDs for people, places, events, documents, datasets)
- **Fact vs interpretation separation** (especially critical when AI tooling is involved)
- **Visualization bindings** (map layers, overlays, timeline cues, and optional 3D scenes)

Think of it as:

> 📄 *Narrative text* + 🧾 *evidence pointers* + 🕸️ *graph links* + 🧭 *UI state*

---

## Focus Mode contract

**Focus Mode** is the “reading cockpit” 🚀:

- Story on one side
- Map + timeline + panels on the other
- Every interactive cue must remain **evidence-linked and governed**

### What Focus Mode must do (minimum)

- Show citations / footnotes clearly (and make them clickable)
- Show entity chips (place/person/event) that resolve via the API
- Allow “inspect provenance” on:
  - datasets
  - overlays
  - analysis outputs
- Respect governance (CARE/sovereignty) via:
  - generalization of sensitive coordinates
  - restricted content banners / redaction

---

## Recommended folder layout

> Adjust to match your actual repo structure — this is the **intended shape** for the web layer.

```text
📁 web/
└── 📁 story_nodes/
    ├── 📄 README.md                     # (this file)
    ├── 📁 schema/                       # JSON schema(s) for runtime validation
    │   ├── 🧾 story_node.v3.schema.json
    │   └── 🧾 focus_overlay.v10.schema.json
    ├── 📁 types/                        # TS types + helpers
    │   ├── 🧩 storyNode.ts
    │   ├── 🧩 focusMode.ts
    │   └── 🧩 overlays.ts
    ├── 📁 registry/                     # manifest(s) for discovery + navigation
    │   ├── 🗂️ storyNodes.index.json
    │   └── 🗂️ tags.index.json
    ├── 📁 loaders/                      # fetch + parse + validate
    │   ├── ⛏️ fetchStoryNode.ts
    │   ├── ✅ validateStoryNode.ts
    │   └── 🧼 sanitizeMarkdown.ts
    ├── 📁 renderers/                    # UI render components
    │   ├── 🧾 StoryNodeRenderer.tsx
    │   ├── 🧭 MapBindings.tsx
    │   └── 🧪 EvidencePanel.tsx
    ├── 📁 assets/                       # story-node-owned assets (thumbnails, local overlays)
    │   ├── 🖼️ thumbs/
    │   └── 🧩 overlays/
    └── 📁 __tests__/                    # snapshot + schema tests
        ├── 🧪 storyNodes.schema.test.ts
        └── 🧪 storyNodes.render.test.ts
```

---

## Story Node anatomy

### 1) Front matter (YAML) = machine contract 🧾

Suggested minimum fields:

- `id` (stable slug)
- `version` (semver or date-version)
- `status` (`draft | review | published | deprecated`)
- `title`, `summary`
- `time_range` (start/end)
- `spatial` (bbox + optional center/zoom)
- `entities[]` (graph IDs)
- `evidence[]` (catalog references: STAC/DCAT/PROV pointers)
- `ui` (map layers, overlays, camera, panels, etc.)
- `care` / `sensitivity` flags (if applicable)

Example (template-ish):

```yaml
---
id: ks.1860.terrain.tichenor-elevation
version: 1860.0.1
status: draft
title: "3D Terrain Story: Elevation Model (Kansas, 1860)"
summary: "A reproducible walkthrough of historical terrain evidence and its implications."
time_range:
  start: 1860-01-01
  end: 1860-12-31
spatial:
  bbox: [-102.05, 37.00, -94.60, 40.00]
  center: [-98.30, 38.50]
  zoom: 6
entities:
  - graph:place:ks
  - graph:dataset:tichenor_elevation_1860
evidence:
  - stac:item:ks-elevation-tichenor-1860
  - dcat:dataset:ks-elevation-historic
  - prov:bundle:run-2025-11-10-tichenor
ui:
  mode: focus
  map:
    layers:
      - id: basemap.terrain
      - id: hydrology.rivers
    overlays:
      - overlay_id: focusmode_overlay_drought_v10_2025
  scene_3d:
    engine: cesium
    camera_path: "camera/ks_1860_walkthrough.json"
care:
  sensitivity_level: low
  redaction_required: false
---
```

### 2) Markdown body = narrative + citations ✍️

Keep the markdown body readable and structured:

- `## Claims` (facts + citations)
- `## Interpretation / hypothesis` (clearly labeled)
- `## Methods` (how the evidence was processed)
- `## What changed vs previous version` (diff summary)

---

## Versioning & reproducibility

Story Nodes become truly powerful when they support **time-travel** 🕰️:

### Recommended capabilities

- **Version strip** in UI:
  - predecessor → current → successor
  - “latest” label
  - deprecated flag
  - keyboard navigation
  - click-to-diff

- **Version lock**:
  - Freeze map layers to that node version
  - Disable auto-updating datasets
  - Lock charts/tables to the version
  - Emit telemetry: `version_locked`

### Diff model (minimum)

When diffing versions, compare:

- Metadata fields (title, summary, tags, time range)
- Asset inventory (added/removed/changed checksums)
- Geometry diffs (GeoJSON / tiles)
- Raster diffs (pixel or checksum)
- Semantic diffs (optional; report-only)

---

## Visualization assets & overlays

Story Nodes frequently bind to overlays and visual layers (especially in Focus Mode).  
This is where **trust + accessibility** becomes visible.

### Overlay types (common)

| Overlay Type 🧩 | Use | Typical Format |
|---|---|---|
| Hydrology overlays 🌊 | drought/flood indices, moisture gradients | PNG / WebP |
| Settlement density 🏘️ | KDE surfaces, clustering | PNG / WebP |
| Treaty / boundary context 🧾 | treaty polygons, disputed lines | SVG |
| Narrative alignment 🧠 | model-backed “why here” signals | JSON |
| Temporal dynamics ⏱️ | time-series change layers | PNG / WebP |

### Overlay metadata requirements (web must enforce)

Each overlay should have a metadata entry with:

- stable `id`
- `type` + `domain`
- `care_status` + `fairstatus`
- `asset_file` + `checksum_sha256`
- `generated_by` + timestamp
- `stac_extensions[]` (if raster/geo)
- `alt_text` (required ✅)

Accessibility rules ♿:

- Minimum contrast ratio **4.5:1**
- Avoid red–green-only encoding (use texture/shape)
- Provide static fallback for animated overlays

---

## Validation & CI gates

Treat Story Nodes like **shipping code**, not “just docs” ✅

### Minimum checks

- Markdown lint + formatting
- No secrets / credentials / tokens
- Links stable where possible (prefer DOI/permalink)
- Evidence references resolve to catalog entries
- Schema validation (front matter + overlays)
- Asset existence + checksum match
- CARE redaction flags respected (no sensitive coordinate leakage)
- Render snapshot tests (prevent UI regressions)

---

## Security & safety notes

Story Nodes are a high-leverage surface area for UI integrity 🔐:

- Sanitize markdown → prevent XSS
- Do not allow arbitrary HTML injection in markdown body
- Treat external links as untrusted (open in new tab + rel protections)
- Never render raw coordinates for sensitive content when redaction is required
- Prefer **checksums + manifests** for released assets (supply-chain friendliness)

---

## PR checklist

Use this when adding or modifying Story Nodes ✅

### Content integrity
- [ ] Every factual claim has a citation (STAC/DCAT/PROV or cataloged external)
- [ ] Fact vs interpretation is clearly labeled
- [ ] AI-assisted text is labeled and does not introduce unsourced claims

### UX & accessibility
- [ ] All overlays have `alt_text`
- [ ] Contrast ≥ 4.5:1 and no red–green-only encoding
- [ ] Story renders cleanly on mobile + desktop

### Reproducibility
- [ ] Node has version metadata
- [ ] Assets have checksums and are inventory-able
- [ ] Version diff summary included (when updating)

### Governance
- [ ] CARE / sovereignty flags set appropriately
- [ ] Sensitive locations generalized or masked
- [ ] License notes are present for any redistributed material

---

## Project library mapping

This repo’s Story Node system is informed by a broad set of project references 📚  
(These are *inputs to design decisions* — don’t copy licensed content into public docs unless allowed.)

### 🧭 Architecture, governance, and KFM vision
- **KFM Master Guide / Markdown Protocol** — Story Nodes + Focus Mode rules, contracts-first approach
- **Kansas Frontier Matrix design docs** — system vision, geospatial + narrative hub design
- **KFM Engineering + Design Audit docs** — domain gaps, enhancement opportunities, and pipeline design notes
- **Latest Ideas / Other Ideas** — operational patterns: overlays, version locks, telemetry, CI gates

### 🗺️ Geospatial + visualization
- **Making Maps (GIS design)** — cartography clarity, symbol hierarchy, legend discipline
- **Mobile Mapping** — context-aware storytelling, map UX on constrained devices
- **Python Geospatial Analysis Cookbook** — ETL/processing patterns that become story evidence artifacts
- **Cloud Remote Sensing w/ Google Earth Engine** — remote sensing-derived layers + reproducible outputs
- **WebGL Programming Guide** — interactive 3D techniques for story scene nodes
- **Responsive Web Design (HTML/CSS)** — layout patterns for Focus Mode + narrative panels
- **Compressed image formats** — choosing PNG/WebP/SVG wisely for story assets

### 📈 Statistics, modeling, and “evidence quality”
- **Scientific Modeling & Simulation (NASA-grade guide)** — reproducibility, validation mindset for model-backed nodes
- **Understanding Statistics & Experimental Design** — defensible inference + uncertainty communication
- **Regression analysis w/ Python** (+ linear regression slides) — analysis nodes, diagnostics, explainability
- **Graphical Data Analysis with R** — EDA visuals + distribution sanity checks
- **Think Bayes** — Bayesian updates, uncertainty as a first-class story element
- **Spectral Geometry of Graphs** — graph analytics foundations (useful for network-based story claims)
- **Topology optimization** — optimization narratives, constraint-driven design stories
- **Scalable Data Management for Future Hardware** — performance strategies for graph/query workloads backing story views

### 🧠 AI, data mining, and legal framing
- **Data Mining Concepts & Applications** — clustering/classification patterns that should be narrated responsibly
- **Data Spaces** — interoperability, governance, and data product thinking
- **AI Law foundations** — policy/ethics framing for AI-assisted narrative components
- **Deep Learning for Coders (fastai/PyTorch)** — ML story nodes (model cards, dataset shift, evaluation)

### 🔐 Security + resilience
- **Ethical Hacking & Countermeasures** — threat modeling and hardening mindset
- **Gray Hat Python** — defensive awareness for parsing/rendering content safely
- **Concurrent / real-time / distributed Java** — concurrency patterns for future tooling or services
- **PostgreSQL Notes** — storage and indexing patterns for Story Node catalogs and metadata

### 🧰 Programming reference compendiums (fast lookup)
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

---

## Glossary

- **Story Node** 🧩: A governed narrative unit (markdown + semantics + citations + UI bindings).
- **Focus Mode** 🎛️: The interactive reading experience that pairs story + map + timeline + evidence panels.
- **Evidence bundle** 🧾: The referenced STAC/DCAT/PROV artifacts that support claims.
- **Overlay** 🖼️: A visualization asset (raster/vector/json) bound into map/3D state with metadata + checksums.
- **Version lock** 🔒: Freezes the UI to a specific node+dataset version for reproducibility.
- **CARE** 🪶: Governance principle set for collective benefit, authority to control, responsibility, ethics.
- **FAIR** 🔎: Findable, Accessible, Interoperable, Reusable data principles.

---

<div align="center">

**Kansas Frontier Matrix** · `web/story_nodes`  
🧠 Evidence-first · 🧾 Provenance-linked · 🗺️ Map-native storytelling

</div>

