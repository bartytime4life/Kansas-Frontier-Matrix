# 📸 UI View Screenshot Library — `web/assets/media/screenshots/ui/views/`

![Screenshots](https://img.shields.io/badge/type-screenshots-%F0%9F%93%B8-informational)
![Scope](https://img.shields.io/badge/scope-web%2Fviews-%F0%9F%96%A5%EF%B8%8F-blue)
![Provenance-first](https://img.shields.io/badge/principle-provenance--first-%E2%9C%85-success)
![Docs](https://img.shields.io/badge/used_in-docs%20%7C%20PRs%20%7C%20release%20notes-%F0%9F%93%9A-purple)

> 🧭 **Purpose:** Keep a clean, “golden set” of **canonical screenshots** for **top-level UI views/pages** (e.g., Map, Data Catalog, Story mode, Focus Mode) so the team can quickly:
> - document UX 📚
> - review UI regressions 🧪
> - build consistent guides & demos 🎥
> - keep “what the UI looks like” **discoverable** and **traceable** 🧾

---

## 🗺️ What counts as a “View” screenshot?

A **view** screenshot represents a **page-level surface** (not a tiny component).  
Think: `MapPage`, `DataCatalogPage`, `StoryPage`, “Focus Mode panel open”, etc.

✅ **Belongs here**
- Full view/page screenshots (with key panels, toolbars, timeline controls, etc.)
- Important “page states” (layer panel open, feature selected, story step active, AI answer visible)

🚫 **Does NOT belong here**
- Component-only captures (put those under `.../screenshots/ui/components/` if/when it exists)
- Story-specific images that are *part of the narrative content* (keep those with the Story Node assets)
- Sensitive/regulated visuals (PII, secrets, private URLs, internal-only data)

---

## 🧱 Folder layout

Keep the structure **mirroring the app’s top-level views** so people can find things fast.

```text
📁 web/assets/media/screenshots/ui/views/
├─ 📄 README.md ✅ (you are here)
├─ 📁 map-page/
│  ├─ 🖼️ map-page--default--desktop--light.png
│  ├─ 🖼️ map-page--layer-panel-open--desktop--light.png
│  ├─ 🖼️ map-page--feature-selected--desktop--light.png
│  └─ 🧾 map-page--feature-selected--desktop--light.meta.json (optional)
├─ 📁 data-catalog-page/
│  ├─ 🖼️ data-catalog-page--grid--desktop--light.png
│  ├─ 🖼️ data-catalog-page--filters-open--desktop--light.png
│  └─ 🖼️ data-catalog-page--dataset-details--desktop--light.png
├─ 📁 story-page/
│  ├─ 🖼️ story-page--story-list--desktop--light.png
│  ├─ 🖼️ story-page--step-01--desktop--light.png
│  └─ 🖼️ story-page--citations-open--desktop--light.png
└─ 📁 focus-mode/
   ├─ 🖼️ focus-mode--panel-open--desktop--light.png
   ├─ 🖼️ focus-mode--answer-with-citations--desktop--light.png
   └─ 🧾 focus-mode--answer-with-citations--desktop--light.meta.json (optional)
```

> 🔁 **Rule:** If you add a new top-level UI route/view, create a new folder here and add it to the **Screenshot Matrix** below.

---

## 🏷️ Naming convention

### ✅ Recommended filename pattern

```text
{view}--{state}--{breakpoint}--{theme}.png
```

**Examples**
- `map-page--default--desktop--light.png`
- `map-page--timeline-active--desktop--light.png`
- `story-page--step-03--desktop--light.png`
- `focus-mode--answer-with-citations--desktop--light.png`

### Conventions (so files sort nicely)
- Use **kebab-case** everywhere
- Use `step-01`, `step-02`, … (leading zero) for Story steps
- Prefer “what the user sees” in `{state}`:
  - ✅ `layer-panel-open`
  - ✅ `feature-selected`
  - ✅ `citations-open`
  - ❌ `state-2`
  - ❌ `final`

---

## 📐 Capture standards (consistency = speed)

### Breakpoints
Pick one “canonical” set and keep it consistent:

- **desktop**: 1440×900 (recommended)
- **tablet**: 1024×768 (optional, only if UI differs meaningfully)
- **mobile**: 390×844 (optional, only if UI differs meaningfully)

### Theme
- Default: **light**
- If the project supports dark mode and it meaningfully changes UX, add **dark** versions.

### Browser + zoom
- Use a modern Chromium browser
- **100% zoom**
- Hide devtools
- Avoid OS notification popups

---

## 🧾 Provenance & safety rules (screenshots are “published artifacts”)

### ✅ Must do
- Use **stable demo/test datasets** whenever possible
- Ensure any shown data is **licensed/allowed** and properly attributable
- If a view includes provenance/citations UI (layer info, source popover, AI citations), capture **at least one** screenshot where that provenance UI is visible

### 🚫 Must not do
- No API keys, tokens, passwords, emails, private URLs
- No personal data (unless explicitly approved and redacted)
- No sensitive locations if the UX is meant to protect them (generalize/blur)

> 🧼 If you must capture a sensitive-like interface state (e.g., an error with a URL), **sanitize** it first.

---

## ✅ Screenshot Matrix (minimum “golden set”)

This is the **baseline** set we keep current. Add more screenshots when a PR changes UX.

| View folder | Minimum states (required) | Nice-to-have states |
|---|---|---|
| `map-page/` | `default`, `layer-panel-open`, `feature-selected`, `timeline-active` | `3d-on`, `legend-open`, `search-open` |
| `data-catalog-page/` | `grid`, `filters-open`, `dataset-details` | `empty-state`, `sort-changed` |
| `story-page/` | `story-list`, `step-01`, `citations-open` | `step-0X` for each major beat, `exit-to-map` |
| `focus-mode/` | `panel-open`, `answer-with-citations` | `source-preview-open`, `no-answer-in-data` |

> 🧠 **Focus Mode note:** always prefer screenshots that show **citations/sources** (that’s the trust contract).

---

## 🧾 Optional: Sidecar metadata (`.meta.json`)

If a screenshot would be hard to reproduce later, add a sidecar metadata file:

**Same basename**, `.meta.json` extension  
Example:
- `map-page--feature-selected--desktop--light.png`
- `map-page--feature-selected--desktop--light.meta.json`

Template:

```json
{
  "view": "map-page",
  "state": "feature-selected",
  "breakpoint": "desktop",
  "theme": "light",
  "route": "/<route-here>",
  "viewport": { "width": 1440, "height": 900 },
  "data_context": {
    "dataset_ids": ["<dataset-id-1>", "<dataset-id-2>"],
    "time_range": { "start": "<YYYY-MM-DD>", "end": "<YYYY-MM-DD>" },
    "active_layers": ["<layer-id>"]
  },
  "provenance_ui": {
    "shown": true,
    "what_is_visible": ["layer-source-popover", "ai-citations"]
  },
  "capture": {
    "browser": "chromium",
    "os": "<mac|windows|linux>",
    "created_at": "<ISO8601>",
    "commit": "<git-sha>",
    "notes": "What to click / how to reproduce this exact state."
  }
}
```

---

## 🧩 Add / update checklist

When adding or updating screenshots:

- [ ] Put it in the correct **view folder**
- [ ] Use the correct **filename pattern**
- [ ] Verify **no secrets/PII**
- [ ] Verify the screenshot represents a **real** UI state (not a half-loaded frame)
- [ ] Ensure at least one screenshot per relevant view shows **provenance/citations UI**
- [ ] (Optional) Add `.meta.json` if repro steps aren’t obvious
- [ ] If you changed UX, update the **Screenshot Matrix** rows if needed

---

## 🔗 Related docs & conventions

- 📘 Repo-wide documentation standards: see the project’s **Master Guide / Markdown Work Protocol**
- 🧠 Story content: keep **narrative assets** with Story Nodes (don’t mix story media into this UI library)
- 🗺️ UI trust model: provenance-first + citations-first behavior should be visible in key screenshots

---

## 🧯 FAQ

**Q: Why keep screenshots in-repo instead of just in PRs?**  
A: PR images disappear into history. This folder is a stable “visual spec” and regression reference.

**Q: PNG or WebP?**  
A: PNG is safest for crisp UI text. WebP is fine if your workflow keeps text sharp and file size smaller.

**Q: Do I need to update all breakpoints?**  
A: Only if the UX meaningfully changes across breakpoints. Otherwise keep the golden set lean.

---
