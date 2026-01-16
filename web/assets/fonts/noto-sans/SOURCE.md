# Noto Sans — Source & Licensing 🔤

![License: OFL-1.1](https://img.shields.io/badge/License-OFL--1.1-success)
![Asset: Web Fonts](https://img.shields.io/badge/Asset-Web%20Fonts-blue)
![Family: Noto Sans](https://img.shields.io/badge/Family-Noto%20Sans-informational)

This folder contains **Noto Sans** webfont assets used by the KFM/Kansas-Frontier-Matrix web UI.

> 🧭 **Provenance-first note:** KFM treats provenance as a first-class feature. This file exists so the font assets are **traceable, auditable, and reproducible**—just like datasets and map layers.

---

## 📁 Directory

```text
📁 web/assets/fonts/noto-sans/
├─ 🧾 SOURCE.md                 # this file (provenance + update notes)
├─ 📜 LICENSE.txt / OFL.txt      # SIL Open Font License 1.1 (must be present)
└─ 🔤 *.woff2 / *.woff / *.ttf   # font binaries (exact set depends on build choice)
```

---

## 🧾 Upstream Source

- **Font family:** Noto Sans  
- **Publisher / project:** Google’s Noto font project  
- **Primary distribution:** Google Fonts  
- **Upstream references (preferred):**
  - Google Fonts family page (for webfont builds)
  - Noto fonts source repository (for upstream source + metadata)

> ✅ **Rule:** If font files in this folder are replaced/updated, also update the metadata below.

---

## 🧷 Local Asset Metadata

Fill in / keep current whenever the files change:

```yaml
asset_id: noto-sans
family: "Noto Sans"
intended_use: "UI typography (web)"
source: "Google Fonts / Noto project"
license: "SIL Open Font License 1.1 (OFL-1.1)"
downloaded_or_updated_at: "UNKNOWN"   # YYYY-MM-DD
upstream_version_or_commit: "UNKNOWN" # tag/commit/hash if known
formats_in_repo:
  - woff2
subsets:
  - "UNKNOWN" # e.g., latin, latin-ext (if subsetted)
notes:
  - "Do not remove license file."
```

---

## ⚖️ License & Attribution

- **License:** SIL Open Font License, Version 1.1 (**OFL-1.1**)  
- **What that means (practical summary):**
  - ✅ You may use, embed, and redistribute the fonts (including in commercial projects).
  - ✅ You may modify the fonts, but **do not** claim the originals are yours.
  - ✅ Keep the license text with any redistribution of the font files.
  - ⚠️ If you ship modified fonts, follow OFL requirements (including naming / Reserved Font Names if applicable).

📌 **Required in this folder:** `LICENSE.txt` (or `OFL.txt`) containing the OFL-1.1 text from the upstream package.

---

## 🛠️ How These Fonts Should Be Updated

### Option A — Recommended (Modern): Variable `.woff2`
1. Download the Noto Sans webfont package from Google Fonts.
2. Prefer a **variable** `.woff2` if available (smaller + flexible weights).
3. Replace the existing `.woff2` files in this folder.
4. Ensure `LICENSE.txt`/`OFL.txt` is present and matches the upstream package.
5. Update the **Local Asset Metadata** block in this file.
6. (Optional but recommended) record hashes (see below).

### Option B — Static weights (Fallback / Compatibility)
1. Download static weight styles you actually use (avoid shipping unused weights).
2. Keep a minimal set (example):
   - Regular
   - Italic
   - Bold
   - Bold Italic
3. Replace files + update metadata + keep license.

---

## ✅ Optional: Integrity / Reproducibility Checklist

- [ ] `LICENSE.txt` / `OFL.txt` is present in this directory
- [ ] Local metadata block updated (`downloaded_or_updated_at`, `upstream_version_or_commit`)
- [ ] Only the weights/styles actually used by the UI are shipped
- [ ] `woff2` preferred for web performance
- [ ] (Optional) checksums recorded

### 🔐 Recording checksums (recommended)
Run from repo root:

```bash
sha256sum web/assets/fonts/noto-sans/* > web/assets/fonts/noto-sans/SHA256SUMS.txt
```

---

## 🎛️ Optional: CSS Usage Snippet

<details>
  <summary><strong>Example @font-face (adjust filenames to match this folder)</strong></summary>

```css
@font-face {
  font-family: "Noto Sans";
  src: url("/assets/fonts/noto-sans/NotoSans.woff2") format("woff2");
  font-weight: 100 900; /* variable font range if applicable */
  font-style: normal;
  font-display: swap;
}
```

</details>

---

## 🧩 Notes for Contributors

- If you ever change **filenames**, also update any CSS/JS imports referencing them.
- If you subset fonts (e.g., `latin` only), document:
  - the subset tool used,
  - the glyph ranges,
  - and the command used to reproduce the output.
- Keep this folder “boring”: **minimal files, clear provenance, predictable naming**. 🧼