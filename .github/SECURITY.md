---
title: "Kansas Frontier Matrix — Security Policy & Vulnerability Disclosure"
path: ".github/SECURITY.md"
version: "v12.0.0-draft"
last_updated: "2025-12-18"
status: "draft"
doc_kind: "Policy"
license: "CC-BY-4.0 (code is MIT in repo root unless stated otherwise)"
markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP v2.0"
ontology_protocol_version: "KFM-OP v2.1"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v1.0.0"
dcat_profile: "KFM-DCAT v1.0.0"
prov_profile: "KFM-PROV v1.0.0"
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/ethics/ETHICS.md"
sovereignty_policy: "docs/policies/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"
doc_uuid: "urn:kfm:doc:security-policy:v12.0.0-draft"
semantic_document_id: "kfm.doc.security-policy.v12.0.0-draft"
event_source_id: "kfm.repo.commit.<sha>"
commit_sha: "<latest-commit-hash>"
ai_transform_permissions: "summarize|classify|extract|transform"
ai_transform_prohibited: "generate_policy|legal_advice|security_claims_without_citation"
doc_integrity_checksum: "<sha256-of-content>"
---

# Kansas Frontier Matrix — Security Policy & Vulnerability Disclosure

## 🧭 Overview

### 🎯 Purpose

This document provides a clear, governed, FAIR+CARE-aligned process for handling vulnerabilities, supply-chain risks, incident response, and ethical security concerns across the KFM ecosystem (ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode).  

**This is the high-level policy.** Deeper technical standards and procedures live under `docs/security/`.

### 🧩 Scope

**In scope**
- Source code, workflows, configs, schemas, and documentation in this repository.
- KFM pipeline stages and governed artifacts:
  - ETL outputs and logs that ship with the repo
  - STAC/DCAT/PROV catalogs and schemas
  - Graph + ontology schema artifacts
  - APIs (REST/GraphQL) and contract surfaces
  - Frontend/UI layer registry and map rendering logic
  - Story Nodes + Focus Mode narrative features (including AI-assisted outputs)

**Out of scope**
- Vulnerabilities in third-party services not controlled by the project (unless KFM misconfiguration is involved).
- Issues requiring physical access.
- Social engineering against maintainers (reporting these is still appreciated, but remediation may be limited).

### 👥 Audience

- Security researchers / responsible reporters
- Maintainers and reviewers
- Contributors implementing fixes
- Downstream users who need to know how security updates are communicated

### 🔑 Definitions

- **Vulnerability:** A weakness that impacts confidentiality, integrity, or availability of KFM code/data/artifacts.
- **Coordinated disclosure:** Private reporting → fix → public advisory (if applicable).
- **Sensitive data / sensitive location:** Any data restricted by governance and sovereignty rules; may include precise coordinates, cultural knowledge, or protected ecological/habitat information.
- **Provenance-only content (Focus Mode):** Narratives must not appear without a source link; sensitive details may be blurred/generalized per CARE.

### ✅ Definition of Done (for this document)

- [ ] Front matter is present and accurate (version, status, refs).
- [ ] Reporting channel(s) are clearly described and workable.
- [ ] Supported versions are stated.
- [ ] Disclosure workflow is stated, including advisory publishing expectations.
- [ ] Severity + remediation targets are referenced (or defined).
- [ ] Links to deeper standards exist (`docs/security/`).
- [ ] AI/data sovereignty safety is explicitly in scope.
- [ ] A changelog exists and review cadence is defined.

---

## 🚨 Reporting a Vulnerability (Quick Start)

**Please do not open public issues for security vulnerabilities.**

Preferred path:
1. Go to this repository’s **Security** tab
2. Open **Security Advisories**
3. Use **“Report a vulnerability”** (Private Vulnerability Reporting)

Alternative path (if you cannot use GitHub PVR):
- Email: **`<security-contact-email@domain>`** (TBD — maintainers must set this)

### What to include in a report

- Clear description of the issue and potential impact
- Steps to reproduce (minimal, safe)
- Affected versions/commit SHA (if known)
- Proof-of-concept (PoC) **that avoids real sensitive data**
- Any suggested fix or mitigation

### What NOT to include

- Secrets, tokens, credentials, or private keys
- Personal data (PII)
- Precise coordinates or details for protected/sensitive locations
- Instructions aimed at causing harm or exploitation in the wild

If your report involves **sensitive datasets, cultural sovereignty concerns, or AI narrative safety** (e.g., “Focus Mode reveals protected location detail”), report it through the same channels and explicitly label it as **SOVEREIGNTY / CARE SENSITIVE**.

---

## 🔎 Supported Versions

KFM prioritizes security fixes on the **default branch** and the **latest stable release line**.

| Version / Branch | Security Fixes | Notes |
|---|---:|---|
| `main` (default branch) | ✅ Yes | Fixes land here first |
| Latest stable release (tagged) | ✅ Yes | Recommended for most users |
| Older releases / archived branches | ❌ No | Upgrade to receive fixes |

If the project introduces an LTS branch, this table must be updated.

---

## 📌 Security Advisories, CVEs, and Public Notifications

- Verified vulnerabilities are handled privately until fixed.
- After a fix is released, maintainers will publish a **Security Advisory** describing the impact and remediation steps.
- For significant issues, maintainers may request a **CVE** to ensure downstream tooling can alert users.

---

## 🔄 Disclosure Process and Timeline

### Coordinated disclosure (expected flow)

- **Acknowledge**: Maintainers confirm receipt (as quickly as possible).
- **Triage**: Confirm impact and severity; identify affected components.
- **Fix**: Patch and validate; apply defense-in-depth where appropriate.
- **Release**: Ship fix to supported version(s).
- **Advisory**: Publish a Security Advisory (and CVE if applicable).
- **Credit**: Credit reporter(s) unless anonymity is requested.

### Fallback public disclosure timeline

If a reported issue cannot be resolved quickly, KFM follows a coordinated disclosure approach and may adopt a **90-day maximum disclosure** fallback (coordinated with the reporter) to align expectations and avoid indefinite silence.

---

## 🧱 Core Security Principles

KFM security posture is guided by the following non-negotiable principles:

- **Least Privilege**: Minimal permissions for CI and accounts.
- **Defense in Depth**: Multiple, layered controls (schemas, static analysis, CI gates, artifact integrity verification).
- **Secure Defaults**: Conservative defaults (e.g., protected branches, restricted automation tokens).
- **No Secrets in Repo**: Secrets belong in secret vaults or secure CI secret stores.
- **Privacy & Sovereignty by Design**: Avoid PII; apply masking/generalization per FAIR+CARE.
- **AI & Narrative Safety**: AI-generated content must be grounded in real data and respect cultural constraints; no hallucinated or unsourced narrative is allowed in provenance-only contexts.

---

## 🧬 Severity and Remediation Targets (Policy-Level)

KFM uses a CVSS-inspired severity scheme: **Critical / High / Medium / Low**.

Target remediation SLAs are defined in `docs/security/vulnerability-management.md`.  
At minimum, **Critical** issues target patching within **24 hours** (where feasible).

---

## 🔗 Supply Chain Integrity and Release Security

KFM enforces strict supply-chain controls to reduce compromise risk:

- **SBOMs for releases** (SPDX 2.3)
- **SLSA-style provenance attestations**
- **Artifact signing** (e.g., Sigstore/Cosign)
- **Dependency scanning** (e.g., OSV Scanner, Grype, Trivy)
- Checks for dependency confusion or malicious package scripts
- A hardened posture against risky NPM lifecycle scripts (documented as a standard)

Artifacts that fail integrity or policy checks must not be released.

---

## 🧪 Threat Modeling and Secure Development

- Threat modeling follows **STRIDE** (security) and **LINDDUN** (privacy).
- Developer-facing secure coding guidance should be maintained under `docs/security/` (e.g., OWASP Top 10 / ASVS mapping where applicable).
- Security-sensitive changes may require additional review sign-offs per governance rules.

---

## 🧯 Incident Response

Incident response follows an established lifecycle approach (Detection → Analysis → Containment → Eradication → Recovery → Postmortem).

- Incident reports and postmortems live under `docs/security/reports/` (or the repository’s designated incident-report location).
- After incidents, KFM updates relevant governance documents, SBOMs, and controls to prevent recurrence.

---

## 📁 Directory Layout

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 🛡️ SECURITY.md

📁 docs/
└── 🔐 security/
    ├── 📄 README.md
    ├── 📄 <threat-model>.md
    ├── 📄 <supply-chain>.md
    ├── 📄 <vulnerability-management>.md
    ├── 📄 <incident-response>.md
    └── 📁 reports/
        └── 📁 <incidents>/
            └── 📄 YYYY-MM-DD-incident.md
~~~

### Related repository paths

- `.github/SECURITY.md` (this policy)
- `docs/security/` (normative standards and procedures)
- `docs/governance/ROOT_GOVERNANCE.md` (roles and approvals)
- `docs/policies/SOVEREIGNTY.md` (data sovereignty requirements)

### Directory governance rules

- Policy changes require review by the maintainers and the project’s security governance roles (as defined in the Governance Charter).
- Policy updates must not weaken protections for sensitive data or sovereignty constraints.

---

## 🧭 Context

### Background

KFM’s end-to-end pipeline and narrative features (Story Nodes / Focus Mode) make security broader than “code vulns”:
- Integrity and provenance of catalogs matter
- AI safety includes preventing harmful inferences (e.g., sensitive location revelation)
- Sovereignty and CARE constraints are treated as security concerns, not optional ethics

### Assumptions

- The repository uses GitHub Security Advisories / PVR for private intake.
- CI enforces gated validation before merge/release.

### Constraints / invariants

- The canonical pipeline order is fixed (ETL → catalogs → graph → APIs → UI → stories).
- Frontend must not bypass APIs to access protected graph data.
- Provenance-only contexts must not display unsourced narrative.

### Open questions (must be resolved to promote status to “active”)

- Confirm the official security contact email and any PGP key.
- Confirm exact supported release line(s) and any LTS/EoL policy.
- Confirm the full SLA matrix for High/Medium/Low severities in `docs/security/vulnerability-management.md`.

### Future extensions (non-binding)

- Add SBOM drift checks on releases (SBOM diffing)
- Add automated dependency update tooling (e.g., Dependabot/Renovate) if desired
- Add SAST/DAST/fuzzing policy references and CI implementation details

---

## 🗺️ Diagrams (Mermaid where possible)

### Vulnerability disclosure flow

~~~mermaid
flowchart TD
  A[Reporter finds potential vuln] --> B[Private report via GitHub PVR / Security Advisory]
  B --> C[Maintainer acknowledgement]
  C --> D[Triage + severity classification]
  D --> E[Fix + tests + integrity checks]
  E --> F[Release patch to supported versions]
  F --> G[Publish Security Advisory (+ CVE if applicable)]
  G --> H[Credit reporter (optional)]
~~~

### Secure release gates (conceptual)

~~~mermaid
flowchart LR
  C[Commit/PR] --> CI[CI gates: tests + schema validation + scans]
  CI --> SBOM[Generate SBOM]
  SBOM --> Prov[Generate provenance attestation]
  Prov --> Sign[Sign artifacts]
  Sign --> Rel[Release]
  Rel --> Adv[Advisory (if security fix)]
~~~

---

## 📦 Data & Metadata

### Inputs

- Vulnerability reports (private)
- Dependency scan findings
- CI security gate outputs
- Incident telemetry (when applicable)

### Outputs

- Patches / releases
- Security advisories (and CVEs where applicable)
- SBOMs and provenance attestations
- Postmortems and remediation tasks

### Sensitivity & redaction

- Never include secrets, PII, or restricted coordinates in public issues, logs, or advisories.
- When security issues involve protected sites or sovereignty-sensitive knowledge, prefer generalization and redaction over disclosure.

---

## 🧾 STAC/DCAT/PROV alignment (when applicable)

Security and integrity expectations extend to KFM catalogs and provenance:

- Catalog and provenance artifacts must preserve integrity (validation + release controls).
- Sensitive data handling must propagate into metadata (e.g., sensitivity classification, redaction rules).
- Provenance should support forensic analysis without leaking restricted information.

---

## Versioning & Change Control

### Changelog

- **v12.0.0-draft (2025-12-18)** — Drafted/standardized to the governed Universal Doc template; includes supported-versions table and a 90-day disclosure fallback; clarifies advisory publishing expectations.

### Review cadence

- Review at least annually, and upon major release milestones or security program changes.