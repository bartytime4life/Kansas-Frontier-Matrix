# 🎛️ UI Icons for KFM Web

![Asset Type](https://img.shields.io/badge/asset-ui%20icons-blue)
![Preferred Format](https://img.shields.io/badge/format-SVG-informational)
![A11y](https://img.shields.io/badge/a11y-ARIA%20friendly-success)
![Principle](https://img.shields.io/badge/principle-provenance--first-purple)

> 📍 **Location:** `web/assets/media/icons/ui/`  
> 🎯 **Purpose:** Small, reusable icons for **KFM’s Web UI controls** (layer panel, search, timeline, popups, settings, etc.). [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧭 What belongs in this folder

✅ **Put UI control icons here**, like:
- Navigation & panels: `close`, `menu`, `chevron-left/right`, `expand`, `collapse`
- Map UI controls: `zoom-in/out`, `locate`, `reset-view`, `fullscreen`
- Discovery: `search`, `filter`, `sort`, `layers`, `legend`, `info`
- Editing/ops: `edit`, `save`, `download`, `share`, `copy`, `delete`
- Status: `warning`, `error`, `success`, `loading`, `locked`, `restricted`

❌ **Do not put these here**
- Map symbology / markers tied to datasets (those belong in a **map/symbology** area, not UI controls)
- Brand marks / logos
- Large illustrations, photos, hero images
- Anything with unclear licensing or missing source info (see Provenance)

---

## 📁 Folder layout

```text
📁 web/
  📁 assets/
    📁 media/
      📁 icons/
        📁 ui/
          📄 README.md          ← you are here
          🖼️ *.svg              ← UI icons (preferred)
          🧩 ui.sprite.svg      ← optional generated sprite (recommended)
          🧾 ui.icons.manifest.*← optional provenance manifest (recommended)
```

> [!NOTE]
> The KFM technical docs explicitly call out `assets/` as the home for static assets like **icons/images**, and emphasize a **responsive + accessible** web UI with standard UI elements (layer list, search, legends, timeline, info panels). [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧱 Naming conventions

Keep names predictable and diff-friendly:

- **kebab-case** only: `zoom-in.svg`, not `ZoomIn.svg`
- Avoid ambiguous names like `icon1.svg`
- Prefer **semantic names** over visual ones:
  - ✅ `layers.svg` (meaning)  
  - ❌ `stack.svg` (looks like)

### Suggested prefixes
Use prefixes only when it prevents collisions:

- `nav-` → navigation/panels (`nav-close.svg`, `nav-chevron-left.svg`)
- `map-` → map UI controls (`map-zoom-in.svg`, `map-locate.svg`)
- `status-` → feedback states (`status-warning.svg`, `status-success.svg`)
- `action-` → actions (`action-download.svg`, `action-share.svg`)

---

## 🎨 SVG design standards

> [!IMPORTANT]
> Consistency matters more than “perfect art.” Icons are UI language.

### Recommended geometry
- **Default viewBox:** `0 0 24 24` (most UI libraries assume this)
- Keep stroke widths consistent across the pack
- Avoid micro-details that vanish at 16–20px sizes
- Use simple paths whenever possible (smaller files, faster rendering)

### Color rules
- Prefer **theme-driven** color:
  - Use `fill="currentColor"` or `stroke="currentColor"` so icons inherit CSS color.
  - Two-tone is allowed if it still inherits from parent color rules (see usage section). [oai_citation:2‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

### SVG hygiene
- **Always include a viewBox** (scales correctly across responsive UI). [oai_citation:3‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
- Strip editor metadata/namespaces when exporting (e.g., Sketch namespaces) to reduce size. [oai_citation:4‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
- Remove empty `<defs>` unless you actually need it. [oai_citation:5‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

---

## ♿ Accessibility rules

### Decorative icons
If the icon is purely decorative (e.g., a chevron next to a label):
- `<img alt="" aria-hidden="true">`  
- or inline `<svg aria-hidden="true" focusable="false">`

### Meaningful icons
If the icon conveys meaning without text (e.g., “warning”, “locked”, “download”):
- Provide an accessible name:
  - Use `<title>` and (optionally) `<desc>` inside SVG for screen readers. [oai_citation:6‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
  - Or label the button element (`aria-label="Download"`), and keep SVG hidden.

> [!TIP]
> If the UI already has visible text (“Download”), keep the icon decorative. Less noise for screen readers ✅

---

## 🧾 Provenance and licensing

KFM’s core ethos is **provenance-first** and careful license handling, because it “avoids legal pitfalls and fosters collaboration.” [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Rules for icons
- Every icon **must** have a known source:
  - ✅ Original KFM design
  - ✅ Third-party with a compatible license and attribution
  - ❌ Unknown origin / copied from random sites

### Recommended manifest
Add a simple manifest when this icon set grows (or if any icon is third-party):

Example `ui.icons.manifest.yml`:
```yaml
version: 1
icons:
  - file: nav-close.svg
    source: "KFM original"
    license: "Project license"
    author: "KFM"
    notes: "24x24, stroke=2, currentColor"
  - file: map-locate.svg
    source: "Vendor pack name / URL"
    license: "License type"
    attribution: "Required attribution text"
    modified: true
    notes: "Simplified paths; removed editor metadata"
```

This mirrors KFM’s general standards: **provenance first** and **validation gates** that reject missing provenance/citations in governed content. [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ⚡ Optimization

> [!TIP]
> SVGs ship to every user. Optimize early, avoid death by 1,000 icons.

### Quick checklist
- Remove unused groups, transforms, masks
- Minimize path count
- Remove inline hard-coded fills/strokes unless absolutely required
- Keep file sizes small (aim for “tiny”, but don’t over-optimize readability for contributors)

### Suggested tooling
- `svgo` (recommended)
- Optional: pre-commit hook to auto-optimize changed SVGs

---

## 🧩 Usage patterns

### Option A: External SVG sprite
Best for performance + caching:
```html
<svg class="Icon" aria-hidden="true" focusable="false">
  <use href="/assets/media/icons/ui/ui.sprite.svg#icon-search"></use>
</svg>
```

Why:
- External sprite files can be cached by the browser while still enabling `<use>` references. [oai_citation:9‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

> [!NOTE]
> If your build system already bundles assets, keep the sprite generation inside the build pipeline so it stays deterministic and repeatable (aligned with KFM’s “deterministic pipeline” mindset). [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### Option B: Inline SVG in components
Best for dynamic styling and straightforward a11y control:
```html
<button type="button" aria-label="Close">
  <svg class="Icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
    <!-- paths here -->
  </svg>
</button>
```

### Option C: `<img>` tag
Use for purely decorative icons or when inline/svg sprite isn’t available:
```html
<img src="/assets/media/icons/ui/action-download.svg" alt="" aria-hidden="true">
```

---

## 🛠️ Adding a new icon

1. **Design** on a consistent grid (prefer 24×24).
2. **Export** as SVG with a proper `viewBox` (avoid hardcoded width/height unless required). [oai_citation:11‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
3. Normalize to `currentColor` (fill or stroke) so themes work cleanly. [oai_citation:12‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
4. Strip editor namespaces/metadata during optimization (e.g., Sketch namespaces). [oai_citation:13‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
5. Name the file using the naming rules above.
6. If using a manifest/sprite:
   - Add the icon to `ui.icons.manifest.*`
   - Rebuild `ui.sprite.svg` (or let CI do it)
7. **Validate** in the UI at typical icon sizes (16/20/24px) and with theme colors.

---

## ✅ Definition of done for a UI icon

- [ ] Icon renders correctly at 16/20/24px
- [ ] Has `viewBox` and scales predictably [oai_citation:14‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
- [ ] Uses `currentColor` unless explicitly justified [oai_citation:15‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
- [ ] No editor junk (namespaces, unused defs) [oai_citation:16‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
- [ ] Accessibility is handled (decorative vs meaningful)
- [ ] Provenance/license is recorded (manifest or documented)
- [ ] Validation steps are repeatable and documented (project-wide doc standard) [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗺️ UI surfaces these icons commonly support

KFM’s web UI includes standard surfaces like:
- 📚 Layer catalog/list (toggle layers, adjust settings)
- 🔎 Search bar
- 🧾 Legends (map symbology explanations)
- 🕒 Timeline slider for temporal navigation
- 🪟 Popups / side panels for feature details [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Keep icons legible and consistent across these contexts.

---

## 📚 References

- **KFM Web UI & assets structure:** `assets/` contains static assets (icons/images) and the UI targets responsive + accessible design. [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **KFM licensing discipline:** careful license handling supports adoption and collaboration. [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Repo standards (provenance & gates):** provenance-first + validation gates are core invariants. [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **SVG practicals:** viewBox scaling, removing namespaces, and using `<title>/<desc>` for accessibility. [oai_citation:22‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
- **`currentColor` + external sprite caching:** enables theme inheritance and browser caching for icon defs. [oai_citation:23‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
