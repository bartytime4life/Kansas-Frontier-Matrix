<div align="center">

# 🗂️ Kansas-Frontier-Matrix — **Source Descriptors** (`data/sources/`)

**Mission:** This folder contains **small, curated JSON descriptors** for every dataset used in the Kansas Frontier Matrix pipeline.  
They are the **canonical index** of external dependencies: URLs, licenses, provenance, temporal/spatial extents.  

📌 **Tiny, explicit, hand-edited JSONs** (a few KB).  
📌 **Never** store raw payloads here — those live in `data/raw/**`.  
📌 Validated against [`schema.source.json`](./schema.source.json).  

</div>

---

## Purpose

- 📖 Document external dependencies (URLs, licenses, provenance).  
- 🔄 Provide reproducible fetch/ETL recipes.  
- ⚙️ Drive `make fetch` and `make stac` jobs.  
- 🔍 Guarantee transparency & reproducibility in the historical GIS pipeline.  

Descriptors = **truth table** of data inputs → all downstream stages depend on them.

---

## Directory Layout

```text
data/sources/
├── schema.source.json   # JSON Schema for validation
├── ks_hydrography.json  # Example descriptor: hydrography
├── ks_roads_1930s.json  # Example descriptor: historic roads
└── ks_landcover_1936.json


⸻

Schema — Core Fields

Field	Type	Description
id	string	Unique machine-safe ID (lowercase, underscores or hyphens).
title	string	Human-readable dataset title.
type	enum	One of: vector, raster, collection, service.
period	string	Temporal coverage (1936, 1930s, 1854-1861).
urls	array	Download URLs or service endpoints.
bbox	array	[west, south, east, north] in EPSG:4326.
crs	string	Coordinate system (default: EPSG:4326).
license	object	License name + URL.
provenance	object	Attribution, publisher, DOI, or citation.
retrieved	string	ISO 8601 datetime when last fetched.
confidence	number	(Optional) confidence score (0.0–1.0).
notes	string	(Optional) free-form comments.


⸻

Workflow

flowchart TD
  A[Create/Edit Descriptor<br/>data/sources/*.json] --> B[Validate<br/>make validate-sources]
  B --> C[Fetch Raw Data<br/>make fetch → data/raw/** + checksums]
  C --> D[Process<br/>make cogs / make vectors → data/processed/**, data/cogs/**]
  D --> E[Build STAC<br/>make stac → data/stac/items/**]

<!-- END OF MERMAID -->



⸻

Examples
	•	ks_hydrography.json — Kansas surface water layers.
	•	ks_roads_1930s.json — Historic roads dataset.
	•	ks_landcover_1936.json — Land-cover snapshot.

👉 urls[] can list multiple files (e.g., county sheets). Fetch step will fan out and merge.

⸻

Git Policy
	•	✅ Always tracked in git.
	•	🚫 data/raw/** ignored by .gitignore.
	•	🔔 CI triggers on changes:
	•	Schema validation (make validate-sources)
	•	License/provenance checks
	•	STAC rebuild

⸻

Quickstart
	1.	Add a descriptor

$ $EDITOR data/sources/ks_new_dataset.json


	2.	Validate

make validate-sources


	3.	Fetch raw data

make fetch


	4.	Process & publish

make cogs vectors stac



⸻

TL;DR
	•	data/sources/ = curated index of inputs.
	•	Keeps raw payloads out of git, but guarantees reproducibility.
	•	Bridges source → raw → processed → STAC.
	•	Backbone of transparency, traceability, and MCP-grade reproducibility.

✅ If it’s in the pipeline, it must be listed here.

