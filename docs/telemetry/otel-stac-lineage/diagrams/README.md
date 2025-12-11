---
title: "🗺️ Kansas Frontier Matrix — OTel → STAC Lineage: Diagrams (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/otel-stac-lineage/diagrams/README.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.6/otel-stac-lineage-diagrams-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/otel-stac-lineage-diagrams-v11.2.6.json"
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
doc_kind: "Standard Index"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "telemetry-otel-stac-lineage-diagrams"
  applies_to:
    - "docs/telemetry/otel-stac-lineage/diagrams/**"
    - "docs/telemetry/otel-stac-lineage/specs/**"
    - "docs/telemetry/otel-stac-lineage/validators/**"
    - "schemas/telemetry/**"
    - ".github/workflows/telemetry-export.yml"
    - ".github/workflows/docs-lint.yml"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Architecture diagrams; must not embed restricted coordinates or sensitive identifiers"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by OTel → STAC Lineage Diagrams v12"

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
  - "docs/telemetry/otel-stac-lineage/diagrams/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:otel-stac-lineage:diagrams:v11.2.6"
semantic_document_id: "kfm-telemetry-otel-stac-lineage-diagrams-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:otel-stac-lineage:diagrams:v11.2.6"
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
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
transform_registry:
  allowed:
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
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
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"

ci_integration:
  workflow: ".github/workflows/docs-lint.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
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

# 🗺️ **Kansas Frontier Matrix — OTel → STAC Lineage: Diagrams**
`docs/telemetry/otel-stac-lineage/diagrams/README.md`

**Purpose**  
Central index for **render-safe** diagrams that explain how **OpenTelemetry (OTel) lineage signals** map into **STAC / DCAT / PROV** structures in KFM.  
These diagrams are used by workflow docs, telemetry specs, validators, governance dashboards, and Focus Mode summaries.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Telemetry-OTel_STAC_Lineage-informational" />
<img src="https://img.shields.io/badge/Diagrams-Mermaid_v1-success" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

This directory is the **single source of truth** for diagram assets that describe:

- OTel spans and attributes used for ETL lineage evidence.
- How those spans are transformed into:
  - **STAC Items + Assets**,
  - **DCAT Datasets + Distributions**,
  - **PROV Activities + Entities + Agents**.
- How validators and CI gates ensure:
  - determinism,
  - schema conformance,
  - redaction and sovereignty-aware safety.

These diagrams MUST be:

- **Mermaid-renderable** in CI documentation renderers.
- **Readable** (human-first) without sacrificing machine predictability.
- **Safe** (no restricted coordinates, no sensitive identifiers, no secrets).

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 otel-stac-lineage/
        ├── 📄 README.md                         — OTel → STAC lineage telemetry overview (parent index)
        ├── 📁 specs/
        │   └── 📄 README.md                     — Schema/spec registry for OTel lineage events
        ├── 📁 validators/
        │   └── 📄 README.md                     — Validator behavior + CLI contracts
        ├── 📁 storage/
        │   └── 📄 README.md                     — Storage layout for lineage payloads and snapshots
        └── 📁 diagrams/
            ├── 📄 README.md                     — ← This index (diagram rules + pointers)
            ├── 📄 otel_to_stac_flow.mmd          — Mermaid source (flowchart profile)
            ├── 📄 otel_lineage_timeline.mmd      — Mermaid source (timeline profile)
            └── 📁 exports/
                ├── 📄 otel_to_stac_flow.svg     — Rendered export for docs/web (optional)
                └── 📄 otel_lineage_timeline.svg — Rendered export for docs/web (optional)
~~~

Notes:

- `.mmd` files are treated as **diagram sources**.
- `exports/` is optional, but if present it SHOULD contain **rendered SVG** for stable embedding.
- If your repo prefers `.md` with embedded `~~~mermaid` blocks, keep sources here and link them from specs/docs.

---

## 🧭 Context

### 1. Why “diagram safety” is a governed requirement

We have to satisfy two constraints simultaneously:

- **Renderer robustness:** documentation renderers are strict; certain characters and HTML tags can break Mermaid parsing.
- **Governance safety:** lineage can include identifiers, paths, and sometimes hints of sensitive locations; diagrams must not leak restricted info.

This folder exists to enforce stable practices so diagram updates do not break docs-lint, schema-lint, or governance audits.

### 2. What diagrams should and should not include

Diagrams SHOULD:

- show relationships between components (spans → mapping → catalogs/graph),
- highlight key invariants (stable IDs, schema versions, redaction boundary),
- reference artifacts by **class** (e.g., “STAC Item”) rather than by sensitive instance IDs.

Diagrams MUST NOT:

- embed secrets, tokens, or credentials,
- embed restricted coordinates or “sensitive site” identifiers,
- embed real internal URLs that are not safe to publish.

---

## 🗺️ Diagrams

### 1. Reference flow diagram (render-safe example)

This is an example of the preferred Mermaid style for this directory:

- keep labels ASCII-friendly,
- wrap labels in quotes,
- avoid HTML (no `<br/>`),
- avoid wildcards and leading dots inside labels.

~~~mermaid
flowchart LR
  A["OpenTelemetry spans"] --> B["Lineage mapping and normalization"]
  B --> C["STAC Item and Assets"]
  B --> D["DCAT Dataset and Distributions"]
  B --> E["PROV Activity and Entities"]
  C --> F["Catalog and Graph"]
  D --> F
  E --> F
~~~

### 2. Diagram authoring rules (normative)

All Mermaid diagrams in this directory MUST:

- use only allowed diagram profiles:
  - `flowchart LR` (or `flowchart TD`)
  - `timeline`
- use `~~~mermaid` fences (tilde fences) in Markdown documents that embed diagrams
- prefer quoted labels: `X["label text"]`
- avoid:
  - HTML tags inside labels (e.g., `<br/>`)
  - wildcards in labels (e.g., `*.yml`, `.github/workflows/*`)
  - complex punctuation in labels where possible (`()`, `/`, `·`, `*`)
- keep node IDs simple and stable: `A`, `B`, `MAP`, `STAC`, `PROV`

If a diagram fails to render:

- simplify labels to ASCII and quote them,
- remove punctuation and try again,
- validate the file locally (see **🧪 Validation & CI/CD**).

---

## 🧠 Story Node & Focus Mode Integration

Diagrams are consumed by narrative layers as **supporting evidence**:

- `urn:kfm:story-node:telemetry:otel-stac-lineage:<run_id>` may link to:
  - a flow diagram showing mapping logic,
  - a timeline showing run lifecycle and export steps.

Focus Mode MAY:

- embed or link to diagram exports (SVG) for explainability,
- summarize what a diagram indicates.

Focus Mode MUST NOT:

- treat diagrams as authoritative evidence of run results,
- infer real-world coordinates or sensitive metadata from diagram structure.

---

## 🧪 Validation & CI/CD

### 1. CI enforcement

The following checks SHOULD cover this directory:

- `docs-lint.yml`:
  - ensures Mermaid blocks parse (when embedded in Markdown),
  - ensures only allowed diagram profiles are used,
  - ensures directory layout fences and approved H2 headings are respected.

If `.mmd` sources are used:

- a diagram-check step SHOULD validate `.mmd` files (either by rendering or by syntax validation).

### 2. Local validation (recommended)

If you render diagrams locally:

- generate SVG exports into `exports/` for stable embedding
- keep exports deterministic (same source → same SVG, ignoring timestamps)

Example command pattern (tooling may vary per repo):

~~~bash
# Example pattern: render Mermaid source to SVG (adjust to your local tooling)
# mmdc -i docs/telemetry/otel-stac-lineage/diagrams/otel_to_stac_flow.mmd \
#      -o docs/telemetry/otel-stac-lineage/diagrams/exports/otel_to_stac_flow.svg
~~~

---

## 📦 Data & Metadata

### 1. Inputs

- Mermaid sources (`*.mmd`) and/or Markdown docs embedding `~~~mermaid` blocks.
- Diagram registry information (file names, intent, version history).

### 2. Outputs

- Optional rendered exports (`exports/*.svg`) for stable embedding.
- Telemetry (optional) summarizing:
  - diagrams changed,
  - render validation pass/fail,
  - export generation status.

---

## 🌐 STAC, DCAT & PROV Alignment

- **DCAT**
  - Diagram sources and exports can be cataloged as `dcat:Distribution` assets of the OTel lineage documentation dataset.
- **STAC**
  - Diagrams are non-spatial documentation assets; if included in STAC:
    - `geometry: null`
    - `assets` include SVG/Markdown.
- **PROV-O**
  - Diagram generation (rendering) can be modeled as a `prov:Activity` that:
    - `prov:used` a `.mmd` source
    - `prov:generated` an `.svg` export

---

## 🧱 Architecture

This folder is intentionally small and strict:

- `diagrams/` holds the **diagram contract and sources**
- `specs/` defines event schemas and mapping specifications
- `validators/` enforces shape rules and redaction boundaries
- `storage/` defines where lineage payloads and snapshots live

Diagrams SHOULD reflect the specs and validators, not replace them.

---

## ⚖ FAIR+CARE & Governance

Diagrams MUST respect:

- FAIR: stable naming, findable locations, version history, reproducibility of exports.
- CARE: no leakage of sensitive identifiers, and sovereignty-aware handling of culturally sensitive information.

Governance expectations:

- diagram updates that change mapping meaning SHOULD be accompanied by:
  - corresponding updates in `specs/` and/or `validators/`,
  - a version history entry,
  - (when applicable) a governance note in the parent README.

---

## 🕰️ Version History

| Version | Date       | Author        | Summary                                                                 |
|--------:|------------|---------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-11 | `@kfm-docs`   | Built from scratch: establishes render-safe Mermaid rules and diagram layout for OTel → STAC lineage docs. |
| v11.2.4 | 2025-12-06 | `@kfm-docs`   | Prior baseline guidance (superseded by v11.2.6 rewrite).                |

---

<div align="center">

🗺️ **KFM — OTel → STAC Lineage: Diagrams (v11.2.6)**  
Render-Safe Mermaid · Governance-Ready Architecture · Focus Mode Friendly

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ OTel STAC Lineage Telemetry](../README.md) ·
[⬅ Telemetry Home](../../README.md) ·
[🧾 Specs](../specs/README.md) ·
[🧪 Validators](../validators/README.md) ·
[📦 Storage](../storage/README.md) ·
[⚙ Workflows Index](../../../workflows/README.md) ·
[⚙ Telemetry Export Workflow](../../../workflows/telemetry-export.yml.md) ·
[📘 Docs Root](../../../README.md) ·
[📘 Markdown Protocol](../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[📚 Glossary](../../../glossary.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>