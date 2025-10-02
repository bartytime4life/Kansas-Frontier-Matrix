name: "🐞 Bug Report"
about: "Report a reproducible problem in the site, data pipeline, AI reasoning, or docs"
title: "[BUG] <short summary>"
labels: ["bug", "needs-triage"]
assignees: []
---

<div align="center">

# 🐞 Kansas-Frontier-Matrix — Bug Report

[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../actions/workflows/tests.yml)
[![CI](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml/badge.svg)](../../actions/workflows/ci.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../actions/workflows/stac-validate.yml)
[![Site](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../actions/workflows/site.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../actions/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../actions/workflows/trivy.yml)

</div>

---

## 📝 Summary

**What happened?**  
_A clear, concise description of the problem._

**Where did it happen?**  
- Area: `web` | `data pipeline` | `NLP/AI` | `GIS layer` | `docs` | `ci`
- Path (if code): `web/...`, `scripts/...`, `src/...`, `mcp/...`
- URL (if Pages): <link to live map/viewer page>

---

## 🔁 Steps to Reproduce

1. …
2. …
3. …

**Expected behavior**  
_What you thought would happen._

**Actual behavior**  
_What actually happened (include error messages, screenshots)._

---

## 💻 Environment

- OS: macOS | Linux | Windows
- Browser (if UI): Chrome | Firefox | Safari — version
- Python: `python --version`
- Node (if web build): `node -v` / `npm -v`
- GDAL: `gdalinfo --version`
- QGIS (if relevant): version
- Git SHA (commit reproducing bug): `abcdef1`
- Branch: `main` | `feature/...`

---

## 📦 Data & Reproducibility (MCP / DVC)

⚠️ **Do not attach large binaries.** Link artifacts or provide IDs.

- **STAC / sources JSON**:  
  - Path: `stac/items/<id>.json` | `stac/collections/<id>.json` | `data/sources/<file>.json`  
  - ID: `<id>`
- **DVC-tracked artifacts**:  
  - `.dvc` file path(s): `data/raw/.../foo.tif.dvc`  
  - Checksum(s): `md5: <hash>`
- **Git LFS files**: paths to large files under LFS
- **Minimal repro dataset**: public URL / DOI if available

**Helpful checks (optional, paste output):**

```bash
# Validate STAC items (requires kgt)
kgt validate-stac stac/items --no-strict || true

# JSON sanity check for changed files
jq -e 'type=="object"' <changed.json>
````

---

## 🌍 Geospatial Context (if map/data related)

* Layer/file(s): `data/processed/...` or tileset ID
* Geometry type: raster | vector (points | lines | polygons)
* CRS: `EPSG:4326` | `EPSG:3857` | other
* Spatial extent / AOI: bbox or WKT
* Time slice(s): year(s) / timestamp(s)
* Styling/config involved: fragments from `web/config/app.config.json` or style JSON

---

## 📜 Logs / Console / Trace

<details>
<summary>Expand logs</summary>

* Browser console (UI bugs): …
* Build logs (Node/GDAL/Python): …
* Python traceback (pipeline/AI): …
* CI run link (if failing in Actions): …

</details>

---

## 🖼 Screenshots / Recordings

> Redact sensitive info (secrets, protected site coordinates).

* Image(s): drag & drop or link
* Short GIF/video (optional): …

---

## ⚠️ Impact

* **Severity**: `blocker` | `high` | `medium` | `low`
* **Affected outputs**: map layer(s) | docs page | model output | CI job
* **Reproducibility break?** (`make prebuild` / pipeline): yes/no
* **Regression?** yes/no → last known good commit/tag: …

---

## 💡 Additional Notes / Hypothesis

*Any clues, bisect results, suspected commit, or config diffs.*

---

## 📑 Roadmap Link (if applicable)

* Milestone: …
* Related epic/issue: …
* Roadmap marker:

  ```
  <!-- roadmap:key=bug-<stable-key> -->
  ```

---

## ✅ Checklist

* [ ] Reproduced on **main** at latest commit
* [ ] Included **exact steps** and **environment details**
* [ ] Linked **STAC/sources** entry or **DVC/LFS IDs** (no big uploads)
* [ ] Added **logs/screenshots**
* [ ] Confirmed not a **data license/access** issue
