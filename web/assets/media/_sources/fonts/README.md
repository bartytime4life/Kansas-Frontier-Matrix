<div align="center">

# 🔤 Font Sources (`web/assets/media/_sources/fonts/`)

Static **font sources** (downloads + licenses + provenance) for the **Kansas Frontier Matrix (KFM)** web UI.

![scope](https://img.shields.io/badge/scope-web%2Fassets%2Fmedia-blue)
![provenance](https://img.shields.io/badge/provenance-required-success)
![licenses](https://img.shields.io/badge/license-per--font-file-critical)
![preferred](https://img.shields.io/badge/preferred-woff2-informational)

</div>

---

## 🧭 Quick Nav
- [✅ What lives here](#-what-lives-here)
- [⛔ What does *not* live here](#-what-does-not-live-here)
- [🧱 Non-negotiables](#-non-negotiables)
- [🗂️ Folder layout](#️-folder-layout)
- [➕ Add or update a font](#-add-or-update-a-font)
- [🎨 Using fonts in CSS](#-using-fonts-in-css)
- [⚡ Performance notes](#-performance-notes)
- [🧾 Licensing & attribution](#-licensing--attribution)
- [❓ FAQ](#-faq)

---

## ✅ What lives here

This folder is a **source vault** 🏦 for fonts that we ship (or plan to ship) in the front-end.

**Keep:**
- 📦 The **original upstream download** (ZIP and/or original `.ttf` / `.otf`)
- 🧾 The **license text** *verbatim* (OFL, Apache, proprietary EULA, etc.)
- 🧬 Provenance metadata (where it came from, version, checksums, who added it, why)
- 🧰 Notes about conversions/subsets used to produce production-ready assets

> [!NOTE]
> Think of `_sources/` as the place we can always point to and say:  
> “This is exactly where this font came from, under what terms, and how we produced the web-ready files.” 🧠✨

---

## ⛔ What does *not* live here

🚫 **Do not** place these in `_sources/fonts`:
- CDN references / “hotlinked” font URLs  
- Mystery font files (no source, no license, no version)
- Production build outputs that the app imports directly (these belong in the **served** assets location, not the source vault)

---

## 🧱 Non-negotiables

> [!IMPORTANT]
> **If a font doesn’t have licensing + provenance, it doesn’t ship.** 🛑

For every font family added here:
1. ✅ Include a license file (`LICENSE*`, `OFL.txt`, `COPYING`, `EULA.txt`, etc.)
2. ✅ Include provenance metadata (template below)
3. ✅ Keep the original upstream artifacts (ZIP preferred)
4. ✅ If you subset or transform files, document **what changed** and **why**

---

## 🗂️ Folder layout

Suggested structure (versioned + auditable) 🧩:

```text
📁 web/
└─ 📁 assets/
   └─ 📁 media/
      ├─ 📁 _sources/
      │  └─ 📁 fonts/
      │     ├─ 📄 README.md  👈 you are here
      │     └─ 📁 <family-slug>/                # e.g. inter/, source-serif-4/
      │        └─ 📁 <version>/                 # e.g. 3.19/, 4.005/
      │           ├─ 📦 upstream.zip            # original download (preferred)
      │           ├─ 📁 original/               # extracted originals (ttf/otf)
      │           ├─ 📄 LICENSE.txt             # verbatim license
      │           ├─ 📄 SOURCE.yml              # provenance + checksums
      │           ├─ 📄 SUBSET.md               # only if subsetting was done
      │           └─ 📁 derived/                # optional: woff2 outputs *for review*
      │              ├─ 🔤 <file>.woff2
      │              └─ 🔤 <file>.woff
      └─ 📁 fonts/                              # ✅ served, production-ready fonts (recommended)
         └─ 📁 <family-slug>/
            └─ 🔤 <file>.woff2
```

> [!TIP]
> If your bundler/build pipeline expects a different served output location, keep the same principle:
> **_sources = upstream truth** ✅, **served assets = optimized outputs** 🚀.

---

## ➕ Add or update a font

### 1) Create a family + version folder
Example:
- `web/assets/media/_sources/fonts/inter/3.19/`

### 2) Drop in the upstream artifacts
- ✅ `upstream.zip` (preferred)
- ✅ `original/` extracted files if helpful

### 3) Add the license (verbatim)
- ✅ `LICENSE.txt` (or whatever the upstream provides)

### 4) Create `SOURCE.yml` 🧬
Use this template:

```yaml
# SOURCE.yml ✅ provenance + reproducibility
family: "Inter"
family_slug: "inter"
version: "3.19"

upstream:
  name: "Inter"
  url: "REPLACE_WITH_UPSTREAM_DOWNLOAD_URL"
  retrieved_utc: "YYYY-MM-DDTHH:MM:SSZ"
  notes: "Any context on where/why we chose this font."

license:
  summary: "REPLACE (e.g., SIL Open Font License 1.1)"
  redistribution_allowed: true   # set false for restricted fonts
  attribution_required: true     # if applicable
  license_files:
    - "LICENSE.txt"

files:
  - path: "upstream.zip"
    sha256: "REPLACE_WITH_SHA256"
  - path: "original/Inter-Regular.ttf"
    sha256: "REPLACE_WITH_SHA256"

build:
  produced_woff2: false
  subset: false
  subset_notes: ""
```

> [!TIP]
> If you do any transformations (subset, hinting changes, conversion), keep that recorded here (or in `SUBSET.md`). 📌

### 5) (Optional) Produce web formats
If the project serves fonts directly, prefer modern web formats:
- ✅ `.woff2` first
- 🟡 `.woff` only if you need broader fallback

If subsetting is possible, do it to reduce size 🎯:
- Example: Latin-only vs “everything”

---

## 🎨 Using fonts in CSS

Most modern setups use `@font-face` and point to the **served** font files (not the source vault). Example:

```css
/* Example only — adjust paths to match the served asset location */
@font-face {
  font-family: "Inter";
  src: url("/assets/media/fonts/inter/Inter-Regular.woff2") format("woff2"),
       url("/assets/media/fonts/inter/Inter-Regular.woff") format("woff");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

:root {
  --font-sans: "Inter", system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
}
```

<details>
<summary><strong>🧠 Why multiple formats?</strong></summary>

Different browsers historically preferred different formats (e.g., `.eot`, `.ttf`, `.svg`, `.woff`, `.woff2`).  
Modern practice is usually **WOFF2-first**, with **WOFF fallback** if needed.

</details>

---

## ⚡ Performance notes

- 🪶 Prefer **subset fonts** when possible (language/glyph-limited builds)
- 📉 Fewer weights/styles = fewer downloads
- 🧠 Consider **variable fonts** when they replace multiple static weights
- 🧊 Set cache headers for served fonts (long-lived + hashed filenames if feasible)
- 🚫 Avoid third-party font CDNs for privacy + reliability (self-host is predictable)

---

## 🧾 Licensing & attribution

> [!CAUTION]
> Fonts are software. Licenses matter. Some allow redistribution, some don’t.  
> **Do not commit restricted fonts** unless the repo’s distribution model + license explicitly allow it.

**Rules of thumb:**
- ✅ Keep license text verbatim in the same version folder
- ✅ If attribution is required, note it in `SOURCE.yml`
- ✅ When updating a font, treat it like a versioned dependency: new folder, new checksums

---

## ❓ FAQ

### Why do we keep fonts in `_sources/`?
Because it’s the audit trail 🧾: the original download + license + provenance.

### Can we reference fonts directly from `_sources/` in production?
Prefer **no**. `_sources/` is for traceability; production should load from an optimized served path (e.g., `web/assets/media/fonts/`).

### Can we add Google Fonts?
Yes, but **self-host** and store the upstream package + license here first.

### What if a font is “paid” or restricted?
Then we typically **cannot** store it in a public repo. Keep only metadata (and instructions) unless redistribution is explicitly permitted.

---

<div align="center">

✨ If it’s not traceable, it’s not shippable. ✨  
🔍 Provenance + 🧾 licensing + ⚡ performance = 💚 KFM-grade assets.

</div>
