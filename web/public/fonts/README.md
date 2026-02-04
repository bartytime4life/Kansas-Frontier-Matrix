# 🆎 `web/public/fonts` — Fonts & Typography Assets

![Static Assets](https://img.shields.io/badge/assets-static-blue)
![Format](https://img.shields.io/badge/fonts-WOFF2%20first-success)
![Performance](https://img.shields.io/badge/perf-weights%20minimized-orange)
![Governance](https://img.shields.io/badge/KFM-provenance%E2%80%91first-purple)

This folder contains **self-hosted web font files** served directly by the KFM web app (the `public/` tree).  
It exists because some front-end libraries and CSS conventions expect fonts to be resolvable via a predictable `/fonts/...` path (and often via relative paths like `../fonts`). [oai_citation:0‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

> 🧭 **KFM rule of thumb:** _No license, no font._  
> KFM is “provenance-first” and built around traceable sources (“the map behind the map”). That mindset applies to UI assets too—especially fonts. [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📦 What belongs here

- ✅ `.woff2` (preferred), `.woff` (fallback) font files  
- ✅ Variable fonts (recommended when available)
- ✅ Font licenses (`LICENSE.*`) and provenance notes (`SOURCE.md` / `README.md`)
- ✅ Small font metadata manifests (optional but encouraged)

Fonts are **files** that contain a typeface (design). Typeface and font are often confused, but they are not the same thing. [oai_citation:2‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)

---

## 🗂️ Recommended folder structure

> Keep it boring + predictable. This makes caching, CDN behavior, and debugging much easier.

```text
web/
  public/
    fonts/                      👈 you are here
      README.md
      <family-name>/            (optional but recommended)
        LICENSE.txt
        SOURCE.md               (where it came from + link + version)
        <family>-<axis>.woff2   (variable) or <family>-<weight>.woff2
```

---

## 🚀 Quick start: add a new font family

### 1) Drop the files
Put the `.woff2` (and optional `.woff`) inside `web/public/fonts/<family-name>/`.

### 2) Add licensing + provenance
Before you reference the font in CSS, ensure:
- a license file is present (e.g., `LICENSE.txt`)
- you have rights to self-host (or you’re using a clearly permissive source)

Embedding fonts is easy technically—but **licensing still applies**; uploading font files to your server can enable unauthorized reuse if you don’t have permission. [oai_citation:3‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)

### 3) Register it in CSS (`@font-face`)
Web fonts are typically included via `@font-face`, which sets a `font-family` name and a `src` path to the font file(s). [oai_citation:4‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)

Example (create/update something like `web/src/styles/fonts.css` or `_fonts.scss`):

```css
/* Example: Self-hosted font */
@font-face {
  font-family: "KFM Sans";
  src:
    local("KFM Sans"),
    url("/fonts/kfm-sans/kfm-sans.woff2") format("woff2");
  font-weight: 100 900; /* variable fonts often support ranges */
  font-style: normal;
  font-display: swap;
}

/* Use it */
:root {
  --font-ui: "KFM Sans", system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
}
body {
  font-family: var(--font-ui);
}
```

> 💡 If you use `public/`, the font URL is typically absolute-from-site-root (e.g., `/fonts/...`).  
> In many web app layouts, `public/index.html` is the “centerpiece” that loads the app’s assets, so anything in `public/` is expected to be web-addressable. [oai_citation:5‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

---

## ⚖️ Self-hosting vs Google Fonts

If you’re experimenting, Google Fonts can be integrated quickly (either via `<link>` in `<head>` or `@import`). [oai_citation:6‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444) [oai_citation:7‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

However:
- self-hosting improves long-term stability and reduces third-party dependency risk
- **only select the weights/styles you actually use**; more selections increase download time (Google even warns about this). [oai_citation:8‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

> ✅ KFM preference: self-host when possible, with explicit licensing + provenance notes (aligned with KFM’s governance model). [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🎛️ Typography guidance (practical)

Typography works best with a **clear hierarchy** and consistent scaling. A common approach is to define a base size and scale headings using percentages/relative sizing so the system is coherent across the UI. [oai_citation:10‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda) [oai_citation:11‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)

A simple hierarchy example (illustrative):

```css
:root {
  --font-size-base: 16px;
  --line-height-base: 1.5;
}

body {
  font-size: var(--font-size-base);
  line-height: var(--line-height-base);
}

h1 { font-size: 2.2em; }
h2 { font-size: 1.6em; }
h3 { font-size: 1.35em; }
```

---

## ⚡ Performance checklist

- ✅ Prefer **WOFF2** first
- ✅ Use **variable fonts** to reduce file count (when it doesn’t bloat size)
- ✅ Limit weights (e.g., 400 + 600) unless you truly need more [oai_citation:12‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)
- ✅ Set `font-display: swap` (avoid invisible text)
- ✅ Consider subsetting for large fonts (e.g., Latin-only subsets if appropriate)
- ✅ Cache aggressively (long-lived cache headers) once versions are fingerprinted

---

## 🧾 Governance & provenance

KFM emphasizes traceability and responsible reuse (FAIR/CARE) across the system. [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
For fonts, that means every family should ideally have:

- `LICENSE.*` — the actual license text
- `SOURCE.md` — where you got it (vendor/site), version, and any build steps (subsetting, axis pinning, etc.)
- (Optional) `FONTLOG.txt` — if provided by the font author

### Suggested `SOURCE.md` template

```md
# Source / Provenance

- Font family:
- Source URL:
- Retrieved on:
- License:
- Modifications:
  - [ ] Subset (characters/ranges)
  - [ ] Renamed files
  - [ ] Converted formats
- Notes:
```

---

## 🧯 Troubleshooting

### Font loads locally but 404s in prod
- Ensure the deployed build actually includes `web/public/fonts/**`
- Verify the URL is `/fonts/...` (not `./fonts/...`) if your router rewrites paths
- Confirm case sensitivity (Linux servers are strict)

### A library can’t find its fonts (e.g., icons)
Some CSS packages assume fonts live at `../fonts` relative to the CSS file location.  
That’s why a top-level `/fonts` directory pattern is common (and why we keep this folder). [oai_citation:14‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

---

## 📚 References used for this README

- **KFM provenance-first architecture principles** [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  [oai_citation:16‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- **Embedding web fonts with `@font-face` + licensing cautions** [oai_citation:17‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  [oai_citation:18‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- **Why `/fonts` paths matter & common asset layout expectations** [oai_citation:19‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  
- **Keeping typography consistent with scale/hierarchy** [oai_citation:20‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda) [oai_citation:21‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)

---