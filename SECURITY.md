---
title: "Kansas Frontier Matrix — Security Policy"
path: "SECURITY.md"
version: "v1.0.0"
last_updated: "2025-12-21"
status: "draft"
doc_kind: "Policy"
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

doc_uuid: "urn:kfm:doc:security:security-policy:v1.0.0"
semantic_document_id: "kfm-security-policy-v1.0.0"
event_source_id: "ledger:kfm:doc:security:security-policy:v1.0.0"
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

# Kansas Frontier Matrix — Security Policy

**Do not open public issues for security vulnerabilities.** Use a private channel as described below.

## 📘 Overview

### Purpose
- Provide a clear, safe process for reporting vulnerabilities affecting Kansas Frontier Matrix (KFM).
- Define how project maintainers coordinate triage, fixes, and disclosure across the KFM pipeline.

### Scope

| In Scope | Out of Scope |
|---|---|
| Vulnerabilities in KFM repository code, configurations, schemas, docs tooling, and data-processing workflows that impact confidentiality, integrity, availability, or safety | Feature requests, general support questions, and non-security bugs without a plausible security impact |
| Vulnerabilities that could expose sensitive or restricted location data, PII, secrets, or internal infrastructure details | Vulnerabilities in third-party services or dependencies that do not have a KFM-specific exploit or misconfiguration |
| Supply-chain risks introduced by changes in dependencies, CI, artifacts, or build tooling | Social engineering attempts, phishing, or physical attacks |

### Audience
- Primary: Security researchers and reporters
- Secondary: Project maintainers and contributors
- Tertiary: Downstream deployers and integrators

### Definitions
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Vulnerability:** A weakness that can be exploited to compromise confidentiality, integrity, or availability.
  - **Incident:** Confirmed exploitation or data exposure requiring containment and notification steps.
  - **Sensitive knowledge:** Any data requiring redaction or generalization under `docs/governance/SOVEREIGNTY.md` or similar governance controls.
  - **Coordinated disclosure:** Private reporting and collaborative remediation before public disclosure.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This policy | `SECURITY.md` | Maintainers | Canonical security reporting guidance |
| Private report channel | GitHub Security Advisories | Maintainers | Preferred if enabled |
| Governance policy | `docs/governance/ROOT_GOVERNANCE.md` | Governance owners | Defines decision authority |
| Ethics policy | `docs/governance/ETHICS.md` | Governance owners | “Do no harm” constraints |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | Governance owners | Redaction and generalization rules |

### Definition of done
- [ ] Front-matter complete and valid
- [ ] Reporting channels are unambiguous and usable by external reporters
- [ ] Sensitive-data handling rules are explicit
- [ ] Validation and governance steps are listed and repeatable

## 🗂️ Directory Layout

### This document
- `path`: `SECURITY.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed outputs and catalogs |
| Documentation | `docs/` | Governed docs, standards, and reports |
| Schemas | `schemas/` | STAC/DCAT/PROV/telemetry/UI/story node schemas |
| Pipelines | `src/pipelines/` | ETL and catalog generation transforms |
| Graph | `src/graph/` | Graph build and ontology bindings |
| APIs | `src/server/` | Contract-first API layer |
| Frontend | `web/` | React and map clients |
| CI and repo hygiene | `.github/` | Workflows, issue templates, CI gates |
| MCP runs and experiments | `mcp/` | Runs, experiments, model cards, SOPs |

### Expected file tree for this sub-area

~~~text
📄 SECURITY.md
📁 .github/
├── 📁 workflows/               # CI checks (if present)
│   └── …
└── 📁 ISSUE_TEMPLATE/          # optional
    └── …
📁 docs/
└── 📁 security/                # optional deeper standards or playbooks
    └── …
~~~

## 🧭 Context

### Background
KFM spans an end-to-end pipeline from ETL and standardized catalogs (STAC/DCAT/PROV) through a graph layer, APIs, and a React-based UI that surfaces Story Nodes and Focus Mode narratives. Security issues can arise anywhere in this chain, including data leakage, broken access controls, injection vulnerabilities, or provenance and integrity failures.

### Assumptions
- This repository is hosted on GitHub and can use GitHub-native private reporting features.
- Maintainers can privately coordinate fixes before public disclosure.
- Sensitive or restricted knowledge may exist and must be handled under governance rules.

### Constraints and invariants
- Canonical pipeline order is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- The UI must not read from Neo4j directly; access is mediated by the API layer.
- Public-facing narrative and evidence must be provenance-linked; security fixes must not introduce unsourced content.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Is GitHub private vulnerability reporting enabled for this repo | Maintainers | TBD |
| Do we maintain a dedicated security contact address and PGP key | Maintainers | TBD |
| Do we publish a formal incident notification process for sensitive-data exposure | Governance owners | TBD |

### Future extensions
- Dedicated incident playbooks under `docs/security/`
- Automated dependency and secret scanning gates in CI
- Formal advisory publishing workflow

## 🗺️ Diagrams

### Security reporting flow

~~~mermaid
flowchart LR
  R[Reporter] --> C[Private reporting channel]
  C --> T[Triage]
  T --> F[Fix and tests]
  F --> P[Patch release]
  P --> A[Advisory and coordinated disclosure]
~~~

### Optional sequence diagram

~~~mermaid
sequenceDiagram
  participant Reporter
  participant Maintainers
  participant CI as CI/CD
  Reporter->>Maintainers: Private vulnerability report
  Maintainers->>Maintainers: Triage and reproduce
  Maintainers->>CI: Add regression test and patch
  CI-->>Maintainers: Checks pass
  Maintainers-->>Reporter: Fix available and disclosure plan
~~~

## 📦 Data and Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Vulnerability report | GitHub advisory text | External reporter | Repro steps, affected commit/tag, impact |
| Proof of concept | Code snippet or steps | External reporter | Must be safe and minimal |
| Logs or traces | Text | Reporter or maintainer | Remove secrets and PII |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Fix | Code and tests | `src/**`, `web/**` | CI gates and contract tests |
| Advisory | GitHub advisory | GitHub | Maintainer-reviewed |
| Remediation notes | Markdown | `docs/security/` | Governed-doc standards |

### Sensitivity and redaction
- Do not include secrets, tokens, private keys, or credentials in reports.
- Do not include PII or restricted location coordinates. If needed to demonstrate impact, use generalized locations or synthetic examples.
- If a report involves culturally sensitive knowledge, treat it as high sensitivity and follow sovereignty rules for redaction and generalization.

### Quality signals
- A report is reproducible with minimal steps and clearly states impact.
- Fixes include regression tests.
- Changes that affect catalogs, graph, APIs, or UI maintain contract integrity and do not introduce data leakage.

## 🛡️ Vulnerability reporting

### Preferred reporting channel
1. **Use GitHub Security Advisories** (preferred):
   - Open a private advisory or use the repository’s “Report a vulnerability” workflow if available.
2. If private reporting is not available:
   - Open a public issue **only to request a private channel**, and **do not** include exploit details, sensitive data, or PoC content.

### What to include in a report
- A clear description of the issue and why it is a security risk
- Impact assessment
- Affected component paths (for example: `src/server/`, `web/`, `src/pipelines/`, `schemas/`, `data/`)
- Exact version, tag, or commit SHA tested
- Reproduction steps and a minimal PoC if applicable
- Suggested mitigation or patch if available

### What not to include in a report
- Secrets, credentials, access tokens, or private keys
- Full copies of sensitive datasets, restricted location coordinates, or personal data
- Destructive payloads

### Supported versions

| Version | Supported | Notes |
|---|---:|---|
| `main` | ✅ | Security fixes land here first |
| Latest release tag | ✅ | Best-effort backports when feasible |
| Older releases | ❌ | Upgrade recommended |

### Maintainer response process
- Triage and reproduce the issue
- Assess severity and scope, including any data sensitivity implications
- Develop and test a fix with regression coverage
- Coordinate a disclosure timeline with the reporter
- Publish an advisory and release notes when a fix is available

### Researcher guidelines
- Act in good faith and avoid privacy violations or service disruption.
- Test only against systems you control or have explicit authorization to test.
- Do not publicly disclose details until a fix is available or a coordinated plan is agreed.

## 🌐 STAC, DCAT and PROV alignment

### STAC
If a vulnerability affects published STAC assets (for example: malicious or sensitive content in an asset), remediation may include:
- Deprecating or replacing affected Items or Assets
- Updating metadata to reflect corrected lineage and access rules

### DCAT
If a dataset listing requires correction after remediation:
- Update the dataset record to reflect changes in access, redaction, or corrected assets

### PROV-O
For incidents involving data corrections or redactions:
- Record remediation as a provenance activity so downstream consumers can trace changes

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest and normalize data | Config and run logs |
| Catalogs | STAC/DCAT/PROV generation | JSON and validators |
| Graph | Entity linkage and provenance | API-mediated access |
| APIs | Contract-first serving and redaction | REST/GraphQL |
| UI | Map and narrative experience | API calls |
| Story Nodes | Curated narrative docs | Provenance-linked evidence |
| Focus Mode | Contextual synthesis | Provenance-linked bundles |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver and changelog |
| API contracts | `src/server/contracts/` | Contract tests required |
| UI layer registry | `web/**/layers/**` | Schema-validated |

### Extension points checklist
- [ ] Data: sensitive domains flagged and handled
- [ ] STAC: collections and items validate and do not expose restricted data
- [ ] PROV: remediation activity and agent identifiers recorded when applicable
- [ ] Graph: affected labels and relations reviewed and migrated safely
- [ ] APIs: auth, redaction, and rate limits reviewed; contract tests updated
- [ ] UI: no injection or leakage; accessibility and security checks pass
- [ ] Focus Mode: provenance rules preserved
- [ ] Telemetry: security-relevant signals updated if introduced

## 🧠 Story Node and Focus Mode integration

### How this work surfaces in Focus Mode
- Vulnerabilities in Story Node rendering, citation handling, or asset loading can directly impact Focus Mode safety and trust.
- Fixes that change narrative or citation rendering must preserve provenance linkage and redaction rules.

### Provenance-linked narrative rule
- Every factual claim shown to users must trace to a dataset, record, or asset identifier.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation and CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV and other schemas)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks
- [ ] Security and sovereignty checks when applicable

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run unit/integration tests
# 2) validate schemas (schemas/, data/stac/, data/catalog/dcat/, data/prov/)
# 3) run doc lint / markdown checks
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| vulnerability_reported | Reporter / GitHub | `docs/telemetry/` + `schemas/telemetry/` |
| security_fix_released | Maintainers | `docs/telemetry/` + release notes |
| sensitive_data_redaction | Governance / pipeline | `data/prov/` + audit logs |

## ⚖ FAIR+CARE & Governance

### Review gates
- Security policy updates: maintainers and governance owners
- Changes affecting sensitive knowledge or redaction: sovereignty review required
- New public endpoints or auth changes: additional review recommended

### CARE and sovereignty considerations
- Follow `docs/governance/SOVEREIGNTY.md` for any restricted or culturally sensitive locations or knowledge.
- Prefer generalization and minimization over disclosure; log redaction actions for traceability where required.

### AI usage constraints
- This document’s AI permissions and prohibitions are defined in front-matter and must remain consistent with intended use.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial security policy draft | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

