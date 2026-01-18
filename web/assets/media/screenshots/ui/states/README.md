# 📸 UI State Screenshots (KFM Web)

![asset](https://img.shields.io/badge/asset-screenshots-1f6feb)
![scope](https://img.shields.io/badge/scope-web%2Fui-7e57c2)
![quality](https://img.shields.io/badge/use-docs%20%26%20visual%20QA-2ea043)
![principle](https://img.shields.io/badge/principle-provenance--first-brightgreen)

> **Directory:** `web/assets/media/screenshots/ui/states/`  
> **Purpose:** Store **curated, reviewable screenshots** of key **UI states** in the Kansas Frontier Matrix (KFM) web app — for docs, PR review, and (optional) visual regression baselines.

---

## 🎯 Why this folder exists

KFM is designed around **trustable, inspectable outputs**: provenance-first data, citations, and UI affordances that let users see *where things came from* (layers, notes, AI hints). Screenshots help us:
- ✅ keep UI behavior **auditable** and consistent across releases
- ✅ document **how the UI communicates provenance** (source inspectors, citations, “AI-generated” labels, etc.)
- ✅ support **human-centered UX reviews** (especially for sensitive/regulated map contexts)

KFM emphasizes that **citations + metadata are first-class**, and the UI should let users inspect a layer’s source or an AI note’s reference.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧭 What counts as a “UI state” (vs a “flow”)?

### ✅ UI State (belongs here)
A **single screen** snapshot that captures a *stable* state of the interface:
- map + layer list open
- dataset details drawer expanded
- “provenance panel” open
- Focus Mode reading view (story + map + timeline)
- AI hint panel open (opt-in) and clearly labeled

### 🧵 Flow (does *not* belong here)
A multi-step journey (login → onboarding → upload → publish).  
Flows should live elsewhere (e.g., `ui/flows/` if/when we add it), ideally as a sequence with a small storyboard.

---

## 🗂️ Recommended folder structure

Keep it simple and browsable. Group by **feature area**, then by **breakpoint**.

```text
📁 web/assets/media/screenshots/ui/states/
├── 📄 README.md
├── 📁 map/
│   ├── 📁 desktop/
│   ├── 📁 tablet/
│   └── 📁 mobile/
├── 📁 layers/
├── 📁 search/
├── 📁 dataset/
├── 📁 provenance/
└── 📁 focus-mode/
```

> Tip 💡: Prefer fewer folders with clear names over deep nesting.

---

## 🏷️ Naming convention (deterministic + diff-friendly)

### ✅ File name pattern

Use **kebab-case** and **double-underscore** separators for structured parsing:

```text
<route-or-area>__<state>__<theme>__<viewport>__v<nn>.png
```

**Examples**
- `map__empty-state__light__desktop-1440x900__v01.png`
- `layers__layer-inspector-open__dark__desktop-1440x900__v03.png`
- `focus-mode__story-open__light__mobile-390x844__v02.png`

### Allowed values

- **theme:** `light` | `dark`
- **viewport:**  
  - `desktop-1440x900` (default)  
  - `tablet-1024x768`  
  - `mobile-390x844`

> If you need a new viewport size, add it intentionally and use it consistently (don’t invent one-offs).

---

## 📷 Capture protocol (how we keep screenshots “stable”)

### 1) Use deterministic content 🧪
Screenshots should not rely on live production-like data. Prefer:
- seeded fixtures
- local mock API responses
- stable demo datasets

This aligns with KFM’s **deterministic, evidence-first pipeline** approach (stable outputs for stable inputs).  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 2) Freeze UI volatility 🧊
Before capturing:
- disable animations/transitions (or set them to 0ms)
- hide cursors, toasts, and ephemeral notifications
- ensure consistent time/timezone (avoid “Just now” labels)

### 3) Always show trust affordances 🔎
If the state involves data interpretation, make sure the screenshot demonstrates KFM UX principles:
- provenance/source inspector visible when relevant
- citations visible for narrative/AI-assisted content
- AI-generated outputs clearly labeled and opt-in

KFM’s Focus Mode is intended to display only provenance-linked content, with strict trust guardrails (opt-in AI + clear labeling + no unsourced material).  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔐 Redaction & sensitivity rules (non-negotiable)

Screenshots are **public artifacts** once merged. Treat them like documentation:

- **No secrets**: API keys, tokens, internal endpoints, private repo URLs
- **No PII**: emails, phone numbers, user names, addresses, identifiers
- **No sensitive location leaks**: if the UI is designed to generalize/blur sensitive sites, ensure screenshots reflect that behavior (do not manually “zoom in” to expose restricted detail)

Focus Mode guardrails explicitly include preventing sensitive location leakage (generalize/omit restricted locations).  [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

✅ If you must illustrate a sensitive UI screen:
- use synthetic coordinates
- blur/crop identifying UI parts
- prefer “placeholder cards” over real entities

---

## 🧾 Optional: `manifest.json` (for indexing & automation)

If/when we want to:
- generate screenshot galleries
- power docs pages automatically
- run visual regression in CI

…add a simple manifest.

### Suggested schema (lightweight)

```json
{
  "id": "focus-mode.story-open.desktop.light.v02",
  "file": "focus-mode/desktop/focus-mode__story-open__light__desktop-1440x900__v02.png",
  "feature": "focus-mode",
  "route": "/focus/:storyId",
  "state": "story-open",
  "theme": "light",
  "viewport": "desktop-1440x900",
  "tags": ["provenance", "citations", "story-node"],
  "notes": "Citations panel visible; AI hint closed (default)."
}
```

> Contract-first mindset: if we adopt a manifest, define a JSON Schema under `schemas/ui/` and validate it in CI.  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔗 Using screenshots in docs (examples)

### In a Markdown doc (recommended)
```md
![Layer inspector with provenance visible](/web/assets/media/screenshots/ui/states/layers/desktop/layers__layer-inspector-open__light__desktop-1440x900__v03.png)
```

### In Story Node / Focus Mode docs
Use screenshots sparingly; prioritize **evidence artifacts** and provenance-linked visuals when possible.  [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ✅ PR checklist (Definition of Done for screenshots)

- [ ] File placed in the correct feature folder (`map/`, `focus-mode/`, etc.)
- [ ] Filename matches the naming convention (state + theme + viewport + version)
- [ ] Screenshot is deterministic (no live/volatile data, no “Just now” timestamps)
- [ ] No secrets / PII / sensitive location leakage
- [ ] If AI content is shown: it is **opt-in** and clearly labeled
- [ ] Image is optimized (don’t commit 8–20MB PNGs if avoidable)

---

## 📚 References

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- KFM Master Guide v13 (pipeline → UI → Focus Mode; governance + evidence-first + determinism)  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
