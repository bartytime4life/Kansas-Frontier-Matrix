# 🧩 Glyphs for MapLibre and Mapbox GL

![MapLibre](https://img.shields.io/badge/MapLibre-GL%20JS-2b6cb0?logo=mapbox&logoColor=white)
![Format](https://img.shields.io/badge/Format-PBF-4a5568)
![Purpose](https://img.shields.io/badge/Purpose-Map%20labels-2f855a)
![Hosting](https://img.shields.io/badge/Works%20on-GitHub%20Pages-6f42c1)

This folder contains **glyph PBFs** (signed-distance-field glyphs) used by the KFM web map styles to render **text labels** (place names, roads, boundaries, legends) in **MapLibre GL**.

It exists so our `web/` front-end can be **self-contained** ✅ (fast, predictable, and not dependent on third-party glyph servers).

---

## 🎯 What lives here

- **Output files only**: `*.pbf` glyph ranges organized by **fontstack**
- Used by MapLibre GL at runtime via the **style JSON** `glyphs` URL template

> [!NOTE]
> These are **not CSS webfonts**. If you’re looking for `.woff/.woff2`, this is the wrong folder.

---

## 🧠 How glyph requests work

MapLibre style JSON has a `glyphs` URL template, typically like:

```json
{
  "glyphs": "/assets/maps/styles/glyphs/{fontstack}/{range}.pbf"
}
```

When a symbol layer uses `text-font`, MapLibre will request glyph PBFs like:

- `.../glyphs/Open%20Sans%20Regular/0-255.pbf`
- `.../glyphs/Open%20Sans%20Regular/256-511.pbf`

### Tokens MapLibre substitutes

- **`{fontstack}`** → the requested font stack (URL-encoded)
- **`{range}`** → a Unicode range bucket, usually in steps of **256**
  - `0-255`, `256-511`, `512-767`, etc.

> [!IMPORTANT]
> If the browser console/network tab shows `404` on glyphs, labels will disappear or render as ☐ boxes.

---

## 🗂️ Folder layout

```text
web/assets/maps/styles/glyphs/
├─ 🔤 <fontstack>/                 # 🔤 Glyph stack folder (name must match {fontstack} requested by styles)
│  ├─ 🔤📦 0-255.pbf                # Glyphs for Unicode codepoints 0–255 (256-codepoint pack)
│  ├─ 🔤📦 256-511.pbf              # Glyphs for Unicode codepoints 256–511
│  ├─ 🔤📦 512-767.pbf              # Glyphs for Unicode codepoints 512–767
│  └─ ➕ …                          # Additional 256-codepoint ranges as needed (e.g., 768-1023.pbf)
└─ 📄 README.md                     # 📘 How glyphs are generated/served + URL template + stack naming + licensing
```

### Naming rules that matter ✅

- Folder names must match what MapLibre requests for `{fontstack}` **after URL decoding**.
  - Browsers request with `%20`, servers typically map that to a real space.
- If your `text-font` includes a *stack* (multiple fonts), MapLibre may request a comma-separated `fontstack`.
  - Example request path (URL-encoded):  
    `Noto%20Sans%20Regular,Arial%20Unicode%20MS%20Regular`

> [!TIP]
> To avoid “combinatorial fontstack explosion”, prefer consistent single-font `text-font` usage where possible, and only add fallbacks where required.

---

## 🧰 Adding or updating glyphs

### Step 1: Identify which fonts are needed

Search your style JSON(s) under `web/assets/maps/styles/` for `text-font`.

Here’s a quick way (requires `jq`):

```bash
jq -r '.. | objects | .["text-font"]? // empty | .[]' web/assets/maps/styles/*.json | sort -u
```

Make sure every font name you see there is available via glyphs.

---

### Step 2: Use fonts we can legally ship

KFM prioritizes **clean licensing & provenance** 🧾

Before adding a font, capture:

- Font name + version
- Source (official repo/site)
- License type (ideally OFL or similarly permissive)
- Any required attribution text

> [!WARNING]
> Do not commit proprietary fonts or fonts with unclear redistribution rights.

---

### Step 3: Generate PBF ranges

There are multiple ways to generate glyph PBFs. Pick a repeatable approach that:
- produces `{range}.pbf` files
- matches the exact font names used in `text-font`
- is consistent across machines/CI

#### Option A: Use a known glyph build toolchain

Many teams use a `fontnik`-based workflow (Node + native deps) to generate glyphs.

Typical packages used in MapLibre ecosystems include:

- `@mapbox/fontnik`
- `@mapbox/glyph-pbf-composite`

Example (tooling may vary by OS/toolchain):

```bash
npm i -g @mapbox/fontnik @mapbox/glyph-pbf-composite
# then run your project’s glyph build script / workflow
```

#### Option B: Use a containerized workflow

If native builds are painful, prefer a containerized build so output is reproducible.  
(If/when we add a project script, this README should link it here.)

---

### Step 4: Commit with sanity checks

At minimum:

- `web/assets/maps/styles/glyphs/<fontstack>/0-255.pbf` exists for every required font
- style JSON `glyphs` path points to this folder correctly
- the map loads without glyph 404s in DevTools network tab

---

## ✅ Quick QA checklist

### Visual
- [ ] Zoom in/out and confirm labels remain stable
- [ ] Check bold/italic layers (if used) render correctly
- [ ] Confirm special characters used by Kansas place names render properly (apostrophes, diacritics if present)

### Network
- [ ] No `404` for `.../glyphs/.../*.pbf`
- [ ] No CORS errors (especially on GitHub Pages)

### Repo hygiene
- [ ] Added/updated font license and attribution info
- [ ] Kept glyph footprint reasonable (avoid shipping unused ranges)

---

## 🧯 Troubleshooting

### Labels missing entirely
- Check style JSON has a valid `glyphs` field
- Confirm the path is correct relative to how `web/` is hosted

### Labels render as empty squares ☐
- Glyph files exist, but the range you need is missing
- Add additional ranges beyond `0-255` (common when encountering non-ASCII characters)

### Some labels show, others don’t
- You may have multiple `text-font` values across layers and only generated one fontstack
- Re-run the `jq` command above and confirm coverage

### Works locally but fails on GitHub Pages
- Path issue: absolute (`/assets/...`) vs relative (`./assets/...`) depending on your Pages base path
- Also check that folder names with spaces/commas are served correctly by the host

---

## 🔐 License and provenance expectation

This project treats **assets like code** 🧠✅  
If you add or replace glyphs, also add:

- a clear record of the font source
- the font license text or a pointer to it
- any required attribution

> [!TIP]
> A lightweight pattern is to include a `SOURCES.md` or `FONTS.md` at the style/assets level that lists fonts + licenses + URLs.

---

## 📌 Related folders

```text
web/assets/maps/styles/
├─ *.json                # MapLibre styles (expect `glyphs` to point here)
├─ sprites/              # Icon + pattern sprites used by styles
└─ glyphs/               # You are here ✅
```

---

🧭 If you’re updating map styles and text starts behaving strangely, check glyphs first — they’re one of the most common silent failure points in MapLibre-based front-ends.
