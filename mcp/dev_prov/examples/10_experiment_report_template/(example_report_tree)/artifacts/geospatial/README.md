# 🗺️ Geospatial Artifacts (Experiment Report Bundle)

![STAC](https://img.shields.io/badge/STAC-JSON-0B7285?style=flat&logo=json&logoColor=white)
![DCAT](https://img.shields.io/badge/DCAT-catalog-4C6EF5?style=flat)
![PROV](https://img.shields.io/badge/PROV--O-lineage-845EF7?style=flat)
![GeoJSON](https://img.shields.io/badge/GeoJSON-vector-2F9E44?style=flat)
![GeoParquet](https://img.shields.io/badge/GeoParquet-columnar-2B8A3E?style=flat)
![COG](https://img.shields.io/badge/COG-raster-1864AB?style=flat)
![PMTiles](https://img.shields.io/badge/PMTiles-vector%20tiles-0C8599?style=flat)
![3D%20Tiles](https://img.shields.io/badge/3D%20Tiles-Cesium-1C7ED6?style=flat)
![MapLibre](https://img.shields.io/badge/MapLibre-2D%20viewer-212529?style=flat)
![Cesium](https://img.shields.io/badge/Cesium-3D%20viewer-343A40?style=flat)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-auditable-FF922B?style=flat)

> 📍 **Purpose:** This folder is the **portable, audit-friendly** home for any **geospatial outputs** produced by the experiment (maps, layers, tiles, rasters, 3D assets) packaged with **provenance + governance** so they can be rendered in KFM-style UIs (MapLibre/Cesium), reviewed, and reused later.

---

## 📌 Contents

- [✅ What belongs here](#-what-belongs-here)
- [🧭 Golden rules](#-golden-rules)
- [🗂️ Suggested folder layout](#️-suggested-folder-layout)
- [📦 Supported artifact types](#-supported-artifact-types)
- [🧾 Metadata + provenance (Evidence-First)](#-metadata--provenance-evidence-first)
- [🧪 QA & policy gates](#-qa--policy-gates)
- [👀 Viewing (2D/3D) + publishing](#-viewing-2d3d--publishing)
- [🔗 Hooking into Story Nodes / Pulse Threads](#-hooking-into-story-nodes--pulse-threads)
- [📦 Optional: OCI registry distribution](#-optional-oci-registry-distribution)
- [🛡️ Sensitivity & ethics](#️-sensitivity--ethics)
- [🧯 Troubleshooting](#-troubleshooting)
- [✅ Contributor checklist](#-contributor-checklist)

---

## ✅ What belongs here

Put **experiment outputs** that are inherently spatial (or time+space):

- 🧭 **Vector** results (boundaries, points, routes, extracted placenames-as-features)
- 🛰️ **Raster** results (classified imagery, interpolations, gridded time series, scanned map mosaics)
- 🧱 **Tiles** (vector tiles for fast web rendering, time-sliced tiles, regionated packages)
- 🌍 **3D assets** (terrain, point clouds, historical 3D reconstructions)
- 🖼️ **Previews** (thumbnails, screenshots, small HTML viewers)
- 🧾 **Metadata** (STAC/DCAT/PROV) and integrity (checksums, signatures)

> 🚫 **Not for:** raw source dumps, scratch outputs, or transient intermediates.  
> Those belong in a `data/raw/` or `data/work/` style area (outside an experiment report) — this folder is for **final/published artifacts** for the report.

---

## 🧭 Golden rules

### 🧠 Reuse-first formats (open + web-friendly)
- Prefer **GeoParquet** for large vectors, **COG** for rasters, **PMTiles** for web tiles.
- Use **GeoJSON** only for small outputs or API-like payloads.

### 🌐 Web display defaults
- Provide a web-ready version in **EPSG:4326 (WGS84)** when practical.
- If calculations require a projected CRS, keep that too — but **record CRS + transforms** in provenance.

### ⏱️ Time is a first-class filter
If your artifact is time-aware, make time explicit:
- Use ISO 8601 timestamps.
- Prefer “one Collection + many Items” (per time slice) in STAC.

### 🧾 Evidence-first by default
Every artifact should be defensible:
- **What is it?** (metadata)
- **Where did it come from?** (provenance)
- **Who/what produced it?** (agents + run id)
- **Can I verify it?** (checksums + signatures)

---

## 🗂️ Suggested folder layout

> You can simplify this if your experiment is small — but keep **metadata + checksums** no matter what.

```text
📁 artifacts/
  📁 geospatial/
    📄 README.md

    📁 layers/                       # "human-scale" vectors (ready for analysis + review)
      📁 <artifact_id>/
        📄 data.geoparquet           # preferred (or .geojson for small)
        📄 schema.json               # optional (but great for QA)
        🖼️ preview.png               # tiny map snapshot
        📄 stac.item.json            # ✅ required for publishable outputs
        📄 dcat.json                 # ✅ required for catalog interoperability
        📄 prov.jsonld               # ✅ required for lineage
        📄 checksums.sha256          # ✅ required for integrity

    📁 rasters/                      # imagery / grids / scanned maps (COG preferred)
      📁 <artifact_id>/
        📄 data.cog.tif
        🖼️ preview.png
        📄 stac.item.json
        📄 prov.jsonld
        📄 checksums.sha256

    📁 tiles/                        # web speed packs
      📁 <artifact_id>/
        📄 tiles.pmtiles             # preferred single-file vector tiles
        📄 tilejson.json             # map client config
        🖼️ preview.png
        📄 stac.item.json
        📄 prov.jsonld
        📄 checksums.sha256

    📁 3d/                           # Cesium-friendly packages
      📁 <artifact_id>/
        📄 tileset.json              # 3D Tiles entrypoint
        📁 content/                  # b3dm/i3dm/pnts/etc
        🖼️ preview.png
        📄 stac.item.json
        📄 prov.jsonld
        📄 checksums.sha256

    📁 previews/                     # optional: richer previews for humans
      📄 index.html                  # mini viewer (static)
      📁 screenshots/
        🖼️ step_01.png
        🖼️ step_02.png

    📁 _meta/                        # experiment-level metadata (optional but recommended)
      📄 artifact-index.json         # list of all geospatial artifacts in this folder
      📄 run_manifest.json           # run id + params + tool versions + digests
      📄 evidence_manifest.yml       # story/pulse-ready evidence ledger
```

---

## 📦 Supported artifact types

| Type 🧩 | Best format ✅ | OK formats 👍 | Primary viewer 👀 | Notes 📝 |
|---|---|---|---|---|
| Vector layers | **GeoParquet** | GeoJSON, GeoPackage | MapLibre / QGIS | Use GeoJSON only if small. |
| Raster layers | **COG (GeoTIFF)** | GeoTIFF, NetCDF (document carefully) | MapLibre (COG range) / QGIS | COG enables HTTP range reads for static hosting. |
| Web tiles | **PMTiles** | MBTiles + TileJSON | MapLibre | PMTiles keeps “one file per tileset”. |
| 3D assets | **3D Tiles / CZML** | glTF (if small) | Cesium | Favor streamed tiles for large content. |
| Google Earth exports | KML/KMZ | — | Google Earth | Use for lightweight 3D sharing if needed. |

---

## 🧾 Metadata + provenance (Evidence-First)

KFM-style pipelines standardize on a **metadata backbone**:

- 🛰️ **STAC** → describes spatial+temporal assets
- 🗃️ **DCAT** → catalog-friendly interoperability record
- 🧬 **PROV-O** → lineage: Entity / Activity / Agent

### ✅ Minimum required per artifact folder
- `stac.item.json` (or `stac.collection.json` if you bundle a collection)
- `prov.jsonld`
- `checksums.sha256`
- `preview.png` (strongly recommended)
- `license` field present in at least one metadata doc (STAC or DCAT)

---

### 🛰️ STAC: recommended pattern for time-enabled layers

If your output is time-sliced:
- Create **one** `stac.collection.json` at `layers/<artifact_id>/`
- Create **many** `items/<timestamp>/stac.item.json` referencing the right asset(s)

<details>
<summary>📄 Minimal STAC Item skeleton (copy/paste)</summary>

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "<artifact_id>__<time_or_slice>",
  "collection": "<artifact_id>",
  "bbox": [ -102.05, 36.99, -94.59, 40.00 ],
  "geometry": { "type": "Polygon", "coordinates": [] },
  "properties": {
    "datetime": "1850-01-01T00:00:00Z",
    "title": "<human title>",
    "license": "CC-BY-4.0"
  },
  "assets": {
    "data": {
      "href": "./data.geoparquet",
      "type": "application/x-parquet",
      "roles": ["data"]
    },
    "preview": {
      "href": "./preview.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    }
  }
}
```
</details>

---

### 🧬 PROV: what we expect to see

At minimum, your `prov.jsonld` should link:
- **Entity** → the produced artifact file(s)
- **Activity** → the experiment run step(s) that produced them
- **Agent** → the tool/person/CI identity

Include:
- `run_id` (or equivalent)
- Git SHA / version for code that produced it
- Input dataset identifiers or source URLs
- Transformation notes (reprojection, filters, joins, QA steps)

<details>
<summary>🧬 Minimal PROV JSON-LD skeleton (copy/paste)</summary>

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@graph": [
    {
      "@id": "urn:kfm:entity:<artifact_id>",
      "@type": "prov:Entity",
      "prov:label": "<artifact_id>",
      "prov:value": "layers/<artifact_id>/data.geoparquet",
      "prov:wasGeneratedBy": { "@id": "urn:kfm:activity:<run_id>" }
    },
    {
      "@id": "urn:kfm:activity:<run_id>",
      "@type": "prov:Activity",
      "prov:startedAtTime": { "@value": "2026-01-22T00:00:00Z", "@type": "xsd:dateTime" },
      "prov:wasAssociatedWith": { "@id": "urn:kfm:agent:<actor>" },
      "prov:used": [
        { "@id": "urn:kfm:entity:<input_dataset_id>" }
      ]
    },
    {
      "@id": "urn:kfm:agent:<actor>",
      "@type": "prov:Agent",
      "prov:label": "<name or CI>",
      "prov:type": "software"
    }
  ]
}
```
</details>

---

### 🗃️ DCAT: why we include it

DCAT makes your artifact easier to index, federate, and expose through catalogs.

**Good DCAT practice here:**
- Include **license**
- Include an **access URL** (local path or API endpoint)
- Optionally include **distribution** entries for:
  - local file path
  - OCI registry digest (see below)
  - web preview page

---

### 🧾 Evidence manifest (for Story Nodes + Pulse Threads)

If your experiment report includes narratives (Story Nodes) or “Pulse” updates:
- maintain an `evidence_manifest.yml` that lists each map artifact + its claims + source links.

This keeps the report **auditable** and supports “hover provenance” UI patterns.

<details>
<summary>🧾 Evidence manifest example (copy/paste)</summary>

```yaml
version: 1
experiment_id: "<experiment_id>"
run_id: "<run_id>"

evidence:
  - id: "ev-001"
    artifact_id: "<artifact_id>"
    kind: "geospatial.layer"
    file: "layers/<artifact_id>/data.geoparquet"
    stac: "layers/<artifact_id>/stac.item.json"
    prov: "layers/<artifact_id>/prov.jsonld"
    claim:
      text: "This layer represents extracted place mentions from letters (1850–1860)."
      confidence: 0.84
    sources:
      - source_id: "<input_dataset_id_or_url>"
        note: "Original letters corpus (curated)"
    integrity:
      sha256: "<sha256>"
    governance:
      sensitivity: "public"
      license: "CC-BY-4.0"
```
</details>

---

### 🧾 Run manifest (experiment-level)

Place a `_meta/run_manifest.json` to pin:
- run id
- parameters / config
- tool versions (GDAL, python libs, model ids)
- input IDs + checksums
- output digests
- **idempotency key** (if your pipeline supports it)

> 🎯 Goal: a reviewer can prove that “processed outputs are fully reproducible from raw + code”.

---

## 🧪 QA & policy gates

Treat data artifacts like software artifacts ✅

### ✅ Required checks (CI-friendly)
- [ ] **Checksums present** for every “primary” asset (data file, tileset, COG, tileset.json)
- [ ] **License present** (STAC/DCAT) and compatible with sources
- [ ] **CRS recorded** (and reprojection documented if performed)
- [ ] **Geometry validity** (no self-intersections, correct winding where applicable)
- [ ] **Bounding box matches** actual data extent (sanity check)
- [ ] **Time fields valid ISO 8601** if time-aware
- [ ] **Sensitivity tags** present (`public / restricted / sensitive`) if applicable
- [ ] **PROV links resolve** (paths exist, run_id exists, inputs referenced exist)

### 🔒 Policy-as-code (recommended)
Use OPA/Conftest-style policy packs to enforce:
- license field required
- provenance required
- “no sensitive data without redaction/generalization”
- disallow restricted sources without auth controls

---

## 👀 Viewing (2D/3D) + publishing

### 🗺️ 2D: MapLibre-first
- Use **PMTiles** for high-performance vector rendering.
- Use **COGs** for rasters (static hosting friendly).

Suggested deliverables for web display:
- `tiles.pmtiles` + `tilejson.json`
- `data.cog.tif` + `preview.png`

### 🌍 3D: Cesium-ready
For 3D storytelling or terrain context:
- ship `3D Tiles` (`tileset.json` + content/)
- optionally include **CZML** if time-dynamic

### 🧰 Desktop sanity checks
- QGIS is a great “truth check” for:
  - CRS correctness
  - alignment with basemaps
  - attribute sanity
  - raster statistics

---

## 🔗 Hooking into Story Nodes / Pulse Threads

If your experiment report supports KFM narrative patterns:

### 🧵 Pulse Threads (geo-tagged updates)
- Every pulse map update should reference:
  - the artifact id
  - evidence id(s)
  - where (bbox / geometry)
  - when (time slice)
  - why (claim + uncertainty)

### 🧠 Conceptual Attention Nodes (optional but powerful)
If your layer supports “concept-first navigation” (e.g., drought, migration, treaties):
- include tags/keywords in STAC/DCAT
- link concept identifiers into PROV as “used” inputs or as annotations

> 🧠 The idea: a user can find the map by concept **even if they don’t know a county name**.

---

## 📦 Optional: OCI registry distribution

For **large artifacts** (COGs, tilesets, 3D packages), consider storing them as **OCI artifacts** instead of (or in addition to) Git:

- ✅ standard tooling for transport (ORAS)
- ✅ signatures + provenance attachments (Cosign)
- ✅ registry access control for restricted/sensitive data

Suggested pattern:
- store local file in this folder (or a small “pointer” file)
- include OCI digest + ref in DCAT + STAC asset fields

<details>
<summary>📦 Example (conceptual) ORAS + Cosign flow</summary>

```bash
# Push (example — your registry + naming may differ)
oras push registry.example.org/kfm/geospatial/<artifact_id>:<version> \
  ./tiles.pmtiles:application/vnd.pmtiles \
  ./prov.jsonld:application/ld+json \
  ./stac.item.json:application/json

# Sign (keyless or key-based depending on your setup)
cosign sign registry.example.org/kfm/geospatial/<artifact_id>:<version>
```
</details>

---

## 🛡️ Sensitivity & ethics

If anything is **sensitive / restricted**:
- mark it in metadata
- consider **generalization** (e.g., hex bins instead of exact points)
- consider **removal of exact coordinates**
- ensure access control if stored in registries or published sites

🧷 UI expectation: sensitive layers should render with **lock / warning** indicators and/or be hidden for general users.

---

## 🧯 Troubleshooting

### “My GeoJSON is huge and the browser dies”
✅ Convert to:
- GeoParquet for analysis
- PMTiles for web rendering

### “My layer doesn’t line up”
Check:
- CRS mismatch
- wrong axis order
- missing transform step  
Fix:
- reproject to EPSG:4326 for web
- record original CRS in provenance

### “Tiles look different across time slices”
Usually:
- inconsistent classification bins
- missing time parameter in tile endpoint/build process
- caching collision  
Fix:
- include time slice in artifact id + TileJSON
- include time in STAC Item id

---

## ✅ Contributor checklist

Before committing:
- [ ] Data in open format (GeoParquet / COG / PMTiles preferred)
- [ ] `preview.png` included
- [ ] `stac.item.json` included
- [ ] `prov.jsonld` included
- [ ] `checksums.sha256` included
- [ ] license + sensitivity tagged
- [ ] artifact is referenced from the experiment report (link it!)
- [ ] if huge, consider OCI distribution instead of Git blob commits

---

### 🧭 Final note

This folder is intentionally **portable**: a reviewer should be able to pick up the experiment report tree, open the metadata, verify checksums, and understand **exactly** how each map output was produced — without requiring access to a live database or proprietary GIS tooling. ✨
