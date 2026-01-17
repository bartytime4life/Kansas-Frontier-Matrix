# 🎬 Hero Video Assets — KFM Web UI

![Asset Type](https://img.shields.io/badge/asset-hero%20video-blue)
![Location](https://img.shields.io/badge/path-web%2Fassets%2Fmedia%2Fvideo%2Fhero-informational)
![Performance](https://img.shields.io/badge/goal-fast%20%26%20lightweight-success)
![Accessibility](https://img.shields.io/badge/a11y-prefers--reduced--motion-important)
![Provenance](https://img.shields.io/badge/provenance-required-critical)

> [!IMPORTANT]
> Hero videos are **decorative** ✨  
> The site must remain fully usable, readable, and fast **without** them (poster-only fallback + reduced motion support).

---

## 🧭 What this folder is

This directory contains the **final, web-ready** hero background video loops used by the Kansas Frontier Matrix (KFM) frontend (landing/hero section).

- ✅ Small, silent loops  
- ✅ Optimized for web delivery  
- ✅ Paired with metadata for **provenance + licensing** (KFM principle: nothing should be a “black box”)

---

## 📍 Path

```text
web/assets/media/video/hero/
```

---

## 🗂️ Expected contents

```text
📁 web/assets/media/video/hero/
├── 📄 README.md
├── 🎞️ kfm-hero-prairie-v1.mp4
├── 🎞️ kfm-hero-prairie-v1.webm              # optional (smaller on some browsers)
├── 🖼️ kfm-hero-prairie-v1.poster.webp       # preferred poster
├── 🖼️ kfm-hero-prairie-v1.poster.jpg        # fallback poster
├── 🧾 kfm-hero-prairie-v1.meta.json         # REQUIRED provenance/license + technical info
└── 📄 ATTRIBUTION.md                        # optional (roll-up credits for humans)
```

---

## 📛 Naming & versioning rules (stable IDs ✅)

KFM favors stability and auditability. Treat filenames like stable identifiers:

### ✅ DO
- Use **kebab-case**
- Include a semantic theme
- Include an explicit version
- Bump version instead of overwriting an existing file

**Pattern**
```text
kfm-hero-<theme>-v<major>.<ext>
```

**Examples**
- `kfm-hero-prairie-v1.mp4`
- `kfm-hero-flint-hills-v2.webm`
- `kfm-hero-archive-maplines-v1.poster.webp`

### ❌ DON’T
- Rename assets after they’ve shipped (breaks caching + references)
- Use ambiguous names like `final-final2.mp4`
- Replace the content of an existing filename without versioning

---

## 🧾 Provenance sidecar metadata (REQUIRED)

Every hero video must ship with a matching `*.meta.json`.

### ✅ Required sidecar mapping

| Asset | Required sidecar |
|------|-------------------|
| `kfm-hero-xyz-v1.mp4` | `kfm-hero-xyz-v1.meta.json` |
| `kfm-hero-xyz-v1.webm` (optional) | same `.meta.json` |

### 🧩 Suggested `*.meta.json` schema

Keep this **human-readable** and **machine-parseable** (future-friendly for automation).

```json
{
  "id": "kfm-hero-prairie-v1",
  "title": "Kansas Prairie — Golden Hour",
  "description": "Slow pan across prairie grasses at golden hour. Decorative hero background.",
  "tags": ["kansas", "prairie", "landscape", "hero"],
  "created_at": "2026-01-17",
  "created_by": {
    "name": "KFM Contributors",
    "contact": "docs/CONTRIBUTING.md"
  },

  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Video by <Name/Org>. Used under CC BY 4.0.",
    "source_url": "https://example.com/source",
    "notes": "If you can't verify license/rights, DO NOT commit the asset."
  },

  "technical": {
    "duration_seconds": 8.0,
    "resolution": { "width": 1920, "height": 1080 },
    "frame_rate": 30,
    "has_audio": false,
    "codecs": {
      "mp4": "h264",
      "webm": "vp9"
    }
  },

  "integrity": {
    "sha256_mp4": "<paste sha256 here>",
    "sha256_webm": "<paste sha256 here if present>"
  },

  "accessibility": {
    "is_decorative": true,
    "flashing_risk": "none",
    "recommended_overlay": "High-contrast text + optional gradient scrim"
  }
}
```

> [!TIP]
> If a hero video is generated (e.g., composited, stylized, or AI-assisted), record that in `description` and/or a `provenance` block (inputs/tools/settings). KFM’s culture is **evidence-first** and **traceable**.

---

## 🖼️ Posters & fallbacks (REQUIRED)

Hero video must have a static poster for:
- slow connections 📶
- browsers that block autoplay 🎚️
- users with **reduced motion** enabled ♿

### ✅ Requirements
- Provide **WebP poster**: `*.poster.webp`
- Provide **JPEG fallback**: `*.poster.jpg`
- Posters should be visually consistent with the loop (same “moment”)

---

## 🧰 Encoding recipes (FFmpeg)

> [!NOTE]
> We store **final** encoded assets here. Keep raw source footage elsewhere (don’t bloat the repo).

### 🎞️ MP4 (H.264) baseline (recommended)
Good compatibility across browsers.

```bash
ffmpeg -i input.mov \
  -an \
  -vf "scale=1920:-2:flags=lanczos,format=yuv420p" \
  -r 30 \
  -c:v libx264 -preset slow -crf 23 \
  -movflags +faststart \
  kfm-hero-prairie-v1.mp4
```

### 🎞️ Optional WebM (VP9) (smaller for some clients)
```bash
ffmpeg -i input.mov \
  -an \
  -vf "scale=1920:-2:flags=lanczos,format=yuv420p" \
  -r 30 \
  -c:v libvpx-vp9 -b:v 0 -crf 33 -row-mt 1 \
  kfm-hero-prairie-v1.webm
```

### 🖼️ Poster frame extraction
```bash
ffmpeg -ss 00:00:01 -i kfm-hero-prairie-v1.mp4 -vframes 1 kfm-hero-prairie-v1.poster.jpg
```

Convert to WebP (if `cwebp` is available):
```bash
cwebp -q 82 kfm-hero-prairie-v1.poster.jpg -o kfm-hero-prairie-v1.poster.webp
```

### 🔐 Integrity hashes (paste into `.meta.json`)
```bash
sha256sum kfm-hero-prairie-v1.mp4
sha256sum kfm-hero-prairie-v1.webm
```

---

## 🧩 How to use in HTML/React

### ✅ HTML example (progressive enhancement)
```html
<video
  class="HeroVideo"
  autoplay
  muted
  loop
  playsinline
  preload="metadata"
  poster="/assets/media/video/hero/kfm-hero-prairie-v1.poster.webp"
>
  <source src="/assets/media/video/hero/kfm-hero-prairie-v1.webm" type="video/webm" />
  <source src="/assets/media/video/hero/kfm-hero-prairie-v1.mp4" type="video/mp4" />
  <!-- Fallback text (older browsers) -->
  Your browser does not support HTML5 video.
</video>
```

> [!IMPORTANT]
> Never autoplay audio 🔇  
> Background hero video should be **muted** and **looping** (or disabled entirely when reduced motion is set).

---

## ♿ Accessibility & motion safety

### ✅ Respect `prefers-reduced-motion`
If a user asks for reduced motion, show the poster and skip the video.

```css
@media (prefers-reduced-motion: reduce) {
  .HeroVideo {
    display: none;
  }
  .HeroPoster {
    display: block;
  }
}
```

### ✅ Avoid risky motion
- No flashing or strobing 🚫
- Avoid rapid cuts
- Prefer slow pans / subtle motion
- Keep overlays readable (use a gradient scrim if needed)

---

## 🚀 Performance budget

Target constraints (practical defaults):
- **Duration:** 6–12 seconds loop ⏱️
- **No audio track:** always 🧼
- **File size:** aim **≤ 5 MB** (hard cap: **≤ 10 MB**) 📦
- **Resolution:** 1920×1080 max (consider 1280×720 if it still looks good) 🖥️📱
- **Preload:** `metadata` (don’t download full video before first paint)

---

## ✅ QA checklist (before merge)

- [ ] MP4 plays in Chrome/Firefox/Safari (desktop + mobile if possible)
- [ ] Video is **muted**, loops cleanly, no jarring seam
- [ ] Poster exists (`.webp` + `.jpg`)
- [ ] `prefers-reduced-motion` shows poster (no video)
- [ ] `.meta.json` exists and includes license + attribution + hashes
- [ ] No questionable rights / unknown source
- [ ] File size is within budget
- [ ] Hero text remains readable over the footage (contrast test)

---

## 📜 Licensing & attribution (non-negotiable)

KFM is provenance-first. That includes UI media. ✅

### Rules
- Only commit assets with **clear usage rights**
- Include **SPDX** identifier when possible (e.g., `CC0-1.0`, `CC-BY-4.0`, `MIT`, etc.)
- Put **human attribution text** in `license.attribution`
- Add `source_url` whenever available
- If license is unclear → **do not add the asset**

Optional: maintain a roll-up `ATTRIBUTION.md` in this folder for quick human review.

---

## 🤝 Contributing a new hero video (quick steps)

1. 🎥 Choose/create footage that fits KFM tone (calm, grounded, Kansas-centric)
2. 🧰 Encode web versions (`.mp4` required, `.webm` optional)
3. 🖼️ Generate posters (`.webp` + `.jpg`)
4. 🔐 Compute SHA256 hashes and fill `*.meta.json`
5. 🧪 Run the QA checklist above
6. ✅ Open a PR with the assets + metadata

---

## 🔗 Related project docs (good context)

- 📘 `docs/MASTER_GUIDE_v13.md` — provenance-first & evidence-first expectations  
- ⚖️ `docs/governance/` — ethics, sovereignty, review gates  
- 🌐 `schemas/ui/` — UI contracts (if/when we formalize media manifests)

---
