# 🧭 UI Flow Screenshots (KFM Web)

![Asset: Screenshots](https://img.shields.io/badge/asset-screenshots-blue?style=flat)
![Scope: UI flows](https://img.shields.io/badge/scope-ui%20flows-orange?style=flat)
![Principle: Provenance-first](https://img.shields.io/badge/principle-provenance--first-success?style=flat)

> “Citations and metadata are first-class data; nothing is a black box.” 🧾✨

This directory holds **canonical screenshots** for **end-to-end UI flows** in the KFM web app (Map + Timeline, Story Mode, Focus Mode, etc.).  
They’re used for docs, Story Nodes, QA, onboarding, and PR reviews.

---

## 📌 What belongs here

| ✅ In scope | 🚫 Out of scope |
|---|---|
| Multi-step journeys (5–15 steps) | Icons / logos / UI sprites |
| Story Mode walkthroughs | One-off “pretty” marketing shots |
| Focus Mode (AI) interactions (opt-in) | Component-only captures (use a `ui/components/` screenshots folder if present) |
| Critical error/empty/loading flows | Screenshots containing secrets/PII |

---

## ✅ Folder contract (non-negotiables)

1. **One folder = one flow** 🧩  
2. Every flow includes a **`flow.yml` manifest** 🧾 (context + steps)  
3. Screenshot filenames are **step-numbered** and **stable** 🔒 (avoid renames)  
4. Anything showing data/AI should show **provenance affordances** (sources, citations, metadata) 🔎  
5. **No secrets. No PII. No sensitive location leaks.** 🛡️

---

## 📂 Recommended structure

```text
web/
└── 📁 assets/
    └── 📁 media/
        └── 📁 screenshots/
            └── 📁 ui/
                └── 📁 flows/
                    ├── 📄 README.md                      # 👈 you are here
                    ├── 📁 _templates/                    # (optional) starter files
                    │   ├── 📄 flow.template.yml
                    │   └── 📄 screenshot.template.yml
                    └── 📁 <area>--<flow>/                # one folder per flow
                        ├── 📄 flow.yml                   # required ✅
                        ├── 📄 README.md                  # optional (notes, gotchas)
                        ├── 🖼️ 00__<step>.png
                        ├── 🖼️ 01__<step>.png
                        └── 🖼️ ...
```

---

## 🏷️ Naming conventions

### Flow folder names

Format: `<area>--<verb-noun>` (kebab-case)

Examples:
- `focus-mode--ask-question`
- `story-mode--play-story`
- `map--add-layer`
- `timeline--scrub-time`
- `layers--inspect-provenance`

### Screenshot file names

Format: `NN__<screen-or-action>--<short-desc>.<png|webp>`

Examples:
- `00__map--default-view.png`
- `01__layers-panel--open.png`
- `02__layer--inspect-source.png`
- `03__focus-mode--answer-with-citations.png`

Rules:
- `NN` is **zero padded** (`00`, `01`, `02`, …) so it sorts correctly
- Prefer **PNG** for crisp UI text (WebP is fine if lossless / visually identical)
- Avoid spaces; use `-` inside slugs

---

## 📸 Capture standards

### 🖥️ Viewport + scale

Pick **one baseline per flow** and record it in `flow.yml`.

Suggested defaults:
- **Desktop:** 1440×900 @2×
- **Mobile:** 390×844 @3×

If a flow must show responsiveness, use the **Variants** pattern below.

### 🌗 Theme, locale, and browser

- Theme: `light` or `dark` (record it)
- Locale: `en-US` (record any deviations)
- Browser: record name + version (screenshots should be reproducible)

### 🧪 Data fixtures only

Use demo/fixture data so screenshots are:
- reproducible ✅
- safe to publish ✅
- stable across time ✅

### 🔐 Safety + governance

Before committing:
- ✅ hide keys/tokens/usernames/emails
- ✅ confirm any “restricted” or sovereignty-protected locations remain **redacted/generalized** in the UI
- ✅ prefer “public” layers unless the flow explicitly tests role-based access

### 🧾 Provenance-first visuals

If a screenshot contains:
- a dataset/layer claim, or
- an AI-generated response, or
- a narrative statement tied to evidence

…then the screenshot should show how a user can inspect **sources/citations/metadata** (e.g., provenance panel open, citations visible, “AI-generated” label visible).

---

## 🧾 `flow.yml` manifest

Every flow folder must include `flow.yml`. Treat it like a **mini data contract** for screenshots.

<details>
<summary>🗂️ Suggested <code>flow.yml</code> template (click to expand)</summary>

```yml
id: ui.flow.<area>.<slug>              # stable ID (do not change once used in docs)
title: "Focus Mode — Ask a question"
area: focus-mode                       # map | timeline | story-mode | focus-mode | settings | ...
status: draft                           # draft | verified | deprecated

owners:
  - "@handle"                           # optional
last_verified:
  date: "YYYY-MM-DD"
  by: "@handle"

environment:
  app_version: "vX.Y.Z"                 # or commit SHA / build number
  commit: "<git_sha>"
  build: "dev|staging|prod"
  browser: "Chrome <version>"
  os: "macOS|Windows|Linux"
  locale: "en-US"
  theme: "light"

viewport:
  kind: "desktop"
  width: 1440
  height: 900
  device_scale_factor: 2

preconditions:
  - "User is on /map with demo dataset loaded"
  - "Timeline set to 1935"

data_fixtures:
  datasets:
    - "<catalog_id_or_slug>"            # prefer stable IDs from catalogs/graph
  story_nodes:
    - "docs/reports/story_nodes/published/<story_slug>/story.md"

steps:
  - n: 0
    file: "00__open-focus-mode.png"
    title: "Open Focus Mode"
    route: "/map"
    action: "Click the AI Assistant button"
    expected: "Focus Mode panel opens"
    map:
      camera: { lon: -98.0, lat: 38.5, zoom: 5 }
      timeline: "1935"
      layers: ["<layer_id>"]
    ai:
      visible: false

  - n: 1
    file: "01__ask-question.png"
    title: "Ask a question"
    action: "Enter prompt and submit"
    expected: "System begins answering (loading state)"

  - n: 2
    file: "02__answer-with-citations.png"
    title: "AI answer w/ citations"
    expected: "Answer is labeled AI-generated and includes citations (+ confidence if available)"
    ai:
      visible: true
      label_visible: true
      citations_visible: true
      confidence_visible: true

sensitivity:
  classification: "public"              # public | internal | restricted
  notes: "No real user data; demo-only"
```

</details>

---

## 🧩 Variants (responsive / theme / language)

If one flow needs multiple variants, create subfolders:

```text
<flow>/
├── desktop-light/
├── desktop-dark/
└── mobile-light/
```

Options:
- each variant has its own `flow.yml`, **or**
- one `flow.yml` in the parent and `variants:` in YAML

Pick one approach and stay consistent within the flow folder.

---

## 🧷 Embedding screenshots in docs

Use **relative paths** and **alt text**:

```md
![Layer provenance panel open](./layers--inspect-provenance/02__layer--inspect-source.png)
```

Optional caption convention:

*Figure: Inspecting a layer’s source & processing steps (demo data).*

---

## 🔄 Updating / deprecating flows

When UI changes:
1. Update screenshots 🖼️
2. Update `flow.yml` (`commit`, `app_version`, `last_verified`) 🧾

If a flow is removed:
- set `status: deprecated`
- keep the folder for historical context unless repo size becomes a concern

---

## ✅ PR checklist

- [ ] Folder name follows `<area>--<verb-noun>`
- [ ] All screenshots are step-numbered (`00__`, `01__`, …)
- [ ] `flow.yml` present and updated
- [ ] No secrets / PII / restricted coordinates
- [ ] AI flows show **AI-generated label** + **citations** (and confidence if available)
- [ ] Images are reasonably sized + optimized (no accidental 20MB screenshots 😅)
- [ ] Any docs referencing screenshots use relative links + meaningful alt text

---

## 🗺️ Flow catalog (fill in as you add flows)

| Flow folder | Area | Status | Last verified | Notes |
|---|---|---:|---:|---|
| `focus-mode--ask-question/` | Focus Mode | draft | — | Needs demo dataset IDs |
| `story-mode--play-story/` | Story Mode | draft | — | Capture 3–5 story steps |
| `layers--inspect-provenance/` | Map | draft | — | Show source + processing steps |

---

## 🔗 Related docs (repo root)

- `docs/MASTER_GUIDE_v13.md` 📘
- `docs/standards/` 🧾 (STAC/DCAT/PROV, governance, review gates)
- `docs/reports/story_nodes/` 📚 (narratives + assets)

---

[⬆️ Back to top](#-ui-flow-screenshots-kfm-web)
