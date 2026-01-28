# 🔐 Security Policy

![Security Policy](https://img.shields.io/badge/Security-Policy-blue?style=for-the-badge)
![Responsible Disclosure](https://img.shields.io/badge/Responsible-Disclosure-brightgreen?style=for-the-badge)
![No Public Exploits](https://img.shields.io/badge/Please-No%20Public%20Issues%20for%20Vulns-red?style=for-the-badge)

> ⚠️ **Please do not open public GitHub Issues/Discussions for security vulnerabilities.**  
> Use the **private reporting** process below so we can investigate and fix safely.

---

## ✅ Supported Versions

We provide security updates for:

| Version / Branch | Supported | Notes |
|---|:---:|---|
| `main` | ✅ | Actively developed |
| Latest GitHub Release | ✅ | Recommended for production deployments |
| Older releases / forks | ❌ | Please upgrade and re-test |

> 🧭 If you’re unsure which version you’re on, include the **commit SHA** and any **tag/release** in your report.

---

## 🚨 Reporting a Vulnerability

### Preferred: GitHub Private Vulnerability Report (Security Advisories)

1. Go to this repository on GitHub  
2. Click **Security** → **Report a vulnerability** (or **Advisories** → **New draft advisory**)  
3. Submit your report with as much detail as possible (template below)

### Alternate: Private contact (if GitHub reporting is unavailable)

- Contact the maintainers **privately** via the repository owner/maintainer channels (e.g., the maintainer’s GitHub profile contact links).
- As a last resort, open a **public issue with *no technical details*** titled:  
  `Security: Request private reporting channel`  
  ✅ Include only: how to reach you + confirmation you have details to share privately.

---

## 🧾 What to Include in Your Report

Please include:

- 🔎 **Summary** of the issue and why it matters  
- 🎯 **Affected component(s)** (API, UI, pipelines, auth, policy, data layer, CI, etc.)  
- 🧪 **Reproduction steps** (or a minimal PoC)  
- 💥 **Impact** (what an attacker can do)  
- 🧷 **Version info**: commit SHA, branch, release tag, deployment type (local/docker/cloud)  
- 📎 **Logs/screenshots** if helpful (**redact secrets & personal info**)  
- 🛠️ **Suggested fix/mitigation** (optional but appreciated)

<details>
<summary><strong>📋 Copy/Paste Report Template</strong></summary>

```text
Title:
Severity (guess): Critical / High / Medium / Low
Affected area(s):
- e.g., src/api, auth, policy engine, UI, pipeline, infra

Environment:
- commit SHA:
- release/tag:
- deployment: local / docker / cloud
- OS/runtime:

Description:
Steps to reproduce:
1)
2)
3)

Expected result:
Actual result:

Impact:
- What can be accessed/changed/executed?

Proof of concept (optional):
- code / request / payload (redacted)

Suggested mitigation (optional):
```
</details>

---

## ⏱️ Response Targets (Best Effort)

We aim to:

- 📩 **Acknowledge** within **3 business days**
- 🧭 **Triage** within **7 business days**
- 🧯 Provide a **fix or mitigation plan** as soon as practical
- 🤝 Coordinate a **responsible disclosure timeline** (typically ~**30–90 days**, depending on severity & complexity)

> We may ask for additional details, logs, or a test environment to confirm the issue.

---

## 🧩 Scope

### ✅ In Scope

- 🔐 Authentication / authorization flaws (RBAC/ABAC/policy bypass, privilege escalation)
- 🗃️ Data exposure (including “restricted”/sensitive datasets, metadata leaks, unintended downloads)
- 🧬 Injection issues (SQL/Cypher/GraphQL/command/template injection)
- 🌐 SSRF, request smuggling, CORS misconfig, insecure redirects
- 🧨 RCE / sandbox escape / container breakout
- 🧷 Secrets exposure (tokens/keys committed, logs leaking secrets)
- 🧷 Supply-chain vulnerabilities **introduced by this repo** (dependency compromise, build script risk)
- 🤖 AI-specific security issues **when they cause real impact**, e.g.:
  - policy bypass leading to restricted data leakage
  - prompt injection leading to unintended tool actions
  - data exfiltration via retrieval/agent behaviors

### ❌ Out of Scope (Generally)

- 🔨 Denial-of-service (DoS) via very high traffic / volumetric attacks
- 🎭 Social engineering / phishing
- 🧱 Physical attacks
- 🧩 Vulnerabilities in third-party services outside our control (unless we misuse them)
- 🧪 Reports without a reasonable proof/impact explanation

> If you’re unsure, **report it anyway**—we’ll help classify it.

---

## 🔒 Sensitive Data & Privacy Notes

- 🚫 **Do not** include secrets, access tokens, private keys, or personal data in reports.
- 🧯 If you believe sensitive data is exposed (even accidentally), treat it as a **security issue** and report privately.

---

## 🛡️ Safe Harbor (Good-Faith Security Research)

We support good-faith security research that helps keep the community safe. Please:

- ✅ Make a good-faith effort to **avoid privacy violations**, data destruction, and service disruption
- ✅ Use the **minimum necessary** access to demonstrate the issue
- ✅ Report promptly and keep details **confidential** until a fix is available
- ❌ Do not use vulnerabilities for extortion, persistence, or lateral movement

---

## 🏷️ Credit

If you’d like, we’re happy to credit reporters in release notes or advisories. 🙌  
(Just tell us the name/handle to use—or ask to remain anonymous.)

---

## 📁 Related Governance Docs

- 📄 `CONTRIBUTING.md` — contribution rules & review expectations  
- 📄 `CODE_OF_CONDUCT.md` — community standards  
- 📄 `.github/workflows/*` — CI checks (lint/tests/security scanning where configured)

---

**Thanks for helping keep this project and its users safe.** 🧡