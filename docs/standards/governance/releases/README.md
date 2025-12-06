---
title: "🏛️ Kansas Frontier Matrix — Governance Release Records Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/governance/releases/README.md"
version: "v10.2.3"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Per-Release + Annual Index Review"
content_stability: "stable"
commit_sha: "<latest-commit-hash>"

signature_ref: "releases/v10.2.3/signature.sig"
attestation_ref: "releases/v10.2.3/slsa-attestation.json"
sbom_ref: "releases/v10.2.0/sbom.spdx.json"
manifest_ref: "releases/v10.2.0/manifest.zip"
telemetry_ref: "releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-governance-releases-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "../ROOT-GOVERNANCE.md"
ethics_ref: "../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "governance"
  applies_to:
    - "governance-releases"
    - "all-kfm"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Supersedes prior Governance Release Records Index versions ≤ v10.2.2"

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
  - "docs/standards/governance/releases/README.md@v10.2.3"  # origin root version

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-governance-releases-index-v10.2.3.schema.json"
shape_schema_ref: "schemas/shacl/kfm-governance-releases-index-v10.2.3-shape.ttl"

story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:standards:governance:releases-index:v10.2.3"
semantic_document_id: "kfm-governance-releases-index-v10.2.3"
event_source_id: "ledger:kfm:doc:standards:governance:releases-index:v10.2.3"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
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
    - timeline-generation
    - semantic-highlighting
    - 3d-context-render
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
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
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
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"

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
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🏛️ **Kansas Frontier Matrix — Governance Release Records Index**  
`docs/standards/governance/releases/README.md`

**Purpose:**  
Define and index the canonical, per-release governance record packages for the Kansas Frontier Matrix (KFM).  
This document describes how governance artifacts (ledgers, audits, FAIR+CARE reports, AI governance summaries) are organized by release and linked back to the **Root Governance Charter** and **Governance & Ethical Oversight Framework**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../faircare.md)
[![Status: Active](https://img.shields.io/badge/Status-Releases%20Indexed-success)]()

</div>

---

## 📘 Overview

This index defines how **governance release records** are structured within:

`docs/standards/governance/releases/`

Each KFM release (e.g., `v10.2.0`, `v10.2.3`) has a **governance packet** that captures:

- Governance decisions and ledger extracts relevant to the release.  
- FAIR+CARE and contract validation summaries.  
- AI governance results (bias, drift, explainability).  
- Public-facing narratives about governance state and changes.

This index:

- Provides the **canonical directory structure** for governance release records.  
- Establishes **naming conventions** and documentation expectations for each release folder.  
- Connects per-release packages to:
  - The root charter (`ROOT-GOVERNANCE.md`), and  
  - The governance framework index (`docs/standards/governance/README.md`).  

It is **normative**: deviations from this structure must be explicitly justified in governance decisions and tracked via the governance ledger.

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/governance/
├── 📄 README.md                     # Governance & Ethical Oversight Framework (index)
├── 📄 ROOT-GOVERNANCE.md            # Root Governance Charter (authoritative)
└── 📂 releases/                     # Per-release governance record packages (this directory)
    ├── 📄 README.md                 # Governance Release Records Index (this document)
    ├── 📂 v10.2.0/                  # Governance packet for release v10.2.0
    │   ├── 📄 governance_summary.md # Human-readable governance overview for the release
    │   ├── 📄 faircare_report.md    # Narrative FAIR+CARE summary derived from validation reports
    │   ├── 📄 ai_governance_report.md
    │   └── 📄 changelog_governance.md
    └── 📂 v10.2.3/                  # Governance packet for release v10.2.3 (pattern repeats)
        ├── 📄 governance_summary.md
        ├── 📄 faircare_report.md
        ├── 📄 ai_governance_report.md
        └── 📄 changelog_governance.md
~~~

**Author rules:**

- Each release **MUST** have a dedicated folder named exactly after the release tag (e.g., `v10.2.0/`).  
- Each release folder **SHOULD** contain, at minimum:
  - `governance_summary.md` — high-level narrative of governance state.  
  - `faircare_report.md` — curated FAIR+CARE narrative keyed to reports in `reports/fair/`.  
  - `ai_governance_report.md` — explanation of AI governance and model-specific decisions.  
  - `changelog_governance.md` — governance-focused changelog describing policy-relevant changes.  
- Each Markdown file inside a release folder **MUST** itself be KFM-MDP-compliant, with its own front-matter and version history.

---

## 🧭 Context

### Relationship to Root Charter and Governance Index

This index operates under:

- **Root Governance Charter:** `docs/standards/governance/ROOT-GOVERNANCE.md`  
- **Governance & Ethical Oversight Framework:** `docs/standards/governance/README.md`

The charter defines **who** decides and **how** decisions are made.  
The framework index explains **governance systems and metrics**.  
This release index defines **where those decisions and metrics are recorded per release**.

### Scope of Governance Release Records

Each governance packet:

- Covers a **specific versioned release** (software + datasets + documentation).  
- Captures governance state **as of that release’s cut date**.  
- Must be immutable after release, except for:
  - Errata (documented in governance ledger and release manifests).  
  - Legally required corrections (also documented and traceable).

---

## 🧠 Story Node & Focus Mode Integration

Governance release packets are designed to be **Story Node-friendly** and **Focus Mode-aware**.

### Release-Focused Story Nodes

Typical Story Nodes targeting this directory:

~~~text
{
  "target": "kfm-governance-releases-index-v10.2.3",
  "scope": {
    "kind": "release",
    "id": "v10.2.0"
  },
  "references": [
    "docs/standards/governance/releases/v10.2.0/governance_summary.md",
    "docs/standards/governance/releases/v10.2.0/faircare_report.md",
    "reports/audit/governance-ledger.json"
  ]
}
~~~

These nodes enable Focus Mode to overlay:

- Release-specific governance summaries.  
- Key FAIR+CARE decisions.  
- Any special conditions or restrictions tied to that release.

### Focus Mode Behavior

When a user focuses on a release (e.g., `v10.2.0`) in the UI:

- **MAY:**
  - Surface summaries from `governance_summary.md` and `faircare_report.md`.  
  - Highlight high-impact governance changes (e.g., new CARE restrictions).  
  - Show links to the relevant ledger slices and audit reports.
- **MUST NOT:**
  - Invent governance decisions or imply non-existent approvals.  
  - Rewrite or override the normative content of the release packet.

---

## 🧪 Validation & CI/CD

Per-release governance records participate in CI/CD gating.

### Release Governance Flow

~~~mermaid
flowchart LR
  A["Release Candidate Tagged (e.g., v10.2.0-rc)"]
    --> B["FAIR+CARE & Contract Validation Pipelines"]
  B --> C{"Governance Issues?"}
  C -->|No| D["Finalize Governance Packet → v10.2.0/"]
  C -->|Yes| E["Council Review & Decisions"]
  E --> F["Ledger & Telemetry Updates"]
  F --> D
  D --> G["Release Manifest & STAC/DCAT Update"]
~~~

### Required Checks Before Release

For each release:

- Governance packet presence:
  - `docs/standards/governance/releases/<version>/` exists.  
  - Required Markdown files exist and pass `markdown-lint`, `schema-lint`, `footer-check`.  
- Linkage checks:
  - Each document references the correct release tag and manifest.  
  - References to reports under `reports/audit/` and `reports/fair/` resolve.
- Provenance checks:
  - Governance packet is referenced from:
    - `reports/audit/release-manifest-log.json`  
    - STAC/DCAT entries for the release.

Failures in these checks **block promotion** of the release from staging to production.

---

## 📦 Data & Metadata

### Crosswalk: Governance Release Records ↔ Data Artifacts

| Governance Doc (per release) | Primary Audience | Backing Data Artifacts |
|---|---|---|
| `governance_summary.md` | General KFM users, governance observers | `reports/audit/governance-ledger.json`, `reports/audit/release-manifest-log.json` |
| `faircare_report.md` | FAIR+CARE Council, data stewards | `reports/fair/faircare_summary.json` |
| `ai_governance_report.md` | AI Governance Subcommittee, AI users | `reports/audit/ai_models.json`, model evaluation artifacts |
| `changelog_governance.md` | Developers, governance historians | Git history, PRs, governance ledger entries, manifests |

**Author guidance:**

- Markdown narratives must **summarize** and **interpret** the underlying JSON records, not contradict them.  
- Each narrative must clearly indicate:
  - The release tag it refers to.  
  - The data artifacts and ledger ranges it summarizes.  

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT View

For each release:

- A `dcat:Dataset` or `dcat:CatalogRecord` for the release may include:
  - Links to its governance packet directory as `dcat:Distribution` entries:
    - `accessURL` → rendered HTML or Markdown views.  
    - `downloadURL` → raw `.md` and JSON reports.

### STAC View

In a `kfm-releases` STAC Collection:

- Each release Item:
  - `id` = release tag (e.g., `v10.2.0`).  
  - `properties.datetime` = release cut timestamp.  
  - Governance assets:
    - `assets.governance-summary` → link to `governance_summary.md`.  
    - `assets.governance-faircare` → link to `faircare_report.md` and FAIR+CARE JSON.  
    - `assets.governance-ai` → link to `ai_governance_report.md` and AI metrics.

### PROV View

- Each release governance packet is an aggregate `prov:Entity`:
  - `prov:wasGeneratedBy` a release governance activity (e.g., `ex:release_v10_2_0_governance`).
- Activities:
  - Use:
    - FAIR+CARE validation entities,  
    - Ledger entities,  
    - Manifest entities, and  
    - Root charter + governance framework entities.
- Agents:
  - FAIR+CARE Council, AI Governance Subcommittee, Technical Standards Committee.

---

## 🧱 Architecture

From the architecture pipeline:

1. **Deterministic ETL / Validation**
   - Data and model pipelines emit FAIR+CARE and governance metrics into `reports/` and `releases/*`.  
   - Governance release packets **must** reflect those metrics, not override them.

2. **Knowledge Graph**
   - Release nodes (`:Release {tag: "v10.2.0"}`) connect to:
     - Governance packet docs (`:Document` nodes).  
     - Governance decisions (`:Decision` nodes drawn from ledger).  
     - Policies (`:Policy` nodes for charter and related standards).

3. **API**
   - Versioned governance endpoints expose:
     - Current governance view for a release.  
     - Historical comparisons across multiple releases.

4. **Web / Focus Mode**
   - Release views surface:
     - Governance badges (e.g., “FAIR+CARE: ✓”, “AI Governance: ✓ / ⚠”).  
     - Links to per-release governance docs in this directory.  
     - Timeline visualizations of governance changes between releases.

---

## ⚖ FAIR+CARE & Governance

This index enforces FAIR+CARE in a **release-aware** way:

- **Findable:**  
  - Standardized directory and file naming patterns.  
  - Indexed in catalogs and the graph by release tag.

- **Accessible:**  
  - Public, CC-BY 4.0-licensed governance narratives.  
  - JSON reports exposed for programmatic use where appropriate.

- **Interoperable:**  
  - DCAT, STAC, and PROV-compatible records.  
  - Shared identifier schemes across manifests, ledger entries, and governance docs.

- **Reusable:**  
  - Per-release histories allow longitudinal governance analysis.  
  - Explicit mapping of decisions to policies and datasets.

CARE considerations:

- Release packets must clearly flag:
  - Any datasets subject to special Indigenous or community constraints.  
  - The CARE reasoning behind restrictions or conditions.  
- Sensitive detail may be generalized or omitted, but **never falsified**; omissions should be explicitly noted (e.g., “location details omitted for cultural sensitivity”).

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| **v10.2.3** | 2025-12-06 | A. Barta | Created canonical Governance Release Records Index; aligned with KFM-MDP v11.2.4 and governance charter/framework; defined directory layout, per-release doc expectations, and STAC/DCAT/PROV alignment. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Governed under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Governance Index](../README.md) · [Root Governance Charter](../ROOT-GOVERNANCE.md) · [Standards Index](../../README.md)

</div>

