<div align="center">

# 📸 Kansas-Frontier-Matrix — Web Screenshots  
`web/assets/screenshots/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Store **small, optimized screenshots** that demonstrate the Kansas Frontier Matrix web viewer.  
These images are used in **README files, docs, GitHub Pages, and presentations**.

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Capture screenshots\n(MapLibre viewer · web UI)"] --> B["Optimize\n(PNG/JPEG compression)"]
  B --> C["Store in web/assets/screenshots/"]
  C --> D["Reference in README/docs\n(Markdown embeds)"]
  D --> E["Validate\n(file size limits, naming conventions)"]

<!-- END OF MERMAID -->



⸻

📂 Typical Contents

web/assets/screenshots/
├── viewer-dark.png       # dark theme demo
├── viewer-light.png      # light theme demo
├── treaty-overlay.png    # treaty boundaries overlay example
├── floodplain-map.png    # hydrology + floodplain visualization
└── README.md

	•	viewer-dark.png / viewer-light.png → show default UI themes
	•	treaty-overlay.png → demonstrate vector overlays
	•	floodplain-map.png → hydrology & hazards example

⸻

🧭 Conventions
	•	Formats → PNG preferred (lossless + transparency), JPEG allowed for large full-screen captures
	•	File size → ≤250 KB per screenshot
	•	Dimensions → 1200×800 or 2× for HiDPI scaling
	•	Naming → lowercase-hyphenated (treaty-overlay.png)
	•	Content → UI should be uncluttered, highlight a single feature

⸻

📑 Example Usage (Markdown Embed)

![Kansas Frontier Matrix Viewer — Dark Theme](../screenshots/viewer-dark.png)

This embeds the screenshot into docs/READMEs for visual context.

⸻

🔗 Integration
	•	Documentation → used in README.md across the repo
	•	GitHub Pages → referenced in index.html or docs pages
	•	Presentations → lightweight images for slides/demos
	•	Knowledge Hub → examples showing overlays, treaties, hazards

⸻

📝 Notes
	•	✅ Always optimize before commit (oxipng, pngquant, mozjpeg)
	•	✅ Keep screenshots descriptive but minimal
	•	❌ Do not add raw, uncompressed screen captures
	•	❌ No large background images or heavy raster data (belongs in data/)

⸻

📚 See Also
	•	../ → global web assets (logos, palette, typography)
	•	../ui/ → UI icons & vector elements
	•	../../docs/ → project documentation referencing screenshots

⸻

✅ Mission Principle

Screenshots should be lightweight, optimized, and illustrative.
They visually demonstrate Kansas Frontier Matrix features while keeping the repo lean.
