---
title: "🗺️ Kansas Frontier Matrix — Archaeology Spatial Analysis (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/methods/spatial_analysis.md"
version: "v11.0.0"
last_updated: "2025-11-25"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/archaeology-methods-spatial-v11.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Method Specification"
intent: "archaeology-spatial-analysis"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
immutability_status: "version-pinned"
semantic_document_id: "kfm-arch-method-spatial-v11"
doc_uuid: "urn:kfm:docs:archaeology:methods:spatial:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Archaeology Spatial Analysis**  
`docs/analyses/archaeology/methods/spatial_analysis.md`

**Purpose:**  
Define FAIR+CARE-compliant **spatial analysis methods** for archaeology in KFM, including point pattern analysis, density estimation, surface modeling, and landscape metrics, all implemented with generalized geometries, H3 masking, and Focus Mode v3 / Story Node v3 interoperability.

</div>

---

## 📘 Overview

This document specifies how KFM performs **spatial analysis** on archaeological data while:

- Preserving **site confidentiality** and **Indigenous data sovereignty**  
- Operating only on **generalized geometries** (regions, H3 grids, buffered units)  
- Producing **reproducible, provenance-rich** outputs  
- Feeding results into **Focus Mode v3** and **Story Node v3** for narrative use  

Core analysis categories:

- Point pattern analysis (generalized)  
- Kernel density & intensity surfaces (H3-based)  
- Spatial autocorrelation (generalized Moran’s I, Geary’s C)  
- Landscape & terrain metrics (viewshed, cost surfaces)  
- Settlement & route modeling (least-cost paths, corridor analysis)  

All methods are **explicitly prohibited** from revealing or inferring **exact site coordinates** or sensitive feature locations.

---

## 🗂 Directory Layout

```text
docs/
- analyses/
  - archaeology/
    - methods/
      - spatial_analysis.md
      - proximity_statistics.md
```

This file defines **spatial analysis methods**; proximity-specific methods are detailed in `proximity_statistics.md`.

---

## 🧭 General Principles

All archaeology spatial analysis in KFM MUST:

- Use **masked / generalized geometries** only:
  - H3 grids at resolution ≥ 6  
  - Region-scale polygons (watersheds, physiographic regions, counties, buffered corridors)  
- Apply **dynamic H3 generalization** to any sensitive cultural data  
- Exclude:
  - Raw excavation-unit extents  
  - Feature polygons  
  - Raw artifact point coordinates  
- Log every analysis as:
  - A **PROV-O activity** with explicit `prov:used` inputs  
  - A **derived dataset** with STAC-compatible metadata  
- Respect **CARE**:
  - `care:sensitivity`, `care:notes`, `care:review` required on outputs  
  - No outputs enabling reverse-engineering of protected locations  

---

## 📊 Method Families

### 1️⃣ Generalized Point Pattern Analysis

Point-based archaeology data are first:

- Aggregated to **H3 cells** (res ≥ 6), or  
- Aggregated to **region polygons** (e.g. county, watershed, landform unit)  

Allowed statistics:

- **Generalized nearest-neighbor index** (using H3 centroids or region centroids)  
- **Quadrat analysis** on H3 grid / regions  
- **Ripley-style** distance functions using *binned, generalized centroids*, never raw points  

Outputs:

- `kfm:pattern_type` — `"clustered"`, `"random"`, `"dispersed"` (at chosen scale)  
- `kfm:scale_km` — spatial scale in km (must be ≥ 1–2 km depending on sensitivity)  
- `kfm:confidence` — quality of inference based on data density & masking  

### 2️⃣ Kernel Density & Intensity Surfaces

KFM uses **masked kernel density** on:

- H3 counts per cell  
- Aggregated region counts  

Rules:

- **No** cell smaller than H3 res 6  
- Kernels parameterized in **km**, not meters  
- Resulting rasters exported as:
  - COG GeoTIFF (generalized)  
  - Optional H3-intensity per cell  

Used for:

- Generalized intensity surfaces (e.g. “higher relative density of recorded sites”)  
- Cultural landscape Story Nodes (e.g. “high-density interaction corridor”)  

### 3️⃣ Spatial Autocorrelation (Generalized Moran’s I / Geary’s C)

KFM computes **area-based spatial autocorrelation** on:

- Regions (e.g. counties, hydrological units, physiographic provinces)  
- H3 cells (res ≥ 6 only)  

Variables:

- Generalized counts or intensities (e.g. number of known sites per region, generalized artifact categories, modeled environmental variables)  

Outputs:

- `kfm:autocorrelation_stat` — e.g. `"Moran_I"` or `"Geary_C"`  
- `kfm:autocorrelation_value` — numeric statistic  
- `kfm:scale_km` — analysis scale  
- `kfm:notes` — method, weights, and any masking caveats  

Used in:

- Regional clustering assessments  
- Focus Mode explanations (“evidence of clustering at regional scale”)  

### 4️⃣ Terrain & Landscape Metrics

Computations over **open, non-sensitive layers** (elevation, slope, landcover), plus masked cultural layers.

Examples:

- **Viewshed** from generalized lookout regions or fort corridors (approximate, not exact)  
- **Cost-distance surfaces** using:
  - Elevation-derived slope  
  - Landcover (e.g. prairie vs. woodland)  
  - Generalized barriers (rivers, canyons)  
- **Least-cost paths & corridors** between generalized cultural regions  

Outputs:

- `kfm:cost_surface_id` — cost surface identifier  
- `kfm:path_type` — `"least_cost_path"` or `"cost_corridor"`  
- `kfm:distance_km` — total path distance (generalized)  
- `kfm:notes` — variables used, masking applied  

These outputs are used for:

- Story Nodes describing **travel, routes, and constraints**  
- Focus Mode explanations of **environmental affordances**  

---

## 🧱 Spatial Generalization & Masking

All archaeology spatial analyses must align with KFM’s **Dynamic H3 Generalization Standard** and **CARE masking**:

- For Indigenous sites or sacred locations:
  - Use broader H3 or region levels  
  - Optionally jitter or snap region boundaries to non-identifying shapes  
- For highly sensitive contexts (e.g. burials):
  - Only allow aggregated reporting at **large regional frames** (multi-county / multi-watershed)  
  - No detailed pattern statistics, only coarse narrative summaries  

Any analysis that could materially aid illicit site discovery is **prohibited**.

---

## 🔗 STAC, DCAT & PROV-O Integration

Spatial analysis outputs are **derived datasets** and MUST be:

- Represented as **STAC Items** or `scientific` extension fields attached to Items  
- Cataloged in **DCAT 3.0** as derived datasets  
- Linked with **PROV-O**:

  - `prov:Activity` — describes the computation (tool, parameters, date)  
  - `prov:used` — input layers (generalized cultural, environmental, hydrology, etc.)  
  - `prov:wasGeneratedBy` — output dataset → activity  

Key metadata:

- `kfm:method_name` — e.g. `"generalized_morans_i"`, `"masked_kde"`, `"viewshed_generalized"`  
- `kfm:software` — library / version or pipeline ID  
- `kfm:parameters` — serialized parameter summary (bandwidth, neighbors, weight matrix type)  

---

## 🔍 Focus Mode & Story Node Integration

Spatial analysis is not just numeric; it supports **narrative and interactive exploration**.

### Focus Mode v3

- When focusing on a **place**, Focus Mode can surface:
  - Nearby generalized cultural clusters  
  - Landscape affordances (e.g. “elevated ridge near main corridor”)  
  - Relationship to hydrology and terrain  

- When focusing on an **event or route**, Focus Mode can:
  - Highlight generalized least-cost paths  
  - Show density surfaces relevant to that era  
  - Provide textual explanations referencing spatial metrics  

### Story Node v3

Story Nodes may reference spatial analysis results via:

- `spacetime.geometry` — generalized footprints enriched by analysis  
- `spacetime.place_labels` — region names (“central Smoky Hill region”, “Arkansas River corridor”)  
- Narrative fields that describe patterns qualitatively, **without** precise directions to sensitive sites.

No Story Node may embed or imply specific directions to a sensitive cultural location.

---

## 🧪 CI & Validation Requirements

This method specification is enforced by:

- `archaeology-spatial-validate.yml`  
- CARE audit workflow for derived spatial outputs  
- PROV-O lineage validator  
- STAC + DCAT conformance checks for derived datasets  
- Markdown protocol validator (KFM-MDP v11.0.0)  
- FAIR+CARE metadata checker  

Outputs of spatial analyses MUST be testable and reproducible, with stable seeds and parameter logs where stochastic elements are used.

---

## 🕰 Version History

| Version | Date       | Author                                   | Notes                       |
|---------|------------|-------------------------------------------|-----------------------------|
| v11.0.0 | 2025-11-25 | Archaeology Working Group · FAIR+CARE Council | Initial spatial methods spec |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · MCP-DL v6.3 · STAC 1.0.0 · DCAT 3.0  

[⬅ Back to Archaeology Methods](../README.md) ·  
[📑 Metadata Standards](../../../standards/README.md) ·  
[📘 Master Guide v11](../../../reference/kfm_v11_master_documentation.md)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~markdown
