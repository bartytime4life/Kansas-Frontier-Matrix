---
title: "🌬️ KFM v11.2 — Meteorology Pipelines Index (HRRR · NDFD · Zarr · GRIB2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/meteorology/README.md"

version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmosphere Working Group · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:pipelines:meteorology:index:v11.2.2"
semantic_document_id: "kfm-pipelines-meteorology-index"
event_source_id: "ledger:docs/pipelines/meteorology/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/meteorology-index-v11.2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

status: "Active / Enforced"
doc_kind: "Pipeline README"
intent: "meteorology-pipelines-index"
category: "Pipelines · Meteorology · ETL · STAC · Forecast Integration"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Aligned Atmospheric Data Use"

classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "Annual Review"
sunset_policy: "Superseded by Meteorology Pipelines Index v12"
---

<div align="center">

# 🌬️ **KFM v11.2 — Meteorology Pipelines Index**  
`docs/pipelines/meteorology/README.md`

**Purpose**  
Provide the **authoritative entrypoint** for all atmospheric and forecast ETL pipelines within the Kansas Frontier Matrix.  
This index governs ingestion, subsetting, reproducibility, metadata creation, validation, and knowledge-graph integration for:

- **HRRR (High-Resolution Rapid Refresh)**
- **Byte-Range GRIB2 Pipelines**
- **HRRR-Zarr Atmospheric Archives**
- **NDFD Forecast Grids**
- **NAM-Nest (optional)**
- **Future RRFS Pipelines**

All pipelines follow:  
**Deterministic ETL · FAIR+CARE Governance · STAC/DCAT Compliance · PROV-O Lineage · OpenLineage v2.5**

  
<!-- Badge Row -->
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.2-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Meteorology-gold" />
<img src="https://img.shields.io/badge/OpenLineage-v2.5-informational" />
<img src="https://img.shields.io/badge/Atmosphere-Pipelines-lightgrey" />

</div>

---

## 📘 1. Overview

The KFM meteorology pipelines deliver:

- **High-resolution atmospheric models** (HRRR, NDFD, NAM-Nest)  
- **Forecast + analysis ingestion**  
- **Byte-range GRIB2 ETL** (no full GRIB downloads)  
- **Zarr-chunked, cloud-optimized workflows**  
- **Full CF compliance, CRS harmonization, and vertical-axis correctness**  
- **STAC-/DCAT-ready Items and Collections**  
- **Knowledge Graph population (AtmosphericVariable, ForecastSlice, Influences)**  
- **Focus Mode v3 atmospheric narratives**  
- **Energy/carbon telemetry for sustainability goals**  

This index represents the **top-level meteorology subsystem** inside the v11.2 environmental intelligence stack.

---

## 🗂️ 2. Directory Layout (Canonical)

```text
📁 docs/
└── 📁 pipelines/
    └── 📁 meteorology/
        📄 README.md                               — ← This file (index)
        📄 meteorology-integration-blueprint.md    — Full design of HRRR/GRIB2 ETL
        📁 etl/                                    — Atmospheric ETL modules
        │   📁 hrrr/                               — HRRR byte-range + Zarr ingestion
        │   📁 ndfd/                               — NDFD gridded forecasts
        │   📁 common/                             — CF, CRS, regridding, utilities
        📁 validation/
        │   📁 schemas/                            — GE + CF + STAC schemas
        │   📁 qc/                                 — QC reports for atmospheric fields
        📁 stac/
        │   📁 collections/                        — STAC Collections (HRRR/NDFD/etc.)
        │   📁 items/                              — Cycle-specific STAC Items
        📁 kg/
            📁 enrichers/                          — Adds KG nodes for atmospheric data
            📁 links/                              — Connects atmospheric → hydrology, wildfire, etc.
```

---

## 🌡️ 3. Supported Meteorology Pipelines

### 🌬️ **HRRR Hourly Ingestion (Byte-Range GRIB2)**  
- Primary atmospheric backbone (3 km, hourly).  
- Implements `.idx` parsing & byte-range extraction.  
- Uses CF-standard vertical coordinates.  
- Produces STAC Items per cycle and COG/NetCDF assets.

### 🌩️ **HRRR-Zarr Integration**  
- Cloud-optimized archive for long-term backfill and historical contexts.  
- Supports variable- and chunk-level retrieval.

### 🌦️ **NDFD Forecast Grids**  
- Surface and near-surface fields (temperature, wind, RH, precip).  
- Supports hazard overlays and short-term environmental narrative generation.

### 🌀 **NAM-Nest / RRFS (Optional)**  
- Optional mesoscale integrations for specialized regional simulations.

---

## 🧩 4. Atmospheric ETL Requirements

All meteorology ETL MUST:

- Implement **WAL-first** execution (idempotency, replay safety).  
- Produce **CF-compliant coordinates** and variable metadata.  
- Support **EPSG:4326** and optionally **native atmospheric grids**.  
- Emit **OpenLineage v2.5** events at each ETL stage.  
- Generate **STAC Items & Collections** for all cycles/products.  
- Apply **FAIR+CARE** safeguards (ethical context, sensitivity flags).  
- Record **provenance** through:
  - `kfm:lineage`  
  - PROV-O nodes  
  - JSON-LD graphs

---

## 🧮 5. Byte-Range GRIB2 Workflow (v11.2.2)

### Retrieval  
- Download only needed GRIB2 byte sections using `.idx` index.  
- Avoid full-file downloads at all costs.

### Decode  
- Decode slices into CF-compliant structures via wgrib2 or python-eccodes.  
- Preserve physical units (Pa, m/s, K, mm).

### Harmonize  
- Standardize vertical axes (pressure, height AGL).  
- Regrid/clip Kansas extent + buffer.  
- Convert to COG/NetCDF/Zarr as appropriate.

### Publish  
- Create and validate STAC Items.  
- Populate STAC Collections:  
  - `hrrr_hourly_conus`  
  - `hrrr_kansas`  
  - `ndfd_surface`  
- Create Knowledge Graph nodes for all variables and slices.

---

## 🌐 6. STAC / DCAT / JSON-LD Standards

**STAC Items MUST include:**

- `bbox`, `geometry`, `proj:*`  
- `raster:*` bands  
- `hrrr:variables` (KFM extension)  
- `via:*` (byte-range source metadata)  
- `kfm:lineage` + `kfm:care`  
- OpenLineage run ID  

**STAC Collections MUST include:**

- Spatial + temporal extent  
- Variables summary  
- Provider list  
- Keywords (`meteorology`, `forecast`, `hrrr`, etc.)

**DCAT Entries MUST include:**

- Access URLs  
- License  
- Attribution (NOAA)  
- Temporal coverage & version tags  
- JSON-LD context generation

---

## 🧱 7. Reliability & Governance

Atmospheric pipelines MUST:

- Use WAL checkpoints  
- Provide deterministic ETL flows  
- Maintain reproducibility for backfills  
- Provide dry-run safety  
- Validate:
  - Units  
  - CF compliance  
  - Vertical axes  
  - Spatial alignment  
- Respect CARE constraints:
  - Avoid protected community inference  
  - Apply sovereignty rules when integrated with landscape layers

Promotion gates require:

- STAC valid  
- DCAT valid  
- GE tests pass  
- Carbon/energy telemetry emitted  
- Governance-approved lineage

---

## 🧠 8. Focus Mode v3 Integration

Atmospheric pipelines supply:

- Hourly or sub-hourly atmospheric slices  
- Weather-aware narrative blocks  
- Time-aligned multi-domain overlays  
- Environmental scenario summaries

Narratives such as:

- “Wind shift toward the corridor at 19:00 may increase smoke transport.”  
- “Overnight cooling reduces visibility across river plains.”  
- “Precipitation pulsing influences soil moisture models downstream.”

All Focus Mode narratives follow **Focus Transformer v3** safety rules.

---

## 🔮 9. Future Extensions (Roadmap)

- Integration of HRRR-Smoke / HRRR-Fire.  
- Fine-scale air quality integration with BlueSky.  
- NOAA RRFS (when operational).  
- AI-based atmospheric downscaling.  
- Real-time hazard synthesis (wind × fire × precip × hydrology).  
- Meteorology-driven archaeological site risk narratives.

---

## 🕰 10. Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Canonical v11.2.2 rewrite; added badges, footer, telemetry, KG specs.  |
| v11.2.0 | 2025-11-27 | Initial Meteorology Pipeline Index for HRRR/byte-range/Zarr workflows. |

---

<div align="center">

## 🌬️ **Kansas Frontier Matrix — Meteorology Pipelines (v11.2.2)**  
*Atmospheric intelligence for an environmental Kansas — reproducible · governed · FAIR+CARE aligned.*  

  
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.2-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Meteorology-gold" />
<img src="https://img.shields.io/badge/OpenLineage-v2.5-informational" />
<img src="https://img.shields.io/badge/Atmosphere-Pipelines-lightgrey" />

  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.2 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Pipelines](../README.md) ·  
[⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·  
[📘 KFM Documentation Home](../../README.md)

</div>

