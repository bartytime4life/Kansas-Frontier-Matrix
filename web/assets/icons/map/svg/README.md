# 🗺️ Map SVG Icons (`web/assets/icons/map/svg`)

![Format](https://img.shields.io/badge/format-SVG-success)
![Scope](https://img.shields.io/badge/scope-Map%20UI-blue)
![Theming](https://img.shields.io/badge/theming-currentColor-informational)
![A11y](https://img.shields.io/badge/a11y-title%2Fdesc%20when%20semantic-orange)
![Provenance](https://img.shields.io/badge/provenance-required-red)

This folder is the **canonical home for map-related SVG icons** used across the KFM web UI (layers, legend, timeline, markers, tools, etc.). ✅  
Keep icons **consistent, themeable, accessible**, and (when sourced externally) **properly attributed**.

---

## 📁 Folder map

```text
📦 web
└─ 📁 assets
   └─ 📁 icons
      └─ 🗺️ 📁 map
         └─ 🧩 📁 svg
            ├─ 📄 README.md   👈 you are here
            ├─ 🖼️ pin.svg
            ├─ 🖼️ layers.svg
            └─ 🖼️ legend.svg
```

---

## ✅ Icon contract (the rules that keep things sane)

> [!IMPORTANT]
> **Every icon in this folder should follow these rules unless there’s a very good reason not to.**
>
> - **One icon = one file** (no multi-icon packs per SVG file).
> - **Use a `viewBox`** (icons must scale cleanly).
> - **No hard-coded UI colors** (prefer `currentColor` so dark/light themes “just work”).
> - **Keep geometry simple** (avoid unnecessary groups, transforms, filters).
> - **Strip editor metadata** (Sketch/Illustrator/Inkscape namespaces, empty `defs`, etc., unless truly needed).
> - **If an icon is third‑party**: include **source + license** in the SVG header comment (see below).

---

## 🎨 Design spec

### 1) Size & grid
- Default canvas: **24 × 24** with `viewBox="0 0 24 24"`.
- If you *must* use a different grid (e.g., a detailed legend glyph), document it in a short comment at the top of the SVG.

### 2) Stroke vs fill
Pick one of these styles per icon (mixing is OK when intentional):

**Line icon (recommended for UI controls):**
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
  <path d="..." stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

**Solid icon (recommended for markers / emphasis):**
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <path d="..." fill="currentColor"/>
</svg>
```

### 3) Two‑tone (optional, still “single color”)
If you need a subtle two-tone effect without creating a multi-color asset, you can structure the SVG so one path uses `currentColor` while others inherit `fill` from CSS (handy for hover/active states).

> [!TIP]
> Keep this subtle. Map UI benefits from calm, legible symbols.

---

## ♿ Accessibility (a11y) rules

### Decorative icons (most UI chrome)
If the icon is purely decorative, hide it from assistive tech:
```html
<svg class="kfm-icon" aria-hidden="true"><!-- ... --></svg>
```

### Meaningful icons (icons that *communicate*)
Use a `<title>` / `<desc>` + `aria-labelledby`:
```svg
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 24 24"
     role="img"
     aria-labelledby="iconTitle iconDesc">
  <title id="iconTitle">Layer list</title>
  <desc id="iconDesc">Opens the map layer control panel</desc>
  <path d="..." fill="currentColor"/>
</svg>
```

---

## 🧩 How to use these icons

<details>
<summary><strong>Option A — Inline SVG (max control ✅)</strong></summary>

Inline SVG gives you full control over CSS (including `currentColor` theming) and accessibility attributes.

```html
<button class="LayerToggle" type="button" aria-label="Toggle layers">
  <!-- inline svg here -->
</button>
```

**Pros:** themeable, animatable, accessible  
**Cons:** repeated markup if used many places

</details>

<details>
<summary><strong>Option B — SVG sprite via <code>&lt;use&gt;</code> (best for many icons 🚀)</strong></summary>

If your build pipeline creates (or you maintain) an external sprite (e.g., `defs.svg` / `sprite.svg`),
you can reference symbols without duplicating markup:

```html
<svg class="kfm-icon" aria-hidden="true">
  <use href="/assets/icons/map/defs.svg#icon-layer"></use>
</svg>
```

> [!NOTE]
> Some legacy setups use `xlink:href` instead of `href`. Prefer `href` unless you’re targeting older browsers.

**Pros:** caching-friendly, cleaner HTML  
**Cons:** requires sprite generation/maintenance

</details>

<details>
<summary><strong>Option C — <code>&lt;img&gt;</code> tag (simple ✅)</strong></summary>

```html
<img src="/assets/icons/map/svg/pin.svg" alt="" />
```

**Pros:** simplest  
**Cons:** limited styling from CSS (no `currentColor` control inside)

</details>

---

## 🧾 Provenance & licensing (non‑negotiable for third‑party icons)

If an icon is copied or derived from an external set, add a short header comment inside the SVG:

```svg
<!--
Source: Mapbox Maki (example)
License: (verify + record license)
Changes: simplified paths + matched 24px grid
-->
```

> [!IMPORTANT]
> If you can’t clearly state the license and origin, **don’t add the icon**.

---

## ✅ Adding a new icon checklist

- [ ] Named in **kebab-case** (`layer-stack.svg`, `timeline-play.svg`, `pin.svg`)
- [ ] Has `viewBox` (default `0 0 24 24`)
- [ ] No hard-coded colors (uses `currentColor` / CSS)
- [ ] Paths are simplified; no unnecessary `<g>` nesting or transforms
- [ ] Editor junk removed (extra namespaces, unused IDs, empty `defs`)
- [ ] Decorative vs semantic a11y considered (`aria-hidden` **or** `title/desc`)
- [ ] If third‑party: source + license comment added
- [ ] If used in a map layer legend/popup: icon meaning matches the legend label 🎯

---

## 🧰 Helpful tools

- 🧑‍🎨 Authoring: Illustrator, Sketch, Inkscape
- 🧼 Cleanup/Optimization: SVGO (or your preferred SVG optimizer)
- 🔍 QA: zoom-test at 100%, 125%, 150%, 200% (stroke icons can get weird fast)

---

## 🌍 Good sources for map symbol inspiration (verify licenses)

- Mapbox Maki
- OpenStreetMap icon sets
- OSGeo map symbol resources
- Public-domain / CC0 mapping icon collections

---

## 🧠 KFM UI note (map icons aren’t “just decoration”)

These icons often appear in **layer lists, legends, popups, and timeline controls**. When you add icons that represent *data layers*, make sure the UI around them still supports KFM’s provenance-first UX (legend text + source citation + inspectability).

---

*Last updated: keep this doc aligned with the project’s UI + provenance standards.* ✨