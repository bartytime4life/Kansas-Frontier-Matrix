# 🧵 Textures — Source Assets (`_sources`)  

![asset](https://img.shields.io/badge/assets-textures-informational)
![pipeline](https://img.shields.io/badge/pipeline-contract--first%20%26%20provenance--first-success)
![rules](https://img.shields.io/badge/rule-no%20mystery%20layers-critical)
![target](https://img.shields.io/badge/target-web%20%2F%20WebGL%20%2F%20Map%20UI-blue)

> ✅ **Purpose:** this folder holds **high-quality, editable “source textures”** plus **provenance metadata**.  
> ⚙️ **Build output:** optimized/runtime textures should be generated elsewhere (typically `web/assets/media/textures/` or similar).  
> 🔎 **Non‑negotiable:** **no texture ships without a metadata contract** (license + source + processing steps). [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🗺️ Where this sits in the repo

```text
🌐 web/
└─ 🧰 assets/
   └─ 🖼️ media/
      ├─ 🧪 _sources/
      │  └─ 🧵 textures/   👈 you are here
      │     ├─ 🧱 materials/
      │     ├─ 🏞️ terrain/
      │     ├─ 🎛️ ui/
      │     ├─ 🧩 decals/
      │     ├─ 🌌 skyboxes/
      │     └─ README.md
      └─ ⚙️ textures/      (generated / optimized runtime assets)
```

This matches KFM’s “clean separation” philosophy: **source → governed contracts → generated outputs → UI** (no leapfrogging). [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔒 Provenance-first rule (KFM-style)

KFM’s core trust model is: **anything that appears in the UI must be traceable back to cataloged sources and provable processing**—and **unsourced assets are not allowed** (“no mystery layers”). We apply the same rule to textures. [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### ✅ What that means here
- Every texture **MUST** include a **sidecar metadata file** (a “media contract”).
- Metadata **MUST** include at minimum:
  - **source** (URL / archive reference / creator)
  - **license** (and attribution requirements)
  - **processing steps** (what we changed + tools used)
- CI should reject textures missing required metadata fields (same enforcement principle as KFM data validators). [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧾 Texture “Media Contract” (sidecar metadata)

### 📄 File naming
For every texture file, add a matching metadata file:

```text
my_texture_basecolor_2048.png
my_texture_basecolor_2048.meta.json
```

> Tip: keep the **metadata filename identical** to the texture filename, plus `.meta.json`. It makes automation trivial.

### 🧩 Minimal schema (example)
```json
{
  "id": "kfm.mat.limestone.01",
  "title": "Limestone Material 01",
  "category": "materials",
  "maps": ["basecolor", "normal", "roughness", "ao"],
  "source": {
    "type": "original|scan|third-party",
    "url": "https://…",
    "author": "Name / Org",
    "retrieved_at": "2026-01-17"
  },
  "license": {
    "spdx": "CC0-1.0|CC-BY-4.0|CC-BY-SA-4.0|MIT|…",
    "attribution": "Required credit line (if any)",
    "notes": "Any restrictions (NC/ND not allowed unless explicitly approved)"
  },
  "processing": [
    "Cropped to tile cleanly",
    "Generated normal map from height",
    "Exported optimized WebP"
  ],
  "checksums": {
    "sha256": "…"
  },
  "usage": {
    "intended_for": ["webgl", "ui", "map-overlay"],
    "notes": "Where/why it’s used"
  }
}
```

### 🤖 Why the contract matters
KFM’s documentation explicitly highlights that contract-first metadata enables **automatic attribution/credits** and **method traces** when presenting combined content. [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

So: if we keep this metadata clean, the UI can later generate:
- a **Credits** panel ✅  
- a **“What’s this texture?”** provenance inspector ✅  
- a **build report** mapping textures → usage ✅  

---

## 🧱 Folder conventions

Use these subfolders to keep the library navigable:

- `🧱 materials/` — PBR materials (rock, soil, metal, wood, etc.)
- `🏞️ terrain/` — terrain patterns, hillshade overlays, noise masks, slope ramps
- `🎛️ ui/` — UI backgrounds, panels, subtle patterns, UI-only textures
- `🧩 decals/` — stamps, labels, icons-as-textures, marker atlases
- `🌌 skyboxes/` — equirect HDR/EXR sources + derived cubemap faces
- `🧪 _incoming/` (optional) — staging area for new assets until metadata is complete

> 🧠 Keep “source truth” here. Keep “runtime outputs” elsewhere.

---

## 🏷️ Naming conventions (stable + searchable)

### ✅ General rules
- **lowercase**
- **kebab-case** or **snake_case** (pick one and stick to it)
- no spaces, no special characters
- include **map type** + **resolution**
- include **variant** if multiple similar assets exist

### 🧾 Suggested pattern
```text
kfm_<domain>_<asset>__<map>_<res>.<ext>
```

Examples:
```text
kfm_mat_soil_loam__basecolor_2048.png
kfm_mat_soil_loam__normal_2048.png
kfm_mat_soil_loam__roughness_2048.png
kfm_ui_papergrain__mask_1024.png
kfm_terrain_hillshade__overlay_4096.png
```

### 🗂️ Common map suffixes
| Map | Suffix | Notes |
|---|---|---|
| Base Color / Albedo | `basecolor` | **sRGB** |
| Normal | `normal` | **linear**, tangent-space |
| Roughness | `roughness` | **linear** |
| Metallic | `metallic` | **linear** |
| Ambient Occlusion | `ao` | **linear** |
| Height/Displacement | `height` | **linear** |
| Emissive | `emissive` | sRGB (usually) |
| Opacity/Alpha | `opacity` / `alpha` | choose one and be consistent |
| Mask (UI) | `mask` | typically linear |

---

## 🖼️ Formats & export guidance (web-friendly)

### ✅ Source formats (good for editing)
- `.psd`, `.kra`, `.tif` — layered masters
- `.exr` / `.hdr` — skyboxes / lighting sources
- `.svg` — vector patterns/icons (when applicable)

### ✅ Runtime formats (good for shipping)
- `.webp` — great default for UI patterns & many textures
- `.png` — when alpha quality must be perfect (or lossless is required)
- `.jpg` — large photos with no alpha
- `ktx2` (optional) — best-in-class for GPU-friendly compressed textures when we adopt it

### 🎯 Performance tips (keep WebGL happy)
- Prefer **power-of-two** sizes (512/1024/2048/4096) when mipmaps are needed.
- Don’t ship 8K unless there’s a proven need (and memory budget is clear).
- Keep “detail” textures tiling and small where possible (repeat patterns beat giant images).

---

## 🧪 Build pipeline expectations

KFM’s canonical approach is a strict pipeline ordering—**no bypassing governed contracts** before content hits UI. [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

For textures, treat this as the non-negotiable order:

```text
🧵 Source Texture → 🧾 Media Contract → ⚙️ Optimization → 🧾 Manifest → 🌐 UI usage
```

### Suggested automation goals
- Generate optimized outputs to `web/assets/media/textures/`
- Generate a `textures.manifest.json` (id → paths → attribution)
- Fail CI if:
  - metadata missing
  - license missing/invalid
  - forbidden license (e.g., unknown provenance or incompatible terms)

---

## ⚖️ Licensing & attribution (no surprises)

KFM emphasizes **license transparency**, including a license field per asset and correct attribution when combining sources. [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### ✅ Allowed (recommended)
- **CC0** (best)
- **CC-BY 4.0** (ok; attribution required)
- **CC-BY-SA 4.0** (ok; share-alike implications must be understood)

### 🚫 Avoid by default
- **NC / ND** licenses (non-commercial / no-derivatives) unless explicitly approved
- “unknown license”
- ripped game/film assets (hard no)

### 🧩 Combining assets
If you composite multiple sources into one derived texture, treat the result as governed by the **most restrictive compatible** license and record all upstream sources in metadata. [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📦 Large binaries (Git size discipline)

Some assets can get big fast. KFM planning documents propose using **DVC** for large artifacts to avoid bloating Git while keeping version/data relationships tracked. [oai_citation:9‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

### Practical rule of thumb
- If a single source texture (or master) is **huge** (e.g., layered `.psd`), prefer:
  - Git LFS **or**
  - DVC (if the repo standardizes on it)
- Still commit the **metadata contract** in Git so provenance is always available.

---

## ✅ PR checklist (add a new texture)

- [ ] Texture placed in the correct subfolder (`materials/`, `ui/`, etc.)
- [ ] Filename follows convention (`__map_res`)
- [ ] Sidecar metadata exists: `*.meta.json`
- [ ] Metadata includes **source + license + processing steps**
- [ ] If derived/composited: upstream sources listed clearly
- [ ] Optimized runtime outputs generated (if our pipeline expects it)
- [ ] Visual sanity check (seams, gamma, compression artifacts)

---

## 🧠 FAQ

<details>
  <summary><strong>Why do we treat textures like “data”?</strong> 📚</summary>

KFM is built on **provenance-first** principles: anything presented to users should be auditable and source-linked. Textures influence interpretation (maps, terrain, UI cues), so they must be governed the same way. [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

</details>

<details>
  <summary><strong>What’s the fastest way to add attribution correctly?</strong> 🧾</summary>

Put the full credit line into `license.attribution` and keep `source.url` accurate. This enables automated credit generation later (a KFM design goal). [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

</details>

---

## 📚 Sources (project files)

- KFM contract-first & provenance-first principles (no “mystery layers”). [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- KFM license transparency & combining licensing constraints. [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- KFM v13 pipeline ordering + `web/` as UI boundary (directory layout). [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- Large artifact versioning direction (DVC) from KFM design doc. [oai_citation:19‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)  [oai_citation:20‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)  
