<div align="center">

# 🤝 Kansas-Frontier-Matrix — Contributing Guide (`web/`)

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.github/workflows/pre-commit.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy Security Scan](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

</div>

---

## 📖 Introduction

Welcome! 🎉  
This document explains how to contribute to the **Kansas-Frontier-Matrix web viewer** (`web/`) in a way that is **consistent, accessible, and reproducible**.

---

## 1. 🌟 General Principles

- **Config-driven** → do not hardcode layers. Use `app.config.json` or `config/*.json`.
- **Relative paths only** → always use `./`, never `../` (breaks GitHub Pages).
- **Accessibility first** → check focus-visible, reduced motion, color contrast.
- **Consistency** → follow the [STYLE_GUIDE.md](STYLE_GUIDE.md) for CSS, JS, and JSON.
- **Reproducibility** → validate configs with `jq`, preview locally before PR.

---

## 2. ⚙️ Development Workflow

### Local setup
Any static server will work:

```sh
cd web
npx http-server -p 8080
# Open http://localhost:8080/

Editing flow
	1.	Edit configs (app.config.json or add to config/*.json).
	2.	Place data in the correct directory:
	•	Raster → web/tiles/...
	•	GeoJSON → web/vectors/... or web/data/processed/...
	3.	Update layers[] with id, type, url/data, time, etc.
	4.	Validate JSON syntax:

jq . web/app.config.json > /dev/null

	5.	Preview in browser and check:
	•	Sidebar group & toggle visibility
	•	Timeline slider filtering
	•	Opacity & legend rendering

⸻

3. 📝 Commit Guidelines

We use conventional commit prefixes:

Prefix	Scope examples	Usage example
css:	tokens, layout, range UI	css: polish legend styles
js:	app.js, helpers, events	js: add timeline year filter
config:	app.config.json, sources	config: add 1900 railroads layer
docs:	Markdown in web/docs/	docs: expand CONTRIBUTING.md with CI notes
tiles:	new raster layers	tiles: add 1937 DEM hillshade
vectors:	new GeoJSON layers	vectors: add 1894 treaties dataset
a11y:	accessibility fixes	a11y: improve focus-visible on slider
build:	CI/CD, validation scripts	build: add JSON schema check to CI


⸻

4. 🗺 Adding a New Layer (Quick Recipe)
	1.	Place data in web/tiles/ or web/vectors/.
	2.	Add entry in app.config.json:

{
  "id": "usgs-1902-topeka",
  "title": "USGS Historic Topo — Topeka (1902)",
  "group": "Historic Topographic Maps",
  "type": "raster",
  "url": "./tiles/historic/usgs_1902_topeka/{z}/{x}/{y}.png",
  "opacity": 0.75,
  "visible": false,
  "time": { "start": "1902-01-01", "end": "1902-12-31" },
  "attribution": "USGS Historical Topographic Maps (Public Domain)"
}

	3.	(Optional) Add legend[] if needed.
	4.	Preview in browser.
	5.	Commit with config: or vectors: prefix.

⸻

5. 📚 Documentation Contributions
	•	Add new guides to web/docs/.
	•	Use GitHub-flavored Markdown.
	•	Test Mermaid diagrams in GitHub preview (quote labels, use \n line breaks).
	•	Scope docs clearly:
	•	ARCHITECTURE.md → structure & flow
	•	STYLE_GUIDE.md → coding conventions
	•	DEVELOPER_GUIDE.md → daily workflows
	•	CONTRIBUTING.md → this guide

⸻

6. ✅ CI & Validation
	•	JSON linting with jq required before PR.
	•	Optional schema check:

jq -e '
  .version and .layers and (.layers | type=="array") and
  ([.layers[] | has("id") and has("type") and (
      (.type=="raster" and has("url")) or
      (.type=="geojson" and has("data"))
  )] | all)
' web/app.config.json > /dev/null

	•	Ensure all links resolve in a static server context.
	•	CI runs JSON validity + STAC item validation.

⸻

7. 🌱 Community Standards
	•	Be respectful & collaborative.
	•	PRs should include:
	•	Description of change
	•	Before/after screenshots (UI changes)
	•	Data sources & licenses
	•	Major features/changes → open an Issue before PR.

⸻

8. 🔄 Contribution Workflow (Visual)

flowchart LR
  A["Fork Repo"] --> B["Create Feature Branch"]
  B --> C["Edit Configs & Docs"]
  C --> D["Run Local Server\nValidate JSON (jq)"]
  D --> E["Commit with Conventional Prefix"]
  E --> F["Open Pull Request"]
  F --> G["CI Runs\n(JSON lint, STAC validate, security scans)"]
  G --> H{"CI Passes?"}
  H -->|Yes| I["PR Review & Merge"]
  H -->|No| J["Fix Issues & Push Updates"]


⸻

9. ✅ Good First PR Checklist

Before opening a PR, check off:
	•	JSON passes jq lint
	•	Configs use relative ./ paths only
	•	New layer appears in sidebar + legend
	•	Timeline filter works as expected
	•	Attribution included for dataset
	•	Commit message uses correct prefix
	•	Screenshots added for UI changes (if applicable)

⸻


<div align="center">


✅ Following this guide ensures contributions are consistent, portable, accessible, and reproducible — strengthening the Kansas-Frontier-Matrix web viewer.

</div>
```
