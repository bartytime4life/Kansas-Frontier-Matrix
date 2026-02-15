<!--
Path: .github/SECURITY.md
Purpose: Security policy + vulnerability reporting guidance for this repository.
Governed Artifact: Changes can affect trust guarantees and disclosure posture; review via CODEOWNERS.
-->

# 🛡️ Security Policy (KFM)

> **Do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**
> Use a **private** reporting channel instead (see **Reporting a Vulnerability**).

KFM treats security as part of governance: a bug that causes **evidence failure**, **policy bypass**, **sensitive data exposure**, or **audit/provenance tampering** is a security incident.

---

## 📌 Scope

This policy applies to security and safety issues affecting:

- Source code in this repository (backend, frontend, tools, scripts)
- CI/CD workflows and build/release automation
- Container images, deployment manifests, and infrastructure-as-code stored here
- Data ingestion/pipeline code, promotion logic, receipts, and validation gates
- Configuration that could expose secrets, credentials, tokens, internal endpoints, or privileged metadata
- Governance-related exposures, including:
  - unintended publication of restricted/sensitive information
  - missing/incorrect redaction/generalization controls (sensitive-location, aggregate-only, culturally sensitive)
  - access-control bypasses affecting governed datasets, catalogs, evidence resolvers, or audit trails
  - failures of “cite-or-abstain” enforcement
  - failures of “fail-closed” behavior when required proofs are missing
  - tamper or bypass opportunities for receipts/checksums/catalogs/audit ledgers

### Out of scope (typically)

Unless you can demonstrate clear security impact:

- Social engineering (phishing/vishing), physical attacks, or threats
- Denial-of-service (DoS) / load testing against shared infrastructure
- Vulnerabilities only affecting outdated/unpatched third-party software where the fix is simply to upgrade
- Issues requiring access you do not have (e.g., “if I were an admin…”)

---

## ✅ Supported Versions

We prioritize fixes for supported development and release lines.

| Version / Branch | Supported | Notes |
|---|---:|---|
| `main` | ✅ | Actively maintained |
| Latest tagged release | ✅ | Receives fixes when feasible |
| Older tags/releases | ⚠️ | Best-effort; may require upgrading |

> If you’re unsure whether a version is supported, report anyway.

---

## 🚨 Reporting a Vulnerability

### Preferred channel (private)

Use GitHub’s private vulnerability reporting **if enabled**:

1) Go to the repository **Security** tab  
2) Select **Report a vulnerability** (or **Advisories → New draft advisory**)  

This is the safest way to share details and attachments privately with maintainers.

### If private reporting is not available

If the Security tab does not provide private reporting, use a **private communication method** approved by maintainers (for example, an email address listed in `README.md`, `docs/runbooks/oncall/`, or an org security contact).  
Do not post exploit details publicly.

---

## 🧾 What to include in your report

To help us reproduce and fix quickly, include:

- Clear description of the issue and **security impact**
- Affected component(s): file paths, modules, endpoints, workflows
- Steps to reproduce (or minimal PoC)
- Expected vs actual behavior
- Relevant logs/stack traces/request samples (**redact secrets**)
- Your severity assessment (low/medium/high/critical) and why
- Suggested remediation/mitigation (if you have one)

### Sensitive data handling during reporting

If your report involves sensitive records (privacy or culturally restricted content):

- Minimize what you share (only what is needed to verify)
- Prefer hashes, IDs, or redacted excerpts over full payloads
- Avoid raw data dumps or precise coordinates unless essential
- If you accidentally encounter sensitive data, stop testing and report immediately

---

## ⏱️ Response targets (best effort)

- Acknowledge receipt within **72 hours**
- Triage and severity assess within **7 days**
- Provide mitigation guidance or a remediation plan as soon as practical

Complex issues (supply chain, infra, multi-component pipeline/policy) may take longer; we will keep you informed in the private thread.

---

## 🤝 Coordinated Disclosure

We support coordinated disclosure.

- Please allow a reasonable remediation window before public disclosure.
- Default target disclosure window is **up to 90 days**, adjusted based on severity and exploitability.
- If you plan to publish details (blog post, talk, etc.), coordinate timing with maintainers first.

---

## 🧑‍⚖️ Safe Harbor (Good-Faith Research)

We welcome good-faith security research intended to improve the project.

**Please do:**
- Test in ways that avoid harm to users, infrastructure, or data integrity
- Use the least intrusive technique needed to demonstrate impact
- Stop testing if you encounter sensitive data unintentionally

**Please do not:**
- Exfiltrate data, attempt persistence, or pivot into unrelated systems
- Use automated scanning that could degrade service availability
- Publicly disclose exploit details before coordination

---

## 🔐 Security expectations for contributors

When contributing, follow these baseline practices:

- Never commit secrets (API keys, tokens, credentials, private certs)
- Use example configs (`.env.example`) and secret managers where applicable
- Keep dependencies updated; prefer pinned/locked versions for reproducibility
- Avoid unsafe deserialization, command injection, SSRF, and auth bypass patterns
- Treat provenance/audit trails as security-relevant (tamper resistance matters)

### Governance-specific security requirements (KFM)

- **Fail-closed always:** missing policy inputs, missing receipts, missing catalogs, missing checksums → deny
- **Cite-or-abstain always:** Focus Mode must not return factual claims without resolvable citations
- **No trust membrane bypass:** UI must never access DBs; all access goes through governed API + policy
- **Sensitive-location protection:** do not publish precise sensitive coordinates; use generalized derivatives and enforce policy

If you suspect a contribution introduces a security regression, report it privately rather than opening a public issue.

---

## 📣 Security advisories & credit

Confirmed vulnerabilities may result in a GitHub Security Advisory and a fix release/patch.

We can credit reporters in advisories/release notes **if you want attribution**—tell us what name/handle to use.
