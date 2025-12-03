---
title: "🧾 KFM v11.2.3 — Flint Hills Eco-Cultural Region Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/metadata/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
backward_compatibility: "Aligned with v11.2.3 cultural-landscape-region metadata-contract"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-cultural-landscape-regions-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Region Metadata"
intent: "cultural-landscape-region-flint-hills-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧾 **KFM — Flint Hills Eco-Cultural Landscape Region · Metadata**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/metadata/README.md`

**Purpose:**  
Define and govern the **region-specific metadata** for the **Flint Hills Eco-Cultural Landscape Region**.  
This directory holds **DCAT/JSON-LD, contextual markdown, and optional helper metadata** that:

- Describe the Flint Hills eco-cultural region as a governed dataset within KFM  
- Align the region with the **global region metadata registry**, STAC catalogs, and PROV-O provenance logs  
- Provide human-readable narrative context for Story Nodes and Focus Mode  
- Enforce FAIR+CARE and sovereignty rules at the **region metadata** layer  

All files here must be **machine-readable**, **CI-validated**, and **consistent** with the global region metadata and provenance registries.

</div>

---

## 📘 Overview

This `metadata/` directory provides the **Flint Hills–specific view** of:

- Region-level **DCAT/JSON-LD metadata**  
- Region context markdown for Story Nodes / Focus Mode panels  
- Optional convenience or computed summary metadata  

It is tightly coupled to:

- Region dataset spec:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/README.md`
- Global region metadata registry:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/README.md`
- Global provenance system:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/README.md`

This directory does **not** replace the global registry; instead, it:

- Hosts the **canonical per-region DCAT/JSON-LD record** referenced by the registry  
- Provides region-specific narrative & technical context for UIs and documentation  
- Ensures that all Flint Hills metadata remains **graph-safe** and **governed**.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/metadata/
├── 📄 README.md                                        # This file (region metadata contract)
│
├── 🧾 dcat-flint-hills-region-v1.jsonld                # DCAT/JSON-LD metadata record (canonical per-region)
├── 🧾 extras-flint-hills-region-metadata.v1.json       # Optional derived/summary metadata (non-authoritative)
│
└── 📖 context-flint-hills-region-v1.md                 # Human-readable contextual narrative (for Story Nodes/Focus Mode)
~~~

**Directory contract:**

- `dcat-flint-hills-region-v1.jsonld` is the **canonical region-level metadata record** for Flint Hills (version 1).  
- The global metadata registry entry for this region must reference this file as its authoritative source.  
- `context-flint-hills-region-v1.md` provides narrative/contextual content and is **not a schema authority**.  
- Any `extras-*.json` files must be treated as **derived, non-authoritative summaries** backed by the canonical JSON-LD.

---

## 📦 DCAT/JSON-LD Metadata Requirements

The file:

- `dcat-flint-hills-region-v1.jsonld`

must conform to:

- The core region metadata schema:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/schemas/region-metadata.schema.v1.json`
- The archaeology profile:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/schemas/region-metadata-profile-archaeology.v1.json`

### Core Identification

Required fields (illustrative names):

- `@id`  
  - Stable URI/URN for this region metadata record.  
- `dct:title`  
  - `"Flint Hills Eco-Cultural Landscape Region"`.  
- `kfm:region_slug`  
  - `"flint-hills-region"`.  
- `kfm:region_kind`  
  - `"eco-cultural"` (and optionally other ontology tags like `"upland-escarpment"` if modeled).

### Descriptive Content

- `dct:description`  
  - Concise description of the region’s eco-cultural purpose and context (tallgrass prairie + chert-bearing uplands, long-term land use and movement corridors).  
- `dcat:keyword`  
  - e.g., `"Flint Hills"`, `"eco-cultural region"`, `"tallgrass prairie"`, `"chert"`, `"upland escarpment"`.  
- `dct:license`  
  - `"CC-BY 4.0"` (unless stricter governance is explicitly approved).  
- `dct:temporal`  
  - Temporal coverage matching the cultural phases and OWL-Time intervals defined for this region.  
- `dct:spatial`  
  - High-level spatial descriptor or reference; **not raw geometry**.

### Links to STAC & Provenance

The metadata record must include:

- `kfm:stac_collection_id`  
  - E.g., `"kfm-arch-lands-flint-hills-region-v1"`.  
- `kfm:stac_item_ids`  
  - Optional list of Item IDs under `regions/stac/items/` (e.g., `item-flint-hills-region-v1`).  
- `kfm:provenance_ref`  
  - Reference(s) to canonical PROV-O logs, e.g.:  
    `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/flint-hills-region-v1.json`.  

These links must match:

- Entries in `docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/registry/region-provenance-index.v1.json`.  
- STAC Collections/Items in `docs/analyses/archaeology/datasets/cultural-landscapes/regions/stac/`.

---

## ⚖ CARE & Sovereignty Metadata

The Flint Hills metadata must explicitly encode CARE and sovereignty information:

Required fields:

- `care:sensitivity`  
  - `"generalized"` or `"restricted-generalized"` for public artifacts.  
- `care:review`  
  - `"faircare"`, `"tribal"`, or a combined string (e.g., `"faircare+tribal"`).  
- `care:notes`  
  - Explanation of generalization strategy, eco-cultural and lithic considerations, review process, and any suppressed areas.  
- `care:visibility_rules`  
  - `"polygon-generalized"`, `"h3-only"`, `"no-exact-boundaries"` or governed combinations.  

Optional:

- `kfm:sovereignty_policy_ref`  
  - Reference to specific sovereignty or CARE policy documents where applicable.

**Requirements:**

- CARE metadata here must **match**:
  - STAC Collections/Items for this region.  
  - Canonical PROV-O provenance logs.  
  - Region entries in the region provenance registry.  
- `care:sensitivity = "restricted"` is **not permitted** for public metadata; such cases must remain internal-only.

---

## 🕰️ Temporal & Cultural-Phase Alignment

Region metadata must encode the Flint Hills region’s **temporal scope** and cultural-phase alignment:

- Use OWL-Time constructs where possible:
  - `time:Interval`, `time:hasBeginning`, `time:hasEnd`.  
- Link to KFM archaeology ontology via:
  - `kfm:culture_phase` (e.g., `"Woodland"`, `"Late Prehistoric"`, `"Protohistoric"`).  

**Consistency rules:**

- Temporal coverage in this JSON-LD file must align with:
  - STAC Collections/Items’ temporal extent.  
  - Provenance activities’ time spans.  
- Temporal uncertainty (e.g., diffuse phase boundaries) must be clearly documented using:
  - Ranges, approximate dates, or explicit uncertainty notes.

---

## 🧭 Spatial & Ontology Alignment

The metadata **must not** embed detailed geometry, but must:

- Refer to the region’s spatial extent via:
  - Eco-region names, geologic units (chert-bearing formations), upland escarpment descriptors, etc.  
- Use KFM ontology references where available:
  - `kfm:eco_region_ref`, `kfm:geologic_unit_ref`, `kfm:hydrological_unit_ref` (if hydrologic context is modeled).  
- Align with GeoSPARQL and CIDOC-CRM semantics when transformed into the graph.

All geometries themselves live in:

- `../data/` (GeoJSON/H3)  
- And are cataloged via STAC Items/Collections under `../../stac/`.

---

## 📖 Context Markdown (`context-*.md`)

The file:

- `context-flint-hills-region-v1.md`

is a **human-readable companion** used by:

- Story Nodes  
- Focus Mode UI panels  
- Documentation readers  

It should:

- Describe the Flint Hills eco-cultural region as a **tallgrass prairie + chert-rich upland** landscape.  
- Summarize key environmental, geological, and cultural factors:
  - Lithic provisioning, grazing/hunting, movement corridors.  
- Highlight important governance, sovereignty, and CARE considerations (without revealing sensitive details).  

**Important:**

- This context file is **not authoritative metadata**; if it conflicts with JSON-LD or STAC, the machine-readable metadata wins.  
- It must not contain sensitive coordinates or detailed descriptions of confidential locations.

---

## 🧪 Validation & CI/CD

All metadata in this directory is **CI-enforced**:

### Schema validation

- JSON-LD must validate against:
  - `region-metadata.schema.v1.json`  
  - `region-metadata-profile-archaeology.v1.json`  

### Cross-link validation

- `kfm:region_slug` must match `flint-hills-region`.  
- `kfm:stac_collection_id` and `kfm:stac_item_ids` must refer to existing STAC artifacts for Flint Hills.  
- `kfm:provenance_ref` must refer to valid PROV-O logs.

### CARE consistency

- CARE fields must match STAC and provenance.  
- No unauthorized downgrades of sensitivity or visibility.

Indicative CI workflows:

- `metadata-validate.yml`  
- `artifact-stac-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml`  
- `region-metadata-registry-validate.yml`  

CI must **block**:

- New or modified metadata that breaks schema or cross-link rules.  
- CARE/sovereignty regressions relative to provenance or global metadata.  
- Region metadata that is out of sync with the global region metadata registry.

---

## 🧠 Graph, Story Node & Focus Mode Integration

### Knowledge Graph (Neo4j)

From `dcat-flint-hills-region-v1.jsonld`, graph loaders derive:

- **Nodes**
  - `CulturalRegion { slug: "flint-hills-region" }`  
  - `RegionMetadataRecord` (optional explicit node type).  
  - Linked `CulturalPhase`, `EcoRegion`, `GeologicUnit`, etc.

- **Relationships**
  - `HAS_METADATA` (region ↔ metadata record).  
  - `HAS_PROVENANCE` (region ↔ provenance, via `kfm:provenance_ref`).  
  - `OCCURRED_DURING` (region ↔ cultural phases).  
  - `ASSOCIATED_WITH` (region ↔ eco-regions, geologic units, hydrological units).  
  - `HAS_SENSITIVITY` (region ↔ CARE sensitivity classification).

### Story Nodes

Story Nodes use this metadata to:

- Discover the Flint Hills region as a spatial/narrative anchor.  
- Pull high-level temporal and cultural-phase context.  
- Attach CARE and provenance chips (e.g., “FAIR+CARE + Tribal Review”).

The context markdown file is used to:

- Provide non-sensitive narrative text in sidebars, panels, and tooltips.

### Focus Mode v2/v3

Focus Mode uses this metadata to:

- Filter overlays by region kind (`"eco-cultural"`), cultural phase, or sensitivity.  
- Drive “inspect region” panels with:
  - Temporal coverage  
  - Cultural-phase associations  
  - CARE notes & visibility rules  

- Enforce region-level visibility behaviors:
  - Where `"h3-only"` is required, polygon overlays may be hidden or replaced.

---

## 🧭 Authoring & Maintenance Workflow

When updating the Flint Hills region:

1. **Update Region Dataset & Geometry**  
   - Adjust `../README.md` and `../data/` as needed (with updated provenance).

2. **Update STAC & Global Metadata**  
   - Ensure STAC artifacts under `../../stac/` and global registry entries under `../../metadata/` are updated.

3. **Edit Region Metadata JSON-LD**  
   - Update `dcat-flint-hills-region-v1.jsonld`, or bump to `v2` as needed.  
   - Maintain links to STAC and provenance.

4. **Update Context Markdown**  
   - Adjust `context-flint-hills-region-v1.md` (or bump version) to reflect new understanding or narratives.

5. **Run Local Validation**  
   - Use repo tooling (e.g., `make validate-region-flint-hills-metadata`) to run all checks.

6. **Submit PR & Address Feedback**  
   - CI and governance review ensure schema correctness, CARE integrity, and linkage consistency.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established Flint Hills region metadata layout, DCAT/JSON-LD contract, CARE/sovereignty rules, and CI linkage to STAC and provenance; aligned with global region metadata registry and KFM-MDP v11.2.2. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Flint Hills Eco-Cultural Region](../README.md) · [⬅ Back to Cultural Landscape Regions](../..//README.md) · [⬅ Back to Global Region Metadata Registry](../../metadata/README.md)

</div>