# 📖 Arkansas River Basin Cultural Landscape Region — Context v1  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/metadata/context-arkansas-river-basin-region-v1.md`

> **Non-authoritative narrative companion.**  
> Canonical truth for this region lives in:
> - Region spec: `../README.md`  
> - Region metadata JSON-LD: `dcat-arkansas-river-basin-region-v1.jsonld`  
> - STAC Collection/Item JSON: `../../stac/`  
> - PROV-O logs: `../../../provenance/`  

---

## 🧭 1. Region Snapshot (Human View)

- **Name:** Arkansas River Basin Cultural Landscape Region  
- **Kind:** Drainage-centered, multi-phase cultural landscape  
- **Scale:** Basin and major tributaries within the KFM domain (generalized)  
- **Primary Uses in KFM:**
  - Basin-scale **context layer** for site- and landscape-level analyses  
  - Spatial anchor for **Story Nodes** about riverine movement, exchange, and settlement  
  - Regional frame for **Focus Mode** when users explore hydrology, culture, and time together  

The region is not a legal, political, or sovereign boundary. It is an **analytic construct**: a generalized envelope where hydrology, geomorphology, and cultural evidence overlap strongly enough to treat the Arkansas River corridor as a coherent interpretive unit.

---

## 🌊 2. Environmental & Geomorphic Frame

The Arkansas River Basin region, as modeled in KFM, is anchored in:

- **Hydrology**
  - Main Arkansas River corridor and key tributaries within the project’s spatial extent  
  - Floodplains, low terraces, and adjacent valley bottoms  
  - Major confluences and corridor segments that are important for movement and resource access  

- **Geomorphology**
  - Multi-terrace valley systems (older terraces, low alluvial surfaces, active floodplains)  
  - Bluff lines and valley walls that constrain movement and settlement options  
  - Zones of alluvial deposition and erosion that influence site preservation and visibility  

- **Ecology**
  - Riparian forests and floodplain environments  
  - Adjacent upland ecotones with grazing, hunting, and agricultural potential  
  - Resource patches (e.g., soils, vegetation, water access) that interact with cultural practice  

The **generalized region geometry** is derived from these environmental structures but deliberately smoothed and simplified to avoid encoding internal survey or site boundaries.

---

## 🕰️ 3. Cultural–Temporal Frame

The Arkansas River Basin region is used as a **multi-phase analytical framework**, spanning:

- **Late Prehistoric**
  - Riverine settlement clustering and agricultural strategies  
  - Use of valley corridors for movement, interaction, and resource acquisition  

- **Protohistoric**
  - Intensified intercultural movements along the Arkansas corridor  
  - Intersections between Indigenous polities, trade networks, and early colonial presence  

- **Early Historic (as governed)**
  - Basin as a route for migration, trade, and conflict  
  - Changes in land use, settlement distribution, and environmental impacts  

Temporal coverage and phase labels are governed in:

- Region metadata JSON-LD (`dct:temporal`, `kfm:culture_phase`)  
- STAC temporal extents and provenance timespans  

This context file **does not introduce new periods**; it only narrates the existing temporal frame.

---

## 🧪 4. Evidence & Methods (Narrative Summary)

Region definition synthesizes multiple evidence streams (details in metadata + provenance):

- **Archaeological Records (internal-level detail)**
  - Survey data and site records along the Arkansas River and tributaries  
  - Distributional patterns (clustering, gaps) used qualitatively, not exposed directly  

- **Geomorphology & Hydrology**
  - Basin outlines, sub-basin boundaries, and valley-form mapping  
  - Terrace sequences, floodplain extents, and channel migration zones  

- **Historical & Ethnohistoric Sources**
  - Cartographic materials depicting river corridors and settlements (generalized)  
  - Textual references to travel routes, villages, trading points, and crossings  

- **Paleoenvironment & Environmental Data**
  - Alluvial stratigraphy, pollen/charcoal where available  
  - Modeled or mapped land cover and flood regimes  

The **region polygon and H3 mosaics** are produced from these inputs through governed generalization and clipping steps documented in PROV-O:

- Basin and valley selection  
- Buffering and smoothing  
- Simplification and H3 tiling  

---

## ⚖ 5. Generalization, CARE & Sovereignty

The Arkansas River Basin region is explicitly **generalized** to protect sensitive information:

- **What the region geometry is allowed to show**
  - A basin-scale envelope for interpretation  
  - Approximate extents of floodplain/valley systems  
  - High-level patterns relevant to Story Nodes and Focus Mode  

- **What the region geometry is **not** allowed to show**
  - Precise site locations, clusters, or inferred “hot spots”  
  - Exact outlines of sensitive cultural places or ceremonial landscapes  
  - Any boundary that could reasonably be treated as a legal or sovereign claim  

CARE-aligned principles applied:

- `care:sensitivity`: at least `"generalized"`; `"restricted-generalized"` if governance deems necessary  
- `care:visibility_rules`:
  - Polygon-level views at regional zooms  
  - H3-only visualizations where additional abstraction is required  
  - No zoom-dependent view may effectively reconstruct sensitive details  

Sovereignty and FAIR+CARE review paths (e.g., `"faircare"`, `"tribal"`, or `"faircare+tribal"`) are **governed in provenance and metadata**, not here.

---

## 🗺️ 6. How KFM Uses This Region

### In the Knowledge Graph

- As a `CulturalRegion` node with relationships to:
  - Hydrological units, eco-regions, and geomorphic units  
  - Cultural phases and periodization entities  
  - Story Node clusters and dataset collections  

### In Story Nodes

- As a **spatial scaffold** for narratives about:
  - Riverine movement and exchange  
  - Changes in settlement through time  
  - Intersections of environment, infrastructure, and culture  

Story Nodes should:

- Reference the region via its **slug** or STAC IDs  
- Use the region for **context**, not as a proxy for precise site locations  

### In Focus Mode

- As an overlay option (polygon or H3) to:
  - Provide “where am I in the basin?” context  
  - Explain why certain datasets or narratives are being emphasized  
  - Surface provenance and CARE badges as chips or side-panels  

Focus Mode must honor CARE visibility policies when deciding:

- Whether to show polygons, H3 cells, or nothing at certain zooms  
- When to gate deeper contextual explanations behind provenance-aware UI flows  

---

## 🚧 7. Known Limitations & Future Refinements

This context reflects the **current v1 understanding** of the Arkansas River Basin region:

- Boundaries may evolve as:
  - New geomorphic mapping, hydrological modeling, or environmental data are integrated  
  - Archaeological syntheses and research programs refine understandings of movement and settlement  
  - Additional sovereign partners provide guidance on representation and generalization  

Any substantial change to:

- Spatial extent  
- Temporal coverage  
- CARE/sovereignty interpretations  

must be expressed first in:

1. PROV-O provenance logs  
2. Region metadata JSON-LD and STAC artifacts  
3. Region README and related documentation  

This context file can then be updated to **describe**, not drive, those changes.

---

## 📌 8. How to Read This File (For Implementers)

- Treat this file as **human-facing guidance** only:
  - It should inform UI copy, Story Node design, and explanatory text.  
  - It must not be parsed as a source of authoritative IDs, dates, or geometry.  

- For anything machine-critical, always rely on:
  - Region metadata JSON-LD  
  - STAC Collection/Item JSON  
  - PROV-O provenance logs  
  - KFM ontologies and schemas  

If you need to change behavior in code (ETL, Focus Mode, Story Nodes), **change the governed data and metadata first**, then revise this context file to match.

---
