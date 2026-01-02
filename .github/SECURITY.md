# 🛡️ Kansas Frontier Matrix — Security Policy

![Security Policy](https://img.shields.io/badge/security-policy-blue)
![Coordinated Disclosure](https://img.shields.io/badge/disclosure-coordinated-success)
![Do Not Publicly Disclose](https://img.shields.io/badge/reporting-private%20channel-important)

> 🚨 **Do not report security vulnerabilities via public GitHub Issues, Discussions, or PR comments.**  
> Please use **private vulnerability reporting** (preferred) or the alternative contact methods below.

---

## 🎯 What this policy covers

Kansas Frontier Matrix (KFM) is a multi-layered platform designed around clean separation of concerns (interface, infrastructure, and supporting frameworks) and includes a modern web UI plus service/integration layers. The project documentation also references integrations common to geospatial/remote-sensing workflows (e.g., external providers and Earth Engine-style pipelines), which expands our security surface area (APIs, data pipelines, credentials, and third‑party integrations).  

This policy explains how to **responsibly report vulnerabilities** and what we consider **in-scope**, with special attention to:
- 🌎 Geospatial & mapping workflows (data integrity + access control)
- 🛰️ Remote sensing pipelines (credentials, cloud assets, and data governance)
- 🧠 ML/analytics components (data poisoning, leakage, reproducibility risks)
- 🧱 Web + API security (authZ/authN, input validation, SSRF/XSS/CSRF, etc.)
- 🐳 Containerized deployments (image hardening, secrets, supply chain)

---

## ✅ Supported Versions

We prioritize fixes for actively developed code.

| Target | Supported for Security Fixes | Notes |
|---|---:|---|
| `main` branch | ✅ | Always supported |
| Latest tagged release | ✅ | Recommended for deployments |
| Older tags/releases | ⚠️ Best effort | Fixes may not be backported |

> If you’re running an older release, please be prepared to upgrade to a patched release on the latest supported line.

---

## 🐛 Reporting a Vulnerability

### Preferred: GitHub Private Vulnerability Reporting
1. Go to this repository’s **Security** tab
2. Click **Report a vulnerability**
3. Provide details (see checklist below)

This keeps the report private while we investigate.

### Alternative: Security contact (fallback)
If private reporting is not available in your environment, use one of the following:
- 📧 **Security email:** `security@YOUR-DOMAIN.example` *(replace with your real inbox)*  
- 🔐 If you require encryption, include your **PGP key** details in this repository (recommended) and reference it here.

> ⚠️ Please avoid sending secrets in plaintext if email is your only option.

---

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
- **Proof of concept** (safe, non-destructive)
- **Suggested fix** (if you have one)
- **Version/commit** tested

---

## ⏱️ Coordinated Disclosure (CVD) expectations

We follow a coordinated disclosure approach:

- 📩 **Acknowledgement:** we aim to confirm receipt promptly.
- 🔎 **Triage & validation:** we reproduce and assess severity.
- 🛠️ **Fix & test:** we patch, add regression tests, and verify.
- 📣 **Advisory & release:** we publish a fix and (when appropriate) a GitHub Security Advisory.

### 🏷️ Severity guidance (quick rubric)
| Severity | Examples |
|---|---|
| **Critical** | RCE, auth bypass, secrets exfiltration, full DB compromise |
| **High** | privilege escalation, SSRF into internal services, significant data leakage |
| **Medium** | stored XSS with meaningful impact, IDOR with limited scope |
| **Low** | minor info leaks, non-exploitable misconfigurations |

---

## 🧭 Safe Harbor (good-faith research)

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

---

## 🚫 Out of scope (typical examples)

- Issues requiring **physical access** to a device
- **Denial of Service** via high traffic / brute force load testing
- Vulnerabilities **only in upstream providers** (report upstream first), unless our configuration makes them exploitable here
- Reports without a plausible security impact

> If you’re unsure, report anyway — we’ll help route it.

---

## 🔐 Secure Development Guidelines (for contributors)

Security is a design constraint, not an afterthought. These practices are expected across the stack.

### 🔑 Secrets & credentials
- Never commit secrets (API keys, DB passwords, service credentials)
- Use `.env` files locally, exclude them via `.gitignore`
- Prefer managed secret stores in production (CI secrets, vaults, cloud secret managers)
- Rotate any credential that may have been exposed

### 🧩 Dependency & supply-chain hygiene
- Use lockfiles (`package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`, etc.)
- Keep dependencies updated; avoid abandoned packages
- Pin container base images; rebuild regularly
- Prefer verified sources for geospatial/ML datasets and tooling

### 🐳 Container & runtime hardening
- Run as non-root where possible
- Minimize image size (multi-stage builds, only required binaries)
- Don’t bake secrets into images
- Treat CI runners as sensitive infrastructure

### 🌐 Web/UI security (including WebGL)
- Validate and sanitize user inputs (client + server)
- Avoid unsafe HTML injection patterns
- Apply standard web protections (CSRF where relevant, secure cookies, CSP)
- Treat 3D/model assets as untrusted input (parsers can be attack surfaces)

### 🛰️ GIS & remote sensing integrations
- Restrict API keys by domain/IP/service account permissions
- Enforce least privilege for cloud assets (buckets, Earth Engine assets, etc.)
- Protect sensitive layers (e.g., precise locations, private infrastructure)
- Maintain provenance metadata to detect tampering and poisoning

### 🧠 ML/analytics security & integrity
- Track dataset provenance, versions, and checksums (poisoning defense)
- Avoid leaking training data via logs or artifacts
- Consider model inversion / membership inference risks for exposed models
- Use robust evaluation and avoid “metric gaming” (integrity is part of security)

### 🗄️ Database security
- Least privilege DB roles
- Parameterized queries everywhere (avoid injection)
- Separate read/write credentials where feasible
- Encrypt backups and restrict access

---

## ✅ PR Security Checklist (copy into PRs)

- [ ] No secrets committed (keys, tokens, `.env`, credentials)
- [ ] Inputs validated + outputs encoded (XSS/Injection resistant)
- [ ] AuthZ checks added/verified for any new data access path
- [ ] Dependencies updated/locked; no suspicious new packages
- [ ] New endpoints covered by tests (including negative/security cases)
- [ ] Logging does not include sensitive data (PII, keys, tokens)
- [ ] Container/runtime changes follow least-privilege principles

---

## 🧯 Suspected active exploitation?

If you believe there is **active exploitation** or imminent risk:
- Use **private vulnerability reporting** immediately (preferred)
- Include “🚨 ACTIVE EXPLOITATION SUSPECTED” in the subject/title
- If safe to do so, include indicators of compromise (IoCs), logs (redacted), and scope estimate

---

## 📚 Project Security Reference Library (used to shape this policy)

These project files influenced our security posture across architecture, web, data, GIS, remote sensing, and ML:

### 🏗️ Architecture & engineering foundations
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation**
- **Clean Architectures in Python**
- **Implementing Programming Languages (Compilers/Interpreters)**
- **Introduction to Docker**
- **Command Line Kung Fu (Bash scripting & shell ops)**

### 🌐 Web UI, visualization & graphics
- **Responsive Web Design with HTML5 and CSS3**
- **WebGL Programming Guide (Interactive 3D Graphics)**
- **Computer Graphics using JAVA 2D & 3D**

### 🗄️ Databases & scalable data systems
- **PostgreSQL Notes for Professionals**
- **MySQL Notes for Professionals**
- **Scalable Data Management for Future Hardware**

### 🌎 GIS, mapping & geoprocessing
- **Geographic Information System Basics**
- **Geoprocessing with Python**
- **Python Geospatial Analysis Cookbook**
- **Making Maps (Visual Guide to Map Design for GIS)**
- **Google Maps JavaScript API Cookbook**
- **Google Maps API Succinctly**

### 🛰️ Remote sensing & Earth Engine workflows
- **Cloud-Based Remote Sensing with Google Earth Engine (Fundamentals & Applications)**
- **Google Earth Engine Applications**

### 📊 Statistics, experiments & scientific computing integrity
- **Understanding Statistics & Experimental Design**
- **Statistics Done Wrong**
- **Bayesian Computational Methods**
- **Graphical Data Analysis with R**
- **Regression Analysis with Python**
- **Scientific Modeling and Simulation (NASA‑grade guide)**
- **MATLAB Programming for Engineers**

### 🤖 AI / ML / data mining foundations
- **AI Foundations of Computational Agents**
- **Data Mining Concepts & Applications**
- **Artificial Neural Networks (Introduction)**
- **Deep Learning in Python — Prerequisites**
- **Data Science & Machine Learning (Mathematical & Statistical Methods)**
- **Applied Data Science with Python and Jupyter**

### 🧠 Human factors, autonomy & responsible systems
- **Introduction to Digital Humanism**
- **Principles of Biological Autonomy**

---

<!--
Internal grounding notes (chat-only):
- KFM architecture/layers + technologies + integration surface: :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}
- Docker security features referenced (secrets, DCT, health checks, scanning): :contentReference[oaicite:2]{index=2}
- Digital Humanism emphasis on rights/values shaping systems: :contentReference[oaicite:3]{index=3}

File anchors (chat-only):
:contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6}
-->
