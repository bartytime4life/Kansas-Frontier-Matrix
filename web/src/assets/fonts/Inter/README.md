<!--
📍 Path: web/src/assets/fonts/Inter/README.md
🎯 Purpose: Single source of truth for Inter font binaries used by the Web UI
-->

# Inter — UI Font Assets ✨

> **Local Inter font files** for the KFM web frontend (kept in-repo for consistency, reproducible builds, and offline-friendly dev). 🌐

---

## 🧾 Quick Facts

| Item | Value |
|------|-------|
| 🧩 Font family | **Inter** |
| 📦 Preferred format | **WOFF2** (web-optimized) |
| 🎛️ Recommended type | **Variable fonts** (one file covers many weights) |
| 🪪 License | **SIL Open Font License (OFL-1.1)** *(keep license text in this folder)* |
| 🎯 Scope | UI typography (not map glyph pipelines) |

> [!IMPORTANT]
> Fonts are **third‑party binaries**. Treat them like dependencies: keep **version + provenance + license** next to the files. 🧾✅

---

## 🗂️ Expected Folder Contents

This folder is intentionally small and self-contained.

```text
📁 web/src/assets/fonts/Inter/
├── 📄 README.md
├── 📄 LICENSE_OFL.txt            # required (or OFL.txt / LICENSE.txt)
├── 📄 VERSION.txt                # recommended (e.g., "Inter vX.Y")
├── 📄 SOURCE.txt                 # recommended (where we got it + release/tag)
├── 📄 CHECKSUMS.sha256           # recommended (integrity + supply-chain sanity)
├── 🧩 Inter-roman.var.woff2       # recommended (variable, normal)
└── 🧩 Inter-italic.var.woff2      # recommended (variable, italic)
```

> [!NOTE]
> If you don’t use variable fonts, store only the weights you actually use (e.g., Regular/Medium/SemiBold/Bold) as `.woff2` to keep bundle size down. 📉

---

## 🎨 How the UI should load Inter

### Option A — Keep font-face next to the binaries ✅ (recommended)

1) Create a small CSS file **inside this folder** (keeps paths simple):

**`web/src/assets/fonts/Inter/inter.css`**
```css
/* Inter — variable fonts (recommended) */
@font-face {
  font-family: "Inter";
  font-style: normal;
  font-weight: 100 900;          /* variable range */
  font-display: swap;
  src: url("./Inter-roman.var.woff2") format("woff2");
}

@font-face {
  font-family: "Inter";
  font-style: italic;
  font-weight: 100 900;          /* variable range */
  font-display: swap;
  src: url("./Inter-italic.var.woff2") format("woff2");
}
```

2) Import it once near your app entry (example paths — match your actual entry file):

```ts
// web/src/main.tsx OR web/src/index.tsx
import "./assets/fonts/Inter/inter.css";
```

3) Use it via a global font stack (example):

```css
:root {
  --font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
}

body {
  font-family: var(--font-sans);
}
```

---

### Option B — Centralized typography file (also fine)

If your project already has a single canonical typography entry (e.g., `src/styles/typography.css`), move only the `@font-face` blocks there and reference the font files via a relative path.

> [!TIP]
> Keep `@font-face` declarations in **global CSS** (not CSS Modules) so they load once and don’t depend on component import order. 🧠

---

## 🧬 Provenance & Integrity (don’t skip) 🛡️

When adding/updating font files:

- **Record version** in `VERSION.txt`
- **Record source** in `SOURCE.txt` (where you downloaded it, release tag, date)
- **Include license text** in `LICENSE_OFL.txt` (or equivalent)
- **Generate checksums** in `CHECKSUMS.sha256` (helps detect accidental corruption)

<details>
  <summary>🔧 Optional: Generate SHA256 checksums</summary>

```bash
# Run from this folder:
# web/src/assets/fonts/Inter
sha256sum *.woff2 > CHECKSUMS.sha256
```
</details>

---

## 🔁 Updating Inter (safe checklist) ✅

- [ ] Download Inter from the **official upstream release**
- [ ] Prefer **WOFF2 variable** fonts where possible
- [ ] Keep filenames stable (or update the `@font-face` paths accordingly)
- [ ] Update `VERSION.txt`
- [ ] Update `SOURCE.txt`
- [ ] Update `CHECKSUMS.sha256`
- [ ] Ensure **normal + italic** are both present (if your UI uses italic anywhere)
- [ ] Smoke test typography in the UI (headers, body, buttons, tables)

---

## 🚫 Common Footguns (avoid these) 🧨

- ❌ Mixing multiple Inter versions across the app (subtle layout shifts)
- ❌ Shipping `.ttf/.otf` to production instead of `.woff2` (bigger + slower)
- ❌ Missing italic face → browser fakes it (looks “slanted” and low quality)
- ❌ Over-including weights you don’t use (bundle bloat)
- ❌ Forgetting `font-display: swap` (risk of FOIT / invisible text)

---

## 🧯 Troubleshooting

**Text is using a fallback font**
- Confirm the `@font-face` file paths resolve (check devtools Network tab for 404s).
- Confirm the CSS containing `@font-face` is imported **once** at startup.

**Bold/weights don’t look right**
- If using variable fonts: make sure `font-weight: 100 900;` is set on the face.
- If using static fonts: confirm you included the exact weight files you reference.

**Italic looks “fake”**
- Ensure an italic `@font-face` exists and points at an italic font file.

---

## 🧠 Tiny Reference Diagram

```mermaid
flowchart LR
  A[🧩 Inter .woff2 files<br/>web/src/assets/fonts/Inter] --> B[🎛️ @font-face declarations<br/>(global CSS)]
  B --> C[🎨 Typography tokens / CSS vars]
  C --> D[⚛️ React UI components]
```
