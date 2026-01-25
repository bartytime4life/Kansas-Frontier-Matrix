# 🏺 Archaeology 3D Tileset — `<site-slug>`

![3D Tiles](https://img.shields.io/badge/3D%20Tiles-streaming%20LOD-blue)
![CesiumJS](https://img.shields.io/badge/CesiumJS-3D%20globe%20viewer-2b7cff)
![Evidence-First](https://img.shields.io/badge/Policy-Evidence--First%20Publishing-success)
![STAC/DCAT/PROV](https://img.shields.io/badge/Metadata-STAC%20%2B%20DCAT%20%2B%20PROV-informational)
![FAIR+CARE](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-8a2be2)
![Sensitive-Location](https://img.shields.io/badge/Safety-Sensitive%20Location%20Controls-orange)

> **📌 Entry point:** `tileset.json`  
> **🛰️ Renderer:** CesiumJS (KFM 3D view)  
> **🎯 Purpose:** Stream a site-scale archaeology model (terrain / structures / point clouds) as **3D Tiles**, while staying compliant with KFM’s **provenance-first + policy-gated** publishing model. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## ✨ What belongs in this folder

This directory contains the **web-deployable** 3D Tileset for a single archaeology site:

- ✅ `tileset.json` + all referenced tile payloads (`.b3dm`, `.i3dm`, `.pnts`, `.cmpt`, `.glb`, etc.)
- ✅ Optional previews for the UI (thumbnail / screenshot)
- ✅ Optional “local manifest” that *points to* the canonical KFM **STAC + DCAT + PROV** records (recommended)

KFM explicitly supports a **2D↔3D workflow** (MapLibre for 2D, Cesium for 3D), where Story Nodes can transition viewers from 2D map context into 3D terrain / models. :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}

---

## 🧭 KFM design contract (why this README is strict)

KFM is **contract-first + provenance-first**: anything that appears in the UI (or is referenced by Focus Mode / AI features) must be traceable to **cataloged sources** and governed by **policy gates** (license, sensitivity, metadata completeness, provenance, etc.). No “mystery layers.” :contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}

That means this tileset is not “just a file drop” — it is a **publishable evidence artifact** that must link into the KFM evidence triplet:

- 🧾 **STAC** (asset-level spatial/temporal + file links)
- 🗂️ **DCAT** (dataset-level catalog entry)
- 🧬 **PROV** (lineage: inputs + processing + agents)

KFM stores and cross-links these records and ingests them into the knowledge graph for discovery and traceability. :contentReference[oaicite:6]{index=6}:contentReference[oaicite:7]{index=7}

---

## 📁 Recommended folder layout

> You can keep it minimal (just 3D Tiles), but **don’t skip metadata** — KFM policy gates expect it somewhere in the repo. :contentReference[oaicite:8]{index=8}

```text
web/assets/3d/archaeology/sites/<site-slug>/models/tileset/
├── 📄 README.md
├── 🧩 tileset.json
├── 🧱 tiles/                      # (or flat files; match tileset.json references)
│   ├── 0/0/0.b3dm
│   └── ...
├── 🧾 kfm.tileset.manifest.yml     # ✅ recommended (local pointer → STAC/DCAT/PROV)
├── 🔐 access-policy.yml            # ✅ recommended for sensitive sites (local policy hints)
└── 🖼️ previews/                    # optional, but great for UX
    ├── thumbnail.jpg
    └── cesium-screenshot.png
```

---

## 🧾 Required: Evidence triplet links (STAC + DCAT + PROV)

KFM expects published artifacts to be “evidence-first” — catalog + lineage must exist before graph/UI use. :contentReference[oaicite:9]{index=9}:contentReference[oaicite:10]{index=10}

### ✅ Local manifest template

Create `kfm.tileset.manifest.yml` (or `.json`) as a **local pointer** to canonical records:

```yaml
kfm:
  site_slug: "<site-slug>"
  domain: "archaeology"
  artifact_type: "3d-tiles"
  entrypoint: "tileset.json"

  # ⚖️ Governance + safety tags (policy gates care about these)
  classification: "public"        # public | restricted | internal
  sensitivity_reason: ""          # e.g., "looting-risk", "cultural-protocol", "private-land"
  location_policy: "generalized"  # exact | generalized | hidden

  # 🔗 Canonical evidence triplet (repo paths or URIs)
  evidence:
    stac_item: "data/stac/<...>/item.json"
    dcat_dataset: "data/catalogs/dcat/<...>.jsonld"
    prov_record: "data/prov/<...>.jsonld"

  # 🌐 Distribution (what the UI loads)
  distribution:
    web_url: "/assets/3d/archaeology/sites/<site-slug>/models/tileset/tileset.json"
    # optional: OCI artifact reference (see below)
    oci_ref: ""
```

Why this matters:
- STAC/DCAT/PROV are core KFM metadata standards (interop + discovery + lineage). :contentReference[oaicite:11]{index=11}
- Policy gates can fail a PR if PROV is missing when processed artifacts change (e.g., **KFM-PROV-001**). :contentReference[oaicite:12]{index=12}

---

## 🔐 Sensitivity & cultural protocols (archaeology-safe defaults)

Archaeological site locations can be sensitive. KFM explicitly calls for:
- **Location generalization** (e.g., show a large hex area instead of an exact point)
- **Access controls / hiding layers**
- **Sensitivity tagging and warnings** :contentReference[oaicite:13]{index=13}

### ✅ Practical rules for this folder

1) **If the tileset is sensitive, do not ship an “exact” public tileset.**  
   - Provide a generalized / redacted public variant (or ship nothing publicly). :contentReference[oaicite:14]{index=14}

2) **Prefer “differential access” design** (role-based access + cultural protocols).  
   KFM explicitly cites approaches like Mukurtu-style cultural protocols and tiered access for heritage content. :contentReference[oaicite:15]{index=15}

3) **Honor CARE (Authority to Control) for heritage sites.**  
   If the data relates to Indigenous cultural heritage, governance should reflect community authority and approval workflows. :contentReference[oaicite:16]{index=16}

4) **Never publish output less restricted than inputs.**  
   “No output may be less restricted than inputs.” :contentReference[oaicite:17]{index=17}

> 🧠 Ethics reminder: even in other domains, data preparation practice often includes removing information that could harm participants/orgs and ensuring anonymity. That “remove what can cause harm” mindset applies strongly here. :contentReference[oaicite:18]{index=18}

---

## 🛠️ Build & update workflow (suggested)

> This section is tool-agnostic on purpose — KFM’s key requirement is **reproducibility + provenance + governance**. :contentReference[oaicite:19]{index=19}

### 1) Source capture (typical)
- 📸 Photogrammetry (drone/ground images)
- 📡 LiDAR / point clouds
- 🧱 CAD/mesh from reconstruction

### 2) Geospatial alignment & QA
Use GIS tooling to:
- validate CRS, scale, and offsets
- clip to intended extent
- produce footprints / AOI polygons  
(Geospatial workflows commonly use GIS tools like QGIS and Python geospatial libraries for data preparation tasks.) :contentReference[oaicite:20]{index=20}

### 3) Tile generation (3D Tiles)
Generate:
- `tileset.json`
- multi-resolution tiles (LOD)  
KFM highlights that **Cesium supports streaming 3D Tiles**, which is why tilesets matter for performance and large datasets. :contentReference[oaicite:22]{index=22}

### 4) Evidence artifacts (non-negotiable)
Update/create:
- STAC item(s)
- DCAT dataset entry
- PROV record (JSON-LD / PROV-O style)  
KFM’s catalog + lineage approach is central to how it stays auditable and queryable. :contentReference[oaicite:23]{index=23}

### 5) Policy gates & CI checks
Expect automated checks (license, metadata completeness, sensitivity classification, provenance completeness) and “fail closed” behavior. :contentReference[oaicite:24]{index=24}

---

## 🌐 Using the tileset in the KFM web UI (CesiumJS)

KFM’s 3D mode uses **CesiumJS** and supports **3D Tiles** layers as a core feature. :contentReference[oaicite:25]{index=25}

### Minimal CesiumJS load example

```js
// Example only — wire it into KFM's layer system / state store.
const url = "/assets/3d/archaeology/sites/<site-slug>/models/tileset/tileset.json";

const tileset = new Cesium.Cesium3DTileset({ url });
viewer.scene.primitives.add(tileset);

tileset.readyPromise.then(() => viewer.zoomTo(tileset));
```

### 🔎 Evidence in the UI (important)

KFM aims for “map behind the map”: the UI should be able to display provenance / citations for layers and stories. Make sure the layer registration includes pointers to STAC/DCAT/PROV so the UI (and Focus Mode) can cite sources. :contentReference[oaicite:26]{index=26}:contentReference[oaicite:27]{index=27}

---

## 🧩 Story Nodes integration (2D → 3D narrative transitions)

KFM Story Nodes can drive camera transitions and mode switches (2D map → 3D terrain/model flythrough), which is a core storytelling pattern in the project docs. :contentReference[oaicite:28]{index=28}

**Suggested story step pattern (pseudo-config):**

```json
{
  "type": "scene",
  "mode": "3d",
  "layers": [
    {
      "id": "archaeology:<site-slug>:tileset",
      "kind": "3dtiles",
      "url": "/assets/3d/archaeology/sites/<site-slug>/models/tileset/tileset.json",
      "evidence": {
        "stac": "data/stac/<...>/item.json",
        "dcat": "data/catalogs/dcat/<...>.jsonld",
        "prov": "data/prov/<...>.jsonld"
      }
    }
  ],
  "camera": { "flyTo": "tilesetBoundingSphere" }
}
```

---

## 🚚 Publishing & distribution (Static files + signed OCI artifacts)

Large binary artifacts (like tilesets) are strong candidates for **OCI registry distribution**, using:
- `oras` for transfers
- `cosign` for signing
- registry permissions for sensitive artifacts  
This approach is explicitly proposed for KFM artifacts (including “model files” and other large geospatial outputs). :contentReference[oaicite:30]{index=30}:contentReference[oaicite:31]{index=31}

<details>
<summary><strong>📦 Optional: OCI publishing pattern (recommended for big tilesets)</strong></summary>

- Keep the web folder as the “deployment mirror” (what the site serves)
- Publish the canonical tileset as an OCI artifact:
  - tag versions (`:<date>` / `:v1.2.3`)
  - attach PROV as a referrer
  - sign with cosign

Why:
- Better versioning, integrity, and supply chain provenance for heavy binaries. :contentReference[oaicite:32]{index=32}

</details>

---

## ✅ PR checklist (don’t skip — policy gates will bite 😅)

- [ ] `tileset.json` loads in Cesium without missing resources
- [ ] **License is declared** in DCAT and/or dataset metadata (no unknown license) :contentReference[oaicite:33]{index=33}
- [ ] **Sensitivity classification is set** (`public` / `restricted` / `internal`) :contentReference[oaicite:34]{index=34}
- [ ] STAC + DCAT + PROV exist and cross-link (evidence triplet) :contentReference[oaicite:35]{index=35}
- [ ] PROV updated for any change to the artifact (avoid **KFM-PROV-001**) :contentReference[oaicite:36]{index=36}
- [ ] If sensitive: public view is generalized/redacted or hidden :contentReference[oaicite:37]{index=37}:contentReference[oaicite:38]{index=38}
- [ ] (Optional) Checksums / signatures updated if you use OCI publishing :contentReference[oaicite:39]{index=39}

---

## 🧰 Troubleshooting

### “Tiles load, but appear shifted / floating / underground”
- Verify the model is correctly georeferenced before tiling (CRS + vertical datum).
- Confirm you didn’t accidentally mix local model coordinates with WGS84/world coordinates.

### “Some tiles 404”
- Check that the file paths in `tileset.json` are correct relative paths to the binary tiles folder.

### “Sensitive site exposure risk”
- Stop. Reclassify to restricted, remove from public build, and provide generalized proxies instead. KFM’s security model explicitly expects this behavior. :contentReference[oaicite:40]{index=40}

---

## 📚 References & internal libraries (project files)

### Core KFM docs (design truth)
- 📘 **Comprehensive Technical Documentation** (2D/3D UI, Story Nodes, evidence-first constraints) :contentReference[oaicite:41]{index=41}:contentReference[oaicite:42]{index=42}
- 🧱 **Comprehensive Architecture, Features, and Design** (STAC/DCAT/PROV, policy gates, “fail closed”) :contentReference[oaicite:43]{index=43}:contentReference[oaicite:44]{index=44}
- 🤖 **AI System Overview** (Cesium + 3D Tiles streaming as a supported visualization layer) 
- 🖥️ **Comprehensive UI System Overview** (3D Tiles as a first-class map layer type) :contentReference[oaicite:46]{index=46}
- 📥 **Data Intake – Technical & Design Guide** (provenance-first publishing, evidence triplet, policy pack behavior) :contentReference[oaicite:47]{index=47}:contentReference[oaicite:48]{index=48}
- 💡 **Innovative Concepts** (cultural protocols, differential access, credit + authority to knowledge holders) :contentReference[oaicite:49]{index=49}:contentReference[oaicite:50]{index=50}
- 🧠 **Additional Project Ideas** (OCI artifacts via ORAS + Cosign, provenance attachments) :contentReference[oaicite:51]{index=51}

### Reference libraries (PDF portfolios)
- 🗺️ **Maps / Virtual Worlds / Archaeology / WebGL portfolio** (embedded GIS + WebGL references) 
- 🧠 **AI Concepts & more portfolio** (embedded AI references / reading library) 
- 🧰 **Programming languages & resources portfolio** (embedded dev + ops references) 
- 🗄️ **Data management portfolio** (embedded data engineering / architecture references) 

### Handy embedded docs used in this README
- 🧭 Python geospatial workflows reference (QGIS/Python patterns) :contentReference[oaicite:56]{index=56}
- 📝 Markdown conventions / best practices (for consistent project docs) 

---

## 🏁 TL;DR (for future-you)

- Put a valid `tileset.json` here ✅  
- Register it in STAC + DCAT + PROV ✅  
- Tag sensitivity and **don’t expose sensitive sites** ✅  
- Let policy gates enforce the rest ✅ :contentReference[oaicite:58]{index=58}

