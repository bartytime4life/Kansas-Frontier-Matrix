# 🎧 Ambience Audio (Soundscapes)

![Asset](https://img.shields.io/badge/asset-audio-4c8bf5) ![Type](https://img.shields.io/badge/type-ambience%20%2F%20soundscape-6f42c1) ![Provenance](https://img.shields.io/badge/provenance-required-2ea44f) ![Web](https://img.shields.io/badge/target-web%20client-111111)

Ambient audio is a **non-data** layer that supports immersion while exploring Kansas in the KFM web experience. It should **never** change the interpretation of maps, analysis, or evidence—only the vibe. 🌾🌬️

> [!IMPORTANT]
> **User control comes first.**  
> Ambience must be **off by default** (or at minimum muted until a user explicitly enables it), and there must be a clear UI toggle + volume control. ♿🔇

---

## 🎯 What lives here

This folder contains **runtime-ready** ambience assets (typically seamless loops) used to build **soundscapes** like:

- 🌾 Prairie wind + grass rustle
- 🪲 Summer insects at dusk
- 🌧️ Rain on leaves / distant thunder
- 🌊 Riverbank water movement
- 🏘️ Subtle town “bed” (non-identifiable crowd + room tone style)

**Not for:**
- UI clicks / beeps (put those in a `sfx/` folder if present)
- Music tracks (keep separate from ambience)
- Raw production files (WAV masters, DAW sessions) — keep those outside web runtime assets

---

## 🧭 KFM-aligned principles (Provenance-first)

KFM is designed around **traceability** and “no mystery layers.” These ambience assets follow the same standard:

- 🧾 **Every audio file MUST have a metadata sidecar** (`*.meta.json`) describing source + license + processing.
- 🚫 **No metadata = no shipping.** (CI should block it.)
- 🧠 **Soundscapes are optional storytelling context**, not evidence. Keep it honest.

---

## 📁 Folder layout

> **Example structure** (your set may differ):

```text
📁 web/assets/media/audio/ambience/
├─ 📄 README.md
├─ 📄 soundscapes.json              # optional: registry mapping contexts → clips
├─ 📁 prairie/
│  ├─ 🔊 ks_prairie_day__summer__v1.ogg
│  ├─ 🔊 ks_prairie_day__summer__v1.mp3
│  └─ 🧾 ks_prairie_day__summer__v1.meta.json
├─ 📁 weather/
│  ├─ 🔊 ks_rain_light__loop__v1.ogg
│  ├─ 🔊 ks_rain_light__loop__v1.mp3
│  └─ 🧾 ks_rain_light__loop__v1.meta.json
└─ 📁 towns/
   ├─ 🔊 ks_smalltown__bed__v1.ogg
   ├─ 🔊 ks_smalltown__bed__v1.mp3
   └─ 🧾 ks_smalltown__bed__v1.meta.json
```

---

## 🏷️ Naming conventions

Keep names **predictable**, **sortable**, and **stable**.

### ✅ Recommended filename pattern

```text
<region>_<biome-or-context>__<time-or-weather>__<variant>__v<major>[.<codec-ext>]
```

**Examples**
- `ks_prairie__day__summer__v1.ogg`
- `ks_prairie__night__cicadas__v2.mp3`
- `ks_riverbank__calm__v1.ogg`
- `ks_rain__light__loop__v1.ogg`

### Rules
- Use lowercase + underscores.
- Use double-underscore `__` to separate semantic chunks.
- Include a version suffix: `__v1`, `__v2`…
- If it loops, include `__loop__` in the name **and** mark it in metadata.

---

## 🎚️ Audio specs (web-friendly)

These are pragmatic targets to keep playback consistent across browsers and devices:

### Delivery formats
- ✅ **Primary:** `.ogg` (Opus or Vorbis)
- ✅ **Fallback:** `.mp3` (broad compatibility, especially for older Safari builds)
- 🚫 Avoid shipping `.wav` here unless explicitly needed for a special pipeline case

### Technical targets (suggested)
- Sample rate: **48 kHz** (or 44.1 kHz if your pipeline is standardized there—just be consistent)
- Channels: **Stereo** unless the recording truly benefits from mono
- Loudness target: **~ -18 LUFS integrated** (ambience should sit under narration/UI)
- True peak: **≤ -1.0 dBTP**
- Duration: **30–120 seconds** loop beds (longer is fine if file size stays reasonable)

> [!TIP]
> Favor “low attention demand” beds: stable, natural, non-repeating textures. Ambience should support focus, not hijack it. 🧘

---

## 🧾 Required metadata sidecar (`*.meta.json`)

Every audio asset must ship with a matching `*.meta.json` file using the same base name.

### Example
If you add:

- `ks_prairie__night__cicadas__v1.ogg`
- `ks_prairie__night__cicadas__v1.mp3`

You must also add:

- `ks_prairie__night__cicadas__v1.meta.json`

### Suggested metadata schema

<details>
<summary>🧾 Click to expand suggested <code>*.meta.json</code> schema</summary>

```json
{
  "id": "urn:kfm:audio:ambience:ks_prairie__night__cicadas__v1",
  "title": "Kansas Prairie Night — Cicadas (Loop)",
  "kind": "ambience",
  "tags": ["kansas", "prairie", "night", "insects", "loop"],

  "files": [
    { "path": "prairie/ks_prairie__night__cicadas__v1.ogg", "codec": "ogg", "sha256": "..." },
    { "path": "prairie/ks_prairie__night__cicadas__v1.mp3", "codec": "mp3", "sha256": "..." }
  ],

  "audio": {
    "loop": true,
    "duration_sec": 60,
    "sample_rate_hz": 48000,
    "channels": 2,
    "loudness_lufs_i": -18.0,
    "true_peak_db": -1.0
  },

  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Author Name — Source Collection",
    "source_url": "https://example.com/original",
    "notes": "Any special attribution requirements go here."
  },

  "provenance": {
    "created_utc": "2026-01-18T00:00:00Z",
    "contributors": ["your-handle"],
    "processing_steps": [
      "Trimmed to 60s loop bed",
      "Noise reduction (light)",
      "EQ: low shelf -2dB @ 120Hz",
      "Loudness normalized to -18 LUFS-I",
      "Exported OGG + MP3"
    ]
  }
}
```
</details>

> [!NOTE]
> The `sha256` fields are optional but strongly recommended for **auditability** and cache-busting discipline. 🔍

---

## 🗺️ Optional: `soundscapes.json` registry

If the web client supports a registry-driven ambience system, keep a single file that maps UI context → ambience set.

**Example shape (adapt as needed):**
```json
{
  "defaults": {
    "enabledByDefault": false,
    "masterVolume": 0.6
  },
  "soundscapes": [
    {
      "id": "prairie_day",
      "label": "Prairie — Day",
      "when": { "biome": "prairie", "timeOfDay": "day" },
      "layers": [
        { "ref": "prairie/ks_prairie__day__summer__v1", "gain": 0.7 },
        { "ref": "prairie/ks_wind__light__v1", "gain": 0.4 }
      ],
      "crossfadeMs": 1200
    }
  ]
}
```

---

## ▶️ Web playback patterns

Use the browser’s audio stack responsibly:

- ✅ Prefer **Web Audio API** for layering + gain staging + crossfades
- ✅ Ensure **user gesture** before playback (mobile restrictions)
- ✅ Lazy-load: don’t download ambience until enabled
- ✅ Cache smartly; avoid re-downloading when switching layers

### Minimal HTML fallback example
```html
<audio controls loop preload="none">
  <source src="./prairie/ks_prairie__day__summer__v1.ogg" type="audio/ogg" />
  <source src="./prairie/ks_prairie__day__summer__v1.mp3" type="audio/mpeg" />
  Your browser does not support the audio element.
</audio>
```

---

## 🧪 QA checklist (before merging)

- [ ] 🔇 Default state respects user choice (no surprise autoplay)
- [ ] 🔁 Loop is seamless (no click/pop, no obvious restart)
- [ ] 🎚️ No clipping, consistent loudness vs other ambience assets
- [ ] 📦 File size reasonable for web delivery (mobile-friendly)
- [ ] 🧾 Metadata present, complete, license verified
- [ ] 🧼 No identifiable voices / private conversations / sensitive audio
- [ ] 🧭 Tested on at least: Chrome + Safari + mobile

---

## 🤝 Contributing a new ambience clip

1. ➕ Add `.ogg` + `.mp3` files into a themed subfolder (e.g., `prairie/`, `weather/`)
2. 🧾 Add matching `*.meta.json` with license + provenance
3. 🧩 If used by the app, register it in `soundscapes.json`
4. ✅ Verify QA checklist above
5. 🔍 Open PR with a short description + screenshot/video of it working (if applicable)

---

## 📜 Credits & attribution

Attribution is **per-file** via `*.meta.json`.  
If you need an aggregated credits page, generate it from metadata (don’t maintain a second manual list unless required). 🧾✨
