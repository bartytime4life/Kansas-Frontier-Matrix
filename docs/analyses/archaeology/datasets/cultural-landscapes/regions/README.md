---
title: "🗺️ KFM v11.2.3 — Cultural Landscape Regions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.4.0 → v11.2.3 region-metadata-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscape-regions-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Dataset Subcategory"
intent: "cultural-landscape-regions"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Cultural Landscape Regions**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/README.md`

**Purpose:**  
Define and govern all **cultural landscape region datasets** included in the Kansas Frontier Matrix (KFM).  
These regions represent **generalized archaeological, cultural, historical, and environmental territories** used for:

- Chronological-cultural mapping  
- Story Node regional narratives  
- Focus Mode v2/v3 interpretive overlays  
- MapLibre & Cesium polygon visualizations  
- Cultural-phase modeling and AI reasoning  
- Environmental → cultural interaction synthesis  
- Archaeological settlement & landscape analysis  

All datasets must comply with **FAIR+CARE**, **STAC/DCAT**, **PROV-O**, **GeoSPARQL**, **CIDOC-CRM**, and **KFM-MDP v11.2.2**.

</div>

---

## 📘 Overview

**Cultural landscape regions** are high-level landscape zones representing spatial aspects of:

- Prehistoric and protohistoric cultural phases  
- Settlement patterns and clustering  
- Resource availability and ecological niches  
- Cultural interaction territories and spheres  
- Migration pathways and corridors  
- Long-term human–environment relationships

Regions are **never mapped at full precision**—they are intentionally generalized polygons or H3 mosaics derived from:

- Literature synthesis (archaeology, ethnohistory, geomorphology)  
- Environmental models and eco-regions  
- Aggregated archaeological datasets and surveys  
- Pollen/charcoal/paleoecological proxies  
- Geophysics and LiDAR interpreted surfaces  

Common region types include:

- **Settlement Regions**  
- **Subsistence Zones**  
- **Territorial / Cultural Extents (generalized)**  
- **Cultural Phases by Drainage Basin**  
- **Eco-cultural Landscapes**  

Regions function as the **meso-scale scaffold** that connects site-level information, environmental layers, and Story Node narratives.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/
├── 📄 README.md                               # This file (region dataset standard & index)
├── 🗺️ flint-hills-region/                     # Generalized region polygons + STAC + metadata + provenance
├── 🗺️ smoky-hill-region/                      # Cultural-ecological drainage region dataset(s)
├── 🗺️ arkansas-river-basin/                   # Multi-phase cultural region dataset(s)
├── 🗂️ stac/                                   # STAC Items & Collections for all region datasets
├── 🧾 metadata/                               # DCAT, JSON-LD, CARE, and region-level context metadata
└── 🧬 provenance/                             # PROV-O provenance logs & review documentation (see ../provenance/)
~~~

**Directory contract:**

- Each region (e.g., `flint-hills-region/`) is a **self-contained dataset directory** with:
  - STAC Items/Collections (under `stac/` or within the region directory)  
  - Region-level metadata in `metadata/`  
  - Linked provenance records in `../provenance/`  
- The `stac/`, `metadata/`, and `provenance/` directories provide **shared catalogs** and **cross-region governance**.

---

## 🌄 Region Definition Requirements

Each region dataset must define:

| Element                | Description |
|------------------------|-------------|
| **Region Name**        | Culturally/archaeologically recognized landscape zone (human-readable) |
| **Region Identifier**  | Stable, machine-friendly slug used in STAC IDs and paths (e.g., `flint-hills-region`) |
| **Temporal Span**      | One or more OWL-Time intervals (e.g., cultural phases, date ranges) |
| **Spatial Representation** | Generalized polygon(s) and/or H3 mosaic at approved resolution(s) |
| **Environmental Context**  | Biome/soil/topography/hydrology ties; relevant environmental layers |
| **Cultural Connections**   | Material culture, settlement patterns, subsistence indicators, interaction networks |
| **Sources**                | Archaeology, geomorphology, paleoenvironment, historical cartography references |
| **Sensitivity Classification** | CARE-compliant sensitivity + visibility rules |

Regions must be defined so they can be **unambiguously mapped** into:

- STAC Items/Collections  
- DCAT records  
- The KFM Neo4j graph (region nodes + relationships)  

---

## 🧭 Examples of Cultural Landscape Regions

> These examples are conceptual; real datasets must be backed by documented sources and governed provenance.

### **Flint Hills Cultural–Ecological Region**

- Tallgrass prairie + chert-rich ecotone  
- Strong correlation with Late Prehistoric settlement clusters  
- Lithic raw material availability shaping regional patterns  
- Generalized boundaries based on eco-region + archaeological distribution

### **Smoky Hill Cultural Drainage Region**

- Environmental corridor linking multiple cultural phases and traditions  
- Aggregates fluvial, ecological, and archaeological evidence  
- Supports modeling of **movement** and **interaction** along the drainage

### **Arkansas River Basin Cultural Region**

- Multi-phase cultural landscape used for settlement/timeline synthesis  
- Key region for protohistoric intercultural movements and exchange  
- May contain **sub-regions** for specific time slices or interaction spheres

---

## 📦 Required Metadata (Region Datasets)

Region datasets must include **aligned STAC + DCAT + CARE + KFM** metadata.

### ✔ STAC Item / Collection Fields

Each region STAC Item/Collection must define:

- `id` — versioned, semantic ID (e.g., `kfm-arch-lands-flint-hills-region-v1`)  
- `bbox` — generalized bounding box (no site-level precision)  
- `geometry` — Polygon/MultiPolygon (generalized; CRS = EPSG:4326)  
- `properties.kfm:culture_phase` — one or more cultural phases or periods  
- `properties.kfm:region_kind` — e.g., `"eco-cultural"`, `"drainage"`, `"territorial-generalized"`  
- `properties.care:sensitivity` — sensitivity classification (see below)  
- `properties.care:visibility_rules` — UI/pipeline visibility contract  
- `assets.data.href` — link to region geometry file(s)  
- `kfm:provenance` — pointer to PROV-O provenance record(s) under `../provenance/`

### ✔ DCAT Metadata

Region-level DCAT records must include:

- `dct:title` — human-readable region title  
- `dct:description` — region purpose and context  
- `dcat:distribution` — link(s) to data files and STAC catalogs  
- `dct:temporal` — temporal coverage (OWL-Time aligned)  
- `dct:license` — must match `CC-BY 4.0` unless otherwise governed  
- `dcat:keyword` — keywords for culture, environment, region type, etc.  

### ✔ CARE Metadata

Regions must include the following CARE fields:

| CARE Field              | Allowed Values / Notes |
|-------------------------|------------------------|
| `care:sensitivity`      | `generalized`, `restricted-generalized` (public artifacts only) |
| `care:review`           | `faircare`, `tribal`, or combined (e.g., `"faircare+tribal"`) |
| `care:notes`            | Explanation of generalization, cultural considerations, and constraints |
| `care:visibility_rules` | `polygon-generalized`, `h3-only`, `no-exact-boundaries` |

**Forbidden for public region datasets:**

- `care:sensitivity = "restricted"`  
- Exact ceremonial, burial, or sacred territorial boundaries  
- Any representation violating sovereignty or confidentiality constraints  

### ✔ Provenance Link

Every region must specify (at minimum):

- `kfm:provenance` — path or identifier for the PROV-O record documenting:
  - Generalization process  
  - Data sources and interpretation lines  
  - FAIR+CARE and tribal review  
  - Version lineage and review history  

The provenance log itself must comply with:

- `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/README.md`

---

## 🧭 Spatial Requirements

- All regions must use **generalized polygons and/or H3 mosaics**; no site-level fidelity.  
- Sensitive boundaries must **avoid precision** even when underlying data is more detailed.  
- Territorial regions must **not represent exact or disputed political/sovereign borders**.  
- For high-sensitivity zones:
  - Prefer **H3-only** representations (e.g., aggregated grid cells).  
- Coordinate reference system (CRS) for stored geometries:
  - **EPSG:4326** (WGS84 lon/lat).  
- Polygons must include **topological simplification** and de-noising to avoid reverse-engineering of sensitive details.

---

## 🕰️ Temporal Requirements

Regions must include:

- OWL-Time compatible temporal coverage (e.g., `time:Interval` or equivalent properties)  
- Cultural-phase references:
  - Examples: `"Late Prehistoric"`, `"Protohistoric"`, `"Middle Ceramic"`, etc.  
- For multi-era regions:
  - Specify earliest & latest documented presence or relevance.  
- Optional uncertainty metadata:
  - Time-range uncertainty  
  - Confidence levels or commentary on dating

Temporal information must be consistent across:

- Region metadata (`metadata/`)  
- STAC Items/Collections (`stac/`)  
- Provenance logs (`../provenance/`)

---

## 🧪 Validation Requirements

All region datasets must pass **governed validation** before ingestion:

- **Schema validation**
  - Region metadata schema (KFM archaeology region profile)  
  - CARE cultural safety schema  
  - DCAT compliance checks  
  - STAC Item + Collection schema validation  

- **Provenance linkage**
  - `kfm:provenance` must resolve to a valid PROV-O JSON-LD log under `../provenance/`.  
  - CARE + sensitivity fields must be consistent with provenance CARE fields.

- **Spatial generalization audit**
  - Confirm that geometries meet generalization requirements.  
  - Verify that no coordinates are precise enough to expose sensitive locales.

### CI Workflows

Typical CI workflows include:

- `metadata-validate.yml`  
- `faircare-audit.yml`  
- `artifact-stac-validate.yml`  
- `archaeology-provenance-validate.yml` (or equivalent)

**CI blocks ingestion** if:

- Region metadata is missing or malformed.  
- CARE sensitivity/visibility rules conflict with governance policy.  
- No valid provenance record exists, or links are broken.  
- Spatial generalization does not meet minimum abstraction thresholds.

---

## 🧠 Integration Into the KFM Ecosystem

### Knowledge Graph (Neo4j)

From each region dataset, the KFM ETL pipelines materialize:

- **Nodes**
  - `CulturalRegion`  
  - `EnvironmentalRegion` (where derived from eco-regions)  
  - `CulturalPhase`  
  - `ResourceZone`  
  - `ProvenanceRecord`  

- **Relationships**
  - `PART_OF` (sub-regions → larger composite regions)  
  - `ASSOCIATED_WITH` (regions ↔ cultural phases, materials, or site clusters)  
  - `OCCURRED_DURING` (regions ↔ temporal intervals/phases)  
  - `GENERALIZED_FROM` (region ↔ underlying, more detailed internal representations)  
  - `HAS_PROVENANCE` (region ↔ provenance log)  
  - `HAS_SENSITIVITY` (region ↔ sensitivity classification)

### Story Nodes

Regions provide **spatial anchors** for:

- Landscape-scale cultural narratives and interpretive arcs  
- Cross-cutting stories about movement, subsistence, and interaction  
- Multi-phase diachronic overviews connecting multiple datasets  

Story Nodes must reference region identifiers so Focus Mode can:

- Explain **why** a story is grounded in a particular region.  
- Surface provenance and CARE information as contextual chips.  
- Respect visibility rules (e.g., avoid zoom or visual detail beyond allowed generalization).

### Focus Mode v2/v3

Region metadata powers Focus Mode behaviors:

- Spatial contextualization for site-level or dataset-level views.  
- Region-aware tooltips and info panels with:
  - Cultural-phase summaries  
  - Environmental descriptions  
  - Provenance and CARE badges  

- Ethical visibility constraints:
  - Hiding or generalizing boundaries at certain zoom levels.  
  - Avoiding overlays in contexts where sensitivity is high.  

- Provenance-chip injection:
  - Quick indicators of review status (FAIR+CARE, tribal).  
  - Links to detailed provenance and metadata.

---

## 📊 Dataset Index

> This table is illustrative. Actual entries must be kept in sync with STAC/DCAT records and provenance logs.

| Region Dataset              | Category           | Status     | Last Review | Notes                                |
|-----------------------------|-------------------|-----------|-------------|--------------------------------------|
| `flint-hills-region/v1`     | Eco-cultural      | 🟢 Active | 2025-11     | Generalized & FAIR+CARE-approved     |
| `smoky-hill-region/v1`      | Cultural drainage | 🟢 Active | 2025-10     | STAC/DCAT aligned; provenance linked |
| `arkansas-river-basin/v1`   | Multi-era region  | 🟡 Review | 2025-09     | Tribal review required for final pub |

Region index entries must **not** be treated as authoritative without corresponding, validated:

- STAC records  
- Metadata records in `metadata/`  
- Provenance records in `../provenance/`

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Aligned with KFM-MDP v11.2.2; added CI/validation, graph, Story Node, and Focus Mode integration; updated release metadata to v11.2.3. |
| v10.4.0  | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council   | Established region-level governance, metadata rules, STAC/DCAT/CARE requirements. |
| v10.0.0  | 2025-11-10 | Cultural Landscape Team                     | Initial directory scaffold for cultural landscape regions.             |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cultural Landscapes](../README.md)

</div>