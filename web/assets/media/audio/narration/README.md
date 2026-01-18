# 🎙️ Narration Audio (Web) — `web/assets/media/audio/narration/`

![Asset](https://img.shields.io/badge/asset-narration%20audio-blue?style=for-the-badge)
![Scope](https://img.shields.io/badge/scope-web%20ui-informational?style=for-the-badge)
![Trust](https://img.shields.io/badge/trust-provenance--first-success?style=for-the-badge)
![A11y](https://img.shields.io/badge/a11y-transcripts%20required-important?style=for-the-badge)

> [!IMPORTANT]
> This folder is for **web-ready** narration assets that ship to the UI (Story Nodes / Focus Mode / guided tours).  
> **No “mystery audio”**: every clip must be accompanied by a metadata sidecar + transcript. ✅

---

## ✨ What lives here

This directory holds **final delivery audio** for narration:
- 🧭 **Story Nodes** (Narrative Mode): narrated “slides” / steps / chapters
- 🔎 **Focus Mode**: narration attached to evidence-backed content
- 🎛️ **UI walkthroughs** (optional): short, reusable prompts like “Use the timeline to scrub years…”

**Not here** (by design):
- 🎚️ raw takes / DAW sessions / uncompressed masters (store elsewhere; see “Masters vs Delivery” below)
- 🧪 experiments, scratch renders, or anything without provenance + license + transcript

---

## ✅ Non‑negotiables (trust + governance)

1. **Provenance-first** 🧾  
   If it appears in the UI, it must be traceable: sources, license, and how it was produced.

2. **Contract-first** 📦  
   Every narration clip must ship with a **metadata JSON** (a “data contract” for the asset).

3. **Accessibility is required** ♿  
   Every clip must have a **transcript** (and optionally captions).

4. **AI narration must be opt‑in & labeled** 🤖  
   If TTS/AI is used, it must be explicitly declared in metadata and clearly labeled in the UI.

---

## 🗂️ Folder layout

Suggested structure (friendly to Story Nodes + localization):

```text
web/assets/media/audio/narration/
├── README.md
├── index.json                       # (optional) registry/manifest for quick lookup by the UI
└── story_nodes/
    └── <story_slug>/
        ├── en-US/
        │   ├── <node_id>.v1.mp3
        │   ├── <node_id>.v1.ogg               # optional alt codec
        │   ├── <node_id>.v1.meta.json         # REQUIRED: contract + provenance + licensing
        │   ├── <node_id>.v1.transcript.md     # REQUIRED: human-readable transcript
        │   └── <node_id>.v1.captions.vtt      # optional: captions for HTML5 video/audio
        └── es-US/
            └── ...
```

> [!TIP]
> Keep filenames stable. When narration changes, **bump the version** (e.g., `v1 → v2`) so caches/CDNs behave.

---

## 🏷️ Naming convention

Use a predictable pattern so the UI can resolve assets without guesswork:

**Pattern**
```text
<node_id>.v<major>[.<minor>].<ext>
```

**Examples**
- `intro.v1.mp3`
- `slide-03_outmigration.v2.1.ogg`
- `slide-03_outmigration.v2.1.meta.json`
- `slide-03_outmigration.v2.1.transcript.md`

**Rule of thumb**
- **major** bump (`v1 → v2`) if the *meaning* changes (script rewrite, new claims, different sources)
- **minor** bump (`v2.0 → v2.1`) if it’s a *presentation* tweak (timing, clarity edits, tiny wording)

---

## 🎚️ Masters vs Delivery (don’t bloat the repo)

- ✅ Store **web delivery** here (compressed, normalized, small).
- 🗃️ Store **masters** (WAV/FLAC, multitrack, DAW projects) in a non-web location:
  - `data/processed/...` (preferred if you’re treating narration as a first-class evidence artifact)
  - or an external artifact store (CDN/object storage), referenced by provenance metadata

---

## 🎛️ Audio spec (recommended defaults)

These defaults are safe for most web playback:

- **Primary codec:** `MP3` (broadest compatibility)
- **Optional codec:** `Ogg Vorbis` (nice-to-have)
- **Sample rate:** `48 kHz` (or `44.1 kHz`—choose one and stay consistent)
- **Channels:** `mono` preferred for narration (smaller + clearer), stereo allowed if needed
- **Target loudness:** `-16 LUFS` (integrated) for perceived consistency
- **True peak ceiling:** `≤ -1.0 dBTP` (avoid clipping on mobile players)
- **Trim:** remove dead air; add light fades to avoid “hard cuts”

> [!NOTE]
> Don’t guess quality. Store measured values (LUFS, peaks, duration) in the `*.meta.json` so the UI and QA can validate.

---

## 🧾 Sidecar metadata (REQUIRED)

Every audio file must have a `*.meta.json`. This is the “contract” for the clip.

### ✅ Required sidecars per clip
- `*.meta.json` — provenance, sources, licensing, and technical info  
- `*.transcript.md` — readable transcript (supports accessibility + search indexing)

### 📌 Minimal metadata schema (example)

```json
{
  "id": "dust-bowl/slide-03",
  "kind": "narration",
  "story_slug": "dust-bowl",
  "node_id": "slide-03_outmigration",
  "locale": "en-US",
  "version": "2.1",

  "title": "Dust Bowl — Out-migration (1930s)",
  "summary": "Narration for slide 3, explaining out-migration patterns and contributing factors.",

  "audio": {
    "mp3": "/assets/media/audio/narration/story_nodes/dust-bowl/en-US/slide-03_outmigration.v2.1.mp3",
    "ogg": "/assets/media/audio/narration/story_nodes/dust-bowl/en-US/slide-03_outmigration.v2.1.ogg",
    "duration_s": 24.2,
    "sample_rate_hz": 48000,
    "channels": 1,
    "lufs_i": -16.0,
    "true_peak_db": -1.0
  },

  "transcript": {
    "markdown": "/assets/media/audio/narration/story_nodes/dust-bowl/en-US/slide-03_outmigration.v2.1.transcript.md",
    "captions_vtt": "/assets/media/audio/narration/story_nodes/dust-bowl/en-US/slide-03_outmigration.v2.1.captions.vtt"
  },

  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Kansas Frontier Matrix contributors",
    "notes": "If combined with more restrictive sources, follow the more restrictive license."
  },

  "sources": [
    { "type": "stac_item", "id": "stac:item:..." },
    { "type": "dcat_dataset", "id": "dcat:dataset:..." },
    { "type": "bibliography", "id": "biblio:..." }
  ],

  "provenance": {
    "created_at": "2026-01-18",
    "created_by": "human",
    "pipeline_run_id": "prov:run:...",
    "git_commit": "abc1234"
  },

  "ai": {
    "generated": false,
    "engine": null,
    "voice": null,
    "model": null,
    "prompt_hash": null,
    "confidence": null
  }
}
```

> [!TIP]
> Keep `sources[]` machine-joinable (IDs), not just prose. The UI and Focus Mode should be able to jump to evidence.

---

## 🧩 `index.json` manifest (optional, but recommended)

If the UI needs fast lookup without scanning directories, add a registry:

- `index.json` maps `{story_slug, node_id, locale, version} → asset paths + metadata path`
- it can be **generated** as part of build/CI to prevent drift

**Example shape**
```json
{
  "version": 1,
  "items": [
    {
      "story_slug": "dust-bowl",
      "node_id": "slide-03_outmigration",
      "locale": "en-US",
      "version": "2.1",
      "meta": "/assets/media/audio/narration/story_nodes/dust-bowl/en-US/slide-03_outmigration.v2.1.meta.json"
    }
  ]
}
```

---

## ➕ Adding new narration (checklist) ✅

1. 📝 Write/update the script (keep it aligned with Story Node content + citations)
2. 🎙️ Record (human) **or** generate (TTS) — follow AI policy below
3. 🎛️ Edit + normalize (LUFS / true peak / trims)
4. 📤 Export web delivery (`.mp3`, optional `.ogg`)
5. 🧾 Create `*.meta.json` (license + sources + provenance + technical measures)
6. ♿ Create transcript (`*.transcript.md`) + optional captions (`*.vtt`)
7. 🧪 Run validations (or ensure CI will validate)
8. 🧭 Update `index.json` (if used)

> [!WARNING]
> If you can’t list sources + license + provenance, **don’t ship the clip** to this folder.

---

## 📜 Licensing & attribution

Narration is “content,” so it inherits KFM’s stance on license transparency:

- Every clip must declare an SPDX-style license identifier when possible (e.g., `CC-BY-4.0`, `CC0-1.0`)
- Include the proper attribution string
- If narration synthesizes/quotes restricted sources, ensure the resulting distribution respects the **most restrictive** requirement

> [!NOTE]
> If a human voice actor is used, ensure you have a release/permission for distribution and note it in metadata.

---

## 🤖 AI / TTS policy

If `ai.generated = true`, the metadata must include:
- engine/provider (e.g., `engine: "tts_vendor_x"`)
- model + voice identifier
- prompt/script hash (so we can reproduce the same output)
- any confidence/uncertainty info (if the pipeline provides it)

And the UI should:
- show an **AI-generated** badge/tag
- keep it **opt-in** (don’t autoplay AI narration without user intent)

---

## 🧪 Quality gates (what CI or reviewers should enforce)

Minimum checks (automatable):
- `*.mp3` exists ✅
- `*.meta.json` exists + parses ✅
- `*.transcript.md` exists ✅
- metadata contains: `license`, `sources[]`, `provenance`, `audio.duration_s` ✅
- loudness + peak are within tolerance ✅
- paths in metadata actually resolve ✅
- no orphan audio files without metadata ✅

---

## 🔧 Troubleshooting

- **Audio is too quiet/loud** → re-normalize to the target LUFS and re-export (don’t “fix” in the player)
- **Clicks at start/end** → add 5–20ms fades
- **Mobile playback clipping** → lower true peak ceiling and re-export
- **UI can’t find narration** → check naming + `index.json` entry + locale code
- **Cache won’t update** → bump `version` in filename and metadata

---

## 🔗 See also (repo references)

- 📖 `docs/templates/TEMPLATE__STORY_NODE_V3.md` (Story Node structure + citations)
- 🧭 `docs/governance/ETHICS.md` (human-centered safeguards)
- 🧾 `docs/standards/KFM_PROV_PROFILE.md` (provenance conventions)
- 📦 `docs/data/contracts/` (data contract patterns)
