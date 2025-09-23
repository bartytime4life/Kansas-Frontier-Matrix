# Web Assets — Kansas Frontier Matrix / Kansas Geo Timeline

This folder contains the **UI/brand assets** used by the lightweight MapLibre web viewer and GitHub Pages site.

> **Required files (tests expect these to exist):**
>
> - `logo.png` — project logo (raster fallback)
> - `favicon.svg` — vector favicon for modern browsers  
>   *(PNG fallbacks are optional; see “Favicons & app icons”)*

---

## Folder layout

web/
├─ app.js
├─ app.css
├─ app.config.json           # optional, rendered from STAC via make site-config
├─ layers.json               # minimal site manifest (written by make site)
└─ assets/
├─ logo.png
├─ favicon.svg
├─ icons/                 # platform icons (generated)
├─ palette.json           # design tokens (colors, spacing, radii)
├─ typography.json        # (optional) font tokens
├─ ui/                    # small UI svgs (buttons, chevrons, etc.)
└─ screenshots/           # small, compressed demo screenshots

---

## Naming & conventions

- **Lowercase, hyphen-separated** filenames: `kansas-frontier-logo.svg`, `map-pin.svg`
- Prefer **SVG** for flat graphics/icons, **PNG** for screenshots, **JPEG** for photos.
- Keep raster assets **power-of-two** or **×2** sizes where reasonable for crisp rendering on HiDPI.
- **No spaces** in filenames (helps downstream tooling and URLs).

---

## Brand tokens (design system)

Include a small set of tokens to keep the site consistent and easy to restyle.

**`palette.json` (example)**
```json
{
  "brand": {
    "primary": "#1C4E80",
    "secondary": "#F3A712",
    "accent": "#6BB187"
  },
  "ui": {
    "bg": "#0B0D10",
    "surface": "#12151A",
    "muted": "#8FA3B9",
    "text": "#E8EEF5",
    "link": "#69A7FF",
    "danger": "#E24C4B",
    "warning": "#F2C94C",
    "success": "#2DBE7E"
  },
  "elevation": {
    "dem": "#B9D6F2",
    "hillshade": "#8C8C8C",
    "slope": "#E67E22",
    "aspect": "#1ABC9C"
  },
  "opacity": {
    "overlay": 0.85,
    "muted": 0.6
  },
  "radii": { "sm": 4, "md": 8, "lg": 12 }
}

Usage: app.js can load assets/palette.json at startup to theme controls and legends.

⸻

Logo specs

Keep a master vector (prefer logo.svg) and export PNGs as needed.

Purpose	File	Size(s)	Notes
Main logo	logo.png	512×512 (required)	Transparent background, ≤ 50 KB
Vector logo	logo.svg	1× (scales)	Optional but recommended
Social share	og.png	1200×630	Optional; Open Graph/Twitter Card

Export tips
	•	Trim extra transparent padding.
	•	For PNG: use indexed color when possible, and optimize (see below).

⸻

Favicons & app icons

Place a single source (favicon.svg) and generate a small set of platform icons:
	1.	Generate icons (local or CI) using your tool of choice (e.g., RealFaviconGenerator CLI, sharp, or a small script).
	2.	Save to web/assets/icons/:

File	Size	Purpose
favicon.svg	vector	Modern browsers (required)
favicon-32.png / favicon-16.png	32/16 px	Legacy fallback
apple-touch-icon.png	180×180	iOS home screen
android-chrome-192x192.png	192×192	Android
android-chrome-512x512.png	512×512	Android / PWA
site.webmanifest	—	Optional PWA manifest

If you don’t use a PWA, site.webmanifest is optional. Keep the SVG + a 32 px PNG fallback.

⸻

Optimization (keep the repo lean)
	•	SVG: run svgo (remove metadata, collapse groups).
	•	PNG: run oxipng -o 4 --strip all or pngquant --quality=70-85.
	•	JPEG: mozjpeg -quality 78 or cjpeg -quality 78 -optimize.
	•	Aim for ≤100 KB per asset; screenshots ≤250 KB.

Large geospatial data (DEM/COGs) lives in data/ and is already handled by Makefile + (optionally) Git LFS. Do not place heavy images here.

⸻

How the site uses these files
	•	logo.png + favicon.svg are referenced by index.html/app.css and used by tests.
	•	palette.json (optional) can be fetched by app.js to style UI widgets.
	•	Icons in assets/icons/ are linked in <head> tags when present.

If you change file names, update references in:
	•	web/index.html (or your template)
	•	web/app.css
	•	tests/test_sources.py (if paths are asserted)

⸻

Quick checks (before commit)
	•	logo.png present, ≤50 KB, transparent, crisp on dark BG
	•	favicon.svg loads in browser (no external fonts or <script>)
	•	Icons (PNGs) optimized (if added)
	•	palette.json validates as JSON (no trailing commas)
	•	No unintended large binaries added here

⸻

Licensing & attribution
	•	Ensure any third-party icons/images are open-licensed (CC-BY/CC-0) and attributed in CREDITS.md (root or here).
	•	Your project logo should be clearly licensed under MIT repo terms or a separate notice.

⸻

Future niceties
	•	Auto-generate favicons in CI (npm run build:icons or a small Python script).
	•	A tiny “legend” SVG based on palette.json that renders slope/aspect swatches.
	•	An assets-manifest.json (hash → path) if you add cache-busting later.

⸻

TL;DR
	•	Keep logo.png and favicon.svg here.
	•	Optimize everything.
	•	Use palette.json to drive consistent UI colors.

