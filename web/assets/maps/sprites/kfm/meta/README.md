# 🧩 KFM Map Sprite Metadata (`/web/assets/maps/sprites/kfm/meta`)

![Contract-first](https://img.shields.io/badge/contract--first-required-success)
![Provenance-first](https://img.shields.io/badge/provenance--first-required-blue)
![Map UI assets](https://img.shields.io/badge/ui--assets-sprites-informational)
![No mystery icons](https://img.shields.io/badge/no--mystery--icons-enforced-critical)

> **What this folder is:** the **metadata + governance** layer for the KFM sprite bundle used by the web map UI.  
> **What this folder is not:** the sprite PNG/JSON themselves (those live one level up in `../`).

---

## 🎯 Why `meta/` exists

KFM treats anything that appears in the UI as a **governed artifact**—that includes icons.

This folder keeps sprite assets aligned with KFM’s standards:

- 📜 **Licensing & attribution are explicit** (no “mystery icons”).
- 🔎 **Provenance is recorded** (where did this icon come from? why is it here?).
- 🧪 **Builds are repeatable** (deterministic input → deterministic outputs).
- 🧭 **Semantics are documented** (icons map to concepts like “Story Node”, “Treaty”, “Sensor”, etc.).

---

## 🗂️ Directory layout

```text
📁 web/assets/maps/sprites/kfm/
├── 🖼️ sprite.png
├── 🖼️ sprite@2x.png
├── 🧾 sprite.json
├── 🧾 sprite@2x.json
└── 📁 meta/
    ├── 📄 README.md   ← you are here
    ├── 🧾 (suggested) sprite.contract.json
    ├── 🧾 (suggested) icon-registry.json
    ├── 📄 (suggested) ATTRIBUTION.md
    └── 📁 (optional) sources/
        └── 📁 svg/
            ├── 🧩 story-node.svg
            ├── 🧩 treaty.svg
            └── 🧩 sensor.svg
```

> ✅ **Rule of thumb:**  
> - `../sprite*.{png,json}` = **generated** artifacts used by the map runtime  
> - `meta/` = **human + machine metadata** that explains and governs them

---

## 🗺️ How the web map uses sprites (quick refresher)

Most MapLibre/Mapbox-style pipelines reference sprites via a **URL prefix** (no extension), and load:

- `sprite.json` + `sprite.png` (1x)
- `sprite@2x.json` + `sprite@2x.png` (retina)

Example (typical `style.json` pattern):

```json
{
  "version": 8,
  "sprite": "/assets/maps/sprites/kfm/sprite",
  "sources": {},
  "layers": []
}
```

Then layers reference icons by the **JSON key**:

```json
{
  "id": "story-nodes",
  "type": "symbol",
  "source": "story_nodes",
  "layout": {
    "icon-image": ["get", "icon_id"],
    "icon-allow-overlap": true
  }
}
```

---

## 📦 What should live in `meta/`

### 1) `sprite.contract.json` (recommended ✅)

A **contract-first** manifest for the sprite bundle as a whole.

Minimum recommended fields:

- `bundle_id` (e.g., `"kfm"`)
- `version` (semantic version or content hash strategy)
- `license_policy` (what licenses are allowed / disallowed)
- `generator` (tool + version)
- `inputs` (where the canonical icon sources live)
- `outputs` (expected generated files + checksums)
- `attribution` (how attribution is satisfied: file, UI panel, etc.)

Example sketch:

```json
{
  "bundle_id": "kfm",
  "version": "0.1.0",
  "generator": {
    "tool": "sprite-packer",
    "config_path": "web/assets/maps/sprites/kfm/meta/sprite.config.json"
  },
  "inputs": {
    "source_dir": "web/assets/maps/sprites/kfm/meta/sources/svg",
    "canonical_format": "svg"
  },
  "outputs": [
    { "path": "web/assets/maps/sprites/kfm/sprite.json" },
    { "path": "web/assets/maps/sprites/kfm/sprite.png" },
    { "path": "web/assets/maps/sprites/kfm/sprite@2x.json" },
    { "path": "web/assets/maps/sprites/kfm/sprite@2x.png" }
  ],
  "license_policy": {
    "allowed_spdx": ["CC0-1.0", "MIT", "Apache-2.0"],
    "notes": "Any icon without a clear license/provenance is not eligible for inclusion."
  }
}
```

---

### 2) `icon-registry.json` (recommended ✅)

A registry for individual icon semantics + provenance.

Recommended per-icon fields:

- `id` (must match the sprite JSON key)
- `title` / `description`
- `category` (legend grouping)
- `tags` / `keywords` (search, UX)
- `source` (URL/citation or “internal”)
- `license_spdx`
- `attribution` (string that can be shown in UI credits)
- `notes` (design intent, usage constraints)

Example:

```json
{
  "bundle_id": "kfm",
  "icons": [
    {
      "id": "story-node",
      "title": "Story Node",
      "category": "narrative",
      "keywords": ["story", "citation", "focus-mode"],
      "source": { "type": "internal", "ref": "KFM design system" },
      "license_spdx": "CC0-1.0",
      "attribution": null
    }
  ]
}
```

---

### 3) `ATTRIBUTION.md` (recommended ✅)

A human-readable attribution list (great for compliance + trust).  
If you surface attributions in the UI, this file is still useful as the “source of truth”.

---

## ➕ Adding or updating an icon

### ✅ Required steps

1. **Add or edit the canonical icon source** (prefer SVG) in `meta/sources/svg/`.
2. **Register it** in `meta/icon-registry.json` with:
   - license (SPDX if possible)
   - source/provenance
   - attribution text (if required)
3. **Regenerate** the sprite outputs in `../` (1x + @2x).
4. **Verify** the icon renders correctly in the map (legend + layer).
5. **Commit**:
   - the updated generated sprite artifacts
   - the updated metadata in `meta/`

### 🚫 Anti-patterns (don’t do these)

- Editing `sprite.json` by hand (it should be generated).
- Adding an icon to the sprite without registering provenance/licensing.
- Introducing a visually ambiguous icon that won’t read at small sizes.

---

## 🎨 Icon design guidelines (KFM defaults)

- 📐 **Clarity over detail**: icons must remain readable at map zoom + small sizes.
- 🧱 **Consistent visual weight**: stroke widths / fill style should match the existing set.
- 🎯 **Semantic uniqueness**: if two icons look similar, they’ll confuse users in the legend.
- 🧭 **Legend-first thinking**: the icon should make sense both on-map and in a list/legend.

---

## ✅ Quality gates (Definition of Done)

- [ ] Icon appears in `icon-registry.json` with license + provenance
- [ ] Icon ID matches sprite JSON key exactly
- [ ] Both 1x and @2x sprite assets updated
- [ ] No visual collisions / cropping in sprite output
- [ ] UI legend label exists (or is intentionally hidden)
- [ ] Attribution updated (if required)

---

## 🧯 Troubleshooting

**Icon doesn’t render**  
- Check `icon-image` value matches the sprite JSON key exactly (case-sensitive).
- Confirm the style’s `"sprite"` URL prefix points to the right path.

**Icon is blurry on retina screens**  
- Ensure `sprite@2x.*` exists and the JSON entries contain the correct `pixelRatio`.

**Icon appears clipped**  
- Add padding in the source SVG, or adjust packing settings to include safe margins.

---

## 🔗 Related (recommended reading)

- 📘 KFM governance: contract-first + provenance-first (apply the same mindset to UI artifacts)
- 🧱 Repo standards: deterministic pipeline + validation gates
- 🗺️ Map styling: MapLibre style + sprite pipeline conventions

---
