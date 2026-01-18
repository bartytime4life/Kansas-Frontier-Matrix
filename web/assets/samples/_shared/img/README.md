---
title: "🖼️ Shared Sample Images"
path: "web/assets/samples/_shared/img/README.md"
version: "v0.1.0"
status: "active"
last_updated: "2026-01-16"
license: "Per-asset (see Asset Registry)"
doc_kind: "Asset README"
---

# 🖼️ `_shared/img` — Shared Images for Sample Pages

![scope](https://img.shields.io/badge/scope-web%2Fassets-blue)
![usage](https://img.shields.io/badge/usage-samples-brightgreen)
![provenance](https://img.shields.io/badge/provenance-first-important)
![license](https://img.shields.io/badge/license-per--asset-yellow)

**Location:** `web/assets/samples/_shared/img/`  
**Goal:** One **canonical** place for images reused across multiple sample pages (icons, logos, UI screenshots, “hero” placeholders, etc.).

> [!NOTE]
> If an image is **sample-specific**, it should live in that sample’s own folder (e.g., `web/assets/samples/<sample_name>/img/`) — keep `_shared/` truly shared. ✅

---

## 📦 What belongs here?

Use this folder for:

- 🧩 **UI icons** (prefer `.svg`)
- 🏷️ **Logos / branding** used by multiple samples
- 🧭 **Common map thumbnails** and legend snippets used across demos
- 🖥️ **UI screenshots** used in docs or sample walkthroughs
- 🧪 **Demo placeholders** (generic images used for layout/testing)

Avoid putting:

- 🧨 Huge raw images (camera originals, uncompressed exports)
- 🧱 Build artifacts (auto-generated spritesheets, cache outputs)
- 🚫 Anything with unclear licensing or missing attribution

---

## 🧱 Folder map (expected pattern)

```text
web/
└─ 📁 assets/
   └─ 🧪 samples/
      └─ ♻️ _shared/
         └─ 🖼️ img/                  # 👈 you are here 📌 Tiny images used only by samples/demos (NOT canonical UI assets)
            ├─ 📄 README.md           # 📘 What belongs here, size limits, and naming/redaction rules
            └─ 🖼️ …                  # Icons, logos, screenshots, placeholders (keep small + license-noted)
```

---

## 🔗 How to reference these images

### ✅ From a sample page inside `web/assets/samples/<sample_name>/...`

Typical relative paths:

```html
<!-- Example: web/assets/samples/my_demo/index.html -->
<img
  src="../_shared/img/logo_kfm.svg"
  alt="Kansas Frontier Matrix logo"
/>
```

### ✅ In CSS

```css
/* Example: web/assets/samples/my_demo/styles.css */
.hero {
  background-image: url("../_shared/img/hero_placeholder.webp");
  background-size: cover;
  background-position: center;
}
```

### ✅ In JS

```js
const img = new Image();
img.src = "../_shared/img/ui_screenshot_panel.png";
img.alt = "Sample UI panel screenshot";
document.querySelector("#preview").appendChild(img);
```

> [!TIP]
> Prefer **relative paths** inside `web/` so GitHub Pages / static deployments don’t break when base URLs change.

---

## 🏷️ Naming conventions (keep it boring, predictable, searchable)

### ✅ File naming rules

- Use **lower_case_with_underscores**
- Use descriptive prefixes: `icon_`, `logo_`, `map_`, `ui_`, `hero_`, `photo_`
- Add size when relevant: `*_640w`, `*_1280w`, `@2x`
- Avoid spaces, avoid “final_v7_reallyfinal.png” 🙃

Examples:

- `logo_kfm.svg`
- `icon_layers.svg`
- `ui_timeline_panel.png`
- `hero_kansas_skyline_1280w.webp`
- `map_smoky_hill_river_thumbnail_640w.jpg`

---

## 🧰 Formats & best choices

### 🟩 Prefer: SVG (icons / diagrams / logos)
**Use when:** crisp scaling is needed, icons, simple illustrations.

✅ Checklist:
- Ensure `viewBox` is set  
- Remove editor metadata if possible  
- Keep paths clean (no hidden layers)

### 🟦 PNG (UI screenshots / sharp edges)
**Use when:** text/UI needs pixel-perfect clarity.

✅ Checklist:
- Crop tight
- Optimize before commit (PNG can balloon fast)

### 🟧 JPEG (photography)
**Use when:** photos/continuous tone images.

✅ Checklist:
- Reasonable quality (avoid max-quality exports)
- Consider WebP for smaller size

### 🟪 WebP (preferred for “hero” images)
**Use when:** large background / hero imagery and you want smaller downloads.

✅ Checklist:
- Provide a fallback if your sample needs legacy compatibility

---

## ⚡ Performance rules (samples should load fast)

**Targets (guidelines):**
- Icons/logos: **< 50 KB**
- UI screenshots: **< 250 KB**
- Hero images: **< 500 KB** (or less if possible)

> [!WARNING]
> If you add an image bigger than ~1 MB, add a note in the Asset Registry explaining why. Large assets slow demos and increase repo weight.

---

## ♿ Accessibility rules

- Every `<img>` must have meaningful `alt` text **unless** purely decorative.
- Decorative images: use empty alt `alt=""` and avoid confusing screen readers.
- Don’t embed critical text inside images unless you also provide the text in HTML nearby.

Example:

```html
<img src="../_shared/img/icon_layers.svg" alt="Layers icon" />
<img src="../_shared/img/ui_banner.png" alt="" aria-hidden="true" />
```

---

## 🔎 Provenance & licensing (non-negotiable ✅)

Treat images like **first-class assets**:

1. **Know the source** (created in-house, public domain, CC, dataset export, etc.)
2. **Record the license** and attribution requirements
3. **Record transformations** if the asset is derived (cropped, recolored, annotated)

### Option A: Sidecar metadata file (recommended)
For each image `X.ext`, add `X.meta.yml`.

<details>
<summary><strong>🧾 Suggested <code>.meta.yml</code> template</strong></summary>

```yaml
# Example: logo_kfm.svg.meta.yml
asset:
  file: "logo_kfm.svg"
  kind: "logo"
  used_in:
    - "web/assets/samples/*"
  source:
    origin: "in_house"   # in_house | external | derived
    url: ""              # if external
    license: "TBD"
    attribution: "TBD"
  provenance:
    created_by: "TBD"
    created_on: "TBD"
    modified_on: "2026-01-16"
    tools:
      - "inkscape"
      - "svgo"
    derived_from: []
  notes: "Shared logo for sample pages."
```

</details>

### Option B: Track everything in the registry table below
If you don’t want sidecars, keep the table up to date **religiously**.

---

## ✅ Adding a new image (Definition of Done)

- [ ] Correct location (`_shared/` vs sample-specific folder)
- [ ] Correct name (`lower_case_with_underscores`)
- [ ] File size is reasonable (optimized)
- [ ] `alt` text plan is clear (where/how it will be used)
- [ ] Source + license recorded (sidecar `.meta.yml` or registry)
- [ ] If derived, note what changed (crop, recolor, annotate, etc.)

---

## 📚 Asset Registry (keep this updated)

| File | Type | Purpose | Source / License | Notes |
|---|---|---|---|---|
| `logo_kfm.svg` | SVG | Shared logo used by multiple demos | TBD | Add `logo_kfm.svg.meta.yml` |
| `icon_layers.svg` | SVG | Toolbar icon (layers toggle) | TBD | Keep under 50 KB |
| `ui_timeline_panel.png` | PNG | Screenshot for demo walkthroughs | TBD | Crop tight, reduce size |

> [!TIP]
> If an asset is used as “evidence” (charts, maps, historical imagery), include the **data/source reference** in its metadata so it stays auditable.

---

## 🧹 Housekeeping

- Prefer **fewer shared assets** over dumping everything here.
- Remove unused assets when sample pages are retired.
- Keep the folder tidy: if a new category grows, consider subfolders like:
  - `icons/`, `logos/`, `screenshots/`, `photos/`

---
