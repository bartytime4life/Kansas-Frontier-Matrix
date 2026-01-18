# 📊 KFM Chart Meta Schema (UI Contract)

![Contract-First](https://img.shields.io/badge/contract--first-JSON%20Schema-0b7285)
![Provenance-First](https://img.shields.io/badge/provenance--first-required-2f9e44)
![Scope](https://img.shields.io/badge/scope-UI%20Charts%20%26%20Media-364fc7)
![Status](https://img.shields.io/badge/status-governed%20schema-f59f00)

This folder defines the **JSON Schema contracts** for chart metadata consumed by the web UI (including Focus Mode). In KFM, anything shown in the UI must be **traceable to cataloged sources** and backed by **machine-validated metadata** (“data contracts”).  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧭 What this is for

Charts in `web/assets/media/charts/` are treated as **evidence artifacts** (not decoration). That means:

- ✅ every chart must have a **metadata JSON** (“chart contract”) and pass validation before appearing in UI  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- ✅ every chart must link back to **cataloged sources** (STAC/DCAT) and/or a PROV lineage record  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- ❌ no “mystery charts” (unsourced or ad-hoc) are allowed  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- ✅ Focus Mode displays only provenance-linked content (charts included)  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  

This mirrors the repo-wide invariant: **ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode** (no skipping stages).  [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗂️ Expected folder layout

```text
web/assets/media/charts/
  ├─ meta/
  │   ├─ <chart_id>.chart.json              # chart metadata (instance)
  │   └─ ...
  ├─ rendered/
  │   ├─ <chart_id>.svg|png                 # optional pre-rendered artifacts
  │   └─ ...
  └─ meta/schema/
      ├─ README.md                          # (this file)
      ├─ chart-meta.schema.json             # main schema (recommended)
      ├─ chart-series.schema.json           # shared defs (recommended)
      └─ chart-provenance.schema.json       # shared defs (recommended)
```

> If your repo uses different filenames, keep the *contract intent* identical: **versioned JSON Schema + validated instances**.

---

## ✅ Chart metadata: required fields (v1)

A chart metadata JSON should be **portable** (can be rendered again) and **auditable** (can be traced back).

### Minimal required keys

| Field | Type | Why it exists |
|---|---:|---|
| `schema_version` | string | contract versioning (breaking changes require bump) |
| `id` | string | stable chart ID (use consistent naming) |
| `title` | string | display title |
| `summary` | string | one-paragraph description |
| `chart_type` | string | e.g. `line`, `bar`, `scatter`, `map-linked-timeseries` |
| `outputs` | object | where rendered artifacts live (SVG/PNG) + accessibility text |
| `data_sources` | array | pointers to cataloged assets/datasets (STAC/DCAT IDs) |
| `provenance` | object | PROV linkage / lineage summary |
| `license` | object | usage rights + attribution string |

### Strongly recommended keys

- `encodings` (axes + series mappings)
- `transforms` (aggregation, filters, units, time grain)
- `quality` (known limitations, uncertainty notes, sampling caveats)
- `ui` (display defaults: colors handled by UI theme, but layout hints ok)
- `links` (deep links to catalog items, graph nodes, Story Nodes)

---

## 🧬 Provenance rules (non-negotiable)

KFM’s trust model depends on **contract-first** and **provenance-first** publishing.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

For charts, that means:

1. **At least one catalog pointer**  
   - `stac_item_ids` (for assets) and/or  
   - `dcat_dataset_ids` (for datasets/distributions)

2. **A lineage hook**  
   - `prov_record_id` (preferred) or  
   - an embedded PROV-style summary (Entity/Activity/Agent) aligned with PROV concepts  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  

3. **No chart without a source**  
   Focus Mode hard-gates provenance-linked content.  [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧾 Example chart metadata (instance)

Create: `web/assets/media/charts/meta/kfm.ks.drought.spi_30d.v1.chart.json`

```json
{
  "schema_version": "1.0.0",
  "id": "kfm.ks.drought.spi_30d.v1",
  "title": "Standardized Precipitation Index (30-day) — Kansas",
  "summary": "SPI (30-day) aggregated statewide with monthly rollups.",
  "chart_type": "line",
  "outputs": {
    "preferred": "web/assets/media/charts/rendered/kfm.ks.drought.spi_30d.v1.svg",
    "alt_text": "Line chart showing 30-day SPI over time for Kansas; values below -1 indicate drought conditions."
  },
  "encodings": {
    "x": { "field": "date", "type": "temporal", "format": "YYYY-MM" },
    "y": { "field": "spi_30d", "type": "quantitative", "unit": "index" },
    "series": [
      { "field": "region", "label": "Kansas (statewide)" }
    ]
  },
  "transforms": [
    { "op": "filter", "expr": "region == 'ks'" },
    { "op": "aggregate", "groupby": ["date"], "fields": [{ "field": "spi_30d", "as": "spi_30d", "reduce": "mean" }] }
  ],
  "data_sources": [
    {
      "kind": "dcat_dataset",
      "id": "kfm.ks.climate.spi",
      "version": "v1",
      "license": "CC-BY-4.0"
    }
  ],
  "provenance": {
    "prov_record_id": "prov:kfm.ks.climate.spi.pipeline_run.2026-01-01T00:00:00Z",
    "processing_summary": [
      "ETL → validated dataset contract → derived monthly aggregation → chart render artifact"
    ]
  },
  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Data © Source Provider(s) as referenced in catalog; chart compilation by KFM.",
    "notes": "Chart may be redistributed with attribution; see dataset license for upstream constraints."
  },
  "quality": {
    "known_limits": [
      "Aggregation may mask regional variation.",
      "SPI depends on baseline period choice; see dataset docs."
    ],
    "uncertainty": "See dataset metadata for methodology and uncertainty notes."
  },
  "ui": {
    "default_view": { "show_legend": true, "y_zero_line": false },
    "focus_mode": { "map_linked": false }
  }
}
```

---

## 🧪 Validation (local + CI)

Because KFM treats contracts as first-class artifacts, validation should run:

- locally (pre-commit / pre-push), and
- in CI (hard gate)

This is consistent with the “contract-first approach… enforced via validators” principle.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Option A — Ajv (Node)

```bash
npx ajv-cli validate \
  -s web/assets/media/charts/meta/schema/chart-meta.schema.json \
  -d "web/assets/media/charts/meta/*.chart.json"
```

### Option B — python-jsonschema

```bash
python -m pip install jsonschema
python -c "import glob, json; from jsonschema import validate; \
  schema=json.load(open('web/assets/media/charts/meta/schema/chart-meta.schema.json')); \
  [validate(instance=json.load(open(p)), schema=schema) for p in glob.glob('web/assets/media/charts/meta/*.chart.json')]; \
  print('ok')"
```

---

## 🔁 Versioning rules

- **Non-breaking** additions (new optional fields): bump patch/minor as your policy defines.
- **Breaking** changes (rename/remove/semantic change): bump **major** and keep prior schema for existing assets.
- UI should prefer the newest schema it supports; older charts remain readable.

---

## 🧠 Design principles (why it’s strict)

KFM is built around:
- **Provenance-first** publishing and “no unsourced content” (especially in Focus Mode)  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- **Contract-first** interfaces so components can rely on self-described schemas and lineage  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- **Hard gates** preventing unsourced materials from entering official UI pathways  [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  

If you’re adding a new chart type, add it by:
1) extending the schema (versioned),
2) adding an example instance JSON,
3) ensuring CI validation passes, and
4) wiring UI rendering *without bypassing the catalogs/provenance chain*.  [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧩 Quick checklist ✅

- [ ] Chart file exists (`rendered/*.svg|png`) **or** renderer can generate it from `data_sources`
- [ ] `meta/<chart_id>.chart.json` exists
- [ ] Metadata validates against JSON Schema
- [ ] `data_sources[]` points to catalog IDs (STAC/DCAT)
- [ ] `provenance` includes `prov_record_id` or equivalent lineage summary
- [ ] `license.attribution` is present (auto-attribution is supported by contract-first metadata)  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---
