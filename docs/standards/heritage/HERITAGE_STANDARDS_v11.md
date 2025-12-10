---
title: "🏺 Kansas Frontier Matrix — Unified Heritage Standards v11 (Schemas · Examples · Assets)"
path: "docs/standards/heritage/HERITAGE_STANDARDS_v11.md"
version: "v11.0.1"
last_updated: "2025-12-06"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../../releases/v11.0.1/signature.sig"
attestation_ref: "../../../releases/v11.0.1/slsa-attestation.json"
sbom_ref: "../../../releases/v11.0.1/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.1/manifest.zip"
telemetry_ref: "../../../releases/v11.0.1/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/heritage-standards-v11.json"
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

status: "Active / Enforced"
doc_kind: "HeritageStandards"
intent: "heritage-standards-v11"
role: "heritage-governance-reference"
header_profile: "standard"
footer_profile: "standard"

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "heritage"
  applies_to:
    - "archaeology"
    - "historic-preservation"
    - "cultural-landscapes"
    - "oral-history-linked-geographies"

fair_category: "F1-A1-I1-R1"
care_label: "Protected / High-Risk"
sensitivity: "Heritage (sensitive by default)"
sensitivity_level: "High"
public_exposure_risk: "Medium"
classification: "Internal Heritage Governance Document"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
risk_category: "Heritage Protection"
redaction_required: true

data_steward: "KFM FAIR+CARE Council"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next major KFM heritage revision"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "CreativeWork"
  prov_o: "prov:Plan"
  owl_time: "Instant"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/standards/heritage/HERITAGE_STANDARDS_v10.md@v10.x"
  - "docs/standards/heritage/HERITAGE_STANDARDS_v11.md@v11.0.0"
  - "docs/standards/heritage/HERITAGE_STANDARDS_v11.md@v11.0.1"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../schemas/json/heritage-standards-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/heritage-standards-v11-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:heritage:standards:v11.0.1"
semantic_document_id: "kfm-heritage-standards-v11.0.1"
event_source_id: "ledger:kfm:doc:standards:heritage:HERITAGE_STANDARDS_v11.0.1"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "culturally-sensitive-inference"
  - "governance-override"

transform_registry:
  allowed:
    - "summary"
    - "semantic-highlighting"
    - "a11y-adaptations"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-historical-claims"
    - "culturally-sensitive-inference"
    - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "heritage-schema-lint"
  - "heritage-redaction-check"
  - "heritage-assets-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Heritage Protection × FAIR+CARE Ethics × Open Standards"
  architecture: "Generalize the Geometry · Preserve the Meaning"
  analysis: "Evidence-Led · Community-Governed · Open by Design"
  data-spec: "Linked Open Heritage × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable Protection · Open Provenance"
  telemetry: "Transparent Risk · Ethical Metrics · Sustainable Preservation"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields: []
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Unified Heritage Standards v11**  
**Schemas · Examples · Assets**  
`docs/standards/heritage/HERITAGE_STANDARDS_v11.md`

**Status:** Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

**Purpose**  
Provide the canonical, governance-safe **single-source-of-truth** for all **heritage‑protection standards** in KFM v11, merging:

- the **Schemas Index**  
- the **Example Library**  
- the **Assets Index**  

This unified document governs ALL heritage pipelines, visual assets, spatial generalization methods, metadata rules, and FAIR+CARE / sovereignty requirements.

[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Certified-gold.svg)]()  
[![Markdown KFM-MDP v11.2.4](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.4-blue.svg)]()  
[![License CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen.svg)]()

</div>

---

## 📘 Overview

### 1. Scope and Intent

This v11 heritage standard applies to **all KFM artifacts that intersect with cultural heritage**, including:

- archaeological sites and landscapes  
- sacred or culturally significant places  
- historic structures, districts, and viewsheds  
- oral‑history‑linked locations and story layers  
- any derived product that could be used to infer **precise** heritage locations  

It unifies three previously separate strands:

1. **Schemas** — JSON/SHACL schemas for heritage datasets, sensitive locations, H3 generalization, and provenance.  
2. **Examples** — a curated set of **synthetic** examples that demonstrate correct usage while *never* exposing real sites.  
3. **Assets** — diagrams, icons, and templates that are abstraction‑only and sovereignty‑aware.

Wherever there is tension between openness and protection, this document **prioritizes protection**, in alignment with Kansas legal requirements and Indigenous data sovereignty guidance.

### 2. Core Heritage Principles

1. **Generalization‑First**  
   Raw coordinates for protected sites are never published in KFM public or shared layers. Heritage products use H3 or equivalent generalization with minimum aggregation thresholds.

2. **Sovereignty‑First**  
   Indigenous communities retain authority over how their cultural data are represented. Relevant datasets **must** carry sovereignty flags and CARE‑aligned metadata, and may be further restricted or withdrawn.

3. **Least‑Reveal Principle**  
   Public or shared outputs expose only the information required for research, education, or management — no more. All examples in this document are synthetic and safe by design.

4. **Full Provenance, Controlled Access**  
   Internally, raw location and workflow provenance are preserved as PROV‑O entities. Access is governed by separate authorization policies; this standard controls **what may leave** protected contexts.

5. **Graph‑Native, Catalog‑Native**  
   Heritage entities are first‑class nodes and datasets: they must be representable in Neo4j (KFM‑OP v11), STAC Collections/Items, and DCAT catalogs.

6. **Reproducible Redaction**  
   Generalization and redaction are deterministic, config‑driven ETL steps. Given the same inputs and configs, KFM must be able to reproduce the same generalized heritage products.

### 3. Relationship to Other KFM Standards

This document sits alongside:

- **KFM‑MDP v11.2.4 (Markdown Protocol)** — governs this file’s structure, headings, and metadata.  
- **STAC / DCAT / PROV standards** — define how heritage datasets and workflows are cataloged and traced.  
- **Indigenous Data Protection & FAIR+CARE guides** — define sovereignty, consent, and ethical use obligations.  
- **Kansas Frontier Matrix architecture and history docs** — describe how heritage layers integrate into maps, timelines, and story views.

Any heritage‑related SOP, pipeline design, or UI spec **must reference and conform to this standard**.

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    ├── 📁 standards/
    │   ├── 📁 heritage/
    │   │   ├── 🏺 HERITAGE_STANDARDS_v11.md          # This unified heritage standards document
    │   │   ├── 📁 schemas/                           # JSON / SHACL heritage schemas (governed here)
    │   │   │   ├── 📄 h3-generalization-standard.json
    │   │   │   ├── 📄 heritage-sensitive-location.schema.json
    │   │   │   ├── 📄 heritage-dataset.schema.json
    │   │   │   ├── 📄 heritage-protection-flags.schema.json
    │   │   │   └── 📄 lineage-provenance.schema.json
    │   │   ├── 📁 examples/                          # Synthetic, non-sensitive examples only
    │   │   │   ├── 📄 h3-generalization-demo.json
    │   │   │   ├── 📄 sensitive-location-example.json
    │   │   │   ├── 📄 heritage-dataset-stac.json
    │   │   │   ├── 📄 heritage-dataset-dcat.json
    │   │   │   ├── 📄 provenance-lineage-example.json
    │   │   │   └── 📄 storynode-heritage-demo.json
    │   │   ├── 📁 assets/                            # Diagrams, icons, infographics, templates
    │   │   │   ├── 📁 diagrams/
    │   │   │   ├── 📁 icons/
    │   │   │   ├── 📁 infographics/
    │   │   │   └── 📁 templates/
    │   │   └── 📄 README.md                          # Heritage standards index / navigation
    │   ├── 📁 governance/
    │   ├── 📁 faircare/
    │   └── 📁 sovereignty/
    │
    ├── 📁 data/
    │   ├── 📁 sources/                               # Heritage source manifests (DCAT / provenance)
    │   ├── 📁 raw/                                   # Access-controlled raw heritage locations (non-public)
    │   ├── 📁 work/                                  # Masked / intermediate heritage products
    │   ├── 📁 processed/                             # Generalized heritage layers (H3, hexes, tiles)
    │   └── 📁 stac/                                  # STAC Collections/Items for heritage assets
    │
    └── 📁 schemas/
        ├── 📁 json/
        │   └── 📄 heritage-standards-v11.schema.json # JSON schema for this document’s front matter
        └── 📁 shacl/
            └── 📄 heritage-standards-v11-shape.ttl   # SHACL shapes for heritage graph entities
~~~

**Directory rules**

- Every directory in this tree must have either a `README.md` or be documented here with a clear purpose.  
- `docs/standards/heritage/examples/` MUST contain only **synthetic or irreversibly generalized** content.  
- Raw site coordinates belong only under `data/raw/` and protected storage — never under `docs/` or `assets/`.

---

## 🧭 Context

KFM functions as a **scientific‑grade historical atlas** with verifiable lineage and transparent data handling. Heritage content adds additional obligations:

- Archaeological site locations and many cultural resource records are exempt from open disclosure (e.g., NHPA §304 and state regulations), requiring **masking or omission** in public products.  
- KFM integrates **Indigenous perspectives and oral histories**, which may carry cultural protocols that differ from Western archival practice; these must be reflected in metadata and access rules.  
- Heritage datasets often intersect with other domains (hydrology, agriculture, climate). Cross‑domain joins must **never** re‑identify or relocate sensitive sites.

Heritage standards therefore:

- Define how **location precision** is managed (H3 resolutions, aggregation thresholds).  
- Govern **cataloging** of heritage layers in STAC/DCAT with explicit protection flags.  
- Specify how **provenance** is recorded so that every generalized product can be traced back to workflows and (where appropriate) raw confidential inputs.  
- Coordinate with Focus Mode / Story Node features so that narrative overlays never leak restricted detail.

---

## 🗺️ Diagrams

### 1. Allowed Diagram Profiles

- `mermaid-flowchart-v1` — heritage ETL, generalization, and publication flows.  
- `mermaid-timeline-v1` — high‑level historical / stewardship timelines (no sensitive coordinates).

### 2. Heritage‑Specific Diagram Rules

- No diagram may depict the **exact geometry** or **precise coordinates** of a sensitive site.  
- Diagrams must use **H3 cells, bounding boxes, or schematic shapes** only.  
- Any map‑like figure represents **aggregated regions** or stylized forms, never detailed site outlines.

### 3. Example — Heritage Generalization Flow

~~~mermaid
flowchart LR
    RAW["Raw heritage inputs (restricted)"]
        --> GEN["H3 generalization & masking"]
    GEN --> META["Heritage STAC/DCAT metadata"]
    META --> GRAPH["Heritage entities in KFM graph"]
    GRAPH --> VIEWS["Generalized public & research views"]
~~~

### 4. Accessibility

- All diagrams must have a short textual summary near the figure.  
- Color is not the sole differentiator; shapes and labels are required.  
- SVGs must meet WCAG 2.1 AA contrast requirements.

### 5. Forbidden Practices

- ASCII art that encodes precise site shapes.  
- Embedding secret URLs, raw coordinates, or identifiers that could be joined to external leaks.  
- Using real aerial imagery or scans that clearly reveal protected locations without masking.

---

## 🧠 Story Node & Focus Mode Integration

### 1. Heritage Story Nodes

Heritage Story Nodes (e.g., for cultural landscapes, generalized mound regions, or interpreted narratives):

- Must reference **generalized spatial footprints** (H3 cells, buffered polygons), not raw site points.  
- Should carry explicit flags such as `heritage_protected`, `care_level`, and `cultural_sensitivity`.  
- **Must not** embed raw coordinates or sensitive site codes in free text; those belong only in protected internal systems.

Synthetic example:

~~~json
{
  "id": "node-ks-heritage-102",
  "type": "story-node",
  "title": "Generalized Mound Landscape",
  "heritage_protected": true,
  "cultural_sensitivity": "restricted",
  "care_level": "Level III",
  "summary": "A generalized representation of a culturally significant mound landscape.",
  "h3_id": "872830829ffffff",
  "h3_resolution": 7,
  "display_rules": {
    "map": "hex",
    "timeline": true,
    "min_zoom": 8
  }
}
~~~

All identifiers, codes, and descriptions in example files must be **synthetic** and **non‑identifying**.

### 2. Focus Mode Behavior

When Focus Mode operates on this document or heritage Story Nodes:

- **Focus Mode MAY:**
  - summarize sections within `ai_transform_permissions`  
  - highlight key constraints (no raw coordinates, sovereignty flags, redaction rules)  
  - extract metadata for catalogs and dashboards  

- **Focus Mode MUST NOT:**
  - infer hidden locations from generalized data  
  - synthesize “likely coordinates” for heritage sites  
  - generate new historical or cultural claims not present in the source documents  
  - override or omit sovereignty, CARE, or governance references  

These constraints are enforced by the `ai_transform_*` and `transform_registry` settings in the front matter and the system governance layer.

### 3. Writing Patterns for Heritage Narratives

To remain Focus‑friendly and sovereignty‑aligned:

- Use explicit, descriptive language (“generalized mound landscape in northeast Kansas”) instead of micro‑local hints.  
- Avoid combining detailed context clues (micro‑toponyms, hyper‑local geomorphology) in ways that could re‑identify a site.  
- Keep each subsection focused on a single heritage concept (e.g., “H3 Resolution Policy”, “Sovereignty Flags”) for clean Story Node extraction.

---

## 🧪 Validation & CI/CD

### 1. Document‑Level Checks

All heritage standards Markdown files must pass core KFM‑MDP checks:

- `markdown-lint` — heading structure, lists, spacing.  
- `schema-lint` — front‑matter validation against `heritage-standards-v11` JSON schema.  
- `metadata-check` — required identity, lifecycle, and ethics metadata present.  
- `provenance-check` — `provenance_chain` consistent with Version History.  
- `footer-check` — governance footer present and correctly linked.

### 2. Heritage‑Specific Checks

Additional test profiles for heritage content:

- `heritage-schema-lint` — validates heritage JSON/SHACL schemas under `docs/standards/heritage/schemas/`.  
- `heritage-redaction-check` — scans Markdown, JSON examples, and assets for:
  - raw lat/lon values above precision thresholds  
  - restricted site codes or identifiers  
  - unmasked geometries in embedded GeoJSON  
- `heritage-assets-check` — ensures that diagrams and icons:
  - are vector‑first (SVG)  
  - use abstraction‑only visuals  
  - include required metadata (creator, license, CARE/sovereignty tags)

Suggested local commands (illustrative):

~~~text
make validate-heritage-docs
make validate-heritage-schemas
make validate-heritage-assets
~~~

These checks must be wired into `.github/workflows/kfm-ci.yml` so that heritage violations **block merges**.

---

## 📦 Data & Metadata

This section merges the **Schema Registry**, **Example Library**, and **Asset Guidelines** into a single reference.

### 1. Heritage Schema Registry

#### 1.1 Schema Directory Layout

~~~text
docs/standards/heritage/schemas/
├── 📄 h3-generalization-standard.json
├── 📄 heritage-sensitive-location.schema.json
├── 📄 heritage-dataset.schema.json
├── 📄 heritage-protection-flags.schema.json
└── 📄 lineage-provenance.schema.json
~~~

#### 1.2 Schema Descriptions

**🧮 `h3-generalization-standard.json`**

- Allowed H3 resolutions (e.g., r5–r8) for public and partner‑only releases.  
- Minimum **site count per cell** or equivalent aggregation thresholds.  
- Rules for removing raw coordinates and single‑site cells from generalized outputs.  
- Parameters for NHPA §304 and state‑level heritage protection compliance.  
- Overrides for Indigenous sovereignty requirements (e.g., stricter masking in certain territories).

**🏺 `heritage-sensitive-location.schema.json`**

- `cultural_sensitivity` levels (open / restricted / confidential).  
- CARE labels and `indigenous_rights_flag`.  
- Tribal or community affiliation fields (controlled vocabulary; may be redacted in exports).  
- Prohibition of `lat`/`lon` fields — only generalized spatial references (H3, coarse polygons, bounding boxes).  
- Required governance metadata (legal basis, access conditions).

**📦 `heritage-dataset.schema.json`**

- Dataset‑level STAC/DCAT alignment for heritage collections.  
- Temporal and spatial extent fields referencing generalized geometries.  
- Links to underlying workflows and configuration identifiers.  
- Required protection flags (`heritage_protected`, `care_level`, `redaction_policy`).

**🔐 `heritage-protection-flags.schema.json`**

- Protection tiers (e.g., Tier I–III) mapped to allowed zoom levels, export rules, and sharing scopes.  
- UI hints (icon choice, color semantics) for protected content.  
- Rules for indexing or excluding records from public search.

**🧬 `lineage-provenance.schema.json`**

- PROV‑aligned lineage for generalized heritage datasets:  
  - `prov:wasDerivedFrom`, `prov:used`, `prov:wasGeneratedBy`  
  - SHA256 or equivalent integrity hashes for inputs and outputs  
  - workflow version identifiers and configuration fingerprints

### 2. Example Library (Synthetic Only)

#### 2.1 Example Directory Layout

~~~text
docs/standards/heritage/examples/
├── 📄 h3-generalization-demo.json
├── 📄 sensitive-location-example.json
├── 📄 heritage-dataset-stac.json
├── 📄 heritage-dataset-dcat.json
├── 📄 provenance-lineage-example.json
└── 📄 storynode-heritage-demo.json
~~~

_All examples are synthetic and must never encode real or easily re‑linkable sites._

#### 2.2 Example: H3 Generalization

~~~json
{
  "h3_id": "872830829ffffff",
  "h3_resolution": 7,
  "site_count": 4,
  "periods": ["Archaic", "Late Prehistoric"],
  "heritage_protected": true,
  "generalization_method": "H3",
  "raw_coordinates_removed": true,
  "mcp_protected": true,
  "care_level": "Level III"
}
~~~

#### 2.3 Example: Sensitive Location Metadata (Synthetic)

~~~json
{
  "id": "KS-ARCH-004198",
  "type": "heritage_site",
  "cultural_sensitivity": "restricted",
  "legal_basis": "NHPA Section 304",
  "care_level": "Level III",
  "tribal_affiliation": ["Kaw Nation"],
  "description": "Earthen mound feature with significant cultural importance (generalized).",
  "h3_id": "872830829ffffff",
  "h3_resolution": 7,
  "raw_coordinates_removed": true,
  "mcp_protected": true
}
~~~

> **Note:** IDs and affiliations here are illustrative; curators must never paste real site codes or confidential notes into example files.

#### 2.4 Example: Heritage STAC Item

~~~json
{
  "stac_version": "1.0.0",
  "type": "Item",
  "id": "ks-heritage-generalized-2025",
  "collection": "kfm-heritage",
  "properties": {
    "heritage_protected": true,
    "care_level": "Level III",
    "generalization_method": "H3",
    "h3_resolution": 7,
    "raw_coordinates_removed": true,
    "mcp_protected": true
  },
  "assets": {
    "hex_geojson": {
      "href": "hexes/ks-heritage-2025.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
~~~

#### 2.5 Example: Heritage DCAT Metadata

~~~json
{
  "dct:title": "Kansas Protected Heritage (Generalized to H3-r7)",
  "dct:description": "Generalized heritage dataset with H3-based masking and NHPA-compliant redaction.",
  "dct:spatialResolution": "H3-r7",
  "dct:provenance": "Generalized from protected archaeological coordinates.",
  "dct:conformsTo": "KFM Heritage H3 Generalization Standard v11",
  "dct:rights": "NHPA §304 restrictions apply; CARE Level III."
}
~~~

#### 2.6 Example: Lineage Metadata

~~~json
{
  "version": "2025.11.20",
  "lineage": {
    "predecessor": "2025.07.15",
    "successor": "2026.02.01",
    "latest": "2026.02.01"
  },
  "reproducibility": {
    "workflow_hash": "sha256-b94c...",
    "inputs_hash": "sha256-09af...",
    "prov": {
      "wasDerivedFrom": "urn:kfm:raw:heritage:2025-07-15",
      "generatedBy": "urn:kfm:workflow:heritage-generalization-v11"
    }
  }
}
~~~

#### 2.7 Example: Story Node (Heritage)

~~~json
{
  "id": "node-ks-heritage-102",
  "type": "story-node",
  "title": "Ancient Mound Site (Generalized)",
  "heritage_protected": true,
  "cultural_sensitivity": "restricted",
  "periods": ["Late Woodland"],
  "summary": "A generalized representation of an important cultural heritage location.",
  "h3_id": "872830829ffffff",
  "h3_resolution": 7,
  "mcp_protected": true,
  "display_rules": {
    "map": "hex",
    "timeline": true
  },
  "relations": [],
  "spacetime": {
    "geometry": { "type": "Point", "coordinates": [0, 0] },
    "when": { "start": "1600-01-01T00:00:00Z", "precision": "year" }
  }
}
~~~

The `[0, 0]` coordinates are a **non‑location placeholder** indicating that any real coordinates must be generalized or omitted.

### 3. Heritage Assets

#### 3.1 Asset Directory Layout

~~~text
docs/standards/heritage/assets/
├── 📁 diagrams/
│   ├── 📄 h3-protection-flow.svg
│   ├── 📄 heritage-protection-overview.svg
│   ├── 📄 sensitive-location-governance.svg
│   ├── 📄 lineage-flow.svg
│   └── 📄 ...
├── 📁 icons/
│   ├── 📄 heritage_protected.svg
│   ├── 📄 heritage_level_III.svg
│   ├── 📄 cultural_care_flag.svg
│   └── 📄 ...
├── 📁 infographics/
│   ├── 📄 heritage_risk_matrix.svg
│   ├── 📄 h3-resolution-scale.svg
│   └── 📄 ...
└── 📁 templates/
    ├── 📄 heritage_stac_template.json
    ├── 📄 heritage_dcat_template.json
    └── 📄 storynode_heritage_template.json
~~~

#### 3.2 Asset Requirements

All heritage assets must:

- avoid sensitive or sacred imagery unless explicitly vetted and approved  
- represent locations only in generalized or symbolic form  
- adhere to WCAG 2.1 AA+ contrast standards  
- prefer SVG (vector‑first) for scalability and clarity  
- carry metadata for license, creator, `heritage_protected`, `care_level`, and sovereignty tags  
- never depict real‑world coordinates or recognizable burial sites, shrines, or restricted landscapes without explicit, documented consent

#### 3.3 Asset Validation

Assets are subject to:

- Heritage stewardship review for cultural appropriateness  
- FAIR+CARE Council sign‑off for high‑risk materials  
- automated checks via `heritage-assets-check` (file types, metadata completeness, basic redaction scanning)

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. DCAT Alignment

Heritage datasets appear in DCAT as `dcat:Dataset` with:

- `dct:title`, `dct:description`, `dct:identifier`  
- `dct:spatial` using generalized geometries (bounding boxes or coarse polygons)  
- `dct:accessRights` and `dct:rights` describing NHPA/CARE‑driven restrictions  
- `dct:provenance` pointing to generalized workflows and legal basis for redaction

Distributions must declare:

- whether they are **public** (generalized only)  
- **restricted** (partner‑only under agreements)  
- **internal** (stewardship and research only)

### 2. STAC Alignment

Heritage layers are represented in STAC via a `kfm-heritage` Collection, where Items may be:

- non‑spatial (metadata‑only)  
- spatial with generalized geometries (H3 aggregated footprints, coarse polygons)

Key STAC properties:

- `properties.heritage_protected: true`  
- `properties.care_level`  
- `properties.generalization_method: "H3"` (or equivalent)  
- `properties.h3_resolution` (where applicable)  
- asset roles clearly labeling generalized products (e.g., `roles: ["data", "generalized"]`)

Spatial fields (`geometry`, `bbox`) must **never** reflect ungeneralized site footprints.

### 3. PROV‑O Alignment

Heritage pipelines must produce PROV‑compatible provenance:

- raw heritage datasets as restricted `prov:Entity` instances  
- generalization workflows as `prov:Activity` instances, with:
  - configuration files, container images, and code versions  
  - timestamps and responsible `prov:Agent`s (stewardship team, ETL service)  
- generalized outputs as derived `prov:Entity` instances, with:
  - `prov:wasDerivedFrom` referencing protected inputs  
  - `prov:wasGeneratedBy` referencing generalization activities  
  - integrity hashes matching STAC/DCAT records

This alignment ensures that even while public products remain generalized, stewards can audit and reconstruct the full heritage data lifecycle.

---

## 🧱 Architecture

### 1. Heritage Data Flow (Conceptual)

Heritage content moves through KFM in a controlled way:

1. **Ingest Restricted Sources** — archival records, archaeological inventories, oral histories, and GIS layers are ingested into protected storage.  
2. **Normalize & Link** — data are normalized into heritage schemas and linked to the KFM graph, but remain access‑controlled.  
3. **Generalize & Mask** — deterministic H3 generalization and redaction workflows transform raw inputs into safe outputs.  
4. **Catalog** — generalized products are registered in STAC/DCAT with protection flags and provenance links.  
5. **Expose** — appropriate slices are surfaced to maps, timelines, and Story Nodes, respecting tiered access and sovereignty restrictions.

### 2. Mermaid Architecture Sketch

~~~mermaid
flowchart LR
    INGEST["Restricted heritage ingest"]
        --> NORM["Normalize & link (internal schemas)"]
    NORM --> MASK["H3 generalization & redaction"]
    MASK --> CATALOG["STAC/DCAT registration"]
    CATALOG --> GRAPH["Heritage nodes in KFM graph"]
    GRAPH --> VIZ["Generalized UI views & Story Nodes"]
~~~

### 3. Roles & Responsibilities

- **Authors** of heritage documentation must adhere to this standard and reference relevant schemas and examples.  
- **Pipeline developers** must treat redaction and generalization as **non‑optional**, config‑driven ETL stages.  
- **UI designers** must respect protection flags in rendering (disable high‑zoom for sensitive hexes, avoid overlays that might re‑identify locations).

---

## ⚖ FAIR+CARE & Governance

### 1. Legal & Policy Anchors

Heritage standards are grounded in:

- Kansas and U.S. frameworks governing archaeological and cultural resource data (e.g., NHPA §304)  
- CARE principles for Indigenous data governance  
- KFM’s internal sovereignty and ethical‑use policies

Where law and community guidance diverge, KFM defaults to the **stricter protective regime**.

### 2. CARE & Sovereignty Practice

At minimum, heritage datasets must:

- flag `indigenous_rights_flag: true` when any Indigenous community’s heritage is involved  
- provide fields for community affiliation, consent status, and special handling instructions  
- respect community decisions regarding visibility, generalization levels, and narrative framing  
- maintain clear contacts and governance notes for escalation

### 3. Governance Review & Audit

- Material changes to this standard require FAIR+CARE Council review and, where relevant, community consultation.  
- Heritage ETL pipelines and UI behaviors are subject to periodic audits:
  - spot‑checking generalized products for re‑identification risk  
  - reviewing telemetry and provenance logs for unauthorized access patterns  
- This document is a **prov:Plan**; authoritative decisions rest with human councils and community partners.

---

## 🕰️ Version History

| Version  | Date       | Notes                                                                                                                                              |
|----------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| v11.0.1  | 2025-12-06 | Aligned with KFM‑MDP v11.2.4; added heading registry, CI test profiles, unified directory layout, and explicit STAC/DCAT/PROV mapping and assets. |
| v11.0.0  | 2025-11-20 | Unified heritage schemas, examples, and assets into a single v11 heritage standards document.                                                      |
| v10.x    | 2025       | Earlier separate heritage standards, schema drafts, and asset guidelines maintained ad‑hoc.                                                       |

---

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.4</sub>

<br/>

<div align="center">

🏺 **Kansas Frontier Matrix — Unified Heritage Standards v11**  
Heritage Protection · Sovereignty‑First · FAIR+CARE Governance  

[📘 Docs Root](../..) · [📂 Standards Index](../README.md) · [🏺 Heritage Index](./README.md) · [⚖ Governance](../governance/ROOT-GOVERNANCE.md)

</div>