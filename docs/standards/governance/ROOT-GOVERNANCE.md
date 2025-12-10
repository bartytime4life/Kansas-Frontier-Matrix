---
title: "🏛️ Kansas Frontier Matrix — Root Governance Charter (FAIR+CARE Council) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/governance/ROOT-GOVERNANCE.md"
version: "v11.2.6"
last_updated: "2025-12-10"
release_stage: "Stable / Authoritative"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual / Formal Council Review"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"

signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/docs-root-governance-v2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Authoritative"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "governance"
  applies_to:
    - "all-governance"
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
sunset_policy: "Supersedes prior Root Governance Charter versions ≤ v10.2.3"

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
  - "docs/standards/governance/ROOT-GOVERNANCE.md@v10.2.3"
  - "docs/standards/governance/ROOT-GOVERNANCE.md@v10.2.2"
  - "docs/standards/governance/ROOT-GOVERNANCE.md@v9.7.0"
  - "docs/standards/governance/ROOT-GOVERNANCE.md@v9.5.0"
  - "docs/standards/governance/ROOT-GOVERNANCE.md@v9.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

json_schema_ref: "../../../schemas/json/kfm-root-governance-v11.2.6.schema.json"
shape_schema_ref: "../../../schemas/shacl/kfm-root-governance-v11.2.6-shape.ttl"

story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:standards:governance:root-charter:v11.2.6"
semantic_document_id: "kfm-root-governance-charter-v11.2.6"
event_source_id: "ledger:kfm:doc:standards:governance:root-charter:v11.2.6"
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
  - "layout-normalization"
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
    - layout-normalization
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

fencing_profile: "outer-backticks-inner-tildes-v1"

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

# 🏛️ **Kansas Frontier Matrix — Root Governance Charter**  
`docs/standards/governance/ROOT-GOVERNANCE.md`

**Purpose:**  
Establish the foundational ethical, procedural, technical, and operational governance charter of the Kansas Frontier Matrix (KFM).  
Defines the **FAIR+CARE Council**, its authority, duties, decision-making processes, and alignment with **Master Coder Protocol (MCP v6.3)**, **KFM-MDP v11.2.6**, and international open-data governance standards.

This charter is the governance spine for the canonical KFM pipeline:  
**Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode.**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../faircare/FAIRCARE-GUIDE.md)
[![Status: Authoritative](https://img.shields.io/badge/Status-Authoritative-blue)]()

</div>

---

## 📘 Overview

This **Root Governance Charter** defines how decisions, validations, and ethical reviews are executed within the Kansas Frontier Matrix (KFM).  
It ensures that all project activities — from data ingestion to AI model deployment — uphold **FAIR (Findable, Accessible, Interoperable, Reusable)** and **CARE (Collective Benefit, Authority to Control, Responsibility, Ethics)** principles.

This charter:

- Represents the **highest level of organizational and ethical oversight** for the KFM initiative.  
- Supersedes all subordinate governance documents and policies when conflicts arise.  
- Serves as the authoritative reference for councils, committees, and automation workflows implementing governance.  
- Binds all stages of the KFM pipeline to transparent, reproducible, PROV-aligned decision making.

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/governance/
├── 📄 README.md           # Governance & Ethical Oversight Framework (index)
└── 📄 ROOT-GOVERNANCE.md  # Root Governance Charter (this document; authoritative)
~~~

**Author rules:**

- This directory structure is minimal and canonical; additional governance standards must:
  - Live alongside these files with KFM-MDP-compliant front-matter and structure.
  - Reference this charter as their `governance_ref` root where applicable.
  - Be discoverable from `docs/standards/governance/README.md`.

---

## 🧭 Context

### Governance Purpose & Scope

**Objectives**

1. Maintain **ethical integrity** in data and AI governance.  
2. Ensure **technical compliance** with international data standards (FAIR, STAC, DCAT, ISO 19115).  
3. Protect **Indigenous sovereignty**, community rights, and cultural knowledge.  
4. Guarantee **reproducibility and open access** for all published outputs.  
5. Foster **sustainability and accountability** in project stewardship (aligned with ISO 50001 / 14064).  
6. Ensure that all stages of the KFM pipeline expose **machine-readable provenance (PROV-O)** and **geospatial semantics (GeoSPARQL)**.

**Scope**

- Applies to all datasets, documentation, workflows, and software within KFM.  
- Enforced across all branches of development, CI/CD pipelines, and public releases.  
- Reviewed **annually** by the FAIR+CARE Council and published publicly.

### Organizational Structure (FAIR+CARE Council)

The **FAIR+CARE Council** is the primary governing body responsible for interpreting and enforcing this charter.

| Role | Responsibilities | Appointment |
|---|---|---|
| **Council Chair** | Oversees governance policy and ethics review; convenes Council meetings. | Elected annually by council vote. |
| **Technical Standards Lead** | Ensures alignment with MCP, FAIR, STAC/DCAT/PROV, KFM-OP, and schema standards. | Appointed by Council. |
| **Indigenous Data Steward** | Protects cultural heritage and CARE compliance; advocates for Indigenous data sovereignty. | Appointed by partner organizations or tribal entities. |
| **Open Science Director** | Promotes transparency, licensing, accessibility, and reproducibility. | Appointed by the Open Science Board. |
| **AI Ethics Lead** | Oversees AI model governance, explainability, robustness, and fairness. | Appointed by Council. |
| **Accessibility Auditor** | Validates UI and docs compliance with WCAG 2.1 AA+. | Appointed by Council. |
| **Community Liaison** | Represents stakeholder input and public/community engagement. | Nominated by regional partners. |

**Quorum Requirement**

- A minimum of **5 members**, including **at least 1 Indigenous representative**, must be present for any binding vote.

### Termination or Transfer of Authority

If the FAIR+CARE Council ceases to operate:

1. This **Root Governance Charter** remains in effect until superseded.  
2. Authority temporarily transfers to the **Open Science Board**, which must:
   - Maintain the Governance Ledger.  
   - Convene a reconstitution process for the Council.  
3. All existing records and ledgers remain permanently accessible.  
4. The transfer of authority is recorded in `reports/audit/governance-ledger.json`.

---

## 🗺️ Diagrams

This charter is the normative source for governance-related diagrams used across KFM.

**Diagram rules**

- Diagrams in this document and dependent standards **must** use one of the declared `diagram_profiles`:
  - `"mermaid-flowchart-v1"` for governance flows and decision chains.
- All diagrams **must**:
  - Include descriptive text in the surrounding section so that meaning is preserved without rendering.  
  - Avoid depicting sensitive locations (e.g., precise coordinates of restricted Indigenous or archaeological sites).  
  - Reflect the canonical KFM pipeline when describing technical governance flows:

    > Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

- Governance diagrams **must not**:
  - Contradict or override the decisions recorded in the Governance Ledger.  
  - Introduce speculative data flows or AI capabilities not present in the current KFM architecture.

**CI expectations**

- `diagram-check` validates:
  - Mermaid syntax and rendering.  
  - Conformance to approved `diagram_profiles`.  
  - Presence of alt-text style narrative in the adjacent prose.

---

## 🧠 Story Node & Focus Mode Integration

This charter is a primary reference for governance-related **Story Nodes** and **Focus Mode** overlays.

### Focus Mode Behavior

When Focus Mode is scoped to governance (e.g., for a dataset, model, or document):

- **MAY:**
  - Summarize relevant charter sections (e.g., decision-making rules, ethical principles).  
  - Highlight which governance bodies and procedures apply to the focused asset.  
  - Link to recent ledger entries, audits, or policy references tied to that asset.
- **MUST NOT:**
  - Invent or alter governance rules, roles, or decisions.  
  - Dilute or hide FAIR+CARE or Indigenous sovereignty constraints.  
  - Suggest policy exceptions that are not explicitly recorded in the governance ledger.

These rules are enforced through `ai_transform_permissions` and `ai_transform_prohibited` and validated in CI.

### Story Node Patterns

Governance Story Nodes typically:

- Target this charter or its subsections:

  ~~~text
  "target": "kfm-root-governance-charter-v11.2.6"
  ~~~

- Reference concrete artifacts:

  ~~~text
  "references": [
    "reports/audit/governance-ledger.json",
    "docs/reports/telemetry/governance_scorecard.json"
  ]
  ~~~

- Include a **scope** (dataset, model, collection, or release) so Focus Mode can show “governance status” contextually.
- Distinguish:
  - **Facts** — direct quotes or summaries from this charter or ledgers.  
  - **Interpretation** — council or steward analysis of those facts.  
  - **Speculation** — hypotheses or future-scenario discussion, which must be explicitly tagged as speculative.

Story Node metadata must capture relevant identifiers (dataset IDs, release tags, council decision IDs) so the graph layer can connect narrative overlays to PROV entities and activities.

---

## 🧪 Validation & CI/CD

Governance is integrated into CI/CD so charter rules are enforced deterministically.

### Governance Documentation Chain

~~~mermaid
flowchart TD
  A["Dataset or Model Submitted"] --> B["Deterministic ETL Validation (Contracts & Schemas)"]
  B --> C["FAIR+CARE Validation (CI/CD)"]
  C --> D{"CARE / Ethics Triggered?"}
  D -->|No| E["Auto-Approve → STAC/DCAT/PROV Catalog & Telemetry"]
  D -->|Yes| F["Council Review & Deliberation"]
  F --> G["Decision Recorded in Governance Ledger"]
  G --> H["Graph Ingestion (Neo4j, PROV, GeoSPARQL)"]
  H --> I["API & UI Exposure (React/MapLibre/Cesium)"]
  I --> J["Story Nodes & Focus Mode Overlays"]
  E --> H
~~~

This diagram is the canonical mapping of governance actions into the KFM pipeline.

| Governance Record | Description | File Location |
|---|---|---|
| **Governance Ledger** | Immutable log of all council decisions. | `reports/audit/governance-ledger.json` |
| **AI Models Ledger** | Record of approved and audited AI/ML models. | `reports/audit/ai_models.json` |
| **Experiment Ledger** | Validated research and reproducibility reports. | `reports/audit/experiments-ledger.json` |
| **Release Manifest Log** | Checksums and provenance of each release. | `reports/audit/release-manifest-log.json` |

### Governance Automation Integration

Governance actions are tightly coupled with CI/CD workflows and telemetry.

| Workflow | Purpose | Output |
|---|---|---|
| `faircare-validate.yml` | Automated FAIR+CARE & contract compliance check. | `reports/fair/faircare_summary.json` |
| `docs-lint.yml` | Validates governance docs structure + metadata. | `reports/self-validation/docs/lint_summary.json` |
| `stac-validate.yml` | Ensures catalogs reference correct governance metadata. | `reports/self-validation/stac_validation.json` |
| `telemetry-export.yml` | Synchronizes governance metrics to dashboards. | `releases/v11.2.6/focus-telemetry.json` |
| `build-and-deploy.yml` | Publishes updated governance docs with each release. | `releases/v*/manifest.zip` |

### Governance Review Cycle

| Review Type | Frequency | Output | Location |
|---|---|---|---|
| **FAIR+CARE Audit** | Quarterly | `faircare_summary.json` | `reports/fair/` |
| **Ethical Review** | Continuous | `governance-ledger.json` | `reports/audit/` |
| **AI Governance Review** | Biannual or post-major model release | `ai_models.json` | `reports/audit/` |
| **Public Governance Summary** | Annual | `governance_scorecard.json` | `docs/reports/telemetry/` |

All reviews must be reproducible, scriptable, and linked into PROV graphs as activities.

---

## 📦 Data & Metadata

### Governance Data Assets

Core governance data assets governed by this charter include:

- `reports/audit/governance-ledger.json` – canonical decision log.  
- `reports/audit/ai_models.json` – AI governance evaluations and approvals.  
- `reports/audit/experiments-ledger.json` – experiment governance and reproducibility records.  
- `reports/audit/release-manifest-log.json` – release-level checksums and provenance.  
- `reports/fair/faircare_summary.json` – FAIR+CARE validation summaries.  
- `docs/reports/telemetry/governance_scorecard.json` – aggregated governance metrics.  
- `releases/v*/focus-telemetry.json` – per-release telemetry, including security and governance signals.

All assets must include:

- Stable identifiers and timestamps.  
- Explicit linkage to the decisions and policies that governed them.  
- Checksums and provenance entries in release manifests.  
- References to relevant STAC Collections, DCAT Datasets, and PROV Activities/Entities.

### Governance Ledger Example

~~~json
{
  "event": "ethical_review",
  "dataset_id": "ks_treaties_1854",
  "decision": "approved",
  "reviewer": "FAIR+CARE Council",
  "notes": "Dataset reviewed and cleared for Indigenous data sensitivity with agreed contextual notes.",
  "timestamp": "2025-11-12T18:45:00Z",
  "telemetry_ref": "releases/v11.2.6/focus-telemetry.json"
}
~~~

This example is illustrative; actual entries must follow the current governance ledger schema and may include additional fields (e.g., issue references, policy citations, reviewer IDs, AI model IDs, or graph node URIs).

---

## 🌐 STAC, DCAT & PROV Alignment

This charter and the artifacts it governs integrate with KFM’s cataloging and provenance standards.

### DCAT & Documentation

- This charter is modeled as a `dcat:Dataset` (and `dcat:Resource`) in the KFM standards catalog.  
- Key properties:
  - `dct:title` → document `title`.  
  - `dct:description` → Purpose and Overview.  
  - `dct:license` → `CC-BY 4.0`.  
  - `dct:modified` → `last_updated`.  
  - `dct:identifier` → `doc_uuid` / `semantic_document_id`.  
  - `dcat:distribution` → canonical URLs for the markdown, rendered HTML/PDF, and release artifacts.

### STAC & Governance Collections

- Governance data assets (ledgers, scorecards, manifests) are grouped in a `kfm-governance` STAC Collection.  
- Example:
  - `id` = `kfm-governance-ledger`.  
  - `properties.datetime` = last decision timestamp.  
  - Assets:
    - `governance-ledger-json` → `reports/audit/governance-ledger.json`  
    - `ai-models-ledger-json` → `reports/audit/ai_models.json`  
    - `telemetry-governance-scorecard` → `docs/reports/telemetry/governance_scorecard.json`

### PROV-O & Lineage

- This charter is modeled as a `prov:Plan`.  
- Each governance decision:
  - Is a `prov:Activity` referencing:
    - Entities: datasets/models/docs under review, validation reports, ledger entries.  
    - Agents: FAIR+CARE Council, specific reviewers, committees, or automated agents.  
- Amendments to this charter:
  - Are new `prov:Entity` versions with `prov:wasDerivedFrom` relations to prior versions.  
  - Are linked to CI pipeline runs, PRs, and release manifests via `prov:used` and `prov:wasGeneratedBy`.

This alignment enables full, machine-readable lineage from any governed asset back to the charter clauses that applied at decision time and the CI runs that enforced them.

---

## 🧱 Architecture

From an architectural perspective, this charter shapes all layers of KFM and must be reflected consistently in:

1. **Canonical Pipeline**

   All governance-aware systems must model and expose the pipeline as:

   > Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

   - ETL pipelines write validated assets into STAC/DCAT/PROV catalogs.  
   - Catalogs are ingested into the Neo4j knowledge graph with GeoSPARQL geometries and PROV lineage.  
   - APIs query the graph; frontends call APIs only.  
   - Story Nodes and Focus Mode consume API/graph output, never raw data files.

2. **Pipelines (ETL / Validation)**  
   - FAIR+CARE and contract checks are deterministic pipeline steps.  
   - Governance gates (schema validation, CARE triggers, license checks) run before data reaches production catalogs.  
   - Failing governance gates halt promotion to production and create remediation tasks.

3. **Knowledge Graph (Neo4j)**  
   - Councils, roles, policies, decisions, audits, datasets, and models are modeled as nodes and relationships.  
   - Queries like “datasets rejected on CARE grounds last year” or “policies active during a given release” must be answerable from the graph.  
   - Graph schema aligns with CIDOC-CRM, PROV-O, GeoSPARQL, and OWL-Time.

4. **API Layer**  
   - Governance status for a given dataset/model is accessible via APIs.  
   - Clients (web UI, external tools) can fetch current and historical decisions, along with policy references and ledger entries.  
   - APIs must never bypass graph/governance checks when serving data to Focus Mode or external consumers.

5. **Web / Focus Mode**  
   - UI renders governance badges, decision summaries, and policy links contextually.  
   - Focus Mode uses this charter as the root reference for explaining why a dataset/model is gated, restricted, or approved with conditions.  
   - Governance overlays must be traceable back to specific ledger events and PROV activities.

Any new governance-relevant feature or dataset must define:

- Its governance entities (policies, procedures, roles).  
- How those entities are surfaced in graph, API, and UI.  
- Which sections of this charter apply.  
- How violations are detected in CI and recorded in the governance ledger.

---

## ⚖ FAIR+CARE & Governance

### Ethical Data Handling Principles

1. **Transparency** — All governance decisions and audits are logged with reasons, timestamps, and responsible parties.  
2. **Consent** — No data or cultural information is published without explicit permission or legal basis from data owners or communities.  
3. **Reciprocity** — Data must generate shared benefit for contributing communities (education, access, decision-support).  
4. **Accountability** — Governance actions are traceable; Council members are accountable to the charter and public.  
5. **Respect** — Data from Indigenous or vulnerable communities receives additional CARE review and may be restricted.  
6. **Minimization** — Public-facing views avoid unnecessary exposure of sensitive attributes, precise locations, or personal information.

These principles must be reflected in:

- Data contracts and CARE fields.  
- Council decisions and ledger entries.  
- Telemetry, dashboards, and public summaries.  
- Story Nodes and Focus Mode narratives.

### Governance Responsibilities

| Domain | Responsibility | Deliverable |
|---|---|---|
| **Data Governance** | Ensure all datasets comply with FAIR+CARE and open license policies. | Quarterly FAIR+CARE Audit Report |
| **Ethical Review** | Review cultural, Indigenous, and sensitive data submissions. | CARE Compliance Statement |
| **AI Governance** | Audit ML models for transparency, robustness, bias, and responsible use. | AI Model Audit Report |
| **Technical Validation** | Maintain continuous validation pipelines (STAC/DCAT, contracts, schemas). | STAC/DCAT Validation Report |
| **Public Communication** | Publish audit results, decisions, and governance changes. | Governance Transparency Bulletin |

Deliverables are stored under:

~~~text
📂 reports/
└── 📂 audit/
    ├── 📄 governance-ledger.json
    ├── 📄 ai_models.json
    ├── 📄 experiments-ledger.json
    └── 📄 release-manifest-log.json
~~~

### Amendment Procedures

| Amendment Type | Approval Threshold | Documentation |
|---|---|---|
| **Minor (Procedural)** | Simple majority (≥ 51%). | Logged in Governance Ledger and summarized in transparency reports. |
| **Major (Ethical or Policy)** | Supermajority (≥ 67%). | New version of `ROOT-GOVERNANCE.md` created and referenced in manifest. |
| **Emergency Amendment** | Chair authority; subject to later ratification. | Temporary addendum noted in ledger and reviewed at next quorum meeting. |

All amendments must include:

- A **version bump** in this document’s YAML header.  
- An entry in `reports/audit/release-manifest-log.json`.  
- A corresponding telemetry event in `releases/v*/focus-telemetry.json`.  
- Updated STAC/DCAT/PROV entries reflecting the new version and deprecation of superseded versions.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| **v11.2.6** | 2025-12-10 | A. Barta | Aligned Root Governance Charter with KFM-MDP v11.2.6 (fencing profile, heading registry including 🗺️ Diagrams, telemetry and schema path conventions, AI transform registry), made the canonical ETL → STAC/DCAT/PROV → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode pipeline explicit, and updated references to release v11.2.6 artifacts. |
| **v10.2.3** | 2025-12-06 | A. Barta | Aligned Root Governance Charter with earlier KFM-MDP v11.2.4 (front-matter, heading registry, CI/telemetry metadata); clarified STAC/DCAT/PROV alignment, Story Node & Focus Mode behavior, and architectural implications. |
| v10.2.2 | 2025-11-12 | A. Barta | Updated release/telemetry paths to v10.2.0; clarified governance automation and Council quorum requirements; added explicit amendment → telemetry linkage. |
| v9.7.0 | 2025-11-05 | A. Barta | Established full governance charter with decision-making procedures, roles, and audit integration. |
| v9.5.0 | 2025-10-20 | A. Barta | Added amendment and AI governance procedures. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Created baseline FAIR+CARE Council charter. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
This charter is binding under **Master Coder Protocol v6.3**, **KFM-MDP v11.2.6**, and **FAIR+CARE Governance Certification** · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Governance Index](README.md) · [Standards Index](../README.md)

</div>