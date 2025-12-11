---
title: "🔐 Kansas Frontier Matrix — Supply-Chain Security Workflow (`security-supply-chain.yml`) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/workflows/security-supply-chain.yml.md"

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
telemetry_ref: "releases/v11.2.6/security-supply-chain-telemetry.json"
telemetry_schema: "schemas/telemetry/security-supply-chain-workflow-v11.2.6.json"
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
    - ".github/workflows/security-supply-chain.yml"
    - "package.json"
    - "package-lock.json"
    - "pnpm-lock.yaml"
    - "yarn.lock"
    - "requirements.txt"
    - "poetry.lock"
    - "pyproject.toml"
    - "Cargo.toml"
    - "Cargo.lock"
    - "Dockerfile"
    - "docker-compose.yml"
    - "helm/**"
    - ".github/workflows/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Build and dependency metadata; low direct sensitivity"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Supply-Chain Security Workflow v12"

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
  - "docs/workflows/security-supply-chain.yml.md@v10.2.4"
  - "docs/workflows/security-supply-chain.yml.md@v10.1.0"
  - "docs/workflows/security-supply-chain.yml.md@v9.9.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:workflows:security-supply-chain-yml:v11.2.6"
semantic_document_id: "kfm-workflow-security-supply-chain-yml-v11.2.6"
event_source_id: "ledger:kfm:doc:workflows:security-supply-chain-yml-v11.2.6"
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
  workflow: ".github/workflows/security-supply-chain.yml"
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

# 🔐 **Kansas Frontier Matrix — Supply-Chain Security Workflow (`security-supply-chain.yml`)**  
`docs/workflows/security-supply-chain.yml.md`

**Purpose**  
Define the **governed GitHub Actions workflow** that secures the **software supply chain** for the Kansas Frontier Matrix (KFM):  
building **SBOMs**, running **vulnerability & license scans**, performing **SLSA attestations**, **Cosign signing**, **npm worm defense**, and **secrets checks**, then emitting **governance-ready audit reports** and **telemetry**.

<img src="https://img.shields.io/badge/Docs·MCP-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Status-Automated-brightgreen" />

</div>

---

## 📘 Overview

### 1. Workflow Intent

`security-supply-chain.yml` is the **supply‑chain security gate** for KFM. It ensures that:

- ✅ Dependencies (npm, Python, Rust, etc.) are **tracked** via SBOM and checked for known vulnerabilities.  
- ✅ Container images and Dockerfiles are scanned for **CVEs and misconfigurations**.  
- ✅ Builds are accompanied by **SLSA attestations** and **Cosign signatures**.  
- ✅ **npm worm defense** and dependency pinning guard against malicious packages.  
- ✅ **Secrets scanning** reduces risk of credential leakage.  
- ✅ All checks produce **machine‑readable audit reports** and **telemetry** for governance.

This workflow complements functional CI by focusing specifically on **integrity, provenance, and risk** in KFM’s software stack.

### 2. Role in the KFM Pipeline

Within:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

`security-supply-chain.yml`:

- Protects **ETL, backend, and frontend** code from compromised dependencies.  
- Helps ensure that artifacts used by catalogs, the graph, and UIs are **signed**, **attested**, and **audited**.  
- Provides long‑term evidence for governance and incident response.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 workflows/
    📄 README.md                               — CI/CD & governance workflows index
    📄 security-supply-chain.yml.md            — ← This supply-chain security workflow spec

📁 .github/
└── 📁 workflows/
    📄 security-supply-chain.yml               — GitHub Actions workflow (supply-chain security)

📁 tools/
└── 📁 security/
    📄 aggregate_supply_chain_report.py        — Aggregates scanner outputs → summary JSON
    📄 emit_supply_chain_telemetry.py          — Converts summary → telemetry records
    📄 npm_worm_guard.mjs                      — npm worm-defense and lockfile consistency checks

📁 reports/
└── 📁 audit/
    📄 supply_chain_security_summary.json      — Canonical machine-readable audit summary
    📄 sbom_scan.json                          — Vulnerability results from SBOM scan
    📄 container_scan.json                     — Container image scan results
    📄 dependency_diff.json                    — Dependency change summary (PR vs base)
    📄 secrets_scan.json                       — Secrets & token leak findings

📁 releases/
└── 📁 v11.2.6/
    📄 security-supply-chain-telemetry.json    — Aggregated telemetry for this workflow
    📄 sbom.spdx.json                          — SPDX SBOM (multi-language)
    📄 manifest.zip                            — Release manifest (hashes, attestation refs)
~~~

---

## 🧭 Context

### 1. Triggers & Scope

| Trigger            | Paths                                                                 | Notes                                       |
|-------------------:|-----------------------------------------------------------------------|---------------------------------------------|
| `pull_request`     | `**/package.json`, `**/package-lock.json`, `**/pnpm-lock.yaml`,<br>`**/yarn.lock`, `**/requirements*.txt`, `**/poetry.lock`,<br>`**/pyproject.toml`, `Cargo.toml`, `Cargo.lock`,<br>`Dockerfile`, `docker-compose.yml`, `.github/workflows/**` | Blocks merge if critical issues detected    |
| `push` (protected) | Same as PR                                                           | Required on `main` & `release/**` branches  |
| `workflow_dispatch`| —                                                                     | Manual re‑run for incidents or audits       |

Coverage:

- Package manifests and lockfiles.  
- Container build descriptors (Dockerfiles, Helm charts).  
- GitHub Actions workflows (for insecure patterns).

### 2. Relationship to Other Workflows

- **Peers**:
  - `docs-lint.yml` — docs structure and KFM‑MDP compliance.  
  - `faircare-validate.yml` — ethics & data governance checks.  
  - `ai-train.yml` + `ai-explainability.yml` — governed AI training & audits.  
- **Downstream**:
  - Release workflows that publish artifacts only after supply‑chain checks pass.  
  - Governance dashboards that rely on `security-supply-chain-telemetry.json`.

---

## 🗺️ Diagrams

### 1. Supply-Chain Security Flow

~~~mermaid
flowchart LR
    A["PR / Protected Push"] --> B["Checkout & Baseline Dependency Diff"]
    B --> C["Generate SBOM (SPDX)"]
    C --> D["Vulnerability & License Scan (SBOM / Container)"]
    D --> E["npm Worm Defense · Lockfile Consistency"]
    E --> F["Secrets Scan (Repository & History)"]
    F --> G["Aggregate Findings → Summary JSON"]
    G --> H["SLSA Attestations · Cosign Signatures (if applicable)"]
    H --> I["Upload Artifacts · Emit Telemetry"]
    I --> J["Governance Ledger · Release Gate"]
~~~

### 2. Timeline — From Change to Attested Artifact

~~~mermaid
timeline
    title Supply-Chain Security — Change Lifecycle
    section Code & Config
      T0 : Dependency / workflow change opened in PR
      T1 : security-supply-chain.yml runs scans
    section Audit & Governance
      T2 : Findings aggregated → summary & telemetry
      T3 : Governance checks gates merge / release
    section Release
      T4 : SLSA attestations & Cosign signatures issued
      T5 : Provenance & SBOM archived with release
~~~

---

## 🧠 Story Node & Focus Mode Integration

### 1. Story Node Types

Supply-chain security runs can produce Story Nodes such as:

- `urn:kfm:story-node:infra:supply-chain:<run_id>`  
  - Summarizes vulnerabilities found, fixed, or deferred.  

- `urn:kfm:story-node:infra:dependency-evolution:<package>`  
  - Tracks the story of key dependencies (e.g., mapping libraries, AI frameworks) across versions.

Each Story Node may reference:

- `reports/audit/supply_chain_security_summary.json`.  
- Telemetry entries from `security-supply-chain-telemetry.json`.  
- Related PRs or releases.

### 2. Focus Mode Behavior

Focus Mode may:

- Surface **current supply‑chain health** for a module or service.  
- Show **dependency drift and remediation history** (e.g., when a CVE was addressed).  
- Highlight **high‑risk areas** (e.g., unpinned dependencies, outdated images).

Focus Mode must not:

- Declare a build “secure” beyond what the recorded scans show.  
- Rewrite or reinterpret audit results; it may only summarize them.  
- Reveal any secrets or sensitive tokens discovered by scans.

---

## 🧪 Validation & CI/CD

### 1. Conceptual Workflow YAML

~~~yaml
name: "Supply-Chain Security (Governed)"

on:
  pull_request:
    paths:
      - "**/package.json"
      - "**/package-lock.json"
      - "**/pnpm-lock.yaml"
      - "**/yarn.lock"
      - "**/requirements*.txt"
      - "**/poetry.lock"
      - "**/pyproject.toml"
      - "Cargo.toml"
      - "Cargo.lock"
      - "Dockerfile"
      - "docker-compose.yml"
      - ".github/workflows/**"
  push:
    branches: ["main", "release/**"]
    paths:
      - "**/package.json"
      - "**/package-lock.json"
      - "**/pnpm-lock.yaml"
      - "**/yarn.lock"
      - "**/requirements*.txt"
      - "**/poetry.lock"
      - "**/pyproject.toml"
      - "Cargo.toml"
      - "Cargo.lock"
      - "Dockerfile"
      - "docker-compose.yml"
      - ".github/workflows/**"
  workflow_dispatch: {}

permissions:
  contents: read
  id-token: write

concurrency:
  group: security-supply-chain-${{ github.ref }}
  cancel-in-progress: true

jobs:
  security-supply-chain:
    runs-on: ubuntu-22.04
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup tooling
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install security tooling
        run: |
          pip install -r requirements.txt
          pip install cyclonedx-bom
          pip install jq
          npm install -g npm@latest
          curl -sSfL https://raw.githubusercontent.com/gitleaks/gitleaks/master/install.sh | bash
          curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | bash
          curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | bash

      - name: Generate SBOM (SPDX)
        run: |
          mkdir -p releases/v11.2.6
          ./syft dir:. -o spdx-json=./releases/v11.2.6/sbom.spdx.json

      - name: Scan SBOM for vulnerabilities
        run: |
          mkdir -p reports/audit
          ./grype sbom:./releases/v11.2.6/sbom.spdx.json -o json > reports/audit/sbom_scan.json || true

      - name: Container scan (if Dockerfile present)
        run: |
          if [ -f Dockerfile ]; then
            docker build -t kfm-app-under-test .
            ./grype kfm-app-under-test -o json > reports/audit/container_scan.json || true
          else
            echo '{}' > reports/audit/container_scan.json
          fi

      - name: npm worm defense & lockfile consistency
        run: |
          node tools/security/npm_worm_guard.mjs \
            --root "." \
            --out reports/audit/dependency_diff.json

      - name: Secrets scan
        run: |
          ./gitleaks detect --source . --report-format json \
            --report-path reports/audit/secrets_scan.json || true

      - name: Aggregate supply-chain security report
        run: |
          python tools/security/aggregate_supply_chain_report.py \
            --sbom reports/audit/sbom_scan.json \
            --container reports/audit/container_scan.json \
            --dependencies reports/audit/dependency_diff.json \
            --secrets reports/audit/secrets_scan.json \
            --out reports/audit/supply_chain_security_summary.json

      - name: Install Cosign
        uses: sigstore/cosign-installer@v3

      - name: SLSA attest build provenance
        if: github.ref == 'refs/heads/main'
        uses: slsa-framework/slsa-github-generator/actions/attest-build-provenance@v1
        with:
          subject-path: "releases/v11.2.6/"

      - name: Cosign sign SBOM (optional)
        if: github.ref == 'refs/heads/main'
        run: |
          cosign sign-blob --yes \
            --output-signature releases/v11.2.6/signature.sig \
            --output-certificate releases/v11.2.6/certificate.pem \
            releases/v11.2.6/sbom.spdx.json

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: security_supply_chain_reports
          path: |
            reports/audit/**
            releases/v11.2.6/sbom.spdx.json
            releases/v11.2.6/signature.sig
            releases/v11.2.6/certificate.pem

      - name: Emit telemetry
        run: |
          python tools/security/emit_supply_chain_telemetry.py \
            --summary reports/audit/supply_chain_security_summary.json \
            --out security_supply_chain_telemetry.json

      - name: Append telemetry to unified log
        run: |
          python scripts/merge_telemetry.py \
            --in  security_supply_chain_telemetry.json \
            --dest releases/v11.2.6/security-supply-chain-telemetry.json
~~~

### 2. Quality Gates

The job should:

- **Fail** on:
  - Critical or high vulnerabilities without documented waivers.  
  - Unapproved or unpinned critical dependencies (per project policy).  
  - Secrets scan hits above thresholds.  
- **Warn** (but may not fail) on:
  - Medium/low vulnerabilities with mitigations.  
  - Non‑critical license concerns.

Policy thresholds and waivers should be configuration‑driven (e.g., YAML in `configs/security/`).

---

## 📦 Data & Metadata

### 1. Inputs

- Source repository at the current commit (code, manifests, Dockerfiles).  
- Security configuration files, e.g.:
  - `configs/security/vuln_policy.yaml`  
  - `configs/security/license_policy.yaml`

### 2. Outputs & Artifacts

| Artifact Path                                      | Purpose                                          |
|----------------------------------------------------|--------------------------------------------------|
| `reports/audit/sbom_scan.json`                     | Vulnerabilities found via SBOM                   |
| `reports/audit/container_scan.json`                | Container image findings                         |
| `reports/audit/dependency_diff.json`               | Dependency changes (base vs PR)                  |
| `reports/audit/secrets_scan.json`                  | Potential secrets and tokens                     |
| `reports/audit/supply_chain_security_summary.json` | Aggregated machine-readable summary              |
| `releases/v11.2.6/sbom.spdx.json`                  | SPDX SBOM for the repository                     |
| `releases/v11.2.6/signature.sig`                   | Cosign signature of SBOM (where applicable)      |
| `releases/v11.2.6/certificate.pem`                 | Cosign certificate                               |

Telemetry records aggregate into:

- `releases/v11.2.6/security-supply-chain-telemetry.json`

with fields like:

- `vulns_critical`, `vulns_high`, `vulns_medium`,  
- `dependencies_added`, `dependencies_removed`,  
- `secrets_found`,  
- `workflow_duration_sec`, `energy_wh`, `carbon_gco2e`.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. DCAT

Supply-chain reports may be modelled as a DCAT Dataset:

- `dct:title`: "KFM Supply-Chain Security Audit Reports".  
- `dct:description`: "Automated vulnerability, license, and secrets audit reports for KFM's software supply chain."  
- `dct:identifier`: stable dataset ID, with per-run entries.

Distributions:

- `supply_chain_security_summary.json`  
- `sbom.spdx.json`  
- Telemetry JSON as a separate distribution or linked dataset.

### 2. STAC

If integrated into STAC:

- Collection: `kfm-infra-security`.  
- Item per run:
  - `id`: `security-supply-chain-<run_id>`.  
  - `properties.datetime`: completion time.  
- Assets:
  - `summary-json`: `supply_chain_security_summary.json`.  
  - `sbom-spdx`: `sbom.spdx.json`.

Non‑spatial governance results can use `geometry: null`.

### 3. PROV-O

Entities:

- `ex:SBOM_<run_id>`, `ex:ScanReport_<run_id>`, `ex:SupplyChainSummary_<run_id>`.

Activity:

- `ex:SupplyChainScan_<run_id>`.

Agents:

- `ex:KFM_CI_Bot` (software agent).  
- `ex:SecurityWG` (governance org) for downstream review.

Relations:

- `ex:SupplyChainScan_<run_id> prov:used` → repo at specific commit.  
- `ex:SBOM_<run_id> prov:wasGeneratedBy ex:SupplyChainScan_<run_id>`.  
- `ex:SupplyChainSummary_<run_id> prov:wasGeneratedBy ex:SupplyChainScan_<run_id>`.  
- `ex:SupplyChainScan_<run_id> prov:wasAssociatedWith ex:KFM_CI_Bot`.

---

## 🧱 Architecture

### 1. Module Boundaries

- **Workflow orchestration**: `.github/workflows/security-supply-chain.yml`.  
- **Security tooling wrapper scripts**: `tools/security/*.py` and `tools/security/*.mjs`.  
- **Configs**: `configs/security/*.yaml` (policies, thresholds, waivers).  
- **Reports**: `reports/audit/**`.  
- **Telemetry**: `releases/v11.2.6/security-supply-chain-telemetry.json`.

The workflow delegates complex logic to scripts and tools; YAML remains declarative.

### 2. Determinism & Reproducibility

- Tool versions pinned via `requirements.txt`, `package.json`, or specific installer versions.  
- Policies and thresholds stored in versioned configs.  
- For the same commit and config, the same vulnerabilities and findings should be produced.

---

## ⚖ FAIR+CARE & Governance

### 1. FAIR

| Principle        | Implementation                                                  |
|-----------------:|-----------------------------------------------------------------|
| **Findable**     | Reports and SBOMs in predictable locations, catalog entries     |
| **Accessible**   | Where policy allows, security reports can be shared internally |
| **Interoperable**| SPDX, JSON, DCAT, and PROV usage for security data             |
| **Reusable**     | Versioned policies, reproducible scans, persistent telemetry   |

### 2. CARE

Even though security data is technical, it has CARE implications:

- **Collective Benefit**: A resilient supply chain protects all KFM stakeholders.  
- **Authority to Control**: Policies define who can see which portions of scan output (e.g., internal only vs public).  
- **Responsibility**: Clear expectations on remediation timelines, and tracking of pending vulnerabilities.  
- **Ethics**: Avoid outing vulnerabilities or secrets in ways that increase risk; handle disclosures responsibly.

### 3. Governance Hooks

- Critical vulnerabilities should be tied to **governance tickets** and remediation SLAs.  
- Telemetry helps governance teams see:
  - Trends in vulnerability counts.  
  - Areas with persistent risk.  
  - The impact of dependency management practices.

---

## 🕰️ Version History

| Version    | Date       | Author          | Summary                                                                                                                        |
|-----------:|------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| **v11.2.6** | 2025-12-11 | `@kfm-sec`      | Aligned to KFM v11.2.6; updated release/telemetry paths and telemetry schema reference; no functional changes to security checks. |
| v11.2.4   | 2025-12-06 | `@kfm-sec`      | Aligned with KFM-MDP v11.2.4; expanded front-matter; added STAC/DCAT/PROV alignment, Story Node hooks, telemetry wiring, and detailed supply-chain scan flow. |
| v10.2.4   | 2025-11-12 | `@kfm-sec`      | Introduced telemetry v3 schema; unified audit artifact paths; added secrets scan integration and dependency diff summary.      |
| v10.1.0   | 2025-11-10 | `@kfm-sec`      | Added SBOM generation, container scans, SLSA attestations, and Cosign signing.                                                |
| v9.9.0    | 2025-11-08 | `@kfm-sec`      | Initial governed supply-chain security workflow documentation; basic SBOM + vulnerability scanning.                           |

---

<div align="center">

🔐 **Kansas Frontier Matrix — Supply-Chain Security Workflow (`security-supply-chain.yml`)**  
Secure Dependencies · FAIR+CARE Governance · Sustainable CI/CD  

[⬅ Back to Workflows Index](./README.md) ·  
[📘 Docs Root](../README.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>
