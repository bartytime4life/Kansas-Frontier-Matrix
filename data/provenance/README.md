# Kansas-Frontier-Matrix — Data Provenance

This directory tracks **provenance, lineage, and licensing** for all datasets used in the  
**Kansas-Frontier-Matrix** knowledge hub. It provides a mission-grade record of where data came from,  
how it was transformed, and how its integrity can be verified.

Provenance is the **backbone of MCP reproducibility**: every file in `data/` must map to a verifiable  
lineage record here and to its corresponding **STAC Item/Collection**.

---

## Purpose

- Ensure **reproducibility** → every dataset can be traced back to its raw source and processing steps.  
- Document **lineage** → raw → processed → STAC-cataloged → web/export.  
- Track **checksums + file sizes** for integrity verification.  
- Record **licenses and usage terms** for open compliance.  
- Provide an audit trail aligned with the **Master Coder Protocol (MCP)** [oai_citation:0‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468) [oai_citation:1‡Kansas Data Resources for Frontier-Matrix Project.pdf](file-service://file-Q9AC5RwLTeV6QgadxHDf5P).  

---

## Directory Layout

data/provenance/
├── registry.json      # Master dataset registry (IDs → URLs, checksums, lineage)
├── LICENSES.md        # License texts and attribution notes
├── audits/            # Optional per-dataset audit logs (e.g., GCP reports, ETL configs)
└── README.md          # This file

---

## Provenance Workflow

1. **Fetch**  
   - Record original **source URL(s)**, retrieval date, and metadata.  
   - Save unmodified data in `data/raw/`.  

2. **Checksum**  
   - Compute SHA256 and file size for every raw and processed file:  
     ```bash
     scripts/gen_sha256.sh data/raw/<file>
     scripts/gen_sha256.sh data/processed/<file>
     ```  
   - Store values in `registry.json` keyed by dataset ID.  

3. **Process**  
   - Document transformations: reprojection, resampling, clipping, OCR, or GCP warps.  
   - Use **MCP-style logs**: problem → method → result.  
   - If scripts/Makefile are used, record target name + parameters.  

4. **STAC Entry**  
   - Add dataset metadata under `data/stac/collections/` or `data/stac/items/`.  
   - STAC Item must link back to provenance entries for verification (`href`, checksum).  

5. **License & Attribution**  
   - Record license text in `LICENSES.md`.  
   - Note any special terms (e.g., public domain, CC-BY-4.0, state-specific licenses).  

---

## Example registry.json Entry

```json
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

Best Practices
	•	Every dataset must have a provenance record (registry + audit if needed).
	•	If data are uncertain (e.g., OCR text, ambiguous place names), mark with a confidence flag.
	•	Keep audit logs human-readable and long-term accessible.
	•	Prefer authoritative open sources (USGS, NOAA, FEMA, Kansas GIS Hub, KGS).
	•	Ensure stable dataset IDs to avoid breaking STAC/web references.
	•	Sync registry.json updates with Makefile pipelines to maintain integrity.

⸻

Connections
	•	STAC catalog → Provenance checksums + lineage referenced in every Item.
	•	Makefile workflows → Provenance updated automatically after make fetch, make terrain, make stac.
	•	Web configs → Layers in web/data/*.json ultimately trace back here.
	•	Experiments → MCP logs in experiments/ must cite provenance IDs for datasets used.
	•	KML exports → Provenance for Google Earth KMZs (in data/kml/) must link back to source rasters in this registry.

⸻

References
	•	STAC 1.0.0 Specification
	•	MCP Templates → docs/mcp_templates/ (Scientific Method & Experiment Logs) ￼
	•	[Kansas Frontier Matrix — Design Audit Report] ￼
	•	[Data Resource Analysis Report] ￼

⸻

✅ This directory ensures Kansas Frontier Matrix datasets are auditable, reproducible, and compliant with both MCP and STAC standards.

----