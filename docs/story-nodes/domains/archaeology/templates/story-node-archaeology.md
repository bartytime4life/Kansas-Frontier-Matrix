---
title: "🏺 Archaeology Story Node Template (KFM v11.2.2)"
path: "docs/story-nodes/domains/archaeology/templates/story-node-archaeology.md"
version: "v11.2.2"
last_updated: "2025-11-30"

template_type: "markdown-authoring-template"
domain: "archaeology"
governance_level: "FAIR+CARE · Indigenous Data Sovereignty"
masking_required: true
schema_ref: "../../../../schemas/json/story-node.schema.json"

license: "CC-BY 4.0"
---

<div align="center">

# 🏺 **Archaeology Story Node — Authoring Template**  
### *Generalized, Ethical, FAIR+CARE-Compliant Narrative Structure*  

Use this template to author archaeology Story Nodes for the  
**Kansas Frontier Matrix (KFM v11)**.

</div>

---

# 🧩 Instructions for Authors

- **Do not** include precise site coordinates.  
- **Do not** mention burial locations, sacred locations, restricted knowledge, or internal site codes.  
- **Do** use generalized geometries (H3 cells, counties, watersheds, broad regions).  
- **Do** clearly separate:  
  - **Observation** (what is documented),  
  - **Interpretation** (supported conclusions),  
  - **Uncertainty** (limited or conflicting data).  
- **Do** assign correct temporal precision (“year”, “century”, “day” only when appropriate).  
- **Do** use the relation patterns from `relation-patterns.md`.

All Story Nodes created with this template must validate against  
`story-node.schema.json`.

---

# 🏺 Story Node Template (Fill In All Sections)

## 🧾 Metadata

**ID (public-safe):**  
Format: `arch-ks-{county-fips}-{slug}-{nn}`  
Example: `arch-ks-165-lower-walnut-village-01`

**Title:**  
Short, descriptive, generalized.  
Example: *Generalized Protohistoric Settlement Near Lower Walnut Creek*

**Summary (2–3 sentences):**  
A short overview used in previews and Focus Mode cards.

---

## 📖 Narrative

### **1. Context & Description (Observation)**  
Describe **documented** features, artifacts, or site forms in a generalized, non-sensitive way.  
Avoid exact counts, coordinates, or burial/sacred details.

*Example prompts:*  
- What is physically present?  
- What is known from surveys or archives?  
- What general environmental setting applies?

---

### **2. Interpretation (Supported Inference)**  
Explain what archaeologists believe these observations mean.  
Reference cultural periods, technological markers, or settlement patterns  
**only when documented**.

---

### **3. Uncertainty & Debates**  
Document disagreements, alternative explanations, or limited data.  
Never “fill in” missing information with speculation.

---

### **4. Archaeological Methods**  
Describe (in safe general form):

- survey type (pedestrian, geophysics, lidar, archival)  
- excavation season/date (generalized)  
- recording techniques (photogrammetry, gridding, scanning)  

Avoid exposing internal field form details.

---

### **5. Sovereignty & Ethical Notes**  
Describe the ethical considerations and any CARE-driven decisions:  

- masking of geometry  
- consultation status  
- cultural sensitivity  
- withheld content  

---

## 🌐 Spacetime

### **Geometry (Generalized GeoJSON)**  
Describe the geometry type and why it is masked:  
County polygon, H3 cell, watershed, park boundary, etc.

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [/* generalized / safe */]
  },
  "properties": {
    "masking_level": "H3-6"
  }
}
```

---

### **Temporal Bounds**

**Start:** `YYYY` or ISO-8601  
**End (optional):** `YYYY`  
**Precision:** `"century"`, `"year"`, `"year-range"`, `"decade"`  
**Original Label:** e.g., `"Protohistoric, ca. 1450–1650 CE"`

---

## 🔗 Relations (Graph Links)

Use only approved patterns from `relation-patterns.md`.

Suggested structure:

```json
[
  {
    "rel": "about",
    "id": "place:arch-ks-165-lower-walnut-village"
  },
  {
    "rel": "references",
    "id": "doc:kshs-1973-arch-report"
  },
  {
    "rel": "counterpoint",
    "id": "story:arch-ks-165-reinterpretation-01"
  }
]
```

---

## 🗃 Sources & Provenance

List:  
- reports  
- datasets  
- maps  
- survey logs (if public)  
- published academic works  
- archival resources  

**Do not** cite restricted internal forms or unpublished coordinates.

---

## 🖼 Media (Optional, STAC-Linked)

Only include **generalized**, **non-sensitive** media.  
Rasters from geophysics, lidar hillshades, or generalized diagrams are acceptable.

Example:

```json
[
  {
    "href": "https://example.org/stac/fort-larned/geophysics/ft1.tif",
    "title": "Generalized Geophysics Raster",
    "mime": "image/tiff",
    "license": "CC-BY 4.0"
  }
]
```

---

# 🕰️ Version History

| Version | Date       | Summary                                                            |
|--------:|------------|--------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed archaeology Markdown template for Story Nodes.    |
| v11.2.1 | 2025-11-29 | Added author instructions, spacetime rules, & sovereignty notes.   |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

