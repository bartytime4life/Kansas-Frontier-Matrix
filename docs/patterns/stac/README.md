---
title: "🛰 STAC Patterns for KFM v11"
path: "docs/patterns/stac/README.md"

version: "v0.1.0"
last_updated: "2025-12-16"
release_stage: "Draft"
lifecycle: "Working Draft"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
content_stability: "evolving"

status: "Draft"
doc_kind: "Pattern"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "documentation"
  applies_to:
    - "docs/patterns/stac/**"
    - "data/stac/**"
    - "tools/validation/**"
    - "schemas/**"
    - "src/pipelines/**"
    - "docs/data/**"
  out_of_scope:
    - "Direct frontend-to-graph access (UI consumes via APIs)"
    - "STAC API infrastructure deployment details"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive by default; apply masking rules for sensitive locations)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Review on KFM-MDP major revision (v12)"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"
  - "KFM Ontology (Neo4j)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
provenance_chain: []
story_node_refs: []

doc_uuid: "urn:kfm:doc:patterns:stac:readme:v0.1.0"
semantic_document_id: "kfm-patterns-stac-readme"
event_source_id: "ledger:kfm:doc:patterns:stac:readme:v0.1.0"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fencing_profile: "outer-backticks-inner-tildes-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"
  - "secret-scan"
  - "pii-scan"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---


<div align="center">

# 🛰 STAC Patterns for KFM v11

`docs/patterns/stac/README.md`

**Purpose**  
Define how KFM produces, validates, and publishes STAC catalogs so spatiotemporal assets are discoverable, versioned, and provenance-linked across the KFM pipeline (ETL → STAC/DCAT/PROV → Graph → APIs → UI).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/STAC-1.0.0-blue" />
<img src="https://img.shields.io/badge/Status-Draft-yellow" />

[📘 Docs Root](../../README.md) ·
[📂 Standards Index](../../standards/README.md) ·
[📄 Templates Index](../../templates/README.md) ·
[⚙ Workflows](../../workflows/README.md) ·
[🏛️ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>

## 📘 Overview

This pattern pack explains:

- What goes in `data/stac/` (Catalogs, Collections, Items).
- How STAC records relate to DCAT (catalog interoperability) and PROV‑O (lineage).
- How STAC versioning concepts are applied so updates remain traceable.

Non-goals:

- Replacing domain schemas under `data/processed/`.
- Defining UI behavior (UI consumes catalog through APIs; do not couple UI to STAC storage layout).

## 🗂️ Directory Layout

STAC metadata lives under `data/stac/` (Collections + Items). Domain assets referenced by STAC live under `data/processed/` (or other `data/**` subtrees).

~~~text
📁 KansasFrontierMatrix/
├── 📁 data/                                      — Data lifecycle & catalogs
│   ├── 📁 stac/                                  — STAC collections & items (spatiotemporal metadata)
│   │   ├── 🧾 catalog.json                       — Root STAC Catalog (optional but recommended)
│   │   └── 📁 collections/
│   │       └── 📁 <collection-id>/
│   │           ├── 🧾 collection.json            — STAC Collection
│   │           └── 📁 items/
│   │               └── 🧾 <item-id>.json         — STAC Item(s)
│   ├── 📁 processed/                             — Canonical processed outputs (assets referenced by STAC)
│   └── 📁 checksums/                             — Integrity hashes (when used)
├── 📁 docs/                                      — Documentation (human + machine readable)
│   ├── 📁 patterns/
│   │   └── 📁 stac/
│   │       └── 📄 README.md                      — This document
│   ├── 📁 data/                                  — Data contracts, catalogs, schemas (DCAT docs)
│   └── 📁 standards/                             — KFM standards (Markdown, governance, FAIR+CARE)
├── 📁 tools/
│   └── 📁 validation/                            — STAC/DCAT schema checks, link checks, lint scripts
└── 📁 schemas/                                   — Schemas (docs, telemetry, SHACL, STAC/DCAT mappings)
    ├── 📁 json/
    └── 📁 shacl/
~~~

Notes:

- Keep **data assets** under `data/processed/` (or other `data/**` subtrees).
- Keep **metadata catalogs** under `data/stac/`.
- Avoid duplicating large assets inside `data/stac/`; Items should reference assets by `assets.*.href`.

## 🧭 Context

In KFM, STAC functions as the “catalog spine” for geospatial (and time-aware) assets:

- **ETL / ingestion** extracts and normalizes raw sources into canonical artifacts.
- **STAC (1.0.0)** describes each dataset with footprint, time, asset links, and properties.
- **DCAT (3.0)** expresses dataset-level catalog metadata for broader interoperability.
- **PROV‑O** captures lineage (what a dataset was derived from, and which activity produced it).
- **Graph (Neo4j)** links STAC objects (and their versions) to semantic entities and Story Nodes.

## 🧱 Architecture

### Two supported publication modes

1. **Static catalog (files on disk)**
   - STAC JSON stored in `data/stac/`.
   - Suitable for “release artifacts” and offline review.

2. **Service-backed catalog (STAC API)**
   - Catalog served via an API layer, backed by a database.
   - Suitable for fast search (bbox/time/property filtering) and large item counts.

KFM may use either (or both): static JSON for governance/release packaging and an API for interactive discovery.

### Versioning model

KFM applies STAC versioning concepts to keep updates traceable:

- When a source changes, mint a new Item version and relate it to the prior version (predecessor/successor).
- Preserve stable identifiers where appropriate and expose “current vs historical” in downstream systems (graph + APIs).

## 📦 Data & Metadata

### Core STAC objects

- **Catalog**: entry point and link hub (optional but recommended).
- **Collection**: groups related Items and declares extents.
- **Item**: describes one asset or one logical dataset “unit” with geometry + time + assets.

### Minimal Item shape

Example below assumes the Item is stored at `data/stac/collections/<collection-id>/items/<item-id>.json` and references a processed asset under `data/processed/…`.

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "<item-id>",
  "collection": "<collection-id>",
  "geometry": { "type": "Polygon", "coordinates": [] },
  "bbox": [-180.0, -90.0, 180.0, 90.0],
  "properties": {
    "datetime": "2025-01-01T00:00:00Z"
  },
  "assets": {
    "data": {
      "href": "../../../../processed/<domain>/<asset>",
      "type": "application/octet-stream",
      "roles": ["data"]
    }
  },
  "links": [
    { "rel": "self", "href": "./<item-id>.json", "type": "application/geo+json" }
  ]
}
~~~

Conventions:

- Use deterministic, stable `<collection-id>` and `<item-id>` values (avoid timestamps in IDs unless the dataset identity is time-sliced).
- Put domain-specific fields in `properties` and/or via `stac_extensions` rather than inventing ad-hoc top-level keys.
- Prefer explicit licensing and citation metadata (via DCAT mapping and/or relevant STAC extensions).

### Extensions

Common extensions to consider (use only what you need):

- **Versioning** (predecessor/successor and version fields)
- **Projection** (`proj:*`) when CRS/transform matters
- **Scientific / citations** when the asset is tied to publications
- **EO** (electro‑optical metadata) when relevant

## 🌐 STAC, DCAT & PROV Alignment

KFM treats these as complementary layers:

- **STAC**: spatiotemporal *asset* metadata and discovery structure
- **DCAT**: dataset catalog interoperability (titles/descriptions/keywords/licenses/distributions)
- **PROV‑O**: transformation and derivation lineage

### Mapping guidance

| STAC field | What it represents | Where it tends to map in KFM |
|---|---|---|
| `id` | Stable dataset/item identifier | Dataset/Item UUID or semantic ID |
| `geometry` / `bbox` | Spatial footprint / extent | GeoJSON geometry + graph spatial node |
| `properties.datetime` (or time range) | Temporal scope | Temporal extent fields + graph time node |
| `assets.*.href` | Distribution/asset location | DCAT Distribution + API access URL |
| `links` | Relationship graph | Catalog traversal + version/predecessor edges |
| `properties.*` | Domain metadata | Graph properties + search index fields |

### Provenance pattern

- Use PROV to express: *this item was derived from X via activity Y*.
- Keep provenance “machine-first”: stable IDs, timestamped activities, and explicit agent/role when available.

## 🧠 Story Node & Focus Mode Integration

STAC Items can represent:

- Primary assets (e.g., scanned maps, georeferenced rasters, vector layers)
- Derived narrative artifacts (e.g., Story Node datasets produced from extraction/curation)

When STAC represents derived narrative artifacts:

- Ensure the Item includes provenance links (PROV) back to original sources.
- Keep versions explicit so Focus Mode can “lock” to a historical state for reproducibility.

## 🧪 Validation & CI/CD

Validation is mandatory before catalog publication:

- **Schema checks**: STAC JSON schema compliance (Item/Collection/Catalog).
- **Required fields**: at minimum `id`, `geometry`, and `datetime` for Items.
- **Link integrity**: `self`, `parent`, `collection`, `root`, and asset `href` targets resolve.
- **Versioning integrity**: predecessor/successor relationships are acyclic and coherent.

Recommended artifacts:

- Store validation outputs under `data/reports/` (e.g., `data/reports/stac-validation/`).
- Pin validator versions in CI to keep results reproducible.

## 🗺️ Diagrams

### KFM catalog flow

~~~mermaid
flowchart LR
  A["Raw sources\\ndata/raw"] --> B["ETL / normalization\\ndata/processed"]
  B --> C["STAC metadata\\ndata/stac"]
  B --> D["DCAT metadata\\ndocs/data or data catalogs"]
  B --> E["PROV lineage\\ncatalog + graph"]
  C --> F["Graph ingest\\nNeo4j"]
  D --> F
  E --> F
  F --> G["APIs"]
  G --> H["Web UI\\nReact + MapLibre"]
  G --> I["Focus Mode\\nStory Nodes"]
~~~

### Versioning flow

~~~mermaid
flowchart TB
  V1["Item v1"] -->|successor| V2["Item v2"]
  V2 -->|successor| V3["Item v3"]
  V2 -->|derived from| S["Source asset"]
~~~

## ⚖ FAIR+CARE & Governance

- Treat catalog metadata as governed: if you change identifiers, licensing, or provenance semantics, it may require review under governance processes.
- If an asset or location is sensitive (cultural heritage sites, vulnerable resources, etc.), avoid publishing precise coordinates and follow the Indigenous Data Protection policy.
- Ensure license and attribution are present and consistent across STAC (where expressed), DCAT, and downstream graph/API representations.
- Changes to **license terms**, **security policy**, or **sovereignty handling** should be treated as governance-reviewed edits (not AI-autopatched changes).

## 🕰️ Version History

| Version | Date | Changes |
|---|---:|---|
| v0.1.0 | 2025-12-16 | Initial STAC pattern README (front matter + structure, alignment, validation, diagrams). |

---

<div align="center">

[📘 Docs Root](../../README.md) ·
[📂 Standards Index](../../standards/README.md) ·
[🏛️ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>