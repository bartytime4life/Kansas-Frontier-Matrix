# Kansas-Frontier-Matrix — `data/tmp/` (Ephemeral Temporary Files)

This folder is reserved for **purely transient artifacts** — files created during builds, tests, or experiments  
that **do not belong in version control** and can be safely deleted at any time.

It acts as a scratchpad for pipelines, fetchers, and experiments so canonical data directories (`raw/`, `processed/`, `cogs/`, `derivatives/`) remain clean.

---

## Purpose

- Provide a writable sandbox for scripts and Makefile targets.  
- Hold downloads, unzipped archives, or intermediate exports that will be discarded after use.  
- Prevent clutter or accidental pollution in reproducible directories.  
- Serve as a **pipeline buffer**: e.g., temporary mosaics before COG conversion, OCR scratch text, clipped shapefiles before reproject.  

---

## Rules

- 🚫 **Never commit files in `data/tmp/`.**  
  - This directory is excluded by `.gitignore`.  
  - CI jobs ignore its contents entirely.  

- ✅ If a temporary file proves useful, **promote it**:  
  - → `data/work/` if it is an intermediate worth tracking short-term.  
  - → `data/processed/` or `data/cogs/` if it is analysis-ready.  
  - → `data/raw/` if it is a canonical upstream input.  
  - Update **STAC Items** and **provenance** if promoted.  

- 🧹 Everything here is **safe to delete** — scripts and Makefile rules must regenerate outputs as needed.  

---

## Typical Contents

- Temporary raster/vector conversions before COG/GeoJSON promotion.  
- Cache files from fetch scripts or API queries.  
- Zipped archives extracted mid-pipeline.  
- Test exports, thumbnails, or draft images.  
- Partial OCR text dumps during document processing.  
- Scratch shapefiles or clipped regions for inspection.  

---

## Connections in Data Lifecycle

This folder sits at the **lowest rung** of the data lifecycle:

tmp/  →  work/  →  processed/ | cogs/  →  derivatives/  →  stac/

- `tmp/` → ephemeral, ignored, wipeable.  
- `work/` → semi-scratch, tracked if reproducibility is valuable.  
- `processed/` & `cogs/` → validated, canonical inputs.  
- `derivatives/` → reproducible analysis outputs.  
- `stac/` → metadata catalog for discovery, versioning, and lineage.  

> MCP principle: **If it matters, promote it and document it. If not, let it vanish.** [oai_citation:0‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468)

---

## Usage Examples

### DEM pipeline scratch
```bash
# Mosaic raw tiles before creating a final COG
gdal_merge.py -o data/tmp/ks_mosaic_2018.tif data/raw/elevation/tiles/*.tif
rio cogeo create data/tmp/ks_mosaic_2018.tif data/cogs/dem/ks_1m_dem_2018.tif

OCR scratch

# Store intermediate OCR text here, not in processed/
tesseract data/raw/docs/treaty_osage_1825.pdf data/tmp/treaty_osage_1825 -l eng


⸻

Makefile Integration

Add tmp as a safe build target:

clean-tmp:
\trm -rf data/tmp/*

.PHONY: clean-tmp

CI pipelines can call make clean-tmp after runs to prevent accumulation.

⸻

Provenance & STAC Connections
	•	No provenance or STAC entries are required for files in data/tmp/.
	•	If promotion happens, immediately:
	•	Compute checksum (scripts/gen_sha256.sh)
	•	Add an entry to data/provenance/registry.json
	•	Create/update the relevant STAC Item (data/stac/items/**.json)

⸻

✅ Summary:
Use data/tmp/ for anything transient and disposable.
If a file becomes important → promote and document it; otherwise, let it vanish.

----