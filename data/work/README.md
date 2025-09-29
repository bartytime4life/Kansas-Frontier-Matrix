# Kansas-Frontier-Matrix — `data/work/` (Scratch + Intermediate Workspace)

This folder is a **sandbox for in-progress work products**:  
temporary outputs, drafts, or exploratory runs that are **not yet analysis-ready**.  

It exists to support **reproducibility of the scientific process**, while keeping canonical datasets  
(`data/raw/`, `data/cogs/`, `data/processed/`, `data/derivatives/`) clean and stable.

Think of `work/` as the **lab bench**: messy by design, wiped down once results are formalized and promoted.

---

## What Belongs Here (and What Doesn’t)

### ✅ Belongs
- **Intermediate artifacts** from ETL pipelines (e.g., uncleaned CSVs, OCR text dumps, staging GeoTIFFs before COG conversion).  
- **Scratch joins / test merges** of sources before formal schema integration.  
- **Temporary outputs** from notebooks, scripts, or pipelines under review.  
- **Experimental exports** (e.g., clipping county DEMs, trial STAC Items, trial vectorizations).  

### 🚫 Doesn’t
- Canonical raw downloads → `data/raw/**`.  
- Analysis-ready COGs, GeoJSON, MBTiles, PMTiles → `data/cogs/**` or `data/derivatives/**`.  
- Validated STAC Items & Collections → `data/stac/**`.  

---

## Suggested Directory Layout

data/work/
├── scratch/        # ad-hoc scripts, CSVs, GeoJSONs, test exports
├── ocr/            # raw OCR text prior to cleanup/normalization
├── staging/        # intermediate rasters/vectors prior to COG/GeoJSON conversion
├── joins/          # temporary merges or overlays of multiple sources
└── tmp/            # transient files (ignored by git)

> `.gitignore` excludes large binaries and `tmp/`.  
> Only promote files here into version control if they represent a reproducible intermediate stage worth documenting.

---

## Workflow Policy

1. **Stage here first**  
   - New raw pulls, OCR runs, or geoprocessing steps should land in `work/` before normalization.  

2. **Promote when reproducible**  
   - Once a file is cleaned, standardized (EPSG:4326, COG, GeoJSON, etc.), and documented:  
     - Move to `data/processed/` (analysis-ready reproducible outputs).  
     - Or to `data/derivatives/` (final products such as hillshade, slope classes).  
     - Create/update a corresponding STAC Item.  

3. **Ephemeral by default**  
   - Files here may be overwritten or discarded.  
   - If a file represents unique human effort (e.g., hand-digitized polygons), promote it to `data/raw/` or `data/sources/` with provenance metadata.  

---

## Provenance & Documentation

Even in scratch space, **minimum metadata** is required:

- Use descriptive filenames:  
  - `countyX_dem_clip_raw.tif`  
  - `ocr_treaty_1854.txt`  

- If a step is **non-reproducible** (e.g., manual QGIS edits), log it in a sidecar:  
  - Markdown note: `clip_log.md`  
  - Or append to `work_log.jsonl` with: `timestamp, action, notes`.  

- Use consistent datetime stamps in filenames for clarity:  
  - `trial_merge_2025-09-28.geojson`.  

---

## Connections to MCP & Knowledge Hub

- Mirrors the **“lab notebook”** stage in MCP experiment templates [oai_citation:0‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468).  
- Supports **integration of cartographic, geological, and historical data** before formal STAC ingestion.  
- Provides a staging ground for **AI/ETL backend pipelines**: OCR text, NLP-extracted entities, batch geocoding, or graph linking before promotion to Neo4j [oai_citation:1‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).  
- Helps bridge raw historical scans → cleaned processed files → **discoverable STAC Items** used by the web viewer.  

---

## Cleanup & CI

- Run `make clean-work` to purge temporary files safely.  
- Promote anything worth keeping **before cleanup**.  
- CI jobs may fail if `work/` contains large untracked binaries.  

### Suggested Makefile Targets

```makefile
clean-work:
\trm -rf data/work/*

promote-work-to-processed:
\t# example placeholder: move staged outputs to processed + run STAC update


⸻

Lifecycle Connections

tmp/   →   work/   →   processed/ | cogs/   →   derivatives/   →   stac/   →   web/

	•	tmp/ → transient, safe to wipe.
	•	work/ → staging, exploratory, logged but not canonical.
	•	processed/ → reproducible, analysis-ready.
	•	cogs/ → mission-final rasters.
	•	derivatives/ → reproducible analysis products.
	•	stac/ → catalog metadata (discoverability + provenance).
	•	web/ → published artifacts for viewer / public distribution.

⸻

✅ Summary:
data/work/ is a scratch + staging workspace — ephemeral but documented enough to support reproducibility, and cleaned regularly.
It is the bridge between raw data chaos and structured archival order.

---
