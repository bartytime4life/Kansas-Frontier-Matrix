---
title: "KFM Security Policy"
path: ".github/SECURITY.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

## 📘 Overview

### Purpose
- Define how to **report**, **triage**, **remediate**, and **disclose** security vulnerabilities affecting Kansas Frontier Matrix (KFM).
- Set baseline expectations for protecting **sensitive content** and reducing risk across the full pipeline (ETL → catalogs → graph → APIs → UI → Story/Focus Mode).

### Scope

| In Scope | Out of Scope |
|---|---|
| Vulnerabilities in repo code, workflows, configs, schemas, and documentation that impact confidentiality/integrity/availability | General product questions/support requests |
| Exposure of sensitive/culturally restricted data (e.g., precise coordinates that should be generalized/redacted) | Vulnerabilities in third-party services not operated by the project (unless triggered by repo misconfiguration) |
| Authn/authz, rate limiting, injection, SSRF, XSS, CSRF, secrets leakage, dependency risk | Social engineering, physical attacks, or issues requiring physical access |
| Supply-chain issues (malicious deps, compromised build artifacts) | Denial-of-service testing without explicit written permission |
| Security issues in Focus Mode / narrative surfacing (e.g., unintended data leakage) | Feature requests that do not present a security risk |

### Audience
- Primary: security researchers, maintainers, contributors.
- Secondary: data stewards/governance reviewers, operators of deployments, downstream integrators.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Vulnerability**: a weakness that can be exploited to compromise confidentiality, integrity, or availability.
  - **Coordinated disclosure**: private reporting and fix coordination before public disclosure.
  - **Sensitive content**: restricted data or culturally sensitive knowledge requiring redaction/generalization.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Security policy | `.github/SECURITY.md` | Maintainers | This document |
| Security documentation | `docs/security/` | Maintainers | Optional deeper standards (threat model, incident playbooks) |
| Reporting channel (preferred) | GitHub “Security Advisories” | Maintainers | Use private disclosure workflow |
| Governance references | `docs/governance/*` | Governance reviewers | Sovereignty/Ethics/CARE constraints |
| Telemetry governance | `docs/telemetry/` + `schemas/telemetry/` | Maintainers | Optional observability + security metrics |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Reporting guidance is unambiguous (private first; no public exploit details)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] “TBD” placeholders reviewed and finalized by maintainers

---

### Supported versions
KFM support policy can vary by release cadence. Until defined:
- **Supported:** default branch and the most recent tagged release (**TBD — confirm repo release strategy**).
- **Unsupported:** unmaintained forks / untagged historical snapshots unless explicitly noted.

---

### Reporting a vulnerability

**Please do not open a public GitHub issue** for security-sensitive reports.

Preferred reporting path:
1. Use the repository’s **Security Advisories** workflow (private reporting / draft advisory).
2. Include the details below (“What to include”).

Alternate reporting path (only if advisories are unavailable):
- Email: **TBD — add project security contact**
- Encryption: **TBD — publish PGP key fingerprint (optional)**

#### What to include in a report
- A clear description of the issue and why it is a security concern
- Affected component(s): ETL / catalogs / graph / API / UI / Story/Focus Mode / CI workflows
- Reproduction steps (minimal, safe proof-of-concept preferred)
- Expected vs actual behavior
- Potential impact and any known exploitation conditions
- Suggested remediation (if you have one)
- Whether the report includes **sensitive location data** or restricted cultural knowledge (so we can apply redaction handling immediately)

#### What happens next
- Maintainers will evaluate severity and coordinate remediation privately.
- Fixes should include tests and/or validation steps to prevent regression.
- If/when public disclosure occurs, the project may publish a short advisory and optionally credit the reporter (by request).

---

## 🗂️ Directory Layout

### This document
- `path`: `.github/SECURITY.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub governance files | `.github/` | Repo health + policy + workflows |
| Security docs (optional) | `docs/security/` | Threat model, incident response, scanning standards |
| Telemetry specs | `docs/telemetry/` + `schemas/telemetry/` | Observability + security/governance metrics |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV/telemetry) |
| Pipelines | `src/pipelines/` | ETL + catalog build logic |
| Graph | `src/graph/` | Ontology, constraints, migrations |
| API layer | `src/server/` (or repo-specific) | Contracted access (REST/GraphQL); redaction enforced here |
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
KFM is designed to handle historical/cultural/ecological data and includes governance constraints for sensitive or culturally restricted content. Security therefore includes both conventional software vulnerabilities and risks of unintended sensitive-data exposure.

### Assumptions
- The project uses GitHub and can accept private vulnerability reports via Security Advisories.
- “TBD” values (contact email, SLAs, encryption keys, supported versions) require maintainer confirmation.

### Constraints / invariants
- Security fixes must preserve KFM’s canonical architecture ordering (ETL → catalogs → graph → APIs → UI → story/focus).
- UI must not access the graph directly; all access is mediated via the API layer and its redaction/authorization rules.
- Focus Mode outputs must remain provenance-linked; no unsourced or fabricated narrative.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the official security contact email? | Maintainers | TBD |
| Do we publish a PGP key for vulnerability reports? | Maintainers | TBD |
| What versions/branches are supported for security fixes? | Maintainers | TBD |
| Do we publish advisories publicly by default? | Maintainers | TBD |

### Future extensions
- Add `docs/security/threat_model.md` (assets, actors, trust boundaries)
- Add `docs/security/incident_response.md` (severity rubric, comms plan, postmortems)
- Add CI security gates (secret scanning, SAST, dependency review) and document them

---

## 🗺️ Diagrams

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
| Vulnerability report | Advisory text | GitHub Security Advisories | Completeness checklist (below) |
| Secrets leakage alert | Tool output | CI security gates (if enabled) | Verified secret rotation steps |
| Dependency alert | Advisory feed | Dependency scanning tooling | Severity + affected versions |
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

### Quality signals
- Reproducible steps using minimal safe proof-of-concept
- Clear affected component + version/commit range
- Fix includes tests and validation steps
- No new secrets introduced; no new data leakage pathways

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not directly applicable (policy doc), but incidents involving catalog artifacts should reference the affected STAC collection/item IDs.

### DCAT
- Not directly applicable (policy doc), but incidents involving dataset publication should reference DCAT dataset identifiers where possible.

### PROV-O
- Not directly applicable (policy doc), but incident remediation activities may be recorded as governance artifacts if the project adopts an incident PROV pattern.

### Versioning
- Security-related changes should be traceable to commits/releases and (if advisories are published) cross-referenced.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts + enforce redaction | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Layer registry | `web/.../layers/*.json` | Schema-validated |

### Extension points checklist (for future work)
- [ ] Telemetry: add security signals + schema version bump
- [ ] APIs: define explicit redaction behaviors for sensitive classes
- [ ] CI: add/strengthen security scanning gates and document them
- [ ] Governance: define an incident review + approval workflow

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Security-related constraints should prevent Focus Mode or story rendering from:
  - exposing restricted datasets/locations
  - presenting non-provenanced claims as fact
  - bypassing API-layer redaction/authorization

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

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV) (as applicable)
- [ ] Graph integrity checks (as applicable)
- [ ] API contract tests (as applicable)
- [ ] UI schema checks (layer registry) (as applicable)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

---

## ⚖ FAIR+CARE & Governance

### Review gates
- Security fixes that affect:
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
| v1.0.0 | 2025-12-22 | Initial SECURITY.md scaffold aligned to KFM Universal Template | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
