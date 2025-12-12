---
title: "🌱 Kansas Frontier Matrix — Soil Story Nodes (Domain Index · Governed · Public-Safe)"
path: "docs/story-nodes/domains/soil/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Soil Domain Board · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.6/storynodes-soil-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/storynodes-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Domain Index"
intent: "kfm-soil-storynodes-domain-index"

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "storynodes-soil"
  applies_to:
    - "docs/story-nodes/domains/soil/**"
    - "schemas/storynodes/**"
    - ".github/workflows/storynodes-validate.yml"
    - ".github/workflows/docs-lint.yml"

fair_category: "F1-A1-I1-R2"
care_label: "Environmental · Land Stewardship"
sensitivity: "General (public-safe soil narratives; no PII; no parcel-owner data; no restricted site disclosure)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Soil Domain Board · KFM FAIR+CARE Council"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 soil Story Nodes"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "KFM Story Node v11"
  - "STAC 1.0.0 (references)"
  - "DCAT 3.0 (references)"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/story-nodes/domains/soil/README.md@v11.2.6"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:storynodes:soil:index:v11.2.6"
semantic_document_id: "kfm-storynodes-soil-index-v11.2.6"
event_source_id: "ledger:storynodes/soil/index"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "timeline-generation"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - summary
    - semantic-highlighting
    - timeline-generation
    - a11y-adaptations
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-architectural-claims
    - narrative-fabrication
    - governance-override

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

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
  - "diagram-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"
  - "sensitivity-check"

ci_integration:
  workflow: ".github/workflows/docs-lint.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  soil: "Soils · Land Stewardship · Evidence-Led Narratives"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🌱 **Kansas Frontier Matrix — Soil Story Nodes**  
`docs/story-nodes/domains/soil/README.md`

**Purpose**  
Define the **soil domain contract** for KFM Story Nodes: scope, templates, examples, relations, validation gates, and governance rules.  
Soil Story Nodes describe **soil properties, soil processes, and land stewardship impacts** across Kansas using **public-safe**, provenance-backed narratives that remain compatible with **STAC/DCAT/PROV** and Focus Mode.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Story_Nodes-Soil-success" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

Soil Story Nodes are **machine-validated narrative objects** that explain soil-related facts and change over time, including:

- Soil properties (texture, organic matter, pH, salinity, bulk density, SOC, etc.)
- Soil moisture / drought-relevant soil conditions (as observations or modeled products, clearly labeled)
- Soil processes (erosion, compaction, salinization, carbon change)
- Land stewardship practices (cover crops, conservation tillage, restoration) **only at public-safe abstraction**
- Cross-domain coupling (soil ↔ hydrology ↔ climate ↔ land cover) without overstating causality

**What this domain index guarantees**

- A predictable directory layout (templates, examples, validators).
- Domain-specific safety rules (no PII; no parcel-owner data; no “re-identification by detail”).
- A clean bridge to catalogs and provenance:
  - Story Node = narrative / semantic layer
  - STAC = geospatial asset layer
  - DCAT = catalog / distribution layer
  - PROV = lineage / accountability layer

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 🧠 story-nodes/
    ├── 📄 README.md                                      — Global Story Nodes index (all domains)
    └── 🌐 domains/
        └── 🌱 soil/
            ├── 📄 README.md                              — ← Soil domain index (this file)
            ├── 📄 relation-patterns.md                   — Allowed relation patterns for soil nodes
            ├── 📁 templates/                             — Canonical authoring templates (Markdown/JSON)
            │   ├── 📄 README.md                          — Templates index (soil)
            │   ├── 📝 story-node-soil.md                 — Authoring template (human-facing)
            │   ├── 🧩 story-node-soil.json               — Schema-aligned JSON skeleton (fixture)
            │   └── 🔗 relation-patterns.md               — Optional: template-scoped relation notes
            ├── 📁 examples/                              — Public-safe example Story Nodes (fixtures)
            │   ├── 📄 README.md                          — Examples index (soil)
            │   └── 🧩 example-*.json                     — Example nodes (generalized; no sensitive detail)
            └── 📁 validators/                            — Domain validator notes + local fixtures
                └── 📄 README.md                          — Validator contract & checks (soil)
~~~

**Author rules (normative)**

- Every new file under `docs/story-nodes/domains/soil/` MUST remain consistent with KFM-MDP v11.2.6.
- The soil domain MUST maintain:
  - `templates/` (how to write)
  - `examples/` (how “good” looks)
  - `relation-patterns.md` (what relations are allowed)
- Examples MUST be **public-safe fixtures**:
  - generalized geometry only
  - no private landowner/parcel identity
  - no sensitive operational details

---

## 🧭 Context

### Soil domain scope in KFM

Soil Story Nodes support analysis and explanation across KFM’s pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → UI → Story Nodes → Focus Mode

In practice, soil nodes may connect to:

- climate nodes (drought, precipitation anomaly, wind regimes)
- hydrology nodes (runoff, infiltration, floodplain dynamics)
- land cover / land use layers (vegetation change, cropland expansion)
- governance + sustainability telemetry (stewardship impact claims must be sourced)

### Public-safe constraints

Soil narratives can become sensitive when they imply:

- parcel-level management practices
- landowner identity
- fine-scale locations that enable targeted inference

Therefore, soil Story Nodes MUST:

- avoid parcel-centric “blame” or “credit” narratives
- remain grounded in data and provenance
- present uncertainties explicitly when using modeled or inferred data

---

## 🗺️ Diagrams

### Soil Story Node lifecycle (conceptual)

~~~mermaid
flowchart LR
  A["Soil source data"] --> B["ETL and QA"]
  B --> C["STAC and DCAT records"]
  C --> D["Soil Story Nodes"]
  D --> E["Validation gates"]
  E --> F["Graph and API"]
  F --> G["UI and Focus Mode"]
~~~

Text note: this flow shows how soil evidence becomes a governed narrative object and is then surfaced safely in Focus Mode.

---

## 🧠 Story Node & Focus Mode Integration

Soil Story Nodes are designed to be consumed by Focus Mode without guessing.

**Focus Mode MAY**

- summarize soil properties and change over time
- highlight “observation vs model” distinctions
- surface provenance links to STAC/DCAT records and pipeline runs
- show safe, generalized spatial context (county / watershed / region-scale)

**Focus Mode MUST NOT**

- invent soil measurements, thresholds, or causes not present in the node or linked evidence
- turn correlation into causation (e.g., “X caused erosion”) unless the node explicitly provides sourced causal evidence
- upgrade governance posture (“certified”, “approved”, “safe”) beyond what the node and governance references state

---

## 🧪 Validation & CI/CD

Soil Story Nodes are **contract-checked**.

### Expected checks

- `docs-lint`
  - front-matter validity, heading registry, directory layout fences, footer links
- `storynodes-validate`
  - Story Node v11 schema validation for all `*.json` fixtures
- Domain safety checks (`sensitivity-check`)
  - blocks precise coordinates when public-safe classification is declared
  - blocks PII, private identifiers, and leak-prone detail patterns
- `provenance-check`
  - ensures version history and provenance fields are coherent and not fabricated

### What must fail CI (normative)

CI MUST fail if any soil Story Node or example includes:

- PII or landowner-identifying data
- parcel IDs, private addresses, or “pinpoint” location metadata in a public-safe context
- hidden or unreferenced governance decisions (policy changes must link to governance docs)
- diagrams that do not parse (Mermaid syntax errors)

---

## 📦 Data & Metadata

### Recommended soil Story Node content blocks

Soil Story Nodes SHOULD include:

- `summary` that states:
  - what is being described
  - whether the evidence is observational or modeled
  - the spatial and temporal granularity
- `spacetime`:
  - an interval for change narratives
  - a geometry that is appropriate for public-safe use
- `measurements` (if your Story Node schema supports it):
  - units declared explicitly
  - source dataset references (STAC/DCAT IDs or stable file refs)
- `provenance`:
  - data sources used
  - pipeline activity that generated derived metrics
  - any transformations applied

### Minimal skeleton (schematic, public-safe)

Adapt field names to the Story Node v11 schema used in your repo.

~~~json
{
  "schema_version": "v11",
  "type": "story-node",
  "domain": "soil",
  "id": "urn:kfm:story-node:soil:example:001",
  "title": "Soil condition narrative (public-safe example)",
  "classification": "Public",
  "jurisdiction": "Kansas / United States",
  "spacetime": {
    "when": { "start": "1930-01-01", "end": "1939-12-31" },
    "geometry": null,
    "geometry_precision": "generalized"
  },
  "claims": [
    {
      "kind": "observation",
      "text": "Example claim with provenance-backed references.",
      "confidence": "documented"
    }
  ],
  "links": {
    "stac": [],
    "dcat": []
  },
  "prov": {
    "wasDerivedFrom": [],
    "wasGeneratedBy": [],
    "wasAttributedTo": []
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT

Soil Story Nodes (and their supporting docs) may be represented in DCAT as:

- `dcat:Dataset` (the node as a documented knowledge asset), with:
  - `dct:title` from the node title
  - `dct:description` from the summary
  - `dct:spatial` (generalized) where allowed
  - `dct:temporal` for the interval described
- `dcat:Distribution` for:
  - the JSON file
  - any public-safe supporting reports

### STAC

When soil nodes reference spatial assets:

- reference STAC Items by stable IDs
- ensure referenced assets are themselves public-safe and do not embed restricted coordinates in metadata

### PROV-O

Soil Story Nodes MUST preserve lineage:

- derived metrics MUST be linked to:
  - pipeline run activities (`prov:Activity`)
  - source datasets (`prov:Entity`)
  - responsible agents (`prov:Agent`)

---

## 🧱 Architecture

At the system level, soil nodes sit between:

- **data assets** (rasters/vectors/tables + STAC/DCAT records), and
- **explanations** (Story Nodes + Focus Mode cards + graph relationships)

Soil domain graph patterns often connect:

- `soil` ↔ `climate` (drought, precipitation, temperature extremes)
- `soil` ↔ `hydrology` (infiltration, runoff, watershed response)
- `soil` ↔ `land-use` (cropping, grassland conversion, conservation programs)

This README defines the **domain boundaries** and how those cross-links must remain provenance-backed.

---

## ⚖ FAIR+CARE & Governance

Soil data is environmental, but governance still applies.

**FAIR**

- stable IDs, predictable paths, and catalog-aligned references improve findability and reuse
- provenance and version history enable auditability

**CARE / Sovereignty**

- soil narratives MUST not expose restricted land or culturally sensitive locations through detail
- if a node intersects Indigenous governance contexts, apply the sovereignty policy and avoid precision that enables re-identification
- when uncertainty exists, state uncertainty and link to governance docs rather than asserting absolutes

---

## 🕰️ Version History

| Version   | Date       | Author       | Summary                                                                 |
|----------:|------------|--------------|-------------------------------------------------------------------------|
| v11.2.6   | 2025-12-12 | `@kfm-soil`  | Initial governed Soil domain index; aligned to KFM-MDP v11.2.6 structure, directory layout profile, validation gates, and governance links. |

---

<div align="center">

🌱 **Kansas Frontier Matrix — Soil Story Nodes (v11.2.6)**  
Public-Safe Environmental Narratives · Provenance-Backed · Governed for Stewardship

<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governed-gold" />
<img src="https://img.shields.io/badge/Focus_Mode-Compatible-informational" />

[⬅ Story Nodes Index](../../README.md) ·
[🌐 Domains Index](../README.md) ·
[🔗 Relation Patterns](./relation-patterns.md) ·
[📁 Templates](./templates/README.md) ·
[🧪 Examples](./examples/README.md) ·
[📘 Docs Home](../../../README.md) ·
[📏 Standards Index](../../../standards/README.md) ·
[📑 Markdown Protocol](../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[📈 Telemetry Standard](../../../standards/telemetry_standards.md) ·
[♿ UI Accessibility](../../../standards/ui_accessibility.md) ·
[⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[📚 Glossary](../../../glossary.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6

</div>
