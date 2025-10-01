<div align="center">

# 🖼️ Kansas-Frontier-Matrix — Web Assets  
`web/assets/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Hold the **UI & brand assets** used by the MapLibre web viewer and GitHub Pages site.  
Tests expect **`logo.png`** and **`favicon.svg`** to exist here.

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Design tokens & assets\n(palette.json · icons/ · logo.svg)"] --> B["Optimize\n(svgo · oxipng · mozjpeg)"]
  B --> C["Assemble site\n(index.html · app.css · app.js)"]
  C --> D["Viewer config\n(web/config/layers.json)"]
  D --> E["Build & Deploy\n(GitHub Pages)"]

<!-- END OF MERMAID -->



⸻

📂 Folder Layout

web/
├─ app.js
├─ app.css
├─ app.config.json           # optional; can be rendered from STAC via `make site-config`
├─ layers.json               # minimal site manifest (written by `make site`)
└─ assets/
   ├─ logo.png               # required (raster fallback)
   ├─ favicon.svg            # required (vector favicon)
   ├─ icons/                 # generated platform icons
   ├─ palette.json           # design tokens (colors, spacing, radii)
   ├─ typography.json        # (optional) font tokens
   ├─ ui/                    # small UI SVGs (buttons, chevrons, etc.)
   └─ screenshots/           # small, compressed demo screenshots


⸻

🧭 Naming & Conventions
	•	Filenames lowercase-hyphenated: kansas-frontier-logo.svg, map-pin.svg.
	•	Prefer SVG for flat graphics/icons, PNG for screenshots, JPEG for photos.
	•	Keep raster sizes power-of-two or ×2 where reasonable for crisp HiDPI rendering.
	•	No spaces in filenames (downstream tooling & URLs stay happy).

⸻

🎨 Brand Tokens (Design System)

Keep a small token set to theme the viewer consistently.

palette.json (example)

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
  "opacity": { "overlay": 0.85, "muted": 0.6 },
  "radii": { "sm": 4, "md": 8, "lg": 12 }
}

Usage: app.js can load assets/palette.json at startup to theme controls and legends.

⸻

🔖 Logo Specs

Purpose	File	Size(s)	Notes
Main logo	logo.png	512×512	Transparent background, ≤ 50 KB
Vector logo	logo.svg	1× (scales)	Optional but recommended
Social share	og.png	1200×630	Optional (Open Graph/Twitter Card)

Export tips
	•	Trim extra transparent padding.
	•	For PNG: prefer indexed color & optimize (see below).

⸻

🧩 Favicons & App Icons

Place favicon.svg and generate a small set of platform icons into assets/icons/:

File	Size	Purpose
favicon.svg	vector	Modern browsers (required)
favicon-32.png, favicon-16.png	32 / 16	Legacy fallback
apple-touch-icon.png	180×180	iOS home screen
android-chrome-192x192.png	192×192	Android
android-chrome-512x512.png	512×512	Android / PWA
site.webmanifest	—	Optional PWA manifest

If you don’t use a PWA, site.webmanifest is optional. Keep the SVG plus a 32-px PNG fallback.

⸻

🧪 Optimization (keep the repo lean)
	•	SVG: svgo (remove metadata, collapse groups)
	•	PNG: oxipng -o 4 --strip all or pngquant --quality=70-85
	•	JPEG: mozjpeg -quality 78 or cjpeg -quality 78 -optimize
	•	Target ≤100 KB per asset; screenshots ≤250 KB.
	•	Large geospatial data (DEM/COGs) belongs in data/ (already handled by Makefiles/LFS).
Do not drop heavy images here.

⸻

🔗 How the Site Uses These Files
	•	logo.png & favicon.svg referenced by index.html / app.css and used by tests.
	•	palette.json (optional) is fetched by app.js to theme UI widgets.
	•	Icons in assets/icons/ are linked in <head> when present.

If you change file names, update references in:
	•	web/index.html (or the template)
	•	web/app.css
	•	tests (e.g., tests/test_sources.py, if paths are asserted)

⸻

✅ Quick Checks (pre-commit)
	•	logo.png present, ≤ 50 KB, transparent, crisp on dark BG
	•	favicon.svg loads in browser (no external fonts or <script>)
	•	Added icons are optimized
	•	palette.json validates as JSON (no trailing commas)
	•	No unintended large binaries added

⸻

⚖️ Licensing & Attribution
	•	Any third-party icons/images must be open-licensed (CC-BY / CC-0)
and attributed in CREDITS.md (root or here).
	•	Your project logo should be clearly licensed (MIT repo terms or a separate notice).

⸻

🛠️ Future Niceties
	•	Generate favicons in CI (npm run build:icons or a tiny Python script).
	•	Tiny “legend” SVG based on palette.json (slope/aspect swatches).
	•	Optional assets-manifest.json (hash → path) if adding cache-busting.

⸻

🧾 TL;DR
	•	Keep logo.png and favicon.svg here.
	•	Optimize everything.
	•	Use palette.json to drive consistent UI colors.

⸻


