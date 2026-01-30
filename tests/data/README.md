# 🧪 `tests/data/` — Test Fixtures & Sample Datasets

![Fixtures](https://img.shields.io/badge/tests-fixtures-2ea44f) ![Deterministic](https://img.shields.io/badge/deterministic-yes-blue) ![Provenance](https://img.shields.io/badge/provenance-PROV%20ready-purple)

This folder contains **small, deterministic, documented** datasets used by automated tests (unit ✅, integration 🔁, regression 🧷). It exists so tests don’t depend on the network, production databases, or “whatever data happens to be on a dev machine”.

---

## 🎯 Goals (what belongs here)

- **Minimal**: smallest data that still reproduces the behavior/bug.
- **Deterministic**: stable ordering, stable randomness (seeded), stable floating-point expectations.
- **Documented**: every fixture has a short “what/why/how” + provenance + license.
- **Portable**: tests should pass on CI without special accounts or external services.
- **Aligned with KFM’s canonical pipeline**: _Raw → Processed → Catalog/Prov → Database → API → UI_ (tests mirror this, even in miniature).  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 🚫 Non-goals (what should NOT go here)

- Large rasters / huge exports / multi-GB dumps (use DVC or download-on-demand harnesses).  [oai_citation:1‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)  
- Private, sensitive, or licensed-restricted data (no “just for testing” exceptions).
- Fixtures that require “optional stopping” (tweaking data until tests pass) — instead, fix the code or re-generate fixtures with a repeatable script.  [oai_citation:2‡Understanding Statistics & Experimental Design.pdf](sediment://file_0000000038e0722f8ee76e6a371bf703)

---

## 🗂️ Recommended layout (keep it boring & predictable)

> If your fixture set grows beyond “a couple files”, make it a **named package folder** with sidecars.

```text
tests/data/
├── README.md                 # you are here 🙂
├── manifest.yaml             # optional: quick index of fixture packages
├── licenses/                 # optional: bundled license texts for 3rd-party data
│   └── <source>-LICENSE.txt
├── fixtures/
│   ├── <fixture_name>/
│   │   ├── raw/              # “as acquired” tiny input(s)
│   │   ├── processed/        # expected transform outputs
│   │   ├── catalog/          # STAC/DCAT-like metadata (small + local)
│   │   ├── provenance/       # W3C PROV lineage docs (JSON recommended)
│   │   ├── goldens/          # expected outputs for regression tests
│   │   └── NOTES.md          # ultra-short human notes (optional)
│   └── ...
└── tmp/                      # (gitignored) scratch outputs during tests
```

This mirrors the project’s “**no data enters without documentation**” stance.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📦 Fixture “package” contract (required sidecars)

For each fixture package folder (`tests/data/fixtures/<fixture_name>/`):

| File/Folder | Required? | Purpose |
|---|---:|---|
| `raw/` | ✅ | Minimal inputs (CSV/GeoJSON/TIF/etc.) |
| `processed/` | ✅ | Outputs produced by the pipeline/code under test |
| `catalog/` | ✅ | Metadata records (STAC Item/Collection, DCAT record, or project JSON schema)  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) |
| `provenance/` | ✅ | W3C PROV (or equivalent) describing lineage (inputs, script, commit, date)  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) |
| `goldens/` | ➕ | Snapshot outputs for regression tests (API responses, tiles, normalized JSON) |
| `licenses/` or `LICENSE.txt` | ✅ if 3rd-party | License text or link + attribution |

**CI expectation:** project-wide checks often validate that datasets have matching catalog + provenance entries and that GeoJSON is sane (valid JSON, coordinates plausible). Treat test fixtures the same way.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧭 Data conventions (so tests stay stable)

### 1) Tabular (`.csv`, `.tsv`, `.parquet`)
- UTF-8 ✅, header row ✅
- Deterministic row ordering (sort by stable key in generation scripts)
- ISO-8601 timestamps (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM:SSZ`)
- Avoid locale traps (decimal `.` not `,`)

### 2) Vector geospatial (`.geojson`, `.gpkg`)
- Default CRS: **WGS84 / EPSG:4326** unless the test explicitly targets projection logic.
- Coordinate order: **[lon, lat]** (GeoJSON standard).
- Keep geometries tiny (e.g., 3–20 features) unless testing performance/corner cases.

### 3) Raster / remote sensing (`.tif`, “COG-ish” if needed)
- Prefer **very small** rasters (e.g., 32×32, 128×128) for unit tests.
- Include a `catalog/` STAC record when raster semantics matter (bands, nodata, bounds).
- If you’re testing time-series processing patterns, keep a *short* series but keep metadata honest (dates, QA flags).  [oai_citation:7‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](sediment://file_00000000a58071f586f00793dee712d6)

### 4) Time-oriented fixtures (timelines, events, intervals)
- Store event times as ISO-8601.
- Normalize timezone assumptions (UTC recommended).
- For charts/derived analytics, store **inputs** + **expected summaries** (don’t snapshot charts unless you must).

### 5) Graph/network fixtures (edges, nodes)
- Use small adjacency lists or edge tables.
- Ensure stable node IDs and deterministic traversal order (especially for snapshot tests).

---

## 🧾 Provenance (W3C PROV “mini”)

KFM treats provenance as a first-class artifact (lineage docs live alongside data).  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
For each fixture package, include `provenance/<fixture>.prov.json` containing:

- **Inputs**: file paths under `raw/`
- **Process**: script/module name + version (include git commit hash if possible)
- **Run context**: date/time, parameters, seed
- **Outputs**: file paths under `processed/` + `goldens/` when applicable

Example fields to capture are described directly in the blueprint (script + commit + run date + produced outputs).  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🪙 Golden files (regression snapshots)

Use `goldens/` when you want to lock behavior:

- API JSON responses (normalized)
- Derived GeoJSON (normalized)
- Search results (stable ranking rules)
- SQL query outputs (ordered)

**Golden rules**
- Normalize before snapshotting (sort keys, stable ordering, rounded floats).
- Store **one canonical** expected file per assertion when possible.
- If a golden changes, the PR should explain **why** (bug fix vs. intentional behavior change).

---

## ➕ Adding a new fixture (checklist)

1. Create folder: `tests/data/fixtures/<fixture_name>/`
2. Add minimal input(s) in `raw/`
3. Generate expected outputs into `processed/` using a script or a documented command
4. Add `catalog/` metadata (STAC/DCAT/project schema)  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
5. Add `provenance/` lineage doc (include seed + commit where possible)  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
6. Add `LICENSE`/attribution if anything is derived from a 3rd-party source
7. Wire the fixture into tests
8. Ensure fixtures validate cleanly (GeoJSON validity, plausible coords), mirroring CI expectations  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧯 Common gotchas

- **“It worked locally”**: avoid reading from `data/` or user home directories; always reference `tests/data/`.
- **Floating point drift**: use tolerances; snapshot rounded values only.
- **GeoJSON precision**: if comparisons fail, normalize coordinates (rounding) in the test harness.
- **File permissions in containers**: if tests write outputs, write to `tests/data/tmp/` (gitignored).  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📚 Project-aligned references (why we do it this way)

- KFM repo structure + data/provenance as lineage docs  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- Canonical pipeline order (Raw → Processed → Catalog/Prov → …)  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- “No data without documentation” + metadata/provenance strictness  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- DVC for large artifacts + CI validating catalogs/sample outputs  [oai_citation:17‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)  

### 📎 Library pointers loaded in this workspace
(Handy when you’re aligning fixture design with broader research notes.)

- Mobile Mapping  [oai_citation:18‡Mobile Mapping - project_muse.pdf](sediment://file_000000000d04722fac99f6dd4ff63d3e)  
- Scalable Data Management for Future Hardware  [oai_citation:19‡Scalable Data Management for Future Hardware.pdf](sediment://file_000000007d74722fa87beabc663630f7)  
- Data Spaces  [oai_citation:20‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)  
- Generalized Topology Optimization for Structural Design  [oai_citation:21‡Generalized Topology Optimization for Structural Design.pdf](sediment://file_00000000f9a8722f9319f46a88852e01)  
- Spectral Geometry of Graphs  [oai_citation:22‡Spectral Geometry of Graphs.pdf](sediment://file_00000000cedc71f5a7af8031244dcd32)  
- Introduction to Digital Humanism  [oai_citation:23‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488)  
- Visualization of Time-Oriented Data  [oai_citation:24‡Visualization of Time-Oriented Data.pdf](sediment://file_000000001468722f929b8752236e5a72)  
- Cloud-Based Remote Sensing with Google Earth Engine  [oai_citation:25‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](sediment://file_00000000a58071f586f00793dee712d6)  