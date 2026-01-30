# 🧩 `pipelines/shared/` — Shared Pipeline Toolkit

![Provenance First](https://img.shields.io/badge/provenance-first-blue)
![Deterministic](https://img.shields.io/badge/pipelines-deterministic-brightgreen)
![Quality Gates](https://img.shields.io/badge/quality-gates-important-orange)
![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-purple)

> [!IMPORTANT]
> This folder is the **single source of truth** for reusable pipeline helpers.
> If multiple pipelines need the same logic, it belongs here (or it becomes tech debt). 🧯

---

## 🎯 What this folder is

`pipelines/shared/` contains **reusable building blocks** used by KFM ETL + simulation pipelines—so dataset pipelines can stay short, consistent, and reviewable.

Think of this folder as your **pipeline standard library**:

- ✅ deterministic execution (same inputs/config → same outputs)
- 🧾 provenance + metadata generation helpers
- 🧪 validation + “quality gates”
- 🗺️ geospatial utilities (CRS, geometry fixes, bounds, tiling helpers)
- 📦 consistent IO + path conventions
- 🧰 shared CLI patterns (if/when we add them)

---

## 🧭 Canonical data flow contract

KFM pipelines are designed to respect a strict data lifecycle:

```text
Raw → Processed → Catalog/Prov → Database → API → UI
```

This directory exists to **make it easy** for every pipeline to comply with that flow (and hard to accidentally bypass it). 🔒

---

## 🗂️ Suggested layout inside `pipelines/shared/`

> [!NOTE]
> Your repo may already have some of these files. This is the **target mental model** for how we organize shared pipeline logic.

```text
📁 pipelines/
  ├─ 📁 shared/
  │  ├─ 📄 README.md
  │  ├─ 🐍 __init__.py
  │  ├─ 🧭 paths.py              # “Where does this dataset live?” helpers
  │  ├─ 📦 io.py                 # read/write helpers (csv/parquet/geojson/geotiff)
  │  ├─ 🧾 provenance.py         # W3C PROV-ish run logs (inputs/outputs/agents/activity)
  │  ├─ 🗺️ geo.py                # CRS transforms, geometry cleanup, bbox/extent helpers
  │  ├─ ✅ validate.py           # schema + domain validation (quality gates)
  │  ├─ 🧰 config.py             # config loading + env overlay
  │  ├─ 📝 logging.py            # structured logging conventions
  │  └─ 🧪 testing_fixtures.py    # shared test helpers (optional)
  └─ 📄 import_some_dataset.py   # dataset-specific pipeline scripts live outside /shared
```

---

## 🧱 Design rules for shared helpers

### ✅ Rule 1: Shared code must be boring
Shared helpers should be:
- small 🧩
- predictable 🎯
- well-tested 🧪
- documented 📝
- stable APIs 🔒

Avoid:
- dataset-specific logic
- hidden globals / hidden state
- network calls inside shared functions (downloading belongs in explicit “fetch raw” steps)

---

### ✅ Rule 2: Determinism is non‑negotiable
Shared helpers must support deterministic pipelines:

- no interactive prompts
- fixed RNG seeds where randomness is used (simulations)
- consistent sorting / stable output writing
- checksum-based “no-op” detection when inputs didn’t change (where appropriate)

---

### ✅ Rule 3: Everything that becomes “KFM data” gets documentation
A pipeline isn’t “done” until it can also:
- write/update **processed outputs**
- write/update **catalog metadata** (STAC / DCAT style)
- write/update **provenance logs** (inputs, outputs, script version, timestamps, params)

Shared helpers should make that workflow fast and repeatable. ⚙️

---

## 🧾 Provenance contract (what shared helpers should capture)

A provenance record for a pipeline run should be able to answer:

> “How was this dataset produced?” 🕵️‍♂️

At minimum, provenance utilities should capture:

- **Entities**: input raw files (plus checksum and/or source URL) + produced output files
- **Activity**: what ran (script / notebook / command), when, with which parameters
- **Agents**: pipeline code version + person/system triggering the run

**Practical tip:** treat provenance generation as a first-class output, not a “logging extra”.

---

## ✅ Quality gates (recommended)

Shared validation helpers should support checks like:

### 🧪 Structural checks
- required columns exist
- types match expectations (date, numeric, category)
- no duplicate primary keys (where applicable)
- no unexpected null spikes

### 🗺️ Spatial checks (if geodata)
- CRS is what we expect
- geometries are valid (fixable invalids repaired; unfixables flagged)
- bbox/extent computed and saved to metadata
- coordinates are plausible (Kansas-ish bounds, or dataset-specific bounds)

### 📊 Statistical sanity checks
- row counts within expected range
- min/max within plausible bounds
- distribution checks (optional; guardrails, not overfitting)

---

## 🧰 Example: “typical pipeline” skeleton (using shared utilities)

> [!TIP]
> This is a pattern, not a strict implementation. The point is: **pipelines should read like a checklist**.

```python
"""
pipelines/import_census_1900.py
"""

from pipelines.shared import paths, io, geo, validate, provenance, logging as klog

def main():
    logger = klog.get_logger(__name__)

    run = provenance.start_run(
        pipeline="import_census_1900",
        params={"year": 1900},
    )

    # 1) Read RAW (read-only)
    raw_path = paths.raw("census_1900/census_1900.csv")
    df = io.read_csv(raw_path)

    # 2) Transform / Clean
    df = validate.required_columns(df, ["county", "population"])
    gdf = geo.attach_geometry(df, lon_col="lon", lat_col="lat", crs="EPSG:4326")
    gdf = geo.make_valid(gdf)

    # 3) Write PROCESSED
    out_path = paths.processed("census/1900_population.geojson")
    io.write_geojson(gdf, out_path)

    # 4) Write METADATA + PROVENANCE (hard requirement)
    # catalog.write_stac_item(...)
    provenance.finish_run(
        run,
        inputs=[raw_path],
        outputs=[out_path],
        notes="Imported and cleaned 1900 census; validated schema and geometry.",
    )

    logger.info("done", extra={"output": str(out_path)})

if __name__ == "__main__":
    main()
```

---

## 🧪 Testing guidance (shared code)

Shared utilities should ship with tests because:
- one bug here can corrupt many datasets 🧨
- deterministic pipelines are only believable if testable ✅

Recommended test layers:
- **unit tests** for each helper
- **integration tests** for “mini pipelines” on tiny fixture datasets
- CI runs tests on PRs and mainline merges (keep the pipeline green) 🟢

---

## 🧩 Contributing checklist for `pipelines/shared/`

When you add or modify shared helpers, include:

- [ ] docstring + README update (if behavior changes)
- [ ] unit test(s)
- [ ] clear failure modes (raise with helpful messages)
- [ ] stable function signatures (or version/breaking-change note)
- [ ] deterministic behavior verified
- [ ] no hidden side effects (esp. touching `data/raw/`)

---

## 🔗 Related docs (recommended)

- 📄 `docs/architecture/system_overview.md` (system pipeline rules + data lifecycle)
- 📁 `data/` folder READMEs (raw/processed/catalog/provenance expectations)
- 🧠 `docs/` AI + provenance policies (if pipelines feed AI features)

---

## 🧯 Troubleshooting

### “My pipeline output differs between runs…”
Common causes:
- RNG seed not fixed
- non-deterministic row ordering before writing
- floating precision changes (ensure consistent rounding or encoding)
- environment-dependent parsing (pin versions; normalize timezones)

### “CI says metadata/provenance is missing…”
That’s expected behavior. If a pipeline creates/updates data, it should also create/update:
- catalog metadata
- provenance logs

---

> [!END]
> Goal: make pipelines feel like **repeatable scientific procedures**, not one-off scripts. 🧪🗺️

