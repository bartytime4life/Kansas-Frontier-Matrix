# KfmSerif — Source, License & Usage 🔤📜

![asset](https://img.shields.io/badge/asset-font-blue)
![status](https://img.shields.io/badge/status-needs_review-orange)
![license](https://img.shields.io/badge/license-TBD-lightgrey)

> 📌 **Purpose:** This `SOURCE.md` exists so every bundled font in **Kansas Frontier Matrix (KFM)** has clear **provenance + licensing**.  
> Fonts are not “just files” — they’re **licensed software/artwork**, and web-embedding them requires the right permissions.

---

## 🧭 Table of Contents

- [📦 Folder Contents](#-folder-contents)
- [🧾 Provenance Record](#-provenance-record)
- [✅ License & Distribution Checklist](#-license--distribution-checklist)
- [🔧 Build & Conversion Notes](#-build--conversion-notes)
- [🧑‍💻 Usage in the Web App](#-usage-in-the-web-app)
- [🔐 Integrity](#-integrity)
- [🔄 Updating This Font](#-updating-this-font)

---

## 📦 Folder Contents

> Keep this list **in sync** with the actual files in this folder.

📁 `web/src/assets/fonts/KfmSerif/`

- `*.woff2` — ✅ preferred webfont format
- `*.woff` — optional fallback
- `*.ttf` / `*.otf` — optional “source” format (generally **not** served to browsers)
- `LICENSE*` / `OFL*` — **required** license text (exact name depends on upstream)
- `SOURCE.md` — ✅ this provenance + licensing record

Example (rename to match reality):
```text
📁 web/src/assets/fonts/KfmSerif/
├─ KfmSerif-Regular.woff2
├─ KfmSerif-Italic.woff2
├─ KfmSerif-Bold.woff2
├─ LICENSE.txt
└─ SOURCE.md
```

---

## 🧾 Provenance Record

> ⚠️ **Do not ship this font publicly** until the **license + upstream source** below are confirmed.

| Field | Value |
|---|---|
| **Font family (local name)** | `KfmSerif` |
| **Upstream typeface name** | `TBD` |
| **Designer / Foundry** | `TBD` |
| **Original source URL** | `TBD` |
| **Retrieved on** | `YYYY-MM-DD` |
| **Upstream version / release** | `TBD (tag/version/commit)` |
| **License type** | `TBD (e.g., OFL-1.1 / Apache-2.0 / Commercial)` |
| **License file in this folder** | `TBD (e.g., LICENSE.txt / OFL.txt)` |
| **Allowed usage confirmed** | ☐ desktop ☐ web embedding ☐ app ☐ ePub ☐ other: ___ |
| **Attribution required** | `TBD (yes/no + exact wording if required)` |
| **Modifications made** | `TBD (none / renamed / subset / converted)` |
| **Modified by / date** | `TBD` |

---

## ✅ License & Distribution Checklist

### Minimum bar to merge ✅
- [ ] **Source confirmed** (designer/foundry + where it was obtained)
- [ ] **License confirmed** (license name + text included locally)
- [ ] License explicitly permits **web embedding** (shipping `.woff2` with the app)
- [ ] If attribution is required: it exists in the appropriate credits/legal place
- [ ] If commercial/proprietary: we have proof of purchase + redistribution terms documented

### Red flags 🚩 (stop ship)
- [ ] “Free for personal use only”
- [ ] “No redistribution”
- [ ] “Desktop license only” (no webfont license)
- [ ] Source is unknown / “found on the internet”

> If any red flag applies, replace KfmSerif with a clearly licensed alternative and document it here.

---

## 🔧 Build & Conversion Notes

If the upstream font was provided as `.ttf` / `.otf` and we generated webfonts:

- Tooling used: `TBD` (e.g., `fonttools`, `pyftsubset`, `woff2_compress`)
- Subsetting: `TBD` (glyph ranges / unicode ranges)
- Output targets:
  - ✅ `woff2` (primary)
  - ☐ `woff` (fallback)

Optional: record build commands for reproducibility:
```bash
# Example only — replace with real commands if you used them
# pyftsubset Upstream.ttf --output-file=KfmSerif-Regular.woff2 --flavor=woff2 --layout-features='*'
```

---

## 🧑‍💻 Usage in the Web App

### `@font-face` example 🎛️

> Adjust file names + paths to match your bundler (Vite/Webpack/etc).  
> Because this `SOURCE.md` sits next to the font files, relative paths shown here are “local-folder examples”.

```css
/* Example only — update filenames to match actual assets */

@font-face {
  font-family: "KfmSerif";
  src: url("./KfmSerif-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "KfmSerif";
  src: url("./KfmSerif-Italic.woff2") format("woff2");
  font-weight: 400;
  font-style: italic;
  font-display: swap;
}

@font-face {
  font-family: "KfmSerif";
  src: url("./KfmSerif-Bold.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
```

### Design token suggestion 🧩

Use a token so theming can swap fonts cleanly:

```css
:root {
  --font-serif: "KfmSerif", ui-serif, Georgia, "Times New Roman", Times, serif;
}
```

---

## 🔐 Integrity

Recommended: record checksums whenever font binaries change.

```text
# sha256 (fill in)
TBD  KfmSerif-Regular.woff2
TBD  KfmSerif-Italic.woff2
TBD  KfmSerif-Bold.woff2
```

---

## 🔄 Updating This Font

1. ✅ Identify the upstream typeface and official distribution source.
2. ✅ Verify the license supports:
   - bundling in this repo (redistribution)
   - web embedding (webfont usage)
3. ✅ Add the full license text into this folder (`LICENSE.txt`, `OFL.txt`, etc.).
4. ✅ If converting/subsetting:
   - document the tools + commands in **Build & Conversion Notes**
5. ✅ Update:
   - **Provenance Record**
   - **Integrity checksums**
6. ✅ Confirm the UI still renders correctly across:
   - headings
   - body text
   - italics/bold
   - extended characters (if needed)

---

### 🧠 Reminder

Having the technical ability to embed a font does **not** automatically grant legal permission to do so. Treat this file as the “single source of truth” for **what we shipped and why we’re allowed to ship it**.
