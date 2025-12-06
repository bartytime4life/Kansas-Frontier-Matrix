---
title: "🗂️ Kansas Frontier Matrix — STAC/DCAT Validation Workflow (`stac-validate.yml`) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/workflows/stac-validate.yml.md"

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
telemetry_ref: "releases/v11.2.4/stac-validate-telemetry.json"
telemetry_schema: "schemas/telemetry/workflows/stac-validate-v11.2.4.json"
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
    - ".github/workflows/stac-validate.yml"
    - "data/stac/**"
    - "schemas/**"
    - "docs/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "General (catalog metadata; sensitivity via care_tag)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by STAC/DCAT Validation Workflow v12"

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
  - "docs/workflows/stac-validate.yml.md@v10.2.4"
  - "docs/workflows/stac-validate.yml.md@v10.1.0"
  - "docs/workflows/stac-validate.yml.md@v9.9.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:workflows:stac-validate-yml:v11.2.4"
semantic_document_id: "kfm-workflow-stac-validate-yml-v11.2.4"
event_source_id: "ledger:kfm:doc:workflows:stac-validate-yml:v11.2.4"
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
  workflow: ".github/workflows/stac-validate.yml"
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

# 🗂️ **STAC/DCAT Validation Workflow — `stac-validate.yml`**  
`docs/workflows/stac-validate.yml.md`

**Purpose**  
Define the **GitHub Actions** workflow that validates all **STAC 1.0** Catalogs/Collections/Items and their **DCAT 3.0** mirrors, checks asset availability & checksums, enforces **FAIR+CARE**/contract fields, and publishes machine-readable validation reports with **telemetry v3** for Diamond⁹ / Crown∞Ω certification.

<img src="https://img.shields.io/badge/Docs·MCP-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io-badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Status-Automated-brightgreen" />

</div>

---

## 📘 Overview

### 1. Catalog Gate for KFM

`stac-validate.yml` is the **catalog gate** for the Kansas Frontier Matrix. It guarantees that everything under `data/stac/**`:

- ✅ Conforms to **STAC 1.0.0** (core + extensions: `proj`, `raster`, `eo`, `label`, `version`, `checksum`).  
- ✅ Mirrors correctly into **DCAT 3.0** where required (see data architecture docs).  
- ✅ Provides **dereferenceable assets** (HTTP / PMTiles / OGC endpoints) with **verifiable checksums**.  
- ✅ Satisfies **FAIR+CARE** and **data-contract** required metadata (license, temporal extent, bbox, provider, `care_tag`).  
- ✅ Emits **validation reports** and **telemetry** (counts, error types, energy/duration) for governance.

Within the KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

this workflow protects the **catalog layer**, ensuring downstream components can trust KFM STAC/DCAT metadata.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 workflows/
    📄 README.md                               — CI/CD & governance workflows index
    📄 stac-validate.yml.md                    — ← This STAC/DCAT validation workflow spec

📁 .github/
└── 📁 workflows/
    📄 stac-validate.yml                       — GitHub Actions workflow (STAC/DCAT validation)

📁 data/
└── 📁 stac/
    📁 catalogs/                               — Root catalogs (if used)
    📁 collections/                            — STAC Collections
    📁 items/                                  — STAC Items (flat or nested by collection)

📁 schemas/
├── 📁 stac/
│   📄 kfm-stac-profile.json                   — KFM-STAC profile & required fields
│   📄 kfm-stac-extensions.json                — Extension configuration/requirements
├── 📁 dcat/
│   📄 dcat-ap-3.0.json                        — DCAT 3.0 / KFM-DCAT profile
└── 📁 json/
    📄 telemetry/workflows/stac-validate-v11.2.4.json  — Telemetry schema for this workflow

📁 scripts/
└── 📁 stac/
    📄 stac_contract_check.py                  — FAIR+CARE + contract field validation
    📄 stac_asset_audit.py                     — Asset reachability & checksum audit
    📄 dcat_validate.py                        — DCAT mirror validation
    📄 stac_summarize.py                       — Aggregates validation results → summary

📁 reports/
└── 📁 self-validation/
    📁 stac/
        📄 structure.json                      — PySTAC structural validation
        📄 validator.log                       — Raw stac-validator output
        📄 contract_faircare.json              — FAIR+CARE + contract field results
        📄 assets_audit.json                   — Asset + checksum audit
        📄 dcat_validation.json                — DCAT parity results
        📄 stac_validation.json                — Canonical summary (JSON)
        📄 stac_summary.md                     — Human-readable summary (PR view)

📁 releases/
└── 📁 v11.2.4/
    📄 stac-validate-telemetry.json            — Telemetry for this workflow
    📄 sbom.spdx.json                          — SBOM for tools used in validation
    📄 manifest.zip                            — Release manifest (hashes, configuration)
~~~

---

## 🧭 Context

### 1. Triggers & Scope

| Trigger            | Paths                          | Notes                                  |
|-------------------:|--------------------------------|----------------------------------------|
| `pull_request`     | `data/stac/**`, `schemas/**`, `docs/**` | Blocks merge on failure        |
| `push` (protected) | `data/stac/**`                 | Required for releases                  |
| `schedule`         | nightly                        | Catalog regression & link‑rot checks   |

Ignored:

- Large binary assets (e.g., `*.tif`, `*.cog.tif`, `*.zip`) are not uploaded as artifacts, but are still checked via HTTP **HEAD** / Range requests where applicable.

### 2. Relationship to Other Workflows

- **Upstream**: ETL pipelines that emit STAC Items/Collections.  
- **Peers**:
  - `faircare-validate.yml` — ethics and data governance validation.  
  - `schema-lint.yml` — JSON/SHACL schema validation.  
- **Downstream**:
  - Graph loaders that trust STAC IDs, extents, and contract fields.  
  - Frontend layers (MapLibre/Cesium) that rely on stable asset URLs and metadata.

---

## 🗺️ Diagrams

### 1. High-Level Validation Flow

~~~mermaid
flowchart LR
  A["PR / Push / Schedule"] --> B["PySTAC / stac-validator"]
  B --> C["Contract + FAIR+CARE Audit"]
  C --> D["Asset & Link Checks"]
  D --> E["DCAT Mirror Validation"]
  E --> F["Reports + Telemetry"]
  F --> G["Governance Ledger / Publish Gate"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### 1. Story Nodes

This workflow can produce infrastructure‑style Story Nodes, for example:

- `urn:kfm:story-node:infra:stac-validate:<run_id>`  
  - Explains which STAC Collections/Items were validated, how many warnings/errors, and any notable changes.  

- `urn:kfm:story-node:data:collection-health:<collection_id>`  
  - Describes the validation history and health of a specific Collection.

Story Nodes reference:

- `reports/self-validation/stac/stac_validation.json` for machine‑readable status.  
- Telemetry entries in `releases/v11.2.4/stac-validate-telemetry.json`.

### 2. Focus Mode

Focus Mode may:

- Summarize **catalog health** (e.g., “All Collections valid as of date X”).  
- Highlight **Items or Collections with repeated issues** (e.g., missing checksums).  
- Provide **links to specific validation reports** for deeper inspection.

It must not:

- Declare a Collection “valid” without corresponding validation results.  
- Hide failures or override FAIR+CARE or contract rules.

---

## 🧪 Validation & CI/CD

### 1. Conceptual Workflow (YAML)

~~~yaml
name: "STAC/DCAT Validate (Governed)"

on:
  pull_request:
    paths: ["data/stac/**", "schemas/**", "docs/**"]
  push:
    branches: ["main", "release/**"]
    paths: ["data/stac/**"]
  schedule:
    - cron: "15 2 * * *"

permissions:
  contents: read

concurrency:
  group: stac-validate-${{ github.ref }}
  cancel-in-progress: true

jobs:
  validate:
    runs-on: ubuntu-22.04
    timeout-minutes: 45
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install validators
        run: |
          pip install \
            pystac[validator]==1.10.1 \
            stac-validator==3.3.0 \
            stactools==0.5.5 \
            jsonschema==4.23.0 \
            rfc3986==2.0.0 \
            requests==2.32.3 \
            lxml==5.* \
            kfm-stac-tools[checksums,links]
          sudo apt-get update && sudo apt-get install -y jq moreutils

      - name: Validate STAC structure (catalog/collection/item)
        run: |
          mkdir -p reports/self-validation/stac
          python -m pystac.validate data/stac --recursive --ignore-links \
            --output-format json > reports/self-validation/stac/structure.json || true

      - name: Run stac-validator (strict)
        run: |
          stac-validator data/stac --recursive --log-level INFO --extended --asset --links \
            | tee reports/self-validation/stac/validator.log

      - name: Verify required fields (FAIR+CARE + Contract)
        run: |
          python scripts/stac/stac_contract_check.py \
            --root data/stac \
            --contract docs/contracts/data-contract-v3.json \
            --faircare docs/standards/faircare.yaml \
            --out reports/self-validation/stac/contract_faircare.json

      - name: Asset availability & checksum audit
        run: |
          python scripts/stac/stac_asset_audit.py \
            --root data/stac \
            --concurrency 10 \
            --require-checksum \
            --out reports/self-validation/stac/assets_audit.json

      - name: DCAT mirror validation
        run: |
          python scripts/stac/dcat_validate.py \
            --stac-root data/stac \
            --out reports/self-validation/stac/dcat_validation.json

      - name: Summarize results
        run: |
          python scripts/stac/stac_summarize.py \
            --structure  reports/self-validation/stac/structure.json \
            --validator  reports/self-validation/stac/validator.log \
            --contract   reports/self-validation/stac/contract_faircare.json \
            --assets     reports/self-validation/stac/assets_audit.json \
            --dcat       reports/self-validation/stac/dcat_validation.json \
            --out        reports/self-validation/stac/stac_validation.json \
            --markdown   reports/self-validation/stac/stac_summary.md

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: stac_validation_reports
          path: reports/self-validation/stac/

      - name: Emit telemetry (v3)
        run: |
          python scripts/emit_telemetry.py \
            --kind stac_validate \
            --summary reports/self-validation/stac/stac_validation.json \
            --out stac_telemetry.json

      - name: Append to unified telemetry
        run: |
          python scripts/merge_telemetry.py \
            --in  stac_telemetry.json \
            --dest releases/v11.2.4/stac-validate-telemetry.json
~~~

### 2. Validation Rules

#### STAC Core & Extensions

- **Core**  
  - `type`, `id`, `stac_version`, `links`, `assets` (per spec).  

- **Item**  
  - `bbox`, `geometry`, `properties.datetime` or `start_datetime`/`end_datetime`.  

- **Extensions** (when declared)  
  - `proj` — `proj:epsg` or `proj:wkt2`.  
  - `raster` — band metadata (dtype, nodata, scale/offset).  
  - `eo`, `label` — as per extension docs.  
  - `version` — versioning fields where used.  
  - `checksum` — `checksum:multihash` or equivalent.

#### FAIR+CARE & Contract Fields

Validated by `stac_contract_check.py`:

- `license` — SPDX/CC or project license; required and non‑empty.  
- `providers` — must include at least one `producer` and `licensor`.  
- `kfm:care_tag` ∈ {`public`, `restricted`, `sensitive`}.  
- `kfm:contract_id`, `kfm:checksum_sha256` or `checksum:multihash`.  
- Collections must define spatial + temporal `extent`.

#### Link & Asset Checks

- Structural links: `self`, `root`, `parent`, `collection` resolve (2xx).  
- Assets:
  - HTTP(S) assets respond to **HEAD** / Range requests.  
  - COGs: `Accept-Ranges: bytes` and appropriate `Content-Type`.  
  - PMTiles: validated via configured proxy or endpoint.

---

## 📦 Data & Metadata

### 1. Inputs

- STAC catalog tree under `data/stac/**`.  
- Contract and FAIR+CARE configuration:
  - `docs/contracts/data-contract-v3.json`.  
  - `docs/standards/faircare.yaml`.

### 2. Outputs & Artifacts

| Artifact Path                                        | Purpose                                           |
|------------------------------------------------------|---------------------------------------------------|
| `reports/self-validation/stac/stac_validation.json`  | Canonical JSON summary of STAC/DCAT validation   |
| `reports/self-validation/stac/stac_summary.md`       | Human-readable validation overview (for PRs)     |
| `reports/self-validation/stac/structure.json`        | PySTAC structural validation output              |
| `reports/self-validation/stac/validator.log`         | Raw `stac-validator` log                         |
| `reports/self-validation/stac/assets_audit.json`     | Asset reachability & checksum audit              |
| `reports/self-validation/stac/dcat_validation.json`  | DCAT mirror compliance report                    |
| `reports/self-validation/stac/contract_faircare.json`| Contract + FAIR+CARE field validation            |

Telemetry is appended to:

- `releases/v11.2.4/stac-validate-telemetry.json`  
  (schema: `stac-validate-v11.2.4`).

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC

This workflow enforces:

- **STAC 1.0.0** core compliance for Catalog, Collection, and Item.  
- Correct use of extensions, especially:
  - `proj`, `raster`, `eo`, `label`, `version`, and checksums.  
- KFM‑specific extensions (`kfm:care_tag`, `kfm:contract_id`, etc.) via contract checks.

### 2. DCAT

DCAT validation ensures:

- For required STAC → DCAT mirrors:
  - `dct:title`, `dct:description`, `dct:identifier` mirror STAC titles/IDs.  
  - `dct:license`, `dct:spatial`, `dct:temporal` consistent with STAC properties.  
  - Distributions point to the same assets (URLs, media types).

### 3. PROV

Validation runs can be represented as:

- Entities:  
  - `ex:StacValidationReport_<run_id>` (summary JSON).  
  - `ex:StacStructureReport_<run_id>`, etc.  

- Activity:  
  - `ex:StacValidationRun_<run_id>`.  

- Agent:  
  - `ex:KFM_CI_Bot` (prov:SoftwareAgent).

Relations:

- `ex:StacValidationRun_<run_id> prov:used` → catalog at specific commit.  
- `ex:StacValidationReport_<run_id> prov:wasGeneratedBy ex:StacValidationRun_<run_id>`.  
- `ex:StacValidationRun_<run_id> prov:wasAssociatedWith ex:KFM_CI_Bot`.

---

## 🧱 Architecture

### 1. Module Boundaries

- **Workflow orchestration**: `.github/workflows/stac-validate.yml`.  
- **Validation scripts**: `scripts/stac/*.py`.  
- **Schemas/configs**: `schemas/stac/**`, `schemas/dcat/**`, `docs/contracts/**`.  
- **Reports**: `reports/self-validation/stac/**`.  
- **Telemetry**: `releases/v11.2.4/stac-validate-telemetry.json`.

### 2. Determinism & Reproducibility

- Tools pinned via `requirements.txt` (exact versions for PySTAC, stac-validator, etc.).  
- Contract and FAIR+CARE rules come from versioned JSON/YAML configs.  
- For a given commit:
  - Same STAC tree + same config → identical validation results (modulo network availability for asset/link checks).

---

## ⚖ FAIR+CARE & Governance

### 1. Alignment Table

| Principle | Enforcement                                                      | Evidence                              |
|-----------|------------------------------------------------------------------|---------------------------------------|
| **Findable**   | Stable IDs, `self` links, Collections hierarchy             | `structure.json`                      |
| **Accessible** | Reachable assets; license & provider metadata present       | `assets_audit.json`                   |
| **Interoperable** | Extension schema validation; DCAT parity                 | `validator.log`, `dcat_validation.json` |
| **Reusable**   | Provenance, checksums, contract & FAIR+CARE fields          | `contract_faircare.json`              |
| **CARE**       | `kfm:care_tag` respected; sensitive items gated from public | `contract_faircare.json`              |

Items or Collections with `kfm:care_tag = sensitive`:

- Are withheld from public endpoints until **FAIR+CARE Council** approval.  
- May be exposed only as generalized or aggregate data in public catalogs.

### 2. Governance Hooks

- Failures in validation or FAIR+CARE checks can block:
  - Publication to public STAC APIs.  
  - Neo4j ingestion for certain Collections.  
- Governance dashboards can use telemetry to:
  - Track catalog health over time.  
  - Identify Collections that repeatedly fail checks.

---

## 🕰️ Version History

| Version    | Date       | Author          | Summary                                                                                                                            |
|-----------:|------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | `@kfm-devops`   | Aligned with KFM-MDP v11.2.4; added full front-matter, directory layout, Story Node hooks, STAC/DCAT/PROV alignment, and dedicated telemetry file for this workflow. |
| v10.2.4   | 2025-11-12 | `@kfm-devops`   | Upgraded to telemetry schema v3; unified artifact paths under `reports/self-validation/stac/`; refined asset/extension checks.   |
| v10.1.0   | 2025-11-10 | `@kfm-devops`   | Telemetry v2 adoption; stricter checksum/link rules; first DCAT parity report.                                                    |
| v9.9.0    | 2025-11-08 | `@kfm-devops`   | Initial governed STAC/DCAT validation doc with asset/link checks and telemetry export.                                            |

---

<div align="center">

🗂️ **Kansas Frontier Matrix — STAC/DCAT Validation Workflow (`stac-validate.yml`)**  
Interoperable Catalogs · FAIR+CARE Governance · Sustainable CI/CD  

[⬅ Back to Workflows Index](./README.md) ·  
[📘 Docs Root](../README.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>
