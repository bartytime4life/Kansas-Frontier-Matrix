# 🧪 Quickstart Input — Minimal Triplet (STAC + DCAT + PROV)

![Example](https://img.shields.io/badge/example-00__quickstart__minimal__triplet-2563eb?style=for-the-badge)
![Provenance](https://img.shields.io/badge/provenance-first-7c3aed?style=for-the-badge)
![STAC](https://img.shields.io/badge/STAC-JSON-0ea5e9?style=for-the-badge)
![DCAT](https://img.shields.io/badge/DCAT-JSON--LD-22c55e?style=for-the-badge)
![PROV](https://img.shields.io/badge/W3C%20PROV-JSON--LD-ef4444?style=for-the-badge)
![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-governance-111827?style=for-the-badge)

> [!NOTE]
> This folder contains the **smallest “evidence pack”** KFM-style systems can accept: **STAC + DCAT + PROV**.
> It’s intentionally minimal so you can swap in your own dataset without changing the example’s shape.

---

## 📦 What goes in `input/`

This `input/` directory is the payload for the **`00_quickstart_minimal_triplet`** example under `mcp/dev_prov`.

Think of it as: **“Here is the dataset 🧱 + here is what it is 🧾 + here is how it was made 🧬.”**

### 🗂️ Recommended layout

```text
input/
  🧾 stac.item.json            # STAC Item (or Collection) describing the geospatial asset(s)
  🧾 dcat.dataset.jsonld        # DCAT Dataset describing catalog + licensing + distributions
  🧾 prov.bundle.jsonld         # W3C PROV bundle linking source(s) -> process -> outputs
  📦 artifacts/                 # (optional) local data files referenced by STAC/DCAT
    ├─ 🗺️ data.geojson
    ├─ 🧊 data.parquet
    └─ 🧾 README.md             # (optional) human notes about artifacts
  📝 README.md                  # this file
```

> [!TIP]
> If the runner expects specific filenames, keep the defaults above.
> If your implementation supports configuration, you can rename—**but keep the STAC/DCAT/PROV roles intact**.

---

## 🧩 The “Triplet” explained (in plain English)

### 🧾 1) STAC (SpatioTemporal Asset Catalog)
Describes **where/when** a geospatial asset applies and points to the asset(s) (files, tiles, COGs, GeoParquet, etc.).

### 🧾 2) DCAT (Data Catalog Vocabulary)
Describes **what the dataset is** in catalog terms: title, description, publisher, license, themes, distributions, access URLs.

### 🧬 3) W3C PROV
Describes **how it came to be**: sources used, processing activity, responsible agent(s), timestamps, derivations.

> [!IMPORTANT]
> KFM’s stance is “no mystery layers”: **if it’s shown, it must be attributable and traceable** ✅

---

## ✅ Required files (minimum expectations)

| File | Role | Minimal must-haves | “Why it matters” |
|---|---|---|---|
| `stac.item.json` | 📍 Spatial/temporal footprint + asset links | `id`, `bbox`, `geometry`, `datetime` or `start/end`, `assets` | Powers map layer extents, spatial search, timeline hooks 🗺️⏳ |
| `dcat.dataset.jsonld` | 📚 Catalog + license + distribution | `identifier`, `title`, `description`, `license`, `distribution` | Powers discovery + attribution + legal clarity 🧾⚖️ |
| `prov.bundle.jsonld` | 🧬 Lineage graph | `Entity`(source/output), `Activity`, `Agent`, `used`, `generated` | Powers auditing, reproducibility, “why should I trust this?” 🔎 |

---

## 🧠 Conventions that keep the triplet “KFM-grade”

### 1) 🔒 Treat `input/` like immutable evidence
- Don’t “fix bytes in place” during a run.
- If something needs cleaning/reprojection, do it as a **new derived artifact** and record it in **PROV**.

### 2) 🏷️ IDs should be stable & boring
Pick a dataset identifier that won’t change every run, e.g.:

- `kfm.ks.rivers.usgs_nwis.points.v1`
- `kfm.ks.counties.boundaries.2024.v1`

> [!TIP]
> If you *do* version, version intentionally (`v1`, `v2`), not accidentally (timestamps in IDs).

### 3) 🧾 Always include a license
If you can’t state licensing clearly, **don’t publish**. (Even for examples, use a placeholder like “UNKNOWN” and fail the gate in CI if desired.)

### 4) 🧯 Sensitivity / FAIR+CARE
If any data could be sensitive (private land stations, protected site locations, culturally restricted material):
- mark it clearly in metadata (DCAT + optional custom fields)
- ensure the system can enforce visibility rules

### 5) 🧪 Determinism & reproducibility
If you run the same inputs + config, outputs should be reproducible.
That’s the whole point of connecting **artifacts** to **lineage**.

---

## 🛠️ Drop-in steps (swap this example to your own dataset)

### Step 1 — Put your data artifacts (optional)
Place your files under `artifacts/` (or point to remote URLs/registries).

Examples:
- `artifacts/data.geojson`
- `artifacts/data.parquet`
- `artifacts/raster.tif` (COG preferred)

### Step 2 — Update STAC to point at the artifact(s)
- Update `assets.*.href` to the correct relative/absolute location(s)
- Ensure `bbox/geometry` reflect the spatial extent
- Ensure time fields are present (`datetime` or `start_datetime` + `end_datetime`)

### Step 3 — Update DCAT to describe the dataset
- Title, description, keywords/themes
- License ✅
- Add at least one distribution:
  - local file
  - API endpoint
  - object store URL
  - registry reference

### Step 4 — Update PROV to connect the dots
- PROV `Entity` for the raw source(s)
- PROV `Activity` describing ingestion/transformation
- PROV `Entity` for the outputs (STAC/DCAT and/or produced data artifacts)
- PROV `Agent` representing the pipeline and/or maintainer

---

## 🧱 Minimal templates (copy/paste friendly)

> [!NOTE]
> These are intentionally tiny. Add richer fields/extensions as your gates require.

### 🧾 STAC Item — minimal skeleton

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "<dataset_id>",
  "bbox": [-102.051, 36.993, -94.588, 40.003],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.051, 36.993], [-94.588, 36.993],
      [-94.588, 40.003], [-102.051, 40.003],
      [-102.051, 36.993]
    ]]
  },
  "properties": {
    "datetime": "2026-01-21T00:00:00Z"
  },
  "assets": {
    "data": {
      "href": "artifacts/data.geojson",
      "type": "application/geo+json",
      "roles": ["data"],
      "title": "Primary dataset artifact"
    }
  },
  "links": []
}
```

### 🧾 DCAT Dataset — minimal JSON-LD skeleton

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dcterms": "http://purl.org/dc/terms/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@type": "dcat:Dataset",
  "dcterms:identifier": "<dataset_id>",
  "dcterms:title": "Example Dataset Title",
  "dcterms:description": "One-paragraph description of what this dataset represents and how it can be used.",
  "dcterms:license": "https://spdx.org/licenses/CC-BY-4.0.html",
  "dcat:keyword": ["kansas", "example", "geospatial"],
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dcterms:title": "Download (GeoJSON)",
      "dcat:downloadURL": "artifacts/data.geojson",
      "dcterms:format": "GeoJSON"
    }
  ]
}
```

### 🧬 PROV Bundle — minimal JSON-LD skeleton

```json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "@graph": [
    {
      "@id": "urn:kfm:agent:pipeline",
      "@type": "prov:Agent",
      "prov:label": "dev_prov example pipeline"
    },
    {
      "@id": "urn:kfm:activity:ingest:001",
      "@type": "prov:Activity",
      "prov:startedAtTime": "2026-01-21T00:00:00Z",
      "prov:endedAtTime": "2026-01-21T00:00:05Z",
      "prov:wasAssociatedWith": { "@id": "urn:kfm:agent:pipeline" }
    },
    {
      "@id": "urn:kfm:entity:artifact:data",
      "@type": "prov:Entity",
      "prov:label": "Input data artifact",
      "prov:location": "artifacts/data.geojson"
    },
    {
      "@id": "urn:kfm:entity:stac",
      "@type": "prov:Entity",
      "prov:label": "STAC Item",
      "prov:location": "stac.item.json",
      "prov:wasGeneratedBy": { "@id": "urn:kfm:activity:ingest:001" }
    },
    {
      "@id": "urn:kfm:entity:dcat",
      "@type": "prov:Entity",
      "prov:label": "DCAT Dataset",
      "prov:location": "dcat.dataset.jsonld",
      "prov:wasGeneratedBy": { "@id": "urn:kfm:activity:ingest:001" }
    },
    {
      "@id": "urn:kfm:activity:ingest:001",
      "prov:used": [
        { "@id": "urn:kfm:entity:artifact:data" }
      ]
    },
    {
      "@id": "urn:kfm:entity:stac",
      "prov:wasDerivedFrom": { "@id": "urn:kfm:entity:artifact:data" }
    },
    {
      "@id": "urn:kfm:entity:dcat",
      "prov:wasDerivedFrom": { "@id": "urn:kfm:entity:artifact:data" }
    }
  ]
}
```

---

## 🧷 Validation checklist (what “good” looks like)

- [ ] **STAC parses** and contains `id`, `assets`, `bbox/geometry`, and time
- [ ] **DCAT parses** and contains `identifier`, `title`, `description`, `license`, `distribution`
- [ ] **PROV parses** and includes at least one `Agent`, `Activity`, and `Entity` chain
- [ ] **All references resolve** (file paths exist, URLs valid, registry refs correct)
- [ ] **License exists** (no “mystery data”)
- [ ] **Sensitivity is explicit** if needed (don’t leak restricted locations)
- [ ] **Triplet is coherent**: IDs match, outputs are linked, provenance tells a real story

> [!IMPORTANT]
> “Fail closed” is the intended posture: if metadata is incomplete, the dataset should not be accepted or shown. 🚫✅

---

## 🌐 Why this triplet matters beyond the example

Even in a “minimal quickstart,” this triplet is the foundation for:

- 🗺️ **UI transparency**: layer popups can show “source/license/how prepared”
- 🧭 **Focus Mode / AI answers with citations**: responses can cite back to DCAT + lineage
- 📤 **Exports with attribution**: sharing a view/report can include proper credits automatically
- 📦 **Artifact registries & signing**: artifacts can be versioned, signed, and linked back to PROV
- ⏱️ **Real-time feeds**: repeated observations still need provenance stubs before display

---

## 🧯 Common pitfalls (and how to avoid them)

- **BBox order wrong** → use `[minLon, minLat, maxLon, maxLat]`
- **Missing time** → at least `datetime` (or start/end range)
- **Assets don’t exist** → broken `href` paths, wrong relative roots
- **License missing** → gate should reject
- **PROV is “decorative”** → if it doesn’t connect sources → activity → outputs, it’s not provenance
- **IDs drift** → keep a stable dataset identifier across triplets

---

## 📚 Project docs behind this design (optional deep dive)

<details>
<summary><strong>Open the KFM design context 🧭</strong></summary>

- **Data Intake philosophy**: provenance-first, immutable raw boundary, deterministic pipelines
- **Architecture**: STAC/DCAT/PROV as mandatory artifacts; policy gates; FAIR+CARE
- **AI system**: retrieval + governance checks + citations + PROV logging for derived answers
- **UI system**: “map behind the map,” layer provenance panels, timeline/story nodes
- **Future proposals**: real-time watchers producing STAC/DCAT; bulk doc ingestion; AR modes
- **Research packs**: mapping/virtual worlds/WebGL + data management + AI concepts + polyglot resources

</details>

