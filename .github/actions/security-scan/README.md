---
title: "GitHub Action — Security Scan"
path: ".github/actions/security-scan/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Guide"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:github-actions:security-scan:readme:v1.0.0"
semantic_document_id: "kfm-action-security-scan-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:security-scan:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# GitHub Action Security Scan

## 📘 Overview

### Purpose
- Provide a reusable GitHub Action wrapper to run the repository’s security scanning gates in CI.
- Standardize outputs (job summary + artifacts) and failure behavior (exit status / thresholds) across workflows.

### Scope
| In Scope | Out of Scope |
|---|---|
| Running one or more repository-approved scanners (SAST, secrets, dependency scanning, etc.) | Remediation, automatic patching, or approving risk exceptions |
| Producing machine-readable artifacts (for example SARIF or SBOM) and a human-readable step summary | Replacing GitHub org/repo security settings and policies |
| Enforcing CI hygiene for KFM outputs and artifacts | Scanning external systems unless explicitly wired in a workflow |

### Audience
- Primary: Repo maintainers and CI/CD maintainers
- Secondary: Contributors who need to understand PR gate failures

### Definitions
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **SAST**: Static application security testing
  - **SCA**: Software composition analysis / dependency scanning
  - **SARIF**: Static Analysis Results Interchange Format
  - **SBOM**: Software bill of materials (SPDX or CycloneDX)

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Composite action definition | `.github/actions/security-scan/action.yml` | Repo maintainers | Authoritative inputs and outputs live here |
| This README | `.github/actions/security-scan/README.md` | Repo maintainers | Intended behavior and usage examples |
| Workflows using this action | `.github/workflows/*.yml` | Repo maintainers | Gate configuration per workflow |

### Definition of done
- [ ] Front-matter complete and valid
- [ ] README matches the actual inputs and outputs in `action.yml`
- [ ] Usage snippet included for common scenarios
- [ ] Security considerations documented (permissions, token handling, artifact hygiene)

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/security-scan/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| GitHub composite actions | `.github/actions/` | Reusable actions called from workflows |
| GitHub workflows | `.github/workflows/` | CI pipelines that invoke this action |
| Security docs | `docs/security/` | Security standards and playbooks (not confirmed in repo) |
| Telemetry schemas | `schemas/telemetry/` | Scan telemetry schemas (not confirmed in repo) |

### Expected file tree for this sub-area
~~~text
📁 .github/
├── 📁 actions/
│   └── 📁 security-scan/
│       ├── 📄 action.yml
│       └── 📄 README.md
└── 📁 workflows/
    ├── 📄 security.yml
    └── 📄 ci.yml
~~~

## 🧭 Context

### Background
KFM expects strict validation and governance gates (schema validity, security posture, controlled publication). This action centralizes security scanning so workflows stay consistent as the system grows.

### Assumptions
- `action.yml` exists and defines the real inputs and outputs for this action.
- Workflows invoking this action set appropriate permissions for any uploads they enable (for example SARIF to Code Scanning).
- Scanners are executed either:
  - locally in the GitHub runner, or
  - via trusted GitHub Actions that are pinned and reviewed.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved. This action is a cross-cutting CI gate, not a pipeline stage.
- No secrets or credentials are committed to the repo or emitted in logs.
- Artifacts must not leak sensitive data, including precise locations that should be generalized.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Which scanners are mandatory vs optional for this repo? | TBD | TBD |
| What are the failing thresholds (severity, allowlist rules)? | TBD | TBD |
| Should SARIF be uploaded to Code Scanning, or stored only as artifacts? | TBD | TBD |

### Future extensions
- Add SBOM generation and signature verification as standard outputs.
- Add supply-chain controls: action pinning enforcement, provenance attestations, dependency allow and deny rules.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[GitHub Workflow] --> B[security-scan composite action]
  B --> C[Scanner 1..N]
  C --> D[Reports: SARIF / SBOM / JSON]
  D --> E[PR Check + Step Summary]
  D --> F[Artifact Upload]
~~~

### Sequence diagram
~~~mermaid
sequenceDiagram
  participant GH as GitHub Workflow
  participant ACT as security-scan action
  participant SCN as scanners
  participant ART as artifacts

  GH->>ACT: Invoke action with inputs
  ACT->>SCN: Run configured scanners
  SCN-->>ACT: Findings and reports
  ACT-->>GH: Fail or pass gate and summary
  ACT->>ART: Upload reports when enabled
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Repository workspace | Git checkout | GitHub Actions | Clean checkout; submodules as needed |
| Scan scope | paths or globs | workflow `with:` | Validate globs; default to whole repo |
| Failure thresholds | severity list or numeric | workflow `with:` | Validate allowed values |
| Allowlist | file path | repo or workflow | Ensure allowlist is versioned and reviewed |
| GitHub token | secret env | GitHub Actions | Least privilege; no echoing |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Step summary | Markdown | GitHub job summary | Human-readable |
| Findings report | SARIF recommended | artifact | SARIF v2.1.0 example, not confirmed in repo |
| Dependency report | JSON | artifact | Tool-specific, not confirmed |
| SBOM | SPDX or CycloneDX | artifact | Tool-specific, not confirmed |

### Sensitivity & redaction
- Do not include file contents or secrets in artifacts.
- Prefer redacted findings where tools support it.
- If scanning historical documents or datasets that may contain personal data, ensure reports do not expose raw PII.

### Quality signals
- Scanners and third-party actions should be pinned to immutable versions in workflows.
- Deterministic behavior: prefer config-driven scanning and stable allowlists.
- Keep allowlists explicit with rationale and require human review for additions.

## 🌐 STAC, DCAT & PROV Alignment

This action does not generate catalogs directly. It supports KFM governance by helping prevent:
- publication of secrets inside STAC, DCAT, or PROV outputs,
- unsafe dependencies entering the pipeline,
- accidental leakage of sensitive location data into public artifacts.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| GitHub workflow | Schedules and triggers the scan | `.github/workflows/*.yml` |
| `security-scan` action | Orchestrates scanners and gate logic | `.github/actions/security-scan/action.yml` |
| Scanners | Produce findings | Tool-specific CLI or actions |
| Artifact storage | Stores reports | GitHub Actions artifacts |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Action inputs and outputs | `.github/actions/security-scan/action.yml` | Semver; update README and workflow callers |
| Allowlist format | `docs/security/` or repo root | Schema plus review gate, not confirmed in repo |

### Extension points checklist
- [ ] Add new scanner with explicit config file and pinned version
- [ ] Add new report output with schema and format documented
- [ ] Add allowlist rules with rationale and reviewer requirement

## 🧠 Story Node & Focus Mode Integration

This is CI infrastructure, but it protects downstream Story Nodes and Focus Mode by enforcing that generated narrative artifacts and catalogs cannot accidentally include secrets or sensitive location details.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Action is invoked in at least one workflow
- [ ] Reports are generated or explicitly disabled in predictable locations
- [ ] Failure thresholds behave as expected
- [ ] Artifacts do not contain secrets

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific scanner commands.
# The authoritative scanner list lives in `.github/actions/security-scan/action.yml`.

# 1) run secret scan
# <tool> scan --config <path>

# 2) run dependency scan
# <tool> audit --format json

# 3) run SAST
# <tool> analyze --sarif out.sarif
~~~

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| Scan duration | GitHub Actions | Job logs |
| Finding counts by severity | Scanner output | Step summary and artifacts |
| Allowlist usage | Action logs | Step summary |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes to gating behavior or thresholds require human review.
- Introducing new external scanners or SaaS uploads requires security review. This process is not confirmed in repo.

### CARE / sovereignty considerations
- Security reports must not reveal culturally sensitive or restricted locations. If findings include coordinates or place names from restricted datasets, redact or generalize before publication.

### AI usage constraints
- This action should not send repository content to third-party AI services.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for security-scan action | TBD |

---
Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`