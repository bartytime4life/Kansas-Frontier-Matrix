---
title: "KFM Geo Validation Tooling"
path: "tools/validation/geo/README.md"
version: "v0.1.0"
last_updated: "2026-01-14"
status: "draft"
doc_kind: "Tool README"
license: "CC-BY-4.0"
markdown_protocol_version: "KFM-MP-v13"
pipeline_contract_version: "KFM-pipeline-v13"
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_ref: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"
doc_uuid: "urn:kfm:doc:tools:validation:geo:readme:v0.1.0"
commit_sha: "TBD"
doc_integrity_checksum: "sha256:TBD"
---

# 🌍 Geo Validation (KFM) — `tools/validation/geo`

<p align="center">
  <img alt="KFM" src="https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-2ea44f?style=for-the-badge">
  <img alt="Validation" src="https://img.shields.io/badge/validation-geo-blue?style=for-the-badge">
  <img alt="CI Gate" src="https://img.shields.io/badge/CI-gates--required-red?style=for-the-badge">
  <img alt="Status" src="https://img.shields.io/badge/status-draft-orange?style=for-the-badge">
</p>

> [!IMPORTANT]
> In KFM, geo data is never “just a file.” Every spatial asset is a governed, reproducible **boundary artifact** that must be validated **before** it flows downstream into catalogs (STAC/DCAT), provenance (PROV), graph, API, UI, and Story Nodes.

---

## Overview

### What this is 🧪
`tools/validation/geo` is the **geo QA gate** for the Kansas Frontier Matrix pipeline. It runs deterministic checks against geospatial assets to catch:
- broken CRS / projection issues 🧭
- invalid geometries / topology errors 🧩
- out-of-bounds extents / spatial outliers 🚧
- raster metadata problems (nodata, resolution, etc.) 🛰️
- COG compliance failures (when COG is expected) ☁️
- governance issues (missing `care_label`, precision leaks, etc.) ⚖️

### Why it exists 🚦
KFM’s architecture relies on a **non-negotiable pipeline order**:

**ETL → Catalogs → Graph → API → UI → Story Nodes**

Geo validation sits *between* ETL and Catalog creation, ensuring we never publish or ingest bad spatial artifacts into the graph or the UI.

### Scope ✅ / 🚫
| In scope ✅ | Out of scope 🚫 |
| --- | --- |
| CRS checks, extent checks, geometry validity | Full ETL (conversion/georeferencing) |
| Raster metadata & (optional) COG compliance | Deep semantic validation of domain attributes |
| Human+CI-friendly reports (JSON + summary) | Manual cartographic judgment (human review) |
| Governance hooks (FAIR+CARE & precision) | UI rendering correctness (handled elsewhere) |

### Who this is for 👥
- 🧑‍💻 Data engineers (ETL + publishing)
- 🗺️ GIS maintainers (layer QA)
- 🧪 Researchers (evidence artifacts & analysis outputs)
- 🔍 Reviewers (PR validation + moderation)

---

## How this fits the KFM pipeline 🧱

```mermaid
flowchart LR
  A[📥 Raw sources\n(data/raw/...)] --> B[🛠️ ETL & normalization\n(data/work/...)]
  B --> C[✅ Geo validation\n(tools/validation/geo)]
  C --> D[📦 Catalog boundary artifacts\nSTAC + DCAT + PROV]
  D --> E[🧠 Graph ingestion\nNeo4j]
  E --> F[🔌 API layer\n(governed access)]
  F --> G[🗺️ UI / Map / Timeline]
  G --> H[📖 Story Nodes + Focus Mode]
```

**Golden rule:** the validator must be runnable **locally** and in **CI** and produce **the same report** for the same inputs + profile.

---

## Directory Layout 📁

```text
📦 tools/
└─ 🧪 validation/
   └─ 🌍 geo/
      ├─ README.md                           ✅ you are here
      ├─ cli.py                              🧰 CLI entrypoint (recommended)
      ├─ validate.py                          ⚙️ orchestrator (profiles → rules → report)
      ├─ profiles/                            🎛️ rule sets + thresholds
      │  ├─ strict.yml
      │  ├─ lenient.yml
      │  └─ historical_scan.yml
      ├─ rules/                               🧩 small, testable checks
      │  ├─ format_integrity.py
      │  ├─ crs.py
      │  ├─ extent.py
      │  ├─ vector_geometry.py
      │  ├─ vector_topology.py
      │  ├─ raster_metadata.py
      │  ├─ raster_cog.py
      │  ├─ metadata_links.py
      │  └─ governance.py
      ├─ schemas/
      │  └─ geo_validation_report.schema.json 📜 report contract
      └─ tests/
         ├─ fixtures/                         🧪 known-good & known-bad datasets
         └─ test_rules_*.py
```

> [!NOTE]
> If your repo uses a different layout, keep **stable rule IDs** and the **report schema** intact. Those are the real contracts.

---

## Quick Start ⚡

### Prereqs (recommended baseline) 🧰
- 🐍 Python 3.10+  
- 🧭 GDAL/OGR + PROJ (format + CRS sanity)
- 🗺️ GeoPandas + Shapely + PyProj (vector checks)
- 🛰️ Rasterio (raster checks)

Optional “big data” backends:
- 🐘 PostGIS (heavy topology checks + spatial indexing)
- 🧱 PDAL (point clouds; if/when used)
- ☁️ Earth Engine workflows (remote sensing QA integration)

### Validate a single dataset (CLI) ✅
```bash
# Vector example
python -m tools.validation.geo.cli validate \
  --input data/processed/land-treaties/boundaries.geojson \
  --profile tools/validation/geo/profiles/strict.yml \
  --out data/validation/geo/boundaries.validation.json

# Raster example (COG expected)
python -m tools.validation.geo.cli validate \
  --input data/processed/elevation/dem.cog.tif \
  --profile tools/validation/geo/profiles/strict.yml \
  --out data/validation/geo/dem.validation.json
```

### Exit codes 🚥
- `0` ✅ all checks passed
- `2` ⚠️ warnings only (policy-controlled; can still fail CI if configured)
- `3` ❌ errors found (CI should fail)

> [!TIP]
> Upload validation reports as CI artifacts. They become part of the dataset’s traceable evidence trail.

---

## Profiles 🎛️

Profiles are YAML contracts defining:
- canonical CRS
- AOI (Kansas boundary or project AOI)
- enabled rules
- thresholds & severity overrides

Example profile:

```yaml
name: strict
canonical_crs: "EPSG:4326"

aoi:
  name: kansas
  # repo convention: store AOIs under docs/standards/geo/aoi/
  path: "docs/standards/geo/aoi/kansas_boundary.geojson"
  mode: "intersects"   # intersects | within | contains

rules:
  format.readable:
    enabled: true
    severity: ERROR

  crs.present:
    enabled: true
    severity: ERROR

  crs.allowed:
    enabled: true
    severity: ERROR
    allowed:
      - "EPSG:4326"
      - "EPSG:3857"

  extent.valid_bbox:
    enabled: true
    severity: ERROR

  extent.within_aoi:
    enabled: true
    severity: WARN
    tolerance_m: 5000

  vector.geometry_valid:
    enabled: true
    severity: ERROR

  governance.care_label_present:
    enabled: true
    severity: ERROR
```

---

## What gets validated 🔍

### Validation domains (rule families)
1) **File & format integrity** 📦  
   Supported type, readable, metadata extractable, optional checksums.

2) **CRS & coordinate sanity** 🧭  
   CRS present, parseable, allowlisted, axis order sane, units sane, optional reprojection test.

3) **Extent & region checks** 🗺️  
   bbox validity, outliers, and (optional) Kansas/project AOI checks.

4) **Vector geometry validity** 🧩  
   empty geometries, invalid polygons, wrong geometry types, duplicate features.

5) **Vector topology rules (dataset-type specific)** 🧷  
   overlap/gap checks, sliver detection, network connectivity, snap tolerances.

6) **Raster metadata & content checks** 🛰️  
   nodata, dtype, band structure, resolution expectations, optional basic stats.

7) **COG compliance (if expected)** ☁️  
   internal tiling, overviews, cloud-friendly layout.

8) **Metadata & provenance hooks** 🧾  
   ensure required boundary artifacts exist (STAC/DCAT/PROV) *or* are generated by pipeline steps.

9) **Governance & sensitivity checks (FAIR+CARE)** ⚖️  
   care label propagation, precision redaction policies, coordinate leak detection.

---

## Rule catalog 🧩

Each rule is defined by:
- `id` (stable dotted namespace)
- `applies_to` (`vector|raster|tiles|any`)
- `severity` (`INFO|WARN|ERROR`)
- `message` + `fix_hint`
- optional `metrics` + `sample`

### Minimal core rules (ship these first) ✅
| Rule ID | Applies | Fails when… | Severity |
| --- | --- | --- | --- |
| `format.readable` | any | file can’t be opened/parsed | ERROR |
| `crs.present` | vector/raster | CRS missing | ERROR |
| `crs.allowed` | vector/raster | CRS not in allowlist | ERROR |
| `extent.valid_bbox` | any | bbox invalid/empty | ERROR |
| `extent.within_aoi` | any | outside AOI (when enabled) | WARN/ERROR |
| `vector.no_empty_geometry` | vector | NULL/empty geometries exist | ERROR |
| `vector.geometry_valid` | vector | invalid geometries exist | ERROR |
| `raster.nodata_defined` | raster | nodata missing | WARN/ERROR |
| `raster.cog_compliant` | raster | COG checks fail (if expected) | WARN/ERROR |
| `governance.care_label_present` | any | missing care_label | ERROR |
| `governance.precision_ok` | any | precision violates policy | ERROR |

<details>
<summary>🧠 Extended rules (recommended as the project grows)</summary>

- `vector.attribute.required_fields`
- `vector.attribute.unique_id`
- `vector.topology.no_overlaps`
- `vector.topology.no_gaps`
- `vector.topology.sliver_area_threshold`
- `vector.topology.network_connectivity`
- `raster.band.expected_count`
- `raster.stats.value_range`
- `metadata.stac_profile_conforms`
- `metadata.dcat_profile_conforms`
- `provenance.prov_bundle_present`
- `provenance.links_resolve`

</details>

---

## Output: Geo Validation Report (contract) 📜

### Report shape (example)
```json
{
  "tool": "kfm-geo-validator",
  "tool_version": "0.1.0",
  "run": {
    "run_id": "2026-01-14T00:00:00Z--<uuid>",
    "profile": "strict",
    "started_at": "2026-01-14T00:00:00Z",
    "finished_at": "2026-01-14T00:00:03Z"
  },
  "inputs": [
    {
      "path": "data/processed/.../layer.geojson",
      "sha256": "…",
      "size_bytes": 123456
    }
  ],
  "summary": { "errors": 0, "warnings": 2, "info": 5 },
  "checks": [
    {
      "id": "crs.allowed",
      "status": "pass",
      "severity": "ERROR",
      "metrics": { "epsg": 4326 }
    },
    {
      "id": "extent.within_aoi",
      "status": "warn",
      "severity": "WARN",
      "message": "2 features fall outside Kansas AOI by > 5km",
      "sample": [{ "feature_id": "abc123" }, { "feature_id": "def456" }]
    }
  ]
}
```

### Schema location
- `tools/validation/geo/schemas/geo_validation_report.schema.json`

> [!IMPORTANT]
> Treat the report schema like an API contract. Breaking changes must be versioned.

---

## Methodology: “NASA‑grade” V&V mindset for maps 🧠✨

Geo validation works best when treated like **V&V + uncertainty**:
- **Verification**: rule implementations are tested against known-good/known-bad fixtures (unit tests).
- **Validation**: rules are calibrated against real historical datasets (and known failure modes).
- **Uncertainty**: borderline cases produce metrics + warnings rather than silent pass/fail.

> [!NOTE]
> When you run many checks, false alarms become more likely (classic multiple-testing problem). Use profiles to control severity and thresholds so CI noise doesn’t drown real issues.

---

## CI / automation hooks 🤖

### GitHub Actions (example)
```yaml
name: geo-validation

on:
  pull_request:
    paths:
      - "data/**"
      - "tools/validation/geo/**"

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install deps
        run: |
          pip install -r requirements.txt
      - name: Run geo validation (changed files)
        run: |
          python -m tools.validation.geo.cli validate-changed \
            --profile tools/validation/geo/profiles/strict.yml \
            --reports-dir data/validation/geo
      - name: Upload validation reports
        uses: actions/upload-artifact@v4
        with:
          name: geo-validation-reports
          path: data/validation/geo/*.json
```

### Pre-commit (example)
```yaml
repos:
  - repo: local
    hooks:
      - id: kfm-geo-validate
        name: KFM Geo Validation
        entry: python -m tools.validation.geo.cli validate
        language: system
        files: \.(geojson|gpkg|shp|tif|tiff)$
```

---

## Extending the validator (adding rules) 🧩

### Rule design principles
- ✅ Small, pure, testable
- ✅ Deterministic outputs
- ✅ Clear `fix_hint`
- ✅ Metrics > opinions
- ✅ Profile-driven thresholds (avoid “one-off” hacks)

### Minimal rule interface (suggested)
```python
class Rule(Protocol):
    id: str
    applies_to: set[str]  # {"vector"} / {"raster"} / {"any"}
    default_severity: str # INFO/WARN/ERROR

    def run(self, ctx: ValidationContext) -> RuleResult:
        ...
```

### Testing strategy 🧪
- Every rule should ship with:
  - a **known-good** fixture ✅
  - a **known-bad** fixture ❌
- Store fixtures in `tools/validation/geo/tests/fixtures/`
- Keep fixtures tiny (fast CI) but representative (realistic failure modes)

---

## Security & robustness 🔒

Treat all inputs as untrusted:
- never eval/exec anything derived from dataset metadata
- sanitize paths (avoid traversal and remote path injection)
- if PostGIS is used, parameterize queries (no string concatenation)
- constrain resource use (memory/time) for large or malicious files

> [!TIP]
> Validation is a boundary defense layer: it should fail fast, log clearly, and avoid “partial publish” states.

---

## Governance & safety (FAIR+CARE) ⚖️

> [!WARNING]
> Some spatial data is sensitive even when it looks “public.” Exact coordinates can expose vulnerable sites, culturally sensitive locations, or protected resources.

This module should enforce:
- `care_label` present and propagated into:
  - validation report
  - STAC/DCAT metadata
  - PROV activity bundle
- coordinate precision policies by label (example):
  - **Public**: full precision allowed
  - **Restricted**: geometry must be generalized / redacted
  - **Tribal Sensitive**: default deny + governance review required

**Where to document policy**
- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`

---

## Performance notes 🏎️

- For large rasters: prefer windowed reads (streaming).
- For large vectors: validate in chunks; avoid full-dataset reprojections unless necessary.
- Heavy topology checks: prefer PostGIS + spatial indexes.
- Emit timing per rule for profiling (helps keep CI fast).

---

## Troubleshooting (common failures) 🛠️

<details>
<summary>🧭 CRS errors</summary>

- **Symptom:** `crs.present` fails  
  **Fix:** ensure CRS is set during conversion/georeferencing and preserved in output.

- **Symptom:** `crs.allowed` fails  
  **Fix:** reproject into a profile-allowed CRS:
  ```bash
  ogr2ogr -t_srs EPSG:4326 out.geojson in.shp
  ```

</details>

<details>
<summary>🧩 Invalid polygons</summary>

- **Symptom:** `vector.geometry_valid` fails (self-intersections / bowties)  
  **Fix:** run a “make valid” step (tooling-dependent), then re-run validation.

</details>

<details>
<summary>🛰️ COG compliance</summary>

- **Symptom:** `raster.cog_compliant` fails  
  **Fix:** re-encode as COG:
  ```bash
  gdal_translate in.tif out.cog.tif -of COG
  ```

</details>

---

## Reference library (project files) 📚

This module’s design pulls patterns from the project’s included references (geospatial workflows, modeling V&V, statistics, governance, systems performance, security, and visualization).

<details>
<summary>📖 Expand: complete project file index</summary>

### Core KFM architecture & documentation
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`
- `Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf`
- `MARKDOWN_GUIDE_v13.md.gdoc`
- `Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx`
- `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf`

### Geo & cartography
- `python-geospatial-analysis-cookbook.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- `Archaeological 3D GIS_26_01_12_17_53_09.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`

### Modeling / stats / uncertainty (for anomaly detection & QA thresholds)
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `graphical-data-analysis-with-r.pdf`

### Data systems & performance
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `Database Performance at Scale.pdf`
- `Scalable Data Management for Future Hardware.pdf`
- `Data Spaces.pdf`
- `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`

### Graphs / optimization (background for graph-based spatial reasoning)
- `Spectral Geometry of Graphs.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`

### Ethics / society / law (context for governance)
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`

### Security & robustness
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

### UI / visualization & media formats
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `responsive-web-design-with-html5-and-css3.pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### Programming encyclopedias (language & systems reference)
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

### ML (optional)
- `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf`

</details>

---

## Version history 🗓️
| Version | Date | Notes |
| --- | --- | --- |
| v0.1.0 | 2026-01-14 | Initial README scaffold + contracts + CI patterns |

---

## Definition of Done ✅
- [ ] YAML front-matter complete + valid
- [ ] Rule IDs are stable + documented
- [ ] Report schema exists + is versioned
- [ ] CLI returns correct exit codes
- [ ] CI integration example works
- [ ] Governance & sovereignty considerations documented
- [ ] At least 1 fixture per rule (good + bad)
- [ ] Validation reports can be linked into PROV
