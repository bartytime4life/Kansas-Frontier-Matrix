# 🏷️ Logos — Source Assets (KFM)

> 📁 **Path:** `web/assets/media/_sources/icons/logos/`  
> 🧭 **Role:** Canonical, editable logo sources (first‑party + third‑party) used across the KFM web UI, docs, and attribution surfaces.  
> ✅ **Status:** 🧾 licensed · 🔎 traceable · 🧱 contract-minded · ♻️ optimization-ready

---

## 🎯 What this folder is for

This directory is the **source-of-truth** home for **brand marks** (“logos”): wordmarks, logomarks, lockups, partner/provider marks, and any other **identity graphics** used in the Kansas Frontier Matrix (KFM) experience.

We treat logos as **governed media assets**:
- **Provenance-first**: every logo must have a clear origin + usage rights.
- **Contract-first** (lightweight): every logo should have a small metadata sidecar so the UI and docs can reliably reference it.
- **Web-ready**: vector-first, optimized exports, predictable naming.

---

## ✅ What belongs here vs. elsewhere

### ✅ Put here
- 🟦 **KFM first‑party marks**: logomark, wordmark, lockups, monochrome variants.
- 🤝 **Third‑party marks** we’re allowed to display (partners, data providers, platforms).
- 🧩 **SVG masters** (preferred) and optional original design sources (e.g., `.ai`, `.fig`, `.pdf`) *if licensing allows*.
- 🧾 **Metadata sidecars** for each logo (recommended, see below).

### 🚫 Don’t put here
- 🧷 UI icons / pictograms (use the `icons/` system folder, not `logos/`)
- 🖼️ Photos, screenshots, illustrations (those are *media*, not *logos*)
- 🏗️ Generated build artifacts (minified bundles, hashed filenames, build outputs)

---

## 🗂️ Suggested layout

Keep the layout predictable so code and docs can reference assets without guesswork.

```text
web/assets/media/_sources/icons/logos/
├─ 📄 README.md
├─ 📁 kfm/                       # ✅ First‑party KFM marks
│  ├─ 🖼️ kfm--mark.svg
│  ├─ 🖼️ kfm--wordmark.svg
│  ├─ 🖼️ kfm--lockup-horizontal.svg
│  ├─ 🖼️ kfm--lockup-stacked.svg
│  ├─ 🖼️ kfm--mono.svg
│  └─ 🧾 kfm.meta.json
└─ 📁 third-party/               # ⚠️ Trademarked / externally governed marks
   ├─ 📁 <vendor_or_org_slug>/
   │  ├─ 🖼️ <slug>--mark.svg
   │  ├─ 🖼️ <slug>--wordmark.svg
   │  ├─ 🖼️ <slug>--lockup-horizontal.svg
   │  └─ 🧾 <slug>.meta.json
   └─ 📄 THIRD_PARTY_NOTES.md     # optional, if needed
```

> 💡 If your repo already uses a different structure, keep the spirit: **one logo family per folder**, **vector-first**, **metadata next to the asset**.

---

## 🏷️ Naming conventions

**Goal:** deterministic, grep-friendly names that encode intent.

Use this pattern:

```text
<owner>--<variant>[--<theme>].<ext>
```

**Examples**
- `kfm--mark.svg`
- `kfm--wordmark.svg`
- `kfm--lockup-horizontal.svg`
- `kfm--lockup-stacked.svg`
- `kfm--mono.svg`
- `providerx--mark--dark.svg` (only if truly needed)

### 🧠 Variants we recognize
| Variant | Meaning | Notes |
|---|---|---|
| `mark` | symbol/logomark | no text |
| `wordmark` | text-only logo | typography-based |
| `lockup-horizontal` | mark + wordmark | horizontal composition |
| `lockup-stacked` | mark + wordmark | stacked composition |
| `mono` | single-color | best for theming |
| `badge` | contained mark | only if used in UI components |

---

## 🧾 Metadata sidecar (recommended)

To keep logos *governable* and *traceable*, add a sidecar file next to each logo family:

- `kfm.meta.json`
- `third-party/<slug>/<slug>.meta.json`

### ✅ Why we do this
- Prevent “mystery assets” ✅
- Allow automated **attribution/credits** where required ✅
- Make it safe to ship partner marks without legal ambiguity ✅
- Enable UI + docs to reference a stable ID rather than “whatever filename exists” ✅

<details>
<summary><strong>📦 Suggested <code>.meta.json</code> schema (copy/paste)</strong></summary>

```json
{
  "id": "kfm",
  "kind": "logo",
  "owner": "Kansas Frontier Matrix",
  "variants": [
    { "name": "mark", "file": "kfm--mark.svg" },
    { "name": "wordmark", "file": "kfm--wordmark.svg" },
    { "name": "lockup-horizontal", "file": "kfm--lockup-horizontal.svg" },
    { "name": "lockup-stacked", "file": "kfm--lockup-stacked.svg" },
    { "name": "mono", "file": "kfm--mono.svg" }
  ],
  "license": {
    "type": "proprietary",
    "spdx": null,
    "notes": "First-party KFM identity asset."
  },
  "provenance": {
    "source": "internal",
    "source_url": "https://example.com/source-or-design-system", 
    "retrieved_utc": "2026-01-18T00:00:00Z",
    "maintainer": "KFM Maintainers"
  },
  "usage": {
    "allowed_contexts": ["web-ui", "docs", "attribution"],
    "restrictions": [
      "Do not distort, recolor (except mono), or add effects.",
      "Respect clearspace; avoid crowding with other marks."
    ]
  },
  "accessibility": {
    "default_alt": "Kansas Frontier Matrix",
    "decorative_ok": true
  }
}
```

> 📝 Notes:
> - `source_url` is optional for internal marks; **required** for third-party where possible.
> - For third-party marks, set `license.type` to the most accurate label you have (e.g., “trademark”, “brand-asset-policy”, “custom-permission”).
```

</details>

---

## 🧠 File format guidance (keep it crisp)

### ✅ Preferred: SVG
SVG is the default for logos because it stays sharp at any size and is typically smaller when optimized.

**SVG rules**
- ✅ Keep `viewBox`
- ✅ Convert text to outlines (or embed safely) to avoid font substitution surprises
- ✅ Strip editor metadata unless you need it
- ✅ Avoid embedded raster images inside SVG unless unavoidable
- ✅ Keep fills/strokes intentional; don’t “bake in” background rectangles unless necessary

### 🟨 Allowed: PNG (fallback only)
Use PNG only when:
- a vendor provides no usable vector, or
- the mark uses effects that don’t translate cleanly to SVG.

**PNG rules**
- Provide `@2x` where needed (retina)
- Keep dimensions consistent and documented in metadata
- Optimize before committing

---

## 🧰 Optimization workflow (source → ship)

This folder is `_sources/` on purpose: keep assets **editable**, then create optimized deliverables for runtime use.

A practical workflow:
1. ✏️ Add/edit source SVG(s)
2. 🧼 Optimize SVG (e.g., with `svgo`)
3. 🧪 Verify rendering on light/dark backgrounds
4. 🧾 Ensure metadata exists and is accurate
5. ✅ Use the optimized file in UI/docs

Example commands (adjust to your toolchain):

```bash
# Optimize an SVG in-place (example)
npx svgo -i kfm--mark.svg -o kfm--mark.svg

# If you must ship PNGs, optimize them too (example)
# pngquant --force --ext .png --quality=70-90 your-logo.png
```

---

## ♿ Accessibility rules

Logos are “content” when they communicate identity.

- If the logo is **informational** (brand identity): provide meaningful `alt` text (e.g., “Kansas Frontier Matrix”).
- If the logo is purely **decorative**: use empty alt (`alt=""`) and ensure surrounding context still makes sense.

> ✅ If you’re unsure, default to informative alt text and let design review decide.

---

## 🧩 Using logos in the web UI

**Recommendation:** prefer **external SVG files** (cached like normal images) unless you need to style internal paths.

Typical patterns:

```tsx
// Example (bundler-dependent): import URL for asset
import logoUrl from "./kfm--lockup-horizontal.svg";

export function HeaderLogo() {
  return <img src={logoUrl} alt="Kansas Frontier Matrix" height={28} />;
}
```

If you need mono theming via CSS, consider a mono SVG and apply color via CSS if authored to support it.

---

## ⚠️ Third‑party logos: trademark + permission notes

Third‑party marks are often trademarks and/or governed by brand usage policies.

**Before committing a third-party logo:**
- ✅ Confirm we’re allowed to store + display it
- ✅ Record the source and any usage constraints in `<slug>.meta.json`
- ✅ Prefer official brand assets (not random web pulls)

> 🧾 If the usage rights are unclear: **do not add the logo yet**—open an issue and track permission first.

---

## ✅ Contribution checklist (PR-ready)

- [ ] Logo file name follows convention (`<owner>--<variant>.svg`)
- [ ] SVG is optimized (no unnecessary editor metadata)
- [ ] Metadata sidecar exists and includes license + provenance
- [ ] Third-party marks include restriction notes (if any)
- [ ] Visual check passed on light + dark backgrounds
- [ ] Intended usage documented (UI component, docs, attribution, etc.)

---

## 🧭 Quick FAQ

**Q: Why is this in `_sources/`?**  
A: Because we want a clean separation between *editable sources* and *runtime-deliverable* assets.

**Q: Can I just drop a logo PNG I found online?**  
A: Not unless the rights are clear and it’s documented. Prefer official brand assets and record provenance.

**Q: Where do UI icons go?**  
A: In the icon system folders, not here—logos are identity marks, icons are interface symbols.

---
