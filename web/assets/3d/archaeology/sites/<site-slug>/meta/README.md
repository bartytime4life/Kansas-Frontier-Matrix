# 🏺 Archaeology Site Meta Pack — `<site-slug>`  

![KFM](https://img.shields.io/badge/KFM-archaeology_site_meta-blue)
![Evidence%20First](https://img.shields.io/badge/Evidence--First-Required-success)
![STAC](https://img.shields.io/badge/STAC-Catalog-orange)
![DCAT](https://img.shields.io/badge/DCAT-Dataset_Metadata-orange)
![PROV](https://img.shields.io/badge/PROV-Lineage-orange)
![Sensitive%20Safe](https://img.shields.io/badge/Sensitive_Sites-Location_Generalization-critical)

> 📌 **Purpose:** This `meta/` folder is the **contract** that makes a 3D archaeology site *discoverable, citable, safe-to-display,* and *traceable* across KFM’s UI, API, and knowledge graph.

---

## 🧭 What KFM expects (design constraints)

These constraints shape everything in this folder:

- **Evidence-first + provenance-first**: nothing in KFM should be a “black box”; outputs must remain traceable to sources and processing steps. :contentReference[oaicite:0]{index=0}  
- **Contract-first metadata**: KFM uses machine-readable JSON metadata as an enforced contract (not just notes), aligned to open standards (STAC/DCAT/PROV). :contentReference[oaicite:1]{index=1}  
- **2D + 3D map UI**: KFM’s web stack uses **MapLibre** (2D) and **Cesium** (3D), streaming **3D Tiles** and supporting narrative layers. :contentReference[oaicite:2]{index=2}  
- **Story Nodes are first-class content** (Markdown + structured JSON, with citations/evidence links). :contentReference[oaicite:3]{index=3}  
- **Sensitive site safety is mandatory**: archaeological sites may require **location generalization** (e.g., a hexagon instead of exact coordinates) to reduce looting risk, plus access controls and explicit permission for precise data. :contentReference[oaicite:4]{index=4}  
- **Policy gates are “fail-closed”**: schema checks, STAC/DCAT/PROV completeness, license presence, sensitivity classification, and provenance completeness must pass before publish. :contentReference[oaicite:5]{index=5}  
- **Deterministic pipelines + immutable raw evidence**: raw data is read-only; processing is config/code-driven; manual edits to processed outputs are disallowed. :contentReference[oaicite:6]{index=6}  
- **Focus Mode AI is advisory + citation-bound**: it always cites sources and may refuse to answer if it can’t cite or if content is sensitive. :contentReference[oaicite:7]{index=7}  
- **Offline packs are a target**: KFM is designed so MapLibre/Cesium can run with pre-packaged data bundles for field/museum/offline use. :contentReference[oaicite:8]{index=8}

---

## 📁 Folder layout (inside `web/assets/3d/archaeology/sites/<site-slug>/`)

```text
📁 web/assets/3d/archaeology/sites/<site-slug>/
  📁 meta/                       👈 you are here
    📄 README.md
    📄 site.json                 ✅ required (site identity + public-safe geometry)
    📄 assets.json               ✅ required (what files exist + how to load them)
    📄 stac.collection.json      ✅ required (or a stac.item.json if single-item)
    📁 stac.items/               ✅ recommended (scan-by-scan / survey-by-survey)
      📄 <item-id>.json
    📄 dcat.dataset.jsonld       ✅ required (dataset-level citation + license)
    📄 prov.jsonld               ✅ required (lineage / chain-of-custody)
    📄 checksums.sha256          ✅ required (integrity + reproducibility)
    📄 evidence_manifest.yaml    ⭐ recommended (claims ↔ evidence inventory)
    📁 thumbnails/               ⭐ recommended
      🖼️ hero.webp
      🖼️ preview.webp
  📁 tiles/                      (3D Tiles, point cloud tiles, etc.)
    📄 tileset.json
  📁 models/                     (glTF/GLB, OBJ, etc.)
  📁 textures/
  📁 annotations/                (labels, hotspots, interpretive layers)
```

> ✅ **Rule:** If it appears in the public KFM UI, it must be backed by **STAC + DCAT + PROV** records and a sensitivity decision. :contentReference[oaicite:9]{index=9}

---

## 🏷️ Site slug rules

- Use **kebab-case** (lowercase, hyphens): `monument-rocks-arch-site`
- Keep it **stable forever** once published (it becomes part of URLs, IDs, citations, and provenance)

---

## 🧩 Core files and what they do

### 1) `site.json` — “Who/what is this place?” (public-safe)
This file defines the **site identity** and a **public-safe geometry**.

Minimum recommended fields:
- `id` (stable string or UUID)
- `slug`
- `name`
- `summary`
- `description` (keep interpretive claims citable)
- `tags[]`
- `time_range` (best-known; can be approximate)
- `geometry` (GeoJSON **WGS84/EPSG:4326**)
- `bbox` (WGS84)
- `sensitivity` (classification + display rules)
- `rights` (license, attribution, usage constraints)
- `links` to STAC/DCAT/PROV files

> 🌍 KFM standardizes on **WGS84 (EPSG:4326)** for web consistency (other CRSs can exist in provenance, but public display aligns to WGS84). :contentReference[oaicite:10]{index=10}

#### 🔒 Sensitive location policy (required)
If the site is sensitive:
- **Do not publish exact point coordinates** in this public repo.
- Prefer **generalized geometry** (hex polygon, coarse bounding region), or hide geometry entirely and rely on restricted access workflows. :contentReference[oaicite:11]{index=11}

---

### 2) `assets.json` — “What files exist and how do I load them?”
This is the **runtime manifest** the web viewer (and offline pack builder) uses.

Each asset entry should include:
- `asset_id`
- `role` (e.g., `tileset`, `model`, `pointcloud`, `dem`, `orthophoto`, `thumbnail`, `annotation`)
- `href` (relative path **or** OCI distribution reference)
- `type` (MIME)
- `format` (e.g., `3d-tiles`, `glb`, `laz`, `cog`)
- `crs` (EPSG, if relevant)
- `size_bytes`
- `checksum_sha256`
- `provenance_ref` (pointer into `prov.jsonld`)

#### 📦 Large binary guidance
If assets are large (tilesets, point clouds), consider treating them as **data artifacts** (like packages), not “random binaries,” so they can be versioned and verified.

KFM explores storing artifacts in **OCI registries** using **ORAS** and signing with **Cosign** for integrity and provenance. :contentReference[oaicite:12]{index=12}  
This can be referenced from metadata via an OCI distribution entry. :contentReference[oaicite:13]{index=13}

---

### 3) `stac.collection.json` + `stac.items/*.json` — “Where/when/what?”
Use STAC as the **primary geospatial catalog surface** for the site’s 3D and related assets.

KFM describes STAC records as answering:  
- **What** the dataset is  
- **Where** it applies (bbox/geometry)  
- **When** it applies (temporal extent)  
- **Which files exist** (assets + links)  
…and linking to provenance. :contentReference[oaicite:14]{index=14}

✅ Recommended pattern:
- `stac.collection.json` = site-level umbrella  
- `stac.items/<item-id>.json` = each capture/survey/scan date or each derived product  

---

### 4) `dcat.dataset.jsonld` — “How do we cite and reuse this?”
DCAT is your **dataset-level citation record**:
- title, description, publisher/creator
- license
- keywords/themes
- distribution links (HTTP and/or OCI)
- contact / attribution

> 🧾 KFM makes license presence and metadata completeness non-optional via policy gates. :contentReference[oaicite:15]{index=15}

---

### 5) `prov.jsonld` — “How was it made?”
PROV should include:
- inputs (raw scans, LiDAR, photos, field notes)
- activities (photogrammetry build, meshing, decimation, tiling, coordinate alignment)
- agents (people, tools, CI)
- parameters + tool versions where possible

KFM treats provenance as mandatory for anything that reaches graph/UI use (including streaming or dynamic outputs). :contentReference[oaicite:16]{index=16}

⭐ Optional but powerful: attach a **run manifest** / pipeline ledger (run_id, tool versions, digests) for auditability. :contentReference[oaicite:17]{index=17}

---

### 6) `evidence_manifest.yaml` — “Claims ↔ evidence inventory” (recommended)
If your `site.json` description includes interpretive claims (“this structure dates to…”, “occupation period…”, “associated with…”), keep a compact manifest listing:
- cited sources (documents, datasets)
- IDs/URIs
- query parameters / timestamps
- checksums where applicable

KFM’s “evidence manifest” pattern is designed so a reader can drill down and verify narrative claims from the exact supporting materials. :contentReference[oaicite:18]{index=18}

---

## 🧠 How the KFM UI + AI will use this folder

### 🗺️ Map + 3D Viewer
KFM’s web stack supports 2D + 3D integration:
- 2D map navigation + layers (MapLibre)
- 3D terrain + streamed 3D data (Cesium + 3D Tiles) :contentReference[oaicite:19]{index=19}

Your `assets.json` and STAC records are what make the viewer able to:
- locate the tileset/model
- decide which LOD(s) to load
- show **citations + provenance links** in the site panel

### 🧾 “Map behind the map” (trust UI)
KFM’s UI philosophy explicitly includes exposing provenance: users can see the “map behind the map” (where it came from, how it was processed). :contentReference[oaicite:20]{index=20}

### 🤖 Focus Mode
Focus Mode uses the knowledge graph + catalogs to answer questions with citations and guardrails. It’s advisory and can refuse if it cannot safely cite. :contentReference[oaicite:21]{index=21}

### ⚡ Pulse Threads + Concepts (optional future linkages)
If you connect this site to emergent updates (new survey, preservation threat, wildfire exposure), KFM proposes **Geotagged Pulse Threads** that:
- are stored as graph nodes
- include provenance metadata + an evidence manifest
- appear as map popups or a side-panel feed :contentReference[oaicite:22]{index=22}

For thematic discovery, KFM also proposes **Conceptual Attention Nodes** (e.g., “cultural heritage”) used both by the AI and UI as a lens/filter. :contentReference[oaicite:23]{index=23}

---

## 🧱 Publishing workflow (recommended)

1) **Pick classification early**  
   Decide whether this site is public-safe, restricted, confidential, or culturally sensitive.  
   If sensitive: prepare generalized geometry and redact precise coordinates. :contentReference[oaicite:24]{index=24}

2) **Create `site.json` + `assets.json` first**  
   Treat these as the “front door” contract.

3) **Generate STAC + DCAT + PROV**  
   These are the boundary artifacts that let data flow downstream into graph/API/UI. :contentReference[oaicite:25]{index=25}

4) **Integrity pass**  
   Compute checksums; keep a deterministic build chain. KFM’s ingestion gate patterns emphasize checksums + structured logs. :contentReference[oaicite:26]{index=26}

5) **Policy gate validation**  
   KFM uses automated checks (policy gates) that block merges on violations. :contentReference[oaicite:27]{index=27}

> 🔐 Reminder: no secrets in the repo (API keys, tokens, credentials). :contentReference[oaicite:28]{index=28}

---

## ✅ QA checklist (copy/paste)

- [ ] `site.json` exists and is public-safe  
- [ ] WGS84 geometry + bbox are present (or intentionally withheld for sensitivity) :contentReference[oaicite:29]{index=29}
- [ ] `assets.json` includes checksums for each artifact  
- [ ] STAC + DCAT + PROV exist and cross-link each other (links/refs) :contentReference[oaicite:30]{index=30}
- [ ] License + attribution are explicit (DCAT + site.json rights) :contentReference[oaicite:31]{index=31}
- [ ] Sensitivity classification is set and consistent; outputs aren’t less restricted than inputs :contentReference[oaicite:32]{index=32}
- [ ] Provenance describes: inputs, activities, agents, tools/versions  
- [ ] (If interpretive claims) `evidence_manifest.yaml` is present and complete :contentReference[oaicite:33]{index=33}
- [ ] Viewer loads in 2D/3D mode without console errors (tileset.json reachable)

---

## 🧪 Templates (starter files)

<details>
<summary><strong>🧾 site.json (template)</strong></summary>

```json
{
  "id": "kfm:archaeology-site:<site-slug>",
  "slug": "<site-slug>",
  "name": "<Site Display Name>",
  "summary": "<1–2 sentence summary for UI cards>",
  "description": "<Longer description. Keep interpretive claims citable via evidence_manifest.yaml>",
  "tags": ["archaeology", "cultural-heritage", "3d"],
  "time_range": {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD",
    "certainty": "approximate"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
  },
  "bbox": [0, 0, 0, 0],
  "crs": "EPSG:4326",
  "sensitivity": {
    "level": "public | restricted | confidential | sacred",
    "location_display": "exact | generalized | hidden",
    "rationale": "<why>",
    "authority": "<who approved (if applicable)>"
  },
  "rights": {
    "license": "<SPDX or clear text>",
    "attribution": "<how to cite / credit>",
    "usage_constraints": "<e.g., non-commercial, community-approved terms>"
  },
  "links": {
    "assets_manifest": "./assets.json",
    "stac_collection": "./stac.collection.json",
    "dcat_dataset": "./dcat.dataset.jsonld",
    "provenance": "./prov.jsonld",
    "evidence_manifest": "./evidence_manifest.yaml"
  }
}
```
</details>

<details>
<summary><strong>📦 assets.json (template)</strong></summary>

```json
{
  "site_slug": "<site-slug>",
  "version": "0.1.0",
  "assets": [
    {
      "asset_id": "tileset-main",
      "role": "tileset",
      "href": "../tiles/tileset.json",
      "type": "application/json",
      "format": "3d-tiles",
      "crs": "EPSG:4978",
      "size_bytes": 0,
      "checksum_sha256": "<sha256>",
      "provenance_ref": "prov:entity:tileset-main"
    },
    {
      "asset_id": "hero-image",
      "role": "thumbnail",
      "href": "./thumbnails/hero.webp",
      "type": "image/webp",
      "format": "image",
      "size_bytes": 0,
      "checksum_sha256": "<sha256>",
      "provenance_ref": "prov:entity:hero-image"
    }
  ],
  "distribution": {
    "mode": "relative | oci",
    "oci": {
      "registry": "ghcr.io",
      "repository": "<org>/<repo>/<artifact>",
      "tag": "<version-tag>",
      "digest": "sha256:<digest>",
      "files": [
        {
          "path": "tileset.json",
          "media_type": "application/json"
        }
      ]
    }
  }
}
```

</details>

---

## 🧰 Implementation notes (3D + geospatial)

- For geospatial calculations (buffers, area, distance), use a meter-based CRS (UTM/State Plane), then convert back to WGS84 for web delivery; track CRS changes in provenance.   
- KFM’s broader mapping architecture emphasizes open web mapping libraries (MapLibre/Leaflet), with Cesium considered for 3D and Cesium-friendly formats like 3D Tiles or CZML. :contentReference[oaicite:35]{index=35}

---

## 🛡️ Privacy + safety (extra)

If you publish aggregated or derived site metrics (visitation counts, sensor summaries, etc.), consider formal privacy-preserving methods such as k-anonymity / l-diversity / t-closeness / differential privacy as appropriate. 

---

## 📚 Project references (all core project files)

> These docs are the “why” behind this folder’s contract and policies.

- 🧭 UI architecture & experience: :contentReference[oaicite:37]{index=37} :contentReference[oaicite:38]{index=38}  
- 📥 Data intake (provenance-first pipeline, gates, catalogs): :contentReference[oaicite:39]{index=39} :contentReference[oaicite:40]{index=40}  
- 🏗️ Comprehensive architecture & policy gates: :contentReference[oaicite:41]{index=41} :contentReference[oaicite:42]{index=42}  
- 🤖 AI system overview (Focus Mode constraints + citations): :contentReference[oaicite:43]{index=43} :contentReference[oaicite:44]{index=44}  
- 🧪 Technical documentation (web stack + 2D/3D): :contentReference[oaicite:45]{index=45} :contentReference[oaicite:46]{index=46}  
- 💡 Innovative concepts (AR + immersive storytelling direction): :contentReference[oaicite:47]{index=47} :contentReference[oaicite:48]{index=48}  
- 🌟 Latest ideas / proposals (timeline, packaging patterns, offline packs): :contentReference[oaicite:49]{index=49} :contentReference[oaicite:50]{index=50}  
- 🧠 Additional ideas (Pulse Threads, Concept Nodes, OCI artifacts): :contentReference[oaicite:51]{index=51} :contentReference[oaicite:52]{index=52}  
- 🗺️ Open-source mapping hub design (MapLibre/Leaflet + Cesium direction): :contentReference[oaicite:53]{index=53}  
- 🧰 Geospatial coding cookbook (projection + workflow helpers): :contentReference[oaicite:54]{index=54}  
- 📦 Reference libraries (PDF portfolios — open in Adobe Reader for embedded docs):  
  - 🗺️ WebGL / maps / archaeology graphics portfolio: :contentReference[oaicite:55]{index=55} :contentReference[oaicite:56]{index=56}  
  - 🤖 AI concepts portfolio: :contentReference[oaicite:57]{index=57} :contentReference[oaicite:58]{index=58}  
  - 🧱 Data management theories portfolio: :contentReference[oaicite:59]{index=59} :contentReference[oaicite:60]{index=60}  
  - 🧑‍💻 Programming languages/resources portfolio: :contentReference[oaicite:61]{index=61} :contentReference[oaicite:62]{index=62}  
- 📘 Data mining concepts (privacy + methods background): :contentReference[oaicite:63]{index=63}  

---

## 🧾 Glossary (KFM-native)

- **Policy gate**: automated rules (CI) that block merges when metadata/governance requirements are unmet. :contentReference[oaicite:64]{index=64}  
- **OCI artifact distribution**: storing data artifacts (tilesets, models, PMTiles, etc.) in an OCI registry, versioned by digest. :contentReference[oaicite:65]{index=65}  
- **Cosign signature**: cryptographic signing for origin + integrity of artifacts. :contentReference[oaicite:66]{index=66}  
- **Evidence manifest**: a compact inventory of “what evidence supports which claims,” enabling verification. :contentReference[oaicite:67]{index=67}  

---

### ✅ Done when…
This folder can stand alone as a **portable site pack**:
- discoverable (STAC/DCAT)
- traceable (PROV + checksums)
- safe (sensitivity + generalized geometry if needed)
- viewable (assets manifest for MapLibre/Cesium UI)

