---
title: "Security Scan Action Scripts — README"
path: ".github/actions/security-scan/scripts/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:github-actions:security-scan:scripts-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-security-scan-scripts-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:security-scan:scripts-readme:v1.0.0"
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

# Security Scan Action Scripts — README

## 📘 Overview

### Purpose

- Document the scripts under `.github/actions/security-scan/scripts/` and how they are intended to be used by the repository’s security scanning automation.
- Establish safe, repeatable conventions for running and maintaining these scripts in CI and locally, including logging, outputs, and redaction.

### Scope

| In Scope | Out of Scope |
|---|---|
| Script purpose + inventory for this folder | Organization-wide security policy, incident response, or disclosure policy |
| Conventions for script inputs/outputs, exit codes, and logging | Selecting or endorsing specific third-party scanners (unless explicitly documented elsewhere) |
| CI reproducibility guidance and validation checklist | Remediation guidance for specific vulnerabilities or findings |

### Audience

- Primary: repo maintainers and CI owners working on `.github/actions/security-scan/`
- Secondary: contributors who need to understand (or update) security scan behavior for PRs

### Definitions

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Composite action**: a reusable GitHub Action defined in-repo under `.github/actions/<name>/`.
  - **Finding**: a single reportable issue detected by a scan (e.g., secret exposure, vulnerable dependency, insecure config).
  - **Redaction**: removing or masking sensitive values so logs/artifacts are safe to publish.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Security scan action | `.github/actions/security-scan/` | Repo maintainers | Entrypoint is typically `action.yml` (verify in-repo) |
| Scripts directory | `.github/actions/security-scan/scripts/` | Repo maintainers | Script inventory and conventions live here |
| CI workflows | `.github/workflows/` | Repo maintainers | Workflows call the security scan action (verify which) |
| Governance refs | `docs/governance/*` | Governance owners | Defines broader review + sovereignty rules |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] This README lists scripts in this directory (or documents how to enumerate them)
- [ ] Script inputs/outputs are documented with safe defaults and redaction rules
- [ ] Validation + reproduction steps are listed and repeatable
- [ ] Governance and sensitivity considerations are explicit for scan outputs

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/security-scan/scripts/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Security scan action | `.github/actions/security-scan/` | Action definition, inputs/outputs, orchestration |
| Security scan scripts | `.github/actions/security-scan/scripts/` | Script helpers invoked by the action |
| CI workflows | `.github/workflows/` | Jobs that run scanning and gating |
| Governance | `docs/governance/` | Security posture, ethics, sovereignty constraints |
| Schemas | `schemas/` | Any machine-readable contracts (if scan outputs are schema-governed) |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 security-scan/
        ├── 📄 action.yml                  # expected composite action entrypoint (verify)
        └── 📁 scripts/
            ├── 📄 README.md               # this document
            ├── 🧾 <script_1>              # bash/python helper (example placeholder)
            └── 🧾 <script_n>
~~~

### Script inventory

Maintain this table as scripts are added/removed.

| Script | Purpose | Runtime | Local usage |
|---|---|---|---|
| TBD | TBD | TBD | TBD |

## 🧭 Context

### Background

KFM’s architecture is layered and contract-driven. CI security scanning is a cross-cutting guardrail that helps keep the repository safe while preserving the canonical system pipeline and contracts (ETL → catalogs → graph → APIs → UI → story/focus layers). This scripts folder exists to keep scan logic close to the action definition, auditable, and reviewable.

### Assumptions

- These scripts run in a CI context (GitHub Actions runners) and may also be executed locally for reproduction.
- The action orchestrator (e.g., `action.yml`) is responsible for selecting which scripts to run and for providing configuration to them.

### Constraints and invariants

- Scripts should be safe to run on untrusted PR branches: do not execute untrusted code paths beyond the repository content being scanned.
- Prefer deterministic behavior: given the same commit + config, the scripts should produce the same outputs (or explain unavoidable nondeterminism).
- Do not leak secrets or sensitive data in logs, step summaries, or artifacts.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we standardize on a single machine-readable finding format (e.g., SARIF/JSON) for all scripts? | TBD | TBD |
| Where should scan artifacts be written so they are easy to collect in workflows? | TBD | TBD |
| What review gate is required for changes that modify pass/fail thresholds? | TBD | TBD |

### Future extensions

- Add explicit schemas for scan outputs (and validate them in CI).
- Add a normalized summary generator script to populate the workflow job summary.
- Add caching strategy for any scanners that require large databases, while preserving determinism and provenance.

## 🗺️ Diagrams

### System and dataflow diagram

~~~mermaid
flowchart LR
  PR[PR / Push] --> WF[GitHub Workflow Job]
  WF --> ACT[security-scan composite action]
  ACT --> S1[script A]
  ACT --> S2[script B]
  S1 --> OUT[Reports + logs]
  S2 --> OUT[Reports + logs]
  OUT --> GATE[Pass/Fail gate]
~~~

### Optional sequence diagram

~~~mermaid
sequenceDiagram
  participant WF as Workflow
  participant ACT as security-scan action
  participant SCR as script
  participant GH as GitHub Checks

  WF->>ACT: run action (with inputs)
  ACT->>SCR: invoke script (env + args)
  SCR-->>ACT: exit code + outputs
  ACT-->>GH: job summary / artifacts / status
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Repository workspace | Filesystem tree | CI workspace / local checkout | N/A (script-specific checks apply) |
| CI context | Environment variables | GitHub Actions context | Presence checks in script |
| Action configuration | Strings / files | Action inputs or config files | Validate required keys + allowed values |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Console logs | Text | CI logs | No secrets; redact sensitive values |
| Gate decision | Exit code | Process exit code | Script or action-defined convention |
| Human summary | Markdown | CI step/job summary | Keep high-level; avoid sensitive content |
| Machine report | TBD | TBD | If governed, define schema and validate |

### Sensitivity and redaction

- Do not print secret material, credentials, tokens, private keys, or raw matched secret strings.
- Prefer reporting file paths and finding types without including the sensitive value.
- If a script must show a snippet for triage, mask the value and keep the snippet minimal.

### Quality signals

- Stable exit behavior (success/failure/error distinct)
- Findings count and severity distribution (if applicable)
- Runtime consistency and clear failure modes

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Not applicable: these scripts do not define or emit STAC artifacts by default.

### DCAT

- Not applicable: these scripts do not define or emit DCAT artifacts by default.

### PROV-O

- Not applicable by default: these scripts do not emit `data/prov/` lineage bundles.
- If scan outputs become governed artifacts, record provenance minimally (commit SHA + tool/script identity + inputs) and store it in an agreed location.

### Versioning

- If scripts change behavior materially (thresholds, output formats, contracts), update this README and bump `version`.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| GitHub workflow job | Triggers scans on PR/push | `.github/workflows/*.yml` |
| security-scan action | Orchestrates scan steps | `.github/actions/security-scan/*` |
| Scripts in this folder | Execute specific checks | CLI args + env vars + exit code |
| Governance docs | Define review triggers | `docs/governance/*` |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Script conventions | `.github/actions/security-scan/scripts/README.md` | Semver bump for behavior changes |
| Action interface | `.github/actions/security-scan/action.yml` | Keep backward compatibility or document breaking changes |
| Report formats | TBD | If schema-governed, validate in CI |

### Extension points checklist

- [ ] Add a new script under `.github/actions/security-scan/scripts/`
- [ ] Update the script inventory table in this README
- [ ] Update the action orchestrator to invoke the new script
- [ ] Document output format and redaction rules for new findings
- [ ] Add validation/linting for the new script as applicable

## 🧠 Story Node and Focus Mode Integration

### How this work surfaces in Focus Mode

- This work does not surface directly in Focus Mode.
- It supports the system by preventing unsafe or non-compliant changes from being merged.

### Provenance-linked narrative rule

- Not applicable to scan scripts directly.
- If scan results are ever presented in user-facing UI, they must be provenance-linked and follow governance redaction rules.

### Optional structured controls

~~~yaml
# Not applicable for this document.
~~~

## 🧪 Validation and CI/CD

### Validation steps

- [ ] Markdown protocol checks for this README
- [ ] Script linting (shell/python/etc.), if configured
- [ ] Action-level smoke run in CI workflow
- [ ] Security and sovereignty checks remain enabled where applicable

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands and actual script names

# From repo root:
# 1) Inspect scripts available
# ls .github/actions/security-scan/scripts

# 2) Run a specific script locally (example pattern)
# bash .github/actions/security-scan/scripts/<script_name>.sh --help

# 3) If scripts rely on env vars, export them explicitly for local repro
# export <VAR>=<VALUE>
# bash .github/actions/security-scan/scripts/<script_name>.sh
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| security_scan_findings_total | security-scan action | CI logs / optional telemetry docs |
| security_scan_exit_code | script/action | CI logs |
| security_scan_duration_seconds | workflow runner | CI logs |

## ⚖ FAIR+CARE and Governance

### Review gates

- Changes that alter scan pass/fail thresholds, redaction behavior, or artifact publishing should receive heightened review (security-sensitive).

### CARE and sovereignty considerations

- If scans touch data under `data/` that may include restricted or culturally sensitive content, do not emit that content into logs/artifacts beyond what is necessary for remediation.
- Apply generalization and redaction rules defined in governance docs.

### AI usage constraints

- Respect `ai_transform_permissions` and `ai_transform_prohibited` in front-matter.
- Do not use this document as a vehicle to generate policy text; policy lives under governance docs.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README scaffold for security-scan scripts | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
