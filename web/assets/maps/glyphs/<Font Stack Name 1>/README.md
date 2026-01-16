# 🧩 Glyphs — `<Font Stack Name 1>` (MapLibre / Mapbox GL)

![Status](https://img.shields.io/badge/status-active-2ea44f)
![Type](https://img.shields.io/badge/type-generated%20asset-blue)
![Map](https://img.shields.io/badge/rendering-MapLibre%20GL%20JS-6f42c1)
![Format](https://img.shields.io/badge/format-PBF%20(SDF%20glyphs)-informational)

> **What this folder is:** Pre-generated **SDF glyph** protobufs (`*.pbf`) for the **font stack** named **`<Font Stack Name 1>`**.  
> **Why it exists:** So the KFM web map can render labels **without relying on Mapbox-hosted fonts** and **without local-font variability**.

---

## 🧾 Policy metadata (KFM-MDP aligned)

| Field | Value |
|---|---|
| File | `web/assets/maps/glyphs/<Font Stack Name 1>/README.md` |
| Status | ✅ Active |
| Asset posture | 🧱 Generated + versioned (treat as build artifact) |
| Last updated | 2026-01-15 |
| Owners | `@kfm-web` + `@kfm-maps` *(update if you use CODEOWNERS)* |
| Downstream impact | 🗺️ Map label rendering (MapLibre style `glyphs` URL) |

---

## 📦 What’s inside

Typical contents (ranges may vary depending on generator + coverage):

```text
📁 web/assets/maps/glyphs/
  └─ 📁 <Font Stack Name 1>/
     ├─ 0-255.pbf
     ├─ 256-511.pbf
     ├─ 512-767.pbf
     ├─ ...
     └─ README.md  👈 you are here
```

### 🧠 How MapLibre uses these files
Your map style’s root `glyphs` property points to a URL template like:

```json
{
  "glyphs": "/assets/maps/glyphs/{fontstack}/{range}.pbf"
}
```

Then, any layer using `text-field` + `text-font` will trigger MapLibre to request:

```text
/assets/maps/glyphs/<Font Stack Name 1>/0-255.pbf
/assets/maps/glyphs/<Font Stack Name 1>/256-511.pbf
...
```

📚 Specs (handy):
- MapLibre Style Spec — glyphs: https://www.maplibre.org/maplibre-style-spec/glyphs/
- Mapbox Style Spec — glyphs: https://docs.mapbox.com/style-spec/reference/glyphs/

---

## ✅ When to add / regenerate glyphs

Regenerate this stack when **any** of the following changes:
- you swap the underlying `.ttf/.otf` font file(s)
- you add new languages / characters (diacritics, Cyrillic, etc.)
- you change hinting / normalization steps in your font pipeline
- you’re seeing “□” tofu boxes or missing glyph warnings in the map UI

---

## 🛠️ How to generate (two supported paths)

### Path A — Quick + visual (recommended for one-off)
Use **MapLibre Font Maker** and download the generated zip:

- https://maplibre.org/font-maker/

**Notes**
- Great for fast iteration ✅  
- Still treat the output as **generated**: keep the source font and record its license.

---

### Path B — Scriptable / CI-friendly (recommended for long-term)
Pick a generator and **pin versions** (deterministic builds matter).

Common options:
- `fontnik` (JS): https://github.com/mapbox/fontnik  
- `genfontgl` (used by OpenMapTiles docs): https://openmaptiles.org/docs/style/mapbox-gl-style-spec/  
- `node-fontnik` (older toolchain): https://github.com/mapbox/node-fontnik

**Example (pseudo) workflow**
```bash
# 1) Put your source font(s) somewhere tracked (ideally outside this glyph output folder)
#    e.g. web/assets/maps/fonts-src/<Family>/*.ttf

# 2) Generate glyph PBF ranges into this folder
#    (exact command depends on chosen generator)
generate-glyphs \
  --font "path/to/<Font Stack Name 1>.ttf" \
  --out  "web/assets/maps/glyphs/<Font Stack Name 1>/"
```

🎯 Goal: output files named like `0-255.pbf`, `256-511.pbf`, etc.

---

## 🔍 Sanity checks (before you commit)

- [ ] **License**: font is compatible with the repo’s distribution goals (prefer **SIL OFL**, Apache-2.0, etc.)
- [ ] **Coverage**: labels render for expected languages/diacritics (spot check)
- [ ] **No 404s**: devtools → Network → glyph requests should not 404
- [ ] **Size**: glyph folder size is reasonable (avoid committing huge stacks accidentally)
- [ ] **Naming**: `<Font Stack Name 1>` matches the style’s `text-font` exactly

---

## 🧯 Troubleshooting

### “□” boxes (tofu) in labels
Likely causes:
- missing glyph range file for the characters being displayed
- style points at wrong `glyphs` endpoint
- font stack name mismatch (spaces/case matter)

Fix:
1) open devtools → Network → filter by `.pbf`  
2) confirm requested URL exists  
3) if missing, regenerate with broader charset coverage

### Random font differences between machines
That usually happens when `glyphs` is not set (MapLibre falls back to local fonts).  
✅ Make sure the style **does** set `glyphs` and the app serves these PBFs.

---

## 🧼 House rules for this folder

- 🚫 Don’t hand-edit `.pbf` files.
- ✅ Keep this README accurate for **this specific stack**.
- 🧷 If you change the underlying font, record:
  - font name + version
  - source URL
  - license name + text (or pointer to where it’s stored in-repo)

---

## 🔗 Related folders (mental map)

```text
🗺️ web/assets/maps/
  ├─ 🎨 styles/     (MapLibre style JSON)
  ├─ 🧩 glyphs/     (this folder)
  └─ 🧿 sprites/    (icons/markers in sprite PNG+JSON or sprite PBF)
```

If you’re adding a whole new typography system, you’ll usually touch:
✅ `styles/` (text-font + glyphs URL)  
✅ `glyphs/` (this)  
✅ possibly `sprites/` (label shields / POI icons)

---