# 📣 KFM Social Branding Assets

[![KFM](https://img.shields.io/badge/KFM-Living%20Atlas-2ea44f?style=for-the-badge)](../../../../../README.md)
[![Brand](https://img.shields.io/badge/Brand-Social%20Kit-blue?style=for-the-badge)](./README.md)
[![Provenance](https://img.shields.io/badge/Provenance-First-important?style=for-the-badge)](../../../../../docs/MASTER_GUIDE_v13.md)

> [!NOTE]
> **KFM is “provenance-first.”** Social graphics should be as *auditable* as the platform: cite sources, avoid black-box claims, and keep media traceable back to its data + design origins. 🧾🧭

---

## 📌 Quick links

- ↩️ **Branding root:** `../README.md`
- 🧭 **Project root:** `../../../../../README.md`
- 🧾 **License:** `../../../../../LICENSE`
- 🧠 **Story Nodes (governed narrative assets):** `../../../../../docs/reports/story_nodes/`

---

## 🎯 What this folder is for

This directory contains **social-ready** media for Kansas Frontier Matrix (KFM), including:

- 🧑‍🎨 **Profile / avatar** images (light + dark variants)
- 🏞️ **Headers / banners** (safe-area friendly)
- 🔗 **Share cards** (Open Graph / link previews)
- 🧩 **Post templates** (square / portrait / landscape)
- 🎞️ **Short motion assets** (stingers, lower-thirds, intro/outro)

### ✅ Design goals

- **Consistency:** recognizable KFM look across platforms
- **Traceability:** every asset should be attributable (design + data provenance)
- **Accessibility:** readable type, strong contrast, alt-text friendly
- **Performance:** optimized file sizes without visible artifacts

---

## 🧭 “Provenance-first” in social graphics

When a social graphic includes **maps, charts, satellite imagery, or historical material**, it must preserve traceability:

- Include a **source line** somewhere (small footer text is fine) **or** include a **post caption** with the source(s).
- If content is derived, include a short **“Derived from …”** note in the metadata sidecar (see below).
- Prefer **links into KFM** (Story Node / layer / dataset page) over external links when possible.

> [!TIP]
> The best social content is **evidence-first**: *what you’re showing* + *where it came from* + *how to verify it*. ✅

---

## 🗂️ Recommended directory layout

Keep this folder tidy and predictable. If some folders don’t exist yet, create them as assets are added.

```text
📁 web/assets/media/branding/social/
├── 📄 README.md
├── 📄 manifest.social.json               # optional: index of assets + usage + provenance pointers
│
├── 📁 avatars/                           # profile images
│   ├── 🖼️ kfm-avatar--icon--light@1x.png
│   ├── 🖼️ kfm-avatar--icon--light@2x.png
│   ├── 🖼️ kfm-avatar--icon--dark@1x.png
│   └── 🖼️ kfm-avatar--icon--dark@2x.png
│
├── 📁 headers/                           # cover images / banners
│   ├── 🖼️ kfm-header--default--light.png
│   └── 🖼️ kfm-header--default--dark.png
│
├── 📁 og/                                # link preview cards (OpenGraph)
│   ├── 🖼️ kfm-og--default.png
│   ├── 🖼️ kfm-og--release.png
│   └── 🖼️ kfm-og--story-node.png
│
├── 📁 templates/
│   ├── 📁 post-square/                   # 1:1
│   ├── 📁 post-portrait/                 # 4:5 / 9:16 variants, etc.
│   ├── 📁 post-landscape/                # 16:9
│   └── 📁 thumbnails/
│
├── 📁 video/
│   ├── 🎞️ stingers/
│   ├── 🎞️ lower-thirds/
│   └── 🎞️ loops/
│
└── 📁 _masters/                          # ⚠️ optional: editable sources (Figma exports, SVG masters, etc.)
    ├── 🧩 kfm-social-template--square.svg
    └── 🧩 kfm-social-template--og.svg
```

> [!IMPORTANT]
> If `_masters/` contains **large** files (design sources), keep them minimal and consider storing originals in a dedicated design repo or artifact store — but keep **exported** deliverables here.

---

## 🏷️ Naming conventions

Use predictable names so assets can be referenced in code, docs, and automation.

### ✅ Suggested pattern

`kfm-<group>--<asset>--<variant>[@<scale>].<ext>`

Examples:

- `kfm-avatar--icon--light@2x.png`
- `kfm-header--default--dark.png`
- `kfm-og--release--v1.png`
- `kfm-template--post-square--base.svg`

### Rules

- Use **kebab-case** and **double-dash** separators (`--`) for readability
- Variants: `light | dark | mono | outline | filled | hi-contrast`
- Scales: `@1x`, `@2x` (retina), optionally `@3x` for icons only
- Version when needed: `--v1`, `--v2` (prefer versioning over overwriting widely-used files)

---

## 🧾 File formats and when to use them

| Format | Use for | Notes |
|---|---|---|
| `.svg` | masters, logos, templates | ✅ best for crisp type + vector shapes |
| `.png` | transparency, UI-safe exports | ✅ predictable rendering across platforms |
| `.webp` | web-optimized previews | ✅ smaller than PNG; verify platform support |
| `.jpg` | photos (no transparency) | ✅ smaller than PNG for photo-heavy assets |
| `.mp4` | short motion assets | ✅ universal-ish playback |
| `.webm` | web delivery | ✅ often smaller; not always supported on every platform |

> [!TIP]
> Default to **SVG master → PNG/WebP exports**.

---

## 📐 Composition & safe-area guidelines

Social platforms crop aggressively. Design with **safe areas**:

- Keep **logos + titles** away from edges
- Assume **center-crop** for avatars and some previews
- Avoid tiny text: if you must include it, treat it as **optional**, not essential

### Type & legibility

- Use **large text** and short headlines
- Prefer **high-contrast** overlays over map imagery
- Avoid thin font weights on busy backgrounds

---

## 📊 Charts, maps, and data-viz rules

When exporting social graphics that include data:

- Label **axes with quantity + unit** (if there are axes) 📏
- Note **uncertainty / error bounds** when relevant (or link to details)
- Keep units consistent (don’t mix units without explicit conversions)
- If a number is derived, note the **method** in metadata (or in the Story Node)

> [!NOTE]
> When in doubt, link to a **Story Node** or a KFM page where details + citations live.

---

## ♿ Accessibility checklist

**Every** social post should be accessible *by default*:

- ✅ Provide **alt text** (or a caption that describes the image)
- ✅ Avoid color-only meaning (use icons/labels/patterns)
- ✅ Keep contrast strong (especially over maps)
- ✅ For video: **captions** or burned-in subtitles for short clips

---

## 🧬 Provenance metadata (recommended)

For each exported asset, add a tiny sidecar file:

- `kfm-og--release--v1.png`
- `kfm-og--release--v1.meta.json`

### Minimal `.meta.json` template

```json
{
  "id": "kfm-og--release--v1",
  "title": "KFM Release Share Card (v1)",
  "type": "og",
  "variant": "default",
  "language": "en",
  "license": "SEE_REPO_LICENSE",
  "created_by": "KFM Contributors",
  "exported_from": "web/assets/media/branding/social/_masters/kfm-og--release.svg",
  "data_sources": [
    {
      "label": "Example Dataset / Layer",
      "ref": "STAC/DCAT/PROV reference or URL/path"
    }
  ],
  "notes": "Short explanation of what changed or how the asset is intended to be used."
}
```

> [!TIP]
> If an asset uses map layers, include references to **catalog artifacts** (STAC/DCAT/PROV) or the Story Node that cites them.

---

## 🔁 Asset pipeline (suggested)

```mermaid
flowchart LR
  A[🧩 Master Template (SVG/Figma)] --> B[🖼️ Export PNG/WebP/JPG]
  B --> C[🧬 Add .meta.json provenance]
  C --> D[🧾 Update manifest.social.json]
  D --> E[✅ Review & approve]
  E --> F[🚀 Use in posts / site OG tags]
```

---

## ✅ Review gates (before publishing)

### Quick QA checklist

- [ ] Looks good on **light & dark** backgrounds
- [ ] Text remains readable when viewed **small**
- [ ] Cropping doesn’t remove key info (center-crop check)
- [ ] File size is reasonable (avoid multi‑MB images unless necessary)
- [ ] Provenance is present (footer source line, caption, or `.meta.json`)
- [ ] No sensitive locations disclosed (redact/generalize if needed)

---

## 🤝 Contributing a new social asset

1. 🧩 Add/Update a master template in `_masters/`  
2. 🖼️ Export deliverables into the correct folder (`avatars/`, `og/`, `templates/`, etc.)  
3. 🧬 Add a `.meta.json` sidecar (recommended)  
4. 🧾 Update `manifest.social.json` (if used)  
5. ✅ Run quick checks (readability, crop safety, file size)  
6. 📌 Reference the asset in docs or UI where relevant

---

## 📎 “Do / Don’t” (brand integrity)

| ✅ Do | ❌ Don’t |
|---|---|
| Keep logos crisp and unwarped | Stretch, skew, or re-color the logo arbitrarily |
| Use approved light/dark variants | Put dark logo on dark imagery (or vice versa) |
| Cite map/data sources | Post map claims with no attribution |
| Keep safe margins | Put critical text at edges |

---

## 🧯 Legal & attribution

- Only include media you have the rights to use.
- Respect dataset licenses and attribution terms.
- Avoid using third-party trademarks/logos unless explicitly permitted.

---

## 📬 Where to ask questions

- Open a GitHub issue tagged `branding` or `social-assets`
- Or post in the project’s collaboration channel (if configured)

💛 Keep it clean. Keep it verifiable. Keep it KFM.
