# 🛡️ Kansas Frontier Matrix — Security Policy

![Security Policy](https://img.shields.io/badge/security-policy-blue)
![Coordinated Disclosure](https://img.shields.io/badge/disclosure-coordinated-success)
![Private Reporting](https://img.shields.io/badge/reporting-private%20channel-important)
![PSA](https://img.shields.io/badge/PSA-no%20issues%2FPR%20comments-red)
![Supply Chain](https://img.shields.io/badge/supply--chain-hardened-black)
![Data Integrity](https://img.shields.io/badge/data-integrity-provenance%20%2B%20checksums-purple)

> [!IMPORTANT]
> 🚨 **Do not report security vulnerabilities via public GitHub Issues, Discussions, or PR comments.**  
> Please use **private vulnerability reporting** (preferred) or the alternative contact methods below.

> [!NOTE]
> If a security report is accidentally posted publicly, maintainers may **edit/remove** it to reduce exposure, then ask you to re-submit privately.

---

<a id="quick-links"></a>

## 📌 Quick links

- [🎯 Scope](#scope)
- [🧱 Trust boundaries](#trust-boundaries)
- [🔒 Data classification & access control](#data-classification)
- [✅ Supported versions](#supported-versions)
- [🐛 Reporting a vulnerability](#reporting)
- [🧾 What to include](#report-contents)
- [🗞️ Advisories & notifications](#advisories)
- [⏱️ Coordinated disclosure](#cvd)
- [🧭 Safe harbor](#safe-harbor)
- [🚫 Out of scope](#out-of-scope)
- [🧰 Secure development guidelines](#secure-dev)
- [🧪 Security gates in CI](#ci-gates)
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
| Last updated | **2026-01-07** |
| Review cycle | Quarterly 🔁 |
| Applies to | This repository + official releases + supported deployments |

> [!TIP]
> GitHub recognizes `SECURITY.md` in **repo root**, `.github/`, or `docs/`. Pick one canonical location and keep it consistent.

---

<a id="scope"></a>

## 🎯 Scope

Kansas Frontier Matrix (KFM) is a **geospatial + historical mapping platform** with a web UI, services/APIs, spatial databases, ingestion/processing pipelines, and integrations common to GIS & remote-sensing workflows.

This policy focuses on:
- 🌎 **Geospatial & mapping workflows** (data integrity + access control)
- 🛰️ **Remote sensing pipelines** (credentials, cloud assets, data governance)
- 🧠 **ML/analytics components** (poisoning, leakage, reproducibility)
- 🧱 **Web + API security** (authN/authZ, input validation, SSRF/XSS/CSRF)
- 🐳 **Containerized deployments** (image hardening, secrets, supply chain)
- 📦 **Data supply chain** (STAC/DCAT/PROV, provenance, checksums, link integrity)

### ✅ In-scope vulnerability examples

- Authentication bypass, broken authorization (IDOR), privilege escalation
- Injection (SQL/NoSQL/command), SSRF, XSS (stored/reflected), CSRF with meaningful impact
- Unsafe deserialization / RCE, sandbox escape, unsafe file upload, path traversal
- Secrets exposure (tokens/keys), sensitive data leakage, insecure default configs
- Supply-chain risks introduced **by our repo** (malicious scripts, compromised dependency patterns)
- GIS + remote sensing specific:
  - Unauthorized access to private assets/layers
  - Integrity compromises (tampering/poisoning) with plausible downstream impact
  - Mis-scoped cloud permissions enabling unintended access

### ✅ Where to focus testing

- 🧑‍💻 UI / WebGL / frontend asset handling (**treat 3D assets as untrusted input**)
- 🔌 API / services / queues / background workers
- 🗄️ DB layer (PostgreSQL/PostGIS), migrations, role separation
- 🗺️ GIS & remote sensing connectors / external provider integrations
- 🧠 ML pipelines (datasets, training artifacts, model outputs, evaluation)
- 🐳 Container images, CI/CD workflows, scripts, build/release pipelines

---

<a id="trust-boundaries"></a>

## 🧱 Trust boundaries

<details>
<summary><strong>🧩 KFM trust boundaries at a glance</strong></summary>

```mermaid
flowchart LR
  U[🌐 User / Client] -->|HTTPS| FE[🧑‍💻 Web UI (incl. WebGL)]
  FE -->|API calls| API[🔌 API / Services]
  API --> W[⚙️ Workers / Pipelines]
  API --> DB[(🗄️ Spatial DB<br/>PostgreSQL/PostGIS)]
  W --> OBJ[(🪣 Object Storage<br/>tiles • COGs • assets)]
  W --> EXT[🛰️ External Providers<br/>GIS APIs • Earth Engine • archives]
  API --> AUTH[(🔐 AuthN/AuthZ<br/>RBAC/ABAC as needed)]
```
</details>

> [!IMPORTANT]
> Anything crossing a trust boundary must assume **untrusted input** until validated (files, JSON, GeoJSON, tilesets, STAC catalogs, external API responses).

---

<a id="data-classification"></a>

## 🔒 Data classification & access control

KFM is “mostly open”, but **not everything should be treated as public**:
- Sensitive cultural locations (e.g., sacred sites)
- Private infrastructure details
- Credentials, internal endpoints, operational logs
- Any modern/personal data (if ever integrated)

### 🧭 Classification levels (recommended)

| Classification | Who can access | Typical examples |
|---|---|---|
| **Public** 🌍 | Everyone | Published layers, historical scans with clear licensing |
| **Internal** 🏢 | Maintainers & collaborators | Draft pipelines, staging catalogs, internal runbooks |
| **Confidential** 🔐 | Admin/Owners + explicitly approved users | Sensitive layers requiring controlled sharing |
| **Restricted** 🧨 | Admin/Owners + explicitly approved users | Credentials, security-sensitive operational data |

### 👥 Role model (recommended)

- **Admin** — full control, emergency actions, security operations  
- **Owner** — dataset/module stewardship + approvals  
- **Collaborator** — write access in scoped areas (via CODEOWNERS)  
- **Read-only** — view access to internal docs/logs as granted  

> [!TIP]
> Treat **classification + role** as a first-class constraint enforced by:
> - API layer (authZ + redaction/generalization)
> - storage policies (bucket ACLs, signed URLs)
> - CI gates (block publishing restricted data into public catalogs)

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

> [!TIP]
> If you can’t find the entry point, try the direct route:  
> `https://github.com/<owner>/<repo>/security/advisories/new` *(replace placeholders)*

### 📧 Alternative: security contact (fallback)

If GitHub private reporting is not available in your environment, use:

- 📧 **Security email:** `security@YOUR-DOMAIN.example` *(maintainers: replace with a real monitored inbox)*  
- 🔐 **Encryption:** publish a PGP public key in-repo and reference it here:
  - File: `docs/security/pgp-public-key.asc`
  - Fingerprint: `XXXX XXXX XXXX XXXX XXXX  XXXX XXXX XXXX XXXX XXXX` *(placeholder)*

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
  - DB layer (PostgreSQL/PostGIS)  
  - GIS & remote sensing connectors  
  - ML/analytics pipelines  
  - Containers / CI/CD / scripts  
  - **Data catalogs** (STAC/DCAT) & provenance (PROV)  
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
> Complex fixes may require longer timelines (e.g., dependency patches, coordinated upstream fixes, high-risk migrations). We’ll keep reporters updated.

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

## 🧰 Secure development guidelines (for contributors)

Security is a design constraint, not an afterthought. These practices are expected across the stack.

### 🔑 Secrets & credentials

- Never commit secrets (API keys, DB passwords, service credentials)
- Use `.env` files locally; exclude them via `.gitignore`
- Prefer managed secret stores in production (GitHub Environments/Secrets, vaults, cloud secret managers)
- Rotate any credential that may have been exposed
- Treat logs as sensitive: avoid tokens/PII in logs

### 🧬 Data supply-chain security (STAC/DCAT/PROV as a control)

KFM treats **metadata + provenance** as security-critical:
- provenance reduces tampering risk
- catalog validation prevents accidental publishing of restricted data
- checksums/versioning support reproducibility & incident forensics

**Required “boundary artifacts” before publishing data:**
- STAC entry for datasets/layers (where applicable)
- DCAT dataset entry (where applicable)
- PROV lineage record in `data/prov/` (inputs → transformations → outputs)
- Checksums/version stamp for large artifacts (recommended)

> [!IMPORTANT]
> Any **derived/AI-generated** layer is treated as a first-class dataset with full provenance (not “just a file”).

### 🛰️ GIS & remote sensing integrations

- Restrict API keys by domain/IP/service account permissions
- Enforce least privilege for cloud assets (buckets, Earth Engine assets, etc.)
- Protect sensitive layers (precise locations, private infrastructure, cultural sites)
- Maintain provenance metadata to detect tampering and poisoning
- Validate external data inputs (bounds, schema, CRS, expected ranges)

### 🌐 Web/UI security (including WebGL)

- Validate + sanitize user inputs (client + server)
- Avoid unsafe HTML injection patterns
- Apply standard web protections (CSRF where relevant, secure cookies, CSP)
- Treat 3D/model assets as untrusted input (parsers can be attack surfaces)
- Prefer safe defaults for CORS (least privilege)

### 🗄️ Database security (PostgreSQL/PostGIS)

- Least privilege DB roles (separate read/write where feasible)
- Parameterized queries everywhere (avoid injection)
- Encrypt backups and restrict access
- Use migration tooling carefully; test rollback/forward paths
- Audit sensitive operations (writes, privilege changes, export endpoints)

### 🧠 ML/analytics security & integrity

- Track dataset provenance, versions, and checksums (poisoning defense)
- Avoid leaking training data via logs or artifacts
- Consider model inversion / membership inference risks for exposed models
- Separate training/eval/test data clearly; keep reproducibility in mind
- Prefer transparent evaluation (metrics + failure cases), not vibes

### ♻️ Dependency & supply-chain hygiene

- Use lockfiles (`package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`, etc.)
- Keep dependencies updated; avoid abandoned packages
- Pin container base images; rebuild regularly
- Pin GitHub Actions by commit SHA where possible
- Consider SBOM generation for releases (recommended)

### 🐳 Container & runtime hardening

- Run as non-root where possible
- Minimize image size (multi-stage builds, only required binaries)
- Don’t bake secrets into images
- Use read-only filesystems where feasible
- Treat CI runners as sensitive infrastructure

---

<a id="ci-gates"></a>

## 🧪 Security gates in CI (recommended)

Security must be repeatable and boring. Suggested baseline:

### ✅ Code security (SAST + reviews)
- CodeQL scanning
- Dependency Review (for PRs)
- Secret scanning + push protection
- Lint/typecheck/tests as required checks

### 🧾 Catalog/data integrity checks (geo-specific)
- **STAC/DCAT quick gate** (license/providers/stac_extensions present)
- Link-check critical `links[].href` in STAC root/collections
- Validate CRS metadata for spatial assets (projection fields, EPSG codes)
- Provenance presence (PROV record required before publishing)

> [!TIP]
> Gate “production catalog publish” on **Stable** STAC extensions only; warn on Pilot/Proposal extensions until reviewed.

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
- [ ] Data changes include provenance + catalog updates (STAC/DCAT/PROV)
- [ ] Docs updated if security posture or configuration changes

---

<a id="repo-security-files"></a>

## 🗂️ Recommended repo security files (optional but 🔥 useful)

<details>
<summary><strong>📁 Suggested layout</strong></summary>

```text
📦 .github/
 ├─ 🛡️ SECURITY.md                # (optional mirror) policy copy
 ├─ 🧾 dependabot.yml
 ├─ 🧑‍⚖️ CODEOWNERS
 ├─ 🧪 workflows/
 │   ├─ 🔍 codeql.yml
 │   ├─ 🧾 dependency-review.yml
 │   ├─ 🔐 secret-scanning.yml     # (docs + settings + optional checks)
 │   ├─ 🧷 scorecard.yml           # OpenSSF (optional)
 │   └─ 🧪 ci.yml
📦 docs/
 ├─ 🔐 security/
 │   ├─ 🔑 pgp-public-key.asc
 │   ├─ 🧾 threat-model.md
 │   ├─ 📋 security-testing.md
 │   └─ 🧪 incident-response.md
📦 tools/
 ├─ ✅ validation/
 │   └─ catalog_qa/                # STAC/DCAT link + field gate
📦 data/
 ├─ 🧾 prov/                       # provenance records (PROV)
 ├─ 🗂️ stac/                       # STAC catalogs/items
 └─ 📚 catalog/
     └─ dcat/                      # DCAT entries
```
</details>

---

<a id="security-reference-library"></a>

## 📚 Project Security Reference Library (used to shape this policy)

These project files influenced our posture across architecture, web, data, GIS, remote sensing, CI, and ML.

<details>
<summary><strong>🏗️ KFM architecture, governance & ops notes</strong></summary>

- `docs/architecture/Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx`
- `docs/ideas/Latest Ideas.docx`
- `docs/guides/MARKDOWN_GUIDE_v13.md.gdoc`

</details>

<details>
<summary><strong>🗄️ Databases & scalable data systems</strong></summary>

- `docs/library/PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `docs/library/Scalable Data Management for Future Hardware.pdf`
- `docs/library/Data Spaces.pdf`

</details>

<details>
<summary><strong>🌐 Web UI, visualization & graphics</strong></summary>

- `docs/library/responsive-web-design-with-html5-and-css3.pdf`
- `docs/library/webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `docs/library/compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

</details>

<details>
<summary><strong>🌎 GIS, mapping & geoprocessing</strong></summary>

- `docs/library/python-geospatial-analysis-cookbook.pdf`
- `docs/library/making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `docs/library/Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`

</details>

<details>
<summary><strong>🛰️ Remote sensing & Earth Engine workflows</strong></summary>

- `docs/library/Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`

</details>

<details>
<summary><strong>📊 Statistics, experiments & scientific computing integrity</strong></summary>

- `docs/library/Understanding Statistics & Experimental Design.pdf`
- `docs/library/regression-analysis-with-python.pdf`
- `docs/library/graphical-data-analysis-with-r.pdf`
- `docs/library/Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `docs/library/think-bayes-bayesian-statistics-in-python.pdf`

</details>

<details>
<summary><strong>🧨 Security testing & defensive thinking (reference only)</strong></summary>

- `docs/library/ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `docs/library/Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

> [!NOTE]
> These are used to inform defensive controls (threat modeling, incident response, testing strategy).  
> They are **not** a request for offensive tooling contributions.

</details>

---

<!--
Maintainers’ TODOs (keep or remove):
- Replace security@YOUR-DOMAIN.example with a real monitored inbox.
- Add a PGP key at docs/security/pgp-public-key.asc and reference its fingerprint.
- Add workflows for CodeQL + dependency review + CI.
- Add a minimal incident-response runbook (roles, comms, logging, containment).
- Decide and document the public/internal/confidential/restricted classification rules for KFM layers.
-->