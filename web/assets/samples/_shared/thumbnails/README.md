---
title: "🖼️ Shared Sample Thumbnails"
path: "web/assets/samples/_shared/thumbnails/README.md"
version: "v1.0.0"
status: "active"
last_updated: "2026-01-18"
doc_kind: "Asset README"
license: "See root LICENSE"
markdown_protocol_version: "1.0"
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_ref: "docs/governance/SOVEREIGNTY.md"
security_ref: "SECURITY.md"
---

# 🖼️ Shared Sample Thumbnails

![KFM](https://img.shields.io/badge/KFM-v13-blue)
![web](https://img.shields.io/badge/web-assets-informational)
![perf](https://img.shields.io/badge/perf-small%20%26%20optimized-success)

This folder contains **shared thumbnail images** used by the **web sample gallery / sample cards** inside the KFM UI (`web/`).  
These are intentionally centralized under `_shared/` so multiple samples can reference the same preview assets without duplication ✅

---

## 📁 Where this sits

```text
web/
└─ assets/
   └─ samples/
      └─ _shared/
         └─ thumbnails/
            ├─ README.md   👈 you are here
            └─ *.webp / *.png
```

> [!NOTE]
> `_shared/` means **cross-sample** assets. If a thumbnail is *truly sample-specific* (and not reused), consider keeping it closer to the sample definition (depending on how samples are structured in `web/assets/samples/`).

---

## 🎯 What thumbnails are for

Thumbnails are **fast-loading previews** meant to:
- 🧭 Help users visually scan sample options
- ⚡ Keep the samples index page snappy (small file sizes)
- 🧩 Provide consistent UI affordances (same aspect ratio & framing)

They are **not** a replacement for full screenshots, documentation figures, or marketing imagery.

---

## ✅ Asset rules

### 📐 Required spec

| Spec | Requirement | Why |
|---|---:|---|
| Aspect ratio | **16:9** (recommended) | Consistent card/grid rendering |
| Primary format | **`.webp`** | Smaller assets + good quality |
| Fallback (optional) | `.png` | For environments without WebP |
| Max file size | **≤ 200 KB** (target: 80–150 KB) | Keeps gallery fast |
| Content | Public-safe UI view | Avoids governance/security issues |

> [!TIP]
> If you’re unsure what aspect ratio the UI expects, search in `web/` for `thumbnail`, `preview`, or `card` and confirm the CSS container ratio before exporting.

---

## 🧾 Naming convention

Use **kebab-case** and match the sample identifier/slug used by the sample registry.

**Preferred pattern**
- `<sample_slug>.webp`
- (optional retina) `<sample_slug>@2x.webp`
- (optional fallback) `<sample_slug>.png`

**Examples**
- `treaty-boundaries.webp`
- `air-quality-heatmap.webp`
- `soil-profile@2x.webp`

**Avoid**
- spaces (`My Sample.webp`)
- uppercase (`Treaty.webp`)
- ambiguous names (`demo1.webp`)
- dates in filenames (use Git history instead)

> [!NOTE]
> Keep filenames stable. Renaming thumbnails can break references in UI sample manifests/config.

---

## 🛠️ Creating / updating a thumbnail

### 1) Capture a clean source image 📸
- Use a consistent viewport (ex: 1280×720 or 1920×1080)
- Prefer a “hero” state: clear layers, readable theme, minimal popovers
- Avoid transient UI (toasts, cursor, dev overlays)

### 2) Crop to the standard aspect ratio ✂️
- Crop to **16:9**
- Keep “visual focus” near center (map content, key overlay)

### 3) Export & compress 🗜️

<details>
<summary><strong>Option A — ImageMagick (common)</strong></summary>

```bash
# Example: create a 640×360 WebP thumbnail (center crop)
magick input.png \
  -resize 640x360^ \
  -gravity center \
  -extent 640x360 \
  -quality 82 \
  output.webp
```
</details>

<details>
<summary><strong>Option B — cwebp (WebP CLI)</strong></summary>

```bash
# Example: compress to WebP with a quality target
cwebp -q 80 input.png -o output.webp
```
</details>

<details>
<summary><strong>Option C — sharp (Node-based, great for batching)</strong></summary>

```js
// sharp example (pseudo-snippet)
// Resize + crop to 640×360, export WebP
// (Use a local script if we decide to standardize thumbnail generation in tools/)
```
</details>

### 4) Drop the final file into this folder 📦
Place your exported thumbnail in:

`web/assets/samples/_shared/thumbnails/`

### 5) Wire it up in the sample registry 🔗
Because sample registration can vary by implementation, use a quick repo search:

```bash
# From repo root
rg -n "thumbnail|previewImage|preview_image|thumb" web/assets/samples web
```

Then reference the thumbnail with the correct relative path, e.g.:

```text
/assets/samples/_shared/thumbnails/<sample_slug>.webp
```

---

## 🔒 Governance, safety, and “don’t leak data” rules

Thumbnails are **UI-facing outputs** and must respect KFM governance constraints.

> [!WARNING]
> Do **not** publish thumbnails that reveal:
> - personal data (PII), names, addresses, user-specific identifiers
> - sensitive locations or culturally restricted sites
> - any “restricted” layer states that would normally be guarded by API redaction rules

If a sample depends on restricted data, the thumbnail should be a **public-safe representation** (example: generalized view, placeholder layer, or synthetic demo data).

**Related policies**
- `docs/governance/ETHICS.md` ⚖️  
- `docs/governance/SOVEREIGNTY.md` 🪶  
- `SECURITY.md` 🔐  

---

## ✅ Thumbnail Definition of Done

- [ ] Filename follows kebab-case and matches sample slug
- [ ] Aspect ratio matches UI expectation (default **16:9**)
- [ ] File size is within target (≤ 200 KB)
- [ ] No sensitive/PII content visible
- [ ] Looks good at small sizes (scan test at ~240px wide)
- [ ] Sample registry/config updated (if required)
- [ ] No broken references in the sample gallery

---

## 🔗 Useful repo references

- `docs/MASTER_GUIDE_v13.md` — overall repo layout + subsystem ownership 🗺️  
- `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` — Markdown conventions (admonitions, front-matter, etc.) ✍️  
- `docs/governance/ROOT_GOVERNANCE.md` — governance triggers & review gates 🚦  

---
