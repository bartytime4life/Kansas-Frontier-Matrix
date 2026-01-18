# 🖼️ Illustrations (Web UI)

![assets](https://img.shields.io/badge/assets-illustrations-0A66C2)
![preferred](https://img.shields.io/badge/preferred-SVG-success)
![provenance](https://img.shields.io/badge/provenance-required-important)
![license](https://img.shields.io/badge/license-required-critical)

This folder holds **UI illustrations** used by the KFM web app (landing, onboarding, empty-states, inline help, diagrams, etc.).  
In KFM, **anything that shows up in the UI must be traceable** to its source and allowed usage terms — no “mystery layers/assets.” [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ✨ Quick rules (read this first)

> [!IMPORTANT]
> **Every illustration needs provenance + license metadata.**  
> KFM’s “contract-first / provenance-first” approach (metadata required, validators/CI checks) is a core principle; we apply the same standard to visuals that ship in the UI. [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

- ✅ Prefer **SVG** for drawings/icons/diagrams (crisp at any DPI; often smaller than bitmap alternatives). [oai_citation:2‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)
- ✅ Keep UI copy **out of illustrations** when possible (use real HTML text for i18n/accessibility).
- ✅ Optimize before committing (SVG minify, bitmap compression).
- ✅ Keep files **kebab-case**, predictable, and searchable.
- ❌ No copyrighted logos/art unless explicitly licensed + documented.
- ❌ No unsafe SVG content (scripts/external refs).

---

## 📦 What belongs here (and what doesn’t)

### ✅ Belongs here
- Product/UI illustrations: onboarding scenes, empty states, “how it works” diagrams
- Simple cartographic UI visuals (non-data) like “layer stack” metaphors
- Small explanatory diagrams used in docs pages inside the app

### ❌ Does not belong here
- Large **data layers** (rasters/tiles/COGs/GeoJSON) → those live in the data/catalog pipelines (not in the web UI assets)
- Photos / marketing images unrelated to UI flow (put in the appropriate media folder)
- Anything without clear license/provenance

---

## 🗂️ Suggested folder layout

> [!NOTE]
> This directory may start simple. If/when it grows, use a structure like:

```text
web/assets/media/illustrations/
├─ 📄 README.md                # you are here 🙂 📌 What counts as an illustration + sizing/naming + licensing rules
├─ 🎨 _src/                    # Optional editable sources (Figma exports, .ai, layered originals; keep small or store elsewhere)
├─ 🎛️ ui/                      # Onboarding, empty states, helper scenes, UI-friendly illustrations
├─ 📐 diagrams/                # Architecture/flow diagrams used in-app (prefer SVG + accessible labels)
├─ 🗺️ map/                     # Map-adjacent visuals (non-data): explainer art, legend how-tos, layer concepts
└─ 🏷️ brand/                   # Mascots/brand illustrations (ONLY if licensed & approved; keep governance tight)
```

If you add folders, keep them **purpose-based** (not “misc”). ✂️

---

## 🏷️ Naming conventions

### Filenames
Use **kebab-case** with a stable prefix:

- `kfm-<area>-<purpose>.<ext>`
- Add variants with `--light` / `--dark` or size suffixes when needed.

Examples:
- `kfm-onboarding-layer-stack.svg`
- `kfm-empty-state-no-results--light.svg`
- `kfm-empty-state-no-results--dark.svg`
- `kfm-diagram-data-contract.svg`
- `kfm-map-legend-example@2x.png`

### Sidecar metadata file
Every shippable illustration should have a **matching** metadata file:

- `kfm-onboarding-layer-stack.svg`
- `kfm-onboarding-layer-stack.meta.json`

---

## 🎨 Formats & when to use what

KFM is web-first, so we pick formats with browser support and predictable output. Traditional web formats include **JPEG, GIF, PNG** (and others like BMP/XBM exist, but are rarely appropriate for UI assets). [oai_citation:3‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)

| Format | Use it for ✅ | Avoid it for ❌ | Notes |
|---|---|---|---|
| **SVG** | icons, line art, diagrams, UI illustrations | photo-like textures, heavy filters, embedded scripts | Best default for UI; scales cleanly. [oai_citation:4‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M) |
| **PNG** | transparency + crisp raster art | huge full-screen scenes | Good fallback when SVG isn’t feasible |
| **JPEG** | photos / complex raster imagery | sharp text/lines (compression artifacts) | Use for photos only |
| **GIF** | tiny “meme-size” loops only | modern animations | Prefer MP4/WebM/Lottie for real UI animation |

> [!TIP]
> If you’re choosing between SVG and PNG for a drawing: **try SVG first** for resolution independence and often smaller payloads. [oai_citation:5‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)

---

## 🧩 SVG guidance (the “don’t regret it later” section)

### 1) Pick one delivery method and stick to it
Mixing SVG insertion strategies becomes maintenance-heavy (especially with theming/fallbacks). [oai_citation:6‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

Common approaches:
- `<img src="...">` (simple, cache-friendly)
- CSS `background-image: url(...)`
- **Inline SVG** (best for theming/animation; requires sanitization)

### 2) Media queries inside SVG behave differently depending on embedding
If an SVG is included via `img`, `object`, or as a CSS background, **media queries inside the SVG evaluate against the SVG itself**, not the outer page viewport; inline SVG behaves more like the outer document. [oai_citation:7‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

**Practical takeaway:**
- If you rely on responsive behavior inside SVG, prefer **inline SVG** or use device-based queries appropriately. [oai_citation:8‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

### 3) Keep SVGs safe
- Strip `script`, `foreignObject`, and external `href`/remote resources
- Avoid embedded raster images unless necessary
- Prefer solid fills, strokes, and simple paths for performance

---

## 🚀 Optimization & performance

### SVG optimization
- Remove editor metadata, hidden layers, unused defs
- Minify with an SVG optimizer (e.g., SVGO) and keep output deterministic

### Bitmap optimization (PNG/JPEG)
- Compress losslessly where possible
- Ensure correct dimensions (don’t ship 4000px-wide PNGs for a 600px UI slot)

> [!TIP]
> “Automate as many steps in the asset creation process as possible” to reduce human error and keep outputs predictable. [oai_citation:9‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

---

## 🧾 Provenance & licensing (KFM-style “asset contract”)

KFM treats **metadata + lineage as fundamental** and disallows unsourced entries in its official catalog — no “mystery layers.” [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
For illustrations, that means: **every asset must declare who made it, what it’s based on (if anything), and the license**.

### ✅ Required: `*.meta.json` sidecar

Create a file next to the illustration with this minimum schema:

```json
{
  "id": "kfm-onboarding-layer-stack",
  "title": "Onboarding — Layer Stack",
  "type": "illustration",
  "format": "svg",
  "created_at": "2026-01-15",
  "created_by": "YOUR NAME OR TEAM",
  "license": "CC BY 4.0 | MIT | Proprietary | Public Domain | ...",
  "source": {
    "kind": "original | derived | third-party",
    "url": "https://example.com/source-if-any",
    "attribution": "Required if not original",
    "license": "License of the upstream asset, if applicable",
    "notes": "What changed / what was used"
  },
  "usage": {
    "contexts": ["onboarding", "landing", "empty-state"],
    "alt": "Short human description for accessibility",
    "dark_mode_variant_of": null
  }
}
```

> [!IMPORTANT]
> KFM’s practice is to **avoid legal pitfalls and foster collaboration by addressing license matters carefully** — treat illustration licensing the same way. [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ✅ Adding a new illustration (checklist)

### Step-by-step
1. **Design/export**
   - Export SVG where possible
   - Avoid embedded text if it needs translation
2. **Optimize**
   - Run SVG/bitmap optimization
3. **Add provenance**
   - Create `*.meta.json` and fill the required fields
4. **Add variants (if needed)**
   - `--light` / `--dark` or themable SVG via CSS variables
5. **Smoke test**
   - Check rendering in Chrome + Firefox (and Safari if possible)
   - Verify at 1× and 2× scaling
6. **Accessibility**
   - Ensure a good `alt` string exists in metadata (and is used in UI)
7. **PR hygiene**
   - Keep diffs clean, avoid unnecessary re-exports that churn paths

### PR checklist
- [ ] File name follows convention
- [ ] Optimized output (no editor junk)
- [ ] `*.meta.json` present & complete
- [ ] License verified and documented
- [ ] Dark mode story accounted for (variant or theming)
- [ ] Used in UI with alt text

---

## 🧪 Using illustrations in the web app

### HTML
```html
<img
  src="/assets/media/illustrations/ui/kfm-empty-state-no-results.svg"
  alt="No results found. Try widening the map extent or changing filters."
/>
```

### CSS background
```css
.emptyState {
  background: center / contain no-repeat
    url("/assets/media/illustrations/ui/kfm-empty-state-no-results.svg");
}
```

### Inline SVG (when you need theming/animation)
- Sanitize content
- Prefer `fill="currentColor"` or CSS variables
- Keep IDs unique to avoid collisions

---

## 📚 References (project docs & supporting material)

- KFM “Contract-first / provenance-first” principle and metadata requirements [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- SVG usage for resolution independence (web workflow guidance) [oai_citation:14‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)
- SVG embedding + media query behavior + workflow tips [oai_citation:15‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa) [oai_citation:16‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
- Core web image formats background (JPEG/GIF/PNG and related formats) [oai_citation:17‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)
