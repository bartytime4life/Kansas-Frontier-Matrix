# data/raw

Immutable **source payloads** live here — exactly as acquired from upstream providers (no edits, no re-projection). Every file must ship with:
- a `*.sha256` checksum, and
- a compact provenance sidecar `*.src.json`.

This folder is a **landing zone** used by the ingestion pipeline to create reproducible derivatives under `data/processed/**` and `data/cogs/**`. Do **not** modify, clip, reproject, or repackage files in place; any fixups belong in processing scripts with documented steps.

---

## Layout & sidecars

```

data/raw/
├── elevation/
│   ├── ks\_1m\_dem\_2018\_2020.tif               # as-downloaded (if mirroring tiles, store the original bundle/zip)
│   ├── ks\_1m\_dem\_2018\_2020.tif.sha256        # SHA-256 of the raw payload
│   └── ks\_1m\_dem\_2018\_2020.src.json          # compact provenance (see example below)
├── historic\_maps/
│   └── usgs\_topo\_larned\_1894.tif
├── vectors/
│   └── plss\_ks\_2020.zip
└── docs/
└── treaty\_osage\_1825.pdf

````

**Sidecar `*.src.json` (minimal, publication-safe):**
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
````

This mirrors the project principle of **documentation-first + traceability** without leaking pipeline internals into raw storage.

---

## What is allowed here

* **Original** rasters (GeoTIFF/IMG), archives (ZIP/TGZ), tabular/vector sources (SHP/FGDB/GeoPackage), and **primary docs** (PDF/CSV) straight from publishers.
* **No edits**: keep upstream CRS, tiling, compression, nodata as-is. Derivatives must be emitted to `data/processed/**` and cataloged with STAC-like metadata.

---

## Size & storage policy

* Prefer **remote references** (service URLs) when sources are stable and rate-limits allow; mirror locally only what’s required for reproducibility or offline builds.
* Large artifacts should use **Git LFS**/**DVC**; git tracks **checksums + metadata** only.
* Default caps (tune in `Makefile`/CI):

  * Raw file ≤ **8 GB** (single); bundle ≤ **20 GB**
  * Journal supplement bundles ≤ **200 MB** (downsampled visuals; full-res via DOI)

---

## Provenance & checksums

Create SHA-256 and record it in the sidecar:

```bash
shasum -a 256 data/raw/elevation/ks_1m_dem_2018_2020.tif \
  | awk '{print $1}' > data/raw/elevation/ks_1m_dem_2018_2020.tif.sha256
```

Capture minimal **source** fields (who/what/when/where/license/sha) — enough for readers to relocate and verify.

> If license is unclear or conflicting, move the payload to `data/raw/_quarantine/` and resolve before use.

---

## Ingestion → processing (typical flow)

1. **Validate** raw payload (checksum, license, format).
2. **Catalog** via a lightweight **sources JSON** (STAC-like entry used by the app/pipeline).
3. **Derive** COGs/GeoJSON to `data/cogs/**` and `data/processed/**` with full metadata (roles, MIME, checksums).
4. **Publish** compact, publication-ready JSON + CITATION (CFF); limit supplements to checksums + downsampled visuals.

---

## Naming

Use stable slugs:
`<topic>_<year-or-range>[_{region|scale|edition}].<ext>`

Examples:

* `ks_1m_dem_2018_2020.tif`
* `usgs_topo_larned_1894.tif`
* `plss_ks_2020.zip`

---

## Licensing & ethics

* Record **license** verbatim in `*.src.json`.
* For culturally sensitive layers (e.g., sacred sites, oral histories), apply the project’s ethics guardrails; use access controls or spatial/attribute generalization as required.

---

## Quick checks

```bash
# Inspect spatial metadata
gdalinfo data/raw/elevation/ks_1m_dem_2018_2020.tif | sed -n '1,80p'

# Validate GeoTIFF tags minimally
listgeo -no_norm data/raw/elevation/*.tif | head -n 40

# Verify ZIP integrity
unzip -t data/raw/vectors/plss_ks_2020.zip
```

---

## DOs / DON’Ts

* ✅ Keep original bits **immutable**; add sidecars for **provenance + sha256**.
* ✅ Store a compact **pub JSON** only when mirroring in-repo for papers.
* ❌ Don’t reproject/clip/compress here (do it in processing).
* ❌ Don’t commit multi-GB datasets to git without LFS/DVC + checksum entries.

---

## Notes for maintainers

* Ensure `.gitattributes` treats large binaries as **LFS** and prevents auto-merge on binaries.
* `data/raw/**` should be ignored by most linters/formatters; CI should only **verify checksums** and **validate sidecars**.

```
