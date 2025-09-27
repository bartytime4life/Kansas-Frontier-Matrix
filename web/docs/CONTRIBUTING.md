# Kansas-Frontier-Matrix — Contributing Guide

Welcome! 🎉  
This document explains how to contribute to the **Kansas-Frontier-Matrix web viewer** (`web/`) in a way that is **consistent, accessible, and reproducible**.

---

## 1. General Principles

- **Config-driven**: Do not hardcode layers in code. Add/update them via `app.config.json`.
- **Relative paths**: All assets use `./` relative paths (never `../`), or they will fail on GitHub Pages.
- **Accessibility first**: Always check focus-visible, color contrast, and reduced-motion settings.
- **Consistency**: Follow the [STYLE_GUIDE.md](STYLE_GUIDE.md) for CSS, JS, and JSON conventions.
- **Reproducibility**: Validate configs with `jq` and test locally before submitting a PR.

---

## 2. Development Workflow

### Local setup
You only need a static web server:

```sh
cd web
npx http-server -p 8080
# Open http://localhost:8080/
````

### Editing flow

1. Edit configs (`app.config.json` or a new `config/*.json`).
2. Place data in the correct directory:

   * Raster → `web/tiles/...`
   * GeoJSON → `web/vectors/...` or `web/data/processed/...`
3. Update `layers[]` in config with correct fields (`id`, `type`, `url`/`path`, `time`, etc.).
4. Validate JSON syntax:

```sh
jq . web/app.config.json > /dev/null
```

5. Preview in browser. Check:

   * Sidebar shows new layer in the right group.
   * Timeline filtering works.
   * Opacity slider and legend render correctly.

---

## 3. Commit Guidelines

We use **conventional commit prefixes** for clarity:

| Prefix     | Scope examples            | Usage example                                |
| ---------- | ------------------------- | -------------------------------------------- |
| `css:`     | tokens, layout, range UI  | `css: polish legend styles`                  |
| `js:`      | app.js, helpers, events   | `js: add timeline year filter`               |
| `config:`  | app.config.json, sources  | `config: add 1900 railroads layer`           |
| `docs:`    | Markdown in `web/docs/`   | `docs: expand CONTRIBUTING.md with CI notes` |
| `tiles:`   | new raster layers         | `tiles: add 1937 DEM hillshade`              |
| `vectors:` | new GeoJSON layers        | `vectors: add 1894 treaties dataset`         |
| `a11y:`    | accessibility fixes       | `a11y: improve focus-visible on slider`      |
| `build:`   | CI/CD, validation scripts | `build: add JSON schema check to CI`         |

---

## 4. Adding a New Layer (Quick Recipe)

1. Place data in `web/tiles/` or `web/vectors/`.
2. Add entry in `app.config.json`:

```json
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
```

3. (Optional) Add `legend[]` items if the dataset benefits from interpretation.
4. Run local preview and confirm visibility, timeline, and attribution.
5. Commit with `config:` or `vectors:` prefix.

---

## 5. Documentation Contributions

* Place new guides in `web/docs/`.
* Use **GitHub-flavored Markdown** with headings, code blocks, and fenced Mermaid diagrams.
* Validate Mermaid diagrams in GitHub’s preview (quote labels, use `\n` for line breaks).
* Keep each doc short and scoped:

  * `ARCHITECTURE.md` → structure & flow
  * `STYLE_GUIDE.md` → coding conventions
  * `DEVELOPER_GUIDE.md` → day-to-day workflows
  * `CONTRIBUTING.md` → this guide

---

## 6. CI & Validation

* JSON linting with `jq` is required before PR.
* Optionally, run local config check:

```sh
jq -e '
  .version and .layers and (.layers | type=="array") and
  ([.layers[] | has("id") and has("type") and (
      (.type=="raster" and has("url")) or
      (.type=="geojson" and has("path"))
  )] | all)
' web/app.config.json > /dev/null
```

* Ensure all links resolve in a local static server environment.
* CI will check JSON validity and STAC item connections.

---

## 7. Community Standards

* Be respectful and collaborative.
* PRs should include:

  * A description of the change
  * Before/after screenshots if it affects UI
  * References to source datasets and licensing
* Discussions for new features or structural changes belong in Issues before PR.

---

✅ Following this guide ensures contributions are consistent, portable, and keep the Kansas-Frontier-Matrix web UI accessible and reproducible.

```

