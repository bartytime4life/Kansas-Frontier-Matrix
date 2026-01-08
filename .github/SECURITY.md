# 🛡️ Kansas Frontier Matrix (KFM) — Security Policy

<div align="left">

![Security Policy](https://img.shields.io/badge/security-policy-blue)
![Coordinated Disclosure](https://img.shields.io/badge/disclosure-coordinated-success)
![Private Reporting](https://img.shields.io/badge/reporting-private%20channel-important)
![PSA](https://img.shields.io/badge/PSA-no%20issues%2FPR%20comments-red)
![Supply Chain](https://img.shields.io/badge/supply--chain-hardened-black)
![Data Integrity](https://img.shields.io/badge/data-integrity-provenance%20%2B%20checksums-purple)

</div>

> [!IMPORTANT]
> 🚨 **Do not report security vulnerabilities via public GitHub Issues, Discussions, or PR comments.**  
> Use **private vulnerability reporting** (preferred) or the alternative contact methods below.

> [!NOTE]
> KFM is a **geospatial + knowledge + modeling** system: security issues can live in **code**, **infrastructure**, **data catalogs**, and **derived outputs** (models/Story Nodes). Treat any report as potentially sensitive.

---

## 🔥 TL;DR (reporting in 60 seconds)

✅ **Preferred (private):** Repo **Security** tab → **Report a vulnerability**  
✅ Include: **impact**, **repro steps**, **affected component**, **commit/tag**, and (if relevant) **dataset IDs** (STAC/DCAT/PROV)

If you suspect **active exploitation**, put **“🚨 ACTIVE EXPLOITATION SUSPECTED”** in the title and report privately ASAP.

---

## 📌 Table of contents

- [🧾 Policy metadata](#-policy-metadata)
- [⭐ Security invariants (v13-aligned)](#-security-invariants-v13-aligned)
- [🎯 Scope](#-scope)
- [🧩 Threat model (KFM-shaped)](#-threat-model-kfm-shaped)
- [🧱 Trust boundaries](#-trust-boundaries)
- [🔒 Data classification & access control](#-data-classification--access-control)
- [✅ Supported versions](#-supported-versions)
- [🐛 Reporting a vulnerability](#-reporting-a-vulnerability)
- [🧾 What to include](#-what-to-include)
- [🗺️ Dataset / sensitive data takedown requests](#-dataset--sensitive-data-takedown-requests)
- [🗞️ Advisories & notifications](#-advisories--notifications)
- [⏱️ Coordinated disclosure](#-coordinated-disclosure)
- [🧭 Safe harbor](#-safe-harbor)
- [🚫 Out of scope](#-out-of-scope)
- [🧰 Secure development guidelines](#-secure-development-guidelines)
- [🧪 Security gates in CI](#-security-gates-in-ci)
- [✅ PR security checklist](#-pr-security-checklist)
- [🗂️ Recommended repo security files](#-recommended-repo-security-files)
- [📚 Project reference library](#-project-reference-library)

---

## 🧾 Policy metadata

| Field | Value |
|---|---|
| Policy file | `SECURITY.md` |
| Status | Active ✅ |
| Last updated | **2026-01-08** |
| Review cycle | Quarterly 🔁 *(or after material security changes)* |
| Applies to | This repo + official releases + supported deployments |

> [!TIP]
> GitHub recognizes `SECURITY.md` in the **repo root**, `.github/`, or `docs/`.  
> Pick **one canonical location** and keep it consistent (mirrors allowed, but avoid drift).

---

## ⭐ Security invariants (v13-aligned)

KFM’s architecture has **non-negotiable invariants** that double as security controls:

1) 🧬 **Pipeline ordering is absolute**  
**ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**  
No stage should consume artifacts that haven’t passed the previous stage’s formal outputs and checks.

2) 🔌 **API boundary rule**  
The UI must **never** query the graph directly. All access goes through governed APIs (authZ, redaction, schema contracts).

3) 🧾 **Provenance-first publishing**  
If it’s visible in UI/story/graph, it must have:
- STAC/DCAT metadata
- PROV lineage
- (Recommended) checksums / stable IDs

4) ♻️ **Deterministic, idempotent ETL**  
Same input + config should produce the same output. Pipelines must be re-runnable safely.

5) 🧭 **Sovereignty & classification propagation**  
No output artifact can be **less restricted** than its inputs. Redaction/generalization is required to publish sensitive inputs safely.

6) ✅ **Validation gates enforce all of the above**  
CI must fail if provenance is missing, catalogs are broken, links are dead, or sensitive content leaks.

> [!IMPORTANT]
> For KFM, **metadata is security-critical**. A broken catalog link or missing license/provider can become a supply-chain problem for downstream consumers.

<!-- v13 sources (hidden):  [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) -->

---

## 🎯 Scope

Kansas Frontier Matrix (KFM) is a **geospatial + historical mapping + modeling platform** that typically includes:

- 🖥️ Web UI (including WebGL/3D viewers)
- 🔌 APIs/services (e.g., FastAPI)
- 🧰 Workers/pipelines (ETL + analytics + publishing)
- 🗄️ Spatial storage (PostgreSQL/PostGIS)
- 🪣 Object storage (rasters/COGs, tiles, docs, artifacts)
- 🕸️ Knowledge graph (entities/events/citations)
- 🗂️ Catalog + provenance layer (STAC/DCAT/PROV)

### ✅ In-scope vulnerability examples

- AuthN/authZ bypass (including IDOR), privilege escalation
- Injection (SQL/command), SSRF, stored/reflected XSS, CSRF with real impact
- Unsafe file upload, path traversal, deserialization issues, RCE
- Secrets exposure (tokens/keys), sensitive data leakage (including sensitive coordinates)
- Supply-chain risks introduced by this repo (dependencies, CI scripts, GitHub Actions)
- Geo-specific:
  - Catalog poisoning (malicious STAC/DCAT links/fields) causing unsafe fetches or consumer compromise
  - Integrity tampering of published assets (COGs/tiles/documents/model artifacts)
  - “Geospatial DoS” payloads (massive geometries, decompression bombs, pathological tilesets) that crash pipelines/UI

### 🧭 Where to focus testing (high value)

- 🧑‍💻 UI/WebGL asset handling (**treat 3D assets as untrusted input**)
- 🔌 API/services, background workers, queues, webhooks
- 🗄️ Postgres/PostGIS queries, migrations, exports
- 🛰️ Remote sensing connectors / external providers (Earth Engine-style, archives, portals)
- 🧠 ML/analytics pipelines (data leakage, poisoning, artifact integrity, reproducibility)
- 🐳 Container images, CI/CD workflows, build/release scripts

---

## 🧩 Threat model (KFM-shaped)

KFM’s “threat surface” includes more than code:

### 🎯 Assets we protect
- 🔐 Credentials (cloud keys, DB creds, service tokens, CI secrets)
- 🧾 Catalog integrity (STAC/DCAT) + provenance integrity (PROV)
- 🗺️ Sensitive location data (protected/cultural sites, private infrastructure)
- 📦 Published artifacts (tiles/COGs/GeoJSON/Parquet, reports, model outputs)
- 🧠 Trust in narratives (Story Nodes/Focus Mode must be evidence-backed)

### 👤 Likely threat actors
- Opportunistic attackers (common web vulns, exposed secrets, misconfig)
- Malicious data contributors (poisoning/tampering)
- Supply-chain attackers (dependencies/CI)
- Data scrapers targeting sensitive coordinates or operational details
- Well-meaning contributors who accidentally leak restricted data

### 🧨 Common KFM-specific failure modes
- “It’s just metadata” mindset → broken/unsafe STAC links, licensing gaps, missing provenance
- UI directly contacting internal stores/graph → bypassing authZ/redaction
- Pipelines fetching remote assets without allowlists → SSRF + internal exposure
- Publishing exact sensitive coordinates in public layers/story content
- Weak artifact integrity controls → silent tampering, untraceable outputs

---

## 🧱 Trust boundaries

<details>
<summary><strong>🧩 KFM trust boundaries at a glance</strong></summary>

```mermaid
flowchart LR
  U[🌐 User / Client] -->|HTTPS| FE[🧑‍💻 Web UI<br/>(incl. WebGL/3D)]
  FE -->|governed calls| API[🔌 API / Services]
  API --> W[⚙️ Workers / Pipelines]
  API --> DB[(🗄️ Spatial DB<br/>PostgreSQL/PostGIS)]
  W --> OBJ[(🪣 Object Storage<br/>tiles • COGs • docs • artifacts)]
  W --> EXT[🛰️ External Providers<br/>GIS APIs • Earth Engine • archives]
  API --> GRAPH[(🕸️ Knowledge Graph<br/>entities • events • citations)]
  API --> AUTH[(🔐 AuthN/AuthZ<br/>RBAC/ABAC as needed)]
```
</details>

> [!IMPORTANT]
> Anything crossing a trust boundary must assume **untrusted input** until validated  
> (files, JSON, GeoJSON, tilesets, STAC catalogs, external API responses).

---

## 🔒 Data classification & access control

KFM is “mostly open” — but **not everything should be public**.

### 🧭 Recommended classification levels

| Classification | Who can access | Typical examples |
|---|---|---|
| **Public** 🌍 | Everyone | Published layers with clear licensing |
| **Internal** 🏢 | Maintainers/collaborators | Draft catalogs, staging pipelines, runbooks |
| **Confidential** 🔐 | Explicitly approved | Sensitive layers requiring controlled sharing |
| **Restricted** 🧨 | Admin/Owners only | Credentials, security logs, protected exact coordinates |

### 🧬 Propagation rule (non-negotiable)

**No output artifact can be less restricted than its inputs.**  
If a source is sensitive, all derivatives inherit equal-or-higher restrictions unless explicitly reviewed and redacted.

### 🗺️ Sensitive Location Policy (KFM-specific)

If a dataset/story/model output contains culturally sensitive or personal location data:
- **Offset/coarsen/omit** precise coordinates
- Show broad regions when needed (“exact location protected”)
- Require explicit permission to include precise data

> [!TIP]
> Redaction strategies that tend to work well:
> - publish at **county/region** resolution instead of point precision  
> - snap to **grid cells** (e.g., 1–10km) for public releases  
> - provide controlled access (signed URLs, private collections) for approved users

<!-- KFM governance sources (hidden):  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS) -->

---

## ✅ Supported versions

We prioritize fixes for actively developed code.

| Target | Supported for security fixes | Notes |
|---|---:|---|
| `main` branch | ✅ | Always supported |
| Latest tagged release | ✅ | Recommended for deployments |
| Older releases | ⚠️ Best effort | Fixes may not be backported |

---

## 🐛 Reporting a vulnerability

### ✅ Preferred: GitHub Private Vulnerability Reporting

1. Go to this repository’s **Security** tab  
2. Click **Report a vulnerability**  
3. Provide details (see the checklist below)

Direct route (repo-specific):
- `https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/advisories/new`

> [!NOTE]
> If a security report is accidentally posted publicly, maintainers may **edit/remove** it to reduce exposure, then ask you to re-submit privately.

### 📧 Alternative: security contact (fallback)

If GitHub private reporting is not available:

- 📧 **Security email:** `security@YOUR-DOMAIN.example` *(maintainers: replace with a real monitored inbox)*  
- 🔐 **PGP key (recommended):**
  - File: `docs/security/pgp-public-key.asc`
  - Fingerprint: `XXXX XXXX XXXX XXXX XXXX  XXXX XXXX XXXX XXXX XXXX`

> [!CAUTION]
> Avoid sending secrets in plaintext. If you must include credentials for reproduction:
> - use short-lived test creds  
> - label them **“TEMP FOR REPRO ONLY”**  
> - include revocation instructions

### 🧯 Suspected active exploitation?

If you believe there is **active exploitation** or imminent risk:
- Report privately immediately
- Include **“🚨 ACTIVE EXPLOITATION SUSPECTED”** in the title
- If safe: include redacted logs/IoCs and scope estimates

---

## 🧾 What to include

To speed up triage, include:

- **Summary** (what is vulnerable?)
- **Impact** (what can an attacker do?)
- **Attack scenario** (realistic path)
- **Reproduction steps** (minimal)
- **Affected component(s)** (UI/API/DB/pipelines/catalogs/CI)
- **Safe proof of concept** *(non-destructive, no public exploit chains)*
- **Suggested fix** *(optional)*
- **Version/commit** tested
- **Environment** (OS/browser/runtime/container tags)

### 🧭 KFM-specific info that helps a lot
- Dataset IDs (e.g., `kfm.ks.<domain>.<layer>.<time>.vN`)
- STAC path(s): `data/stac/.../collection.json` or item IDs
- DCAT entry path(s): `data/catalog/dcat/...`
- PROV run record ID/path: `data/prov/...` *(or `data/provenance/...` if that’s your repo’s canonical folder)*
- Whether the issue leaks **exact coordinates** vs redacted/generalized outputs

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

KFM-specific context (if relevant):
- Dataset ID(s):
- STAC/DCAT paths or IDs:
- PROV run record:
- Does it expose sensitive coordinates? (Y/N)

Suggested fix (optional):

Notes:
- Auth required? Y/N
- User interaction required? Y/N
- Network: public/private/internal-only
- Data exposure: metadata/PII/secrets/infra access
```

---

## 🗺️ Dataset / sensitive data takedown requests

Not every urgent issue is a “software vuln.” Sometimes the risk is:
- license/attribution problems
- accidental publication of sensitive coordinates
- inclusion of culturally sensitive data without approval
- misclassified artifacts (public when they should be restricted)

**How to request a takedown / restriction change**
- Preferred: private vulnerability report (Security tab) labeled **“DATA TAKEDOWN / SENSITIVE DATA”**
- Include:
  - dataset ID(s)
  - where it’s published (STAC/DCAT links)
  - why it must be restricted/removed
  - requested remediation (remove, redact, generalize, move to private)

> [!IMPORTANT]
> We treat sensitive-location mistakes as **security incidents** (containment + remediation), not “content disagreements.”

---

## 🗞️ Advisories & notifications

We use GitHub security tooling when available:
- 🧾 **GitHub Security Advisories** for private triage + coordinated disclosure
- 📦 **Tagged releases** for patched versions (when applicable)

How to stay informed:
- ⭐ Watch this repo for **Releases**
- 🔔 Subscribe to advisories when published

> [!NOTE]
> We avoid publishing exploit details before a fix is available (unless otherwise agreed).

---

## ⏱️ Coordinated disclosure

We follow coordinated disclosure:

- 📩 **Acknowledgement**: confirm receipt promptly  
- 🔎 **Triage & validation**: reproduce + assess  
- 🛠️ **Fix & test**: patch + regression coverage  
- 📣 **Release & advisory**: disclose with mitigations

### ⏳ Target response timelines (guidance)

| Stage | Target |
|---|---|
| Initial acknowledgement | **≤ 2 business days** |
| Triage started | **≤ 7 days** |
| Fix ETA communicated | **after validation** |
| Patch release (Critical/High) | **as fast as feasible** |
| Patch release (Medium/Low) | **scheduled / best effort** |

### 🏷️ Severity rubric (quick)

| Severity | Examples |
|---|---|
| **Critical** | RCE, auth bypass, secrets exfiltration, full DB compromise |
| **High** | privilege escalation, SSRF into internal services, major sensitive data exposure |
| **Medium** | stored XSS with meaningful impact, IDOR with limited scope |
| **Low** | minor info leaks, non-exploitable misconfigurations |

> [!TIP]
> If you have a CVSS vector/score (v3.1 or v4.0), include it (optional). We’ll still apply our own assessment.

---

## 🧭 Safe harbor

We support good‑faith security research that is:
- ✅ Non-destructive
- ✅ Minimal necessary testing
- ✅ Avoids privacy violations and data exfiltration
- ✅ Reported privately with reasonable detail

**Please do not:**
- ❌ Disrupt service (DoS / load testing) without explicit permission
- ❌ Access or modify data that isn’t yours
- ❌ Attempt social engineering (phishing, impersonation)
- ❌ Publish details before a patch is available (unless otherwise agreed)

> [!IMPORTANT]
> If you follow this policy in good faith, we consider your actions authorized and we will not pursue legal action against you for accidental, good‑faith violations. If unsure, **stop and report privately**.

---

## 🚫 Out of scope

- Issues requiring **physical access** to devices
- **Denial of Service** via high-traffic/brute-force load testing
- Vulnerabilities **only in upstream providers** (report upstream), unless KFM configuration makes them exploitable
- Automated scanner output **without** actionable context or plausible impact

Usually out of scope unless chained:
- Missing headers without exploitability
- Clickjacking on non-sensitive pages
- Open redirects with no meaningful impact
- Self-XSS without a privilege chain

---

## 🧰 Secure development guidelines

Security is a design constraint, not a patch.

### 🔑 Secrets & credentials
- Never commit secrets (`.env`, keys, tokens, credentials)
- Use `.env` locally + `.gitignore`
- Prefer secret stores in production (GitHub Secrets/Environments, vaults, cloud secret managers)
- Rotate anything potentially exposed
- Treat logs as sensitive; avoid printing tokens/PII

### 🧾 Data supply-chain security (STAC/DCAT/PROV as a control)
KFM treats **metadata + provenance** as security-critical:
- Provenance deters tampering and supports incident forensics
- Catalog validation prevents accidental publication of restricted data
- Checksums/versioning support reproducibility and rollback

**Before publishing any dataset or derived artifact:**
- STAC entry (when applicable)
- DCAT entry (when applicable)
- PROV lineage record (per run)
- (Recommended) checksums for large assets

> [!IMPORTANT]
> Any **derived/AI-generated** dataset is a first-class artifact with full provenance.

### 🛰️ Remote sensing integrations (Earth Engine-style, archives, portals)
- Restrict API keys/service accounts by least privilege
- Separate “build” vs “publish” permissions
- Keep provider identifiers in provenance (script IDs, date ranges, reducers)
- Validate external inputs (bounds, schema, CRS, expected ranges)
- Avoid embedding long-lived credentials in notebooks or exports

### 🌐 Web/UI security (including WebGL & 3D)
- Validate inputs on **server** (client validation is UX, not security)
- Encode outputs; avoid unsafe HTML injection
- Use secure cookies, CSRF protections where relevant, and a strict CSP
- Treat 3D assets (glTF/3D Tiles/etc.) as untrusted input
- Keep CORS least-privilege (avoid `*` with credentials)

### 🗄️ Database security (PostgreSQL/PostGIS)
- Separate read/write roles (and separate migration role if possible)
- Use parameterized queries everywhere (no string-built SQL)
- Encrypt backups; restrict access and audit restore paths
- Validate geometry (types, SRID, bounds) before insert
- Rate-limit expensive geospatial queries and exports

### ⚙️ Pipeline & worker safety (race conditions + resource safety)
- Make pipeline runs idempotent; avoid partial publishes
- Run decoders/parsers with guardrails (size limits, timeouts)
- Treat ZIPs, PDFs, images, and large geometries as hostile until validated
- Prefer atomic writes + staging directories + final “commit” step

### 🧠 ML/analytics integrity & safety
- Track dataset provenance, versions, checksums (poisoning defense)
- Separate train/eval/test; avoid leakage in artifacts
- Report uncertainty and limitations (don’t ship “false certainty”)
- Store model cards/experiment logs for any published ML output
- Be mindful of model inversion/membership inference for exposed models

### ♻️ Dependency & CI supply-chain hygiene
- Use lockfiles (`package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`, etc.)
- Keep dependencies updated; avoid abandoned packages
- Pin base images; rebuild regularly
- Pin GitHub Actions by commit SHA when feasible
- Consider SBOM generation for releases (recommended)

### 🐳 Container & runtime hardening
- Run as non-root where possible
- Minimize image size (multi-stage builds)
- Don’t bake secrets into images
- Use read-only filesystems where feasible
- Treat CI runners as sensitive infrastructure

---

## 🧪 Security gates in CI

Security must be repeatable and boring.

### ✅ Code security (baseline)
- CodeQL scanning
- Dependency Review (for PRs)
- Secret scanning + push protection
- Lint/typecheck/tests as required checks
- Container scanning (recommended)

### 🗂️ Catalog/data integrity checks (geo-specific)
- STAC/DCAT quick gate (required fields, license/providers/extensions)
- Link-check critical `links[].href` in root/collections
- CRS + bounds validation (Kansas bounds where applicable)
- Provenance presence (PROV required before publish)
- “Classification propagation” checks (prevent public publish of restricted inputs)

> [!TIP]
> Gate “production catalog publish” on **Stable** STAC extensions; warn on Pilot/Proposal until reviewed.

<!-- ingestion/governance sources (hidden):  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS) -->

---

## ✅ PR security checklist

Copy into PRs when relevant:

- [ ] No secrets committed (keys, tokens, `.env`, credentials)
- [ ] Inputs validated + outputs encoded (XSS/Injection resistant)
- [ ] AuthZ checks added/verified for new data access paths
- [ ] Dependencies updated/locked; no suspicious packages
- [ ] New endpoints covered by tests (including negative/security cases)
- [ ] Logging avoids sensitive data (PII, keys, tokens)
- [ ] Container/runtime changes follow least privilege
- [ ] Data changes include provenance + catalog updates (STAC/DCAT/PROV)
- [ ] Docs updated if security posture/config changes

---

## 🗂️ Recommended repo security files

<details>
<summary><strong>📁 Suggested layout (v13-friendly)</strong></summary>

```text
📦 .github/
 ├─ 🛡️ SECURITY.md                # (optional mirror) policy copy
 ├─ 🧾 dependabot.yml
 ├─ 🧑‍⚖️ CODEOWNERS
 ├─ 🧪 workflows/
 │   ├─ 🔍 codeql.yml
 │   ├─ 🧾 dependency-review.yml
 │   ├─ 🔐 secret-scanning.yml     # docs + settings + optional checks
 │   ├─ 🧷 scorecard.yml           # OpenSSF (optional)
 │   └─ 🧪 ci.yml

📦 docs/
 ├─ 🔐 security/
 │   ├─ 🔑 pgp-public-key.asc
 │   ├─ 🧾 threat-model.md
 │   ├─ 📋 security-testing.md
 │   └─ 🧪 incident-response.md
 ├─ ❤️ governance/
 │   ├─ 🧭 data-classification.md
 │   ├─ 🧾 sensitive-location-policy.md
 │   └─ ✅ review-gates.md

📦 tools/
 └─ ✅ validation/
     └─ catalog_qa/                # STAC/DCAT link + field gate

📦 data/
 ├─ 🗂️ stac/
 ├─ 📚 catalog/
 │   └─ dcat/
 └─ 🧾 prov/                       # provenance records (PROV)
```
</details>

---

## 📚 Project reference library

> [!NOTE]
> These references inform KFM’s defensive posture (threat modeling, data governance, integrity, validation, and secure implementation).  
> They are **not** a request for offensive tooling contributions.

<details>
<summary><strong>🏗️ KFM architecture, invariants, governance</strong></summary>

- `docs/specs/Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx` <!--  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS) -->
- `docs/specs/MARKDOWN_GUIDE_v13.md.gdoc` <!--  [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) -->
- *(Design audit + collaboration rules live alongside the above in `docs/specs/` and `/.github/`)*

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
- `docs/library/compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` <!--  [oai_citation:9‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi) -->

</details>

<details>
<summary><strong>🌎 GIS, mapping & geoprocessing</strong></summary>

- `docs/library/python-geospatial-analysis-cookbook.pdf`
- `docs/library/making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `docs/library/Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` <!--  [oai_citation:10‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj) -->

</details>

<details>
<summary><strong>🛰️ Remote sensing & Earth Engine workflows</strong></summary>

- `docs/library/Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` <!--  [oai_citation:11‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-JVv3nbvtonX1HcpeERi9kV) -->

</details>

<details>
<summary><strong>📊 Statistics, experiments & scientific computing integrity</strong></summary>

- `docs/library/Understanding Statistics & Experimental Design.pdf`
- `docs/library/regression-analysis-with-python.pdf`
- `docs/library/Regression analysis using Python - slides-linear-regression.pdf` <!--  [oai_citation:12‡Regression analysis using Python - slides-linear-regression.pdf](file-service://file-Ekbky5FwpaPHfZC2ttv6xR) -->
- `docs/library/graphical-data-analysis-with-r.pdf`
- `docs/library/think-bayes-bayesian-statistics-in-python.pdf` <!--  [oai_citation:13‡think-bayes-bayesian-statistics-in-python.pdf](file-service://file-LXwJApPMVhRZgyqLb9eg7c) -->
- `docs/library/Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`

</details>

<details>
<summary><strong>🧪 Optimization, graphs & advanced math (assurance mindset)</strong></summary>

- `docs/library/Generalized Topology Optimization for Structural Design.pdf`
- `docs/library/Spectral Geometry of Graphs.pdf`

</details>

<details>
<summary><strong>❤️ Ethics, autonomy & accountability</strong></summary>

- `docs/library/Introduction to Digital Humanism.pdf`
- `docs/library/Principles of Biological Autonomy - book_9780262381833.pdf`
- `docs/library/On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` <!--  [oai_citation:14‡On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf](file-service://file-NtashtRjti9J1THyYXkhAv) -->

</details>

<details>
<summary><strong>🧰 Systems & concurrency</strong></summary>

- `docs/library/concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` <!--  [oai_citation:15‡concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf](file-service://file-Y45SvXbmLoZL1MNmrcyqz6) -->

</details>

<details>
<summary><strong>🛡️ Security references (defense only)</strong></summary>

- `docs/library/ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` <!--  [oai_citation:16‡ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf](file-service://file-Q7EeqPb17SD9sV8Fb12LQX) -->
- `docs/library/Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` <!--  [oai_citation:17‡Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf](file-service://file-Mu6zixTqF9Lubf5QMjepRg) -->

> Used to inform defensive controls (threat modeling, incident response, testing strategy).  
> We do **not** accept contributions that add misuse-ready exploit instructions or weaponized tooling.

</details>

<details>
<summary><strong>📚 General programming shelf (bundles)</strong></summary>

- `docs/library/A programming Books.pdf`
- `docs/library/B-C programming Books.pdf`
- `docs/library/D-E programming Books.pdf`
- `docs/library/F-H programming Books.pdf`
- `docs/library/I-L programming Books.pdf`
- `docs/library/M-N programming Books.pdf`
- `docs/library/O-R programming Books.pdf`
- `docs/library/S-T programming Books.pdf`
- `docs/library/U-X programming Books.pdf`

</details>

<!--
Maintainers’ TODOs:
- Replace security@YOUR-DOMAIN.example with a real monitored inbox.
- Add a PGP key at docs/security/pgp-public-key.asc and publish its fingerprint.
- Add incident-response runbook: containment, comms, logging, recovery, postmortem.
- Decide & document data classification rules + propagation enforcement.
- Wire CI gates: CodeQL, dependency review, secret scanning, container scanning, STAC/DCAT/PROV validation.
- Consider OpenSSF Scorecard + SBOM generation for tagged releases.
-->