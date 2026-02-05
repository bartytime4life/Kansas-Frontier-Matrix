# 🖼️ Placeholder Images

![asset](https://img.shields.io/badge/asset-placeholder_images-blue)
![scope](https://img.shields.io/badge/path-web%2Fsrc%2Fassets%2Fimages%2Fplaceholders-lightgrey)
![intent](https://img.shields.io/badge/intent-safe_UI_fallbacks-informational)

> **TL;DR:** This folder contains **intentional “stand-ins”** for UI images (loading, missing media, empty states) so the app never looks broken or janky. ✅

---

## 📍 Location

```text
📦 web/
 └─ 🧩 src/
    └─ 🎨 assets/
       └─ 🖼️ images/
          └─ 🧱 placeholders/
             ├─ README.md  👈 you are here
             └─ (placeholder image files live here)
```

---

## 🎯 What counts as a “placeholder” here?

A placeholder image is **not content**. It’s a **visual fallback** used when:

- An image is still loading (slow network, large payload)
- A record has **no thumbnail** (dataset/story node/attachment missing media)
- An image fails to load (404/timeout/bad URL)
- A feature is behind a flag but layout should remain stable

✅ The goal is **stable layout + clear affordances** + **consistent UX**.

---

## 🧠 Design principles for KFM placeholders

### 1) Make the UI feel responsive (without lying)
- Prefer **neutral** visuals (shapes, gradients, subtle patterns).
- Avoid anything that could be mistaken for *real* map imagery, historical photos, or evidence artifacts.
- Keep “fallbacks” **predictable** so users quickly learn what they mean.

### 2) Prevent layout shift (CLS)
- Match the **final aspect ratio**: 1:1, 4:3, 16:9, etc.
- When possible, pair placeholders with CSS like `aspect-ratio` to reserve space.

### 3) Keep them lightweight 🚀
- Placeholders should load *fast* and cache well.
- Don’t ship large, unoptimized binaries.

---

## 🧾 Naming conventions

Use **kebab-case** and include **purpose + aspect/size**.

✅ Recommended pattern:

```text
ph-<purpose>-<ratio_or_size>.<ext>
```

Examples:

- `ph-avatar-1x1.svg`
- `ph-card-4x3.png`
- `ph-hero-16x9.jpg`
- `ph-mapthumb-16x9.png`
- `ph-dataset-3x2.svg`

> Tip: If size matters, use `WIDTHxHEIGHT` (`ph-card-640x480.png`).

---

## 🧩 Format guidelines

| Use case | Prefer | Why |
|---|---|---|
| Simple shapes / icons / skeleton blocks | **SVG** | Crisp at any scale, tiny payload |
| Flat UI thumbnails with transparency | **PNG** | Predictable rendering, alpha support |
| Photo-like placeholders (rare) | **JPG** | Smaller for photographic gradients/textures |
| Animated placeholders | Avoid unless necessary | Animation can be distracting + heavier |

---

## 🗜️ Compression & performance rules

**Do:**
- Export at (or close to) the size you actually display.
- Compress aggressively (placeholders rarely need detail).

**Don’t:**
- Add “full-size” images and rely on HTML/CSS to shrink them.
- Use endlessly repeating backgrounds that look “cheap” or accidental.

---

## ♿ Accessibility rules (non‑negotiable)

### Decorative placeholders
If the placeholder is purely decorative (layout scaffolding):

```html
<img src="..." alt="" aria-hidden="true" />
```

### Meaningful placeholders
If it communicates state (“no thumbnail available”), use an informative `alt`, e.g.:

- `"No thumbnail available"`
- `"Dataset preview unavailable"`

✅ Prefer communicating meaning with **real text in UI** (HTML), not embedded in the image.

---

## ⚛️ Usage patterns (React)

> These snippets assume the KFM web UI uses React/TS, but the pattern applies anywhere.

### ✅ `onError` fallback swap
```tsx
import { useState } from "react";

// Example path; adjust import style to your bundler/aliases
import fallback from "./ph-card-16x9.svg";

type ImgWithFallbackProps = {
  src?: string;
  alt: string;
  className?: string;
};

export function ImgWithFallback({ src, alt, className }: ImgWithFallbackProps) {
  const [failed, setFailed] = useState(false);

  const resolvedSrc = !src || failed ? fallback : src;

  return (
    <img
      className={className}
      src={resolvedSrc}
      alt={alt}
      loading="lazy"
      decoding="async"
      onError={() => setFailed(true)}
    />
  );
}
```

### ✅ “No file needed” placeholder using CSS
If you can do it with CSS (background color/gradient), prefer that for ultra-light skeletons:

```css
.ph-block {
  border-radius: 12px;
  /* Keep it neutral, subtle, and consistent */
  background: linear-gradient(90deg, rgba(0,0,0,.06), rgba(0,0,0,.10), rgba(0,0,0,.06));
}
```

---

## ✅ Adding a new placeholder checklist

- [ ] Name follows convention (`ph-...`)
- [ ] Aspect ratio matches the component it represents
- [ ] Compressed / optimized (no massive files)
- [ ] Looks like a placeholder (neutral, non-deceptive)
- [ ] Doesn’t embed important text (localization-friendly)
- [ ] Has a known usage pattern (decorative vs meaningful alt text)

---

## 📋 Inventory template

> Keep this list updated as placeholders are added.

| File | Purpose | Ratio/Size | Format | Notes |
|---|---|---:|---|---|
| `ph-…` | e.g. dataset card fallback | 16:9 | SVG | neutral, no text |

---

## 📚 Sources & anchors (project references)

- KFM UI focus on usability, consistent patterns, and clear feedback loops. [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- KFM web frontend context (React & TypeScript). [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- CSS background patterns as lightweight alternatives to image placeholders. [oai_citation:2‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)
- Avoiding “unprofessional” background repetition + prioritizing compressed images for web performance. [oai_citation:3‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc) [oai_citation:4‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)

### 📎 Linked source files
- KFM Comprehensive System Documentation:  [oai_citation:5‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- KFM Technical Blueprint:  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- Professional Web Design (Techniques & Templates):  [oai_citation:7‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  
- Learn to Code HTML & CSS:  [oai_citation:8‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- AI/ML best-practices compendium (project library):  [oai_citation:9‡Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf](sediment://file_0000000036fc71fda445161776f735db)
