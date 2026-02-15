<!--
Path: .github/SECURITY.md
Purpose: Security policy + vulnerability reporting guidance for this repository.
GOVERNED ARTIFACT NOTICE: Changes can affect trust guarantees and disclosure posture; review via CODEOWNERS.
-->

# 🛡️ Security Policy (KFM)

![Governed](https://img.shields.io/badge/governed-artifact-critical)
![Private reporting](https://img.shields.io/badge/reporting-private%20only-important)
![Fail-closed](https://img.shields.io/badge/policy-default%20deny-111827)
![Cite or abstain](https://img.shields.io/badge/focus%20mode-cite%20or%20abstain-critical)
![Sensitivity](https://img.shields.io/badge/sensitivity-restricted%20%7C%20sensitive--location%20%7C%20aggregate--only-important)
![Supply chain](https://img.shields.io/badge/supply%20chain-SBOM%20%2B%20attestations%20optional-6b7280)

> [!IMPORTANT]
> **Do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**
> Use a **private** reporting channel instead (see **Reporting a Vulnerability**).

KFM treats security as part of governance: a bug that causes **evidence failure**, **policy bypass**, **sensitive data exposure**, or **audit/provenance tampering** is a security incident.

---

## Table of contents

- [Scope](#-scope)
- [Out of scope](#out-of-scope-typically)
- [Supported versions](#-supported-versions)
- [Reporting a vulnerability](#-reporting-a-vulnerability)
- [What to include](#-what-to-include-in-your-report)
- [Severity guide](#-severity-guide)
- [Response targets](#-response-targets-best-effort)
- [Coordinated disclosure](#-coordinated-disclosure)
- [Safe harbor](#-safe-harbor-good-faith-research)
- [Security expectations for contributors](#-security-expectations-for-contributors)
- [Advisories and credit](#-security-advisories--credit)

---

## 📌 Scope

This policy applies to security and safety issues affecting:

- source code in this repository (backend, frontend, tools, scripts)
- CI/CD workflows and build/release automation
- container images, deployment manifests, and infrastructure-as-code stored here
- data ingestion/pipeline code, promotion logic, receipts, and validation gates
- configuration that could expose secrets, credentials, tokens, internal endpoints, or privileged metadata
- **governance-related exposures**, including:
  - unintended publication of restricted/sensitive information
  - missing/incorrect redaction/generalization controls (sensitive-location, aggregate-only, culturally sensitive)
  - access-control bypasses affecting governed datasets, catalogs, evidence resolvers, or audit trails
  - failures of “cite-or-abstain” enforcement
  - failures of “fail-closed” behavior when required proofs are missing
  - tamper/bypass opportunities for receipts, checksums, catalogs, or audit ledgers

---

## Out of scope (typically)

Unless you can demonstrate clear security impact:

- social engineering (phishing/vishing), physical attacks, or threats
- denial-of-service (DoS) / load testing against shared infrastructure
- vulnerabilities only affecting outdated/unpatched third-party software where the fix is simply to upgrade
- issues requiring access you do not have (e.g., “if I were an admin…”)

---

## ✅ Supported versions

We prioritize fixes for supported development and release lines.

| Version / Branch | Supported | Notes |
|---|---:|---|
| `main` | ✅ | actively maintained |
| latest tagged release | ✅ | receives fixes when feasible |
| older tags/releases | ⚠️ | best-effort; may require upgrading |

> [!NOTE]
> If you’re unsure whether a version is supported, report anyway.

---

## 🚨 Reporting a vulnerability

### Preferred channel (private)

Use GitHub’s private vulnerability reporting **if enabled**:

1) go to the repository **Security** tab  
2) select **Report a vulnerability** (or **Advisories → New draft advisory**)  

This is the safest way to share details and attachments privately with maintainers.

### If private reporting is not available

If the Security tab does not provide private reporting, use a **private communication method** approved by maintainers (for example, a security contact listed in the repo docs/runbooks or maintainer profile).  
Do **not** post exploit details publicly.

> [!CAUTION]
> If you believe the issue involves **active exploitation** or **sensitive-data exposure**, state that clearly in the first line of your report.

---

## 🧾 What to include in your report

Include as much as you can **without** sharing sensitive payloads:

- clear description of the issue and **security impact**
- affected component(s): file paths, modules, endpoints, workflows
- steps to reproduce (or minimal PoC)
- expected vs actual behavior
- relevant logs/stack traces/request samples (**redact secrets**)
- severity assessment (low/medium/high/critical) and why
- suggested remediation/mitigation (if you have one)

### Sensitive data handling during reporting

If your report involves sensitive records (privacy or culturally restricted content):

- minimize what you share (only what is needed to verify)
- prefer hashes, IDs, or redacted excerpts over full payloads
- avoid raw data dumps or precise coordinates unless essential
- if you accidentally encounter sensitive data: **stop testing** and report immediately

---

## 📏 Severity guide

This table is a **guideline** to help align expectations (final severity is determined during triage).

| Severity | Typical impact | Examples (KFM-specific) |
|---|---|---|
| **Critical** | remote compromise, large-scale data exposure, policy bypass with sensitive content | policy bypass that reveals restricted fields; evidence resolver leaks sensitive-location precision; receipt/audit tampering enabling untraceable outputs |
| **High** | significant confidentiality/integrity risk; practical exploitation | SSRF to internal services; authentication/authorization bug; uncontrolled publish/promotion path bypassing Promotion Contract gates |
| **Medium** | security weakness with constraints; limited exposure | missing fail-closed behavior on some paths; partial leakage of metadata; misconfigured egress allowlist |
| **Low** | minor weakness; hard to exploit; minimal impact | informational leak without sensitive content; minor hardening improvements |

> [!IMPORTANT]
> For KFM, “governance bypass” issues (fail-closed breaks, cite-or-abstain breaks, sensitive-location exposure) often rank **High** or **Critical** even if no classic “RCE” exists.

---

## ⏱️ Response targets (best effort)

- acknowledge receipt within **72 hours**
- triage and severity assess within **7 days**
- provide mitigation guidance or a remediation plan as soon as practical

Complex issues (supply chain, infra, multi-component pipeline/policy) may take longer; we will keep you informed in the private thread.

---

## 🤝 Coordinated disclosure

We support coordinated disclosure.

- please allow a reasonable remediation window before public disclosure
- default disclosure window: **up to 90 days**, adjusted based on severity and exploitability
- if you plan to publish details (blog post, talk, etc.), coordinate timing with maintainers first

---

## 🧑‍⚖️ Safe harbor (good-faith research)

We welcome good-faith security research intended to improve the project.

**Please do:**
- test in ways that avoid harm to users, infrastructure, or data integrity
- use the least intrusive technique needed to demonstrate impact
- stop testing if you encounter sensitive data unintentionally

**Please do not:**
- exfiltrate data, attempt persistence, or pivot into unrelated systems
- use automated scanning that could degrade service availability
- publicly disclose exploit details before coordination

---

## 🔐 Security expectations for contributors

When contributing, follow these baseline practices:

- never commit secrets (API keys, tokens, credentials, private certs)
- use example configs (`.env.example`) and secret managers where applicable
- keep dependencies updated; prefer pinned/locked versions for reproducibility
- avoid unsafe deserialization, command injection, SSRF, and auth bypass patterns
- treat provenance/audit trails as security-relevant (tamper resistance matters)

### Governance-specific security requirements (KFM)

- **Fail-closed always:** missing policy inputs, missing receipts, missing catalogs, missing checksums → deny
- **Cite-or-abstain always:** Focus Mode must not return factual claims without resolvable citations
- **No trust membrane bypass:** UI must never access DBs; all access goes through governed API + policy
- **Sensitive-location protection:** do not publish precise sensitive coordinates; use generalized derivatives and enforce policy
- **Promotion Contract enforcement:** no publish without receipts + catalogs + checksums + validation

> [!NOTE]
> If you suspect a contribution introduces a security regression, report it privately rather than opening a public issue.

---

## 📣 Security advisories & credit

Confirmed vulnerabilities may result in a GitHub Security Advisory and a fix release/patch.

We can credit reporters in advisories/release notes **if you want attribution**—tell us what name/handle to use.

<details>
<summary><strong>What we typically publish in an advisory</strong></summary>

- affected versions/branches
- severity and impact summary
- fixed versions and upgrade guidance
- mitigations/workarounds (if any)
- CVE identifier (if assigned)
- credit (optional)

</details>
