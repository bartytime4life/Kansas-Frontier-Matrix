# 🧩 Map Glyphs — `{fontstack}`

<p align="center">
  <img alt="MapLibre" src="https://img.shields.io/badge/MapLibre-Glyphs-2b2b2b?logo=maplibre&logoColor=white" />
  <img alt="Format" src="https://img.shields.io/badge/Format-PBF%20(SDF)-2b2b2b" />
  <img alt="Asset type" src="https://img.shields.io/badge/Asset-Static%20Runtime-2b2b2b" />
  <img alt="Governance" src="https://img.shields.io/badge/Workflow-Contract--First-2b2b2b" />
</p>

> **📍 You are here:** `web/src/assets/map/glyphs/{fontstack}/`  
> **🎯 Purpose:** Serve **SDF glyph ranges** (`*.pbf`) for MapLibre/Mapbox-style **text labels** (symbol layers).  
> **🧠 Key idea:** the map client requests *only the glyph ranges it needs* while rendering labels.

---

## ✅ What belongs in this folder

This directory is a **single font stack** (MapLibre/Mapbox “fontstack”) worth of glyph ranges.

Typical layout:

```text
📂 web/src/assets/map/glyphs/{fontstack}/
  ├─ 📄 0-255.pbf
  ├─ 📄 256-511.pbf
  ├─ 📄 512-767.pbf
  ├─ 📄 ...
  └─ 📘 README.md   👈 you are reading this
```

### 🔤 What `{range}.pbf` means

- Glyph files are chunked into **256-codepoint ranges**.
- Each file name is the **inclusive range** it contains, like:
  - `0-255.pbf`
  - `256-511.pbf`
  - `512-767.pbf`
- The renderer loads whichever ranges are required by features currently in view.

---

## 🔗 How MapLibre finds these glyphs

Your **style JSON** must include a `glyphs` URL template containing:
- `{fontstack}`
- `{range}`

Example (recommended pattern: compute an absolute base URL at runtime):

```jsonc
{
  "glyphs": "https://YOUR_DOMAIN/assets/map/glyphs/{fontstack}/{range}.pbf"
}
```

And your symbol layers reference a font stack using `text-font`:

```jsonc
{
  "id": "place-labels",
  "type": "symbol",
  "layout": {
    "text-field": ["get", "name"],
    "text-font": ["{fontstack}"],
    "text-size": 12
  }
}
```

> ⚠️ **Contract:** The string inside `text-font` must match this folder name **exactly** (after URL encoding rules, e.g., spaces become `%20` in HTTP requests).

---

## 🧠 Folder contract (non-negotiables)

### 1) 🧾 Folder name must match the style’s `text-font`
- If your style uses `"{fontstack}" = "Open Sans Regular"`, then the folder should be:
  - `web/src/assets/map/glyphs/Open Sans Regular/`
- The request URL will likely contain `%20` for spaces; your static server must correctly map that.

### 2) 🧱 Files must be served *as static binary* (stable paths)
These files cannot be “imported” like typical bundler assets.

**Your build must ensure:**
- Output keeps a stable path like:
  - `/assets/map/glyphs/{fontstack}/{range}.pbf`
- Files are served with a binary-safe content type and allow range requests/caching.

> 💡 If your bundler fingerprints assets (hashing filenames), MapLibre won’t be able to resolve them via `{range}.pbf`. Ensure this directory is copied verbatim to the final build output.

### 3) ✋ Do not hand-edit `.pbf`
Glyph PBFs are **generated artifacts**. If anything is wrong:
- fix the font input(s),
- regenerate glyph ranges,
- replace the `.pbf` files.

---

## 🧭 Provenance & governance checklist

KFM treats “assets that affect interpretation” as **evidence-adjacent**. Fonts change what is readable, how names appear, and whether language-specific characters render correctly.

Fill this in and keep it current ✅

| Field | Value |
|---|---|
| Font stack name | `{fontstack}` |
| Upstream font family | `TODO` |
| Upstream font file(s) (`.ttf/.otf`) | `TODO` |
| Upstream version / release tag | `TODO` |
| License (SPDX if possible) | `TODO` |
| Proof of license / source URL | `TODO` |
| Generator tool | `TODO` |
| Generation command / script | `TODO` |
| Generation date (YYYY-MM-DD) | `TODO` |
| Unicode coverage (high-level) | `TODO (e.g., Latin-1 + Latin Extended-A/B)` |
| Integrity hash (folder or build artifact) | `TODO (sha256)` |

> 🧷 If this font stack is used for Indigenous place names / languages, be extra strict about correctness, supported diacritics, and the permissions/authority to distribute the font and derived glyphs.

---

## 🚀 Performance guidance (keep maps snappy)

A glyph pipeline can quietly become a perf bottleneck because it’s:
- many small files,
- requested on demand,
- often “invisible” until labels appear.

Best practices:
- ✅ Prefer **fewer font stacks** (fewer folders = fewer potential downloads).
- ✅ Prefer **fewer weights** (Regular + Bold beats 8 weights).
- ✅ Ensure strong caching:
  - long-lived caching in production
  - versioned deploy paths if needed
- ✅ Keep glyph hosting close to tile hosting (same origin if possible) to reduce CORS issues and latency.
- ✅ Watch for missing glyph ranges in Network tab (404s = broken labels).

---

## 🧯 Troubleshooting

### 🟨 Symptom: no labels at all
**Likely causes**
- `glyphs` URL template is wrong
- fontstack folder mismatch
- server not serving `.pbf` from the expected path
- CORS blocked if glyphs are hosted elsewhere

**What to check**
- Browser DevTools → **Network**:
  - do you see requests like `{fontstack}/0-255.pbf`?
  - are they **200** or **404/403**?
- Confirm `text-font` values exactly match folder naming.

---

### ⬜ Symptom: “tofu” squares (□) or missing characters
**Likely causes**
- the glyph range exists, but the font has no glyph for that codepoint
- the wrong font stack is being used in the layer
- fallback font stacks are missing

**Fix**
- add/adjust fallback stacks in `text-font`
- regenerate glyphs from a font that includes the needed characters

---

## 🛠️ Adding or updating a font stack (safe procedure)

1) ✅ Confirm you have the legal right to distribute:
   - the font files **and**
   - the derived glyph PBFs

2) 🧪 Generate glyph PBF ranges from the font(s)
   - Use a known-good glyph generator (project-standard toolchain).
   - Prefer deterministic builds (same input → same output).

3) 📦 Drop outputs into:
   - `web/src/assets/map/glyphs/{fontstack}/`

4) 📝 Update this README metadata table (provenance + license)

5) 🧭 Update style(s)
   - `glyphs` template points to your hosted path
   - symbol layers include the `text-font` stack(s)

6) 🔍 Verify in dev + prod build
   - check for **404 glyph requests**
   - validate label rendering at multiple zoom levels

---

## 🗺️ Why this exists in KFM

KFM is map-centric (vector tiles + interactive labels). Text rendering must be:
- deterministic ✅
- reproducible ✅
- license-compliant ✅
- governed like any other shipped artifact ✅

This folder is where typography meets the evidence pipeline.

---

## 📚 References (specs & tooling)

- MapLibre Style Spec — `glyphs`
- MapLibre Style Spec — root (`glyphs` URL rules)
- Mapbox Style Spec — `glyphs`
- TileServer-GL notes on glyph ranges and file layout
- `fontnik` / `node-fontnik` (common open tooling for generating glyph PBFs)

> Keep external links in project-level docs if you want this README to remain fully offline-friendly.