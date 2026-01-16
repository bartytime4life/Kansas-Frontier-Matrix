---
title: "KFM Brand Icons"
version: "v1.0.0"
status: "active"
doc_kind: "UI Asset Standard"
last_updated: "2026-01-14"
doc_uuid: "urn:kfm:doc:web:assets:icons:brand:v1.0.0"
license: "See: License & Trademark"
---

# Kansas Frontier Matrix (KFM) — Brand Icons 🧭✨

![provenance-first](https://img.shields.io/badge/provenance-first-%E2%9C%85-2ea44f)
![contract-first](https://img.shields.io/badge/contract-first-%E2%9C%85-2ea44f)
![web-perf](https://img.shields.io/badge/web%20perf-%E2%9A%A1-1f6feb)
![a11y](https://img.shields.io/badge/accessibility-%F0%9F%A6%BD-8a2be2)

Canonical **brand** marks for the KFM web UI (`web/assets/icons/brand/`).  
This folder is for **identity assets** (logo/wordmark/lockups/favicons), not general UI glyphs.

> 🔎 KFM principle: anything that appears in the UI should be **traceable** and **auditable**—no “mystery assets.”[^kfm-provenance]

---

## Quick Nav 🧷

- [What belongs here](#what-belongs-here-)
- [Folder layout](#folder-layout-)
- [Naming rules](#naming-rules-)
- [Formats](#formats-)
- [Theming & accessibility](#theming--accessibility-)
- [Optimization & performance](#optimization--performance-)
- [Provenance & licensing](#provenance--licensing-)
- [Usage examples](#usage-examples-)
- [Contribution workflow](#contribution-workflow-)
- [Definition of Done](#definition-of-done--)
- [References](#references-)

---

## What belongs here ✅

**✅ Put here**
- KFM logo mark (icon-only)
- Wordmark (text-only)
- Lockups (horizontal / stacked)
- Monochrome variants for UI theming
- Favicons (SVG/PNG/ICO), pinned-tab icon
- Social/share variants (if used by the web build)

**❌ Don’t put here**
- Generic UI icons (buttons, tools, layers, etc.) → `web/assets/icons/ui/` (or equivalent)
- Map symbols for datasets/layers → `web/assets/icons/layers/` (or equivalent)
- One-off marketing images → `web/assets/media/` (or equivalent)

---

## Folder layout 📁

```text
web/ 🌐
└─ 🧰 assets/
   └─ 🧩 icons/
      └─ 🧭 brand/
         ├─ 📘 README.md                    # (this file) 📌
         ├─ 🟩🧷 kfm-mark.svg
         ├─ 🅺🧷 kfm-wordmark.svg
         ├─ ↔️🧷 kfm-lockup-horizontal.svg
         ├─ ↕️🧷 kfm-lockup-stacked.svg
         ├─ ⚪️🧷 kfm-mark-mono.svg
         ├─ ⭐🧷 favicon.svg
         ├─ 🟦🖼️ favicon-32.png
         ├─ 🟦🖼️ favicon-16.png
         ├─ 🍎🖼️ apple-touch-icon.png
         ├─ 🧷🧩 safari-pinned-tab.svg
         └─ 🧾 _meta/
            ├─ 🧾 kfm-mark.meta.json
            ├─ 🧾 kfm-wordmark.meta.json
            └─ ➕ …
            └─ ...
```

> 🧠 Why `_meta/`? KFM is **contract-first**: assets ship with structured metadata so the UI/build/pipeline can validate licensing + provenance automatically.[^kfm-contract-first]

---

## Naming rules 🏷️

KFM values **stable identifiers** and predictable naming (treat asset naming like API naming).[^stable-ids]

### Conventions
- **Lowercase kebab-case**: `kfm-mark.svg`
- Prefix brand assets with **`kfm-`** to prevent collisions.
- Use **explicit, durable** tokens:
  - `mark`, `wordmark`, `lockup-horizontal`, `lockup-stacked`
  - `mono` for monochrome/themable variants
  - `dark` / `light` only if you truly need distinct files (prefer mono + CSS)

### Avoid
- Embedding “temporary meaning” in filenames (e.g., `kfm-logo-new.svg`, `kfm-logo-2026.svg`)
- Replacing old assets silently (if you must change appearance, bump the metadata `version`)

---

## Formats 📦

### Primary (preferred)
- **SVG** for web UI: crisp at any scale, smallest payload when optimized.
- Keep:
  - `viewBox` (mandatory)
  - simple paths (avoid unnecessary groups/masks when possible)
  - no raster embedding inside SVG (no base64 PNGs inside SVG)

### Secondary (when needed)
- **PNG** for:
  - platform-specific icons (Apple touch icon)
  - environments that don’t support SVG well
- **ICO** only if your deployment pipeline requires it.

> 🧩 PNG/GIF/JPEG details matter for performance and portability; treat these outputs as engineered artifacts, not “just images.”[^img-formats]

---

## Theming & accessibility ♿🎨

### Monochrome (recommended)
Provide `*-mono.svg` variants that can inherit color from CSS using `currentColor`.[^currentColor]

**Goal:** One icon file that works across light/dark + custom themes.

### Accessibility requirements
- If the logo conveys meaning in context:
  - include meaningful `alt` text (`alt="Kansas Frontier Matrix"`)
- If the logo is decorative:
  - set `alt=""` and/or `aria-hidden="true"` (depending on usage)
- Don’t rely on color alone for state (hover/active) where the icon is part of a control.

> 🧑‍⚖️ Digital humanism reminder: interface choices influence trust; clarity + transparency beat “mystique.”[^digital-humanism]

---

## Optimization & performance ⚡

### Why this matters
KFM’s architecture is designed to scale (more users, more data, more UI surfaces). Keeping brand assets small and cache-friendly helps everything else feel fast.[^kfm-scale]  

Also: KFM targets modern browsers *and* mobile hardware—optimize for constrained devices.[^future-hw]

### Recommended pipeline
1. **Export** from your source tool (Figma/Illustrator/Inkscape)
2. **Normalize** geometry (clean paths, remove hidden layers)
3. **Optimize** with SVGO (keep `viewBox`)
4. **Generate** PNGs (only for required sizes)
5. **Validate** metadata + license in CI

<details>
<summary>✅ Suggested <code>svgo</code> config (copy/paste)</summary>

```js
// svgo.config.js
module.exports = {
  multipass: true,
  plugins: [
    // keep the viewBox so SVG remains responsive
    { name: "preset-default", params: { overrides: { removeViewBox: false } } },

    // reduce useless metadata
    "removeDimensions",
    "removeScriptElement",
    "removeStyleElement",
  ],
};
```
</details>

### Sprite / caching strategy (optional)
For many icons, external SVG sprite references can be cached effectively.[^currentColor]  
If you ever render brand marks as textures in 3D/WebGL contexts, remember image mapping and coordinate systems behave independently of image pixel size.[^webgl-texture]

---

## Provenance & licensing 🧾🔒

KFM’s rule: **no unsourced UI artifacts**. Anything shipped must have:
- source (where it came from)
- license (how we’re allowed to use it)
- version history (what changed)
- integrity hash (so builds can verify exact bytes)

This mirrors KFM’s broader **provenance-first / contract-first** approach for data and UI outputs.[^kfm-provenance][^kfm-contract-first][^v13-invariants]

### Asset metadata sidecar (`_meta/*.meta.json`)
Each brand asset should have a sibling metadata file.

<details>
<summary>🧾 Example <code>kfm-mark.meta.json</code></summary>

```json
{
  "asset_id": "urn:kfm:asset:brand:kfm-mark",
  "kind": "brand_mark",
  "version": "1.0.0",
  "source": {
    "tool": "figma",
    "design_file": "REDACTED_OR_LINK",
    "exported_by": "REDACTED_OR_HANDLE"
  },
  "license": {
    "spdx": "CC-BY-4.0",
    "notes": "If trademark restrictions apply, document them here."
  },
  "integrity": {
    "sha256": "REPLACE_WITH_REAL_HASH"
  },
  "a11y": {
    "default_alt": "Kansas Frontier Matrix",
    "decorative_ok": false
  },
  "usage": {
    "preferred": ["header", "about", "splash"],
    "avoid": ["dataset-layer-icon", "button-glyph"]
  }
}
```
</details>

> 🧷 Licensing clarity builds adoption and trust—KFM treats this as a first-class feature, not paperwork.[^kfm-licensing]

---

## Usage examples 🧪

### Plain HTML
```html
<img
  src="/assets/icons/brand/kfm-lockup-horizontal.svg"
  alt="Kansas Frontier Matrix"
  width="180"
  height="48"
/>
```

### Inline SVG (theming via `currentColor`)
```html
<!-- Use mono variant for theming -->
<svg class="kfm-brand-mark" aria-label="Kansas Frontier Matrix" role="img">
  <use href="/assets/icons/brand/sprite.svg#kfm-mark-mono"></use>
</svg>
```

```css
.kfm-brand-mark {
  width: 2rem;
  height: 2rem;
  color: currentColor; /* icon inherits */
}
```

### React (example)
```tsx
export function KfmLogo() {
  return (
    <img
      src="/assets/icons/brand/kfm-mark.svg"
      alt="Kansas Frontier Matrix"
      width={32}
      height={32}
      loading="eager"
      decoding="async"
    />
  );
}
```

---

## Contribution workflow 🤝

1. **Add / update** the SVG(s) in this folder.
2. **Add / update** matching `_meta/*.meta.json`.
3. Run local checks:
   - `npm run icons:optimize` (SVGO / PNG optimize)
   - `npm run icons:lint` (no scripts, has viewBox, etc.)
4. Open a PR:
   - include before/after screenshots in PR description
   - include license/provenance proof (link to source design file, license text)

> 🧭 KFM docs are governed artifacts; treat UI assets similarly (reviewable, versioned, reproducible).[^md-governance]

---

## Definition of Done ✅✅

A brand asset update is “done” when:

- [ ] SVG renders correctly in light + dark UI backgrounds
- [ ] `viewBox` preserved; no hardcoded pixel dimensions unless required
- [ ] No embedded scripts, external references, or fonts that won’t ship
- [ ] File size is reasonable (SVGO applied)
- [ ] `_meta/*.meta.json` exists and includes:
  - [ ] `asset_id` (stable)
  - [ ] `version`
  - [ ] `source`
  - [ ] `license`
  - [ ] `sha256`
- [ ] Any trademark constraints are documented
- [ ] PR includes a visual diff + rationale

---

## References 📚

These project documents informed the standards above (provenance, governance, performance, cartography-aware design):

- KFM Technical Documentation (architecture, contract-first + provenance-first)  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- KFM “v13” Markdown / repo governance invariants (pipeline ordering, evidence-first)  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- Documentation governance patterns (YAML front matter, evidence & review gates)  [oai_citation:3‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  
- Responsive Web Design (SVG reuse, `currentColor`, external defs/sprites)  [oai_citation:4‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)  
- Digital Humanism (trust, transparency, sociotechnical responsibility)  [oai_citation:5‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  
- Mobile Mapping (maps are performative/political; UI symbols are never “neutral”)  [oai_citation:6‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj)  
- WebGL Programming Guide (texture/image mapping considerations for 3D contexts)  [oai_citation:7‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)  
- Compressed Image File Formats (PNG/GIF/JPEG technical considerations)  [oai_citation:8‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)  
- Scalable Data Management for Future Hardware (mobile/ARM performance realities)  [oai_citation:9‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)  
- Database Performance at Scale (performance mindset & system thinking)  [oai_citation:10‡Database Performance at Scale.pdf](file-service://file-36z8qyiVJRtrSs6QG7Epen)  
- Flexible Software Design (stable identifiers; long-haul design thinking)  [oai_citation:11‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)  
- Archaeological 3D GIS (3D spatial thinking as KFM expands modalities)  [oai_citation:12‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  
- KFM geospatial web/API patterns (context for where icons appear in mapping UX)  [oai_citation:13‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  
- Kansas-Frontier-Matrix design doc (modularity/traceability expectations)  [oai_citation:14‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)  

Additional reference shelf (project library, optional reading):
- Data Mining (conceptual framing for “signals → meaning” in UI)  [oai_citation:15‡D-E programming Books.pdf](file-service://file-6Lmmw9aqHnfP2mo9cSrNeg)  
- SciPy Lecture Notes (reproducible, testable computational workflows)  [oai_citation:16‡S-T programming Books.pdf](file-service://file-NT32tqqzGW9RvfcNZmMH1K)  
- Objective-C Notes (cross-platform asset portability mindset)  [oai_citation:17‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)  
- Implementing Programming Languages (build pipelines & determinism)  [oai_citation:18‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a)  
- MATLAB Notes (scientific workflow context)  [oai_citation:19‡M-N programming Books.pdf](file-service://file-EYCp5md89QY2cy5PCYS18e)  
- Bash Notes (automation glue for asset pipelines)  [oai_citation:20‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ)  
- Understanding Machine Learning (communicating uncertainty; avoid misleading UI cues)  [oai_citation:21‡U-X programming Books.pdf](file-service://file-3hYtSGHtHmb6wyTtavym6M)  
- B-C / F-H / O-R programming books (broad engineering reference shelf)  [oai_citation:22‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ)  [oai_citation:23‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)  [oai_citation:24‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)  

---

### Footnotes

[^kfm-provenance]: KFM guiding rule: anything shown in UI/Focus Mode must be traceable back to cataloged sources and provable processing.  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
[^kfm-contract-first]: KFM treats metadata schemas/contracts as first-class, enabling validation and automatic attributions/credits.  [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
[^kfm-scale]: KFM backend/API is designed for horizontal scaling; UI performance still matters at scale.  [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
[^kfm-licensing]: KFM emphasizes careful license handling to avoid legal pitfalls and increase collaboration/trust.  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
[^v13-invariants]: v13 governance: strict ordering + evidence-first narrative expectations; “no unsourced content.”  [oai_citation:30‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
[^md-governance]: Governed docs: YAML front matter + reviewable provenance patterns.  [oai_citation:31‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  
[^stable-ids]: Stable identifiers and long-haul design principles (apply to asset IDs and naming).  [oai_citation:32‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)  
[^currentColor]: `currentColor` technique for SVG icon theming + external SVG reuse/caching trade-offs.  [oai_citation:33‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)  
[^img-formats]: PNG/JPEG/GIF are widely used web image formats with format-specific constraints; treat as engineered outputs.  [oai_citation:34‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)  
[^digital-humanism]: Transparent, accountable human-ADS interfaces and sociotechnical considerations improve trust.  [oai_citation:35‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  
[^future-hw]: Hardware variability (e.g., ARM) can affect performance; optimize assets for constrained environments.  [oai_citation:36‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)  
[^webgl-texture]: WebGL texture coordinate system and image mapping are normalized and independent of image pixel dimensions.  [oai_citation:37‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)  
