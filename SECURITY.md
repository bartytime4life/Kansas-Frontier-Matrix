<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/2c3a0c1e-4d86-4e2f-9e2a-0c54b4c26e9a
title: KFM Security Policy
type: standard
version: v1
status: draft
owners: KFM Security Working Group (TBD)
created: 2026-03-03
updated: 2026-03-03
policy_label: public
related:
  - docs/security/threat-model.md
  - docs/security/vulnerability-management.md
  - docs/security/incident-response.md
  - docs/security/secrets-policy.md
  - docs/security/supply-chain.md
  - policy/
  - .github/workflows/
tags: [kfm, security, vuln-reporting, supply-chain, incident-response]
notes:
  - This policy is written for an evidence-first, fail-closed system.
  - Claims are explicitly labeled Confirmed / Proposed / Unknown (with verification steps for Unknown).
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🔒 Security Policy — Kansas Frontier Matrix
One-line purpose: how to report security issues + how KFM triages, fixes, and discloses them (evidence-first, fail-closed).  
**Status:** `draft` • **Owners:** `TBD` • **Location:** recommended at `.github/SECURITY.md`

[![SECURITY.md](https://img.shields.io/badge/Security-Policy-blue)](#-reporting-a-vulnerability)
[![Disclosure](https://img.shields.io/badge/Disclosure-Responsible-informational)](#-coordinated-disclosure)
[![Fail--Closed](https://img.shields.io/badge/Posture-Fail--Closed-critical)](#-security-design-principles)
[![SBOM](https://img.shields.io/badge/SBOM-SPDX-lightgrey)](#-supply-chain-security)
[![SLSA](https://img.shields.io/badge/Provenance-SLSA-lightgrey)](#-supply-chain-security)

> **Confirmed:** This repository follows (or intends to follow) a “fail-closed / deny-by-default” posture for governance and promotion gates.  
> **Proposed:** This file makes that posture explicit for security reporting, triage, and releases.  
> **Unknown:** Exact org contacts/SLAs and which GitHub security features are enabled.

---

## 🧭 Quick navigation
- [📣 Reporting a vulnerability](#-reporting-a-vulnerability)
- [🧩 What to report](#-what-to-report)
- [🗓️ Supported versions](#-supported-versions)
- [🔐 Security design principles](#-security-design-principles)
- [🧰 Supply chain security](#-supply-chain-security)
- [🗝️ Secrets and credentials](#-secrets-and-credentials)
- [🧬 Data sensitivity and privacy](#-data-sensitivity-and-privacy)
- [🚨 Incident response](#-incident-response)
- [🧪 Security testing and gates](#-security-testing-and-gates)
- [✅ Verification checklist](#-verification-checklist)

---

## 📣 Reporting a vulnerability

### Where to report

- **Proposed:** Use **GitHub Security Advisories / Private Vulnerability Reporting** for this repository (preferred when available).
- **Proposed:** If GitHub private reporting is not available, email a dedicated security alias (see below).
- **Unknown:** The canonical security email alias for this project.
  - **Smallest verification step:** confirm the maintainer-approved alias (and who monitors it) and update this file.

**Proposed security contact (placeholder):**
- Email: `security@<YOUR-DOMAIN>` (replace)
- Optional PGP key: `TBD` (replace)

### What to include in your report

- **Proposed:** Affected component(s) and version/commit.
- **Proposed:** Impact summary (what can an attacker do).
- **Proposed:** Reproduction steps that minimize harm (e.g., proof-of-concept against local/dev only).
- **Proposed:** Any indicators of active exploitation (logs, unusual traffic, etc.).
- **Proposed:** Whether the issue could expose or enable targeting of sensitive locations/datasets (see Data Sensitivity).

### Where NOT to report

- **Proposed:** Do **not** open public GitHub issues for security vulnerabilities.
- **Proposed:** Do **not** post exploit code, credentials, or sensitive data in public channels.

<a href="#top">Back to top</a>

---

## 🧩 What to report

- **Proposed:** Auth/authz bypass in governed APIs.
- **Proposed:** Data exfiltration paths (including SSRF/XXE/file-read) in pipeline tools, parsers, or extractors.
- **Proposed:** Injection issues (SQL/Cypher/command) anywhere in the stack.
- **Proposed:** Privilege escalation paths in CI/CD, runners, containers, or policy engines.
- **Proposed:** Sensitive geospatial leakage (exact coordinates, re-identification, “unmasking” without policy + audit).
- **Proposed:** Supply-chain compromise indicators (malicious dependency updates, poisoned artifacts, signature bypass).

<a href="#top">Back to top</a>

---

## 🗓️ Supported versions

> **Unknown:** This repo’s release/versioning scheme (tags, release branches, support windows).
> - **Smallest verification step:** confirm whether KFM publishes versioned releases (e.g., `vX.Y.Z`) and which branches are maintained.

**Proposed support policy (until verified):**
- **Proposed:** `main` (or `trunk`) is supported.
- **Proposed:** The latest tagged release is supported.
- **Proposed:** Older releases receive security fixes if they are within an explicit support window (TBD).

Example table (edit once verified):

| Version / Branch | Supported | Notes |
|---|---:|---|
| `main` | ✅ (Proposed) | Security fixes land here first |
| `release/*` | ❓ (Unknown) | Define which release branches exist |
| `<latest tag>` | ✅ (Proposed) | Pin a real tag once releases exist |

<a href="#top">Back to top</a>

---

## 🔐 Security design principles

### Governance posture

- **Confirmed:** Policy evaluation is intended to be **deny-by-default** and **fail-closed** (if a gate fails, promotion stops).  
- **Confirmed:** Policy gates are expected to run in CI (e.g., Conftest/OPA) and hard-fail on DENY.  
- **Proposed:** The same “deny-by-default” posture applies to security disclosures: if unsure whether something is sensitive, treat it as sensitive and route privately.

### Trust boundary and API invariants

- **Confirmed:** Clients/UI must not access databases or storage directly; access crosses a governed API and policy boundary.
- **Confirmed:** Core logic must not bypass the repository/adapter layer to reach storage.
- **Proposed:** Any new externally exposed endpoint requires a threat model entry before release.

### Evidence-first security

- **Proposed:** Security-relevant decisions (triage, severity, remediation acceptance) must be recorded as “evidence artifacts” (issue/advisory references, receipts, test evidence, SBOM deltas).
- **Proposed:** If a vulnerability affects data governance obligations, access may be restricted until mitigations are deployed.

<a href="#top">Back to top</a>

---

## 🧰 Supply chain security

- **Proposed:** Releases should be accompanied by:
  - **SBOM** (SPDX or CycloneDX)
  - **Provenance/attestations** (SLSA / in-toto)
  - **Vulnerability scanning results** (dependency + container)

- **Proposed:** Dependency update tooling (e.g., Dependabot) should be enabled, but security PRs must not be auto-merged for high-risk components (manual review required).

- **Unknown:** Which scanners and CI workflows are currently installed/enforced.
  - **Smallest verification step:** confirm whether CodeQL/Trivy/osv-scanner/Dependabot are enabled and which are “required checks” in GitHub branch protection.

<a href="#top">Back to top</a>

---

## 🗝️ Secrets and credentials

- **Confirmed:** Secrets must not enter the repository.
- **Proposed:** Use least-privilege tokens; prefer short-lived credentials and OIDC in CI where possible.
- **Proposed:** Rotate credentials immediately after suspected exposure and treat as a security incident.

- **Unknown:** The current secret scanning configuration.
  - **Smallest verification step:** verify whether GitHub secret scanning / push protection is enabled (or alternative tooling), and document it here.

<a href="#top">Back to top</a>

---

## 🧬 Data sensitivity and privacy

- **Confirmed:** KFM applies governance controls to prevent sensitive-data exposure (including geoprivacy-style masking and redaction obligations before publishing).
- **Proposed:** Vulnerabilities that could expose sensitive locations, cultural heritage, Indigenous sovereignty-related data, or protected ecological sites are treated as **High/Critical** by default until proven otherwise.

- **Proposed:** When reporting issues that touch sensitive data:
  - Use **private channels** only.
  - Avoid including real coordinates or identifiers in reports; use synthetic examples when possible.
  - Include “potential community harm” considerations as part of impact.

<a href="#top">Back to top</a>

---

## 🚨 Incident response

- **Confirmed:** KFM expects an incident response framework integrated with threat modeling, vulnerability management, secrets policy, and supply-chain practices.
- **Proposed:** Security incidents follow: detect → contain → eradicate → recover → postmortem.
- **Unknown:** The on-call/response roster and the canonical incident commander rotation.
  - **Smallest verification step:** identify maintainers responsible for incident response and publish the escalation path.

<a href="#top">Back to top</a>

---

## 🧪 Security testing and gates

### CI “fail closed” gate

- **Confirmed:** CI gates are expected to run policy tests and **fail the job on DENY** (fail-closed).
- **Proposed:** Security-critical checks should be required checks on protected branches.

Example (pseudocode):

~~~bash
# Evaluate policy bundle against artifacts/receipts; deny-by-default
conftest test receipts/run_receipt.json --policy policies
# If DENY -> exit non-zero -> block merge/promotion
~~~

### Emergency deny (“kill switch”)

- **Confirmed:** A synthetic “emergency deny” policy toggle is a valid pattern to verify the entire stack fails closed and the trust boundary holds.
- **Proposed:** When exploitation is suspected, enable emergency deny for promotion/publishing until containment is complete.

<a href="#top">Back to top</a>

---

## 🧾 Coordinated disclosure

- **Proposed:** We aim to acknowledge reports quickly and coordinate a fix + disclosure timeline with the reporter.
- **Unknown:** Explicit SLA targets (acknowledgement time, fix targets by severity).
  - **Smallest verification step:** maintainers set severity-based targets and publish them here.

**Proposed safe-harbor statement (review with maintainers):**
- Good-faith security research is welcome. Please avoid privacy violations, data destruction, and service disruption.

<a href="#top">Back to top</a>

---

## ✅ Verification checklist

Use this section to convert Unknown → Confirmed with minimal repo checks.

1) **Security contact**
- ❓ Unknown: security email alias / monitoring group  
- ✅ To confirm: maintainer-approved alias + GitHub security reporting availability

2) **Supported versions**
- ❓ Unknown: release branches and support window  
- ✅ To confirm: tag scheme, supported branches, and EOL policy

3) **Security tooling**
- ❓ Unknown: which of CodeQL/Trivy/osv-scanner/Dependabot are enabled  
- ✅ To confirm: check `.github/workflows/`, repo “Security” tab, and required checks

4) **Supply chain artifacts**
- ❓ Unknown: whether SBOM + SLSA attestations are produced for releases  
- ✅ To confirm: locate `releases/` artifacts or CI outputs, and document exact paths

5) **Incident response ownership**
- ❓ Unknown: on-call/escalation  
- ✅ To confirm: list owners and escalation channel (private)

<a href="#top">Back to top</a>
