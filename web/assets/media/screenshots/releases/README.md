# 📸 Release Screenshots (Web UI)

![Path](https://img.shields.io/badge/path-web%2Fassets%2Fmedia%2Fscreenshots%2Freleases-2ea44f)
![Use](https://img.shields.io/badge/use-GitHub%20Releases%20%7C%20CHANGELOG%20%7C%20Docs-blue)
![Policy](https://img.shields.io/badge/policy-provenance--first%20%26%20public--safe-important)

This folder contains **release-ready screenshots** for the **Kansas Frontier Matrix (KFM)** web application (React + MapLibre/Cesium UI). These images are intended to be stable, shareable, and safe to publish.

> 🧭 KFM is *evidence-first* and *provenance-first*. If a screenshot depicts data, it should make **source/metadata/citations** obvious (or be captioned so the reader can find the evidence fast). ✅

---

## ✅ What belongs here

- 📦 **Curated screenshots** used in:
  - GitHub Releases notes
  - `CHANGELOG.md`
  - Docs / feature walkthroughs
  - Social previews / project updates
- 🧪 **Deterministic(ish) UI captures** that represent a feature at release time
- 🧾 Screens that clearly show **provenance-linked** UX (layer metadata, citations, evidence panels) when relevant

---

## 🚫 What does NOT belong here

- 🧻 One-off “WIP” screenshots for PR comments (attach directly to the PR/Issue instead)
- 🔐 Anything that includes secrets, tokens, API keys, private URLs, admin panels, or internal-only dashboards
- 🧑‍🤝‍🧑 Any personal data (PII), private accounts, real emails, real names, real addresses
- 🪶 Sensitive locations/data that violate sovereignty/classification rules (see **🛡️ Governance** below)

---

## 🗂️ Folder structure

Use a **folder per release tag** (recommended), plus optional shared assets.

```text
web/
└─ 📁 assets/
   └─ 🎞️ media/
      └─ 📸 screenshots/
         └─ 🗞️ releases/
            ├─ 📄 README.md                    # 📘 How to curate release screenshots + naming/order + redaction rules
            ├─ 🏷️ vX.Y.Z/                      # One folder per release version (ordered, publish-ready)
            │  ├─ 🌟🖼️ 00-hero.png              # Hero image for release notes/social/blog
            │  ├─ 🗺️🖼️ 01-map-overview.png       # High-level map overview (layers/timeline visible)
            │  ├─ 🧾🗂️🖼️ 02-layer-metadata.png    # Layer metadata/provenance panel capture
            │  ├─ 🎬🖼️ 03-story-mode-step-02.png  # Story Mode step example (numbered for sequence)
            │  ├─ 🔎📚🖼️ 04-focus-mode-with-citations.png # Focus Mode with citations/evidence shown
            │  └─ 🧾📄 manifest.yml              # (optional, 🔥 recommended) captions, alt text, links, approvals
            └─ ♻️ _shared/                      # (optional) Shared assets used across releases (frames, logos)
               ├─ 🏷️🖼️ kfm-logo.png             # Logo used in framed/templated release images
               └─ 🖼️🧩 release-frame.svg         # Reusable frame/border overlay for consistent styling
```

**Why per-release folders?**  
Because release notes should be **immutable**: a screenshot referenced in `v1.2.0` notes should not silently change later.

---

## 🏷️ Naming convention

### Rules (please follow)
- ✅ **lowercase + kebab-case**
- ✅ prefer **PNG** for UI
- ✅ prefix with a **2-digit order** (`00-`, `01-`, …) when a set is meant to be read in sequence
- ✅ include **mode/context** in the name when useful (`2d`, `3d`, `story`, `focus-mode`)
- ❌ no spaces, no “final_FINAL_2.png”, no random hashes

### Suggested pattern
`NN-<area>-<feature>-<state>.png`

Examples:
- `00-hero.png`
- `01-map-overview-2d.png`
- `02-layer-panel-metadata-open.png`
- `03-story-mode-dust-bowl-step-02.png`
- `04-focus-mode-answer-with-citations.png`
- `05-cesium-3d-terrain-toggle.png`

---

## 🧩 Recommended screenshot set per release

> Not every release needs every shot. But if we ship UI changes, try to include at least **one “hero” + one “proof”** screenshot.

### Minimum (strongly recommended)
- [ ] **Hero**: the app “in context” (map + key UI panels)
- [ ] **Feature proof**: the *new* UI/feature visible and understandable
- [ ] **Provenance proof** (if the feature touches data): metadata/citations panel shown or clearly accessible

### If the release touched these areas…
- 🗺️ Map/Layers:
  - [ ] layer toggles + legend/opacity
  - [ ] layer details / metadata view
- 🧭 Story Mode (narratives):
  - [ ] narrative panel visible + map synchronized to a step
- 🤖 Focus Mode (AI assistant):
  - [ ] question + answer + **references/citations visible**
  - [ ] any AI content clearly indicated as AI-generated (no “mystery authority”)

<details>
<summary>📚 Why we push “provenance visible” screenshots</summary>

KFM’s UI and narratives are designed to be *provenance-linked* and *evidence-first* (STAC/DCAT/PROV before story interpretation). In Focus Mode, AI output must remain **advisory** and be constrained by evidence with visible sources.

Release screenshots are a lightweight public artifact proving those standards are actually visible to users. ✅

</details>

---

## 🧪 Capture workflow

### 1) Prep the UI (make the screenshot reproducible)
- ✅ Use a **public/demo-safe dataset** (no restricted layers, no private endpoints)
- ✅ Set a **stable map view** (center/zoom) and avoid transient UI state (toasts, loaders, “new version available”)
- ✅ Prefer **light theme** unless the release is explicitly about dark mode
- ✅ If you’re capturing Story Mode: pick a step that clearly shows the story + map sync
- ✅ If you’re capturing Focus Mode: ensure the **citations/references** are visible in-frame

### 2) Standardize capture settings
- 🖥️ Viewport recommendation: **1440×900** (or 1920×1080 if needed)
- 🔎 Browser zoom: **100%**
- 🧼 Hide bookmarks bar / extensions / devtools
- 🧯 Avoid capturing cursor unless it’s showing a key interaction (hover tooltip, etc.)

### 3) Take the screenshot
- Prefer OS-level “capture window” or browser screenshot tools
- If the UI includes “sensitive-location blurring/generalization”, **verify it is active** before capture

### 4) Post-process (fast + consistent)
- ✂️ Crop only if it increases clarity (don’t over-crop context out of the UI)
- 🧊 Keep text readable (don’t resize down to mush)
- 🗜️ Compress images so the repo stays lean

---

## 🛡️ Governance, licensing & redaction (non-negotiable)

### 🚨 Privacy / security checklist
- [ ] No API keys, auth headers, cookies, tokens, session IDs
- [ ] No real user names/emails
- [ ] No internal-only endpoints or private URLs
- [ ] No “admin” screens unless explicitly intended and safe for public release notes

### 🪶 Data sovereignty / classification
If a source dataset is sensitive/restricted, **screenshots are also restricted** unless properly redacted/approved.

- ✅ Use the UI’s safeguards (blur/generalize sensitive locations)
- ✅ Prefer aggregated/public-safe views for demos
- ❌ Never publish restricted Indigenous data or culturally sensitive locations in a release screenshot

### 🧾 Licensing (don’t accidentally redistribute what we can’t)
If the screenshot includes:
- third-party imagery,
- licensed basemaps,
- restricted photos,
- or externally sourced scans,

…ensure redistribution is permitted **and** attribution is present or documented in the release notes.

---

## ⚡ File size & performance budget

Targets (guideline):
- ✅ Typical UI screenshot: **≤ 500 KB**
- ✅ Hero screenshot: **≤ 1.5 MB**
- ❌ Avoid multi-megabyte PNGs unless absolutely necessary

Optional tools (pick what you like):
```bash
# lossless PNG optimization (example)
oxipng -o 4 -i 0 --strip all web/assets/media/screenshots/releases/vX.Y.Z/*.png

# lossy PNG quantization (example)
pngquant --quality=70-90 --strip --skip-if-larger --output out.png in.png
```

---

## 🔗 How to reference these screenshots (release notes / docs)

From repo root (recommended for release notes):
```md
![KFM vX.Y.Z — Focus Mode with citations](web/assets/media/screenshots/releases/vX.Y.Z/04-focus-mode-answer-with-citations.png)
```

From within the release folder itself:
```md
![Map overview](./vX.Y.Z/01-map-overview-2d.png)
```

---

## 🤖 Optional: automate capture (highly recommended)

KFM’s testing approach includes E2E browser testing (commonly Cypress/Playwright style). You can reuse that pattern to produce **stable screenshots**:

- ✅ Add an E2E test that navigates to a known route/state
- ✅ Set viewport and deterministic data fixtures
- ✅ `screenshot()` at known UI states
- ✅ Copy “golden” screenshots into `web/assets/media/screenshots/releases/vX.Y.Z/`

<details>
<summary>🧾 Optional <code>manifest.yml</code> (metadata for a release screenshot set)</summary>

Adding a manifest makes screenshots easier to reuse in tooling, docs generators, and release builders.

**Example** (`web/assets/media/screenshots/releases/vX.Y.Z/manifest.yml`):
```yml
release: "vX.Y.Z"
captured_at: "YYYY-MM-DD"
commit: "abcdef1234567890"
viewport: "1440x900"
browser: "chromium"
notes: "Public-safe demo dataset; light theme; citations visible"
images:
  - id: "hero"
    file: "00-hero.png"
    alt: "KFM map UI with layer panel and timeline"
    route: "/"
  - id: "focus-mode"
    file: "04-focus-mode-answer-with-citations.png"
    alt: "Focus Mode answer with references visible"
    route: "/map?...&focusMode=true"
classification: "public"
```

</details>

---

## 🧹 Maintenance & archival

- ✅ Keep screenshots **forever per release** (they document history)
- ✅ If you must replace an image, do it in a **new release folder** (don’t mutate old releases)
- ✅ If storage becomes an issue, prefer:
  - stronger compression, or
  - Git LFS for heavy media (only if the repo policy allows it)

---

## ✅ Definition of Done (DoD) for adding release screenshots

- [ ] Stored under the correct `vX.Y.Z/` folder
- [ ] Filenames follow conventions (ordered, readable)
- [ ] Public-safe: no secrets, PII, or restricted data
- [ ] If AI/Focus Mode is shown: citations/references are visible
- [ ] Image is optimized (size budget met)
- [ ] Referenced correctly in the release notes / docs

---

<!--
Sources used to author & align this README with KFM standards (internal references):
 [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:4‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
-->
