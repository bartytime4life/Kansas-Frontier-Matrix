# 📊 Derived NDVI Stats — Landsat 8 (Experiment: `2026-01-02__ndvi__landsat8`)

> **Folder:** `data/work/experiments/2026-01-02__ndvi__landsat8/data/derived/stats/`  
> **Stage:** `data/work` (intermediate workspace; not a published artifact):contentReference[oaicite:0]{index=0}

This directory stores tabular/statistical summaries computed from the experiment’s NDVI rasters (e.g., per-field zonal stats, scene-level summaries, QC counts). NDVI is a normalized difference index defined as `(NIR - red) / (NIR + red)` with outputs in **[-1, 1]**; healthy green vegetation tends to be ~0.8–0.9, and water tends to be near −1:contentReference[oaicite:1]{index=1}.

---

## 🧭 Context

| Item | Value |
| --- | --- |
| Sensor | Landsat 8 (OLI) |
| Nominal spatial resolution | 30 m:contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3} |
| Nominal revisit | 16 days:contentReference[oaicite:4]{index=4} |
| Source collection (typical) | `LANDSAT/LC08/C02/T1_L2` (Collection 2, Level‑2 SR):contentReference[oaicite:5]{index=5} |

---

## 📦 What lives here

<details>
<summary>📁 Typical contents (may vary by run)</summary>

```text
stats/
  README.md
  ndvi_stats__by_feature.(parquet|csv)
  ndvi_stats__by_scene.(parquet|csv|json)
  ndvi_histograms.(json|parquet)
  qc__pixel_counts.(json|csv)
  schema__ndvi_stats.json
  run_metadata.json
```

</details>

> If you promote any artifact to `data/processed/...`, include boundary artifacts (STAC/DCAT/PROV) and treat the output as a first-class dataset (API-gated, reproducible):contentReference[oaicite:6]{index=6}:contentReference[oaicite:7]{index=7}.

---

## 🧮 How these stats are produced (high level)

### 1) NDVI computation 🧮🌿

- NDVI formula: `NDVI = (NIR - red) / (NIR + red)`:contentReference[oaicite:8]{index=8}.
- Example for Landsat 8 Collection 2 Level‑2 SR in Earth Engine:

  ```js
  var ndvi = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
    // ...
    .median()
    .normalizedDifference(['SR_B5', 'SR_B4'])
    .rename('NDVI');
  ```

  :contentReference[oaicite:9]{index=9}

- NDVI workflows must handle noise from clouds/atmospheric contamination and other data issues:contentReference[oaicite:10]{index=10}:contentReference[oaicite:11]{index=11}.

### 2) Cloud / quality masking ☁️✅

The Landsat 8 Level‑2 product includes a `QA_PIXEL` band used for masking clouds and other unwanted pixels:contentReference[oaicite:12]{index=12}.

In the example workflow, `QA_PIXEL` is decoded as a bitmask with:

- bit 0 fill
- bit 1 dilated cloud
- bit 2 cirrus (L8)
- bit 3 cloud
- bit 4 cloud shadow
- bit 5 snow
- bit 6 clear (**1 = clear**)
- bit 7 water:contentReference[oaicite:13]{index=13}

> **Rule of thumb for this folder:** compute stats on the *masked* NDVI (clear/valid pixels), and include pixel-count diagnostics so coverage can be audited and modeled.

### 3) Zonal statistics (per feature / region) 🗺️📊

For vector geometries (plots, fields, counties, etc.), zonal stats are typically produced by running `reduceRegions` for each image (or mapping a helper like `zonalStats` over an ImageCollection):contentReference[oaicite:14]{index=14}.

A common output pattern is one row per feature per time, with identifiers + timestamps (example columns include `plot_id`, `timestamp`, and `Datetime`):contentReference[oaicite:15]{index=15}.

---

## 📑 Data contract

### ✅ Minimum required columns (recommended)

| Column | Type | Meaning |
| --- | --- | --- |
| `feature_id` | string/int | Stable ID for the geometry being summarized (field/plot/etc.) |
| `timestamp` | int64 | Observation time (Unix ms) for alignment across datasets:contentReference[oaicite:16]{index=16} |
| `datetime` | string | ISO-8601 datetime (human-readable):contentReference[oaicite:17]{index=17} |
| `ndvi_mean` | float | Mean NDVI over clear pixels (masked) |
| `ndvi_median` | float | Median NDVI over clear pixels |
| `ndvi_min` / `ndvi_max` | float | NDVI extrema (masked) |
| `ndvi_p10` / `ndvi_p90` | float | Percentiles (optional but useful) |
| `n_pixels_total` | int | Pixels intersecting the geometry at analysis scale |
| `n_pixels_clear` | int | Pixels flagged as clear (QA_PIXEL bit 6):contentReference[oaicite:18]{index=18} |
| `n_pixels_valid` | int | Pixels that are both clear and non-nodata (after all masks) |
| `clear_frac` | float | `n_pixels_clear / n_pixels_total` |
| `scale_m` | int | Analysis scale in meters (often 30 for Landsat):contentReference[oaicite:19]{index=19} |
| `source_collection` | string | e.g., `LANDSAT/LC08/C02/T1_L2`:contentReference[oaicite:20]{index=20} |
| `run_id` | string | Run identifier (ties back to logs/config) |
| `git_sha` | string | Code version used to generate these stats (if applicable) |

> If you add/change columns, update `schema__ndvi_stats.json` (if present) and note the change in the experiment report/runbook.

### 🧾 Recommended companion files

- `schema__ndvi_stats.json` – the canonical contract for downstream users.
- `run_metadata.json` – config snapshot, data filters (dates, cloud thresholds), and software versions.
- `qc__pixel_counts.*` – coverage metrics (clear/valid fraction) so missingness is visible and reproducible.

---

## ✅ QA / sanity checks

### NDVI range checks 🧪

- NDVI values should fall in **[-1, 1]**:contentReference[oaicite:21]{index=21}.
- If NDVI looks inverted/strange, confirm the **band order** in `normalizedDifference` (NIR first, red second):contentReference[oaicite:22]{index=22}.

### Coverage checks 🧊

- `n_pixels_valid > 0` for geometries expected to be observed.
- `clear_frac` near 0 → likely cloud/shadow/water masking dominated; downstream modeling should treat these as low-confidence.

### Spot-checking 🔎

Render NDVI for a handful of dates/features to verify plausibility (vegetation high, water low):contentReference[oaicite:23]{index=23}.

---

## 🧪 Statistical notes (don’t skip)

- Many comparisons → higher chance of false positives (e.g., 12 independent tests increases the probability of ≥1 false alarm to ~0.46 at α=0.05):contentReference[oaicite:24]{index=24}.
- Only reporting “successful” outcomes can inflate effect sizes and mislead conclusions:contentReference[oaicite:25]{index=25}.
- Prefer communicating uncertainty with **confidence intervals** rather than only “significant / not significant” labels:contentReference[oaicite:26]{index=26}.

---

## 🔁 Reproducibility checklist

This project prioritizes contract-first, deterministic pipelines:contentReference[oaicite:27]{index=27}.

Before you trust or publish stats, ensure you can answer:

- [ ] What raw sources (scene IDs / date filters) were used?
- [ ] What cloud/QA rules were applied (`QA_PIXEL` bits, cloud threshold)?
- [ ] What AOI/feature set was summarized (and versioned)?
- [ ] What reducer(s) were used (mean/median/etc.) and at what `scale_m`?
- [ ] What exact code version produced this output (git SHA / tag)?
- [ ] Is there an experiment report + log entry documenting intent/results? (see `mcp/experiments/` conventions):contentReference[oaicite:28]{index=28}.

---

## 🚚 Downstream usage

These NDVI stats commonly feed into higher-level products like “field health” indices and yield prediction pipelines:contentReference[oaicite:29]{index=29}—and can be wired into automated update workflows (ingest → NDVI → DB update → model inference):contentReference[oaicite:30]{index=30}.

---

## 🧰 Quick load examples

### Python 🐍

```python
import pandas as pd

# Pick whichever file exists for your run:
df = pd.read_parquet("ndvi_stats__by_feature.parquet")  # or pd.read_csv(...)
df.head()
```

### SQL-ish mindset 🧠

Treat the stats as a fact table keyed by `(feature_id, timestamp)`; join to:
- a feature dimension table (field boundaries, attributes)
- a time dimension table (day-of-year, season, phenology phase)
- weather/soil tables (if modeling yield/health)

---

## 📚 References (in-repo sources)

- Cloud-based workflows, NDVI math, masking with `QA_PIXEL`, Landsat L2 examples, and zonal stats patterns are drawn from *Cloud-Based Remote Sensing with Google Earth Engine*:contentReference[oaicite:31]{index=31}:contentReference[oaicite:32]{index=32}:contentReference[oaicite:33]{index=33}:contentReference[oaicite:34]{index=34}.
- Data staging + evidence artifact guidance comes from the project Markdown/work protocols:contentReference[oaicite:35]{index=35}:contentReference[oaicite:36]{index=36}.
- Landsat resolution/cadence and KFM pipeline context comes from KFM technical documentation:contentReference[oaicite:37]{index=37}:contentReference[oaicite:38]{index=38}.
- Statistical cautions are summarized from *Understanding Statistics & Experimental Design* and *Statistics Done Wrong*:contentReference[oaicite:39]{index=39}:contentReference[oaicite:40]{index=40}:contentReference[oaicite:41]{index=41}.

