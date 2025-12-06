---
title: "🛡️ Kansas Frontier Matrix — Archaeology & Indigenous Sensitive Location Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geospatial/archaeology-sensitive-locations.md"

version: "v11.2.4"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Tribal Sovereignty Board"
content_stability: "stable"
backward_compatibility: "v11.0.0 → v11.2.4 privacy-contract compatible"

status: "Active / Enforced"
doc_kind: "Standard"
intent: "archaeology-sensitive-locations"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/archaeology-sensitive-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-archaeology-sensitive-v11.2.4.json"
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
  domain: "archaeology-sensitive-locations"
  applies_to:
    - "geospatial"
    - "archaeology"
    - "cultural-heritage"
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
    - "ai-narrative"

fair_category: "F1-A1-I1-R1"
care_label: "Indigenous Sensitive / High Sovereignty"
sensitivity: "High (Indigenous & cultural heritage)"
sensitivity_level: "High"
public_exposure_risk: "High (without masking)"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council & Tribal Sovereignty Board"

ttl_policy: "24 months"
sunset_policy: "Supersedes archaeology-sensitive-locations v11.0.0"

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
  - "docs/standards/geo/archaeology-sensitive-locations.md@v11.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/archaeology-sensitive-locations-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/archaeology-sensitive-locations-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:geospatial:archaeology-sensitive-locations:v11.2.4"
semantic_document_id: "kfm-archaeology-sensitive-locations-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geospatial:archaeology-sensitive-locations"

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
  - "heritage-h3-only-v11.0.0"
---

<div align="center">

# 🛡️ **Kansas Frontier Matrix — Archaeology & Indigenous Sensitive Location Standard (v11.2.4)**  
`docs/standards/geospatial/archaeology-sensitive-locations.md`

**Purpose**  
Define the **mandatory protection, masking, generalization, metadata, provenance, and ethical governance requirements** for archaeological, cultural heritage, and Indigenous sovereign locations within KFM v11.2.4.  
This standard overlays the **Geoprivacy & Cultural-Safety Masking Standard** with archaeology- and sovereignty-specific rules (H3/generalization, sovereignty ladder, narrative limits) so that all such locations are protected across ETL, catalogs, graph, APIs, UI, Story Nodes, and Focus Mode.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/
└── 📂 standards/
    └── 📂 geospatial/
        📄 README.md                             # 🌎 Geospatial Standards Index
        📂 geoprivacy-masking/                   # 🛡 Core geoprivacy & masking standard
        │   📄 README.md
        │   📂 examples/
        │   📂 schemas/
        📂 tiling-resolution/                    # 🧩 Tiling & zoom-level governance
        │   📄 README.md
        │   📄 examples.md
        📂 crs-topology/                         # 📐 CRS, geometry & topology governance
        │   📄 README.md
        │   📂 geoprivacy-masking/
        │       📄 README.md                     # CRS + masking integration
        📄 archaeology-sensitive-locations.md    # 🛡 Archaeology & Indigenous sensitive location overlay (this file)
        📄 hydrology-standards.md                # 💧 Hydrology spatial standards
        📄 vertical-axis-and-dod.md              # 📐 Vertical datum & DoD rules
~~~

Author rules:

- This document is the **domain-specific overlay** for archaeology & Indigenous-sensitive locations; it must not contradict:
  - `geoprivacy-masking/README.md` (masking methods, radii, metadata), or  
  - `crs-topology/README.md` (CRS/topology rules).  
- Any archaeology-specific masking or narrative policy change must update this file **and** be consistent with the global geoprivacy standard.

---

## 📘 Overview

Sensitive cultural spaces — archaeological sites, ceremonial grounds, burial locations, traditional cultural properties, tribal historic places, and restricted Indigenous knowledge areas — require **mandatory protection** in all KFM workflows.

This standard:

- Defines an **archaeology & sovereignty ladder** (L1–L4) for cultural sensitivity.  
- Maps that ladder onto the generic geoprivacy labels (`kfm:sensitivity_label`: `public`, `community`, `sensitive`, `sacred`).  
- Requires **deterministic donut masking** (geoprivacy standard) **plus** H3/generalization behavior tuned for cultural data.  
- Specifies **STAC/DCAT/JSON-LD metadata** for heritage/sensitivity fields.  
- Embeds **CARE sovereignty controls** across ETL, AI, UI, and Story Nodes.  
- Defines strict **AI/Focus Mode narrative limits** for high-sovereignty locations.  
- Hardens **CI/CD enforcement** for archaeology-sensitive datasets.

It does **not** re-define masking algorithms or CRS rules; instead, it constrains how they must be applied for heritage data.

---

## 🧭 Context

This standard sits at the intersection of:

- 🛡 **Geoprivacy & Cultural-Safety Masking Standard**  
  - Donut masking, sensitivity labels, STAC metadata, masking provenance.  

- 📐 **CRS, Geometry & Topology Governance Standard**  
  - EPSG:4326 storage, EPSG:3857 display, topology validity, GeoSPARQL.  

- 🧩 **Tiling Resolution & Zoom-Level Governance Standard**  
  - Zoom bands B0–B4, layer categories, sacred/sensitive zoom ceilings.  

- ⚖ **FAIR+CARE & Sovereignty Governance**  
  - Careful handling of Indigenous rights, consent, and authority to control spatial narratives.

For any dataset marked as archaeology/heritage-sensitive:

- Masking must follow the **geoprivacy standard**.  
- CRS and topology must follow the **CRS/topology standard**.  
- Zoom ceilings must follow the **tiling standard**.  
- Additional **heritage-specific rules** in this document must also be satisfied.

---

## 🧱 Architecture

### 1. Sovereignty Ladder (L1–L4) and geoprivacy mapping

KFM classifies archaeology & heritage sensitivity into four levels:

| Level | Description                                           | Example                                      | Required `kfm:sensitivity_label` |
|------:|-------------------------------------------------------|----------------------------------------------|----------------------------------|
| L1    | Public archaeological (low additional sensitivity)    | Well-known excavated village sites           | `public`                         |
| L2    | Restricted archaeological (moderate sensitivity)      | State/tribal records with controlled access  | `community`                      |
| L3    | Indigenous cultural heritage (high sensitivity)       | Cultural landscapes, ceremonial/trad places  | `sensitive`                      |
| L4    | Sovereignty-protected (very high sensitivity)         | Burials, sacred sites, confidential loci     | `sacred`                         |

Normative mapping:

- `heritage:sensitivity` ∈ {`L1`,`L2`,`L3`,`L4`}  
- `kfm:sensitivity_label` ∈ {`public`,`community`,`sensitive`,`sacred`}  
- The above mapping must be 1:1 as in the table.

### 2. Masking stack: donut + H3/generalization

All archaeology-sensitive geometries must follow this sequence:

1. **CRS normalization**  
   - Raw (`Point`, etc.) → EPSG:4326 (per CRS/topology standard).  

2. **Deterministic donut masking**  
   - Apply **donut_geomask_v1** as defined in the geoprivacy standard.  
   - Radii chosen from the geoprivacy sensitivity table, per `kfm:sensitivity_label`.  

3. **Heritage-specific generalization**  
   - For archaeology/heritage datasets, enforce **minimum H3/generalization levels**:  

     - `L1` → H3 resolution ≥ 7 (≈150 m cells)  
     - `L2` → H3 resolution ≥ 6 with ring expansion  
     - `L3` → H3 resolution 4–5 (≈2–15 km cells) + optional ring expansion  
     - `L4` → **no H3 exposure**; fully redacted from public views  

   - All public-facing geometries for L1–L3 must use **H3 cell polygons or equivalent generalized polygons**, never the masked points themselves.

4. **Topology validation & export**  
   - H3-derived or generalized polygons must be valid EPSG:4326 `Polygon`/`MultiPolygon`.  
   - For L4, no spatial geometries may be exposed outside vault/protected analytical contexts.

### 3. UI & tiling implications

- L1–L2 layers may be shown as **H3 cell polygons** at allowed zooms (per tiling standard, default category `analytic-sensitive` / `sensitive`).  
- L3 must be shown only at coarse scales (e.g., B1–B2) as broad regions; no site-level inference.  
- L4 must never appear in tiles or public map overlays.

Tiling configs must:

- Use a tiling profile and zoom ranges consistent with `sensitive` / `sacred` rules in the tiling standard.  
- Explicitly mark archaeology/heritage layers with appropriate `kfm:tiling_category` and `heritage:*` fields.

---

## 📦 Data & Metadata

### 1. Heritage-specific fields

For any STAC Item (or equivalent JSON record) representing archaeology/heritage-sensitive data, the following **heritage fields are required**:

~~~json
{
  "heritage:sensitivity": "L1",
  "heritage:sovereignty": "tribal",
  "heritage:taxonomy": "archaeological",
  "heritage:h3_index": "8ab4dxxxxxxxxxx",
  "heritage:masking_method": "donut_geomask_v1 + h3-generalization",
  "care:authority": "Example Tribal Nation",
  "care:consent_required": true
}
~~~

Notes:

- `heritage:h3_index` may be a representative or root index; full H3 footprints may be stored separately as geometry.  
- `heritage:taxonomy` is a domain label (e.g., `archaeological`, `ceremonial`, `burial`, `traditional`, `historic`).  

### 2. Integration with `kfm:*` geoprivacy fields

In addition to `heritage:*` and `care:*`, archaeology-sensitive items must include:

~~~json
{
  "kfm:sensitivity_label": "sensitive",
  "kfm:privacy_method": "donut_geomask_v1",
  "kfm:masking_run_id": "urn:kfm:etl-run:2025-12-06T00:00Z",
  "kfm:prov_ref": "prov/archaeology_masking_run_2025-12-06.jsonld",
  "kfm:h3_resolution": 5,
  "kfm:access_label": "restricted",
  "kfm:sovereignty_label": "Example Tribal Nation"
}
~~~

Combined, an archaeology-sensitive record must carry:

- **Heritage semantics** (`heritage:*`).  
- **Geoprivacy mechanics** (`kfm:*`).  
- **CARE sovereignty semantics** (`care:*`, `kfm:sovereignty_label`).

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Heritage-sensitive STAC Items must:

  - Use GeoJSON `geometry` that reflects **generalized polygons** (H3 or equivalent) for L1–L3.  
  - Omit raw point geometries for any sensitive/sacred site.  
  - Include `heritage:*`, `care:*`, and `kfm:*` fields as above.

- Collections representing heritage layers must also declare:

  - The range of `heritage:sensitivity` levels present.  
  - Links to this standard via `dct:conformsTo` (in JSON-LD mappings).

### DCAT

Recommended DCAT mappings:

| Field                 | DCAT / DCT mapping            |
|-----------------------|-------------------------------|
| `heritage:sensitivity` | `dct:accessRights`            |
| `care:authority`      | `dct:rightsHolder`            |
| `heritage:masking_method` | `dct:provenance` / PROV link |
| `heritage:h3_index`   | `dct:spatial`                 |
| `kfm:sensitivity_label` | custom extension (KFM-DCAT)  |

DCAT records must ensure that any downstream consumer is aware:

- The dataset is archaeology/heritage-sensitive.  
- Spatial footprints are generalized and not exact site locations.

### PROV-O

Each heritage generalization/masking step must include:

- `prov:used` → raw sensitive geometry entity (vault only).  
- `prov:wasGeneratedBy` → masking/generalization ETL activity.  
- `prov:generatedAtTime` → timestamp.  
- `prov:wasAssociatedWith` → pipeline/service/agent.  
- `prov:wasInfluencedBy` → relevant governance decisions (e.g., tribal policy docs).

A masking PROV bundle referenced by `kfm:prov_ref` should show:

1. Raw heritage dataset.  
2. CRS normalization.  
3. Donut masking.  
4. H3/generalization.  
5. STAC/DCAT publication step.

---

## 🧪 Validation & CI/CD

A PR that introduces or modifies archaeology/heritage-sensitive datasets must pass:

1. **Schema checks**

   - `heritage:*`, `care:*`, and `kfm:*` fields validated against:
     - `archaeology-sensitive-locations-v11.2.4.schema.json`.  

2. **Sensitivity mapping checks**

   - Verify `heritage:sensitivity` ↔ `kfm:sensitivity_label` follows the L1–L4 mapping table; any mismatch fails CI.  

3. **Geometry checks**

   - Ensure geometries used in STAC/web layers are **generalized polygons**:
     - No raw points.  
     - H3 resolution ≥ required minimum per sensitivity level.  
   - Confirm L4 records expose **no public geometry**.

4. **Provenance checks**

   - `kfm:masking_run_id` and `kfm:prov_ref` must be present and resolvable.  
   - PROV bundles must show CRS normalization → masking → generalization sequence.

5. **Story Node & Focus Mode tests**

   - Automated tests scan Story Nodes and Focus Mode outputs to ensure:
     - No archaeological Story Node uses point coordinates for L2–L4.  
     - No Story Node or Focus Mode narrative is generated for L4.  
     - L3 narratives are only present where explicitly allowed by `care:authority`.

Any failing check is a **hard block** for merge.

---

## 🧠 Story Node & Focus Mode Integration

### 1. Narrative permissions by level

- **L1 (public archaeological)**  
  - Allowed: high-level historical context, site-type explanations, region-level patterns.  
  - Spatial: generalized to H3-7+; Story Nodes refer to areas, not precise coordinates.

- **L2 (restricted archaeological)**  
  - Allowed: controlled narratives, often region-level or aggregated.  
  - Spatial: H3-6+ with ring expansion; no implied parcel/site coordinates.

- **L3 (Indigenous cultural heritage)**  
  - Allowed: only narratives explicitly approved by `care:authority`.  
  - Spatial: H3-4/5; described as “regions” or “landscapes”, not sites.

- **L4 (sovereignty-protected)**  
  - Story Nodes and narratives are **prohibited** unless an explicit, documented opt-in is granted by the Tribal authority — and even then, only with highly generalized, non-locational narrative.

### 2. Story Node schema expectations

For allowed L1–L2 heritage Story Nodes:

~~~json
{
  "target_layer_id": "kfm_archaeology_generalized_v1",
  "heritage:sensitivity": "L2",
  "kfm:sensitivity_label": "community",
  "spacetime": {
    "geometry": { "type": "Polygon", "coordinates": "H3-derived" },
    "when": { "precision": "year" }
  },
  "relations": [
    { "role": "sensitive-generalized", "target": "urn:kfm:site:xyz" }
  ],
  "care:authority": "Example Tribal Nation",
  "care:consent_required": true
}
~~~

Focus Mode behavior:

- Detect `heritage:sensitivity` and automatically select a **CARE-restricted narrative mode**.  
- Suppress detailed coordinates and replace them with approved, high-level language.  
- Deny attempts to “zoom in” narratively beyond allowed resolution or sensitivity level.

---

## ⚖ FAIR+CARE & Governance

This standard is a direct implementation of FAIR+CARE and Indigenous data sovereignty for archaeology & heritage.

- **FAIR**

  - *Findable*: heritage datasets are clearly labeled and discoverable as sensitive, with appropriate metadata.  
  - *Accessible*: documentation and policies are open; data access itself is carefully constrained.  
  - *Interoperable*: fields align with STAC, DCAT, PROV-O, GeoSPARQL, and KFM’s ontology.  
  - *Reusable*: clear masking, generalization, and provenance allow safe reuse without re-identification.

- **CARE & Sovereignty**

  - *Collective Benefit*: data use must support Tribal and community goals, not undermine them.  
  - *Authority to Control*: `care:authority`, `care:consent_required`, and sovereignty policies define who decides.  
  - *Responsibility*: KFM operators and AI systems must enforce this standard and avoid speculative or sensational narratives.  
  - *Ethics*: burials, sacred sites, and restricted knowledge areas are treated as **non-narratable** unless explicitly consented.

Governance hooks:

- Any change that:
  - Relaxes L3/L4 protections,  
  - Alters H3 or zoom levels for sacred data, or  
  - Expands AI narrative capabilities around sensitive locations  

must undergo review by:

- FAIR+CARE Council, and  
- Tribal Sovereignty Board (or equivalent partners),

and must update this document, relevant geoprivacy/CRS/tiling standards, and associated schemas.

---

## 🕰️ Version History

| Version    | Date       | Status            | Notes                                                                                                       |
|-----------:|------------|-------------------|-------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Active / Enforced | Aligned to KFM-MDP v11.2.4; moved to `docs/standards/geospatial/`; integrated with geoprivacy, CRS/topology, and tiling standards; clarified L1–L4 ↔ `kfm:sensitivity_label` mapping and H3/generalization requirements. |
| v11.0.0    | 2025-11-22 | Superseded        | Initial archaeology & Indigenous sensitive location standard (KFM-MDP v11.0.0); H3-centric masking and CARE-focused sovereignty rules. |

---

<div align="center">

🛡️ **Kansas Frontier Matrix — Archaeology & Indigenous Sensitive Location Standard (v11.2.4)**  
Sovereignty · Protection · Respect · FAIR+CARE  

[🌎 Geospatial Standards Index](./README.md) · [🛡 Geoprivacy Masking](./geoprivacy-masking/README.md) · [📐 CRS & Topology](./crs-topology/README.md) · [⚖ Governance](../governance/ROOT-GOVERNANCE.md)

</div>
