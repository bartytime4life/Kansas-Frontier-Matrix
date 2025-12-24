---
title: "KFM Security Policy"
path: ".github/SECURITY.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:github:security-policy:v1.0.0"
semantic_document_id: "kfm-security-policy-v1.0.0"
event_source_id: "ledger:kfm:doc:github:security-policy:v1.0.0"
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

# KFM Security Policy

> **Purpose (required):** Provide a **private, safe process** for reporting security vulnerabilities affecting Kansas Frontier Matrix (KFM), and define how maintainers triage, remediate, and coordinate disclosure across the full KFM pipeline (ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode).

**Do not open public GitHub issues for security vulnerabilities.**  
Use a private channel as described in “Reporting a vulnerability.”

## 📘 Overview

### Purpose
- Define how to **report**, **triage**, **remediate**, and **disclose** security vulnerabilities affecting KFM.
- Set baseline expectations for protecting **sensitive content** and reducing risk across the full pipeline (ETL → catalogs → graph → APIs → UI → Story/Focus Mode).
- Make security handling consistent with **FAIR+CARE** governance (including sovereignty/redaction rules).

### Scope

| In Scope | Out of Scope |
|---|---|
| Vulnerabilities in repo code, workflows, configs, schemas, release artifacts, and documentation that impact confidentiality/integrity/availability | General product questions/support requests |
| Exposure of sensitive/culturally restricted data (e.g., precise coordinates that should be generalized/redacted) | Vulnerabilities in third-party services not operated by the project (unless triggered by repo misconfiguration) |
| Authn/authz, rate limiting, injection, SSRF, XSS, CSRF, secrets leakage, dependency/supply-chain risk | Social engineering, physical attacks, or issues requiring physical access |
| Security issues in Focus Mode / narrative surfacing (e.g., unintended data leakage; unsafe asset loading) | Denial-of-service testing without explicit written permission |
| CI/workflow misconfigurations that could expose secrets or enable malicious builds | Feature requests that do not present a security risk |

### Audience
- Primary: security researchers, maintainers, contributors.
- Secondary: data stewards/governance reviewers, operators of deployments, downstream integrators.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Vulnerability**: a weakness that can be exploited to compromise confidentiality, integrity, or availability.
  - **Incident**: confirmed exploitation or data exposure requiring containment and notification steps.
  - **Coordinated disclosure**: private reporting and fix coordination before public disclosure.
  - **Sensitive content**: restricted data or culturally sensitive knowledge requiring redaction/generalization.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Security policy (canonical) | `.github/SECURITY.md` | Maintainers | This document |
| Security docs (optional deeper standards) | `docs/security/` | Maintainers | Threat model, incident playbooks, scanning standards |
| Reporting channel (preferred) | GitHub “Security Advisories” | Maintainers | Use private disclosure workflow (if enabled) |
| Governance references | `docs/governance/*` | Governance reviewers | Sovereignty/Ethics/CARE constraints |
| Telemetry governance | `docs/telemetry/` + `schemas/telemetry/` | Maintainers | Optional observability + security metrics |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Reporting guidance is unambiguous (private first; no public exploit details)
- [ ] Sensitive-data handling rules (redaction/generalization) are explicit
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] “TBD” placeholders reviewed and finalized by maintainers

---

### Supported versions
KFM support policy can vary by release cadence. Until maintainers define it:
- **Supported:** default branch (`main`) and the most recent tagged release (**TBD — confirm release strategy**).
- **Unsupported:** unmaintained forks / untagged historical snapshots unless explicitly noted.

---

## 🛡️ Vulnerability reporting

### Reporting a vulnerability

**Please do not open a public GitHub issue** for security-sensitive reports.

Preferred reporting path:
1. Use the repository’s **Security Advisories** workflow (private reporting / draft advisory), if enabled.
2. If advisories are not available, open a **public issue only to request a private channel**, and **do not** include exploit details, sensitive data, or PoC content.

Alternate reporting path (only if advisories are unavailable):
- Email: **TBD — add project security contact**
- Encryption: **TBD — publish PGP key fingerprint (optional)**

### What to include in a report
- A clear description of the issue and why it is a security concern
- Affected component(s): ETL / catalogs / graph / API / UI / Story/Focus Mode / CI workflows
- Affected paths (examples: `src/pipelines/`, `schemas/`, `src/graph/`, `src/server/`, `web/`, `.github/workflows/`)
- Exact version, tag, or commit SHA tested
- Reproduction steps (minimal, safe proof-of-concept preferred)
- Expected vs actual behavior
- Potential impact and any known exploitation conditions
- Suggested remediation (if you have one)
- Whether the report involves:
  - secrets/credentials exposure
  - PII exposure
  - restricted/sensitive location or cultural knowledge (so we can apply sovereignty handling immediately)

### What not to include in a report
- Secrets, credentials, access tokens, private keys, or session cookies
- Full copies of sensitive datasets, restricted location coordinates, or personal data
- Destructive payloads (e.g., irreversible deletion, ransomware-like behavior)

### Severity and response targets (TBD)
This table is a **fill-in** to make expectations explicit. Maintainership should set realistic targets.

| Severity | Examples (non-exhaustive) | Acknowledgement target | Fix / mitigation target |
|---|---|---|---|
| Critical | RCE, auth bypass, active secrets leakage, mass data exfiltration | TBD | TBD |
| High | Privilege escalation, significant sensitive-data exposure, SSRF to internal metadata | TBD | TBD |
| Medium | XSS with constraints, limited info leaks, dependency issue without clear exploit | TBD | TBD |
| Low | Hardening opportunities, non-exploitable misconfigs, low-impact issues | TBD | TBD |

### Maintainer response process
- Triage and attempt to reproduce.
- Assess severity and scope, including any **sensitivity** implications (PII / restricted location/cultural knowledge).
- Contain if active incident is suspected (rotate secrets, disable affected endpoints, restrict access).
- Develop and test a fix with regression coverage.
- Update catalogs/metadata/provenance if any artifacts are corrected/redacted (see STAC/DCAT/PROV section).
- Coordinate a disclosure timeline with the reporter.
- Publish an advisory and release notes when a fix is available (TBD: advisory publication defaults).

### Researcher guidelines
- Act in good faith and avoid privacy violations or service disruption.
- Test only against systems you control or have explicit authorization to test.
- Stop immediately if you encounter unexpected sensitive data; report privately and do not retain/share it.
- Do not publicly disclose details until a fix is available or a coordinated plan is agreed.

---

## 🗂️ Directory Layout

### This document
- `path`: `.github/SECURITY.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub governance files | `.github/` | Repo health + policy + workflows |
| Security docs (optional) | `docs/security/` | Threat model, incident response, scanning standards |
| Telemetry specs (optional) | `docs/telemetry/` + `schemas/telemetry/` | Observability + security/governance metrics |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV/telemetry/UI/story nodes) |
| Pipelines | `src/pipelines/` | ETL + catalog build logic |
| Graph | `src/graph/` | Ontology, constraints, migrations |
| API layer | `src/server/` | Contracted access (REST/GraphQL); redaction enforced here |
| UI | `web/` | Map + narrative UI; must not bypass API |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts; provenance requirements |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📄 SECURITY.md

📁 docs/
└── 📁 security/                # (optional)
    ├── 📄 threat_model.md
    ├── 📄 incident_response.md
    └── 📁 advisories/          # internal writeups if desired
~~~

---

## 🧭 Context

### Background
KFM handles historical/cultural/ecological data and includes governance constraints for sensitive or culturally restricted content. Security includes both conventional software vulnerabilities and risks of unintended sensitive-data exposure through catalogs, APIs, UI layers, and narrative surfacing.

### Assumptions
- The project uses GitHub and can accept private vulnerability reports via Security Advisories (if enabled).
- “TBD” values (contact email, SLAs, encryption keys, supported versions) require maintainer confirmation.

### Constraints / invariants
- Security fixes must preserve KFM’s canonical architecture ordering: ETL → catalogs → graph → APIs → UI → story/focus.
- UI must not access the graph directly; all access is mediated via the API layer and its redaction/authorization rules.
- Focus Mode outputs must remain provenance-linked; no unsourced or fabricated narrative.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the official security contact email? | Maintainers | TBD |
| Do we publish a PGP key for vulnerability reports? | Maintainers | TBD |
| What versions/branches are supported for security fixes? | Maintainers | TBD |
| Do we publish advisories publicly by default? | Maintainers | TBD |
| Do we maintain an incident notification procedure for sensitive-data exposure? | Governance owners | TBD |

### Future extensions
- Add `docs/security/threat_model.md` (assets, actors, trust boundaries)
- Add `docs/security/incident_response.md` (severity rubric, comms plan, postmortems)
- Add CI security gates (secret scanning, SAST, dependency review) and document them

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  R[Reporter] --> C[Private reporting channel]
  C --> T[Triage + reproduce]
  T --> F[Fix + regression tests]
  F --> P[Patch release]
  P --> A[Advisory + coordinated disclosure]
~~~

~~~mermaid
sequenceDiagram
  participant Reporter
  participant Maintainers
  participant CI
  participant Release

  Reporter->>Maintainers: Private report (Security Advisory)
  Maintainers->>Maintainers: Triage + severity assessment
  Maintainers->>CI: Patch + tests + validation
  CI-->>Maintainers: Checks pass/fail
  Maintainers->>Release: Merge + release notes/advisory (as appropriate)
  Release-->>Reporter: Credit (optional) + disclosure coordination
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Vulnerability report | Advisory text | GitHub Security Advisories | Completeness checklist (above) |
| Secrets leakage alert | Tool output | CI security gates (if enabled) | Verified secret rotation steps |
| Dependency alert | Advisory feed | Dependency tooling (if enabled) | Severity + affected versions |
| Sensitive-data exposure report | Narrative + examples | Users/governance reviewers | Verify classification + redaction rules |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Patch | Code | repo | Tests + CI gates |
| Advisory | Markdown | GitHub Security Advisory | Coordinated disclosure rules |
| Regression tests | Code | `tests/` | Test framework + CI |
| Incident note (optional) | Markdown | `docs/security/…` | Markdown protocol checks |

### Sensitivity & redaction
- Do not publish exploit details or sensitive examples (especially exact locations) until remediation and governance review are complete.
- If sensitive location/cultural data is involved, prefer generalized geometry, redacted examples, and private handling.
- If a report contains restricted content, maintainers should treat it as **high sensitivity** until reviewed under sovereignty policy.

### Quality signals
- Reproducible steps using minimal safe proof-of-concept
- Clear affected component + version/commit range
- Fix includes tests and validation steps
- No new secrets introduced; no new data leakage pathways

### Telemetry signals (recommended; align to `docs/telemetry/` + `schemas/telemetry/` if adopted)
| Signal | Source | Where recorded |
|---|---|---|
| `vulnerability_reported` | Reporter / GitHub | Security advisory + optional telemetry |
| `security_fix_released` | Maintainers | Release notes + optional telemetry |
| `sensitive_data_redaction` | Governance / pipeline | `data/prov/` + audit notes (if adopted) |

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
If a vulnerability affects published STAC artifacts (for example: malicious content in an asset, or sensitive content that should not be public), remediation may include:
- Deprecating or replacing affected Items/Assets
- Rebuilding derived artifacts that referenced the affected asset
- Ensuring corrected STAC validates against the project profile

### DCAT
If a dataset listing requires correction after remediation:
- Update the dataset record to reflect changes in access, redaction, or corrected assets
- Ensure any distribution links do not expose restricted content

### PROV-O
For incidents involving data corrections or redactions:
- Record remediation as a provenance activity (where adopted) so downstream consumers can trace changes
- Ensure lineage does not “downgrade” sensitivity (outputs must not be less restricted than inputs)

### Versioning
- Security-related changes should be traceable to commits/releases and (if advisories are published) cross-referenced.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Graph build + API-mediated access |
| APIs | Serve contracts + enforce redaction | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Provenance-linked evidence |
| Focus Mode | Contextual synthesis | Provenance-linked bundles |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API contracts | `src/server/contracts/` (or repo-specific) | Contract tests required |
| UI layer registry | `web/**/layers/**` | Schema-validated; no direct graph access |

### Extension points checklist (for future work)
- [ ] Telemetry: add security signals + schema version bump
- [ ] APIs: define explicit redaction behaviors for sensitive classes
- [ ] CI: add/strengthen security scanning gates and document them
- [ ] Governance: define incident review + approval workflow

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Security constraints should prevent Focus Mode or story rendering from:
- exposing restricted datasets/locations
- presenting non-provenanced claims as fact
- bypassing API-layer redaction/authorization
- loading untrusted remote assets unsafely (where applicable)

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Validation steps (recommended)
- [ ] Markdown protocol checks (lint + fences)
- [ ] Schema validation (STAC/DCAT/PROV and other schemas, as applicable)
- [ ] Graph integrity checks (as applicable)
- [ ] API contract tests (as applicable)
- [ ] UI schema checks (layer registry) (as applicable)
- [ ] Secret scanning (recommended)
- [ ] PII/sensitive-location scanning for public outputs (recommended)

### Reproduction (deterministic)
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run unit/integration tests
# 2) validate schemas (schemas/, data/stac/, data/catalog/dcat/, data/prov/)
# 3) run doc lint / markdown checks
~~~

---

## ⚖ FAIR+CARE & Governance

### Review gates
Security fixes that affect:
- authentication/authorization
- redaction/generalization rules
- public-facing endpoints
- sensitive datasets/layers
should receive governance review per the referenced governance documents.

### CARE / sovereignty considerations
- Identify impacted communities and apply protection rules for restricted locations and culturally sensitive knowledge.
- Prefer least-privilege access, careful redaction, and documented justification for any exposure.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use.
- Do not use AI to infer or reconstruct sensitive locations or restricted knowledge.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Expanded SECURITY.md scaffold: clarified reporting paths, added response process, STAC/DCAT/PROV remediation guidance, and recommended telemetry signals | TBD |

---

## Footer refs (do not remove)
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---
