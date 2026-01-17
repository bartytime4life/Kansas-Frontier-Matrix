# 🎬 Web Demo Videos (KFM)  
![Asset Type](https://img.shields.io/badge/asset-video-informational?style=for-the-badge) ![Scope](https://img.shields.io/badge/scope-web%20ui%20demos-blue?style=for-the-badge) ![Default Format](https://img.shields.io/badge/default-mp4%20(h.264)-success?style=for-the-badge) ![A11y](https://img.shields.io/badge/accessibility-captions%20required-orange?style=for-the-badge)

📍 **Folder:** `web/assets/media/video/demos/`  
This directory holds **small, web-optimized demo clips** used to showcase the Kansas Frontier Matrix (KFM) web experience (🌍 map + 🧭 timeline + 📚 narrative).

> [!IMPORTANT]
> These are **public-facing assets**. Do **not** include: personal data, private endpoints, API keys/tokens, non-redistributable imagery, or any copyrighted material without explicit permission.

---

## 🧭 Quick Nav
- [✅ What belongs here](#-what-belongs-here)
- [🚫 What does not belong here](#-what-does-not-belong-here)
- [🗂️ Folder layout](#️-folder-layout)
- [🏷️ Naming conventions](#️-naming-conventions)
- [🧾 `demo.meta.json` spec](#-demometajson-spec)
- [♿ Accessibility rules](#-accessibility-rules)
- [🎞️ Encoding guidelines](#️-encoding-guidelines)
- [🧰 Git + file size](#-git--file-size)
- [🔗 Embedding in docs/UI](#-embedding-in-docsui)
- [✅ PR checklist](#-pr-checklist)

---

## ✅ What belongs here
Use this folder for **short** demo clips that help explain or market the web UI:

- 🗺️ **Map interactions**: layer toggles, legends, symbology switches
- 🔎 **Search**: finding a place/dataset, jumping to a feature
- 🕰️ **Timeline navigation**: sliders, decade filters, “time travel” sequences
- 🧩 **Popups & side panels**: clicking a feature to open details/metadata
- 🧠 **Focus Mode / guided flows**: short “here’s what this feature does” walkthroughs
- 🧾 **Provenance moments**: showing how users inspect a layer’s source/metadata (key KFM value)

---

## 🚫 What does not belong here
- 🎥 **Raw recordings** (`.mov`, huge `.mp4` screen captures, long takes)  
- 📦 **Project deliverables** like webinars, talks, or full tutorials (store elsewhere)
- 🧪 **Experimental clips** tied to unstable UI states (keep local until stable)
- 🔐 Any clip containing secrets, internal URLs, or sensitive UI-only flags

---

## 🗂️ Folder layout
**Rule:** *one demo = one folder* (keeps posters/captions/metadata together).

<details>
<summary>📁 Example structure</summary>

```text
web/assets/media/video/demos/
├── 📄 README.md
├── 📄 manifest.json                # (optional) gallery/index manifest
└── 📁 kfm__focus-mode__tornado-timeline/
    ├── 🎞️ demo.mp4                 # required
    ├── 🖼️ poster.jpg               # required (or poster.webp)
    ├── 📝 captions.en.vtt          # required
    ├── 📄 transcript.md            # required
    └── 🧾 demo.meta.json           # required
```
</details>

### Required companion files
| File | Required | Purpose |
|---|:---:|---|
| `demo.mp4` | ✅ | Primary format (most compatible) |
| `poster.jpg` / `poster.webp` | ✅ | Thumbnail shown before playback |
| `captions.en.vtt` | ✅ | Captions (accessibility + silent viewing) |
| `transcript.md` | ✅ | Text alternative + searchable content |
| `demo.meta.json` | ✅ | License + provenance + tags + pointers |

Optional extras:
- `demo.webm` (✅ nice-to-have for modern browsers)
- localized captions (e.g., `captions.es.vtt`)
- short preview GIF (only if truly needed; usually skip for performance)

---

## 🏷️ Naming conventions
### Folder slug
Use a stable, readable slug:

- `kfm__<area>__<topic>`
- lowercase, hyphenated topic
- no spaces, no special characters beyond `-` and `_`

Examples:
- `kfm__layers__county-boundaries`
- `kfm__timeline__railroads-expansion`
- `kfm__focus-mode__dust-bowl-story`

### Inside each folder
Use consistent filenames:
- `demo.mp4`
- `poster.jpg`
- `captions.en.vtt`
- `transcript.md`
- `demo.meta.json`

> [!TIP]
> Keep filenames boring ✨—the folder name carries meaning; the files stay predictable.

---

## 🧾 `demo.meta.json` spec
Each demo must ship with a small metadata file.

Minimum recommended fields:
```json
{
  "id": "kfm__focus-mode__tornado-timeline",
  "title": "Focus Mode: Tornado Timeline",
  "summary": "Shows timeline scrubbing + feature click to open details.",
  "tags": ["focus-mode", "timeline", "popups"],
  "created_at": "2026-01-17",
  "owners": ["@your-gh-handle"],

  "kfm": {
    "ui_area": "web",
    "feature_flags": [],
    "tested_browsers": ["Chrome", "Firefox", "Safari"]
  },

  "evidence_refs": {
    "datasets": [],
    "stac_items": [],
    "dcat_datasets": [],
    "prov_runs": []
  },

  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Kansas Frontier Matrix contributors"
  }
}
```

### Notes on `evidence_refs`
If the demo highlights a specific dataset or Story Node, **link it**:
- dataset IDs / catalog IDs (preferred)
- Story Node slug(s) (if relevant)
- “prov run” IDs (when showing derived/analysis outputs)

---

## ♿ Accessibility rules
- ✅ Captions required (`.vtt`)  
- ✅ Transcript required (`transcript.md`)  
- ✅ No autoplay-with-sound (avoid surprise audio)  
- ✅ Ensure UI text is readable at playback resolution  
- ✅ Avoid flashing content / rapid zooms

> [!NOTE]
> Many users will watch these muted (especially inside docs). Captions are not optional.

---

## 🎞️ Encoding guidelines
Keep demos **small + fast**:
- ⏱️ Target length: **10–45s**
- 📐 Target resolution: **1280×720** (720p) unless detail requires 1080p
- 🎚️ Target fps: **30**
- 🔇 Audio: optional; if present, keep it clean and low-bitrate
- 🚀 “fast start”: enable progressive download (`moov atom` first)

### Suggested `ffmpeg` (MP4 / H.264)
```bash
ffmpeg -i input.mov \
  -vf "scale=-2:720,fps=30" \
  -c:v libx264 -crf 23 -preset slow -pix_fmt yuv420p \
  -movflags +faststart \
  -c:a aac -b:a 128k \
  demo.mp4
```

### Optional `ffmpeg` (WebM)
```bash
ffmpeg -i demo.mp4 \
  -c:v libvpx-vp9 -crf 32 -b:v 0 \
  -c:a libopus -b:a 96k \
  demo.webm
```

> [!TIP]
> If UI text becomes blurry, either bump to 1080p **or** zoom the recording area—don’t ship unreadable clips.

---

## 🧰 Git + file size
Videos grow fast. Keep PRs manageable:
- ✅ Prefer **small** demos (< 10–20MB per clip when possible)
- ✅ If files are consistently large, use **Git LFS** for `*.mp4`, `*.webm`, `*.mov`

Example (repo root):
```bash
git lfs track "*.mp4"
git lfs track "*.webm"
git lfs track "*.mov"
```

---

## 🔗 Embedding in docs/UI
### Embed in Markdown (GitHub-friendly)
```html
<video controls playsinline width="100%" poster="./kfm__focus-mode__tornado-timeline/poster.jpg">
  <source src="./kfm__focus-mode__tornado-timeline/demo.mp4" type="video/mp4" />
  <track kind="captions" srclang="en" src="./kfm__focus-mode__tornado-timeline/captions.en.vtt" label="English" default />
  Sorry — your browser doesn’t support embedded video.
</video>
```

### Embed in React
If your bundler supports static imports:
```tsx
import demo from "./demos/kfm__focus-mode__tornado-timeline/demo.mp4";
import poster from "./demos/kfm__focus-mode__tornado-timeline/poster.jpg";

export function Demo() {
  return (
    <video controls playsInline poster={poster} style={{ width: "100%" }}>
      <source src={demo} type="video/mp4" />
    </video>
  );
}
```

---

## ✅ PR checklist
Before opening a PR, confirm:

- [ ] Demo has its own 📁 folder slug
- [ ] `demo.mp4` present and plays in major browsers
- [ ] `poster.*` present
- [ ] `captions.en.vtt` present and synced
- [ ] `transcript.md` present
- [ ] `demo.meta.json` present with license + attribution
- [ ] No secrets, private URLs, or sensitive data captured
- [ ] File size is reasonable (or Git LFS is used)
- [ ] Demo accurately reflects current UI behavior (no outdated flows)

---

## 🧩 Optional: `manifest.json` (demo gallery index)
If/when we build an in-app demo gallery, add a `manifest.json` in this folder that lists demos + their metadata so the UI can render a searchable demo catalog.

✨ Suggested shape:
```json
{
  "version": 1,
  "demos": [
    {
      "id": "kfm__focus-mode__tornado-timeline",
      "path": "kfm__focus-mode__tornado-timeline/demo.mp4",
      "poster": "kfm__focus-mode__tornado-timeline/poster.jpg"
    }
  ]
}
```
