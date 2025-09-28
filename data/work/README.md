# `data/work/` — Scratch + Intermediate Workspace

This folder is a **sandbox for in-progress work products**:
temporary outputs, drafts, or exploratory runs that are **not yet analysis-ready**.
It exists to support reproducibility of the scientific process, while keeping
canonical datasets (`data/cogs/`), curated sources (`data/sources/`),
and reproducible derivatives (`data/derivatives/`) clean.

---

## What belongs here (and what doesn’t)

- ✅ **Belongs**:
  - intermediate artifacts from ETL pipelines (e.g. un-cleaned CSVs, OCR text, staging GeoTIFFs before conversion to COGs)
  - scratch joins / test merges of sources before formal schema integration
  - temporary outputs from notebooks or scripts under review
  - experimental exports (e.g. clipping county DEMs, trial STAC items)  
- 🚫 **Doesn’t**:
  - canonical raw downloads → `data/sources/**`
  - analysis-ready COGs, GeoJSON, or tiled outputs → `data/cogs/**` or `data/derivatives/**`
  - validated STAC items and collections → `data/stac/**`

Think of `work/` as a **lab bench**: messy by design, but wiped down
once results are formalized and promoted.

---

## Directory layout

```

data/
└─ work/
├─ scratch/        # ad-hoc scripts, CSVs, GeoJSONs, test exports
├─ ocr/            # raw text from OCR before cleaning
├─ staging/        # intermediate rasters/vectors prior to COG/GeoJSON conversion
├─ joins/          # temporary merges or overlays of multiple sources
└─ tmp/            # transient files (ignored by git except when explicitly promoted)

```

> Note: `.gitignore` is set to exclude large binaries and `tmp/` contents.
> Only promote files here into version control if they represent a reproducible
> intermediate stage worth documenting.

---

## Workflow policy

1. **Stage here first**  
   New raw pulls, OCR runs, or geoprocessing steps land here before normalization.

2. **Promote when reproducible**  
   Once a file is cleaned, standardized (EPSG:4326, COG, GeoJSON, etc.), and
   documented, it should be moved to `data/processed/` or `data/derivatives/`
   with an accompanying STAC item.

3. **Ephemeral by default**  
   Files in `work/` may be overwritten or discarded. If a file represents a unique
   effort (e.g. hand-digitized boundaries), promote it to `sources/` with full provenance.

---

## Provenance and Documentation

Even though `work/` is scratch space, **minimum metadata** is still expected:

- Name files descriptively: `countyX_dem_clip_raw.tif`, `ocr_treaty_1854.txt`
- If a step is non-reproducible (manual fix, GUI QGIS operation), **log the action**
  in a sidecar `.md` note or `work_log.jsonl`
- Use consistent datetime and version stamps for clarity.

---

## Connections to MCP & Knowledge Hub

This folder aligns with **Master Coder Protocol** practices:

- Mirrors the **“lab notebook”** stage in experiment templates:contentReference[oaicite:0]{index=0}
- Allows integration of **cartographic, geological, and historical data** before
  final STAC ingestion:contentReference[oaicite:1]{index=1}
- Supports **AI/ETL backend pipelines** that often require staging directories for
  OCR text, NLP-extracted entities, or batch geocoding before pushing to the
  Neo4j knowledge graph:contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}

---

## Cleanup

- Run `make clean-work` (see Makefile) to purge temporary files safely.
- Promote anything worth keeping before cleanup.
- CI jobs may fail if `work/` contains large untracked binaries.

---

✦ **Summary:** `data/work/` is a **scratch + staging workspace** — ephemeral, flexible,
documented only enough to reproduce key steps, and cleaned regularly.
It is the bridge between raw data chaos and structured archival order.
```

