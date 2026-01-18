# 🎧 Audio Manifests (`web/assets/media/audio/_manifests/`)

![contract-first](https://img.shields.io/badge/contract--first-required-1f6feb)
![provenance-first](https://img.shields.io/badge/provenance--first-always-1f6feb)
![accessibility](https://img.shields.io/badge/accessibility-captions%20%2B%20transcripts-2da44e)
![license-aware](https://img.shields.io/badge/licensing-respected-f0b429)

> **Source-of-truth metadata** for every audio asset used in the KFM web UI (Story Nodes, Focus Mode, tours, ambient layers, etc.).  
> If it plays in the UI, it **must** have a manifest. ✅

---

## 🧭 What is a “manifest” here?

An **audio manifest** is a small JSON file that describes:
- ✅ **What** the audio is (title, kind, language, duration)
- ✅ **Where** it lives (local file paths and/or remote URLs)
- ✅ **How** it can be used (license + attribution)
- ✅ **How** it was made (provenance: edits, remastering, AI/TTS, tools)
- ✅ **How** it stays inclusive (captions/transcripts, warnings)
- ✅ **How** it connects back to evidence (sources, related Story Nodes, datasets)

This mirrors KFM’s “contract-first / provenance-first” approach, but applied to **media**. 🎛️

---

## 🗂️ Suggested layout

> This folder holds **only manifests**. Audio files themselves live alongside `audio/` (or are served via a CDN and referenced here).

```text
📁 web/
  📁 assets/
    📁 media/
      📁 audio/
        📁 _manifests/          👈 you are here
          ├─ README.md
          ├─ index.json         (optional; generated or maintained)
          ├─ kansas-river-1951.audio.json
          └─ dust-bowl-oral-history.audio.json
        📁 kansas-river-1951/
          ├─ kansas-river-1951.mp3
          ├─ kansas-river-1951.ogg            (optional alt)
          ├─ kansas-river-1951.en.vtt         (captions)
          ├─ kansas-river-1951.transcript.txt (readable transcript)
          └─ cover.webp                       (optional)
```

✅ **Naming rule:** `"<id>.audio.json"`  
- Keep `id` stable forever (it becomes a reference handle across Story Nodes + UI).
- Prefer kebab-case.

---

## 🔥 Why we do this (the “no mystery audio” rule)

Manifests keep the platform:
- **Traceable** 🔎 (citations + provenance)
- **Accessible** ♿ (captions/transcripts)
- **Legally safe** ⚖️ (license-attribution is explicit)
- **Maintainable** 🧱 (repeatable ingestion + validation)
- **Composable** 🧩 (Story Nodes can reference a single `audioId`)

---

## 🧩 Audio Manifest Contract (v1)

### ✅ Required fields (minimum viable)

| Field | Type | Notes |
|------|------|------|
| `id` | `string` | Stable slug (kebab-case recommended) |
| `title` | `string` | Human title shown in UI |
| `kind` | `string` | e.g. `narration`, `interview`, `ambient`, `sonification`, `music` |
| `language` | `string` | BCP-47-ish, e.g. `en`, `en-US`, `es` |
| `files` | `array` | One or more playable sources |
| `license` | `object` | SPDX + attribution |
| `sources` | `array` | Evidence / archive records (URLs or internal IDs) |
| `sensitivity` | `string` | `public` \| `restricted` \| `sensitive` |

### 🎁 Strongly recommended fields

- `description` (short UI description)
- `durationSec`
- `captions` (VTT tracks)
- `transcript` (plain text)
- `credits` (voice, editor, producer)
- `provenance` (edits, tools, AI usage)
- `contentWarnings` (e.g. distressing content, slurs in historical material)

---

## 🧪 Example manifest

> File: `kansas-river-1951.audio.json`

```json
{
  "id": "kansas-river-1951",
  "title": "Kansas River Flood of 1951 — Short Narration",
  "kind": "narration",
  "language": "en-US",
  "description": "A brief narration introducing the 1951 flood and its regional impacts.",
  "durationSec": 94,

  "files": [
    {
      "format": "mp3",
      "mime": "audio/mpeg",
      "path": "../kansas-river-1951/kansas-river-1951.mp3",
      "bytes": 1264832,
      "sha256": "TODO_SHA256"
    },
    {
      "format": "ogg",
      "mime": "audio/ogg",
      "path": "../kansas-river-1951/kansas-river-1951.ogg",
      "bytes": 1048576,
      "sha256": "TODO_SHA256"
    }
  ],

  "captions": [
    {
      "kind": "captions",
      "srclang": "en",
      "label": "English",
      "path": "../kansas-river-1951/kansas-river-1951.en.vtt"
    }
  ],

  "transcript": {
    "path": "../kansas-river-1951/kansas-river-1951.transcript.txt"
  },

  "credits": {
    "narrator": "KFM Volunteer Narration Team",
    "editor": "KFM Media Pipeline",
    "producer": "Kansas Frontier Matrix"
  },

  "license": {
    "spdx": "CC-BY-4.0",
    "url": "https://creativecommons.org/licenses/by/4.0/",
    "attribution": "Kansas Frontier Matrix contributors",
    "notes": "Do not imply endorsement by original source institutions."
  },

  "sources": [
    {
      "label": "Primary evidence bundle (Story Node references)",
      "type": "kfm-story-node",
      "ref": "story:1951-flood-overview"
    },
    {
      "label": "Archive collection landing page",
      "type": "url",
      "url": "https://example.org/archive/kansas-flood-1951"
    }
  ],

  "provenance": {
    "createdAt": "2026-01-18",
    "workflow": [
      "scripted narration drafted from cited Story Node evidence",
      "audio recorded",
      "noise reduction + normalization",
      "exported to mp3 + ogg",
      "captions generated + manually reviewed"
    ],
    "ai": {
      "used": false
    }
  },

  "sensitivity": "public",
  "tags": ["kansas", "flood", "1951", "rivers", "history"]
}
```

---

## ➕ Add a new audio asset (fast path ✅)

1. **Create / obtain the audio** 🎙️  
   - Prefer open formats + provide at least one broadly compatible file (MP3 recommended).
2. **Create accessibility artifacts** ♿  
   - Spoken audio should ship with:
     - `*.en.vtt` captions (or multiple languages)
     - `*.transcript.txt` readable transcript
3. **Write the manifest** 🧾  
   - Copy the example above and adjust.
4. **Provenance + licensing sanity check** ⚖️  
   - Every manifest must state license + attribution.
5. **Wire it into UI content** 🧩  
   - Story Nodes / UI configs should reference by `audioId` (stable).

---

## ♿ Accessibility rules (non-negotiable)

✅ If there are spoken words, you should include:
- Captions (`.vtt`) and/or subtitles tracks
- A plain transcript (`.txt`) that can be read, searched, and copied

### Example HTML usage (what the UI should roughly render)

```html
<audio controls>
  <source src="file.mp3" type="audio/mpeg" />
  <track kind="captions" src="foo.en.vtt" srclang="en" label="English" />
  Your browser does not support the audio element.
</audio>
```

---

## 🤖 AI / TTS audio policy (keep it honest)

If AI is involved (TTS voice, AI cleanup, AI translation), the manifest **must** say so:

- `provenance.ai.used = true`
- Include **model/tool name**, **human review**, and **what was generated**
- The UI should label AI-generated audio clearly (no ambiguity)
- Never “invent” sources: any narration must be backed by **cited evidence** (usually a Story Node)

---

## 🔒 Integrity & performance tips

- Prefer multiple encodes (`mp3` + optional `ogg`) so browsers can choose best.
- Include `sha256` for each file whenever feasible (helps detect accidental changes).
- Avoid committing huge binaries if possible:
  - Option A: store audio in-repo (small files)
  - Option B: store audio in object storage/CDN and reference via `url` in `files[]`

---

## 🧰 Validation checklist (PR-ready ✅)

Before merging:
- [ ] Manifest JSON parses
- [ ] `id` is unique and matches filename
- [ ] `license.spdx` present and correct
- [ ] `sources[]` present (no “mystery audio”)
- [ ] Spoken audio includes captions/transcript
- [ ] `sensitivity` correct (`public` vs `restricted/sensitive`)
- [ ] If AI used → marked + review noted

---

## 🔗 How this connects to Story Nodes & Focus Mode

```mermaid
flowchart LR
  A[🎙️ Audio File(s)] --> B[🧾 Audio Manifest]
  B --> C[📜 Story Node]
  C --> D[🧠 Focus Mode / UI]
  B --> D
```

- **Story Nodes** reference `audioId` to embed audio with correct attribution + evidence links.
- **Focus Mode** should only surface audio that is provenance-linked and allowed by `sensitivity`.

---

## 🧾 Common “kinds” (recommended)

| kind | Use case |
|------|----------|
| `narration` | Guided explanations tied to Story Nodes |
| `interview` | Oral history clips, transcripts required |
| `ambient` | Background soundscapes (no words) |
| `sonification` | Turning datasets into sound (must cite dataset + method) |
| `music` | Only if license is crystal-clear |

---

## 🧠 FAQ

**Q: Do we always need a local audio file in the repo?**  
A: Not necessarily. Manifests can reference remote assets (CDN/object storage). The key requirement is **provenance + license clarity**.

**Q: Can we ship historical audio with offensive language?**  
A: Possibly, but it needs:
- clear `contentWarnings[]`
- correct `sensitivity`
- careful citations and contextual handling in Story Nodes

---

🛠️ **TODO (nice-to-have):** add a JSON Schema + CI validator so these manifests become machine-enforced “media contracts”.
