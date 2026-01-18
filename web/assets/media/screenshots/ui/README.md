# UI Screenshots 📸🧭  
![asset](https://img.shields.io/badge/asset-screenshots-1f6feb) ![scope](https://img.shields.io/badge/scope-web%20ui-8250df) ![format](https://img.shields.io/badge/format-png%20%7C%20webp-2da44e)

Welcome to **`web/assets/media/screenshots/ui/`** — the canonical home for **KFM Web UI screenshots** used in docs, stories, PRs, release notes, and design review.

---

## 📌 What belongs here

✅ **Do add screenshots** that:  
- Explain UI behavior (map interactions, timeline, layer toggles, metadata panels)  
- Document **trust features** (source/citation panels, dataset metadata, “AI-generated” labeling)  
- Capture **states** (empty, loading, error, offline, permission denied)  
- Provide before/after evidence for UX changes

❌ **Do not add screenshots** that:  
- Contain secrets (tokens/keys), personal data, private emails, or private coordinates  
- Leak sensitive locations (blur/generalize if needed)  
- Are blurry / low-resolution / full of irrelevant browser chrome

> [!NOTE]
> Treat screenshots as **evidence artifacts**: they should help someone understand **what the UI showed**, **why**, and **where the data came from**.

---

## 🗂️ Suggested subfolders

You can keep the folder flat for small volumes, but once it grows, prefer this layout:

```text
web/assets/media/screenshots/ui/
├── 📄 README.md                 # 📘 Screenshot conventions: naming, sizes, redaction, and allowed UI surfaces
├── 🧩 components/               # UI component captures (panels, toolbars, dialogs, legends, citations UI)
├── 🧭 views/                    # Page/view captures (map, timeline, focus-mode, story reader)
├── 🔁 flows/                    # Multi-step journeys (search → inspect → cite) captured as ordered sequences
├── 🚦 states/                   # State captures (empty/loading/error/permission/offline) for docs and QA
├── 📱 breakpoints/              # Desktop/tablet/mobile comparisons (same scene across sizes)
└── 🗞️ releases/                 # Versioned, publish-ready screenshots used in changelogs/release notes
```

---

## 🏷️ File naming convention

Use **kebab-case**, ASCII only, no spaces.

### ✅ Recommended pattern

```text
ui__<area>__<feature>__<state>__<breakpoint>__<theme>__<yyyy-mm-dd>.png
```

**Fields**  
- `area` → `map`, `timeline`, `focus-mode`, `search`, `layers`, `metadata`, `story`  
- `feature` → what changed or what’s being explained (`layer-info`, `citation-panel`, `time-scrub`)  
- `state` → `default`, `hover`, `selected`, `loading`, `error`, `empty`  
- `breakpoint` → `desktop-1440`, `tablet-1024`, `mobile-390`  
- `theme` → `light`, `dark`

### Examples ✅

- `ui__map__layer-panel__default__desktop-1440__light__2026-01-17.png`  
- `ui__focus-mode__ai-hint__expanded__desktop-1440__dark__2026-01-17.png`  
- `ui__timeline__scrub__loading__mobile-390__light__2026-01-17.png`

> [!TIP]
> If a screenshot is tied to a PR, add the PR number at the end:  
> `...__2026-01-17__pr-428.png`

---

## 🧪 Capture standards (make screenshots consistent)

### Viewports 📐
Pick one of these **standard breakpoints** (unless you have a reason not to):

- **Desktop:** 1440×900 (or 1440×1024)  
- **Tablet:** 1024×768  
- **Mobile:** 390×844 (iPhone-ish baseline)

### Pixel density ✨
- Prefer **2× device pixel ratio** exports when possible (crisper text)
- Avoid screenshots that are resized with blur (resize with sharp scaling if needed)

### Theme + UI settings 🌗
- If a feature is theme-dependent, capture both **light** and **dark**
- Keep zoom level, basemap, and visible layers stable for comparisons

### Crop discipline ✂️
- Crop to the **UI area that matters** (don’t include your OS taskbar)
- Keep enough context so users know what they’re looking at (panel title, legend, etc.)

---

## 🧾 Provenance metadata (recommended, not required)

When a screenshot is used in docs or a Story Node, attach a sidecar JSON to preserve context:

```text
ui__map__layer-panel__default__desktop-1440__light__2026-01-17.png
ui__map__layer-panel__default__desktop-1440__light__2026-01-17.meta.json
```

### Example `.meta.json`

```json
{
  "captured_at": "2026-01-17T00:00:00Z",
  "route": "/#map?lat=38.5&lng=-98.0&z=6",
  "breakpoint": "desktop-1440",
  "theme": "light",
  "git_sha": "PUT_COMMIT_SHA_HERE",
  "build": "dev",
  "layers": [
    { "id": "stac:item:ks:railroads:1885", "title": "1885 Railroad Map" }
  ],
  "notes": "Shows layer panel + metadata panel open for provenance visibility.",
  "redactions": []
}
```

> [!IMPORTANT]
> If you had to blur/omit anything, record it in `redactions`.

---

## 🔒 Redaction & sensitive-data rules

- **Never** commit secrets, keys, personal data, private emails, internal URLs, or non-public coordinates  
- If the UI can show sensitive locations, **generalize, blur, or avoid** capturing them  
- Prefer **public demo datasets** and public basemaps for screenshots

> [!WARNING]
> Screenshots can become a “side channel.” If a location should be hidden in the product, it should be hidden in screenshots too.

---

## 🧩 Using screenshots in docs

### Markdown embedding

From a doc near the repo root:

```md
![Layer panel with provenance](web/assets/media/screenshots/ui/ui__map__layer-panel__default__desktop-1440__light__2026-01-17.png)
```

From another file inside `docs/`:

```md
![Focus Mode evidence panel](../web/assets/media/screenshots/ui/ui__focus-mode__citation-panel__expanded__desktop-1440__light__2026-01-17.png)
```

### Alt text (accessibility) ♿
Write alt text that explains **what the user learns**, not just what’s on screen:

✅ “Layer panel open showing dataset title, license, and source attribution.”  
❌ “Screenshot of panel.”

---

## 🧹 Maintenance & hygiene

- Keep files **small** (optimize PNG/WebP; avoid multi-megabyte screenshots)  
- Replace outdated screenshots during UI changes (don’t let docs drift)  
- Prefer `releases/` for long-term, versioned documentation

---

## ✅ “Definition of Done” checklist

Before committing a screenshot, confirm:

- [ ] Correct naming convention  
- [ ] Crisp text, correct crop, minimal chrome  
- [ ] No secrets / PII / private coordinates  
- [ ] If used in docs, includes meaningful alt text  
- [ ] (Optional) `.meta.json` added for provenance context  
- [ ] Works in GitHub rendering (relative paths correct)

---

## 🔗 Related docs

- `docs/MASTER_GUIDE_v13.md` (pipeline + contracts)  
- `docs/architecture/` (UI/UX principles, provenance-first design)  
- `docs/governance/` (sensitivity + review gates)  

🧠 If you’re documenting **Focus Mode**, ensure screenshots clearly show:  
- provenance-linked evidence,  
- explicit labeling for AI assistance (when shown),  
- and any safeguards around sensitive locations.

---
