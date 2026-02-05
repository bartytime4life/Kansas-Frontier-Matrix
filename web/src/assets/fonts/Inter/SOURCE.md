# Inter Font Source 📦✨

![Font Family](https://img.shields.io/badge/Font-Inter-111827?style=flat&labelColor=0b1220)
![Formats](https://img.shields.io/badge/Formats-WOFF2%20%7C%20(optional%20WOFF)-2563eb?style=flat&labelColor=0b1220)
![Usage](https://img.shields.io/badge/Usage-Web%20UI%20Typography-16a34a?style=flat&labelColor=0b1220)
![License](https://img.shields.io/badge/License-OFL--1.1-blue?style=flat&labelColor=0b1220)

> This folder vendors the **Inter** typeface for the **Kansas Frontier Matrix** web UI so builds are consistent and self-contained ✅

---

## 📁 Folder Location

**Path:** `web/src/assets/fonts/Inter/`

```text
web/
└─ src/
   └─ assets/
      └─ fonts/
         └─ Inter/
            ├─ (font files live here)  🧠
            ├─ LICENSE*               ⚖️
            └─ SOURCE.md              👈 you are here
```

---

## 🧾 Upstream Source

- **Name:** Inter
- **Designer:** Rasmus Andersson
- **Primary upstream:** https://rsms.me/inter/
- **Upstream repository:** https://github.com/rsms/inter

> If you update fonts in this folder, always record the upstream version/tag and checksums below 🧷

---

## ✅ Why we vendor the font (instead of fetching at runtime)

- **Offline-friendly builds** (no external font dependency) 🚫🌐  
- **Performance control** (WOFF2, caching, `font-display`) ⚡  
- **Consistent branding & UI rhythm** across environments 🎯  
- **Easier theming via design tokens** (e.g., one `--font-sans` variable) 🎨

---

## 🔐 License & Attribution

Inter is commonly distributed under the **SIL Open Font License (OFL) 1.1**.

**Rules of thumb (keep it safe & boring):**
- Keep the **license file** shipped alongside the font files 🧾
- Don’t self-host fonts you aren’t licensed to host ⚠️
- If fonts are modified, follow OFL naming constraints (Reserved Font Name rules may apply)

📌 See the `LICENSE*` file in this folder.

---

## 📦 Included Assets

> Update this table to match what is **actually** in `web/src/assets/fonts/Inter/`.

| File | Style | Weight(s) | Format | Notes |
|---|---|---:|---|---|
| `Inter-Variable.woff2` | Normal | 100–900 | WOFF2 | Variable font (recommended) |
| `Inter-Italic-Variable.woff2` | Italic | 100–900 | WOFF2 | Use for true italic (avoid synthetic italics) |
| `Inter-Regular.woff2` | Normal | 400 | WOFF2 | *(Optional static)* |
| `Inter-Bold.woff2` | Normal | 700 | WOFF2 | *(Optional static)* |

---

## 🧩 How the app should use Inter

### 1) CSS `@font-face` (recommended) 🎛️

```css
/* Example: web/src/styles/fonts.css */

@font-face {
  font-family: "Inter";
  src: url("/src/assets/fonts/Inter/Inter-Variable.woff2") format("woff2");
  font-style: normal;
  font-weight: 100 900;
  font-display: swap;
}

@font-face {
  font-family: "Inter";
  src: url("/src/assets/fonts/Inter/Inter-Italic-Variable.woff2") format("woff2");
  font-style: italic;
  font-weight: 100 900;
  font-display: swap;
}

/* Design token (recommended) */
:root {
  --font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
}

body {
  font-family: var(--font-sans);
}
```

### 2) Optional preload (for LCP-heavy pages) 🚀

```html
<!-- Example: in your app shell (adjust paths to match your bundler) -->
<link
  rel="preload"
  href="/src/assets/fonts/Inter/Inter-Variable.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
```

### 3) Practical guardrails 🧠

- Prefer **WOFF2** first. Add **WOFF** only if you truly need older browser support.
- Use **real italic** files. Don’t rely on browser “fake italic”.
- Be deliberate with **font sizing units** (px/em/%). Consider:
  - browser vs print needs
  - expected OS/browser mix
  - whether users should be able to resize fonts easily

---

## 🔄 How to Update Inter (repeatable checklist)

1. Choose an upstream **release tag/version**.
2. Download the desired assets (variable fonts recommended).
3. Replace the font files in this folder.
4. Update the **Version & Integrity** section.
5. Run a quick UI sanity check:
   - headings, body text, buttons, map labels
   - dark mode / light mode readability
   - italics + bold rendering

### 🧾 Version & Integrity

- **Upstream version/tag:** `TBD`
- **Pulled on (YYYY-MM-DD):** `TBD`
- **Source URL:** `TBD (release page or commit reference)`
- **Checksums:**
  - `Inter-Variable.woff2` → `sha256: TBD`
  - `Inter-Italic-Variable.woff2` → `sha256: TBD`

Generate checksums:

```bash
# from repo root
sha256sum web/src/assets/fonts/Inter/*.woff2
```

---

## 🧪 Troubleshooting

- **Font not loading?**  
  - Confirm the path you use in `url(...)` matches how your bundler serves static assets.
  - Check for `crossorigin` needs when using `preload`.
  - Ensure your `@font-face` is loaded before components render (import order matters).

- **Italic looks “fake”?**  
  - Verify you’ve included an italic face and set `font-style: italic` correctly.

---

## 📚 Project References

These internal library sources informed the conventions used here (embedding web fonts, licensing awareness, and font sizing considerations):

- *Learn to Code HTML & CSS: Develop & Style Websites* — Shay Howe (New Riders, 2014)
- *Professional Web Design: Techniques and Templates* — Clint Eccher (Cengage, 2015)
