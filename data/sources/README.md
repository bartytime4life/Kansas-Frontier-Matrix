<div align="center">

# 🗂️ Kansas Geo Timeline — Source Descriptors  
`data/sources/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.pre-commit-config.yaml)  
[![Docs](https://img.shields.io/badge/docs-MCP%20Standards-blue.svg)](../../docs/)  
[![Data Provenance](https://img.shields.io/badge/provenance-verified✅-green.svg)](../../stac/items/)  

**Mission:** This folder contains **small, curated JSON descriptors** for every dataset used in the Kansas Frontier Matrix pipeline.  
They are the **canonical index** of external dependencies: URLs, licenses, provenance, and spatial/temporal extents.  

📌 **Tiny, explicit, hand-edited JSONs** (a few KB).  
📌 **Never** store raw payloads here → those live in `data/raw/**`.  
📌 Validated against [`schema.source.json`](./schema.source.json).  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Create/Edit Descriptor\n(data/sources/*.json)"] --> B["Validate\n(make validate-sources)"]
  B --> C["Fetch Raw Data\n(make fetch → data/raw/** + checksums)"]
  C --> D["Process\n(make cogs / make vectors → data/processed/**, data/cogs/**)"]
  D --> E["Build STAC\n(make stac → data/stac/items/**)"]
  E --> F["Viewer integration\n(web/config/layers.json)"]

<!-- END OF MERMAID -->



⸻

🎯 Purpose
	•	📖 Document external dependencies (URLs, licenses, provenance).
	•	🔄 Provide reproducible fetch/ETL recipes.
	•	⚙️ Drive make fetch and make stac jobs.
	•	🔍 Guarantee transparency & reproducibility in the historical GIS pipeline.

Descriptors = truth table of inputs → all downstream stages depend on them.

⸻

📂 Directory Layout

data/sources/
├── schema.source.json   # JSON Schema for validation
├── ks_hydrography.json  # Kansas hydrography example
├── ks_roads_1930s.json  # Historic roads (1930s)
├── ks_landcover_1936.json
└── README.md


⸻

🧭 Schema — Core Fields

Field	Type	Description
id	string	Unique ID (lowercase, underscores or hyphens).
title	string	Human-readable dataset title.
type	enum	One of: vector, raster, collection, service.
period	string	Temporal coverage (e.g., 1936, 1930s, 1854–1861).
urls	array	Download URLs or service endpoints.
bbox	array	[west, south, east, north] in EPSG:4326.
crs	string	Coordinate system (default: EPSG:4326).
license	object	License name + URL.
provenance	object	Attribution, publisher, DOI, or citation.
retrieved	string	ISO 8601 datetime when last fetched.
confidence	number	(Optional) confidence score (0.0–1.0).
notes	string	(Optional) free-form comments.


⸻

🔄 Workflow
	1.	Add/Edit descriptor → data/sources/*.json
	2.	Validate

make validate-sources

	3.	Fetch raw data → saves to data/raw/** with checksums

make fetch

	4.	Process → convert into COGs or vectors

make cogs
make vectors

	5.	Build STAC → generate catalog Items

make stac


⸻

📑 Examples
	•	ks_hydrography.json → Kansas surface water layers
	•	ks_roads_1930s.json → historic road network
	•	ks_landcover_1936.json → land-cover snapshot

👉 urls[] can include multiple files (e.g., county sheets).
The make fetch step will fan out and merge as required.

⸻

🔐 Git Policy
	•	✅ Always tracked in git.
	•	🚫 data/raw/** ignored by .gitignore.
	•	🔔 CI runs on changes:
	•	Schema validation (make validate-sources)
	•	License/provenance checks
	•	STAC rebuild

⸻

🚀 Quickstart

# 1. Add descriptor
$EDITOR data/sources/ks_new_dataset.json

# 2. Validate
make validate-sources

# 3. Fetch
make fetch

# 4. Process & publish
make cogs vectors stac


⸻

✅ QA Checklist
	•	Descriptor schema validated (schema.source.json)
	•	License and provenance explicitly recorded
	•	Raw payload downloaded into data/raw/ with .sha256 checksum
	•	All downstream outputs trace back to descriptor ID
	•	Descriptor committed to git, reviewed, and approved

⸻

📝 TL;DR
	•	data/sources/ = curated index of inputs
	•	Keeps raw payloads out of git while ensuring reproducibility
	•	Bridges source → raw → processed → STAC
	•	Backbone of transparency, traceability, and MCP reproducibility

<div align="center">


✅ If it’s in the pipeline, it must be listed here.

</div>
```
