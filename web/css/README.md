# Kansas-Frontier-Matrix — CSS Layering

This folder contains the **styling system** for the web viewer (`web/`).  
The CSS is **split into layers** so structure, theming, and overrides remain modular.

---

## Files

- **`layout.css`**  
  Core **layout & UI structure**.  
  Defines the grid (toolbar, sidebar, map), component shells (cards, toggles, sliders, timeline), and responsive/mobile rules.  
  - Treat this file as the “skeleton” of the web app.
  - Safe to extend with new components if they are structural.

- **`theme.css`**  
  **Skinning layer**.  
  Defines color palettes, typography, shadows, radii, and utility classes.  
  - Import after `layout.css`.
  - Supports light/dark via `prefers-color-scheme`.
  - Easy to reskin the whole app without touching layout.

- *(optional future)* `theme-alt.css`  
  Alternative themes (e.g., sepia / parchment for archival maps).

---

## Usage Order

Always include **`layout.css` first**, then **`theme.css`**:

```html
<link rel="stylesheet" href="css/layout.css">
<link rel="stylesheet" href="css/theme.css">
````

---

## Design Tokens

Both files rely on **CSS custom properties** (`--var-name`) at the `:root` level.
Examples:

* `--bg`, `--panel`, `--ink` → background & text layers
* `--accent`, `--accent-2` → highlight colors
* `--radius`, `--shadow-1` → radii & elevation
* `--font`, `--mono` → typography stacks

Changing these in `theme.css` propagates across the app.

---

## Responsiveness

* **Desktop:** Sidebar docked on the left.
* **Mobile (≤1024px):** Sidebar collapses into a drawer (`.is-open` class toggled by JS).
* Timeline and overlays reposition to edges for smaller screens.

---

## Accessibility

* **Focus rings**: `:focus-visible` outlines use `--focus`.
* **Reduced motion**: `prefers-reduced-motion: reduce` disables transitions.
* **High contrast**: `forced-colors: active` swaps system colors.
* **Print mode**: Hides UI chrome (sidebar, toolbar, timeline).

---

## Contribution Guidelines

* Add **new structural rules** to `layout.css`.
* Add **color, typography, or visual style rules** to `theme.css`.
* Use **tokens** instead of hard-coded colors/sizes wherever possible.
* Test in both **light** and **dark** system modes.
* Keep sidebar/mobile drawer behavior consistent with JS (`.is-open`).

---

## Quick Reference

| File         | Role           | Safe to edit?                   |
| ------------ | -------------- | ------------------------------- |
| `layout.css` | Structure & UI | Only for new layout/structure   |
| `theme.css`  | Colors & style | Yes (preferred place for edits) |

---

🚀 This modular CSS system makes it easy to scale, reskin, and maintain the Kansas-Frontier-Matrix viewer.

```
