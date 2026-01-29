# 🧾 Known Issues — Census Sources (External)

![Status](https://img.shields.io/badge/status-living%20doc-blue)
![Scope](https://img.shields.io/badge/scope-census%20sources-6f42c1)
![Data](https://img.shields.io/badge/data-external-lightgrey)
![Governance](https://img.shields.io/badge/governance-fail%20closed-critical)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-brightgreen)

> According to a document from **2024**, Census TIGER boundaries (e.g., blocks) can be imported as vector features (e.g., `TIGER/2010/Blocks`), and **Shapefiles require multiple component files**—including a `.prj` that describes the **map projection**—which is a common failure point in Census data workflows. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}:contentReference[oaicite:2]{index=2}

---

## 🧭 Quick links

- [📁 Where this file lives](#-where-this-file-lives)
- [🧱 KFM governance expectations](#-kfm-governance-expectations)
- [🚦 Severity legend](#-severity-legend)
- [🧨 Known issue index](#-known-issue-index)
- [✅ Pre-ingest checklist](#-pre-ingest-checklist)
- [🧩 New issue template](#-new-issue-template)
- [📚 Project sources consulted](#-project-sources-consulted)

---

## 📁 Where this file lives

```text
🗂️ data/
  🌐 external/
    🗺️ mappings/
      🧮 census/
        📦 sources/
          📄 known_issues.md   👈 you are here
```

This document tracks **known issues** found when acquiring, importing, normalizing, and joining Census-related sources (geometry + attributes) in the KFM pipeline.

---

## 🧱 KFM governance expectations

### Canonical “data moves” order (don’t skip steps)
KFM’s data pipeline is intentionally staged so issues can be isolated early (and documented before they propagate):

```mermaid
flowchart LR
  raw["🧊 raw (immutable snapshot)"] --> processed["🧼 processed (cleaned/standardized)"] --> catalog["📇 catalog + 🔗 prov"] --> db["🗄️ database"] --> api["🧩 API"] --> ui["🗺️ UI"]
```

KFM explicitly defines a canonical pipeline order: **Raw → Processed → Catalog/Prov → Database → API → UI**. :contentReference[oaicite:3]{index=3}

### “Fail closed” on undocumented or unprovenanced data ✅🚫
- KFM is explicit that **data cannot enter the system without documentation**, and CI should reject missing metadata/provenance. :contentReference[oaicite:4]{index=4}
- Expected metadata alignment includes **STAC + DCAT + W3C PROV**, with examples like `census_1900.prov.json`. :contentReference[oaicite:5]{index=5}
- The Markdown guide explicitly calls for **STAC/DCAT/PROV alignment** and cross-references between them. :contentReference[oaicite:6]{index=6}

### Prefer standards for interchange 🧩
GIS benefits from standard formats, reference systems, and metadata to enable storage/interchange. 

---

## 🚦 Severity legend

- 🟥 **High**: produces wrong joins, wrong maps, or breaks downstream; must fix or explicitly quarantine
- 🟧 **Medium**: risky/ambiguous; can proceed only with explicit documentation + validation
- 🟨 **Low**: nuisance/perf/ergonomics; track but not blocking

---

## 🧨 Known issue index

| ID | Severity | Category | Short name |
|---:|:-------:|:--|:--|
| CEN-001 | 🟥 | 🗺️ Geography | Boundary “vintage” mismatch |
| CEN-010 | 🟥 | 🔢 IDs/Keys | FIPS/GEOID leading zeros lost |
| CEN-020 | 🟧 | 🎨 Cartography | Choropleth totals vs rates / aggregation artifacts |
| CEN-030 | 🟥 | 🧭 CRS/Projection | Missing/incorrect CRS or `.prj` |
| CEN-031 | 🟧 | 🧭 CRS/Projection | Coordinate order / CRS confusion (GeoJSON/CSV) |
| CEN-040 | 🟧 | 📦 Packaging | Shapefile sidecar files missing |
| CEN-041 | 🟧 | 🧪 Geometry | Invalid geometries break spatial ops |
| CEN-050 | 🟥 | ⚙️ Governance | Missing STAC/DCAT/PROV (fail closed) |
| CEN-060 | 🟧 | 🧮 Comparability | Non-comparable populations/variables/sources |
| CEN-070 | 🟥 | 🔒 Privacy | Attempting address-level mapping / disclosure risk |
| CEN-080 | 🟨 | ⚡ Performance | Block-scale data too heavy without tiling/simplification |

---

## 🗺️ Geography & vintage issues

### CEN-001 — Boundary “vintage” mismatch 🟥
**Symptoms**
- Attribute joins “work” but spatial overlays don’t align (odd slivers, offsets, low join coverage).
- Aggregations “look” different between runs even when using the same query logic.

**Root cause**
- Mixing different **boundary vintages** (e.g., 2010 blocks with later tracts/counties).
- Mixing local TIGER/Line downloads with another boundary source without explicit crosswalk.

**Mitigation**
- Decide (and document) the “analysis vintage” per dataset before any joins.
- If using Earth Engine TIGER blocks, document the dataset ID and its implied vintage (e.g., `TIGER/2010/Blocks`). :contentReference[oaicite:8]{index=8}

**Detection / tests**
- Compare expected ID lengths/patterns (see CEN-010).
- Spatial sanity check: overlay on a basemap and visually inspect known landmarks.
- Quant check: compute spatial-join match rate and flag if below threshold.

---

## 🔢 IDs & keys issues

### CEN-010 — FIPS/GEOID leading zeros lost 🟥
**Symptoms**
- Joins drop rows unexpectedly.
- IDs “look right” in spreadsheets, but differ in code (e.g., `2001` vs `02001` style problems).

**Root cause**
- IDs cast to integer somewhere (CSV import, pandas dtype inference, DB schema mismatch).

**Mitigation**
- Treat FIPS/GEOID as **strings**, preserve width, and pad with zeros where required.
- Normalize IDs in `processed/` outputs (never rely on “whatever the loader did”).

**Detection / tests**
- Assert fixed length for expected geographies (state/county/tract/block group/block).
- Fail pipeline on mixed-length IDs in the same column.

---

## 🎨 Cartography & aggregation issues

### CEN-020 — Choropleth totals vs rates / aggregation artifacts 🟧
**Symptoms**
- A choropleth map visually “lies” (big counties dominate) or implies a continuous surface.
- Users interpret the map as representing a phenomenon rather than the structure of the data.

**Root cause**
- Mapping totals instead of normalized rates/densities.
- Aggregation choices change the phenomenon being described (“data ≠ phenomenon”).

**Notes**
- Mapping aggregated Census values into area units is inherently interpretive; the map can show the structure of the **data**, not necessarily the underlying phenomenon. :contentReference[oaicite:9]{index=9}

**Mitigation**
- Prefer per-capita / density measures for choropleths unless totals are explicitly required.
- Document the denominator and aggregation rule in metadata/provenance.

**Detection / tests**
- Automated check: if choropleth uses a “count” field, require a justification note in metadata.
- QA check: side-by-side map of totals vs rates.

---

## 🧭 CRS / projection issues

### CEN-030 — Missing/incorrect CRS or `.prj` 🟥
**Symptoms**
- Layers appear in the wrong place (e.g., off the planet / in the ocean).
- Spatial joins return ~0 matches.
- Reprojection errors or silently incorrect geometry.

**Root cause**
- Shapefile missing `.prj` or wrong projection assumptions.
- Loader assumes CRS incorrectly.
- `.prj` exists but doesn’t match actual coordinates.

**Evidence**
- Shapefiles require multiple files, and the `.prj` describes the map projection; you need all four key components to create a valid feature asset. :contentReference[oaicite:10]{index=10}
- It’s common to encounter data without a `.prj`; without it, “the computer doesn’t know where to project the data.” :contentReference[oaicite:11]{index=11}

**Mitigation**
- Require CRS explicitly at ingest time.
- If `.prj` missing: quarantine in `raw/` and create a remediation note before any join.

**Detection / tests**
- Pipeline check: fail if shapefile is missing `.prj` (unless explicitly waived in metadata).
- Bounds sanity: ensure geometries fall within expected region extent (e.g., Kansas workflow expects KS extents).

---

### CEN-031 — Coordinate order / CRS confusion (GeoJSON/CSV) 🟧
**Symptoms**
- Points appear far away (often “in the ocean”).
- CSV point import doesn’t match polygons; join coverage is near zero.

**Root cause**
- Coordinate order swapped (lon/lat vs lat/lon).
- No CRS declared for CSV points.
- GeoJSON/other files stored in a CRS that downstream tools interpret as WGS84.

**Evidence**
- When importing GeoJSON, “x is longitude and y is latitude”—swapping them puts data in the ocean. :contentReference[oaicite:12]{index=12}
- Missing coordinate system on CSV point import can lead to “zero matching locations.” :contentReference[oaicite:13]{index=13}

**Mitigation**
- Require explicit CRS metadata for any point source.
- Run coordinate sanity checks on first N points.

**Detection / tests**
- Validate coordinate ranges (lon ∈ [-180,180], lat ∈ [-90,90]) and expected bounding box.
- Plot a quick preview map in CI artifact.

---

## 📦 Packaging issues

### CEN-040 — Shapefile sidecar files missing 🟧
**Symptoms**
- Geometry loads but attributes are missing.
- Loader fails intermittently on different machines.

**Root cause**
- Only `.shp` is present; missing `.dbf`/`.shx`/`.prj` (or wrong versions).
- Zipped download unpacked incorrectly.

**Evidence**
- Shapefile components: `.shp` (geometry), `.dbf` (attributes), `.shx` (index), `.prj` (projection). “You will need to load all four files.” :contentReference[oaicite:14]{index=14}

**Mitigation**
- Treat shapefile as a **bundle**, not a file.
- Store as a single archived artifact in `raw/` (and verify checksum).

**Detection / tests**
- File presence check: fail if any required sidecar is missing.

---

## 🧪 Geometry validity & spatial operations

### CEN-041 — Invalid geometries break spatial operations 🟧
**Symptoms**
- Spatial joins throw errors or return inconsistent results.
- Some polygons fail to render.

**Root cause**
- Self-intersections, ring direction issues, invalid multipolygons.

**Evidence**
- PostGIS validity checks exist (e.g., `ST_IsValid`, `ST_IsValidReason`, `ST_IsValidDetail`) and invalid geometry can cause errors/no results. :contentReference[oaicite:15]{index=15}

**Mitigation**
- Validate geometries before loading to DB or producing tiles.
- Repair in `processed/` and keep the original invalid artifacts in `raw/`.

**Detection / tests**
- `is_valid` checks (geopandas) or `ST_IsValid` checks (PostGIS) as a gating step.

---

## ⚙️ Governance / metadata issues

### CEN-050 — Missing STAC/DCAT/PROV (fail closed) 🟥
**Symptoms**
- Data appears in DB/tiles but cannot be traced back to raw files or license constraints.
- Consumers can’t reproduce results.

**Root cause**
- Skipping catalog/provenance creation.
- Missing linkage between dataset, process run, and outputs.

**Evidence**
- KFM requires STAC/DCAT/PROV alignment and expects provenance artifacts (example: `census_1900.prov.json`). :contentReference[oaicite:16]{index=16}:contentReference[oaicite:17]{index=17}

**Mitigation**
- Treat missing metadata/prov as a **build failure** (default).
- Add a “data acceptance gate” that checks:
  - License present
  - STAC item/collection exists
  - DCAT dataset record exists
  - PROV bundle exists and references raw inputs + processing code version

**Detection / tests**
- CI: reject merges that add/modify sources without updated catalog/prov. :contentReference[oaicite:18]{index=18}

---

## 🧮 Statistical comparability issues

### CEN-060 — Non-comparable populations/variables/sources 🟧
**Symptoms**
- Trend charts show abrupt “changes” that are actually definitional changes.
- Comparisons across time/regions give misleading conclusions.

**Root cause**
- Comparing apples to oranges:
  - Different populations
  - Different variable definitions
  - Different data sources / collection methods

**Evidence**
- Comparisons require comparable populations, variables, and sources; often you must standardize (e.g., adjusting for inflation in monetary variables). :contentReference[oaicite:19]{index=19}

**Mitigation**
- Maintain a “variable dictionary” per source vintage.
- For every derived metric, record:
  - Definition
  - Universe/population
  - Notes on known breaks in series
  - Standardization performed (and how)

**Detection / tests**
- Require a metadata field: `comparability_notes` when joining across vintages or mixing ACS/decennial.

---

## 🔒 Privacy & disclosure issues

### CEN-070 — Attempting address-level mapping / disclosure risk 🟥
**Symptoms**
- A workflow attempts to map point-level residences / precise household locations.
- A dataset includes overly granular location fields that could be identifying.

**Root cause**
- Misunderstanding what is publicly releasable vs confidential.

**Evidence**
- The Census counts people at individual addresses, but you can’t map at that resolution; “the Census Bureau keeps this resolution secret to protect privacy.” :contentReference[oaicite:20]{index=20}

**Mitigation**
- Enforce minimum geography policy for public-facing maps (e.g., block group+ unless explicitly cleared).
- Strip or hash sensitive quasi-identifiers during processing.
- Add a privacy review step for any “point-like” population data.

**Detection / tests**
- Scan schemas for fields like exact address, lat/lon of households, or other direct identifiers.
- Block publication of point layers unless explicitly flagged as non-sensitive.

---

## ⚡ Performance / scale issues

### CEN-080 — Block-scale data too heavy without tiling/simplification 🟨
**Symptoms**
- Extremely slow processing, huge outputs, big tile sizes.
- UI performance issues, timeouts.

**Root cause**
- Census blocks are extremely numerous; full-resolution geometries are heavy.

**Mitigation**
- Clip to AOI early.
- Use multiple resolutions (raw full, processed simplified).
- Tile intelligently; don’t ship national-scale blocks to a Kansas-only workflow.

**Detection / tests**
- Size budgets for artifacts (e.g., max GeoJSON size, max tile payload).
- Benchmark pipeline step times.

---

## ✅ Pre-ingest checklist

> Use this checklist before anything leaves `raw/` and becomes “trusted” in `processed/`.

- [ ] **Source snapshot is immutable** (raw zip/tar kept, checksum recorded)
- [ ] **All shapefile components** present (`.shp`, `.dbf`, `.shx`, `.prj`) :contentReference[oaicite:21]{index=21}
- [ ] CRS is explicit and correct (or quarantined) :contentReference[oaicite:22]{index=22}
- [ ] ID columns are strings; leading zeros preserved (CEN-010)
- [ ] Geometry validity check passes (or repairs documented) :contentReference[oaicite:23]{index=23}
- [ ] Vintage is explicit (e.g., 2010 vs other), documented in metadata (CEN-001) :contentReference[oaicite:24]{index=24}
- [ ] **STAC + DCAT + PROV** are created/updated and cross-linked :contentReference[oaicite:25]{index=25}:contentReference[oaicite:26]{index=26}
- [ ] Privacy review for any point-like population data (CEN-070) :contentReference[oaicite:27]{index=27}
- [ ] Comparability notes added for any cross-vintage comparisons (CEN-060) :contentReference[oaicite:28]{index=28}

---

## 🧩 New issue template

<details>
<summary><strong>Click to expand: “Known Issue” entry template</strong></summary>

```yaml
id: CEN-XXX
title: "Short, searchable title"
severity: high | medium | low
category: geography | ids | projection | packaging | geometry | governance | comparability | privacy | performance

symptoms:
  - "What someone sees when it breaks"

root_cause:
  - "Why it happens (technical + process)"

impact:
  - "Downstream consequences (joins, maps, stats, privacy, reproducibility)"

mitigation:
  - "How we fix or safely proceed"
  - "What to document in metadata/prov"

detection_tests:
  - "Automated checks"
  - "Manual QA steps"

provenance_notes:
  - "Where to record the decision (STAC/DCAT/PROV fields, run ids, etc.)"

links:
  - "Relative path to related mapping spec or schema doc"
```

</details>

---

## 📚 Project sources consulted

- KFM pipeline order and “fail closed” expectations :contentReference[oaicite:29]{index=29}:contentReference[oaicite:30]{index=30}
- KFM STAC/DCAT/PROV alignment and example provenance artifacts :contentReference[oaicite:31]{index=31}:contentReference[oaicite:32]{index=32}
- TIGER blocks in Earth Engine (`TIGER/2010/Blocks`) and shapefile component requirements (`.shp`, `.dbf`, `.shx`, `.prj`) :contentReference[oaicite:33]{index=33}:contentReference[oaicite:34]{index=34}
- Projection pitfalls: missing `.prj`, coordinate order issues in GeoJSON/CSV :contentReference[oaicite:35]{index=35}
- Geometry validity checks in PostGIS workflows :contentReference[oaicite:36]{index=36}
- Mapping/privacy: address-level secrecy to protect privacy :contentReference[oaicite:37]{index=37}
- Comparability and standardization guidance for analysis :contentReference[oaicite:38]{index=38}

