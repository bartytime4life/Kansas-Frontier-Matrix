# 🏺 GLB Models — `<site-slug>` (Archaeology)

![asset](https://img.shields.io/badge/asset-3D%20models%20(.glb)-informational)
![format](https://img.shields.io/badge/format-glTF%202.0%20Binary%20(GLB)-blue)
![viewer](https://img.shields.io/badge/viewer-Cesium%20(3D)%20%2B%20MapLibre%20(2D)-orange)
![governance](https://img.shields.io/badge/governance-evidence--first%20%2B%20provenance-brightgreen)
![safety](https://img.shields.io/badge/safety-sensitive--site%20aware-red)

> ✅ **Purpose:** This folder holds **web-ready** `.glb` models for the archaeology site slugged as `<site-slug>`, intended for **KFM’s 2D↔3D mapping experience (MapLibre + Cesium)** and narrative features like **Story Nodes**. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🧭 Quick rules (read this first)

### ✅ DO
- **Ship only web-optimized artifacts** (not raw scan dumps).
- **Include provenance + metadata sidecars** so the model can be cataloged and governed (STAC/DCAT/PROV linkage).:contentReference[oaicite:2]{index=2}
- **Respect sensitivity**: if this model reveals a vulnerable location, keep it **out of public web assets** and use **generalization / access controls** instead.:contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}

### ❌ DON’T
- Don’t embed precise coordinates or “treasure-map” placement for looting-prone sites in public builds.
- Don’t drop in models with unknown license/rights or missing contributor credit.
- Don’t bypass the pipeline (raw → … → catalogs → UI) with “mystery blobs” that can’t be traced.:contentReference[oaicite:5]{index=5}

---

## 🧱 How KFM uses models like these

KFM’s front-end supports:
- **2D historical map mode** (MapLibre) and a **3D globe/terrain mode** (Cesium) with a **toggle** between them.:contentReference[oaicite:6]{index=6}:contentReference[oaicite:7]{index=7}
- 3D terrain + **3D Tiles** integration for scalable 3D visualization (GLBs can be used directly for small assets or as source artifacts for tiling).:contentReference[oaicite:8]{index=8}:contentReference[oaicite:9]{index=9}

---

## 🔐 Sensitivity & anti-looting policy (non-negotiable)

KFM explicitly treats **archaeology site locations** as potentially sensitive:
- The UI can show a **large hexagon region** instead of an exact point to reduce looting risk.:contentReference[oaicite:10]{index=10}:contentReference[oaicite:11]{index=11}
- Governance includes **location generalization / fuzzing** and **access controls** for sensitive records.:contentReference[oaicite:12]{index=12}:contentReference[oaicite:13]{index=13}
- For culturally sensitive data, KFM policy highlights **permission and community-approved representation**, aligned with **CARE / Indigenous Data Sovereignty** expectations.:contentReference[oaicite:14]{index=14}:contentReference[oaicite:15]{index=15}

**Practical rule for this folder:**  
If a model meaningfully reveals a sensitive site, **do not store it in `web/assets/`**. Publish a generalized proxy (or none), and store the full model behind authenticated delivery.

> 💡 Inspiration: platforms like Mukurtu use Traditional Knowledge (TK) labels and cultural protocols for fine-grained access; KFM proposals encourage similar “differential access” for sensitive heritage content.:contentReference[oaicite:16]{index=16}

---

## 📁 Recommended layout (within the site)

> This README lives in: `web/assets/3d/archaeology/sites/<site-slug>/models/glb/README.md`

Suggested nearby structure (adjust if your repo differs):

```text
🗺️ web/assets/3d/archaeology/sites/<site-slug>/
├─ 🧾 site.meta.json                  # site-level metadata (optional but recommended)
└─ 🧩 models/
   └─ 🧊 glb/
      ├─ README.md                    # 👈 you are here
      ├─ <model-id>.glb
      ├─ <model-id>.meta.json         # required sidecar (see below)
      ├─ <model-id>.thumb.webp        # optional thumbnail for UI cards
      ├─ <model-id>__lod1.glb         # optional lower LOD
      └─ <model-id>__collision.glb    # optional collision mesh (simple)
```

---

## 🏷️ Naming conventions

Keep names stable, URL-safe, and machine-sortable.

### ✅ Recommended pattern
`<model-id>__v<YYYYMMDD>__lod<N>.glb`

Examples:
- `mound-a__v20260125__lod0.glb`
- `mound-a__v20260125__lod1.glb`
- `ceramic-shard-017__v20260125__lod0.glb`

### 🎯 Why this format?
- Works well with static hosting + caching
- Supports reproducible snapshots (version tags)
- Makes LOD selection deterministic

KFM also emphasizes **reproducible research and versioned releases/snapshots** as a broader platform goal, so explicit model versions help long-term traceability.:contentReference[oaicite:17]{index=17}

---

## 🧾 Sidecar metadata (required)

Every `.glb` must have a sibling `<same-name>.meta.json`.

Why: KFM is **catalog-driven / evidence-first**, linking **STAC/DCAT/PROV** so assets remain discoverable, governable, and auditable.:contentReference[oaicite:18]{index=18}

### ✅ Minimum required fields (recommended)
- `id` (stable internal id)
- `site_slug`
- `title`, `description`
- `license` + attribution
- `kfm:classification` + `kfm:sensitivity`
- `sha256` (or equivalent checksum)
- `crs` + `units`
- `prov` / `stac` / `dcat` references (URLs or IDs)

> KFM policy gates expect sensitivity + license fields and metadata QA is designed to fail if required fields are missing.:contentReference[oaicite:19]{index=19}

### 📄 Example `*.meta.json` (template)
```json
{
  "id": "kfm:archaeology:<site-slug>:mound-a",
  "site_slug": "<site-slug>",
  "model_id": "mound-a",
  "title": "Mound A (LOD0)",
  "description": "Web-optimized 3D surface model for interpretive visualization.",
  "license": "CC-BY-4.0",
  "attribution": [
    "Example University Lab",
    "Kansas Frontier Matrix Contributors"
  ],
  "kfm:classification": "public",
  "kfm:sensitivity": "sensitive-location",
  "units": "meters",
  "up_axis": "Y",
  "sha256": "<fill-me>",
  "placement": {
    "mode": "generalized",
    "note": "Do not store precise coordinates in public web assets."
  },
  "links": {
    "stac_item": "<stac-item-url-or-id>",
    "dcat_dataset": "<dcat-dataset-url-or-id>",
    "prov_activity": "<prov-activity-url-or-id>"
  },
  "cultural_protocols": {
    "tk_labels": [],
    "notes": "If applicable, add community-defined access protocols."
  }
}
```

---

## 🛰️ Coordinates, CRS, and placement

KFM standardizes geospatial data to **WGS84 / EPSG:4326** while retaining original CRS in provenance/metadata.:contentReference[oaicite:20]{index=20}

For placement logic, keep these concepts separate:
- **Model space**: the mesh in meters (local coordinates)
- **Geographic placement**: lat/lon/height + orientation (handled by the viewer/runtime)

The broader KFM ecosystem commonly exports geometries to WGS84 (EPSG:4326).:contentReference[oaicite:21]{index=21}:contentReference[oaicite:22]{index=22}

### 🫥 Sensitive-site placement guidance
If location is sensitive, store only generalized placement (or none). Some platforms round sensitive coordinates to ~10 km and display a generic marker; KFM proposals encourage similar obfuscation techniques for vulnerable sites/species.:contentReference[oaicite:23]{index=23}

---

## 🪶 Optimization & performance (web targets)

> These are pragmatic defaults; tune per site + device targets.

### 🎛️ Suggested budgets
- **LOD0 (desktop):** 50k–250k triangles
- **LOD1 (mobile):** 10k–75k triangles
- **Texture max:** 2K (4K only if justified)
- Prefer **PBR** materials and avoid “unlit” unless intentionally stylized

### ✅ Best practices
- Center pivot sensibly (avoid huge offsets)
- Remove hidden geometry
- Bake detail to normals where possible
- Prefer compressed textures (KTX2/Basis) when supported by your runtime

---

## ✅ Validation & policy gates (KFM-style)

KFM’s pipeline is designed so that **artifacts are promoted** through a reproducible flow:

```mermaid
flowchart LR
  RAW[📥 Raw] --> WORK[🛠️ Work]
  WORK --> PROC[⚙️ Processed]
  PROC --> CATS[📚 Catalogs (STAC/DCAT/PROV)]
  CATS --> GRAPH[🧠 Graph]
  GRAPH --> API[🔌 API]
  API --> UI[🖥️ UI]
  UI --> STORY[📖 Story / Focus]
```

This ordering is explicitly called out in KFM documentation.:contentReference[oaicite:24]{index=24}

### 🔎 Checks to run (recommended)
- glTF validation (structure, extensions)
- File size / triangle thresholds
- Metadata completeness (license, sensitivity, attribution, links)
- Hash generation and recording

KFM’s Policy Pack approach is intended to **break the build** if provenance/metadata requirements aren’t met, using automated checks in the pipeline.:contentReference[oaicite:25]{index=25}

---

## 📦 Storage & distribution (large binaries)

3D models get big fast. KFM guidance suggests using tooling that avoids bloating normal Git history:
- **Git LFS** for large binaries (recommended for big `.glb` files).:contentReference[oaicite:26]{index=26}
- **DVC** can be used for large artifacts with reproducible pointers/versions.:contentReference[oaicite:27]{index=27}

### 🧰 Advanced: OCI artifact delivery (optional)
For “artifact-as-package” workflows (especially if you want signatures + SBOMs), KFM proposals suggest distributing datasets/artifacts via OCI registries using tools like `oras`, `cosign`, and `syft` (in addition to standard object storage/CDNs).:contentReference[oaicite:28]{index=28}

---

## 🧩 Hooking a model into Story Nodes

KFM Story Nodes are designed as:
- Markdown content **with structured metadata** (JSON header) for machine ingest and rendering in the UI.
- Managed as versioned content in the UI system (story loading / management is a core feature).:contentReference[oaicite:30]{index=30}

### 📄 Suggested Story Node snippet (example)
> **Note:** Schema may evolve; treat this as a starting convention.

```markdown
{
  "id": "story:<site-slug>:mound-a",
  "title": "Mound A — 3D View",
  "mode": "3d",
  "assets": [
    {
      "type": "model/glb",
      "src": "/assets/3d/archaeology/sites/<site-slug>/models/glb/mound-a__v20260125__lod0.glb",
      "meta": "/assets/3d/archaeology/sites/<site-slug>/models/glb/mound-a__v20260125__lod0.meta.json"
    }
  ]
}

## Interpretation
Explain what the user is seeing, and cite sources.
```

---

## 🧠 Focus Mode + model narratives (evidence-first)

KFM’s AI “Focus Mode” is designed to:
- **Always cite sources** and maintain an evidence-first posture (no uncited claims).
- Show an **audit panel** describing sources, reasoning steps, and provenance context.:contentReference[oaicite:31]{index=31}

If you add AI-generated descriptions of a model (or interpretive text), treat the `.meta.json` and linked STAC/DCAT/PROV as the “source of truth” so the AI can cite properly.

---

## 🔄 Updating & refresh cadence (don’t let models rot)

Some source data (especially web-sourced) can be dynamic and may require periodic reprocessing; data mining literature notes web data changes over time and mining processes may need replication at intervals.:contentReference[oaicite:32]{index=32}

For models, that often means:
- re-running decimation/texture bakes when standards/tools change
- regenerating LODs for new device targets
- updating metadata when license/attribution changes

---

## 📚 Project docs used & related (grab these first)

### 🧠 Core KFM system docs
- KFM Technical Documentation :contentReference[oaicite:33]{index=33}  
- KFM Architecture / Features / Design :contentReference[oaicite:34]{index=34}  
- KFM AI System Overview (Focus Mode, auditability) :contentReference[oaicite:35]{index=35}  
- KFM UI System Overview (2D/3D, Story Nodes, sensitive layers)   
- KFM Data Intake Guide (STAC/DCAT/PROV, policy gates, pipeline order) :contentReference[oaicite:37]{index=37}  

### 💡 Ideas & future proposals
- Latest Ideas & Future Proposals :contentReference[oaicite:38]{index=38}  
- Innovative Concepts to Evolve KFM (CARE, cultural protocols, sensitivity) :contentReference[oaicite:39]{index=39}  
- Additional Project Ideas (OCI artifacts, domain packs)   

### 🛠️ Engineering & research references bundled in the project
- Open-Source Hub Design (pipeline + web folder, MapLibre/Cesium context) :contentReference[oaicite:41]{index=41}  
- Python Geospatial Analysis Cookbook (WGS84/EPSG:4326 patterns) :contentReference[oaicite:42]{index=42}  
- Scientific Method / Master Coder Protocol (large files, Git LFS)   
- Data Mining Concepts & Applications (refresh cadence, ETL framing) :contentReference[oaicite:44]{index=44}  

### 📦 PDF portfolio libraries (open in Acrobat to browse the embedded references)
- AI Concepts & more (PDF portfolio) :contentReference[oaicite:45]{index=45} 
- Data Management / Architectures / Data Science (PDF portfolio) :contentReference[oaicite:47]{index=47} 
- Maps / Google Maps / Virtual Worlds / Archaeological CG / WebGL (PDF portfolio) :contentReference[oaicite:49]{index=49} 
- Various Programming Languages & Resources (PDF portfolio) :contentReference[oaicite:51]{index=51} :contentReference[oaicite:52]{index=52}

---

## 🧷 Maintainer checklist (copy/paste)

- [ ] Add `.glb` with stable naming + version tag  
- [ ] Add matching `.meta.json` with **license + sensitivity + attribution + checksums**  
- [ ] Ensure sensitive sites are **generalized** (or kept out of public web assets)  
- [ ] Link to STAC/DCAT/PROV IDs (or plan the promotion step that will mint them)  
- [ ] Run validator + size/perf checks  
- [ ] Confirm Story Nodes / UI references point to the right asset paths  
- [ ] If AI narrative is added, ensure **citations** + auditable provenance  

🧡 If you’re unsure whether a model is safe to publish: default to **restrict** + **generalize** first, then escalate through governance.

