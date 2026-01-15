# 🧩 Map Sprite Icons (MapLibre / Style Sprite)

![MapLibre](https://img.shields.io/badge/MapLibre-GL%20JS-2b7cff?logo=maplibre&logoColor=white)
![Sprites](https://img.shields.io/badge/format-sprite.json%20%2B%20sprite.png-6f42c1)
![Assets](https://img.shields.io/badge/location-web%2Fassets%2Ficons%2Fmap%2Fsprite-0aa)

📍 **Folder:** `web/assets/icons/map/sprite/`  
🎯 **Goal:** Provide a single, consistent **icon sprite** for the map UI (fast loads, fewer requests, consistent icon names).

---

## ✨ What is a “sprite” in MapLibre?

A MapLibre/Mapbox-style **sprite** is a pair (or trio) of files that MapLibre fetches to render icons used by symbol layers:

- `sprite.json` → metadata: icon names + coordinates inside the sprite sheet
- `sprite.png` → the packed icon sheet (1×)
- `sprite@2x.png` → the packed icon sheet (2×, retina)

> ✅ When the map style references an `icon-image`, MapLibre looks for that name in `sprite.json` and then pulls pixels from `sprite.png` / `sprite@2x.png`.

---

## 📦 Expected files in this folder

| File | Purpose | Edit manually? |
|------|---------|----------------|
| `sprite.json` | Icon atlas metadata (names → positions) | ❌ No (generated) |
| `sprite.png` | 1× sprite sheet | ❌ No (generated) |
| `sprite@2x.png` | 2× sprite sheet | ❌ No (generated) |
| `README.md` | You are here 🙂 | ✅ Yes |

> 🧠 **Rule of thumb:** If you’re changing icons, change the **source icons**, then **rebuild** the sprite.

---

## 🔌 How the map style loads this sprite

In your MapLibre style JSON, the sprite is set as a **base URL** (no extension).  
MapLibre will request `.../sprite.json` and `.../sprite.png` automatically.

```json
{
  "version": 8,
  "sprite": "/assets/icons/map/sprite/sprite",
  "sources": {},
  "layers": []
}
```

### Using an icon in a layer

```json
{
  "id": "historic-sites",
  "type": "symbol",
  "source": "kfm",
  "layout": {
    "icon-image": "kfm-site",
    "icon-size": 1
  }
}
```

> 🧩 `icon-image` must match a **key** in `sprite.json`.

---

## 🧭 Naming conventions (keep it boring + stable)

Icon names become API-like identifiers. Choose names that won’t need renaming later.

✅ Recommended:
- **kebab-case**
- **prefix by scope** (helps avoid collisions)
- short but descriptive

Examples:
- `kfm-site`
- `kfm-battle`
- `kfm-marker`
- `kfm-weather-station`
- `kfm-rail`

🚫 Avoid:
- spaces (`"my icon"`)
- uppercase (`KFM-Site`)
- vague names (`icon1`, `new`, `temp`)

> 🔒 **Stability matters:** renaming an icon can silently break styles, layers, legends, story nodes, and UI affordances.

---

## 🎨 Design constraints for map icons

Map icons are tiny. Design for legibility, not detail.

### ✅ Do
- Use **simple silhouettes** and **bold shapes**
- Keep strong contrast (transparent background)
- Align strokes to the pixel grid when possible
- Test at common sizes (12–24px in UI terms)

### 🚫 Don’t
- Add small text (it will blur)
- Use thin strokes everywhere
- Use gradients / complex shading (often muddies at small sizes)

---

## 🌈 Color strategy: “baked” vs “tintable (SDF)”
Depending on how the sprite is generated, icons may be:

### 1) Baked-color icons 🖼️
- The icon’s color is part of the PNG pixels.
- Pros: exact look
- Cons: hard to recolor per layer

### 2) Tintable icons (SDF) 🎛️
- The sprite stores icons as Signed Distance Fields.
- Pros: can recolor with style properties like `icon-color`
- Cons: requires SDF-compatible generation + simple shapes

> 💡 If you expect to recolor icons per layer/theme, prefer SDF icons and keep the geometry clean.

---

## 🛠️ Updating the sprite (typical workflow)

Since repos differ in tooling, **follow your project’s existing sprite build script** if it exists.

If you *don’t* have a script yet, the recommended approach is:

1) Put editable source icons (usually SVG) in a predictable place  
   Example convention:
   - `web/assets/icons/map/sprite/svg/` ✅ (suggested)
2) Run a sprite generator to output:
   - `sprite.json`
   - `sprite.png`
   - `sprite@2x.png`
3) Verify in the map UI (search a layer that uses the new icon)

<details>
<summary>🧪 Suggested “source + build” folder layout</summary>

```text
📁 web/assets/icons/map/sprite/
  ├─ 📄 README.md
  ├─ 📁 svg/                 # ✅ editable icon sources (recommended)
  │   ├─ kfm-site.svg
  │   ├─ kfm-battle.svg
  │   └─ ...
  ├─ 🧾 sprite.json           # ❌ generated
  ├─ 🖼️ sprite.png            # ❌ generated (1×)
  └─ 🖼️ sprite@2x.png         # ❌ generated (2×)
```

</details>

---

## ✅ QA checklist (before committing)

- [ ] **New icon shows on the map** (no missing-image placeholders)
- [ ] Icon is readable at typical zoom levels + icon-size values
- [ ] `sprite.json` contains the new icon key exactly as expected
- [ ] `sprite.png` and `sprite@2x.png` both updated
- [ ] No accidental renames/removals of existing icon keys
- [ ] If applicable: dark/light basemap contrast still works 🌗

---

## 🧯 Troubleshooting

### “Could not load sprite” / missing icons everywhere
- Check the style’s `"sprite"` URL is correct.
- Ensure `sprite.json` and `sprite.png` are deployed together.

### A single icon doesn’t appear
- Verify the `icon-image` name exactly matches the key in `sprite.json`
- Confirm the sprite was rebuilt after adding the source icon
- Check for naming typos (`kfm-site` vs `kfm_sites`)

### Retina looks blurry
- Ensure `sprite@2x.png` exists and is truly 2×
- Make sure the generator outputs consistent metadata for both

---

## 📜 Licensing & provenance 🧾

Icons may be original to KFM or derived from third-party sets.

✅ Best practices:
- Prefer icons with clear permissive licensing (or originals)
- Keep an internal note of icon provenance (source + license)
- If you import an external icon, ensure attribution requirements are met

---

## 🔗 Related (where these icons are used)

- 🗺️ Map styles (`sprite` URL + `icon-image` usage)
- 🧭 Map viewer (MapLibre UI)
- 🧩 Legends / layer catalog UI (icon preview + symbology)

---

## 🧼 Maintenance tips (future-you will thank you)

- 🧊 **Cache busting:** if icons change but clients don’t update, consider a version query string on the sprite URL (e.g., `.../sprite?v=YYYYMMDD`) in the style.
- 🔁 **Automate builds:** sprite generation should be deterministic and scripted (CI-friendly).
- 🧯 **Avoid breaking changes:** removing/renaming icons should be treated like an API change.

---

> 🚀 If you’re adding a new dataset/layer category, consider adding the icon at the same time—icons are part of the UX language.