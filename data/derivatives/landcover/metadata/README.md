<div align="center">

# 🌿 Kansas Frontier Matrix — Landcover Derivative Metadata  
`data/derivatives/landcover/metadata/`

**Purpose:** Provide structured, machine-readable metadata for **landcover derivative datasets** —  
vegetation rasters, NLCD composites, cropland extent models, and historical land-use reconstructions —  
produced, validated, and versioned via the **KFM ETL pipeline**.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `metadata/` directory defines **JSON metadata records** describing all processed landcover derivatives  
under `data/derivatives/landcover/`.  
Each record provides:

- 📜 **Provenance & lineage** (data source, transformation, validation)  
- 🌎 **Spatial & temporal metadata** (coverage, CRS, timestamps)  
- 🧮 **Variables & classification schema**  
- 🧾 **Checksums and STAC linkages**  
- 🔗 **MCP compliance & reproducibility tags**

These metadata files make every derivative self-describing, auditable, and interoperable  
across the **Kansas Frontier Matrix (KFM)** knowledge system and **STAC 1.0.0** catalogs.

---

## 🧭 Metadata Generation Flow

```mermaid
flowchart TD
  A["Landcover Sources<br/>USGS NLCD · KARS · USDA NRCS"]
    --> B["ETL<br/>Extract · Normalize · Derive"]
  B --> C["Landcover Derivatives<br/>COG · GeoJSON · Parquet · CSV"]
  C --> D["Metadata JSONs<br/>variables · CRS · temporal range · provenance"]
  D --> E["Checksums<br/>SHA-256 Validation"]
  D --> F["STAC Items<br/>Link assets + metadata"]
  F --> G["Knowledge Graph<br/>entity creation + relations"]
  G --> H["API & Web UI<br/>landcover layers · vegetation analytics"]
````

<!-- END OF MERMAID -->

---

## 🗂️ Directory Layout

```bash
data/derivatives/landcover/metadata/
├── nlcd_1992_2021.json
├── vegetation_zones_1850_ks.json
├── landuse_1900_2000_composite.json
├── prairie_extent_2020.json
└── README.md
```

Each `.json` file corresponds to a processed derivative artifact
and adheres to the **KFM Derivative Metadata Schema**, aligned with
**STAC**, **DCAT**, and **MCP provenance conventions**.

---

## 🧾 Metadata Schema (Example)

```json
{
  "id": "nlcd_1992_2021",
  "title": "National Land Cover Database (NLCD) Composite for Kansas (1992–2021)",
  "description": "Landcover composite derived from USGS NLCD rasters, harmonized to consistent categories and clipped to Kansas boundaries.",
  "type": "raster",
  "format": "COG",
  "file": "../nlcd_1992_2021_cog.tif",
  "checksum": "../checksums/nlcd_1992_2021_cog.tif.sha256",
  "source": "../../../sources/usgs_nlcd.json",
  "stac_item": "../../../stac/items/nlcd_1992_2021.json",
  "spatial": {
    "crs": "EPSG:4326",
    "bbox": [-102.05, 36.99, -94.59, 40.00]
  },
  "temporal": {
    "start": "1992-01-01",
    "end": "2021-12-31"
  },
  "variables": [
    {
      "name": "landcover_class",
      "units": "categorical",
      "description": "NLCD-derived landcover categories (e.g., water, forest, grassland, developed)."
    }
  ],
  "license": "CC-BY-4.0",
  "created": "2025-10-10",
  "mcp_stage": "derivatives"
}
```

💡 **Tip:**
Align all relative paths (`file`, `checksum`, `stac_item`) to this directory.
Each JSON record must be referenced in its STAC Item under `data/stac/items/`.

---

## 🧩 Relationship to Other Metadata Layers

| Layer                      | Path                                    | Purpose                                                           |
| :------------------------- | :-------------------------------------- | :---------------------------------------------------------------- |
| 🌿 **Source Metadata**     | `data/sources/`                         | Defines provenance for inputs (e.g., USGS NLCD, KARS vegetation). |
| 🧮 **Derivative Metadata** | `data/derivatives/landcover/metadata/`  | Describes transformed landcover layers.                           |
| 🧾 **Checksums**           | `data/derivatives/landcover/checksums/` | Verifies file integrity (SHA-256).                                |
| 🗺️ **STAC Catalog**       | `data/stac/`                            | Registers assets with spatial/temporal context.                   |
| 🧠 **Knowledge Graph**     | `src/graph/`                            | Connects datasets to entities and temporal relations.             |

---

## ⚙️ Usage in the Pipeline

* **ETL Automation:** Python scripts under `tools/landcover/` generate/update metadata post-processing.
* **Schema Validation:** `jsonschema-cli` and `stac-validator` enforce compliance.
* **CI/CD Integration:**

  * `.github/workflows/stac-validate.yml` ensures metadata and checksums are consistent.
* **Knowledge Graph Sync:**

  * Metadata attributes (`variables.name`, `temporal.start`) populate Neo4j entities.

---

## 🧱 Metadata Best Practices

| Category           | Guideline                                                  |
| :----------------- | :--------------------------------------------------------- |
| ✅ **Completeness** | Every derivative must include a metadata JSON file.        |
| 🔗 **Linkage**     | Reference source manifest, checksum, and STAC item.        |
| 🕓 **Timestamps**  | Use ISO 8601 for `created` and `last_updated`.             |
| 🌾 **Variables**   | Explicitly define landcover variable names and categories. |
| 🧾 **Licensing**   | Include `license` field (default: CC-BY-4.0).              |
| 🧪 **Validation**  | Run `make validate-landcover` or rely on CI workflows.     |

---

## 🔒 Reproducibility & MCP Alignment

Landcover metadata implements **Master Coder Protocol (MCP)** standards by:

* Encoding **semantic metadata** (STAC, DCAT, CIDOC CRM).
* Linking derivatives to **provenance and checksum** artifacts.
* Capturing **temporal, spatial, and categorical** metadata for traceability.
* Enforcing **schema + STAC validation** across CI/CD pipelines.

> Every dataset is **machine-actionable**, **traceable**, and **AI-ready** for downstream GIS and analytics pipelines.

---

## ✅ MCP Compliance Summary

| MCP Principle       | Implemented | Evidence                                 |
| :------------------ | :---------: | :--------------------------------------- |
| Documentation-First |      ✅      | README + JSON metadata + CI links        |
| Provenance          |      ✅      | Linked STAC items + checksums            |
| Reproducibility     |      ✅      | Automated validation via Makefile & CI   |
| Schema Validation   |      ✅      | `jsonschema-cli` + `stac-validator`      |
| Transparency        |      ✅      | Open repository + CC-BY-4.0 data license |

---

## 🧩 Related Documentation

* [`../checksums/README.md`](../checksums/README.md) — Checksum workflow
* [`../../../../stac/README.md`](../../../../stac/README.md) — STAC item structure
* [`../../../../../../docs/architecture.md`](../../../../../../docs/architecture.md) — ETL & provenance system design
* [`../../../../sources/README.md`](../../../../sources/README.md) — Source manifest conventions

---

## 🗓️ Version History

| Version    | Date       | Author                                   | Notes                                                               |
| :--------- | :--------- | :--------------------------------------- | :------------------------------------------------------------------ |
| **v1.1.0** | 2025-10-11 | KFM Landcover & Ecology Integration Team | Added frontmatter, compliance summary, and enhanced structure       |
| **v1.0.0** | 2025-10-10 | KFM Data Standards Team                  | Initial creation of landcover derivative metadata schema & examples |

---

## 🪶 License & Provenance

**License:** [CC-BY 4.0](../../../../../LICENSE)
**Provenance:** Authored under the **Master Coder Protocol (MCP)** — documentation-first, auditable, and version-controlled.
**Maintainers:** Kansas Frontier Matrix Landcover & Ecology Integration Team
**Last Updated:** 2025-10-11

---

<div align="center">

*“From satellite light to prairie life — every pixel tells a story of Kansas.”*

</div>
```

---
