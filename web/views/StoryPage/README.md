# 🧭 StoryPage — Story Nodes (Scrollytelling ✍️ + Map Sync 🗺️)

![React](https://img.shields.io/badge/React-SPA-61DAFB?logo=react&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-typed-blue?logo=typescript&logoColor=white)
![Maps](https://img.shields.io/badge/MapLibre-2D%20maps-success)
![3D](https://img.shields.io/badge/Cesium-3D%20tiles-success)
![KFM](https://img.shields.io/badge/KFM-contract--first%20%26%20evidence--first-yellow)

> **StoryPage** is the KFM view that turns governed data + provenance into **interactive narratives** called **Story Nodes** — a guided tour where the **map state (2D/3D, layers, time)** stays synchronized with the **narrative text, media, and citations**.

---

## 📌 What lives here

**Path:** `web/views/StoryPage/`  
**Primary job:** Render a *Story Node* as a **narrative panel + synchronized map playback**, and provide clean integration hooks to:

- 🗺️ **Map viewers** (MapLibre 2D + Cesium 3D)
- 🧾 **Citations / provenance UI** (attribution, footnotes, dataset provenance links)
- 🧠 **Knowledge graph linking** (turn story mentions into graph-backed interactions)
- 🤖 **Focus Mode** (optional AI panel, citations-first + audit-friendly)

---

## 🧩 Table of contents

- [🧠 Core concepts](#-core-concepts)
- [✅ Non-negotiable KFM invariants](#-non-negotiable-kfm-invariants)
- [📁 Suggested folder layout](#-suggested-folder-layout)
- [📚 Story Node content model](#-story-node-content-model)
- [🗺️ Map sync contract](#️-map-sync-contract)
- [🔗 Knowledge graph linking](#-knowledge-graph-linking)
- [🤖 Focus Mode integration](#-focus-mode-integration)
- [🧪 Testing & validation](#-testing--validation)
- [⚡ Performance](#-performance)
- [🔐 Security](#-security)
- [♿ Accessibility](#-accessibility)
- [🛰️ Telemetry & audit trails](#️-telemetry--audit-trails)
- [🛠️ Authoring workflow](#️-authoring-workflow)
- [🗺️ Troubleshooting](#️-troubleshooting)
- [🧭 Roadmap](#-roadmap)
- [📚 Project library](#-project-library)
- [📖 Glossary](#-glossary)

---

## 🧠 Core concepts

### Story Node ✍️
A **Story Node** is a governed narrative unit that pairs:

- **Markdown** → the narrative text (with images, citations, footnotes)
- **JSON config** → the step-by-step “map choreography” (layers, camera, time, highlights)

### Step 🎞️
A story is divided into **steps** (“slides” or scroll sections). Each step can:

- set the **map camera** (lon/lat/zoom or 3D view)
- toggle **layers** & style/opacity
- set **timeline** (year/date/range)
- call attention to **features** (highlight / label / focus)

### StoryPage UI pattern 🧭
Common layout pattern:

- **Left panel:** narrative + step navigation + citations
- **Right panel:** map viewer (2D/3D)
- Optional: **bottom timeline slider** & **layer control panel**

---

## ✅ Non-negotiable KFM invariants

StoryPage must enforce and *make visible* the project’s “trust contract”:

- 🧾 **Contract-first + provenance-first:** anything shown in the UI must trace back to cataloged sources + versioned processing.
- 🚫 **No mystery layers:** if a layer appears in a story, StoryPage must be able to show attribution/lineage/contract metadata.
- 🧱 **Evidence-first pipeline:** stories are downstream of catalogs → graph → APIs → UI (no leapfrogging).
- ✅ **CI-backed validation:** Story Nodes should fail CI if citations/contracts are missing or schemas are invalid.
- 🧭 **Draft vs Published:** story content should support a governed lifecycle (draft → reviewed → published).

📎 Recommended reading:
- `../../../docs/MASTER_GUIDE_v13.md`
- `../../../docs/reports/story_nodes/`

---

## 📁 Suggested folder layout

> Adjust names to match the current codebase — this is the **intended** shape for a clean StoryPage subsystem.

```text
web/
└─ 📁 views/
   └─ 📚 StoryPage/
      ├─ ✅📄 README.md                    # you are here 📌 Overview, responsibilities, and integration points
      │
      ├─ 🧭📄 StoryPage.tsx                # route-level view: page layout + orchestration (data, map, playback, UI)
      │
      ├─ 🧩 components/                   # UI building blocks for the Story experience
      │  ├─ 🧾 StoryHeader.tsx             # title, subtitle, badges, share/print entrypoints
      │  ├─ 🧱 StoryStep.tsx               # renders a single step (markdown + blocks + step chrome)
      │  ├─ 🧭 StepNav.tsx                 # step-to-step navigation (prev/next, list, keyboard)
      │  ├─ 📍 ProgressRail.tsx            # progress indicator / scroll position visualization
      │  ├─ 📚 CitationsDrawer.tsx         # evidence/citations UI (expandable drawer/panel)
      │  ├─ 🏷️ AttributionBar.tsx          # required credits/licensing strip (layer + media attribution)
      │  └─ 🚨 StoryErrorState.tsx         # graceful error UI (missing story, validation failure, offline)
      │
      ├─ 🪝 hooks/                        # Story state + side-effects (loading, playback, map coupling)
      │  ├─ 📥🪝 useStoryNode.ts           # loads story content + validates against schema/contract
      │  ├─ ▶️🪝 useStoryPlayback.ts       # step index + scroll↔step sync + playback controls
      │  └─ 🗺️🪝 useMapStoryActions.ts     # applies step actions to the map (camera/layers/time/highlights)
      │
      ├─ 🧰 lib/                          # Pure-ish logic: parsing, validation, action interpretation
      │  ├─ 📐🛡️ storySchema.ts            # schema wrapper (zod/jsonschema) + helpers
      │  ├─ 🎬 storyActions.ts             # action interpreter (camera/layers/time/highlights)
      │  ├─ 🧼📝 markdownPipeline.ts        # markdown → sanitized HTML pipeline
      │  └─ 🧾📚 citations.ts              # parse footnotes + build normalized citation list
      │
      ├─ 🎨 styles/                       # Component-scoped styling
      │  └─ 🎨📄 storyPage.module.css      # StoryPage layout + typography + responsive rules
      │
      └─ 🧪 __tests__/                    # Unit tests for contracts + action behavior
         ├─ 🧪📐 storySchema.test.ts
         └─ 🧪🎬 storyActions.test.ts
```

---

## 📚 Story Node content model

### Where Story Nodes live 📂

KFM v13 treats Story Nodes as **governed docs** (source-of-truth), typically:

```text
📁 docs/
  📁 reports/
    📁 story_nodes/
      📁 draft/
      📁 published/
```

> A build/publish step may optionally copy **published** nodes into a web-consumable location, but the governed `docs/` tree remains the canonical authoring home.

### Recommended story package 📦

A single story should be a self-contained folder:

```text
📁 docs/reports/story_nodes/published/dust_bowl_1930s/
  📄 story.md
  📄 story.json
  📁 assets/
    🖼️ hero.jpg
    🖼️ figure_01.png
    🎥 clip_01.mp4
```

---

### `story.md` (recommended shape)

Use the Story Node template (v3) and keep it predictable.

```markdown
---
id: dust_bowl_1930s
title: "Dust Bowl: Kansas in the 1930s"
status: published
version: 1.0.0
authors:
  - name: "KFM Team"
created: 2026-01-01
updated: 2026-01-10
tags: ["climate", "migration", "agriculture"]
datasets:
  - id: "dcat:some-dataset-id"
    role: "primary"
---

# Dust Bowl: Kansas in the 1930s

## Step 1 — Before the storms
Narrative text here... [^1]

## Step 2 — Drought and dust
More narrative... [^2]

[^1]: Full citation / dataset contract link
[^2]: Full citation / dataset contract link
```

### `story.json` (step choreography)

> This is the **map-sync contract**. StoryPage should treat this file as the source of step logic.

```json
{
  "id": "dust_bowl_1930s",
  "version": "1.0.0",
  "mode": "scrollytelling",
  "steps": [
    {
      "id": "step-1",
      "title": "Before the storms",
      "contentAnchor": "step-1---before-the-storms",
      "map": {
        "view": "2d",
        "camera": { "center": [-98.0, 38.5], "zoom": 6.2, "bearing": 0, "pitch": 0 },
        "time": { "type": "year", "value": 1928 }
      },
      "layers": [
        { "id": "landcover_1920s", "visible": true, "opacity": 0.9 }
      ],
      "highlights": [
        { "type": "bbox", "bounds": [-102.0, 36.8, -94.6, 40.0], "label": "Kansas" }
      ]
    }
  ]
}
```

---

## 🗺️ Map sync contract

StoryPage should implement a **small, deterministic** interpreter for step actions:

### Supported step actions ✅ (recommended minimum)

- 🎥 `camera`  
  - 2D: center/zoom/bearing/pitch  
  - 3D: destination/heading/pitch/range OR Cesium camera params
- 🧅 `layers[]`  
  - toggle visibility, set opacity, set style overrides (safe subset)
- 🕰️ `time`  
  - set global timeline value/range, and notify time-filtered layers
- ✨ `highlights[]`  
  - highlight features/areas/labels in a non-destructive overlay layer
- 🧭 `view`  
  - switch between `2d` and `3d` *only when the story step requires it*

### A clean rule of thumb 🧼
**A step should never directly “poke” MapLibre/Cesium APIs from random UI components.**  
Route everything through one adapter (e.g., `useMapStoryActions()`), so behavior is testable and consistent.

---

## 🔗 Knowledge graph linking

Story Nodes can be more than static markdown:

- Turn references (people, places, events, datasets) into **interactive links**
- On hover/click, show a **graph-backed info panel** (with citations)

### Practical pattern
1. Parse/transform markdown into HTML.
2. Detect “entity tokens” (by convention) and replace with components:
   - `@place(neo4j:Place:uuid)`
   - `@person(neo4j:Person:uuid)`
   - `@dataset(dcat:dataset-id)`

> Keep this **opt-in** and schema-backed. Don’t invent magical parsing rules that authors can’t predict.

---

## 🤖 Focus Mode integration

StoryPage should be able to open Focus Mode **in-context**:

- “Ask about this step”
- “Explain this layer”
- “Show sources”

### Guardrails 🧱
- Always pass **context pointers**, not raw guesses:
  - story id + step id
  - active layer ids
  - time selection
  - map bounds
  - relevant graph node ids
- Focus Mode responses should surface **citations** and **provenance**, not just narrative.

---

## 🧪 Testing & validation

### Validation gates ✅
Story Nodes should be validated *before* rendering:

- JSON schema validation for `story.json`
- frontmatter validation for `story.md`
- link checking (assets, dataset refs)
- citation completeness (minimum bar varies per story type)

### Suggested test layers 🧰
- **Unit**: story schema parsing + action interpreter
- **Integration**: StoryPage loads a story, renders markdown, and applies step actions
- **E2E**: “open story → step forward → map changes → citations open → exit story”

---

## ⚡ Performance

StoryPage should feel instant even when story content is rich:

- 🧠 **Prefetch next step** assets (images, lightweight JSON, thumbnails)
- 🧵 **Debounce/Throttle** map updates during scroll-driven stories
- 🧊 **Cache** story manifests & markdown (memory + HTTP cache headers)
- 🧅 **Lazy-load** heavy layers / 3D tiles only on steps that require them
- 🪄 Use virtualization for long narratives (if a story has many steps)

---

## 🔐 Security

StoryPage is a common attack surface (markdown + links + assets):

- 🧼 **Sanitize markdown HTML** (no script, no inline event handlers)
- 🔗 Enforce safe link behavior:
  - add `rel="noopener noreferrer"` to external links
  - consider allowlist for embedded media
- 🧷 Avoid leaking private/sensitive content in stories:
  - respect governance rules + redaction notices
- 🛡️ If a “Story Builder” UI exists:
  - treat all save/publish endpoints as privileged actions
  - require auth + CSRF protections + audit logs

---

## ♿ Accessibility

Minimum expectations:

- ⌨️ Full keyboard navigation (step next/prev, citations drawer, exit)
- 🗣️ ARIA labels for step regions and controls
- 🎛️ Respect reduced motion (`prefers-reduced-motion`) for map fly-to animations
- 🧾 Provide readable focus indicators & skip links

---

## 🛰️ Telemetry & audit trails

Telemetry should help answer:

- “What step did a user view?”
- “What citations were opened?”
- “Did we show a redaction notice?”
- “Which layers were activated by a story step?”

Recommended events (names are examples):

- `story_opened`
- `story_step_changed`
- `story_citation_opened`
- `story_exited`
- `focus_mode_opened`
- `focus_mode_redaction_notice_shown`

> Keep telemetry payloads **privacy-safe** and aligned with governance requirements.

---

## 🛠️ Authoring workflow

### 1) Evidence first 🧾
Before writing narrative, ensure referenced datasets exist and are cataloged (STAC/DCAT/PROV).

### 2) Create the story (draft) ✍️
Create:

- `docs/reports/story_nodes/draft/<story_id>/story.md`
- `docs/reports/story_nodes/draft/<story_id>/story.json`
- `docs/reports/story_nodes/draft/<story_id>/assets/*`

### 3) Validate locally ✅
Run schema validation + link check + markdown lint.

### 4) PR review 🧑‍⚖️
Review focuses on:
- accuracy of claims
- citations completeness
- UI behavior (steps match narrative)
- accessibility

### 5) Publish 🚀
Move to `published/` and ensure CI passes.

---

## 🗺️ Troubleshooting

**Map doesn’t update when changing steps**
- Confirm step has `map` block
- Confirm action interpreter is receiving the step change event
- Check layer IDs match catalog/layer registry IDs

**Story renders but citations drawer is empty**
- Confirm markdown footnotes exist
- Confirm markdown pipeline preserves footnote tokens
- Confirm story config provides dataset refs where required

**3D step is slow**
- Ensure 3D tiles load only on steps requiring 3D
- Reduce tile density / use LOD
- Consider a “loading” interstitial step for heavy 3D transitions

---

## 🧭 Roadmap

- 🧙‍♂️ **Story Builder GUI** (non-developers can create stories without editing JSON)
- 🎚️ More polished **Map + Timeline MVP** (layer groups, opacity UI, time filtering)
- 🏔️ “**Kansas From Above**” 3D demo story (2D → 3D blended narrative)
- 🔎 Richer **graph linking** (auto-suggest entities + inline provenance chips)
- 🧾 Auto-generated **bibliography panel** from dataset contracts + footnotes

---

## 📚 Project library

<details>
<summary>📚 Click to expand the full KFM project library that informs StoryPage design</summary>

### 🧱 KFM architecture, governance, and contracts
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `MARKDOWN_GUIDE_v13.md` (Master Guide v13)
- `Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf`
- *(Referenced in docs)* `Audit of the Kansas Frontier Matrix (KFM) Repository.pdf`
- *(Referenced in docs)* `Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx`

### 🗺️ GIS, cartography, and geospatial storytelling
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- `Archaeological 3D GIS_26_01_12_17_53_09.pdf`
- `python-geospatial-analysis-cookbook.pdf`
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`

### 🌍 2D/3D rendering + interaction
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- *(KFM stack references)* MapLibre + Cesium + 3D Tiles

### 📱 Web UX / front-end foundations
- `responsive-web-design-with-html5-and-css3.pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### 🛰️ Remote sensing
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`

### 📊 Statistics, uncertainty, and analysis literacy
- `Understanding Statistics & Experimental Design.pdf`
- `graphical-data-analysis-with-r.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`

### 🗄️ Data systems & performance
- `Database Performance at Scale.pdf`
- `Scalable Data Management for Future Hardware.pdf`
- `Data Spaces.pdf`

### 🔐 Security mindset (for Story Builder + content rendering)
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

### 🧠 Ethics & human-centered systems
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`

### 🧮 Graphs, optimization, and “future features”
- `Spectral Geometry of Graphs.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`

### 🧵 Concurrency reference shelf
- `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`

### 📚 General programming compendiums (A → X)
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

</details>

---

## 📖 Glossary

| Term | Meaning |
|---|---|
| **Story Node** | A governed narrative artifact (markdown + step config) that ties text/media to map actions. |
| **Step** | A single “scene” in the story (slide/scroll section) that can update map camera/layers/time. |
| **Data contract** | Metadata + schema describing a dataset (source, license, extent, lineage). |
| **Provenance (PROV)** | The “lineage record” explaining how derived artifacts were created from sources. |
| **Focus Mode** | AI assistant mode that answers questions using graph + cataloged evidence (with citations). |
| **Mystery layer** | Any map layer shown without traceable source/contract/provenance (not allowed). |

---

🧭 **If you change StoryPage behavior, also update the Story Node schema + templates** so authors always know what’s supported. ✅
