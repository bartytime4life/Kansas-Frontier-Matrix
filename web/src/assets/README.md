# 🧩 `web/src/assets/` — UI Asset Vault (Bundled)

![Scope](https://img.shields.io/badge/scope-web%2Fsrc%2Fassets-blue)
![Bundled](https://img.shields.io/badge/build-imported%20assets%20are%20fingerprinted-success)
![Rules](https://img.shields.io/badge/rules-no%20big%20data%20files-critical)
![Governance](https://img.shields.io/badge/governance-licensing%20%2B%20provenance%20required-9cf)

This folder is the **source-controlled, build-time (bundled)** home for **small UI assets** used by the React app:
icons, brand marks, small UI images, fonts, and *optionally* map style helpers. 🗺️✨

> 💡 **KFM doctrine reminder:** the UI should **not** “smuggle” datasets through `assets/`.  
> Geospatial/historical data must flow through the governed pipeline (**ETL → catalogs → APIs → UI**) and remain traceable.  
> See: [`../../../docs/MASTER_GUIDE_v13.md`](../../../docs/MASTER_GUIDE_v13.md)

---

## ⚡ Golden Rules (non-negotiable)

- ✅ **Keep it small & fast:** assets here should be *UI-sized* (think **KB**, not **MB**).
- ✅ **Prefer modern formats:** `svg`, `woff2`, `avif/webp`, `png` (when transparency matters).
- ✅ **Accessibility matters:** icons must be legible at 16–24px; images need meaningful `alt`.
- ✅ **No license? No merge.** Every non-trivial asset needs **license + attribution** (details below). 🧾
- ✅ **One place, not two:** do **not** duplicate assets that belong with Story Nodes or datasets.

---

## 🗂️ Suggested Folder Map

> Your actual tree may differ — this is the recommended layout for clarity + scale.

```text
web/src/assets/
├── 📄 README.md
├── 📁 brand/                  # Logos, wordmarks, lockups (SVG preferred)
│   ├── 🖼️ logo.svg
│   └── 🖼️ wordmark.svg
├── 📁 icons/                  # UI + map icons (SVG preferred)
│   ├── 📁 ui/
│   ├── 📁 map/
│   └── 📁 story/
├── 📁 images/                 # Small UI imagery (placeholders, UI illustrations)
│   ├── 📁 placeholders/
│   └── 📁 ui/
├── 📁 fonts/                  # woff2 only + license
├── 📁 map/                    # Optional: style JSON, legend swatches, sprite sources
│   ├── 📁 styles/
│   └── 📁 legend/
└── 📁 _meta/                  # Asset metadata & manifests (recommended)
    ├── 📄 ASSETS_MANIFEST.json
    └── 📁 licenses/
```

---

## ✅ What belongs here (and what does not)

### ✅ Yes (good fits)
- 🎨 **Brand assets**: `logo.svg`, `wordmark.svg`, favicon sources.
- 🧷 **Icons**: UI actions, layer symbols, small glyphs (SVG).
- 🖼️ **UI images**: placeholders, empty-states, tiny illustrations (AVIF/WebP/PNG).
- 🔤 **Fonts**: `woff2` (variable fonts welcome).
- 🗺️ **Map UI helpers**: legend chips, small symbol swatches, optional style JSON.

### 🚫 No (move these elsewhere)
- 🧱 **Large rasters / scans / historical photos** (MB–GB): store with governed content (Story Nodes or data pipeline outputs).
- 🗺️ **Geodata** (GeoJSON, SHP, TIFF, MBTiles, PMTiles, etc.) that represents real datasets: belongs in `data/` and served via APIs.
- 🔐 **Anything sensitive**: keys, credentials, private imagery, restricted documents.
- 🧩 **“Random downloads”**: every asset needs a reason, owner, and license.

> 📌 Story-specific media belongs with Story Nodes:  
> `docs/reports/story_nodes/(draft|published)/<story_slug>/assets/`  
> (See repo layout guidance in the master docs.)

---

## 🧾 Naming Conventions

| Asset Type | Convention ✅ | Example |
|---|---|---|
| Icons | `kebab-case.svg` | `search.svg`, `layer-trails.svg` |
| Brand | `kebab-case.svg` | `kfm-logo.svg`, `kfm-wordmark.svg` |
| Images | `topic-variant@2x.webp` (optional) | `empty-state@2x.webp` |
| Fonts | `Family-Style.woff2` | `Inter-Variable.woff2` |
| Map styles | `kebab-case.style.json` | `kfm-basemap.style.json` |

**Avoid:** spaces, `final_final2.png`, and ambiguous names like `icon1.svg`. 🙃

---

## 🧰 Using assets in code (React)

### Importing (bundled)
Use imports for anything in `src/assets/` so the build pipeline can fingerprint + optimize caching.

```ts
import logoUrl from "@/assets/brand/logo.svg";
import searchIconUrl from "@/assets/icons/ui/search.svg";
```

```tsx
<img src={logoUrl} alt="Kansas Frontier Matrix" />
```

### SVG as a component (if configured)
If your build supports SVG → component transforms (varies by setup):

```tsx
// Example only — depends on your bundler config.
import { ReactComponent as SearchIcon } from "@/assets/icons/ui/search.svg";

<SearchIcon aria-hidden="true" focusable="false" />
```

### When to use `web/public/` instead
Use `public/` for assets that must be referenced by **URL at runtime** (e.g., third-party libs expecting `/path/file.ext`).

Examples:
- Map styles referencing sprite/glyph URLs
- Cesium viewer assets that need absolute URL paths

---

## 🗺️ Map-related assets (MapLibre / Cesium)

KFM’s UI is map-centric, so keep map UI assets tidy and predictable. 🧭

### MapLibre (2D)
Recommended:
- `web/src/assets/map/styles/*.json` for style templates you import into code
- sprites/glyphs usually live in `web/public/` or are served remotely (URL-based)

**Style JSON conventions**
- Prefer *config-driven* tile endpoints (don’t hardcode production domains).
- Keep sources named clearly: `basemap`, `counties`, `trails`, `water`, etc.

Example snippet (vector tiles):
```json
{
  "version": 8,
  "sources": {
    "historic_trails": {
      "type": "vector",
      "tiles": ["/tiles/historic_trails/{z}/{x}/{y}.pbf"]
    }
  }
}
```

### Cesium (3D)
Rules of thumb:
- ✅ Small UI icons are fine here
- ⚠️ Tiny illustrative models are okay (only if truly small)
- 🚫 Large 3D Tiles / terrain / imagery **do not** belong in `src/assets/` (serve from the backend or a storage/CDN tier)

---

## 🧾 Provenance, Licensing & Attribution

KFM is evidence-first. Assets are “evidence-adjacent,” so we treat them with the same respect. ✅

### Required for any non-trivial asset
For each asset you add, include at least one of the following:

**Option A (recommended): sidecar metadata**
- `my-asset.svg`
- `my-asset.meta.json`
- `my-asset.license.md` *(or include license in meta)*

**Option B: centralized manifest**
- Add entry to `web/src/assets/_meta/ASSETS_MANIFEST.json`

### Suggested `*.meta.json` shape
```json
{
  "title": "Layer: Historic Trails Icon",
  "description": "UI icon used in the layer toggle and legend.",
  "source": {
    "type": "original | derived | third-party",
    "url": "https://example.com/source",
    "author": "Name/Org"
  },
  "license": {
    "spdx": "CC-BY-4.0",
    "textFile": "my-asset.license.md",
    "attribution": "© Author, used under CC BY 4.0"
  },
  "created": "2026-02-05",
  "createdBy": "github-handle",
  "derivation": {
    "derivedFrom": ["original-file-or-url"],
    "tools": ["inkscape", "svgo"],
    "notes": "Simplified paths and optimized for 16–24px rendering."
  }
}
```

> 🧠 If you’re unsure how strict to be: choose “over-documented.”  
> Governance docs live in: `../../../docs/governance/`

---

## ⚙️ Optimization Checklist (keep the UI snappy)

### Icons (SVG)
- ✅ Run SVGO (or equivalent)
- ✅ Prefer strokes with consistent widths
- ✅ Test at **16px, 20px, 24px**
- ✅ Ensure contrast passes accessibility needs

### Images
- ✅ Photographic: `avif` → fallback `webp` → fallback `jpg`
- ✅ Transparent UI art: `webp` or `png`
- ✅ Avoid GIF (prefer video or Lottie where appropriate)

### Fonts
- ✅ `woff2` only
- ✅ Subset if the font is large
- ✅ Include font license text

---

## 🔁 Asset Lifecycle (how assets should flow)

```mermaid
flowchart LR
  A[🎨 Source / Design] --> B[📤 Export (SVG/AVIF/WOFF2)]
  B --> C[🧼 Optimize (svgo / imagemin)]
  C --> D[🧾 Add License + Meta]
  D --> E[📦 Import in React]
  E --> F[🏗️ Build (fingerprinted assets)]
  F --> G[🚀 Deploy (long-cache headers)]
```

---

## ✅ PR Checklist (copy/paste into your PR)

- [ ] Asset is placed in the correct folder (`brand/`, `icons/`, `images/`, `fonts/`, `map/`)
- [ ] File name follows convention (kebab-case, no spaces)
- [ ] Asset is optimized (SVGO / image compression)
- [ ] License + attribution added (sidecar meta or manifest)
- [ ] No large datasets or restricted media added
- [ ] UI uses import-based references (unless `public/` is required)
- [ ] Visual QA: looks correct at expected sizes + in dark/light backgrounds (if applicable)

---

## 🔗 Related docs (project source of truth)

- 📚 Master guide: [`../../../docs/MASTER_GUIDE_v13.md`](../../../docs/MASTER_GUIDE_v13.md)
- 🧭 Repo structure standard: [`../../../docs/standards/KFM_REPO_STRUCTURE_STANDARD.md`](../../../docs/standards/KFM_REPO_STRUCTURE_STANDARD.md)
- 🧬 Provenance profile: [`../../../docs/standards/KFM_PROV_PROFILE.md`](../../../docs/standards/KFM_PROV_PROFILE.md)
- 🧾 DCAT profile: [`../../../docs/standards/KFM_DCAT_PROFILE.md`](../../../docs/standards/KFM_DCAT_PROFILE.md)
- 🗺️ STAC profile: [`../../../docs/standards/KFM_STAC_PROFILE.md`](../../../docs/standards/KFM_STAC_PROFILE.md)
- 🛡️ Review gates: [`../../../docs/governance/REVIEW_GATES.md`](../../../docs/governance/REVIEW_GATES.md)

---

<details>
<summary>🧯 Troubleshooting</summary>

### “Why isn’t my asset showing up?”
- Ensure you imported it from `src/assets/` (bundled) or placed it in `public/` (URL-based).
- Confirm the path casing matches exactly (Linux is case-sensitive).
- If using SVG-as-component, confirm the bundler plugin is enabled.

### “Why did my filename change in build output?”
- That’s expected: most React build pipelines fingerprint assets for caching.

</details>

