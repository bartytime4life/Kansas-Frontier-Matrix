# 🗺️ PMTiles Artifacts (Template) — `artifacts/geospatial/pmtiles/`

![Artifact](https://img.shields.io/badge/artifact-PMTiles-2b6cb0)
![Type](https://img.shields.io/badge/type-vector%20tiles-0f766e)
![Use](https://img.shields.io/badge/use-offline%20%26%20fast%20maps-7c3aed)
![Governance](https://img.shields.io/badge/governance-provenance--first-f97316)

> **Goal:** This folder holds **PMTiles** outputs (single-file vector tile archives) produced by an experiment run—optimized for **high-performance rendering** and **offline “packs”** in the KFM ecosystem. KFM explicitly calls out offline bundles that may include **pre-rendered map tiles** such as **PMTiles** (or MBTiles), alongside a mini-app for local navigation.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 📦 What belongs here (and why)

KFM’s mapping stack uses MapLibre for 2D and Cesium for 3D, and discusses **offline packs** where the map viewer points at **local tile sources**.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
It also calls out **Tippecanoe/PMTiles** as part of the geospatial tooling for generating vector tile sets for the web.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

A concrete pattern appears in the “surficial geology package” idea: produce **GeoParquet (analysis)** + **PMTiles (visualization)** from the same source, and register artifacts via metadata.  [oai_citation:4‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 🧱 Expected folder layout

```text
📁 artifacts/
  📁 geospatial/
    📁 pmtiles/
      ├─ README.md                    👈 you are here
      ├─ <layer_id>.pmtiles           ✅ primary artifact
      ├─ <layer_id>.style.json        ✅ MapLibre style snippet (or full style)
      ├─ <layer_id>.preview.png       ✨ optional quicklook
      ├─ checksums.sha256             ✅ integrity (at least the .pmtiles)
      ├─ metadata/
      │   ├─ stac.item.json           ✅ STAC pointer(s) to assets + extent
      │   ├─ dcat.dataset.jsonld       ✅ DCAT discovery + licensing
      │   └─ prov.jsonld              ✅ PROV lineage (inputs + process)
      └─ oci/                         ✨ optional publishing helpers
          ├─ distribution.oci.yaml
          └─ signing/                 (cosign bundles/notes if used)
```

### ✅ Required files (minimum bar)
- `*.pmtiles`
- `checksums.sha256`
- `metadata/stac.item.json`, `metadata/dcat.dataset.jsonld`, `metadata/prov.jsonld`  
  KFM treats **STAC/DCAT/PROV** as the metadata backbone for discoverability + traceability.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### ✨ Optional but recommended
- `*.style.json` (to make “drop-in” map usage easy)
- `*.preview.png` (for reports, PRs, and catalog browsing)
- `oci/` content if you publish artifacts as OCI blobs (see below)

---

## 🧪 Experiment vs. “official” data (promotion rule)

This template is meant for **experiment reports** and work-in-progress outputs. KFM’s workflow emphasizes **sandbox vs. promotion**: experimental results are not considered “official” until reviewed and promoted alongside catalogs and provenance.  [oai_citation:6‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧭 Data contracts, provenance, and “no mystery layers”

KFM’s governance philosophy is contract-first and provenance-first: **no unsourced/ad-hoc layers** are allowed into the official catalog, and metadata is enforced via validators/CI.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
Policy gates are designed to **fail closed** on missing metadata, licensing, sensitivity classification, and provenance completeness.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### ✅ “Definition of Done” checklist (PMTiles)
- [ ] `*.pmtiles` generated deterministically (same inputs/config ⇒ same output)  [oai_citation:9‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] CRS decision documented; KFM’s web standard is **WGS84 (EPSG:4326)** for serving/display  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] `checksums.sha256` includes the PMTiles hash (and any sibling artifacts)
- [ ] `metadata/` includes STAC + DCAT + PROV links and license info  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] Sensitivity reviewed (and restricted distribution if needed)  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] If surfaced in UI/reporting, the UI can show “map behind the map” context (source + metadata links)  [oai_citation:13‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

---

## 🏗️ How PMTiles are typically produced (reference pipeline)

KFM describes using vector tiles for heavy layers and tooling like Tippecanoe for generation.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 🧩 Practical flow
1) **Prepare source vectors** (GeoJSON / GeoParquet / PostGIS query export)  
2) **Normalize CRS** for web serving (document any reprojection in PROV)  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
3) **Generate vector tiles** (e.g., Tippecanoe)  
4) **Package as PMTiles**  
5) **Write metadata + checksums**  
6) **(Optional) publish as OCI artifact** for versioned distribution

```mermaid
flowchart LR
  A[📥 Source data<br/>raw evidence] --> B[🧹 Clean/standardize<br/>deterministic ETL]
  B --> C[🧭 CRS normalize<br/>WGS84 for web]
  C --> D[🧩 Vector tiles<br/>Tippecanoe]
  D --> E[📦 PMTiles<br/>single-file archive]
  E --> F[🗂 STAC/DCAT/PROV<br/>metadata + lineage]
  F --> G[🔐 Checksums + (optional) signatures]
  G --> H[🌍 Served in UI / Offline pack]
```

KFM’s intake philosophy: **raw is immutable evidence**, transformations are controlled downstream, and outputs are traceable by design.  [oai_citation:16‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🌐 Using PMTiles in KFM UI (2D / 3D / Offline)

- **2D:** MapLibre GL JS is the core 2D renderer and is designed to work with self-hosted/pre-packaged data for offline usage.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **3D:** Cesium is integrated for 3D, and KFM plans offline patterns that can still leverage pre-packaged data.  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **Offline packs:** explicitly discussed as a distribution target, bundling layers + stories + pre-rendered tiles.  [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

> 🔎 **UX note:** KFM emphasizes surfacing provenance in the UI (layer info panels / provenance overlays) so users can inspect source, license, and prep summary.  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:22‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 📤 Publishing PMTiles as OCI artifacts (recommended distribution pattern)

KFM proposes storing artifacts like **PMTiles + GeoParquet** in an **OCI registry** using **ORAS**, and signing them with **Cosign** for integrity and provenance.  [oai_citation:23‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
This yields content-addressable versioning (digest + human tags) and supports attaching provenance/signatures as referrers.  [oai_citation:24‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:25‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Suggested media types
- `application/vnd.pmtiles`
- `application/vnd.geo+parquet`  [oai_citation:26‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### `oci/distribution.oci.yaml` (template)
```yaml
registry: ghcr.io
repository: <org>/<project>/<dataset_id>
tag: <yyyymmdd-or-semver>
digest: "sha256:<filled_after_push>"
artifacts:
  - file: "<layer_id>.pmtiles"
    mediaType: "application/vnd.pmtiles"
  - file: "<layer_id>.geo.parquet"
    mediaType: "application/vnd.geo+parquet"
provenance:
  stac: "../metadata/stac.item.json"
  dcat: "../metadata/dcat.dataset.jsonld"
  prov: "../metadata/prov.jsonld"
```

---

## 🔐 Security & privacy notes (don’t skip)

Even “processed outputs” can leak sensitive info; privacy research highlights that results can disclose information and that **query auditing / inference control** can deny queries that enable disclosure.  [oai_citation:27‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  
In KFM terms: ensure **sensitivity classification** and apply appropriate access controls (e.g., private OCI repos).  [oai_citation:28‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧰 QA / sanity checks (fast & practical)

### Visual check in QGIS (or similar)
A practical workflow is to open intermediate vectors and validate geometry/topology in GIS tools; QGIS is explicitly referenced as a place to inspect results.  [oai_citation:29‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

### CRS sanity check
OSM and many web datasets are in EPSG:4326; recipes often transform to EPSG:3857 for some operations, but KFM’s serving standard favors WGS84 for web consistency.  [oai_citation:30‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  [oai_citation:31‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🔭 Future-facing: PMTiles as a building block for AR & 4D storytelling

KFM’s roadmap and concept docs repeatedly push toward **mobile + offline + AR** experiences, with standardized services and governed data feeding new clients/modes.  [oai_citation:32‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  [oai_citation:33‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
PMTiles fits naturally as a **portable, cache-friendly** layer format for these experiences.

---

## 🗃️ Notes on bundled “reference PDFs” in this repo

Some reference packs are distributed as **PDF portfolios** that render best in Adobe Reader (Acrobat X or later), and may not extract cleanly in all tooling.  [oai_citation:34‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  [oai_citation:35‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)  [oai_citation:36‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  [oai_citation:37‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)

---

## ✍️ Why this README exists (reporting & evidence-first)

KFM treats Markdown as a first-class medium for provenance logs and technical reports, aiming for “evidence-first” documentation where claims are tied to references.  [oai_citation:38‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  
This README is the **human entrypoint** for the PMTiles artifact bundle in an experiment report.
