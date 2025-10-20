<div align="center">

# 🗂️ **Kansas Frontier Matrix — File & Directory Architecture (v2.0.0 · Tier-Ω+∞ Certified)**  
`docs/architecture/file-architecture.md`

**Mission:** Define the **complete repository layout, file contracts, naming standards, and lineage rules** for the **Kansas Frontier Matrix (KFM)** — so every file and folder is **discoverable**, **validated**, **provenanced**, and **reproducible** under **MCP-DL v6.3** and **FAIR/CARE**.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../docs/)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../.github/workflows/stac-validate.yml)
[![SBOM](https://img.shields.io/badge/SBOM-Syft%20%7C%20Grype-blue)](../../.github/workflows/sbom.yml)
[![SLSA Provenance](https://img.shields.io/badge/Supply--Chain-SLSA%20Attestations-green)](../../.github/workflows/slsa.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — File & Directory Architecture"
document_type: "Architecture Spec"
version: "v2.0.0"
last_updated: "2025-11-16"
owners: ["@kfm-architecture","@kfm-data","@kfm-web","@kfm-ai","@kfm-security","@kfm-docs"]
status: "Stable"
maturity: "Production"
license: "CC-BY 4.0"
tags: ["file-architecture","standards","stac","checksums","lfs","dvc","provenance","dq","fair","care","slsa"]
alignment:
  - MCP-DL v6.3
  - STAC 1.0 / DCAT 2.0
  - JSON Schema / ISO 8601 / RFC 3339
  - CIDOC CRM / OWL-Time / GeoSPARQL
  - SPDX / CycloneDX (SBOM)
  - SLSA Level ≥ 2
validation:
  docs_ci_required: true
  frontmatter_required: ["title","version","owners","last_updated","license"]
  mermaid_end_marker: "<!-- END OF MERMAID -->"
observability:
  endpoint: "https://metrics.kfm.ai/file-architecture"
  metrics: ["frontmatter_coverage_pct","broken_link_count","lfs_tracking_pct","checksum_presence_pct","stac_link_valid_pct"]
preservation_policy:
  retention: "raw permanent · processed 5y · tiles 2y · logs 90d"
  checksum_algorithm: "SHA-256"
  replication_targets: ["GitHub","Zenodo DOI (major)","OSF"]
---
```

---

## 📚 Overview

The KFM repository is organized so **anyone can trace a file’s purpose, lineage, and integrity** in seconds.  
Every directory includes **README + schema/manifest + checksums**, with **CI gates** that block drift.

---

## 🗃️ Top-Level Repository Layout

```bash
Kansas-Frontier-Matrix/
├── data/                      # Core data management system
│   ├── sources/               # Source manifests (origin/license/coverage/URLs)
│   ├── raw/                   # Immutable originals (LFS/DVC optional)
│   ├── processed/             # Validated, standardized outputs
│   ├── checksums/             # SHA-256 parity files for reproducibility
│   ├── stac/                  # STAC catalog (Items/Collections)
│   ├── tiles/                 # Raster/Vector tiles for web viewers
│   ├── work/                  # tmp/cache/staging/logs (transient)
│   └── ARCHITECTURE.md        # Data-specific architecture
│
├── docs/                      # Documentation system
│   ├── architecture/          # Architecture specs & diagrams
│   ├── standards/             # Style, schema, validation policies
│   ├── templates/             # SOP/experiment/model-card templates
│   └── glossary.md            # Canonical terminology
│
├── src/                       # ETL + processing pipelines
│   ├── etl/                   # Domain ETL code
│   ├── graph/                 # Neo4j loaders & schema
│   ├── api/                   # FastAPI + GraphQL backend
│   └── utils/                 # Shared helpers/validators
│
├── web/                       # Web app
│   ├── config/                # UI layer config & layer registries
│   ├── assets/                # Logos/icons/images
│   └── index.html
│
├── .github/                   # CI/CD automations
│   ├── workflows/             # Actions: validate/deploy/provenance
│   └── ISSUE_TEMPLATE/        # Contribution entry points
│
├── Makefile                   # Reproducible tasks
├── LICENSE                    # MIT (code) + CC-BY 4.0 (docs/data)
└── README.md                  # Repo overview
```

---

## 🧱 Data Subsystem Hierarchy

```bash
data/
├── sources/                 # Manifest registry (JSON)
├── raw/                     # Immutable inputs (untouched)
├── processed/               # Cleaned standard outputs
│   ├── terrain/             # DEM, slope, hillshade
│   ├── hydrology/           # Rivers, basins, floods
│   ├── landcover/           # NLCD, crops
│   ├── climate/             # Temp/precip/drought
│   ├── hazards/             # Tornado/flood/wildfire
│   ├── tabular/             # Census/ag/economics
│   └── text/                # OCR & transcripts
│
├── processed/metadata/      # STAC-linked metadata + thumbnails
├── checksums/               # SHA-256 files (*.sha256)
├── stac/                    # Items/Collections (versioned)
├── tiles/                   # Mosaics/tilesets (MVT/COG)
└── work/                    # tmp · cache · staging · logs
```

**Each domain** contains:

- `README.md` (purpose + owners + schema refs)  
- `metadata/` (STAC items + JSON Schema)  
- `thumbnails/` (previews)  
- `checksums/` (asset `.sha256`)  

---

## 🧩 Workspace Roles & Retention

| Directory            | Purpose                                  | Lifecycle | Retention |
|:--|:--|:--|:--|
| `data/work/tmp/`     | Intermediates during ETL                 | Ephemeral | `make clean-tmp` |
| `data/work/cache/`   | Reused intermediates                     | Semi-persistent | Monthly purge |
| `data/work/staging/` | Pre-validation holding area              | Transitional | Promote/purge post-validate |
| `data/work/logs/`    | ETL/CI logs for reproducibility          | Continuous | 90 days |

---

## 🧾 File Naming & Path Contracts

- **Lowercase + underscores**; ASCII only; no spaces.  
- **Deterministic, descriptive** naming:

| Category | Pattern | Example |
|:--|:--|:--|
| Dataset | `<domain>_<dataset>_v<MAJOR>.<MINOR>_<year>.<ext>` | `terrain_ks_1m_dem_v2.0_2020.tif` |
| Metadata | `<dataset>.json` | `terrain_ks_1m_dem_v2.0_2020.json` |
| Checksum | `<dataset>.<ext>.sha256` | `terrain_ks_1m_dem_v2.0_2020.tif.sha256` |
| Thumbnail | `<dataset>.png` | `terrain_ks_1m_dem_v2.0_2020.png` |
| Source manifest | `<provider>_<dataset>.json` | `usgs_3dep_dem.json` |
| Logs | `<domain>_etl_debug.log` | `terrain_etl_debug.log` |

**Timestamps:** **RFC 3339 / ISO 8601** (`YYYY-MM-DDTHH:MM:SSZ`).  
**CRS policy:** Catalog coordinates **EPSG:4326**; tiles **EPSG:3857**; rasters may retain native CRS (documented in STAC via `proj:`).

---

## 🧷 Git Attributes, LFS & Ignore Rules

**`.gitattributes` (excerpt)**  
```text
# Large binaries to LFS
*.tif filter=lfs diff=lfs merge=lfs -text
*.tiff filter=lfs diff=lfs merge=lfs -text
*.png filter=lfs diff=lfs merge=lfs -text
*.pdf filter=lfs diff=lfs merge=lfs -text
*.mbtiles filter=lfs diff=lfs merge=lfs -text
# Preserve line endings and UTF-8
*.json text eol=lf
*.md   text eol=lf
```

**`.gitignore` (excerpt)**  
```text
# Transients
data/work/tmp/
data/work/cache/
data/work/staging/
__pycache__/
*.log
```

> For **DVC** use `.dvc/config` + `dvc.yaml` to track large lineage; CI verifies pointers with `dvc-sync.yml`.

---

## 🧪 Source Manifest & JSON Schema

**Manifest example — `data/sources/terrain/usgs_3dep_dem.json`**  
```json
{
  "$schema": "../../schemas/source.schema.json",
  "id": "usgs_3dep_dem",
  "title": "USGS 3DEP 1m DEM (Kansas subset)",
  "providers": [{"name": "USGS", "roles": ["producer"]}],
  "license": "Public Domain",
  "coverage": {"bbox": [-102.05,36.99,-94.59,40.00], "temporal": "2018/2020"},
  "access": {"type": "https", "url": "https://elevation.nationalmap.gov/arcgis/rest/..."},
  "checksum": {"alg": "sha256", "value": null}
}
```

**Schema excerpt — `docs/standards/schemas/source.schema.json`**  
```json
{
  "type": "object",
  "required": ["id","title","providers","license","coverage","access"],
  "properties": {
    "id": {"type":"string"},
    "coverage": {
      "type":"object",
      "required":["bbox","temporal"]
    }
  }
}
```

---

## 🔗 Provenance Chain (File Relationships)

```text
data/sources/<domain>/<source>.json
    ↓ fetch
data/raw/<domain>/<dataset>.<ext>
    ↓ etl
data/processed/<domain>/<dataset>.<ext>
    ↓ checksum
data/checksums/<domain>/<dataset>.<ext>.sha256
    ↓ catalog
data/stac/<domain>/<dataset>.json
    ↓ publish
data/tiles/<domain>/<dataset>/{z}/{x}/{y}.pbf
```

**All steps** are validated via STAC and checksum workflows; links must be **relative and resolvable**.

---

## 🧮 Data Quality (DQ) Pack

| Rule | Description | Target |
|:--|:--|:--|
| Schema completeness | Required STAC + custom fields present | 100% |
| Geometry validity | No self-intersections/empties | 100% |
| CRS declared | CRS in file + metadata | 100% |
| Checksum parity | Raw→processed parity | 100% |
| Temporal plausibility | Dates in expected intervals | ≥ 99% |

Reports emitted to `data/processed/metadata/<domain>/dq_report.json`.

---

## ⚙️ Makefile Bridges

```bash
make fetch         # pull sources by manifest
make process       # run ETL pipelines
make stac          # generate & validate STAC items/collections
make checksums     # compute & diff SHA-256
make tiles         # build MVT/COG tiles
make validate      # run DQ suite (schema/geometry/dates)
```

---

## 🧩 Policy-as-Code & CI Gates

- **OPA/Conftest**: block PRs missing required metadata (license/providers/created/derived_from).  
- **Action pinning**: critical workflows pinned by **SHA**.  
- **CARE flags**: publishing blocked for restricted layers (STAC `properties.data_ethics`).  
- **docs-validate**: front-matter + mermaid end-marker required.

---

## 📈 Observability & Storage Hygiene

```yaml
storage_metrics:
  export_to: "https://metrics.kfm.ai/data"
  budgets:
    raw_growth_gb_month: 20
    tiles_growth_gb_month: 10
  fields:
    - storage_growth_gb
    - lfs_tracking_pct
    - checksum_presence_pct
    - stac_link_valid_pct
```

---

## 🧭 Directory README Contract (template)

Every top-level and domain directory must include a README with:

```yaml
---
title: "terrain domain"
owners: ["@kfm-data"]
version: "vX.Y.Z"
last_updated: "YYYY-MM-DD"
schema_refs: ["../../docs/standards/schemas/source.schema.json"]
---
```

- **Scope and purpose**  
- **Inputs/outputs** (paths)  
- **How to reproduce** (`make`/script snippets)  
- **Known issues** (QA notes)  

---

## 🧠 MCP Compliance Summary

| Pillar | Implementation |
|:--|:--|
| Documentation-first | README + schema + examples in every directory |
| Reproducibility | Deterministic ETL + checksums + STAC |
| Open Standards | GeoTIFF (COG), GeoJSON, Parquet, JSONL, STAC |
| Provenance | Per-stage links + relative paths + DOIs (major) |
| Auditability | CI artifacts, DQ reports, policy gates |

---

## 🧨 Risk Register (File/Layout)

| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|:--|:--|:--:|:--:|:--|:--|
| FILE-001 | Missing checksums | M | H | CI gate + `make checksums` | @kfm-data |
| FILE-002 | STAC link rot | M | M | link audit in `stac-validate` | @kfm-data |
| FILE-003 | LFS mis-track | L | M | `.gitattributes` + CI path check | @kfm-architecture |
| FILE-004 | CRS mismatch | M | M | CRS policy + DQ check | @kfm-data |
| FILE-005 | Care-policy bypass | L | H | OPA rule + review label | @kfm-security |

---

## 🔗 Related Documentation

- `docs/architecture/architecture.md` — System overview  
- `docs/architecture/data-architecture.md` — Data flow & lineage  
- `docs/architecture/api-architecture.md` — API stack & contracts  
- `data/ARCHITECTURE.md` — Per-domain details & SOPs  
- `.github/workflows/README.md` — Governance automation

---

## 🧾 Versioning & Lifecycle

```yaml
versioning:
  policy: "Semantic Versioning (MAJOR.MINOR.PATCH)"
  tag_pattern: "file-arch-v*"
  doi_on_major: true
  provenance_bundle:
    - "file_architecture.prov.json"
    - "file_architecture.sha256"
```

---

## 🕰 Version History

| Version | Date | Summary |
|:--|:--|:--|
| **v2.0.0** | 2025-11-16 | Tier-Ω+∞: Added LFS/DVC policies, manifest/schema examples, directory README contract, DQ framework, storage budgets, OPA gates, and provenance bundle. |
| v1.0.0 | 2025-10-04 | Initial file/directory architecture & lineage design. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every File Has a Purpose. Every Path Has a Provenance.”*  
📍 `docs/architecture/file-architecture.md` — Canonical directory & file-level standards for KFM.

</div>