# 🏷️ Logos (Brand + Partners)

![Format](https://img.shields.io/badge/format-SVG%20preferred-2ea44f?style=flat-square)
![Fallback](https://img.shields.io/badge/fallback-PNG%402x-blue?style=flat-square)
![Provenance](https://img.shields.io/badge/provenance-required-critical?style=flat-square)
![A11y](https://img.shields.io/badge/accessibility-alt%20%2B%20ARIA-important?style=flat-square)

This folder contains **logo assets** used by the KFM web UI (project branding, partner marks, sponsor marks, etc.).  
Logos are *not* the same thing as UI glyph icons: keep **brand marks** here so they can be managed with clear **licensing, attribution, and provenance**.

---

<details>
  <summary><strong>📚 Contents</strong> (click to expand)</summary>

- [🧭 What belongs here](#-what-belongs-here)
- [✅ Golden rules](#-golden-rules)
- [🗂️ Recommended folder structure](#️-recommended-folder-structure)
- [🧾 Provenance manifest](#-provenance-manifest)
- [🏷️ Naming conventions](#️-naming-conventions)
- [🧪 Variants (light/dark/mono)](#-variants-lightdarkmono)
- [🖼️ Formats + export rules](#️-formats--export-rules)
- [⚡ Optimization](#-optimization)
- [♿ Accessibility rules](#-accessibility-rules)
- [📜 Licensing + attribution](#-licensing--attribution)
- [🧰 Usage examples](#-usage-examples)
- [🧩 Add a new logo (PR checklist)](#-add-a-new-logo-pr-checklist)

</details>

---

## 🧭 What belongs here

✅ **Put in this folder:**
- KFM brand marks (mark + lockups)
- Partner/sponsor organization logos (with explicit permission / license)
- “Powered by …” marks used in footers, credits, onboarding, etc.

🚫 **Do NOT put in this folder:**
- UI glyph icon sets (arrows, pins, buttons) → those belong in `web/assets/media/icons/…`
- One-off images for docs/blog posts → those belong in a docs/media directory
- Any asset with unknown origin → *no “mystery logos”*

---

## ✅ Golden rules

> [!IMPORTANT]
> **No provenance = no merge.** Every logo must have a source/creator, license, and attribution recorded.

- **SVG-first**: use `.svg` whenever possible for crisp rendering at any DPI.
- **Stable references**: treat logo IDs as stable (your app code should reference a stable ID, not a fragile filename).
- **Accessibility**: every usage must have meaningful `alt` text (or be explicitly decorative).
- **Licensing clarity**: if we can’t redistribute it, it can’t live here.

---

## 🗂️ Recommended folder structure

> [!NOTE]
> This is the *suggested* structure for scalability—use what the repo already does, but keep it tidy.

```text
web/
  assets/
    media/
      icons/
        logos/
          README.md
          logos.manifest.json        🧾 provenance + licensing + attribution
          kfm/                       🟩 first-party brand
            kfm-mark.svg
            kfm-lockup.svg
            kfm-lockup-mono.svg
          partners/                  🤝 third-party marks (with permission)
            usgs.svg
            nasa.svg
          sponsors/                  💛 sponsor marks (if applicable)
            example-sponsor.svg
```

---

## 🧾 Provenance manifest

KFM is **provenance-first**. Apply the same “data contract” thinking to UI media:  
**every logo must be described by metadata** so the system can generate attribution/credits and avoid unsourced assets.

Create/maintain: `logos.manifest.json`

### Minimal manifest shape

```jsonc
[
  {
    "id": "kfm.primary",                 // stable identifier used by code
    "file": "kfm/kfm-lockup.svg",        // relative path from this folder
    "title": "Kansas Frontier Matrix",
    "kind": "first_party",               // first_party | partner | sponsor
    "variant": "primary",                // primary | mono | dark | light | etc
    "license": {
      "spdx": "CC-BY-4.0",               // or "Proprietary", "Public-Domain", etc
      "url": "https://example.com/license"
    },
    "source": {
      "type": "internal",                // internal | external
      "url": "https://example.com/source", // required if external
      "notes": "Created by KFM design team"
    },
    "attribution": "KFM Contributors",
    "alt": "Kansas Frontier Matrix logo"
  }
]
```

> [!TIP]
> If a logo is used in multiple contexts (header/footer/loading), keep **one** canonical `id`, then add extra fields like `usage: ["header","footer"]` rather than duplicating files.

---

## 🏷️ Naming conventions

**Files**
- Use **kebab-case**: `kfm-lockup.svg`, `usgs.svg`, `example-sponsor.svg`
- No spaces. No version numbers in filenames unless required by the licensor.
- Keep filenames short; the *stable ID* lives in the manifest.

**Stable IDs (recommended)**
- Use dot-namespace IDs that rarely change:
  - `kfm.primary`
  - `partner.usgs`
  - `sponsor.example`
- Code should reference the **ID**, and your loader/registry resolves it to a file path.

---

## 🧪 Variants (light/dark/mono)

If a logo needs multiple treatments, use **explicit variants** instead of hacks:

- `*-mono.svg` → single-color, ideally compatible with `currentColor`
- `*-dark.svg` → tuned for dark backgrounds
- `*-light.svg` → tuned for light backgrounds

> [!WARNING]
> Don’t “fix” contrast in CSS with filters unless you have to—create correct variants instead.

---

## 🖼️ Formats + export rules

### ✅ Preferred: SVG
Your SVG should:
- Include a `viewBox`
- Avoid embedded raster images unless unavoidable
- Be clean/minified (see [Optimization](#-optimization))

### ✅ Allowed: PNG (fallback)
Use PNG only when:
- The source logo is not legally or practically convertible to SVG, **or**
- The logo depends on effects that don’t survive SVG simplification

If using PNG:
- Provide at least `@2x` (retina) resolution
- Keep transparency where appropriate
- Keep filesize tight (compress)

---

## ⚡ Optimization

Suggested tooling (choose what your repo already uses):
- `svgo` for SVG optimization
- `oxipng` or `pngquant` for PNG optimization

Example npm scripts:
```jsonc
{
  "scripts": {
    "optimize:logos": "svgo -f web/assets/media/icons/logos --config=svgo.config.js",
    "lint:logos": "node scripts/validate-logos-manifest.js"
  }
}
```

---

## ♿ Accessibility rules

Every logo in UI must be one of:

✅ **Informative** (most logos)
- Provide meaningful `alt`, e.g.  
  `alt="United States Geological Survey (USGS) logo"`

✅ **Decorative** (rare)
- Use empty alt: `alt=""`  
- AND ensure it’s not the only way to convey meaning.

Recommended HTML:
```html
<img
  src="/assets/media/icons/logos/partners/usgs.svg"
  alt="United States Geological Survey (USGS) logo"
  height="28"
/>
```

If the logo is inside a link, consider:
- `aria-label="Visit USGS website"` on the link when needed
- Keep the logo’s alt concise (avoid repeating surrounding text)

---

## 📜 Licensing + attribution

> [!IMPORTANT]
> **A logo is not “free” just because it’s on the internet.**  
> Third‑party marks must include license/permission details in the manifest.

Rules:
- Every third-party logo needs:
  - Source URL (where it came from)
  - License/permission terms
  - Attribution line
- If a logo has usage restrictions (e.g., “do not modify”, “color must remain”), document it in `source.notes` and respect it.

---

## 🧰 Usage examples

### JS/TS registry pattern (recommended)

```ts
// pseudo-example: adapt to your actual app structure
import manifest from "./logos.manifest.json";

export function getLogoFile(id: string): string {
  const item = manifest.find(x => x.id === id);
  if (!item) throw new Error(`Unknown logo id: ${id}`);
  return `/assets/media/icons/logos/${item.file}`;
}
```

### CSS background (sparingly)

```css
.partner-logo {
  background-image: url("/assets/media/icons/logos/partners/usgs.svg");
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
}
```

---

## 🧩 Add a new logo (PR checklist)

- [ ] ✅ Add SVG (preferred) or PNG fallback to the correct subfolder
- [ ] 🧾 Add/Update `logos.manifest.json` entry (source, license, attribution, alt)
- [ ] ♿ Verify accessibility (alt text, link labeling if clickable)
- [ ] ⚡ Optimize asset (`svgo` / `oxipng`)
- [ ] 🔍 Confirm it renders correctly on light + dark backgrounds
- [ ] 🧪 Run any logo/manifest validation scripts (CI should enforce this)

---

💡 If you’re unsure where a logo belongs, default to **documenting it and isolating it** (with metadata) rather than scattering it across the repo.
