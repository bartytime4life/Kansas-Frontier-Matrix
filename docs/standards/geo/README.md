---
title: "🌎 Kansas Frontier Matrix — Geospatial Standards Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geospatial/README.md"

version: "v11.2.4"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Semiannual · FAIR+CARE Council & Spatial Governance Board"
content_stability: "stable"
backward_compatibility: "v11.2.2 → v11.2.4 directory-compatible"

status: "Active / Enforced"
doc_kind: "Standard"
intent: "geo-standards-index"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/standards-geospatial-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-geospatial-index-v11.2.4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "geospatial-standards-index"
  applies_to:
    - "geospatial"
    - "ingest"
    - "etl"
    - "analysis"
    - "stac"
    - "dcat"
    - "graph"
    - "tiling"
    - "api"
    - "frontend"
    - "story-nodes"
    - "focus-mode"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
ttl_policy: "24 months"
sunset_policy: "Superseded by Geospatial Standards Index v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/standards/geo/README.md@v11.2.2"
  - "docs/standards/geo/README.md@v11.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "diagram-extraction"
  - "3d-context-render"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "governance-override"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - metadata-extraction
    - diagram-extraction
    - 3d-context-render
    - a11y-adaptations
  prohibited:
    - content-alteration
    - speculative-additions
    - governance-override
    - unverified-architectural-claims
    - narrative-fabrication

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "🗂️ Directory Layout"
    - "📘 Overview"
    - "🧭 Context"
    - "🧱 Architecture"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧪 Validation & CI/CD"
    - "🧠 Story Node & Focus Mode Integration"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_geo_standards_index_v10.4"
---

<div align="center">

# 🌎 **Kansas Frontier Matrix — Geospatial Standards Index (v11.2.4)**  
`docs/standards/geospatial/README.md`

**Purpose**  
Serve as the **authoritative entrypoint** for all geospatial standards in the Kansas Frontier Matrix (KFM).  
Index and describe the required rules for **CRS**, **topology**, **vertical datums**, **tiling & zoom governance**, **geoprivacy masking**, **hydrology schemas**, and **STAC/DCAT/GeoSPARQL geospatial fields**, ensuring deterministic, FAIR+CARE-aligned, sovereignty-respecting spatial behavior across ETL, catalogs, graph, APIs, UI, Story Nodes, and Focus Mode.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/
└── 📂 standards/
    └── 📂 geospatial/
        📄 README.md                          # 🌎 Geospatial Standards Index (this file)
        📂 geoprivacy-masking/                # 🛡 Geoprivacy & cultural-safety masking standard
        │   📄 README.md                      #   Masking methods, radii, sovereignty rules
        │   📂 examples/                      #   Fixtures, masking runs, CI scenarios
        │   📂 schemas/                       #   Masking metadata JSON/SHACL schemas
        📂 tiling-resolution/                 # 🧩 Tiling resolution & zoom-level governance
        │   📄 README.md                      #   Band definitions, layer categories, zoom ceilings
        │   📄 examples.md                    #   Worked profiles for Kansas layers
        📂 crs-topology/                      # 📐 CRS, geometry & topology governance
        │   📄 README.md                      #   Storage/display CRS, topology rules
        │   📂 geoprivacy-masking/            #   CRS+masking integration
        │       📄 README.md                  #   Where masking runs in CRS space; topology constraints
        📄 stac-geo-spec.md                   # 🛰 STAC geospatial extensions & KFM profiles (planned/standardized)
        📄 vertical-axis-and-dod.md           # 📐 Vertical datum rules, CF Z-axis, DoD convention
        📄 hydrology-standards.md             # 💧 Hydrology & water-surface spatial schemas
        📄 soil-source-comparison.md          # 🌱 SDA/SSURGO/STATSGO2/gNATSGO provenance & crosswalks
~~~

Author rules:

- New geospatial standards **must** live under `docs/standards/geospatial/` and be listed here.  
- Directory trees in this index must use `text` fenced blocks with canonical `📂` / `📄` glyphs and `├──` / `└──` branches.  
- Each substandard (e.g., geoprivacy, tiling, CRS/topology, hydrology) must have its own README aligned to **KFM-MDP v11.2.4**.

---

## 📘 Overview

All KFM v11.2.4 spatial datasets—raster, vector, point clouds, DEMs, bathymetry, hydrology, archaeological survey data, landcover layers, and STAC Items—must conform to the geospatial standards indexed here.

This index covers, via dedicated standards:

- **CRS & Topology**  
  - Storage/display CRS policies, reprojection rules, geometry validity, and GeoSPARQL topology.  

- **Geoprivacy & Cultural-Safety Masking**  
  - Deterministic donut masking, sacred generalization (H3/polygons), sovereignty flags, and CI.  

- **Tiling & Zoom Governance**  
  - Canonical zoom bands (B0–B4), layer categories, public vs sacred zoom ceilings, and tile contracts.  

- **Vertical Datums & DoD**  
  - Vertical reference frames (e.g., NAVD88), geoid models, and difference-of-dem (DoD) interpretation rules.  

- **STAC/DCAT/Geo Metadata**  
  - STAC geospatial extension usage, DCAT spatial coverage, and JSON-LD contexts.  

- **Hydrology & Domain Layers**  
  - Standards for streams, basins, reservoirs, bathymetry, and WID-related products.  

All geospatial ETL, STAC ingest, tile pipelines, and graph loaders **must route through** these standards; ad-hoc spatial behavior is treated as non-compliant.

---

## 🧭 Context

This index operates within the KFM v11 architecture:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

- **Markdown Protocol (KFM-MDP v11.2.4)** defines how these standards are authored.  
- **Ontology Protocol (KFM-OP v11)** and **GeoSPARQL** define how spatial entities and relations are represented in the graph.  
- **Geospatial Standards** (this index) define **how space itself is handled**:
  - Which CRS and vertical datums are valid.  
  - How sensitive locations are masked and generalized.  
  - How tiles and zoom levels are governed.  

This index is therefore the **routing table** for any question of “What geospatial rule applies?” inside KFM.

---

## 🧱 Architecture

At a high level:

- `docs/standards/geospatial/README.md`  
  - Aggregates and describes all geospatial standards.  
  - Provides directory layout and linkage to sub-standards.  

- **Sub-standards** define contracts for:

  - **CRS & Topology** (`crs-topology/`):  
    - EPSG:4326 storage, EPSG:3857 display.  
    - Topology cleaning, ring orientation, and GeoSPARQL predicates.

  - **Geoprivacy Masking** (`geoprivacy-masking/`):  
    - Donut masking algorithm, radii per `kfm:sensitivity_label`, H3 generalization for sacred data.  

  - **CRS + Masking Integration** (`crs-topology/geoprivacy-masking/`):  
    - Where masking runs in CRS space, in what order relative to reprojection/topology.  

  - **Tiling Resolution & Zoom Governance** (`tiling-resolution/`):  
    - Zoom bands B0–B4, min/max zoom per layer category, and sacred/sensitive zoom ceilings.  

  - **Vertical & Hydrology Standards**:  
    - Datum, DoD, and water-surface conventions.

Each sub-README is a **first-class standard** with its own metadata, CI hooks, and governance; this index ensures they are discoverable and structurally consistent.

---

## 📦 Data & Metadata

For geospatial standards, the index enforces:

- **Identity & Versioning**

  - Each standard must define:
    - `doc_uuid`, `semantic_document_id`, `version`, `last_updated`.  
    - Clear linkage via `provenance_chain` and `provenance_requirements`.

- **Geospatial Metadata Profiles**

  - All geospatial standards must reference:
    - `stac_profile: "KFM-STAC v11"`  
    - `dcat_profile: "KFM-DCAT v11"`  
    - `prov_profile: "KFM-PROV v11"`  
    - `metadata_profiles` including at least STAC, DCAT, PROV-O, FAIR+CARE.

- **Sensitivity & Sovereignty**

  - Standards touching spatial privacy must carry:
    - `sensitivity`, `sensitivity_level`, `public_exposure_risk`, `indigenous_rights_flag`.  
    - `sovereignty_policy` and `data_steward` pointing to current governance docs.

- **Geospatial Field Requirements**

  - Sub-standards must define:
    - Required `kfm:*` geospatial fields (e.g., `kfm:storage_crs`, `kfm:privacy_method`, `kfm:tiling_category`).  
    - How these fields appear in:
      - STAC Items/Collections,  
      - DCAT Datasets/Distributions,  
      - Neo4j node/edge properties.

This index does **not** re-specify these fields; it requires each sub-README to document them explicitly and consistently.

---

## 🌐 STAC, DCAT & PROV Alignment

The geospatial standards index is itself:

- A **STAC-like metadata object** for the standards suite:
  - `semantic_document_id = "kfm-geo-standards-index"`.  
  - Can be modeled as a dataset in STAC/DCAT for documentation catalogs.

- A **DCAT Catalog/Collection** root for geospatial standards:
  - High-level description of CRS, masking, tiling, hydrology, etc.  
  - Links to sub-standards as `dcat:Dataset` entries.

- A **PROV Plan** (`prov:Plan`) for the geospatial policy regime:
  - Each sub-standard is a derived `prov:Entity` (also Plans).  
  - Updates to any geospatial standard should be captured as `prov:Activity`s tied back to this index.

Sub-standards are responsible for more detailed STAC/DCAT/PROV mappings in their own domains; this index ensures all of them are aligned to shared profiles.

---

## 🧪 Validation & CI/CD

This index is wired into CI in three main ways:

1. **Structure & Metadata Checks**

   - `markdown-lint`, `schema-lint`, `metadata-check` validate:
     - YAML front-matter against `geo-standards-index-v11.2.4.schema.json`.  
     - Presence of required fields and heading structure.  

2. **Cross-Standard Consistency Checks**

   - Custom CI steps ensure:
     - Every sub-directory referenced in the directory layout exists and has a README.  
     - Sub-standards reference this index or each other in expected ways (e.g., CRS, tiling, masking cross-links).  

3. **Provenance & Governance Checks**

   - `provenance-check` ensures `provenance_chain` is updated when versions change.  
   - `footer-check` ensures governance links (ROOT-GOVERNANCE, FAIRCARE, sovereignty policy) are present and correct.

Any failure in these checks blocks merges that modify:

- This index, or  
- Any sub-standard listed in this index.

---

## 🧠 Story Node & Focus Mode Integration

For Story Nodes and Focus Mode:

- This index is the **routing table** for spatial rules:

  - When Focus Mode needs to explain **why** a sacred layer stops at a certain zoom:
    - It resolves to the tiling-resolution standard.  

  - When it needs to explain **how** a location was masked:
    - It resolves to the geoprivacy masking + CRS-integration standards.  

- Story Nodes that carry spatial references (counties, basins, heritage sites, etc.):

  - Should reference the appropriate geospatial standards where applicable via `target_standard` fields (e.g., `kfm-doc-crs-topology-v11.2.4`).  
  - Rely on the CRS/topology standard for spatial predicates and scale semantics.

Focus Mode must treat this index and its sub-standards as **authoritative** for any geospatial reasoning; speculative reinterpretation of CRS, masking, or zoom behavior is prohibited.

---

## ⚖ FAIR+CARE & Governance

The geospatial standards index ensures FAIR+CARE is embedded across all spatial work:

- **FAIR**

  - *Findable*:  
    - All geospatial policies live under a single, predictable path: `docs/standards/geospatial/`.  

  - *Accessible*:  
    - Publicly licensed (CC-BY 4.0) and readable, with full metadata and provenance.  

  - *Interoperable*:  
    - Anchored to STAC, DCAT, PROV-O, GeoSPARQL, and KFM-OP v11.  

  - *Reusable*:  
    - Clear versioning, governance references, and spatial metadata profiles.

- **CARE & Sovereignty**

  - The index highlights standards that handle:
    - Indigenous cultural sites, sovereignty flags, and sacred-region generalization.  
    - Hydrology and landscape standards where community impact is direct.

  - Governance hooks via:
    - `governance_ref`, `ethics_ref`, `sovereignty_policy`, and `data_steward`.  
    - Explicit review cycles involving FAIR+CARE Council and Spatial Governance Board (and Tribal partners for relevant standards).

Any change that relaxes masking, modifies CRS behavior for sacred sites, or alters tiling zoom ceilings **must**:

- Update this index, and  
- Undergo appropriate governance review as defined in the referenced governance documents.

---

## 🕰️ Version History

| Version    | Date       | Status            | Summary                                                                                                                   |
|-----------:|------------|-------------------|---------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Active / Enforced | Aligned with **KFM-MDP v11.2.4**; moved path to `docs/standards/geospatial/`; integrated new CRS/topology, tiling, and geoprivacy standards; expanded metadata and governance hooks. |
| v11.2.2    | 2025-11-27 | Superseded        | “Geo Standards Index” for `docs/standards/geo/`; unified layout; CRS/vertical/tile/soil standards; FAIR+CARE and STAC/DCAT consistency hardened. |
| v11.0.0    | 2025-11-22 | Superseded        | Initial v11 geo standards index; organized CRS, vertical axis, tiling, and STAC geo-spec under a single directory.                         |

---

<div align="center">

🌎 **Kansas Frontier Matrix — Geospatial Standards Index (v11.2.4)**  
Spatial Integrity · Semantic Consistency · FAIR+CARE Governance  

[📘 Docs Root](../..) · [📂 Standards Index](../README.md) · [📂 Geospatial Standards](./) · [⚖ Governance](../governance/ROOT-GOVERNANCE.md)

</div>
