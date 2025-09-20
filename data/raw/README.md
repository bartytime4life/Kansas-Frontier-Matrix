# data/raw

Immutable **source payloads** live here — exactly as acquired from upstream providers (no edits, no re-projection). Every file must have a sidecar with provenance and a checksum.

This folder is a **landing zone** used by the ingestion pipeline to create reproducible, COG/GeoJSON derivatives under `data/processed/**` and `data/cogs/**`:contentReference[oaicite:0]{index=0}. Do **not** modify, clip, or repackage files in-place; any fixups belong in processing scripts with documented steps:contentReference[oaicite:1]{index=1}.

---

## Layout & sidecars

```

data/raw/
├── elevation/
│   ├── ks\_1m\_dem\_2018\_2020.tif           # as-downloaded (if mirroring service tiles, store zip bundle)
│   ├── ks\_1m\_dem\_2018\_2020.tif.sha256    # SHA-256 of the raw payload
│   └── ks\_1m\_dem\_2018\_2020.src.json      # compact provenance (see schema below)
├── historic\_maps/
│   └── usgs\_topo\_larned\_1894.tif
├── vectors/
│   └── plss\_ks\_2020.zip
└── docs/
└── treaty\_osage\_1825.pdf

````

**Sidecar `*.src.json` (minimal, publication-safe)**:
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

This mirrors the MCP principle of **documentation-first + traceability** without leaking pipeline internals into raw storage.

---

## What is allowed here

* **Original** rasters (GeoTIFF, IMG), archives (ZIP/TGZ), tabular/vector sources (SHP/FGDB/GeoPackage), and **primary docs** (PDF/CSV) straight from publishers.
* **No edits**: keep upstream CRS, tiling, compression, nodata as-is. Derivatives must be emitted to `data/processed/**` and cataloged with STAC-like metadata.

---

## Size & storage policy

* Prefer **remote references** (service URLs) when sources are stable and rate-limits allow; mirror locally only what’s required for reproducibility or offline builds.
* Large artifacts should use DVC/LFS or be archived with a DOI; git tracks **checksums + metadata** only.
* Default caps (tune in Makefile/CI):

  * Raw file ≤ 8 GB (single); bundle ≤ 20 GB
  * Journal supplement bundles ≤ 200 MB (downsampled visuals; full-res via DOI)

---

## Provenance & checksums

Create SHA-256 and record in the sidecar:

```bash
shasum -a 256 data/raw/elevation/ks_1m_dem_2018_2020.tif \
  | awk '{print $1}' > data/raw/elevation/ks_1m_dem_2018_2020.tif.sha256
```

Capture minimal **source** fields (who/what/when/where/license/sha) — enough for readers to relocate and verify, per MCP reproducibility guidance.

---

## Ingestion → processing

Typical flow (scripted in `scripts/` / `Makefile`):

1. **Validate** raw payload (checksum, license, format).
2. **Catalog** via a lightweight **sources JSON** (STAC-like entry used by your app/pipeline).
3. **Derive** COGs/GeoJSON to `data/cogs/**` and `data/processed/**` with full metadata (roles, MIME, checksums).
4. **Publish** compact, publication-ready JSON + CITATION (CFF) and limit supplements to checksums + downsampled visuals.

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

* Record **license** verbatim. If unclear, quarantine in `data/raw/_quarantine/` until resolved.
* For culturally sensitive layers (e.g., sacred sites, oral histories), follow the project’s ethics guardrails; apply access controls or generalization where appropriate.

---

## Quick checks

```bash
# Inspect spatial metadata
gdalinfo data/raw/elevation/ks_1m_dem_2018_2020.tif | sed -n '1,80p'

# Validate GeoTIFF tags minimally
listgeo -no_norm data/raw/elevation/*.tif | head -n 40

# Verify zip integrity
unzip -t data/raw/vectors/plss_ks_2020.zip
```

---

## DOs / DON’Ts

* ✅ Keep original bits **immutable**; add sidecars for **provenance + sha256**.
* ✅ Add a compact **pub JSON** only when mirroring in the repo for papers.
* ❌ Don’t reproject/clip/compress here (do it in processing).
* ❌ Don’t commit multi-GB datasets to git without LFS/DVC + checksum entries.

---

## References

* STAC-like cataloging, COG/GeoJSON derivatives, and viewer auto-discovery
* MCP reproducibility & documentation-first templates (experiments, SOPs, model/data cards)
* Design audit guidance on data source documentation, size control, and public-safe artifacts

```
