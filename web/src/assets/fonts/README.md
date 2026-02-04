# 🔤 Fonts & Typography (KFM Web UI)

Welcome to `web/src/assets/fonts/` — the **single home** for self-hosted web fonts used by the KFM web front-end.

> 🧠 Rule of thumb: **If it affects how text looks in the UI, it belongs here.**  
> If it affects **map label glyphs**, that’s typically configured via map style/glyph pipelines (not CSS fonts).

---

## 🗺️ What this folder is for

KFM’s web UI is map-centric (2D + 3D), so typography needs to remain readable across panels, overlays, legends, search, and narrative/story UI.

This folder supports:
- ✅ UI typography (React components, dashboards, story panels, toolbars, modals)
- ✅ Consistent branding + design tokens (font stacks, weights, sizes)
- ✅ Offline-friendly / self-hosted fonts (when desired)

This folder is **not** intended to be:
- ❌ A dumping ground for random `.ttf` files
- ❌ A place to store unlicensed/proprietary fonts without permission
- ❌ The source of truth for map label glyphs (that’s a separate concern)

---

## 📁 Recommended structure

Keep fonts organized **by family**, then by weight/style. Each family gets its own mini “provenance bundle”.

```text
📁 web/
  📁 src/
    📁 assets/
      📁 fonts/
        📝 README.md  👈 you are here
        📄 fonts.css  (optional but recommended)
        📁 Inter/
          🔤 Inter-Regular.woff2
          🔤 Inter-Italic.woff2
          🔤 Inter-SemiBold.woff2
          📄 LICENSE.txt
          📝 SOURCE.md
        📁 KfmSerif/
          🔤 KfmSerif-Regular.woff2
          📄 LICENSE.txt
          📝 SOURCE.md
```

### 🏷️ Naming conventions
- **Family folder:** `Inter/`, `KfmSerif/`, `KfmMono/`
- **Files:** `Family-WeightStyle.woff2`  
  Examples: `Inter-Regular.woff2`, `Inter-SemiBoldItalic.woff2`
- Prefer: **WOFF2 first**, optionally include **WOFF fallback** if needed.

---

## ✅ Principles (the “KFM way”)

### 1) 🧾 Provenance-first
Every font family **must** include:
- `LICENSE.txt` (or equivalent license file)
- `SOURCE.md` with:
  - where it came from (vendor / foundry / repo)
  - version (if known)
  - any special attribution requirements

### 2) ⚡ Performance matters
- Prefer **WOFF2**
- Ship **only the weights you use**
- Consider subsetting later (if/when needed)

### 3) 🎛️ Use tokens, not hardcoded fonts everywhere
Centralize font usage with CSS variables so components stay consistent.

### 4) ♿ Accessibility & hierarchy
Typography should be planned, not random:
- clear heading levels
- sane line-height
- readable defaults for dense data + map UI

---

## 🧠 Font strategy options

### Option A — System / “web-safe” stacks (fastest + zero licensing headaches)
This is your baseline fallback stack and should **always** exist as a safety net.

Example stack pattern:
- Sans UI: `system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif`
- Serif: `Georgia, "Times New Roman", Times, serif`
- Mono: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Courier New", monospace`

### Option B — Self-hosted web fonts via `@font-face` (recommended for consistency)
Use `@font-face` to register local font files, then reference them in `font-family`.

> ⚠️ Self-hosting fonts still requires correct licensing.

### Option C — Hosted fonts (only if online dependency is acceptable)
If you use a hosted provider (ex: via `<link>` in HTML), document it clearly and consider offline implications.

---

## 🛠️ Adding a new font (checklist)

### Step 1 — Drop font files into a family folder
- Put fonts in `web/src/assets/fonts/<FamilyName>/`
- Prefer `.woff2`

### Step 2 — Add provenance files
Inside the family folder:
- ✅ `LICENSE.txt`
- ✅ `SOURCE.md`

### Step 3 — Register the font in CSS (`fonts.css`)
Create (or update) `web/src/assets/fonts/fonts.css`:

```css
/* web/src/assets/fonts/fonts.css */

@font-face {
  font-family: "KFM Sans";
  src:
    url("./KfmSans/KfmSans-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "KFM Sans";
  src:
    url("./KfmSans/KfmSans-SemiBold.woff2") format("woff2");
  font-weight: 600;
  font-style: normal;
  font-display: swap;
}
```

> 💡 Tip: `font-display: swap;` is a pragmatic default for UI apps.

### Step 4 — Expose a font token
Put this somewhere global (example: `web/src/styles/typography.css` or equivalent):

```css
:root {
  --font-sans: "KFM Sans", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
  --font-serif: "KFM Serif", Georgia, "Times New Roman", Times, serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Courier New", monospace;
}

body {
  font-family: var(--font-sans);
}
```

### Step 5 — Import the font CSS once (global entry)
Import it at the app entry point (one-time):

```ts
// e.g., web/src/main.tsx or web/src/index.tsx
import "./assets/fonts/fonts.css";
```

---

## 📏 A simple typography scale (starter)

Don’t overthink it, but don’t freestyle it either. A consistent hierarchy helps the UI feel coherent.

Starter approach:
- Body: `1rem` with a comfortable line-height
- Headings: use a small set of stepped sizes (H1 > H2 > H3 > H4)

Example token idea:

```css
:root {
  --text-body: 1rem;
  --text-small: 0.875rem;

  --text-h1: 1.75rem;
  --text-h2: 1.375rem;
  --text-h3: 1.125rem;
  --text-h4: 1rem;

  --leading-body: 1.5;
}
```

---

## 🚀 Performance tips (optional, but useful)

### ✅ Preload the “first paint” font weights (only if you’re sure of build output paths)
If your bundler/build setup supports it, preload the most-used WOFF2 file(s):

```html
<link
  rel="preload"
  as="font"
  type="font/woff2"
  href="/assets/fonts/KfmSans/KfmSans-Regular.woff2"
  crossorigin
/>
```

> ⚠️ This path is build-tool dependent — verify it in DevTools ➜ Network.

---

## 🧯 Troubleshooting

- **Font not applying**
  - Check `font-family` string matches exactly
  - Confirm the `@font-face` rule is loaded (DevTools ➜ Sources)

- **Wrong weight shows**
  - Ensure `font-weight` in `@font-face` matches the CSS usage (`400`, `600`, etc.)

- **404 on font file**
  - Verify relative paths inside `fonts.css`
  - Confirm bundler is configured to load `woff2` assets

---

## ✅ PR checklist (fonts)

- [ ] Only required weights/styles are added (no “full family” dumps)
- [ ] `.woff2` is included (preferred)
- [ ] `LICENSE.txt` is present
- [ ] `SOURCE.md` is present and complete
- [ ] Font registered in `fonts.css` (or documented alternate loading)
- [ ] UI verified in DevTools (no 404s, expected weight renders)

---

## 🧩 Future upgrades (nice-to-haves)
- ✂️ Font subsetting (reduce file size)
- 🧪 Visual regression checks for typography
- 🎛️ Theme support (dark mode readability + contrast tuning)