# 🧾 Web Media Source Vault — `web/assets/media/_sources/`

![Provenance‑First](https://img.shields.io/badge/Provenance-First-2ea44f?style=flat-square)
![Contract‑First](https://img.shields.io/badge/Contract-First-1f6feb?style=flat-square)
![Deterministic](https://img.shields.io/badge/Build-Deterministic-8250df?style=flat-square)
![Web Assets](https://img.shields.io/badge/Scope-Web%20Media-444?style=flat-square)

This folder is the **source-of-truth pantry** for media used by the KFM web UI.  
It stores **original/source media** (and the evidence needed to justify using it) so the repo can generate **web‑ready, shippable assets** without guesswork.

> [!IMPORTANT]
> **No “mystery assets.”** If an image/video/audio shows up in the UI, we should be able to explain:
> **where it came from**, **what license governs it**, and **how it was processed**. ✅

---

## 🧠 Why `_sources` exists

KFM is built around evidence-first + provenance-first rules: anything that shows up in the UI should be traceable and auditable (data, narrative, *and* media).  
This directory is how we apply that principle to **web UI media** (logos, icons, story visuals, thumbnails, background imagery, short clips, etc.).

In short: **keep originals + metadata here → generate optimized outputs elsewhere**.

---

## 🗺️ Where this fits in the repo

The broader system pipeline is strict (data → catalogs → graph → API → UI → narratives).  
This folder is **UI-adjacent** and should **never** become a side-channel that bypasses cataloged evidence.

✅ Use `_sources/` for *web asset provenance + reproducible builds*  
❌ Do **not** use `_sources/` as a dumping ground for datasets, GIS layers, or “raw evidence” that should live under `data/raw/…` and be cataloged.

---

## 📦 Directory expectations

Suggested structure (keep it boring + predictable 😌):

```text
web/assets/media/
├── 🖼️ images/                 # ✅ Optimized / deployable images (served)
├── 🎞️ video/                  # ✅ Optimized / deployable video (served)
├── 🔊 audio/                  # ✅ Optimized / deployable audio (served)
├── 🔤 fonts/                  # ✅ Deployable fonts (served)
└── 🧾 _sources/               # 🧾 Originals + provenance (this folder; NOT served)
    ├── 🖼️ images/             # Original image sources (PSD/AI/SVG masters, raw captures, etc.)
    ├── 🎞️ video/              # Original video sources (project files, high-bitrate masters)
    ├── 🔊 audio/              # Original audio sources (WAV sessions, stems, scripts)
    ├── 🔤 fonts/              # Source font packages + license texts
    ├── 🧷 icons/              # Master icon sets + upstream attribution
    ├── 🎨 textures/           # Source textures/material scans + bake inputs
    └── 🗂️ manifests/          # Optional rollups/indexes (provenance summaries, inventory exports)
```

> [!NOTE]
> If `_sources/` is not meant to be deployed, make sure your build/deploy step excludes it.

---

## ✅ What belongs here (and what doesn’t)

### ✅ Belongs here
- 🎨 **Original design exports** (e.g., `.svg`, `.png`, `.tif`, `.psd` *if allowed*, `.ai` *if allowed*)
- 🗺️ **Original maps / scans** used to create web-ready derivatives
- 🎥 **High-quality video/audio masters** used to generate web-friendly formats
- 🧾 **Provenance + license metadata** (required)
- 🔁 **Reproducible transformation notes** (how we produced the final assets)

### ❌ Does *not* belong here
- 🧱 Raw datasets that should be in the data pipeline (`data/raw`, `data/processed`, STAC/DCAT/PROV)
- 🗃️ Random downloads with no licensing clarity
- 🧨 “Temporary” exports that are used directly in production
- 🔐 Sensitive media that shouldn’t be publicly shipped (unless governance explicitly approves)

---

## 🏷️ Naming conventions

Keep names **URL-safe**, **lowercase**, and **stable**.

**Rules**
- ✅ `kebab-case` only
- ✅ ASCII only
- ✅ avoid spaces, parentheses, and `#`
- ✅ include a *version* or *date* when updates are likely

**Examples**
- `kfm-logo-v1.svg`
- `hero-kansas-prairie-1890-scan-v2.tif`
- `timeline-marker-set-v1.svg`
- `story__land-treaties__map-overlay__v03.png`

---

## 🧾 Metadata sidecar contract (required)

Every asset (or asset folder) **must** include a metadata sidecar file:

- `meta.yml` (preferred) or `meta.json`  
- stored next to the original source file

### Minimum required fields
| Field | Required | Example |
|---|---:|---|
| `id` | ✅ | `urn:kfm:media:image:hero-kansas-prairie:v2` |
| `title` | ✅ | `Kansas prairie hero image` |
| `type` | ✅ | `image \| video \| audio \| font \| icon` |
| `role` | ✅ | `ui \| story \| thumbnail \| background` |
| `source.url` | ✅ | `https://…` (or `local_archive`, etc.) |
| `source.retrieved_at` | ✅ | `2026-01-15` |
| `license.spdx` | ✅ | `CC-BY-4.0` (or other) |
| `license.attribution` | ✅ | `Author / Institution / Link` |
| `checksums.sha256` | ✅* | `…` (*required if the binary is stored in repo*) |
| `outputs[]` | ✅ | list of generated, web-ready output files |

### Suggested `meta.yml` template

```yaml
id: "urn:kfm:media:image:hero-kansas-prairie:v2"
title: "Kansas Prairie — Hero Background"
type: "image"               # image | video | audio | font | icon
role: "background"          # ui | story | thumbnail | background | texture

source:
  url: "https://example.org/archive/item/123"
  publisher: "Example Archive"
  creator: "Unknown"
  retrieved_at: "2026-01-15"
  notes: "Downloaded as high-res TIFF; cropped for web hero use."

license:
  spdx: "CC-BY-4.0"
  attribution: "Example Archive (Item 123), CC-BY-4.0"
  attribution_url: "https://example.org/archive/item/123"
  restrictions: "none"       # e.g., noncommercial-only, no-derivatives, etc.

sensitivity:
  care_label: "Public"       # Public | Restricted | Sensitive | TBD
  notes: "No known sensitivity concerns."

processing:
  intent: "Generate responsive web images (avif/webp) + thumbnail."
  pipeline: "TBD"            # name the script/tool once it exists
  params:
    max_width_px: 2400
    formats: ["avif", "webp"]
    quality: 82
  changelog:
    - "v2: re-cropped for better subject framing"

checksums:
  sha256: "PUT_SHA256_HERE"

outputs:
  - path: "../../images/hero-kansas-prairie-v2.avif"
    kind: "primary"
  - path: "../../images/hero-kansas-prairie-v2.webp"
    kind: "fallback"
  - path: "../../images/hero-kansas-prairie-v2.thumb.webp"
    kind: "thumbnail"
```

> [!TIP]
> If the **original binary** is too large to store in Git, store a **pointer file** instead (URL + checksum + retrieval notes), and still include `meta.yml`.

---

## 🔁 Deterministic build rules

To stay aligned with KFM’s deterministic pipeline mindset:

- ✅ Treat output generation as a **repeatable build step**
- ✅ Prefer **scripted** conversions over manual edits
- ✅ Record **parameters** (resize, crop, quality, format) in `meta.yml`
- ✅ Outputs should be reproducible from `_sources/` + scripts/config

### Typical output expectations (images)
- Primary: `AVIF` (best compression)
- Fallback: `WebP`
- Optional legacy fallback: `PNG/JPG` only when needed
- Thumbnails: small, aggressively compressed, fast-loading

### Typical output expectations (video)
- Primary: `mp4 (h.264)` for compatibility
- Optional: `webm` for better compression where supported
- Always include: poster image (thumbnail) + caption/subtitle file if applicable

---

## ♿ Accessibility & UX (required)

Media is part of UX, not decoration.

- ✅ Every non-trivial image used in docs/story/UI should have **alt text** and/or a caption.
- ✅ Videos should have **captions** where feasible.
- ✅ Audio should have a **transcript** where feasible.

> [!NOTE]
> If you can’t describe what an asset is, we probably shouldn’t ship it.

---

## ⚖️ Licensing & attribution rules

- ✅ If license is unclear → **do not commit the binary**
- ✅ If attribution is required → include it in `meta.yml` + wherever the UI renders credits
- ✅ If the license restricts redistribution → store a pointer + instructions instead of the file
- ✅ Prefer open licenses for shipped UI media

---

## ✅ “Definition of Done” for a new asset

Before merging a media PR:

- [ ] Asset stored under the correct `_sources/<type>/…` folder
- [ ] `meta.yml` present and complete (source + license + outputs)
- [ ] Outputs generated to `web/assets/media/<type>/…` (or referenced if build not yet implemented)
- [ ] File names are stable + URL-safe
- [ ] Size/performance is reasonable (no accidental multi‑MB PNGs)
- [ ] Accessibility needs considered (alt/captions/transcripts)
- [ ] No sensitive/surveillance/unsafe content shipped unintentionally

---

## 🔗 Related docs (project-level)

- 📘 `docs/MASTER_GUIDE_v13.md` (provenance-first / contract-first / pipeline ordering)
- 🧱 `docs/standards/` (profiles, governance, review gates)
- 🧩 `web/` (UI entrypoint; avoid bypassing governed API rules)

---

## 🙋 FAQ

<details>
  <summary><strong>Do I ever reference files in <code>_sources/</code> directly from the UI?</strong></summary>

No (in general). The UI should use the optimized outputs in `web/assets/media/**`.  
Treat `_sources/` as build inputs + provenance records.

</details>

<details>
  <summary><strong>What if the source is huge or not redistributable?</strong></summary>

Commit:
- `meta.yml` (with license + URL + retrieval notes)
- checksum
- a small preview (if allowed)

Do **not** commit the original binary if licensing or size makes it risky.

</details>
