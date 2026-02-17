# Icons

![scope: public](https://img.shields.io/badge/scope-public-brightgreen)
![governance](https://img.shields.io/badge/governance-required-blue)
![formats](https://img.shields.io/badge/formats-SVG%20%7C%20PNG%20%7C%20ICO-lightgrey)

This folder contains **static icon assets** for the web UI.

> [!WARNING]
> Anything under `web/public/` ships to browsers and may be **publicly accessible**.
> Do **not** place sensitive imagery, partner-restricted assets, or anything that should require authentication in this folder.

---

## Directory layout

Keep icons grouped by *meaning* (UI vs map vs branding), not by file type.

```text
web/public/icons/
├── README.md
├── ui/                 # (optional) generic UI icons (toolbar, buttons, status)
├── map/                # (optional) map symbology + markers used in the map UI
├── logos/              # (optional) brand marks (ONLY if explicitly permitted for public distribution)
└── manifest.json       # (recommended) provenance + license registry for non-KFM-original assets
```

> [!NOTE]
> Your repo may already use different category folders. That’s fine—just keep the same intent:
> **categorize**, **name consistently**, and **track provenance** for anything not created in-house.

---

## Naming conventions

| Goal | Convention | Example |
|---|---|---|
| Stable URLs | `kebab-case` filenames | `zoom-in.svg` |
| Category clarity | folder = category | `ui/zoom-in.svg` |
| Avoid collisions | prefix when needed | `map/marker-springfield.svg` |
| No spaces | use hyphens | ✅ `north-arrow.svg` / ❌ `North Arrow.svg` |
| No duplicates | one canonical file per glyph | don’t copy the same icon into multiple folders |

**Rule of thumb:** If you would import it as an identifier, name it like one.

---

## Supported formats

| Format | Use for | Notes |
|---|---|---|
| `.svg` | **default** for icons | scalable, themeable, usually smallest when optimized |
| `.png` | raster-only art / photorealistic assets | provide 1× and 2× if used across DPIs |
| `.ico` | legacy browser favicon use-cases | typically served from `/favicon.ico`, not `icons/` |

---

## Adding a new icon

### Definition of Done

- [ ] Confirm the icon is safe to publish (license + sensitivity).
- [ ] Prefer **SVG** unless raster is required.
- [ ] Optimize (remove editor metadata, simplify paths).
- [ ] Ensure SVG has a correct `viewBox`.
- [ ] Decide color strategy:
  - [ ] **Themeable**: use `currentColor` (recommended for UI glyphs)
  - [ ] **Fixed-color**: allowed when meaning depends on color (document why)
- [ ] Add/update `manifest.json` if:
  - [ ] third-party sourced, **or**
  - [ ] partner-provided, **or**
  - [ ] requires attribution / special terms
- [ ] Confirm the icon renders correctly at common sizes (16px / 24px / 32px).

---

## Provenance and licensing

If an asset is **not** KFM-original, record provenance. A lightweight registry keeps this folder governed and auditable.

### Recommended `manifest.json` shape

```json
{
  "icons": [
    {
      "id": "ui/zoom-in",
      "file": "ui/zoom-in.svg",
      "license": "CC-BY-4.0",
      "attribution": "Author Name",
      "source": "SOURCE_URL_OR_REFERENCE",
      "notes": "Any required credit text / restrictions / approval ticket ID."
    }
  ]
}
```

> [!IMPORTANT]
> If a logo/mark is not explicitly cleared for **public redistribution**, it should **not** live in `web/public/`.
> Store it in a controlled location and serve it through the governed boundary.

---

## Usage patterns

### Use as an image

```html
<img src="/icons/ui/zoom-in.svg" alt="Zoom in" width="16" height="16" />
```

### Use as a CSS background

```css
.button--zoom-in {
  background: url("/icons/ui/zoom-in.svg") no-repeat center / contain;
}
```

### Inline SVG

Inline SVG is appropriate when you need dynamic styling (hover, theme colors).

```html
<svg role="img" aria-label="Zoom in" width="1em" height="1em">
  <use href="/icons/sprite.svg#zoom-in"></use>
</svg>
```

<details>
<summary><strong>Optional: sprite workflow (single-file icon set)</strong></summary>

If your UI uses many small icons, an SVG sprite (a single `sprite.svg` containing `<symbol>` entries) can reduce network requests.

Document (in this README or a build README):
- how `sprite.svg` is generated,
- how IDs map to symbols,
- your cache-busting strategy for sprite updates.

</details>

---

## Accessibility

- Always provide text alternatives:
  - `<img alt="…">` when using `<img>`
  - `aria-label` (or a `<title>`) when using inline `<svg>`
- For icon-only buttons/controls:
  - add a visible label, **or**
  - add `aria-label` on the interactive element.

---

## Security

SVG is XML and can contain scripting or external references. Treat SVGs as **code**:

- No `<script>` blocks in SVG files.
- No external `href`/`xlink:href` references to untrusted domains.
- Avoid embedding remote fonts or images.
- If accepting third‑party SVGs, prefer a sanitizer/optimizer step in CI.

---

## Style consistency

- Validate at common sizes (16×16, 24×24).
- Align to pixel grid where possible (reduces blur).
- Keep stroke widths consistent within a category.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Icon looks cropped | missing/incorrect `viewBox` | add/repair `viewBox` to match artwork bounds |
| Icon is blurry | non-integer transforms / odd stroke alignment | snap to grid; simplify transforms |
| Wrong color | hard-coded fills | switch to `currentColor` or document why fixed colors are required |
| Icon doesn’t load | incorrect path | verify URL in browser: `/icons/...` |

---

## Governance reminder

If an icon change affects public-facing narratives (e.g., historically sensitive symbols), flag it for review before merge.