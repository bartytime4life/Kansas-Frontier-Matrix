---
title: "⚙️ Kansas Frontier Matrix — CI Automation Tools (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/ci/README.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "tools-ci-platform"
role: "ci-automation-layer"
category: "CI/CD · Validation · Governance · Telemetry"

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
layout_profile: "immediate-one-branch-with-descriptions-and-emojis"
fencing_profile: "outer-backticks-inner-tildes-v1"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
signature_ref: "../../releases/v11.2.6/signature.sig"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"

sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/tools-ci-registry-v4.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I2-R2"
care_label: "Public · Low-Risk"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_data_flag: false
risk_category: "Low"
redaction_required: false

jurisdiction: "United States · Kansas"
lifecycle_stage: "operational"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next CI-tools architecture update"
immutability_status: "mutable-plan"

provenance_chain:
  - "tools/ci/README.md@v11.2.2"
  - "tools/ci/README.md@v11.0.0"
  - "tools/ci/README.md@v10.2.2"
  - "tools/ci/README.md@v10.0.0"
  - "tools/ci/README.md@v9.7.0"
  - "tools/ci/README.md@v9.6.0"
  - "tools/ci/README.md@v9.5.0"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalDuration"
  prov_o: "prov:Plan"

json_schema_ref: "../../schemas/json/tools-ci-readme-v11.json"
shape_schema_ref: "../../schemas/shacl/tools-ci-readme-v11.shape.ttl"

doc_uuid: "urn:kfm:doc:tools:ci:readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ci"
event_source_id: "ledger:tools/ci/README.md"

ai_training_inclusion: false
ai_training_guidance: "CI logs and governance data MUST NOT be used for model training."
ai_outputs_require_explainability: true
ai_outputs_require_bias_audit: true

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_readable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# ⚙️ **Kansas Frontier Matrix — CI Automation Tools (v11.2.6)**
`tools/ci/README.md`

**Purpose**  
Define and maintain the **canonical CI automation toolchain** for the Kansas Frontier Matrix (KFM).  
This layer provides **deterministic, governed validation** across the pipeline:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/MapLibre UI → Story Nodes/Focus Mode**

It is enforced under:

- **MCP‑DL v6.3** (documentation‑first, reproducibility)
- **KFM‑MDP v11.2.6** (Markdown + metadata rules)
- **FAIR+CARE** (ethics, stewardship, sovereignty)
- **Diamond⁹ Ω / Crown∞Ω** reliability and governance expectations

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Status-Stable%20%2F%20Governed-brightgreen" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />

</div>

---

## 📘 Overview

### 1) What this directory is

`tools/ci/` is the **CI automation tooling layer**. It is intended to be called by:

- GitHub Actions workflows under `.github/workflows/**` (or equivalent CI runner),
- reusable composites under `.github/actions/**`,
- and local developer workflows when validating before PRs.

This directory is the **toolbox**; the workflow runner is the **orchestrator**.

### 2) What CI MUST guarantee

A governed KFM CI run MUST ensure:

1. **Documentation integrity**  
   Front‑matter, headings, links, diagrams, and schemas are valid and CI‑safe.

2. **Data integrity**  
   Release artifacts (datasets, manifests, SBOMs) are checksum‑verified.

3. **Governance integrity**  
   FAIR+CARE, sovereignty, licensing, and risk labels are validated and recorded.

4. **Security integrity**  
   Dependency/code scanning is enforced; secrets/PII are blocked.

5. **Traceability**  
   Every run produces machine‑readable outputs suitable for cataloging (DCAT/STAC) and lineage (PROV‑O).

### 3) Hard constraints (repo safety)

- **Fail closed**: no partial deploy when governance/security gates fail.
- **Deterministic by default**: pinned tool versions, stable sorting, fixed seeds where relevant.
- **No secrets, no PII** in logs or artifacts.
- **Frontend stays behind APIs**: CI validates that UI build artifacts do not bypass API contracts.

---

## 🗂️ Directory Layout

~~~text
📁 tools/
├── 📁 ci/                                      — CI automation tooling (this folder)
│   ├── 📄 README.md                            — CI tools architecture + contracts (this document)
│   ├── 📄 docs_validate.yml                    — Markdown + front‑matter + links validation (tool config)
│   ├── 📄 checksum_verify.yml                  — SBOM/manifest/dataset checksum verification (tool config)
│   ├── 📄 faircare_validate.yml                — FAIR+CARE + sovereignty gating (tool config)
│   ├── 📄 governance_sync.yml                  — Governance bundle/ledger sync (tool config)
│   ├── 📄 security_scan.yml                    — Code/dependency/container scanning (tool config)
│   ├── 📄 site_deploy.yml                      — Docs/UI build + deploy rules (tool config)
│   ├── 📄 telemetry_report.yml                 — CI telemetry export rules (tool config)
│   └── 📄 ci_cleanup.yml                       — Optional retention/compaction rules (if enabled)
└── 📄 ARCHITECTURE.md                          — Tools subsystem architecture (see cross-links)
~~~

Notes:

- The **authoritative workflow entry points** are expected under `.github/workflows/**`.
- Documentation describing each workflow SHOULD live under `docs/workflows/**` (one `*.yml.md` per workflow).

---

## 🧭 Context

### 1) Where CI sits in the KFM pipeline

KFM is pipeline‑driven. CI is the governance and quality “membrane” across all stages:

- **ETL**: validates new ingests, derived products, checksums, and catalog updates.
- **Catalogs**: validates STAC/DCAT/PROV alignment and schema compliance.
- **Graph**: validates ontology adherence and ingest contracts (through APIs/loaders, not direct UI access).
- **APIs**: validates contract integrity (OpenAPI/GraphQL contracts if present) and version compatibility.
- **UI**: validates build integrity, accessibility, and that content remains governed (no sensitive leaks).
- **Story Nodes / Focus Mode**: validates that AI‑adjacent artifacts are explainable, bias‑audited, and policy‑constrained.

### 2) What “governed CI” means here

Governed CI is not just “tests pass.” It means:

- evidence is logged,
- provenance is preserved,
- ethics/sovereignty checks are first‑class gates,
- and release artifacts are verifiable and reproducible.

---

## 🧱 Architecture

### 1) CI stages (canonical, v11)

This architecture defines a **gate chain**. Stages may be implemented as separate workflows, jobs, or composite actions, but the ordering and fail-closed semantics remain.

1. **Docs validation**
2. **Checksum / artifact integrity**
3. **FAIR+CARE + sovereignty**
4. **Governance sync + ledger bundle**
5. **Security scan**
6. **Deploy (docs/UI)**
7. **Telemetry export (always-on, degraded mode allowed)**

### 2) Gating rules

- Any failure in stages **1–6** MUST block:
  - merge into protected branches,
  - release tagging,
  - deployment jobs.

- Telemetry export SHOULD still run (degraded mode) to record:
  - failure events,
  - runtime cost,
  - governance gate outcome,
  - energy/carbon estimates where available.

---

## 🗺️ Diagrams

The diagram below expresses the **logical CI flow**, independent of runner implementation.

~~~mermaid
flowchart TD
  A["PR, push, or scheduled run"] --> B["Docs validation"]
  B --> C["Artifact integrity checks"]
  C --> D["FAIR+CARE and sovereignty gate"]
  D --> E["Governance sync and ledger bundle"]
  E --> F["Security scanning"]
  F --> G["Deploy docs and UI"]
  G --> H["Telemetry export (degraded mode allowed)"]
~~~

Plain-language interpretation:

- CI is a **pipeline of gates**.
- Governance and security are **hard gates**.
- Telemetry is **observability**, and is expected to record both success and failure.

---

## 🧪 Validation & CI/CD

### 1) Minimum validation profiles (required)

The CI tooling MUST support (directly or via the orchestrator) these minimum profiles:

| Profile | What it protects |
|---|---|
| `markdown-lint` | heading rules, formatting constraints, structural validity |
| `schema-lint` | YAML front‑matter schema compliance |
| `metadata-check` | required keys present and consistent (identity, governance, IDs, provenance) |
| `diagram-check` | Mermaid parse + allowed diagram profiles |
| `footer-check` | governance links + footer ordering |
| `accessibility-check` | basic a11y checks (heading order, list semantics) |
| `provenance-check` | provenance chain + version history coherence |
| `secret-scan` | blocks secrets/tokens/credentials |
| `pii-scan` | blocks obvious PII leakage |

### 2) Workflow responsibilities (canonical mapping)

This section maps responsibilities to the common CI tool configs in `tools/ci/`.  
Runner implementations MAY aggregate these into fewer workflows, but MUST preserve behavior.

#### A) Docs validation (`docs_validate.yml`)

Validates:

- YAML front‑matter is present and parseable
- Approved H2 headings only (per KFM‑MDP)
- Directory trees and fences (no broken boxes; tildes for fences)
- Mermaid parseability and guardrails
- Internal links and file paths

Outputs (example destinations):

- `data/reports/validation/docs-validation.json`
- PR annotations for violations when supported by the runner

#### B) Artifact integrity (`checksum_verify.yml`)

Ensures:

- Release‑critical artifacts have SHA‑256 checksums
- SBOM + manifest checksums match computed values
- Dataset assets referenced by catalogs remain consistent with on‑disk hashes

Outputs:

- `data/reports/validation/checksums-ci.json`

#### C) FAIR+CARE + sovereignty (`faircare_validate.yml`)

Enforces:

- CARE labels are present and consistent
- sovereignty constraints are validated (including redaction/generalization rules when applicable)
- licensing and attribution constraints are satisfied
- governance risk labeling is coherent

Outputs:

- `data/reports/faircare/summary.json`
- PR annotations for governance reviewers

#### D) Governance sync (`governance_sync.yml`)

Responsibilities:

- consolidates validation outputs into an auditable bundle
- updates append‑only ledgers and integrity logs
- prepares release metadata updates (manifest/SBOM references, signatures, attestations)

Outputs (example destinations):

- `data/reports/audit/data_provenance_ledger.json`
- `data/reports/audit/archive_integrity_log.json`

#### E) Security scanning (`security_scan.yml`)

Runs:

- static analysis (e.g., CodeQL or equivalent)
- dependency vulnerability scanning
- optional container scanning
- secret scan and PII scan (if not executed elsewhere)

Policy:

- CRITICAL and HIGH findings MUST block releases unless an approved exception exists in governance records.

#### F) Deploy (`site_deploy.yml`)

Builds:

- static docs site
- optionally the web UI bundle (behind APIs)

Constraints:

- must depend on successful completion of docs, validation, governance, and security gates
- MUST publish deployment status back to the runner (PR check, annotation, or build record)

#### G) Telemetry export (`telemetry_report.yml`)

Aggregates and serializes:

- job durations, pass/fail counts, warnings
- FAIR+CARE gate outcomes
- energy and carbon estimates (when enabled)
- error summaries and retry counts

Outputs:

- `releases/<version>/focus-telemetry.json`
- `data/reports/telemetry/ci/*.json`

### 3) Determinism requirements

CI tooling MUST prefer:

- pinned versions of validators and linters
- stable ordering for generated files
- reproducible archives (stable timestamps where supported)
- fixed seeds for any stochastic steps

---

## ⚖ FAIR+CARE & Governance

### 1) CI governance duties

CI MUST:

- enforce FAIR+CARE labeling and sovereignty constraints,
- record governance outcomes in machine‑readable audit artifacts,
- prevent shipment of unreviewed high‑risk changes.

CI MUST NOT:

- override governance policy,
- fabricate provenance or approvals,
- “auto‑approve” sensitive releases.

### 2) Governance matrix (CI tools)

| Principle | CI implementation | Oversight (example) |
|---|---|---|
| Findable | workflows and tool configs are documented and indexed | `@kfm-architecture` |
| Accessible | CI outputs are readable, versioned, and published as artifacts | `@kfm-accessibility` |
| Interoperable | telemetry and audit outputs align with schemas and catalog models | `@kfm-data` |
| Reusable | pinned versions, deterministic builds, stable contracts | `@kfm-design` |
| Collective Benefit | prevents untrustworthy artifacts from shipping | `@faircare-council` |
| Authority to Control | sovereignty and governance policy define gates | `@kfm-governance` |
| Responsibility | logs show what ran, what failed, and why | `@kfm-security` |
| Ethics | blocks unethical releases via mandatory gates | `@kfm-ethics` |

### 3) Security and privacy baseline

- CI logs MUST NOT contain secrets, tokens, or credentials.
- CI logs MUST NOT contain PII or sensitive location precision beyond policy.
- CI SHOULD support redaction/scrubbing for accidental leakage, but the default posture is **block and fail**.

---

## 📦 Data & Metadata

### 1) CI telemetry and audit record example

~~~json
{
  "id": "ci_registry_v11.2.6_2025-12-15_001",
  "branch": "main",
  "commit_sha": "<latest-commit-hash>",
  "workstreams": [
    "docs-validate",
    "checksum-verify",
    "faircare-validate",
    "governance-sync",
    "security-scan",
    "site-deploy",
    "telemetry-report"
  ],
  "results": {
    "schema_passed": true,
    "checksum_verified": true,
    "faircare_compliant": true,
    "security_compliant": true,
    "site_deployed": true,
    "governance_registered": true,
    "telemetry_logged": true
  },
  "sustainability": {
    "energy_wh": 1.3,
    "carbon_gco2e": 1.7
  },
  "runtime": {
    "ci_runtime_sec": 312,
    "ci_retry_count": 0,
    "ci_failed_jobs": 0
  },
  "created_at": "2025-12-15T00:00:00Z",
  "validator": "@kfm-ci-core",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
~~~

### 2) Sustainability and observability targets (configurable)

These values are targets and MAY vary by environment.

| Metric | Target |
|---|---|
| Avg CI Run Energy | ≤ 1.6 Wh |
| Avg CI Run Carbon | ≤ 1.9 gCO₂e |
| FAIR+CARE Gate Pass Rate | 100% for release runs |
| Telemetry Coverage | 100% of CI runs (including failures) |

### 3) Retention and provenance policy (defaults)

| Artifact | Retention | Notes |
|---|---:|---|
| CI runner logs | 90 days | rotated after aggregated summaries |
| CI reports (JSON) | 180 days | used for reproducibility audits |
| FAIR+CARE validation logs | 365 days | used for governance re-certification |
| Governance ledgers | permanent | append‑only; no hard deletions |
| Telemetry bundles | permanent | versioned per release |

---

## 🌐 STAC, DCAT & PROV Alignment

### 1) DCAT alignment (documentation as an asset)

- This README can be modeled as a documentation dataset (`dcat:Dataset` or `dcat:CatalogRecord`).
- `semantic_document_id` maps to `dct:identifier`.
- The Markdown file is a `dcat:Distribution` (`mediaType: text/markdown`).

### 2) STAC alignment (optional representation)

This doc MAY be represented as a non‑spatial STAC Item:

- `geometry: null`
- `properties.datetime = last_updated`
- `assets.markdown.href` points to the repo path or artifact store location

### 3) PROV‑O alignment

- This architecture is a `prov:Plan`.
- CI runs are `prov:Activity` instances.
- CI bots, councils, and maintainers are `prov:Agent`s.

---

## 🧠 Story Node & Focus Mode Integration

CI tooling supports Story Nodes / Focus Mode by ensuring documentation and run outputs are:

- stable to summarize (predictable H2 sections),
- safe to transform (explicit AI transform permissions),
- traceable (stable IDs and provenance chains).

**Focus Mode MAY:**

- summarize and highlight sections,
- generate navigation aids and timelines,
- extract metadata fields and link them to catalogs.

**Focus Mode MUST NOT:**

- alter normative requirements,
- invent governance status,
- fabricate provenance or dataset relationships.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| v11.2.6 | 2025-12-15 | Upgraded to KFM‑MDP v11.2.6; normalized approved H2 headings; fixed fence styles (inner tildes); corrected relative refs; expanded validation profiles and governance alignment. |
| v11.2.2 | 2025-11-27 | KFM‑MDP v11.2.2 baseline; workflow descriptions; FAIR+CARE & telemetry flow. |
| v11.0.0 | 2025-11-24 | v11 CI tools redesign; governance + telemetry gating introduced. |
| v10.2.2 | 2025-11-12 | JSON‑LD exports; telemetry schema updates; sustainability logging; AI response checks. |
| v10.0.0 | 2025-11-10 | SBOM sync + early FAIR+CARE gating. |
| v9.7.0 | 2025-11-05 | Governance sync + improved security scanning. |
| v9.6.0 | 2025-11-03 | CI determinism hardening + audit artifact normalization. |
| v9.5.0 | 2025-11-02 | Initial FAIR+CARE‑aware CI gating framework. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
**KFM CI Automation Tools v11.2.6**  
FAIR+CARE Certified · MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

[⬅️ Back to Tools Index](../README.md) · [🧱 Tools Architecture](../ARCHITECTURE.md) · [🛡 Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>