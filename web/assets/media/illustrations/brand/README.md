# 🎨 Brand Illustrations (Kansas Frontier Matrix)

![scope](https://img.shields.io/badge/scope-brand%20illustrations-blue?style=flat-square)
![format](https://img.shields.io/badge/prefer-SVG%20first-success?style=flat-square)
![a11y](https://img.shields.io/badge/a11y-required-important?style=flat-square)
![principle](https://img.shields.io/badge/principle-provenance--first-6f42c1?style=flat-square)

> 📍 **Folder:** `web/assets/media/illustrations/brand/`  
> 🧭 **Purpose:** Official **KFM** brand artwork used in the **web UI** and **public-facing** materials.

---

## 🧭 What “brand” means in KFM

KFM’s core promise is **trust through transparency**: users should be able to understand *what they’re seeing*, where it came from, and what it means.  
Brand visuals should reinforce that promise — **clear, calm, legible, and consistent** 🧠🗺️

This folder keeps **brand-level** visuals separate from:
- UI illustrations (feature art, onboarding, empty-states)
- UI icons (toolbars, map controls)
- Dataset thumbnails and story-node assets

---

## ✅ What belongs here

Keep this folder *small and “official”* 🔒

**Typical contents:**
- 🧩 **Logomarks** (icon-only)
- 🔤 **Wordmarks** (text-only)
- 🧷 **Lockups** (mark + wordmark combos)
- 🌐 **OpenGraph / Social share images** (default OG)
- 🏷️ **App icons / favicons** (exported)
- 🧾 **Press kit exports** (if your repo includes them)

---

## 🚫 What does NOT belong here

Put these elsewhere (usually under `web/assets/...` or Story Node assets folders):

- 🗺️ Map symbology / layer icons (belongs with the map UI system)
- 🎛️ UI control icons (zoom, draw tools, filters)
- 📚 Narrative images unique to a Story Node (belongs in Story Node `assets/`)
- 📊 Charts, data previews, dataset thumbnails (belongs with dataset/story artifacts)

---

## 📁 Suggested folder layout

> If your repo already has a preferred layout, follow that. Otherwise, this structure keeps things sane ✅

```text
📁 web/
└─ 📁 assets/
   └─ 📁 media/
      └─ 📁 illustrations/
         └─ 📁 brand/
            ├─ 📄 README.md
            ├─ 📁 logos/              # canonical SVGs (source of truth)
            ├─ 📁 lockups/            # horizontal/stacked combinations
            ├─ 📁 favicon/            # favicon.svg + PNG exports
            ├─ 📁 social/             # og-default, social share templates
            ├─ 📁 raster/             # PNG exports for email/docs if needed
            └─ 📁 source/             # editable originals (Figma/AI/etc), if tracked
```

---

## 🏷️ Naming conventions

**Goals:** predictable imports, easy searching, clean diffs.

### ✅ Do
- Use **kebab-case**: `kfm-wordmark-dark.svg`
- Include **variant** in filename: `light`, `dark`, `mono`, `color`
- Include **size** for raster exports: `-512`, `-1024` or `@2x`

### 🚫 Don’t
- Don’t use spaces: `KFM Logo Final FINAL.svg`
- Don’t omit variants: `logo.svg` (too ambiguous)
- Don’t bake environment names into filenames: `logo-prod.svg`

### Suggested pattern

```text
<product>-<asset>-<variant>.<ext>

Examples:
kfm-mark-mono.svg
kfm-wordmark-dark.svg
kfm-lockup-horizontal-light.svg
kfm-og-default-1200x630.png
```

---

## 🧩 File formats & export rules

### SVG (preferred) ✅
- Use **SVG** for the web UI whenever possible.
- Ensure a proper `viewBox` so it scales cleanly.
- Avoid hard-coded `width/height` unless required by a build tool.
- Optimize before committing (strip editor junk, metadata blobs, unused defs).

**Accessibility for inline SVG** (recommended when the logo conveys meaning):
- include `<title>` and optionally `<desc>`
- set `role="img"`
- reference ids via `aria-labelledby`

```html
<svg role="img" aria-labelledby="kfmTitle kfmDesc" viewBox="0 0 256 64">
  <title id="kfmTitle">Kansas Frontier Matrix</title>
  <desc id="kfmDesc">KFM wordmark</desc>
  <!-- paths here -->
</svg>
```

### PNG (exports) 🖼️
Use PNG for:
- social images (OG)
- places that **can’t** render SVG safely (some email clients, certain CMS embeds)

**Guidelines**
- Prefer transparent backgrounds where possible
- Export at common sizes (and/or `@2x`):
  - icons: 16, 32, 48, 64, 128, 256
  - app/icon: 512, 1024
  - OpenGraph: 1200×630

---

## 🌗 Theme + contrast expectations

Brand assets must remain legible over:
- light UI chrome ☀️
- dark UI chrome 🌙
- map imagery (busy backgrounds) 🗺️

**Recommended variants**
- `mono` (single color, CSS-themeable if inline)
- `light` (for dark backgrounds)
- `dark` (for light backgrounds)
- `color` (only where a fixed palette is explicitly required)

> 💡 If you can safely make a mark `currentColor` in SVG, do it — it makes theme + contrast handling dramatically easier.

---

## 🧾 Provenance & licensing

KFM is provenance-first in spirit — and brand assets still need clean origins ✅

### Minimum requirements for any new brand asset
- Track **source file** (Figma/AI/etc) OR record its origin
- Record **license / usage rights** (especially for fonts or third-party shapes)
- Record **export steps** (so we can reproduce and update it)

### Optional: sidecar metadata (recommended)
If your repo supports it, store a `*.meta.json` beside the asset:

```json
{
  "id": "kfm-wordmark-dark",
  "type": "wordmark",
  "variant": "dark",
  "source": {
    "tool": "Figma",
    "file": "source/kfm-brand.fig",
    "export": "SVG export + svgo optimize"
  },
  "license": {
    "kind": "repo-license-or-brand-policy",
    "notes": "Confirm trademark usage policy before external redistribution"
  },
  "updated_at": "YYYY-MM-DD",
  "notes": "Works on light backgrounds, minimum 120px width recommended"
}
```

---

## 🧪 Contribution checklist (Definition of Done ✅)

When adding/updating brand assets:

- [ ] File name follows conventions (`kfm-…-variant.ext`)
- [ ] SVG has valid `viewBox` and scales cleanly
- [ ] SVG optimized (no editor junk / unnecessary metadata)
- [ ] Looks good on **light + dark** UI backgrounds
- [ ] Looks acceptable over **map imagery**
- [ ] Accessibility handled (alt text for `<img>`, or `title/desc` for inline SVG)
- [ ] Licensing/provenance recorded (in PR description or sidecar metadata)
- [ ] If you changed a canonical logo: include a screenshot diff 📸

---

## 🧰 Usage examples

### Basic `<img>` (safe default)
```html
<img
  src="/assets/media/illustrations/brand/logos/kfm-wordmark-dark.svg"
  alt="Kansas Frontier Matrix"
/>
```

### Decorative usage (no screen reader noise)
```html
<img
  src="/assets/media/illustrations/brand/logos/kfm-mark-mono.svg"
  alt=""
  aria-hidden="true"
/>
```

---

## 🔗 Related (recommended) docs

- 📘 `docs/MASTER_GUIDE_v13.md` — repo structure, invariants, governance
- ⚖️ `docs/governance/ETHICS.md` + `docs/governance/SOVEREIGNTY.md` — visual/data handling constraints
- 🌐 `web/` — frontend application (React + map UI)
- 🧾 `LICENSE` / `TRADEMARKS` (if present) — what you can ship where

---

## 🧠 Quick FAQ

<details>
  <summary><strong>Should brand assets be used as “evidence” in Story Nodes?</strong></summary>

No. Brand art is **decorative/identity** content. Evidence must remain provenance-linked, cited, and cataloged through the normal pipeline.

</details>

<details>
  <summary><strong>Where do Story Node images go?</strong></summary>

Inside the Story Node’s own `assets/` folder (keeps narratives portable and governed).

</details>

<details>
  <summary><strong>Where do UI icons go?</strong></summary>

In the dedicated UI icon system folder (keep “brand” minimal and stable).

</details>
