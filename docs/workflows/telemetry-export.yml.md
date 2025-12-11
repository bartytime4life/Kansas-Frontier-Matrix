---
title: "📈 Telemetry Export Workflow — `telemetry-export.yml` (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/workflows/telemetry-export.yml.md"

version: "v11.2.4"
last_updated: "2025-12-06"
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
telemetry_schema: "schemas/telemetry/workflows/telemetry-export-v11.2.4.json"
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
    - ".github/workflows/telemetry-export.yml"
    - "reports/**"
    - "releases/**"
    - "schemas/telemetry/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "General (summarized metrics; auto-mask rules apply)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Telemetry Export Workflow v12"

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
  - "docs/workflows/telemetry-export.yml.md@v10.2.4"
  - "docs/workflows/telemetry-export.yml.md@v10.1.0"
  - "docs/workflows/telemetry-export.yml.md@v9.9.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:workflows:telemetry-export-yml:v11.2.4"
semantic_document_id: "kfm-workflow-telemetry-export-yml-v11.2.4"
event_source_id: "ledger:kfm:doc:workflows:telemetry-export-yml:v11.2.4"
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
  workflow: ".github/workflows/telemetry-export.yml"
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

# 📈 **Telemetry Export Workflow — `telemetry-export.yml`**  
`docs/workflows/telemetry-export.yml.md`

**Purpose**  
Aggregate and normalize **build, validation, and governance metrics** from all CI jobs (docs, STAC/DCAT, FAIR+CARE, AI training, security, web builds) into a single, FAIR+CARE‑aligned telemetry ledger: **`releases/<version>/focus-telemetry.json`**.  
Provide a **machine-readable, auditable** source for sustainability dashboards, governance reviews, and certification under **MCP‑DL v6.3** and **Diamond⁹ Ω / Crown∞Ω**.

<img src="https://img.shields.io/badge/Docs·MCP-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Status-Automated-brightgreen" />

</div>

---

## 📘 Overview

### 1. Workflow Intent

`telemetry-export.yml` consolidates metrics emitted by other governed workflows, including:

- **Documentation** — `docs-lint.yml` (front-matter, links, mermaid guardrails).  
- **Governance** — `faircare-validate.yml` (FAIR+CARE, PII, abandonment registry).  
- **Catalog** — `stac-validate.yml` (STAC/DCAT + asset checksums).  
- **Schemas** — `schema-lint.yml` (JSON/SHACL/schema health).  
- **AI** — `ai-train.yml`, `ai-explainability.yml` (training/eval, drift, explainability, SBOM, SLSA).  
- **Security** — `security-supply-chain.yml` (SBOM, vulns, secrets, attestations).  
- **Other builds** — web/pipelines build time, size, cache hits, test results.

All inputs are normalized to a **stable telemetry schema** and merged into **`releases/v11.2.4/focus-telemetry.json`** for longitudinal analysis and governance.

### 2. Role in the KFM Pipeline

Within:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

this workflow:

- Acts as the **telemetry aggregator** and **governance ledger bridge**.  
- Provides a unified event stream that other systems (dashboards, audits, Story Nodes) consume.  
- Supplies **energy, carbon, and quality metrics** required for sustainability and FAIR+CARE reporting.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 workflows/
    📄 README.md                               — CI/CD & governance workflows index
    📄 telemetry-export.yml.md                 — ← This telemetry export workflow spec

📁 .github/
└── 📁 workflows/
    📄 telemetry-export.yml                    — GitHub Actions workflow (telemetry aggregator)

📁 schemas/
└── 📁 telemetry/
    📄 docs-index-v3.json                      — Unified telemetry index schema
    📄 workflows/docs-lint-v3.json             — Per-workflow telemetry schema (docs-lint)
    📄 workflows/faircare-validate-v3.json     — Per-workflow telemetry schema (faircare)
    📄 workflows/stac-validate-v3.json         — Per-workflow telemetry schema (STAC/DCAT)
    📄 workflows/ai-train-v3.json              — Per-workflow telemetry schema (AI train)
    📄 workflows/telemetry-export-v11.2.4.json — This workflow's schema & contract

📁 scripts/
└── 📁 telemetry/
    📄 pull_artifact.py                        — Downloads artifacts from upstream runs
    📄 normalize_docs_lint.py                  — Maps docs-lint output → telemetry events
    📄 normalize_faircare.py                   — Maps faircare-validate output → events
    📄 normalize_stac.py                       — Maps stac-validate output → events
    📄 normalize_ai.py                         — Maps ai-train output → events
    📄 normalize_security.py                   — Maps security-supply-chain output → events
    📄 merge_telemetry.py                      — Merges multiple event streams → ledger
    📄 summarize_telemetry.py                  — Creates summary JSON/MD for dashboards

📁 reports/
└── 📁 telemetry/
    📄 summary.json                            — Aggregated statistics & trends
    📄 summary.md                              — Human-readable summary for PRs / governance

📁 releases/
└── 📁 v11.2.4/
    📄 focus-telemetry.json                    — Unified telemetry ledger for KFM v11.2.4
    📄 sbom.spdx.json                          — SBOM for telemetry toolchain
    📄 manifest.zip                            — Release manifest (hashes, configs, versions)
~~~

---

## 🧭 Context

### 1. Triggers & Scope

| Trigger             | Paths / Workflows                             | Notes                                      |
|--------------------:|-----------------------------------------------|--------------------------------------------|
| `workflow_run`      | docs-lint, faircare-validate, stac-validate, ai-train, ai-explainability, security-supply-chain | Primary mode; runs after these complete |
| `schedule`          | hourly                                        | Roll-up of last N runs; trend refresh      |
| `workflow_dispatch` | —                                             | Manual backfill or emergency re-aggregation|

**Upstream requirement:** Each contributing workflow **must** emit a JSON summary conforming to its telemetry schema and upload it as an artifact.

### 2. Relationship to Other Workflows

- **Upstream**: all metric‑emitting workflows (docs, data, AI, security, builds).  
- **Peers**: none — this is the **aggregation root**.  
- **Downstream**:
  - Governance dashboards and sustainability reports.  
  - Story Nodes that summarize infrastructure health.  
  - External certifications (Diamond⁹ Ω / Crown∞Ω) that reference the telemetry ledger.

---

## 🗺️ Diagrams

### 1. High-Level Telemetry Export Flow

~~~mermaid
flowchart LR
  A["Upstream Workflows (docs, data, AI, security)"] --> B["Pull Artifacts & Summaries"]
  B --> C["Normalize to Per-Workflow Schemas (v3)"]
  C --> D["Merge Streams → focus-telemetry.json"]
  D --> E["Validate Unified Telemetry (docs-index-v3)"]
  E --> F["Export Summaries & Attach Artifacts"]
  F --> G["Governance Dashboards & Sustainability Reports"]
~~~

### 2. Telemetry Lifecycle Timeline

~~~mermaid
timeline
    title Telemetry Export — Run Lifecycle
    section Ingestion
      T0 : Upstream workflows finish & upload summaries
      T1 : Telemetry Export pulls artifacts
    section Normalization & Merge
      T2 : Per-workflow normalization → events
      T3 : Merge streams → focus-telemetry.json
    section Validation & Reporting
      T4 : Schema validation & quality checks
      T5 : Summaries generated & published
      T6 : Dashboards / governance views updated
~~~

---

## 🧠 Story Node & Focus Mode Integration

### 1. Story Nodes

Telemetry export runs can be captured as **infrastructure Story Nodes**, for example:

- `urn:kfm:story-node:infra:telemetry-export:<run_id>`  
  - Describes how many events were merged, which workflows contributed, and any anomalies.

- `urn:kfm:story-node:infra:telemetry-trend:<period>`  
  - Summarizes trends in energy use, failure rates, and governance metrics over a time window.

Each node links to:

- `releases/v11.2.4/focus-telemetry.json` (or a time‑bounded slice).  
- `reports/telemetry/summary.json` and `summary.md`.  
- Specific workflow docs (docs-lint, faircare-validate, etc.) as needed.

### 2. Focus Mode

Focus Mode may:

- Answer questions like “How healthy is CI right now?” or “What is the energy footprint over the last week?” using telemetry.  
- Provide high‑level summaries of metrics per workflow, branch, or service.  
- Highlight regressions or improvements over time.

Focus Mode must not:

- Fabricate telemetry — it may only summarize existing records.  
- Mask or delete anomalies; it may annotate them but not override them.

---

## 🧪 Validation & CI/CD

### 1. Conceptual Workflow YAML

~~~yaml
name: "Telemetry Export (Governed)"

on:
  workflow_run:
    workflows:
      - "Docs Lint (Governed)"
      - "FAIR+CARE Validate (Governed)"
      - "STAC/DCAT Validate (Governed)"
      - "AI Train (Governed)"
      - "AI Explainability (Governed)"
      - "Supply-Chain Security (Governed)"
    types: [completed]
  schedule:
    - cron: "0 * * * *" # hourly aggregation
  workflow_dispatch: {}

permissions:
  contents: write
  id-token: write

concurrency:
  group: telemetry-export-${{ github.ref }}
  cancel-in-progress: true

jobs:
  export:
    runs-on: ubuntu-22.04
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install tooling
        run: |
          pip install jsonschema jq
          pip install -r requirements.txt || true

      - name: Collect inputs
        run: |
          mkdir -p .telemetry/in .telemetry/out releases/v11.2.4
          python scripts/telemetry/pull_artifact.py --name docs_lint_reports             --out .telemetry/in/docs      || true
          python scripts/telemetry/pull_artifact.py --name faircare_reports              --out .telemetry/in/faircare  || true
          python scripts/telemetry/pull_artifact.py --name stac_validation_reports       --out .telemetry/in/stac      || true
          python scripts/telemetry/pull_artifact.py --name schema_lint_reports           --out .telemetry/in/schema    || true
          python scripts/telemetry/pull_artifact.py --name ai_*_artifacts                --out .telemetry/in/ai        || true
          python scripts/telemetry/pull_artifact.py --name security_supply_chain_reports --out .telemetry/in/security || true

      - name: Normalize to telemetry schemas
        run: |
          python scripts/telemetry/normalize_docs_lint.py \
            --in .telemetry/in/docs \
            --schema schemas/telemetry/workflows/docs-lint-v3.json \
            --out .telemetry/out/docs.json || echo "{}" > .telemetry/out/docs.json

          python scripts/telemetry/normalize_faircare.py \
            --in .telemetry/in/faircare \
            --schema schemas/telemetry/workflows/faircare-validate-v3.json \
            --out .telemetry/out/faircare.json || echo "{}" > .telemetry/out/faircare.json

          python scripts/telemetry/normalize_stac.py \
            --in .telemetry/in/stac \
            --schema schemas/telemetry/workflows/stac-validate-v3.json \
            --out .telemetry/out/stac.json || echo "{}" > .telemetry/out/stac.json

          python scripts/telemetry/normalize_schema.py \
            --in .telemetry/in/schema \
            --schema schemas/telemetry/workflows/schema-lint-v3.json \
            --out .telemetry/out/schema.json || echo "{}" > .telemetry/out/schema.json

          python scripts/telemetry/normalize_ai.py \
            --in .telemetry/in/ai \
            --schema schemas/telemetry/workflows/ai-train-v3.json \
            --out .telemetry/out/ai.json || echo "{}" > .telemetry/out/ai.json

          python scripts/telemetry/normalize_security.py \
            --in .telemetry/in/security \
            --schema schemas/telemetry/workflows/security-supply-chain-v3.json \
            --out .telemetry/out/security.json || echo "{}" > .telemetry/out/security.json

      - name: Merge streams → focus-telemetry.json
        run: |
          python scripts/telemetry/merge_telemetry.py \
            --in  .telemetry/out/*.json \
            --dest releases/v11.2.4/focus-telemetry.json

      - name: Validate unified telemetry
        run: |
          python - <<'PY'
          import json
          from jsonschema import Draft202012Validator
          with open("schemas/telemetry/docs-index-v3.json") as f: schema = json.load(f)
          with open("releases/v11.2.4/focus-telemetry.json") as f: data = json.load(f)
          Draft202012Validator(schema).validate(data)
          print("Unified telemetry valid; events:", len(data.get("events", [])))
          PY

      - name: Export quick summaries
        run: |
          mkdir -p reports/telemetry
          python scripts/telemetry/summarize_telemetry.py \
            --in  releases/v11.2.4/focus-telemetry.json \
            --out reports/telemetry/summary.json \
            --md  reports/telemetry/summary.md

      - name: Attach artifacts
        uses: actions/upload-artifact@v4
        with:
          name: telemetry_ledger
          path: |
            releases/v11.2.4/focus-telemetry.json
            reports/telemetry/**
~~~

### 2. Quality Gates

The job should:

- **Fail** if:
  - Any per‑workflow normalized payload fails its schema validation.  
  - The unified ledger fails validation against `docs-index-v3.json`.  
  - The ledger is unexpectedly empty for the time window when upstream workflows have run.  

- **Warn** (non‑fatal) if:
  - Some upstream workflows had no artifacts for the time window.  
  - Optional metrics (e.g., energy estimates from legacy runs) are missing.

---

## 📦 Data & Metadata

### 1. Input Contracts

Each upstream workflow must provide:

- A **summary JSON** conforming to its telemetry schema.  
- A **consistent artifact name**, e.g.:
  - `docs_lint_reports` → `lint_summary.json`  
  - `faircare_reports` → `faircare_summary.json`  
  - `stac_validation_reports` → `stac_validation.json`  
  - `ai_<model>_artifacts` → `metrics.json`, `drift.json`, `explainability.json`  
  - `security_supply_chain_reports` → `supply_chain_security_summary.json`  

The exporter uses those contracts plus `schemas/telemetry/workflows/*.json` to shape events.

### 2. Unified Telemetry Schema (Core Fields)

Core event fields in `focus-telemetry.json`:

| Field          | Type    | Description                                                  |
|----------------|---------|--------------------------------------------------------------|
| `event_id`     | string  | UUIDv4 per record                                           |
| `event_type`   | enum    | `docs_lint` \| `faircare` \| `stac_validate` \| `schema_lint` \| `ai_train` \| `security_supply_chain` \| `build` |
| `timestamp`    | string  | ISO‑8601 UTC timestamp                                      |
| `workflow`     | string  | GitHub workflow name                                        |
| `run_id`       | string  | CI run identifier                                           |
| `branch`       | string  | Git ref / release tag                                       |
| `duration_sec` | number  | Total workflow runtime                                      |
| `energy_wh`    | number  | Estimated energy consumption                                |
| `carbon_gco2e` | number  | CO₂eq estimate                                              |
| `status`       | enum    | `success` \| `warning` \| `failure`                         |
| `payload`      | object  | Workflow‑specific, validated against its own schema         |

This ledger is append‑only and versioned with releases (`v11.2.4`).

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. DCAT

Telemetry can be represented as a DCAT Dataset:

- `dct:title`: "KFM CI/CD Telemetry Ledger (v11.2.4)".  
- `dct:description`: "Aggregated workflow telemetry for CI/CD, governance, and sustainability metrics."  
- `dct:identifier`: stable ID per major version.  
- `dct:temporal`: coverage of the telemetry window (e.g., release cycle).

Distributions:

- `focus-telemetry.json` (`application/json`).  
- `summary.json` / `summary.md`.  

### 2. STAC

If telemetry is indexed in STAC:

- Collection: `kfm-telemetry`.  
- Items per period (e.g., day / week / release):

  - `id`: `telemetry-v11.2.4-<period>`.  
  - `properties.datetime`: end of aggregation period.  
  - `assets.telemetry-json`: `focus-telemetry.json` or a time slice.

Non‑spatial; `geometry: null` is acceptable under KFM‑STAC profile.

### 3. PROV-O

Per run:

- **Entity**: `ex:TelemetryLedger_<run_id>` (or per‑period entity).  
- **Activity**: `ex:TelemetryExportRun_<run_id>`.  
- **Agent**: `ex:KFM_CI_Bot`.

Relations:

- `ex:TelemetryExportRun_<run_id> prov:used` → upstream summary entities.  
- `ex:TelemetryLedger_<run_id> prov:wasGeneratedBy ex:TelemetryExportRun_<run_id>`.  
- `ex:TelemetryExportRun_<run_id> prov:wasAssociatedWith ex:KFM_CI_Bot`.

---

## 🧱 Architecture

### 1. Module Boundaries

- **Workflow orchestration**: `.github/workflows/telemetry-export.yml`.  
- **Normalization & merge logic**: `scripts/telemetry/*.py`.  
- **Schemas**: `schemas/telemetry/**`.  
- **Reports & summaries**: `reports/telemetry/**`.  
- **Unified ledger & related artifacts**:  
  - `releases/v11.2.4/focus-telemetry.json`  
  - `releases/v11.2.4/sbom.spdx.json`  
  - `releases/v11.2.4/manifest.zip`

### 2. Determinism & Reproducibility

- For a given set of upstream artifacts and configuration, normalization and merge steps are **deterministic**.  
- Tool versions (Python, `jsonschema`, etc.) are pinned in `requirements.txt` and captured in `sbom.spdx.json`.  
- Schema versions are explicit (`workflows/*-v3.json`, `docs-index-v3.json`).

---

## ⚖ FAIR+CARE & Governance

### 1. FAIR

| Principle      | Implementation                                              |
|----------------|-------------------------------------------------------------|
| **Findable**   | Telemetry stored under `releases/v11.2.4/` and indexed     |
| **Accessible** | JSON + Markdown summaries; internal dashboards             |
| **Interoperable** | JSON Schema, DCAT, PROV mapping                         |
| **Reusable**   | Versioned schemas, events, and aggregation scripts         |

### 2. CARE

- **Collective Benefit**: Telemetry enables better sustainability and reliability decisions across KFM.  
- **Authority to Control**: Governance can limit exposure of internal telemetry if needed.  
- **Responsibility**: Metrics highlight bottlenecks and waste, encouraging optimization.  
- **Ethics**: Telemetry focuses on systems, not individuals; avoid per‑person metrics.

Governance bodies use telemetry evidence in regular reviews and certification processes.

---

## 🕰️ Version History

| Version    | Date       | Author          | Summary                                                                                                                       |
|-----------:|------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | `@kfm-devops`   | Aligned with KFM-MDP v11.2.4; expanded front-matter; added directory layout, Story Node hooks, STAC/DCAT/PROV alignment, and dedicated telemetry schema reference. |
| v10.2.4   | 2025-11-12 | `@kfm-devops`   | Upgraded to telemetry schema v3; unified artifact paths; strengthened validation of upstream summary schemas.                |
| v10.1.0   | 2025-11-10 | `@kfm-devops`   | Added hourly aggregation, artifact uploader v4, telemetry-export v2.                                                          |
| v9.9.0    | 2025-11-08 | `@kfm-devops`   | Initial governed telemetry exporter with schema validation and sustainability metrics.                                       |

---

<div align="center">

📈 **Telemetry Export Workflow — `telemetry-export.yml` (v11.2.4)**  
Evidence-Driven Governance · FAIR+CARE Telemetry · Sustainable CI/CD  

[⬅ Back to Workflows Index](./README.md) ·  
[📘 Docs Root](../README.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>