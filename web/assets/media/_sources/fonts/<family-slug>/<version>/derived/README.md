# 🅰️ Derived Web Fonts — `<family-slug>` / `<version>`

![Derived](https://img.shields.io/badge/derived-generated-blue)
![Formats](https://img.shields.io/badge/formats-woff2%20%7C%20woff-informational)
![Provenance](https://img.shields.io/badge/provenance-first-success)
![Cache](https://img.shields.io/badge/cache-versioned%20path-brightgreen)
![License](https://img.shields.io/badge/license-see%20LICENSE-lightgrey)

> [!IMPORTANT]
> **This folder is build output.** Treat it like a compiled artifact: **do not hand-edit binaries**.  
> If something needs to change, update the upstream/source inputs + pipeline and regenerate ✅

---

## 📌 What is this folder?

This `derived/` directory contains **web-ready** font artifacts generated from the upstream/source fonts located in sibling folders (commonly `../upstream/` and/or `../source/`).  

It exists so the KFM web app can ship fonts that are:

- ⚡ **Fast** (compressed + optionally subset)
- 🧠 **Predictable** (versioned path for caching)
- 🧾 **Auditable** (provenance + checksums + license trail)

---

## 🧭 Quick navigation

- [📁 Folder map](#-folder-map)
- [📦 Expected artifacts](#-expected-artifacts)
- [🧬 Provenance manifest](#-provenance-manifest)
- [🛠️ Regenerating derived fonts](#️-regenerating-derived-fonts)
- [🎨 Using the fonts in CSS](#-using-the-fonts-in-css)
- [✅ QA checklist](#-qa-checklist)
- [⚖️ Licensing & attribution](#️-licensing--attribution)
- [🧯 Troubleshooting](#-troubleshooting)

---

## 📁 Folder map

```text
📁 web/
  📁 assets/
    📁 media/
      📁 _sources/
        📁 fonts/
          📁 <family-slug>/
            📁 <version>/
              📁 upstream/        👈 pristine upstream download(s)
              📁 source/          👈 optional normalized sources (rename/organize only)
              📁 derived/         ✅ you are here (generated outputs)
                📄 README.md
                📄 provenance.json
                📄 checksums.sha256
                🎨 *.css
                🔤 *.woff2
                🔤 *.woff
```

> [!NOTE]
> The exact sibling folder names can vary (`upstream/`, `source/`, `original/`, etc.).  
> The **rule** is consistent: `derived/` is **reproducible output**, not the place to store the “source of truth”.

---

## 📦 Expected artifacts

| Item | Required | Purpose |
|---|:---:|---|
| `*.woff2` | ✅ | Primary web format (small + modern) |
| `*.woff` | ✅ | Fallback web format |
| `*.css` | ⚠️ recommended | One importable file with `@font-face` rules pointing at local font binaries |
| `provenance.json` | ✅ | Where this font came from + exactly how it was transformed |
| `checksums.sha256` | ✅ | Verifiable integrity for generated artifacts |
| `LICENSE` / `LICENSES/` | ✅ (in `<version>/`) | Ensure license text is present and discoverable |
| `ATTRIBUTION.md` | ⚠️ recommended | Human-readable credit + upstream link(s) |

### 🧩 Naming conventions (recommended)

Keep names deterministic and cache-friendly:

- `<family-slug>-<style>-<weight>.woff2`
- `<family-slug>-<style>-<weight>.woff`
- Optional subsets:
  - `<family-slug>-latin-regular-400.woff2`
  - `<family-slug>-latin-ext-regular-400.woff2`
  - `<family-slug>-full-regular-400.woff2`

> [!TIP]
> If you subset, encode **subset scope** in the filename (e.g., `latin`, `ui`, `symbols`) so you can reason about glyph coverage without opening the font.

---

## 🧬 Provenance manifest

KFM treats “anything visible in the UI” as traceable and non-mysterious. Fonts are UI-visible too. 🧾

### ✅ `provenance.json` (minimum suggested fields)

Create/maintain a `provenance.json` with at least:

- Upstream identity: name, author/publisher, URL(s), version/tag
- License: SPDX identifier if possible + link to license text
- Inputs: filenames + hashes for upstream/source inputs
- Pipeline: toolchain + commands/steps (high-level is fine)
- Outputs: generated filenames + hashes
- Notes: subsetting strategy, unicode ranges, hinting choices

Example:

```json
{
  "assetType": "font",
  "familySlug": "<family-slug>",
  "version": "<version>",
  "upstream": {
    "name": "<Upstream Family Name>",
    "url": "<https://…>",
    "releaseTagOrVersion": "<vX.Y.Z>",
    "retrievedAt": "<YYYY-MM-DD>"
  },
  "license": {
    "spdx": "<OFL-1.1|Apache-2.0|…>",
    "licenseFile": "../LICENSE"
  },
  "inputs": [
    { "path": "../upstream/<file>.ttf", "sha256": "<…>" }
  ],
  "transform": [
    { "step": "subset", "notes": "Latin + punctuation for UI", "unicodes": "U+0000-00FF, U+2000-206F" },
    { "step": "convert", "notes": "WOFF2 + WOFF outputs generated" }
  ],
  "outputs": [
    { "path": "./<family-slug>-regular-400.woff2", "sha256": "<…>" },
    { "path": "./<family-slug>-regular-400.woff", "sha256": "<…>" }
  ]
}
```

> [!IMPORTANT]
> “No mystery assets.” If a font ships in the web UI, it must have **source + license + transform steps** recorded here.

---

## 🛠️ Regenerating derived fonts

### 1) Put upstream sources in the right place

- Drop pristine upstream archives/files into `../upstream/`
- Preserve upstream license text(s) alongside the upstream files or at `<version>/LICENSE*`
- If you normalize filenames, do it in `../source/` (not in `derived/`)

### 2) Update metadata + checksums

- Update `provenance.json`
- Recompute `checksums.sha256` after regeneration

Example format for `checksums.sha256`:

```text
<sha256>  <family-slug>-regular-400.woff2
<sha256>  <family-slug>-regular-400.woff
<sha256>  provenance.json
```

### 3) Run the font pipeline (project-specific)

This repo may generate derived assets via a Make target, a script under `scripts/`, or the web build pipeline.

**Recommended pattern:**
- A single deterministic command that can be run in CI (and locally)
- Outputs written only to `derived/`
- Updates `checksums.sha256`

> [!NOTE]
> If you can’t find a font pipeline yet, create one in `scripts/fonts/` and wire it into CI. This keeps the “derived” contract real, not aspirational.

---

## 🎨 Using the fonts in CSS

### ✅ Recommended: ship a local `*.css` in `derived/`

Create something like `./<family-slug>.css` so the web UI can import one file.

Example `@font-face` (WOFF2 primary + WOFF fallback):

```css
@font-face {
  font-family: "<Family Display Name>";
  src:
    url("./<family-slug>-regular-400.woff2") format("woff2"),
    url("./<family-slug>-regular-400.woff") format("woff");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

Then in your site CSS:

```css
@import url("/assets/media/_sources/fonts/<family-slug>/<version>/derived/<family-slug>.css");

:root {
  --kfm-font-ui: "<Family Display Name>", system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
}

body {
  font-family: var(--kfm-font-ui);
}
```

> [!TIP]
> Paths in `@font-face` are **relative to the CSS file location**. If you move the CSS, update URLs accordingly.

### ⚡ Optional: preload

If the font is critical to above-the-fold UI:

```html
<link
  rel="preload"
  href="/assets/media/_sources/fonts/<family-slug>/<version>/derived/<family-slug>-regular-400.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
```

---

## ✅ QA checklist

Before merging derived font updates:

- [ ] **License present** (OFL/Apache/etc. text included and correct)
- [ ] **Attribution present** (`ATTRIBUTION.md` recommended)
- [ ] **Provenance complete** (`provenance.json` has upstream URL + transform summary)
- [ ] **Checksums updated** (`checksums.sha256` matches current outputs)
- [ ] **No broken URLs** in `*.css` (`@font-face` points at existing binaries)
- [ ] **Browser sanity check** (Chrome/Firefox/Safari)
- [ ] **Weight/style mapping correct** (400 vs 700, italic vs normal, etc.)
- [ ] **Performance budget** met (avoid shipping unused glyph ranges)
- [ ] **No remote dependencies** introduced (fonts should load from repo-hosted assets)

---

## ⚖️ Licensing & attribution

Fonts are *not* code — they carry their own licenses and attribution requirements.

**Rules of thumb:**
- Always store license text at `<version>/LICENSE*` (or `<version>/LICENSES/…`)
- Always keep upstream URLs in `provenance.json`
- If upstream requires attribution, include an `ATTRIBUTION.md`

Example `ATTRIBUTION.md` template:

```md
# Attribution — `<family-slug>` `<version>`

- Upstream: <name>
- URL: <link>
- License: <SPDX>
- Notes: Derived outputs (WOFF2/WOFF) generated for KFM web UI.
```

---

## 🧯 Troubleshooting

### Font loads but doesn’t apply
- `font-family` name mismatch between `@font-face` and your CSS usage
- Weight mismatch (e.g., you request `font-weight: 600` but only shipped 400/700)

### 404 / missing font files
- Import path is wrong (absolute vs relative)
- `@font-face` URLs are relative to the CSS file location

### CORS / preload issues
- If you serve fonts from a different origin (CDN), ensure `crossorigin` is set consistently on preload + server headers.

---

## 🧪 Optional: deeper notes (click to expand)

<details>
  <summary><strong>🔬 Subsetting strategy</strong></summary>

- Prefer small “UI” subsets when the font is only used for interface chrome (menus, buttons, labels).
- Keep a “full” variant only when needed for story text, multilingual content, or citations.

</details>

<details>
  <summary><strong>🧊 Cache strategy</strong></summary>

- The `<version>/` folder is a natural cache-buster.
- If you also fingerprint filenames (hash in filename), you can cache forever and avoid invalidations.

</details>
