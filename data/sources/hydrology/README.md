<div align="center">

# 💧 Kansas Frontier Matrix — Hydrology Source Manifests

`data/sources/hydrology/`

**Mission:** Define, document, and validate all **external hydrology data sources**
powering the Kansas Frontier Matrix (KFM). These inputs form the hydrologic framework
for modeling watersheds, stream networks, flood risk, and groundwater systems.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![Schema Validate](https://img.shields.io/badge/JSON%20Schema-validated-success?logo=json)](../schema/source.schema.json)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data (CC-BY 4.0)](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

The `data/sources/hydrology/` directory maintains JSON manifests describing
each external hydrologic data source integrated into KFM — from river networks
and watershed boundaries to FEMA flood hazard maps and groundwater datasets.

These sources underpin:

* Streamflow and basin delineation
* Floodplain and hazard analysis
* Hydrologic connectivity and modeling
* STAC-registered hydrology collections

Every manifest conforms to `data/sources/schema/source.schema.json`
to ensure structure, validation, and reproducibility.

---

## 🗂️ Directory Layout

```bash
data/sources/hydrology/
├── README.md
├── usgs_nhd_flowlines.json    # National Hydrography Dataset (NHD)
├── epa_wbd_huc12.json         # Watershed Boundary Dataset (HUC12)
└── fema_nfhl.json             # FEMA National Flood Hazard Layer
```

> **Note:**
> Each `.json` manifest defines provider, format, spatial/temporal coverage,
> update frequency, provenance, and licensing — providing full traceability
> for all hydrologic data inputs.

---

## 💧 Example: `usgs_nhd_flowlines.json`

```json
{
  "id": "usgs_nhd_flowlines",
  "title": "USGS National Hydrography Dataset (NHD) Flowlines",
  "provider": "U.S. Geological Survey (USGS)",
  "description": "Vector hydrography representing the surface water drainage network across Kansas.",
  "endpoint": "https://prd-tnm.s3.amazonaws.com/StagedProducts/Hydrography/NHD/HU4/HighResolution/GDB/NHD_HU4_GDB.zip",
  "access_method": "HTTP download",
  "license": "Public Domain (US Government)",
  "data_type": "vector",
  "format": "FileGDB",
  "spatial_coverage": "Kansas, USA",
  "temporal_coverage": "2019–Present",
  "update_frequency": "Quarterly",
  "last_verified": "2025-10-12",
  "linked_pipeline": "hydrology_pipeline.py",
  "notes": "Provides the foundational vector network for stream, river, and waterbody mapping."
}
```

---

## 🧭 System Context (GitHub-safe Mermaid)

```mermaid
flowchart TD
  A["External Hydrology Data\n(USGS · EPA · FEMA)"] --> B["Source Manifests\n`data/sources/hydrology/*.json`"]
  B --> C["Hydrology Pipeline\n`src/pipelines/hydrology_pipeline.py`"]
  C --> D["Processed Hydrology Layers\n`data/processed/hydrology/`"]
  D --> E["STAC Collections\n`data/stac/collections/hydrology.json`"]
  E --> F["Web Layers Config\n`web/config/layers.json`"]
  D --> G["Derivatives\nFlow Accumulation · Watershed Boundaries · Flood Zones"]
  G --> H["Knowledge Graph\n\"Hydrologic Connectivity\" Relationships"]
%%END OF MERMAID%%
```

---

## ⚙️ Hydrology Source Summary

| Manifest File             | Provider | Description                         | Coverage        | Format    | Verified     |
| :------------------------ | :------- | :---------------------------------- | :-------------- | :-------- | :----------- |
| `usgs_nhd_flowlines.json` | USGS     | High-resolution hydrography network | Kansas (HUC4)   | GDB       | ✅ 2025-10-12 |
| `epa_wbd_huc12.json`      | EPA      | Watershed boundaries (HUC12)        | Kansas          | Shapefile | ✅ 2025-10-12 |
| `fema_nfhl.json`          | FEMA     | Flood hazard polygons               | Kansas counties | GDB       | ✅ 2025-10-12 |

---

## 🧾 ETL Integration

**Pipeline:** `src/pipelines/hydrology_pipeline.py`
**Target:** `data/processed/hydrology/`

### ETL Workflow:

1. **Validate** manifests (`make sources-validate`)
2. **Download & extract** hydrologic datasets
3. **Reproject** to EPSG:3857 and standardize geometry
4. **Clip** to Kansas boundary
5. **Generate** derivatives (flow accumulation, stream order, flood extents)
6. **Link** outputs with STAC and provenance metadata

---

## 🧪 Validation Commands

**Manual Validation**

```bash
python src/utils/validate_sources.py data/sources/hydrology/ --schema data/sources/schema/source.schema.json
```

**Makefile Shortcuts**

```bash
make hydrology-sources
make hydrology-validate
```

**Automated CI**

* Schema validation
* URL endpoint checks
* License & attribution validation
* Temporal coverage consistency check

---

## 🧩 Provenance Integration

| Component                              | Function                                          |
| :------------------------------------- | :------------------------------------------------ |
| `data/raw/hydrology/`                  | Immutable raw NHD, WBD, NFHL datasets             |
| `data/processed/hydrology/`            | Reprojected, clipped, and merged hydrology layers |
| `data/stac/collections/hydrology.json` | STAC metadata linking back to source manifests    |
| `data/checksums/hydrology/`            | Integrity validation via `.sha256` hashes         |
| `src/pipelines/hydrology_pipeline.py`  | Automated ETL for all hydrology sources           |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                      |
| :---------------------- | :------------------------------------------------------------------ |
| **Documentation-first** | Each hydrology source documented via schema-based manifest.         |
| **Reproducibility**     | Manifest-driven ETL ensures deterministic re-creation of layers.    |
| **Open Standards**      | STAC, JSON Schema, GeoPackage, and CRS standards used throughout.   |
| **Provenance**          | End-to-end traceability from manifest → pipeline → STAC → checksum. |
| **Auditability**        | Continuous validation via GitHub Actions and CI tests.              |

---

## 🧾 Changelog

| Version  | Date       | Summary                                                                                |
| :------- | :--------- | :------------------------------------------------------------------------------------- |
| **v1.1** | 2025-10-12 | Added CI validation links, improved table formatting, and new NHD/WBD/FEMA references. |
| v1.0     | 2025-10-04 | Initial creation of hydrology source manifest directory.                               |

---

## 🏷️ Version Block

```text
Component: data/sources/hydrology/README.md
SemVer: 1.1.0
Spec Dependencies: MCP v1.0 · STAC 1.0
Last Updated: 2025-10-12
Maintainer: @bartytime4life
```

---

<div align="center">

**Kansas Frontier Matrix** — *“Rivers remember the land — and data remembers the rivers.”*
📍 [`data/sources/hydrology/`](.) · **Canonical hydrology registry** powering KFM’s water systems and watershed modeling.

</div>

