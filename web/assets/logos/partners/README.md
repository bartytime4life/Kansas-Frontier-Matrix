# 🤝 Partner Logos (Web Assets)

![Asset Scope](https://img.shields.io/badge/assets-partner%20logos-blue?style=for-the-badge)
![Provenance](https://img.shields.io/badge/provenance-first-success?style=for-the-badge)
![A11y](https://img.shields.io/badge/a11y-semantic%20HTML%20%2B%20ARIA-9cf?style=for-the-badge)
![Performance](https://img.shields.io/badge/performance-keep%20it%20lightweight-orange?style=for-the-badge)

> 📍 **Path:** `web/assets/logos/partners/`  
> This folder is the **single source of truth** for partner & collaborator logos used in the KFM web experience (footer attribution, “About”, data provider callouts, onboarding, map UI overlays, etc.).

---

<details>
  <summary><strong>🧭 Quick Nav</strong> (click to expand)</summary>

- [✅ Golden Rules](#-golden-rules)
- [📁 Folder Contract](#-folder-contract)
- [🧾 Provenance Metadata](#-provenance-metadata)
- [🖼️ Formats & Variants](#️-formats--variants)
- [♿ Accessibility Requirements](#-accessibility-requirements)
- [🛡️ Security Rules](#️-security-rules)
- [⚡ Performance Budget](#-performance-budget)
- [➕ Adding a New Partner Logo](#-adding-a-new-partner-logo)
- [🧪 Definition of Done Checklist](#-definition-of-done-checklist)
- [🧩 Usage Examples](#-usage-examples)
- [📚 Project Reference Shelf](#-project-reference-shelf)

</details>

---

## ✅ Golden Rules

- ✅ **Only include logos we’re allowed to use.** If permission/terms are unclear, **don’t commit** the logo yet.
- ✅ **Prefer SVG** for sharpness + small size (raster only when necessary).
- ✅ **Every partner folder must include provenance metadata** (see below).
- ✅ **Support light & dark UI** (either variants or ensure the logo works on both).
- ✅ **Don’t distort branding** (aspect ratio, spacing, colors, lockups).

**Hard “No” list** 🚫  
- 🚫 No random filenames like `final_final2.png`
- 🚫 No scripts, tracking pixels, or external references inside SVGs
- 🚫 No “mystery source” assets (if we can’t trace it, we can’t ship it)

---

## 📁 Folder Contract

This directory is **organized by partner slug** (stable identifier).

```text
📁 web/
  📁 assets/
    📁 logos/
      📁 partners/
        📄 README.md
        📄 partners.manifest.json              ← optional, but recommended
        📁 <partner-slug>/
          🖼️ logo.svg                         ← preferred primary
          🖼️ logo-dark.svg                    ← if needed
          🖼️ logo-light.svg                   ← if needed
          🖼️ logo.png                         ← fallback (transparent)
          🖼️ logo@2x.png                      ← fallback retina
          🧾 provenance.json                   ← REQUIRED
          📄 NOTES.md                          ← optional (quirks/usage notes)
```

### Slug rules 🏷️
- lowercase
- hyphen-separated
- no spaces
- keep it stable over time (branding may change; slug shouldn’t)

Examples:
- `kansas-department-of-transportation`
- `usgs`
- `acme-university`

---

## 🧾 Provenance Metadata

Every partner must ship with **`provenance.json`** to keep attribution, rights, and source traceable.

### `provenance.json` template

```json
{
  "partner": {
    "name": "Example Partner Name",
    "slug": "example-partner",
    "type": "government | university | nonprofit | company | community",
    "relationship": "data-provider | collaborator | sponsor | integrator",
    "website": "https://example.org",
    "valid_from": "2025-01-01",
    "valid_to": null
  },
  "logo": {
    "primary": "logo.svg",
    "variants": {
      "dark": "logo-dark.svg",
      "light": "logo-light.svg"
    },
    "fallback": {
      "raster_1x": "logo.png",
      "raster_2x": "logo@2x.png"
    }
  },
  "rights": {
    "trademark_owner": "Example Partner Name",
    "usage_permission": "explicit-brand-kit | written-permission | public-domain | unknown",
    "permission_reference": "docs/permissions/example-partner.md",
    "attribution_required": true,
    "notes": "Do not recolor. Maintain clear space."
  },
  "source": {
    "download_url": "https://example.org/brand",
    "retrieved_at": "2025-02-10",
    "checksum_sha256": "PUT_SHA256_HERE"
  }
}
```

### Why we care 🧠
Partner logos are not “just images” — they are **identity + attribution**. Provenance lets us:
- defend usage rights & terms
- update safely during rebrands
- show correct partners for time-bounded collaborations (`valid_from` / `valid_to`)
- avoid accidental endorsement or misrepresentation

---

## 🖼️ Formats & Variants

### Preferred: SVG (vector) ✅
Use SVG unless you have a hard blocker (license only provides PNG, or logo contains photographic raster).

**SVG must:**
- include a sane `viewBox`
- keep strokes/paths crisp at small sizes
- avoid unnecessary editor metadata (e.g., tool namespaces) unless needed
- not include external URLs/resources

**Accessibility note for SVG:**  
If used inline, include meaningful `<title>` / `<desc>` where appropriate. If used via `<img>`, ensure **`alt`** is correct (see A11y section).

### Raster: PNG fallback 🧩
Use PNG for fallback or when SVG isn’t feasible.

**PNG must:**
- be transparent (when needed)
- be high enough resolution for retina (`@2x`)
- avoid palette artifacts around edges (logos often need real alpha transparency)

### Avoid 🚫
- JPEG (bad for sharp edges + no transparency)
- animated GIFs in partner logos folder (not a logo)
- “banner” images (belongs elsewhere)

---

## ♿ Accessibility Requirements

Partner logos are meaningful content in most contexts (attribution + identity). Don’t ship inaccessible branding.

### Minimum requirements ✅
- `<img>` logos must have correct `alt` text:
  - If logo is purely decorative **and** adjacent text already names partner → `alt=""`
  - If logo is the only visible identity → `alt="Partner Name"`
- If logo is a link:
  - link should have an accessible name (often the same as partner name)
- Maintain logical heading structure and semantic layout around partner sections

### “Looks fine” is not a11y 😅
Test with:
- keyboard only (Tab / Enter / Space)
- light & dark mode
- high zoom (200%+)
- reduced motion (if you animate anything near logos)

---

## 🛡️ Security Rules

SVG can be a security footgun if mishandled.

### SVG safety checklist ✅
- no `<script>` tags
- no external `<image href="https://...">`
- no external stylesheets
- no `foreignObject` unless you truly know why (often breaks canvas + security expectations)
- treat incoming SVGs as **untrusted input** until inspected

If logos are ever drawn into `<canvas>` / WebGL:
- ensure the SVG has explicit width/height where required
- watch for browser quirks that can “taint” a canvas and block export/reads

---

## ⚡ Performance Budget

Logos show up everywhere (footer, nav, about, attribution). Keep the budget tight.

### Targets 🎯
- SVG: “small as possible without breaking semantics”
- PNG: keep within reason; use `@2x` only when actually needed

### Recommended tooling (optional but great) 🧰
- SVG optimization (e.g., SVGO)
- PNG optimization (lossless where possible)

> 💡 Don’t blindly optimize away accessibility: if inline SVG needs `<title>`/`<desc>`, preserve it.

---

## ➕ Adding a New Partner Logo

1) **Create folder**
```text
web/assets/logos/partners/<partner-slug>/
```

2) **Add assets**
- `logo.svg` (preferred)
- optional `logo-dark.svg` / `logo-light.svg`
- `logo.png` + `logo@2x.png` fallback if needed

3) **Add provenance**
- Create `provenance.json` and fill all fields you can
- If permission is not explicit → set `usage_permission: "unknown"` and stop 🚫 (don’t ship unknown)

4) **(Recommended) Add/update manifest**
If the web app uses a single registry, update `partners.manifest.json`:

```json
[
  {
    "name": "Example Partner Name",
    "slug": "example-partner",
    "logo": "/assets/logos/partners/example-partner/logo.svg",
    "url": "https://example.org",
    "relationship": "data-provider"
  }
]
```

5) **Verify in UI**
- light mode + dark mode
- mobile + desktop
- footer + partner grid
- keyboard focus ring on linked logos

---

## 🧪 Definition of Done Checklist

- [ ] Folder uses correct slug
- [ ] SVG primary exists **or** raster fallback exists (prefer both)
- [ ] No distortion (aspect ratio preserved)
- [ ] `provenance.json` exists and is complete enough to trace:
  - [ ] source URL
  - [ ] retrieval date
  - [ ] trademark owner / permission type
- [ ] Accessible alt/link labeling is correct
- [ ] Security scan performed (SVG inspected for scripts/external refs)
- [ ] File sizes are reasonable (no accidental 5MB “logo”)
- [ ] Partner appears correctly in both light/dark UI

---

## 🧩 Usage Examples

### Plain HTML
```html
<a
  href="https://example.org"
  aria-label="Visit Example Partner"
  rel="noopener noreferrer"
  target="_blank"
>
  <img
    src="/assets/logos/partners/example-partner/logo.svg"
    alt="Example Partner"
    height="36"
    loading="lazy"
    decoding="async"
  />
</a>
```

### Inline SVG (when you must style it)
```html
<svg role="img" aria-labelledby="logoTitle logoDesc" viewBox="0 0 100 24">
  <title id="logoTitle">Example Partner</title>
  <desc id="logoDesc">Partner logo used for attribution.</desc>
  <!-- paths go here -->
</svg>
```

### Suggested CSS (framework-agnostic)
```css
.partnerLogo img {
  height: 36px;
  width: auto;
  max-width: 180px;
  object-fit: contain;
}
```

---

## 📚 Project Reference Shelf

These project docs/books informed our asset policy mindset (provenance, a11y, security, web delivery, GIS context):

- 📘 KFM technical documentation (provenance-first mindset)
- 🧭 Open-source mapping hub design notes (web-first distribution)
- ♿ Responsive Web Design (SVG + accessibility)
- 🧱 HTML5/SVG guidance (embedding + semantics)
- 🧪 Documentation governance patterns (README structure + doc hygiene)
- 🛡️ Security notes (injection/XSS awareness)
- 🗺️ Map design references (logos appear inside map UIs)
- 🧊 WebGL references (logos may be used in interactive 3D contexts)
- 🧩 Data spaces & provenance systems (cross-org collaboration + audit trails)
- 🕰️ Temporal thinking (partnerships change; metadata should reflect time)

---

### 👀 FAQ

**Q: Do we need both `logo-dark.svg` and `logo-light.svg`?**  
A: Only if the primary logo doesn’t work across light/dark backgrounds. If one SVG works universally, keep it simple.

**Q: Can I recolor a logo to match our theme?**  
A: Usually **no**. Logos are trademarks/brand assets. Use variants supplied by the partner or approved by their brand kit.

**Q: Why the provenance.json requirement?**  
A: Because KFM is built around traceability and attribution — we treat assets like data: sourceable, reviewable, auditable.

---
