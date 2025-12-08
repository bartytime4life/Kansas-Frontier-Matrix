---
title: "📜 Kansas Frontier Matrix — History Story Nodes Domain Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/story-nodes/domains/history/README.md"
version: "v11.2.4"
last_updated: "2025-12-07"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council · History Working Group"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "StoryDomainGuide"
intent: "story-nodes-domain-history-index"
role: "history-story-domain-index"
category: "Story Nodes · Historical Narratives"

commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/story-nodes-history-telemetry.json"
telemetry_schema: "schemas/telemetry/story-nodes-history-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Documentation / History"
indigenous_rights_flag: true
redaction_required: false

json_schema_ref: "schemas/json/story-nodes-history-domain-v1.schema.json"
shape_schema_ref: "schemas/shacl/story-nodes-history-domain-v1-shape.ttl"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Article"
  owl_time: "ProperInterval"
  prov_o: "prov:Collection"
  geosparql: "geo:FeatureCollection"

doc_uuid: "urn:kfm:doc:story-nodes:domains:history:index:v11.2.4"
semantic_document_id: "kfm-story-nodes-domain-history-index"
event_source_id: "ledger:docs/story-nodes/domains/history/README.md"
doc_integrity_checksum: "<sha256-of-this-file>"
immutability_status: "version-pinned"

machine_extractable: true
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative additions"
  - "fabricated historical events"
  - "unverified architectural claims"
  - "governance-override"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next major Story Node domain reorganization"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — History Story Nodes Domain Index**  
`docs/story-nodes/domains/history/README.md`

**Purpose**  
Serve as the **canonical index and design guide** for all **history-focused Story Nodes** in the Kansas Frontier Matrix (KFM), spanning **Kansas history** and **KFM project history** and connecting them to the Neo4j graph, STAC/DCAT catalogs, and Focus Mode.

</div>

---

## 📘 Overview

The **History Story Nodes Domain** organizes narrative units about:

- **Kansas history** — from pre‑contact and treaty eras through agriculture, industry, energy, and digital infrastructure.  
- **KFM project history** — major releases, architectural shifts, governance milestones, and key incidents (linked to `docs/history/**`).

Each Story Node in this domain is:

- Backed by **graph entities** (Events, Places, People, Sources).  
- Anchored in **time** (OWL‑Time intervals) and **space** (GeoJSON/H3 footprints).  
- Connected to **datasets and documents** via PROV-O and DCAT/STAC references.  
- Designed for use in **Focus Mode**, time‑scrubbers, and narrative overlays on maps and timelines.

This README defines:

- How history Story Nodes are organized on disk.  
- How they relate to `docs/history/**` and the KFM graph.  
- How authors should structure and validate history Story Node bundles.

---

## 🗂️ Directory Layout

```text
📁 docs/
└── 📁 story-nodes/
    └── 📁 domains/
        └── 📁 history/
            📄 README.md                        # ← This file (history Story Node domain index)
            📁 kansas-history/                  # Kansas historical narratives
            │   📄 README.md                    # Domain intro for Kansas history Story Nodes
            │   📁 eras/                        # Eras & long intervals (e.g., pre-contact, statehood)
            │   │   📄 00-precontact.md
            │   │   📄 10-territorial-kansas.md
            │   │   📄 20-statehood-and-railroads.md
            │   │   📄 30-dust-bowl-and-new-deal.md
            │   │   📄 40-postwar-and-interstates.md
            │   │   📄 50-energy-digital-frontier.md
            │   📁 events/                      # Discrete, date-bounded historical events
            │   │   📄 1854-kansas-nebraska-act.md
            │   │   📄 1861-kansas-statehood.md
            │   │   📄 1930s-dust-bowl-sequences.md
            │   │   📄 1950s-interstate-buildout.md
            │   └── 📁 figures/                 # Key people & organizations (biographical Story Nodes)
            │       📄 lane-james-henry.md
            │       📄 nicodemus-founders.md
            │       📄 osage-nation-land-history.md
            │
            📁 project-history/                 # KFM project history Story Nodes
            │   📄 README.md                    # Bridge to docs/history/** (project history archive)
            │   📄 kfm-era-v10-launch.md
            │   📄 kfm-era-v11-focus-mode-expansion.md
            │   📄 kfm-governance-milestones.md
            │
            📁 bundles/                         # Machine-readable Story Node bundles (JSON/JSON-LD)
            │   📄 kansas-history-timeline-v1.json
            │   📄 project-history-timeline-v1.json
            │
            📁 schemas/                         # Domain-specific Story Node schemas and examples
                📄 story-node-history-example.md
                📄 story-node-history-fields.md
```

All narrative Markdown files must be:

- **Story-Node extractable** (consistent headings, metadata blocks).  
- **Graph-insertable** (clear references to events, places, people, docs).  
- **Catalog-indexable** (links to STAC/DCAT/PROV entities where applicable).

---

## 🧭 Domain Scope & Relationship to Other Docs

History Story Nodes sit at the intersection of:

- `docs/history/**` — **factual historical ledger** (project + datasets + governance).  
- `docs/analyses/**` — analytical work (e.g., historical land use, hydrology).  
- `data/stac/**` + `dist/provenance/**` — data and provenance catalogs.  
- `src/graph/**` — graph schema and ingestion code.

Design intent:

- **Kansas history** Story Nodes:
  - Provide narrative context for how landscapes, infrastructure, and communities evolved.  
  - Link to spatial layers (e.g., treaties, land use, railroads, energy infrastructure).  
  - Integrate with Focus Mode to explain **why the map looks the way it does**.

- **KFM project history** Story Nodes:
  - Summarize how KFM itself has evolved (versions, patterns, governance).  
  - Link directly to `docs/history/releases/**`, `docs/history/architecture/**`, and incident postmortems.  
  - Support meta‑views (e.g., “What changed between v10 and v11?”).

History Story Nodes **must not** introduce new historical claims; they must reference and assemble already‑documented facts and sources.

---

## 🧩 Story Node Model (History Domain)

History Story Nodes follow the generic Story Node schema, specialized for history:

### 1. Minimal conceptual fields

- `id` — globally unique Story Node identifier (e.g., `urn:kfm:story:history:events:1854-kansas-nebraska-act:v1`).  
- `title` — concise, human-readable title.  
- `text` — narrative body (Markdown), fact-based with citations.  
- `temporal_extent` — OWL‑Time interval:
  - `start_at` / `end_at` (ISO 8601, may be same day or long interval).  
- `spatial_extent` — spatial footprint:
  - GeoJSON bounding box or `H3` index set; can be generalized for sovereignty/CARE.  
- `graph_links`:
  - References to Neo4j nodes: `HistoricalEvent`, `Place`, `Person`, `Dataset`, `Document`.  
- `sources`:
  - References to KFM docs (e.g., `docs/history/...`), external citations, or datasets (STAC/DCAT IDs).  
- `care_flags`:
  - Whether narrative includes Indigenous lands, sacred sites, or sensitive cultural content.

### 2. Example (JSON, conceptual)

```json
{
  "id": "urn:kfm:story:history:events:1854-kansas-nebraska-act:v1",
  "domain": "history",
  "kind": "event",
  "title": "The Kansas–Nebraska Act and the Opening of the Kansas Territory",
  "temporal_extent": {
    "start_at": "1854-05-30",
    "end_at": "1854-05-30"
  },
  "spatial_extent": {
    "h3": ["871fb5bffffffff", "871fb5cffffffff"],
    "note": "Generalized; see treaty and land cession datasets for precise boundaries."
  },
  "graph_links": {
    "events": ["HistoricalEvent:KansasNebraskaAct1854"],
    "places": ["Place:KansasTerritory"],
    "documents": ["Document:US_Statutes_at_Large_10_277"]
  },
  "sources": [
    "docs/history/datasets/heritage-history.md#kansas-nebraska-act",
    "docs/history/governance/sovereignty-milestones.md#treaty-land-context"
  ],
  "care_flags": {
    "involves_indigenous_lands": true,
    "additional_review_required": true
  }
}
```

Concrete JSON/JSON‑LD bundle formats must conform to:

- `json_schema_ref` and `shape_schema_ref` referenced in the front-matter.

---

## 🌐 Graph & Catalog Alignment

History Story Nodes must be expressible as:

- **Neo4j** subgraphs:
  - `(:StoryNode {id, domain, title, ...})`  
  - Relationships:
    - `(:StoryNode)-[:DESCRIBES_EVENT]->(:HistoricalEvent)`  
    - `(:StoryNode)-[:DESCRIBES_PLACE]->(:Place)`  
    - `(:StoryNode)-[:CITES_DOCUMENT]->(:Document)`  
    - `(:StoryNode)-[:LINKS_DATASET]->(:DatasetVersion)`

- **PROV-O**:
  - Story Nodes are `prov:Entity` linked to:
    - `prov:wasDerivedFrom` historical documents and datasets,  
    - `prov:wasAttributedTo` authors or working groups.

- **STAC/DCAT**:
  - Where relevant, Story Nodes may be referenced from:
    - STAC `links` (e.g., `"rel": "describes"`),  
    - DCAT `dct:description` or `prov:qualifiedAttribution` fields.

The goal is that any Story Node can be reconstructed or validated from:

- Historical docs under `docs/history/**`,  
- Catalogs in `data/stac/**` and DCAT exports,  
- Graph content in Neo4j.

---

## 🧪 Validation, FAIR+CARE & CI

History Story Nodes are subject to:

- **FAIR+CARE**:
  - Especially for narratives involving Indigenous lands, treaties, or cultural heritage.  
  - Story Nodes must respect sovereignty policies and may require **IDGB review**.

- **Validation**:
  - JSON/JSON‑LD bundles validated against:
    - `json_schema_ref` (`story-nodes-history-domain-v1.schema.json`),  
    - `shape_schema_ref` (SHACL constraints on graph alignment).
  - Markdown Story Nodes must:
    - Include front-matter that identifies their `id`, `domain`, and `graph_links`.  
    - Avoid speculative or fabricated history.

- **CI checks**:
  - `metadata-check` — front-matter and field coverage.  
  - `schema-lint` / `shape-lint` — for bundles under `bundles/`.  
  - `provenance-check` — Story Nodes reference real docs/datasets/graph entities.  
  - Optional narrative quality linting (e.g., link presence, date formats).

Non-compliant Story Nodes must not be promoted to production Focus Mode views.

---

## 🕰️ Version History

| Version  | Date       | Summary                                                                                   |
|----------|------------|-------------------------------------------------------------------------------------------|
| v11.2.4  | 2025-12-07 | Initial governed History Story Nodes domain index; aligned with KFM-MDP v11.2.4 and project history archive. |

---

<div align="center">

📜 **Kansas Frontier Matrix — History Story Nodes Domain**  

[📘 Docs Root](../../../README.md) ·  
[📜 Project History Archive](../../../history/README.md) ·  
[⚖️ Root Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
