<div align="center">

# 🅰️ Font Family: `{{family_slug}}` — `{{version}}`

**KFM Web UI font source package** (versioned + provenance-first) ✨

![Status](https://img.shields.io/badge/status-source%20package-blue)
![Scope](https://img.shields.io/badge/scope-web%2Fassets%2Fmedia-lightgrey)
![Version](https://img.shields.io/badge/version-{{version}}-informational)
![License](https://img.shields.io/badge/license-SEE%20LICENSE-lightgrey)

</div>

> 🎯 **Purpose:** This folder is the *version-pinned* home for the `{{family_slug}}` font files used by the KFM `web/` UI.  
> 🧬 **Rule:** No “mystery fonts” — every file here must be traceable to an upstream source + license, and older versions should remain immutable for reproducibility.

---

## 🧾 Quick Facts

| Field | Value |
|---|---|
| 📦 Family slug (folder name) | `{{family_slug}}` |
| 🏷️ Version (folder name) | `{{version}}` |
| 🎨 CSS `font-family` name | `{{css_family_name}}` |
| ⚖️ License (SPDX or human-readable) | `{{license_id}}` |
| 🔗 Upstream source | `{{upstream_name}}` — `{{upstream_url}}` |
| 📅 Retrieved | `YYYY-MM-DD` |
| ✂️ Subset | `{{subset_or_full}}` (e.g., `latin`, `latin-ext`, `full`) |

---

## 📁 What Lives Here

This directory should contain **only** the files required to ship this font family + version.

```text
web/assets/media/_sources/fonts/{{family_slug}}/{{version}}/
├─ 📄 README.md                      # you are here
├─ 📄 LICENSE*                       # license text(s) for this exact package
├─ 📄 SOURCE.md  (recommended)        # provenance notes (where we got it, how)
├─ 📄 CHECKSUMS.txt (recommended)     # sha256/sha512 for supply-chain sanity
├─ 🗂️ files/ or direct files:
│  ├─ 🔤 {{file_1}}.woff2
│  ├─ 🔤 {{file_1}}.woff
│  ├─ 🔤 {{file_2}}.woff2
│  └─ 🔤 {{file_2}}.woff
└─ 📄 font.asset.json (optional)      # machine-readable “font contract”
```

### ✅ Minimum required files
- `README.md` (this)
- `LICENSE*` (must exist and match upstream terms)
- At least **WOFF2** (preferred) and/or **WOFF** files for the variants you use

---

## 🔍 Provenance & License

### ✅ Required (human-readable)
Fill these in (or add `SOURCE.md` if it’s too long):

- **Upstream**: `{{upstream_url}}`  
- **Upstream version / tag**: `{{upstream_tag}}`  
- **Retrieved on**: `YYYY-MM-DD`  
- **License**: `{{license_id}}`  
- **Redistribution allowed?** `yes/no/unknown`  
- **Modifications**: `none` / `subset` / `renamed files` / `converted formats` (be explicit)

> ⚠️ If redistribution is **not** allowed, do **not** commit the font binaries here. Instead: store acquisition instructions, add a CI-safe fetch step, and keep any restricted artifacts out of Git.

---

## 🎛️ Font Variants Included

List every variant this version provides (and what the UI is actually allowed to use).

| Variant | Weight | Style | Files |
|---|---:|---|---|
| `{{variant_name_1}}` | `400` | `normal` | `{{file_1}}.woff2`, `{{file_1}}.woff` |
| `{{variant_name_2}}` | `700` | `italic` | `{{file_2}}.woff2`, `{{file_2}}.woff` |

---

## 🎨 Using This Font in CSS (`@font-face`)

> 🧭 **Path note:** Be careful with relative paths — they depend on where your CSS lives (and/or your bundler). Keep the URLs correct for how the site serves static assets.

### Recommended modern setup (WOFF2 + WOFF)

```css
/* Example: web/styles/fonts/{{family_slug}}.css */

@font-face {
  font-family: "{{css_family_name}}";
  src:
    url("/assets/media/fonts/{{family_slug}}/{{version}}/{{file_1}}.woff2") format("woff2"),
    url("/assets/media/fonts/{{family_slug}}/{{version}}/{{file_1}}.woff") format("woff");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

### Usage in your UI styles

```css
:root {
  --font-ui: "{{css_family_name}}", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
}

body {
  font-family: var(--font-ui);
}
```

<details>
<summary>🧓 Legacy browsers / extra formats (optional)</summary>

If your support matrix includes older browsers, you may need additional formats beyond WOFF/WOFF2.

```css
@font-face {
  font-family: "{{css_family_name}}";
  src: url("{{file_1}}.eot");
  src:
    url("{{file_1}}.eot?#iefix") format("embedded-opentype"),
    url("{{file_1}}.woff2") format("woff2"),
    url("{{file_1}}.woff") format("woff"),
    url("{{file_1}}.ttf") format("truetype"),
    url("{{file_1}}.svg#{{svg_id}}") format("svg");
  font-weight: 400;
  font-style: normal;
}
```

</details>

---

## 🚀 Performance Notes

- ✂️ **Subset if possible.** If you only need a language subset (e.g., `latin`), ship that instead of the full glyph set to reduce filesize.
- 🧊 Prefer **WOFF2** for smallest payload; keep **WOFF** as a fallback when needed.
- 🧠 Avoid loading unused weights/styles — declare only what you use.

---

## 🔄 Updating / Adding a New Version

1. 📁 Create a new folder: `web/assets/media/_sources/fonts/{{family_slug}}/{{new_version}}/`
2. 📦 Add font files for the new version (don’t overwrite the old version).
3. ⚖️ Copy/update `LICENSE*` and provenance fields (source URL, tag, retrieval date).
4. 🧾 Update `CHECKSUMS.txt` (recommended).
5. 🎨 Update the CSS registration (wherever `@font-face` is declared) to point to the new version.
6. ✅ Validate in browser: no 404s, correct weight selection, and layout stability is acceptable.

---

## 🧪 PR Checklist

- [ ] `LICENSE*` included and matches upstream license terms  
- [ ] Source URL + upstream version/tag recorded  
- [ ] Font files are versioned (no overwriting older versions)  
- [ ] CSS `@font-face` uses correct paths (no broken URLs)  
- [ ] Only required variants included (no bloat)  
- [ ] `font-display` set appropriately (recommend `swap`)  
- [ ] Attribution updated (if required by license)

---

## 🧷 Attribution Snippet

> Copy into a central attribution file if your license requires it.

```text
Font: {{css_family_name}} ({{version}})
Source: {{upstream_url}}
License: {{license_id}} (see LICENSE*)
```

---

## 🧬 Optional: “Font Contract” (Machine-Readable)

If you want this to behave like other governed artifacts in KFM, add a `font.asset.json` beside this README:

```json
{
  "kind": "font",
  "family": {
    "slug": "{{family_slug}}",
    "cssName": "{{css_family_name}}"
  },
  "version": "{{version}}",
  "source": {
    "name": "{{upstream_name}}",
    "url": "{{upstream_url}}",
    "tag": "{{upstream_tag}}",
    "retrievedAt": "YYYY-MM-DD"
  },
  "license": {
    "id": "{{license_id}}",
    "files": ["LICENSE.txt"],
    "redistribution": "unknown"
  },
  "variants": [
    { "weight": 400, "style": "normal", "files": ["{{file_1}}.woff2", "{{file_1}}.woff"] }
  ],
  "notes": "Fill in any subsetting or conversion details here."
}
```

---

### 🧭 Related (Repo-Local)

- `web/` — Frontend UI (React/Map UI, CSS, static assets)
- `docs/MASTER_GUIDE_v13.md` — Governance + contract-first patterns (if present)
- `docs/governance/` — Ethics/licensing guidance (if present)
