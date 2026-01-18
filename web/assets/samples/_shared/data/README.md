# 🧪📦 Shared Sample Data (Frontend)

![Scope](https://img.shields.io/badge/scope-frontend%20samples-blue)
![Contracts](https://img.shields.io/badge/contract--first-required-success)
![Provenance](https://img.shields.io/badge/provenance-traceable%20by%20design-brightgreen)
![Formats](https://img.shields.io/badge/formats-GeoJSON%20%7C%20JSON%20%7C%20CSV%20%7C%20STAC-informational)

Welcome to **`web/assets/samples/_shared/data/`** 🗂️  
This directory holds **small, deterministic, front-end–friendly datasets** used by **UI samples**, **demos**, and **test fixtures**.

> [!IMPORTANT]
> ✅ **This is not the canonical data store.**  
> Canonical datasets flow through the pipeline (**ETL → catalogs → graph → APIs → UI**).  
> Anything “real” belongs upstream (e.g., `data/processed/` + `data/catalog/`), not here.

---

## 🎯 Why this folder exists

We keep a shared data shelf for samples so we can:
- build UI components without waiting on the full backend,
- keep demos deterministic (fixtures don’t “drift”),
- avoid duplicating the same small datasets across multiple sample apps,
- prototype map layers / story steps safely.

---

## ✅ What belongs here

- 📄 **Tiny datasets** that load fast in the browser (fixtures & demos)
- 🧩 **Schema-aligned** data that mirrors API responses or cataloged assets
- 🧾 **Metadata alongside data** (contracts + provenance pointers)
- 🧪 **Deterministic** content (repeatable builds / consistent screenshots)

---

## 🚫 What does *not* belong here

- 🧱 “Real” production datasets (large rasters, full vector layers, raw downloads)
- 🕵️ “Mystery files” with no provenance, license, or attribution
- 🔐 Anything sensitive or disallowed by governance/redaction rules
- 🧨 Data that bypasses the backend contracts (this folder must never become a side-door)

---

## 🧭 Relationship to the KFM pipeline

KFM is designed so **every displayed claim/data product can be traced back to evidence**.  
Even samples should respect that posture:

### ✅ Sample data rules of thumb
- If the data is **derived from a canonical dataset**, include a **pointer back**:
  - STAC Item / Collection ID (or path)
  - DCAT dataset entry (or path)
  - PROV lineage bundle (or path)
- If it’s **purely synthetic**, say so explicitly and label it as a fixture.
- Samples should **mimic real shapes** (schemas) so UI dev doesn’t “lie” to us.

---

## 🗂️ Recommended structure

> This folder may evolve, but **keep things predictable** and grouped by purpose.

```text
web/
└─ 📁 assets/
   └─ 🧪 samples/
      └─ ♻️ _shared/
         └─ 🗂️ data/
            ├─ 📄 README.md                       # 👈 you are here 📌 What fixtures exist, size limits, and “not authoritative” rules
            ├─ 🧭🧾 manifest.samples.json          # 🧭 Optional index: sampleId → file pointers + tags + intended demo use
            ├─ 🗺️ geojson/                        # 🗺️ Vector fixtures (tiny GeoJSON for layer demos/tests)
            ├─ 🛰️ stac/                           # 🛰️ Small STAC examples (Items/Collections + minimal assets)
            ├─ 📊 tables/                         # 📊 CSV/TSV fixtures for charts/tables (small + deterministic)
            ├─ 🖼️ images/                         # 🖼️ Tiny thumbnails used in demos (webp/png; keep minimal)
            └─ 🧾 _meta/                          # 🧾 Shared metadata: licenses, citations, generation notes, provenance hints
```

---

## 🏷️ Naming conventions

Keep names:
- **lowercase + kebab-case**
- **explicitly sample-scoped**
- paired with a contract file

Examples ✅
- `geojson/kansas-counties.sample.geojson`
- `tables/weather-stations.sample.csv`
- `stac/flint-hills.sample.item.json`

Pair each data file with a contract ✅
- `kansas-counties.sample.geojson`
- `kansas-counties.sample.contract.json`

---

## 🧾 Sample “data contract” (metadata) expectations

Even in samples, we want **contract-first** behavior: every dataset is accompanied by machine-readable metadata.

**Minimum** contract fields (recommended):
- `id` (stable unique identifier)
- `title`, `description`
- `version` (semver-style)
- `kind` (`vector | raster | table | stac | api-fixture`)
- `formats` / `mimeTypes`
- `license` + attribution
- `sources[]` (citations or “synthetic” declaration)
- `canonicalRefs` (optional but preferred)
- `spatial` / `temporal` (when applicable)
- `schemaHints` (columns/properties used by UI)

<details>
<summary><strong>📄 Contract template (copy/paste)</strong></summary>

```json
{
  "id": "kfm.sample.kansas-counties",
  "title": "Kansas Counties (Sample)",
  "description": "Small GeoJSON fixture for UI layer toggles, styling, and hover/click popups.",
  "version": "1.0.0",
  "kind": "vector",
  "formats": ["geojson"],
  "license": "SEE_SOURCES",
  "attribution": "See sources[]",
  "sources": [
    {
      "type": "source",
      "name": "AUTHORITATIVE_SOURCE_NAME_OR_ARCHIVE",
      "url": "https://example.com/source",
      "retrieved": "YYYY-MM-DD",
      "license": "PUBLIC_DOMAIN_OR_LICENSE_ID",
      "notes": "If synthetic, set type='synthetic' and explain generation."
    }
  ],
  "canonicalRefs": {
    "stacItem": "../../../../../data/stac/items/EXAMPLE.item.json",
    "stacCollection": "../../../../../data/stac/collections/EXAMPLE.collection.json",
    "dcatDataset": "../../../../../data/catalog/dcat/EXAMPLE.dataset.jsonld",
    "provBundle": "../../../../../data/prov/EXAMPLE.prov.jsonld"
  },
  "spatial": {
    "crs": "EPSG:4326",
    "bbox": [-102.05, 36.99, -94.59, 40.00],
    "geometryType": "Polygon"
  },
  "temporal": {
    "start": null,
    "end": null
  },
  "schemaHints": {
    "primaryKey": "GEOID",
    "displayName": "NAME",
    "properties": ["GEOID", "NAME"]
  },
  "redaction": {
    "status": "none",
    "notes": "Confirm no sensitive attributes exist."
  }
}
```

</details>

---

## 🧪 Using sample data in the UI

### Option A — Fetch as a static asset 🌐
```js
const url = "/assets/samples/_shared/data/geojson/kansas-counties.sample.geojson";
const geojson = await fetch(url).then(r => r.json());
```

### Option B — Use as a fixture in tests 🧫
- Keep fixtures **small**
- Keep fixtures **stable**
- Prefer loading from disk rather than copy/pasting into test files

---

## 🧷 Performance + size budgets

Suggested budgets (keep samples snappy ⚡):

| Type | Target | Hard stop |
|------|--------|-----------|
| GeoJSON | < 250 KB | 1 MB |
| CSV | < 200 KB | 1 MB |
| Images | < 100 KB | 300 KB |
| STAC JSON | < 50 KB | 200 KB |

> [!TIP]
> If you need more than the hard stop, the data probably belongs upstream and should be streamed/served via the API.

---

## ✅ Checklist before adding new sample data

- [ ] 📄 Data file added under the right subfolder
- [ ] 🧾 Matching `*.contract.json` created
- [ ] 🪪 License + attribution included (or clearly “synthetic”)
- [ ] 🧭 `canonicalRefs` added when derived from canonical sources
- [ ] 🧼 Linted/validated (JSON valid, CSV consistent)
- [ ] 🔐 No sensitive content; respects governance/redaction expectations
- [ ] 🧪 Used by at least one sample/demo/test (avoid dead fixtures)

---

## 🔗 Related docs (repo-relative)

> Paths below assume repo root is `../../../../../` from this README.

- 📘 Master guide: `../../../../../docs/MASTER_GUIDE_v13.md`
- 🧾 Schemas: `../../../../../schemas/`
- 🛰️ STAC outputs: `../../../../../data/stac/`
- 🧠 DCAT catalog: `../../../../../data/catalog/dcat/`
- 🧬 PROV lineage: `../../../../../data/prov/`
- 🎬 Story Nodes (governed): `../../../../../docs/reports/story_nodes/`

---

## 🧩 FAQ

**“Isn’t the UI supposed to have no hidden data files?”**  
Correct ✅ — production UI should rely on the API. This folder exists *only* for **explicit sample tooling** and is isolated under `samples/` so it never becomes a stealth data path.

**“Where do big rasters / COGs / tiles go?”**  
Upstream in the pipeline (processed assets + catalogs). The UI should reference them via API/catalog, not by dropping them into web assets.

**“Can I include synthetic data?”**  
Yes — but label it **synthetic** in the contract, explain how it was generated, and keep it obviously non-authoritative.
