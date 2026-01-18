# 📍 Marker Icons (Map Pins & Point Symbols)

![Asset Type](https://img.shields.io/badge/asset-markers-blue)
![Format](https://img.shields.io/badge/format-SVG%20first-success)
![Map UI](https://img.shields.io/badge/usage-map%20UI%20%2B%20timeline-informational)
![A11y](https://img.shields.io/badge/a11y-shape%20%2B%20contrast-important)
![KFM](https://img.shields.io/badge/project-KFM-black)

Point symbols + pin markers used by the **Kansas Frontier Matrix** web experience 🗺️.  
These icons should stay **consistent, legible, and “trust-friendly”** (icons help users navigate; they don’t *prove* the data).

> [!IMPORTANT]
> Marker icons are part of the UI contract 🧩  
> Keep IDs stable, keep visuals consistent, and ensure every marker has a clear semantic meaning.

---

## 📚 Contents

- [🧭 What lives here](#-what-lives-here)
- [🗂️ Folder layout](#️-folder-layout)
- [🏷️ Naming rules](#️-naming-rules)
- [🎨 Design rules](#-design-rules)
- [🧠 Semantics](#-semantics)
- [⚡ Performance](#-performance)
- [🧪 Usage examples](#-usage-examples)
- [➕ Adding a new marker](#-adding-a-new-marker)
- [✅ QA checklist](#-qa-checklist)

---

## 🧭 What lives here

This folder is specifically for **map markers** (point symbols) — not general UI icons.

Markers are used for things like:
- 📌 Features users can click/tap (places, events, datasets)
- ✨ “Sites of interest” / highlights
- 🧭 Wayfinding pins (selected / hovered / bookmarked)
- 🧾 Evidence-linked map annotations (when applicable)

---

## 🗂️ Folder layout

> Keep structure boring + predictable 😌  
> (Less treasure-hunt. More shipping.)

```text
web/
  assets/
    media/
      icons/
        markers/
          README.md  👈 you are here
          manifest.json           (recommended)
          🧷 core/
            pin.svg
            pin-selected.svg
            pin-hover.svg
          🗺️ categories/
            historic-site.svg
            archival-record.svg
            waterway.svg
            settlement.svg
          ✨ ai/
            site-of-interest.svg
          ♿ a11y/
            high-contrast/
              pin.svg
```

**If your repo already has a different structure:** keep it — but still follow the rules below.

---

## 🏷️ Naming rules

### ✅ File naming

- **kebab-case** only
- **no spaces**, **no capitals**
- keep names semantic, not visual  
  ✅ `historic-site.svg`  
  ❌ `blue-pin.svg`

### ✅ States & variants

Use suffixes for interaction/state variants:

| Variant | Suffix example |
|---|---|
| default | `pin.svg` |
| hover | `pin-hover.svg` |
| selected | `pin-selected.svg` |
| disabled | `pin-disabled.svg` |
| high contrast | `a11y/high-contrast/pin.svg` |

> [!NOTE]
> Try to keep the number of variants small. Prefer styling in code (when feasible) over multiplying files.

---

## 🎨 Design rules

### 1) Size & legibility 🔎
Markers must remain readable at **small sizes** (common targets):
- 16×16 (dense views)
- 24×24 (default map symbol)
- 32×32 (focus/selected)

**Rule of thumb:** if the glyph is unclear at 24px, simplify it.

### 2) Consistent silhouette 🧷
Markers should share a consistent family style:
- similar stroke weight
- similar corner radii
- consistent “visual weight” (don’t mix super-thin icons with chunky ones)

### 3) Anchor point 🎯
Design for predictable anchoring (especially for pin shapes):
- **Pin markers:** anchor at the **tip**
- **Dot/circle markers:** anchor at the **center**

If you add a `manifest.json`, store anchor rules there (recommended).

### 4) Color discipline 🎨
- Don’t rely on color alone to communicate meaning.
- Prefer a **shape difference** (or glyph change) for categories.
- Use color as a **secondary** cue (e.g., status/severity).

### 5) A11y / contrast ♿
- Ensure contrast works on light + dark basemaps.
- Provide a high-contrast variant when needed (folder: `a11y/high-contrast/`).

---

## 🧠 Semantics

### Qualitative vs quantitative 🚦
Think about what the marker is communicating:

- **Qualitative (different kinds):** use distinct **shapes/glyphs/icons**  
  Example: settlement vs waterway vs historic site

- **Quantitative (more/less):** prefer **size/value** changes *in styling*, not totally different icons  
  Example: low/medium/high intensity should ideally be styling-driven (size/opacity/value), not “3 unrelated icons”.

### “Truth & trust” principle 🧾
Markers should never imply certainty if the underlying data is uncertain.  
If a marker represents an AI-flagged insight, use a **distinct** icon family (e.g., under `ai/`) so users don’t confuse it with primary-source features.

---

## ⚡ Performance

### Preferred formats 🧰
- ✅ **SVG** (default)
- ⚠️ PNG only when required (legacy browsers, very specific rendering constraints)

### Optimization ✅
Before committing:
- optimize SVGs (e.g., SVGO or equivalent)
- remove editor metadata
- keep path counts reasonable

> [!TIP]
> If you decide to ship markers via a sprite sheet, keep it consistent across the codebase (don’t mix 3 delivery methods).

---

## 🧪 Usage examples

### MapLibre-style usage (conceptual) 🗺️
```js
// Example: resolve a marker URL (bundler-friendly)
const iconUrl = new URL(
  "./categories/historic-site.svg",
  import.meta.url
).toString();

// Pseudo-code; actual implementation depends on your map stack
map.loadImage(iconUrl, (err, image) => {
  if (err) throw err;
  map.addImage("historic-site", image);
});
```

### Leaflet-style usage (conceptual) 📌
```js
const iconUrl = new URL("./core/pin.svg", import.meta.url).toString();

const pinIcon = L.icon({
  iconUrl,
  iconSize: [24, 24],
  iconAnchor: [12, 24], // bottom center for pins
});

L.marker([lat, lng], { icon: pinIcon }).addTo(map);
```

---

## ➕ Adding a new marker

### Step-by-step 🛠️
1. **Pick the semantic ID** (kebab-case): `historic-site`
2. **Create the SVG** (match the style + stroke rules)
3. **Export** and place it in the right folder (`categories/`, `core/`, `ai/`, etc.)
4. **Optimize** the SVG
5. **Add/Update `manifest.json`** (recommended)
6. **Preview on-map** at 16/24/32px on light & dark basemaps
7. ✅ Commit with a clear message: `add marker: historic-site`

### Recommended `manifest.json` (optional, but ideal) 📦
<details>
  <summary><strong>Example manifest shape (click to expand)</strong></summary>

```json
{
  "version": 1,
  "markers": [
    {
      "id": "historic-site",
      "label": "Historic site",
      "path": "categories/historic-site.svg",
      "anchor": "bottom",
      "tags": ["place", "history"],
      "license": "project-owned"
    }
  ]
}
```
</details>

---

## ✅ QA checklist

- [ ] Filename is kebab-case and semantic
- [ ] Looks good at 24px (and still recognizable at 16px)
- [ ] Anchor behavior is correct (tip vs center)
- [ ] Contrast holds on light + dark basemaps
- [ ] No “meaning by color only”
- [ ] SVG optimized (no editor junk)
- [ ] If third-party: license + attribution recorded
- [ ] (If applicable) entry added/updated in `manifest.json`

---

## 🧭 Guiding principle

**Markers are for navigation + clarity — not claims.**  
If a marker points to evidence, make sure the UI can lead the user back to that evidence path (source, provenance, metadata) 🔎🧾
