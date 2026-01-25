# 🏛️ 3D Landmark Modeling Decisions — `<landmark_slug>`

![KFM](https://img.shields.io/badge/KFM-3D%20Landmark-2ea44f)
![Provenance](https://img.shields.io/badge/Provenance-First-blue)
![Formats](https://img.shields.io/badge/Formats-GLB%20%7C%203D%20Tiles-informational)
![Governance](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-purple)
![Policy%20Gates](https://img.shields.io/badge/Policy%20Gates-OPA%20%2F%20Conftest-orange)

> **Path:** `web/assets/3d/landmarks/<landmark_slug>/citations/notes/modeling_decisions.md`  
> **Why this exists:** KFM is **contract-first** and **provenance-first** — anything the user sees (including 3D) must be traceable, governed, and reproducible.

---

## 🧾 Snapshot (fill these in)

| Field | Value |
|---|---|
| Landmark Name | `TODO` |
| Landmark Slug | `<landmark_slug>` |
| KFM Entity ID | `TODO (e.g., place:<landmark_slug>)` |
| Location (WGS84) | `lat: TODO, lon: TODO, elev_m: TODO` |
| Model Version | `v0.0.0` |
| Status | `draft / review / published` |
| Owner | `@TODO` |
| Reviewers | `@TODO` |
| Representation Type | `Scan / Photogrammetry / Procedural / Interpretive Reconstruction` |
| Confidence (0–5) | `TODO` |
| Target Viewers | `Cesium 3D Mode / MapLibre 2D fallback / AR mode` |
| Primary Outputs | `model/<landmark_slug>.glb` + `model/tileset/` |
| Provenance Record | `metadata/prov.jsonld` |
| Catalog Records | `metadata/stac_item.json` + `metadata/dcat_dataset.json` |

---

## 🗂️ Landmark folder conventions (recommended)

```text
web/assets/3d/landmarks/<landmark_slug>/
  📦 model/
    🧊 <landmark_slug>.glb
    🧱 tileset/                 # 3D Tiles (if used)
      tileset.json
      content/...
    🎨 textures/
  🧾 metadata/
    stac_item.json
    dcat_dataset.json
    prov.jsonld
    checksums.txt
  📚 citations/
    sources/                    # raw evidence references (photos, lidar, maps, etc.)
    notes/
      modeling_decisions.md     # <-- this file
      qa_notes.md
    screenshots/
  🧪 qa/
    validation_report.md
```

---

## 🎯 Decision drivers (what this asset must satisfy)

KFM’s map stack uses **MapLibre for 2D** and **CesiumJS for 3D**, streaming **3D Tiles** and supporting 3D mode toggling without losing context.

KFM’s publishing rules require:

- **WGS84 (EPSG:4326)** as the web/display standard, with original CRS tracked in provenance.
- **No “mystery layers”**: everything in UI has citations + provenance + policy context (the “Evidence Triplet”).
- **Policy gates fail closed** (license, sensitivity, provenance, etc.).
- **Sensitive locations** may require generalization (e.g., hex areas), and CARE principles apply for culturally sensitive data.

---

## 📌 Modeling Decision Log (keep this updated)

| Category | Decision | Chosen | Rationale | Evidence (local links) | Tradeoffs / Notes |
|---|---|---|---|---|---|
| Scope | What the model represents | `TODO` | `TODO` | `citations/sources/...` | `TODO` |
| CRS | Display CRS | `EPSG:4326 (WGS84)` | KFM web standard | `metadata/prov.jsonld` | Track source CRS |
| Units | Model units | `meters` | Web + geospatial convention | `notes/qa_notes.md` | Avoid cm/m drift |
| Up Axis | `Z-up` or `Y-up` | `TODO` | Align export pipeline | `notes/qa_notes.md` | Must be explicit |
| Origin | Anchor point | `TODO` | Stable placement in Cesium | `metadata/stac_item.json` | Avoid huge coords in DCC |
| Formats | Delivery formats | `GLB + (optional) 3D Tiles` | Cesium streaming | `model/...` | Two pipelines to maintain |
| Materials | Shading model | `PBR (metal/rough)` | Consistent lighting | `citations/sources/...` | Texture memory |
| Textures | Texture budget | `TODO` | Web performance | `qa/validation_report.md` | Device variability |
| LOD | LOD strategy | `TODO` | Browser safety | `qa/validation_report.md` | Authoring time |
| Governance | Sensitivity classification | `TODO` | Required by policy | `metadata/dcat_dataset.json` | May limit public display |

---

## 🧱 1) Scope & “truth model” (what this asset *claims*)

### Representation type
Select one and justify:

- **Scan / LiDAR / Photogrammetry** (highest fidelity; claims “as captured”)
- **Procedural / Simplified** (claims “approximate geometry”)
- **Interpretive reconstruction** (claims “historical hypothesis”)

> If the model includes interpretive elements, we must label it clearly in metadata + UI so it’s not mistaken for measured truth.

### Included
- ✅ `TODO: e.g., main rock formation + immediate base`
- ✅ `TODO: historically relevant additions (fence line, signage, etc.)`
  
### Excluded
- ❌ `TODO: interior spaces?`
- ❌ `TODO: vegetation micro-detail?`
- ❌ `TODO: surrounding town context?`

---

## 🌍 2) Spatial reference, georeferencing & alignment

KFM standardizes display to **WGS84 (EPSG:4326)**, reprojecting on ingest and recording that in provenance.

### Decisions
- **Authoring CRS (DCC / Blender / etc.):** `TODO (often local ENU for stability)`
- **Display CRS:** `EPSG:4326`
- **Terrain vertical datum:** `TODO (meters; specify datum if known)`
- **Anchor strategy:**  
  - `TODO: Anchor at centroid` vs `anchor at surveyed marker`  
  - `TODO: store anchor in metadata + prov`

### Minimum required metadata (for placement)
Store **all** of the following somewhere versioned (ideally `metadata/stac_item.json` + `metadata/prov.jsonld`):

```json
{
  "kfm:landmark_slug": "<landmark_slug>",
  "kfm:anchor_wgs84": { "lat": 0, "lon": 0, "elev_m": 0 },
  "kfm:up_axis": "Z",
  "kfm:units": "m",
  "kfm:crs_display": "EPSG:4326",
  "kfm:crs_source": "TODO"
}
```

---

## 🧩 3) Geometry strategy (web-safe, Cesium-ready)

KFM’s 3D mode uses CesiumJS and streams heavy 3D content via **3D Tiles** for performance.

### Decisions to record
- **Mesh partitioning:** `TODO`  
  - (Recommended: split into logical chunks that align with LOD/streaming boundaries.)
- **Topology cleanup:** `TODO`  
  - Non-manifold edges? Loose parts? Double faces?
- **Collision / picking mesh:** `TODO`  
  - (Recommended: separate simplified collider mesh for interaction.)

### Suggested web budgets (guideline — adjust per landmark)
- **Hero LOD (closest):** `~50k–200k tris` (depending on device target)
- **Mid LOD:** `~10k–50k tris`
- **Far LOD:** `~500–5k tris`

> Use 3D Tiles for anything that needs progressive refinement while zooming, since Cesium can load more detailed tiles as you move in.

---

## 🎨 4) Materials, textures & appearance (PBR + performance)

### Decisions
- **Material model:** `PBR metal/rough`
- **Base color source:** `TODO (photo set / scan textures / manual paint)`
- **Normal/AO baking:** `TODO`
- **Texture atlas:** `TODO (yes/no; why)`
- **Compression:** `TODO (KTX2/Basis recommended if supported by pipeline)`

### Naming conventions
- `tex_<landmark_slug>_basecolor.(png|ktx2)`
- `tex_<landmark_slug>_normal.(png|ktx2)`
- `tex_<landmark_slug>_orm.(png|ktx2)` (Occlusion-Roughness-Metallic packed)

---

## 🧠 5) LOD + streaming strategy (GLB vs 3D Tiles)

KFM supports **Cesium 3D Tiles** for streaming 3D datasets like models or point clouds.

### Choose one (or both)

#### Option A — Single GLB
Use when:
- The landmark is small enough to load as a single binary file without stalling the browser.
- You need simple distribution and fewer moving pieces.

Record:
- `GLB file size`
- `tri count`
- `draw calls`
- `texture memory estimate`

#### Option B — 3D Tiles
Use when:
- The model is large or needs progressive detail.
- You want Cesium to load higher-detail tiles as users zoom in.

Record:
- Tiling scheme (spatial subdivision)
- LOD thresholds (SSE or distance bands)
- Tile content formats used (`b3dm`, `glb`, point cloud tiles, etc.)

---

## 📱 6) AR mode constraints (if this landmark can appear in AR)

KFM’s UI planning explicitly expects an AR mode that loads **only a subset** of features and **simplified geometry** to avoid clutter and performance issues.

### AR readiness checklist
- [ ] Provide an **AR-friendly LOD** (very low poly + reduced texture set)
- [ ] Provide **clear interaction hotspots** (markers/labels rather than dense geometry)
- [ ] Ensure **stable anchor** (GPS drift and compass drift are real; note mitigation strategy).
- [ ] Define **AR scene radius** (e.g., X meters around user) and justify.

---

## 🧾 7) Provenance, citations, and “Evidence Triplet” compliance

KFM’s “Evidence Triplet” concept: **Data + Provenance + Policy** is what users experience — not raw data alone.

### Minimum provenance expectations (for this 3D asset)
- Every source (photo, scan, map, dataset) listed in `citations/sources/`
- Every transformation step recorded (tool + version + operator + date)
- Every output file referenced from STAC/DCAT, with links to PROV records

### Suggested “run manifest” (create alongside PROV)
📄 `metadata/run_manifest.json`

```json
{
  "run_id": "TODO",
  "timestamp_utc": "TODO",
  "tools": {
    "dcc": "Blender TODO",
    "gdal": "TODO",
    "tile_builder": "TODO"
  },
  "inputs": [
    "citations/sources/..."
  ],
  "outputs": [
    "model/<landmark_slug>.glb",
    "model/tileset/tileset.json"
  ],
  "notes": "TODO"
}
```

> Treat this like a reproducibility artifact; KFM’s broader doc culture expects transparent, repeatable steps and strong documentation discipline.

### Policy gate reminder
Automated governance checks are expected to **fail closed** when required fields like license or sensitivity are missing.

---

## ⚖️ 8) Licensing, attribution, and reuse

Record:
- **License of each source** (and proof)
- **License of derived model**
- **Attribution text** (exact string to show in UI)
- **Any restrictions** (non-commercial, no-derivatives, etc.)

> If we distribute 3D assets via artifact registries, we can attach provenance and signatures to improve integrity and traceability.

---

## 🧭 9) Sensitivity, ethics, and safe disclosure

KFM explicitly supports sensitivity classification, masking/aggregation, and CARE-aligned governance—especially for culturally sensitive sites and indigenous data sovereignty.

### Classification (required)
- `public`
- `sensitive`
- `restricted`
- `confidential`

### If the landmark is sensitive
Document at least one mitigation:
- Location generalization (e.g., show hex area instead of exact point)
- Reduced-detail public model (no actionable details)
- Auth-gated access
- Community approval workflow (if applicable)

---

## ✅ 10) QA & validation checklist (before publishing)

### Geometry
- [ ] Correct real-world scale (meters)
- [ ] Orientation correct (up axis recorded)
- [ ] No non-manifold geometry (or explicitly accepted)
- [ ] Pivot/origin matches anchor strategy
- [ ] No hidden high-poly meshes accidentally exported

### Visual
- [ ] Textures referenced correctly (no missing files)
- [ ] Reasonable mipmapping behavior (no shimmer)
- [ ] No baked lighting that fights Cesium lighting (unless intentional)

### Geospatial alignment
- [ ] Aligns with basemap/terrain in 3D mode at multiple zoom levels
- [ ] WGS84 anchor and CRS recorded in metadata

### Governance
- [ ] License present + compatible
- [ ] Sensitivity classification present
- [ ] Citations complete
- [ ] PROV JSON-LD exists and links from STAC/DCAT

---

## 🔁 11) Change control (append-only + auditable)

KFM intake philosophy: **append-only** (no silent rewrites), plus traceability from code/PR → provenance records.

### Versioning rules
- Patch bump: texture tweak, metadata fix
- Minor bump: geometry changes but same footprint
- Major bump: anchor/scale changes or “truth model” changes

### Change log
```text
v0.0.1 — TODO — initial draft mesh + WGS84 anchor
v0.1.0 — TODO — added LODs and 3D Tiles packaging
v1.0.0 — TODO — reviewed + published
```

---

## 📎 Appendix A — Evidence inventory template (copy/paste)

Create `citations/sources/README.md` and list:

- Source ID
- Type (photo / lidar / map / doc)
- License
- Date captured
- Provider
- Notes

---

## 📎 Appendix B — If AI assisted any step, document it

KFM expects AI enhancements to remain provenance-first; AI-suggested additions should be logged and marked as AI-generated for transparency.

Record:
- Tool/model used
- Prompt or method summary
- Human review performed by
- What was accepted vs rejected

---

## 📚 Sources consulted (project docs)

<details>
<summary>📦 Core KFM design & governance docs</summary>

- :contentReference[oaicite:41]{index=41} Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf  
- :contentReference[oaicite:42]{index=42} Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf  
- :contentReference[oaicite:43]{index=43} Kansas Frontier Matrix – Comprehensive UI System Overview.pdf  
- :contentReference[oaicite:44]{index=44} 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf  
- :contentReference[oaicite:45]{index=45} Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf  
- :contentReference[oaicite:46]{index=46} Additional Project Ideas.pdf  
- :contentReference[oaicite:47]{index=47} Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf  

</details>

<details>
<summary>🧠 Idea vaults / portfolios (PDF portfolios)</summary>

These are PDF portfolios (embedded libraries). Extract attachments when you need deeper guidance.

- :contentReference[oaicite:48]{index=48} AI Concepts &amp; more.pdf  
- :contentReference[oaicite:49]{index=49} Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf  
- :contentReference[oaicite:50]{index=50} Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf  
- :contentReference[oaicite:51]{index=51} Various programming langurages &amp; resources 1.pdf  

</details>

<details>
<summary>🧭 Roadmap / proposals</summary>

- :contentReference[oaicite:52]{index=52} Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf  
- :contentReference[oaicite:53]{index=53} 🌟 Kansas Frontier Matrix – Latest Ideas &amp; Future Proposals.docx.pdf  

</details>

