<!--
doc_id: NEEDS VERIFICATION
title: Kansas gSSURGO → GeoParquet Ingest Recipe (RAW → WORK → CATALOG)
type: standard
version: v1
status: draft
owners: [@bartytime4life, NEEDS VERIFICATION]
created: 2026-04-01
updated: 2026-04-01
policy_label: public
related: [docs/governance/ROOT_GOVERNANCE.md, docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md]
tags: [kfm, soils, ssurgo, gssurgo, stac, geoparquet, evidence-first]
notes: [Baseline ingest shape for Kansas; external references NEEDS VERIFICATION before publish]
-->

# Kansas gSSURGO → GeoParquet Ingest Recipe

**Purpose:** Minimal, CI‑friendly ingest to fetch USDA gSSURGO (Kansas), flatten MU attributes, validate, emit GeoParquet + STAC, and attach a signed run_receipt for trust‑visible publishing.

**Repo fit:**  
- **Path (PROPOSED):** `pipelines/soils/gssurgo-ks/`  
- **Upstream:** USDA NRCS gSSURGO FGDB (Kansas)  
- **Downstream:** KFM STAC Catalog; governed CATALOG/TRIPLET surfaces

**Status:** experimental · **Owners:** @bartytime4life (fallback) · **Sensitivity:** geoprivacy‑aware · **Badges:** evidence‑first · map‑first

---

## Quick Jumps
- [Scope](#scope) • [Inputs](#inputs) • [Exclusions](#exclusions) • [Directory Tree](#directory-tree) • [Step‑by‑Step](#step-by-step) • [Validations](#minimal-validations) • [STAC](#stac-catalog--items) • [Run Receipt](#run_receipt--signing) • [Automation Prompt](#automation-ai-prompt) • [Checklist](#publish-checklist)

## Scope
This recipe ingests **Kansas gSSURGO** polygons, joins essential MU/COMP/HYDRATE/HYDGRP attributes, writes **OGC GeoParquet v1.x**, performs fail‑closed validations, emits **STAC Item(s)**, and generates a **signed run_receipt**. It follows KFM’s RAW→WORK→CATALOG promotion and evidence obligations.

## Inputs
- SOURCE_URL (Kansas gSSURGO File Geodatabase ZIP) — NEEDS VERIFICATION
- DEST_BUCKET (e.g., `s3://kfm-prod/soils/`)
- SIGN_KEY / CI signer (cosign/Tekton Chains/KMS)

## Exclusions
- Component‑level deep profiles beyond columns listed here
- Non‑Kansas extents
- Rasterized/gridded exports (optional preview COG only)

## Directory Tree (PROPOSED)

```text
pipelines/soils/gssurgo-ks/
├─ Makefile
├─ recipe.sh
├─ env.sample
├─ validate.py
├─ stac_emit.py
├─ schema/
│  └─ geoparquet_schema.json
├─ WORK/
├─ RAW/
└─ CATALOG/
```

---

## Step‑by‑Step

### 1) SOURCE — download + evidence
- Download Kansas gSSURGO FGDB (ZIP) to `RAW/ks_gssurgo.gdb.zip`
- Record: `RAW/source_etag.txt`, `RAW/source_sha256.txt`, retrieval timestamp (ISO‑8601)

### 2) EXTRACT — flatten MU attributes
Extract **MUPOLYGON** and join key tables to single row per MU polygon:

Required columns (PROPOSED canonical):
```
mukey, musym, mapunitname,
component_pct, dominant_comp_pct,
texture_class, om_pct, ph_surface,
hydric_flag, hydgrpd_pct_a, hydgrpd_pct_b, hydgrpd_pct_c, hydgrpd_pct_d,
geometry
```

Implementation options:
- `ogr2ogr` SQL or `pyogrio/geopandas` joins over `MAPUNIT`, `COMPONENT`, `HYDRATE` (hydric), `HYDGRP` (hydrologic group shares)
- Document deterministic rule if retaining component splits; else produce one canonical MU polygon row

### 3) REPROJECT + STANDARDS
- Reproject to **EPSG:4326**
- Optional topology simplification (preserve area/centroid within tolerance)
- Normalize types:
  - `om_pct` 0–100 (float)
  - `ph_surface` 0–14 (float)
  - `texture_class` (controlled SSURGO vocab)
- Compute **spec_hash** = SHA256 of: sorted `mukey→attributes` CSV + `source_etag` + `retrieval_timestamp` → write `RAW/spec_hash.txt`

### 4) GEOARROW / GEOPARQUET
Write **GeoParquet** with column metadata (OGC GeoParquet v1.x):

Schema (PROPOSED):
```
mukey: STRING
musym: STRING
mapunitname: STRING
component_pct: FLOAT
dominant_comp_pct: FLOAT
texture_class: STRING
om_pct: FLOAT
ph_surface: FLOAT
hydric_flag: BOOLEAN
hydgrpd_pct_a/b/c/d: FLOAT
source_uri: STRING
product_version: STRING
last_updated: TIMESTAMP (ISO-8601)
geometry: GEOMETRY(Polygon/MultiPolygon, EPSG:4326)
```

Set sensible row_group sizes and optional zonemaps for scan speed.

### 5) MINIMAL VALIDATIONS
**Fail‑closed** on critical errors.

- **MUKEY completeness:** no NULL `mukey`; every polygon’s `mukey` resolves to MAPUNIT
- **MUKEY uniqueness:** one canonical `mukey→polygon` row or documented tiling rule
- **Ranges:** `om_pct ∈ [0,100]`; `ph_surface ∈ [0,14]`; `component_pct ∈ (0,100]`
- **HYDGRP share check:** `hydgrpd_pct_*` sum ≈ 100 (tolerance ±0.5%)
- **Hydric consistency:** if any COMPONENT is hydric, `hydric_flag == true` (warn on mismatch)
- **Controlled vocab:** `texture_class` maps to SSURGO taxonomic textures

### 6) STAC (CATALOG) — Items
Create a **STAC Catalog + Item(s)** describing the GeoParquet artifact.

`Item.properties` MUST include:
- `kfm:evidence_refs` (source_uri, product_version, last_updated, spec_hash)
- Geometry bbox/centroid; `item.modified = last_updated`
- `assets['geoparquet']` → href (signed URL or registry path)
- Optional preview `assets['cog']`

### 7) RUN_RECEIPT & SIGNING
Emit `run_receipt.json` alongside STAC:

```json
{
  "run_id": "<iso-utc>-kansas-soils-1",
  "runner": "ci/soil-ingest:v1",
  "inputs": [{"uri": "https://.../ks_gssurgo.gdb.zip", "etag": "<etag>"}],
  "spec_hash": "<sha256_hex>",
  "outputs": [{"href": "s3://kfm-prod/soils/kansas-soils.parquet", "sha256": "<sha256>"}],
  "timestamp": "2026-04-01T00:00:00Z",
  "signature": "<cosign-base64-or-rekor-ref>"
}
```

Sign with **cosign** (keyless via Fulcio) or **Tekton Chains**; push to evidence store / Rekor if available.

### 8) EMIT & PUBLISH RULES
- Push GeoParquet to `CATALOG/` (or object store path)
- Push STAC Item to STAC server or static catalog
- Attach `run_receipt` and `spec_hash` to catalog metadata
- **Promote to PUBLISHED only when** Conftest/OPA policy checks pass:
  - MUKEY completeness ✅
  - Hydric consistency ✅
  - `kfm:evidence_refs` present ✅

---

## Quickstart (CLI outline)

```bash
make init   # install pyogrio, geopandas, pyarrow, geoparquet/cli, stactools, conftest, cosign

# 1) Download + evidence
./recipe.sh fetch "$SOURCE_URL" RAW/

# 2) Extract + flatten
./recipe.sh extract RAW/ks_gssurgo.gdb.zip WORK/flatten.parquet

# 3) Canonicalize + spec_hash
./recipe.sh standardize WORK/flatten.parquet WORK/flatten_std.parquet RAW/spec_hash.txt

# 4) Validate (fail-closed)
python validate.py WORK/flatten_std.parquet

# 5) Emit GeoParquet + STAC
./recipe.sh emit WORK/flatten_std.parquet CATALOG/kansas-soils.parquet
python stac_emit.py --asset CATALOG/kansas-soils.parquet --out CATALOG/stac/

# 6) Sign run_receipt
cosign sign-blob --output-signature CATALOG/run_receipt.sig CATALOG/run_receipt.json
```

---

## Automation‑AI Prompt

> You are a reproducible‑data operator. Given SOURCE_URL, DEST_BUCKET, and SIGN_KEY, run: (1) download SOURCE_URL → compute etag+sha256; (2) extract MUPOLYGON+join HYDRATE/HYDGRP tables; (3) canonicalize attributes and compute spec_hash; (4) write GeoParquet to DEST_BUCKET and generate STAC Item with kfm:evidence_refs; (5) produce run_receipt JSON and sign it with cosign (or Tekton Chains) and return STAC Item URL + run_receipt URL. **Fail and exit non‑zero** if mukey completeness OR hydric/hydgrp validation fails.

---

## Publish Checklist

- [ ] Owners, paths, and SOURCE_URL **CONFIRMED**
- [ ] GeoParquet validates (schema + metadata)  
- [ ] Validations all pass; Conftest policy **PASS**
- [ ] STAC Item fields present; `kfm:evidence_refs` complete  
- [ ] `run_receipt.json` signed and stored; `spec_hash.txt` attached  
- [ ] README updated with exact artifact hrefs and dates
- [ ] Exposure class reviewed (public‑safe vs steward‑only)

---

## Appendix: Pseudocode Snippets

**Flatten via pyogrio/GeoPandas (sketch):**
```python
import pyogrio, geopandas as gpd, pandas as pd

gdb = "RAW/ks_gssurgo.gdb"
mu = gpd.read_file(gdb, layer="MUPOLYGON")
mapunit = pd.read_parquet("WORK/MAPUNIT.parquet")  # or read from FGDB tables
component = pd.read_parquet("WORK/COMPONENT.parquet")
hydrate = pd.read_parquet("WORK/HYDRATE.parquet")
hydgrp = pd.read_parquet("WORK/HYDGRP.parquet")

# joins + aggregation to required columns...
# write WORK/flatten_std.parquet with metadata
```

**Conftest/OPA gate (sketch Rego):**
```rego
package kfm.soils

deny[msg] {
  input.metrics.mukey_missing > 0
  msg := sprintf("MUKEY completeness failed: %v missing", [input.metrics.mukey_missing])
}

deny[msg] {
  abs(input.metrics.hydgrp_sum_delta) > 0.5
  msg := "HYDGRP percentages not ~100%"
}
```