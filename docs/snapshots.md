<div align="center">

# 📊 Kansas-Frontier-Matrix — Status Snapshots

**Mission:** Track **current data layers, STAC items, and assets** at a glance.  
Snapshots help maintain **traceability, reproducibility, and provenance** across the project.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](.github/workflows/stac-validate.yml)  
[![STAC Badges](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](.github/workflows/stac-badges.yml)  

[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](.github/workflows/tests.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](.github/workflows/trivy.yml)  

![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen?logo=dependabot)  
![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)  
![License](https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix)  

</div>

---

## 📂 Current Layers

| Layer                       | STAC Item                                        | Asset Path                                             |
|-----------------------------|--------------------------------------------------|--------------------------------------------------------|
| DEM (1 m, 2018–2020)        | `stac/items/ks_1m_dem_2018_2020.json`            | `data/cogs/dem/ks_1m_dem_2018_2020.tif`               |
| Hillshade (derived)         | same Item (`assets.hillshade`)                   | `data/cogs/hillshade/ks_hillshade_2018_2020.tif`       |
| Historic Topo (Larned 1894) | `stac/items/overlays/usgs_topo_larned_1894.json` | `data/cogs/overlays/usgs_topo_larned_1894.tif`         |

---

## 🔄 Snapshot Lifecycle

```mermaid
flowchart TD
  A["Raw Sources\n(data/sources/*.json)"] --> B["COGs / Overlays\n(data/cogs/**)"]
  B --> C["STAC Items\n(stac/items/*.json)"]
  C --> D["Status Snapshot\n(this table)"]
  D --> E["Web Viewer\n(web/app.config.json · _site/)"]
````

<!-- END OF MERMAID -->

---

## 🧮 Validation & Provenance

* ✅ All listed STAC items must validate:

```bash
make stac-validate
```

* ✅ Each asset must include `checksum:sha256` in STAC metadata
* ✅ Each derived product must carry `_meta.json` (origin, command, timestamp, hash)

**Example `_meta.json`:**

```json
{
  "origin": "data/raw/usgs_topo_larned_1894.tif",
  "command": "gdal_translate -of COG ...",
  "timestamp": "2025-10-01T21:00:00Z",
  "checksum:sha256": "f6b2a34d..."
}
```

---

## 📑 Roadmap Integration

Snapshots should link into milestones and roadmap:

```markdown
<!-- roadmap:key=status-snapshot -->
```

---

## ✅ Checklist

* [ ] STAC item paths exist for each asset
* [ ] Asset file paths exist in `data/cogs/**`
* [ ] STAC validates with `make stac-validate`
* [ ] Checksums included in STAC + `_meta.json`
* [ ] Viewer config (`web/app.config.json`) updated if relevant

---

## ✅ Summary

This file provides a **living index** of datasets currently integrated.
Snapshots ensure **traceability, reproducibility, and roadmap connectivity**,
so all contributors can see **which layers are live and validated** at a glance.
