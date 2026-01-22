# 🧾 STAC Items — Experiment Evidence Catalog

![STAC](https://img.shields.io/badge/STAC-Items-blue)
![W3C PROV](https://img.shields.io/badge/W3C-PROV-orange)
![W3C DCAT](https://img.shields.io/badge/W3C-DCAT-purple)
![Evidence-First](https://img.shields.io/badge/Evidence-First-success)
![Policy-as-Code](https://img.shields.io/badge/Policy-as%20Code-informational)

> [!IMPORTANT]
> This folder is the **STAC** portion of an experiment’s **evidence triplet**:
> **STAC (this folder) + DCAT + PROV** → so every output is discoverable, mappable (when relevant), and reproducible/auditable.

---

## 📍 You are here

`mcp/dev_prov/examples/10_experiment_report_template/(example_report_tree)/stac/items/`

This directory contains **STAC Item JSON** files — one per **experiment artifact** (dataset output, figure, report, model, log bundle, etc.).

---

## 🧩 What belongs in `stac/items/`

✅ Put a STAC Item here when the experiment produces **something you’d want to reference, cite, compare, or re-use**, such as:

- 🗺️ **Geospatial outputs**: GeoJSON, GeoPackage, COG/GeoTIFF, vector tiles, 3D Tiles, etc.
- 📈 **Analysis outputs**: plots, metrics tables, dashboards exports, notebooks (as artifacts), reports (PDF/MD)
- 🤖 **Model outputs**: weights/checkpoints, evaluation results, model cards
- 🧾 **Run evidence**: checksums, manifests, configs, pipeline logs (as assets linked from the Item)

❌ Don’t put the *raw bytes* directly in this folder. **This folder is metadata**, not storage.

---

## 🗂️ How it fits the “example report tree”

A typical “experiment report tree” looks like this:

```text
(example_report_tree)/
├─ 📁 stac/
│  ├─ 📁 collections/
│  └─ 📁 items/          👈 you are here
├─ 📁 dcat/
├─ 📁 prov/
├─ 📁 report/
└─ 📁 assets/            (optional: local artifact storage)
```

**The report** cites Items by `id`, and automation can build an “Artifacts” table by reading this directory. 🧠

---

## 🧠 Why STAC Items in an experiment report?

- **One consistent artifact format** for discovery + linking (even when outputs are a mix of spatial + non-spatial)
- **Trust by design**: every visual layer/chart/model can be traced back to its sources and transformations
- **Reproducibility**: every result can point to the exact bytes + method + code version
- **UI friendliness**: Items can drive map layers, time sliders, and “show me the source” panels

---

## 🔁 Core principles (the rules of the road)

> [!NOTE]
> These rules are written in “RFC language”:
> **MUST / SHOULD / MAY** = required / recommended / optional.

### ✅ Evidence-first publishing
- An artifact **MUST** have enough metadata to be audited and re-produced.
- An artifact **MUST** link to **its provenance** (PROV) and **its catalog entry** (DCAT).

### 🧬 Deterministic + replayable
- Outputs **SHOULD** be reproducible from raw inputs + config + code version.
- Items **SHOULD** include a stable `run_id` / `experiment_id` and a code reference (e.g., git SHA).

### 🔒 Governance-aware
- Items **MUST** declare **license** and **classification/sensitivity** (project policy may enforce this).
- If an output includes sensitive coordinates, you **SHOULD** generalize/obfuscate geometry and mark it.

### 🧩 No “mystery artifacts”
- Every Item in this folder **MUST** be attributable to:
  - a run (activity),
  - an agent (who/what produced it),
  - and its inputs (what it was derived from).

---

## 🧱 STAC Item contract (template)

At minimum, every Item in this folder **MUST** include:

### 1) Required STAC shape
- `type` (usually `"Feature"`)
- `stac_version`
- `id`
- `properties`
  - `datetime` **or** `start_datetime` + `end_datetime`
- `assets` (at least **one** asset)
- `links` (at least to **collection** and to **PROV/DCAT**)

### 2) Recommended dev_prov / KFM-style extensions (names are project-defined)
Add these (or your project equivalents) to make Items “queryable evidence”:

- `properties.kfm:dataset_id` (or equivalent stable dataset key)
- `properties.kfm:classification` / `properties.kfm:sensitivity`
- `properties.kfm:experiment_id` / `properties.kfm:run_id`
- `properties.kfm:code_ref` (git SHA/tag) and/or `properties.kfm:pr_ref`
- `properties.kfm:inputs` (IDs of input Items / dataset IDs)
- `properties.kfm:checksums` (sha256 or multihash for key assets)
- `properties.kfm:qa` (validation summary, thresholds passed, etc.)

---

## 🔗 Link relations we expect

You’ll typically include these `links[]` entries:

| `rel` | Points to | Why it matters |
|---|---|---|
| `collection` | the parent STAC Collection | groups related experiment outputs |
| `root` / `parent` | catalog navigation (if used) | supports traversing the STAC tree |
| `via` or `derived_from` (project-defined) | upstream Item(s) | lineage at the STAC level |
| `describedby` | DCAT dataset entry | discovery, publisher, license, distributions |
| `provenance` (project-defined) | PROV bundle/document | reproducibility + audit trail |

> [!TIP]
> Keep the **STAC Item** about *what this artifact is*, and let **PROV** describe *how it was made*.

---

## 📦 Assets: what an Item should point to

Each `assets.{key}` entry **SHOULD** include:

- `href` (local relative path, API URL, or content-addressed reference)
- `type` (MIME type)
- `roles` (e.g., `["data"]`, `["metadata"]`, `["thumbnail"]`, `["model"]`, `["report"]`, `["logs"]`)
- optional: `title`, `description`

### Storage options (choose what the template supports)
- 🗃️ **Repo-local** (small outputs): `../assets/...`
- ☁️ **Object storage / HTTP** (large outputs): `https://...`
- 📦 **OCI artifacts** (supply-chain friendly): `oci://...@sha256:...` (great for signed bundles)

---

## 🧪 Common patterns (copy these mental models)

### A) 🗺️ Spatial layers (Map-friendly)
Use real `geometry` + `bbox`, and set temporal fields if it varies by time.  
If you support 2D/3D, assets may include:
- raster (COG/GeoTIFF)
- vector tiles
- 3D Tiles / glTF
- a thumbnail preview

### B) 📈 Non-spatial artifacts (metrics, PDFs, notebooks)
Still create a STAC Item (for uniformity), but:
- use `geometry: null` and `bbox: null` **or** a project-approved placeholder
- rely on rich `properties` + `assets`

### C) 📡 Streaming / incremental observations
Two safe strategies:
- **1 Item per observation** (immutable receipts), or
- **1 Item per time bucket** (hour/day) with versioned assets

Either way, don’t overwrite evidence silently.

### D) 🤖 AI/model outputs (treat as first-class evidence)
A model artifact **SHOULD** include assets for:
- model weights/checkpoint
- evaluation metrics
- training config (exact hyperparams)
- model card (human-readable)

> [!IMPORTANT]
> AI-produced narratives/results should be **evidence-backed**: link to the Items/inputs they summarize or use.

### E) 🕰️ AR / 4D / simulation outputs (future-proofing)
If you’re producing “time travel” outputs, scenarios, or 3D story layers:
- store them as normal Items
- keep time explicit (per-slice Items or per-scenario Items)
- point to 3D Tiles/CZML/glTF assets when relevant

---

## 🛡️ Validation & policy gates (what will break CI)

Expect automated checks to enforce:
- presence of the evidence triplet (STAC + DCAT + PROV)
- license + classification/sensitivity labels
- provenance completeness (inputs ↔ activity ↔ outputs)
- schema validity (STAC JSON shape + project profile)
- “no unsourced outputs” (especially for AI-facing artifacts)

> [!TIP]
> If you’re unsure what’s required: add more metadata, not less. Your future self will thank you. 😄

---

## 🧾 Examples (copy/paste starters)

<details>
<summary><strong>Example 1 — Geospatial raster output (COG)</strong> 🗺️</summary>

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "EXP-001__ndvi__2025-06-01",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.05, 40.00],
      [-94.60, 40.00],
      [-94.60, 36.99],
      [-102.05, 36.99],
      [-102.05, 40.00]
    ]]
  },
  "bbox": [-102.05, 36.99, -94.60, 40.00],
  "properties": {
    "datetime": "2025-06-01T00:00:00Z",
    "title": "NDVI Raster (June 1, 2025)",
    "description": "Derived NDVI output for EXP-001.",
    "kfm:experiment_id": "EXP-001",
    "kfm:run_id": "run-20250601-001",
    "kfm:code_ref": "git:abcdef1234567890",
    "kfm:classification": "public"
  },
  "links": [
    { "rel": "collection", "href": "../collections/EXP-001.collection.json", "type": "application/json" },
    { "rel": "describedby", "href": "../../dcat/EXP-001.dataset.jsonld", "type": "application/ld+json" },
    { "rel": "provenance", "href": "../../prov/EXP-001.run-20250601-001.prov.jsonld", "type": "application/ld+json" }
  ],
  "assets": {
    "data": {
      "href": "../../assets/EXP-001/ndvi_2025-06-01.tif",
      "type": "image/tiff; application=geotiff",
      "roles": ["data"],
      "title": "NDVI COG"
    },
    "thumbnail": {
      "href": "../../assets/EXP-001/ndvi_2025-06-01.thumb.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    }
  }
}
```
</details>

<details>
<summary><strong>Example 2 — Non-spatial metrics + report</strong> 📈</summary>

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "EXP-001__evaluation__run-20250601-001",
  "geometry": null,
  "bbox": null,
  "properties": {
    "datetime": "2025-06-01T03:14:15Z",
    "title": "Evaluation Metrics",
    "description": "Metrics + report for EXP-001 run-20250601-001.",
    "kfm:experiment_id": "EXP-001",
    "kfm:run_id": "run-20250601-001",
    "kfm:code_ref": "git:abcdef1234567890",
    "kfm:classification": "internal"
  },
  "links": [
    { "rel": "collection", "href": "../collections/EXP-001.collection.json", "type": "application/json" },
    { "rel": "describedby", "href": "../../dcat/EXP-001.dataset.jsonld", "type": "application/ld+json" },
    { "rel": "provenance", "href": "../../prov/EXP-001.run-20250601-001.prov.jsonld", "type": "application/ld+json" }
  ],
  "assets": {
    "metrics": {
      "href": "../../assets/EXP-001/metrics.csv",
      "type": "text/csv",
      "roles": ["data"]
    },
    "report": {
      "href": "../../report/EXP-001.md",
      "type": "text/markdown",
      "roles": ["report"]
    },
    "config": {
      "href": "../../assets/EXP-001/run-config.yaml",
      "type": "text/yaml",
      "roles": ["metadata"]
    }
  }
}
```
</details>

---

## 🧷 Quick checklist (before you commit)

- [ ] Item file name is stable + meaningful (includes `experiment_id` and/or `run_id`)
- [ ] `id` is unique and stable (won’t collide across runs)
- [ ] `assets` include the actual artifact bytes (or a stable reference to them)
- [ ] `links` include: **collection**, **DCAT**, **PROV**
- [ ] License + classification/sensitivity are present (project policy)
- [ ] If spatial, `geometry` + `bbox` are valid and safe to publish
- [ ] If AI/model output, include model card + config and link to inputs

---

## 🧵 Optional: Pulse Threads & micro-audits (dev_prov friendly)

If you track micro-updates during a run (mini “lab notebook” entries), reference STAC Item IDs in those updates.  
This makes it easy to build timelines of “what changed and why” without guessing.

---

## 🔎 Mini-glossary

- **STAC Item**: one “artifact card” describing a single output and its assets.
- **STAC Collection**: groups related Items (e.g., all artifacts for EXP-001).
- **DCAT Dataset**: higher-level catalog record (publisher, license, distributions).
- **PROV**: lineage record describing inputs → activity → outputs (and agents).

---

## 🧭 See also (sibling folders)

- `../collections/` — the parent collections for these items
- `../../dcat/` — dataset-level discovery records
- `../../prov/` — lineage bundles for reproducibility
- `../../report/` — the human-readable experiment report
