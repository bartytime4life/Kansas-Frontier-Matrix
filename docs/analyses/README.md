---
title: "📘 Kansas Frontier Matrix — Analyses Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"

doc_uuid: "urn:kfm:doc:analyses-overview:v11.2.6"
semantic_document_id: "kfm-doc-analyses-overview"
event_source_id: "ledger:kfm:doc:analyses-overview:v11.2.6"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/analyses-overview-v4.json"
signature_ref: "../../releases/v11.2.6/signature.sig"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "analyses-index"

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

provenance_chain:
  - "docs/analyses/README.md@v11.2.4"
  - "docs/analyses/README.md@v11.0.0"
  - "docs/analyses/README.md@v10.2.2"
  - "docs/analyses/README.md@v10.2.0"
  - "docs/analyses/README.md@v10.1.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../schemas/json/kfm-analyses-overview-v11.2.6.schema.json"
shape_schema_ref: "../../schemas/shacl/kfm-analyses-overview-v11.2.6-shape.ttl"
story_node_refs: []

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "analyses"
  applies_to:
    - "docs/analyses/**"

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
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
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

# 📘 **Kansas Frontier Matrix — Analyses Overview (v11.2.6)**
`docs/analyses/README.md`

**Purpose**
Provide the canonical entry point for analysis work in the Kansas Frontier Matrix (KFM), including directory conventions, governance constraints, and how analysis outputs connect to catalogs, the graph, APIs, and Story Nodes.

All analytical workflows follow:

- FAIR+CARE governance
- MCP-DL v6.3 reproducibility standards
- KFM-MDP v11.2.6 formatting and metadata
- KFM-OP v11 ontology alignment

<img src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Certified-gold" />
<img src="https://img.shields.io/badge/Status-Active-brightgreen" />

</div>

---

## 📘 Overview

The Analyses layer is where KFM transforms governed datasets into measurable insight and evidence-led interpretation.

KFM analyses commonly cover:

- Hydrology and watershed analysis
- Climatology and anomaly modeling
- Geology, soils, geomorphology, and geophysics
- Ecology and biodiversity intelligence
- Historical–environmental correlation
- Cross-domain synthesis and multimodal reasoning

Every analysis is expected to be:

- versioned (manifests and stable IDs)
- checksum-verifiable (release packet references)
- catalog-linked (STAC/DCAT references to inputs and outputs)
- provenance-complete (PROV-O activities and entities)
- governance-aware (FAIR+CARE labels, sovereignty constraints)

Telemetry is published into:

`../../releases/v11.2.6/focus-telemetry.json`

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/                                — 📘 Root of analysis documentation and domain methods
│
├── 📄 README.md                                 — 📘 This overview file (Analyses index)
│
├── 📁 hydrology/                                — 🌊 Hydrology and streamflow analytics
│   ├── 📄 README.md                             — Domain overview (methods, scope, governance)
│   ├── 📁 datasets/                             — Linked datasets and catalog references
│   ├── 📁 methods/                              — Drought/flood methods, harmonization notes
│   ├── 📁 results/                              — Derived metrics, plots, maps, tables
│   └── 📁 metadata/                             — Provenance notes and analysis run summaries
│
├── 📁 climatology/                              — 🌦 Climate trends and projections
│   ├── 📄 README.md
│   ├── 📁 datasets/
│   ├── 📁 methods/
│   ├── 📁 results/
│   └── 📁 metadata/
│
├── 📁 geology/                                  — 🪨 Geology, soils, geomorphology
│   ├── 📄 README.md
│   ├── 📁 datasets/
│   ├── 📁 methods/
│   ├── 📁 results/
│   └── 📁 metadata/
│
├── 📁 ecology/                                  — 🌱 Biodiversity and ecological modeling
│   ├── 📄 README.md
│   ├── 📁 datasets/
│   ├── 📁 methods/
│   ├── 📁 results/
│   └── 📁 metadata/
│
├── 📁 historical/                               — 🏛 Historical and archival environmental linkage
│   ├── 📄 README.md
│   ├── 📁 datasets/
│   ├── 📁 methods/
│   ├── 📁 results/
│   └── 📁 metadata/
│
├── 📁 cross-domain/                             — 🔗 Integrated multi-domain analytics
│   ├── 📄 README.md
│   ├── 📁 datasets/
│   ├── 📁 methods/
│   ├── 📁 results/
│   └── 📁 metadata/
│
└── 📁 metadata/                                 — 🗄 Global analyses-level metadata, audits, and registries
    ├── 📄 README.md
    └── 📁 audit-reports/
~~~

Layout rules:

- New domains should mirror the folder set: README, datasets, methods, results, metadata.
- Directory trees must use `~~~text` fences.
- Use only approved H2 headings.

## 🧭 Context

The Analyses layer sits downstream of governed acquisition and ETL, and upstream of narrative and user-facing products.

Downstream dependencies (inputs):

- source and ETL pipelines (`data/sources/**`, `src/**`)
- catalogs (`data/stac/**`, DCAT views)
- graph entities for places, events, and datasets (Neo4j)

Upstream consumers (outputs):

- Story Nodes and Focus Mode narratives
- map and dashboard layers (MapLibre/Cesium)
- derived dataset publications (STAC/DCAT)
- governance and sustainability reporting (telemetry)

## 🧱 Architecture

Analyses are treated as deterministic, replayable procedures.

An analysis run should be modelable as:

- a plan (this documentation)
- one or more activities (analysis runs)
- entities used (input datasets, parameters, configs)
- entities generated (derived datasets, reports, figures)

Recommended boundaries:

- code and orchestration live under `src/` and `mcp/` (not here)
- this directory documents methods, assumptions, and validation
- derived data outputs belong under `data/processed/` and are cataloged under `data/stac/`

## 🗺️ Diagrams

### Analytical governance workflow

~~~mermaid
flowchart TD
  A["Raw multidomain data"] --> B["ETL harmonization and STAC/DCAT registration"]
  B --> C["Domain analysis pipelines (docs/analyses/*/methods)"]
  C --> D["Results and visualizations (docs/analyses/*/results)"]
  D --> E["Validation and FAIR+CARE audit"]
  E --> F["Telemetry export (runtime, energy, CO2e, ethics)"]
  F --> G["Governance ledger update (Diamond⁹ Ω / Crown∞Ω)"]
~~~

This flow shows the canonical lifecycle: governed inputs → deterministic methods → validated outputs → telemetry and governance trace.

## 🧠 Story Node & Focus Mode Integration

Analyses feed Story Nodes and Focus Mode in two ways:

- evidence assets (maps, tables, derived datasets) referenced by Story Nodes
- derived indicators and interpretations linked to graph entities (Place, Event, Dataset)

Requirements:

- narrative outputs must be evidence-led and provenance-aware
- facts must be separable from interpretation, and speculation must be labeled as hypothetical
- sensitive locations or restricted cultural knowledge must be generalized or withheld by default

## 🧪 Validation & CI/CD

Analyses documentation and outputs are validated through CI profiles listed in front matter.

Minimum expectations:

- front matter schema validation (`schema-lint`)
- heading and fence constraints (`markdown-lint`)
- diagrams parse (`diagram-check`)
- provenance coherence (`provenance-check`)
- footer includes governance links (`footer-check`)

Sustainability and telemetry targets may be enforced in pipeline CI:

| Metric | Target (v11) | Unit | Source |
|---|---:|---:|---|
| Energy per workflow | ≤ 12 | Wh | `energy_schema` |
| Carbon footprint | ≤ 0.005 | gCO₂e | `carbon_schema` |
| Telemetry completeness | ≥ 98 | % | `telemetry_schema` |
| FAIR+CARE audit pass | 100 | % | Governance + FAIR+CARE checks |

## 📦 Data & Metadata

Analyses should reference their canonical inputs and outputs via STAC/DCAT IDs rather than embedding raw datasets inside `docs/`.

Common data sources referenced by analyses include:

| Source | Description | Typical formats | FAIR+CARE status |
|---|---|---|---|
| NOAA / NCEI | Climate normals and station series | NetCDF, CSV | Certified (expected) |
| Daymet / PRISM | Gridded daily climate | NetCDF, GeoTIFF/COG | Certified (expected) |
| USGS NWIS | Streamflow and hydrology | CSV, JSON | Certified (expected) |
| NASA Earthdata | Remote sensing imagery and derived layers | COG, NetCDF | Certified (expected) |
| NRCS SSURGO | Soil maps and properties | GeoPackage, raster | Certified (expected) |
| GBIF / KU Biodiversity | Species occurrence | CSV, JSON-LD | Certified (expected) |
| Kansas Historical Society | Archival scans and records | TIFF, JSON-LD | Conditional (review) |

Example analysis-run record (documentation-safe):

~~~json
{
  "analysis_id": "kfm:analysis:example:v1",
  "domains": ["Hydrology", "Climatology"],
  "inputs": ["stac:collection:usgs-nwis", "stac:collection:prism"],
  "outputs": ["stac:item:derived:flood-risk-index"],
  "energy_wh": 58.4,
  "carbon_gco2e": 0.021,
  "faircare_compliance": "certified",
  "validation_status": "passed",
  "record_created": "2025-12-14T00:00:00Z"
}
~~~

## 🌐 STAC, DCAT & PROV Alignment

Analyses are represented in catalogs and lineage as follows.

DCAT:

- this document may be treated as a documentation dataset (`dcat:Dataset` or `dcat:CatalogRecord`)
- `semantic_document_id` maps to `dct:identifier`
- Markdown is a `dcat:Distribution` (`mediaType: text/markdown`)

STAC:

- derived layers produced by analyses should be registered as STAC Items
- collections may be organized by domain (hydrology, climate, ecology) or by indicator family

PROV-O:

- each analysis run is a `prov:Activity`
- inputs and outputs are `prov:Entity`
- the method and constraints described here function as a `prov:Plan`

## ⚖ FAIR+CARE & Governance

Analyses must not bypass governance.

Hard constraints:

- do not expose secrets, credentials, or internal endpoints
- respect Indigenous data sovereignty and culturally sensitive information controls
- apply masking/generalization rules for restricted locations by default

Governance references:

- governance: `governance_ref`
- ethics: `ethics_ref`
- sovereignty policy: `sovereignty_policy`

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| **v11.2.6** | 2025-12-14 | Updated to KFM-MDP v11.2.6; corrected Mermaid labels (no HTML); added missing required sections (Architecture, Story Node & Focus Mode Integration); updated release packet references and standardized footer links. |
| v11.2.4 | 2025-12-06 | Upgraded to KFM-MDP v11.2.4; expanded metadata, alignment, sustainability targets, and directory layout. |
| v11.0.0 | 2025-11-24 | Initial v11 analyses overview; introduced telemetry schema v4 and expanded FAIR+CARE matrix. |
| v10.2.2 | 2025-11-10 | Added cross-domain integration section and ISO metrics alignment. |
| v10.2.0 | 2025-11-09 | Linked metadata registry to FAIR+CARE pipelines for analyses. |
| v10.1.0 | 2025-11-08 | Established initial analyses index across hydrology, climatology, ecology, geology, and history. |

---

[⬅ Back to Documentation Index](../README.md) · [📂 Standards Index](../standards/README.md) · [🏛️ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) · [🤝 FAIR+CARE Guide](../standards/faircare/FAIRCARE-GUIDE.md) · [🪶 Indigenous Data Protection](../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)