# 🗺️ KFM Map Styles (Web)

![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
![Map Style](https://img.shields.io/badge/Map%20Style-Mapbox%20Spec%20%2F%20MapLibre%20Compatible-2ea44f)
![Assets](https://img.shields.io/badge/Assets-Sprites%20%26%20Glyphs-informational)
![Governance](https://img.shields.io/badge/Governance-Provenance--First%20✅-8A2BE2)

> [!IMPORTANT]
> This directory is **UI-facing**, but it is still part of the **KFM “truth path”**: styles must render **governed** map layers in a way that stays **traceable**, **accessible**, and **environment-safe** (no secrets, no private URLs hardcoded).

---

## 📍 You are here

`web/src/assets/map/styles/`

These files define **how KFM map layers look** (colors, line weights, labels, ordering) when rendered in the web client.

---

## ✨ What lives in this folder

Typical contents (update this list if/when files change):

```text
🗂️ web/
  🗂️ src/
    🗂️ assets/
      🗂️ map/
        🗂️ styles/
          📄 README.md                👈 you are here
          🎨 kfm.light.style.json     (example)
          🌙 kfm.dark.style.json      (example)
          🧩 sprites/
            🖼️ kfm.sprite.png         (example)
            🧾 kfm.sprite.json        (example)
          🔤 glyphs/                  (optional; if self-hosting fonts)
          🧱 tokens/                  (optional; shared design tokens)
```

> [!NOTE]
> If your repo already uses different filenames, keep the **concepts** the same and update the **tree** above to match reality.

---

## 🚀 Quick start (how these styles are used)

### 🧭 In a MapLibre-style map component (example)

```ts
import maplibregl from "maplibre-gl";

// Example: import a local JSON style (path may differ in your app)
import kfmLight from "./kfm.light.style.json";

const map = new maplibregl.Map({
  container: "map",
  style: kfmLight as any,
  center: [-98.0, 38.5], // Kansas-ish
  zoom: 5,
});
```

### 🔌 Where style `sources` should point

KFM serves map layers as tiles. Your style sources should reference **tile endpoints**, typically:

- Vector tiles: `/tiles/<layer>/{z}/{x}/{y}.pbf`
- Raster tiles (fallback / special cases): `/tiles/<layer>/{z}/{x}/{y}.png` or `.webp`

✅ Preferred (environment-agnostic):
- Use **relative URLs** (`/tiles/...`) whenever the web app is served behind the same origin / reverse proxy as the API.
- If you must use absolute URLs, do it via **runtime substitution** (see “Environment Safety” below).

---

## 🧱 Style conventions (KFM-friendly)

### 1) 🔒 Environment safety (no secrets)
**Never** commit:
- API keys
- tokens
- private base URLs
- internal hostnames

**Good patterns**
- ✅ `tiles: ["/tiles/geo_counties/{z}/{x}/{y}.pbf"]`
- ✅ runtime patching of a placeholder base URL (e.g. replacing `__KFM_TILE_BASE__`)
- ✅ building style JSON from a small config object at runtime

**Bad patterns**
- ❌ `https://internal-prod.example.com/tiles/...`
- ❌ `?token=...` in a style file
- ❌ embedding user-identifying query params

---

### 2) 🧾 Naming conventions (keep layers intelligible)

#### `source` keys
Use stable, readable names:
- `kfm:base`
- `kfm:ref_counties`
- `kfm:hist_railroads_1880`
- `kfm:analysis_hotspots`

#### `layer.id`
Use a **taxonomy** so ordering and debugging are easy:

- `base/*` → land, water, background, terrain shading
- `ref/*` → roads, boundaries, labels, POIs
- `hist/*` → historical overlays, time-sliced layers
- `analysis/*` → derived layers (heatmaps, clusters, model outputs)
- `ui/*` → UI-only affordances (selection outlines, hover halos)

Example IDs:
- `base/land`
- `ref/boundary_state`
- `hist/towns_1870`
- `analysis/density`

---

### 3) 🧬 Provenance + traceability (a “map behind the map” mindset)

KFM’s core promise is that users can trace what they see back to sources. Styles can help by embedding metadata:

✅ Recommended:
- Put dataset identifiers in `layer.metadata`
- Use `source.attribution` for human-readable attribution
- Add links (where your UI can surface them) like `stac`, `dcat`, `prov`, `storyNodeId`

Example pattern:

```json
{
  "id": "hist/railroads_1880",
  "type": "line",
  "source": "kfm:hist_railroads_1880",
  "source-layer": "railroads",
  "metadata": {
    "kfm:dataset_id": "ks_railroads_1880",
    "kfm:provenance": "prov:ks_railroads_1880@v1",
    "kfm:catalog_ref": "stac:collections/ks_railroads_1880"
  }
}
```

> [!IMPORTANT]
> **If it can’t be traced, it shouldn’t ship.** Treat style edits as part of the product’s trust surface.

---

## 🎨 Cartographic rules of thumb (practical + consistent)

### ✅ Visual hierarchy
- Make “base” layers quieter (low contrast)
- Promote the story layer (your “active” narrative layer)
- Avoid turning the map into a high-frequency texture wall

### ✅ Figure–ground clarity
- Stronger boundaries where needed
- Softer fills for regions
- Use halos for labels when they overlap complex backgrounds

### ✅ Contrast & accessibility
- Maintain readable contrast for text + key lines
- Don’t rely on color alone for meaning (use width, pattern, opacity, icons)
- Prefer colorblind-safe ramps for choropleths and heatmaps

---

## 🧪 Validation & QA checklist

### 🧰 Style validation
Before merging:
- [ ] JSON is valid (no trailing commas, correct types)
- [ ] The map loads at zoom 0 → max
- [ ] No missing sprites / glyphs
- [ ] Layer order matches intent (base → ref → overlays → UI)
- [ ] Labels aren’t exploding (duplicate names / collisions)

### ♿ Accessibility + semantic correctness
- [ ] Text size is readable (and scales appropriately by zoom)
- [ ] Contrast is sufficient for labels & critical geometry
- [ ] Legend semantics match units and classifications
- [ ] Every visible layer can be tied back to provenance (via metadata or UI link-out)

---

## 🧩 Adding a new style or theme

### ✅ New theme (light/dark/print)
1. Duplicate an existing style JSON
2. Change:
   - `name`
   - theme tokens (colors, background, label halos)
3. Keep:
   - `sources` structure (unless deliberately changing basemap approach)
   - provenance metadata patterns
4. Add screenshots to the PR (before/after)

### ✅ New icons (sprites)
1. Add icon to sprite sheet pipeline (if you have one)
2. Ensure sprite JSON maps names correctly
3. Use consistent naming:
   - `icon:railroad`
   - `icon:fort`
   - `icon:town`
4. Verify at multiple DPIs / zooms

---

## 📴 Offline / packaged tiles (optional workflow)

If the project supports offline tiles (e.g., PMTiles/MBTiles), keep styles portable by:
- isolating tile source configuration (so it can swap from HTTP tiles → packaged tiles)
- avoiding absolute URLs in committed styles
- documenting any special “offline style” variant here

---

## 🧯 Troubleshooting

### “The map is blank”
- Check network requests for `/{z}/{x}/{y}` tiles returning 404/500
- Confirm the style source `type` matches:
  - `"vector"` for `.pbf`
  - `"raster"` for `.png`/`.webp`
- Verify `source-layer` matches the tileset layer name

### “Icons don’t show”
- Sprite URL is wrong, sprite JSON missing, or icon name mismatch
- Confirm the style references the sprite correctly:
  - `"sprite": "…/kfm"` (without extension)

### “Labels look fuzzy / clipped”
- Check font stack / glyphs setup
- Ensure halos are used appropriately over busy backgrounds

---

## 🔗 Related docs (in-repo)

- 📚 Backend tiles & API boundary: `../../../../../src/server/api/README.md`
- 🧭 Governance / PR expectations: `../../../../../.github/README.md`
- 🧪 Validators & tooling: `../../../../../tools/validation/` (if present)
- 🏛️ Architecture & standards: `../../../../../docs/`

---

## ✅ PR checklist (map style changes)

When your PR touches styles, include:

- [ ] Before/after screenshots (at relevant zooms)
- [ ] Notes on what changed and why (1–3 bullets)
- [ ] Confirmation that provenance + attribution remain correct
- [ ] Accessibility check (contrast + label readability)
- [ ] Confirmation that no secrets / internal URLs were introduced

---

### 🙌 Keep it boring (in a good way)
Predictable naming + traceable metadata + safe URLs = styles we can ship confidently. ✅
