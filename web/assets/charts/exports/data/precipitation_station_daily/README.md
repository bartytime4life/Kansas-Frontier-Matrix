# 🌧️ Precipitation (Daily) — Station Time Series

![KFM](https://img.shields.io/badge/KFM-Front--End%20Chart%20Export-2ea44f)
![Cadence](https://img.shields.io/badge/Cadence-Daily-blue)
![Scope](https://img.shields.io/badge/Type-Station%20Observations-informational)
![Artifact](https://img.shields.io/badge/Artifact-Derived%20%2F%20Regeneratable-orange)

This folder contains **daily precipitation totals by station**, exported as **static web assets** for charts (e.g., station popups + timeline views) in the KFM UI. 📈🗺️

> ⚠️ **Important:** This is a **derived UI export**, not the “source of truth.”  
> Treat it like build output: don’t hand-edit unless you’re debugging a one-off.

---

## ✨ What this is used for

- 🧭 **Map popups / side panels**: click a station → show a precipitation time series chart.
- 🧱 **Fast UI loading**: pre-shaped files avoid heavy client-side transforms.
- 🧮 **Downstream aggregation**: daily data can be aggregated to weekly/monthly for default views.

---

## 📁 Folder location

`web/assets/charts/exports/data/precipitation_station_daily/`

---

## 🧾 Contents (expected layout)

> Your repo may evolve—this is the **recommended** layout for maintainability and UI performance.

```text
web/
└─ assets/
   └─ charts/
      └─ exports/
         └─ data/
            └─ precipitation_station_daily/
               ├─ README.md
               ├─ meta.json                 # dataset-level contract + generation info
               ├─ stations.json             # station lookup table (id → name/lat/lon/etc.)
               ├─ series/
               │  ├─ <station_id>.json      # one file per station (best for lazy-loading)
               │  └─ ...
               └─ checksums.json            # optional: integrity checks (sha256 per file)
```

---

## 🧩 Data contract

### Dataset semantics

- **Observation type:** daily precipitation total per station (rain gauge / station record)
- **Temporal grain:** 1 day
- **Spatial grain:** point station
- **Primary join key:** `station_id`
- **Recommended “time” field:** `date` as `YYYY-MM-DD` (ISO-8601, date-only)

### Units & conventions ✅

- Prefer **millimeters** (`mm`) for storage (UI can convert to inches).
- Missing / unavailable values should be represented as **`null`** (not `0`).
- If a station’s “day boundary” is local-time dependent, store `tz` or `day_boundary` in `meta.json`.

---

## 🗃️ File specs

### `meta.json` (dataset-level)

Minimal recommended shape:

```json
{
  "dataset_id": "precipitation_station_daily",
  "title": "Daily Precipitation by Station",
  "units": "mm",
  "time_zone": "UTC",
  "date_range": { "start": "YYYY-MM-DD", "end": "YYYY-MM-DD" },
  "generated_at": "YYYY-MM-DDTHH:MM:SSZ",
  "source": {
    "provider": "SEE_CATALOG",
    "license": "SEE_CATALOG",
    "attribution": "SEE_CATALOG"
  },
  "pipeline": {
    "name": "SEE_PIPELINE",
    "version": "x.y.z",
    "run_id": "YYYYMMDD_HHMMSS",
    "inputs_checksum": "OPTIONAL"
  },
  "notes": [
    "Daily series may be visually dense; UI should default to aggregated view (weekly/monthly)."
  ]
}
```

### `stations.json` (lookup table)

Recommended minimal fields:

```json
[
  {
    "station_id": "STATION_001",
    "name": "Example Station",
    "lat": 38.97,
    "lon": -95.23,
    "elevation_m": 270,
    "network": "OPTIONAL",
    "active": true
  }
]
```

### `series/<station_id>.json` (per-station daily series)

Recommended shape optimized for chart libraries:

```json
{
  "station_id": "STATION_001",
  "units": "mm",
  "values": [
    ["2024-01-01", 0.0],
    ["2024-01-02", 12.7],
    ["2024-01-03", null]
  ],
  "qc": {
    "flags": "OPTIONAL",
    "notes": "OPTIONAL"
  }
}
```

---

## ⚡ UI consumption (example)

### TypeScript (lazy-load per station)

```ts
type DailyPoint = [date: string, precipMm: number | null];

export async function loadStationPrecipDaily(stationId: string) {
  const url = `/assets/charts/exports/data/precipitation_station_daily/series/${stationId}.json`;
  const res = await fetch(url);
  if (!res.ok) throw new Error(`Failed to fetch ${url}: ${res.status}`);
  const payload = await res.json() as { station_id: string; units: string; values: DailyPoint[] };
  return payload;
}
```

### UX tip 🎛️

If the date range is long, default the chart to:
- **monthly totals** (or rolling 30-day) for overview
- allow a toggle to **daily** when zoomed in (or when date range ≤ ~180 days)

---

## 📉 Performance notes (don’t skip)

Daily station data can get heavy fast. Recommended patterns:

- ✅ **One file per station** (lazy-load)
- ✅ Keep `values` as tuples (compact)
- ✅ Avoid repeating station metadata inside each series file
- ✅ Consider a `gzip`-friendly JSON shape (arrays > objects)
- ✅ Add `checksums.json` for quick validation & cache-busting

---

## 🧬 Provenance & governance

KFM’s data philosophy is **metadata-first + provenance-first**. 🧾🔗

This folder is a **UI-facing derivative**; the authoritative records should exist in the canonical catalog & provenance locations (STAC/DCAT + PROV), and the “real” processed dataset should live under the curated data area (e.g., `data/processed/...`).

**Rule of thumb:**  
🗂️ `data/processed/…` = truth  
🧾 `data/catalog/…` + `data/prov/…` = governance  
🌐 `web/assets/…` = fast UI delivery

---

## 🔁 Regenerating this export

**Recommended workflow:**

1. Update/verify the dataset metadata contract in the catalog (STAC/DCAT).
2. Run the ingestion/transform pipeline that produces the standardized daily station table.
3. Run the **export step** that:
   - produces `stations.json`
   - splits station series into `series/<station_id>.json`
   - writes `meta.json` (+ optional `checksums.json`)
4. Run quick validation:
   - JSON parse check
   - schema check (if available)
   - spot-check a few stations in the UI

> 🧪 If you’re adding a new station network or changing units, bump the export “version” and keep backwards compatibility where possible.

---

## 🧯 Common pitfalls

- ❌ Treating `0` as missing (it’s a valid “no rain” day)
- ❌ Mixing inches and mm without encoding units
- ❌ Local time day-boundaries without documenting timezone rules
- ❌ Shipping a single massive file that the UI must fully download

---

## 🧷 Maintainers

- **Owner:** Data Engineering / Pipeline owners (see repository governance)
- **Consumers:** `web/` chart & station popup components

---

## ✅ Checklist (for PRs touching this folder)

- [ ] `meta.json` updated (date range, generated_at, pipeline version)
- [ ] `stations.json` unchanged OR intentionally updated with clear reason
- [ ] Sample station charts render correctly in the UI
- [ ] No “mystery units” (mm vs inches)
- [ ] Large diffs explained (new stations? extended date range? backfill?)

---