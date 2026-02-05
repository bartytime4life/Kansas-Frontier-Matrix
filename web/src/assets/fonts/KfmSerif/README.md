# KfmSerif ✒️🧭

![asset](https://img.shields.io/badge/asset-font-3B82F6)
![scope](https://img.shields.io/badge/scope-web%2Fui-22C55E)
![format](https://img.shields.io/badge/preferred-woff2-111827)
![contract](https://img.shields.io/badge/contract-font--family%3A%20KfmSerif-F59E0B)

> **KfmSerif** is the self-hosted **serif typeface** used by the Kansas Frontier Matrix (KFM) web UI.  
> This folder exists to keep typography **versioned, reproducible, and license-tracked** 📜✅

---

## 📦 What lives here?

**Path:** `web/src/assets/fonts/KfmSerif/`

```text
📁 web/
 └─ 📁 src/
    └─ 📁 assets/
       └─ 📁 fonts/
          └─ 📁 KfmSerif/
             ├─ 📄 README.md        👈 you are here
             ├─ 📄 LICENSE*         ✅ required (or OFL.txt / LICENSE.txt)
             ├─ 🔤 KfmSerif-*.woff2 ✅ preferred (web)
             ├─ 🔤 KfmSerif-*.woff  (optional fallback)
             └─ 🔤 KfmSerif-*.ttf   (optional / dev-only)
```

> [!IMPORTANT]
> **No license = no merge.** If we can’t prove redistribution rights, we don’t ship the font binaries. 🔒

---

## 🧩 How it’s used in the app

KFM’s frontend is web-based (React/TypeScript style stack). This folder is intentionally framework-agnostic: you can wire it up via plain CSS, a theme system, or a framework font loader.

```mermaid
flowchart LR
  A[🔤 Font files (.woff2)] --> B[📦 Build / bundler]
  B --> C[🧾 @font-face or framework loader]
  C --> D[🎛️ Design tokens / CSS vars]
  D --> E[🗺️ UI components + map labels]
```

---

## ✅ Asset contract (keep stable)

These are the **rules** that make the font predictable across the UI.

- **Canonical `font-family`:** `"KfmSerif"` (do not rename once released) 🧾
- **Preferred format:** `woff2` (small + fast) ⚡
- **Loading policy:** `font-display: swap` (avoid invisible text) 👀
- **Fallback stack:** `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif`

### 🧱 Recommended filename + weight map

Update this table to match the actual files in this folder.

| CSS `font-weight` | CSS `font-style` | Preferred file name |
|---:|---|---|
| 400 | normal | `KfmSerif-Regular.woff2` |
| 400 | italic | `KfmSerif-Italic.woff2` |
| 500 | normal | `KfmSerif-Medium.woff2` |
| 600 | normal | `KfmSerif-SemiBold.woff2` |
| 700 | normal | `KfmSerif-Bold.woff2` |
| 700 | italic | `KfmSerif-BoldItalic.woff2` |

> Tip 💡: keep names **consistent** and **case-stable** to avoid import bugs across OSes and CI.

---

## ⚡ Option A — Plain CSS (`@font-face`) (works everywhere)

Create or update a global stylesheet (example: `web/src/styles/fonts.css`) and import it once in your app entry.

<details>
<summary><strong>Example @font-face definitions</strong> (adjust filenames)</summary>

```css
/* ✅ Example — update filenames to match this folder */

@font-face {
  font-family: "KfmSerif";
  src:
    url("./KfmSerif-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "KfmSerif";
  src:
    url("./KfmSerif-Italic.woff2") format("woff2");
  font-weight: 400;
  font-style: italic;
  font-display: swap;
}

@font-face {
  font-family: "KfmSerif";
  src:
    url("./KfmSerif-Bold.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
```

</details>

### 🎛️ Recommended token (CSS variable)

```css
:root {
  --font-kfm-serif: "KfmSerif", ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
}

body {
  font-family: var(--font-kfm-serif);
}
```

---

## 🚀 Option B — Next.js local font (optional)

If the frontend is Next.js (App Router), you can use `next/font/local` for automatic optimization.

<details>
<summary><strong>Example (TypeScript)</strong></summary>

```ts
import localFont from "next/font/local";

export const kfmSerif = localFont({
  variable: "--font-kfm-serif",
  display: "swap",
  src: [
    { path: "../assets/fonts/KfmSerif/KfmSerif-Regular.woff2", weight: "400", style: "normal" },
    { path: "../assets/fonts/KfmSerif/KfmSerif-Italic.woff2", weight: "400", style: "italic" },
    { path: "../assets/fonts/KfmSerif/KfmSerif-Bold.woff2", weight: "700", style: "normal" },
  ],
});
```

```tsx
// app/layout.tsx
<html className={kfmSerif.variable}>
  <body>{/* ... */}</body>
</html>
```

</details>

---

## 🏎️ Performance notes

- Prefer **WOFF2** only unless you *must* support legacy browsers.
- Consider **subsetting** (Latin-only vs full Unicode) if files are large.
- Preload only the *most used* face (usually Regular 400).

```html
<!-- Example preload (path may vary by framework/build output) -->
<link
  rel="preload"
  as="font"
  type="font/woff2"
  href="/assets/fonts/KfmSerif/KfmSerif-Regular.woff2"
  crossorigin
/>
```

---

## 🔐 Provenance & licensing

Treat fonts like any other critical asset: **source, license, and rights must be auditable**.

### 🧬 Provenance record (fill this in)

| Field | Value |
|---|---|
| Typeface / Family | KfmSerif |
| Source | (vendor / foundry / internal build) |
| License type | (OFL / Apache / Commercial / Custom) |
| License file | `LICENSE` (or `OFL.txt`, `LICENSE.txt`) |
| Proof of rights | (invoice / email / contract reference) |
| Added by | @your-handle |
| Date added | YYYY-MM-DD |
| Modifications | none / subset / hinting / variable-font export |

> [!NOTE]
> If the font is **commercial**, confirm redistribution terms for: GitHub repo, CI artifacts, Docker images, and any public deployments.

---

## 🧪 Quick verification (developer sanity checks)

**In the browser console:**

```js
document.fonts.check("16px KfmSerif");
```

**In DevTools → Network:**
- confirm `.woff2` files are requested
- confirm HTTP status `200`
- confirm response header `Content-Type: font/woff2` (or equivalent)

---

## 🔧 Updating this folder (checklist)

- [ ] Add/replace `*.woff2` files (preferred)
- [ ] Keep the **`font-family` string** stable (`"KfmSerif"`)
- [ ] Update the **weight/style table**
- [ ] Ensure a **license file exists** and matches the font binaries
- [ ] Validate in at least **Chrome + Firefox**
- [ ] Run the normal lint/build pipeline

---

## 🗺️ Notes for map UI

Typography is a **map symbol**—use weight/style changes intentionally for hierarchy (labels, headings, story nodes). 🧭🗺️  
Keep variations meaningful and consistent across the UI.
