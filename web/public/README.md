# 🌾 Kansas Frontier Matrix (KFM) — `web/public/` 🌐

<!-- Badges (static) -->
![scope](https://img.shields.io/badge/scope-web%2Fpublic-1f6feb)
![type](https://img.shields.io/badge/type-static_assets-2ea043)
![served_as](https://img.shields.io/badge/served_as-is-f85149)
![principle](https://img.shields.io/badge/principle-provenance--first-8b5cf6)
![maps](https://img.shields.io/badge/maps-MapLibre%20%2B%20Cesium-0ea5e9)

> [!NOTE]
> This folder is **public by definition** 🧾 — everything here can be requested directly by a browser or CDN.
> Treat every byte as **user-visible, cacheable, and auditable**.

---

## ✅ What lives in `web/public/`

Static, runtime-served assets for the KFM web portal (the React/TypeScript UI with 2D/3D mapping) 🗺️✨

Typical examples:
- 🧷 Favicons, `robots.txt`, `manifest.webmanifest`
- 🖼️ Images, logos, icons, screenshots, OG/social cards
- 🔤 Fonts and glyph packs (if you self-host)
- 🧭 Map styling artifacts (MapLibre style JSON, sprites, glyphs)  
- 🌎 3D/terrain related static artifacts (only if needed for Cesium workflows)
- 🧩 Runtime config loaded by the browser (e.g., `config/app-config.json`)  
  - This is useful when you want **environment-specific settings without rebuilding** (API base URL, feature flags, etc.)

---

## 🚦 Ground rules (read this before adding anything)

### ✅ Do
- **Keep assets small & web-friendly**: SVG / WebP / PNG, compressed where possible ⚡
- **Prefer immutable, versioned filenames** for cacheability  
  - Example: `kfm-logo.v3.svg`, `ui-sprite.2026-02-03.png`
- **Record provenance + license** for *every non-trivial asset* (see below) 🧾
- **Use open formats** and avoid proprietary encodings when possible 🔓

### ❌ Don’t
- Don’t put React/TS source code here (that belongs in `web/src/`) 🧯
- Don’t commit secrets (API keys, tokens, analytics secrets, service credentials) 🔒
- Don’t add large datasets here (no multi‑MB GeoJSON dumps, rasters, or “temporary exports”)  
  - If it’s data: route it through the **KFM pipeline → catalog → API → UI** instead.

> [!IMPORTANT]
> KFM’s “map behind the map” principle applies here too: **assets must be attributable** (source + license + any modifications).
> If we can’t explain where an asset came from, it doesn’t ship.

---

## 🗂 Suggested structure

Below is a recommended layout (adapt as the repo evolves):

```text
📁 web/
  📁 public/
    📄 README.md                ← you are here ✅
    🧷 favicon.ico
    🤖 robots.txt
    🧭 manifest.webmanifest

    📁 images/                  ← brand + UI images
      🖼️ kfm-logo.svg
      🖼️ og-cover.png

    📁 icons/                   ← small UI icons (SVG preferred)
      🔹 layers.svg
      🔹 timeline.svg

    📁 styles/                  ← map styles, themes
      🗺️ kfm-basemap.style.json
      🗺️ kfm-dark.style.json

    📁 sprites/                 ← MapLibre sprite sheets (if self-hosting)
      🧩 sprites.json
      🧩 sprites.png

    📁 glyphs/                  ← MapLibre glyphs (if self-hosting)
      🔤 {fontstack}/{range}.pbf

    📁 fonts/                   ← self-hosted web fonts (optional)
      🔤 inter.woff2

    📁 config/                  ← runtime browser config
      ⚙️ app-config.json

    📁 attribution/             ← provenance + license tracking
      🧾 ASSETS.md
      🧾 assets.yml
```

---

## 🧾 Asset provenance (required for anything that isn’t “obviously ours”)

When you add or replace an asset, update **one** of the provenance trackers:

- `web/public/attribution/ASSETS.md` (human-friendly)
- `web/public/attribution/assets.yml` (machine-friendly)

### ✍️ Minimal provenance record (YAML)
```yaml
# web/public/attribution/assets.yml
- path: images/kfm-logo.svg
  source: "KFM design team"
  license: "All rights reserved (project-owned)"
  modified: true
  notes: "Updated stroke widths for small-size rendering"

- path: styles/kfm-basemap.style.json
  source: "Derived from internal KFM cartography spec"
  license: "Project-owned"
  modified: true
  notes: "Tile endpoints point to KFM API; added historic trails layer"
```

> [!TIP]
> For icons/fonts/images pulled from the internet, include:
> **author/organization**, **URL**, **license name/version**, and **proof** (screenshot or license file reference).

---

## 🗺️ Mapping assets: MapLibre + Cesium conventions

KFM’s UI is map-centric; keep mapping artifacts tidy, explicit, and environment-safe.

### MapLibre styles (`public/styles/*.json`)
**Goal:** styles should reference tiles through the governed KFM layer.

**Style URL conventions**
- Use root-relative paths for things we host:
  - `/styles/kfm-basemap.style.json`
- Use API-served tiles (vector/raster) via stable endpoints:
  - `/tiles/{layer}/{z}/{x}/{y}.pbf`
  - `/tiles/{layer}/{z}/{x}/{y}.png` (or `.webp`)

**Example snippet**
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

### 3D / Cesium assets (only if needed)
If you add Cesium-related static artifacts:
- Keep them under `public/cesium/`
- Avoid committing any tokens or access keys
- Prefer runtime injection (env → API → config JSON) rather than embedding secrets in public files

---

## ⚡ Performance & caching checklist

- ✅ Prefer SVG for icons, WebP for photos
- ✅ Compress large PNGs (and keep alpha only when necessary)
- ✅ If you must ship large assets, ensure they are:
  - versioned filenames, and
  - served with long cache headers by the reverse proxy/CDN
- ✅ Avoid duplicate assets (one canonical logo, one canonical icon set)

> [!NOTE]
> A reverse proxy (e.g., Nginx) can serve the built static web output efficiently. When that’s the deployment shape,
> anything shipped from `public/` should be assumed to be **edge-cached**.

---

## 🔒 Security & privacy (non-negotiable)

- ❌ No secrets in `public/` (ever)
- ❌ No private datasets, no personally identifying information
- ✅ Treat all files as crawlable and redistributable

---

## ♿ Accessibility & UX basics

- Provide `alt` text for images used in UI
- Ensure icons have sufficient contrast in light/dark modes 🌗
- Favor readable typography (web-safe fallbacks if fonts fail)

---

## 🧪 Quick smoke tests

After adding or changing an asset:

1. Start the web app (dev server or built static output)
2. Open these in the browser:
   - `/favicon.ico`
   - `/images/<asset>`
   - `/styles/<style>.json`
3. Verify caching doesn’t “trap” old assets (rename/version assets if needed)

---

## 🧯 Common gotchas

<details>
  <summary><strong>🧩 “Why isn’t my asset hashed / bundled?”</strong></summary>

Assets in `public/` are typically copied/served **as-is** (bypassing bundler transforms).
If you need bundling, tree-shaking, or hashing, import it from `web/src/` instead.

</details>

<details>
  <summary><strong>🗺️ “My style.json works locally but not in prod”</strong></summary>

Double-check that:
- style URLs are **root-relative** (`/tiles/...`, `/sprites/...`)  
- the reverse proxy routes `/api/*`, `/graphql`, and `/tiles/*` correctly
- the base path (if any) is consistent between environments

</details>

---

## 🧭 North Star: ship a trustworthy map

KFM is an evidence-first platform. Even front-end “static” artifacts should help maintain:
- transparency 🧾
- reproducibility 🧪
- and long-term maintainability 🧰

If an asset can’t be explained, licensed, and tracked — it doesn’t belong in `public/`.