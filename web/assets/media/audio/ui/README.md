# 🎧 UI Audio Assets (`web/assets/media/audio/ui`)

![Scope](https://img.shields.io/badge/scope-web%2Fassets%2Fmedia%2Faudio%2Fui-1f6feb)
![Type](https://img.shields.io/badge/type-UI%20sound%20effects-8a2be2)
![Formats](https://img.shields.io/badge/formats-ogg%20%7C%20mp3-orange)
![A11y](https://img.shields.io/badge/a11y-user%20controlled%20audio-0ea5e9)

Subtle, consistent **sound effects** used across the KFM web UI (clicks, confirmations, warnings, focus-mode events, story navigation, etc.).  
These are **interface cues**, not long-form narration/music.

---

<details>
<summary>📚 Table of Contents</summary>

- [🎯 What belongs here](#-what-belongs-here)
- [🗂️ Folder layout](#️-folder-layout)
- [🏷️ Naming conventions](#️-naming-conventions)
- [🎚️ Audio specs](#️-audio-specs)
- [🧾 Provenance & licensing](#-provenance--licensing)
- [🧩 Manifest (recommended)](#-manifest-recommended)
- [🧑‍💻 Usage patterns](#-usage-patterns)
- [♿ Accessibility rules](#-accessibility-rules)
- [✅ Adding a new sound](#-adding-a-new-sound)
- [🧯 Troubleshooting](#-troubleshooting)

</details>

---

## 🎯 What belongs here

✅ **UI feedback sounds**, short and non-intrusive:

- 🖱️ Click / tap (primary, secondary, toggle)
- ✅ Success / confirm
- ⚠️ Warning / “needs attention”
- ❌ Error / blocked action
- 🧭 Navigation (panel open/close)
- 🗺️ Map interactions (layer on/off, selection)
- 🧠 Focus Mode events (open, response received, citation jump)
- 🎬 Story mode navigation (next/prev step, story complete)

🚫 **Not** for:

- 🎙️ Voice narration (store elsewhere; narration has different licensing + accessibility requirements)
- 🎵 Music beds / long ambience tracks (different mixing + performance concerns)
- 🔒 Any sensitive/private recordings (never commit user/field recordings here)

---

## 🗂️ Folder layout

Recommended structure (adjust as the library grows):

```text
web/assets/media/audio/ui/
├── README.md
├── manifest.ui-audio.json            # optional but strongly recommended
├── click/
│   ├── ui_click_primary_v1.ogg
│   ├── ui_click_primary_v1.mp3
│   └── ui_click_primary_v1.meta.json # optional per-asset metadata (if not using manifest)
├── notify/
├── error/
├── success/
├── focus-mode/
└── story/
```

> [!TIP]
> Keep **runtime assets** here (compressed). If you need raw source audio (WAV/DAW exports), keep it in a separate “source assets” area to avoid bloating the web bundle.

---

## 🏷️ Naming conventions

**Goal:** predictable imports + easy diff review.

**Pattern**
```
ui_<category>_<event>_v<major>.<ext>
```

**Examples**
- `ui_click_primary_v1.ogg`
- `ui_error_blocked_v1.mp3`
- `ui_focus_answer_ready_v1.ogg`
- `ui_story_step_next_v2.mp3`

**Rules**
- 🧊 Lowercase, underscores
- 🔢 Use `v<major>` for audible changes (don’t silently replace sounds)
- 🧠 One “sound identity” per filename (avoid ambiguous names like `sound1.ogg`)

---

## 🎚️ Audio specs

These are UI sounds — optimize for **clarity + speed**.

**Recommended**
- ⏱️ Duration: **50–350 ms** (rarely > 600 ms)
- 🔊 Peak: **≤ -1 dBFS** (avoid clipping)
- 🎛️ Consistent perceived loudness across the set (normalize as a library, not per file randomly)
- 🎧 Prefer “soft transient” designs (less fatigue)

**File formats**
- ✅ `*.ogg` (primary)
- ✅ `*.mp3` (fallback)
- 🚫 Avoid `*.wav` in runtime folders unless there’s a very strong reason

---

## 🧾 Provenance & licensing

KFM is **provenance-first**: if it ships in the UI, it should be traceable and legally safe.

Minimum required per sound (in `manifest.ui-audio.json` or a `*.meta.json` sidecar):

- 🧾 `license` (SPDX identifier when possible)
- 👤 `attribution` (author / source)
- 🔗 `source` (where it came from, or “original / generated”)
- 🛠️ `processing` notes (trim, normalize, EQ, export settings)

> [!IMPORTANT]
> **No “mystery assets.”** If licensing/provenance is unclear, don’t commit it.

---

## 🧩 Manifest (recommended)

A manifest makes audio **discoverable**, **auditable**, and easy to wire into the UI.

**Suggested file**
- `web/assets/media/audio/ui/manifest.ui-audio.json`

**Example**
```json
{
  "version": 1,
  "sounds": [
    {
      "id": "ui.click.primary",
      "category": "click",
      "files": {
        "ogg": "click/ui_click_primary_v1.ogg",
        "mp3": "click/ui_click_primary_v1.mp3"
      },
      "defaultGain": 0.8,
      "license": {
        "spdx": "CC-BY-4.0",
        "attribution": "Author Name (Source / Collection)"
      },
      "source": {
        "type": "generated",
        "createdBy": "KFM",
        "createdAt": "2026-01-18"
      },
      "processing": [
        "Trim to 120ms",
        "Normalize library target",
        "Export OGG+MP3"
      ],
      "tags": ["button", "navigation"]
    }
  ]
}
```

---

## 🧑‍💻 Usage patterns

### Option A: Simple (HTML `<audio>` with fallbacks)
```html
<audio preload="auto">
  <source src="/assets/media/audio/ui/click/ui_click_primary_v1.ogg" type="audio/ogg" />
  <source src="/assets/media/audio/ui/click/ui_click_primary_v1.mp3" type="audio/mpeg" />
</audio>
```

### Option B: App-level `AudioManager` (recommended)
- 🔁 Cache decoded buffers (Web Audio API) for frequently used sounds
- 🧠 Enforce global user settings: mute / volume / reduced cues
- 🧾 Attach provenance/ids to telemetry events if desired

Pseudo-interface:
```ts
type UiSoundId =
  | "ui.click.primary"
  | "ui.error.blocked"
  | "ui.focus.answer_ready";

interface AudioManager {
  setEnabled(enabled: boolean): void;
  setVolume(volume01: number): void;
  play(id: UiSoundId, overrides?: { volume01?: number }): Promise<void>;
}
```

> [!NOTE]
> Browsers often block audio until a **user gesture** occurs. Initialize/resume the audio context on first click/tap.

---

## ♿ Accessibility rules

UI audio must be **optional** and **never the only signal**.

- 🔇 Provide a global **Mute UI sounds** toggle
- 🎚️ Provide **UI sound volume** control
- 🧑‍🦯 Don’t encode critical info only in audio  
  (also show text, icons, toast, ARIA live region, etc.)
- 🧠 Avoid “alarm” sounds; prefer gentle cues
- 📵 No autoplay blasting on page load

---

## ✅ Adding a new sound

Checklist (PR-ready):

- [ ] Add `*.ogg` + `*.mp3` versions  
- [ ] Confirm short duration + consistent loudness
- [ ] Add provenance + license metadata (manifest or `*.meta.json`)
- [ ] Update `manifest.ui-audio.json` (if used)
- [ ] Verify it respects global settings (mute/volume)
- [ ] Confirm it’s not annoying in repeated use (rapid clicking)
- [ ] ✅ Run web build and ensure no large bundle regressions

---

## 🧯 Troubleshooting

**Sound doesn’t play**
- Check browser autoplay policy (must be triggered by user gesture)
- Verify correct MIME types and file paths
- Confirm user settings aren’t muting audio

**Sound is too loud / inconsistent**
- Don’t “normalize per file” blindly — normalize as a **library**
- Set per-sound `defaultGain` for outliers, not global hacks

**PR fails due to governance**
- Missing license / provenance metadata is a hard stop (fix before merge)

---

🧭 _If you’re unsure where a sound belongs:_ if it’s **short UI feedback**, it belongs here. If it’s **narrative, instructional, or long-form**, it belongs somewhere else.
