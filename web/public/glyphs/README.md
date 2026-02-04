# 🅶 Glyphs (MapLibre Font PBFs)

![MapLibre](https://img.shields.io/badge/MapLibre-GL%20JS-1f425f)
![Format](https://img.shields.io/badge/Format-PBF%20(SDF%20Glyphs)-informational)
![Scope](https://img.shields.io/badge/Scope-Map%20labels%20only-blue)
![Served%20From](https://img.shields.io/badge/Served%20From-web%2Fpublic%2Fglyphs-success)

This folder contains **Signed Distance Field (SDF) font glyphs** packaged as **`.pbf`** files for **MapLibre GL JS** label rendering (i.e., any layer using `text-field` + `text-font`).

> ✅ **These are NOT UI icon SVGs**.  
> Icons/patterns for maps are handled by the **style `sprite`** endpoint, not by `glyphs`.

---

## 📦 What lives here

A typical glyph pack is a directory named exactly like a font (the *font face name*), containing many PBF ranges.

```text
📁 web/public/glyphs/
├─ 📄 README.md
├─ 📁 Open Sans Regular/
│  ├─ 0-255.pbf
│  ├─ 256-511.pbf
│  ├─ ...
│  └─ 65280-65535.pbf
└─ 📁 Noto Sans Regular/
   ├─ 0-255.pbf
   ├─ 256-511.pbf
   └─ ...
```

### 🔎 Why so many files?
Glyphs are chunked into **Unicode ranges of 256 code points** (example: `0-255`, `256-511`, etc.). MapLibre requests only the ranges it needs for the text currently visible.

---

## 🧭 How KFM uses these glyphs

KFM’s web map is rendered with **MapLibre GL JS** and loads map resources from a style JSON:
- vector tiles (`.pbf`)
- sprites (icons/patterns)
- **glyphs (this folder)**

If labels disappear or throw font-related errors, this directory (and the `glyphs` URL in the style) is one of the first things to verify.

---

## 🧩 Style JSON setup

Your map **style JSON** must include a **root-level** `glyphs` property.

### ✅ Recommended pattern (same-origin hosting)
Because this folder is under `web/public/`, it is typically served at:

- `/glyphs/...` (app root)

Example style snippet:

```jsonc
{
  "version": 8,
  "name": "KFM Style",
  "sprite": "https://YOUR_DOMAIN/sprites/sprite",
  "glyphs": "https://YOUR_DOMAIN/glyphs/{fontstack}/{range}.pbf",
  "sources": {},
  "layers": []
}
```

> 📝 Note: Many setups work with relative paths too, but an **absolute URL** is the most portable (local dev, production, CDN, editors, etc.).

### 🏷️ Font usage in a layer

```jsonc
{
  "id": "place-labels",
  "type": "symbol",
  "source": "kfm",
  "source-layer": "places",
  "layout": {
    "text-field": ["get", "name"],
    "text-font": ["Open Sans Regular"],
    "text-size": 12
  }
}
```

✅ **Rule:** The value in `text-font` must match the **directory name** inside `web/public/glyphs/`.

---

## 🧠 Important details (fontstack & URL encoding)

### `{fontstack}` is not always a single font
MapLibre can request a **comma-separated list** for `{fontstack}` based on your `text-font` stack.

That means it may request something like:

```text
/glyphs/Open Sans Regular,Arial Unicode MS Regular/0-255.pbf
```

#### ✅ Best practice for static hosting
- Prefer **single-font stacks** in `text-font`, unless you intentionally support concatenated stacks.
- If you **do** use multi-font stacks, ensure your glyph hosting solution supports it (static files usually don’t).

### Spaces & special characters
Folder names with spaces (e.g., `Open Sans Regular`) will be URL-encoded in requests:

- `Open%20Sans%20Regular`

That’s normal ✅

---

## 🛠️ Adding or updating fonts

### Option A: MapLibre Font Maker (quick + friendly)
1. Start with a `.ttf` or `.otf` font file.
2. Convert it to MapLibre-compatible glyph PBFs using a font-to-PBF pipeline/tool.
3. Extract the generated folder into:

```text
web/public/glyphs/<Exact Font Name>/
```

4. Update your style JSON `text-font` to match the folder name exactly.

### Option B: Scripted generation (repeatable builds)
For fully reproducible builds, generate glyphs from source fonts via tooling (e.g., font → SDF glyph PBF pipelines). This is best if:
- you expect frequent style/font changes
- you want CI to validate/produce assets
- you want consistent output across environments

> 💡 Recommendation: If we adopt scripted generation, add a `scripts/glyphs/` build step and document it here (inputs, outputs, licenses).

---

## 🚚 Serving & caching notes

These files are:
- binary (`.pbf`)
- numerous (hundreds per font)
- frequently cached well

### ✅ Suggested server behavior
- **Long cache** (immutable) for glyph PBFs
- **Compression** (gzip or brotli) when possible
- Correct MIME type is helpful (but most clients work with `application/octet-stream`)

### 🧯 Common pitfall: “gzipped PBFs” without headers
Some glyph packs are stored already gzipped while still named `.pbf`. If the server does **not** send `Content-Encoding: gzip`, MapLibre may fail to parse them.

---

## 🧪 Quick sanity checks

### 1) Confirm the file exists (example)
```bash
curl -I "https://YOUR_DOMAIN/glyphs/Open%20Sans%20Regular/0-255.pbf"
```

You want:
- `200 OK`
- sensible `Content-Length`
- (optional) caching headers

### 2) Confirm style points to the right glyph endpoint
Search your style JSON for:

```json
"glyphs"
```

---

## 🧩 Troubleshooting cheatsheet

### ❌ Error: `use of "text-field" requires a style "glyphs" property`
✅ Fix:
- Add `glyphs` at the **root** of your style JSON.
- Ensure the URL is reachable from the client.

### ❌ Labels render as empty squares / tofu
✅ Fix:
- The chosen font may not include those characters (e.g., CJK, Arabic).
- Add a font that supports the needed glyphs and ensure the style references it.

### ❌ 404s for `/glyphs/.../*.pbf`
✅ Fix:
- Folder name mismatch (`text-font` vs directory name)
- URL encoding issues (spaces, commas)
- `glyphs` URL points to the wrong host/path

---

## ⚖️ Licensing & provenance

Fonts are **software** with licenses. Before committing or deploying glyphs:
- confirm you have redistribution rights ✅
- store the font license text alongside the font source (or in a central `THIRD_PARTY_NOTICES` file)
- avoid committing proprietary fonts into public repos

---

## 🧭 Related map assets

- 🧩 **Sprites**: icons/patterns (style `sprite`)
- 🗺️ **Tiles**: vector tiles (`.pbf`) and raster tiles (`.png/.webp`)

> Keeping **tiles + sprites + glyphs** aligned is what makes the map render consistently across dev/prod.

---