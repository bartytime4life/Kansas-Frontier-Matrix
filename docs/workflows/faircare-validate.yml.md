---
title: "⚖️ Kansas Frontier Matrix — FAIR+CARE Validation Workflow (`faircare-validate.yml`) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/workflows/faircare-validate.yml.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "releases/v11.2.6/signature.sig"
attestation_ref: "releases/v11.2.6/slsa-attestation.json"
sbom_ref: "releases/v11.2.6/sbom.spdx.json"
manifest_ref: "releases/v11.2.6/manifest.zip"
telemetry_ref: "releases/v11.2.6/faircare-validate-telemetry.json"
telemetry_schema: "schemas/telemetry/faircare-validate-workflow-v11.2.6.json"
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
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "ci-cd-workflows"
  applies_to:
    - ".github/workflows/faircare-validate.yml"
    - "data/**"
    - "docs/**"
    - "schemas/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Data & metadata governance; may reference sensitive classifications"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by FAIR+CARE Validation Workflow v12"

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
  - "docs/workflows/faircare-validate.yml.md@v10.2.4"
  - "docs/workflows/faircare-validate.yml.md@v10.1.0"
  - "docs/workflows/faircare-validate.yml.md@v9.9.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:workflows:faircare-validate-yml:v11.2.6"
semantic_document_id: "kfm-workflow-faircare-validate-yml-v11.2.6"
event_source_id: "ledger:kfm:doc:workflows:faircare-validate-yml:v11.2.6"
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
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/faircare-validate.yml"
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

# ⚖️ **Kansas Frontier Matrix — FAIR+CARE Validation Workflow (`faircare-validate.yml`)**  
`docs/workflows/faircare-validate.yml.md`

**Purpose**  
Define the **governed GitHub Actions workflow** that validates datasets and docs for **FAIR+CARE** compliance, performs **ethics/PII scans**, enforces **data contracts**, manages **abandonment candidates**, and emits **governance‑ready reports** with full telemetry for Diamond⁹ Ω / Crown∞Ω certification.  
This workflow is the primary **ethics and governance gate** for data and documentation in the Kansas Frontier Matrix (KFM).

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/Data-FAIR%2BCARE-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/Status-Automated-brightgreen" />

</div>

---

## 📘 Overview

### 1. Workflow Intent

`faircare-validate.yml` is the **ethics and governance gate** for KFM. It ensures that any change to **data**, **docs**, or **schemas** is checked for:

- ✅ **FAIR** — Findable, Accessible, Interoperable, Reusable properties.  
- ✅ **CARE** — Collective benefit, Authority to control, Responsibility, Ethics.  
- ✅ **Contracts** — JSON Schema & data‑contract conformance (e.g., `data-contract-v3.json`).  
- ✅ **PII & Sensitive Content** — Automated detection of personally identifiable info and culturally sensitive content.  
- ✅ **Quarantine** — Non‑compliant assets moved to `abandonment_candidates/` with a registry entry.  
- ✅ **Reports & Telemetry** — Machine‑readable audit packs and telemetry for governance ledgers.

The workflow runs as part of the CI/CD pipeline so no dataset or document can progress to production catalogs or the knowledge graph without passing FAIR+CARE validation or being explicitly handled through governance overrides.

### 2. Role in the KFM Pipeline

Within the KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

`faircare-validate.yml` sits between **ETL** and **catalog/graph ingestion**, enforcing:

- Contract and schema validity for new/updated assets.  
- FAIR+CARE and sovereignty rules (including Indigenous data protections).  
- A clear paper trail when data is quarantined or requires council review.

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📚 docs/
│   ├── ⚙️ workflows/
│   │   📄 README.md                           # CI/CD & Governance Workflows index
│   │   📄 faircare-validate.yml.md            # ⚖️ FAIR+CARE validation workflow (this file)
│   └── 📏 standards/
│       ├── 📁 faircare/
│       │   📄 FAIRCARE-GUIDE.md               # FAIR+CARE standard
│       ├── ⚖️ governance/
│       │   📄 ROOT-GOVERNANCE.md              # Governance charter
│       └── 🪶 sovereignty/
│           📄 INDIGENOUS-DATA-PROTECTION.md   # Sovereignty policy
│
├── 🗂️ data/
│   ├── 📁 sources/                            # Source manifests (DCAT-aligned)
│   ├── 📁 raw/                                # Raw ingested data (not committed)
│   ├── 📁 work/
│   │   └── 📁 staging/
│   │       └── 📁 tabular/
│   │           └── 🚫 abandonment_candidates/ # Quarantined assets + registry
│   │               📄 abandonment_registry.json
│   └── 📁 processed/                          # Validated, production-ready assets
│
├── 📊 reports/
│   └── ⚖️ faircare/
│       📄 contract_summary.json               # Data-contract validation summary
│       📄 faircare_summary.json               # FAIR+CARE audit results
│       📄 pii_scan.json                       # PII / sensitive markers
│       📄 provenance_trace.json               # DCAT/PROV-style lineage
│
└── 📦 releases/
    └── 📁 v11.2.6/
        📄 faircare-validate-telemetry.json    # Aggregated FAIR+CARE telemetry
        📄 sbom.spdx.json                      # SBOM for validation tools
        📄 manifest.zip                        # Release manifest (hashes, configs)
~~~

---

## 🧭 Context

### 1. Trigger & Scope

| Trigger            | Paths                         | Notes                                  |
|-------------------:|-------------------------------|----------------------------------------|
| `pull_request`     | `data/**`, `docs/**`, `schemas/**` | Blocks merges on governance failure    |
| `push` (protected) | `data/**`, `docs/**`, `schemas/**` | Required on `main` & `release/**`      |
| `schedule`         | nightly                       | Continuous surveillance of staged data |

**Ignored for content scans:** large binaries (`*.tif`, `*.pmtiles`, etc.) where metadata is instead validated.

### 2. Relationship to Other Workflows

- **Upstream:** ETL and ingest pipelines that place assets in `data/raw/` and `data/work/`.  
- **Peers:**  
  - `docs-lint.yml` — structural Markdown and MDP compliance.  
  - `ai-train.yml` — governed model training.  
  - `ai-explainability.yml` — model‑level explainability and bias audits.  
- **Downstream:** catalog loaders and graph ingesters that only process:
  - Assets that passed FAIR+CARE, or  
  - Assets tagged with explicit governance overrides (documented in the registry).

---

## 🗺️ Diagrams

### High-Level FAIR+CARE Validation Flow

~~~mermaid
flowchart LR
    A["PR / Push / Schedule"] --> B["Data-Contract · FAIR+CARE · PII Validation"]
    B --> C{"Compliant?"}
    C -->|Yes| D["Provenance Trace · Reports"]
    C -->|No| E["Quarantine → abandonment_candidates · Registry Entry"]
    D --> F["Upload Artifacts · Emit Telemetry"]
    E --> F
    F --> G["Governance Ledger · Council Review"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

- Each FAIR+CARE validation run is a potential **Story Node**, e.g.:
  - `urn:kfm:story-node:data:faircare:<run_id>`
- Story Node content may summarize:
  - Number of datasets scanned and their types.  
  - FAIR+CARE violations found and categories.  
  - Assets quarantined and awaiting council review.  
  - Links to provenance traces and DCAT/STAC entries.

**Focus Mode** MAY:

- Summarize recent FAIR+CARE activity for a dataset, collection, or time window.  
- Show which workflows blocked a release due to ethics or sovereignty issues.  
- Surface the abandonment registry entries associated with a given dataset.

**Focus Mode MUST NOT**:

- Invent or alter FAIR+CARE decisions; it may only restate recorded outcomes.  
- Override governance or sovereignty policies defined in referenced standards.

---

## 🧪 Validation & CI/CD

### 1. Conceptual Workflow YAML

~~~yaml
name: "FAIR+CARE Validate (Governed)"

on:
  pull_request:
    paths: ["data/**", "docs/**", "schemas/**"]
  push:
    branches: ["main", "release/**"]
    paths: ["data/**", "docs/**", "schemas/**"]
  schedule:
    - cron: "0 3 * * *"

permissions:
  contents: read
  id-token: write

concurrency:
  group: faircare-validate-${{ github.ref }}
  cancel-in-progress: true

jobs:
  validate:
    runs-on: ubuntu-22.04
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install validators
        run: |
          pip install -r requirements.txt
          pip install jsonschema jq yq

      - name: Validate data contracts (schema)
        run: |
          python scripts/validate_contract.py \
            --root data/ \
            --contract docs/contracts/data-contract-v3.json \
            --out reports/faircare/contract_summary.json

      - name: FAIR+CARE audit (ethics & governance)
        run: |
          python scripts/faircare_audit.py \
            --input data/ \
            --standards docs/standards/faircare/faircare.yaml \
            --out reports/faircare/faircare_summary.json

      - name: PII & sensitive content scan
        run: |
          python scripts/pii_scan.py \
            --input data/ \
            --rules docs/standards/pii_rules.yaml \
            --out reports/faircare/pii_scan.json

      - name: Flag noncompliant → abandonment candidates
        run: |
          python scripts/abandonment_triage.py \
            --violations reports/faircare/faircare_summary.json \
            --pii reports/faircare/pii_scan.json \
            --staging data/work/staging/tabular \
            --quarantine data/work/staging/tabular/abandonment_candidates \
            --registry data/work/staging/tabular/abandonment_candidates/abandonment_registry.json

      - name: Generate provenance trace
        run: |
          python scripts/make_provenance.py \
            --root data/ \
            --out reports/faircare/provenance_trace.json

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: faircare_reports
          path: |
            reports/faircare/**
            data/work/staging/tabular/abandonment_candidates/abandonment_registry.json

      - name: Emit telemetry
        run: |
          python scripts/emit_telemetry.py \
            --kind faircare \
            --summary  reports/faircare/faircare_summary.json \
            --pii      reports/faircare/pii_scan.json \
            --contract reports/faircare/contract_summary.json \
            --out faircare_telemetry.json

      - name: Append telemetry to unified log
        run: |
          python scripts/merge_telemetry.py \
            --in  faircare_telemetry.json \
            --dest releases/v11.2.6/faircare-validate-telemetry.json
~~~

### 2. Quality Gates (Normative)

The job MUST fail if:

- Data‑contract validation detects critical schema violations.  
- FAIR+CARE audit reports blocking issues (e.g., unauthorized use, missing consent, misaligned CARE tags).  
- PII scan finds unmasked sensitive data that should be masked or removed.  
- Abandonment triage fails to write a consistent `abandonment_registry.json`.  
- Provenance trace generation fails or is incomplete.

---

## 📦 Data & Metadata

### 1. Inputs

- `data/**` — Tabular, spatial, and metadata files under review.  
- `docs/**` — Associated documentation (for FAIR+CARE contextual checks).  
- `schemas/**` — JSON/SHACL schemas referenced by data contracts.

### 2. Artifacts

Key artifacts per run:

- `reports/faircare/contract_summary.json` — Data‑contract conformance summary.  
- `reports/faircare/faircare_summary.json` — FAIR+CARE audit results.  
- `reports/faircare/pii_scan.json` — PII and sensitive content findings.  
- `reports/faircare/provenance_trace.json` — DCAT/PROV‑style lineage.  
- `data/work/staging/tabular/abandonment_candidates/abandonment_registry.json` — Registry of quarantined assets.

### 3. Telemetry Records

Telemetry entries are appended to `releases/v11.2.6/faircare-validate-telemetry.json`, e.g.:

~~~json
{
  "workflow": "faircare-validate",
  "run_id": "faircare_2025-12-06T03-00-00Z",
  "datasets_scanned": 152,
  "violations_found": 7,
  "quarantined": 3,
  "frontmatter_failures": 1,
  "faircare_policy_version": "faircare@2025.4",
  "workflow_duration_sec": 740,
  "energy_wh": 96,
  "carbon_gco2e": 0.021,
  "timestamp": "2025-12-06T03:12:20Z"
}
~~~

These records are later merged by the telemetry export workflow into the global `focus-telemetry.json` ledger.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. PROV‑O

For each run:

- **Entities**
  - `ex:DatasetVersion_<id>` — Individual datasets under validation.  
  - `ex:FaircareReport_<run_id>` — Combined FAIR+CARE/PII/contract summary.  
  - `ex:AbandonmentRegistry_<run_id>` — Snapshot of the abandonment registry.
- **Activity**
  - `ex:FaircareValidateRun_<run_id>` — This workflow execution.  
- **Agents**
  - `ex:KFM_CI_Bot` (`prov:SoftwareAgent`).  
  - `ex:FaircareCouncil` (`prov:Organization`).

Relations:

- `ex:FaircareValidateRun_<run_id> prov:used ex:DatasetVersion_<id>`.  
- `ex:FaircareReport_<run_id> prov:wasGeneratedBy ex:FaircareValidateRun_<run_id>`.  
- `ex:FaircareValidateRun_<run_id> prov:wasAssociatedWith ex:KFM_CI_Bot`.  
- `ex:AbandonmentRegistry_<run_id> prov:wasGeneratedBy ex:FaircareValidateRun_<run_id>`.

### 2. DCAT

- The FAIR+CARE reports can be grouped as a `dcat:Dataset`:
  - `dct:title`: "KFM FAIR+CARE Validation Reports".  
  - `dct:description`: "Automated ethics and governance validation results for KFM datasets and documentation."  
  - `dct:identifier`: stable dataset ID or per‑run IDs for a dataset series.  
- `dcat:Distribution` entries:
  - `faircare_summary.json` (`application/json`)  
  - `pii_scan.json`  
  - `contract_summary.json`  
  - `provenance_trace.json`

### 3. STAC

- Optionally, FAIR+CARE runs can be exposed in a `kfm-faircare` STAC Collection:
  - `id`: `faircare-<run_id>`  
  - `properties.datetime`: run completion time.  
  - `assets`:
    - `faircare-summary` → `faircare_summary.json`  
    - `pii-scan` → `pii_scan.json`  
    - `contract-summary` → `contract_summary.json`
- As governance outputs are non‑spatial, `geometry` may be `null` and `bbox` omitted.

---

## 🧱 Architecture

- **Workflow orchestration** lives in `.github/workflows/faircare-validate.yml`.  
- **Validation logic** is implemented as reusable CLIs in `scripts/` (or `tools/validation/`), not embedded directly in YAML.  
- **Reports & telemetry** are written to predictable locations under `reports/` and `releases/` so cataloging and graph loaders can ingest them.

Design principles:

- **Config‑driven:** Rules (e.g., PII patterns, FAIR+CARE criteria, contract definitions) live in versioned YAML/JSON in `docs/standards/` or `schemas/`.  
- **Deterministic:** Given the same commit and configs, the workflow produces identical reports.  
- **Composable:** Other workflows (e.g., `ai-train.yml`) can depend on FAIR+CARE status before proceeding.

---

## ⚖ FAIR+CARE & Governance

### 1. FAIR / CARE Rule Set

**FAIR**

- *F1 (Findable):* Required identifiers, STAC/DCAT presence, and stable IDs.  
- *A1 (Accessible):* Clear licenses, role‑based access, resolvable links.  
- *I1 (Interoperable):* Valid JSON/GeoJSON; DCAT vocab; CRS & units declared.  
- *R1 (Reusable):* Provenance, versioning, checksums; data‑contract fields filled.

**CARE**

- *Collective Benefit:* Ensures datasets contribute to community goals, not extractive use.  
- *Authority to Control:* `care_tag` and sovereignty rules enforced; consent and opt‑out honored.  
- *Responsibility:* PII scan and redaction; risk flags for sensitive content.  
- *Ethics:* Cultural sensitivity checks (e.g., Indigenous data, minors, health data).

**Failure policy (normative):**

- Non‑compliant assets are:
  - Quarantined under `abandonment_candidates/`.  
  - Registered in `abandonment_registry.json` with ID, checksum, path, reason, and reviewer (if any).  
  - Prevented from entering public catalogs or the knowledge graph until remediated or explicitly approved by the FAIR+CARE Council.

### 2. Abandonment Candidates Integration

The abandonment pipeline:

1. **Detection** — FAIR+CARE and PII scans identify violating assets.  
2. **Quarantine** — Files moved into `data/work/staging/tabular/abandonment_candidates/`.  
3. **Registry** — `abandonment_registry.json` updated with:
   - `asset_id`, `checksum`, `path`, `reason`, `timestamp`, `status`.  
4. **Reporting** — Entries are referenced in FAIR+CARE reports and provenance traces.  
5. **Governance** — FAIR+CARE Council reviews and decides:
   - `released`, `remediated`, or `retired`.

Telemetry events (e.g., `dataset-flagged`, `dataset-remediated`, `dataset-retired`) can be emitted for governance dashboards.

---

## 🕰️ Version History

| Version    | Date       | Author        | Summary                                                                                                                                               |
|-----------:|------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **v11.2.6** | 2025-12-11 | `@kfm-gov`   | Aligned to KFM v11.2.6; updated release & telemetry paths, emoji directory layout, and footer/navigation profile; preserved FAIR+CARE workflow semantics and contracts. |
| v11.2.4   | 2025-12-06 | `@kfm-gov`   | Updated to align with KFM‑MDP v11.2.4; expanded front‑matter; added STAC/DCAT/PROV alignment and Story Node hooks; introduced dedicated `faircare-validate-telemetry.json`. |
| v10.2.4   | 2025-11-12 | `@kfm-gov`   | Telemetry schema v3; artifact paths unified; clarified schedule behavior and abandonment registry semantics.                                         |
| v10.1.0   | 2025-11-10 | `@kfm-gov`   | Added contract summary emission and telemetry v2 adoption.                                                                                            |
| v9.9.0    | 2025-11-08 | `@kfm-gov`   | Initial governed FAIR+CARE validation workflow documentation; introduced quarantine registry, PII scan, provenance export, and telemetry merge.      |

---

<div align="center">

⚖️ **Kansas Frontier Matrix — FAIR+CARE Validation Workflow (`faircare-validate.yml`) · v11.2.6**  
Ethical Automation · FAIR+CARE Governance · Sustainable CI/CD  

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/Data-FAIR%2BCARE-gold" />
<img src="https://img.shields.io/badge/Workflow-faircare_validate_v11.2.6-informational" />

[⬅ Back to Workflows Index](./README.md) ·  
[📘 Docs Root](../README.md) ·  
[📚 Glossary](../glossary.md) ·  
[📐 Markdown Protocol (KFM-MDP v11.2.4)](../standards/kfm_markdown_protocol_v11.2.4.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) ·  
[🤝 FAIR+CARE Guide](../standards/faircare/FAIRCARE-GUIDE.md) ·  
[🪶 Indigenous Data Protection](../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

  
© 2025 Kansas Frontier Matrix — CC-BY 4.0 for this document  
MCP-DL v6.3 · KFM-MDP v11.2.4 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

</div>
