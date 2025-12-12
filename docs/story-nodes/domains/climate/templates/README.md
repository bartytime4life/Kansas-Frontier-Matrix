---
title: "🌦️ Kansas Frontier Matrix — Climate Story Node Templates (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/story-nodes/domains/climate/templates/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Climate Systems Board · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.6/storynode-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/storynodes-v11.2.6.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Template Directory README"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "story-nodes"
  applies_to:
    - "docs/story-nodes/domains/climate/templates/README.md"
    - "docs/story-nodes/domains/climate/templates/story-node-climate.md"
    - "docs/story-nodes/domains/climate/templates/story-node-climate.json"
    - "docs/story-nodes/domains/climate/templates/relation-patterns.md"

fair_category: "F1-A2-I2-R2"
care_label: "Environmental"
sensitivity: "Environmental narratives; may reference hazards/impacts; no restricted locations by default"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 climate templates"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/story-nodes/domains/climate/templates/README.md@v11.2.2"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:story-nodes:climate:templates:v11.2.6"
semantic_document_id: "kfm-storynodes-climate-templates-v11.2.6"
event_source_id: "ledger:kfm:doc:story-nodes:climate:templates:v11.2.6"

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
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
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
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/docs-lint.yml"
  environment: "dev → staging → production"

branding_registry:
  graph: "Semantics × Provenance × Spatial Intelligence"
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🌦️ **Kansas Frontier Matrix — Climate Story Node Templates**
`docs/story-nodes/domains/climate/templates/README.md`

**Purpose**  
Provide the **canonical authoring templates**, **JSON skeletons**, and **relation-pattern guidance**
for constructing **Climate Story Nodes** safely, accurately, and consistently under **KFM‑MDP v11.2.6**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Story%20Nodes-Climate-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 story-nodes/
    └── 📁 domains/
        └── 📁 climate/
            └── 📁 templates/
                ├── 📄 README.md                    — ← This index (template contract + usage rules)
                ├── 📝 story-node-climate.md        — Markdown authoring template (narrative scaffold)
                ├── 🧩 story-node-climate.json      — JSON skeleton (schema-aligned fields + placeholders)
                └── 🔗 relation-patterns.md         — Graph-safe relation patterns (climate domain)
~~~

**Normative rule:** every file in this directory MUST remain consistent with the governing Story Node schema and the KFM Markdown Protocol version pinned in front-matter.

---

## 📘 Overview

This directory is the **author-facing template set** for the Climate domain.

It is intended to make climate Story Nodes:

- **scientifically legible** (observations vs. model output vs. interpretation)
- **spacetime-correct** (time intervals, precision, and geometry rules)
- **catalog-ready** (STAC/DCAT-friendly links to datasets and assets)
- **graph-ingestable** (stable IDs + relation patterns that won’t break traversals)
- **public-safe** (no exaggerated attribution; clear uncertainty; governance-aligned language)

### Climate Story Node coverage

Climate Story Nodes commonly describe:

- storms, tornado outbreaks, derechos
- heatwaves, cold spells, freeze events
- drought, precipitation anomalies, hydrologic stressors
- climate variability patterns and seasonal cycles
- smoke and fire-weather context (when relevant)
- event summaries derived from:
  - observations (stations, radar, satellites)
  - reanalysis
  - forecast model outputs
  - curated reports and bulletins

---

## 🧭 Context

KFM treats Story Nodes as governed narrative objects that must remain:

- **traceable** to data and methods (PROV-friendly)
- **composable** across domains (climate ↔ hydrology ↔ ecology ↔ infrastructure)
- **safe to summarize** (Focus Mode may summarize, but may not rewrite policy or invent claims)

For climate content specifically:

- **observations** MUST be separated from **model output**
- **attribution language** MUST be proportional to cited evidence
- **impacts** SHOULD include context (who/what was affected) without speculation

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Template Authoring"] --> B["Schema Aligned JSON and Markdown"]
  B --> C["Validation and Governance Gates"]
  C --> D["Catalog and Graph Ingest"]
  D --> E["Story Nodes and Focus Mode"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### 1. Template intent

These templates exist so that a Climate Story Node can be created with:

- stable identifiers
- predictable sections
- consistent field naming
- explicit provenance
- conservative, evidence-led narrative framing

### 2. Focus Mode behavior

Focus Mode MAY:

- summarize “what happened, where, when, and why we think so”
- highlight key datasets and provenance
- link to STAC/DCAT entries and supporting reports
- surface uncertainty/precision and governance tags

Focus Mode MUST NOT:

- invent climate attribution
- upgrade “model guidance” into “observed truth”
- claim causality beyond cited evidence
- reveal restricted details if any CARE/sovereignty gating applies

---

## 🧪 Validation & CI/CD

Template changes SHOULD be treated as **contract changes**.

When templates change, CI SHOULD run:

- `docs-lint.yml` (KFM‑MDP v11.2.6 structural compliance)
- `schema-lint.yml` (schema and example validation when schemas/examples are updated)
- domain-specific Story Node checks (if present), including:
  - required keys
  - ID formatting rules
  - time interval shape and precision
  - geometry and bbox constraints (where applicable)
  - controlled vocabulary checks (if configured)

**Integrity expectations**

- If a template update changes semantics, update:
  - `previous_version_hash`
  - `doc_integrity_checksum`
  - Version History entry

---

## 📦 Data & Metadata

### 1. Markdown template (`story-node-climate.md`)

The Markdown template SHOULD include prompts for:

- event summary and scope
- observations vs interpretation (explicitly separated)
- data sources and citations (datasets, bulletins, analyses)
- uncertainty and confidence language
- impacts and limitations (without speculation)

### 2. JSON skeleton (`story-node-climate.json`)

The JSON skeleton SHOULD provide placeholders for:

- `id`, `title`, `summary`
- `spacetime.when` (interval + precision)
- `spacetime.geometry` (region, bbox, polygon; as permitted)
- `climate.context` (event type, anomaly metadata, units references)
- `relations[]` (using the patterns documented in `relation-patterns.md`)
- `provenance[]` (datasets, processing steps, human review)
- optional `assets[]` (STAC-like asset references when used)

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. DCAT

Climate Story Nodes can reference DCAT datasets and distributions:

- observational datasets (stations, radar mosaics, satellite products)
- derived datasets (gridded anomalies, composites)
- narrative artifacts (summaries, maps, reports)

Templates SHOULD prompt authors to include stable identifiers and access references, not raw “one-off” links.

### 2. STAC

When climate Story Nodes reference spatial datasets:

- link to STAC Collections/Items for the relevant products
- prefer stable asset identifiers (e.g., `radar`, `satellite`, `anomaly-map`) over ad-hoc naming

### 3. PROV-O

Templates SHOULD support PROV-friendly structure:

- entities: datasets, maps, reports, derived rasters
- activities: processing, interpretation, publication
- agents: pipeline, analyst team, governance body (when applicable)

---

## 🧱 Architecture

In KFM’s documentation architecture:

- templates are **plans** (CIDOC `E29`, PROV `prov:Plan`)
- derived climate Story Nodes become:
  - discoverable documentation artifacts
  - graph nodes connected to data, runs, and governance events
- validation workflows enforce the contract so downstream systems (catalog, graph, UI) remain deterministic

---

## ⚖ FAIR+CARE & Governance

Climate narratives can carry real-world risk if overstated or decontextualized.

Therefore, these templates enforce:

- **FAIR**
  - findable IDs and stable references
  - accessible and reusable structure
  - interoperable metadata patterns (DCAT/STAC/PROV alignment)

- **CARE**
  - responsibility in interpretation
  - clarity about uncertainty and evidence level
  - governance-aligned handling of any restricted or sensitive content

---

## 🕰️ Version History

| Version | Date       | Author                 | Summary                                                                 |
|--------:|------------|------------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-storynodes`      | Updated to KFM‑MDP v11.2.6; corrected relative refs; tightened template/contract rules; expanded governance and validation notes. |
| v11.2.2 | 2025-11-30 | `@kfm-storynodes`      | Initial governed climate template set; synced to v11 domain rules.      |

---

<div align="center">

🌦️ **Kansas Frontier Matrix — Climate Story Node Templates (v11.2.6)**  
Authoring Patterns · Schema Skeletons · Relation Models · Governance-Ready Narrative

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Story%20Nodes-Climate-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />

[⬅ Climate Domain](../README.md) ·
[🧠 Story Nodes Root](../../../README.md) ·
[📄 Templates Index](../../../../templates/README.md) ·
[📘 Docs Root](../../../../README.md) ·
[📘 Markdown Protocol](../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[🧾 Story Node Schema](../../../../../schemas/json/story-node.schema.json) ·
[🧭 STAC Profile](../../../../standards/stac/README.md) ·
[🗃 DCAT Profile](../../../../standards/dcat/README.md) ·
[🧬 PROV Profile](../../../../standards/prov/README.md) ·
[⚖ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>
