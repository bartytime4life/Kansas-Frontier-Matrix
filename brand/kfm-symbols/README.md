---
title: "🟦 KFM Symbol System — SVG Pack"
path: "brand/kfm-symbols/README.md"
version: "KFM-MDP v11.2.6"
status: "draft"
last_updated: "2026-02-02"
license: "CC-BY-4.0 (suggested for brand assets)"
owners:
  - "KFM Core Maintainers"
tags:
  - "branding"
  - "svg"
  - "cartography"
  - "provenance"
  - "design-tokens"
---

# 🌾 Kansas Frontier Matrix — Symbol (SVG Pack)

This pack provides **production-ready SVGs** for the KFM symbol system:
- ✅ Primary mark (Kansas + matrix + frontier line + provenance nodes)
- ✅ Glyph (matrix + frontier + nodes)
- ✅ Lockups (horizontal + stacked)
- ✅ Favicon / app icon
- ✅ Watermark (map-safe)
- ✅ Provenance badge (UI chip)

---

## 🧱 Recommended repo layout 📁

```text
📁 brand/
  📁 kfm-symbols/
    📄 README.md
    📄 tokens.css
    📄 kfm-mark.svg
    📄 kfm-glyph.svg
    📄 kfm-lockup-horizontal.svg
    📄 kfm-lockup-stacked.svg
    📄 kfm-favicon.svg
    📄 kfm-watermark.svg
    📄 kfm-provenance-badge.svg
```

---

## 🎛️ Design Tokens (CSS) 🎨

> Use these tokens in web UI, docs, and SVG `style` blocks.

```css
:root{
  --kfm-prairie-gold: #C9A24D;   /* land / wheat */
  --kfm-soil-brown:  #4A3B2A;   /* grounding / history */
  --kfm-water-blue:  #3A6EA5;   /* rivers / openness */
  --kfm-graph-slate: #2E3440;   /* UI / graph */
  --kfm-canvas:      #F5F2ED;   /* background */

  --kfm-stroke:      3;
  --kfm-stroke-thin: 2;
  --kfm-radius:      18;
}
```

---

## 🟦 1) Primary Mark — `kfm-mark.svg` (Kansas + Matrix + Frontier)

**Intent:** “Place + structure + time + evidence.”  
**Use:** Primary brand mark (docs cover, app header, splash screens).

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="520" viewBox="0 0 720 520" role="img" aria-label="Kansas Frontier Matrix symbol">
  <defs>
    <style>
      :root{
        --kfm-prairie-gold:#C9A24D;
        --kfm-soil-brown:#4A3B2A;
        --kfm-water-blue:#3A6EA5;
        --kfm-graph-slate:#2E3440;
        --kfm-stroke:3;
        --kfm-stroke-thin:2;
      }
      .outline{ fill:none; stroke:var(--kfm-soil-brown); stroke-width:var(--kfm-stroke); stroke-linejoin:round; }
      .grid{ fill:none; stroke:var(--kfm-graph-slate); stroke-width:var(--kfm-stroke-thin); opacity:.85; }
      .frontier{ fill:none; stroke:var(--kfm-water-blue); stroke-width:4; stroke-linecap:round; stroke-linejoin:round; }
      .node{ fill:var(--kfm-prairie-gold); stroke:var(--kfm-soil-brown); stroke-width:2; }
      .soft{ opacity:.35; }
    </style>
  </defs>

  <!-- Kansas (abstracted silhouette) -->
  <!-- Shape notes:
       - Mostly rectangular = survey grid + state geometry
       - Subtle left-side notch = border character without literal detail
  -->
  <path class="outline" d="
    M170,90
    H560
    Q585,90 595,110
    V395
    Q595,415 570,420
    H185
    Q160,420 150,398
    V250
    Q150,235 170,228
    V110
    Q170,90 170,90
    Z" />

  <!-- Inner safe area -->
  <g transform="translate(210,140)">
    <!-- Matrix grid (4x4 cells) -->
    <rect class="grid soft" x="0" y="0" width="320" height="240" rx="10"/>
    <path class="grid" d="M80,0 V240 M160,0 V240 M240,0 V240"/>
    <path class="grid" d="M0,60 H320 M0,120 H320 M0,180 H320"/>

    <!-- Frontier / river / time line -->
    <path class="frontier" d="
      M18,26
      C70,40 92,68 120,78
      C155,90 182,78 212,106
      C245,130 250,160 284,172
      C302,178 312,192 314,216" />

    <!-- Provenance nodes (evidence points) -->
    <circle class="node" cx="80" cy="60" r="10"/>
    <circle class="node" cx="160" cy="120" r="10"/>
    <circle class="node" cx="240" cy="180" r="10"/>
    <circle class="node" cx="300" cy="210" r="10"/>

    <!-- Optional micro "spark" node (matrix discovery) -->
    <circle class="node" cx="40" cy="180" r="6" opacity=".85"/>
  </g>
</svg>
```

---

## 🧩 2) Glyph — `kfm-glyph.svg` (Matrix + Frontier + Nodes)

**Intent:** Compact mark for buttons, badges, and UI corners.  
**Use:** App icon (secondary), section headers, dataset cards.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="320" height="320" viewBox="0 0 320 320" role="img" aria-label="KFM glyph">
  <defs>
    <style>
      :root{
        --kfm-prairie-gold:#C9A24D;
        --kfm-soil-brown:#4A3B2A;
        --kfm-water-blue:#3A6EA5;
        --kfm-graph-slate:#2E3440;
      }
      .frame{ fill:none; stroke:var(--kfm-soil-brown); stroke-width:6; stroke-linejoin:round; }
      .grid{ fill:none; stroke:var(--kfm-graph-slate); stroke-width:3; opacity:.9; }
      .frontier{ fill:none; stroke:var(--kfm-water-blue); stroke-width:6; stroke-linecap:round; stroke-linejoin:round; }
      .node{ fill:var(--kfm-prairie-gold); stroke:var(--kfm-soil-brown); stroke-width:3; }
    </style>
  </defs>

  <rect class="frame" x="26" y="26" width="268" height="268" rx="28"/>

  <!-- Grid -->
  <path class="grid" d="M92,44 V276 M160,44 V276 M228,44 V276"/>
  <path class="grid" d="M44,92 H276 M44,160 H276 M44,228 H276"/>

  <!-- Frontier line -->
  <path class="frontier" d="M58,78 C110,86 126,110 156,118 C194,128 206,154 230,176 C250,196 258,220 262,244"/>

  <!-- Nodes -->
  <circle class="node" cx="92" cy="92" r="12"/>
  <circle class="node" cx="160" cy="160" r="12"/>
  <circle class="node" cx="228" cy="228" r="12"/>
</svg>
```

---

## 🧷 3) Lockup — Horizontal — `kfm-lockup-horizontal.svg`

**Use:** GitHub README headers, site navbar, slide titles.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="980" height="240" viewBox="0 0 980 240" role="img" aria-label="KFM horizontal lockup">
  <defs>
    <style>
      :root{
        --kfm-soil-brown:#4A3B2A;
        --kfm-graph-slate:#2E3440;
      }
      .wordmark{ font: 700 44px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial; fill:var(--kfm-graph-slate); letter-spacing:.5px;}
      .sub{ font: 500 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial; fill:var(--kfm-soil-brown); opacity:.9;}
    </style>
  </defs>

  <!-- Glyph left -->
  <g transform="translate(20,20)">
    <!-- Inline glyph (same geometry as kfm-glyph, scaled) -->
    <svg x="0" y="0" width="200" height="200" viewBox="0 0 320 320">
      <defs>
        <style>
          :root{
            --kfm-prairie-gold:#C9A24D;
            --kfm-soil-brown:#4A3B2A;
            --kfm-water-blue:#3A6EA5;
            --kfm-graph-slate:#2E3440;
          }
          .frame{ fill:none; stroke:var(--kfm-soil-brown); stroke-width:6; stroke-linejoin:round; }
          .grid{ fill:none; stroke:var(--kfm-graph-slate); stroke-width:3; opacity:.9; }
          .frontier{ fill:none; stroke:var(--kfm-water-blue); stroke-width:6; stroke-linecap:round; stroke-linejoin:round; }
          .node{ fill:var(--kfm-prairie-gold); stroke:var(--kfm-soil-brown); stroke-width:3; }
        </style>
      </defs>
      <rect class="frame" x="26" y="26" width="268" height="268" rx="28"/>
      <path class="grid" d="M92,44 V276 M160,44 V276 M228,44 V276"/>
      <path class="grid" d="M44,92 H276 M44,160 H276 M44,228 H276"/>
      <path class="frontier" d="M58,78 C110,86 126,110 156,118 C194,128 206,154 230,176 C250,196 258,220 262,244"/>
      <circle class="node" cx="92" cy="92" r="12"/>
      <circle class="node" cx="160" cy="160" r="12"/>
      <circle class="node" cx="228" cy="228" r="12"/>
    </svg>
  </g>

  <!-- Text right -->
  <text class="wordmark" x="250" y="105">Kansas Frontier Matrix</text>
  <text class="sub" x="250" y="145">Provenance-first • Geospatial • Open-data • Story + Science + AI</text>
</svg>
```

---

## 🧷 4) Lockup — Stacked — `kfm-lockup-stacked.svg`

**Use:** Cover pages, posters, community graphics.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="520" viewBox="0 0 720 520" role="img" aria-label="KFM stacked lockup">
  <defs>
    <style>
      :root{
        --kfm-soil-brown:#4A3B2A;
        --kfm-graph-slate:#2E3440;
      }
      .wordmark{ font: 800 54px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial; fill:var(--kfm-graph-slate); letter-spacing:.6px;}
      .sub{ font: 500 20px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial; fill:var(--kfm-soil-brown); opacity:.9;}
    </style>
  </defs>

  <!-- Primary mark top -->
  <g transform="translate(90,30) scale(0.75)">
    <!-- Inline primary mark -->
    <svg width="720" height="520" viewBox="0 0 720 520">
      <defs>
        <style>
          :root{
            --kfm-prairie-gold:#C9A24D;
            --kfm-soil-brown:#4A3B2A;
            --kfm-water-blue:#3A6EA5;
            --kfm-graph-slate:#2E3440;
            --kfm-stroke:3;
            --kfm-stroke-thin:2;
          }
          .outline{ fill:none; stroke:var(--kfm-soil-brown); stroke-width:var(--kfm-stroke); stroke-linejoin:round; }
          .grid{ fill:none; stroke:var(--kfm-graph-slate); stroke-width:var(--kfm-stroke-thin); opacity:.85; }
          .frontier{ fill:none; stroke:var(--kfm-water-blue); stroke-width:4; stroke-linecap:round; stroke-linejoin:round; }
          .node{ fill:var(--kfm-prairie-gold); stroke:var(--kfm-soil-brown); stroke-width:2; }
          .soft{ opacity:.35; }
        </style>
      </defs>
      <path class="outline" d="M170,90 H560 Q585,90 595,110 V395 Q595,415 570,420 H185 Q160,420 150,398 V250 Q150,235 170,228 V110 Q170,90 170,90 Z"/>
      <g transform="translate(210,140)">
        <rect class="grid soft" x="0" y="0" width="320" height="240" rx="10"/>
        <path class="grid" d="M80,0 V240 M160,0 V240 M240,0 V240"/>
        <path class="grid" d="M0,60 H320 M0,120 H320 M0,180 H320"/>
        <path class="frontier" d="M18,26 C70,40 92,68 120,78 C155,90 182,78 212,106 C245,130 250,160 284,172 C302,178 312,192 314,216"/>
        <circle class="node" cx="80" cy="60" r="10"/>
        <circle class="node" cx="160" cy="120" r="10"/>
        <circle class="node" cx="240" cy="180" r="10"/>
        <circle class="node" cx="300" cy="210" r="10"/>
        <circle class="node" cx="40" cy="180" r="6" opacity=".85"/>
      </g>
    </svg>
  </g>

  <!-- Text -->
  <text class="wordmark" x="80" y="430">Kansas Frontier Matrix</text>
  <text class="sub" x="80" y="468">A living atlas of Kansas — mapped, linked, and sourced.</text>
</svg>
```

---

## 🧿 5) Favicon / App Icon — `kfm-favicon.svg`

**Use:** Browser tab, small UI icon.  
**Tip:** Export to 32×32 and 64×64 PNG if needed.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128" role="img" aria-label="KFM favicon">
  <defs>
    <style>
      :root{
        --kfm-prairie-gold:#C9A24D;
        --kfm-soil-brown:#4A3B2A;
        --kfm-water-blue:#3A6EA5;
        --kfm-graph-slate:#2E3440;
      }
      .frame{ fill:none; stroke:var(--kfm-soil-brown); stroke-width:6; }
      .grid{ fill:none; stroke:var(--kfm-graph-slate); stroke-width:3; opacity:.9; }
      .frontier{ fill:none; stroke:var(--kfm-water-blue); stroke-width:6; stroke-linecap:round; }
      .node{ fill:var(--kfm-prairie-gold); stroke:var(--kfm-soil-brown); stroke-width:3; }
    </style>
  </defs>

  <rect class="frame" x="10" y="10" width="108" height="108" rx="18"/>
  <path class="grid" d="M64,16 V112 M16,64 H112"/>
  <path class="frontier" d="M22,34 C46,38 52,52 64,56 C78,60 88,78 106,98"/>
  <circle class="node" cx="64" cy="64" r="10"/>
</svg>
```

---

## 🗺️ 6) Watermark — `kfm-watermark.svg` (Map-safe)

**Intent:** Subtle provenance watermark for map exports, PDFs, and background layers.  
**Rule:** Should remain readable at low opacity.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="900" height="600" viewBox="0 0 900 600" role="img" aria-label="KFM watermark">
  <defs>
    <style>
      :root{
        --kfm-graph-slate:#2E3440;
      }
      .wm{ fill:none; stroke:var(--kfm-graph-slate); stroke-width:4; opacity:.10; }
      .wm2{ fill:none; stroke:var(--kfm-graph-slate); stroke-width:2; opacity:.12; }
      .node{ fill:var(--kfm-graph-slate); opacity:.12; }
    </style>

    <!-- Tileable pattern -->
    <pattern id="kfmPattern" width="180" height="180" patternUnits="userSpaceOnUse">
      <rect x="18" y="18" width="144" height="144" rx="18" class="wm"/>
      <path d="M90,18 V162 M18,90 H162" class="wm2"/>
      <path d="M30,50 C60,54 68,68 90,74 C112,80 124,104 150,134" class="wm"/>
      <circle cx="90" cy="90" r="8" class="node"/>
      <circle cx="54" cy="54" r="5" class="node"/>
      <circle cx="126" cy="126" r="5" class="node"/>
    </pattern>
  </defs>

  <rect x="0" y="0" width="900" height="600" fill="url(#kfmPattern)"/>
</svg>
```

---

## 🏷️ 7) Provenance Badge — `kfm-provenance-badge.svg`

**Use:** “Evidence / Provenance” pill for UI (dataset cards, AI answers, exports).

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="520" height="120" viewBox="0 0 520 120" role="img" aria-label="KFM provenance badge">
  <defs>
    <style>
      :root{
        --kfm-prairie-gold:#C9A24D;
        --kfm-soil-brown:#4A3B2A;
        --kfm-water-blue:#3A6EA5;
        --kfm-graph-slate:#2E3440;
        --kfm-canvas:#F5F2ED;
      }
      .chip{ fill:var(--kfm-canvas); stroke:var(--kfm-soil-brown); stroke-width:3; }
      .grid{ fill:none; stroke:var(--kfm-graph-slate); stroke-width:2; opacity:.8; }
      .frontier{ fill:none; stroke:var(--kfm-water-blue); stroke-width:4; stroke-linecap:round; }
      .node{ fill:var(--kfm-prairie-gold); stroke:var(--kfm-soil-brown); stroke-width:2; }
      .label{ font: 700 24px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial; fill:var(--kfm-graph-slate); letter-spacing:.4px;}
      .sub{ font: 500 14px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial; fill:var(--kfm-soil-brown); opacity:.9;}
    </style>
  </defs>

  <rect class="chip" x="12" y="12" width="496" height="96" rx="26"/>

  <!-- Mini glyph -->
  <g transform="translate(28,22)">
    <rect x="0" y="0" width="76" height="76" rx="18" class="chip"/>
    <path class="grid" d="M38,8 V68 M8,38 H68"/>
    <path class="frontier" d="M12,22 C26,24 30,32 38,34 C48,36 54,48 66,62"/>
    <circle class="node" cx="38" cy="38" r="7"/>
  </g>

  <text class="label" x="130" y="58">Provenance Verified</text>
  <text class="sub" x="130" y="82">Traceable sources • auditable lineage • evidence-first</text>
</svg>
```

---

## ✅ Quick Usage Notes 🔧

- All SVGs are **pure vector** (no external fonts required; system font stacks used in lockups/badges).
- For strict brand consistency in PDFs, convert text to outlines in your vector editor if needed.
- These marks are built to survive:
  - monochrome printing 🖨️
  - map overlays 🗺️
  - dark-mode UI 🌙 (invert strokes/fills)

---

## 🧪 Suggested Export Targets 📦

- **Favicon:** 32×32, 64×64, 128×128 PNG
- **App icon:** 512×512 PNG (from `kfm-glyph.svg`)
- **Docs cover:** use `kfm-mark.svg` or `kfm-lockup-stacked.svg`
- **Map watermark:** set opacity to 6–12% depending on basemap contrast

---
