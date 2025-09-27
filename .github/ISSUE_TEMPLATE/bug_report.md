---
name: "🐞 Bug report"
about: "Report a reproducible problem in the site, data pipeline, AI reasoning, or docs"
title: "[BUG] <short summary>"
labels: ["bug", "triage"]
assignees: []
---

## Summary

**What happened?**  
_A clear, concise description of the problem._

**Where did it happen?**  
- Area: `web UI` | `data pipeline` | `NLP/AI` | `GIS layer` | `docs` | `CI`
- Path (if code): `web/...`, `scripts/...`, `src/...`, `mcp/...`
- URL (if Pages): <link to live page / map view>

---

## Steps to Reproduce

1. …
2. …
3. …

**Expected behavior**  
_What you thought would happen._

**Actual behavior**  
_What actually happened (include messages, screenshots)._

---

## Environment

- OS: macOS | Linux | Windows
- Browser (if UI): Chrome | Firefox | Safari (version)
- Python: `python --version`
- Node (if web build): `node -v` / `npm -v`
- GDAL: `gdalinfo --version`
- QGIS (if relevant): version
- Git SHA (commit reproducing bug): `abcdef1`
- Branch: `main` | `feature/...`

---

## Data & Reproducibility (MCP/DVC)

> ⚠️ **Do not attach large binaries.** Link artifacts or provide IDs.

- STAC / sources JSON entry (if applicable):  
  - File: `stac/items/<file>.json` or `stac/collections/<file>.json` or `data/sources/<file>.json`
  - Item/Collection ID: `<id>`
- DVC-tracked artifacts (if used):  
  - `.dvc` file path(s): `data/raw/.../foo.tif.dvc`  
  - DVC checksum(s): `md5: <hash>`
- Git LFS (if used): list path(s) to large files managed via LFS.
- Minimal repro dataset or link (public source / DOI): …

**Helpful checks (paste output if relevant):**
```bash
# STAC items quick check (requires kgt, optional)
kgt validate-stac stac/items --no-strict || true

# JSON sanity for changed files (optional)
jq -e 'type=="object"' <changed.json>
````

---

## Geospatial Context (if map/data related)

* Layer/file(s): `data/processed/...` or served tileset ID
* Geometry type: raster | vector (points | lines | polygons)
* CRS: `EPSG:4326` | `EPSG:3857` | other
* Spatial extent / AOI: bbox or WKT
* Time slice(s): year(s) / timestamp(s)
* Styling/config involved: `web/app.config.json` fragments or style snippets

---

## Logs / Console / Trace

<details>
<summary>Show logs</summary>

* Browser console (UI bugs): paste or attach text
* Build logs (Node/GDAL/Python): paste relevant excerpt
* Python traceback (pipeline/AI): …
* CI run link (if failing in Actions): …

</details>

---

## Screenshots / Screen recordings

> Redact sensitive info (secrets, precise coordinates of protected sites).

* Image(s): drag & drop or link
* Short GIF/video (optional): …

---

## Impact

* Severity: `blocker` | `high` | `medium` | `low`
* Affected outputs: map layer(s) | docs page | model output | CI job
* Does it break reproducibility (`make prebuild` / pipeline)? yes/no
* Regression? If yes, **last known good commit/tag**: …

---

## Additional Notes / Hypothesis

*Any clues, bisect results, suspected commit, or config diffs.*

---

## Checklist

* [ ] Reproduced on **main** at latest commit
* [ ] Included **exact steps** and **environment**
* [ ] Linked **STAC/sources** entry or **DVC/LFS IDs** (no big uploads)
* [ ] Added **logs/screenshots**
* [ ] Confirmed not a **data license / access** issue

```
```
