# Fonts 🅰️🗺️

![Provenance-first](https://img.shields.io/badge/Provenance-first-2ea44f)
![Self-hosted](https://img.shields.io/badge/Fonts-self--hosted-1f6feb)
![Formats](https://img.shields.io/badge/Formats-WOFF2%20%7C%20WOFF-6e7781)
![UX](https://img.shields.io/badge/UX-maps%20%26%20data%20UI-8250df)

This folder contains **self-hosted web fonts** used by the Kansas Frontier Matrix (KFM) web UI (maps, dashboards, stories, tooltips, legends, and any “data-with-context” views).

Typography isn’t decoration here — it’s *infrastructure* for readable maps and trustworthy, inspectable UI.

---

## What lives here 📦

✅ **What belongs in this folder**
- Web-optimized font binaries: **`.woff2`** (preferred) and optionally **`.woff`** (fallback)
- A **license file** for each font family (`LICENSE`, `LICENSE.txt`, etc.)
- A **provenance + metadata record** (see “Provenance” below)
- Optional: subsetting scripts/notes, specimen images, and README per family

🚫 **What does *not* belong here**
- “Mystery fonts” with unknown origin or unclear license
- Runtime-loaded third-party font CSS (e.g., remote Google Fonts) for production UI
- Random `.ttf/.otf` binaries intended to be served directly (keep as sources only if needed)

---

## Guiding principles 🧭

### 1) Provenance-first (KFM style) 🔎
Fonts are treated like any other KFM-visible asset: **traceable, auditable, and attributable**.
That means:
- Every font family **must** ship with:
  - source (where it came from),
  - license (how we can use it),
  - and what transformations we applied (subset/convert/version).

### 2) Prefer open, redistributable fonts 🪪
Aim for fonts with clear, permissive redistribution terms (commonly: OFL, Apache 2.0, MIT-like).
If a license is unclear, **do not commit** the font.

### 3) Performance is a feature ⚡
- Prefer **WOFF2**
- Prefer **variable fonts** where it reduces total payload
- Prefer **subset fonts** (latin-only, etc.) when we can justify it
- Use caching + fingerprinting (immutable assets) where the web stack supports it

### 4) Map readability wins 🗺️
Map labels and legends need:
- consistent spacing,
- careful kerning/letterspacing at larger sizes,
- and avoidance of awkward line breaks/hyphenation on labels.

---

## Folder layout 🗂️

Recommended structure:

```text
web/assets/fonts/
├── README.md
├── fonts.manifest.json              (optional, recommended)
├── inter/                           (example)
│   ├── Inter-roman.var.woff2
│   ├── Inter-italic.var.woff2
│   ├── LICENSE.txt
│   ├── SOURCE.md
│   └── font.metadata.json
├── noto-sans/                       (example)
│   ├── NotoSans-latin-400.woff2
│   ├── NotoSans-latin-700.woff2
│   ├── LICENSE.txt
│   ├── SOURCE.md
│   └── font.metadata.json
└── ...more families...
```

**Naming conventions**
- Use `FamilyName-*` filenames (stable + readable)
- If subsetting: encode subset in filename, e.g. `Family-latin-*`, `Family-latin-ext-*`
- If fingerprinting: append hash at build time, e.g. `Inter-roman.var.4c2a1c2.woff2`

---

## Required files per font family ✅

| File | Required | Purpose |
|------|----------|---------|
| `*.woff2` | ✅ | Primary delivery format |
| `*.woff` | ⭕ | Optional fallback for older environments |
| `LICENSE*` | ✅ | Legal redistribution + usage terms |
| `SOURCE.md` | ✅ | Human-readable provenance (URLs, author, version, where downloaded) |
| `font.metadata.json` | ✅ | Machine-readable metadata for attribution + audits |
| `*.ttf/*.otf` | ⭕ | Optional “source” files (not served) |
| `SUBSET.md` | ⭕ | Notes on subsetting decisions + commands used |

---

## Provenance metadata 🔐

### `font.metadata.json` (recommended schema)

At minimum:

```json
{
  "id": "inter",
  "family": "Inter",
  "version": "4.0.0",
  "source": {
    "name": "Upstream project / foundry",
    "url": "https://example.com/font",
    "retrieved_at": "2026-01-14"
  },
  "license": {
    "spdx": "OFL-1.1",
    "file": "LICENSE.txt"
  },
  "files": [
    {
      "path": "Inter-roman.var.woff2",
      "format": "woff2",
      "style": "normal",
      "weight": "100 900",
      "subset": "latin",
      "sha256": "REPLACE_ME"
    }
  ],
  "build": {
    "converted": false,
    "subsetted": true,
    "tools": [
      "fonttools",
      "pyftsubset"
    ],
    "notes": "Subset to latin to reduce payload."
  }
}
```

> [!TIP]
> If your build pipeline can compute hashes automatically, do it — it makes integrity checks and cache busting much easier.

---

## Using fonts in CSS 🎨

We typically define `@font-face` rules in the web app stylesheet (example path: `web/styles/fonts.css`) and reference font files from this directory.

### Example: variable WOFF2
```css
@font-face {
  font-family: "Inter";
  src: url("/assets/fonts/inter/Inter-roman.var.woff2") format("woff2");
  font-style: normal;
  font-weight: 100 900;
  font-display: swap;
}
```

### Example: WOFF2 + WOFF fallback
```css
@font-face {
  font-family: "Noto Sans";
  src:
    url("/assets/fonts/noto-sans/NotoSans-latin-400.woff2") format("woff2"),
    url("/assets/fonts/noto-sans/NotoSans-latin-400.woff") format("woff");
  font-style: normal;
  font-weight: 400;
  font-display: swap;
}
```

> [!NOTE]
> If fonts are served from a different domain/subdomain than the site, confirm `crossorigin` and CORS headers are correct.

---

## Performance & caching ⚡🧊

### Preload only what’s truly critical
Use preload sparingly (usually 1–2 fonts max):

```html
<link
  rel="preload"
  href="/assets/fonts/inter/Inter-roman.var.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
```

### Cache like a grown-up 🧠
When fingerprinting is enabled:
- Serve fonts with long-lived caching, e.g. `Cache-Control: public, max-age=31536000, immutable`
- Change the filename when the file changes

### Subset when it’s justified ✂️
If the UI is primarily English/Latin labels:
- keep a **latin subset** for UI and map labels
- keep a separate broader subset only if needed (e.g., multilingual datasets)

---

## Map & data-UI typography tips 🗺️🔤

- Keep labels **as horizontal as possible** (readability)
- Avoid hyphenation/breaking labels when possible
- Use consistent line spacing for similar features
- Watch kerning on large labels/titles (big text makes spacing issues louder)
- Don’t “justify” label text if it introduces weird spacing

---

## QA checklist ✅

Before merging a new font:
- [ ] Folder exists under `web/assets/fonts/<family>/`
- [ ] `LICENSE*` included and matches actual font license
- [ ] `SOURCE.md` includes upstream URL + version + retrieval date
- [ ] `font.metadata.json` present and accurate
- [ ] Only `.woff2`/`.woff` are served (ttf/otf are not referenced by CSS)
- [ ] Map labels + legends visually checked at typical zoom levels
- [ ] Build output confirms correct caching strategy (fingerprints/headers)

---

## Attribution 🧾

This repo aims to generate attribution automatically when possible.

If you add fonts:
1) Ensure `font.metadata.json` is complete  
2) Ensure the license text is included  
3) If an attribution string is required by the license, add it to `SOURCE.md`

> [!WARNING]
> If a font’s license restricts redistribution or requires special attribution you can’t satisfy, **do not include it**.

---

## Quick “add a font” checklist 🚀

1. 📥 Download font from its official source  
2. 🧼 Convert to `.woff2` (and `.woff` if needed)  
3. ✂️ Subset if appropriate (document the decision)  
4. 🪪 Add license file  
5. 🧾 Write `SOURCE.md` + `font.metadata.json`  
6. 🎨 Add/adjust `@font-face` rules  
7. 🗺️ Visual QA on maps, legends, tooltips  
8. ✅ Commit

---