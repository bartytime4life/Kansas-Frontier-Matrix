---
title: "Release Screenshots — 2026-01"
release: "2026-01"
artifact: "screenshots"
scope: "web"
status: "active"
---

# 📸 Release Screenshots — 2026-01

![Release](https://img.shields.io/badge/release-2026--01-blue)
![Assets](https://img.shields.io/badge/assets-screenshots-orange)
![Scope](https://img.shields.io/badge/scope-web%20ui-brightgreen)
![Principle](https://img.shields.io/badge/principle-provenance--first-7b2cbf)

> [!IMPORTANT]
> In KFM, visuals are **evidence**. Treat every screenshot as a *reproducible* artifact:
> it should be traceable to a build, a dataset state, and a UI route/mode — not “whatever was on screen.” 🧾🧬

---

## 🧭 What this folder is

This directory is the **canonical screenshot set** for the `2026-01` release of the KFM Web UI.

Use these screenshots for:
- 🧪 QA regression snapshots (UI + map composition)
- 📝 Release notes / changelog visuals
- 📚 Documentation & walkthroughs (Map, Story, Focus)
- 🧠 “Visual audit log” of provenance-first UX (sources, citations, layer lineage)

---

## 🚫 What this folder is not

Please **do not** commit:
- 🔐 Sensitive locations (or anything that should be redacted / generalized)
- 🧩 “Mystery layers” with unknown source/provenance
- 🪪 Keys/tokens, local file paths, private endpoints, personal info
- 🗑️ Duplicates (same state, same viewport, no new signal)

---

## 📁 Recommended layout

> You can keep everything flat, but this structure scales cleanly as screenshots grow.

```text
📁 web/assets/media/screenshots/releases/2026-01/
├── 📄 README.md                         ✅ you are here
├── 📄 manifest.json                      🧾 optional but recommended
├── 📁 desktop/
│   ├── 📁 light/
│   └── 📁 dark/
├── 📁 tablet/
│   ├── 📁 light/
│   └── 📁 dark/
├── 📁 mobile/
│   ├── 📁 light/
│   └── 📁 dark/
└── 📁 gifs/                              🎞️ short loops only (optional)
```

---

## 🧾 Filename convention

Keep filenames **stable** and **readable**. Put the *details* in metadata (next section), not in a 200‑char filename.

**Recommended pattern**
```text
<area>__<feature>__<viewport>__<theme>.png
```

**Examples**
```text
map__kansas-overview__1440x900__light.png
layers__provenance-popover__1440x900__dark.png
focus__answer-with-citations__390x844__light.png
story__step-03-map-context__834x1112__dark.png
```

> [!TIP]
> Prefer `__` (double underscore) as a delimiter. It’s grep-friendly and survives tooling.

---

## 🧬 Sidecar metadata (`*.meta.json`) — REQUIRED

For every image:
- `something.png`
- add a sibling: `something.meta.json`

This keeps screenshots **reproducible** and ties them to the KFM contract/provenance mindset.

### ✅ Minimal metadata schema (copy/paste)

```json
{
  "release": "2026-01",
  "captured_at": "2026-01-17T00:00:00Z",

  "app": {
    "name": "KFM Web",
    "version": "0.0.0",
    "git_sha": "abcdef1234567890",
    "build_id": "local-or-ci-build-id"
  },

  "ui": {
    "route": "/",
    "mode": "map | story | focus",
    "theme": "light | dark",
    "locale": "en-US",
    "viewport": { "width": 1440, "height": 900, "dpr": 2 },
    "device": "Desktop Chrome"
  },

  "data": {
    "layers": [
      {
        "id": "stac-or-dcat-or-internal-layer-id",
        "title": "Human readable layer name",
        "license": "SPDX-or-human-readable",
        "source_ref": "linkable id/uri if available"
      }
    ],
    "time": { "as_of": "2026-01-17" }
  },

  "provenance": {
    "prov_run_id": "optional-run-id",
    "dcat_dataset_ids": [],
    "stac_item_ids": []
  },

  "alt": "One-sentence accessible description of what the screenshot shows."
}
```

---

## 🧾 Optional `manifest.json` (recommended)

If this folder is going to be consumed by the web app (gallery, docs pages, etc.), maintain a `manifest.json` that indexes everything.

### Example manifest shape

```json
{
  "release": "2026-01",
  "updated_at": "2026-01-17T00:00:00Z",
  "items": [
    {
      "file": "desktop/light/map__kansas-overview__1440x900__light.png",
      "meta": "desktop/light/map__kansas-overview__1440x900__light.meta.json",
      "tags": ["map", "overview", "baseline"],
      "priority": "high"
    }
  ]
}
```

---

## 📐 Capture matrix

Try to capture each **high‑signal** view in at least:

### Viewports
- 🖥️ Desktop: `1440×900` (baseline)
- 🖥️ Desktop wide: `1920×1080` (optional)
- 📱 Mobile: `390×844` (baseline)
- 📟 Tablet: `834×1112` (optional)

### Themes
- 🌞 Light
- 🌚 Dark

### Modes (when applicable)
- 🗺️ Map (2D / 3D if relevant)
- 📖 Story
- 🤖 Focus (AI + citations)

---

## 🗺️ Map screenshot quality bar

When the screenshot is map-centric, ensure:
- 🧭 **Orientation** is understandable (north arrow if used, or another clear cue)
- 📏 **Scale** is readable (scale bar if relevant)
- 🗂️ **Legend** is present when symbology isn’t obvious
- 🧾 **Attribution/source** is visible and not cropped out
- 🎨 **Color scale** is consistent (don’t “wing it” per screenshot)
- 🧹 Avoid clutter: the map should be the hero, UI chrome should not overwhelm

> [!NOTE]
> If the purpose is to document provenance, intentionally capture a state where
> the user can *inspect* the layer source / metadata (e.g., layer info popover).

---

## 🤖 Focus Mode / AI screenshots quality bar

If the screenshot involves Focus Mode:
- ✅ The answer must show **sources/citations** (or a visible path to them)
- 🧾 The UI should make clear what is **human-authored** vs **AI-generated**
- 🧠 Avoid screenshots of speculative output — capture evidence-constrained answers
- 🔐 If the content is sensitive, **redact/generalize** before committing

---

## 🔐 Sensitive content rules (quick)

If there’s any chance the screenshot reveals:
- exact coordinates of protected sites,
- sensitive ecological locations (e.g., endangered species),
- culturally sensitive places / sovereignty-related context,
- private infrastructure detail,

…then:
- blur, crop, or generalize, **or**
- use a synthetic/staged dataset for the screenshot, **or**
- don’t commit the image here at all.

---

## ✅ “Add a screenshot” checklist

- [ ] Captured on an intended viewport (per matrix)
- [ ] File named with the convention (`area__feature__viewport__theme.png`)
- [ ] Sidecar created (`.meta.json`) with build + provenance details
- [ ] Alt text written (in the meta file at minimum)
- [ ] No sensitive data / secrets / private endpoints in-frame
- [ ] Attribution visible (don’t crop it out)
- [ ] Image optimized (reasonable file size, crisp text)

---

## 🗂️ Screenshot index (fill in as you add assets)

> [!TIP]
> Keep this list short and high-signal. Prefer **10–30** great screenshots over 200 noisy ones.

| Category | Screenshot | Viewport | Theme | Notes |
|---|---|---:|:---:|---|
| 🗺️ Map | *(add link)* | 1440×900 | 🌞/🌚 | Baseline overview |
| 🧾 Provenance | *(add link)* | 1440×900 | 🌞/🌚 | Layer source/metadata visible |
| 🤖 Focus | *(add link)* | 390×844 | 🌞/🌚 | Answer includes citations |
| 📖 Story | *(add link)* | 834×1112 | 🌞/🌚 | Step indicator + map context |

---

## 🧰 Tips for maintainers

<details>
<summary><strong>🧪 Deterministic capture (preferred)</strong></summary>

If there’s an automated screenshot workflow (Playwright/Cypress/etc.), use it:
- deterministic viewport + DPR
- deterministic seed/state
- pinned dataset versions
- consistent theme + locale

Manual screenshots are acceptable, but must still include `.meta.json`.
</details>

<details>
<summary><strong>🗜️ File size & format</strong></summary>

- Prefer **PNG** for UI (text stays crisp).
- Prefer **GIF** only for short motion loops (3–6 seconds).
- Don’t commit huge unoptimized images if the same fidelity can be achieved smaller.
</details>
