<div align="center">

# 📥 Kansas-Frontier-Matrix — **Raw Data** (`data/raw/`)

**Mission:** This is the **landing zone** for **immutable source payloads**.  
Files are stored **exactly as acquired from upstream providers** — no edits, no reprojection, no clipping.  

📌 Every payload ships with:
- a `*.sha256` checksum file  
- a provenance sidecar `*.src.json`

**Golden Rule:** Do **not** modify files in place. All fixups are scripted (in `scripts/` or `Makefile`), with results stored in `data/processed/**` or `data/cogs/**`.

</div>

---

## Contents

- [Directory Layout](#directory-layout)  
- [Sidecar Format](#sidecar-format)  
- [What Belongs Here](#what-belongs-here)  
- [Storage & Size Policy](#storage--size-policy)  
- [Provenance & Integrity](#provenance--integrity)  
- [Ingestion Flow](#ingestion-flow)  
- [Naming Conventions](#naming-conventions)  
- [Licensing & Ethics](#licensing--ethics)  
- [Quick Validation Checks](#quick-validation-checks)  
- [DOs / DON’Ts](#dos--donts)  
- [Maintainer Notes](#maintainer-notes)  
- [TL;DR](#tldr)  

---

## Directory Layout

```text
data/raw/
├── elevation/
│   ├── ks_1m_dem_2018_2020.tif
│   ├── ks_1m_dem_2018_2020.tif.sha256
│   └── ks_1m_dem_2018_2020.src.json
├── historic_maps/
│   └── usgs_topo_larned_1894.tif
├── vectors/
│   └── plss_ks_2020.zip
└── docs/
    └── treaty_osage_1825.pdf


⸻

Sidecar Format

Every payload has a *.src.json — compact, publication-safe provenance.

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

Sidecars = traceability without clutter: they don’t leak pipeline internals, only provenance.

⸻

What Belongs Here

✅ Allowed
	•	Original payloads: rasters (GeoTIFF, IMG), archives (ZIP/TGZ), vector bundles (SHP, FGDB, GPKG), primary docs (PDF, CSV).
	•	Store exactly as published (CRS, tiling, compression intact).

❌ Not Allowed
	•	Reprojected, clipped, resampled, or edited → goes to data/processed/**.
	•	Final Cloud-Optimized GeoTIFFs (COGs) → goes to data/cogs/**.

⸻

Storage & Size Policy
	•	Prefer remote references when stable & reproducible (STAC can point to URLs).
	•	Mirror locally only when required for reproducibility/offline builds.
	•	Track large payloads with Git LFS or DVC.

Suggested caps:
	•	Single raw file ≤ 8 GB
	•	Bundled dataset ≤ 20 GB
	•	Supplement bundles ≤ 200 MB (with pointer to DOI/full-resolution source)

⸻

Provenance & Integrity
	1.	Checksum every raw file:

shasum -a 256 data/raw/elevation/ks_1m_dem_2018_2020.tif \
  | awk '{print $1}' > data/raw/elevation/ks_1m_dem_2018_2020.tif.sha256


	2.	Record provenance in .src.json: source URL, license, spatial/temporal extent, checksum.
	3.	Quarantine rule:
	•	If license unclear/conflicting → move to data/raw/_quarantine/ until resolved.

⸻

Ingestion Flow

flowchart TD
  A[Raw Payload<br/>data/raw/**] --> B[Validate<br/>checksum, license, format]
  B --> C[Catalog<br/>data/sources/*.json]
  C --> D[Process<br/>COGs / GeoJSON<br/>data/cogs/**, data/processed/**]
  D --> E[Publish<br/>STAC Items + Provenance Registry]

<!-- END OF MERMAID -->



⸻

Naming Conventions

Stable slug pattern:

<topic>_<year-or-range>[_{region|scale|edition}].<ext>

Examples:
	•	ks_1m_dem_2018_2020.tif
	•	usgs_topo_larned_1894.tif
	•	plss_ks_2020.zip

⸻

Licensing & Ethics
	•	Record license verbatim in .src.json.
	•	For culturally sensitive content (e.g., sacred sites, oral histories):
	•	Apply access controls and attribute generalization.
	•	Follow provenance + community guidelines before release.

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

✅ Keep original bits immutable
✅ Add .sha256 + .src.json sidecars
✅ Use LFS/DVC for large payloads
❌ Don’t reproject, clip, or compress here
❌ Don’t commit multi-GB binaries without LFS/DVC + checksums

⸻

Maintainer Notes
	•	.gitattributes must route large binaries to LFS and disable auto-merging.
	•	CI should validate:
	•	Checksums (*.sha256)
	•	.src.json against provenance.schema.json
	•	data/raw/** is validation-only: linters/formatters skip it.

⸻

TL;DR
	•	Immutable landing zone: raw payloads live here unmodified.
	•	Every file has a checksum + provenance sidecar.
	•	Processing happens elsewhere → data/processed/**, data/cogs/**.
	•	Traceability preserved: raw → processed → STAC lineage is always auditable.

✅ This directory is the foundation of reproducibility, STAC compliance, and MCP-grade audit trails.

