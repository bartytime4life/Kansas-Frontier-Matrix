---
title: "⚙️ Kansas Frontier Matrix — CI/CD & Governance Workflows (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/workflows/README.md"

version: "v11.2.4"
last_updated: "2025-12-05"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "releases/v11.2.4/signature.sig"
attestation_ref: "releases/v11.2.4/slsa-attestation.json"
sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-workflows-v11.2.4.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard Index"
intent: "ci-cd-and-governance-workflows-index"
category: "CI/CD · Governance · FAIR+CARE"

scope:
  domain: "ci-cd-governance"
  applies_to:
    - ".github/workflows/*.yml"
    - "docs/workflows/*.md"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
ttl_policy: "Annual review"
sunset_policy: "Superseded by CI/CD & Governance Workflows v12"

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
  - "docs/workflows/README.md@v11.2.2"
  - "docs/workflows/README.md@v10.2.4"
  - "docs/workflows/README.md@v10.1.0"
  - "docs/workflows/README.md@v10.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:workflows:ci-cd-governance:v11.2.4"
semantic_document_id: "kfm-ci-cd-governance-workflows-v11.2.4"
event_source_id: "ledger:kfm:doc:workflows:ci-cd-governance:v11.2.4"
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
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "3d-context-render"
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

# ⚙️ **Kansas Frontier Matrix — CI/CD & Governance Workflows (v11.2.4)**  
`docs/workflows/README.md`

**Purpose**  
Define and document the **autonomous CI/CD and governance workflows** that power validation, FAIR+CARE auditing, telemetry exports, supply‑chain hardening, and AI ethics governance across the Kansas Frontier Matrix (KFM).  
All workflows are **MCP‑DL v6.3–certified**, wired into governance ledgers, and emit **sustainability and compliance telemetry** suitable for STAC/DCAT/PROV indexing and graph ingestion.

<!-- Badge Row -->
<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance_Aligned-gold" />
<img src="https://img.shields.io/badge/Lineage-OpenLineage_v2.5-orange" />
<img src="https://img.shields.io/badge/Status-Automated-success" />

</div>

---

## 📘 Overview

### 1. Scope

This index defines how **CI/CD workflows and their documentation** fit into the standard KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

Within that pipeline, this document:

- Describes each **GitHub Actions** / automation job that underpins:
  - Documentation + STAC + DCAT + PROV validation  
  - FAIR+CARE & sovereignty checks  
  - Energy, carbon, and runtime telemetry  
  - AI training, explainability, and bias/drift audits  
  - Supply‑chain security (SBOM, signatures, worm defense)  
  - Governance ledger updates and sustainability reporting
- Standardizes **how workflows are documented** under `docs/workflows/*.md`.
- Ensures every `.yml` in `.github/workflows/` is:
  - **Config‑driven** (no ad‑hoc logic),
  - **Provenance‑logged** (OpenLineage / PROV),
  - **Telemetry‑emitting** (shared schemas),
  - **FAIR+CARE‑auditable**.

Each workflow YAML has a matching Markdown file (`*.yml.md`) capturing:

- 🧩 Purpose & context  
- ⚙️ Execution scope (triggers, inputs, outputs, artifacts)  
- ⚖️ FAIR+CARE & sovereignty hooks  
- 📊 Telemetry schema & metrics  
- 🧠 AI/ethics and human‑in‑the‑loop expectations  

### 2. Workflow Families

KFM workflows fall into four governed families:

1. **Documentation & Metadata Validation** – Markdown, schema, STAC/DCAT/PROV checks.  
2. **FAIR+CARE & Governance** – ethics, accessibility, sovereignty, governance ledger.  
3. **AI Governance & Explainability** – model training, bias, drift, explainability audits.  
4. **Supply‑Chain Security** – SBOM, signatures, SLSA, npm worm/typosquat defenses.

Per KFM‑MDP, this index is the **entry Story Node** for CI/CD in Focus Mode and the canonical reference for adding or modifying workflows.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 workflows/
    📄 README.md                        — ← This index
    📄 docs-lint.yml.md                 — Markdown + README validator
    📄 faircare-validate.yml.md         — FAIR+CARE governance validation
    📄 telemetry-export.yml.md          — Energy + performance telemetry exporter
    📄 stac-validate.yml.md             — STAC/DCAT/PROV catalog validator
    📄 schema-lint.yml.md               — JSON/SHACL schema validator
    📄 ai-train.yml.md                  — AI model training with governance hooks
    📄 ai-explainability.yml.md         — Bias/drift/explainability audit pipeline
    📄 security-supply-chain.yml.md     — SBOM, signing & npm worm defense
    📄 lidar-glo-integration.md         — LiDAR & GLO integration field guide
    📄 workflow_template.md             — Template for new workflow docs
~~~

Author rules:

- Every `.github/workflows/*.yml` **MUST** have a corresponding `docs/workflows/<name>.yml.md` (or `.md` for field guides).  
- New workflows **MUST** be added to this tree and documented using `workflow_template.md`.  
- Directory layout in docs **MUST** use `~~~text` fences and the canonical `├──` / `└──` glyphs.

---

## 🧭 Context

KFM treats **CI/CD as a governed data pipeline**:

- **Source of truth** – Workflow YAML + this index are cataloged as datasets and services in DCAT and STAC.  
- **Provenance** – Each workflow run is a PROV activity, generating entities (artifacts, reports) and attributed to agents (GitHub Actions runners, maintainers).  
- **Graph integration** – Workflow docs, run summaries, and telemetry are ingested into Neo4j as:
  - `:Workflow`, `:WorkflowRun`, `:Report`, `:TelemetrySnapshot` nodes,
  - Linked by `:GENERATED`, `:VALIDATED`, `:OBSERVED`, `:GOVERNED_BY` relationships.
- **Downstream impact** – No dataset, Story Node, or frontend deployment is “production” unless:
  - Docs pass lint & schema checks,
  - FAIR+CARE constraints pass,
  - Telemetry is recorded for energy/carbon,
  - Provenance is attached for later audit.

This index is therefore **both**:

- A **developer‑facing guide** for workflows, and  
- A **catalog record** enabling machine discovery and governance automation.

---

## 🗺️ Diagrams

### CI/CD & Governance Flow (Conceptual)

~~~mermaid
flowchart LR
    A[Commit / PR] --> B[.github/workflows/*]
    B --> C[Docs & Schema Lint]
    B --> D[STAC/DCAT/PROV Validation]
    B --> E[FAIR+CARE & Sovereignty Audit]
    B --> F[Security & Supply-Chain Checks]

    C --> G[Build / Package Artifacts]
    D --> G
    E --> H[Governance Ledger Update]
    F --> G

    G --> I[Telemetry Export<br/>(energy · carbon · quality)]
    I --> J[Dashboards · Focus Mode · Reports]
~~~

All concrete workflow docs in this directory **MUST** explain where they attach in this flow and what artifacts they emit.

---

## 🧠 Story Node & Focus Mode Integration

- **Story Node role**  
  - This file is the **root CI/CD Story Node** for KFM.
  - H2 sections map to Story Node facets (Overview, Context, Validation, Governance, Version History).

- **Focus Mode behaviour**
  - MAY summarize the workflow families, validation matrix, and telemetry design.
  - MAY highlight which workflows gate which repo paths.
  - MUST NOT invent new governance rules; it can only restate text from this and referenced standards.

- **Anchors for other Story Nodes**
  - Each workflow doc (`*.yml.md` / `.md`) should reference this index as its **parent** via `semantic_document_id`.
  - Derived Story Nodes (e.g. `urn:kfm:story-node:workflows:docs-lint`) should link to the corresponding H3 sections in this file and the per‑workflow Markdown.

Result: Focus Mode can answer “What happens when I push to main?” or “Where do FAIR+CARE checks live?” using this index + local subgraph, without guessing.

---

## 🧪 Validation & CI/CD

### 1. Documentation & Metadata Validation

These workflows ensure docs and metadata remain CI‑safe and catalog‑ready.

| Workflow Doc           | Purpose                                                      | Output Artifact                                            |
|------------------------|--------------------------------------------------------------|------------------------------------------------------------|
| `docs-lint.yml.md`     | Enforce KFM‑MDP v11.2.4 + README rules and headings.         | `reports/self-validation/docs/lint_summary.json`           |
| `stac-validate.yml.md` | Validate STAC/DCAT/PROV metadata & geospatial consistency.   | `reports/self-validation/stac/stac_summary.json`           |
| `schema-lint.yml.md`   | Validate JSON/SHACL schemas in `schemas/`.                  | `reports/self-validation/schemas/schema_summary.json`      |

Responsibilities:

- Reject non‑compliant Markdown or front‑matter.  
- Block merges when STAC/DCAT/PROV descriptions drift from schemas.  
- Keep schemas themselves guarded by SHACL/JSON Schema.

---

### 2. FAIR+CARE & Governance Validation

| Workflow Doc                | Purpose                                            | Output Artifact                                 |
|-----------------------------|----------------------------------------------------|-------------------------------------------------|
| `faircare-validate.yml.md`  | FAIR+CARE ethics, accessibility & sovereignty.     | `reports/fair/faircare_summary.json`            |
| `governance-audit.yml.md`   | Sync CI events into governance ledgers.            | `reports/audit/governance_ledger_delta.json`    |
| `telemetry-export.yml.md`   | Consolidate metrics (runtime, energy, carbon).     | `releases/v11.2.4/focus-telemetry.json`         |

These workflows:

- Inspect data classifications, CARE labels, and sovereignty flags.  
- Enforce accessibility basics on docs and UI builds.  
- Emit ledger‑ready records of significant CI/CD events.

---

### 3. AI Governance & Explainability

| Workflow Doc                 | Purpose                                                 | Output Artifact                               |
|------------------------------|---------------------------------------------------------|-----------------------------------------------|
| `ai-train.yml.md`            | Model training with governance + provenance hooks.      | `reports/ai/ai_model_training.json`           |
| `ai-explainability.yml.md`   | Explainability, bias & drift telemetry for models.      | `reports/audit/ai_model_faircare.json`        |

Key expectations:

- Every training run is config‑driven and logged with dataset/model versions.  
- Explainability runs measure bias and drift over time, not just once.  
- Outputs link back to data and code via PROV/lineage identifiers.

---

### 4. Supply‑Chain Security

| Workflow Doc                    | Purpose                                                  | Output Artifact                                         |
|---------------------------------|----------------------------------------------------------|---------------------------------------------------------|
| `security-supply-chain.yml.md`  | SBOM, SLSA, signature checks, npm worm defense.          | `reports/audit/supply_chain_security_summary.json`      |

This family:

- Generates SBOMs and attaches checksums/signatures to artifacts.  
- Scans dependencies for known malicious patterns (e.g., worms/typosquats).  
- Blocks releases when integrity or provenance can’t be established.

---

### 5. Example Workflow: FAIR+CARE Governance Validation

Conceptual behavior documented in `faircare-validate.yml.md`:

~~~yaml
name: FAIR+CARE Governance Validation

on:
  push:
    paths:
      - "data/**"
      - "docs/**"

jobs:
  faircare-audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run FAIR+CARE Validator
        run: python tools/validation/faircare_validator.py --path data/ --docs docs/

      - name: Upload FAIR+CARE Report
        uses: actions/upload-artifact@v4
        with:
          name: faircare_summary
          path: reports/fair/faircare_summary.json
~~~

This pattern is **normative**:

- Data/docs changes **must** trigger FAIR+CARE validation.  
- Reports are uploaded as artifacts and registered in telemetry + catalogs.  
- Failing FAIR+CARE checks **block merges** until fixed.

---

## 📦 Data & Metadata

### 1. Telemetry & Metrics

All workflow runs contribute structured entries to `focus-telemetry.json` (and any run‑specific reports). Typical fields:

- `workflow` (e.g., `faircare-validate`)  
- `run_id` (globally unique)  
- `workflow_duration_sec`  
- `jobs_succeeded`, `jobs_failed`  
- `docs_validated`, `datasets_validated`  
- `faircare_score` (0–100)  
- `energy_wh`, `carbon_gco2e`  
- `timestamp` (UTC ISO‑8601)

Example aggregated entry:

~~~json
{
  "workflow": "faircare-validate",
  "run_id": "faircare_2025-11-27_001",
  "workflow_duration_sec": 92,
  "docs_validated": 184,
  "faircare_score": 98,
  "energy_wh": 3.1,
  "carbon_gco2e": 0.0012,
  "timestamp": "2025-11-27T17:45:12Z"
}
~~~

Telemetry schemas live under `schemas/telemetry/` and are referenced from this doc’s front‑matter.

### 2. Cataloging Workflow Artifacts

For each workflow:

- The YAML definition + Markdown doc = **DCAT Datasets** with **Distributions**:
  - Raw YAML (`text/plain`),
  - Rendered HTML docs,
  - JSON reports from runs.
- Each workflow’s output reports (e.g., `lint_summary.json`) are:
  - DCAT Distributions of a “CI/CD Reports” dataset;  
  - STAC Assets (non‑spatial) in a `kfm-ci` Collection;  
  - PROV Entities linked to Activities (runs) and Agents (runners/maintainers).

This guarantees that **CI/CD itself is cataloged, versioned, and traceable**, just like domain datasets.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. DCAT

- **Catalog**: KFM’s data catalog lists:
  - This index (`kfm-ci-cd-governance-workflows-v11.2.4`) as a `dcat:Dataset` or `dcat:CatalogRecord`.  
  - Each per‑workflow doc as its own `dcat:Dataset`.

- **Distributions**:
  - HTML, Markdown, YAML, and JSON reports as `dcat:Distribution` with proper media types and checksums.

- **Versioning**:
  - This file’s `version` and Version History map to DCAT 3’s versioning properties (`dcat:hasVersion`, `dcat:previousVersion`).

### 2. STAC

- **Collections**:
  - `kfm-ci` Collection for CI/CD artifacts and telemetry.

- **Items**:
  - Each workflow run → STAC Item with:
    - `id` = `run_id`,  
    - `properties.datetime` = run timestamp,  
    - `assets` = telemetry JSON, reports, logs.

- **Geometry & bbox**:
  - Non‑spatial CI/CD items may use `geometry: null` and omit `bbox`, or associate with a default Kansas bbox for region‑scoped analysis if desired.

### 3. PROV‑O

- **Entities**:
  - Workflow YAML, workflow docs, reports, telemetry snapshots.

- **Activities**:
  - Each workflow run is a `prov:Activity` with `prov:startedAtTime` / `prov:endedAtTime`.

- **Agents**:
  - GitHub runners (software agents), maintainers (persons/organizations).

- **Relations**:
  - `prov:wasGeneratedBy` from reports → workflow run.  
  - `prov:used` from run → commit SHA, configs, input datasets.  
  - `prov:wasAssociatedWith` from run → agents.

This alignment lets lineage tools reconstruct exactly **which workflow version** validated **which commit or dataset** and with **what outcome**.

---

## 🧱 Architecture

From a monorepo perspective:

- **docs/**  
  - `docs/workflows/README.md` = CI/CD index (this file).  
  - `docs/workflows/*.yml.md` / `.md` = per‑workflow specs & SOPs.

- **.github/workflows/**  
  - YAML definitions implementing the flows described here.

- **src/pipelines/**  
  - ETL / data pipelines invoked by some workflows (e.g., refresh catalogs).

- **data/stac/** and **data/sources/**  
  - Catalogs and manifests that some validation workflows read.

Design rules:

1. **Config‑driven** – No workflow encodes critical values inline; use configs checked into git.  
2. **Deterministic** – Given the same commit, configs, and inputs, workflows produce the same artifacts.  
3. **Open Provenance** – All runs produce machine‑readable provenance and telemetry.  
4. **Loose coupling** – Workflows interact with pipelines and graph via stable APIs/contracts, not ad‑hoc queries.

Any new workflow proposal **MUST**:

- Declare its triggers, artifacts, telemetry fields, and governance implications.  
- Be accompanied by a new `*.yml.md` / `.md` doc and an update to this index.

---

## ⚖ FAIR+CARE & Governance

### 1. Governance Matrix (CI/CD Lens)

| Principle | Implementation                                            | Oversight                    |
|----------:|-----------------------------------------------------------|------------------------------|
| F1        | Workflows documented here; indexed in catalogs & manifests. | FAIR+CARE Council            |
| A1        | Logs & reports stored in known, queryable locations.      | Reliability Engineering      |
| I1 / I2   | Standardized YAML + JSON Schema + OpenLineage hooks.      | Architecture Working Group   |
| R1        | Templates & SOPs encourage reuse; configs versioned.      | DevOps / CI Working Group    |
| CARE      | Telemetry tracks ethics + sustainability for automation.  | FAIR+CARE Security Working G |

### 2. Policies

- **Review cadence**
  - Weekly workflow health review by FAIR+CARE Security + Reliability teams.

- **Merge conditions**
  - New/changed workflows MUST:
    - Pass schema + lint checks.  
    - Emit telemetry conforming to declared schemas.  
    - Declare purpose, inputs, outputs, and governance impact.

- **Sustainability targets**
  - Aim for ≤ 15 Wh per workflow run on average (per telemetry).  
  - Track carbon emissions per run; highlight large regressions.

- **Retention**
  - Logs & telemetry retained ≥ 12 months (or stricter per governance rules).

These policies are enforced at CI level and visible to Focus Mode users inspecting CI/CD behavior.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                                     |
|-----------:|------------|-----------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-05 | Aligned with KFM‑MDP v11.2.4; adopted standard front‑matter, approved H2s, Story Node/Focus Mode hooks, and STAC/DCAT/PROV mappings. No semantic workflow changes. |
| v11.2.2   | 2025-11-27 | Canonical layout; badges/footer added; telemetry schema updated; FAIR+CARE + governance workflows consolidated.             |
| v10.2.4   | 2025-11-12 | Telemetry schema v3 adoption; governance matrix refresh; sustainability policy alignment.                                   |
| v10.1.0   | 2025-11-10 | Added AI explainability + telemetry exporter workflows.                                                                      |
| v10.0.0   | 2025-11-08 | Established baseline CI/CD and FAIR+CARE validator workflows for KFM.                                                       |

---

<div align="center">

⚙️ **Kansas Frontier Matrix — CI/CD & Governance Workflows (v11.2.4)**  
Ethical Automation · FAIR+CARE Governance · Sustainable CI/CD  

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance_Aligned-gold" />
<img src="https://img.shields.io/badge/OpenLineage-v2.5-informational" />
<img src="https://img.shields.io/badge/CI%2FCD-Automated-lightgrey" />

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.4 · FAIR+CARE Aligned · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Docs Root](../README.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) ·  
[📘 KFM Documentation Home](../README.md)

</div>
