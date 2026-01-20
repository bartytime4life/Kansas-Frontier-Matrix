# 🗺️ 03_geospatial — MCP Notebooks (Kansas Frontier Matrix)

![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange?logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![PostGIS](https://img.shields.io/badge/PostGIS-spatial%20db-336791?logo=postgresql&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-knowledge%20graph-008CC1?logo=neo4j&logoColor=white)
![STAC](https://img.shields.io/badge/STAC-catalog-5b3cc4)
![DCAT](https://img.shields.io/badge/DCAT-metadata-0b7285)
![PROV](https://img.shields.io/badge/W3C-PROV-lineage-005A9C)
![COG](https://img.shields.io/badge/COG-cloud%20optimized%20GeoTIFF-2f9e44)
![PMTiles](https://img.shields.io/badge/PMTiles-tile%20archives-ff922b)
![MapLibre](https://img.shields.io/badge/MapLibre-2D%20maps-343a40?logo=openstreetmap&logoColor=white)
![Cesium](https://img.shields.io/badge/Cesium-3D%20globe-495057)

> **What this folder is:** a reproducible, *evidence-first* lab for KFM’s mapping stack — from **raw geo data ➜ PostGIS/tiles ➜ catalogs (STAC/DCAT/PROV) ➜ graph links ➜ UI-ready assets**.  
> **What MCP means here:** *Master Coder Protocol* — notebooks follow the scientific method + reproducible engineering standards.

---

## 🧭 Why this module exists

KFM’s core promise is the **“map behind the map”**: every visual layer can be traced back to its sources, metadata, and processing lineage — and the AI assistant must cite evidence, or refuse. ✅

This notebook set is where we prototype & validate:

- **Spatiotemporal mapping** (map + timeline, “what happened here in the 1930s?”)
- **Geospatial storage + query** (PostGIS “geo truth”, Neo4j “semantic context”)
- **Packaging + delivery** (COGs, vector tiles, PMTiles, GeoParquet)
- **2D/3D experiences** (MapLibre + Cesium, story-driven camera transitions)
- **Governance & safety** (licenses, sensitivity tags, coordinate generalization)

---

## 🗂️ Suggested folder layout

```text
📁 mcp/
  📁 notebooks/
    📁 03_geospatial/
      📄 README.md  👈 you are here
      📁 notebooks/             # .ipynb experiments (numbered)
      📁 data/                  # small sample inputs only (NO big rasters/tiles)
      📁 artifacts/             # generated outputs (tiles, COGs, GeoParquet, reports)
      📁 catalogs/              # STAC/DCAT/PROV outputs (or links/receipts)
      📁 policies/              # notebook-level policy checks (schemas, gates)
      📁 scratch/               # temporary work (gitignored)
```

> 🔒 **Rule of thumb:** large artifacts don’t live in Git. Store **receipts** (digests, URIs, manifests) + catalogs so results stay reproducible.

---

## 🧪 MCP Notebook Protocol (do this every time)

Each notebook is treated like a small experiment. Keep it runnable **top-to-bottom**.

### ✅ Required header block (top cell)
Include:
- **Question / Problem**
- **Background (links, sources, assumptions)**
- **Hypothesis (expected result)**
- **Method (steps + tools + parameters)**
- **Inputs & licenses**
- **Outputs (artifact list)**
- **Reproducibility (env + seeds + version IDs)**

### ✅ Required footer block (final cell)
- **Results** (what was produced, where)
- **Validation** (policy gates, schema checks, sanity plots)
- **Conclusion** (supports/refutes hypothesis)
- **Next steps** (what to pipeline / what to fix)

---

## 🧱 KFM Geospatial Invariants (don’t break these)

### 1) Evidence triplet is not optional 🧾
Every dataset/layer should be represented by:
- **STAC** for geospatial assets (bbox, time, assets)
- **DCAT** for dataset metadata + distributions (download/API/tiles)
- **PROV** for lineage (inputs, transforms, agents, versions)

If any piece is missing → it’s not “real” in KFM.

### 2) Policy gates must “fail closed” 🚧
Before publishing/serving:
- schema valid
- STAC/DCAT/PROV complete
- license present
- sensitivity classified + enforced
- provenance complete
- AI outputs cite sources (or refuse)

### 3) CRS discipline 🌐
- Preserve **original CRS** in metadata.
- Maintain a **canonical internal CRS** for consistency.
- If you generate web tiles, you’ll likely use **Web Mercator** for tiling.
- **Always record reprojection** as a PROV step.

> ⚠️ CRS mismatch is the #1 cause of “layers don’t line up”.

---

## 🗺️ Notebook Roadmap (recommended)

You can name notebooks however you like — this is a proven flow.

| Phase | Notebook goal | Typical outputs |
|------:|---------------|-----------------|
| 01 | Load a vector layer, validate schema, assign IDs | GeoJSON/GeoParquet + QC report |
| 02 | Reprojection & simplification (multi-zoom) | generalized layers + provenance |
| 03 | PostGIS ingest + spatial indexing | tables, indexes, query benchmarks |
| 04 | Vector tiles (PostGIS ST_AsMVT or external) | `.pbf` tiles or `.pmtiles` |
| 05 | Raster pipeline to COG | `.tif` COGs + tiling receipts |
| 06 | Timeline enablement (time ranges, events) | time-indexed catalogs |
| 07 | “Map behind map” linking (Neo4j) | graph nodes/edges linking datasets ↔ places ↔ events |
| 08 | Sensitivity & redaction (geo-obfuscation) | safe public layer variants |
| 09 | UI handoff (MapLibre/Cesium demos) | TileJSON, style stubs, 3D tiles receipts |
| 10 | Real-time / streaming intake (optional) | append-only observations + STAC items |

---

## 🧠 PostGIS + Neo4j: division of labor

**PostGIS = geo truth**
- heavy lifting: bbox filters, point-in-polygon, joins, stats, tile generation
- spatial indexing for performance

**Neo4j = semantic context**
- “what this is”, relationships, ontology terms, story links, provenance chains
- helps interpret queries like “events near X during Y”, then hands off counting to PostGIS

**API layer = enforcement boundary**
- UI clients should not run raw graph queries directly.
- All access goes through an API to apply redaction, licensing, and policy.

---

## 📦 Packaging patterns (fast + portable)

### ✅ Vector layers
- **GeoParquet** (analysis-friendly, columnar)
- **MVT tiles** (fast map rendering)
- **PMTiles** (single-file tile archives for offline + CDN)

### ✅ Raster layers
- **COG** (Cloud-Optimized GeoTIFF) for HTTP range reads + fast map view fetches
- Optional **pre-tiling** for heavy rasters that must be ultra-snappy

### ✅ Distribution & integrity (advanced)
Treat data artifacts like deployable software:
- publish artifacts to an **OCI registry**
- sign them (e.g., **Cosign**) and verify before use
- store immutable digests in catalogs/receipts

---

## 🧭 UI Integration Notes (MapLibre / Cesium / Timeline / Stories)

### 2D Map (MapLibre)
- render vector tiles / GeoJSON / raster tiles
- style is config-driven so other “Frontier Matrix” regions can reuse UI

### 3D Globe (Cesium)
- terrain, 3D models, and potential **3D Tiles** streaming
- ideal for “Kansas From Above”-style story flyovers and camera choreography

### Timeline
- every layer should declare a **time range** (even if “static”)
- timeline UI should filter layers + story scenes consistently

### AR + Offline (future-facing, but plan for it now)
- offline packs should bundle “just enough” geometry/tiles + catalogs
- AR mode uses subset layers & simplified geometry near user location

---

## 🔐 Governance: sensitive locations, privacy, and safe outputs

Some data cannot be shown as precise points (e.g., sites vulnerable to looting, endangered species, culturally sensitive places).

Recommended protections:
- **coordinate generalization** (e.g., show a hex/grid area instead of exact point)
- **role-based access** (public vs authorized)
- **sensitivity tags** in metadata + UI warnings
- **query auditing / inference control** (advanced): deny queries that could leak protected info
- **differential privacy** (advanced): add noise to aggregates when needed

> 🧩 Treat sensitivity like a first-class schema field — not a human reminder.

---

## ⚡ Performance sanity checklist

- [ ] Spatial indexes exist (PostGIS)
- [ ] Geometry is simplified per zoom (don’t ship full-res polygons everywhere)
- [ ] Tiles are generated from projected geometries appropriate for tiling
- [ ] Rasters are COGs, not plain GeoTIFF
- [ ] Heavy layers have caching and/or PMTiles distribution
- [ ] Provenance includes versions + digests so caching is safe

---

## 🧰 “Reference Vault” (PDF portfolios) — extract for deeper study

Some project PDFs are *portfolios* (a PDF that contains many embedded PDFs).  
To extract embedded files locally:

```bash
# list attachments
pdfdetach -list "Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf"

# extract everything into a folder
mkdir -p _extracted/maps_portfolio
pdfdetach -saveall -o _extracted/maps_portfolio \
  "Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf"
```

Repeat the same approach for:
- `AI Concepts & more.pdf`
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf`
- `Various programming langurages & resources 1.pdf`

---

## 📚 Project Reference Library (use these while building notebooks)

### 🧱 Core KFM docs
- **Comprehensive Technical Documentation** — formats, CRS, tiles, COGs, Cesium/MapLibre integration
- **Comprehensive Architecture, Features, and Design** — policy gates, stack boundaries, fail-closed philosophy
- **Comprehensive UI System Overview** — Map+Timeline UX, story nodes, offline packs, AR concepts
- **AI System Overview** — Focus Mode evidence/citations, hybrid retrieval, graph integration
- **Data Intake Guide** — PostGIS/Neo4j coordination, catalogs-first ingestion patterns

### 🗺️ Geospatial hub blueprint
- **Open-Source Geospatial Historical Mapping Hub Design** — layered maps over time, document ↔ place linking, KML/KMZ export patterns

### ✅ Methodology & quality
- **Scientific Method / Research / Master Coder Protocol** — reproducible experiment & notebook standards
- **Design Audit — Gaps & Enhancements** — modularity, ontology, interoperability recommendations

### 💡 Future-facing / inspiration
- **Innovative Concepts to Evolve KFM** — 4D digital twins, AR storytelling, AI GIS co-pilots, ethical access controls
- **Latest Ideas & Future Proposals** — roadmap items like real-time feeds, “Kansas From Above”, QA + governance expansions
- **Additional Project Ideas** — design packs, specs, artifact distribution/signing, modular domain add-ons

### 🔒 Privacy & inference safety
- **Data Mining Concepts & Applications** — query auditing, privacy-preserving release patterns (useful for sensitive geo)

---

## ✅ Definition of Done (for any geospatial notebook)

A notebook is “done” when:
- [ ] Outputs are **reproducible** (env captured, deterministic where possible)
- [ ] Outputs have **STAC/DCAT/PROV** (or clear receipts pointing to them)
- [ ] **License + sensitivity** are declared and enforced
- [ ] PostGIS and/or tiles are benchmarked for basic performance
- [ ] A short “handoff note” exists for UI/API integration (what endpoint/style expects)
- [ ] A follow-up task exists to convert the notebook into a pipeline step (when ready)

---

## 🧩 Contributing tips

- Keep notebooks **small and composable**: one idea per notebook.
- Promote proven workflows into **pipelines**, and leave notebooks as documented experiments.
- If you invent a new geospatial “unit” (sample geometry/time unit, QC metric, preprocessing rule), capture it as a **spec** (Design Pack style) so it becomes reusable across domains.

🚀 Happy mapping.
