# Fonts — `web/public/fonts` 🔤

![Governed](https://img.shields.io/badge/governed-FAIR%2BCARE-2ea44f)
![Static Assets](https://img.shields.io/badge/type-static%20assets-blue)
![License Required](https://img.shields.io/badge/requirement-license%20file-important)

This directory contains **publicly-served font assets** used by the KFM web UI and map rendering stack.

Because everything under `web/public/` is typically shipped as-is to the browser (no “trust membrane” inside the client), **fonts are treated as third‑party dependencies**: they must be **licensed**, **attributed**, and **pinned**.

---

## What belongs here

### 1) UI Web Fonts
Files such as:
- `*.woff2` (preferred)
- `*.woff` (fallback if required)
- `*.ttf` (generally avoid shipping to browsers unless you have a specific need)

These are referenced via CSS (`@font-face`) and loaded by the application shell/UI.

### 2) Map Glyphs for Map Rendering
If the map style uses a `glyphs` URL template (commonly `{fontstack}/{range}.pbf`), this folder may also host **glyph PBFs** so the app can run **without external font CDNs**.

> ✅ Rule: **No runtime fetching of fonts/glyphs from third-party CDNs** unless explicitly approved by governance review (privacy, availability, licensing).

---

## Directory layout

Recommended structure (one folder per “font asset unit”):

```text
web/public/fonts/
  README.md
  _manifest/
    fonts.manifest.json         # optional but recommended
  <family-name>/
    LICENSE.txt                 # required
    SOURCE.json                 # required
    CHANGELOG.md                # optional
    web/
      <family>-<weight>-<style>.woff2
      <family>-<weight>-<style>.woff
  glyphs/                       # if self-hosting map glyphs
    <Font Stack Name>/
      0-255.pbf
      256-511.pbf
      ...
```

### Naming conventions

| Asset type | Convention | Example |
|---|---|---|
| Folder | kebab-case | `ibm-plex-sans/` |
| Web font file | `family-weight-style.ext` | `ibm-plex-sans-400-normal.woff2` |
| Glyph fontstack folder | must match style `text-font` name | `Noto Sans Regular/` |

> ⚠️ Map glyph “fontstack” names must match what your map style requests. If the style requests `["Noto Sans Regular"]`, the folder name must match exactly.

---

## Governance + compliance requirements (non-negotiable)

Every font family folder **MUST** include:

- `LICENSE.txt`  
  The full license text (or the license file distributed with the font).

- `SOURCE.json`  
  A small provenance record that makes the asset auditable.

### `SOURCE.json` template

```json
{
  "asset_type": "web-font | map-glyphs",
  "family": "Example Sans",
  "version": "1.002",
  "license_spdx": "OFL-1.1",
  "copyright": "Copyright (c) ...",
  "upstream": {
    "name": "Upstream project or foundry",
    "url": "https://example.org/font",
    "retrieved_utc": "2026-02-17T00:00:00Z"
  },
  "files": [
    { "path": "web/example-sans-400-normal.woff2", "sha256": "<sha256>" }
  ],
  "notes": "Describe any subsetting, renaming, or transformation performed."
}
```

### “Definition of Done” checklist ✅

- [ ] Font license is compatible with KFM distribution goals.
- [ ] `LICENSE.txt` is present and accurate.
- [ ] `SOURCE.json` is present and complete.
- [ ] All shipped files are **pinned** with `sha256`.
- [ ] If glyphs exist: glyph folder names match the map style’s requested font stack(s).
- [ ] No external runtime font URLs remain in CSS or map style JSON.

---

## Adding a new UI font

1. Create a folder:
   - `web/public/fonts/<family-name>/`

2. Add provenance + license:
   - `LICENSE.txt`
   - `SOURCE.json`

3. Add web formats:
   - Prefer `woff2` first
   - Add `woff` only if you must support older browsers

4. Reference in CSS (example):

```css
/* Example: web/src/styles/fonts.css */
@font-face {
  font-family: "Example Sans";
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src:
    url("/fonts/example-sans/web/example-sans-400-normal.woff2") format("woff2"),
    url("/fonts/example-sans/web/example-sans-400-normal.woff") format("woff");
}
```

> ✅ Use `font-display: swap` for perceived performance and accessibility (text remains visible).

---

## Adding / generating map glyphs (self-hosted)

If your map style includes something like:

```json
{
  "glyphs": "/fonts/glyphs/{fontstack}/{range}.pbf"
}
```

then you must provide glyph PBF ranges under:

- `web/public/fonts/glyphs/<Font Stack Name>/<range>.pbf`

### Recommended approach

- Keep source TTF/OTF files **out of `public/`** unless you explicitly need to ship them to browsers.
- Generate only the glyph PBF outputs required by your style’s font stacks.

> 🧩 Implementation detail: tooling varies (Fontnik/node-fontnik and similar pipelines exist).  
> If your repo already contains a `fonts:build` script, use that. If not, add one in a governed PR with reproducible inputs + pinned tool versions.

---

## Performance guidance

- Prefer `woff2`
- Avoid shipping multiple large families if you can subset (only if the license permits and you record the transformation in `SOURCE.json`)
- Keep the number of weights/styles minimal (e.g., 400/600 normal, maybe 400 italic)
- Cache aggressively at the CDN/server layer (fonts are great candidates for long-lived caching)

---

## Security & privacy notes

- Fonts are **active content** in the sense that they can be complex binary formats. Treat them like any third‑party dependency:
  - Pin checksums
  - Prefer reputable upstreams
  - Avoid “mystery zip files” with unclear provenance

- Do not load fonts from third-party CDNs by default:
  - avoids passive tracking (network requests)
  - avoids availability failures
  - makes builds reproducible

---

## Troubleshooting

### Map labels show boxes/tofu (□) or missing glyphs
- The map style is requesting a font stack you don’t host.
- Verify:
  - `glyphs` URL template points to `/fonts/glyphs/{fontstack}/{range}.pbf`
  - the folder name under `glyphs/` matches the style’s `text-font` entry exactly

### 404s on `/fonts/...`
- Confirm the build pipeline copies `web/public/*` to the final static output.
- Confirm paths begin with `/fonts/...` (leading slash) for absolute URLs.

---

## Optional: add a manifest for quick auditing

If you choose to maintain a manifest, place it here:

- `web/public/fonts/_manifest/fonts.manifest.json`

Example shape:

```json
{
  "generated_utc": "2026-02-17T00:00:00Z",
  "families": [
    {
      "slug": "example-sans",
      "family": "Example Sans",
      "license_spdx": "OFL-1.1",
      "source_file": "/fonts/example-sans/SOURCE.json"
    }
  ]
}
```

---

## Contact / ownership

- **Owners:** Web UI + Governance reviewers (licenses & provenance)
- **Review required:** any new font family, any license change, any glyph generation pipeline change