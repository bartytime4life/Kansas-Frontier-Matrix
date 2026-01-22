# 🗺️ GeoJSON Artifacts (Experiment Report Template)

![artifact](https://img.shields.io/badge/artifact-GeoJSON-2ea44f)
![scope](https://img.shields.io/badge/scope-geospatial%20vector-blue)
![ethos](https://img.shields.io/badge/ethos-provenance--first-purple)
![status](https://img.shields.io/badge/status-template-lightgrey)

This folder is the **drop-zone for GeoJSON outputs** generated during an experiment run (ETL tests, map-layer prototypes, QA exports, narrative demos). In KFM, “nothing is a black box”: artifacts should be traceable, reproducible, and governed end-to-end.  [oai_citation:0‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🎯 What belongs here (and what doesn’t)

### ✅ Good fits
- **Small/medium vector snapshots** (points/lines/polygons) for quick visual inspection in the UI.
- **Debug exports** from PostGIS queries (e.g., “features inside buffer”) using `ST_AsGeoJSON` + `ST_Transform(..., 4326)` patterns.  [oai_citation:1‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
- **Story / UI prototypes** where a GeoJSON layer is referenced by a story config (Markdown + JSON).  [oai_citation:2‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

### ❌ Not a good fit
- Huge datasets meant for serving at scale. Prefer **vector tiles / PMTiles / GeoParquet** and treat them as versioned artifacts (optionally via OCI registries with provenance attachments + signing) when size/repro demands grow.  [oai_citation:3‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧭 Core Principles (KFM-style)

- **Provenance-first**: every artifact should carry “where it came from” + “how it was made” so it can be reproduced and audited.  [oai_citation:4‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **Deterministic, config-driven** transforms (no mystery edits).  [oai_citation:5‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **Immutable source boundary**: treat raw inputs as read-only evidence; transformations happen downstream.  [oai_citation:6‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **Governance from day zero** (FAIR+CARE, classification labels, license checks).  [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

---

## 📁 Suggested layout (template-friendly)

> Adjust to your report’s needs—this is a “golden path” structure.

```text
📁 artifacts/geospatial/geojson/
├─ 📄 README.md
├─ 📁 exports/                # raw query exports (viewable, but not “published”)
├─ 📁 layers/                 # curated layers meant to be consumed by UI/story demos
├─ 📁 validation/             # QA outputs (geojson lint, geometry checks, counts)
└─ 📁 metadata/               # sidecars: manifests, prov, stac/dcat (if promoting)
```

---

## 🧱 GeoJSON profile (what we expect)

### 1) CRS & coordinate rules
- GeoJSON is assumed to be **WGS84 (EPSG:4326)** (lon/lat).  [oai_citation:8‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  
- Coordinate sanity bounds: `lon ∈ [-180, 180]`, `lat ∈ [-90, 90]`.  [oai_citation:9‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  
- KFM’s web-facing standard is **WGS84** for consistent display across the stack.  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 2) Shape
- Prefer a top-level **`FeatureCollection`**.
- Each feature should include:
  - `id` (stable if possible)
  - `properties` (human-meaningful + machine-joinable keys)
  - Valid GeoJSON geometry (Point/LineString/Polygon/etc.)

> Tip: avoid embedding a non-standard `crs` object—many modern consumers assume 4326 implicitly.  [oai_citation:11‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

---

## 🧾 Sidecar metadata (recommended always; required for promotion)

KFM treats metadata as first-class—policy gates check for **license, sensitivity classification, provenance completeness**, etc.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

| File | Purpose | When |
|---|---|---|
| `*.manifest.json` | Run context: inputs, parameters, author/tooling, output IDs | ✅ recommended |
| `*.checksums.sha256` | Tamper-evidence checksum(s) | ✅ recommended (often expected)  [oai_citation:13‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) |
| `*.prov.jsonld` | Provenance lineage (W3C PROV style) | ✅ recommended; 🔥 required for “publish” ethos  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) |
| `*.stac.item.json` | Spatiotemporal asset description | if promoting to catalog-driven workflows  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) |
| `*.dcat.dataset.jsonld` | Dataset discovery record | if promoting to catalog-driven workflows  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) |

---

## 🔐 Governance & sensitivity (don’t skip this)

KFM supports sensitivity levels (e.g., **public / sensitive / confidential**) and can **restrict, redact, or generalize** outputs when needed.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
Examples include masking coordinates or aggregating to coarser areas for protected sites.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

**Hard rule:** *No output may be less restricted than its inputs.*  [oai_citation:19‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

If a GeoJSON layer is sensitive, expect the UI to indicate it (lock/warning) and possibly display a generalized form.  [oai_citation:20‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

---

## ✅ Validation checklist (fast “ingestion gate” mindset)

KFM’s ingestion gate emphasizes integrity checks, format sanity, license/source presence, and telemetry-style logging.  [oai_citation:21‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

Use this mini-checklist before attaching GeoJSON to a report:

- [ ] Valid JSON (parseable)
- [ ] Valid GeoJSON (`FeatureCollection`, geometries present)
- [ ] CRS is WGS84/EPSG:4326 (lon/lat)  [oai_citation:22‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
- [ ] Coordinates in bounds  [oai_citation:23‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
- [ ] `license` captured (in manifest and/or properties)  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] `sensitivity.classification` captured (public/sensitive/…)  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] Checksums present (recommended)  [oai_citation:26‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Provenance sidecar present (recommended; required if promoting)  [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧪 Exporting GeoJSON from PostGIS (common pattern)

A typical pattern is: **transform to WGS84** and export geometry as GeoJSON, then wrap it as Features/FeatureCollection.  [oai_citation:28‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  
Also note: PostGIS may output only geometry JSON, so your pipeline may need to construct the full FeatureCollection.  [oai_citation:29‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

Example (illustrative) workflow:
1) SQL returns properties + `ST_AsGeoJSON(ST_Transform(...,4326))`  [oai_citation:30‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  
2) A small script wraps rows into a FeatureCollection and writes to disk.  [oai_citation:31‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  

---

## 🧩 Wiring into UI / Stories (why GeoJSON stays handy)

- The KFM UI stack is designed to show geospatial layers (2D via MapLibre, 3D via Cesium), and can consume GeoJSON/JSON endpoints as layer sources.  [oai_citation:32‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- Story content is created and versioned as **Markdown + JSON**, with the JSON referencing layer IDs (so your GeoJSON artifacts often act as temporary layers for narrative experiments).  [oai_citation:33‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  [oai_citation:34‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- Map libraries used by the broader KFM ecosystem can display GeoJSON directly (great for prototypes and validation).  [oai_citation:35‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)  

---

## 🚀 “Sandbox → Promote” (when an experiment becomes real)

Experiment outputs are **not official** until reviewed and promoted to a processed + cataloged state—don’t point production UI at experimental outputs.  [oai_citation:36‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
Promotion typically implies:
- stable IDs,
- STAC/DCAT/PROV artifacts,
- sensitivity review,
- policy gate pass.  [oai_citation:37‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧰 Example: minimal artifact pack

**Files**
- `layers/kfm.example.points.v0.geojson`
- `metadata/kfm.example.points.v0.manifest.json`
- `metadata/kfm.example.points.v0.prov.jsonld`
- `metadata/kfm.example.points.v0.checksums.sha256`

**GeoJSON (tiny example)**
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "pt-0001",
      "properties": {
        "name": "Example Point",
        "kfm:dataset_id": "kfm.example.points.v0",
        "kfm:sensitivity": "public"
      },
      "geometry": { "type": "Point", "coordinates": [-97.3301, 37.6872] }
    }
  ]
}
```

**Manifest (what we care about)**
- dataset_id, run_id, inputs + hashes, parameters, license, sensitivity, tool versions, timestamps  
Because governance and provenance are enforced at multiple checkpoints, missing license/sensitivity/provenance should be treated as a “fail closed” condition.  [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧯 Common gotchas (quick fixes)

- **Lat/Lon swapped** → your geometry “teleports” (bounds check catches this).  [oai_citation:39‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  
- **Wrong projection** → reproject to WGS84/EPSG:4326 before export.  [oai_citation:40‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  
- **Sensitive points accidentally exposed** → aggregate/generalize + mark classification; never publish less-restricted derivatives.  [oai_citation:41‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:42‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **“It’s just an experiment” mindset** → experiments still need provenance; KFM’s culture expects evidence-backed outputs (even AI/narrative outputs must cite sources).  [oai_citation:43‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:44‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

---

## 🧷 PR-ready checklist (copy/paste)

- [ ] GeoJSON is WGS84 (EPSG:4326) + bounds-safe  [oai_citation:45‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  
- [ ] Sidecar manifest includes: license + sensitivity + run context  [oai_citation:46‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- [ ] Checksums recorded  [oai_citation:47‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- [ ] Provenance attached (PROV)  [oai_citation:48‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- [ ] If promoting: STAC/DCAT/PROV completeness + policy gates pass  [oai_citation:49‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

---

### 🔗 See also (in-repo neighbors, if present)
- `../pmtiles/` (vector tiles) 🧱
- `../geoparquet/` (analytics-friendly tables) 🧮
- `../../validation/` (policy gates / QA harness) 🧪
