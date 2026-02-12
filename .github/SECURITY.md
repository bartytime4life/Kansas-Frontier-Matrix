<!--
Path: .github/SECURITY.md
Purpose: Security policy + vulnerability reporting guidance for this repository.
-->

# 🛡️ Security Policy

> **Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**
> Use a **private** reporting channel instead (see **Reporting a Vulnerability** below).

## 📌 Scope

This policy applies to security and safety issues affecting:

- Source code in this repository (backend, frontend, tools, scripts)
- CI/CD workflows and build/release automation
- Container images, deployment manifests, and infrastructure-as-code stored here
- Data ingestion/pipeline code and validation logic
- Configuration that could expose secrets, credentials, tokens, or internal endpoints
- **Governance-related exposures**, including:
  - unintended publication of restricted/sensitive information
  - missing redaction controls for culturally sensitive or privacy-sensitive records
  - access-control bypasses affecting governed datasets or provenance/audit trails

### Out of scope

The following are typically **out of scope** (unless you can demonstrate a clear security impact):

- Social engineering (phishing, vishing), physical attacks, or threats
- Denial of service (DoS) / load testing against shared infrastructure
- Vulnerabilities only affecting outdated/unpatched third-party software **when the fix is to upgrade**
- Issues requiring access you do not have (e.g., “if I were an admin…”)

## ✅ Supported Versions

We prioritize fixes for supported development and release lines.

| Version / Branch | Supported | Notes |
|---|---:|---|
| `main` | ✅ | Actively maintained |
| Latest tagged release | ✅ | Receives security fixes when feasible |
| Older tags/releases | ⚠️ | Best-effort; may require upgrading |

> If you’re unsure whether a version is supported, report anyway.

## 🚨 Reporting a Vulnerability

### Preferred channel (private)

Use GitHub’s private vulnerability reporting if enabled:

- Go to the repository’s **Security** tab
- Select **Report a vulnerability** (or **Advisories** → **New draft advisory**)

This is the safest way to share details and attachments privately with maintainers.

### If private reporting is not available

If the Security tab does not provide private reporting, use a **private communication method** with project maintainers (e.g., a direct message or other maintainers-approved channel).  
**Do not** post exploit details publicly.

## 🧾 What to include in your report

To help us reproduce and fix quickly, include:

- A clear description of the issue and **security impact**
- Affected component(s) (file paths, modules, endpoints, workflows)
- Steps to reproduce (or a minimal PoC)
- Expected vs actual behavior
- Any relevant logs, stack traces, request/response samples (redact secrets!)
- Your assessment of severity (low/medium/high/critical) and why
- If applicable: suggested remediation or mitigation

### Sensitive data handling during reporting

If your report involves sensitive records (privacy or culturally restricted content):

- **Minimize** what you share (only what is needed to verify)
- Prefer **hashes**, **IDs**, or **redacted** excerpts over full payloads
- Avoid uploading raw data dumps or precise coordinates unless essential

## ⏱️ Response targets

We aim (best effort) to:

- **Acknowledge** receipt within **72 hours**
- **Triage** and severity-assess within **7 days**
- Provide a remediation plan or workaround as soon as practical

Complex issues (supply chain, infra, multi-component pipelines) may take longer; we will keep you informed in the private thread.

## 🤝 Coordinated Disclosure

We support coordinated disclosure.

- Please allow a reasonable remediation window before public disclosure.
- Default target disclosure window is **up to 90 days**, adjusted based on severity and exploitability.
- If you plan to publish details (blog post, talk, etc.), coordinate timing with maintainers first.

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

## 🔐 Security Expectations for Contributors

When contributing, please follow these baseline practices:

- **Never commit secrets** (API keys, tokens, credentials, private certs)
- Use example configs (`.env.example`) and secret managers where applicable
- Keep dependencies updated; prefer pinned/locked versions
- Avoid introducing unsafe deserialization, command injection, SSRF, or auth bypass patterns
- Treat provenance/audit trails as security-relevant (tamper resistance matters)

If you suspect a contribution introduces a security regression, report it privately rather than opening a public issue.

## 📣 Security Advisories & Credit

Confirmed vulnerabilities may result in a GitHub Security Advisory and a fix release/patch.

We’re happy to credit reporters in release notes/advisories **if you want attribution**—tell us what name/handle to use.