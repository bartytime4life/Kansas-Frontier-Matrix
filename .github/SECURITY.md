# 🛡️ Security Policy

![Security](https://img.shields.io/badge/Security-Policy-important)
![Disclosure](https://img.shields.io/badge/Disclosure-Coordinated-blue)
![Policy as Code](https://img.shields.io/badge/Governance-Policy%20as%20Code-6f42c1)
![Default Deny](https://img.shields.io/badge/Default-Fail%20Closed-critical)
![Supply Chain](https://img.shields.io/badge/Supply%20Chain-SBOM%20%E2%80%A2%20SLSA%20%E2%80%A2%20Cosign-0aa)
![Web Hardening](https://img.shields.io/badge/Web-HTTPS%20%2B%20HSTS%20%2B%20CSP-2ea44f)
![AI Guardrails](https://img.shields.io/badge/AI-Safety%20Gates%20%2B%20Audit%20Ledger-ff69b4)

KFM / **Kansas-Matrix-System** is built to be **evidence-first** and **governed by design** — that includes security.  
If you discover a security issue, **report it privately** so we can fix it before it’s widely known.

> 🔐 **Private first, always:** Please do **not** open public Issues/PRs with exploit details, tokens, or sensitive dataset locations.

---

## 📌 Table of Contents

- [✅ Supported Versions](#-supported-versions)
- [🚨 Reporting a Vulnerability](#-reporting-a-vulnerability)
- [⏱️ Response Process & Timelines](#-response-process--timelines)
- [🎯 Scope](#-scope)
- [🧑‍⚖️ Coordinated Disclosure & Safe Harbor](#-coordinated-disclosure--safe-harbor)
- [🧾 Security Controls at a Glance](#-security-controls-at-a-glance)
- [🧠 AI & Data Safety as Security](#-ai--data-safety-as-security)
- [🔐 Sensitive Data & Community Governance](#-sensitive-data--community-governance)
- [🧩 Contributor Security Checklist](#-contributor-security-checklist)
- [🧯 Incident Response](#-incident-response)
- [🙏 Thanks](#-thanks)

---

## ✅ Supported Versions

We provide security support for:

| Version / Artifact | Supported | Notes |
|---|:---:|---|
| `main` branch | ✅ | Active development (recommended for contributors) |
| Latest tagged release | ✅ | Recommended for deployments |
| Older tagged releases | ⚠️ | Best-effort; upgrade encouraged |
| Forks / downstream deployments | ⚠️ | We’ll help with root cause, but you own deployment configs |

> 🧠 **Rule of thumb:** if you can reproduce the issue on `main` **or** the latest release, it’s in-scope and actionable.

---

## 🚨 Reporting a Vulnerability

### ✅ Preferred: GitHub Private Vulnerability Reporting (Recommended) 🔐

Use **GitHub Security Advisories** for private reporting:

1. Go to the repository’s **Security** tab  
2. Choose **Report a vulnerability**  
3. Submit details privately ✅

### 🧭 If private reporting is not available

- Create a **minimal** GitHub Issue titled: `Security: Request for private contact`
- **Do not include** technical exploit details, secrets, or sensitive endpoints in the issue body
- A maintainer will respond with a private channel

> ❗ Please avoid posting vulnerabilities in public Issues, Discussions, PRs, or social media.

### 🚫 What NOT to include (anywhere public)

- API keys, tokens, credentials, kubeconfigs, `.env` contents
- Live endpoints that expose sensitive data
- Exact coordinates of protected locations (e.g., archeological sites / sacred sites)
- Proof that relies on exfiltrating real user/community data

---

### 🔍 What to include in a report

<details>
<summary><strong>📋 Click to expand: Recommended report format</strong></summary>

#### 1) Summary
- What is the vulnerability?
- What component(s) are affected? (API / UI / pipeline / policies / infra / AI)

#### 2) Impact
- What can an attacker do?
- Any risk to **confidentiality**, **integrity**, or **availability**?
- Any data exposure risk (PII, sensitive datasets, secrets, protected locations)?
- Any governance impact (policy bypass, provenance forgery, “fail-open” paths)?

#### 3) Reproduction Steps
- Minimal steps to reproduce
- Sanitized requests / logs / screenshots
- Environment details:
  - branch/version + commit
  - OS/runtime versions
  - container image tags (if applicable)

#### 4) Suggested Fix (if you have one)
- Mitigations
- PR link (optional)
  - ⚠️ Please do **not** open a public PR with exploit details

#### 5) Disclosure Preferences
- How you want to be credited (name/handle)
- Whether you want a CVE (if applicable)

</details>

---

## ⏱️ Response Process & Timelines

We treat vulnerability reports as **priority work** and aim for a clear, respectful cadence.

| Step | Target |
|---|---:|
| Acknowledge receipt | ≤ 72 hours |
| Triage + severity assessment | ≤ 7 days |
| Fix plan shared (if accepted) | ≤ 14 days |
| Remediation window (typical) | 30–90 days (severity-dependent) |

> 🧯 If we need more time (complex fix, coordination with downstreams), we’ll communicate clearly and coordinate disclosure timing.

### 🧮 Severity levels (practical)

| Severity | Example |
|---|---|
| **Critical** 🚨 | RCE, auth bypass, secret leakage, unrestricted access to restricted datasets |
| **High** 🔥 | Stored XSS, SSRF to internal network, privilege escalation, provenance tampering |
| **Medium** ⚠️ | Reflected XSS with constraints, weak rate limits, policy gaps with limited impact |
| **Low** 🧩 | Info disclosure without sensitive data, hardening suggestions |
| **Informational** 📝 | Best practice improvements, defense-in-depth |

---

## 🎯 Scope

### ✅ In scope

**Application & API**
- AuthN/AuthZ, RBAC, session/token handling
- Request validation, injection flaws, SSRF, deserialization risks
- Broken access controls and IDOR
- Backend-to-datastore boundary violations (bypassing the API layer)

**Policy enforcement & governance**
- 🧱 OPA/Rego policies (policy-as-code)
- “Fail closed” logic, gatekeeping checks, policy bypasses
- CI policy gates (anything that allows non-compliant merges/releases)

**Pipelines & provenance**
- Data ingestion/ETL validation issues
- Provenance integrity failures (missing/forged lineage, checksum bypass, artifact tampering)
- Audit ledger weaknesses (log deletion/alteration)

**Web & UI**
- XSS (stored/reflected), CSP bypass, unsafe storage, clickjacking, token leakage
- Dependency issues in the web supply chain

**Containers / infrastructure**
- Docker/K8s misconfigs, privilege escalation paths, exposed services
- CI/CD secrets exposure, runner compromise patterns

**AI safety controls as security controls**
- Prompt injection bypass that causes:
  - policy evasion
  - sensitive output leakage
  - citation enforcement bypass
  - unsafe tool-use paths (if tools exist)

### 🚫 Out of scope

- Vulnerabilities in third-party services we don’t control (unless directly triggered by our integration)
- Social engineering of maintainers or contributors
- Physical attacks / device theft scenarios
- DoS testing against production endpoints **without permission**
- Purely theoretical issues with no practical exploit path

---

## 🧑‍⚖️ Coordinated Disclosure & Safe Harbor

We support **good-faith** security research and coordinated disclosure.

✅ Allowed (good-faith):
- Testing against **local/dev** environments and documented test endpoints
- Minimal PoCs that prove impact **without causing harm**
- Reporting responsibly and privately

🚫 Not allowed:
- Exfiltrating real user/community data
- Destroying/modifying data or interrupting services
- Broad scanning/fuzzing of production infrastructure without explicit permission

> 🧯 If you accidentally access sensitive data: **stop immediately**, **do not copy further**, and report what happened privately.

---

## 🧾 Security Controls at a Glance

KFM security is a *system*, not a feature toggle 🧠🧱

| Area | Control | “What this prevents” |
|---|---|---|
| 🔐 Access | RBAC + policy decisions | Broken access control, role drift |
| 🧱 Governance | Policy-as-code gates (CI + runtime) | “fail-open” merges, policy bypass |
| 🧾 Provenance | Mandatory lineage + checksums | Silent tampering, untraceable data |
| 🧰 Supply chain | SBOM + provenance + signed artifacts | Dependency and build pipeline attacks |
| 🌐 Web hardening | HTTPS/HSTS + CSP + secure headers | MITM, script injection, UI compromise |
| 🧪 CI security | Dependency scans + DAST where relevant | Known vulns shipping to prod |
| 🤖 AI guardrails | Prompt/output gates + logging | Sensitive leakage, unsafe behavior |

> 🧷 Design principle: if metadata / provenance / policy checks fail — the operation is blocked (“fail closed”).

---

## 🧠 AI & Data Safety as Security

KFM treats **AI guardrails** and **data governance** as first-class security controls — not “nice to have.”

### What we consider “AI security issues” ✅
- Prompt injection that causes restricted data to be revealed (even partially)
- Bypassing “refuse” behavior for disallowed topics
- Citation/provenance bypass (answers presented as sourced when they are not)
- Unsafe tool invocation paths (if enabled), including data exfil attempts

### Helpful AI-focused reproduction tips 🧪
When reporting AI issues, include:
- the exact prompt
- the exact output
- which data/resource was exposed (even if only described)
- whether the failure is consistent or intermittent
- any “prompt wrapper” used (system prompt, templates, retrieved passages) if available

---

## 🔐 Sensitive Data & Community Governance

KFM explicitly supports **sensitive and community-governed data**, including protected locations and Indigenous/community contributions.

### Data sensitivity rules of thumb 🧭
- **Do not** publish precise locations for protected sites (e.g., archeological/sacred locations)
- Prefer **aggregation/generalization** for public views:
  - county-level summaries instead of point coordinates
  - coordinate rounding / masking
- Avoid publishing PII for living individuals
- Treat “small counts” as a re-identification risk (suppression/thresholding may apply)

### Community-governed data 🪶
If data is contributed under community governance:
- access may be **restricted to an owner group**
- communities may request **withdrawal** or access changes
- labeling/classification is part of governance, not an afterthought

> 🧡 “Open” is not the same as “uncontrolled.” We balance openness with care, consent, and safety.

---

## 🧩 Contributor Security Checklist

Before opening a PR:

### 🔐 Secrets & credentials
- [ ] No secrets in code (keys, tokens, credentials, `.env` files, kubeconfigs)
- [ ] No secrets in logs, screenshots, test fixtures, or sample data

### 🧼 Input handling & access control
- [ ] Validate & sanitize inputs (API, ingestion, UI forms)
- [ ] Enforce authorization at the **API boundary** (no direct datastore shortcuts)
- [ ] Update RBAC/policy rules when introducing new access paths

### 🧱 Policy-as-code & governance
- [ ] Add/update policy rules if you introduced a new:
  - dataset type
  - access class
  - AI capability
  - pipeline output
- [ ] Ensure **fail-closed** behavior remains true under errors

### 🧾 Provenance & auditability
- [ ] Preserve provenance hooks/metadata for new data outputs
- [ ] Ensure outputs are traceable (inputs → process → outputs)

### 📦 Dependencies & supply chain
- [ ] Keep dependencies minimal
- [ ] Update/replace risky or abandoned packages
- [ ] Prefer pinned versions + lockfiles where appropriate

### 🐳 Containers & infra
- [ ] Avoid `--privileged`
- [ ] Run as non-root where possible
- [ ] Least privilege for service accounts and CI permissions

---

### 🧰 Optional: run “security gates” locally

<details>
<summary><strong>🧪 Click to expand: Example local commands</strong></summary>

> These are **examples**. Use the project’s preferred tools/configs where available.

```bash
# 1) Policy-as-code checks (example)
conftest test -p policy/ .

# 2) Dependency checks (examples)
npm audit --production
pip-audit || true

# 3) Secrets scanning (example)
gitleaks detect --no-git || true
```

</details>

---

## 🧯 Incident Response

If we confirm a real-world security incident, we prioritize:

1. **Containment** (stop active harm, revoke keys, disable affected routes)
2. **Assessment** (what happened, what’s impacted, what data risk exists)
3. **Remediation** (patch, rotate credentials, harden controls, add tests/policies)
4. **Communication** (advisory + coordinated disclosure as appropriate)
5. **Post-mortem** (document root cause + corrective actions)

> 🧾 For sensitive data leakage, expect additional steps like reclassification, cache purge, and governance review.

---

## 🙏 Thanks

We appreciate responsible disclosures and will:
- confirm and address valid issues,
- coordinate on release/advisory publication,
- and (if desired) credit you for the discovery.

🧡 Thank you for helping keep KFM safe and trustworthy.