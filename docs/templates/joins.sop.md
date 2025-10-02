<div align="center">

# 🔗 Joins SOP — Reproducible Merges/Overlays  
`docs/templates/joins.sop.md`

**Scope:** Define a **reproducible procedure** for exploratory joins in `data/work/joins/` → promotion into canonical directories with **validation, provenance, STAC registration**, and optional **graph ingestion**.

**Audience:** Contributors performing spatial joins, overlays, dissolves, or schema merges (e.g., treaties × counties, flood rasters × landcover, OCR entities × features).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)
[![Coverage](https://codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix/branch/main/graph/badge.svg)](https://codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)
[![STAC](https://img.shields.io/badge/STAC-1.0.0-blue)](https://stacspec.org)
[![Ontology](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20+%20OWL--Time-purple)](https://www.cidoc-crm.org/)
[![Simulation](https://img.shields.io/badge/Simulation-NASA--grade-green)](./experiment.md)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

</div>


</div>

---

## 🧭 Table of Contents

* [✅ Outcomes](#-outcomes)
* [🗺️ Flow (at a glance)](#️-flow-at-a-glance)
* [0) Prereqs](#0-prereqs)
* [1) Naming & Layout](#1-naming--layout)
* [2) Reprojection (to EPSG:4326)](#2-reprojection-to-epsg4326)
* [3) Run the Join / Overlay](#3-run-the-join--overlay)
* [4) Schema Standardization](#4-schema-standardization)
* [5) QA / Validation](#5-qa--validation)
* [6) Promote (Directories & Files)](#6-promote-directory--files)
* [7) Provenance & Checksums](#7-provenance--checksums)
* [8) STAC Item](#8-stac-item)
* [9) Optional: Graph Ingestion (Neo4j)](#9-optional-graph-ingestion-neo4j)
* [10) Makefile Targets (suggested)](#10-makefile-targets-suggested)
* [11) CI Integration](#11-ci-integration)
* [12) Rollback](#12-rollback)
* [13) Checklist (MCP)](#13-checklist-mcp)
* [14) Examples](#14-examples)
* [↔️ Related SOPs & Docs](#️-related-sops--docs)

---

## ✅ Outcomes

* Clean, standardized join artifacts promoted to:

  * `data/processed/` (vectors/rasters ready for analysis)
  * `data/cogs/` (COGs for rasters)
  * `data/derivatives/` (final composites/indices)
* STAC 1.0.0 Items created/updated
* Provenance + checksums emitted
* **Optional:** Neo4j ingestion (entities/relationships materialized)

> 🧪 **MCP Principle:** Every promoted artifact is auditable, reproducible, and has traceable lineage.

---

## 🗺️ Flow (at a glance)

```mermaid
flowchart TD
  A["Exploratory joins\n(data/work/joins)"] --> B["Standardize CRS & schema"]
  B --> C["QA: geometry, topology, attributes"]
  C --> D["Promote → data/processed or data/cogs or data/derivatives"]
  D --> E["Emit _meta.json + .sha256"]
  E --> F["Create STAC Item(s)"]
  F --> G["Optional: Graph ingestion (Neo4j)"]
```

---

## 0) Prereqs

* **CRS standard:** EPSG:4326 (WGS84) — reproject all inputs before joining.
* **Geometry types:** homogeneous per output (`MultiPolygon`, `MultiLineString`, etc.).
* **Attributes:** `snake_case`, ASCII-only, deterministic order.
* **Data hygiene:** no PII; license compatible; minimal required metadata available.

> 💡 *Tip:* Keep the **original raw** immutable under `data/raw/**`. All experiments live in `data/work/joins/`.

---

## 1) Naming & Layout

**Join trial (working):**

```
data/work/joins/<slug>_trial.geojson
data/work/joins/<slug>_trial.tif
```

**Promoted (final):**

```
data/processed/<theme>/<slug>.geojson
data/cogs/<theme>/<slug>.tif
data/derivatives/<theme>/<slug>.{geojson|tif}
```

**Metadata & checksums:**

```
data/processed/<theme>/<slug>/_meta.json
data/processed/<theme>/<slug>/<artifact>.<ext>.sha256
```

**Slug pattern:**
`<lhs>_x_<rhs>[_clip|_union|_dissolve][_YYYY|YYYY-YYYY]`

**Examples:**

* `treaties_x_counties_1854.geojson`
* `floods_union_1990-2000.tif`
* `treaty1854_x_ocr_entities.geojson`

---

## 2) Reprojection (to EPSG:4326)

```bash
# Vector
ogr2ogr -t_srs EPSG:4326 \
  data/work/joins/counties_4326.geojson data/raw/counties/counties.shp

# Raster (warp)
gdalwarp -t_srs EPSG:4326 \
  data/raw/floods/flood_1993.tif data/work/joins/flood_1993_4326.tif
```

---

## 3) Run the Join / Overlay

### 3.1 SQL-style overlay (OGR Virtual SQL; GPKG/SQLite or PG)

```bash
ogr2ogr -f GeoJSON data/work/joins/treaties_x_counties_trial.geojson \
  counties_4326.gpkg \
  -dialect SQLITE \
  -sql "SELECT t.id AS treaty_id, c.name AS county,
               ST_Intersection(t.geometry, c.geometry) AS geometry
        FROM treaties_4326 t
        JOIN counties_4326 c
        ON ST_Intersects(t.geometry, c.geometry)"
```

### 3.2 Attribute join (CSV → vector)

```bash
ogr2ogr -f GeoJSON data/work/joins/railroads_x_attrs_trial.geojson \
  data/raw/railroads/railroads_4326.geojson \
  -sql "SELECT r.*, a.speed_limit
        FROM 'railroads_4326' r
        LEFT JOIN 'railroads_attrs'.'attrs.csv' a
        ON r.segment_id = a.segment_id"
```

### 3.3 Raster merge (trial)

```bash
gdal_merge.py -o data/work/joins/floods_union_trial.tif data/raw/floods/*_4326.tif
```

---

## 4) Schema Standardization

* **Columns:** `snake_case`, deterministic order, minimal documented attributes.
* **Common fields:**
  `treaty_id, county, overlap_area_km2, overlap_pct, source_lhs, source_rhs, period, license, confidence`
* **Compute derived fields** (area, length, % overlap) post-join:

```bash
# Example: compute area in km² (requires PostGIS/SQLite or geopandas)
python scripts/add_area_km2.py \
  data/work/joins/treaties_x_counties_trial.geojson
```

---

## 5) QA / Validation

### 5.1 Geometry & topology

```bash
# Fix invalid geometries
ogr2ogr -f GeoJSON data/work/joins/<slug>_fixed.geojson \
  data/work/joins/<slug>_trial.geojson -makevalid

# Spot-check layer
ogrinfo data/work/joins/<slug>_fixed.geojson -al -so
```

### 5.2 Attribute checks

* No duplicate columns, consistent types
* No unexpected nulls in join keys
* Enumerations respected (if applicable)

### 5.3 CRS and extent

```bash
ogrinfo data/work/joins/<slug>_fixed.geojson -al -so | grep "EPSG:4326"
```

---

## 6) Promote (Directory & Files)

* **Vector (analysis-ready):** `data/processed/<theme>/<slug>.geojson`
* **Raster (optimized):** convert to **COG** → `data/cogs/<theme>/<slug>.tif`
* **Final composites/indices:** `data/derivatives/<theme>/<slug>.*`

**COG conversion**

```bash
rio cogeo create data/work/joins/floods_union_trial.tif \
  data/cogs/hazards/floods_union_1990-2000.tif \
  --overview-level=5 --web-optimized
```

**Move vector**

```bash
mkdir -p data/processed/land/treaties_x_counties_1854
mv data/work/joins/treaties_x_counties_trial_fixed.geojson \
   data/processed/land/treaties_x_counties_1854/treaties_x_counties_1854.geojson
```

---

## 7) Provenance & Checksums

**Provenance (`_meta.json`)**

```json
{
  "id": "treaties_x_counties_1854",
  "title": "Treaties × Counties (1854) — Overlaps",
  "source_lhs": "data/raw/treaties/treaties_1854.geojson",
  "source_rhs": "data/raw/counties/counties.gpkg",
  "commands": [
    "ogr2ogr -t_srs EPSG:4326 ...",
    "ogr2ogr -dialect SQLITE -sql 'SELECT ... ST_Intersection ...'"
  ],
  "crs": "EPSG:4326",
  "created": "2025-10-01T19:00:00Z",
  "stats": { "features": 312, "total_overlap_km2": 12437.12 },
  "versions": { "gdal": "3.8.x", "ogr": "3.8.x", "python": "3.11" },
  "confidence": 0.92,
  "license": "Public Domain",
  "notes": "Exploratory overlay promoted after QA; no invalid geometry."
}
```

**Checksums**

```bash
shasum -a 256 \
  data/processed/land/treaties_x_counties_1854/treaties_x_counties_1854.geojson \
  > data/processed/land/treaties_x_counties_1854/treaties_x_counties_1854.geojson.sha256
```

---

## 8) STAC Item

**Item path:** `stac/items/<collection>/<id>.json`

**Minimal template:**

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "treaties_x_counties_1854",
  "properties": {
    "datetime": "1854-01-01T00:00:00Z",
    "start_datetime": "1854-01-01T00:00:00Z",
    "end_datetime": "1854-12-31T23:59:59Z",
    "kfm:confidence": 0.92,
    "kfm:source_lhs": "treaties_1854",
    "kfm:source_rhs": "counties"
  },
  "geometry": { "type": "Polygon", "coordinates": [] },
  "bbox": [ -102.05, 36.99, -94.59, 40.00 ],
  "assets": {
    "data": {
      "href": "../../data/processed/land/treaties_x_counties_1854/treaties_x_counties_1854.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    },
    "provenance": {
      "href": "../../data/processed/land/treaties_x_counties_1854/_meta.json",
      "type": "application/json",
      "roles": ["metadata"]
    }
  },
  "links": [],
  "collection": "land"
}
```

**Validate STAC**

```bash
make stac-validate
```

---

## 9) Optional: Graph Ingestion (Neo4j)

**Goal:** Attach relationships derived from the join (e.g., treaty **AFFECTS** county).

**Cypher sketch**

```cypher
UNWIND $records AS r
MERGE (c:Place {name: r.county, type: "county"})
MERGE (t:Treaty {id: r.treaty_id})
MERGE (t)-[rel:AFFECTS {year: 1854}]->(c)
SET rel.overlap_km2 = r.overlap_km2,
    rel.overlap_pct = r.overlap_pct,
    rel.confidence = r.confidence,
    rel.provenance = r.provenance_uri;
```

> 🧩 **Ontology:** Prefer CIDOC CRM classes for events/documents/places; use OWL-Time for intervals.

---

## 10) Makefile Targets (suggested)

```makefile
# Standardize inputs
joins-standardize:
	ogr2ogr -t_srs EPSG:4326 data/work/joins/$(LHS)_4326.$(LEXT) data/raw/$(LHS).$(LEXT)
	ogr2ogr -t_srs EPSG:4326 data/work/joins/$(RHS)_4326.$(REXT) data/raw/$(RHS).$(REXT)

# Run join (user-supplied SQL via $(SQL))
joins-run:
	ogr2ogr -f GeoJSON data/work/joins/$(SLUG)_trial.geojson data/work/joins/ \
	  -dialect SQLITE -sql "$(SQL)"

# QA
joins-qa:
	ogr2ogr -f GeoJSON data/work/joins/$(SLUG)_fixed.geojson \
		data/work/joins/$(SLUG)_trial.geojson -makevalid

# Promote
joins-promote:
	mkdir -p data/processed/$(THEME)/$(SLUG)
	mv data/work/joins/$(SLUG)_fixed.geojson \
	   data/processed/$(THEME)/$(SLUG)/$(SLUG).geojson

# Provenance & checksum
joins-prov:
	python scripts/write_meta.py data/processed/$(THEME)/$(SLUG) $(SLUG)
	shasum -a 256 data/processed/$(THEME)/$(SLUG)/$(SLUG).geojson \
	  > data/processed/$(THEME)/$(SLUG)/$(SLUG).geojson.sha256

# STAC
joins-stac:
	python scripts/write_stac_item.py $(SLUG) $(THEME)

# Clean
clean-joins:
	rm -rf data/work/joins/*
```

---

## 11) CI Integration

* Lint `*.geojson` & JSON syntax
* Validate STAC Items
* Enforce checksums (`.sha256`)
* Require `_meta.json` for promoted artifacts
* Optional: run `ogrinfo -al -so` and report feature counts & CRS

---

## 12) Rollback

* Revert commit that promoted artifact + STAC
* Re-run `clean-joins`
* Restore last-known-good from Git or STAC
* Document rollback in `_meta.json` (`rollback_of`, `reason`)

---

## 13) Checklist (MCP)

* [ ] Inputs reprojected to EPSG:4326
* [ ] Join documented (commands copied to `_meta.json`)
* [ ] Geometry valid; attributes standardized
* [ ] Promoted to correct directory
* [ ] `_meta.json` includes stats/versions/commands
* [ ] `.sha256` created per artifact
* [ ] STAC Item created/updated → **passes** validation
* [ ] (Optional) Graph edges/nodes ingested
* [ ] `data/work/joins/` cleaned

---

## 14) Examples

**Treaties × Counties (1854)**

* Output: `data/processed/land/treaties_x_counties_1854/treaties_x_counties_1854.geojson`
* Fields: `treaty_id, county, overlap_km2, overlap_pct, confidence`
* Confidence mapping: `>0.9 high`, `0.7–0.9 medium`, `<0.7 low`

**Floods union (1990–2000)**

* Output COG: `data/cogs/hazards/floods_union_1990-2000.tif`
* `_meta.json` includes list of input rasters & merge operation

---

## ↔️ Related SOPs & Docs

* **Data lifecycle (README):** `data/README.md`
* **Scratch SOP:** `docs/templates/scratch.experiment.md` (optional)
* **Staging SOP:** `docs/templates/staging.sop.md` (optional)
* **OCR SOP:** `docs/templates/ocr.sop.md` (optional)
* **Model/Experiment template:** `docs/templates/experiment.md`
* **Architecture:** `docs/architecture.md` (ETL → STAC → Neo4j → API → Web)

---

**End of SOP** 🚀
