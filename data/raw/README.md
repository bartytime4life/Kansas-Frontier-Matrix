# Kansas-Frontier-Matrix — Raw Data

This directory is the **landing zone** for immutable source payloads:  
files are stored here *exactly as acquired from upstream providers*  
(no edits, no reprojection, no clipping).  

Every raw payload **must ship with**:  
- a `*.sha256` checksum file, and  
- a compact provenance sidecar `*.src.json`.

This folder feeds the ingestion pipeline that creates reproducible derivatives under `data/processed/**` and `data/cogs/**`.  
**Do not** modify files in place. Any fixups or enhancements must be scripted in `scripts/` or `Makefile` targets,  
with results saved to processed directories.

---

## Directory Layout & Sidecars

data/raw/
├── elevation/
│   ├── ks_1m_dem_2018_2020.tif               # as-downloaded (no edits)
│   ├── ks_1m_dem_2018_2020.tif.sha256        # SHA-256 checksum of payload
│   └── ks_1m_dem_2018_2020.src.json          # provenance sidecar (see below)
├── historic_maps/
│   └── usgs_topo_larned_1894.tif
├── vectors/
│   └── plss_ks_2020.zip
└── docs/
└── treaty_osage_1825.pdf

### Example `*.src.json` (minimal, publication-safe)

```json
{
  "title": "Kansas DEM (1 m; 2018–2020)",
  "provider": "KARS / State of Kansas",
  "access": "https://tiles.kansasgis.org/arcgis/rest/services/Elevation/KS_1m_DEM/ImageServer",
  "downloaded": "2025-09-18T01:50:00Z",
  "license": "CC-BY-4.0",
  "spatial": { "bbox": [-102.05, 36.99, -94.61, 40.00], "crs": "EPSG:4326" },
  "temporal": { "start": "2018-01-01", "end": "2020-12-31" },
  "sha256": "<match file.sha256>"
}

Sidecars mirror the project principle of documentation-first + traceability,
without leaking pipeline internals into raw storage.

⸻

What Belongs Here

✅ Allowed:
	•	Original payloads → rasters (GeoTIFF/IMG), archives (ZIP/TGZ), vector/tabular bundles (SHP/FGDB/GeoPackage), and primary docs (PDF/CSV).
	•	Stored exactly as published (retain CRS, tiling, compression, nodata).

❌ Not allowed:
	•	Reprojected, clipped, resampled, or edited versions → must go to data/processed/**.
	•	Mission-final rasters (COGs) → must go to data/cogs/**.

⸻

Storage & Size Policy
	•	Prefer remote references when sources are stable and reproducible (STAC can point directly at URLs).
	•	Mirror locally only what’s required for reproducibility or offline builds.
	•	Large payloads must be tracked with Git LFS or DVC.
	•	Suggested caps (can be tuned in Makefile/CI):
	•	Single raw file ≤ 8 GB
	•	Bundled dataset ≤ 20 GB
	•	Supplement bundles ≤ 200 MB (with pointer to DOI for full-resolution)

⸻

Provenance & Integrity
	1.	Checksum every raw file:

shasum -a 256 data/raw/elevation/ks_1m_dem_2018_2020.tif \
  | awk '{print $1}' > data/raw/elevation/ks_1m_dem_2018_2020.tif.sha256


	2.	Record provenance in .src.json (source URL, license, spatial/temporal extent, checksum).
	3.	Quarantine rule:
	•	If license is unclear or conflicting → move to data/raw/_quarantine/ and resolve before use.

⸻

Ingestion → Processing Flow
	1.	Validate → checksum, license, format.
	2.	Catalog → via lightweight source descriptors (data/sources/**.json).
	3.	Process → transform into COGs/GeoJSON under data/cogs/** and data/processed/**.
	4.	Publish → update STAC (data/stac/items/**) and provenance registry (data/provenance/registry.json).

This ensures raw → processed → STAC lineage is always traceable ￼.

⸻

Naming Conventions

Stable slugs:

<topic>_<year-or-range>[_{region|scale|edition}].<ext>

Examples:
	•	ks_1m_dem_2018_2020.tif
	•	usgs_topo_larned_1894.tif
	•	plss_ks_2020.zip

⸻

Licensing & Ethics
	•	Record license verbatim in .src.json.
	•	For culturally sensitive materials (e.g., sacred sites, oral histories):
	•	Apply ethics guardrails (access controls, attribute generalization).
	•	Consult provenance and community guidelines before publication ￼.

⸻

Quick Validation Checks

# Inspect spatial metadata
gdalinfo data/raw/elevation/ks_1m_dem_2018_2020.tif | sed -n '1,80p'

# Validate GeoTIFF tags
listgeo -no_norm data/raw/elevation/*.tif | head -n 40

# Verify ZIP integrity
unzip -t data/raw/vectors/plss_ks_2020.zip


⸻

DOs / DON’Ts
	•	✅ Keep original bits immutable.
	•	✅ Add sidecars (.sha256, .src.json) for provenance and verification.
	•	✅ Use LFS/DVC for large payloads.
	•	❌ Don’t reproject, clip, or compress here (do it in data/processed/**).
	•	❌ Don’t commit multi-GB binaries without LFS/DVC + checksum entries.

⸻

Notes for Maintainers
	•	.gitattributes must route large binaries to LFS and disable auto-merging.
	•	CI should:
	•	Verify checksums (*.sha256)
	•	Validate .src.json against schema (provenance.schema.json)
	•	data/raw/** should be ignored by linters/formatters — validation only.

⸻

✅ This directory ensures Kansas Frontier Matrix raw datasets are immutable, verifiable, and traceable,
forming the foundation for reproducible pipelines, STAC compliance, and MCP-grade audit trails.

---