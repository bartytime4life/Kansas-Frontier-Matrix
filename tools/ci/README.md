---
title: "⚙️ Kansas Frontier Matrix — CI Automation Tools (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/ci/README.md"
version: "v11.0.0"
last_updated: "2025-11-24"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_guid: "urn:kfm:doc:tools-ci-readme-v11.0.0"
doc_kind: "Architecture"
intent: "tools-ci-platform"
role: "ci-automation-layer"
category: "CI/CD · Validation · Governance · Telemetry"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tools-ci-registry-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

fair_category: "F1-A1-I2-R2"
care_label: "Public · Low-Risk"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_data_flag: false
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "tools/ci/README.md@v9.5.0"
  - "tools/ci/README.md@v9.6.0"
  - "tools/ci/README.md@v9.7.0"
  - "tools/ci/README.md@v10.0.0"
  - "tools/ci/README.md@v10.2.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalDuration"
  prov_o: "prov:Plan"

json_schema_ref: "../../../schemas/json/tools-ci-readme-v11.json"
shape_schema_ref: "../../../schemas/shacl/tools-ci-readme-v11.shape.ttl"

event_source_id: "ledger:tools/ci/README.md"
immutability_status: "mutable-plan"
doc_uuid: "urn:kfm:doc:tools-ci-readme-v11.0.0"
semantic_document_id: "kfm-doc-tools-ci"

ai_training_allowed: false
ai_training_guidance: "CI logs and governance data MUST NOT be used for model training."
ai_outputs_require_explainability: true
ai_outputs_require_bias_audit: true

machine_readable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States · Kansas"
lifecycle_stage: "operational"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next CI-tools architecture update"
---

<div align="center">

# ⚙️ **Kansas Frontier Matrix — CI Automation Tools (v11)**  
`tools/ci/README.md`

**Purpose**  
Define the **canonical CI/CD automation layer** for the Kansas Frontier Matrix (KFM).  
These tools orchestrate validation, governance sync, security scanning, documentation QA, deployment, and telemetry export under:

- **MCP-DL v6.3** (documentation-first)
- **KFM-MDP v11.0** (markdown + metadata rules)
- **FAIR+CARE** (data & AI ethics, sovereignty)
- **ISO 19115 / 50001 / 14064** (metadata & sustainability)
- **Diamond⁹ Ω / Crown∞Ω** reliability and governance standards

</div>

---

## 📘 1. Overview

The **CI Automation Tools** in `tools/ci/`:

- Run **all automated checks** on **every PR, commit, and release**  
- Enforce **schema, contract, checksum, FAIR+CARE, sovereignty, and security** gates  
- Drive **Docs → Validation → Governance → Deploy → Telemetry** loops  
- Log **energy, carbon, and performance** metrics for sustainability dashboards  
- Ensure that **no artifact** reaches release without passing:

  1. Structural correctness  
  2. FAIR+CARE + sovereignty checks  
  3. Provenance & ledger registration  
  4. Telemetry + sustainability reporting

They are the **entry point** for Reliable Pipelines v11 gating logic.

---

## 🗂️ 2. Directory Layout (KFM-MDP v11 · Box Safe)

~~~~text
tools/ci/
├── README.md                    # This document
│
├── docs_validate.yml            # KFM-MDP v11 docs/guides/READMEs validation
├── checksum_verify.yml          # SBOM · manifest · dataset checksum integrity
├── site_deploy.yml              # Web/docs build & deploy after passing all gates
├── faircare_validate.yml        # FAIR+CARE + sovereignty CI enforcement
├── security_scan.yml            # CodeQL + dependency + container scanning
├── governance_sync.yml          # Ledger + manifest + SBOM sync
└── telemetry_report.yml         # Telemetry export (latency, energy, CO₂e, errors)
~~~~

Each workflow is:

- Versioned and referenced in `manifest_ref` and `sbom_ref`
- Required for protected branches and releases
- Designed to be deterministic and reproducible

---

## 🧬 3. CI Architecture Flow (v11)

~~~~mermaid
flowchart TD
    A["Commit / Pull Request / Scheduled Job"]
      --> B["Validation\n(docs_validate.yml · checksum_verify.yml)"]
    B --> C["FAIR+CARE & Sovereignty\n(faircare_validate.yml)"]
    C --> D["Governance Sync\n(governance_sync.yml)"]
    D --> E["Security Scans\n(security_scan.yml)"]
    E --> F["Deploy\n(site_deploy.yml)"]
    F --> G["Telemetry & Sustainability\n(telemetry_report.yml)"]
    G --> H["Ledger & Release Artifacts\n(SBOM · manifest · telemetry · governance)"]
~~~~

**Gating rules:**

- Any failure in **B → G** **blocks**:

  - PR merge  
  - Release tagging  
  - Deployment jobs  

- Governance & telemetry must run **even on failed pipelines** to record the attempted actions.

---

## ⚙️ 4. Workflow Responsibilities (Expanded v11)

### 4.1 `docs_validate.yml`

- Validates:

  - YAML front-matter (KFM-MDP v11)
  - Markdown heading hierarchy
  - Directory trees and fences (no broken boxes)
  - Cross-linked paths (e.g., relative refs to docs and schemas)
- Ensures every doc contains required front-matter keys:
  - `title`, `path`, `version`, `last_updated`, `governance_ref`, `license`, etc.

### 4.2 `checksum_verify.yml`

- Confirms:

  - Datasets, assets, and critical docs have matching SHA-256 hashes
  - `sbom.spdx.json` and `manifest.zip` integrity
  - STAC asset `checksum:multihash` fields match on-disk content (where applicable)
- Writes a checksum report into:
  - `docs/reports/audit/checksums-ci.json`

### 4.3 `faircare_validate.yml`

- Runs FAIR+CARE & sovereignty checks:

  - CARE labels present and consistent
  - Indigenous data rules (masking, H3 generalization)
  - Consent, licensing, and A11y metadata
- Produces:

  - `docs/reports/fair/data_care_assessment.json`
  - CI summary annotations for maintainers

### 4.4 `governance_sync.yml`

- Synchronizes:

  - Provenance ledger (`data_provenance_ledger.json`)
  - FAIR+CARE reports
  - Checksums and STAC/DCAT metadata
- Links governance entries to:

  - `sbom_ref`
  - `manifest_ref`
  - Release-level telemetry bundles

### 4.5 `security_scan.yml`

- Runs:

  - CodeQL or equivalent static analyzers
  - Dependency vulnerability scans
  - Container image scans (as configured)

- Blocks release if:

  - High/critical vulnerabilities are detected without approved exceptions

### 4.6 `site_deploy.yml`

- Builds and deploys:

  - Static docs site
  - Optional front-end apps (if configured)

- Must run only when:

  - Validation, governance, and security workflows **pass**

### 4.7 `telemetry_report.yml`

- Aggregates:

  - CI job duration
  - CPU, memory (if available)
  - Energy & carbon estimates (via energy/carbon schemas)
  - Test counts, failure rates
  - FAIR+CARE flags, governance events

- Writes into:

  - `focus-telemetry.json` (release root)
  - `docs/reports/telemetry/ci/*.json` (seven-day windows)

---

## 📊 5. Example CI Telemetry & Governance Record (v11)

~~~~json
{
  "id": "ci_registry_v11.0.0",
  "workflows": [
    "docs_validate.yml",
    "checksum_verify.yml",
    "faircare_validate.yml",
    "governance_sync.yml",
    "security_scan.yml",
    "site_deploy.yml",
    "telemetry_report.yml"
  ],
  "executions_logged": 972,
  "schema_passed": true,
  "checksum_verified": true,
  "faircare_compliant": true,
  "security_compliant": true,
  "governance_registered": true,
  "telemetry_logged": true,
  "energy_wh": 1.3,
  "carbon_gco2e": 1.6,
  "created": "2025-11-24T09:00:00Z",
  "validator": "@kfm-ci-core",
  "governance_ref": "docs/reports/audit/data_provenance_ledger.json"
}
~~~~

---

## 🧠 6. FAIR+CARE Governance Matrix (CI Tools)

| Principle           | Implementation                                                         | Oversight          |
|---------------------|-------------------------------------------------------------------------|--------------------|
| **Findable**        | CI workflows listed in manifest/SBOM, DCAT, and docs indices.          | @kfm-data          |
| **Accessible**      | Workflows and logs under MIT; machine-readable status checks.          | @kfm-accessibility |
| **Interoperable**   | CI metadata aligned with DCAT/ISO 19115 and telemetry schemas.         | @kfm-architecture  |
| **Reusable**        | Modular jobs, reusable actions, pinned versions.                       | @kfm-design        |
| **Collective Benefit** | Visible QA status builds trust in KFM as public-science infrastructure. | @faircare-council |
| **Authority to Control** | Council defines CI gates, FAIR+CARE thresholds, exceptions.      | @kfm-governance    |
| **Responsibility**  | CI logs & telemetry retained for audit; anomalies documented.          | @kfm-security      |
| **Ethics**          | Prevents unethical automations by enforcing FAIR+CARE checks & review. | @kfm-ethics        |

---

## 🌱 7. Sustainability & Observability

CI workflows must produce:

- `ci_run_energy_wh`  
- `ci_run_carbon_gco2e`  
- `ci_run_duration_ms`  
- `ci_run_failed_jobs`  
- `ci_run_retries`  
- `ci_run_care_flags`  

**Targets** (example):

| Metric                    | Target           |
|---------------------------|------------------|
| Avg CI Run Energy         | ≤ 1.6 Wh         |
| Avg CI Run Carbon         | ≤ 1.9 gCO₂e      |
| Renewable Energy Coverage | 100% (RE100)     |
| FAIR+CARE Gate Pass Rate  | 100% for releases |

All computed using `energy_schema` and `carbon_schema` in telemetry.

---

## 🛡 8. Security & Privacy Baselines

CI Tools must ensure:

- No secrets printed to logs  
- No PII emerges in logs or metrics  
- Vulnerabilities are surfaced and triaged  
- Only necessary metrics are exported to avoid over-collection  

Security scanning is treated as **governance-critical**.

---

## 🗃 9. Retention & Provenance Policy

| Artifact              | Retention | Policy                                 |
|-----------------------|-----------|----------------------------------------|
| CI Logs               | 90 days   | Rotated after telemetry aggregation    |
| CI Reports (JSON)     | 180 days  | Retained for reproducibility audits    |
| FAIR+CARE CI Logs     | 365 days  | Governance review + certification      |
| Governance Ledgers    | Permanent | Append-only, never pruned              |
| Telemetry Bundles     | Permanent | Versioned per release                  |

Cleanup is handled by `ci_cleanup.yml` in `.github/workflows/`.

---

## 🕰 10. Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.0.0 | 2025-11-24 | Full KFM-MDP v11 rewrite; telemetry v4; FAIR+CARE & sovereignty gating; unbroken fences & enriched architecture. |
| v10.2.2 | 2025-11-12 | JSON-LD exports, telemetry schema v2, sustainability logging, AI hooks. |
| v10.0.0 | 2025-11-10 | Telemetry v2, SBOM sync, FAIR+CARE enforcement.                        |
| v9.7.0  | 2025-11-05 | Governance sync + security improvements.                               |
| v9.5.0  | 2025-11-02 | Initial FAIR+CARE CI gating.                                           |

---

<div align="center">

**Kansas Frontier Matrix — CI Automation Tools (v11)**  
*Automation Integrity × FAIR+CARE Governance × Sustainable Pipelines*  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Tools Index](../README.md) · [Tools Platform Architecture](../ARCHITECTURE.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>