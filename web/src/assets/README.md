<!--
FILE: web/src/assets/README.md
KFM: Web UI static assets (NOT pipeline "assets" / STAC assets)
-->

# `web/src/assets` 🧰

![Governed](https://img.shields.io/badge/Governed-evidence--first-informational)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-aware-informational)
![Layer](https://img.shields.io/badge/Layer-Frontend%20(UI)-informational)

This directory contains **static UI assets** that are *safe to ship to end users* as part of the KFM web frontend bundle (images, icons, small JSON templates, local fonts, etc.).

> [!IMPORTANT]
> **This is not a data drop zone.**
> Do **not** store datasets, tiles, exports, or anything requiring access control here.
> Data artifacts belong to governed pipeline zones + catalogs and must be served through the API/policy boundary.

---

## What belongs here ✅

- Logos, wordmarks, favicons (project-owned or properly licensed)
- SVG icon sets (UI chrome, map layer icons)
- UI illustrations used in onboarding/help panels
- Small JSON snippets used by the UI (ex: style templates/fragments)
- Local fonts (**WOFF2 preferred**) *only if licensing allows redistribution*
- **Test fixtures** that are explicitly non-sensitive (ex: tiny GeoJSON used in unit tests)

## What does NOT belong here ❌

- Any *raw* or *processed* KFM datasets (even “small”)
- PMTiles / MBTiles / large GeoJSON / large rasters
- Anything containing **sensitive location detail** (archaeology, protected habitats, private landowner info)
- Secrets, tokens, `.env` files, API keys, signed URLs

> [!WARNING]
> If an asset would require redaction, permissions, or policy checks, it **does not** belong in `src/assets`.

---

## Recommended layout

> Adjust to match what already exists in the repo—this is a suggested baseline.

```text
web/src/assets/
  README.md
  brand/
    logos/
    favicons/
  icons/
    ui/
    layers/
  illustrations/
  fonts/
  map/
    styles/        # MapLibre style templates / fragments (JSON)
    sprites/       # (optional) dev-only sprite sources (NOT built artifacts)
  third_party/
    NOTICE.md      # attribution + license notes for third-party assets
```

### Folder intent registry

| Path | Purpose | Notes |
|---|---|---|
| `brand/` | KFM identity assets (logos, marks) | Keep source files (e.g., `.svg`) + derived exports. |
| `icons/` | UI + map layer icons | Prefer SVG. Keep size consistent (e.g., 16/20/24 px grid). |
| `illustrations/` | Non-critical visuals | Prefer SVG/WebP. Avoid high-res PNG unless needed. |
| `fonts/` | Self-hosted fonts | WOFF2 only unless there’s a strong reason. |
| `map/styles/` | Style JSON templates | Prefer “template + runtime injection” for endpoints. |
| `third_party/` | Vendor assets | Must include attribution + license notes. |

---

## Importing assets

Most assets in this folder are intended to be **imported by the frontend build** (Vite/Webpack/etc.).

<details>
<summary>Example import patterns (React/TS)</summary>

```ts
// Images / SVG-as-URL (common bundler behavior)
import logoUrl from '@/assets/brand/logos/kfm-mark.svg';

// If your toolchain prefers explicit URLs:
const url = new URL('../assets/brand/logos/kfm-mark.svg', import.meta.url).toString();
```

</details>

> [!TIP]
> If something must be fetched by URL at runtime (e.g., MapLibre glyphs/sprites referenced inside a style),
> prefer hosting it under the app’s static public path (often `web/public/`) or via a tile/style service.

---

## Map rendering assets (MapLibre/Cesium)

KFM’s UI clients **consume governed API contracts** and should not depend on storage internals.  
That means the map style should reference tiles/glyphs/sprites via controlled endpoints (or versioned static hosting).

### Style JSON guidance

- Keep **style templates** here (small JSON).
- Inject environment-specific URLs at runtime (dev/staging/prod) instead of hardcoding endpoints.

### Glyphs & sprites

Glyph/sprite URLs are part of the style contract:

- Ensure they exist and are CORS-safe if served from another domain.
- Prefer immutable / versioned paths for caching stability.

---

## Governance & licensing

### Required for every third-party asset

Add a record in `third_party/NOTICE.md` (or equivalent) with:

- **Source** (where it came from)
- **License** (SPDX identifier if known)
- **Attribution text** (if required)
- **Redistribution allowed?** (yes/no)
- **Any modifications** made (optional)

> [!IMPORTANT]
> When in doubt: treat the asset as **not redistributable** until proven otherwise.

### Sensitivity rule

Assets must be **safe for public distribution**.

If an image/illustration embeds precise locations of protected sites or private individuals, it must be redacted/aggregated elsewhere and served behind policy.

---

## Performance budgets

- Avoid assets that bloat the JS bundle.
- Prefer:
  - SVG for icons/illustrations
  - WebP for photos
  - WOFF2 for fonts
- Treat ~200 KB per individual asset as a soft ceiling (exceptions must be justified).

---

## Adding a new asset checklist

- [ ] Asset is **UI-only** (not a dataset / export / tile archive).
- [ ] Asset contains **no sensitive content** (locations, private info).
- [ ] File name is `lower-kebab-case` and stable.
- [ ] Optimized/compressed (SVG cleaned, images compressed, etc.).
- [ ] License verified + attribution recorded (third-party only).
- [ ] Used via import or stable public URL (no brittle relative URLs).
- [ ] If referenced in a MapLibre style: endpoint is versioned and CORS-safe.

---

## FAQ

<details>
<summary>Why is KFM strict about assets?</summary>

Because the frontend ships to end users. If something needs governance controls, it must remain behind the policy boundary and be served through governed APIs.

</details>