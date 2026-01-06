# 🛡️ Kansas Frontier Matrix — Security Policy

![Security Policy](https://img.shields.io/badge/security-policy-blue)
![Coordinated Disclosure](https://img.shields.io/badge/disclosure-coordinated-success)
![Private Reporting](https://img.shields.io/badge/reporting-private%20channel-important)
![PSA](https://img.shields.io/badge/PSA-no%20issues%2FPR%20comments-red)

> [!IMPORTANT]
> 🚨 **Do not report security vulnerabilities via public GitHub Issues, Discussions, or PR comments.**  
> Please use **private vulnerability reporting** (preferred) or the alternative contact methods below.

> [!NOTE]
> If a security report is accidentally posted publicly, maintainers may **edit/remove** it to reduce exposure, then ask you to re-submit privately.

---

<a id="quick-links"></a>

## 📌 Quick links

- [🎯 Scope](#scope)
- [✅ Supported versions](#supported-versions)
- [🐛 Reporting a vulnerability](#reporting)
- [🧾 What to include](#report-contents)
- [🗞️ Advisories & notifications](#advisories)
- [⏱️ Coordinated disclosure](#cvd)
- [🧭 Safe harbor](#safe-harbor)
- [🚫 Out of scope](#out-of-scope)
- [🔐 Secure development guidelines](#secure-dev)
- [✅ PR security checklist](#pr-checklist)
- [🗂️ Recommended repo security files](#repo-security-files)
- [📚 Security reference library](#security-reference-library)

---

<a id="metadata"></a>

## 🧾 Policy metadata

| Field | Value |
|---|---|
| Policy file | `SECURITY.md` |
| Status | Active ✅ |
| Last updated | **2026-01-06** |
| Applies to | This repository + official releases + supported deployments |

---

<a id="scope"></a>

## 🎯 Scope

Kansas Frontier Matrix (KFM) is a multi-layered platform designed around clean separation of concerns (interface, infrastructure, and supporting frameworks). It includes a modern web UI plus service/integration layers, and the documentation references integrations common to geospatial/remote-sensing workflows (APIs, data pipelines, credentials, and third‑party integrations).

This policy focuses on:
- 🌎 **Geospatial & mapping workflows** (data integrity + access control)
- 🛰️ **Remote sensing pipelines** (credentials, cloud assets, data governance)
- 🧠 **ML/analytics components** (data poisoning, leakage, reproducibility risks)
- 🧱 **Web + API security** (authN/authZ, input validation, SSRF/XSS/CSRF, etc.)
- 🐳 **Containerized deployments** (image hardening, secrets, supply chain)

<details>
<summary><strong>🧩 KFM trust boundaries at a glance</strong></summary>

```mermaid
flowchart LR
  U[🌐 User / Client] -->|HTTPS| FE[🧑‍💻 Web UI (incl. WebGL)]
  FE -->|API calls| API[🔌 API / Services]
  API --> W[⚙️ Workers / Pipelines]
  API --> DB[(🗄️ Database)]
  W --> OBJ[(🪣 Cloud Assets / Object Storage)]
  W --> EXT[🛰️ External Providers / GIS APIs]
```
</details>

### ✅ In-scope vulnerability examples

- Authentication bypass, broken authorization (IDOR), privilege escalation
- Injection (SQL/NoSQL/command), SSRF, XSS (stored/reflected), CSRF with meaningful impact
- Deserialization / RCE, sandbox escape, unsafe file upload, path traversal
- Secrets exposure (tokens/keys), sensitive data leakage, insecure default configs
- Supply-chain risks introduced **by our repo** (malicious scripts, dependency confusion patterns)
- Remote sensing + GIS specific:
  - Unauthorized access to private assets/layers
  - Integrity compromises (tampering, poisoning vectors) with plausible downstream impact
  - Mis-scoped cloud permissions enabling unintended access

### ✅ Where to focus testing

- 🧑‍💻 UI / WebGL / frontend asset handling (**treat 3D assets as untrusted input**)
- 🔌 API / services / queues / background workers
- 🗄️ DB layer (PostgreSQL/MySQL), migrations, role separation
- 🗺️ GIS & remote sensing connectors / external provider integrations
- 🧠 ML pipelines (datasets, training artifacts, model outputs, evaluation)
- 🐳 Container images, CI/CD workflows, scripts, build/release pipelines

---

<a id="supported-versions"></a>

## ✅ Supported versions

We prioritize fixes for actively developed code.

| Target | Supported for security fixes | Notes |
|---|---:|---|
| `main` branch | ✅ | Always supported |
| Latest tagged release | ✅ | Recommended for deployments |
| Older tags/releases | ⚠️ Best effort | Fixes may not be backported |

> [!NOTE]
> If you’re running an older release, please be prepared to upgrade to a patched release on the latest supported line.

---

<a id="reporting"></a>

## 🐛 Reporting a vulnerability

### ✅ Preferred: GitHub Private Vulnerability Reporting

1. Go to this repository’s **Security** tab
2. Click **Report a vulnerability**
3. Provide details (see checklist below)

This keeps the report private while we investigate.

### 📧 Alternative: security contact (fallback)

If GitHub private reporting is not available in your environment, use:

- 📧 **Security email:** `security@YOUR-DOMAIN.example` *(maintainers: replace with your real inbox)*  
- 🔐 **Encryption:** publish a PGP public key in-repo (recommended) and reference it here (fingerprint + link).

> [!CAUTION]
> Please avoid sending secrets in plaintext if email is your only option.  
> If you must include credentials for reproduction, use short-lived test creds and clearly label them **“TEMP FOR REPRO ONLY”**.

### 🧯 Suspected active exploitation?

If you believe there is **active exploitation** or imminent risk:

- Use **private vulnerability reporting** immediately (preferred)
- Include **“🚨 ACTIVE EXPLOITATION SUSPECTED”** in the subject/title
- If safe: include indicators of compromise (IoCs), logs (redacted), and a scope estimate

---

<a id="report-contents"></a>

## 🧾 What to include in a report

To speed up triage, please include:

- **Summary** (what is vulnerable?)
- **Impact** (what can an attacker do?)
- **Attack scenario** (realistic exploitation path)
- **Reproduction steps** (ideally minimal)
- **Affected component(s)**  
  - UI / WebGL / frontend  
  - API / services / message queues  
  - DB layer (PostgreSQL/MySQL)  
  - GIS & remote sensing connectors  
  - ML/analytics pipelines  
  - Containers / CI/CD / scripts  
- **Proof of concept** *(safe, non-destructive)*
- **Suggested fix** *(if you have one)*
- **Version/commit** tested
- **Environment** (OS, browser, runtime versions, container image tag if relevant)

> [!TIP]
> If it helps, include a **minimal exploitability checklist**:
> - Is auth required? Y/N  
> - User interaction required? Y/N  
> - Network reachable? public/private/internal-only  
> - Data exposure type: metadata/PII/secrets/infra access  

### 🧾 Copy/paste report template

```text
Title:
Severity guess (optional):
Component(s):
Tested version/commit:
Environment:

Summary:
Impact:
Attack scenario:

Reproduction steps:
1)
2)
3)

Proof of concept (safe):
Expected result:
Actual result:

Suggested fix (optional):

Notes / context:
- Auth required? Y/N
- User interaction required? Y/N
- Network: public/private/internal-only
- Data exposure: metadata/PII/secrets/infra access
```

---

<a id="advisories"></a>

## 🗞️ Security advisories & notifications

We use GitHub’s security tooling when available:
- 🧾 **GitHub Security Advisories** for private triage + coordinated disclosure
- 📦 **Tagged releases** for patched versions (when applicable)

How to stay informed:
- ⭐ Watch this repository for **Releases**
- 🔔 If an advisory is published, GitHub can notify dependents and subscribers automatically

> [!NOTE]
> We avoid publishing exploit details before a fix is available (unless otherwise agreed as part of coordinated disclosure).

---

<a id="cvd"></a>

## ⏱️ Coordinated disclosure (CVD) expectations

We follow a coordinated disclosure approach:

- 📩 **Acknowledgement:** confirm receipt promptly
- 🔎 **Triage & validation:** reproduce and assess severity
- 🛠️ **Fix & test:** patch + regression tests + verification
- 📣 **Advisory & release:** publish a fix and (when appropriate) a GitHub Security Advisory

### ⏳ Target response timelines (guidance)

| Stage | Target |
|---|---|
| Initial acknowledgement | **≤ 2 business days** |
| Triage started | **≤ 7 days** |
| Fix ETA communicated | **after validation** |
| Patch release (Critical/High) | **as fast as feasible** |
| Patch release (Medium/Low) | **scheduled / best effort** |

> [!NOTE]
> Complex fixes may require longer timelines (e.g., dependency patches, coordinated upstream fixes, or high-risk migrations). We’ll keep reporters updated.

### 🏷️ Severity guidance (quick rubric)

| Severity | Examples |
|---|---|
| **Critical** | RCE, auth bypass, secrets exfiltration, full DB compromise |
| **High** | privilege escalation, SSRF into internal services, significant data leakage |
| **Medium** | stored XSS with meaningful impact, IDOR with limited scope |
| **Low** | minor info leaks, non-exploitable misconfigurations |

> [!TIP]
> If you have a CVSS vector/score (v3.1 or v4.0), include it (optional). We will still apply our own assessment.

---

<a id="safe-harbor"></a>

## 🧭 Safe harbor (good-faith research)

We support good‑faith security research that is:
- ✅ Non-destructive
- ✅ Limited to the minimum necessary testing
- ✅ Avoids privacy violations and data exfiltration
- ✅ Reported privately with reasonable detail

**Please do not:**
- ❌ Disrupt service (DoS / load testing) without explicit permission
- ❌ Access or modify data that isn’t yours
- ❌ Attempt social engineering (phishing, impersonation)
- ❌ Publish details before we’ve had a chance to patch (unless otherwise agreed)

> [!IMPORTANT]
> If you follow this policy in good faith, we consider your actions authorized and we will not pursue legal action against you for accidental, good‑faith violations. If you’re unsure whether a test is acceptable, **stop and report privately**.

---

<a id="out-of-scope"></a>

## 🚫 Out of scope (typical examples)

- Issues requiring **physical access** to a device
- **Denial of Service** via high traffic / brute force load testing
- Vulnerabilities **only in upstream providers** (report upstream first), unless our configuration makes them exploitable here
- Reports without a plausible security impact
- Automated scanner output **without** exploitation detail or actionable context

Common “informational” findings that are usually out of scope *unless chained to impact*:
- Missing security headers without exploitability context
- Clickjacking on non-sensitive pages
- Open redirects without a realistic impact
- Self-XSS without a privilege/impact chain

> [!NOTE]
> If you’re unsure, report anyway — we’ll help route it.

---

<a id="secure-dev"></a>

## 🔐 Secure development guidelines (for contributors)

Security is a design constraint, not an afterthought. These practices are expected across the stack.

### 🔑 Secrets & credentials
- Never commit secrets (API keys, DB passwords, service credentials)
- Use `.env` files locally; exclude them via `.gitignore`
- Prefer managed secret stores in production (CI secrets, vaults, cloud secret managers)
- Rotate any credential that may have been exposed
- Treat logs as sensitive: avoid tokens/PII in logs

### 🧩 Dependency & supply-chain hygiene
- Use lockfiles (`package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`, etc.)
- Keep dependencies updated; avoid abandoned packages
- Pin container base images; rebuild regularly
- Prefer verified sources for geospatial/ML datasets and tooling
- Consider SBOM generation for releases (recommended)

### 🐳 Container & runtime hardening
- Run as non-root where possible
- Minimize image size (multi-stage builds, only required binaries)
- Don’t bake secrets into images
- Use read-only filesystems where feasible
- Treat CI runners as sensitive infrastructure

### 🌐 Web/UI security (including WebGL)
- Validate + sanitize user inputs (client + server)
- Avoid unsafe HTML injection patterns
- Apply standard web protections (CSRF where relevant, secure cookies, CSP)
- Treat 3D/model assets as untrusted input (parsers can be attack surfaces)
- Prefer safe defaults for CORS (least privilege)

### 🛰️ GIS & remote sensing integrations
- Restrict API keys by domain/IP/service account permissions
- Enforce least privilege for cloud assets (buckets, Earth Engine assets, etc.)
- Protect sensitive layers (precise locations, private infrastructure)
- Maintain provenance metadata to detect tampering and poisoning
- Validate external data inputs (bounds, schema, CRS, expected ranges)

### 🧠 ML/analytics security & integrity
- Track dataset provenance, versions, and checksums (poisoning defense)
- Avoid leaking training data via logs or artifacts
- Consider model inversion / membership inference risks for exposed models
- Use robust evaluation and avoid “metric gaming” (integrity is part of security)
- Separate training/eval/test data clearly; keep reproducibility in mind

### 🗄️ Database security
- Least privilege DB roles
- Parameterized queries everywhere (avoid injection)
- Separate read/write credentials where feasible
- Encrypt backups and restrict access
- Use migration tooling carefully; test rollback/forward paths

---

<a id="pr-checklist"></a>

## ✅ PR security checklist (copy into PRs)

- [ ] No secrets committed (keys, tokens, `.env`, credentials)
- [ ] Inputs validated + outputs encoded (XSS/Injection resistant)
- [ ] AuthZ checks added/verified for any new data access path
- [ ] Dependencies updated/locked; no suspicious new packages
- [ ] New endpoints covered by tests (including negative/security cases)
- [ ] Logging does not include sensitive data (PII, keys, tokens)
- [ ] Container/runtime changes follow least-privilege principles
- [ ] Docs updated if security posture or configuration changes

---

<a id="repo-security-files"></a>

## 🗂️ Recommended repo security files (optional but 🔥 useful)

<details>
<summary><strong>📁 Suggested layout</strong></summary>

```text
📦 .github/
 ├─ 🛡️ SECURITY.md
 ├─ 🧾 dependabot.yml
 ├─ 🧑‍⚖️ CODEOWNERS
 ├─ 🧪 workflows/
 │   ├─ 🔍 code-scanning.yml
 │   ├─ 🔐 secret-scanning.yml
 │   └─ 📦 dependency-review.yml
📦 docs/
 ├─ 🔐 security/
 │   ├─ 🔑 pgp-public-key.asc
 │   ├─ 🧾 threat-model.md
 │   ├─ 📋 security-testing.md
 │   └─ 🧪 incident-response.md
```
</details>

---

<a id="security-reference-library"></a>

## 📚 Project Security Reference Library (used to shape this policy)

These project files influenced our security posture across architecture, web, data, GIS, remote sensing, and ML:

<details>
<summary><strong>🏗️ Architecture & engineering foundations</strong></summary>

- Kansas Frontier Matrix (KFM) – Master Technical Specification  
- Clean Architectures in Python  
- Implementing Programming Languages (Compilers/Interpreters)  
- Introduction to Docker  
- Command Line Kung Fu (Bash scripting & shell ops)  

</details>

<details>
<summary><strong>🌐 Web UI, visualization & graphics</strong></summary>

- Responsive Web Design with HTML5 and CSS3  
- WebGL Programming Guide (Interactive 3D Graphics)  
- Computer Graphics using JAVA 2D & 3D  

</details>

<details>
<summary><strong>🗄️ Databases & scalable data systems</strong></summary>

- PostgreSQL Notes for Professionals  
- MySQL Notes for Professionals  
- Scalable Data Management for Future Hardware  

</details>

<details>
<summary><strong>🌎 GIS, mapping & geoprocessing</strong></summary>

- Geographic Information System Basics  
- Geoprocessing with Python  
- Python Geospatial Analysis Cookbook  
- Making Maps (Visual Guide to Map Design for GIS)  
- Google Maps JavaScript API Cookbook  
- Google Maps API Succinctly  

</details>

<details>
<summary><strong>🛰️ Remote sensing & Earth Engine workflows</strong></summary>

- Cloud-Based Remote Sensing with Google Earth Engine (Fundamentals & Applications)  
- Google Earth Engine Applications  

</details>

<details>
<summary><strong>📊 Statistics, experiments & scientific computing integrity</strong></summary>

- Understanding Statistics & Experimental Design  
- Statistics Done Wrong  
- Bayesian Computational Methods  
- Graphical Data Analysis with R  
- Regression Analysis with Python  
- Scientific Modeling and Simulation (NASA‑grade guide)  
- MATLAB Programming for Engineers  

</details>

<details>
<summary><strong>🤖 AI / ML / data mining foundations</strong></summary>

- AI Foundations of Computational Agents  
- Data Mining Concepts & Applications  
- Artificial Neural Networks (Introduction)  
- Deep Learning in Python — Prerequisites  
- Data Science & Machine Learning (Mathematical & Statistical Methods)  
- Applied Data Science with Python and Jupyter  

</details>

<details>
<summary><strong>🧠 Human factors, autonomy & responsible systems</strong></summary>

- Introduction to Digital Humanism  
- Principles of Biological Autonomy  

</details>

---

<!--
Maintainers’ TODOs (remove before publishing if you prefer):
- Replace security@YOUR-DOMAIN.example with a real monitored inbox.
- Add a PGP key at docs/security/pgp-public-key.asc and reference its fingerprint.
- Optionally add workflows for code scanning + dependency review + secret scanning.
- Consider adding dependabot.yml, CODEOWNERS, and an incident-response runbook.
-->
