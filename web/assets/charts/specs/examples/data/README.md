# 📊 Chart Example Data
`web/assets/charts/specs/examples/data/README.md`

![Contract-First](https://img.shields.io/badge/contract--first-required-brightgreen)
![Provenance-First](https://img.shields.io/badge/provenance--first-no%20mystery%20layers-blue)
![Web Asset](https://img.shields.io/badge/scope-web%20asset%20bundle-informational)
![Formats](https://img.shields.io/badge/formats-CSV%20%7C%20JSON%20%7C%20GeoJSON-9cf)

> 🎯 **Purpose:** This folder holds **small, deterministic example datasets** used by the **chart spec examples** in the web UI (and any related docs/tests).  
> In KFM, **anything visible in the UI should be traceable**—even “toy” examples should be labeled clearly as **synthetic** or **source-derived**.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧭 Where this fits in the KFM repo

The **front-end app** lives under `web/` and includes reusable UI components (including **charts**) plus static `assets/`.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
This directory specifically supports chart **spec examples** by providing local data files that can be loaded without hitting APIs.

---

## 📁 Folder layout

```text
🌐 web/
  📦 assets/
    📊 charts/
      🧾 specs/
        🧪 examples/
          📁 data/                  👈 you are here
            📄 README.md
            📄 <dataset>.<ext>
            📄 <dataset>.meta.json  (required)
            📄 <dataset>.prov.json  (optional, recommended)
```

---

## ✅ What belongs here

**Good fits** ✅  
- Tiny (KB–low MB) datasets for:
  - chart demos / storyboarding
  - unit/integration test fixtures
  - documentation screenshots
  - UI development “known-good” samples

**Not a good fit** ❌  
- Large historical datasets, raw rasters, or heavyweight exports  
- Anything sensitive, licensed for restricted use, or containing personal data  
- Anything you can’t describe/prove where it came from (no “mystery layers”)  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

> 💡 **Rule of thumb:** if it’s big or needs a pipeline, it belongs in the governed data catalogs (STAC/DCAT/PROV), not in web assets. 

---

## 🧱 Non‑negotiables: Contract‑First + Provenance‑First

KFM’s architecture is explicit: **anything that shows up in UI/Focus Mode must be traceable**; every dataset should have a **metadata JSON (“data contract”)** and “mystery layers” are not permitted.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Required per dataset
For every data file you add, also add:

- `my_dataset.csv` (or `.json` / `.geojson`)
- `my_dataset.meta.json` ✅ **required**

### Strongly recommended
- `my_dataset.prov.json` ✅ (lineage/provenance in a machine-friendly way)

This matches KFM’s “data → catalogs → graph → API → UI → narrative” contract boundary mindset (even in miniature).  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧾 File naming conventions

Keep names **boring, stable, and grep-able**:

**Recommended pattern**
- `topic__chart__grain__vNN.ext`

Examples:
- `population__timeseries__statewide__v01.csv`
- `drought__severity__county__v02.json`
- `railroads__length__by_year__v01.csv`

**Why?**  
Chart specs should be able to reference a dataset reliably even as examples evolve.

---

## 📦 Supported file formats

KFM emphasizes open, interoperable formats (e.g., CSV/GeoJSON/GeoTIFF in the broader system).  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
For this folder, keep it simple:

| Format | Use when | Notes |
|---|---|---|
| `.csv` | Most charts | Small + readable + diff-friendly |
| `.json` | Nested/structured demo data | Prefer array-of-objects for charts |
| `.geojson` | Map-linked chart demos | Keep geometry count low |
| `.tsv` | Only if needed | Prefer `.csv` unless the data requires it |

---

## 🧩 `*.meta.json` (Data Contract) — required

Every dataset must have a **data contract**: a metadata JSON describing source, license, extents, and processing steps. This is a core KFM design feature.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Minimal template

```json
{
  "dataset_id": "urn:kfm:dataset:examples:population__timeseries__statewide__v01",
  "title": "Population (Statewide) — Example Timeseries",
  "description": "Small example dataset used by chart spec examples. If derived from real data, include source + processing steps.",
  "classification": "public",
  "care_label": "Public",
  "license": "TBD-or-CC-BY-4.0-or-public-domain",
  "is_synthetic": true,

  "source": {
    "kind": "synthetic",
    "citation": "Synthetic example generated for UI development.",
    "url": null
  },

  "temporal_extent": {
    "start": "1900-01-01",
    "end": "2020-12-31",
    "resolution": "year"
  },

  "spatial_extent": {
    "name": "Kansas (statewide)",
    "bbox_wgs84": [-102.051744, 36.993016, -94.588413, 40.003166]
  },

  "fields": [
    { "name": "year", "type": "integer", "unit": "year" },
    { "name": "population", "type": "integer", "unit": "people" }
  ],

  "processing_steps": [
    "Generated synthetic values for demonstration; not intended for analysis."
  ],

  "checks": {
    "row_count": 121,
    "sha256": "PUT_REAL_HASH_HERE"
  },

  "owners": ["kfm-web"],
  "tags": ["examples", "charts", "timeseries"]
}
```

> 🧠 Even “synthetic” examples should say they’re synthetic. Focus Mode is evidence-backed and should not be forced to guess. 

---

## 🔎 `*.prov.json` (Provenance) — optional but recommended

KFM uses open standards (e.g., STAC/DCAT/PROV-O) to capture provenance and processing lineage.   
For examples, we can keep a lightweight lineage record:

```json
{
  "entity": "urn:kfm:dataset:examples:population__timeseries__statewide__v01",
  "wasDerivedFrom": [],
  "activity": {
    "name": "generate_example_dataset",
    "type": "synthetic_generation",
    "when_utc": "2026-01-16T00:00:00Z",
    "code_ref": "repo://web/assets/charts/specs/examples/scripts/generate_population_example.ts",
    "notes": "Deterministic seed = 42"
  }
}
```

---

## 🧷 UI expectation: “the map behind the map” (and chart behind the chart)

KFM’s UI philosophy is to keep context and provenance visible—charts may include citations in captions so users know what’s being shown. 

**Therefore:**  
- If a chart demo is based on real data, ensure `*.meta.json` has a usable `source.citation` and license  
- If it’s synthetic, mark it as synthetic and explain the generator

---

## 🧪 Adding a new example dataset (checklist)

1. 🧾 Add the data file: `my_dataset.csv` / `.json` / `.geojson`
2. 🧩 Add the contract: `my_dataset.meta.json` (**required**)  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
3. 🔎 Add provenance: `my_dataset.prov.json` (recommended)  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
4. 🔗 Update the associated chart spec to reference it (relative path)
5. 🧹 Keep it small + deterministic (stable ordering, stable rounding)
6. 🏷️ Ensure it is safe to ship publicly (this is a web asset!)

---

## 🧯 Safety & licensing notes

Because these files are bundled into the web app:
- ✅ Assume **public distribution**
- ❌ Do not include secrets, personal info, or restricted datasets
- ✅ Include license + attribution in `*.meta.json` (required in KFM’s contract-first approach)  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🔗 Related project docs (conceptual)

- **KFM pipeline ordering & contract/evidence boundaries** (data → catalogs → graph → API → UI → narrative)  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- **KFM technical architecture & provenance-first UI**   
- **System design / data catalogs & traceability**  [oai_citation:11‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

### ✨ Tiny mantra
> **No mystery layers. Even in examples.**  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
