# 🧩 Legend Patterns — `_meta` (Catalog + Rules)

**Path:** `web/assets/maps/legends/patterns/_meta/`

**Purpose:** This folder documents and governs the **metadata + previews** for legend pattern assets (hatching, stipple, dots, etc.) used in the KFM map UI.

> 🧠 Context: KFM’s frontend includes **legends for map symbology** and **symbology controls**. Patterns help keep layers readable when colors overlap, on low-contrast screens, and in print-friendly contexts.  

---

## 🗺️ What lives here (and what does not)

✅ **Lives here**
- A **single source of truth** pattern manifest (IDs, labels, tags, licenses, provenance, etc.)
- Preview images for quick browsing
- Notes, conventions, and contribution rules

🚫 **Does *not* live here**
- The pattern tiles themselves (SVG/PNG)  
  Those should live in: `web/assets/maps/legends/patterns/`

---

## 🗂️ Suggested folder layout

> ⚠️ Layout may evolve — the key requirement is: **metadata must be centralized and validated** (contract-first).

```text
web/assets/maps/legends/patterns/
├── 📄 hatch-diagonal-45.svg
├── 📄 dots-fine.svg
├── 📄 crosshatch.svg
└── 📁 _meta/
    ├── 📄 README.md                👈 you are here
    ├── 📄 patterns.manifest.json   👈 registry + metadata
    ├── 📁 previews/                👈 generated or curated previews
    │   ├── 🖼️ hatch-diagonal-45.png
    │   ├── 🖼️ dots-fine.png
    │   └── 🖼️ crosshatch.png
    └── 📄 (optional) notes.md      👈 extra design notes if needed
```

---

## 🧾 Contract-first metadata (manifest)

KFM is **contract-first** and **provenance-first**: the UI should never rely on undocumented “magic assets.”  
Patterns are “just UI,” but they still carry **license** and **origin** requirements.

### ✅ Recommended: `patterns.manifest.json`

- Keep **one manifest** as the canonical catalog of patterns.
- Use stable `id`s that can be referenced from:
  - UI layer styles
  - legend rendering
  - Story Nodes / Focus Mode map steps (if applicable)

<details>
<summary><b>📦 Example manifest (copy/paste starter)</b></summary>

```json
{
  "$schema": "/schemas/ui/legend-patterns.schema.json",
  "version": "1.0.0",
  "patterns": [
    {
      "id": "hatch-diagonal-45",
      "label": "Diagonal hatch (45°)",
      "file": "../hatch-diagonal-45.svg",
      "format": "svg",
      "tile": { "width": 16, "height": 16, "seamless": true },
      "category": "generic",
      "tags": ["hatch", "linework", "fill"],
      "recommended": {
        "minZoom": 0,
        "maxZoom": 24,
        "fillOpacity": 0.25
      },
      "license": {
        "spdx": "CC0-1.0",
        "attribution": null,
        "source": null
      },
      "provenance": {
        "createdBy": "your-handle",
        "createdAt": "2026-01-17",
        "derivedFrom": []
      },
      "notes": "Good default hatch. Avoid for very small polygons at high zoom."
    }
  ]
}
```

</details>

### 🧱 Field guidance (quick reference)

| Field | Required | Notes |
| --- | --- | --- |
| `id` | ✅ | `kebab-case`, **unique**, stable forever once referenced |
| `label` | ✅ | human-friendly name for legend menus |
| `file` | ✅ | relative path to the pattern tile file |
| `format` | ✅ | `svg` preferred, `png` allowed |
| `tile.width/height` | ✅ | tile size in px (small + repeatable) |
| `category` | ⭕ | UI grouping (keep coarse: `generic`, `hydrology`, `admin`, `hazard`, etc.) |
| `tags` | ⭕ | UI search/filter (3–8 tags is usually enough) |
| `recommended` | ⭕ | optional display hints; avoid hard-coding styling in multiple places |
| `license.spdx` | ✅ | use SPDX identifiers when possible |
| `license.attribution` | ✅* | required if license requires attribution |
| `provenance` | ✅ | created-by + created-at + derived-from |

---

## 🔁 Deterministic asset behavior

KFM’s pipeline philosophy favors deterministic outputs. Apply that mindset here too:

- **Stable ordering:** keep manifest entries consistently ordered (alphabetical by `id` recommended).
- **No hidden coupling:** `id` must match how the UI references the pattern.
- **Reproducible previews:** if previews are generated, generation should be repeatable from the source tile.

> 💡 Tip: If you add a generator later, it should be **idempotent** (running it twice yields identical outputs).

---

## 🖼️ Previews

Previews are for humans (design review, quick scanning, diffs in PRs).

**Recommended preview rules**
- Size: **128×128** or **256×256**
- Format: **PNG**
- Background: **transparent** (so previews work in light/dark UI)
- Naming: `previews/<pattern-id>.png`

---

## ➕ Adding a new pattern (contributor recipe)

1. **Create the tile** 🧵  
   Add `web/assets/maps/legends/patterns/<pattern-id>.svg` (preferred) or `.png`.

2. **Register it** 🧾  
   Add an entry in `patterns.manifest.json`:
   - `id`, `label`, `file`, `format`, `tile`
   - **license** + **provenance** (required)

3. **Add a preview** 🖼️  
   Add `previews/<pattern-id>.png`.

4. **Validate** ✅  
   - File exists and tiles seamlessly
   - Manifest entry is complete
   - IDs are unique

5. **Sanity-check in UI** 🧭  
   Ensure it reads well as:
   - a small legend swatch (≈16–24px)
   - a filled polygon at mid zoom
   - a filled polygon at high zoom (no moiré)

---

## ✅ Definition of Done (DoD)

- [ ] Tile asset exists in `web/assets/maps/legends/patterns/`
- [ ] Seamless repeat confirmed (no visible seams)
- [ ] Added to `patterns.manifest.json` (contract complete)
- [ ] License + attribution correct and explicit
- [ ] Provenance filled (`createdBy`, `createdAt`, `derivedFrom` if applicable)
- [ ] Preview exists in `_meta/previews/`
- [ ] Readable at small legend swatch sizes
- [ ] No culturally sensitive motifs without explicit permission (see Governance)

---

## ♿ Accessibility & cartography tips

- Prefer **texture-first** readability (assume grayscale rendering).
- Avoid ultra-thin linework that disappears at small sizes.
- Avoid dense micro-patterns that cause moiré at common zoom levels.
- Aim for clear differentiation between common “neighbor” patterns:
  - diagonal hatch vs crosshatch
  - dots vs stipple
  - wide stripe vs narrow stripe

---

## 🛡️ Licensing + governance

KFM’s ethos is provenance-first: *nothing is a black box.* That includes visuals.

### Licensing rules 📜
- Prefer **CC0 / Public Domain** sources when pulling externally.
- If adapted from elsewhere:
  - keep the original license
  - include required attribution
  - record `derivedFrom` in provenance

### Cultural sensitivity 🎗️
- Do **not** add patterns that resemble sacred/culturally specific designs (especially Indigenous motifs) unless:
  - the design is licensed appropriately, **and**
  - there is explicit approval to use it in this context.

---

## 🔄 Versioning & deprecations

- **Never** reuse an existing `id` for a different visual.
- If a pattern must be removed:
  - mark it as deprecated in the manifest (recommended: `deprecated: true`)
  - keep the file until all references are migrated

---

## 🔌 Frontend usage hint (renderer-agnostic)

Patterns are typically referenced by their `id` in layer styling / legend configuration.

```ts
// Pseudocode (actual integration depends on renderer + style pipeline):
paint: {
  "fill-pattern": "hatch-diagonal-45"
}
```

---

## 📚 See also

- 📘 `/docs/MASTER_GUIDE_v13.md` — canonical pipeline & invariants
- 🧱 `/docs/standards/KFM_REPO_STRUCTURE_STANDARD.md`
- ✍️ `/docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`
- 🤝 `/CONTRIBUTING.md`
