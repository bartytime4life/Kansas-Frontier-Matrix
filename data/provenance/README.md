<div align="center">

# 🧾 Kansas Geo Timeline — Data Provenance

This directory tracks **provenance, lineage, and licensing**  
for all datasets in the **Kansas Frontier Matrix** knowledge hub.  

It provides a **mission-grade audit trail** of data origins, transformations, and integrity checks.  

Provenance is the **backbone of MCP reproducibility**:  
every file in `data/` must map to a record here and to its corresponding **STAC Item/Collection**.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

```mermaid
flowchart TD
  A["Raw sources\n(data/raw/**)"] --> B["Provenance logging\n(data/provenance/registry.json)"]
  B --> C["Processed outputs\n(data/processed/**, data/cogs/**)"]
  C --> D["Checksums + licenses\n(data/provenance/*.json, LICENSES.md)"]
  C --> E["STAC Items\n(data/stac/items/**)"]
  E --> F["Validate\n(stac-validate)"]
  F --> G["Viewer + exports\n(web/config/** · data/kml/**)"]

<!-- END OF MERMAID -->



⸻

🎯 Purpose
	•	Guarantee reproducibility → every dataset is traceable from raw → processed → published.
	•	Maintain lineage → record transformations (e.g., GCP warps, reprojections).
	•	Track checksums & sizes → ensure file integrity.
	•	Record licenses → comply with open-data usage.
	•	Provide audit logs aligned with the Master Coder Protocol (MCP).

⸻

📂 Directory layout

data/provenance/
├── registry.json      # Master dataset registry (IDs → URLs, checksums, lineage)
├── LICENSES.md        # License texts & attribution notes
├── audits/            # Per-dataset audit logs (e.g., GCP reports, ETL configs)
└── README.md


⸻

🔄 Provenance workflow
	1.	Fetch raw data
	•	Record source URLs, retrieval date, metadata.
	•	Save unmodified files in data/raw/.
	2.	Checksums
	•	Compute SHA256 + file size:

scripts/gen_sha256.sh data/raw/<file>
scripts/gen_sha256.sh data/processed/<file>


	•	Store in registry.json keyed by dataset ID.

	3.	Process
	•	Document transformations (reprojection, clipping, OCR, GCPs).
	•	Record Makefile targets, script parameters, or experiment IDs.
	4.	STAC entry
	•	Add metadata in data/stac/items/ or data/stac/collections/.
	•	Each Item must link back to provenance (href, checksum).
	5.	License & attribution
	•	Record license text in LICENSES.md.
	•	Note terms (Public Domain, CC-BY, etc.).

⸻

📝 Example registry.json entry

{
  "id": "usgs_topo_1894_larned",
  "version": "1.1.0",
  "source_url": "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/KS/USGS_15x15_1894_Larned_Geo.tif",
  "retrieved": "2025-09-20",
  "checksum_sha256": "abc123def456…",
  "filesize_bytes": 104857600,
  "license": "public-domain",
  "lineage": [
    "download raw GeoTIFF from USGS TNM",
    "apply GCP warp to EPSG:4326 using 10 control points",
    "convert to Cloud-Optimized GeoTIFF with rio-cogeo"
  ],
  "stac_item": "data/stac/items/topo/usgs_topo_1894_larned.json"
}


⸻

📌 Best practices
	•	Every dataset must have a provenance record (registry + audit if needed).
	•	Mark uncertain data (OCR, ambiguous features) with a confidence flag.
	•	Keep audit logs human-readable and long-term accessible.
	•	Prefer authoritative sources (USGS, NOAA, FEMA, Kansas GIS Hub, KGS).
	•	Dataset IDs must be stable to avoid breaking STAC/web references.
	•	Sync registry updates with Makefile pipelines for integrity.

⸻

🔗 Connections
	•	STAC catalog → Items reference provenance checksums + lineage.
	•	Makefile workflows → provenance updated after make fetch, make terrain, make stac.
	•	Web configs → every web layer traces back to provenance.
	•	Experiments → MCP experiment logs must cite provenance IDs.
	•	KML exports → KMZ overlays must link back to provenance records.

⸻

📚 References
	•	STAC 1.0.0 specification
	•	MCP templates → docs/mcp_templates/ (Scientific Method & Experiment Logs)
	•	Kansas Frontier Matrix — Design Audit Report
	•	Data Resource Analysis Report

⸻

✅ Mission-grade principle: All datasets must be auditable, reproducible, and MCP-compliant.
This directory is the single source of truth for lineage + licensing across the Kansas Frontier Matrix.

