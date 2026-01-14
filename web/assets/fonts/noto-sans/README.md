<!-- Path: web/assets/fonts/noto-sans/README.md -->

# 🅽🅾🆃🅾 🆂🅰🅽🆂 — Self‑Hosted Web Fonts for KFM 🗺️✨

![Font](https://img.shields.io/badge/font-Noto%20Sans-111827?logo=googlefonts&logoColor=white)
![License](https://img.shields.io/badge/license-OFL%201.1-16a34a)
![Asset%20Type](https://img.shields.io/badge/asset-web%20font-2563eb)
![Principle](https://img.shields.io/badge/principle-provenance--first-f97316)

KFM’s UI is a **data + map** product. Typography is not decoration — it’s **infrastructure** 🧱:
- readable legends & map labels 🧭  
- consistent UI hierarchy 🧩  
- accessible, multilingual-friendly text 🌍  

This folder is the **single source of truth** for the **Noto Sans** font files we self-host for the web frontend.

---

## ✅ Quick Start

### 1) Prefer WOFF2 binaries for the web 📦
Place web-ready font files (ideally **`.woff2`**) in this folder (or in `./woff2/` if you choose to organize that way).

### 2) Wire up `@font-face` 🎛️
Add a CSS file (recommended: `noto-sans.css`) and import it from your global stylesheet / app entry.

```css
/* Example: web/assets/fonts/noto-sans/noto-sans.css */

@font-face {
  font-family: "Noto Sans";
  src: url("./NotoSans-VariableFont_wdth,wght.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Noto Sans";
  src: url("./NotoSans-Italic-VariableFont_wdth,wght.woff2") format("woff2");
  font-weight: 100 900;
  font-style: italic;
  font-display: swap;
}

/* Project-wide default */
:root {
  --font-sans: "Noto Sans", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
}

body {
  font-family: var(--font-sans);
}
```

### 3) (Optional) Preload for faster first paint 🚀
```html
<link rel="preload"
      href="/assets/fonts/noto-sans/NotoSans-VariableFont_wdth,wght.woff2"
      as="font"
      type="font/woff2"
      crossorigin>

<link rel="preload"
      href="/assets/fonts/noto-sans/NotoSans-Italic-VariableFont_wdth,wght.woff2"
      as="font"
      type="font/woff2"
      crossorigin>
```

---

## 📁 Expected Folder Layout

> Keep it boring. Boring is stable. Stable is fast. ⚙️

```text
web/
└─ assets/
   └─ fonts/
      └─ noto-sans/
         ├─ README.md
         ├─ OFL.txt                      # License text (required)
         ├─ noto-sans.meta.json          # Provenance + “asset contract” (recommended)
         ├─ noto-sans.css                # @font-face rules (recommended)
         ├─ NotoSans-VariableFont_wdth,wght.woff2
         ├─ NotoSans-Italic-VariableFont_wdth,wght.woff2
         └─ subsets/                     # Optional: generated unicode-range subsets
            ├─ NotoSans-Latin.woff2
            ├─ NotoSans-LatinExt.woff2
            └─ ...
```

If you choose to store `.ttf` sources for builds, keep them **clearly separated**:

```text
ttf-src/   # source-only (not served by default)
woff2/     # served webfont binaries
```

---

## 🧠 Why Noto Sans for KFM?

Noto Sans is a strong default for a **“living atlas” UI** because it supports:
- **clear UI hierarchy** (lots of weights) 🧱  
- **maps + dashboards + documents** (clean labeling) 🗺️📊  
- **global language coverage via the broader Noto ecosystem** 🌍  

> KFM’s “provenance-first” philosophy applies to *every* asset that reaches the UI — including fonts. 🧾

---

## 🧾 Provenance-First Font Assets

KFM treats metadata as first-class data. Fonts should follow the same rule ✅

### `noto-sans.meta.json` (recommended)
Create a metadata file describing where the font came from, under what license, and how we built the shipped binaries.

```json
{
  "asset_type": "font",
  "family": "Noto Sans",
  "intended_usage": ["ui", "map-labels", "charts", "docs"],
  "source": {
    "upstream": "Google Fonts / Noto Project",
    "download_page": "https://fonts.google.com/noto/specimen/Noto+Sans",
    "retrieved_on": "YYYY-MM-DD",
    "version": "UNKNOWN"
  },
  "license": {
    "name": "SIL Open Font License 1.1",
    "file": "./OFL.txt"
  },
  "build": {
    "served_format": "woff2",
    "notes": "Converted from upstream TTF/OTF using standard tooling.",
    "commands": [
      "pyftsubset ...",
      "woff2_compress ..."
    ]
  },
  "integrity": {
    "files": [
      { "path": "NotoSans-VariableFont_wdth,wght.woff2", "sha256": "TODO" },
      { "path": "NotoSans-Italic-VariableFont_wdth,wght.woff2", "sha256": "TODO" }
    ]
  }
}
```

**Rule of thumb:** if it ships to users, it should have a provenance record. 🧭

---

## ⚡ Performance Notes (Fonts Are “Hot Path” Assets)

### Prefer variable fonts 🎚️
One variable font can replace multiple static files (fewer requests, simpler maintenance).

### Prefer WOFF2 📉
WOFF2 is specifically designed for webfont delivery and better compression.

### Use `font-display: swap` 🪄
Avoid invisible text (FOIT). “Swap” gives a fast readable UI even if the font loads slightly later.

### Subset if needed ✂️
For map-heavy or dashboard-heavy experiences, subsetting can pay off quickly:
- `latin` + `latin-ext` as a base
- add scripts as needed (Arabic, Devanagari, Thai, CJK, etc.)
- use `unicode-range` to load subsets progressively

Example subset split:

```css
@font-face {
  font-family: "Noto Sans";
  src: url("./subsets/NotoSans-Latin.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC;
}
```

---

## 🗺️ Map Labeling Tips (Practical KFM Defaults)

Typography for maps isn’t “just CSS” — it affects comprehension:

- **Use size + weight for hierarchy**, not color alone 🎚️  
- Keep labels readable on **mobile** (avoid hairline weights for tiny text) 📱  
- Prefer **consistent letterspacing** (don’t over-track small labels) 🧷  
- If you’re rendering labels in **Canvas/WebGL overlays**, confirm the font is loaded before drawing 🧠

---

## 🧩 “Flexible Software Design” Applied to Font Assets

To keep typography maintainable long-term:

- **Stable identifiers:** don’t “mystery rename” shipped binaries 🔒  
- **Clear contracts:** keep a metadata JSON (“what is this + where did it come from?”) 🧾  
- **Small blast radius:** keep font assets isolated to this folder (no scattered copies) 🧯  

---

## 🛠️ Updating Noto Sans (Safe Process)

1. 📥 Download from an authoritative upstream (Google Fonts / Noto Project)
2. 📜 Update `OFL.txt` if upstream license text changed (rare)
3. 🧰 Convert to `.woff2` (and subset if applicable)
4. 🔐 Record hashes in `noto-sans.meta.json`
5. ✅ Verify:
   - `@font-face` resolves in DevTools
   - italics render as italics
   - no 404s; correct cache headers
   - Lighthouse / performance budget stays healthy

---

## 🧯 Troubleshooting

### “Font loads but doesn’t apply”
- Confirm CSS is imported and not tree-shaken
- Confirm the `font-family` name matches exactly (`"Noto Sans"`)
- Check if a more specific selector overrides your base styles

### “Network shows font downloaded, but browser rejects it”
- Ensure the server serves `.woff2` with the correct MIME type (`font/woff2`)
- Ensure CORS is correct if fonts are served from a different origin

### “Italic looks fake / slanted”
- Make sure the italic font file is present and mapped to `font-style: italic`

---

## 📜 License

Noto Sans is licensed under the **SIL Open Font License, Version 1.1** ✅  
See: **[`./OFL.txt`](./OFL.txt)**

> If you modify the font files and redistribute them, follow OFL requirements (including naming rules). 🔍

---

## 🔗 External References

- Google Noto: https://fonts.google.com/noto  
- Noto Sans specimen: https://fonts.google.com/noto/specimen/Noto+Sans  
- Noto Fonts dashboard: https://notofonts.github.io/  
- SIL OFL 1.1: https://openfontlicense.org/  
- WOFF2 spec (W3C): https://www.w3.org/TR/WOFF2/  

---

## 📚 Project Reference Shelf (Why we care about typography)

<details>
  <summary>🗂️ Click to expand the KFM project library touchpoints</summary>

- 🧭 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** (provenance-first, clean architecture)
- 🧱 **Flexible Software Design** (stable identifiers, modularity, long-haul maintainability)
- 📱 **Responsive Web Design with HTML5 and CSS3** (web typography, @font-face)
- 🗺️ **Making Maps: A Visual Guide to Map Design for GIS** (labeling & cartographic hierarchy)
- 🛰️ **Cloud-Based Remote Sensing with Google Earth Engine** (dense scientific UI needs clarity)
- 🧮 **Understanding Statistics & Experimental Design / Regression Analysis** (charts + readable annotation)
- ⚙️ **Database Performance at Scale / Scalable Data Management** (performance mindset applied to assets)
- 🧠 **Introduction to Digital Humanism** (human-centered systems; readability is accessibility)
- 🧱 **WebGL Programming Guide** (overlay UI typography considerations)

</details>
