# 🎬 Video Sandbox (`web/assets/media/video/sandbox`)

[⬅️ Back to project README](../../../../../README.md)

![Status](https://img.shields.io/badge/status-sandbox-orange)
![Scope](https://img.shields.io/badge/scope-web%20ui-blue)
![Principle](https://img.shields.io/badge/provenance-first-brightgreen)
![A11y](https://img.shields.io/badge/accessibility-captions%20recommended-informational)

> [!WARNING]
> This folder is a **sandbox** 🧪 — it’s for fast iteration and UI experiments.  
> **Do not treat these assets as stable, “published,” or provenance-complete** until they pass the **Promotion Gate** ✅ (see below).

---

## 🎯 Purpose

This directory holds **experimental video assets** used for:
- UI/UX prototypes 🎛️
- screen recordings of features in progress 🖥️
- quick demos for PRs/issues 🧩
- motion studies (map transitions, 2D↔3D swaps, timeline scrubbing) 🗺️⏱️
- “rough cut” story visualizations before moving into governed narrative assets 📚

---

## 📦 What belongs here (and what doesn’t)

| ✅ Put here | ❌ Don’t put here |
|---|---|
| short, web-friendly `.mp4` demos | raw captures like `.mov` / uncompressed masters |
| lightweight loops for UI motion tests | sensitive location footage or anything needing redaction |
| “draft” videos tied to an issue/PR | licensed/copyrighted material you can’t redistribute |
| videos with a basic sidecar metadata file | “mystery videos” with no source/author/license info |

> [!TIP]
> If a video is **meant to be a governed narrative/story asset**, it probably belongs under **Story Node assets** (see: `docs/reports/story_nodes/**/assets/`) rather than here. 🧭

---

## 🗂️ Expected layout

```text
web/
└─ 📁 assets/
   └─ 🎞️ media/
      └─ 🎞️ video/
         └─ 🧪 sandbox/                                  # 🧪 Staging area for WIP clips (not guaranteed shipped)
            ├─ 📄 README.md                               # 📘 Rules for sandbox videos: naming, size/codec, promotion path
            ├─ 🎞️ kfm_ui_scrub_demo_20260117_v01_1280x720.mp4
            │     # Primary clip (web-optimized MP4; keep short, mute-safe if possible)
            ├─ 🖼️ kfm_ui_scrub_demo_20260117_v01_1280x720.poster.jpg
            │     # Poster/thumbnail frame used in catalogs/players before playback
            ├─ ♿📝 kfm_ui_scrub_demo_20260117_v01_1280x720.en.vtt
            │     # Captions (preferred): language-tagged WebVTT for accessibility/search
            └─ 🧾 kfm_ui_scrub_demo_20260117_v01_1280x720.meta.json
                  # Sidecar contract: title, description, duration, source/provenance, license, checksums, tags
```

### 🎞️ Asset bundle convention (recommended)
For each video, try to include:
- `*.mp4` ✅ (web-playable)
- `*.poster.jpg` ✅ (preview image)
- `*.en.vtt` ✅ (captions/subtitles — strongly recommended)
- `*.meta.json` ✅ (provenance + intent + license)

---

## 🏷️ Naming conventions (cache-friendly)

Use **lower_case_with_underscores** and include enough info to avoid collisions:

**Pattern**
```text
kfm_<topic>_<yyyymmdd>_vNN_<width>x<height>.<ext>
```

**Examples**
```text
kfm_ui_scrub_demo_20260117_v01_1280x720.mp4
kfm_map_fade_test_20260117_v02_1920x1080.mp4
kfm_focusmode_walkthrough_20260117_v01_1920x1080.en.vtt
```

> [!NOTE]
> Version/date-in-filename helps with **cache busting** and keeps iteration history obvious. 🧠

---

## 🧾 Sidecar metadata (`*.meta.json`) 🧬

Even in sandbox, add **minimal provenance** so the asset isn’t a black box.

### Minimum fields (sandbox)
- `id` (stable-ish identifier)
- `title`
- `created_at` (ISO 8601)
- `created_by`
- `source` (what you recorded / where content came from)
- `license` (or “internal-only” if not shareable)
- `sensitivity` (`public` / `internal` / `restricted`)
- `related` (issue/PR/commit)

### Example
```json
{
  "id": "kfm.web.video.ui_scrub_demo.2026-01-17.v01",
  "title": "UI scrub interaction demo (sandbox)",
  "description": "Prototype capture for timeline scrubbing + map layer fade behavior.",
  "created_at": "2026-01-17T00:00:00Z",
  "created_by": "YOUR_NAME_OR_HANDLE",
  "source": {
    "type": "screen_recording",
    "environment": "local-dev",
    "recorded_from": {
      "app": "web",
      "route": "/focus-mode",
      "git_commit": "REPLACE_WITH_COMMIT_SHA"
    }
  },
  "license": "CC-BY-4.0 OR INTERNAL-ONLY",
  "sensitivity": "internal",
  "processing": [
    {
      "step": "transcode_for_web",
      "tool": "ffmpeg",
      "notes": "H.264 + AAC, faststart enabled"
    }
  ],
  "related": {
    "issue": "REPLACE_WITH_ISSUE_OR_LINK",
    "pull_request": "REPLACE_WITH_PR_OR_LINK"
  },
  "notes": ["sandbox", "not_governed", "not_cataloged"]
}
```

---

## 🎚️ Encoding guidance (web-first)

### ✅ Preferred delivery format
- **MP4 (H.264 video + AAC audio)** for broad browser support
- keep it short + light: UI demos are better as **10–30s** clips than 3-minute recordings

### 🔧 Suggested ffmpeg commands

**Transcode to web-friendly MP4 (720p)**
```bash
ffmpeg -i input.mov \
  -vf "scale=-2:720" \
  -c:v libx264 -preset medium -crf 23 \
  -c:a aac -b:a 128k \
  -movflags +faststart \
  kfm_demo_20260117_v01_1280x720.mp4
```

**Extract a poster frame**
```bash
ffmpeg -ss 00:00:01 -i kfm_demo_20260117_v01_1280x720.mp4 \
  -frames:v 1 \
  kfm_demo_20260117_v01_1280x720.poster.jpg
```

> [!TIP]
> `-movflags +faststart` moves MP4 metadata to the front so the video starts faster on the web 🚀

---

## 🧩 Using videos in the UI (HTML5)

### Basic embed
```html
<video
  controls
  preload="metadata"
  width="640"
  height="360"
  poster="/assets/media/video/sandbox/kfm_demo_20260117_v01_1280x720.poster.jpg"
>
  <source
    src="/assets/media/video/sandbox/kfm_demo_20260117_v01_1280x720.mp4"
    type="video/mp4"
  />

  <track
    kind="captions"
    src="/assets/media/video/sandbox/kfm_demo_20260117_v01_1280x720.en.vtt"
    srclang="en"
    label="English"
    default
  />

  Sorry, your browser does not support embedded video.
</video>
```

> [!WARNING]
> Avoid `autoplay` in most cases 🙅 — it’s a UX footgun and often blocked by browsers.

---

## ♿ Accessibility expectations

Even in sandbox:
- captions (`.vtt`) are **strongly recommended** 📝
- avoid flashing content; keep camera motion reasonable
- ensure any important on-screen text is readable at 720p
- if you narrate, consider adding a quick transcript in the `.meta.json` or a sibling `*.transcript.md`

---

## 🔒 Safety, privacy, and sensitive content

KFM’s broader project posture includes **sensitivity tagging** and guardrails. Apply the same thinking to videos:

**Do not commit videos that include:**
- personal data (emails, phone numbers, faces without consent) 🕵️
- API keys, tokens, credentials 🔑
- exact sensitive locations (archaeological sites, endangered species habitats, etc.) 🧭

If you must demonstrate something sensitive:
- blur/redact in the video
- set `"sensitivity": "restricted"`
- keep it out of public builds/releases

---

## ✅ Promotion Gate (Sandbox ➜ Production)

When a video is ready to be “real” (used in docs, Story Nodes, marketing, or shipped UI):
1. **Move** it out of `sandbox/` into the correct stable home (docs assets vs web assets).
2. Ensure the video has:
   - ✅ clear license
   - ✅ provenance metadata (source + who made it + what it depicts)
   - ✅ captions (or an explicit exception note)
   - ✅ no sensitive content (or explicit classification + redaction)
3. Prefer exposure through the **governed pipeline** (catalog + provenance + API), not hard-coded UI references.

> [!NOTE]
> Sandbox is allowed to be scrappy. Production is not. 🧼✨

---

## 🔗 Related docs (project-level)

- 📘 `docs/MASTER_GUIDE_v13.md` (contract-first & evidence-first workflow)
- 🧾 `docs/standards/` (metadata profiles & governance)
- 🧑‍⚖️ `docs/governance/ETHICS.md` + `docs/governance/REVIEW_GATES.md`

---

## ✅ Quick checklist (copy/paste)

- [ ] File name follows convention (`kfm_<topic>_<yyyymmdd>_vNN_<res>.mp4`)
- [ ] MP4 plays in Chrome/Firefox/Safari
- [ ] Poster image exists
- [ ] Captions exist (or `.meta.json` explains why not)
- [ ] `.meta.json` includes source + license + sensitivity
- [ ] No secrets/PII/sensitive locations visible
