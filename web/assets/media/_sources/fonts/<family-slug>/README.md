<!-- 🗂️ Path: web/assets/media/_sources/fonts/<family-slug>/README.md -->

# 🅰️ Font Family: **<Family Name>** (`<family-slug>`)

![KFM](https://img.shields.io/badge/KFM-web%20ui%20asset-1f425f)
![Type](https://img.shields.io/badge/type-font%20family-blue)
![Formats](https://img.shields.io/badge/formats-woff2%20%7C%20woff-success)
![Provenance](https://img.shields.io/badge/provenance-first-7D3C98)

> [!IMPORTANT]
> This folder is the **auditable source-of-truth** for this font family: **upstream source**, **license**, and **transformation notes**.  
> ✅ If it’s not clearly licensed for redistribution + web embedding, it **does not belong** in this repo.

---

## 📌 Purpose

This directory holds everything needed to keep typography **deterministic, reproducible, and legally clean**:

- 📥 **Upstream** font package(s) as received (`.zip`, `.ttf`, `.otf`, vendor kits)
- 🧾 **License** text(s) and attribution requirements
- 🧬 **Provenance** (where it came from, version, download date)
- ⚙️ **Optional**: locally hosted web outputs (`.woff2` / `.woff`) and minimal CSS snippets

> [!NOTE]
> `web/assets/media/_sources/` is for **inputs**. Your app should load fonts from the **published** asset location (typically a sibling “built/served” folder), not from `_sources`.

---

## 🧾 Provenance & License

Fill this in **completely** when adding/updating fonts.

| Field | Value |
|---|---|
| **Font family** | `<Family Name>` |
| **Slug** | `<family-slug>` |
| **Upstream URL** | `TODO: https://…` |
| **Upstream version / tag** | `TODO (e.g., v1.2.3 / commit / release date)` |
| **Downloaded on** | `TODO (YYYY-MM-DD)` |
| **License** | `TODO (e.g., OFL-1.1 / Apache-2.0 / Commercial)` |
| **Redistribution allowed?** | `TODO (Yes/No + notes)` |
| **Embedding allowed?** | `TODO (Web embedding terms)` |
| **Attribution required?** | `TODO (Yes/No + exact wording if required)` |
| **Modifications made** | `TODO (subset, rename, convert, etc.)` |
| **Maintainer** | `TODO (@handle)` |

📎 **License file required:** keep a `LICENSE.*` (and `NOTICE.*` if needed) next to this README.

---

## 📦 Expected contents

```text
<family-slug>/
├─ README.md
├─ LICENSE.*                  # REQUIRED (license terms)
├─ NOTICE.*                   # Optional (if upstream requires it)
├─ upstream/                  # Raw vendor downloads (keep as-received)
│  └─ <vendor-kit>.zip
├─ src/                       # Raw font files (.ttf/.otf) as received
│  ├─ <FamilyName>-Regular.ttf
│  └─ <FamilyName>-Italic.ttf
├─ work/                      # Optional: intermediate build artifacts (subsets, temp files)
├─ dist/                      # Optional: generated web fonts for publishing (.woff2/.woff)
│  ├─ <family-slug>-400-normal.woff2
│  ├─ <family-slug>-700-normal.woff2
│  └─ <family-slug>-400-italic.woff2
├─ css/                       # Optional: per-family @font-face snippets (small + focused)
│  └─ <family-slug>.css
└─ checksums.sha256           # Recommended: sha256 for src/ + dist/
```

> [!TIP]
> If you don’t have a build pipeline yet, still commit `upstream/`, `src/`, `LICENSE.*`, and this README. That alone gets us **auditability**.

---

## 🏷️ Naming conventions

### Folder slug
- Use **kebab-case**: `source-sans-3`, `noto-sans`, `inter`, `ibm-plex-sans`

### Output files (`dist/`)
Pick one convention and be consistent (recommended):

- **Static fonts:**  
  `"<family-slug>-<weight>-<style>.woff2"`  
  Example: `inter-400-normal.woff2`, `inter-700-normal.woff2`, `inter-400-italic.woff2`

- **Variable fonts:**  
  `"<family-slug>-var.woff2"` (+ optional italic)  
  Example: `inter-var.woff2`, `inter-var-italic.woff2`

---

## 🎛️ Styles & weights included

> Replace this table with what’s actually included.

| Weight | Style | File (served) | Notes |
|---:|---|---|---|
| 400 | normal | `dist/<family-slug>-400-normal.woff2` | body / UI |
| 500 | normal | `dist/<family-slug>-500-normal.woff2` | UI emphasis |
| 700 | normal | `dist/<family-slug>-700-normal.woff2` | headings |
| 400 | italic | `dist/<family-slug>-400-italic.woff2` | citations / emphasis |

---

## 🧑‍🎨 Usage in CSS

> [!IMPORTANT]
> These examples assume fonts are **served** from a public/static path (example: `/assets/media/fonts/...`).  
> Adjust paths to match your actual build output.

### Option A — Variable font (preferred if available)

```css
@font-face {
  font-family: "<Family Name>";
  src: url("/assets/media/fonts/<family-slug>/<family-slug>-var.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
```

### Option B — Static weights (+ optional fallback)

```css
@font-face {
  font-family: "<Family Name>";
  src:
    url("/assets/media/fonts/<family-slug>/<family-slug>-400-normal.woff2") format("woff2"),
    url("/assets/media/fonts/<family-slug>/<family-slug>-400-normal.woff") format("woff");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

### Suggested app-level font stack

```css
:root {
  --font-sans: "<Family Name>", system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}
```

---

## ⚡ Performance checklist ✅

- [ ] Prefer `.woff2` (keep `.woff` only if needed for compatibility).
- [ ] Consider **subsetting glyphs** to reduce size (when license allows).
- [ ] Use `font-display: swap` to reduce FOIT risk.
- [ ] Avoid loading many weights/styles “just in case” — ship what the UI uses.
- [ ] Preload only critical fonts (don’t carpet-bomb preloads).

---

## 🛠️ Build / Convert / Subset (suggested)

<details>
<summary>Example workflow (FontTools) ⚙️</summary>

```bash
# One-time install
python -m pip install fonttools brotli

# Example subset (adjust unicode ranges + features for your needs)
pyftsubset src/<FONT>.ttf \
  --output-file=work/<FONT>-subset.woff2 \
  --flavor=woff2 \
  --layout-features='*' \
  --unicodes='U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2212,U+FEFF,U+FFFD'

# Copy into dist/ with canonical naming
cp work/<FONT>-subset.woff2 dist/<family-slug>-400-normal.woff2
```

</details>

> [!WARNING]
> Subsetting/conversion changes binaries. If you modify anything:  
> ✅ keep upstream as-received, ✅ record changes in the provenance table, ✅ update checksums.

---

## 🔐 Checksums

Recommended `checksums.sha256` format:

```text
# sha256sum src/* dist/*
<sha256>  src/<file>
<sha256>  dist/<file>
```

---

## 🔄 Updating this font family

1. 📥 Add the new vendor package to `upstream/` (keep older packages if license allows).
2. 🧾 Update the **Provenance & License** table (version/date/source).
3. ⚙️ Rebuild `dist/` outputs (if applicable).
4. 🔐 Regenerate `checksums.sha256`.
5. 🧪 Validate rendering in the UI (body, headings, map labels, buttons).

---

## ✅ PR checklist (copy into your PR description)

- [ ] License included and compatible with repo distribution
- [ ] Provenance table fully filled in
- [ ] Files named consistently
- [ ] `dist/` fonts load correctly (no 404s)
- [ ] Reasonable file sizes (subset/variable considered)
- [ ] Checksums updated

---

## 📚 Project links (helpful)

- 📘 `docs/MASTER_GUIDE_v13.md` (repo conventions, evidence-first patterns)
- 🧭 UI/style system docs (add link here when available)
