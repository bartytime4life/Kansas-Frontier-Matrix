# 🪨 Monument Rocks — 3D Model Provenance (KFM)

**Badges:** `KFM` • `3D Asset` • `Provenance‑First` • `STAC + DCAT + PROV` • `Cesium / 3D Tiles` • `FAIR + CARE`

📍 **Repo path:** `web/assets/3d/shared/models/monument-rocks/sources/provenance/README.md`

> 🧭 **Why this exists:** KFM is **provenance-first** — every map, dataset, document, *and model* should be auditable, traceable, and reproducible (no black boxes).:contentReference[oaicite:0]{index=0}

---

## 🧩 What this folder is for

This folder is the **“receipt drawer”** for the Monument Rocks 3D model:
- where it came from ✅  
- who/what made it ✅  
- what license governs it ✅  
- exactly how the bytes were produced ✅  
- how to reproduce (or at least re-derive) it ✅  

KFM’s UI is designed to expose *“the map behind the map”* and keep provenance visible to users (including citations for AI answers).:contentReference[oaicite:1]{index=1}:contentReference[oaicite:2]{index=2}

---

## 🗺️ Context in Kansas Frontier Matrix

Monument Rocks is explicitly used as an example landmark for a planned **“Kansas From Above”** flow where KFM transitions from **2D historical maps → 3D terrain → landmark focus (e.g., Monument Rocks with a 3D model)**.:contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}

KFM’s 3D experience is powered by **CesiumJS** and supports **3D Tiles** for streaming large 3D content (point clouds, textured models, etc.).:contentReference[oaicite:5]{index=5}

---

## 📌 Asset identity (fill these in)

> ✅ Treat these identifiers as **stable**, because they’re used by the catalog + graph + UI.

| Field | Value |
|---|---|
| Asset slug | `monument-rocks` |
| Display name | `Monument Rocks` |
| Asset type | `3D Model` |
| Primary deliverable | `TBD` (`.glb` / `.gltf` / `3D Tiles tileset`) |
| KFM Asset ID (recommended) | `kfm:asset:3d:monument-rocks@0.0.0` |
| STAC Item ID | `TBD` |
| DCAT Dataset ID | `TBD` |
| Graph node ID / URI | `TBD` |
| Region / Place node link | `TBD` |
| CRS (web standard) | **WGS84 / EPSG:4326** (serve in WGS84; record original CRS in metadata + provenance):contentReference[oaicite:6]{index=6} |
| Units | `meters` (recommended; document if different) |
| Sensitivity classification | `public` / `sensitive` / `restricted` |
| License | `TBD` (must be explicit) |

---

## 📁 Expected contents of this provenance folder

> KFM generally prefers **manifests** for external sources (so we don’t version giant binaries in Git), while keeping raw evidence immutable and reproducible in the pipeline lifecycle.:contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}

Recommended “receipt set”:

```text
📁 web/assets/3d/shared/models/monument-rocks/
└─ 📁 sources/
   └─ 📁 provenance/
      ├─ ✅ README.md                      (this file)
      ├─ 🧾 source.manifest.yaml           (where it came from + license + links)
      ├─ 🧬 prov.jsonld                    (PROV-O lineage: inputs → activity → output)
      ├─ 🔐 checksums.sha256               (sha256 for each referenced artifact)
      ├─ 📜 LICENSE.txt                    (or LICENSE.md; must match manifest)
      ├─ 🧪 qa.report.md                   (validation results: geometry, textures, etc.)
      └─ 🗒️ notes.md                       (field notes, caveats, TODOs)
```

---

## ✅ Definition of Done (DoD) for “provenance-complete” 🧾

- [ ] **Source manifest** exists and includes **license + attribution**  
- [ ] **Checksums** exist for every referenced artifact  
- [ ] **PROV JSON-LD** exists and links: raw inputs → processing activity → final outputs (agent included):contentReference[oaicite:9]{index=9}:contentReference[oaicite:10]{index=10}  
- [ ] **STAC/DCAT links** are present (either here or cross-linked to canonical catalog paths):contentReference[oaicite:11]{index=11}  
- [ ] Sensitivity classification is set (and generalized if needed):contentReference[oaicite:12]{index=12}:contentReference[oaicite:13]{index=13}  
- [ ] CI policy expectation met: **no publish/use without provenance**:contentReference[oaicite:14]{index=14}

---

## 🧾 1) Source manifest (template)

> Use a manifest approach to record external sources and avoid committing large raw files directly in Git where possible.:contentReference[oaicite:15]{index=15}

Create: `source.manifest.yaml`

```yaml
# source.manifest.yaml (TEMPLATE)
asset:
  slug: monument-rocks
  display_name: "Monument Rocks"
  kfm_asset_id: "kfm:asset:3d:monument-rocks@0.0.0"

source:
  acquisition_type: "TBD"        # photogrammetry | lidar | downloaded | commissioned | other
  captured_by: "TBD"             # person/team/org
  captured_on: "TBD"             # ISO8601 date
  captured_with: "TBD"           # camera/scanner + settings if known
  field_notes: "TBD"
  external_links:
    - label: "Primary source page"
      url: "TBD"
    - label: "Raw archive location"
      url: "TBD"

license:
  spdx: "TBD"                    # e.g. CC-BY-4.0
  attribution: "TBD"
  restrictions: "TBD"            # e.g. non-commercial, no-derivatives, etc.

georeferencing:
  crs_served: "EPSG:4326"        # KFM web standard:contentReference[oaicite:16]{index=16}
  crs_original: "TBD"
  transform_notes: "TBD"
```

---

## 🧬 2) PROV lineage (required)

KFM treats PROV as mandatory for publishing and governance (policies can require PROV records or fail CI).:contentReference[oaicite:17]{index=17}

<details>
<summary>📦 PROV JSON-LD (starter skeleton)</summary>

> The intake guide illustrates a PROV JSON-LD structure that captures: **entities**, **activities**, and **agents**, and links them via `used`, `wasGeneratedBy`, `wasAssociatedWith` patterns.:contentReference[oaicite:18]{index=18}:contentReference[oaicite:19]{index=19}

```json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",

  "entity": {
    "kfm:raw:monument-rocks:photos": {
      "prov:label": "Raw capture set (photos / scans)",
      "prov:type": "prov:Entity"
    },
    "kfm:derived:monument-rocks:model-glb": {
      "prov:label": "Monument Rocks optimized web model (GLB)",
      "prov:type": "prov:Entity"
    }
  },

  "activity": {
    "kfm:activity:monument-rocks:build-3d-model": {
      "prov:label": "Build 3D model from raw capture",
      "prov:startTime": "TBD",
      "prov:endTime": "TBD"
    }
  },

  "agent": {
    "kfm:agent:maintainer": {
      "prov:label": "KFM Maintainer / Pipeline Bot",
      "prov:type": "prov:Agent"
    }
  },

  "used": {
    "_:use1": {
      "prov:activity": "kfm:activity:monument-rocks:build-3d-model",
      "prov:entity": "kfm:raw:monument-rocks:photos",
      "prov:role": "input evidence"
    }
  },

  "wasGeneratedBy": {
    "_:gen1": {
      "prov:entity": "kfm:derived:monument-rocks:model-glb",
      "prov:activity": "kfm:activity:monument-rocks:build-3d-model"
    }
  },

  "wasAssociatedWith": {
    "_:assoc1": {
      "prov:activity": "kfm:activity:monument-rocks:build-3d-model",
      "prov:agent": "kfm:agent:maintainer"
    }
  }
}
```

</details>

---

## 🧠 3) Deterministic pipeline expectations (how we “earn trust”)

KFM requires deterministic, config-driven pipelines and treats raw inputs as immutable evidence (no ad-hoc manual edits).:contentReference[oaicite:20]{index=20}

### Recommended 3D model pipeline stages 🧱

1) **Ingest / archive evidence** (raw capture, scans, control points)  
2) **Reconstruct** (photogrammetry/LiDAR → high-res mesh + textures)  
3) **Normalize** (scale, orientation, units, coordinate conventions)  
4) **Georeference** (serve in WGS84; record original CRS + transformations in provenance):contentReference[oaicite:21]{index=21}  
5) **Optimize for web** (decimate + LODs + texture compression)  
6) **Validate** (geometry + glTF/tileset integrity; record QA report)  
7) **Publish metadata** (STAC + DCAT + PROV links) — required for use in graph/UI:contentReference[oaicite:22]{index=22}:contentReference[oaicite:23]{index=23}

---

## 🧾 4) STAC/DCAT/PROV cross-links (catalog + graph)

KFM catalogs all data with **STAC + DCAT** and captures provenance with **W3C PROV**, storing provenance alongside the catalog to keep everything discoverable and traceable.:contentReference[oaicite:24]{index=24}

### Where to link to (recommended)

Even though this README lives under `web/`, the canonical metadata often lives under KFM’s data catalog/provenance structures.:contentReference[oaicite:25]{index=25}

Add links here (relative paths preferred):

- **STAC Item (canonical):** `TBD`
- **STAC Collection:** `TBD`
- **DCAT Dataset:** `TBD`
- **PROV JSON-LD (canonical):** `./prov.jsonld` (and/or `TBD` if duplicated under `data/provenance/`)

---

## 🔐 5) Sensitivity, ethics, and “don’t create harm” guardrails

KFM explicitly considers sensitive data cases and supports:
- location generalization (coarsening coordinates),
- access controls,
- explicit tagging in metadata,
- UI warnings (lock icon / disclaimers).:contentReference[oaicite:26]{index=26}:contentReference[oaicite:27]{index=27}

### Sensitivity checklist for Monument Rocks model
- [ ] Does the asset expose **precise sensitive location details** (e.g., if paired with archaeological context)?  
- [ ] If yes, do we need a **generalized public version** (reduced resolution / simplified geometry / bounding area)?:contentReference[oaicite:28]{index=28}  
- [ ] Is the license compatible with public hosting?  
- [ ] Do we need UI warnings / restricted access?

### FAIR + CARE alignment
KFM uses FAIR + CARE concepts in metadata (including ethics/collective benefit considerations).:contentReference[oaicite:29]{index=29}:contentReference[oaicite:30]{index=30}  
Innovative concepts also emphasize balancing openness with rights and community context (CARE as people/purpose-oriented).:contentReference[oaicite:31]{index=31}

---

## 📦 6) Distribution strategy for big 3D binaries (recommended)

For large artifacts, KFM proposes using an OCI registry approach (container-tech tooling) with:
- **oras** for transfers
- **cosign** for signing
- attaching provenance manifests (e.g., PROV JSON-LD) as related artifacts/referrers:contentReference[oaicite:32]{index=32}:contentReference[oaicite:33]{index=33}

### Suggested fields to add (when used)
| Field | Example |
|---|---|
| OCI ref | `oci://registry.example/kfm/monument-rocks:0.0.0` |
| Signature | `cosign://...` |
| Provenance attachment | `prov.jsonld` as referrer/attestation |

---

## 🧪 7) QA / validation (minimum bar)

> KFM treats metadata “like code” and validates it in CI to keep quality high and reproducible.:contentReference[oaicite:34]{index=34}

Create: `qa.report.md` and record:

- [ ] triangle/vertex counts (per LOD)
- [ ] texture set list (format, resolution, compression)
- [ ] coordinate system + origin conventions documented
- [ ] glTF/tileset validates (tool + version)
- [ ] runtime performance notes (FPS on baseline device)
- [ ] checksums re-verified

### Data-quality mindset (why QA is not optional)
Even outside pure geospatial, data pipelines can suffer from messy inputs and quality issues; cleansing/verification are required steps before analysis and publication.:contentReference[oaicite:35]{index=35}:contentReference[oaicite:36]{index=36}

---

## 🌐 8) How this model should appear in the KFM UI

KFM’s UI supports:
- **2D map exploration** and **3D globe/terrain visualization** with a smooth toggle  
- streaming **3D Tiles** content in 3D mode  
- provenance tooltips + sensitivity warnings to keep transparency + ethics baked in:contentReference[oaicite:37]{index=37}:contentReference[oaicite:38]{index=38}

### Story Node hook (recommended snippet)
If used in a “Kansas From Above” story scene, record:
- camera target (lat/lon/height)
- asset ID/version
- attribution string
- link to provenance

*(KFM story tooling is explicitly planned to support guided tours with 2D→3D transitions.)*:contentReference[oaicite:39]{index=39}

---

## 🤖 9) AI & automation notes (because this is a first-class KFM artifact)

KFM uses AI to assist ingestion/metadata tasks, but keeps humans in the loop and logs AI-generated additions for transparency.:contentReference[oaicite:40]{index=40}:contentReference[oaicite:41]{index=41}

KFM also explores integrating DevOps events into PROV (PRs as Activities, commits as Entities, authors/reviewers as Agents) to make evolution traceable end-to-end.:contentReference[oaicite:42]{index=42}

And it proposes graph health checks to detect broken provenance chains (e.g., orphan PROV activities).:contentReference[oaicite:43]{index=43}

---

## 🧰 10) Local preview / web visualization (optional technique)

While KFM’s primary 3D UI path is Cesium, general WebGL tooling like **Three.js** can be used for quick local previews and understanding 3D rendering patterns (WebGLRenderer, terrain loading, and browser-based 3D viewing).:contentReference[oaicite:44]{index=44}:contentReference[oaicite:45]{index=45}

---

## 🕰️ Changelog (keep it tight)

- `YYYY-MM-DD` — Created provenance README scaffold (this file)  
- `YYYY-MM-DD` — Added source.manifest.yaml  
- `YYYY-MM-DD` — Added prov.jsonld + checksums + QA report  
- `YYYY-MM-DD` — Published STAC/DCAT links + graph IDs

---

## 📚 Project references used to shape this provenance contract

> Some “project files” are PDF portfolios that require Acrobat/Reader to open fully in their native form (not fully extractable in this environment).:contentReference[oaicite:46]{index=46}:contentReference[oaicite:47]{index=47}:contentReference[oaicite:48]{index=48}:contentReference[oaicite:49]{index=49}

- 📘 KFM technical documentation (provenance, folder structure, 2D↔3D concept, WGS84 standard) :contentReference[oaicite:50]{index=50} :contentReference[oaicite:51]{index=51}  
- 📗 KFM data intake guide (provenance-first, deterministic ETL, PROV enforcement, Policy Pack) :contentReference[oaicite:52]{index=52} :contentReference[oaicite:53]{index=53}  
- 🖥️ KFM UI system overview (map behind map, provenance tooltips, 3D tiles, sensitivity warnings) :contentReference[oaicite:54]{index=54} :contentReference[oaicite:55]{index=55}  
- 🏛️ KFM architecture/features/design (STAC/DCAT/PROV, governance, validation mindset) :contentReference[oaicite:56]{index=56} :contentReference[oaicite:57]{index=57}  
- 🤖 KFM AI system overview (education + reproducibility framing) :contentReference[oaicite:58]{index=58}  
- 💡 Latest ideas & future proposals (Kansas From Above, PR→PROV integration) :contentReference[oaicite:59]{index=59}  
- 🚀 Innovative concepts (AR/hybrid storytelling, FAIR/CARE discussion) :contentReference[oaicite:60]{index=60}  
- 🧠 Additional project ideas (OCI artifacts, cosign/oras, graph health checks) :contentReference[oaicite:61]{index=61}  
- 🌍 Maps/virtual worlds portfolio (resource bundle) :contentReference[oaicite:62]{index=62}  
- 🧰 Programming resources portfolio (resource bundle) :contentReference[oaicite:63]{index=63}  
- 🗄️ Data management portfolio (resource bundle) :contentReference[oaicite:64]{index=64}  
- 🤖 AI concepts portfolio (resource bundle) :contentReference[oaicite:65]{index=65}  

---

## 🚧 TODO (high priority)

- [ ] Fill Asset Identity fields (IDs, formats, license, dates)  
- [ ] Add `source.manifest.yaml`  
- [ ] Add `checksums.sha256`  
- [ ] Add `prov.jsonld`  
- [ ] Add `qa.report.md`  
- [ ] Link STAC/DCAT entries + graph node IDs  
- [ ] Decide OCI artifact strategy for binaries (if needed)

> ✅ Once the above is complete, this model is safe to reference in **3D mode**, **Story Nodes**, and **Focus Mode**, without violating provenance-first publishing expectations.:contentReference[oaicite:66]{index=66}

