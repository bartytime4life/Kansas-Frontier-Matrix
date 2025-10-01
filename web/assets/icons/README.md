<div align="center">

# 🖼️ Kansas-Frontier-Matrix — Web Icons  
`web/assets/icons/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Provide **favicon + platform icon assets** for the Kansas Frontier Matrix web viewer.  
These icons ensure cross-platform compatibility (desktop browsers, iOS/Android, PWAs).  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Source icon (favicon.svg)"] --> B["Generate icons\n(PNG, manifest, Apple Touch)"]
  B --> C["Store in\n(web/assets/icons/)"]
  C --> D["Reference in HTML\n(index.html · app.css)"]
  C --> E["Validate\n(pre-commit checks)"]

<!-- END OF MERMAID -->



⸻

📂 Typical Contents

web/assets/icons/
├── favicon.svg
├── favicon-16.png
├── favicon-32.png
├── apple-touch-icon.png
├── android-chrome-192x192.png
├── android-chrome-512x512.png
├── site.webmanifest
└── README.md

	•	favicon.svg → required, scalable vector source
	•	PNG fallbacks → favicon-16.png, favicon-32.png
	•	apple-touch-icon.png → required for iOS home screen tiles
	•	android-chrome-*.png → required for Android & PWAs
	•	site.webmanifest → optional, defines PWA metadata

⸻

🧭 Conventions
	•	Source of truth: favicon.svg
	•	All PNGs exported from the vector, power-of-two sizes
	•	Transparent backgrounds preferred (unless Apple/iOS spec requires padding)
	•	Filenames lowercase, hyphen-separated
	•	Keep optimized:
	•	PNG → oxipng -o 4 --strip all or pngquant --quality=70-85
	•	SVG → svgo (remove metadata, collapse groups)

⸻

📑 Example site.webmanifest

{
  "name": "Kansas Frontier Matrix",
  "short_name": "KFM",
  "icons": [
    {
      "src": "android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "android-chrome-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "theme_color": "#1C4E80",
  "background_color": "#0B0D10",
  "display": "standalone"
}


⸻

🔗 Integration
	•	HTML → referenced in <head> of index.html

<link rel="icon" href="assets/icons/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/icons/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="assets/icons/apple-touch-icon.png">
<link rel="manifest" href="assets/icons/site.webmanifest">

	•	Web viewer → uses these for tab icons, bookmarks, and PWA installs
	•	Tests → CI ensures required files (favicon.svg, favicon-32.png, apple-touch-icon.png) exist

⸻

📝 Notes
	•	✅ Required: favicon.svg + one PNG fallback (usually 32 px)
	•	✅ Include at least apple-touch-icon.png (180×180) for iOS
	•	✅ Provide android-chrome-192x192.png + 512x512.png for PWAs
	•	❌ Do not add unoptimized assets >100 KB

⸻

📚 See Also
	•	../ → Web assets (logos, palette, typography)
	•	../../config/ → Viewer configs referencing icons
	•	../../tests/ → Tests validating presence of required assets

⸻

✅ Mission Principle

Icons must be consistent, optimized, and cross-platform ready.
They guarantee the Frontier Matrix web viewer looks professional everywhere — browsers, devices, and apps.
