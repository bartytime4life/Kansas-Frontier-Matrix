---
title: "🧾 Kansas Frontier Matrix — Issue Templates & Governance Forms Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/ISSUE_TEMPLATE/README.md"
version: "v11.2.2"
last_updated: "2025-12-09"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/github-issues-v4.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "github-issue-templates"
role: "issue-templates-overview"
category: "Governance · Process · Community"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - ".github/ISSUE_TEMPLATE/README.md@v9.0.0"
  - ".github/ISSUE_TEMPLATE/README.md@v9.5.0"
  - ".github/ISSUE_TEMPLATE/README.md@v9.7.0"
  - ".github/ISSUE_TEMPLATE/README.md@v10.0.0"
  - ".github/ISSUE_TEMPLATE/README.md@v10.3.1"
  - ".github/ISSUE_TEMPLATE/README.md@v10.4.1"
  - ".github/ISSUE_TEMPLATE/README.md@v11.0.0"
  - ".github/ISSUE_TEMPLATE/README.md@v11.0.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/github-issues-readme-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/github-issues-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-issues-readme-v11.2.2"
semantic_document_id: "kfm-doc-github-issues-readme"
event_source_id: "ledger:.github/ISSUE_TEMPLATE/README.md"
immutability_status: "mutable-plan"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next issue-templates update"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Issue Templates & Governance Forms Overview**  
`.github/ISSUE_TEMPLATE/README.md`

**Purpose**  
Define the **governance-aware issue template system** for KFM v11, aligning contributor-facing workflows with **FAIR+CARE**, **sovereignty**, **MCP-DL v6.3**, and **KFM-MDP v11.2.5**.

[![MCP-DL](https://img.shields.io/badge/MCP-v6.3-blue)]() · [![KFM-MDP v11.2.5](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.5-purple)]() · [![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)]()

</div>

---

## 📘 Overview

### 1. Scope & Intent

Issue templates in KFM are **part of the governance, provenance, and reproducibility architecture**, not just GitHub conveniences.

They are the **first governed entrypoint** into the pipeline:

> GitHub Issue → CI workflows → ETL (issue telemetry) → STAC/DCAT/PROV catalogs → Neo4j graph → API → MapLibre/Cesium UI → Story Nodes & Focus Mode.

Each template:

- Embeds **FAIR+CARE** metadata and sovereignty flags  
- Enforces **documentation-first** Master Coder Protocol habits (hypotheses, rationale, evidence)  
- Captures **provenance & licensing** details needed for DCAT / STAC / PROV  
- Identifies **cultural sensitivity & sovereignty** controls before data enters KFM  
- Activates **CI/CD validation workflows** (markdown, schema, STAC, DCAT, FAIR+CARE, security)  
- Produces **deterministic telemetry** for governance dashboards and Focus Mode  

This README is the **single source of truth** for `.github/ISSUE_TEMPLATE/*` and is referenced by:

- Template `description` / `body` help text  
- Governance standards under `docs/standards/governance/`  
- Security & FAIR+CARE docs for incident and risk handling  

### 2. Relation to KFM Architecture & MCP-DL

Within the Kansas Frontier Matrix:

- The **platform mission, data domains, and interactive map/timeline** define what counts as an issue worth tracking (new data layer, map bug, story-node bug, etc.).  
- The **ETL and AI/ML pipelines** rely on structured, reproducible metadata from issues to trigger ingestion, training, and knowledge-graph enrichment runs.  
- The **Master Coder Protocol 2.0** requires experiment/feature work to start with structured documentation; issue templates provide the required links into `mcp/` experiments, SOPs, and model cards.  

Practically:

- Each issue becomes a **PROV Activity** (`prov:Activity`) with associated entities (datasets, docs, code) and agents (contributors, maintainers).  
- Issue metadata feeds into **DCAT dataset records** and **STAC Items** when the issue involves data layers or services.  
- The resulting entities and relationships are ingested into the **Neo4j backbone** as nodes and edges, with GeoSPARQL geometries where spatial context is present.  

---

## 🗂️ Directory Layout

The governance-aware issue templates live under:

~~~text
.github/ISSUE_TEMPLATE/                 # Governance-aware issue templates
│
├── 📄 README.md                        # This overview document (you are here)
├── 🐛 bug_report.yml                   # Deterministic bug reporting with repro metadata
├── 💡 feature_request.yml              # Feature proposals with governance/a11y prompts
├── 🗺️ data_submission.yml              # Dataset/STAC/DCAT ingestion + provenance declaration
└── 🛡️ governance_form.yml              # CARE, sovereignty, and cultural-rights review
~~~

**Primary downstream consumers**

- CI workflows under `.github/workflows/`, including (design / expected):
  - `docs_validate.yml` — KFM-MDP v11.2.5 compliance & markdown lint  
  - `stac_validate.yml` — STAC v1.0.0 validation for data-related issues  
  - `dcat_validate.yml` — DCAT 3.0 / KFM-DCAT profile validation  
  - `faircare_validate.yml` — FAIR+CARE, sovereignty & sensitivity checks  
  - `security_audit.yml` — security & vulnerability-related bug reports  
  - `kfm-ci.yml` — shared CI entrypoint for tests, schemas, and issue-telemetry
- Telemetry ETL (design target locations):
  - `src/pipelines/telemetry/github_issues/` — extract structured issue events
  - `data/processed/telemetry/issues/` — normalized issue telemetry snapshots
  - `releases/<version>/focus-telemetry.json` — aggregated governance/usage metrics

**Authored spec & reference docs**

- Governance standards: `docs/standards/governance/`  
- FAIR+CARE & sovereignty: `docs/standards/faircare/`, `docs/standards/sovereignty/`  
- Catalog & provenance: `data/stac/`, `docs/data/catalog/`, `docs/standards/provenance/`  
- Security policy & threat model: `docs/security/`, `.github/SECURITY.md`  

---

## 🧭 Context

### 1. KFM System Context

The issue template system must align with:

- The **public-facing Kansas Frontier Matrix overview** (mission, map/timeline, community contributions).  
- The **spatiotemporal catalogs** (STAC, DCAT) that describe datasets and services.  
- The **provenance & security frameworks** that govern ETL, CI/CD, and AI/ML pipelines.  

Templates are therefore **not** free-form: they are **schema-bound, catalog-aware forms** that can be:

- Parsed deterministically by ETL scripts and GitHub Actions  
- Mapped into **STAC Items / Collections**, **DCAT Datasets / DataServices**, and **PROV Activities / Entities / Agents**  
- Linked forward into **Story Nodes** and Focus Mode narratives (e.g., “Data Submission #123 → new KGS aquifer dataset → STAC Item → map layer → story node about groundwater decline”)  

### 2. Where This Work Lives (Design View)

- **Source of truth** for templates:  
  - `./.github/ISSUE_TEMPLATE/*.yml` (this README and the YAML templates)  
- **Validation & automation** (design targets, some may already exist):  
  - `.github/workflows/docs_validate.yml` — markdown, metadata, KFM-MDP checks  
  - `.github/workflows/stac_validate.yml` — STAC JSON schema validation, PySTAC runs  
  - `.github/workflows/dcat_validate.yml` — DCAT / RDF validation and SHACL checks  
  - `.github/workflows/faircare_validate.yml` — CARE flags, sovereignty, and masking rules  
  - `.github/workflows/security_audit.yml` — security bug triage, SBOM-linked checks  
- **Downstream governance artifacts**:
  - `docs/reports/audit/governance-ledger.json` — decisions and CARE reviews  
  - `releases/<version>/focus-telemetry.json` — governance & usage metrics for Focus Mode  
  - `data/stac/**` and `docs/data/catalog/**` — dataset entries resulting from data submissions  

These locations should be treated as part of the **governed KFM interface contract**: any new pipeline, API, or frontend code that consumes issues must respect these files and their schemas.

---

## 🧱 Architecture

### 1. Template Roles & Responsibilities

| Template                | Purpose                          | Required Fields                                      | Triggers (design / expected)                            |
|-------------------------|----------------------------------|------------------------------------------------------|---------------------------------------------------------|
| **🐛 bug_report.yml**      | Capture reproducible defects     | environment, repro steps, expected/actual, logs      | `kfm-ci.yml`, `security_audit.yml`                      |
| **💡 feature_request.yml** | Request features with governance | rationale, FAIR+CARE, a11y, deployment/rollout       | `docs_validate.yml`                                     |
| **🗺️ data_submission.yml** | Add/update datasets              | license, provenance, STAC/DCAT, bbox, temporal range | `stac_validate.yml`, `dcat_validate.yml`, `faircare_validate.yml` |
| **🛡️ governance_form.yml** | Cultural/Indigenous review       | CARE, sovereignty, consent, reviewer, decision       | `faircare_validate.yml`, governance-ledger ETL          |

All governance actions are aggregated into:

~~~text
docs/reports/audit/governance-ledger.json
~~~

and included in **release manifests** (`releases/<version>/manifest.zip`) for long-term traceability.

### 2. Template Deep-Dive

#### 2.1 🐛 `bug_report.yml` — System & Security Defects

Captures:

- Runtime environment & version (browser, OS, KFM release, commit SHA)  
- System area (frontend, ETL, graph, STAC/API, Focus Mode, CI/CD, infra)  
- Deterministic reproduction steps  
- Expected vs. actual behavior  
- Logs, screenshots, and relevant dataset IDs / STAC Items (if applicable)  
- Security impact classification (none / low / high / critical)  

Routing:

- General bugs → `kfm-ci.yml` (tests, lint, regression checks)  
- Security-related bugs → `security_audit.yml` with:
  - CVSS-like severity, exploitability, and impact fields  
  - Links to SBOM entries and dependency advisories  
  - Optional mapping to incident reports in `docs/security/reports/`  

Graph/provenance mapping:

- Each bug becomes an **Issue Activity** linked to code entities, datasets, and agents, enabling lineage like “this map bug traces back to this STAC collection and ETL version.”

#### 2.2 💡 `feature_request.yml` — Architecture & Product Changes

Captures:

- Feature rationale and expected user impact  
- Affected components (APIs, ETL, graph, UI, Focus Mode)  
- Documentation impact (new standards, guides, or analyses required)  
- Governance implications:
  - FAIR dimensions (Findable, Accessible, Interoperable, Reusable)  
  - CARE & sovereignty impact for any data touched  
  - Accessibility (WCAG) considerations  
  - Sustainability & energy/carbon impact of new pipelines or models  

Architecture & governance implications:

- Features involving **predictive models, archaeological or Indigenous data, or sensitive locations** must reference relevant standards (security, FAIR+CARE, sovereignty) and may require a paired `governance_form.yml` issue.  
- Approved features should link to:
  - `docs/architecture/<area>-architecture.md`  
  - `mcp/experiments/*` and `mcp/model_cards/*` if ML is involved  

#### 2.3 🗺️ `data_submission.yml` — Datasets, STAC, and DCAT

Used for new or updated datasets. Requires:

- Dataset identifier, scope, and intended audience  
- STAC 1.0.0 metadata (id, geometry, bbox, datetime, assets, properties)  
- DCAT 3.0 metadata (title, description, license, creator, temporal/spatial coverage)  
- Provenance chain (source, author, consent, legal basis)  
- Spatial & temporal extents; CRS references  
- License & rights validation (including Indigenous sovereignty flags as needed)  
- Checksums / integrity data (e.g., SHA-256)  

Triggers:

- `stac_validate.yml` → JSON schema & extension checks  
- `dcat_validate.yml` → RDF/DCAT validation & SHACL shapes  
- `faircare_validate.yml` → CARE & sovereignty review when needed  

“No dataset enters `data/` or `data/stac/` without passing these gates.”

#### 2.4 🛡️ `governance_form.yml` — CARE & Sovereignty Decisions

Used for:

- Indigenous / CARE reviews of datasets, story nodes, or map layers  
- Cultural or sacred-site data  
- Sensitive historical or ecological locations (e.g., burial sites, endangered species)  
- Non-public or governed archival content  

Captures:

- CARE evaluation (Collective Benefit, Authority, Responsibility, Ethics)  
- Sovereignty constraints and data handling rules  
- Masking/generalization requirements (e.g., H3 grids, coarsened coordinates)  
- Reviewer identity, institutional role, date, and decision (approve/deny/conditional)  
- Access, retention, and sunset rules for governed content  

Outputs feed into:

~~~text
docs/reports/audit/governance-ledger.json
releases/<version>/focus-telemetry.json
~~~

for long-term governance traceability and Focus Mode awareness.

---

## 🧪 Validation & CI/CD

### 1. Workflow Routing

~~~mermaid
flowchart TD
  A["✍️ Issue Submitted"] --> B["📋 Template Parser (GitHub form → YAML)"]
  B --> C["📚 Docs Validation (KFM-MDP v11.2.5)"]
  B --> D["🛰 STAC/DCAT Validation (Data Submissions)"]
  B --> E["⚖ FAIR+CARE & Sovereignty Checks"]
  B --> F["🔐 Security Audit (Bugs/Security)"]
  C --> G["📊 Telemetry Export (issue events → focus-telemetry.json)"]
  D --> G
  E --> G
  F --> G
~~~

**Design goals**

- All workflows are **config-driven** and **deterministic**, aligned with MCP-DL:
  - No implicit behavior based solely on textual labels
  - All routing driven by template fields and labels that map to schema-enforced enums  
- Each job:
  - Validates structure (`json_schema_ref`, `shape_schema_ref`)  
  - Produces machine-readable reports in `reports/self-validation/github-issues/*.json`  
  - Updates telemetry in `releases/<version>/focus-telemetry.json`  

### 2. Where to Implement

- CI workflows under `.github/workflows/`:
  - `github-issues-validate.yml` — orchestrator for all issue-related checks  
  - `stac-validate.yml`, `dcat-validate.yml` — reuse same STAC/DCAT tooling used for data catalogs  
  - `faircare-validate.yml` — run FAIR+CARE / sovereignty checks and SHACL shapes  
  - `security-audit.yml` — integrate SBOMs, SLSA attestations, and security advisories  

- Supporting code under:
  - `src/pipelines/ci/github_issues/` — helper scripts to parse issues → telemetry  
  - `src/validation/stac/`, `src/validation/dcat/`, `src/validation/prov/` — shared validators  

---

## 📦 Data & Metadata

### 1. Telemetry Outputs

Telemetry dimensions:

- Metadata completeness per template and field  
- Governance errors/warnings (missing license, missing provenance, etc.)  
- CARE/sovereignty flags and decision outcomes  
- Provenance coverage and chain depth  
- License correctness vs. allowed licenses  
- Accessibility metadata success rate (a11y prompts completed)  
- STAC/DCAT/PROV compliance for data submissions  
- Security-related metrics (e.g., security bugs per release, time-to-patch)  

Aggregated into:

~~~text
releases/<version>/focus-telemetry.json
~~~

and consumed by:

- Governance dashboards (e.g., `web/admin/governance-dashboard`)  
- Focus Mode context in the frontend (weighted selection of governance-relevant Story Nodes)  

### 2. Governance Ledger

`docs/reports/audit/governance-ledger.json` acts as:

- A **PROV-friendly log** of governance Activities (reviews, approvals, denials)  
- A reference for **DCAT-qualified relations** among Datasets (e.g., supersedes, derived-from)  
- A record of **CARE decisions** and sovereignty obligations, connected to dataset IDs and STAC Items  

All entries should be:

- Validated against `shape_schema_ref`  
- Linked to specific GitHub issues via `event_source_id` or similar identifiers  

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC Integration

For `data_submission.yml`:

- Required fields map directly into **STAC Item** properties:
  - `id`, `geometry`, `bbox`, `properties.datetime`, `assets`  
- Collection-level metadata is either referenced or created via **STAC Collections** for dataset families.  
- Validation uses:
  - STAC 1.0.0 JSON Schemas  
  - Extensions such as `scientific`, `checksum`, and `version` where appropriate  

Templates ensure that every dataset entering `data/stac/**` is catalog-ready and can be exposed via a self-hosted STAC API used by the map/timeline.

### 2. DCAT Integration

Issues that describe datasets or services must carry enough information to synthesize:

- **dcat:Dataset** entries (title, description, license, publisher, temporal/spatial coverage)  
- **dcat:Distribution** entries (download links, media type, checksum)  
- Where relevant, **dcat:DataService** entries (API endpoints for map services, STAC APIs, etc.)  

`dcat_validate.yml` should:

- Translate issue data into RDF according to the KFM-DCAT profile  
- Validate with SHACL shapes in `shape_schema_ref`  
- Store draft DCAT RDF under `data/catalog/work/` for human review before publication  

### 3. PROV & Graph Integration

Each issue is modeled as:

- A **PROV Activity** (`prov:Activity`) with:
  - `prov:used` — linked datasets, docs, code modules  
  - `prov:wasAssociatedWith` — contributors, maintainers, councils  
- Output Entities:
  - New or updated docs (`docs/*`), data files (`data/*`), STAC Items, DCAT Datasets  
- Governance Activities (from `governance_form.yml`) link to:
  - CARE decisions as Entities (`prov:Entity` plans, policies)  
  - Agents (FAIR+CARE Council, tribal data stewards)  

In Neo4j:

- Issues become nodes (e.g., `:IssueEvent`) connected via typed relationships to Places, Datasets, Story Nodes, and Governance Decisions, with geometries attached via GeoSPARQL-compatible properties where appropriate.

---

## ⚖ FAIR+CARE & Governance

### 1. FAIR Integration

Issue templates encode FAIR principles:

- **F1 — Findable**: IDs, clear titles, and references to datasets/STAC/DCAT IDs  
- **A1 — Accessible**: Explicit licenses, access conditions, and contact points  
- **I1 — Interoperable**: Use of standard metadata profiles (STAC, DCAT, PROV, GeoSPARQL)  
- **R1 — Reusable**: Documented provenance, rights, and sufficient contextual notes  

### 2. CARE & Sovereignty

The `governance_form.yml` and empowerment fields in other templates:

- Flag Indigenous or culturally sensitive data early in the workflow  
- Capture consent, restrictions, and masking requirements before data is ingested  
- Route decisions through the FAIR+CARE Council and Indigenous partners when required  
- Enforce spatial generalization for sensitive sites (e.g., H3 grids, coarsened bounding boxes)  
- Ensure AI components (Focus Mode, Story Nodes) do **not** surface restricted or sensitive knowledge, nor hallucinate events that could cause harm  

Templates and workflows must never override:

- `sovereignty/INDIGENOUS-DATA-PROTECTION.md`  
- `ROOT-GOVERNANCE.md`  
- Security policies in `.github/SECURITY.md`  

### 3. Concrete Next Steps / Backlog Items

Recommended tasks to harden this design:

1. **Schema hardening**
   - Add per-template JSON Schemas under `schemas/json/github-issues-*.schema.json`.
   - Add SHACL shapes for governance ledger and telemetry under `schemas/shacl/`.
2. **Issue telemetry ETL**
   - Implement `src/pipelines/telemetry/github_issues/` to ingest GitHub Events → normalized telemetry.
   - Wire ETL into `kfm-ci.yml` and nightly batch jobs (for backfill and aggregation).
3. **Graph & Story Node integration**
   - Define Neo4j data model for `:IssueEvent`, `:GovernanceDecision`, and their relationships.
   - Add Focus Mode strategies to prioritize governed issues as candidate Story Nodes.
4. **Security & compliance**
   - Ensure all GitHub Actions used in issue workflows are pinned by SHA and run with least-privilege tokens.
   - Add regression tests to verify that sensitive-location issues are never exposed in public STAC/DCAT outputs without masking.

---

## 🕰️ Version History

| Version | Date       | Notes                                                                                                               |
|--------:|-----------:|---------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-12-09 | Realigned H2 headings to KFM-MDP v11.2.5, clarified CI/CD routing, and strengthened STAC/DCAT/PROV/FAIR+CARE links. |
| v11.0.2 | 2025-11-19 | Full v11 architecture upgrade; expanded sovereignty processing; telemetry hooks added.                              |
| v11.0.1 | 2025-11-19 | Metadata enrichment, directory layout fix, stable MDP-v11 formatting.                                               |
| v11.0.0 | 2025-11-18 | First full v11 version with FAIR+CARE alignment.                                                                    |
| v10.4.1 | 2025-11-16 | Added CARE and a11y fields.                                                                                         |
| v10.3.1 | 2025-11-13 | Introduced telemetry routing.                                                                                       |
| v10.0.0 | 2025-11-09 | Initial Issue Template docs.                                                                                        |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧾 Pull Request Template](../PULL_REQUEST_TEMPLATE.md) · [🛡️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>