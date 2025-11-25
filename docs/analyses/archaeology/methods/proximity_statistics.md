---
title: "📏 Kansas Frontier Matrix — Archaeology Proximity Statistics (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/methods/proximity_statistics.md"
version: "v11.0.0"
last_updated: "2025-11-25"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/archaeology-methods-proximity-v11.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Method Specification"
intent: "archaeology-proximity-statistics"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
immutability_status: "version-pinned"
semantic_document_id: "kfm-arch-method-proximity-v11"
doc_uuid: "urn:kfm:docs:archaeology:methods:proximity:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 📏 **Kansas Frontier Matrix — Archaeology Proximity Statistics**  
`docs/analyses/archaeology/methods/proximity_statistics.md`

**Purpose:**  
Define FAIR+CARE-compliant **proximity-based spatial statistics** used in KFM archaeology workflows, including generalized distance metrics, H3-based masking, cultural-landscape inference, and Focus Mode v3 interoperability.

</div>

---

# 📘 Overview

Proximity statistics measure **generalized distances** between archaeological entities such as:

- Cultural features (generalized polygons)  
- Depositional sequences  
- Paleoenvironments  
- Hydrological features  
- Physiographic regions  
- Artifact clusters (H3-binned, not point-level)  

These metrics support:

- **Cultural-landscape modeling**  
- **Settlement distribution analysis**  
- **Resource-proximity models**  
- **Risk & sensitivity zoning**  
- **Focus Mode v3 contextual reasoning**  
- **Story Node v3 spatial-narrative generation**

To comply with CARE & masking requirements, **no feature-level or point-level coordinates are ever used**. All statistics operate on:

- **Generalized H3 grids (res ≥ 6)**  
- **Region-scale polygons**  
- **Buffered hydrological units**  
- **Masked site-area footprints**

KFM prohibits analytical methods that would infer, predict, or reverse-engineer **exact site or feature locations**.

---

# 🧭 Proximity Metrics (Generalized)

Below are the KFM-approved proximity metrics.

## 📐 1. Region-to-Region Distance (RRD)

Distance between two generalized cultural regions.

- Input: Region A polygon, Region B polygon  
- Transformation: Convert to convex hulls → H3 region summary  
- Metric: Minimum hull-to-hull great-circle distance  

Used in cultural-interaction models and Story Node co-occurrence inference.

## 🟦 2. H3 Grid-Based Proximity (H3-P)

Distance between two area-generalized H3 cells.

- H3 resolutions 6–4 allowed  
- No res 7–15 (avoid micro-resolution clustering)  
- Metric: `h3Distance(cellA, cellB)`  

Suitable for environmental-proximity modeling.

## 🏞 3. Hydro-Proximity (HP)

Distance between a cultural region and a **generalized** hydrological feature.

- Hydrology generalized to watershed units  
- Metric: centroid-to-centroid minimum distance  

Feeds into settlement-hydrology models.

## 🧱 4. Stratigraphic-Sequence Proximity (SSP)

Vertical or horizontal proximity expressed **independently of site coordinates**.

- Vertical: `|depthA - depthB|`  
- Horizontal: region-to-region proxy from generalized site polygons  
- Used only in profiles already generalized  

Maintains archaeological sensitivity boundaries.

## 🏜 5. Paleolandscape Proximity (PLP)

Distance from cultural regions to reconstructed paleolandscape features.

- Inputs: generalized paleosurface polygons, watershed models  
- Metric: minimum hull-to-hull distance  
- Supports paleoenvironmental inference in Focus Mode v3.

---

# 🧱 Spatial Generalization Rules

To comply with CARE, all KFM archaeological proximity analyses MUST:

- Use **generalized region footprints** (never excavation units, features, points).  
- Use **H3 ≥ 6** or equivalent region abstraction.  
- Mask or distort small areas susceptible to inference.  
- Never expose distances smaller than **250–500 m** depending on cultural sensitivity tier.  
- Use dynamic H3 generalization for Indigenous cultural heritage regions.  
- Avoid any operation enabling re-localization of protected sites.

---

# 🧪 Statistical Outputs

Proximity statistics produce the following output fields:

| Field | Description |
|-------|-------------|
| `kfm:proximity_type` | Identifier for method used (`RRD`, `H3-P`, `HP`, `SSP`, `PLP`) |
| `kfm:distance_km` | Region-generalized distance (km) |
| `kfm:confidence` | Confidence rating (0–1) based on dataset quality |
| `care:sensitivity` | `"generalized"` or `"masked"` |
| `prov:wasGeneratedBy` | Link to PROV-O activity |
| `prov:used` | Input datasets used in the computation |
| `kfm:notes` | Methodological notes & flags |

Outputs are integrated into:

- Focus Mode v3 reasoning nodes  
- Story Node `spacetime` supplemental metadata  
- Stratigraphy and settlement interpretation layers  

---

# 🔗 STAC + PROV-O Integration

Proximity statistics are not standalone datasets; they are:

- Stored as **derived assets**  
- Expressed as **STAC Item extensions**  
- Logged using **PROV-O** activity relationships  

Required for every statistical run:

- `prov:Activity` describing computation  
- `prov:Entity` referencing input datasets  
- `prov:wasGeneratedBy` linking output → computation  
- SHA-256 checksums for all generated CSV/JSON files  

---

# 🧰 Example Output Block (Generalized)

```json
{
  "kfm:proximity_type": "RRD",
  "kfm:distance_km": 12.4,
  "kfm:confidence": 0.83,
  "care:sensitivity": "generalized",
  "prov:wasGeneratedBy": "prov/proximity-run-2025-11-25.json",
  "prov:used": [
    "collections/generalized-cultural-regions.json",
    "collections/generalized-hydrology.json"
  ],
  "kfm:notes": "Region-to-region distance using generalized hulls; compliant with CARE masking."
}
```

---

# 🔍 Focus Mode & Story Node Integration

Proximity statistics enrich:

### **Focus Mode v3**
- Landscape context  
- Hydrology relationships  
- Cultural-region adjacency  
- Stratigraphy-environment interactions  

### **Story Node v3**
- Narrative evidence of proximity-based relationships  
- Temporal placement using OWL-Time  
- Spatial generalization compatible with GeoSPARQL  
- Enhanced cultural-landscape summaries  

No Story Node may ever embed precise site-level locations.

---

# 🧪 CI Validation Requirements

This method specification is governed by:

- `archaeology-proximity-validate.yml`  
- CARE audit workflow  
- PROV-O lineage validator  
- Spatial generalization validator (H3 masking)  
- STAC extension validator  
- KFM-MDP v11 Markdown validator  

All validation must pass before merging.

---

# 🕰 Version History

| Version | Date | Author | Notes |
|---------|--------|-------------------------------|------------------------|
| v11.0.0 | 2025-11-25 | Archaeology Working Group · FAIR+CARE Council | Initial release |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · MCP-DL v6.3 · STAC 1.0.0 · DCAT 3.0  

[⬅ Back to Archaeology Methods](../README.md) ·  
[📑 Metadata Standards](../../../standards/README.md) ·  
[📘 Master Guide v11](../../../reference/kfm_v11_master_documentation.md)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~markdown
