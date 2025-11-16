---
title: "🗺️ Kansas Frontier Matrix — LiDAR Relief Visualization (SVF + LRM Integration · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/visualization/lidar-relief-visualization.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Biannual · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/visualization-terrain-v2.json"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "lidar-relief-visualization"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E2"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — LiDAR Relief Visualization (SVF + LRM Integration)**  
`docs/guides/visualization/lidar-relief-visualization.md`

**Purpose**  
Define and standardize terrain visualization workflows — **Sky-View Factor (SVF)** and **Local Relief Model (LRM)** —  
for LiDAR-based archaeological and geomorphological prospection in Kansas Frontier Matrix (KFM).  

Ensures **reproducible**, **FAIR+CARE v2–aligned** visualizations that support discovery of subtle landscape features  
(e.g., buried mounds, trails, terraces, paleochannels) while respecting **sovereignty**, **sensitivity**, and  
**sustainability** requirements.

</div>

---

# 📘 Overview

The **Sky-View Factor (SVF)** and **Local Relief Model (LRM)** techniques enhance LiDAR Digital Elevation Models (DEMs)  
by emphasizing fine-scale terrain structure while suppressing illumination-direction bias and large-scale topography.

Within KFM, SVF and LRM are treated as **core raster derivatives**, feeding:

- Archaeological prospection  
- Hydrological mapping & paleohydrology  
- Geomorphology / landform classification  
- Hazard & erosion modeling  
- Story Nodes and Focus Mode v2 maps  

This guide covers:

- Directory and data layout  
- SVF & LRM parameter recommendations  
- Processing workflows (GRASS GIS / RVT / QGIS / Whitebox)  
- Integration with KFM MapLibre UI & STAC  
- FAIR+CARE v2 + sovereignty generalization patterns  
- Telemetry v2 & Lineage v2 hooks

---

# 🗂️ Directory Layout (Canonical · v10.4.2)

~~~text
KansasFrontierMatrix/
├── data/
│   ├── raw/
│   │   └── lidar/                         # Source LAS/LAZ tiles, DEMs
│   ├── work/
│   │   └── terrain/
│   │       ├── tmp/                       # Intermediate rasters, masks
│   │       └── staging/                   # Validation-ready derivatives
│   └── processed/
│       ├── lidar/
│       │   ├── dem/                       # Harmonized DEMs
│       │   ├── svf/                       # Sky-View Factor outputs (COGs)
│       │   ├── lrm/                       # Local Relief Models (COGs)
│       │   └── combined/                  # Composite visualizations (SVF+LRM etc.)
│       └── lineage/                       # Lineage v2 bundles for terrain pipelines
│
├── docs/
│   ├── guides/visualization/              # Visualization guides (this file, etc.)
│   └── standards/telemetry/               # Telemetry schemas (terrain, visualization)
│
└── src/pipelines/terrain/
    ├── svf_lrm_pipeline.py                # Automated SVF/LRM pipeline orchestration
    ├── svf.py                             # SVF generation logic
    ├── lrm.py                             # LRM & smoothing logic
    ├── combine.py                         # Composite generation (SVF+LRM)
    ├── lineage.py                         # Lineage v2 builder for terrain products
    └── telemetry.py                       # Telemetry v2 emission for SVF/LRM runs
~~~

---

# 🧩 Techniques Overview

| Technique | Concept                                                                 | Visualization Goal                                             |
|----------|-------------------------------------------------------------------------|-----------------------------------------------------------------|
| **SVF**  | Fraction of unobstructed sky visible from each DEM cell (openness).     | Highlight depressions, ditches, ramps, and enclosure features. |
| **LRM**  | Removes broad-scale topography via smoothing & subtraction.             | Emphasize subtle local deviations (platforms, embankments).    |

SVF is relatively **illumination-invariant**, while LRM acts as a **high-pass filter** on relief.

---

# ⚙️ Parameter Guidelines (KFM Defaults)

These ranges are recommended **starting points**; always tune per dataset & project:

| Technique | Parameter       | Typical Range      | Notes                                                |
|----------|-----------------|--------------------|------------------------------------------------------|
| SVF      | Search radius   | 5–25 m             | Smaller → micro-relief; larger → broader features    |
|          | Directions      | 8–32               | More directions → reduced azimuthal bias             |
|          | Min. angle      | 0–5°               | Higher → stronger depth exaggeration                 |
| LRM      | Filter radius   | 5–50 m             | Defines “local” scale; tune to feature size          |
|          | Smoothing type  | Gaussian/mean/morph | Gaussian is preferred for continuous surfaces       |
|          | Normalization   | 0–255 (optional)   | Improves interpretability and export to 8-bit COG    |

**Resolution note:**  
Parameters should scale with DEM resolution (e.g., 1 m vs 3 m vs 10 m).

---

# 🧾 Example Software Workflows

## GRASS GIS

```bash
# Sky-View Factor
r.skyview input=dem output=svf n_directions=16 maxdistance=20

# Local Relief Model
r.local.relief input=dem output=lrm filter_radius=15
````

## Relief Visualization Toolbox (RVT)

* Use RVT for:

  * SVF
  * Slope & Openness
  * Multi-directional Hillshades
  * LRM

Export GeoTIFFs and convert to **COG** with `gdal_translate` (`-of COG`).

## QGIS Workflow

1. Generate SVF (RVT/GRASS/Whitebox).

2. Generate LRM via `Raster → Terrain Analysis → Local Relief Model` or plugin.

3. In Raster Calculator:

   ```text
   ("SVF@1" * 0.6) + ("LRM@1" * 0.4)
   ```

4. Adjust color ramps, brightness/contrast, and export as COG.

5. Register in STAC as visualization asset (`roles: ["overview","visual"]`).

---

# 🧩 Integration with KFM MapLibre UI

SVF/LRM COGs are typically added as **non-interactive visual layers** in MapLibre,
stacked **below** vector layers and **above** basemap.

* **Layer types:** raster layers with discrete or continuous colormaps.
* **Tokenization:** colors come from `map.tokens.ts` tokens, e.g. `color.map.relief.low`, `color.map.relief.high`.
* **Controls:** legend toggles to show/hide SVF/LRM and composites.
* **Focus/Story integration:** clicking an archaeological Story Node zooms to relevant SVF/LRM patch.

STAC examples:

```json
{
  "assets": {
    "svf": {
      "href": "s3://kfm-data/lidar/svf/region-01_svf.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data","visual"],
      "title": "Sky-View Factor",
      "kfm:careLabel": "sensitive"
    },
    "lrm": {
      "href": "s3://kfm-data/lidar/lrm/region-01_lrm.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data","visual"],
      "title": "Local Relief Model"
    }
  }
}
```

---

# ⚖️ FAIR+CARE v2 & Sovereignty Protections

LiDAR-derived visualizations may reveal:

* Indigenous landscapes and sacred sites
* Burial mounds and ceremonial structures
* Historically sensitive infrastructure or defense works

CARE v2 requires:

* `careLabel` classification:

  * `public` — OK for general visualization
  * `sensitive` — generalized shapes; no coordinate-level publishing
  * `restricted` — only coarse or masked visualizations

* Masking strategies applied *before* public publication:

  * cropping out restricted AOIs,
  * H3-based generalization for geometry,
  * using low-resolution or blurred composites for public maps.

Governance metadata:

```json
{
  "kfm:careLabel": "restricted",
  "kfm:maskingStrategy": "h3_r5",
  "kfm:sovereigntyFlags": ["tribal_overlap","archaeological_site"],
  "kfm:lineageRef": "data/processed/lineage/lidar-svf-lrm/v1.0.0.jsonld"
}
```

Sensitive fullscreen layers may only be accessible in **controlled contexts**
(e.g., research logins or non-public deployments) based on Governance Charter decisions.

---

# 📡 Telemetry v2 for Terrain Visualization

Terrain visualization pipelines MUST emit Telemetry v2 metrics:

* `pipeline`: `"terrain-visualization"` or domain-specific
* `stage`: `"preprocess"|"publish"|"runtime"`
* `run_id`: unique ID
* `status`: run outcome
* `duration_ms`: pipeline duration
* `pixels_processed`: count of DEM cells processed
* `energy_wh`, `co2_g`: sustainability metrics
* `care_violations`: count of governance issues
* `sovereigntyConflicts`: count of conflicts found/resolved

Saved to:

```text
data/telemetry/terrain-visualization.ndjson
```

Aggregated into:

```text
releases/v10.4.2/pipeline-telemetry.json
```

---

# 🧬 Lineage v2 (Terrain Pipelines)

Lineage for SVF/LRM pipelines must:

* Capture DEM sources (USGS/USDA/etc.)
* Document the **full processing chain** (reprojection, resampling, SVF, LRM, combination)
* Embed CARE v2 metadata and telemetry summary
* Provide links to STAC Items and data contracts

Stored at:

```text
data/processed/lineage/lidar-svf-lrm/<version>.jsonld
```

and validated via:

```text
src/pipelines/terrain/lineage.schema.json
```

---

# 🧩 Archaeological & Geomorphological Case Context (Informative)

KFM is informed by international LiDAR prospection work, e.g.:

* **Maya Lowlands** — terraces, causeways, berms under heavy canopy
* **Central Europe** — prehistoric enclosures highlighted by SVF + Openness
* **Teotihuacan Valley** — faint platforms detected via diffuse SVF
* **Neolithic in Germany** — LRM accentuating ploughed-out cursus monuments

KFM adapts these practices to **Kansas-specific**:

* mound & village archaeology
* river valley terraces & paleo-channels
* historical trails & infrastructure
* land-use changes across settler + Indigenous landscapes

---

# 🧮 Quality & Performance Guidelines

| Aspect         | Target / Guidance                                      |
| -------------- | ------------------------------------------------------ |
| Resolution     | 1–3 m DEMs for micro-relief; 5–10 m for broad features |
| FPS (MapLibre) | ≥ 30 FPS with SVF/LRM active                           |
| Load latency   | initial COG load ≤ 2–3 seconds per tile set            |
| File formats   | COG (GeoTIFF), STAC-compatible                         |
| Color ramps    | colorblind-safe, high-contrast mode available          |

---

# 🧭 Developer Checklist

Before publishing SVF/LRM-based layers:

* [ ] DEM inputs documented and validated (data-contract v3 compliance).
* [ ] SVF & LRM parameters recorded in processing metadata.
* [ ] CARE v2 labels and masking strategies applied.
* [ ] Lineage v2 bundle generated and validated.
* [ ] Telemetry v2 metrics captured and aggregated.
* [ ] STAC Items updated with SVF/LRM assets and metadata.
* [ ] MapLibre UI configuration tested (performance, A11y, CARE overlays).
* [ ] Governance & FAIR+CARE workflows pass (no open violations).

---

# 🕰 Version History

| Version | Date       | Author              | Summary                                                                                  |
| ------: | ---------- | ------------------- | ---------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Terrain & Viz Team  | Upgraded to KFM-MDP v10.4.2; integrated Telemetry v2, CARE v2, Lineage v2, MapLibre docs |
|  v9.7.0 | 2025-11-09 | A. Barta / Focus AI | Initial LiDAR SVF + LRM visualization standard integrated with MCP-DL v6.3               |

---

<div align="center">

**Kansas Frontier Matrix — LiDAR Relief Visualization (v10.4.2)**
Terrain Storytelling × FAIR+CARE v2 × Sustainable Workflows × Archaeological Respect
© 2025 Kansas Frontier Matrix — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Visualization Guides](../README.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
