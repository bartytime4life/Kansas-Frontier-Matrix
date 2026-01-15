# 🎞️ Video Assets

![Path](https://img.shields.io/badge/path-web%2Fassets%2Fmedia%2Fvideo-2b2b2b)
![Scope](https://img.shields.io/badge/scope-web%20ui-1f6feb)
![Media](https://img.shields.io/badge/media-video-ff4d8d)
![Principle](https://img.shields.io/badge/principle-provenance--first-2ea043)

> **Folder:** `web/assets/media/video/`  
> **Purpose:** Web-deliverable videos used by the KFM frontend (marketing loops, UI walkthroughs, demo clips). 🎬

---

## 🚦 What belongs here

✅ **UI-facing videos** that ship with the frontend bundle, for example:

- Landing / hero background loops (muted) 🌄  
- Short feature demos (layer toggling, timeline scrub, etc.) 🗺️  
- Onboarding / tutorial walkthroughs 🎓  
- Release highlight clips for README / docs landing pages 📣

---

## 🧾 What does **not** belong here

❌ **Evidence media** used to support Story Nodes / Focus Mode claims (archival footage, documentary clips, “this proves X” videos).

If a video is **evidence**, treat it like a governed artifact:
- Store it in the data pipeline (`data/raw/ → data/work/ → data/processed/`)
- Register provenance + metadata (STAC/DCAT/PROV)
- Deliver through the **API layer** (so redaction/classification rules can be enforced)

> ⚠️ Rule of thumb: **If the UI needs governance controls**, don’t bake it into `web/assets/`.

---

## ✅ Quick rules

- **Web-ready only:** Export + compress before commit (no raw screen captures).
- **Don’t overwrite:** Treat filenames as immutable once referenced publicly. Version bump instead.
- **Add a poster:** Provide a thumbnail/poster image for every video.
- **Add captions:** If there’s speech, add `.vtt` captions (accessibility + search).
- **Keep it small:** Prefer short clips + reasonable bitrates to avoid bloating frontend deploys.
- **No sensitive data:** Don’t publish anything that leaks private keys, tokens, PII, or restricted locations/data.

---

## 📁 Suggested structure

Use subfolders by intent so the UI can reference predictably:

```text
📁 web/assets/media/video/
├─ 📄 README.md
├─ 🎞️ hero/            # muted loops, background video
├─ 🎬 demos/            # short feature demos (UI behavior)
├─ 🎓 tutorials/        # longer walkthroughs + captions
└─ 🧪 sandbox/          # temporary clips (avoid committing if possible)
```

---

## 🏷️ Naming conventions

Keep names sortable + stable + grep-friendly:

**Pattern**
```text
kfm__<category>__<slug>__YYYY-MM-DD__vNN.<ext>
```

**Examples**
```text
kfm__hero__prairie_timelapse__2026-01-15__v01.mp4
kfm__demo__timeline_scrub__2026-01-15__v02.webm
kfm__tutorial__focus_mode_walkthrough__2026-01-15__v01.mp4
```

**Guidelines**
- Use **lowercase** + **underscores**
- Keep the slug short but descriptive
- Increment `vNN` when content changes (even small edits)

---

## 📦 Required companion files

For every video, aim to ship a small “bundle”:

| File | Required | Why |
|---|---:|---|
| `… .mp4` | ✅ | Broad browser support |
| `… .webm` | ⭐ Optional | Smaller downloads in modern browsers |
| `… .webp` or `… .jpg` (poster) | ✅ | Faster page load + better UX |
| `… .vtt` (captions) | ✅ if speech | Accessibility + search |
| `… .meta.yml` | ✅ | Provenance + license + attribution |

⭐ Optional but recommended

---

## 🧬 Minimal metadata sidecar

Create a YAML sidecar next to the video (same basename):

**Example**
```yaml
# kfm__demo__timeline_scrub__2026-01-15__v02.meta.yml
id: kfm.web.video.demo.timeline_scrub.2026-01-15.v02
title: "Timeline scrub demo"
type: ui_demo          # ui_demo | tutorial | hero_loop | release_clip
created: 2026-01-15
created_by: "@your-handle"
license: "CC-BY-4.0"   # or project default / internal note
attribution: "Kansas Frontier Matrix contributors"
notes: >
  Recorded on local dev build. No restricted datasets shown.
provenance:
  kind: screen_recording
  repo_commit: "<commit-sha>"
  datasets_referenced:
    - "<stac_item_or_dataset_id_if_applicable>"
renditions:
  mp4: "kfm__demo__timeline_scrub__2026-01-15__v02.mp4"
  webm: "kfm__demo__timeline_scrub__2026-01-15__v02.webm"
  poster: "kfm__demo__timeline_scrub__2026-01-15__v02.webp"
  captions_en: "kfm__demo__timeline_scrub__2026-01-15__v02.en.vtt"
```

> 💡 Keep this light. The goal is quick provenance + license clarity for UI assets.

---

## 🛠️ ffmpeg recipes

<details>
<summary><strong>MP4 (H.264) export</strong> ✅</summary>

```bash
ffmpeg -i input.mov \
  -c:v libx264 -pix_fmt yuv420p -preset slow -crf 23 \
  -movflags +faststart \
  -c:a aac -b:a 128k \
  output.mp4
```

**Notes**
- `+faststart` enables faster playback start in browsers (moov atom first)
- `crf 20–28` is a reasonable range depending on content
</details>

<details>
<summary><strong>WEBM (VP9) export</strong> ⭐</summary>

```bash
ffmpeg -i input.mov \
  -c:v libvpx-vp9 -b:v 0 -crf 33 \
  -row-mt 1 -threads 8 \
  -c:a libopus -b:a 96k \
  output.webm
```
</details>

<details>
<summary><strong>Muted loop (hero background)</strong> 🎞️</summary>

```bash
ffmpeg -i input.mov \
  -an \
  -c:v libx264 -pix_fmt yuv420p -preset slow -crf 24 \
  -movflags +faststart \
  output.mp4
```

Tip: keep hero loops **short** (5–12s) and seamless.
</details>

<details>
<summary><strong>Poster frame</strong> 🖼️</summary>

```bash
ffmpeg -i output.mp4 -ss 00:00:01.000 -frames:v 1 poster.webp
```
</details>

---

## 🧩 Referencing videos in the frontend

Use `<video>` with multiple sources so the browser can choose the best format:

```html
<video
  controls
  preload="metadata"
  poster="/assets/media/video/demos/kfm__demo__timeline_scrub__2026-01-15__v02.webp"
>
  <source
    src="/assets/media/video/demos/kfm__demo__timeline_scrub__2026-01-15__v02.webm"
    type="video/webm"
  />
  <source
    src="/assets/media/video/demos/kfm__demo__timeline_scrub__2026-01-15__v02.mp4"
    type="video/mp4"
  />
  <track
    kind="captions"
    src="/assets/media/video/demos/kfm__demo__timeline_scrub__2026-01-15__v02.en.vtt"
    srclang="en"
    label="English"
    default
  />
</video>
```

**For autoplay background loops**
- Add `muted autoplay loop playsinline`
- Browsers generally block autoplay **unless muted**

---

## 🔍 Review checklist

Before merging a new video:

- [ ] File is **optimized** (not raw capture)
- [ ] Filename follows the naming pattern
- [ ] Poster image exists and looks good
- [ ] Captions included if any speech
- [ ] `.meta.yml` includes license + attribution
- [ ] No sensitive info (tokens, PII, restricted locations/datasets)
- [ ] If it’s evidence for Story Nodes / Focus Mode → **migrate to governed pipeline** (don’t ship as UI asset)

---

## 🔗 Related docs

- 📘 Master guide / pipeline rules: `docs/MASTER_GUIDE_v13.md` (or latest)
- 🧾 STAC/DCAT/PROV profiles: `docs/standards/`
- 🧠 Story Nodes templates: `docs/templates/`

> 🧭 If any of the above paths differ in the current repo, update this section to match the canonical locations.
