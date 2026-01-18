# 🧩 Decal Textures (Source) — `web/assets/media/_sources/textures/decals/`

![scope](https://img.shields.io/badge/scope-web%2Fassets-0b7285)
![asset-tier](https://img.shields.io/badge/asset_tier-_sources_(authoring)-6f42c1)
![rule](https://img.shields.io/badge/rule-provenance_first-critical)
![perf](https://img.shields.io/badge/goal-fast_GPU_friendly-198754)

Decals are **small textures (usually with alpha)** used to “stamp” or overlay visuals in the KFM web UI—think **map annotations**, **highlights**, **stamps**, **markers**, **brush strokes**, **glows**, and other lightweight visual affordances.

> 📍 **Folder contract**
> - This directory holds **authoring / source assets** (lossless + editable when possible).
> - **Do not** treat `_sources/` as “runtime-ready”. A build step should export/optimize these into the runtime asset location (where the app imports from).
> - Every decal must have **clear provenance + license** (KFM standard: transparency and traceability).

---

## 🗂️ Suggested layout

Keep things boringly predictable 😄

```text
web/assets/media/_sources/textures/decals/
├── README.md
├── 📄 ATTRIBUTION.md                 # optional: roll-up credits (recommended)
├── 📁 ui/                            # UI-only overlays (buttons, chips, glows)
├── 📁 map/                           # map/legend-adjacent stamps + overlays
├── 📁 story/                         # story-node specific visual accents
├── 📁 debug/                         # dev-only overlays (never ship by default)
└── 📁 _wip/                          # work-in-progress (not referenced by app)
```

> [!TIP]
> If a decal is tied to a specific dataset/map layer, keep the decal **generic**, and attach dataset provenance in the **layer’s legend/info UI** (don’t “bake” dataset identity into the decal unless it’s truly universal).

---

## ✅ What belongs here

### Preferred file types (authoring-friendly)
- **PNG** (`.png`) — lossless, alpha-friendly, predictable.
- **PSD/KRA/ASEPRITE** (`.psd`, `.kra`, `.aseprite`) — if the decal needs real edit history.
- **SVG** (`.svg`) — if the decal is vector-native (but export to raster for runtime use).

### Avoid (unless you have a strong reason)
- **JPEG** — no alpha; introduces artifacts on crisp edges.
- Massive source files without a clear need (keep `_sources` useful, not bloated).

---

## 🧱 Naming conventions

### Rule of thumb
**kebab-case**, descriptive, stable, and searchable.

**Pattern**
`<domain>-<concept>[-variant][-size].<ext>`

**Examples**
- `map-stamp-wetlands-512.png`
- `ui-glow-soft-256.png`
- `story-highlight-ink-01-512.png`
- `debug-grid-fine-1024.png`

> [!NOTE]
> If you need variants, prefer explicit tokens like `-soft`, `-hard`, `-warm`, `-cool`, `-01`, `-02`.

---

## 🖼️ Texture guidelines (GPU-friendly)

### Size & aspect
- Prefer **power-of-two** dimensions when practical: `128/256/512/1024`.
- Prefer **square** unless the decal truly requires a specific aspect ratio.
- Keep a **padding gutter** (2–8 px) around the visible content to prevent edge bleeding when filtered.

### Alpha
- Use **clean, intentional alpha** (no accidental semi-transparent halos).
- If your decal has crisp edges, consider slight feathering *inside* the edge (not outside it).

### Color & accessibility
KFM UI aims for cartographic clarity and accessibility:
- Design decals to remain readable in **high-contrast modes**
- Avoid color-only meaning; ensure shapes/contrast carry the message.
- Be careful with reds/greens and low-contrast pastels.

---

## 🧾 Provenance & licensing (non-negotiable)

KFM treats **metadata + citations as first-class**. That applies to visuals too. 🧠✨

### Per-decal metadata (recommended)
Alongside each decal, add a small metadata file:

```text
map-stamp-wetlands-512.png
map-stamp-wetlands-512.meta.yml
```

**Template** (`*.meta.yml`)
```yaml
id: map-stamp-wetlands-512
title: "Wetlands Stamp (512px)"
type: decal-texture
created: 2026-01-18
author: "<name/handle>"
license: "<SPDX id or text>"
source:
  kind: "original" # original | adapted | third-party
  url: "<link if applicable>"
  attribution: "<required attribution text>"
notes: >
  Where it is used, why it exists, and any constraints (e.g., map-only, story-only).
processing:
  - "Authored in <tool>"
  - "Exported as PNG (straight alpha)"
  - "Optional: optimized to runtime format via build step"
tags: [map, stamp, overlay, wetlands]
```

### Folder-level attribution (optional but nice)
Create an `ATTRIBUTION.md` that rolls up credits for anything third‑party.

> [!WARNING]
> No “mystery assets.” If we can’t explain where it came from and how we’re allowed to use it, it doesn’t ship.

---

## 🔁 Add a new decal (checklist)

1. **Design / author** the decal (prefer editable sources when needed).
2. **Export** a clean lossless raster (usually `.png`).
3. Add `*.meta.yml` (and attribution if third-party).
4. Keep it **small** and **purposeful**:
   - Is it reusable? Great.
   - Is it story-specific? Put it in `story/`.
5. Run the **asset build/optimization** step (whatever the repo uses).
6. Verify:
   - Looks good at different zoom levels
   - Works in high-contrast mode
   - No edge halos / bleeding
7. Reference it from the UI via the approved config/registry approach (no magical imports).

---

## 🧪 PR quality gates

- [ ] Filename follows conventions
- [ ] Provenance metadata included (`*.meta.yml`)
- [ ] License is compatible + attribution is present (if required)
- [ ] Reasonable size (no unbounded 4K textures “just because”)
- [ ] Works in dark/light + high-contrast modes
- [ ] Not tightly coupled to a single dataset unless placed under `story/` (or explicitly documented)

---

## 🔗 Related (conceptual)

- KFM’s “provenance-first” standard applies to **UI layers and overlays** too.
- When a decal is used to represent a dataset/map layer, ensure the **layer UI** (legend/info) exposes the dataset’s source and license.

> 🧭 If you’re unsure where a decal should live, prefer **generic + reusable** first, and only specialize when the UI story truly demands it.
