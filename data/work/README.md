<div align="center">

# 🧪 Kansas-Frontier-Matrix — Workbench (`data/work/`)

**Mission:** Provide a **scratch + staging workspace** for  
intermediate artifacts, exploratory runs, and draft outputs  
that are **not yet canonical or analysis-ready**.  

Think of `data/work/` as the **lab bench**: messy by design,  
cleaned once results are formalized and promoted.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)

📌 Excluded from releases, partially ignored via `.gitignore`.  
📌 Serves reproducibility during experimentation.  
📌 Files here are **ephemeral by default** — promote if valuable.  

</div>

---

## 🎯 Purpose

- Stage **intermediate outputs** from ETL pipelines.  
- Host **scratch joins** or test merges before schema integration.  
- Support **OCR, NLP, geoprocessing** experiments.  
- Capture **exploratory notebooks/scripts** without polluting canonical dirs.  

---

## 📂 Suggested Layout

```text
data/work/
├── scratch/        # ad-hoc scripts, CSVs, test exports
├── ocr/            # raw OCR text prior to cleanup
├── staging/        # rasters/vectors before COG/GeoJSON conversion
├── joins/          # trial merges/overlays of multiple sources
└── tmp/            # transient files (always gitignored)

.gitignore excludes tmp/ and large binaries.
Promote only files that represent reproducible steps.

⸻

✅ Belongs / 🚫 Doesn’t

✅ Belongs
	•	Intermediate CSVs, OCR dumps, staging GeoTIFFs.
	•	Scratch merges or overlays prior to schema integration.
	•	Draft exports (clipped DEMs, trial vectorizations, test STAC).

🚫 Doesn’t
	•	Canonical raw inputs → data/raw/.
	•	Analysis-ready COGs/GeoJSON/PMTiles → data/cogs/ or data/derivatives/.
	•	Validated metadata → stac/.

⸻

📜 Workflow Policy
	1.	Stage first → land new outputs here before cleanup/normalization.
	2.	Promote when reproducible → once standardized & documented, move to:
	•	processed/ for analysis-ready outputs.
	•	derivatives/ for final products (e.g., slope classes).
	•	Create/update corresponding STAC Items.
	3.	Ephemeral by default → overwrite or delete unless promoted.

If effort is non-reproducible (e.g. manual digitization), promote with provenance.

⸻

📝 Minimum Metadata

Even scratch work must have basic labeling:
	•	Use descriptive filenames:
	•	countyX_dem_clip_raw.tif
	•	ocr_treaty_1854.txt
	•	If manual edits, log them in a sidecar (clip_log.md or work_log.jsonl).
	•	Timestamp filenames for clarity:
	•	trial_merge_2025-09-30.geojson.

⸻

🔄 Lifecycle Position

flowchart LR
  A["Ephemeral scratch\n(data/tmp/)"] --> B["Staging workspace\n(data/work/)"]
  B --> C["Processed / COGs\n(data/processed, data/cogs)"]
  C --> D["Derivatives\n(data/derivatives)"]
  D --> E["Catalog\n(stac/items)"]
  E --> F["Web Viewer\n(web/)"]

<!-- END OF MERMAID -->



⸻

🧹 Cleanup & CI
	•	Run make clean-work to purge contents safely.
	•	Always promote before cleanup if the artifact matters.
	•	CI may fail if large untracked binaries remain here.

Makefile Targets (example):

clean-work:
	rm -rf data/work/*

promote-work-to-processed:
	# Move staged outputs to processed/ + run STAC update


⸻

🔗 MCP & Knowledge Hub Role
	•	Represents the “lab notebook” stage in MCP workflows .
	•	Bridges raw historical scans → processed → STAC Items .
	•	Staging ground for AI/ETL backends (OCR, NLP, batch geocoding, graph linking).

⸻

✅ Summary:
data/work/ is a scratch + staging area — ephemeral,
but documented enough to support reproducibility.
It is the bridge between raw data chaos and archival order.