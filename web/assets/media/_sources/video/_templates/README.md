# 🎞️ Video Source Templates (`web/assets/media/_sources/video/_templates/`)

<p align="center">
  <img alt="KFM" src="https://img.shields.io/badge/KFM-Media%20Pipeline-0b3d91?style=for-the-badge">
  <img alt="Contract-first" src="https://img.shields.io/badge/Contract--First-meta.json%20required-2ea44f?style=for-the-badge">
  <img alt="Provenance" src="https://img.shields.io/badge/Provenance--First-no%20mystery%20layers-6f42c1?style=for-the-badge">
  <img alt="Accessibility" src="https://img.shields.io/badge/Accessibility-captions%20%2B%20transcript-orange?style=for-the-badge">
</p>

These folders are **copy/paste templates** for adding new videos to the KFM web app *the right way*:
- ✅ **source-first** (keep a high-quality original)
- ✅ **web-ready outputs** (MP4/WebM + poster)
- ✅ **contract-first metadata** (`meta.json`) so the UI can auto-render credits/attribution later
- ✅ **accessible by default** (captions + transcript)

> [!IMPORTANT]
> Templates here are **not meant to be imported directly** into the app.  
> **Copy a template** into a new slug folder under `_sources/video/`, then fill it out.

---

## 🧭 Quick navigation

- [📁 Expected folder model](#-expected-folder-model)
- [🧩 Template inventory](#-template-inventory)
- [🛠️ How to add a new video](#️-how-to-add-a-new-video)
- [🧾 `meta.json` contract (minimum)](#-metajson-contract-minimum)
- [🎚️ Encoding + performance guidelines](#️-encoding--performance-guidelines)
- [♿ Accessibility checklist](#-accessibility-checklist)
- [🧪 Review gates (Definition of Done)](#-review-gates-definition-of-done)
- [➕ Creating a new template](#-creating-a-new-template)

---

## 📁 Expected folder model

This is the **recommended mental model** for how video assets live in the repo.

```text
web/assets/media/
├── 📁 video/                      # ✅ built outputs consumed by the web UI
│   └── 📁 <video_slug>/
│       ├── 🎬 <video_slug>.mp4
│       ├── 🎬 <video_slug>.webm
│       ├── 🖼️ poster.jpg
│       ├── 📝 captions.en.vtt
│       └── 🧾 meta.json           # can be copied/derived from source meta.json
│
└── 📁 _sources/                   # ✍️ authoring inputs (raw + editable)
    └── 📁 video/
        ├── 📁 _templates/         # 👈 you are here
        └── 📁 <video_slug>/
            ├── 🎞️ source.mov      # or .mp4/.mkv (highest quality available)
            ├── 🧾 meta.json
            ├── 📝 transcript.md
            ├── 📝 captions.en.vtt
            └── 📄 notes.md        # optional: edit notes / provenance breadcrumbs
```

> [!TIP]
> Keep `_sources/` as the **human-friendly authoring zone**.  
> Keep `video/` as the **deterministic, web-optimized outputs** zone.

---

## 🧩 Template inventory

Create (or copy) templates as subfolders inside this directory. Suggested starting set:

| Template folder | Best for | Includes |
|---|---|---|
| `TEMPLATE__ui-loop__silent/` | Decorative ambient loops (no narration) | `source.*`, `meta.json`, `poster.jpg`, optional captions (usually none) |
| `TEMPLATE__story-clip__captioned/` | Story Nodes / educational clips | `source.*`, `meta.json`, `poster.jpg`, `captions.en.vtt`, `transcript.md` |
| `TEMPLATE__data-animation__map/` | Map/timeline animations | `source.*`, `meta.json`, `poster.jpg`, `captions.en.vtt` (if narrated), `notes.md` (pipeline params) |

> [!NOTE]
> If your repo already has different template names, keep them—just ensure each template documents the **same contract + deliverables**.

---

## 🛠️ How to add a new video

### 1) Pick a slug 🏷️
Use **kebab-case** and keep it stable:

- ✅ `dust-bowl-overview`
- ✅ `kansas-river-flood-1951`
- ❌ `FinalEdit_v7_REALFINAL`

### 2) Copy a template 📋
```bash
# from repo root
cp -R web/assets/media/_sources/video/_templates/TEMPLATE__story-clip__captioned \
      web/assets/media/_sources/video/dust-bowl-overview
```

### 3) Drop in the highest-quality source 🎞️
Replace the placeholder `source.*` with your real file (keep the name simple):

- `source.mov` (preferred if you have a master)
- `source.mp4` (acceptable if it’s the only source)

### 4) Fill out `meta.json` 🧾
This is **non-negotiable**. If we can’t describe it, we can’t trust it.

- source + license + attribution
- what it depicts / why it exists
- how it was processed (at least high-level)

### 5) Generate web derivatives ⚙️
Place the final outputs in:

- `web/assets/media/video/<video_slug>/`

If your project has an existing media build script, use that. If not, use the reference commands below.  
(Goal: deterministic settings → reproducible outputs.)

### 6) Add captions + transcript ♿
If there is **spoken content** or **meaningful audio**, captions + transcript are required.

---

## 🧾 `meta.json` contract (minimum)

> [!IMPORTANT]
> KFM is **contract-first**: metadata is a “data contract” and must exist before an asset is accepted.

Use this as a starting point (extend freely, but don’t remove minimums):

```json
{
  "id": "video:kfm:dust-bowl-overview",
  "title": "Dust Bowl Overview (1930s Kansas)",
  "description": "Short narrated clip used in the Dust Bowl story sequence.",
  "kind": "story-clip",
  "language": "en",

  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Kansas Frontier Matrix contributors",
    "source_url": "https://example.com/source-if-applicable"
  },

  "sources": [
    {
      "type": "archive|capture|render|compiled",
      "citation": "Where the footage came from (institution / collection / call number, etc.)",
      "url": "https://…",
      "notes": "Any constraints (non-commercial, share-alike, etc.)"
    }
  ],

  "created_utc": "2026-01-18T00:00:00Z",
  "updated_utc": "2026-01-18T00:00:00Z",

  "media": {
    "duration_s": 45.0,
    "dimensions_px": { "w": 1920, "h": 1080 },
    "has_audio": true
  },

  "deliverables": {
    "poster": "poster.jpg",
    "captions": {
      "en": "captions.en.vtt"
    },
    "transcript": "transcript.md",
    "derivatives": {
      "mp4": "web/assets/media/video/dust-bowl-overview/dust-bowl-overview.mp4",
      "webm": "web/assets/media/video/dust-bowl-overview/dust-bowl-overview.webm"
    }
  },

  "provenance": {
    "processing_steps": [
      "Trimmed to 45s, normalized audio, exported MP4 (H.264) and WebM (VP9)."
    ],
    "tools": [
      { "name": "ffmpeg", "version": "x.y.z", "notes": "Optional but recommended" }
    ]
  }
}
```

> [!TIP]
> If the video is **evidence** (not decorative), add cross-links that your pipeline can later map into STAC/DCAT/PROV IDs.

---

## 🎚️ Encoding + performance guidelines

### ✅ Output formats (web-safe)
- **MP4 (H.264 + AAC)**: baseline compatibility
- **WebM (VP9/AV1 + Opus)**: better compression where supported
- **Poster image**: `poster.jpg` (or `poster.webp` if your app supports it)

### ✅ Practical recommendations
- Keep loops short (5–15s) if used as UI ambiance
- Avoid giant bitrates; web UI should feel instant
- Prefer 1080p max unless there’s a strong reason for higher
- Normalize audio if narration exists (don’t blow out earbuds)

<details>
<summary><strong>📦 Reference ffmpeg commands (copy/paste)</strong></summary>

> These are **reference presets**. If your repo has a canonical script, use that instead.

```bash
# 1) Poster at ~1s
ffmpeg -y -i source.mov -ss 00:00:01.000 -vframes 1 poster.jpg

# 2) MP4 (H.264)
ffmpeg -y -i source.mov \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -movflags +faststart \
  -crf 20 -preset slow \
  -c:a aac -b:a 160k \
  dust-bowl-overview.mp4

# 3) WebM (VP9)
ffmpeg -y -i source.mov \
  -c:v libvpx-vp9 -crf 32 -b:v 0 \
  -row-mt 1 -deadline good -cpu-used 2 \
  -c:a libopus -b:a 96k \
  dust-bowl-overview.webm
```

</details>

---

## ♿ Accessibility checklist

- ✅ Captions (`.vtt`) for any speech
- ✅ Transcript (`transcript.md`) for narration-heavy videos
- ✅ Avoid flashing patterns / rapid strobe
- ✅ Don’t rely on color alone for meaning (especially for data animations)
- ✅ If the video conveys key info visually, consider an **audio description** track (or a narrated version)

> [!NOTE]
> If the video is purely decorative (ambient loop, no speech, no meaning), captions/transcript can be omitted — but metadata + license still apply.

---

## 🧪 Review gates (Definition of Done)

Before a video is considered “ready” ✅:

- [ ] `meta.json` exists and includes **license + attribution + source**
- [ ] No “mystery” origins (we can answer: *where did this come from?*)
- [ ] Outputs exist in `web/assets/media/video/<slug>/` (MP4 + WebM + poster)
- [ ] Captions + transcript are present for spoken content
- [ ] File size and playback performance are reasonable
- [ ] The video is not hard-coded into UI if it should be served as governed evidence

> [!WARNING]
> If a video is used as **evidence** inside narratives / Focus Mode, it must remain **traceable and governed** (avoid ad-hoc drops that bypass provenance).

---

## ➕ Creating a new template

When you add a new template folder here:

1. Name it like: `TEMPLATE__<category>__<variant>/`
2. Include:
   - `source.<ext>` (placeholder)
   - `meta.json` (with comments or clear placeholder values)
   - `poster.jpg` (placeholder or omitted with instructions)
   - `README.md` (template-specific notes if needed)
3. Update the [Template inventory](#-template-inventory) table above.

---

## 🧠 Philosophy (why this folder exists)

KFM is built so that **anything visible in the UI can be traced back to sources with provenance** — and so tools can automatically generate attribution/citations later.  
Templates help us keep media additions consistent, reproducible, and reviewable.

🚀 When we do this well, adding a new video becomes:
> “copy template → fill contract → run deterministic build → ship”
