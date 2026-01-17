<!--
📄 File: web/assets/media/screenshots/ui/map-viewer/README.md
🧭 Purpose: Curated UI screenshots for the KFM Map Viewer (docs, QA, design reviews)
-->

# 🗺️ Map Viewer — Screenshot Library 📸

| Badge-ish | Meaning |
|---|---|
| 🧩 **UI Area** | Map Viewer (2D/3D) |
| 🗂️ **Asset Type** | Product screenshots (user-facing states) |
| 🧪 **Primary Use** | Docs, PRs, release notes, UX audits, Story/Focus Mode demos |
| 🔍 **Goal** | Consistent “known-good” visuals that explain *how the map works* |

> 🧠 **Rule of thumb:** If it changes how someone *reads the map* (layers, time, legend, provenance, AI citations), it deserves a screenshot.

---

## 🎯 What belongs here

✅ **Do store**
- Full UI screenshots of the **Map Viewer** in meaningful states:
  - 🔎 Search + results
  - 🧱 Layer panel open (grouped layers, toggles)
  - 🎚️ Transparency / legend / symbology controls
  - 🧭 Timeline slider + event markers
  - 🧷 Feature click popup + details sidebar
  - 🧠 Focus Mode panel **with citations visible**
  - 🎬 Story Mode stepper synced to map/time
  - 🌎 Optional 3D toggle view (if applicable)

🚫 **Don’t store**
- Random local dev screenshots with debug overlays
- Screenshots containing secrets (tokens, keys, internal URLs), personal data, or restricted locations
- Generic marketing art (keep UI screenshots “truthful”, not polished composites)

---

## 📁 Suggested structure

If this folder grows, keep it tidy with lightweight subfolders:

```text
📁 web/assets/media/screenshots/ui/map-viewer/
├─ 📄 README.md
├─ 📁 desktop/               # Primary “documentation-grade” captures
├─ 📁 mobile/                # Responsive UI captures
├─ 📁 states/                # Focused UI state shots (panels, popovers)
├─ 📁 flows/                 # Multi-step sequences (01/02/03…)
└─ 📁 _archive/              # Old screenshots kept briefly during transitions
```

> ✨ Keep **desktop/** as the “source of truth” unless a screenshot is explicitly mobile-first.

---

## 🏷️ Naming convention

Make names:
- **Searchable** 🔎
- **Sortable** 🗃️
- **Stable** ✅ (avoid “final2.png” energy)

### ✅ Recommended pattern

```text
YYYY-MM-DD__<breakpoint>__<scenario>__<theme>__v<nn>.<png|webp>
```

- `<breakpoint>`: `desktop-1440x900`, `desktop-1920x1080`, `mobile-390x844`, etc.
- `<scenario>`: short + kebab-case (`layer-panel`, `timeline-events`, `focus-mode-answer`)
- `<theme>`: `light` or `dark`
- `v<nn>`: bump when replacing while keeping meaning (`v01`, `v02`)

### 📌 Examples

```text
2026-01-17__desktop-1440x900__default-map__light__v01.png
2026-01-17__desktop-1440x900__layer-panel-open__light__v01.png
2026-01-17__desktop-1440x900__timeline-events__light__v01.png
2026-01-17__desktop-1440x900__focus-mode-citations__light__v01.png
2026-01-17__mobile-390x844__collapsed-panels__light__v01.png
```

---

## ✅ Capture checklist

### 🧊 Consistency (avoid “false diffs”)
- Same **viewport** and **zoom** for comparable shots
- Same **theme** (default to light unless demonstrating dark)
- Same **time selection** on the timeline (pick a canonical year/time for docs)
- Same **active layers** (avoid “mystery layers”)
- Hide cursor unless the cursor is *the point* (e.g., hover tooltip demo)

### 🧭 Content (what we want visible)
- Top nav / search bar (when relevant)
- Layer list grouped by category (when relevant)
- Transparency controls + legend (for interpretability)
- Timeline slider + event markers (when demonstrating time)
- Feature popup + details sidebar (when demonstrating exploration)
- Focus Mode answer panel **with citations** (transparency / evidence)
- Story Mode step controls (next/back), plus the map/time change they drive

### 🔐 Privacy & safety
- Blur/remove:
  - API keys, tokens, internal endpoints
  - user emails, usernames, browser profiles
  - restricted geospatial details (if any layer/content is not public-safe)
- If something must be demonstrated but is sensitive:
  - use a **sanitized dataset**, or
  - capture a **cropped** view that excludes sensitive info

---

## 🧾 Canonical screenshots (checklist)

Use this as the “minimum set” for docs and regressions:

| ID | Scenario | Suggested filename (example) | Notes |
|---:|---|---|---|
| 01 | Default viewer | `YYYY-MM-DD__desktop-1440x900__default-map__light__v01.png` | Clean baseline |
| 02 | Search in action | `...__search-results__light__v01.png` | Place + dataset search if possible |
| 03 | Layer panel open | `...__layer-panel-open__light__v01.png` | Categories visible |
| 04 | Layer legend + opacity | `...__legend-opacity__light__v01.png` | “Readable map” moment |
| 05 | Timeline slider | `...__timeline-slider__light__v01.png` | Shows time control clearly |
| 06 | Timeline event marker | `...__timeline-events__light__v01.png` | Marker + clicked detail |
| 07 | Feature popup | `...__feature-popup__light__v01.png` | Tooltip/popup clarity |
| 08 | Details sidebar | `...__details-sidebar__light__v01.png` | Metadata + richer info |
| 09 | Focus Mode citations | `...__focus-mode-citations__light__v01.png` | Evidence visible |
| 10 | Story Mode stepper | `...__story-mode-step__light__v01.png` | Narrative + map sync |
| 11 | Mobile layout | `...__mobile-390x844__collapsed-panels__light__v01.png` | Responsive proof |
| 12 | Optional 3D view | `...__3d-view__light__v01.png` | Only if feature exists |

> 🧩 If a PR changes a UI element in this list, **refresh the matching screenshot(s)**.

---

## 🔄 How to add / update screenshots

1. 📸 Capture the screenshot using the agreed viewport + theme.
2. 🧽 Sanitize (blur secrets/PII, crop sensitive regions).
3. 🗜️ Optimize size (keep UI crisp):
   - Prefer **PNG** for sharp text/icons
   - Use **WebP** if the image is large but still needs to look clean
4. 🧾 Place it in the appropriate subfolder (`desktop/`, `mobile/`, etc.)
5. 🧷 Update the **Canonical screenshots** table (or add a new row for new scenarios).
6. 🧪 If used for QA/regression, ensure the screenshot is referenced in the relevant doc/test notes.

---

## 🧪 Optional: “golden” screenshots for UI regression

<details>
  <summary>🧰 If we later add screenshot automation (Playwright/Cypress/etc.)</summary>

- Treat files in `desktop/` as **goldens**:
  - deterministic viewport
  - deterministic time selection
  - deterministic layer set
- Store a tiny “scenario manifest” alongside (optional), e.g.:

```text
📄 2026-01-17__desktop-1440x900__timeline-events__light__v01.meta.json
```

Example fields:
- `viewport`, `theme`, `route`, `timeSelection`, `layersEnabled`, `notes`

This makes diffs reviewable and prevents “why does this look different?” confusion.

</details>

---

## 🧷 Using these screenshots in docs

Example (adjust the filename/path to match the real file):

```md
![Map Viewer with layer panel open](./desktop/YYYY-MM-DD__desktop-1440x900__layer-panel-open__light__v01.png)
```

✅ Always include descriptive alt text (accessibility + searchability).

---

## 🧼 Quick maintenance tips

- 🗑️ Remove/relocate obsolete shots quickly (use `_archive/` temporarily).
- 🧭 Prefer “explanatory states” over “pretty states”.
- 🧩 Keep the list above honest: if a feature changes, refresh the evidence.

---

🧊 **Goal:** This folder should feel like a reliable “UI truth kit” for the Map Viewer.
