# Kansas-Frontier-Matrix — Data Provenance

This directory tracks **provenance, lineage, and licensing** for all datasets used in the  
**Kansas-Frontier-Matrix** knowledge hub. It provides a mission-grade record of where data came from,  
how it was transformed, and how its integrity can be verified.

---

## Purpose

- Ensure **reproducibility** (every dataset can be traced back to its source and processing steps).
- Document **lineage** (raw → processed → STAC-cataloged).
- Track **checksums** and **file sizes** for integrity verification.
- Record **licenses and usage terms** for open compliance.
- Provide an audit trail consistent with the **Master Coder Protocol (MCP)**.

---

## Directory Layout

```

data/provenance/
├── registry.json      # Master dataset → checksum → URL mapping
├── LICENSES.md        # License texts and attribution notes
├── audits/            # Optional per-dataset audit logs (ingestion steps, GCP reports)
└── README.md          # This file

````

---

## Provenance Workflow

1. **Fetch**  
   - Record the original **source URL**, retrieval date, and metadata.  
   - Save unmodified data in `data/raw/`.

2. **Checksum**  
   - Compute SHA256 and file size for each raw and processed file.  
   - Store in `registry.json` under the dataset ID.

3. **Process**  
   - Document transformations: reprojection, resampling, clipping, OCR, or GCP warps.  
   - Each step should include a short MCP-style log (problem → method → result).

4. **STAC Entry**  
   - Add dataset metadata under `data/stac/collections/` or `data/stac/items/`.  
   - Link back to provenance entries for verification.

5. **License & Attribution**  
   - Record license text in `LICENSES.md`.  
   - Note special conditions (e.g., public domain, CC-BY-4.0, government open data).

---

## Example registry.json Entry

```json
{
  "id": "usgs_topo_1894_larned",
  "version": "1.1.0",
  "source_url": "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/KS/USGS_15x15_1894_Larned_Geo.tif",
  "retrieved": "2025-09-20",
  "checksum_sha256": "abc123…",
  "filesize_bytes": 104857600,
  "license": "public-domain",
  "lineage": [
    "download raw GeoTIFF",
    "warp to EPSG:4326 with 10 GCPs",
    "convert to COG"
  ]
}
````

---

## Best Practices

* Every new dataset must have a **provenance record**.
* If data are uncertain (ambiguous place names, OCR errors), note with a **confidence flag**.
* Keep **audit logs human-readable** for long-term use.
* Prefer **open data sources** (USGS, NOAA, FEMA, Kansas GIS Hub, etc.).

---

## References

* [STAC 1.0.0 Specification](https://stacspec.org/)
* [Master Coder Protocol – Scientific Method Templates]: contentReference[oaicite:4]{index=4}
* [Kansas Frontier Matrix – Design Audit]: contentReference[oaicite:5]{index=5}
* [Data Resource Analysis Report]: contentReference[oaicite:6]{index=6}

---

```
