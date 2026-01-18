# 🎵 Web Music Assets (KFM)  
![Asset](https://img.shields.io/badge/asset-music-blue) ![Target](https://img.shields.io/badge/target-web-informational) ![Provenance](https://img.shields.io/badge/provenance-required-success) ![License](https://img.shields.io/badge/license-track--level-important) ![Formats](https://img.shields.io/badge/formats-ogg%20%7C%20mp3%20%7C%20wav-lightgrey)

Welcome to **`web/assets/media/audio/music/`** 🎧  
This folder holds **music tracks** used by the Kansas Frontier Matrix (KFM) web experience—ambient beds, themes, stingers, and UI-friendly loops that support the “living atlas” feel without compromising **performance**, **accessibility**, or **provenance-first** principles.

> [!IMPORTANT]
> KFM is built on **provenance-first** thinking: every asset must be traceable, auditable, and properly licensed—**including music**. Treat audio like any other “data layer”: it needs metadata, attribution, and a clear processing trail. 🧾✨

---

## 🧭 What belongs here?

Use this directory for **music** (not one-shot sound effects).

✅ Good fits:
- 🌾 **Ambient loops** (prairie wind, subtle pads, atmospheric beds)
- 🗺️ **Theme tracks** (menu/home, mode themes)
- ⚡ **Stingers** (short transitions, success/focus cues)
- 🧠 **Focus Mode beds** (subtle, non-distracting, low dynamics)

🚫 Not here:
- 🔊 UI SFX (clicks, pops) → use `../sfx/` (or create it if missing)
- 🎙️ Voiceover narration → use `../voice/` (or create it if missing)
- 🧪 Raw project files intended for DAWs only (keep those in `_src/` and/or Git LFS)

---

## 🽃 Recommended folder layout 📁

```text
web/
└── assets/
    └── media/
        └── audio/
            └── music/
                ├── ambient/        # long loops, subtle soundscapes 🌬️
                ├── themes/         # main themes + mode themes 🗺️
                ├── stingers/       # short transitions ⚡
                ├── ui/             # gentle UI music beds (not SFX) 🧩
                ├── _src/           # OPTIONAL: masters/stems (WAV), not shipped 🚫📦
                ├── LICENSES/       # per-track license + attribution 🧾
                ├── manifest.json   # canonical metadata index 📇
                └── README.md       # you are here 👋
```

> [!NOTE]
> If you don’t want to ship masters/stems, keep `_src/` out of production builds and/or use Git LFS.

---

## 🎚️ Supported formats & export targets

### ✅ Ship formats (web-friendly)
- **`.ogg`** (preferred where supported): good quality/size balance
- **`.mp3`** (fallback): broadest support

### ✅ Source format (authoring/master)
- **`.wav`** (48kHz recommended)

### Suggested export settings
- **Sample rate:** 48kHz (or 44.1kHz if project-wide standard)
- **Bit depth (source):** 24-bit WAV
- **Loudness target (music):** ~ **-14 LUFS integrated** (streaming-friendly baseline)
- **True peak:** ≤ **-1.0 dBTP** (avoid inter-sample clipping)
- **Loops:** ensure clean loop points (no clicks/pops)

> [!WARNING]
> Avoid hyper-compressed masters. KFM’s UI should feel calm, not exhausting. Keep dynamic range reasonable.

---

## 🏷️ Naming convention (stable + human-readable)

Use **kebab-case**, include intent, and keep it consistent:

**Pattern**
```text
<category>--<slug>--v<major>.<minor>.<patch>.<ext>
```

**Examples**
```text
ambient--prairie-dawn--v1.0.0.ogg
themes--kfm-main--v2.1.0.mp3
stingers--mode-enter-focus--v1.0.0.ogg
```

### 🔒 Stable identifiers (don’t break references)
- UI code should reference a **stable `id`** from `manifest.json`, not the filename.
- Filenames can change; **IDs should not**. Prefer UUIDs or deterministic IDs.

> [!TIP]
> This mirrors “stable identifier” thinking: identifiers should be **unique, invariant, and information-free** where possible. ✅

---

## 🗂️ `manifest.json` (required)

`manifest.json` is the canonical index so the web app can load tracks by **stable ID**, and so humans can audit provenance.

### Minimal schema (recommended)
```json
[
  {
    "id": "music_ambient_prairie_dawn_01",
    "title": "Prairie Dawn",
    "category": "ambient",
    "mood": ["calm", "spacious"],
    "loop": true,
    "duration_sec": 96.0,
    "files": {
      "ogg": "ambient/ambient--prairie-dawn--v1.0.0.ogg",
      "mp3": "ambient/ambient--prairie-dawn--v1.0.0.mp3"
    },
    "license": {
      "spdx": "CC-BY-4.0",
      "attribution_file": "LICENSES/music_ambient_prairie_dawn_01.md"
    },
    "provenance": {
      "source": "Original composition",
      "creator": "KFM Team / Contributor Handle",
      "created_utc": "2026-01-18T00:00:00Z",
      "processing": [
        "Mastered to -14 LUFS",
        "True peak limited to -1.0 dBTP",
        "Exported OGG q=5 and MP3 192k"
      ],
      "hashes": {
        "ogg_sha256": "…",
        "mp3_sha256": "…"
      }
    },
    "tags": ["kansas", "atlas", "focus-mode"]
  }
]
```

> [!IMPORTANT]
> **Every track must have a license and attribution file**, even if it’s “original”. (Original ≠ automatically licensed for reuse by everyone.)

---

## ✅ Add-a-track checklist (PR-ready)

- [ ] Export **OGG** + **MP3** (or justify why not)
- [ ] Add/update **`manifest.json`**
- [ ] Add **per-track attribution** in `LICENSES/<id>.md`
- [ ] Confirm loop quality (no clicks), and verify peak/loudness targets
- [ ] Keep file sizes reasonable (prefer < ~5MB per typical loop)
- [ ] No copyrighted/commercial tracks without explicit permission ✅
- [ ] Confirm UX: **no autoplay** unless explicitly user-enabled 🔇➡️🔊

---

## ⚡ Performance + UX guidelines (web)

- 🎯 **Lazy-load** music: don’t preload everything.
- 🧠 Prefer Web Audio API for smooth fades and mixing; fallback to `<audio>` is OK.
- 📴 Respect offline constraints (service worker caching if used).
- 🔇 Always provide a clear **mute/volume** control.
- 🧍 Accessibility: respect user settings and avoid surprise sound.

> [!NOTE]
> If the UI has “Focus Mode”, default to **silent** unless the user opts in. Advisory-first UX applies to media too.

---

## 🧪 Quick QC helpers (optional but recommended)

### ffmpeg conversion examples
```bash
# WAV -> OGG (quality-based)
ffmpeg -i input.wav -c:a libvorbis -q:a 5 output.ogg

# WAV -> MP3 (CBR-ish)
ffmpeg -i input.wav -c:a libmp3lame -b:a 192k output.mp3
```

### Inspect audio metadata
```bash
ffprobe -hide_banner -show_format -show_streams "ambient/ambient--prairie-dawn--v1.0.0.ogg"
```

### Python sanity checks (clipping / peak scan)
```python
# requires: numpy, soundfile (or librosa), optional scipy
import numpy as np
import soundfile as sf

x, sr = sf.read("your_track.wav")
peak = np.max(np.abs(x))
print("sr:", sr, "peak:", peak)
if peak >= 1.0:
    print("⚠️ potential clipping detected")
```

---

## 🧾 Licensing & attribution rules

**Rule of thumb:** if you can’t clearly explain the license, we can’t ship it.

Each `LICENSES/<track-id>.md` should include:
- Track title
- Creator / contributor
- License (SPDX if possible)
- Required attribution text
- Source link (if external)
- Notes on edits/processing

---

## 📚 Project references (design & tooling foundations)

These documents strongly influence how we treat assets in KFM (traceability, stable IDs, tooling, performance, and maintainability):

- KFM vision & provenance-first principles 🧭  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- Flexibility mindset + stable identifiers 🧱  [oai_citation:1‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)  
- Practical performance thinking (applies to asset loading/caching) 🚀  [oai_citation:2‡Database Performance at Scale.pdf](file-service://file-36z8qyiVJRtrSs6QG7Epen)  
- Scientific Python + signal processing foundations 🐍📈  [oai_citation:3‡S-T programming Books.pdf](file-service://file-NT32tqqzGW9RvfcNZmMH1K)  
- MATLAB tooling patterns (optional workflows) 📊  [oai_citation:4‡M-N programming Books.pdf](file-service://file-EYCp5md89QY2cy5PCYS18e)  
- Bash for batch conversion/automation 🧰  [oai_citation:5‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ)  
- ML foundations (future: tagging/embeddings for audio search) 🤖  [oai_citation:6‡U-X programming Books.pdf](file-service://file-3hYtSGHtHmb6wyTtavym6M)  
- Supporting “systems thinking” across the project stack 🧠  [oai_citation:7‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a)  
- Native/mobile considerations if we ship companion apps 📱  [oai_citation:8‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)  
- Spatial storytelling inspiration (how media supports interpretation) 🏺🗺️  [oai_citation:9‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  

---

## 🌟 Optional future upgrades (nice-to-have)
- 📇 Auto-generated `manifest.json` validator (CI)
- 🔐 Automatic SHA256 hashing + size budgets in pre-commit
- 🌊 Waveform previews (`.png`) for quick review
- 🧭 “Soundscape layers” mapped to regions/time (Kansas seasons, biomes)

—  
**Keep it calm. Keep it traceable. Keep it lightweight.** 🎧🌾
