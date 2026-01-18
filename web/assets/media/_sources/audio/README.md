# 🔊 Audio Sources (`web/assets/media/_sources/audio/`)

![KFM](https://img.shields.io/badge/KFM-media%20assets-black?style=for-the-badge)
![Asset](https://img.shields.io/badge/asset-audio-blue?style=for-the-badge)
![Provenance](https://img.shields.io/badge/policy-provenance--first-purple?style=for-the-badge)
![A11y](https://img.shields.io/badge/a11y-transcripts%20%2B%20captions-success?style=for-the-badge)

**This folder contains the _original, high-quality source audio_ used by the KFM web experience** — narration, oral-history clips, ambient/field recordings, UI sounds, and any other audio that needs to be traceable, creditable, and reproducible.

> ✅ Keep **masters** lossless and immutable  
> ✅ Every audio file must have **metadata + license + attribution**  
> ✅ Every spoken clip should ship with **transcripts/captions**  
> ❌ No “mystery clips” (unknown origin/license)  
> ❌ Don’t overwrite originals — version instead

---

## 🧭 Table of contents
- [🎯 What belongs here](#-what-belongs-here)
- [🗂 Suggested folder structure](#-suggested-folder-structure)
- [🏷 Naming conventions](#-naming-conventions)
- [🎚 Formats & quality targets](#-formats--quality-targets)
- [🧬 Metadata & provenance](#-metadata--provenance)
- [♿ Transcripts & accessibility](#-transcripts--accessibility)
- [🧾 Licensing & attribution](#-licensing--attribution)
- [🔐 Privacy & sensitive material](#-privacy--sensitive-material)
- [🛠 Build/export pipeline](#-buildexport-pipeline)
- [🌐 Web usage (HTML `<audio>` snippet)](#-web-usage-html-audio-snippet)
- [🧳 Large files (Git LFS)](#-large-files-git-lfs)
- [✅ PR checklist](#-pr-checklist)

---

## 🎯 What belongs here

This directory is for **source materials** that we want to preserve and audit:

- 🎙️ **Narration** for map stories, explainers, tours
- 🧓 **Oral history** / interview excerpts
- 🌾 **Field ambience** (wind, prairie, river, town square, etc.)
- 🖱️ **UI sounds** (clicks, hover cues, alerts) — if the UI uses them
- 🎼 **Music** (only if licensing permits and we can prove it)

**What does _not_ belong here**
- 🚫 Web-optimized exports that are generated from sources (e.g., “final.mp3” produced by the build).  
- 🚫 Temporary renders, DAW session caches, scratch mixes, etc.  
- 🚫 Any audio without a clear license or provenance trail.

---

## 🗂 Suggested folder structure

> Keep it tidy, but don’t overthink it. Start simple and evolve as needed.

```text
web/assets/media/
└─ 🧾 _sources/
   └─ 🔊 audio/
      ├─ 🎙️ narration/          # 🎙️ Raw voice-over sources for stories/explainers (masters, scripts, takes)
      ├─ 🧓 oral-history/       # 🧓 Interviews/oral-history recordings (handle consent + sensitivity carefully)
      ├─ 🌾 field/              # 🌾 On-location ambience (wind, prairie, town soundscapes, room tone)
      ├─ 🖱️ ui/                 # 🖱️ Raw UI cue sources (clicks, alerts, transitions) before optimization
      ├─ 💥 sfx/                # 💥 Generic SFX sources (licensed; track attribution + usage limits)
      ├─ 🎼 music/              # 🎼 Licensed music sources (only if approved; store license terms here)
      ├─ 🧩 _templates/         # 🧩 Metadata + transcript templates (what every asset must include)
      └─ 📄 README.md           # 📄 you are here 📌 Rules: naming, required metadata, transcripts, and licensing
```

---

## 🏷 Naming conventions

We want filenames that are:
- 🔎 searchable
- 🧾 traceable to sources
- 🧠 predictable for tooling
- 🔁 stable across edits

**Recommended pattern**
```text
kfm_<type>_<YYYY-MM-DD>_<location-or-collection>_<slug>__v###.<ext>
```

**Examples**
```text
kfm_narration_2026-01-17_statewide_intro__v001.wav
kfm_oral-history_2024-08-03_dodge-city_mary-jones_cattle-trail__v002.flac
kfm_field_2025-04-21_flint-hills_wind-grass__v001.wav
kfm_ui_2026-01-10_app_click-soft__v003.wav
```

**Notes**
- `__v###` is required once anything has shipped or been referenced externally.
- Use **kebab-case** for slugs.
- If the audio relates to a specific place, include a place tag (county, town, site, etc.).
- If it belongs to a collection/archive, use a stable collection key (e.g., `kshs`, `loc`, `usgs`, `local-museum`).

---

## 🎚 Formats & quality targets

### ✅ Source/master formats (preferred)
- **WAV** (PCM) — recommended master
  - Sample rate: **48 kHz**
  - Bit depth: **24-bit** (or 16-bit if that’s all you have)
- **FLAC** — acceptable master if you want smaller files without quality loss

### ✅ Web formats (generated outputs)
- **MP3** (VBR) for broad compatibility
- **Opus (Ogg/WebM)** if we want modern compression with excellent speech quality

> ⚠️ Keep masters **lossless** in `_sources/`.  
> Web formats should be generated to the “runtime” assets folder (see pipeline section).

### 🎛 Loudness & peaks (guidelines)
- Spoken narration target: **~ -16 LUFS** (web/podcast-friendly)
- True peak ceiling: **-1 dBTP**
- Avoid clipping, excessive noise reduction, or harsh compression on masters.

---

## 🧬 Metadata & provenance

KFM is **provenance-first**: audio should follow the same spirit as datasets — **no unsourced assets**.

### 📄 Sidecar metadata file

For every audio file, add a sidecar file with the same base name:

```text
kfm_field_2025-04-21_flint-hills_wind-grass__v001.wav
kfm_field_2025-04-21_flint-hills_wind-grass__v001.meta.json
```

### ✅ Minimum required fields

| Field | Required | Example |
|---|---:|---|
| `id` | ✅ | `kfm_field_2025-04-21_flint-hills_wind-grass__v001` |
| `title` | ✅ | `Flint Hills — Wind in Tallgrass` |
| `type` | ✅ | `field`, `narration`, `oral-history`, `ui`, `sfx`, `music` |
| `license.spdx` | ✅ | `CC-BY-4.0` |
| `source` | ✅ | `{ "collector": "...", "url": "...", "archive_ref": "..." }` |
| `recorded_at` | ✅ (if known) | `2025-04-21T18:32:00Z` |
| `checksums.sha256` | ✅ | `...` |
| `provenance[]` | ✅ | digitized/edited/export steps |

### 🧩 Example `*.meta.json`

```json
{
  "id": "kfm_field_2025-04-21_flint-hills_wind-grass__v001",
  "title": "Flint Hills — Wind in Tallgrass",
  "type": "field",
  "language": "zxx",
  "recorded_at": "2025-04-21T18:32:00Z",

  "location": {
    "name": "Flint Hills, KS",
    "lat": 38.5000,
    "lon": -96.5000
  },

  "source": {
    "collector": "KFM Field Team",
    "original_medium": "Zoom H5",
    "notes": "Recorded at dusk, light wind, minimal insects."
  },

  "license": {
    "spdx": "CC-BY-4.0",
    "holder": "Kansas Frontier Matrix Contributors",
    "proof": "docs/legal/audio/kfm_field_2025-04-21_flint-hills_wind-grass__v001.md"
  },

  "provenance": [
    {
      "step": "record",
      "tool": "Zoom H5",
      "when": "2025-04-21T18:32:00Z",
      "by": "KFM Field Team"
    },
    {
      "step": "trim",
      "tool": "Audacity",
      "when": "2025-04-22T02:10:00Z",
      "by": "kfm-user",
      "notes": "Removed handling noise at start/end. No EQ/compression."
    }
  ],

  "checksums": {
    "sha256": "REPLACE_WITH_REAL_SHA256"
  },

  "transcripts": [],
  "usage": {
    "story_ids": [],
    "map_layer_ids": []
  }
}
```

<details>
  <summary><strong>✨ Tip: treat audio metadata like a “mini data contract”</strong></summary>

If the clip is used in a story or map experience, populate:
- `usage.story_ids`
- `usage.map_layer_ids`
- any citations/links in `source`

This keeps the web layer auditable and makes building credits/attribution lists much easier.
</details>

---

## ♿ Transcripts & accessibility

If the clip includes **speech**:
- Provide a **WebVTT** captions file (`.vtt`) for the web
- Optionally provide `.srt`
- Provide a readable transcript (`.md`) if helpful for editing/review

**Naming**
```text
kfm_oral-history_2024-08-03_dodge-city_mary-jones_cattle-trail__v002.wav
kfm_oral-history_2024-08-03_dodge-city_mary-jones_cattle-trail__v002.en.vtt
kfm_oral-history_2024-08-03_dodge-city_mary-jones_cattle-trail__v002.transcript.md
```

**Transcript tips**
- Include speaker labels when there are multiple voices
- Note redactions like `[REDACTED]` if needed
- Include time ranges if you expect re-cuts

---

## 🧾 Licensing & attribution

We only ship audio we can **legally use** and **properly credit**.

### ✅ Do
- Use SPDX license identifiers (e.g., `CC0-1.0`, `CC-BY-4.0`, `CC-BY-SA-4.0`)
- Store proof/notes in `docs/legal/...` (or your project’s equivalent)
- Credit:
  - performer/narrator
  - recordist/collector
  - archive/source institution (if applicable)

### ❌ Don’t
- Don’t include “All Rights Reserved” assets unless we have explicit written permission
- Don’t rely on “I found it on the internet” as a source
- Don’t remove embedded credits if they’re required by license

---

## 🔐 Privacy & sensitive material

Audio can contain personal data.

- 🧑‍⚖️ Ensure consent for interviews/oral histories (especially if identifiable)
- 🧭 Be careful with precise locations tied to sensitive subjects
- 🩹 If redaction is required, keep:
  - the original in a protected place (if policy allows)
  - a redacted public version with clear provenance notes

---

## 🛠 Build/export pipeline

**Goal:** keep `_sources/` clean and immutable, generate runtime assets elsewhere.

```mermaid
flowchart LR
  A[🎙️ Record / Acquire] --> B[📁 Put master in _sources/audio]
  B --> C[🧬 Add .meta.json + license proof]
  C --> D[♿ Add .vtt / transcript for speech]
  D --> E[⚙️ Build step: transcode + normalize (web targets)]
  E --> F[🌐 Runtime assets folder (e.g., web/assets/media/audio)]
  F --> G[🗺️ Story / Map UI consumes audio + captions]
```

### 🔧 Handy `ffmpeg` examples (web exports)

**WAV → MP3 (VBR, good quality)**
```bash
ffmpeg -i input.wav -c:a libmp3lame -q:a 2 output.mp3
```

**WAV → Opus**
```bash
ffmpeg -i input.wav -c:a libopus -b:a 96k output.opus
```

**Loudness normalization (spoken audio)**
```bash
ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1:LRA=11 output_norm.wav
```

> ⚠️ Keep normalization and compression out of masters when possible — prefer generating “listening mixes” or runtime formats.

---

## 🌐 Web usage (HTML `<audio>` snippet)

If you’re wiring audio into a page/component, this is the standard pattern:

```html
<audio controls preload="metadata">
  <source src="/assets/media/audio/example.opus" type="audio/ogg; codecs=opus">
  <source src="/assets/media/audio/example.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
```

---

## 🧳 Large files (Git LFS)

Audio masters can get big fast. If the repo isn’t already using Git LFS, consider it for:

- `*.wav`
- `*.flac`
- `*.aif` / `*.aiff`

Example `.gitattributes`:
```gitattributes
*.wav filter=lfs diff=lfs merge=lfs -text
*.flac filter=lfs diff=lfs merge=lfs -text
*.aif filter=lfs diff=lfs merge=lfs -text
*.aiff filter=lfs diff=lfs merge=lfs -text
```

---

## ✅ PR checklist

Before merging new audio sources:

- [ ] File is in the right folder (`narration/`, `field/`, `ui/`, etc.)
- [ ] Filename follows the naming convention (+ `__v###`)
- [ ] Sidecar metadata exists (`*.meta.json`)
- [ ] License is clear and auditable (proof linked or included)
- [ ] Captions/transcript included for speech (`.vtt` preferred)
- [ ] No sensitive/private data leaked
- [ ] Runtime exports (if committed) match the build pipeline expectations

---

💡 **If you’re unsure:** default to **over-documenting** the source and license. Provenance is the feature. 🧭
