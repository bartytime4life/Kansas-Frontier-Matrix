# Inter Typeface (UI + Map Labels) ✨

![Font](https://img.shields.io/badge/font-Inter-111827?style=for-the-badge)
![Format](https://img.shields.io/badge/format-WOFF2-111827?style=for-the-badge)
![Usage](https://img.shields.io/badge/usage-UI%20%2B%20Maps-111827?style=for-the-badge)

> [!NOTE]
> This folder is the **single source of truth** for the Inter font assets used across the Kansas Matrix System UI (and any map label/legend rendering). We keep typography **fast**, **legible**, and **auditable**.

---

## 📍 Location

```text
web/
└─ assets/
   └─ fonts/
      └─ inter/
         ├─ README.md   ✅ (this file)
         ├─ LICENSE*    ✅ (keep upstream license here)
         ├─ Inter-roman.var.woff2    (recommended)
         ├─ Inter-italic.var.woff2   (recommended)
         └─ static/ (optional: trimmed subsets per weight)
```

---

## Why Inter? (Project-aligned rationale 🧭)

KFM’s UI philosophy is “**provenance-first**”: anything the user sees should be traceable, with metadata treated as a first-class citizen, and no “mystery” assets sneaking into the build. Fonts are UI infrastructure—so they follow the same rules: contracts, traceability, and reviewable updates.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Inter is a great fit for the project’s digital-humanism goals: build tech around **human values and needs** (readability, accessibility, clarity), not the other way around.  [oai_citation:2‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  [oai_citation:3‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)

---

## ✅ What files we expect here

### Recommended (modern browsers)
- `Inter-roman.var.woff2` (variable font, upright)
- `Inter-italic.var.woff2` (variable font, italic)

### Optional (only if you truly need them)
- Static weights (e.g., `static/Inter-Regular.woff2`, `static/Inter-SemiBold.woff2`, etc.)
- Language subsets (Latin only, etc.) to reduce payload (see “Subsetting” below)  [oai_citation:4‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

> [!TIP]
> Prefer **WOFF2** and variable fonts for the modern path. Historically, webfont kits shipped multiple formats (eot/ttf/svg/woff/woff2) for broad compatibility, but keep the footprint minimal unless you have a specific requirement.  [oai_citation:5‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)  [oai_citation:6‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

---

## 🔌 How to load Inter (CSS)

### 1) Variable font `@font-face` (recommended)

```css
/* web/assets/fonts/inter/inter.css */
@font-face {
  font-family: "Inter";
  src: url("/assets/fonts/inter/Inter-roman.var.woff2") format("woff2");
  font-style: normal;
  font-weight: 100 900; /* variable range */
  font-display: swap;
}

@font-face {
  font-family: "Inter";
  src: url("/assets/fonts/inter/Inter-italic.var.woff2") format("woff2");
  font-style: italic;
  font-weight: 100 900; /* variable range */
  font-display: swap;
}
```

Then, set the default stack:

```css
:root {
  --font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
}

html, body {
  font-family: var(--font-sans);
}
```

> [!NOTE]
> If you relocate fonts (e.g., alongside your CSS folder), update paths accordingly—don’t blindly copy/paste stacks without checking relative URLs.  [oai_citation:7‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)  [oai_citation:8‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)

---

## ⚡ Preload (performance win)

Add these in your `<head>` (or your framework’s document template):

```html
<link rel="preload"
      href="/assets/fonts/inter/Inter-roman.var.woff2"
      as="font" type="font/woff2" crossorigin>

<link rel="preload"
      href="/assets/fonts/inter/Inter-italic.var.woff2"
      as="font" type="font/woff2" crossorigin>
```

---

## ✂️ Subsetting (optional but powerful)

If you can download/build a subset specific to the language(s) you intend to use, do it—smaller files, faster loads.  [oai_citation:9‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

**Rules of thumb 🧠**
- ✅ UI-only Latin? Consider Latin subset
- ✅ If you need extended symbols (math, arrows, etc.), don’t over-subset
- ✅ If maps include multilingual labels, be cautious: missing glyphs create “tofu” □□□

---

## 🗺️ Map typography guidance (labels, legends, annotations)

Maps are not paragraphs. Labels need a **clear relationship** to the feature they describe and must stay readable under zoom/pan and clutter. Automated labeling can help, but you **must** review it for clarity and legibility.  [oai_citation:10‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)

### Label placement checklist ✅
- [ ] Labels clearly “attach” to the correct point/line/area
- [ ] Avoid collisions (labels vs labels, labels vs symbols)
- [ ] Maintain consistent style by feature class (towns vs rivers vs roads)
- [ ] Prefer rules-based placement + manual overrides for key features

### Micro-typography that matters 🔍
Line spacing and alignment can make labels readable or miserable. Avoid “set solid” spacing; keep spacing consistent; don’t add so much spacing that labels look like separate lines/features.  [oai_citation:11‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)  
Also: ragged-right is usually fine; avoid justification artifacts; hyphenation is rarely appropriate on labels.  [oai_citation:12‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)

---

## ♿ Accessibility defaults (UI)

Inter is only half the story; the CSS matters too.

```css
body {
  font-family: var(--font-sans);
  line-height: 1.5;
  text-rendering: optimizeLegibility;
}

h1, h2, h3 {
  line-height: 1.15;
}

code, pre {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}
```

> [!TIP]
> Convert design comps into scalable units (e.g., px → rem) to keep typography responsive and consistent across devices.  [oai_citation:13‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)

---

## 🧾 Provenance & “no mystery fonts” policy

In KFM, unsourced artifacts aren’t allowed into the catalog; the same principle applies to UI assets: no untracked font changes.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Add (or update) a tiny manifest ✅
Create `web/assets/fonts/inter/manifest.json` (recommended):

```json
{
  "family": "Inter",
  "source": "UPSTREAM_URL_OR_VENDOR",
  "version": "x.y.z",
  "license": "SEE_LICENSE_FILE",
  "files": [
    {"path": "Inter-roman.var.woff2", "sha256": "..." },
    {"path": "Inter-italic.var.woff2", "sha256": "..." }
  ],
  "notes": "Variable fonts preferred. Any subsetting must be documented."
}
```

This mirrors the platform’s contract-first approach: assets should be self-described so other parts of the system can trust and reuse them confidently.  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧪 QA quick checks (before merging)

- [ ] No missing glyphs in UI (search, filters, legends, citations view)
- [ ] No label tofu on maps for expected locales
- [ ] No CLS surprises: `font-display: swap` used, preload present
- [ ] Mobile: small text remains legible at common zoom levels
- [ ] Dark mode: weight/contrast holds up

---

## 📚 Project references (why these rules exist)

- KFM “contract-first / provenance-first” + no mystery layers  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- Digital Humanism: shape tech around human values/needs; human-centered computing  [oai_citation:19‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  [oai_citation:20‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  
- Web typography: formats, @font-face, and subsetting  [oai_citation:21‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)  [oai_citation:22‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)  
- Map typography: automated labeling must be evaluated; spacing/alignment basics  [oai_citation:23‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)  [oai_citation:24‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)  

---

💚 If you add/upgrade fonts, keep it boring: **document it, hash it, review it, ship it.**
