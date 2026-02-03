# 🛡️ Security Policy

![Security Policy](https://img.shields.io/badge/security-policy-important)
![Coordinated Disclosure](https://img.shields.io/badge/disclosure-coordinated-blue)
![Policy as Code](https://img.shields.io/badge/governance-policy--as--code-6f42c1)

KFM / Kansas-Matrix-System is built to be **evidence-first** and **governed by design** — that includes security.  
If you discover a security issue, please report it privately so we can fix it before it’s widely known.

---

## 📌 Table of Contents
- [✅ Supported Versions](#-supported-versions)
- [🚨 Reporting a Vulnerability](#-reporting-a-vulnerability)
- [🎯 Scope](#-scope)
- [🧑‍⚖️ Coordinated Disclosure & Safe Harbor](#-coordinated-disclosure--safe-harbor)
- [🔍 What to Include in a Report](#-what-to-include-in-a-report)
- [🧱 Security-by-Design Principles](#-security-by-design-principles)
- [🧩 Security Checklist for Contributors](#-security-checklist-for-contributors)

---

## ✅ Supported Versions

We provide security support for:

| Version / Artifact | Supported | Notes |
|---|:---:|---|
| `main` branch | ✅ | Active development (recommended for contributors) |
| Latest tagged release | ✅ | Recommended for deployments |
| Older tagged releases | ⚠️ | Best-effort; upgrade encouraged |
| Forks / downstream deployments | ⚠️ | We’ll help with root cause, but you own deployment configs |

> 🧠 **Rule of thumb:** if you can reproduce the issue on `main` or latest release, it’s in-scope and actionable.

---

## 🚨 Reporting a Vulnerability

### Preferred: GitHub Private Vulnerability Reporting (Recommended) 🔐
Use **GitHub Security Advisories** for private reporting:
1. Go to the repository’s **Security** tab.
2. Choose **Report a vulnerability**.
3. Submit details privately.

### If private reporting is not available
- Create a **minimal** GitHub Issue titled: `Security: Request for private contact`
- **Do not include technical exploit details, secrets, or sensitive endpoints** in the issue body.
- A maintainer will respond with a private channel.

> ❗ Please avoid posting vulnerabilities in public Issues, Discussions, PRs, or social media.

---

## 🎯 Scope

### In scope ✅
- Backend APIs (authN/authZ, RBAC, request validation, SSRF, injection, deserialization issues)
- Policy enforcement (OPA/Rego rules, “fail closed” logic, gatekeeping checks)
- Data pipeline + ingestion workflows (ETL validation, provenance integrity, artifact tampering)
- Frontend security (XSS, CSP bypass, token handling, unsafe storage)
- Container and infrastructure concerns (Docker/K8s misconfigs, privilege escalation, exposed services)
- Secrets exposure (committed keys, leaked env vars, CI logs leaking tokens)
- AI safety controls as security controls (prompt injection bypass, sensitive output leakage, citation enforcement bypass)

### Out of scope 🚫
- Issues in third-party services you don’t control (unless triggered by our integration)
- Social engineering of maintainers or contributors
- Physical attacks or device theft scenarios
- Denial-of-service testing against production endpoints **without permission**
- Purely theoretical issues with no practical exploit path

---

## 🧑‍⚖️ Coordinated Disclosure & Safe Harbor

We support **good-faith** security research and coordinated disclosure.

✅ Allowed (good-faith):
- Testing against local/dev environments and documented test endpoints
- Minimal PoCs that prove impact without causing harm
- Reporting responsibly and privately

🚫 Not allowed:
- Exfiltrating real user data
- Destroying data, modifying data, or interrupting services
- Broad scanning/fuzzing of production infrastructure without explicit permission

> 🧯 If you accidentally access sensitive data: **stop immediately**, **do not copy further**, and report what happened via the private channel.

---

## 🔍 What to Include in a Report

<details>
<summary><strong>📋 Click to expand: Recommended report format</strong></summary>

### 1) Summary
- What is the vulnerability?
- What component(s) are affected?

### 2) Impact
- What can an attacker do?
- Any data exposure risk (PII, sensitive datasets, secrets)?
- Any integrity risks (tampering, provenance forgery, policy bypass)?

### 3) Reproduction Steps
- Minimal steps to reproduce
- Example requests (sanitized) / PoC code (if safe)
- Environment details (branch/version, OS, runtime, docker image tag)

### 4) Suggested Fix (if you have one)
- Mitigations
- PR link (optional, but **do not** open a public PR with exploit details)

### 5) Contact & Disclosure Preferences
- How you want to be credited (name/handle)
- Whether you want a CVE (if applicable)

</details>

---

## 🧱 Security-by-Design Principles

This project treats security as part of the architecture:

- **Fail-closed governance** 🧷  
  If metadata, provenance, policy checks, or access rules fail — the operation is blocked.

- **Least privilege** 🔒  
  Services and users should only have access required to perform their role.

- **Policy as Code** 📜  
  Access and compliance rules are encoded and enforced (runtime + CI gates).

- **Prompt + output safety gates for AI** 🤖🛡️  
  Inputs are sanitized and outputs are policy-checked before delivery to users.

- **Provenance & auditability** 🧾  
  Changes and AI interactions are logged to support traceability and incident review.

- **Secure defaults in delivery** ✅  
  HTTPS-only, hardened headers, dependency scanning, and container/infrastructure guardrails.

---

## 🧩 Security Checklist for Contributors

Before opening a PR:

- [ ] 🔐 **No secrets in code** (keys, tokens, credentials, `.env` files, kubeconfigs)
- [ ] 🧼 Validate & sanitize inputs (API, ingestion, UI forms)
- [ ] 🧯 Add or update policy rules when introducing new access paths (RBAC/OPA)
- [ ] 🧪 Add tests for security-sensitive changes (auth, validation, policy logic)
- [ ] 📦 Keep dependencies minimal; update risky/abandoned packages
- [ ] 🐳 Keep containers least-privileged (avoid `--privileged`, root where possible)
- [ ] 🧾 Ensure provenance hooks/metadata are preserved for pipeline outputs
- [ ] 🧭 Don’t bypass the API layer to access datastores directly

> 👀 If you spot a security smell during review: call it out. Security is a shared responsibility.

---

## 🙏 Thanks

We appreciate responsible disclosures and will:
- work to confirm and address valid issues,
- coordinate on release/advisory publication,
- and (if desired) credit you for the discovery.

🧡 Thank you for helping keep KFM safe and trustworthy.
