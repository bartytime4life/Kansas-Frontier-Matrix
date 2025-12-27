---
title: "🏺 Kansas Frontier Matrix — Unified Heritage Standards v11 (Schemas · Examples · Assets)"
path: "docs/standards/heritage/HERITAGE_STANDARDS_v11.md"
version: "v11.0.2"
last_updated: "2025-12-27"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
signature_ref: "releases/v11.0.2/signature.sig"
attestation_ref: "releases/v11.0.2/slsa-attestation.json"
sbom_ref: "releases/v11.0.2/sbom.spdx.json"
manifest_ref: "releases/v11.0.2/manifest.zip"
telemetry_ref: "releases/v11.0.2/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/heritage-standards-v11.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY-4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

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
jurisdiction: "US-KS"
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
  - "docs/standards/heritage/HERITAGE_STANDARDS_v11.md@v11.0.2"
  - "docs/standards/heritage/HERITAGE_STANDARDS_v11.md@v11.0.1"
  - "docs/standards/heritage/HERITAGE_STANDARDS_v11.md@v11.0.0"
  - "docs/standards/heritage/HERITAGE_STANDARDS_v10.md@v10.x"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/heritage-standards-v11.schema.json"
shape_schema_ref: "schemas/shacl/heritage-standards-v11-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:heritage:standards:v11.0.2"
semantic_document_id: "kfm-heritage-standards-v11.0.2"
event_source_id: "ledger:kfm:doc:standards:heritage:HERITAGE_STANDARDS_v11.0.2"
doc_integrity_checksum: "sha256:<calculated-in-ci>"

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
  - "infer_sensitive_locations"

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
    - "infer_sensitive_locations"

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
  - "provenance-check"
  - "accessibility-check"
  - "diagram-check"
  - "secret-scan"
  - "pii-scan"
  - "heritage-schema-lint"
  - "heritage-redaction-check"
  - "heritage-assets-check"
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

fencing_profile: "outer-backticks-inner-tildes-v1"

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

**Status:** Stable / Governed (LTS) · **High‑Risk Domain** · **Redaction Required**

**Purpose:**  
Provide the canonical, governance‑safe **single source of truth** for KFM **heritage‑protection** rules across:

- **Schemas** (JSON Schema + SHACL)  
- **Example Library** (synthetic only)  
- **Assets** (diagrams/icons/templates, abstraction‑only)

This document governs heritage handling across the canonical pipeline:  
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

[![MCP‑DL v6.3](https://img.shields.io/badge/MCP--DL-v6.3-blue)]()  
[![KFM‑MDP v11.2.6](https://img.shields.io/badge/KFM--MDP-v11.2.6-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]()  
[![WCAG 2.1 AA+](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA%2B-brightgreen)]()  
[![License CC‑BY‑4.0](https://img.shields.io/badge/License-CC--BY--4.0-brightgreen)]()

</div>

---

## 📘 Overview

### Purpose

KFM heritage content is **sensitive by default**. This standard exists to ensure that **no heritage pipeline, dataset, visualization, or story** can accidentally publish (or help re‑identify) protected locations or culturally restricted knowledge.

This document is normative for:

- Heritage ETL (generalization/redaction as deterministic steps)
- Heritage metadata (STAC/DCAT/PROV flags and linkage)
- Heritage graph mappings (first‑class nodes + relationships)
- Heritage UI behaviors (zoom limits, search exclusions, disclosure rules)
- Heritage Story Nodes and Focus Mode rendering rules

### Scope

| In scope | Out of scope |
|---|---|
| Standards for handling cultural heritage locations, assets, and narratives (archaeology, historic preservation, cultural landscapes, oral‑history‑linked geographies). | Publishing raw site coordinates or unmasked site geometries. |
| Deterministic generalization/redaction rules and required metadata flags for any distributable artifact. | Creating/overriding access control policy (RBAC/OIDC) — defined in governance/security docs. |
| Synthetic examples demonstrating correct usage **without** exposing real sites. | “Best guess” inference of locations, affiliations, or cultural protocols not explicitly documented. |
| Provenance requirements for auditing: what dataset/run produced a generalized output. | Legal interpretation; this doc may reference laws as context, but does not replace counsel or community governance. |

### Audience

- **Data stewards / heritage curators** (policy + approvals)
- **Pipeline developers** (ETL + validation + provenance)
- **Graph/ontology maintainers** (entity modeling + linkage)
- **API/UI engineers** (enforced redaction + safe rendering)
- **Narrative editors** (Story Nodes + Focus Mode compliance)

### Non‑negotiable invariants

1. **Canonical pipeline ordering**  
   Heritage artifacts must follow: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.

2. **API boundary**  
   The UI must **never** read Neo4j directly; all access is via contracted APIs.

3. **Generalization‑first**  
   Raw coordinates for protected heritage sites are never published in KFM public artifacts. Distributable products use coarse/generalized spatial references (e.g., H3 cells, generalized polygons, bounding regions).

4. **Sovereignty‑first**  
   Indigenous communities retain authority over how cultural data are represented. If community protocols require stricter handling than baseline rules, the stricter regime applies.

5. **Least‑reveal**  
   Public outputs expose only what is required for research, education, or management — no more.

6. **Reproducible redaction**  
   Generalization and redaction must be deterministic and configuration‑driven, producing reproducible outputs given the same inputs and configs.

7. **Provenance‑linked narrative**  
   Focus Mode and Story Nodes must remain provenance‑linked. Any AI‑derived content must be clearly labeled and carry uncertainty/confidence metadata (if included at all).

### Key artifacts and references

| Artifact | Canonical path | Role |
|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline + extension matrix |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Governed Markdown structure |
| Story Node template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Provenance‑linked narrative structure |
| Governance root (v11) | `docs/standards/governance/ROOT-GOVERNANCE.md` | Governance source of truth |
| FAIR+CARE guide (v11) | `docs/standards/faircare/FAIRCARE-GUIDE.md` | Ethics framework |
| Indigenous data protection (v11) | `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md` | Sovereignty/consent constraints |
| This doc’s JSON schema | `schemas/json/heritage-standards-v11.schema.json` | Front‑matter validation |
| This doc’s SHACL shape | `schemas/shacl/heritage-standards-v11-shape.ttl` | Shape/graph validation |

---

## 🗂️ Directory Layout

Emoji‑enriched, CI‑safe layout for this module (per `fencing_profile: outer-backticks-inner-tildes-v1`).

### Repo top‑levels (expected)

~~~text
.github/
data/
docs/
mcp/
schemas/
src/
tests/
tools/
web/
releases/
~~~

### Heritage governance + data locations

~~~text
docs/
├── 📂 standards/
│   ├── 📂 heritage/
│   │   ├── 🏺 HERITAGE_STANDARDS_v11.md        # This file (unified standards)
│   │   ├── 📄 README.md                       # Heritage standards index
│   │   ├── 📂 examples/                       # Synthetic examples only
│   │   └── 📂 assets/                         # Abstraction-only diagrams/icons/templates
│   ├── 📂 governance/
│   ├── 📂 faircare/
│   └── 📂 sovereignty/
│
├── 📂 reports/
│   └── 📂 story_nodes/                        # Canonical story node home (draft/published)
│       ├── 📂 draft/
│       └── 📂 published/
│
└── 📄 MASTER_GUIDE_v12.md

schemas/
├── 📂 json/
│   └── 📂 heritage/                           # Machine-validated heritage schemas
└── 📂 shacl/
    └── 📂 heritage/                           # SHACL shapes / ontology fragments

data/
├── 📂 raw/
│   └── 📂 heritage/                           # RESTRICTED: raw coordinates, confidential notes
├── 📂 work/
│   └── 📂 heritage/                           # Masked/intermediate artifacts
├── 📂 processed/
│   └── 📂 heritage/                           # Generalized layers (hexes/tiles/summaries)
├── 📂 stac/
│   ├── 📂 collections/
│   └── 📂 items/
├── 📂 catalog/
│   └── 📂 dcat/
└── 📂 prov/

src/
├── 📂 pipelines/                              # ETL + catalog build code (no executable code in docs/)
├── 📂 graph/                                  # Ontology + ingest/migrations
└── 📂 server/                                 # API boundary (REST/GraphQL contracts)

web/                                           # React/Map UI (no direct Neo4j calls)
mcp/
└── 📂 runs/                                   # Run records + pointers to PROV bundles (no duplication)
releases/
└── 📂 v11.0.2/                                # Signed manifests, SBOMs, attestations (if used)
~~~

**Directory rules:**

- **No raw coordinates in `docs/`** — raw heritage locations live only in restricted stores (typically `data/raw/heritage/**`).
- `schemas/**` holds machine‑validated schemas; `docs/standards/**` may describe them but should not become the schema source of truth.
- Story Nodes belong in `docs/reports/story_nodes/**` so they can be validated and reviewed consistently before publication.

---

## 🧭 Context

KFM aims to operate as a provenance‑first geospatial + historical atlas. Heritage content adds **heightened sensitivity** and additional governance constraints:

- Heritage datasets often contain **precise locations** (or contextual clues) that should not be publicly disclosed.
- Cross‑domain joins can accidentally re‑identify sensitive locations (e.g., combining generalized heritage layers with detailed environmental or infrastructure datasets).
- Indigenous cultural knowledge can carry community protocols that differ from conventional archival norms; those protocols must be respected in metadata, access, and narrative framing.

**Heritage standards therefore:**

- Define how **location precision** is managed (generalization and masking policies).
- Govern **cataloging** of heritage layers in STAC/DCAT with explicit protection flags.
- Require **provenance** so every generalized product can be traced to workflow runs and (where appropriate) restricted inputs.
- Coordinate with Story Nodes and Focus Mode so narrative overlays never leak restricted detail.

---

## 🗺️ Diagrams

### Allowed diagram profiles

- `mermaid-flowchart-v1` — heritage ETL/generalization/publication flows
- `mermaid-timeline-v1` — high‑level stewardship or historical timelines (no sensitive coordinates)

### Heritage diagram rules

- No diagram may depict the **exact geometry** or **precise coordinates** of a sensitive site.
- Map‑like diagrams use **schematic shapes, H3 cells, coarse regions**, or abstraction-only visuals.
- Every diagram must have a short textual summary nearby (a11y requirement).

### Example — Heritage protection pipeline (non‑negotiable ordering)

_Text summary:_ Restricted inputs are generalized during ETL, then cataloged (STAC/DCAT/PROV), then mapped into the graph, served through APIs, and finally rendered in the UI and Story/Focus experiences.

~~~mermaid
flowchart LR
    RAW["Restricted heritage inputs (internal)"]
      --> ETL["ETL: normalize + generalize + redact (deterministic)"]
    ETL --> CAT["STAC/DCAT/PROV catalogs (generalized outputs only)"]
    CAT --> GRAPH["Graph build (heritage entities as first-class nodes)"]
    GRAPH --> API["Contracted APIs (enforce redaction + access tiers)"]
    API --> UI["UI (React/Map: safe rendering rules)"]
    UI --> STORY["Story Nodes (provenance-linked)"]
    STORY --> FOCUS["Focus Mode (provenance-linked only)"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### 1. Heritage Story Nodes

Heritage Story Nodes:

- Must follow `docs/templates/TEMPLATE__STORY_NODE_V3.md` structure.
- Must reference **generalized spatial footprints** (H3 cells, coarse polygons, or metadata-only) — never raw points.
- Must keep all factual claims **source-linked** (dataset/document IDs) and provenance-linked.

**Do not** embed raw coordinates, restricted site codes, or sensitive notes in narrative text.

#### Example Story Node (synthetic, Markdown shape)

~~~markdown
---
title: "Story Node — Generalized Heritage Landscape (Synthetic Example)"
path: "docs/reports/story_nodes/draft/node-heritage-syn-0001.md"
version: "v0.1.0"
last_updated: "YYYY-MM-DD"
status: "draft"
doc_kind: "StoryNode"
license: "CC-BY-4.0"

heritage_protected: true
cultural_sensitivity: "restricted"
care_level: "KFM-Level-III"

# Generalized-only location reference (no raw coords)
h3_id: "872830829ffffff"
h3_resolution: 7

source_bundle:
  - type: "stac_item"
    id: "stac:item:kfm-heritage-generalized-syn-2025"
  - type: "prov_activity"
    id: "prov:activity:urn:kfm:workflow:heritage-generalization-v11"
---

## Narrative (factual + source-linked)
A generalized representation of a heritage landscape. This narrative is synthetic and intended
to demonstrate structure and governance flags, not to describe a real site.
~~~

### 2. Focus Mode behavior

When Focus Mode renders heritage content:

- **MUST** be provenance-linked (no orphan facts).
- **MUST NOT** attempt to infer hidden locations from generalized data.
- **MUST** label any AI-derived content clearly (if shipped at all) and include uncertainty/confidence metadata.

This document’s AI permissions/prohibitions apply to any Focus Mode transforms of this file.

### 3. Writing patterns for safe heritage narratives

- Prefer **regional** language over micro-toponyms.
- Avoid combining multiple “nearby” clues that could triangulate a protected site.
- Keep each subsection single-purpose so extraction does not create accidental composite hints.

---

## 🧪 Validation & CI/CD

### Document-level checks

All heritage standards Markdown must pass:

- `markdown-lint` — headings/lists/spacing
- `schema-lint` — front‑matter validation against `schemas/json/heritage-standards-v11.schema.json`
- `metadata-check` — required identity/lifecycle/ethics metadata present
- `provenance-check` — front‑matter `provenance_chain` consistent with Version History
- `footer-check` — required governance links present

### Heritage-specific checks

- `heritage-redaction-check` — scans docs/examples/assets for:
  - raw lat/lon values above precision thresholds
  - restricted identifiers accidentally pasted into examples
  - unmasked geometries in embedded GeoJSON
- `heritage-schema-lint` — validates heritage schemas under `schemas/**`
- `heritage-assets-check` — validates that heritage assets:
  - are vector-first (SVG preferred)
  - have required metadata (license, creator, sensitivity tags)
  - are abstraction-only and do not reveal protected sites

### CI behavior contract (governed)

CI should validate what exists and is applicable:

- **Validate if present:** STAC/DCAT/PROV/schemas/telemetry/story nodes referenced by the doc.
- **Skip if not applicable:** If a subsystem is not present in the current repo revision, CI should not invent failures; it should warn and/or mark “missing required artifact” for governance follow‑up.

### Suggested local commands (placeholders)

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Validate governed docs (Markdown protocol + required sections)
# 2) Run schema checks (JSON Schema + SHACL)
# 3) Run heritage redaction scan (coordinates/identifiers/geometry)
# 4) Run link checks (no orphan pointers)
~~~

### Definition of done (for changes to this document)

- [ ] Front‑matter metadata is complete and consistent (path, version, governance refs).
- [ ] No sensitive location data appears anywhere in the document/examples/assets.
- [ ] Examples are synthetic and cannot be re-linked to real sites.
- [ ] Validation profiles are actionable (can be enforced in CI).
- [ ] Story Node and Focus Mode rules are provenance‑linked and aligned with governance.

---

## 📦 Data & Metadata

This section merges the **Schemas**, **Example Library**, and **Assets** into a single reference.

### 1. Heritage schema registry (machine-validated)

**Canonical home:** `schemas/**` (machine validation).  
**Documentation home:** `docs/standards/heritage/**` (human guidance).

Recommended layout:

~~~text
schemas/
├── 📂 json/
│   └── 📂 heritage/
│       ├── 📄 h3-generalization-standard.schema.json
│       ├── 📄 heritage-sensitive-location.schema.json
│       ├── 📄 heritage-dataset.schema.json
│       ├── 📄 heritage-protection-flags.schema.json
│       └── 📄 heritage-lineage-provenance.schema.json
└── 📂 shacl/
    └── 📂 heritage/
        ├── 📄 heritage-sensitive-location.shape.ttl
        ├── 📄 heritage-dataset.shape.ttl
        └── 📄 heritage-lineage-provenance.shape.ttl
~~~

**Implementation note:** If any referenced schema does not yet exist, treat it as a required artifact to be created under the canonical `schemas/**` tree before publishing heritage data.

### 2. Example library (synthetic only)

~~~text
docs/standards/heritage/examples/
├── 📄 h3-generalization-demo.json
├── 📄 sensitive-location-example.json
├── 📄 heritage-dataset-stac.example.json
├── 📄 heritage-dataset-dcat.example.json
├── 📄 provenance-lineage-example.json
└── 📄 storynode-heritage-demo.example.md
~~~

All examples MUST be:

- Synthetic
- Non-identifying
- Safe to publish within internal docs (no raw coords, no real site IDs, no restricted notes)

#### 2.1 Example — H3 generalized cell summary (synthetic)

~~~json
{
  "h3_id": "872830829ffffff",
  "h3_resolution": 7,
  "site_count": 4,
  "periods": ["Archaic", "Late Prehistoric"],
  "heritage_protected": true,
  "generalization_method": "H3",
  "raw_coordinates_removed": true,
  "care_level": "KFM-Level-III",
  "mcp_protected": true
}
~~~

#### 2.2 Example — Sensitive location metadata (synthetic)

~~~json
{
  "id": "KFM-SYN-HER-0001",
  "type": "heritage_site",
  "cultural_sensitivity": "restricted",
  "legal_basis": "Applicable heritage confidentiality policy (example)",
  "care_level": "KFM-Level-III",
  "community_affiliation": ["Example Nation (synthetic)"],
  "description": "Synthetic example record demonstrating governance fields and generalized location handling.",
  "h3_id": "872830829ffffff",
  "h3_resolution": 7,
  "raw_coordinates_removed": true,
  "mcp_protected": true
}
~~~

#### 2.3 Example — Heritage STAC Item (generalized / metadata-only)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Item",
  "id": "kfm-heritage-generalized-syn-2025",
  "collection": "kfm-heritage",
  "geometry": null,
  "bbox": null,
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "heritage_protected": true,
    "care_level": "KFM-Level-III",
    "generalization_method": "H3",
    "h3_resolution": 7,
    "raw_coordinates_removed": true,
    "mcp_protected": true
  },
  "assets": {
    "hex_geojson": {
      "href": "hexes/kfm-heritage-generalized-syn-2025.geojson",
      "type": "application/geo+json",
      "roles": ["data", "generalized"]
    }
  }
}
~~~

#### 2.4 Example — Heritage DCAT metadata (example shape)

~~~json
{
  "dct:title": "Kansas Protected Heritage (Generalized, Synthetic Example)",
  "dct:description": "Synthetic example describing a generalized heritage dataset with redaction and provenance requirements.",
  "dct:spatialResolution": "H3-r7",
  "dct:provenance": "Generalized from restricted inputs via deterministic redaction workflow.",
  "dct:conformsTo": "KFM Heritage Standards v11",
  "dct:rights": "Restricted handling; do not redistribute raw locations."
}
~~~

#### 2.5 Example — PROV lineage (example shape)

~~~json
{
  "version": "2025.12.27",
  "lineage": {
    "predecessor": "2025.12.06",
    "latest": "2025.12.27"
  },
  "reproducibility": {
    "workflow_hash": "sha256:<workflow-config-hash>",
    "inputs_hash": "sha256:<restricted-inputs-hash>",
    "prov": {
      "wasDerivedFrom": "urn:kfm:raw:heritage:<restricted-dataset-id>",
      "generatedBy": "urn:kfm:workflow:heritage-generalization-v11"
    }
  }
}
~~~

### 3. Heritage assets (abstraction-only)

~~~text
docs/standards/heritage/assets/
├── 📂 diagrams/        # SVG preferred; no exact site shapes
├── 📂 icons/           # Sensitivity flags, tier icons
├── 📂 infographics/    # Risk matrices, generalization scales
└── 📂 templates/       # STAC/DCAT/Story Node templates (example scaffolds)
~~~

**Asset requirements:**

- Avoid sensitive/sacred imagery unless explicitly vetted and approved.
- Locations must be abstracted (no recognizable sites, no unmasked imagery).
- Prefer SVG and meet WCAG 2.1 AA+ needs (contrast + text alternatives).
- Include license/creator metadata and heritage sensitivity tags where applicable.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. Linkage requirements (cross-system)

Heritage artifacts must remain linkable across standards:

- **STAC** Item/Collection IDs identify distributable assets.
- **DCAT** Dataset/Distribution IDs support discovery and access metadata.
- **PROV** bundles record lineage for ETL runs and transformations.
- **Graph** nodes reference STAC/DCAT/PROV identifiers (no “floating” entities).
- **Story Nodes** reference dataset/document IDs and graph IDs.

### 2. DCAT alignment

Heritage datasets should be represented as DCAT `dcat:Dataset` with:

- `dct:title`, `dct:description`, `dct:identifier`
- generalized `dct:spatial` (coarse geometries only)
- explicit `dct:accessRights` / `dct:rights` describing restrictions and handling expectations
- provenance pointers (e.g., `dct:provenance`) that link to PROV runs

### 3. STAC alignment

Heritage layers should be represented in STAC with:

- generalized spatial representations only (or metadata-only items with `geometry: null`)
- properties that surface protection signals:
  - `heritage_protected: true`
  - `care_level`
  - `generalization_method`
  - `h3_resolution` (if used)
- assets clearly labeled as generalized: `roles: ["data", "generalized"]`

### 4. PROV-O alignment

Heritage pipelines must emit provenance such that:

- restricted raw inputs are `prov:Entity` (access-controlled)
- generalization workflows are `prov:Activity` with config and version identifiers
- generalized outputs are derived `prov:Entity` with:
  - `prov:wasDerivedFrom` restricted input IDs
  - `prov:wasGeneratedBy` workflow run IDs
  - integrity hashes for auditing

**Recommended practice:** Prefer meaningful runs to produce (or link to) PROV bundles under `data/prov/**`, while `mcp/runs/**` stores pointers/IDs rather than duplicating provenance payloads.

---

## 🧱 Architecture

### 1. Heritage data flow (conceptual)

Heritage content moves through KFM in a controlled, contract-driven way:

1. **Ingest restricted sources** into protected storage (`data/raw/heritage/**`).
2. **Normalize & link** to internal schemas and graph (still access-controlled).
3. **Generalize & redact** via deterministic workflows (policy-driven configuration).
4. **Catalog** generalized outputs in STAC/DCAT/PROV.
5. **Serve** through APIs (enforce redaction + tiering).
6. **Render** in UI/Story/Focus with safety constraints and provenance.

### 2. Mermaid architecture sketch (including API boundary)

~~~mermaid
flowchart LR
    INGEST["Restricted ingest (data/raw/heritage)"] --> NORM["Normalize & link (internal)"]
    NORM --> MASK["Generalize & redact (deterministic)"]
    MASK --> CAT["STAC/DCAT/PROV (generalized only)"]
    CAT --> GRAPH["Graph build (Neo4j)"]
    GRAPH --> API["APIs (contracted boundary)"]
    API --> UI["UI (React/Map: safe rendering)"]
    UI --> STORY["Story Nodes"]
    STORY --> FOCUS["Focus Mode"]
~~~

### 3. Implementer responsibilities

- **Docs authors:** do not include sensitive coordinates, identifiers, or unapproved imagery.
- **Pipeline developers:** treat redaction/generalization as non-optional ETL stages with reproducible configs.
- **Graph/API engineers:** ensure restricted details cannot be retrieved via public endpoints.
- **UI designers:** enforce zoom/search/overlay rules so generalized layers cannot be re-identified.

---

## ⚖ FAIR+CARE & Governance

### 1. Legal/policy anchors (context)

Heritage confidentiality may be required by applicable legal and policy frameworks and by community governance protocols. When external law and community guidance differ in strictness, KFM defaults to the **stricter protective regime**.

### 2. CARE & sovereignty practice (minimum)

Heritage datasets must:

- flag `indigenous_rights_flag: true` when any Indigenous community heritage is involved
- record consent/handling constraints as metadata (where governance permits)
- support community decisions about visibility, generalization, and narrative framing
- maintain stewardship contacts and escalation paths (via governance docs)

### 3. Governance review triggers

Changes to this document or to heritage pipelines require governance review when they:

- change generalization/redaction policy
- introduce new heritage sources or new public distributions
- alter UI rendering behavior for protected content
- introduce any AI-derived narrative content beyond permitted transforms

---

## 🕰️ Version History

| Version | Date | Notes |
|---|---|---|
| **v11.0.2** | 2025-12-27 | Refined to align with KFM‑MDP v11.2.6 conventions, made pipeline ordering + API boundary explicit, strengthened CI profiles, and hardened synthetic examples (no real-looking IDs/affiliations). |
| v11.0.1 | 2025-12-06 | Aligned with earlier v11 doc structure; added CI test profiles and explicit STAC/DCAT/PROV mapping; clarified synthetic-only examples and asset rules. |
| v11.0.0 | 2025-11-20 | Unified heritage schemas, examples, and assets into a single v11 heritage standards document. |
| v10.x | 2025 | Earlier separate heritage documents and drafts (schemas, examples, and asset guidelines maintained ad‑hoc). |

---

<div align="center">

🏺 **Kansas Frontier Matrix — Unified Heritage Standards v11**  
Heritage Protection · Sovereignty‑First · FAIR+CARE Governance  

[📘 Docs Root](../..) · [📂 Standards Index](../README.md) · [🏺 Heritage Index](./README.md) · [🧭 Master Guide](../../MASTER_GUIDE_v12.md) · [⚖ Governance](../governance/ROOT-GOVERNANCE.md) · [🤝 FAIR+CARE Guide](../faircare/FAIRCARE-GUIDE.md) · [🪶 Indigenous Data Protection](../sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
