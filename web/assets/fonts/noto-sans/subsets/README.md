# 🗂️ Noto Sans — WOFF2 Subsets

![Font](https://img.shields.io/badge/font-Noto%20Sans-111827?style=for-the-badge)
![Format](https://img.shields.io/badge/format-WOFF2-111827?style=for-the-badge)
![Goal](https://img.shields.io/badge/goal-fast%20loads%20%26%20broad%20glyph%20coverage-111827?style=for-the-badge)

This folder contains **WOFF2** font *subsets* for **Noto Sans**, optimized for web delivery (smaller downloads, faster first paint) ✅

> 💡 **Why subsets?** Most pages only need a small fraction of the glyphs included in a full “everything” font.  
> With `unicode-range`, browsers will fetch **only** the subset(s) required for the characters actually used.

---

## 📍 Location

`web/assets/fonts/noto-sans/subsets/`

---

## 🧱 Expected directory layout

```text
📁 web/
  📁 assets/
    📁 fonts/
      📁 noto-sans/
        📁 subsets/
          📄 NotoSans-Latin.woff2
          📄 NotoSans-LatinExt.woff2
          📄 README.md  ← (this file)
```

> 📝 If you also ship multiple weights/styles, keep the naming consistent:
> - `NotoSans-Latin-400.woff2`
> - `NotoSans-LatinExt-400.woff2`
> - `NotoSans-Italic-Latin-400.woff2`
> - etc.

---

## 🧩 Subsets included

| Subset | File | Intended coverage | Typical use |
|---|---|---|---|
| **Latin** | `NotoSans-Latin.woff2` | Basic Latin + Latin-1 punctuation/symbols | UI chrome, most English content |
| **LatinExt** | `NotoSans-LatinExt.woff2` | Latin Extended blocks + diacritics | Place names, historical docs, names w/ accents (e.g., “Č”, “Ł”, “ñ”, “ō”) |

<details>
<summary>🔎 Suggested Unicode ranges (reference)</summary>

These are **common** ranges for a “LatinExt” subset. Your project may need more/less depending on data sources.

- **Latin (typical):**
  - `U+0000-00FF` (Basic Latin + Latin-1 Supplement)

- **LatinExt (typical):**
  - `U+0100-024F` (Latin Extended-A/B)
  - `U+1E00-1EFF` (Latin Extended Additional)
  - `U+0300-036F` (Combining Diacritical Marks — important for decomposed accents)
  - Optional (if your content needs it):
    - `U+0250-02AF` (IPA Extensions)
    - `U+2C60-2C7F` (Latin Extended-C)
    - `U+A720-A7FF` (Latin Extended-D)
    - `U+AB30-AB6F` (Latin Extended-E)

✅ **Best practice:** drive the subset from a corpus (`--text-file`) rather than guessing ranges.

</details>

---

## 🎨 How to use in CSS

### ✅ Recommended: `unicode-range` driven loading

> Browsers will download only the subset matching the characters on the page.

```css
/* Latin (default) */
@font-face {
  font-family: "Noto Sans";
  src: url("/assets/fonts/noto-sans/subsets/NotoSans-Latin.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
  unicode-range: U+0000-00FF;
}

/* Latin Extended (only loads if needed) */
@font-face {
  font-family: "Noto Sans";
  src: url("/assets/fonts/noto-sans/subsets/NotoSans-LatinExt.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
  unicode-range: U+0100-024F, U+1E00-1EFF, U+0300-036F;
}
```

> ⚠️ **Avoid overlap**: If the Latin subset includes extended ranges, the browser may never fetch `LatinExt`.

---

## 🛠️ How to build (generate) subsets

### Prereqs 🧰
- Python 3
- `fonttools` + `brotli` for WOFF2 output

```bash
python -m pip install --upgrade fonttools brotli
```

### Option A: Build from explicit Unicode ranges (fast / okay for early setup)

```bash
pyftsubset "web/assets/fonts/noto-sans/src/NotoSans-Regular.ttf" \
  --output-file="web/assets/fonts/noto-sans/subsets/NotoSans-LatinExt.woff2" \
  --flavor=woff2 \
  --layout-features='*' \
  --no-hinting \
  --name-IDs='*' --name-legacy --name-languages='*' \
  --legacy-cmap --symbol-cmap \
  --unicodes="U+0100-024F,U+1E00-1EFF,U+0300-036F"
```

### ⭐ Option B: Build from a real project corpus (best / provenance-friendly)

1) Create a text file containing **all characters used in the web app and data**  
   Example: `web/assets/fonts/noto-sans/subsets/corpus.txt`

2) Subset using `--text-file`:

```bash
pyftsubset "web/assets/fonts/noto-sans/src/NotoSans-Regular.ttf" \
  --output-file="web/assets/fonts/noto-sans/subsets/NotoSans-LatinExt.woff2" \
  --flavor=woff2 \
  --layout-features='*' \
  --no-hinting \
  --name-IDs='*' --name-legacy --name-languages='*' \
  --legacy-cmap --symbol-cmap \
  --text-file="web/assets/fonts/noto-sans/subsets/corpus.txt"
```

> 🧠 Tip: Treat `corpus.txt` like a **tracked artifact** (it’s the “why” behind which glyphs are shipped).  
> This aligns nicely with provenance-first workflows: the font subset becomes *reproducible* and *auditable*.

---

## ✅ Validation checklist

- [ ] The UI renders correctly in **English-only** pages (Latin subset loads).
- [ ] A page containing “Łódź / Český / São / Dvořák / naïve” loads **LatinExt** subset.
- [ ] No “tofu” boxes (□) appear for expected content.
- [ ] Font files are served with correct `Content-Type` (commonly `font/woff2`).
- [ ] Long-term caching enabled (ideally hashed filenames in production builds).

<details>
<summary>🔬 Quick local sanity checks</summary>

- Inspect tables:
  ```bash
  ttx -l web/assets/fonts/noto-sans/subsets/NotoSans-LatinExt.woff2
  ```

- Compare sizes:
  ```bash
  ls -lh web/assets/fonts/noto-sans/subsets/*.woff2
  ```

</details>

---

## 📜 License note

Noto fonts are typically distributed under the **SIL Open Font License (OFL)**.  
Ensure the upstream font license is included somewhere appropriate in the repo (commonly alongside the source font files). ✅

---

## ✨ Conventions

- ✅ Prefer **WOFF2** only (modern browsers).
- ✅ Prefer `font-display: swap;` for fast rendering.
- ✅ Prefer `unicode-range` so browsers fetch only what they need.
- ✅ Keep subset names stable + predictable (`Latin`, `LatinExt`, etc.).
- 🧾 Keep the build recipe **documented and reproducible** (commands + corpus).

---