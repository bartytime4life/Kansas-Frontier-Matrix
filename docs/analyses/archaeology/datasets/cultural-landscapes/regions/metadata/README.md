---
title: "🧾 KFM v11.2.3 — Cultural Landscape Region Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
backward_compatibility: "v10.4.0 → v11.2.3 region-metadata-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-cultural-landscape-regions-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Region Metadata Registry"
intent: "cultural-landscape-region-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧾 **KFM — Cultural Landscape Region Metadata Registry**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/README.md`

**Purpose:**  
Define and govern the **metadata registry** for all cultural landscape region datasets in the Kansas Frontier Matrix (KFM).  
This directory holds **STAC-aligned, DCAT/JSON-LD, CARE-aware region metadata** that:

- Registers each cultural landscape region (e.g., Flint Hills, Smoky Hill, Arkansas River Basin)  
- Aligns region definitions with STAC, DCAT, PROV-O, GeoSPARQL, and CIDOC-CRM  
- Drives knowledge-graph ingestion and Story Node / Focus Mode behavior  
- Enforces FAIR+CARE and sovereignty rules at the **region metadata** layer  

All files here must be **machine-readable**, **CI-validated**, and **graph-safe**.

</div>

---

## 📘 Overview

The **Cultural Landscape Region Metadata Registry** provides a **single governed place** for:

- Region-level **DCAT/JSON-LD records**  
- CARE and sovereignty flags for each region  
- Crosswalks to STAC Items/Collections and provenance logs  
- Region ontology tags (e.g., `"eco-cultural"`, `"drainage"`, `"interaction-sphere"`)  
- Temporal coverage and cultural-phase alignment (OWL-Time + archaeology ontology)

This registry:

- Normalizes how region datasets are described across the KFM stack  
- Ensures that Story Nodes and Focus Mode can rely on **consistent metadata**  
- Enables CI to reason about **coverage**, **sensitivity**, and **governance status** of regions.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/
├── 📄 README.md                                   # This file (region metadata registry standard)
│
├── 📚 registry/                                   # Region registry index files (JSON/JSON-LD)
│   ├── regions-metadata-index.v1.json             # Global index of cultural landscape regions
│   └── regions-metadata-coverage.v1.json          # Optional coverage/summary (by phase, type, sensitivity)
│
├── 📑 schemas/                                    # JSON/JSON-LD schemas for region metadata
│   ├── region-metadata.schema.v1.json             # Core region metadata schema (DCAT + CARE + KFM)
│   └── region-metadata-profile-archaeology.v1.json# Archaeology-specific profile (cultural phases, ontology links)
│
├── 🧾 flint-hills-region-metadata-v1.jsonld       # Flint Hills region metadata record (DCAT/JSON-LD)
├── 🧾 smoky-hill-region-metadata-v1.jsonld        # Smoky Hill region metadata record
├── 🧾 arkansas-river-basin-region-metadata-v1.jsonld # Arkansas River Basin region metadata record
└── 🧾 <future-region>-metadata-v<semver>.jsonld   # Additional governed region metadata records
~~~

**Directory contract:**

- All **authoritative region metadata records** are stored as `*-metadata-v<semver>.jsonld`.  
- The `registry/` index files provide **summaries and lookups** used by CI and tooling.  
- The `schemas/` directory holds **machine-enforced shapes** for region metadata; changes here are governance events.  
- Per-region folders (e.g., `../flint-hills-region/`) must reference the corresponding metadata file here.

---

## 📦 Region Metadata Record Requirements

Each `*-metadata-v<semver>.jsonld` file must:

- Conform to the **core region metadata schema** (`schemas/region-metadata.schema.v1.json`)  
- Be **DCAT-compliant** and **JSON-LD context aware**  
- Carry **CARE** and sovereignty metadata consistent with the region’s provenance logs  
- Be **joinable** with STAC Items/Collections and the Neo4j graph.

### 1. Core Identification

Required fields:

- `@id`  
  - Stable URI or URN for the region metadata record.  
- `dct:title`  
  - Human-readable region name (e.g., `"Flint Hills Eco-Cultural Landscape Region"`).  
- `kfm:region_slug`  
  - Lowercase slug (e.g., `"flint-hills-region"`).  
- `kfm:region_kind`  
  - One or more controlled values (e.g., `"eco-cultural"`, `"drainage"`, `"territorial-generalized"`).  

### 2. Descriptive Metadata

- `dct:description`  
  - Concise explanation of the region purpose, derivation, and eco-cultural context.  
- `dcat:keyword`  
  - Keywords for culture, environment, geography (e.g., `"tallgrass prairie"`, `"drainage basin"`, `"protohistoric"`).  
- `dct:license`  
  - Must match KFM governance (e.g., `"CC-BY 4.0"`).  
- `dct:temporal`  
  - Temporal coverage; OWL-Time aligned, referencing cultural phases and date ranges.  
- `dct:spatial`  
  - High-level spatial descriptor or link to geometry (not the geometry itself).

### 3. Links to STAC & Provenance

- `kfm:stac_collection_id`  
  - STAC Collection ID for the region.  
- `kfm:stac_item_ids`  
  - Optional list of related STAC Item IDs (for sub-regions or versioned geometries).  
- `kfm:provenance_ref`  
  - Pointer(s) to PROV-O provenance log(s) under:  
    - `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  

These fields ensure that **metadata → STAC → provenance → graph** remains consistent.

---

## ⚖ CARE & Sovereignty Metadata

Region metadata records must include the following CARE-related fields:

- `care:sensitivity`  
  - `generalized` or `restricted-generalized` for public artifacts.  
- `care:review`  
  - `"faircare"`, `"tribal"`, or combined (e.g., `"faircare+tribal"`).  
- `care:notes`  
  - Explanation of generalization strategy, review considerations, and any limitations.  
- `care:visibility_rules`  
  - `"polygon-generalized"`, `"h3-only"`, `"no-exact-boundaries"`, or governed combinations.  
- Optional: `kfm:sovereignty_policy_ref`  
  - Reference to specific sovereignty/CARE policies when applicable.

**Rules:**

- `care:sensitivity = "restricted"` is **not allowed** in public region metadata; such records must remain internal-only.  
- CARE metadata here must **match** the information declared in STAC Items/Collections and provenance logs.  
- Any change to CARE fields is a **governance event** and must go through the FAIR+CARE and sovereignty review path.

---

## 🧭 Temporal & Cultural-Phase Alignment

Region metadata must encode temporal and cultural-phase information that:

- Uses OWL-Time where possible:
  - `time:Interval`, `time:hasBeginning`, `time:hasEnd`.  
- Links to KFM’s archaeology ontology:
  - `kfm:culture_phase` (e.g., `"Woodland"`, `"Late Prehistoric"`, `"Protohistoric"`, `"Early Historic"`).  
- Expresses temporal uncertainty where needed:
  - Ranges, approximate dates, or explicit uncertainty notes.

**Consistency requirements:**

- `dct:temporal` (DCAT), STAC temporal fields, and provenance time fields must **agree within defined tolerances**.  
- Temporal coverage must be appropriate to the region’s conceptual scope (e.g., multi-phase Arkansas River Basin vs. more focused Flint Hills).

---

## 🗺️ Spatial & Ontology Alignment

Region metadata must **not** embed detailed geometry but must:

- Reference spatial extents via:
  - BBOX hints, named eco-regions, hydrological units, or other conceptual identifiers.  
- Use KFM ontology links to represent spatial concepts:
  - `kfm:eco_region_ref`, `kfm:hydrological_unit_ref`, `kfm:geomorphic_unit_ref` (where applicable).  
- Align with GeoSPARQL and CIDOC-CRM patterns when projected into the graph.

All region geometries themselves live in:

- Per-region `data/` folders (e.g., `../flint-hills-region/data/geojson/`) and STAC Items.

---

## 🧪 Validation & CI/CD

This registry is a **CI-enforced contract**. Every change to metadata here must pass:

- **Schema validation**
  - `schemas/region-metadata.schema.v1.json`  
  - `schemas/region-metadata-profile-archaeology.v1.json`  
- **Linked-data checks**
  - JSON-LD context resolution (where applicable).  
  - DCAT field presence and value constraints.  

- **Cross-asset validation**
  - STAC IDs must exist and resolve.  
  - `kfm:provenance_ref` must point to valid provenance logs.  
  - CARE fields must match region provenance and STAC Items.

### Indicative CI workflows

- `metadata-validate.yml`  
- `artifact-stac-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml`  
- `region-metadata-registry-validate.yml` (or equivalent)

**CI must block:**

- New region datasets without corresponding metadata records here.  
- Inconsistent CARE or temporal metadata relative to STAC/provenance.  
- Schema-breaking changes to the `schemas/` subdirectory without governance approval.

---

## 🧠 Graph, Story Node & Focus Mode Integration

### Knowledge Graph (Neo4j)

From this registry, the graph loaders derive:

- **Nodes**
  - `CulturalRegion` (from each region metadata record).  
  - `RegionMetadataRecord` (optional explicit node type).  
  - `CulturalPhase`, `EcoRegion`, `HydrologicalUnit`, etc. (linked via ontology fields).

- **Relationships**
  - `HAS_METADATA` (region ↔ metadata record).  
  - `HAS_PROVENANCE` (region ↔ provenance record, from `kfm:provenance_ref`).  
  - `OCCURRED_DURING` (region ↔ cultural phases).  
  - `ASSOCIATED_WITH` (region ↔ eco-regions, hydrological units).  
  - `HAS_SENSITIVITY` (region ↔ CARE sensitivity classification).

### Story Nodes

Story Nodes use this registry to:

- Discover available regions and their key attributes.  
- Bind narratives to region slugs and IDs.  
- Pull CARE and provenance summaries (e.g., as chips or sidebars) without touching geometry.

### Focus Mode v2/v3

Focus Mode relies on this registry to:

- Filter region overlays by:
  - Cultural phase, sensitivity, region kind, or review status.  
- Inject metadata-based **provenance and CARE badges** into UI panels.  
- Enforce zoom behaviors and visibility rules derived from `care:visibility_rules`.

---

## 🧭 Authoring & Maintenance Workflow

Recommended workflow for adding/updating a region:

1. **Define/Update Region Dataset**
   - Update or create regional README (e.g., `../flint-hills-region/README.md`).  

2. **Create/Update Metadata Record**
   - Add or edit `*-metadata-v<semver>.jsonld` in this directory.  
   - Ensure it conforms to `schemas/` and references correct STAC/provenance IDs.

3. **Update Registry Index**
   - Add/modify entries in `registry/regions-metadata-index.v1.json` and optional coverage summaries.  

4. **Run Local Validation**
   - Use repo tooling (e.g., `make validate-region-metadata`) to run all relevant schema and linkage checks.  

5. **Submit PR**
   - Include:
     - Region dataset changes  
     - Metadata record changes  
     - Any necessary updates to schemas or registry index files  

6. **Address CI & Governance Feedback**
   - Resolve failures from CARE, STAC, DCAT, and provenance validators.  
   - Secure approval from the Cultural Landscape WG and FAIR+CARE Council as required.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established region metadata registry structure, schemas, and CI/governance rules; aligned with KFM-MDP v11.2.2 and cultural landscape region standard. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cultural Landscape Regions](../README.md) · [⬅ Back to Cultural Landscapes](../README.md)

</div>