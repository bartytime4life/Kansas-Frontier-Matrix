# 📊🌾 KFM Chart Domain Catalog (`web/assets/charts/specs/catalog/domains/`)

![KFM](https://img.shields.io/badge/KFM-Chart%20Catalog-0b7285?style=for-the-badge)
![Contract-First](https://img.shields.io/badge/Contract--First-✅-2f9e44?style=for-the-badge)
![Provenance-First](https://img.shields.io/badge/Provenance--First-🔎-1c7ed6?style=for-the-badge)

> [!IMPORTANT]
> This folder is **UI-facing configuration** (a.k.a. a **contract artifact**) that powers the chart browsing experience in the `web/` app.
> It must remain **deterministic, reviewable, and provenance-linked** — i.e., no “magic charts” with unclear origins.

---

## 🧭 What lives here?

This directory defines **Chart Domains** — curated, human-friendly groupings for chart specifications.

Think of domains as:
- 🗂️ **Navigation** (how users browse charts)
- 🧠 **Meaning** (the “topic area” a chart belongs to)
- 🔗 **Traceability glue** (how charts point back to authoritative datasets + provenance)

In KFM terms, these are **UI contracts** that should align with the canonical pipeline:

```mermaid
flowchart LR
  A[📦 data/ (raw → work → processed)] --> B[🗃️ Catalogs (STAC/DCAT/PROV)]
  B --> C[🧠 Graph (ontology + links)]
  C --> D[🔌 API boundary]
  D --> E[🌐 web/ UI]
  E --> F[📊 Chart Domains + Chart Specs (this folder)]
  E --> G[📖 Story Nodes / Focus Mode]
```

---

## ✅ What does NOT belong here?

- ❌ Raw datasets (those belong in `data/<domain>/...`)
- ❌ Heavy analysis outputs (those belong in `mcp/` + registered as evidence artifacts)
- ❌ Unsourced narrative claims (those belong in Story Nodes **with evidence links**)
- ❌ Any chart that cannot be traced back to a dataset + processing lineage

> [!NOTE]
> Charts should support the “**map behind the map**” idea: users must be able to inspect sources/metadata/citations directly from the UI.

---

## 🗂️ Expected folder layout

This README documents the **intended** contract layout (even if your repo is still scaffolding it).

```text
📁 web/
  📁 assets/
    📁 charts/
      📁 specs/
        📁 catalog/
          📁 domains/
            ├── 📄 README.md                 # you are here ✅
            ├── 📄 index.json                # list of all domains (manifest)
            ├── 📁 water-climate/
            │   ├── 📄 domain.json           # domain metadata (contract)
            │   └── 📁 charts/
            │       ├── 📄 index.json        # charts in this domain (manifest)
            │       ├── 📄 annual-precip.chart.json
            │       └── 📄 drought-index.chart.json
            ├── 📁 hazards/
            │   └── ...
            └── 📁 air-quality/
                └── ...
```

### Why manifests (`index.json`)?

Static sites can’t “list directories” at runtime.
A manifest provides:
- ✅ deterministic ordering
- ✅ fast loading
- ✅ explicit review diffs
- ✅ easy schema validation in CI

---

## 🧩 Key concepts (glossary-lite)

| Term | Meaning |
|---|---|
| **Domain** | A thematic bucket (e.g., “Water & Climate”, “Hazards”) used for chart discovery. |
| **Chart Spec** | A machine-readable description of a chart (inputs, transformations, encodings, caption/citations). |
| **Contract artifact** | A versioned spec/schema/config that implementations must honor (no silent breakage). |
| **Evidence artifact** | A derived output treated as data+metadata, registered in catalogs with lineage. |
| **Provenance-first** | “Show your work”: sources + processing steps are first-class. |

---

## 🧱 Domain contract (`domain.json`)

A domain should be **small and stable**: it’s a label + metadata + provenance pointers, not a dumping ground.

### Suggested fields

| Field | Type | Required | Notes |
|---|---:|:---:|---|
| `id` | string | ✅ | Stable ID (suggest: `kfm.domain.<slug>`) |
| `slug` | string | ✅ | Kebab-case, URL-safe |
| `title` | string | ✅ | Human name |
| `summary` | string | ✅ | One sentence |
| `description` | string | ✅ | Longer explanation (still factual / non-speculative) |
| `icon` | string | ✅ | Emoji or icon key |
| `order` | number | ✅ | Sort order in UI |
| `tags` | string[] | ◻️ | Search/filter helpers |
| `dataset_refs` | object[] | ⭐ | Links to authoritative dataset IDs (DCAT/STAC) + PROV lineage |
| `governance` | object | ⭐ | Sensitivity + review hooks (FAIR/CARE aligned) |
| `links` | object[] | ◻️ | Internal docs or Story Nodes relevant to the domain |

### Example `domain.json`

```json
{
  "id": "kfm.domain.water-climate",
  "slug": "water-climate",
  "title": "💧 Water & Climate",
  "summary": "Hydrology + climate indicators across time (observations and derived indices).",
  "description": "Charts and indicators related to precipitation, drought, streamflow, groundwater, and climate normals/projections.",
  "icon": "💧",
  "order": 20,
  "tags": ["hydrology", "climate", "drought", "precipitation"],
  "dataset_refs": [
    {
      "role": "primary",
      "dcat_dataset_id": "dcat:kfm:datasets:noaa-storm-events",
      "stac_collection_id": "stac:kfm:collections:noaa-storm-events",
      "prov_bundle_id": "prov:kfm:runs:hazards-pipeline:2025-01-15"
    }
  ],
  "governance": {
    "sensitivity": "low",
    "care_label": "public",
    "review_required": false
  }
}
```

> [!TIP]
> `dataset_refs` should point to **real catalog entries** (DCAT/STAC) and a **real lineage artifact** (PROV), not just external URLs.

---

## 📈 Chart spec contract (inside each domain)

Chart specs are **implementation-agnostic** descriptions of:
- what data to use
- how to shape it
- how to render it
- how to cite it

A chart spec should include (minimum):
- `id`, `title`, `domain`
- `dataset_refs` (DCAT/STAC/PROV IDs)
- `query` or `data_view` (how the UI/API obtains the data)
- `encoding` (x/y/series, units, aggregation)
- `caption` (human-readable + citations)

### Example chart spec (`*.chart.json`)

```json
{
  "id": "kfm.chart.water-climate.annual-precip",
  "title": "Annual Precipitation (Statewide)",
  "domain": "water-climate",
  "description": "Annual precipitation totals aggregated statewide (by year).",
  "dataset_refs": [
    {
      "role": "primary",
      "dcat_dataset_id": "dcat:kfm:datasets:prism-precip",
      "stac_collection_id": "stac:kfm:collections:prism-precip",
      "prov_bundle_id": "prov:kfm:runs:climate-pipeline:2025-01-12"
    }
  ],
  "data_view": {
    "endpoint": "/api/charts/annual-precip",
    "params": { "aggregation": "statewide", "interval": "year" }
  },
  "encoding": {
    "x": { "field": "year", "type": "temporal" },
    "y": { "field": "precip_mm", "type": "quantitative", "unit": "mm" }
  },
  "caption": {
    "text": "Statewide annual precipitation derived from PRISM gridded products. See dataset and processing lineage for details.",
    "citations": [
      { "label": "PRISM", "ref": "dcat:kfm:datasets:prism-precip" },
      { "label": "Lineage", "ref": "prov:kfm:runs:climate-pipeline:2025-01-12" }
    ]
  }
}
```

---

## 🧪 Validation rules (what CI SHOULD enforce)

### Domain-level checks
- ✅ `slug` unique across catalog
- ✅ `order` is an integer and no duplicates (or duplicates handled intentionally)
- ✅ `domain.json` matches schema
- ✅ `dataset_refs` point to known catalog IDs (DCAT/STAC)
- ✅ governance fields present if sensitivity ≠ low

### Chart-level checks
- ✅ `id` unique globally
- ✅ `domain` matches its folder + a known domain slug
- ✅ chart schema validation passes
- ✅ `dataset_refs` are resolvable
- ✅ caption exists and has at least one citation reference

> [!WARNING]
> If the chart is shown in Focus Mode or attached to a Story Node, it must be **strictly evidence-backed** and **citation-complete**.

---

## ➕ Adding a new domain (checklist)

1. 📁 Create a new folder: `domains/<domain-slug>/`
2. 🧾 Add `domain.json` (with governance + dataset references)
3. 📄 Update `domains/index.json` (add the new domain entry)
4. 📊 Create `domains/<domain-slug>/charts/`
5. 🧷 Add at least one `*.chart.json` + `charts/index.json`
6. 🔗 Ensure referenced datasets exist in catalogs (DCAT/STAC/PROV)
7. ✅ Run validators / tests (local + CI)
8. 👀 If sensitive: trigger governance review (CARE label + approvers)

---

## 🧭 Suggested starter domain taxonomy (KFM-flavored)

These are common “first domains” that map well to the KFM mission:

- 💧 `water-climate` — precipitation, drought indices, streamflow, climate normals/projections  
- 🌪️ `hazards` — tornado tracks, hail, wildfire perimeters, storm events  
- 🌫️ `air-quality` — ozone/PM monitors, smoke episodes  
- 🌾 `agriculture` — soils, crop trends, irrigation signals, land capability  
- 🗺️ `historical` — maps, treaties/land changes, settlements, boundary evolution  
- 🏙️ `demographics` — census time series, population density, migration  
- ⚡ `energy` — oil/gas, renewables, infrastructure footprints  
- 🌿 `ecology` — land cover, habitat indicators, biodiversity proxies

> [!NOTE]
> Domain names should remain **coarse**. If you’re about to create `water-climate-drought-2011-2012`, you probably want a **chart tag**, not a new domain.

---

## 🧠 Design principle: “Explain the chart like a scientist, show it like a designer” 🎛️✨

A good chart spec:
- is honest about uncertainty and limitations
- makes units explicit
- includes citations
- is consistent with KFM governance
- is reusable across UI contexts (dashboard, Focus Mode, Story Nodes)

---

## 🔍 Troubleshooting

### “My chart renders, but provenance panel is empty”
- Check that `caption.citations[].ref` points to a real DCAT/STAC/PROV ID.
- Ensure the UI knows how to resolve those IDs (via API or embedded catalog subset).

### “CI fails: domain not found”
- Confirm the chart spec’s `domain` matches the folder slug and the `domains/index.json` entry.

### “We need a brand-new domain”
- Confirm the datasets exist and are cataloged first (STAC/DCAT/PROV), then add UI contracts.

---

## 📚 Related docs (repo-relative)

- `docs/MASTER_GUIDE_v13.md` — canonical pipeline + contracts  
- `docs/glossary.md` — shared vocabulary  
- `schemas/ui/` — JSON Schemas for UI contracts (domain + chart specs)  
- `docs/governance/` — FAIR/CARE, sovereignty, review gates  
- `mcp/` — experiments + model cards for derived evidence artifacts  

---

<sub>✨ If you keep domains boring and specs strict, the UI can be beautiful and trustworthy.</sub>
