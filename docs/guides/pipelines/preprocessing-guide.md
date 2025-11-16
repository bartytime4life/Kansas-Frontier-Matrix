---
title: "🧼 Kansas Frontier Matrix — Remote Sensing Preprocessing Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/preprocessing-guide.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/preprocessing-guide-v2.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "remote-sensing-preprocessing"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E1"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# 🧼 **Kansas Frontier Matrix — Remote Sensing Preprocessing Guide**  
`docs/guides/pipelines/preprocessing-guide.md`

**Purpose:**  
Define the authoritative **preprocessing standard** for Remote Sensing pipelines within the Kansas Frontier Matrix (KFM).  
Preprocessing transforms raw STAC assets into **deterministic, harmonized, CARE-safe, lineage-complete** geospatial  
products suitable for analytics, hazard modeling, AI summarization, and multi-surface publishing (STAC, DCAT, Neo4j, RDF).

This guide replaces the v10.3.1 version with a **fully upgraded KFM v10.4.2 specification**.

</div>

---

# 📘 Overview

Remote sensing preprocessing is the **bridge between ingestion and analytics**.  
It standardizes diverse sensor inputs into consistent, validated outputs aligned with:

- Deterministic transforms  
- FAIR+CARE v2 governance  
- Semantic versioning  
- Telemetry v2 (energy, CO₂e, masking metrics)  
- SLSA-style provenance + lineage  
- Raster integrity and spatial correctness  
- Multi-sensor harmonization (optical, SAR, thermal, multispectral, DEM)  

Outputs are placed into:

~~~text
data/processed/<dataset>/<version>/
~~~

and become eligible for **staging → publishing** workflows.

---

# 🗂️ Directory Layout (Canonical KFM Preprocessing Layer)

~~~text
src/pipelines/remote-sensing/preprocessing/
├── preprocess.py                        # Pipeline orchestrator
├── cloud_mask.py                        # Cloud/shadow/snow/cirrus mask logic
├── harmonize_gsd.py                     # Resample to target GSD (10m/30m/etc.)
├── reprojection.py                      # Reproject using GDAL/PROJ
├── sar_rtc.py                           # RTC for Sentinel-1 GRD
├── radiometric_normalization.py         # TOA, SR, emissivity, normalization
├── bandstack.py                         # Unified bandstack + metadata
├── masks/                               # Shared mask functions + sovereignty
│   ├── sovereignty_mask.py              # CARE v2 masking logic (H3 R7/R5)
│   └── aoi_mask.py                      # AOI-based exclusion masks
└── utils/                               # GDAL, rasterio, numpy helpers
~~~

---

# 🌐 Full-Page Preprocessing Architecture (KFM-Styled Mermaid)

```mermaid
flowchart TD

subgraph INGEST["STAC Ingest<br/><span style='font-size:12px'>raw bands · metadata · geometry</span>"]
    A["Raw STAC Assets"]
end

subgraph MASKS["Cloud / Shadow / Snow / Sovereignty Masks"]
    B["Cloud & Shadow Masking<br/><span style='font-size:12px'>SCL · QA_PIXEL · QC flags</span>"]
    B2["Sovereignty Masking<br/><span style='font-size:12px'>CARE v2 · H3 Generalization</span>"]
end

A --> B --> B2

subgraph REPROJ["Reprojection<br/><span style='font-size:12px'>Native CRS → Target CRS (EPSG:4326)</span>"]
    C["GDAL / PROJ Warp<br/><span style='font-size:12px'>grid-aligned affine</span>"]
end

B2 --> C

subgraph GSD["GSD Harmonization<br/><span style='font-size:12px'>10m · 30m · 100m</span>"]
    D["Resample & Align<br/><span style='font-size:12px'>nearest/bilinear</span>"]
end

C --> D

subgraph RADIO["Radiometric Normalization"]
    E["TOA / SR / log-scale<br/><span style='font-size:12px'>sensor-specific correction</span>"]
end

D --> E

subgraph SAR["SAR Terrain Correction (RTC)"]
    F["Sigma0 RTC<br/><span style='font-size:12px'>DEM · layover/shadow mask</span>"]
end

E --> F

subgraph BANDS["Bandstack Assembly<br/><span style='font-size:12px'>analytics-ready surfaces</span>"]
    G["Stack Bands + Masks<br/><span style='font-size:12px'>optical · SAR · masks</span>"]
end

F --> G

subgraph STAGING["Staging<br/><span style='font-size:12px'>GX-validated · CARE-labeled · checksum-locked</span>"]
    H["Ready for Publish / Analytics"]
end

G --> H

classDef ingest fill:#ebf8ff,stroke:#2b6cb0,color:#1a365d;
classDef masks fill:#fff5f5,stroke:#e53e3e,color:#742a2a;
classDef reproj fill:#faf5ff,stroke:#805ad5,color:#553c9a;
classDef gsd fill:#f0fff4,stroke:#38a169,color:#22543d;
classDef radio fill:#fffbea,stroke:#dd6b20,color:#7b341e;
classDef sar fill:#e6fffa,stroke:#319795,color:#285e61;
classDef bands fill:#f7fafc,stroke:#4a5568,color:#2d3748;
classDef staging fill:#fefcbf,stroke:#b7791f,color:#744210;

class INGEST ingest;
class MASKS masks;
class REPROJ reproj;
class GSD gsd;
class RADIO radio;
class SAR sar;
class BANDS bands;
class STAGING staging;
````

---

# 🧼 1. Cloud, Shadow & Snow Masking

Masking is **mandatory** for all optical sensors.

## Sources per sensor

| Sensor         | Mask Input                       |
| -------------- | -------------------------------- |
| Landsat C2 L2  | QA_PIXEL / QA_RADSAT             |
| Sentinel-2 L2A | SCL (Scene Classification Layer) |
| MODIS/VIIRS    | QC Flags                         |
| NAIP           | QA metadata                      |
| PlanetScope    | UDM2                             |

Outputs:

* `cloud_mask.tif`
* `shadow_mask.tif`
* `snow_mask.tif`
* `valid_mask.tif`

Telemetry v2:

* `cloud_pct`, `shadow_pct`, `snow_pct`, `valid_pct`
* `mask_duration_ms`

---

# 🛡 2. Sovereignty & CARE v2 Masking (Mandatory)

CARE v2 rules require:

* **H3 R7** generalization for sensitive sites
* **H3 R5** generalization for restricted sites
* Complete removal of exact pixel values in protected AOIs
* Optional centroid substitution

Outputs:

* `sovereignty_mask.tif`
* CARE attributes embedded in metadata

Telemetry:

* `care_violations`
* `masked_pixels`
* `sovereignty_conflicts`

---

# 📐 3. GSD Harmonization

All datasets must harmonize to:

* 10m (Sentinel-1/2)
* 30m (Landsat)
* 1m/60cm (NAIP)
* 250–1000m (MODIS)

Procedure:

1. Resample (nearest for masks, bilinear for rasters)
2. Align to reference grid
3. Confirm target GSD via GX: `gsd_check.min_resolution`

Outputs:

* `*_gsd.tif`
* Telemetry: `pixels_resampled`

---

# 🌐 4. Reprojection (GDAL/PROJ)

KFM publishes everything in **EPSG:4326**.

Requirements:

* Use GDAL Warp with `-t_srs EPSG:4326`
* Preserve pixel alignment
* Ensure affine transform stability

Outputs:

* `*_reproj.tif`

Telemetry:

* `warp_duration_ms`
* `pixels_reprojected`

---

# 🛰 5. Radiometric Normalization

### Landsat

* Apply scale factors
* Convert TOA → SR when needed
* Handle RADCOR flags

### Sentinel-2

* Divide by 10,000
* Handle saturation and negative outliers

### Thermal products

* Use K1/K2 constants

Telemetry:

* `radiometric_valid_pct`
* `clipped_pixels`

---

# 🗻 6. SAR Terrain Correction (RTC)

RTC includes:

* DEM resampling (USGS 3DEP COG)
* Radiometric calibration
* Geometry correction
* Layover & shadow mask
* Optional multi-looking

Outputs:

* `rtc_sigma0.tif`
* `rtc_mask.tif`

Telemetry:

* `rtc_duration_ms`
* `layover_pct`
* `shadow_pct`

---

# 🧱 7. Bandstack Generation

Bandstacks unify:

* Spectral bands
* RTC SAR
* Masks
* Thermal bands
* Metadata

Directory:

```text
bandstack/
├── B02.tif
├── B03.tif
├── B04.tif
├── B08.tif
├── cloud_mask.tif
├── valid_mask.tif
└── metadata.json
```

---

# 🛡 8. CARE & Governance Metadata Injection

Required metadata fields in bandstack and rasters:

* `kfm:careLabel`
* `kfm:maskingStrategy`
* `kfm:sovereigntyFlags[]`
* `kfm:processingSteps[]`
* `kfm:checksum_sha256`
* `kfm:lineageRef`
* `kfm:telemetryRef`

---

# 📡 9. Telemetry v2 (NDJSON)

Saved at:

```text
data/processed/<dataset>/<version>/telemetry.ndjson
```

Must include:

* stage
* duration_ms
* pixels_processed
* masked_pct
* energy_wh
* co2_g
* care_violations
* sovereignty_conflicts
* memory_mb

Aggregated to:

```text
releases/v10.4.2/pipeline-telemetry.json
```

---

# 🧬 10. Lineage (CIDOC + PROV-O + CARE v2)

Stored at:

```text
data/processed/<dataset>/<version>/lineage.jsonld
```

Includes:

* PROV `prov:Activity`, `prov:Entity`, `prov:Agent`
* CARE metadata
* Input → Output derivation
* Sensor-specific processing metadata
* Spatial footprint lineage

Validated against:

```text
src/pipelines/remote-sensing/lineage/schemas/lineage.schema.json
```

---

# 🧪 11. GX Validation (Staging Gate)

Must validate in:

```text
data/work/staging/<pipeline>/
```

Checks:

* GSD correctness
* Band presence
* Mask correctness
* Value range checks
* Metadata completeness
* CARE compliance

Pass → eligible for publishing.
Fail → quarantined.

---

# 🧭 Developer Workflow

```bash
# Preprocess
python preprocess.py --config <config>

# Validate via GX
great_expectations checkpoint run preprocessing_suite

# Promote to processed/
python promote.py

# Optional: publish
python publish.py
```

---

# 🕰 Version History

| Version | Date       | Summary                                                                                                                      |
| ------: | ---------- | ---------------------------------------------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Full KFM v10.4.2 rewrite: CARE v2, telemetry v2, lineage v2, SAR RTC upgrade, harmonization improvements, KFM-styled diagram |
| v10.3.1 | 2025-11-14 | Initial preprocessing guide                                                                                                  |

---

<div align="center">

**Kansas Frontier Matrix — Remote Sensing Preprocessing Guide (v10.4.2)**
Deterministic Remote Sensing × FAIR+CARE v2 × Provenance Integrity × Geospatial Trust
© 2025 KFM — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
