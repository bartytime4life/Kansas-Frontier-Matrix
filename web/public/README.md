<!-- Path: web/public/README.md -->

# 🌾🗺️ `web/public/` — Static (Public) Assets for KFM

![Static Assets](https://img.shields.io/badge/web%2Fpublic-static%20assets-0ea5e9?style=flat-square)
![Provenance](https://img.shields.io/badge/provenance-evidence--first-22c55e?style=flat-square)
![Security](https://img.shields.io/badge/security-no%20secrets%20in%20public-ef4444?style=flat-square)
![Docs](https://img.shields.io/badge/docs-Story%20Nodes%20%2B%20Metadata-8b5cf6?style=flat-square)

> ⚠️ **If it’s in `web/public/`, it’s shipped to the browser.** Treat this folder like a **public billboard**: no secrets, no private data, no “we’ll clean it later.” 🧼

---

## 🧭 What this folder is

`web/public/` holds **static files served as-is** by the web host (dev server / CDN / static server).  
These assets are available via URL paths like:

- `/favicon.ico`
- `/assets/branding/logo.svg`
- `/stories/<slug>/media/cover.webp`
- `/map/styles/base.json`

This aligns with the KFM UI model where the **frontend is modular** (map viewer, timeline, story panel, etc.) and pulls data through governed boundaries rather than “random file reads.” ✅

---

## ✅ What belongs here (do ✅)

- 🪪 **Branding**: logos, wordmarks, favicons, app icons
- 🧩 **UI-static assets**: SVG icons, background images, small static JSON config
- 🗺️ **Map viewer static resources**:
  - style JSON (MapLibre)
  - sprites / glyphs (if self-hosted)
  - small demo overlays (GeoJSON for examples)
- 📖 **Story media** that should load directly in the browser (covers, audio clips, images)
- 📦 **Offline pack manifests** (and optionally pack zips if managed carefully)

---

## 🚫 What does NOT belong here (avoid ❌)

- 🔐 **Secrets**: API keys, tokens, `.env`, service credentials
- 🧍‍♂️ **PII / restricted content**: names + addresses, private records, culturally sensitive coordinates
- 🧱 **Large datasets** (raw/processed): those belong in `data/` + catalogs (STAC/DCAT/PROV) + served via API
- 🧪 **Test fixtures** that don’t need browser fetch (prefer `web/src/__fixtures__/`)

> 🔎 Reminder: even “processed outputs” can leak sensitive information. Don’t publish data mining outputs or derived datasets here unless you’ve reviewed privacy risk (query inference, re-identification, etc.).  

---

## 🗂️ Repo context (why `public/` is stricter than it looks)

KFM’s repo layout expects:
- `web/` = frontend application
- `docs/` = canonical governed docs
- `docs/reports/story_nodes/` = story narrative content (draft vs published)
- `data/` = domain data + catalogs (STAC/DCAT/PROV)
- `schemas/` = JSON Schemas (including story nodes / UI telemetry, etc.)

So: **`web/public` is not a “data folder.”** It’s a **delivery folder** for the browser.

---

## 📁 Suggested folder layout (convention)

> You can deviate, but **keep it predictable** and consistent.

```text
web/public/
├── 🧾 README.md
├── 🤖 robots.txt
├── 🧩 manifest.webmanifest
├── 🪪 favicon.ico
├── 🖼️ assets/
│   ├── 🎨 branding/
│   │   ├── logo.svg
│   │   ├── wordmark.svg
│   │   └── source.json
│   ├── 🧷 icons/
│   │   ├── pin.svg
│   │   ├── layers.svg
│   │   └── source.json
│   └── 🖼️ images/
│       ├── hero.webp
│       ├── hero.source.json
│       └── hero.license.md
├── 📖 stories/
│   ├── published/
│   │   └── <story-slug>/
│   │       ├── story.md
│   │       ├── story.json
│   │       └── media/
│   │           ├── cover.webp
│   │           ├── cover.source.json
│   │           └── transcript.md
│   └── index.json
├── 🗺️ map/
│   ├── styles/
│   │   └── base.json
│   ├── sprites/
│   │   ├── kfm@2x.png
│   │   └── kfm.json
│   └── glyphs/
│       └── <fontstack>/{range}.pbf
└── 📦 offline/
    ├── packs/
    │   └── <pack-id>/
    │       ├── pack.json
    │       └── pack.zip (optional)
    └── index.json
```

---

## 🔗 How to reference assets in the UI

### From React / TypeScript
Use **absolute paths** (browser-root), so the app works in dev and production:

```ts
const logoUrl = "/assets/branding/logo.svg";
const coverUrl = `/stories/published/${slug}/media/cover.webp`;
```

### From Story Node Markdown
Prefer absolute paths so story rendering is stable across routes:

```md
![Cover](/stories/published/dust-bowl-1930s/media/cover.webp)
```

---

## 🧾 Provenance + licensing are required (no exceptions)

KFM’s documentation and data approach is **evidence-first / provenance-first**.  
Static assets shipped to the browser should follow the same standard:

### ✅ Required: sidecar metadata for any non-trivial asset
- `*.source.json` (preferred) **or** `source.json` in the same folder
- `*.license.md` or `LICENSE.md` if attribution requires text
- Optional: `*.prov.json` if the asset is derived (edited, cropped, translated, aggregated)

### 📄 `*.source.json` template

```json
{
  "title": "KFM Hero Image — Kansas Tallgrass Prairie",
  "type": "image",
  "origin": {
    "source_url": "https://example.org/original",
    "retrieved_at": "2026-01-26",
    "publisher": "Example Archive",
    "author": "Jane Doe"
  },
  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Photo © Jane Doe, CC BY 4.0",
    "notes": "Do not remove watermark."
  },
  "integrity": {
    "sha256": "<fill-me-in>",
    "original_filename": "prairie.jpg"
  },
  "kfm": {
    "sensitivity": "public",
    "notes": "Optimized to WEBP; see prov for transformation."
  }
}
```

### 🧬 `*.prov.json` (optional, for derived assets)

```json
{
  "wasDerivedFrom": "prairie.jpg",
  "activity": "convert+resize",
  "tools": ["imagemagick", "cwebp"],
  "parameters": {
    "resize": "1920x1080",
    "format": "webp",
    "quality": 80
  },
  "performedBy": "kfm-dev",
  "performedAt": "2026-01-26"
}
```

---

## 📖 Story Nodes + media in `public/`

KFM Story Nodes are designed as **governed narrative content** (Markdown + JSON) with a clear draft/published workflow, and they’re meant to be reviewable and version-controlled. ✅

### Recommended practice
- **Source-of-truth** stays in: `docs/reports/story_nodes/`
  - `draft/` (work-in-progress)
  - `published/` (reviewed + approved)
- `web/public/stories/published/` can hold:
  - 📦 exported story bundles for static hosting
  - 📡 offline packs
  - 🧪 demo story content for development

### Suggested build step (conceptual)
- Copy `docs/reports/story_nodes/published/**` → `web/public/stories/published/**`
- Generate `web/public/stories/index.json` (registry for the UI)

---

## 🗺️ Map assets, PMTiles, and offline packs

KFM’s UI stack includes modern WebGL mapping (2D + 3D), and the architecture supports **offline / low-connectivity** usage via “offline packs” (mini web app + subset of tiles + stories). 📦🗺️

### 🧱 MapLibre assets
If you self-host:
- `public/map/styles/*.json`
- `public/map/sprites/*`
- `public/map/glyphs/*`

### 🧊 PMTiles (optional)
If you ship **small** PMTiles for demo/offline:
- store PMTiles outside git when large (release artifacts / LFS / separate storage)
- keep **manifests** and indices in `public/` so the UI can discover them

### 📦 Offline pack conventions
Each pack should have a `pack.json` manifest that lists what the UI needs:

```json
{
  "id": "kansas-classroom-pack-01",
  "title": "Kansas Classroom Pack (Intro)",
  "version": "1.0.0",
  "includes": {
    "stories": ["/stories/published/dust-bowl-1930s/story.json"],
    "media_prefixes": ["/stories/published/dust-bowl-1930s/media/"],
    "maps": [
      {
        "type": "pmtiles",
        "url": "/offline/packs/kansas-classroom-pack-01/tiles.pmtiles",
        "style": "/map/styles/base.json"
      }
    ]
  }
}
```

---

## ♿ Accessibility + performance (browser-first)

### ♿ Accessibility
- Always provide meaningful `alt` text for images used in docs/story markdown
- Prefer **SVG** for icons (scales cleanly)
- Captions/transcripts for audio/video when feasible

### ⚡ Performance
- Prefer `webp`/`avif` for photos, `svg` for icons, `mp4` for video
- Keep filenames **kebab-case**: `dust-bowl-cover.webp`
- Avoid huge binaries; prefer external hosting + governed API for big content

---

## 🔐 Security + privacy checklist (public means public)

Before merging anything into `web/public/`:

- [ ] No secrets/tokens/credentials anywhere in the file or metadata
- [ ] License + attribution is documented (`*.source.json`)
- [ ] No sensitive locations (especially culturally protected sites) at high precision
- [ ] No PII or quasi-identifiers that enable re-identification
- [ ] If content is derived from restricted data, **don’t ship it here**—serve through governed APIs with policy checks

> 🛡️ KFM’s governance model includes input/output filtering and policy enforcement (e.g., OPA checks) for AI responses; `web/public` should follow the **same “least privilege / least exposure” mindset**.

---

## 🧰 “Add an asset” workflow (repeatable)

1) 📁 Put the asset in the right subfolder (`assets/`, `stories/`, `map/`, etc.)  
2) 🧾 Add `*.source.json` (and license text if required)  
3) 🧪 Validate in dev:
   - The URL resolves
   - The UI renders correctly
   - No console errors (CORS, missing files, bad JSON)  
4) 🧹 Optimize (size/format)  
5) ✅ PR checklist:
   - [ ] sidecar metadata present
   - [ ] filenames are kebab-case
   - [ ] story links are stable
   - [ ] no sensitive content

---

## 📚 References (project files)

> Keeping these close helps contributors understand *why* the conventions exist. 📌

<details>
<summary>🌾 Core KFM architecture & UI docs</summary>

- 📄 Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap.pdf  
- 📄 Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide).pdf  
- 📄 Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf  
- 📄 Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf  
- 📄 📚 Kansas Frontier Matrix (KFM) – Expanded Technical & Design Guide.pdf  
- 📄 Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf  
- 📄 KFM AI Infrastructure – Ollama Integration Overview.pdf  

</details>

<details>
<summary>🧠 Background library (AI / data / geo / web / security)</summary>

- 📦 AI Concepts & more.pdf *(PDF portfolio / multi-book bundle)*  
- 📦 Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf *(PDF portfolio)*  
- 📦 Mapping-Modeling-Python-Git-HTTP-CSS-Docker-GraphQL-Data Compression-Linux-Security.pdf *(PDF portfolio)*  
- 📦 Geographic Information-Security-Git-R coding-SciPy-MATLAB-ArcGIS-Apache Spark-Type Script-Web Applications.pdf *(PDF portfolio)*  
- 📦 Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf *(PDF portfolio)*  
- 📦 Various programming langurages & resources 1.pdf *(PDF portfolio)*  

</details>

<details>
<summary>📝 Documentation standards (Markdown + evidence-first)</summary>

- 📄 Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx  
- 📄 MARKDOWN_GUIDE_v13.md (repo layout + governed docs conventions)

</details>

---

### 🔝 Back to top
[⬆️ Back to `web/public/`](#-webpublic--static-public-assets-for-kfm)

<!--
Internal grounding notes (for maintainers):
- Repo layout expectations & story node path: docs/reports/story_nodes/ (draft vs published)
- UI modular design + governed API boundary
- Story nodes are Markdown + JSON
- Offline packs concept
- Policy mindset (input filtering / output checks / OPA) inspiring least-exposure rules
-->