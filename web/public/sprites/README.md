# 🧩 Sprites (Map Icons & Patterns)

![Static Assets](https://img.shields.io/badge/served%20as-static%20assets-2ea44f?style=flat-square)
![MapLibre](https://img.shields.io/badge/MapLibre-style%20sprites-1f6feb?style=flat-square)
![PNG%20%2B%20JSON](https://img.shields.io/badge/format-PNG%20%2B%20JSON-8250df?style=flat-square)

This folder contains **sprite sheets** used by the web UI’s mapping stack (🗺️ MapLibre style sprites).

A sprite sheet is:
- `sprite.png` → the packed image atlas 🧱
- `sprite.json` → the “index” (where each icon lives in the atlas) 🗺️

Sprites are used by MapLibre style properties like:
- `icon-image` (symbols) 🏷️
- `background-pattern`, `fill-pattern`, `line-pattern`, `fill-extrusion-pattern` 🎨

---

## ⚡ Quick Start

> [!TIP]
> **The style `sprite` URL must NOT include** `.png`, `.json`, or `@2x`.

In your MapLibre style JSON (root level):

```json
{
  "version": 8,
  "name": "KFM Style",
  "sprite": "/sprites/kfm/sprite"
}
```

MapLibre will automatically request:

- `/sprites/kfm/sprite.json`
- `/sprites/kfm/sprite.png`
- `/sprites/kfm/sprite@2x.json` (HiDPI / Retina)
- `/sprites/kfm/sprite@2x.png` (HiDPI / Retina)

---

## 📁 Recommended Folder Layout

> [!NOTE]
> This repo can support multiple “sprite packs” (themes, eras, UI vs map, etc.). Keep packs small and intentional.

```text
📁 web/public/sprites/
├─ 📄 README.md                         👈 you are here
├─ 📁 kfm/                              🏛️ primary map icon set
│  ├─ 🖼️ sprite.png
│  ├─ 🧾 sprite.json
│  ├─ 🖼️ sprite@2x.png
│  └─ 🧾 sprite@2x.json
└─ 📁 _src/                             🧪 (optional) source SVGs used to generate sprites
   └─ 📁 kfm/
      ├─ 🧩 trailhead.svg
      ├─ 🧩 fort.svg
      └─ 🧩 river_crossing.svg
```

If your repo already stores SVG sources elsewhere, that’s fine—just keep the **generated** `sprite*.png/json` files here in a stable path.

---

## 🏷️ Referencing Icons in a Style

The sprite JSON defines icon names. Use those names in `icon-image`.

Example layer snippet:

```json
{
  "id": "historic-trail-markers",
  "type": "symbol",
  "source": "kfm",
  "layout": {
    "icon-image": "trailhead",
    "icon-size": 1,
    "icon-allow-overlap": true
  }
}
```

---

## 🛠️ Building / Updating Sprites (SVG ➜ PNG+JSON)

A common workflow is to generate MapLibre-compatible sprites from a folder of SVGs using **spritezero**.

### Option A — `npx` (no global install)

```bash
# 1x
npx @mapbox/spritezero-cli web/public/sprites/kfm/sprite web/public/sprites/_src/kfm --ratio=1

# 2x (HiDPI) — IMPORTANT: output name includes @2x
npx @mapbox/spritezero-cli web/public/sprites/kfm/sprite@2x web/public/sprites/_src/kfm --ratio=2
```

### Option B — Install globally

```bash
npm i -g @mapbox/spritezero-cli

# Then run:
spritezero web/public/sprites/kfm/sprite   web/public/sprites/_src/kfm --ratio=1
spritezero web/public/sprites/kfm/sprite@2x web/public/sprites/_src/kfm --ratio=2
```

---

## ✅ Quality Checklist (Before You Commit)

- [ ] **Both** 1x and `@2x` sprite files exist (`.png` + `.json`)
- [ ] Icon names are **stable** (renames break `icon-image` references)
- [ ] SVGs are clean (no giant viewBox, no stray invisible paths)
- [ ] Icons are visually consistent (stroke weight, padding, alignment)
- [ ] File sizes are reasonable (sprites shouldn’t be massive)

---

## 🧯 Troubleshooting

<details>
<summary><strong>Icons don’t show up on the map 🫥</strong></summary>

- Confirm `sprite` in the style JSON is correct and **does not** include extensions.
- Open these directly in the browser:
  - `/sprites/kfm/sprite.json`
  - `/sprites/kfm/sprite.png`
- Check DevTools → Network:
  - 404 → wrong path / not deployed
  - CORS errors → sprite hosted on another domain without proper headers
- Confirm the icon name exists in `sprite.json` and matches `icon-image`.
</details>

<details>
<summary><strong>Icons are blurry on Retina displays 📱</strong></summary>

Make sure you generated and deployed:
- `sprite@2x.png`
- `sprite@2x.json`

MapLibre will request them automatically on HiDPI devices.
</details>

<details>
<summary><strong>Changing icon color doesn’t work 🎨</strong></summary>

MapLibre can only recolor icons if they’re authored/used as **SDF** icons (depending on your pipeline).
If you need runtime recoloring, plan your icon authoring pipeline accordingly.
</details>

---

## 🔐 Licensing & Attribution

> [!IMPORTANT]
> Only add icons we’re allowed to ship.

If you import third‑party icons:
- Keep a short note of **source + license**
- Prefer placing it in a local file like `ATTRIBUTION.md` in this folder or the sprite pack folder.

---

## 📚 References (for future you 🧠)

- MapLibre Style Spec — Sprite: https://www.maplibre.org/maplibre-style-spec/sprite/
- Mapbox Style Spec — Sprite (conceptually equivalent): https://docs.mapbox.com/style-spec/reference/sprite/
- spritezero-cli: https://github.com/mapbox/spritezero-cli